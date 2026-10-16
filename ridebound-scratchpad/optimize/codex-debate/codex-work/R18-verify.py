"""R18 confirmation arithmetic on existing audit data and archived checkpoint tails.
One process; no simulation, build, install, row download, or imported repository modules.
Only mode-x outputs beside this script; preserves all existing inputs.
"""
from __future__ import annotations
import base64, collections, csv, datetime as dt, hashlib, json, pathlib, re, statistics

H=pathlib.Path(__file__).resolve().parent
D=H.parent; S=D.parents[1]; C=D/"claude-work"
result={}; inputs={}
def read(p):
 p=pathlib.Path(p); b=p.read_bytes()
 inputs[str(p)]=dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
 return b.decode("utf-8-sig")
def load(p):return json.loads(read(p))
def record(k,v):
 result[k]=v
 print(k+" "+json.dumps(v,ensure_ascii=True,sort_keys=True),flush=True)

a=load(H/"R15-audit.json"); runs=a["runs"]
measured=[r for r in runs if r["pop"] in ("t38","w07") and r["arm"].startswith("C-")]
record("measured_C",dict(runs=len(measured),acknowledged=sum(r["acknowledged"] for r in measured),
 records=sum(sum(r["budget_candidates"].values()) for r in measured),
 step_fails=sum(r["budget_candidates"].get("step-fails",0) for r in measured),
 cumulative_only=sum(r["budget_candidates"].get("cumulative-reported",0) for r in measured),
 repeated=sum(r["ledger"]["repeated"] for r in measured),
 by_arm={str(k):dict(runs=len(v),records=sum(sum(r["budget_candidates"].values()) for r in v))
 for k,v in ((key,[r for r in measured if (r["pop"],r["arm"])==key])
 for key in sorted({(r["pop"],r["arm"]) for r in measured}))}))
t38={}
for arm in ("U","C-30","Mplus-30"):
 rs=[r for r in runs if r["pop"]=="t38" and r["arm"]==arm]
 fr={}
 for name in ("naive","fc","fc_pad30","fc_pad60"):
  n=sum(r["frontier"][name]["served"] for r in rs)
  fr[name]=dict(served=n,late60=sum(r["frontier"][name]["late60"] for r in rs),
   late120=sum(r["frontier"][name]["late120"] for r in rs),
   early60=sum(r["frontier"][name]["early60"] for r in rs),
   extension_seconds=sum(r["frontier"][name]["ext_sum_ms"] for r in rs)/n/1000)
  fr[name]["timely60"]=n-fr[name]["late60"];fr[name]["timely120"]=n-fr[name]["late120"]
  fr[name]["early60_percent"]=100*fr[name]["early60"]/n
 t38[arm]=dict(runs=len(rs),requests=sum(r["requests"] for r in rs),frontier=fr,
  exposed=sum(r["ledger"]["exposed"] for r in rs),
  repeated=sum(r["ledger"]["repeated"] for r in rs),
  late60_exposed=sum(r["ledger"]["late60_and_exposed"] for r in rs),
  S_max_ms=max(r["ledger"]["S_max_ms"] for r in rs),
  util_incumbent=sum(r["objective"]["incumbent_1e6"] for r in rs),
  util_bound=sum(r["objective"]["bound_1e6"] for r in rs),
  util_present=sum(r["objective"]["util_present"] for r in rs))
record("T38_from_prior_independent_audit",t38)
record("served_overlaps_saved",a["overlaps"])
sign=collections.Counter()
for cell in sorted({r["cell"] for r in runs if r["pop"]=="t38"}):
 rs={r["arm"]:r for r in runs if r["pop"]=="t38" and r["cell"]==cell}
 d=rs["U"]["frontier"]["naive"]["late60"]-rs["C-30"]["frontier"]["naive"]["late60"]
 sign[cell[-3:]+(" positive" if d>0 else " zero" if d==0 else " negative")]+=1
record("T38_late60_cell_signs",dict(sign))
# Arithmetic on independent R17 detailed snow records, not a new forecast fit.
sf=load(H/"R17-screen-forecast-verification.json"); snow=sf["snow"]
methods=list(snow[0]["D"]); late=[r for r in snow if r["A"]-r["P0"]>60000]
total=sum((r["A"]-r["P0"])/1000 for r in late)
dispatch=sum(r["dispatch"]/1000 for r in late)
explained={m:sum(max(0,min(r["D"][m]-r["P0"],r["A"]-r["P0"]-r["dispatch"]))/1000 for r in late) for m in methods}
record("snow",dict(riders=len(snow),naive_late60=len(late),
 late60={m:sum(r["A"]-r["D"][m]>60000 for r in snow) for m in methods},
 HIST_pooled_pct=100*sum(r["A"]-r["D"]["HIST"]>60000 for r in snow)/len(snow),
 total_seconds=total,dispatch_seconds=dispatch,explained_seconds=explained,
 extra_prefix_seconds=explained["BLEND-pre"]-explained["HIST"],
 extra_prefix_percent=100*(explained["BLEND-pre"]-explained["HIST"])/total,
 residual_prefix_seconds=total-dispatch-explained["BLEND-pre"],
 residual_prefix_percent=100*(total-dispatch-explained["BLEND-pre"])/total,
 best_R12_grid=min(sf["fit_grid"])))
