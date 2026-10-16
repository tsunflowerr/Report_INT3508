"""Exploratory: requests and distinct nodes per 2-hour window in sample_10_1 (and _2) for 14-16/11.
Usage: python -B demand_windows.py <out> (mode x)"""
import csv, sys, collections
D = "E:/RideBoundData/wp6/extracted/sha256/d9/d9e86f33645e5eec287d387f8d63ad41ddf41d4ef648138b65d636482e2c599e/FleetPy_Manhattan/demand/Manhattan_2018/matched/Manhattan_2019_corrected"
out = []
for day in ("2018-11-14", "2018-11-15", "2018-11-16"):
    for s in (1, 2):
        rows = list(csv.DictReader(open(f"{D}/{day}_sample_10_{s}.csv", encoding="utf-8")))
        if not out:
            out.append(f"columns: {list(rows[0].keys())}")
        for start in (25200, 28800, 50400, 54000, 57600, 61200):
            sel = [r for r in rows if start <= float(r["rq_time"]) < start + 7200]
            nodes = {r["start"] for r in sel} | {r["end"] for r in sel}
            out.append(f"{day} sample {s} window {start // 3600:02d}:00-{start // 3600 + 2:02d}:00: requests {len(sel)}, distinct nodes {len(nodes)}")
text = "\n".join(out) + "\n"
open(sys.argv[1], "x", encoding="utf-8", newline="\n").write(text)
print(text)
