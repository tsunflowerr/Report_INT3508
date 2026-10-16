"""Score the sealed predictions D1-D7 of SWEEP-PLAN.md §6 against the final sweep tables (read-only).

Each prediction is evaluated literally as sealed; the wording is repeated here next to its test.
Usage: python -B sweep_predictions.py <sweep-jobs.tsv> <sweep-paired.tsv>
"""
import csv
import sys

jobs = list(csv.DictReader(open(sys.argv[1], encoding="utf-8"), delimiter="\t"))
pairs = list(csv.DictReader(open(sys.argv[2], encoding="utf-8"), delimiter="\t"))
by = {(r["arm"], r["world"], r["cell"]): r for r in jobs}
cells = sorted({r["cell"] for r in jobs})
drift = ["W1", "W2", "W4", "W5"]
levels = [30, 60, 120, 300, 600, 900]
f = lambda r, k: float(r[k]) if r.get(k) not in ("", None) else None  # noqa: E731
results = []

# D1: W0, every x, C-x and M+-x accept exactly the same riders, both cells.
d1 = [p for p in pairs if p["world"] == "W0"]
results.append(("D1", all(p["identicalSets"] == "True" for p in d1),
                f"W0 identical completed sets {sum(p['identicalSets'] == 'True' for p in d1)}/{len(d1)}"))

# D2: x = 900, C-900, M+-900 and U the same riders in every (world, cell).
d2 = [p for p in pairs if p["level"] == "900"]
ok2 = all(p["sameAsU_C"] == "True" and p["sameAsU_Mplus"] == "True" for p in d2)
results.append(("D2", ok2, f"x=900 both equal to U {sum(p['sameAsU_C'] == 'True' and p['sameAsU_Mplus'] == 'True' for p in d2)}/{len(d2)}"))

# D3: C-x 0 non-normal decisions and 0 forced breaches, every x and world.
c_rows = [r for r in jobs if r["family"] == "C"]
ok3 = all(int(r["M5_forcedBreaches"]) == 0 and f(r, "M5_nonNormalShare") == 0 for r in c_rows)
results.append(("D3", ok3, f"C jobs with forced/non-normal: {sum(1 for r in c_rows if int(r['M5_forcedBreaches']) or f(r, 'M5_nonNormalShare'))}/{len(c_rows)}"))

# D4: M+ forced at x = 30 in W1, W2, W4, W5 (both cells); none in W0 and W3 at any x; none anywhere at x >= 600.
m = lambda arm, w, c: int(by[(arm, w, c)]["M5_forcedBreaches"])  # noqa: E731
at30 = [(w, c, m("Mplus-30", w, c)) for w in drift for c in cells]
none_w0w3 = [(w, c, x, m(f"Mplus-{x}", w, c)) for w in ("W0", "W3") for c in cells for x in levels]
none_high = [(w, c, x, m(f"Mplus-{x}", w, c)) for w in ("W0", "W1", "W2", "W3", "W4", "W5") for c in cells
             for x in (600, 900)]
ok4a = all(v > 0 for _, _, v in at30)
ok4b = all(v == 0 for *_, v in none_w0w3)
ok4c = all(v == 0 for *_, v in none_high)
results.append(("D4", ok4a and ok4b and ok4c,
                f"x=30 forced>0 in {sum(v > 0 for *_, v in at30)}/8 drift cells "
                f"(zero at: {[(w, c[-3:]) for w, c, v in at30 if v == 0]}); W0/W3 zero {ok4b}; x>=600 zero {ok4c}"))

# D5: at x = 30, completed C-30 >= M+-30 in >= 6/8 of W1, W2, W4, W5 cells.
d5 = [(w, c, int(by[("C-30", w, c)]["M1_completed"]), int(by[("Mplus-30", w, c)]["M1_completed"]))
      for w in drift for c in cells]
n5 = sum(1 for *_, a, b in d5 if a >= b)
results.append(("D5", n5 >= 6, f"C-30 >= M+-30 in {n5}/8: " + ", ".join(f"{w}{c[-3:]} {a}/{b}" for w, c, a, b in d5)))

# D6: W3, M+-x completed >= C-x at every x, both cells.
d6 = [(c, x, int(by[(f"C-{x}", "W3", c)]["M1_completed"]), int(by[(f"Mplus-{x}", "W3", c)]["M1_completed"]))
      for c in cells for x in levels]
results.append(("D6", all(b >= a for *_, a, b in d6), f"W3 M+ >= C in {sum(b >= a for *_, a, b in d6)}/{len(d6)}"))

# D7: for x <= 120 in W1, W2, W4, W5: share A > x of M+-x is > 0, and <= that of C-x in >= 6/8 cells, per x.
parts, ok7 = [], True
for x in (30, 60, 120):
    rows = [(w, c, f(by[(f"Mplus-{x}", w, c)], "M3_shareA_gt_x"), f(by[(f"C-{x}", w, c)], "M3_shareA_gt_x"))
            for w in drift for c in cells]
    positive = sum(1 for *_, mp, _ in rows if mp > 0)
    le = sum(1 for *_, mp, cc in rows if mp <= cc)
    ok7 &= positive == 8 and le >= 6
    parts.append(f"x={x}: M+ A>x >0 in {positive}/8, M+ <= C in {le}/8")
results.append(("D7", ok7, "; ".join(parts)))

for name, ok, detail in results:
    print(f"{name} {'HELD' if ok else 'NOT HELD'} — {detail}")
