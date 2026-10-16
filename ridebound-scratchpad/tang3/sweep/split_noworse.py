"""M+(b) (no-worse run where treated, sweep run otherwise) split into real (W5) and synthetic (W1, W2, W4) traffic,
next to C and M+(a); plus a per-cell check that M+(b) A>x equals C's A>x wherever decisions are identical."""
import csv
import pathlib
import statistics
import sys

TANG3 = pathlib.Path(r"E:/Code/Report_INT3508/ridebound-scratchpad/tang3")
sys.path.insert(0, str(TANG3 / "pilot"))
sys.path.insert(0, str(TANG3 / "sweep"))
import run_noworse  # noqa: E402
import run_sweep  # noqa: E402
from pilot_analyze import fleet_decisions  # noqa: E402

sweep = {(r["arm"], r["world"], r["cell"]): r for r in csv.DictReader(open(TANG3 / "sweep/sweep-jobs-2026-09-26.tsv", encoding="utf-8"), delimiter="\t")}
nw = {(r["arm"], r["world"], r["cell"]): r for r in csv.DictReader(open(TANG3 / "sweep/noworse-jobs-2026-09-26.tsv", encoding="utf-8"), delimiter="\t") if r["kind"] == "treatment"}
cells = sorted({k[2] for k in sweep})
v = lambda r, k: float(r[k] or 0)  # noqa: E731
for name, worlds in (("real", ("W5",)), ("synth", ("W1", "W2", "W4"))):
    print("==", name)
    for x in (30, 60, 120, 300, 600, 900):
        keys = [(w, c) for w in worlds for c in cells]
        c_rows = [sweep[(f"C-{x}", w, c)] for w, c in keys]
        a_rows = [sweep[(f"Mplus-{x}", w, c)] for w, c in keys]
        b_rows = [nw.get((f"Mplus-{x}", w, c), sweep[(f"Mplus-{x}", w, c)]) for w, c in keys]
        same, mismatch = 0, []
        for (w, c), b, cr in zip(keys, b_rows, c_rows):
            treated = (f"Mplus-{x}", w, c) in nw
            b_path = (run_noworse.OUT_ROOT / f"Mplus-{x}-{w}-{c}") if treated else (run_sweep.OUT_ROOT / run_sweep.effective(f"Mplus-{x}-{w}-{c}"))
            mine = [d for _, d in fleet_decisions(b_path / "transcript-00.ndjson")]
            theirs = [d for _, d in fleet_decisions(run_sweep.OUT_ROOT / run_sweep.effective(f"C-{x}-{w}-{c}") / "transcript-00.ndjson")]
            if mine == theirs:
                same += 1
                if v(b, "M3_shareA_gt_x") != v(cr, "M3_shareA_gt_x"):
                    mismatch.append((w, c))
        print(f"  {x:>4}s served C/a/b {sum(v(r,'M1_completed') for r in c_rows):.0f}/{sum(v(r,'M1_completed') for r in a_rows):.0f}/"
              f"{sum(v(r,'M1_completed') for r in b_rows):.0f}  sameAsC {same}/{len(keys)}  "
              f"b broken {statistics.mean(v(r,'M3_shareA_gt_x') for r in b_rows):.3f}  "
              f"b forced {statistics.mean(v(r,'M5_nonNormalShare') for r in b_rows):.3f}  "
              f"b frozen {statistics.mean(v(r,'M5_meanForcedFleetShare') for r in b_rows):.3f}  "
              f"C byM+ {statistics.mean(v(r,'M3_shareA_gt_x') for r in c_rows):.3f}  identical-but-A-differs {mismatch}", flush=True)
