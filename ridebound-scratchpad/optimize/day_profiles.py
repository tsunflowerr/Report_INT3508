"""Exploratory (2026-10-06): measured citywide travel-time factor per hour 06:00-22:00 for each day 12-18/11/2018,
and the 2018-11-15 ratio to the mean of the other weekdays (12, 13, 14, 16). Usage: python -B day_profiles.py <out> (mode x)"""
import csv, pathlib, statistics, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tang3" / "world"))
import preflight_world as pw
S = {}
for d in range(12, 19):
    with (pw.FACTORS / f"2018-11-{d}_tt_factors.csv").open(encoding="utf-8") as h:
        S[d] = {int(r["simulation_time"]): float(r["travel_time_factor"]) for r in csv.DictReader(h)}
out = ["# day_profiles.py (exploratory); factor at the start of each hour (15-min rows)", "hour " + " ".join(f"{d:>6}" for d in S) + "   15/other-weekdays"]
for hh in range(6, 23):
    t = hh * 3600
    row = [S[d].get(t) for d in S]
    others = statistics.mean(S[d][t] for d in (12, 13, 14, 16))
    out.append(f"{hh:02d}:00 " + " ".join(f"{v:6.3f}" for v in row) + f"   {S[15][t] / others:6.3f}")
steps = {d: max(abs(S[d][t + 900] / S[d][t] - 1) for t in range(21600, 79200, 900)) for d in S}
out.append("largest 15-min step 06:00-22:00 per day (%): " + ", ".join(f"{d}: {100 * s:.1f}" for d, s in steps.items()))
text = "\n".join(out) + "\n"
open(sys.argv[1], "x", encoding="utf-8", newline="\n").write(text)
print(text)
