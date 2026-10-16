"""Task B: totals and means over the 8 cells for the thesis, read-only.

Inputs: the jobs table and the report of w07_analyze.py (the report's V-30 own-promise lines). Served = sum over
cells; shares = mean over cells (as the sweep tables). Usage: python -B w07_aggregate.py <jobs.tsv> <report.txt> <new-log>
"""
import csv
import re
import statistics
import sys

V_LINE = re.compile(r"^\s+(?P<cell>d\S+): V>30 V-30 (?P<v>[\d.]+) C-30 (?P<c>[\d.]+) \| V-30 forced (?P<f>[\d.]+) \| same decisions (?P<same>True|False)$")


def main() -> int:
    if len(sys.argv) != 4:
        print(__doc__)
        return 2
    rows = list(csv.DictReader(open(sys.argv[1], encoding="utf-8"), delimiter="\t"))
    by = {(r["arm"], r["cell"]): r for r in rows}
    cells = sorted({r["cell"] for r in rows})
    out = [f"# w07_aggregate.py; inputs {sys.argv[1]} {sys.argv[2]}; cells {len(cells)}, requests {108 * len(cells)}"]
    for arm in ("U", "C-30", "C-60", "C-120", "C-300", "Mplus-30", "Mplus-60", "Mplus-120", "Mplus-300", "V-30", "M-30"):
        rs = [by[(arm, c)] for c in cells]
        mean = lambda key: statistics.mean(float(r[key] or 0) for r in rs)  # noqa: E731
        line = f"{arm:<10} served {sum(int(r['M1_completed']) for r in rs):>4} | forced decisions {mean('M5_nonNormalShare'):.3f}"
        if arm != "U":
            line += f" | A>x {mean('M3_shareA_gt_x'):.3f} | C_r>x {mean('M4_shareC_gt_x'):.3f}"
        out.append(line)
    v = [m for line in open(sys.argv[2], encoding="utf-8") if (m := V_LINE.match(line.rstrip("\n")))]
    if len(v) != len(cells):
        raise SystemExit(f"expected {len(cells)} V-30 lines, found {len(v)}")
    out.append(f"V-30 own promise (drop V > 30 s): mean {statistics.mean(float(m['v']) for m in v):.3f}, range "
               f"{min(float(m['v']) for m in v):.3f}-{max(float(m['v']) for m in v):.3f}; C-30 scored by V's rule mean "
               f"{statistics.mean(float(m['c']) for m in v):.3f}; V-30 forced mean {statistics.mean(float(m['f']) for m in v):.3f}; "
               f"same decisions as C-30 {sum(m['same'] == 'True' for m in v)}/{len(v)}")
    text = "\n".join(out) + "\n"
    with open(sys.argv[3], "x", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
