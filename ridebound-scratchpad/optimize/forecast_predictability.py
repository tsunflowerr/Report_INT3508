"""Exploratory (2026-10-06): how much of the travel-time change over the next 15/30/45 min is predictable from other
days of the same kind (weekday from the other weekdays, weekend from the other weekend day), versus the current
system's implicit assumption "conditions stay as they are now" (naive). Uses the measured FleetPy Manhattan factor
files (column travel_time_factor), 15-min resolution. Error = |predicted ratio - actual ratio| of f(t+h)/f(t), in %.
Usage: python -B forecast_predictability.py <out-file>   (mode "x")
"""
import csv, pathlib, statistics, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tang3" / "world"))
import preflight_world as pw

def series(day):
    rows = {}
    with (pw.FACTORS / f"{day}_tt_factors.csv").open(encoding="utf-8") as h:
        for row in csv.DictReader(h):
            rows[int(row["simulation_time"])] = float(row["travel_time_factor"])
    return rows

DAYS = {f"2018-11-{d}": ("weekend" if d in (17, 18) else "weekday") for d in range(12, 19)}
S = {d: series(d) for d in DAYS}
WINDOWS = {"07:00-09:00": 25200, "08:00-10:00": 28800, "17:00-19:00": 61200}
out = ["# forecast_predictability.py (exploratory)", f"factor rows per day: { {d: len(s) for d, s in S.items()} }"]
for wname, start in WINDOWS.items():
    for h in (1, 2, 3):
        naive, fc, actual_abs = [], [], []
        for day, kind in DAYS.items():
            others = [o for o, k in DAYS.items() if k == kind and o != day]
            for b in range(0, 8 - h + 1):
                t, t2 = start + b * 900, start + (b + h) * 900
                if t not in S[day] or t2 not in S[day]:
                    continue
                actual = S[day][t2] / S[day][t]
                pred = statistics.mean(S[o][t2] for o in others) / statistics.mean(S[o][t] for o in others)
                naive.append(abs(1.0 - actual) * 100); fc.append(abs(pred - actual) * 100); actual_abs.append(abs(actual - 1) * 100)
        out.append(f"{wname} horizon {15*h:>2} min: mean |change| {statistics.mean(actual_abs):.2f}% | error naive {statistics.mean(naive):.2f}% "
                   f"(max {max(naive):.2f}) | error forecast {statistics.mean(fc):.2f}% (max {max(fc):.2f}) | n={len(fc)}")
text = "\n".join(out) + "\n"
open(sys.argv[1], "x", encoding="utf-8", newline="\n").write(text)
print(text)
