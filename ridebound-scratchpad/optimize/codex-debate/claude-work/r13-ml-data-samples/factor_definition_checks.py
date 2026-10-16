"""R13 (2026-10-09, read-only): two definitional checks on the FleetPy Manhattan factor files.
(1) hourly files: is travel_time_factor == speed_nw / speed ?
(2) 15-min files: does bin b's "travel requests" count track the demand-file trips requested in bin b (same bin) or
    in bin b-1 ("in the last 15 min", Syed et al. 2021 Sec. 5.2)? Compares mean |log ratio| of the two alignments.
(3) speed-filter effect: share of demand-file trips per day whose implied free-flow-based speed is not checkable
    (we have no durations), so only counts are compared.
Usage: python -I -B factor_definition_checks.py <out-file>   (mode "x")
"""
import csv, math, pathlib, statistics, sys

ROOT = pathlib.Path("E:/RideBoundData/wp6/extracted/sha256/d9/"
                    "d9e86f33645e5eec287d387f8d63ad41ddf41d4ef648138b65d636482e2c599e/FleetPy_Manhattan")
NET = ROOT / "networks" / "Manhattan_2019_corrected"
DEM = ROOT / "demand" / "Manhattan_2018" / "matched" / "Manhattan_2019_corrected"
out = []


def rows(path):
    with path.open(encoding="utf-8") as h:
        return list(csv.DictReader(h))


worst = 0.0
n = 0
for d in range(11, 19):
    for x in rows(NET / f"2018-11-{d}_tt_factors_hourly.csv"):
        f, s, snw = float(x["travel_time_factor"]), float(x["speed"]), float(x["speed_nw"])
        worst = max(worst, abs(f - snw / s) / f)
        n += 1
out.append(f"(1) hourly rows {n}: max |factor - speed_nw/speed| / factor = {worst:.2e}")

for d in range(12, 19):
    fr = rows(NET / f"2018-11-{d}_tt_factors.csv")
    cnt = {}
    for x in rows(DEM / f"2018-11-{d}.csv"):
        b = int(float(x["rq_time"])) // 900
        cnt[b] = cnt.get(b, 0) + 1
    same, prev, ratio_same = [], [], []
    for x in fr:
        b = int(x["time_interval"])
        req = float(x["travel requests"])
        if b >= 1 and cnt.get(b) and cnt.get(b - 1):
            same.append(abs(math.log(req / cnt[b])))
            prev.append(abs(math.log(req / cnt[b - 1])))
            ratio_same.append(req / cnt[b])
    out.append(f"(2) 2018-11-{d}: mean |log(requests/demand)| same-bin {statistics.mean(same):.4f} vs previous-bin "
               f"{statistics.mean(prev):.4f}; same-bin ratio requests/demand mean {statistics.mean(ratio_same):.4f} "
               f"min {min(ratio_same):.4f} max {max(ratio_same):.4f}")

text = "\n".join(out) + "\n"
open(sys.argv[1], "x", encoding="utf-8", newline="\n").write(text)
print(text)
