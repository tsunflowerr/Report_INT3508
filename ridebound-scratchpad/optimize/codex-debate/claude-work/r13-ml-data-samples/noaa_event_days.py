"""R13 (2026-10-09): count weekday weather-event days at Central Park (GHCND USW00094728, metric units:
PRCP mm, SNOW mm) per period, to size how many 'snow-like' training/test days NYC TLC data could offer.
Source: https://www.ncei.noaa.gov/access/services/data/v1?dataset=daily-summaries&stations=USW00094728&...
Usage: python -I -B noaa_event_days.py <csv> <out-file>   (mode "x")
"""
import csv, datetime, sys

rows = list(csv.DictReader(open(sys.argv[1], encoding="utf-8")))
PERIODS = {
    "2018-09..2018-12": ("2018-09-01", "2018-12-31"),
    "2018-10..2018-12": ("2018-10-01", "2018-12-31"),
    "2014-01..2020-02 (all yellow w/ exact times, pre-COVID)": ("2014-01-01", "2020-02-29"),
    "2016-07..2020-02 (zone-ID era, pre-COVID)": ("2016-07-01", "2020-02-29"),
}
US_HOLIDAYS_NOTE = "weekday = Mon-Fri; federal holidays NOT removed"
out = [f"# noaa_event_days.py; rows {len(rows)}; {US_HOLIDAYS_NOTE}"]
for name, (a, b) in PERIODS.items():
    wk = [r for r in rows if a <= r["DATE"] <= b and datetime.date.fromisoformat(r["DATE"]).weekday() < 5]
    f = lambda k, r: float(r[k]) if r[k] not in ("", None) else 0.0  # noqa: E731
    snow25 = [r["DATE"] for r in wk if f("SNOW", r) >= 25.4]
    snow75 = [r["DATE"] for r in wk if f("SNOW", r) >= 76.2]
    rain20 = [r["DATE"] for r in wk if f("PRCP", r) >= 20.0 and f("SNOW", r) < 25.4]
    out.append(f"{name}: weekdays {len(wk)}; snow >= 1 in: {len(snow25)}; snow >= 3 in: {len(snow75)} {snow75}; "
               f"rain >= 20 mm (no snow >= 1 in): {len(rain20)}")
    if len(snow25) <= 12:
        out.append(f"   snow >= 1 in dates: {snow25}")
text = "\n".join(out) + "\n"
open(sys.argv[2], "x", encoding="utf-8", newline="\n").write(text)
print(text)
