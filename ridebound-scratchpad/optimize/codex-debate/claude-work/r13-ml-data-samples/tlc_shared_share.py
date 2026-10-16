"""R13 (2026-10-09): share of shared trips per day by TLC license class and month, from the TLC monthly
indicators CSV (https://www.nyc.gov/assets/tlc/downloads/csv/data_reports_monthly.csv, saved locally).
Column 'Trips Per Day Shared' / 'Trips Per Day'. All five boroughs (TLC aggregate; NOT Manhattan-only).
Usage: python -I -B tlc_shared_share.py <csv> <out-file>   (mode "x")
"""
import csv, sys


def num(s):
    s = (s or "").replace(",", "").strip()
    return float(s) if s and s != "-" else None


rows = list(csv.DictReader(open(sys.argv[1], encoding="utf-8-sig")))
classes = sorted({r["License Class"] for r in rows})
out = [f"# tlc_shared_share.py; rows {len(rows)}; classes {classes}"]
months = sorted({r["Month/Year"] for r in rows})
out.append(f"months {months[0]} .. {months[-1]}")
for r in sorted(rows, key=lambda r: (r["License Class"], r["Month/Year"])):
    t, s = num(r["Trips Per Day"]), num(r["Trips Per Day Shared"])
    if s is None or t is None:
        continue
    m = r["Month/Year"]
    if m[:4] in ("2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025", "2026"):
        out.append(f"{r['License Class']:<20} {m}: trips/day {t:>9.0f} shared/day {s:>8.0f} share {100 * s / t:5.1f}%")
text = "\n".join(out) + "\n"
open(sys.argv[2], "x", encoding="utf-8", newline="\n").write(text)
print(text)
