"""Task A: group totals for the thesis table (real W5 / synthetic W1, W2, W4 / easing W3), read-only.

Inputs: the jobs table of vm_analyze.py (served, non-normal share) and the log of vm_describe.py (same decisions as
C-30, V-30's own promise V > 30 s). Served = sum over the group's cells; shares = mean over the group's cells (as the
sweep tables). Usage: python -B vm_aggregate.py <jobs.tsv> <describe.txt> <new-log>   (mode "x")
"""
import csv
import re
import sys

GROUPS = {"real (W5)": ("W5",), "synthetic (W1, W2, W4)": ("W1", "W2", "W4"), "easing (W3)": ("W3",)}
LINE = re.compile(r"^(?P<world>W\d) (?P<cell>w\d\d) (?P<arm>\S+)\s+(?P<variant>\S+)\s+\|\s+(?P<served>\d+) \| (?P<same>True|False)\s*\| "
                  r"(?P<v30>[\d.]+) \| (?P<a30>[\d.]+) \| (?P<c30>[\d.]+) \|")


def main() -> int:
    if len(sys.argv) != 4:
        print(__doc__)
        return 2
    jobs = {(r["variant"], r["arm"], r["world"], r["cell"][-3:]): r
            for r in csv.DictReader(open(sys.argv[1], encoding="utf-8"), delimiter="\t")}
    described = {}
    for line in open(sys.argv[2], encoding="utf-8"):
        if m := LINE.match(line.rstrip("\n")):
            described[(m["variant"], m["arm"], m["world"], m["cell"])] = m
    out = [f"# vm_aggregate.py; inputs {sys.argv[1]} {sys.argv[2]}"]
    cells = ("w08", "w17")
    for name, worlds in GROUPS.items():
        keys = [(w, c) for w in worlds for c in cells]
        served = lambda variant, arm: sum(int(jobs[(variant, arm, w, c)]["M1_completed"]) for w, c in keys)  # noqa: E731
        mean = lambda values: sum(values) / len(values)  # noqa: E731
        same = sum(described[("b", "V-30", w, c)]["same"] == "True" for w, c in keys)
        v_own = mean([float(described[("b", "V-30", w, c)]["v30"]) for w, c in keys])
        c_by_v = mean([float(described[("sweep", "C-30", w, c)]["v30"]) for w, c in keys])
        forced = mean([float(jobs[("b", "V-30", w, c)]["M5_nonNormalShare"]) for w, c in keys])
        forced_a = mean([float(jobs[("a", "V-30", w, c)]["M5_nonNormalShare"]) for w, c in keys])
        out.append(f"{name}: cells {len(keys)}, requests {108 * len(keys)} | served C-30 {served('sweep', 'C-30')} "
                   f"V-30 a/b {served('a', 'V-30')}/{served('b', 'V-30')} M-30 a/b {served('a', 'M-30')}/{served('b', 'M-30')} "
                   f"| V-30(b) same decisions as C-30 {same}/{len(keys)} | V-30(b) own promise broken (V>30 s) {v_own:.1%} "
                   f"| C-30 scored by V's rule {c_by_v:.1%} | V-30 forced decisions a/b {forced_a:.1%}/{forced:.1%}")
    text = "\n".join(out) + "\n"
    with open(sys.argv[3], "x", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
