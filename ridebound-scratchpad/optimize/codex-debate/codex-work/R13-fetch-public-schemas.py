from pathlib import Path
import urllib.request, urllib.parse, hashlib, json, concurrent.futures, datetime
ROOT=Path(__file__).resolve().parent
urls={
"chicago-meta":"https://data.cityofchicago.org/api/views/m6dm-c72p.json",
"chicago-sample":"https://data.cityofchicago.org/resource/m6dm-c72p.json?"+urllib.parse.urlencode({"$select":"trip_start_timestamp,trip_end_timestamp,trip_seconds,shared_trip_authorized,trips_pooled","$limit":5}),
"nyc-hvf2019-meta":"https://data.cityofnewyork.us/api/views/4p5c-cbgn.json",
"nyc-hvf2019-sample":"https://data.cityofnewyork.us/resource/4p5c-cbgn.json?"+urllib.parse.urlencode({"$limit":3}),
"nyc-tlc-page":"https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page",
"nyc-hvf-dictionary":"https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_hvfhs.pdf",
"lyft-help":"https://help.lyft.com/hc/en-us/all/articles/115013078668",
"grubhub-terms":"https://lp.grubhub.com/legal/ghgterms"
}
def fetch(item):
 name,url=item
 try:
  req=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0 research-source-verification"})
  with urllib.request.urlopen(req,timeout=20) as response:
   b=response.read(6000000)
   entry={"name":name,"url":url,"final_url":response.url,"status":response.status,"content_type":response.headers.get("Content-Type"),"sha256":hashlib.sha256(b).hexdigest(),"bytes":len(b)}
   filename="R13-public-"+name+(".pdf" if b.startswith(b"%PDF") else ".txt")
   with (ROOT/filename).open("xb") as f:f.write(b)
   entry["file"]=filename
   if "json" in entry["content_type"]:
    data=json.loads(b)
    if isinstance(data,dict) and "columns" in data:
     entry["dataset_name"]=data.get("name");entry["description"]=data.get("description")
     entry["columns"]=[{k:c.get(k) for k in ["fieldName","name","dataTypeName","description"]} for c in data["columns"] if not c["fieldName"].startswith(":")]
    elif isinstance(data,list):entry["sample"]=data
   return entry
 except Exception as exc:return {"name":name,"url":url,"error":str(exc)}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool: results=list(pool.map(fetch,urls.items()))
with (ROOT/"R13-public-fetch-manifest.json").open("x",encoding="utf-8") as f:json.dump({"utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),"results":results},f,indent=2)
for e in results:print(json.dumps(e,ensure_ascii=True),flush=True)
