"""R13 (2026-10-09) EXPLORATORY, NOT SEALED, retrospective (all 7 days were seen before): how well do simple
predictors of the factor GROWTH ratio f(b0+h)/f(b0) do, per window, on the FleetPy Manhattan 15-min factors?
Anchored like the sealed forecast (the current level f(b0) is taken as known; only growth is predicted).
Predictors:
  naive      ratio 1 (current system: conditions stay as they are);
  hist12_13  m(b0+h)/m(b0), m = mean of 12 and 13 Nov (the sealed source vintage);
  hist_loo   same with the mean of the OTHER same-kind days (weekday/weekend), as forecast_predictability.py;
  momentum   (f(b0)/f(b0-1))**h, geometric continuation of the last observed 15-min step;
  blend      sqrt(hist12_13 * momentum).
Caveat: the bundle's factor for bin b is built from trips STARTING in bin b (factor-definition-checks), so f(b0) and
f(b0-1) are not fully observable at t0 in real time; momentum here is optimistic.
Error = |predicted - actual| / actual * 100 (%). Windows start at 07:00, 08:00, 14:00, 15:00, 17:00; b0 = 0..7-h.
Usage: python -I -B growth_predictor_screen.py <out-file>   (mode "x")
"""
import csv, math, pathlib, statistics, sys

NET = pathlib.Path("E:/RideBoundData/wp6/extracted/sha256/d9/"
                   "d9e86f33645e5eec287d387f8d63ad41ddf41d4ef648138b65d636482e2c599e/"
                   "FleetPy_Manhattan/networks/Manhattan_2019_corrected")
DAYS = [f"2018-11-{d}" for d in range(12, 19)]
KIND = {d: ("weekend" if d.endswith(("17", "18")) else "weekday") for d in DAYS}
S = {}
for d in DAYS:
    with (NET / f"{d}_tt_factors.csv").open(encoding="utf-8") as h:
        S[d] = {int(r["simulation_time"]) // 900: float(r["travel_time_factor"]) for r in csv.DictReader(h)}
WIN = {"w07": 28, "w08": 32, "w14": 56, "w15": 60, "w17": 68}


def preds(day, b0, h):
    f = S[day]
    actual = f[b0 + h] / f[b0]
    m = lambda b, src: statistics.mean(S[o][b] for o in src)  # noqa: E731
    src12 = ["2018-11-12", "2018-11-13"]
    loo = [o for o in DAYS if KIND[o] == KIND[day] and o != day]
    p = {"naive": 1.0,
         "hist12_13": m(b0 + h, src12) / m(b0, src12),
         "hist_loo": m(b0 + h, loo) / m(b0, loo),
         "momentum": (f[b0] / f[b0 - 1]) ** h}
    p["blend"] = math.sqrt(p["hist12_13"] * p["momentum"])
    return actual, p


out = ["# growth_predictor_screen.py (exploratory, retrospective, unsealed)"]
names = ["naive", "hist12_13", "hist_loo", "momentum", "blend"]
for h in (2, 4):
    out.append(f"\n## horizon {15 * h} min: mean abs % error of the growth ratio (n = starting bins)")
    for w, s in WIN.items():
        for day in DAYS:
            errs = {k: [] for k in names}
            for b0 in range(s, s + 8 - h):
                actual, p = preds(day, b0, h)
                for k in names:
                    errs[k].append(abs(p[k] - actual) / actual * 100)
            out.append(f"{w} {day} ({KIND[day][:4]}): " + " | ".join(
                f"{k} {statistics.mean(v):5.2f}" for k, v in errs.items()) + f" | n {len(errs['naive'])}")
text = "\n".join(out) + "\n"
open(sys.argv[1], "x", encoding="utf-8", newline="\n").write(text)
print(text)
