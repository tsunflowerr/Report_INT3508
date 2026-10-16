"""R13 (2026-10-09, read-only): inventory of the FleetPy Manhattan travel-time-factor files.

Reports per file: rows, time coverage, step; per day: factor min/max/mean, trips per day ("travel requests"),
and a consistency check of the documented definition ("scaling average free flow travel times to the travel
times of the reported trips", README_Manhattan.md:28) against the bundled demand file and free-flow table:
  ratio_check = (average travel duration) / (mean free-flow tt of that bin's demand-file trips).
Usage: python -I -B factor_inventory.py <out-file>   (mode "x"; reads only, never writes inside the bundle)
"""
import csv, pathlib, statistics, sys
import numpy as np

ROOT = pathlib.Path("E:/RideBoundData/wp6/extracted/sha256/d9/"
                    "d9e86f33645e5eec287d387f8d63ad41ddf41d4ef648138b65d636482e2c599e/FleetPy_Manhattan")
NET = ROOT / "networks" / "Manhattan_2019_corrected"
DEM = ROOT / "demand" / "Manhattan_2018" / "matched" / "Manhattan_2019_corrected"
out = []
p = out.append


def rows(path):
    with path.open(encoding="utf-8") as h:
        return list(csv.DictReader(h))


p("# factor_inventory.py output")
for path in sorted(NET.glob("*.csv")):
    r = rows(path)
    t = [int(float(x["simulation_time"])) for x in r]
    steps = sorted({b - a for a, b in zip(t, t[1:])})
    f = [float(x["travel_time_factor"]) for x in r]
    p(f"{path.name}: rows {len(r)}; columns {list(r[0].keys())}; t {t[0]}..{t[-1]} s; steps {steps}; "
      f"factor min {min(f):.3f} max {max(f):.3f} mean {statistics.mean(f):.3f}")

# per-day 15-min profile summaries
p("")
p("## 15-min files: per day")
for d in range(11, 19):
    path = NET / f"2018-11-{d}_tt_factors.csv"
    if not path.exists():
        p(f"2018-11-{d}: NO 15-min file")
        continue
    r = rows(path)
    f = [float(x["travel_time_factor"]) for x in r]
    n = [float(x["travel requests"]) for x in r]
    hh = lambda h0, h1: [float(x["travel_time_factor"]) for x in r if h0 * 3600 <= int(x["simulation_time"]) < h1 * 3600]  # noqa
    p(f"2018-11-{d}: bins {len(r)}; trips sum {sum(n):.0f}; min trips/bin {min(n):.0f}; factor min {min(f):.3f} "
      f"max {max(f):.3f}; mean 07-09 {statistics.mean(hh(7, 9)):.3f}; mean 14-17 {statistics.mean(hh(14, 17)):.3f}; "
      f"mean 17-19 {statistics.mean(hh(17, 19)):.3f}")

# week file: day coverage
r = rows(NET / "2018-11-11_to_2018-11-18_tt_factors.csv")
t = [int(x["simulation_time"]) for x in r]
p("")
p(f"week 15-min file: first {t[0]} s (= day {t[0] // 86400} after 11 Nov), last {t[-1]} s (= day {t[-1] // 86400}), "
  f"rows {len(r)} = {len(r) / 96:.2f} days of 96 bins")
same = 0
for d in range(12, 19):
    day = {int(x["simulation_time"]): float(x["travel_time_factor"]) for x in rows(NET / f"2018-11-{d}_tt_factors.csv")}
    off = (d - 11) * 86400
    week = {s - off: float(x["travel_time_factor"]) for x in r for s in [int(x["simulation_time"])] if off <= s < off + 86400}
    same += all(abs(day[k] - week[k]) < 1e-12 for k in day) and set(day) == set(week)
p(f"week file equals the 7 daily 15-min files bin by bin: {same}/7 days")

# demand-file consistency check for the documented definition
tt = np.load(NET / "ff" / "tables" / "nn_fastest_tt.npy", mmap_mode="r")
p("")
p(f"## definition check; free-flow table shape {tt.shape}")
for d in (12, 15):
    fr = rows(NET / f"2018-11-{d}_tt_factors.csv")
    dem = rows(DEM / f"2018-11-{d}.csv")
    bins = {}
    for x in dem:
        b = int(float(x["rq_time"])) // 900
        bins.setdefault(b, []).append((int(x["start"]), int(x["end"])))
    lines = []
    for x in fr:
        b = int(x["time_interval"])
        pairs = bins.get(b, [])
        ff = [float(tt[s, e]) for s, e in pairs]
        mff = statistics.mean(ff) if ff else float("nan")
        avg = float(x["average travel duration"])
        fac = float(x["travel_time_factor"])
        lines.append((b, float(x["travel requests"]), len(pairs), fac, avg / mff, mff, avg))
    for b, nreq, ndem, fac, rc, mff, avg in lines:
        if b % 8 == 0 or b in (28, 29, 30, 31, 33, 35):
            p(f"2018-11-{d} bin {b:2d}: factor {fac:.4f} | travel requests {nreq:.0f} vs demand rows {ndem} | "
              f"avg dur {avg:.1f} s / mean ff {mff:.1f} s = {rc:.4f}")
    diffs = [abs(rc - fac) / fac for _, _, _, fac, rc, _, _ in lines]
    p(f"2018-11-{d}: |avgdur/meanff - factor|/factor over 96 bins: mean {100 * statistics.mean(diffs):.2f}% "
      f"max {100 * max(diffs):.2f}%; demand rows/day {len(dem)}; sum travel requests {sum(l[1] for l in lines):.0f}")

text = "\n".join(out) + "\n"
open(sys.argv[1], "x", encoding="utf-8", newline="\n").write(text)
print(text)
