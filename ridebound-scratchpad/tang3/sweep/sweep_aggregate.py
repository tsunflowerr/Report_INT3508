"""Per level, totals over (world, cell) of the final sweep table (read-only, descriptive; added after sealing).

For each x: completed riders summed over the 8 drift cells (W1, W2, W4, W5) and over all 12 cells, for U, C-x, M+-x;
mean over drift cells of each rule's own-promise break share (C: C_r > x; M+: A > x) and of the other rule's; M+
forced breaches, mean non-normal decision share and mean frozen-fleet share over drift cells; E2 mean.
Usage: python -B sweep_aggregate.py <sweep-jobs.tsv>
"""
import csv
import statistics
import sys

rows = list(csv.DictReader(open(sys.argv[1], encoding="utf-8"), delimiter="\t"))
by = {(r["arm"], r["world"], r["cell"]): r for r in rows}
cells = sorted({r["cell"] for r in rows})
drift = [(w, c) for w in ("W1", "W2", "W4", "W5") for c in cells]
allc = [(w, c) for w in ("W0", "W1", "W2", "W3", "W4", "W5") for c in cells]
v = lambda arm, w, c, k: float(by[(arm, w, c)][k] or 0)  # noqa: E731

u_drift = sum(v("U", w, c, "M1_completed") for w, c in drift)
u_all = sum(v("U", w, c, "M1_completed") for w, c in allc)
print(f"U completed: drift cells {u_drift:.0f}, all cells {u_all:.0f}  (8 x 108 = 864 and 12 x 108 = 1296 requests)")
print("   x  | completed drift C  M+ | all C   M+  | C own break  M+ own break | C by M+ rule  M+ by C rule | "
      "M+ forced  nonNorm frozen | E2 C   M+")
for x in (30, 60, 120, 300, 600, 900):
    c, m = f"C-{x}", f"Mplus-{x}"
    mean = lambda arm, k, cs=drift: statistics.mean(v(arm, w, cc, k) for w, cc in cs)  # noqa: E731
    print(f"  {x:>4} | {sum(v(c, w, cc, 'M1_completed') for w, cc in drift):>6.0f} {sum(v(m, w, cc, 'M1_completed') for w, cc in drift):>4.0f} | "
          f"{sum(v(c, w, cc, 'M1_completed') for w, cc in allc):>5.0f} {sum(v(m, w, cc, 'M1_completed') for w, cc in allc):>4.0f} | "
          f"{mean(c, 'M4_shareC_gt_x'):.3f}        {mean(m, 'M3_shareA_gt_x'):.3f}        | "
          f"{mean(c, 'M3_shareA_gt_x'):.3f}         {mean(m, 'M4_shareC_gt_x'):.3f}        | "
          f"{sum(v(m, w, cc, 'M5_forcedBreaches') for w, cc in drift):>6.0f}  {mean(m, 'M5_nonNormalShare'):.3f}  "
          f"{mean(m, 'M5_meanForcedFleetShare'):.3f} | {mean(c, 'M2_E2'):.3f} {mean(m, 'M2_E2'):.3f}")
