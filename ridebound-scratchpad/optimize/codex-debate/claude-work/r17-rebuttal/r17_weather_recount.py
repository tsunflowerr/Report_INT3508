"""R17 rebuttal: independent recount of Codex R16-weather-inventory.txt (flags SNOW >= 25.4 mm or PRCP >= 20 mm;
spells join flagged dates <= 2 calendar days apart; weekdays Mon-Fri, holidays not removed). Read-only; output mode "x".
Usage: python -B r17_weather_recount.py <out.txt>"""
import csv
import datetime as dt
import sys

SRC = (r"E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/claude-work/r13-ml-data-samples/"
       r"noaa_ghcnd_centralpark_2014-2020.csv")
SPLITS = (("fit", "2016-07-01", "2017-12-31"), ("calibration", "2018-01-01", "2018-08-31"),
          ("test_2018", "2018-09-01", "2018-12-31"), ("test_2019", "2019-01-01", "2019-12-31"))


def num(x):
    try:
        return float(x)
    except ValueError:
        return None


rows = {}
with open(SRC, newline="", encoding="utf-8") as fh:
    for r in csv.DictReader(fh):
        rows[dt.date.fromisoformat(r["DATE"])] = (num(r["PRCP"]), num(r["SNOW"]))
lines = [f"# r17_weather_recount.py over {SRC}"]
for name, a, b in SPLITS:
    a, b = dt.date.fromisoformat(a), dt.date.fromisoformat(b)
    days = sorted(d for d in rows if a <= d <= b)
    flagged = [d for d in days if (rows[d][1] or 0) >= 25.4 or (rows[d][0] or 0) >= 20]
    snow = [d for d in days if (rows[d][1] or 0) >= 25.4]
    spells = []
    for d in flagged:
        if spells and (d - spells[-1][-1]).days <= 2:
            spells[-1].append(d)
        else:
            spells.append([d])
    lines.append(f"{name}: available {len(days)} flagged {len(flagged)} flagged_weekdays "
                 f"{sum(d.weekday() < 5 for d in flagged)} spells {len(spells)} snow25 {len(snow)} "
                 f"snow25_weekdays {sum(d.weekday() < 5 for d in snow)} snow25_dates {[d.isoformat() for d in snow]}")
text = "\n".join(lines) + "\n"
with open(sys.argv[1], "x", encoding="utf-8", newline="\n") as fh:
    fh.write(text)
print(text)
