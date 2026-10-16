"""Print a compact view of a pilot_analyze.py TSV (read-only). Usage: python -B show_table.py <tsv> [cellSuffix]"""
import csv
import sys


def number(value, digits=3, scale=1.0):
    if value in ("", None):
        return "-"
    return f"{float(value) / scale:.{digits}f}"


rows = list(csv.DictReader(open(sys.argv[1], encoding="utf-8"), delimiter="\t"))
if len(sys.argv) > 2:
    rows = [r for r in rows if r["cell"].endswith(sys.argv[2])]
print("world arm      state         audit  E1     E2     CVaR95s  sumC_s   sumV_s  nonNorm forced late "
      "gMulti vMultiR vMultiG divU  wall_s  nnDec  fRider maxC1_s X>60")
for r in rows:
    print(f"{r['world']:<5} {r['arm']:<8} {r['state'][:13]:<13} {r['audit'][:5]:<5}  "
          f"{number(r['E1ServedShare'])}  {number(r['E2ShareDropVAbove60s'])}  "
          f"{number(r['dropVCvar95Ms'], 1, 1000):>7}  {number(r['sumDropC'], 1, 1000):>7}  "
          f"{number(r['sumDropV'], 1, 1000):>7}  {r['nonNormalCertificates'] or '-':>6} "
          f"{r['forcedBreaches'] or '-':>6} {r['latePickups'] or '-':>4}  "
          f"{number(r['gatedMultiInsertionShare'])}  {number(r['vehicleRawMultiInsertionShare'])}  "
          f"{number(r['vehicleGatedMultiInsertionShare'])}  {r.get('firstDivergenceFromU') or '-':>4}  "
          f"{r.get('wallSeconds') or '-':>5}  {number(r.get('nonNormalDecisionShare'))}  "
          f"{number(r.get('forcedRiderShare'))}  {number(r.get('maxDropCPerRiderMs'), 1, 1000):>6}  "
          f"{number(r.get('shareDropXAbove60s'))}")
