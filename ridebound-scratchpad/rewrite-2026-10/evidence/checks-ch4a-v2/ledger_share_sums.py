"""Read-only: numerator and denominator of the ledger dispatch share (Bang 4.9 last row), 2026-10-12.

Rule (recompute_addendum_1.py `ledger_dispatch_share_late60`; eq:so of chapter 3): among completed riders with
A - p0 > 60 s (p0 = first drop promise without forecast), share = sum of the signed dispatch part q = sum c (TSV column
netC, ms) divided by sum of (A - p0) (ms). Printed per arm with the registered share for comparison.
Input (read only): optimize/codex-debate/claude-work/r21-stage1a/stage1a-2026-10-10-riders.tsv (U, C-30, C-120).
Usage: python -B -I ledger_share_sums.py <out.txt>   (output opened in mode "x")
"""
import csv
import sys

TSV = (r"E:\Code\Report_INT3508\ridebound-scratchpad\optimize\codex-debate\claude-work\r21-stage1a"
       r"\stage1a-2026-10-10-riders.tsv")
REG = {"U": "73.4", "C-30": "1.2", "C-120": "38.8"}  # REG C24, N-23 (ADD1 ledger_dispatch_share_late60)
acc = {}
with open(TSV, encoding="utf-8", newline="") as fh:
    for row in csv.DictReader(fh, delimiter="\t"):
        if row["lifecycle"] != "completed":
            continue
        lat = float(row["A"]) - float(row["p0"])
        if lat > 60000:
            d = acc.setdefault(row["arm"], [0, 0.0, 0.0])
            d[0] += 1
            d[1] += float(row["netC"])
            d[2] += lat
out = ["# ledger_share_sums.py: riders late > 60 s vs p0; signed dispatch seconds / lateness seconds"]
fails = 0
for arm in ("U", "C-30", "C-120"):
    n, q, s = acc[arm]
    share = f"{100 * q / s:.1f}"
    ok = share == REG[arm]
    fails += (not ok)
    out.append(f"{arm}: riders {n}; sum q = {q / 1000:.3f} s; sum (A - p0) = {s / 1000:.3f} s; share {share}% "
               f"(registered {REG[arm]}%) -> {'OK' if ok else 'FAIL'}")
out.append(f"FAIL count: {fails}")
text = "\n".join(out) + "\n"
with open(sys.argv[1], "x", encoding="utf-8", newline="\n") as fh:
    fh.write(text)
print(text)
