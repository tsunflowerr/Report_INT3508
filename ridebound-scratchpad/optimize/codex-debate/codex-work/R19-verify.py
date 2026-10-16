"""R19 read-only design/provenance checks; no C120 outcome extraction or job control."""
from __future__ import annotations
import collections, datetime, hashlib, json, pathlib
H=pathlib.Path(__file__).resolve().parent; D=H.parent; S=D.parents[1]
T=S/"tang3"; out={}; inputs={}
def digest(p):
 p=pathlib.Path(p); b=p.read_bytes(); z=hashlib.sha256(b).hexdigest()
 inputs[str(p)]=dict(bytes=len(b),sha256=z); return z
def load(p):
 digest(p); return json.loads(pathlib.Path(p).read_text(encoding="utf-8-sig"))
def record(k,v):out[k]=v;print(k+" "+json.dumps(v,sort_keys=True),flush=True)
ag=D/"antigravity-work"
record("input_copies",{n:dict(copy_sha256=digest(ag/"inputs"/n),original_sha256=digest(D/("codex-work" if n=="R15-CONFIRM-CODEX.md" else "claude-work")/n)) for n in ("R13-FINAL-VERDICT.md","R15-CONFIRM-CODEX.md","BAN-GIAO-PHIEN-2026-10-09.md")})
for n in ("ROUND16-FACT-PACK.md","ROUND16-REVIEW-STANDARD.md"):
 digest(ag/"inputs"/n)
digest(ag/"R16-ANTIGRAVITY.md")
plan=T/"t38c120/C120-PLAN.md";seal=T/"t38c120/C120-PLAN.sha256"
expected=seal.read_text().split()[0];actual=digest(plan);digest(seal)
record("seal",dict(expected=expected,actual=actual,matches=expected==actual,
 plan_mtime_utc=datetime.datetime.fromtimestamp(plan.stat().st_mtime,datetime.timezone.utc).isoformat(),
 seal_mtime_utc=datetime.datetime.fromtimestamp(seal.stat().st_mtime,datetime.timezone.utc).isoformat()))
for p in ("t38c120/run_t38c120.py","t38/run_t38.py","w07/run_w07.py","pilot/run_pilot.py","world/preflight_world.py","world/preflight_world_v1_1.py","world/preflight_world_v1_2.py","runner_manifest.py"):
 digest(T/p)
configs={a:load(T/("configs/"+a+".json")) for a in ("U","C-30","C-120")}
def diff(a,b,p=""):
 if isinstance(a,dict) and isinstance(b,dict):
  return [v for k in sorted(set(a)|set(b)) for v in diff(a.get(k,"<absent>"),b.get(k,"<absent>"),p+"/"+k)]
 if isinstance(a,list) and isinstance(b,list) and len(a)==len(b):
  return [v for i,(x,y) in enumerate(zip(a,b)) for v in diff(x,y,p+"/"+str(i))]
 return [] if a==b else [dict(path=p,left=a,right=b)]
record("C30_C120_diff",diff(configs["C-30"],configs["C-120"]))
wp4=load(T/"configs/wp4-tier3-v2.json")
record("WP4",dict(sha256=inputs[str(T/"configs/wp4-tier3-v2.json")]["sha256"],config=wp4))
runner=pathlib.Path("C:/RideBoundData/research/runner-tier3-v2")
body=[]
for p in sorted(runner.rglob("*"),key=lambda p:p.relative_to(runner).as_posix()):
 if p.is_file():body.append(p.relative_to(runner).as_posix()+"\t"+digest(p)+"\t"+str(p.stat().st_size))
