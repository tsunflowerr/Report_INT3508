"""R16: independent inventory of available saved NOAA event labels.
Daily labels are evaluation strata only, never quote-time predictor features.
"""
import csv,datetime,hashlib,json,pathlib
HERE=pathlib.Path(__file__).resolve().parent
SRC=HERE.parent/"claude-work/r13-ml-data-samples/noaa_ghcnd_centralpark_2014-2020.csv"
rows=list(csv.DictReader(SRC.open(encoding="utf-8")))
def amount(r,k):
    try:return float(r.get(k) or 0)
    except ValueError:return 0
out=["# R16 NOAA inventory (existing saved station CSV; no retrieval or model fitting)",
     "source="+str(SRC)+" sha256="+hashlib.sha256(SRC.read_bytes()).hexdigest(),
     "Evaluation-only weather strata: SNOW >=25.4 mm or PRCP >=20 mm; event spells join flagged dates <=2 calendar days apart; this does not prove event independence."]
for name,start,end in (("fit","2016-07-01","2017-12-31"),("calibration","2018-01-01","2018-08-31"),("test_2018","2018-09-01","2018-12-31"),("test_2019","2019-01-01","2019-12-31")):
    part=[r for r in rows if start<=r["DATE"]<=end]
    flagged=[r for r in part if amount(r,"SNOW")>=25.4 or amount(r,"PRCP")>=20]
    dates=sorted(set(r["DATE"] for r in flagged));spells=[]
    for date in dates:
        dt=datetime.date.fromisoformat(date)
        if not spells or (dt-datetime.date.fromisoformat(spells[-1][-1])).days>2:spells.append([])
        spells[-1].append(date)
    weekdays=[r for r in flagged if datetime.date.fromisoformat(r["DATE"]).weekday()<5]
    result=dict(split=name,start=start,end=end,available_dates=len(part),weather_flagged_dates=len(dates),weather_flagged_weekdays=len(weekdays),snow25_dates=[r["DATE"] for r in flagged if amount(r,"SNOW")>=25.4],spells=spells)
    out.append(json.dumps(result,sort_keys=True))
with (HERE/"R16-weather-inventory.txt").open("x",encoding="utf-8",newline="\n") as f:f.write("\n".join(out)+"\n")
print("\n".join(out))

