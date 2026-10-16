"""M⁺ under no-worse recovery (b), aggregated per level over the 8 drift cells, next to C and M⁺ (a) (read-only).

For each (x, drift cell): M⁺(b) is the run_noworse.py run when M⁺-x had forced breaches in the sweep, and the sweep
run otherwise; the 6 controls showed that no-worse recovery changes nothing without a forced vehicle (fleet actions
identical, 6/6). Columns as in sweep_aggregate.py, plus the number of cells where M⁺(b) makes exactly C's decisions.
Usage: python -B noworse_aggregate.py <sweep-jobs.tsv> <noworse-jobs.tsv>
"""
import csv
import statistics
import sys

sys.path.insert(0, r"E:/Code/Report_INT3508/ridebound-scratchpad/tang3/pilot")
import run_noworse  # noqa: E402
import run_sweep  # noqa: E402
from pilot_analyze import fleet_decisions  # noqa: E402

sweep = {(r["arm"], r["world"], r["cell"]): r for r in csv.DictReader(open(sys.argv[1], encoding="utf-8"), delimiter="\t")}
nw = {(r["arm"], r["world"], r["cell"]): r for r in csv.DictReader(open(sys.argv[2], encoding="utf-8"), delimiter="\t")
      if r["kind"] == "treatment"}
cells = sorted({k[2] for k in sweep})
drift = [(w, c) for w in ("W1", "W2", "W4", "W5") for c in cells]
v = lambda r, k: float(r[k] or 0)  # noqa: E731
print("   x  | completed C  M+(a) M+(b) | M+(b) same decisions as C | M+(b) own break | M+(b) forced | M+(b) frozen")
for x in (30, 60, 120, 300, 600, 900):
    c_rows = [sweep[(f"C-{x}", w, c)] for w, c in drift]
    a_rows = [sweep[(f"Mplus-{x}", w, c)] for w, c in drift]
    b_rows = [nw.get((f"Mplus-{x}", w, c), sweep[(f"Mplus-{x}", w, c)]) for w, c in drift]
    same = 0
    for (w, c) in drift:
        b_path = (run_noworse.OUT_ROOT if (f"Mplus-{x}", w, c) in nw else run_sweep.OUT_ROOT)
        b_name = f"Mplus-{x}-{w}-{c}" if (f"Mplus-{x}", w, c) in nw else run_sweep.effective(f"Mplus-{x}-{w}-{c}")
        mine = fleet_decisions(b_path / b_name / "transcript-00.ndjson")
        theirs = fleet_decisions(run_sweep.OUT_ROOT / run_sweep.effective(f"C-{x}-{w}-{c}") / "transcript-00.ndjson")
        same += [d for _, d in mine] == [d for _, d in theirs]
    print(f"  {x:>4} | {sum(v(r, 'M1_completed') for r in c_rows):>11.0f} {sum(v(r, 'M1_completed') for r in a_rows):>5.0f} "
          f"{sum(v(r, 'M1_completed') for r in b_rows):>5.0f} | {same:>2}/8 | "
          f"{statistics.mean(v(r, 'M3_shareA_gt_x') for r in b_rows):.3f} | "
          f"{statistics.mean(v(r, 'M5_nonNormalShare') for r in b_rows):.3f} | "
          f"{statistics.mean(v(r, 'M5_meanForcedFleetShare') for r in b_rows):.3f}", flush=True)
