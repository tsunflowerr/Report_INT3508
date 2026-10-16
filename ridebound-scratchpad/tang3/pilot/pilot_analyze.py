"""T3.7 pilot table, in the check order of §17.2 (read-only on the pilot outputs).

Per job: status -> audit validity (audit_vep cross-checks) -> raw/gated choice opportunity
(choice_metrics) -> first decision that differs from arm U in the same world and cell -> service and
risk (E1, E2, CVaR95 of drop V, sum C/X/V) -> recovery (non-normal certificates, forced breaches) and
late boardings -> cost (wall seconds from summary.json).

Decision comparison: the actions of each acknowledged decision, reduced to what the fleet does
(accept/reject/defer a request, the vehicle plan), are compared in order with U's. The first
differing index and its simTimeMs are reported; after it the runs see different inputs.

Per-rider columns (added 2026-09-25, after the interim table): maxDropCPerRiderMs (largest accumulated
decision-induced drop change of one rider; the C-family cap applies to it) and shareDropXAbove60s (riders whose
traffic-induced drop change exceeds 60 s). Their row sums are cross-checked against the oracle totals.

Usage: python -B pilot_analyze.py <output.tsv>   (created with mode "x")
"""
from __future__ import annotations

import base64
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "evidence"))

import audit_vep  # noqa: E402
import choice_metrics  # noqa: E402
from run_pilot import ARMS, CELLS, OUT_ROOT, WORLD_IDS, state_of  # noqa: E402

FLEET_ACTIONS = {"requestAccepted", "requestRejected", "requestDeferred", "vehiclePlanUpdated"}


def fleet_decisions(transcript: pathlib.Path):
    """[(simTimeMs, digest of the fleet actions)] of acknowledged decisions, in order."""
    sent, order, acknowledged = {}, [], set()
    for line in transcript.read_text(encoding="utf-8").splitlines():
        record = json.loads(line)
        envelope = json.loads(base64.b64decode(record["frameBase64"]))
        kind = envelope.get("messageType")
        if record["direction"] == "runnerToAdapter" and kind == "decision":
            payload = envelope["payload"]
            if payload["decisionHash"] not in sent:
                order.append(payload["decisionHash"])
            actions = sorted(
                json.dumps(action, sort_keys=True) for action in payload.get("actions", [])
                if action.get("decisionType") in FLEET_ACTIONS)
            sent[payload["decisionHash"]] = (
                envelope.get("simTimeMs"), hashlib.sha256("\n".join(actions).encode()).hexdigest())
        elif record["direction"] == "adapterToRunner" and kind == "decisionApplied":
            acknowledged.add(envelope["payload"]["decisionHash"])
    return [sent[key] for key in order if key in acknowledged]


def first_divergence(mine, reference):
    for index, (a, b) in enumerate(zip(mine, reference)):
        if a[1] != b[1]:
            return index, a[0]
    if len(mine) != len(reference):
        index = min(len(mine), len(reference))
        return index, (mine[index][0] if index < len(mine) else None)
    return None, None


def row(name, arm, world, cell, reference):
    state = state_of(name)
    out = {"job": name, "arm": arm, "world": world, "cell": cell, "state": state}
    output = OUT_ROOT / name
    transcript = output / "transcript-00.ndjson"
    if not transcript.exists():
        return out
    summary_file = output / "summary.json"
    if summary_file.exists():
        runs = json.loads(summary_file.read_text(encoding="utf-8")).get("runs") or [{}]
        out["wallSeconds"] = round(runs[0].get("resources", {}).get("wallMilliseconds", 0) / 1000)
    try:
        table, summary = audit_vep.audit(transcript)
        out["audit"] = "ok" if summary.get("finalCheckpoint") else "no-final-checkpoint"
        if table is not None:
            # Per-rider drop C and X from the signed rows; the C sum must equal the oracle's sumDropC.
            rider_c, rider_x = {}, {}
            for request, coordinate, _, kind, _, _, _, _, x, c, _, closed in table:
                if coordinate == "drop" and kind != "initialPromise" and not closed:
                    rider_c[request] = rider_c.get(request, 0) + abs(c)
                    rider_x[request] = rider_x.get(request, 0) + abs(x)
            if sum(rider_c.values()) != summary["sumDropC"] or sum(rider_x.values()) != summary["sumDropX"]:
                out["audit"] = "ROW-ORACLE-MISMATCH"
            out["maxDropCPerRiderMs"] = max(rider_c.values(), default=0)
            if summary.get("promisedRiders"):
                out["shareDropXAbove60s"] = (
                    sum(1 for value in rider_x.values() if value > audit_vep.E2_THRESHOLD_MS)
                    / summary["promisedRiders"])
        out.update({key: summary.get(key) for key in (
            "E1ServedShare", "E2ShareDropVAbove60s", "dropVCvar95Ms", "sumDropC", "sumDropX",
            "sumDropV", "nonNormalCertificates", "latePickups", "latePickupMaxMs",
            "decisionsAcknowledged", "promisedRiders", "ridersWithForcedBreach")})
        out["forcedBreaches"] = (summary.get("breaches") or {}).get("forcedReference", 0)
        if summary.get("decisionsAcknowledged"):
            out["nonNormalDecisionShare"] = (
                summary["nonNormalCertificates"] / summary["decisionsAcknowledged"])
        if summary.get("promisedRiders"):
            out["forcedRiderShare"] = summary["ridersWithForcedBreach"] / summary["promisedRiders"]
    except audit_vep.EvidenceError as error:
        out["audit"] = f"EVIDENCE-ERROR: {error}"
    choice = choice_metrics.measure(transcript)
    out.update({key: choice[key] for key in (
        "decisionsWithPending", "rawMultiInsertionShare", "gatedMultiInsertionShare",
        "vehicleRawMultiInsertionShare", "vehicleGatedMultiInsertionShare")})
    out["gatePrunes"] = sum(choice["gatePrunes"].values())
    if reference is not None and arm != "U":
        index, time_ms = first_divergence(fleet_decisions(transcript), reference)
        out["firstDivergenceFromU"] = index
        out["firstDivergenceMs"] = time_ms
    return out


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    rows = []
    for cell in CELLS:
        for world in WORLD_IDS:
            u_transcript = OUT_ROOT / f"U-{world}-{cell}" / "transcript-00.ndjson"
            reference = fleet_decisions(u_transcript) if u_transcript.exists() else None
            for arm in ARMS:
                rows.append(row(f"{arm}-{world}-{cell}", arm, world, cell, reference))
    columns = sorted({key for r in rows for key in r}, key=lambda k: (k not in (
        "job", "arm", "world", "cell", "state", "audit"), k))
    with open(sys.argv[1], "x", encoding="utf-8", newline="\n") as handle:
        handle.write("\t".join(columns) + "\n")
        for r in rows:
            handle.write("\t".join("" if r.get(c) is None else str(r.get(c)) for c in columns) + "\n")
    print(f"{len(rows)} rows written to {sys.argv[1]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
