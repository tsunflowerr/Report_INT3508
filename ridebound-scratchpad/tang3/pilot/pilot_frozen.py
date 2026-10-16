"""T3.7 recovery burden by vehicle ("frozen vehicles", ADR-075 open question), read-only on the pilot outputs.

A vehicle is FORCED in a decision when the decision's certificate has a `forcedReference` witness for it; under
ADR-075 its only option is then the kept route (forced no-op), so it cannot take a new rider in that decision.
Per job (acknowledged decisions only; fleet size = number of vehicleLosses rows):
  meanForcedFleetShare          mean over decisions of forced vehicles / fleet size
  pendingDecisions              decisions with a pending request
  pendingAnyForcedShare         share of those with >= 1 forced vehicle
  pendingHalfForcedShare        share of those with >= half the fleet forced
  pendingAllForcedShare         share of those with EVERY vehicle forced (nobody can serve the pending rider)
Usage: python -B pilot_frozen.py <output.tsv>   (created with mode "x")
"""
from __future__ import annotations

import base64
import json
import sys

from run_pilot import ARMS, CELLS, OUT_ROOT, WORLD_IDS


def measure(transcript):
    sent, acknowledged = {}, set()
    with open(transcript, encoding="utf-8") as handle:
        for line in handle:
            record = json.loads(line)
            envelope = json.loads(base64.b64decode(record["frameBase64"]))
            kind = envelope.get("messageType")
            if record["direction"] == "runnerToAdapter" and kind == "decision":
                sent.setdefault(envelope["payload"]["decisionHash"], envelope["payload"])
            elif record["direction"] == "adapterToRunner" and kind == "decisionApplied":
                acknowledged.add(envelope["payload"]["decisionHash"])
    decisions = shares = pending = any_forced = half_forced = all_forced = 0
    fleet_sizes = set()
    for key, payload in sent.items():
        if key not in acknowledged:
            continue
        evidence = (payload.get("solver") or {}).get("executionEvidence")
        if not evidence:
            continue
        fleet = len(evidence["generation"]["vehicleLosses"])
        fleet_sizes.add(fleet)
        body = (payload.get("certificate") or {}).get("body") or {}
        forced = {w["vehicleId"] for w in body.get("witnesses") or [] if w.get("stage") == "forcedReference"}
        decisions += 1
        shares += len(forced) / fleet if fleet else 0
        if evidence["generation"]["totalPendingRequestCount"] > 0:
            pending += 1
            any_forced += bool(forced)
            half_forced += fleet > 0 and 2 * len(forced) >= fleet
            all_forced += fleet > 0 and len(forced) == fleet
    ratio = (lambda n, d: n / d if d else None)
    return {
        "decisions": decisions, "fleetSizes": ",".join(map(str, sorted(fleet_sizes))),
        "meanForcedFleetShare": ratio(shares, decisions), "pendingDecisions": pending,
        "pendingAnyForcedShare": ratio(any_forced, pending), "pendingHalfForcedShare": ratio(half_forced, pending),
        "pendingAllForcedShare": ratio(all_forced, pending),
    }


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    columns = ["job", "arm", "world", "cell", "decisions", "fleetSizes", "meanForcedFleetShare", "pendingDecisions",
               "pendingAnyForcedShare", "pendingHalfForcedShare", "pendingAllForcedShare"]
    with open(sys.argv[1], "x", encoding="utf-8", newline="\n") as out:
        out.write("\t".join(columns) + "\n")
        for cell in CELLS:
            for world in WORLD_IDS:
                for arm in ARMS:
                    if arm == "U":
                        continue
                    name = f"{arm}-{world}-{cell}"
                    row = {"job": name, "arm": arm, "world": world, "cell": cell,
                           **measure(OUT_ROOT / name / "transcript-00.ndjson")}
                    out.write("\t".join("" if row[c] is None else str(row[c]) for c in columns) + "\n")
                    out.flush()
                    print(f"{name:<34} meanForced={row['meanForcedFleetShare'] or 0:.3f} "
                          f"pendingAll={row['pendingAllForcedShare'] or 0:.3f} "
                          f"pendingHalf={row['pendingHalfForcedShare'] or 0:.3f}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
