"""R17 small metadata audit: closed HTTP ranges; no row downloads; saved-table arithmetic;
thesis citation search; last-checkpoint witness counts. One process, exclusive outputs.
"""
import base64,collections,csv,hashlib,importlib.util,json,pathlib,re,struct,sys,urllib.request
HERE=pathlib.Path(__file__).resolve().parent;ROOT=HERE.parents[2];C=HERE.parent/"claude-work"
p=C/"r13-ml-data-samples/parquet_footer_probe.py"
source=p.read_text(encoding="utf-8").split("PTYPE =")[0]
ns={"__name__":"r17_footer_decoder"};exec(compile(source,str(p),"exec"),ns)
def http(req,limit=None):
 with urllib.request.urlopen(req,timeout=30) as r:
  if limit is not None:
   assert r.status==206 and int(r.headers["Content-Length"])<=limit
   b=r.read(limit+1);assert len(b)<=limit;return b
  return dict(r.headers)
lines=["R17 metadata verification; closed byte ranges only, no row data."]
for month in ("2013-01","2013-11"):
 url="https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_"+month+".parquet"
 try:
  head=http(urllib.request.Request(url,method="HEAD"));n=int(head.get("Content-Length",head.get("content-length")))
  def get(a,b):return http(urllib.request.Request(url,headers={"Range":"bytes="+str(a)+"-"+str(b)}),100000)
  tail=get(n-8,n-1);assert tail[4:]==b"PAR1"
  k=struct.unpack("<I",tail[:4])[0];meta=ns["file_meta"](get(n-8-k,n-9))
  cols=[x["name"] for x in meta["schema"][1:]]
  assert "PULocationID" in cols and "DOLocationID" in cols and not any("lon" in x.lower() or "lat" in x.lower() for x in cols)
  lines.append("FOOTER "+json.dumps(dict(url=url,bytes=n,rows=meta["num_rows"],columns=cols),sort_keys=True))
 except Exception as e:lines.append("FOOTER UNVERIFIED "+url+" "+type(e).__name__+" "+str(e))
tex=pathlib.Path("E:/Code/Report_INT3508/ridebound/noi-dung")
pats={"HZ":r"(?i)H[?o]rl|Zwick|000561639|Traffic uncertainty in on-demand","T38":r"T3\.8|2[., ]338|2[., ]434"}
for tag,pat in pats.items():
 hits=[dict(path=str(p),line=i+1,text=l) for p in tex.glob("*.tex") for i,l in enumerate(p.read_text(encoding="utf-8").splitlines()) if re.search(pat,l)]
 lines.append("TEX "+tag+" "+json.dumps(hits,ensure_ascii=False))
lines.append("TEX files scanned "+str(len(list(tex.glob("*.tex")))))
# Saved run table verifies 21/22, without pretending it is raw trajectory re-analysis.
sweep=ROOT/"tang3/sweep"
sw={(r["arm"],r["world"],r["cell"]):r for r in csv.DictReader((sweep/"sweep-jobs-2026-09-26.tsv").open(encoding="utf-8"),delimiter="\t")}
nw=[r for r in csv.DictReader((sweep/"noworse-jobs-2026-09-26.tsv").open(encoding="utf-8"),delimiter="\t") if r["kind"]=="treatment"]
lines.append("RECOVERY_B_TABLE "+json.dumps(dict(n=len(nw),b=sum(int(r["M1_completed"]) for r in nw),
 a=sum(int(r["a_M1_completed"]) for r in nw),C=sum(int(r["C_M1_completed"]) for r in nw),
 equal=sum(int(r["M1_completed"])==int(r["C_M1_completed"]) for r in nw)),sort_keys=True))
# Tail reading sufficient only if terminal outgoing checkpoint actually exists in bounded tail.
old=json.loads((HERE/"R15-audit.json").read_text(encoding="utf-8"))["runs"]
agg=collections.Counter();hashes=set();per=[]
for run in old:
 if run["pop"]!="t38" or run["arm"]!="Mplus-30":continue
 p=pathlib.Path(run["path"])
 with p.open("rb") as f:
  start=max(0,p.stat().st_size-64000000);f.seek(start)
  if start:f.readline()
  rows=f.readlines()
 checkpoint=None
 for line in reversed(rows):
  row=json.loads(line)
  if row["direction"]!="runnerToAdapter":continue
  raw=base64.b64decode(row["frameBase64"])
  if b'"checkpoint"' in raw[:256]:
   assert hashlib.sha256(raw).hexdigest()==row["frameSha256"]
   checkpoint=json.loads(raw)["payload"]["content"]["onlineState"];break
 assert checkpoint is not None
 counts=collections.Counter(x["kind"] for x in checkpoint["incidentLedger"]["breaches"])
 agg.update(counts);per.append(dict(cell=run["cell"],counts=dict(counts)))
 with p.open("rb") as f:
  for line in f:
   e=json.loads(base64.b64decode(json.loads(line)["frameBase64"]))
   if e["messageType"]=="initializeRun":
    hashes.add(e["payload"]["manifest"]["policyConfigurationHash"]);break
lines.append("T38 MPLUS30 checkpoints "+json.dumps(dict(runs=len(per),counts=dict(agg),policyConfigurationHashes=sorted(hashes)),sort_keys=True))
lines.extend("T38 "+json.dumps(x,sort_keys=True) for x in per)
with (HERE/"R17-metadata-verification.txt").open("x",encoding="utf-8") as f:f.write("\n".join(lines)+"\n")
print("\n".join(lines))

