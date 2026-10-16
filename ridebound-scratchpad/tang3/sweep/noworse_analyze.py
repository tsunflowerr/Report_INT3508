"""No-worse runs (SWEEP-AMENDMENTS.md A1): the sweep's metrics for every run_noworse.py job, compared with the
same arm/world/cell of the (a) sweep, plus the control check (read-only; outputs with mode "x").

Reuses sweep_analyze.job_row (verified tools) on the no-worse output root. Adds:
  forced breaches by kind (forcedReference = kept route, forcedNoWorse = changed route), riders with any forced
  breach, and decisions whose certificate has a `forcedNoWorse` witness (a forced vehicle still serving);
  for controls: the ordered fleet actions of every acknowledged decision must equal those of the (a) sweep run
  (pilot_analyze.fleet_decisions), since the WP4 content hash differs and hashes cannot be compared.
Usage: python -B noworse_analyze.py <sweep-jobs.tsv> <out.tsv>
"""
from __future__ import annotations

import base64
import csv
import json
import pathlib
import sys

import run_noworse
import run_sweep
import sweep_analyze
from pilot_analyze import fleet_decisions


def forced_details(transcript: pathlib.Path):
    stages, final = {"forcedReference": 0, "forcedNoWorse": 0}, None
    with open(transcript, encoding="utf-8") as handle:
        for line in handle:
            record = json.loads(line)
            if record["direction"] != "runnerToAdapter":
                continue
            envelope = json.loads(base64.b64decode(record["frameBase64"]))
            kind = envelope.get("messageType")
            if kind == "decision":
                body = (envelope["payload"].get("certificate") or {}).get("body") or {}
                seen = {w.get("stage") for w in body.get("witnesses") or []}
                for stage in stages:
                    stages[stage] += stage in seen
            elif kind == "checkpoint":
                final = envelope["payload"]["content"]["onlineState"]
    breaches = final["incidentLedger"]["breaches"] if final else []
    by_kind = {k: sum(1 for b in breaches if b.get("kind") == k) for k in ("forcedReference", "forcedNoWorse")}
    riders = len({b["requestId"] for b in breaches if b.get("kind") in ("forcedReference", "forcedNoWorse")})
    return stages, by_kind, riders


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    sweep = {(r["arm"], r["world"], r["cell"]): r for r in csv.DictReader(open(sys.argv[1], encoding="utf-8"),
                                                                           delimiter="\t")}
    # Point the verified sweep row builder at the no-worse outputs.
    sweep_analyze.OUT_ROOT = run_noworse.OUT_ROOT
    sweep_analyze.effective = lambda name: name
    sweep_analyze.state_of = run_noworse.state_of
    out = []
    for kind, arm, world, cell in run_noworse.jobs(sys.argv[1]):
        name = f"{arm}-{world}-{cell}"
        row = sweep_analyze.job_row(name, arm, world, cell)
        row = {k: v for k, v in row.items() if not k.startswith("_")}
        row["kind"] = kind
        transcript = run_noworse.OUT_ROOT / name / "transcript-00.ndjson"
        if transcript.exists() and row.get("audit") == "ok":
            stages, by_kind, riders = forced_details(transcript)
            row["decisionsWithKeptRouteWitness"] = stages["forcedReference"]
            row["decisionsWithNoWorseWitness"] = stages["forcedNoWorse"]
            row["breachesForcedReference"] = by_kind["forcedReference"]
            row["breachesForcedNoWorse"] = by_kind["forcedNoWorse"]
            row["ridersWithAnyForcedBreach"] = riders
            base = sweep[(arm, world, cell)]
            row["a_M1_completed"] = base["M1_completed"]
            row["a_M3_shareA_gt_x"] = base.get("M3_shareA_gt_x")
            row["a_M5_meanForcedFleetShare"] = base.get("M5_meanForcedFleetShare")
            row["C_M1_completed"] = sweep[(f"C-{arm.split('-')[1]}", world, cell)]["M1_completed"]
            if kind == "control":
                mine = fleet_decisions(transcript)
                reference = fleet_decisions(
                    run_sweep.OUT_ROOT / run_sweep.effective(name) / "transcript-00.ndjson")
                row["controlSameFleetActions"] = [d for _, d in mine] == [d for _, d in reference]
                row["controlDecisions"] = f"{len(mine)}/{len(reference)}"
        out.append(row)
        print(f"{kind:<9} {name:<38} {row.get('state')} {row.get('audit')} completed={row.get('M1_completed')} "
              f"(a)={row.get('a_M1_completed')} C={row.get('C_M1_completed')} "
              f"noWorseDecisions={row.get('decisionsWithNoWorseWitness')} "
              f"sameAsA={row.get('controlSameFleetActions', '-')}", flush=True)
    columns = sorted({k for r in out for k in r}, key=lambda k: (k not in ("job", "kind", "arm", "world", "cell",
                                                                            "state", "audit"), k))
    with open(sys.argv[2], "x", encoding="utf-8", newline="\n") as handle:
        handle.write("\t".join(columns) + "\n")
        for r in out:
            handle.write("\t".join("" if r.get(c) is None else str(r.get(c)) for c in columns) + "\n")
    print(f"written {sys.argv[2]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
