"""Task A, descriptive additions written AFTER the full analysis was read (2026-09-29); not sealed predictions.

Per (world, cell), for C-30 (sweep) and V-30 / M-30 under recovery (a) and (b):
  sameFleetAsC   ordered fleet actions of acknowledged decisions equal those of C-30 (pilot_analyze.fleet_decisions)
  V>30           share of promised riders whose drop V (sum |z| over drop revisions) exceeds 30 s: V-30's own promise
  |A|>30         share of completed riders with |actual drop - first promised drop| > 30 s: M-30's own promise
  C>30           share of promised riders with sum |c| > 30 s: C-30's own promise
  forcedRiders   riders with a forced breach / promised riders (M5_forcedRiderShare); frozen fleet (mean forced share)
Every rule is scored by every promise, as in the sweep. Reads the jobs TSV of vm_analyze.py for the M5 columns.
Usage: python -B vm_describe.py <jobs.tsv> <new-log>   (mode "x")
"""
from __future__ import annotations

import csv
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
TANG3 = HERE.parent
for sub in ("sweep", "pilot", "evidence"):
    sys.path.insert(0, str(TANG3 / sub))

import audit_vep  # noqa: E402
import run_sweep  # noqa: E402
import run_vm  # noqa: E402
from pilot_analyze import fleet_decisions  # noqa: E402
from sweep_analyze import event_times, rider_values  # noqa: E402


def rider_metrics(transcript: pathlib.Path):
    table, summary = audit_vep.audit(transcript)
    first, c = rider_values(table)
    v = {}
    for request, coordinate, _, kind, _, _, _, _, _, _, z, closed in table:
        if coordinate == "drop":
            v.setdefault(request, 0)
            if kind != "initialPromise" and not closed:
                v[request] += abs(z)
    if sum(v.values()) != summary["sumDropV"] or sum(c.values()) != summary["sumDropC"]:
        raise SystemExit(f"{transcript}: per-rider sums do not match the oracle")
    _, alighted = event_times(transcript)
    a = [alighted[r] - first[r] for r in first if r in alighted]
    share = lambda values, limit: sum(1 for x in values if x > limit) / len(values) if values else None  # noqa: E731
    return {"V>30": share(list(v.values()), 30000), "|A|>30": share([abs(x) for x in a], 30000),
            "C>30": share(list(c.values()), 30000)}


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    rows = {(r["variant"], r["arm"], r["world"], r["cell"]): r
            for r in csv.DictReader(open(sys.argv[1], encoding="utf-8"), delimiter="\t")}
    lines = [f"# vm_describe.py (descriptive, after the full analysis); jobs table {sys.argv[1]}",
             "world cell arm variant | served | sameFleetAsC | V>30 | |A|>30 | C>30 | forcedRiders | frozenFleet"]
    for world in run_vm.WORLD_IDS:
        for cell in run_vm.CELLS:
            c_path = run_sweep.OUT_ROOT / run_sweep.effective(f"C-30-{world}-{cell}") / "transcript-00.ndjson"
            c_fleet = [d for _, d in fleet_decisions(c_path)]
            entries = [("C-30", "sweep", c_path)] + [
                (arm, v, run_vm.VARIANTS[v]["out"] / f"{arm}-{world}-{cell}" / "transcript-00.ndjson")
                for arm in run_vm.ARMS for v in ("a", "b")]
            for arm, variant, path in entries:
                row = rows[(variant, arm, world, cell)]
                m = rider_metrics(path)
                same = [d for _, d in fleet_decisions(path)] == c_fleet
                fmt = lambda x: "-" if x in (None, "") else f"{float(x):.3f}"  # noqa: E731
                lines.append(f"{world} {cell[-3:]} {arm:<4} {variant:<5} | {row['M1_completed']:>3} | {str(same):<5} | "
                             f"{fmt(m['V>30'])} | {fmt(m['|A|>30'])} | {fmt(m['C>30'])} | "
                             f"{fmt(row.get('M5_forcedRiderShare'))} | {fmt(row.get('M5_meanForcedFleetShare'))}")
    text = "\n".join(lines) + "\n"
    with open(sys.argv[2], "x", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
