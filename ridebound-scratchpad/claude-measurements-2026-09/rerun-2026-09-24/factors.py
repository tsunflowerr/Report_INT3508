"""Re-read measured Manhattan travel-time factors (K18) for the two drift windows.

Reads the FleetPy Manhattan tt_factors CSVs, prints the header first (a previous
session once read the wrong column), then for each day and each window reports
the factor at the window start, the end/start ratio, and the running maximum of
the ratio over the first 30 minutes. Read-only.
"""
import csv
import glob

PATTERN = ("E:/RideBoundData/wp6/extracted/sha256/*/*/FleetPy_Manhattan/networks/"
           "Manhattan_2019_corrected/2018-11-*_tt_factors.csv")
WINDOWS = {"w08": 28800, "w17": 61200}
LENGTH = 7200

files = sorted(glob.glob(PATTERN))
print("files:", len(files))
with open(files[0], newline="", encoding="utf-8") as h:
    print("header:", next(csv.reader(h)))

for path in files:
    day = path.replace("\\", "/").rsplit("/", 1)[1][:10]
    rows = []
    with open(path, newline="", encoding="utf-8") as h:
        for row in csv.DictReader(h):
            rows.append((float(row["simulation_time"]), float(row["travel_time_factor"])))
    rows.sort()
    for name, start in WINDOWS.items():
        inside = [(t, f) for t, f in rows if start <= t <= start + LENGTH]
        if not inside or inside[0][0] != start:
            print(f"{day} {name}: no row exactly at window start")
            continue
        f0 = inside[0][1]
        end = inside[-1]
        early = max(f / f0 for t, f in inside if t <= start + 1800)
        print(f"{day} {name}: t0={start} f0={f0:.4f} end_t={end[0]:.0f} "
              f"end/start={end[1] / f0:.3f} max_ratio_first30min={early:.4f} "
              f"points={len(inside)}")