pv=load(H/"R17-portfolio-verification.json")
# Saved independent summary rows: re-derive percentages with explicit denominators.
ps=[]
for line in read(H/"R17-portfolio-verification.txt").splitlines():
 if line.startswith("{"):
  x=json.loads(line);z=x["counts"]
  if "cost_first_differs" in z:
   ps.append(dict(arm=x["arm"],frames=z["frames"],new_frames=z["with_new_request"],
    matches=z["validation_match"],changed=z["cost_first_differs"],
    changed_pct=100*z["cost_first_differs"]/z["with_new_request"],
    conditional_mean_saving_pct=x["mean_changed_frame_cost_saving_pct"],
    mean_pct_saving_per_new_frame=x["mean_changed_frame_cost_saving_pct"]*z["cost_first_differs"]/z["with_new_request"],
    ratio_of_summed_plan_cost_pct=-100*x["deltas"]["operational-cost"]/x["selected_plan_cost_sum"],
    summed_cost_saving=-x["deltas"]["operational-cost"],summed_selected_plan_cost=x["selected_plan_cost_sum"],
    accepted_changes=z["accepted_changes"]))
record("cost_first_denominators",ps)
record("portfolio_total_matches",sum(json.loads(l)["counts"]["validation_match"] for l in
 read(H/"R17-portfolio-verification.txt").splitlines() if l.startswith("{")))
case=load(H/"R17-C30-sum-case.txt")
record("C30_special_case",dict(decision=case["decisionHash"],
 per_rider_ms=[r["after"]-r["before"] for r in case["per_rider"]],
 sum_ms=sum(r["after"]-r["before"] for r in case["per_rider"])))
# Independent weather date selection/grouping, station labels only.
wx=list(csv.DictReader(read(C/"r13-ml-data-samples/noaa_ghcnd_centralpark_2014-2020.csv").splitlines()))
def snow_mm(r):return float(r["SNOW"] or 0)
def spells(ds):
 out=[]
 for d in sorted(ds):
  if not out or (d-out[-1][-1]).days>2:out.append([d])
  else:out[-1].append(d)
 return [[str(d) for d in x] for x in out]
test_dates=[dt.date.fromisoformat(r["DATE"]) for r in wx if "2018-09-01"<=r["DATE"]<="2019-12-31" and snow_mm(r)>=25.4]
record("test_snow25_spells",spells(test_dates))
wx13=list(csv.DictReader(read(C/"r16-forecast/noaa-ghcnd-centralpark-2009-2013.csv").splitlines()))
days13=[r for r in wx13 if r["DATE"].startswith("2013") and dt.date.fromisoformat(r["DATE"]).weekday()<5]
fa=[];d=dt.date(2013,1,14)
while len(fa)<10:
 if d.weekday()<4:fa.append(d)
 d+=dt.timedelta(days=1)
index13={r["DATE"]:r for r in wx13}
record("weather2013",dict(snow1_weekdays=[r["DATE"] for r in days13 if snow_mm(r)>=25.4],
 snow3_weekdays=[r["DATE"] for r in days13 if snow_mm(r)>=76.2],
 FAM_ten_MonThu_dates={str(d):dict(SNOW=index13[str(d)]["SNOW"],PRCP=index13[str(d)]["PRCP"]) for d in fa}))
# Config identities and differences on disk.
config=S/"tang3/configs"; bench=pathlib.Path("C:/Code/RideBound-noworse/benchmarks/configurations")
def differences(x,y,where=""):
 if isinstance(x,dict) and isinstance(y,dict):
  return [z for k in sorted(set(x)|set(y)) for z in (
   [dict(path=where+"/"+k,left=x.get(k,"<absent>"),right=y.get(k,"<absent>"))] if k not in x or k not in y
   else differences(x[k],y[k],where+"/"+k))]
 if isinstance(x,list) and isinstance(y,list) and len(x)==len(y):
  return [z for i,(xx,yy) in enumerate(zip(x,y)) for z in differences(xx,yy,where+"/"+str(i))]
 return [] if x==y else [dict(path=where,left=x,right=y)]
configs={}
for name,bname in (("U","wp14-c1-nobudget-v1"),("C-30","wp14-c1-h6-reference-v1"),
 ("C-60","wp14-c1-budget60-v1"),("C-120","wp14-c1-budget120-v1")):
 p=config/(name+".json");q=bench/(bname+".json");read(p);read(q)
 configs[name]=dict(sha256=inputs[str(p)]["sha256"],WP14_sha256=inputs[str(q)]["sha256"],
 byte_identical=inputs[str(p)]["sha256"]==inputs[str(q)]["sha256"])