record("runner_tree",dict(files=len(body),sha256=hashlib.sha256("\n".join(body).encode()).hexdigest()))
split=load(T/"t38/split-t38-v1.json");cells=split["test"]
assert len(cells)==len(set(cells))==34
fixtures=[];total=0
for cell in cells:
 root=pathlib.Path("C:/RideBoundData/research/fixtures-panelA-v1")/cell
 scenario=load(root/"scenario-content.json")
 driver=load(T/("calib/panelA/drivers/"+cell+".driver.json"))
 world=load(T/("calib/panelA/worlds/W5-"+cell[:9]+"-"+cell[-3:]+".json"))
 files={n:digest(root/n) for n in ("derivative-manifest.json","normalization-report.json","selection-frame.json")}
 declared=driver["sourceScenarioContentSha256"]
 assert declared==inputs[str(root/"scenario-content.json")]["sha256"]
 window=scenario["timeWindow"];start=datetime.datetime.fromisoformat(window["sourceWindowStartUtc"].replace("Z","+00:00"))-datetime.timedelta(hours=5)
 ws={"w07":25200,"w08":28800,"w17":61200}[cell[-3:]]
 assert window["sourceTimezoneId"]=="America/New_York"
 assert start.date().isoformat()==world["base"]["day"]=="2018-11-"+cell[7:9]
 assert start.hour*3600+start.minute*60+start.second==world["base"]["windowStart"]==ws
 assert world["sigma"]==world["shockRate"]==0 and world["base"]["exponent"]==1
 counts=scenario["validationSummary"]; assert counts["requestCount"]==108 and counts["vehicleCount"]==8
 total+=counts["requestCount"]
 fixtures.append(dict(cell=cell,scenario_sha256=declared,counts=counts,window=window,world=world,other_sha256=files))
record("fixtures",dict(cells=len(cells),requests=total,windows=dict(collections.Counter(c[-3:] for c in cells)),details=fixtures))
a=load(H/"R15-audit.json")
records=[r for r in a["runs"] if r["pop"] in ("t38","w07") and r["arm"].startswith("C-")]
record("measured_C",dict(runs=len(records),decisions=sum(r["acknowledged"] for r in records),
 prunes=sum(sum(r["budget_candidates"].values()) for r in records),
 step_fails=sum(r["budget_candidates"].get("step-fails",0) for r in records),
 cumulative=sum(r["budget_candidates"].get("cumulative-reported",0) for r in records),
 repeated=sum(r["ledger"]["repeated"] for r in records)))
front={}
for g in a["groups"]:
 if g["pop"]=="t38":
  front[g["arm"]]={n:{**v,"late_percent":100*v["late60"]/v["served"],"extension_s":v["ext_sum_ms"]/v["served"]/1000,"timely60":v["served"]-v["late60"],"timely120":v["served"]-v["late120"],"early_percent":100*v["early60"]/v["served"]} for n,v in g["frontier"].items()}
record("frontier",front)
record("overlaps",a["overlaps"])
record("w07_ladder",[{k:g[k] for k in ("arm","requests","ledger","candidates")} for g in a["groups"] if g["pop"]=="w07"])
sf=load(H/"R17-screen-forecast-verification.json")
snow=sf["snow"];by=collections.defaultdict(list)
for r in snow:by[r["cell"]].append(r)
record("snow",dict(riders=len(snow),cells=len(by),best_fit=min(sf["fit_grid"]),
 naive_late60=sum(r["A"]-r["P0"]>60000 for r in snow),
 hist_late60=sum(r["A"]-r["D"]["HIST"]>60000 for r in snow),
 hist_cellmean_percent=sum(100*sum(r["A"]-r["D"]["HIST"]>60000 for r in rs)/len(rs) for rs in by.values())/len(by),
 hist_pooled_extension_s=sum(r["D"]["HIST"]-r["P0"] for r in snow)/len(snow)/1000,
 hist_cellmean_extension_s=sum(sum(r["D"]["HIST"]-r["P0"] for r in rs)/len(rs)/1000 for rs in by.values())/len(by)))
r18=load(H/"R18-verification.json")
record("R18_keys",list(r18))
record("time",datetime.datetime.now(datetime.timezone.utc).isoformat())
root=pathlib.Path("C:/RideBoundData/research/tier3-t38c120-v1");states=[]
for cell in cells:
 p=root/("C-120-"+cell);q=p/"summary.json"
 status="missing-directory" if not p.exists() else "no-summary"
 if q.exists():
  try:status=json.loads(q.read_text(encoding="utf-8"))["status"]
  except (ValueError,KeyError):status="unreadable-summary"
 states.append(dict(cell=cell,status=status))
record("completion_gate",dict(states=dict(collections.Counter(x["status"] for x in states)),ready=all(x["status"]=="pass" for x in states),details=states))
out["inputs"]=inputs
with (H/"R19-verification.json").open("x",encoding="utf-8") as f:json.dump(out,f,indent=2)
with (H/"R19-verification.txt").open("x",encoding="utf-8") as f:
 for k,v in out.items():
  if k=="inputs":continue
  if k=="fixtures":v={k:x for k,x in v.items() if k!="details"}
  f.write(k+" "+json.dumps(v,sort_keys=True)+"\n")