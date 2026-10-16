"""R16 (2026-10-10): same criteria as r13-ml-data-samples/noaa_event_days.py (weekday Mon-Fri, federal holidays NOT
removed; snow >= 25.4 mm / 76.2 mm; rain >= 20 mm without snow >= 1 in) on GHCND USW00094728 2009-2013, plus the
January 2013 weeks used by Fielbaum & Alonso-Mora 2020 (14-25 Jan 2013).
Source CSV: https://www.ncei.noaa.gov/access/services/data/v1?dataset=daily-summaries&stations=USW00094728&startDate=2009-01-01&endDate=2013-12-31&dataTypes=PRCP,SNOW,SNWD&units=metric&format=csv
Usage: python -I -B noaa_event_days_2009_2013.py <csv> <out-file>   (mode "x")
"""
import csv, datetime, sys
rows = list(csv.DictReader(open(sys.argv[1], encoding="utf-8")))
f = lambda k, r: float(r[k]) if r[k] not in ("", None) else 0.0
out = [f"# noaa_event_days_2009_2013.py; rows {len(rows)}; weekday = Mon-Fri; federal holidays NOT removed"]
for name, (a, b) in {"2009-01..2013-12": ("2009-01-01", "2013-12-31"), "2013 only": ("2013-01-01", "2013-12-31")}.items():
    wk = [r for r in rows if a <= r["DATE"] <= b and datetime.date.fromisoformat(r["DATE"]).weekday() < 5]
    s1 = [r["DATE"] for r in wk if f("SNOW", r) >= 25.4]
    s3 = [r["DATE"] for r in wk if f("SNOW", r) >= 76.2]
    rn = [r["DATE"] for r in wk if f("PRCP", r) >= 20.0 and f("SNOW", r) < 25.4]
    out.append(f"{name}: weekdays {len(wk)}; snow >= 1 in: {len(s1)}; snow >= 3 in: {len(s3)} {s3}; rain >= 20 mm (no snow >= 1 in): {len(rn)}")
    if len(s1) <= 40:
        out.append(f"   snow >= 1 in dates: {s1}")
jan = [r for r in rows if "2013-01-14" <= r["DATE"] <= "2013-01-25"]
out.append("Fielbaum & Alonso-Mora 2020 window 14-25 Jan 2013 (PRCP mm, SNOW mm): " + "; ".join(f"{r['DATE']} {r['PRCP']}/{r['SNOW']}" for r in jan))
text = "\n".join(out) + "\n"
open(sys.argv[2], "x", encoding="utf-8", newline="\n").write(text)
print(text)