record("commitment_config_identity",configs)
record("U_C30_config_diff",differences(load(config/"U.json"),load(config/"C-30.json")))
record("runner_config_diff",differences(load(config/"wp4-tier3-v2.json"),load(bench/"wp14-development-ridebound-hard-vector-v1.json")))
tex=pathlib.Path("E:/Code/Report_INT3508/ridebound/noi-dung")
texts={p.name:read(p) for p in sorted(tex.glob("*.tex"))}
pats={"HZ":r"(?i)H[öo?]rl|Zwick|000561639|Traffic uncertainty in on-demand",
 "T38_numbers":r"T3\.8|2[., ]338|2[., ]434"}
record("thesis_search",dict(files=len(texts),bibitems=len(re.findall(r"\\bibitem",texts["10-tai-lieu.tex"])),
 **{tag:[dict(file=f,line=i,text=l) for f,s in texts.items() for i,l in enumerate(s.splitlines(),1) if re.search(pat,l)]
 for tag,pat in pats.items()}))
record("thesis_files_mtime_not_build_proof",{str(p):dt.datetime.fromtimestamp(p.stat().st_mtime,dt.timezone.utc).isoformat()
 for p in [tex/"02-tom-tat.tex",tex/"05-chuong1.tex",tex/"08-chuong4.tex",tex/"09-chuong5.tex",tex.parent/"main.pdf"]})
record("archived_paths",dict(runner_exists=pathlib.Path("C:/RideBoundData/research/runner-tier3-v2").is_dir(),
 fixture_directory_count=len(list(pathlib.Path("C:/RideBoundData/research/fixtures-panelA-v1").glob("d*"))),
 driver_json_count=len(list((S/"tang3/calib/panelA/drivers").glob("*.json")))))
# Re-decode all 34 Mplus terminal checkpoint tails, verifying message type, byte length, and SHA.
counts=collections.Counter();complete_sets={};core=collections.Counter();per=[]
mrs=[r for r in runs if r["pop"]=="t38" and r["arm"]=="Mplus-30"]
for i,r in enumerate(mrs):
 p=pathlib.Path(r["path"])
 with p.open("rb") as f:
  offset=max(0,p.stat().st_size-64_000_000);f.seek(offset)
  if offset:f.readline()
  lines=f.readlines()
 state=None;envelope=None
 for line in reversed(lines):
  e=json.loads(line)
  if e["direction"]!="runnerToAdapter":continue
  raw=base64.b64decode(e["frameBase64"],validate=True)
  if re.search(rb'"messageType"\s*:\s*"checkpoint"',raw[:256]):
   assert len(raw)==e["frameLengthBytes"]
   assert hashlib.sha256(raw).hexdigest()==e["frameSha256"]
   state=json.loads(raw)["payload"]["content"]["onlineState"];envelope=e;break
 assert state is not None
 ctr=collections.Counter(x["kind"] for x in state["incidentLedger"]["breaches"])
 counts.update(ctr);served={x["requestId"] for x in state["requests"] if x["lifecycle"]=="completed"}
 complete_sets[r["cell"]]=sorted(served)
 per.append(dict(cell=r["cell"],served=len(served),counts=dict(ctr),checkpoint_sha256=envelope["frameSha256"],ordinal=envelope["ordinal"]))
 with p.open("rb") as f:
  for line in f:
   e=json.loads(line);raw=base64.b64decode(e["frameBase64"])
   obj=json.loads(raw)
   if obj["messageType"]=="initializeRun":
    manifest=obj["payload"]["manifest"];core[manifest.get("coreCommit","<missing>")]+=1;break
 if (i+1)%8==0:print("checkpoint progress "+str(i+1),flush=True)
record("Mplus34_raw_checkpoints",dict(runs=len(per),served=sum(p["served"] for p in per),breach_entries=dict(counts),per_cell=per))
# Jobs and statistical endpoint identities (pure arithmetic).
record("jobs",dict(stage1a=34,stage1b=4+2+68,stage1=34+4+2+68,stage2=68+2+2,
 all_stages=34+4+2+68+68+2+2,original_R17=170+4+4,
 historical_wall_hours_stage1=108*15/6/60,historical_wall_hours_stage2=72*15/6/60))
record("primary_identity",dict(baseline_SF_late_gap=203-76,baseline_SF_served_gap=2434-2338,
 baseline_SF_timely60_gap_naive=2231-2262,
 meaning="DiD(late counts)=DiD(served counts)-DiD(timely counts); rejection/composition must be reported."))
# This is not a transcript rescan: identify immutable inputs to all arithmetic above.
result["inputs"]=inputs
for name in ("R18-verification.json","R18-verification.txt"):
 assert not (H/name).exists(),name
with (H/"R18-verification.json").open("x",encoding="utf-8") as f:json.dump(result,f,ensure_ascii=False,indent=2)
with (H/"R18-verification.txt").open("x",encoding="utf-8") as f:
 for k,v in result.items():
  if k!="inputs":f.write(k+" "+json.dumps(v,ensure_ascii=False,sort_keys=True)+"\n")
print("done: exclusive-created R18-verification.json and R18-verification.txt",flush=True)
