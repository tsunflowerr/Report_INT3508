"""Sweep results per traffic world (2 cells each, 216 requests): served U, C, M+(a), M+(b); M+ promise-break share
(a and b), C promise-break share, M+ forced-decision share (a and b). M+(b) = no-worse run where treated, else sweep.
Read-only on the two job tables."""
import csv
import pathlib
import statistics

TANG3 = pathlib.Path(r"E:/Code/Report_INT3508/ridebound-scratchpad/tang3")
sweep = {(r["arm"], r["world"], r["cell"]): r for r in csv.DictReader(open(TANG3 / "sweep/sweep-jobs-2026-09-26.tsv", encoding="utf-8"), delimiter="\t")}
nw = {(r["arm"], r["world"], r["cell"]): r for r in csv.DictReader(open(TANG3 / "sweep/noworse-jobs-2026-09-26.tsv", encoding="utf-8"), delimiter="\t") if r["kind"] == "treatment"}
cells = sorted({k[2] for k in sweep})
v = lambda r, k: float(r[k] or 0)  # noqa: E731
for w in ("W0", "W1", "W2", "W3", "W4", "W5"):
    u = sum(v(sweep[("U", w, c)], "M1_completed") for c in cells)
    req = sum(v(sweep[("U", w, c)], "requests") for c in cells)
    print(f"== {w}  U served {u:.0f}/{req:.0f}")
    for x in (30, 60, 120, 300, 600, 900):
        C = [sweep[(f"C-{x}", w, c)] for c in cells]
        A = [sweep[(f"Mplus-{x}", w, c)] for c in cells]
        B = [nw.get((f"Mplus-{x}", w, c), sweep[(f"Mplus-{x}", w, c)]) for c in cells]
        s = lambda rows, k: sum(v(r, k) for r in rows)  # noqa: E731
        m = lambda rows, k: statistics.mean(v(r, k) for r in rows)  # noqa: E731
        print(f"  {x:>4}s served C/a/b {s(C,'M1_completed'):.0f}/{s(A,'M1_completed'):.0f}/{s(B,'M1_completed'):.0f}"
              f"  Cbroken {m(C,'M4_shareC_gt_x'):.3f}  M+broken a/b {m(A,'M3_shareA_gt_x'):.3f}/{m(B,'M3_shareA_gt_x'):.3f}"
              f"  CbyM+ {m(C,'M3_shareA_gt_x'):.3f}  M+forced a/b {m(A,'M5_nonNormalShare'):.3f}/{m(B,'M5_nonNormalShare'):.3f}"
              f"  E2 C/a {m(C,'M2_E2'):.3f}/{m(A,'M2_E2'):.3f}")
