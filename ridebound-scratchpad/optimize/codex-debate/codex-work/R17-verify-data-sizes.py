"""R17 size verification: 44 HEAD requests; no body retrieval; one process."""
import json,pathlib,urllib.request
P=pathlib.Path(__file__).resolve().parent
rows=[]
for y in range(2016,2021):
 for m in range(1,13):
  if (y,m)<(2016,7) or (y,m)>(2020,2):continue
  date=str(y)+"-"+str(m).zfill(2)
  u="https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_"+date+".parquet"
  with urllib.request.urlopen(urllib.request.Request(u,method="HEAD"),timeout=20) as r:
   n=int(r.headers["Content-Length"])
  rows.append(dict(month=date,url=u,bytes=n))
  if len(rows)%12==0:print("HEAD metadata",len(rows),flush=True)
assert len(rows)==44
total=sum(x["bytes"] for x in rows)
lines=["R17 data sizes: HEAD metadata only; decimal GB.",
 "2016-07..2020-02 files="+str(len(rows))+" bytes="+str(total)+" GB="+str(total/1e9)]
lines += [json.dumps(r,sort_keys=True) for r in rows]
with (P/"R17-data-size-verification.txt").open("x",encoding="utf-8") as f:f.write("\n".join(lines)+"\n")
print(lines[1])

