"""Independent Stage 1a reader. No simulator/library imports, builds, installs or job control.
Do NOT execute before all 34 sealed C120 runs finish. Writes exclusive-create outputs beside this script.
On execution the first action is an all-34 completion gate; no partial outcomes are read.
"""
from __future__ import annotations
import base64, collections, csv, datetime, hashlib, json, pathlib
H=pathlib.Path(__file__).resolve().parent
D=H.parent; S=D.parents[1]; T=S/"tang3"
C120=pathlib.Path("C:/RideBoundData/research/tier3-t38c120-v1")
OLD=pathlib.Path("C:/RideBoundData/research/tier3-t38-v1")
FACTORS=pathlib.Path("E:/RideBoundData/wp6/extracted/sha256/d9/d9e86f33645e5eec287d387f8d63ad41ddf41d4ef648138b65d636482e2c599e/FleetPy_Manhattan/networks/Manhattan_2019_corrected")
EXPECTED_PLAN="cb6da66288b6d3b4a96271b27fc7047843c4e35f260f02ce4c559672bc6fd046"
EXPECTED_SPLIT="b72ac0f731fa7425891f364f0976054ae172a3117a507155ebe7e5c122ea03f1"
EXPECTED_INVENTORY="0da63eaf2b30ab332fba265a6b2b6e5c36b3ee78950cbac6d6267e60f81e4cbe"
EXPECTED_BINARY="a631038b6ea4850ffa29be2d5e4058fba2e57b725ee568075686d7a43c6f5fac"
EXPECTED_CORE="1ce15e92d2c1459d4254bbbcd581529197257fb2"
OUT_JSON=H/"R19-stage1a-analysis.json"
OUT_MD=H/"R19-stage1a-analysis.md"
INPUTS={}
class EvidenceError(RuntimeError):pass
def require(ok,why):
 if not ok:raise EvidenceError(why)
def read_json(p,expected=None):
 p=pathlib.Path(p);b=p.read_bytes();sha=hashlib.sha256(b).hexdigest()
 if expected:require(sha==expected,"input hash changed: "+str(p))
 INPUTS[str(p)]=dict(sha256=sha,bytes=len(b))
 return json.loads(b.decode("utf-8-sig"))
def completion_gate(cells):
 issues=[]
 for cell in cells:
  root=C120/("C-120-"+cell);p=root/"summary.json"
  if not p.is_file():issues.append((cell,"missing summary"));continue
  try:summary=read_json(p)
  except (ValueError,OSError):issues.append((cell,"unreadable summary"));continue
  if summary.get("status")!="pass":issues.append((cell,"summary status "+str(summary.get("status"))))
  if summary.get("repeatCount")!=1:issues.append((cell,"repeatCount is not 1"))
  for name in ("run-00.json","transcript-00.ndjson"):
   q=root/name
   if not q.is_file() or q.stat().st_size==0:issues.append((cell,"missing/empty "+name))
 if issues:
  raise EvidenceError("NOT READY: no outcomes extracted and no output written; "+json.dumps(issues))
def factors():
 result={}
 for day in ("2018-11-12","2018-11-13","2018-11-14"):
  p=FACTORS/(day+"_tt_factors.csv");b=p.read_bytes()
  INPUTS[str(p)]=dict(sha256=hashlib.sha256(b).hexdigest(),bytes=len(b))
  rows=list(csv.DictReader(b.decode("utf-8-sig").splitlines()))
  values={int(r["simulation_time"]):float(r["travel_time_factor"]) for r in rows}
  require(len(values)==96 and all(x>0 for x in values.values()),"invalid historical factor file")
  result[day]=values
 return result
def forecast(t,p,cell,f):
 day="2018-11-"+cell[7:9]
 src=[d for d in ("2018-11-12","2018-11-13","2018-11-14") if d<day] if day in ("2018-11-14","2018-11-15","2018-11-16") else []
 if len(src)<2 or p<=t:return float(p)
 start={"w07":25200,"w08":28800,"w17":61200}[cell[-3:]]
 profile=[sum(f[d][start+b*900] for d in src)/len(src) for b in range(9)]
 b0=int(t//900000);clock=float(t);work=float(p-t)
 for _ in range(10000):
  bin_=int(clock//900000)
  weight=1.0 if bin_==b0 else profile[min(bin_,8)]/profile[min(b0,8)]
  capacity=((bin_+1)*900000-clock)/weight
  if capacity>=work:return max(float(p),clock+work*weight)
  work-=capacity;clock=(bin_+1)*900000
 raise EvidenceError("forecast integration failed to converge")
def read_run(arm,cell,f,old_index):
 root=(C120 if arm=="C-120" else OLD)/(arm+"-"+cell)
 summary=read_json(root/"summary.json");run=read_json(root/"run-00.json")
 require(summary["status"]=="pass" and summary["repeatCount"]==1,"invalid summary: "+str(root))
 require(run.get("status")=="succeeded","run status: "+str(root))
 require(summary["repositoryInventorySha256"]==EXPECTED_INVENTORY,"cwd inventory mismatch")
 require(summary["sourceScenarioContentSha256"]==FIXTURE_HASHES[cell],"source fixture mismatch")
 require(run["semantic"]["requestCount"]==108,"semantic request count mismatch")
 p=root/"transcript-00.ndjson";before=p.stat()
 whole=hashlib.sha256();frames=0;last_ordinal=None;manifest=None;state=None
 decisions={};acks=set();alights={};first_quotes={};checkpoint_digest=None
 with p.open("rb") as handle:
  for line in handle:
   whole.update(line)
   if not line.strip():continue
   record=json.loads(line);ordinal=record["ordinal"]
   require(last_ordinal is None or ordinal>last_ordinal,"non-increasing transcript ordinal")
   last_ordinal=ordinal
   raw=base64.b64decode(record["frameBase64"],validate=True)
   require(len(raw)==record["frameLengthBytes"],"frame length mismatch")
   require(hashlib.sha256(raw).hexdigest()==record["frameSha256"],"frame digest mismatch")
   frames+=1;e=json.loads(raw);typ=e.get("messageType");v=e.get("payload",{})
   if typ=="initializeRun" and record["direction"]=="adapterToRunner":
    require(manifest is None,"duplicate initializeRun");manifest=v["manifest"]
   if typ=="eventBatch" and record["direction"]=="adapterToRunner":
    for event in v.get("events",[]):
     if event.get("eventType")=="passengerAlighted":
      rid=event["payload"]["requestId"]
      require(rid not in alights,"duplicate alight "+rid);alights[rid]=e["simTimeMs"]
   if typ=="decisionApplied" and record["direction"]=="adapterToRunner":
    require(v["decisionHash"] not in acks,"duplicate acknowledgement");acks.add(v["decisionHash"])
   if typ=="checkpoint" and record["direction"]=="runnerToAdapter":
    state=v["content"]["onlineState"];checkpoint_digest=record["frameSha256"]
   if typ!="decision" or record["direction"]!="runnerToAdapter":continue
   h=v["decisionHash"];require(h not in decisions,"duplicate decision")
   normal=(v.get("certificate",{}).get("body") or {}).get("normalOperation")
   require(isinstance(normal,bool),"missing normalOperation evidence")
   solver=v.get("solver") or {};ev=solver.get("executionEvidence") or {}
   require("prunedCandidates" in ev,"missing prune collection")
   pub={}
   for action in v.get("actions",[]):
    if action.get("decisionType")=="promisePublished":
     a=action["payload"];pid=a["publicationId"];require(pid not in pub,"duplicate publication");pub[pid]=a
   decisions[h]=dict(normal=normal,prunes=ev["prunedCandidates"],publications=pub,status=v.get("status"),reason=v.get("reasonCode"))
 require(manifest is not None and state is not None,"no initializeRun or terminal checkpoint")
 require(set(decisions)==acks,"decision/acknowledgement set mismatch")
 after=p.stat();require((before.st_size,before.st_mtime_ns)==(after.st_size,after.st_mtime_ns),"transcript changed during read")
 sha=whole.hexdigest()
 if arm!="C-120":
  known=old_index.get((arm,cell));require(known is not None and sha==known["sha256"],"archived transcript digest changed")
 INPUTS[str(p)]=dict(bytes=before.st_size,sha256=sha,frames=frames)
 require(manifest["masterSeed"]==7 and manifest["policyId"]=="ridebound-hard-vector","seed/policy mismatch")
 require(manifest["binarySha256"]==EXPECTED_BINARY and manifest["coreCommitSha"]==EXPECTED_CORE,"runner binary/core mismatch")
 require(manifest["policyVersion"]=="tier3-exploratory-v1","runner configuration version mismatch")
 requests={r["requestId"]:r for r in state["requests"]}
 require(len(requests)==len(state["requests"])==108,"checkpoint request identities/count mismatch")
 require(all(r["lifecycle"] in ("completed","rejected") for r in requests.values()),"unfinished request at final checkpoint")
 served={rid for rid,r in requests.items() if r["lifecycle"]=="completed"}
 require(set(alights)==served,"completed/alighted population mismatch")
 publications={}
 for d in decisions.values():
  for pid,a in d["publications"].items():
   require(pid not in publications,"duplicate publication across decisions");publications[pid]=a
 histories={h["requestId"]:h for h in state["commitmentLedger"]}
 require(len(histories)==len(state["commitmentLedger"]),"duplicate ledger history")
 require(set(histories)==served,"ledger/served population mismatch")
 riders=[];metrics=collections.Counter();fr={n:collections.Counter() for n in ("naive","causal-no15")}
 overshoots=[];max_used=0
 for rid in sorted(histories):
  es=histories[rid]["entries"];require(es and es[0]["kind"]=="initialPromise","missing first promise")
  signed=[];spent=0
  for i,en in enumerate(es):
   a=publications.get(en["publicationId"]);require(a is not None,"ledger publication is not acknowledged")
   projection=en["publishedPromise"]["projection"]
   require(a["promise"]==projection,"publication/ledger promise mismatch")
   c=0 if i==0 else projection["dropEtaMs"]-en["exogenousProjection"]["dropEtaMs"]
   require(abs(c)==en["deltas"]["decisionInduced"]["dropEtaTotalMs"],"signed/absolute ledger delta mismatch")
   require(en["budgetBefore"]["dropEtaTotalMs"]==spent,"ledger cumulative before mismatch")
   spent+=abs(c)
   require(en["budgetAfter"]["dropEtaTotalMs"]==spent,"ledger cumulative after mismatch")
   if i:signed.append(c)
  t=es[0]["publishedPromise"]["publishedAtMs"];p0=es[0]["publishedPromise"]["projection"]["dropEtaMs"];arrival=alights[rid]
  q=forecast(t,p0,cell,f);nonzero=sum(c!=0 for c in signed)
  metrics["drop_exposed"]+=spent>0;metrics["two_or_more_nonzero_changes"]+=nonzero>=2
  max_used=max(max_used,spent)
  if arm.startswith("C-") and spent>int(arm[2:])*1000:overshoots.append(dict(request=rid,used_ms=spent,cap_ms=int(arm[2:])*1000))
  for name,quote in (("naive",p0),("causal-no15",q)):
   z=fr[name];z["served"]+=1;z["quote_extension_sum_ms"]+=quote-p0
   for threshold in (60,120,300):
    late=arrival-quote>threshold*1000;z["late"+str(threshold)]+=late;z["timely"+str(threshold)]+=not late
   z["early60"]+=arrival-quote< -60000
  metrics["naive_late60_and_drop_exposed"]+=arrival-p0>60000 and spent>0
  riders.append(dict(request=rid,t0=t,P0=p0,arrival=arrival,forecast_quote=q,absolute_dispatch_ms=spent,nonzero_changes=nonzero))
 kinds=collections.Counter();cumulative=[];cum_decisions=set()
 for h,d in decisions.items():
  for candidate in d["prunes"]:
   if candidate.get("code")!="COMMITMENT_BUDGET_EXCEEDED":continue
   ws=[w for w in candidate.get("commitmentWitnesses",[]) if w.get("code")=="COMMITMENT_BUDGET_EXCEEDED"]
   drop=[w for w in ws if w.get("dimension")=="drop_eta_total_ms"]
   for w in drop:
    require(w["before"]>=0 and w["delta"]>=0 and w["before"]+w["delta"]==w["after"],"inconsistent prune witness arithmetic")
    require(w["after"]>w["limit"],"budget witness does not exceed limit")
    if arm=="C-120":require(w["limit"]==120000,"unexpected C120 witness limit")
   if not ws:kind="missing-witness"
   elif not drop:kind="other-budget"
   elif any(w["delta"]>w["limit"] for w in drop):kind="single-increment-fails"
   elif all(0<w["before"] and w["delta"]<=w["limit"]<w["after"] for w in drop):kind="cumulative-only-reported"
   else:kind="unclassified"
   kinds[kind]+=1
   if kind=="cumulative-only-reported":
    cum_decisions.add(h)
    new=candidate.get("newRequestIds",[])
    cumulative.append(dict(decision=h,candidate=candidate["candidateId"],witnesses=drop,new_requests=new,final_lifecycles={r:requests[r]["lifecycle"] for r in new}))
 for z in fr.values():
  z["timely60_per_requests"]=z["timely60"]/108;z["timely120_per_requests"]=z["timely120"]/108
  z["mean_quote_extension_s"]=z["quote_extension_sum_ms"]/len(served)/1000 if served else None
  z["late60_percent_served"]=100*z["late60"]/len(served) if served else None
 return dict(arm=arm,cell=cell,requests=108,served=len(served),served_ids=sorted(served),
 frames=frames,transcript_sha256=sha,checkpoint_frame_sha256=checkpoint_digest,manifest=manifest,
 acknowledged_decisions=len(acks),non_normal_decisions=sum(not d["normal"] for d in decisions.values()),
 decision_statuses=dict(collections.Counter(d["status"] for d in decisions.values())),
 incident_breach_entries=dict(collections.Counter(b["kind"] for b in state["incidentLedger"].get("breaches",[]))),
 ledger=dict(metrics),max_absolute_dispatch_ms=max_used,overshoots=overshoots,
 frontier={n:dict(v) for n,v in fr.items()},prune_classes=dict(kinds),
 cumulative_only_records=cumulative,cumulative_only_decisions=len(cum_decisions),riders=riders)
def aggregate(rows):
 z=dict(runs=len(rows),requests=sum(r["requests"] for r in rows),served=sum(r["served"] for r in rows),
 acknowledged_decisions=sum(r["acknowledged_decisions"] for r in rows),
 non_normal_decisions=sum(r["non_normal_decisions"] for r in rows),
 absolute_dispatch_overshoot_riders=sum(len(r["overshoots"]) for r in rows),
 max_absolute_dispatch_ms=max(r["max_absolute_dispatch_ms"] for r in rows),
 drop_exposed=sum(r["ledger"].get("drop_exposed",0) for r in rows),
 two_or_more_nonzero_changes=sum(r["ledger"].get("two_or_more_nonzero_changes",0) for r in rows),
 cumulative_only_records=sum(len(r["cumulative_only_records"]) for r in rows),
 cumulative_only_decisions=sum(r["cumulative_only_decisions"] for r in rows))
 pc=collections.Counter()
 for r in rows:pc.update(r["prune_classes"])
 z["prune_classes"]=dict(pc);z["frontier"]={}
 for name in ("naive","causal-no15"):
  v={k:sum(r["frontier"][name].get(k,0) for r in rows) for k in ("served","late60","late120","late300","timely60","timely120","timely300","early60","quote_extension_sum_ms")}
  for n in (60,120):v["timely"+str(n)+"_per_3672"]=v["timely"+str(n)]/3672
  v["late60_percent_served"]=100*v["late60"]/z["served"]
  v["mean_quote_extension_s"]=v["quote_extension_sum_ms"]/z["served"]/1000
  z["frontier"][name]=v
 return z
def main():
 global FIXTURE_HASHES
 split=read_json(T/"t38/split-t38-v1.json",EXPECTED_SPLIT);cells=split["test"]
 require(len(cells)==len(set(cells))==34,"not the sealed 34 cells")
 completion_gate(cells)
 require(not OUT_JSON.exists() and not OUT_MD.exists(),"output exists; exclusive-create refuses to overwrite")
 design=read_json(H/"R19-verification.json")
 for name,stamp in design["inputs"].items():
  p=pathlib.Path(name)
  if p.is_relative_to(T) or p.is_relative_to(pathlib.Path("C:/RideBoundData/research/fixtures-panelA-v1")) or p.is_relative_to(pathlib.Path("C:/RideBoundData/research/runner-tier3-v2")):
   require(hashlib.sha256(p.read_bytes()).hexdigest()==stamp["sha256"],"design input changed: "+name)
 require(hashlib.sha256((T/"t38c120/C120-PLAN.md").read_bytes()).hexdigest()==EXPECTED_PLAN,"plan changed")
 FIXTURE_HASHES={x["cell"]:x["scenario_sha256"] for x in design["fixtures"]["details"]}
 inventory=read_json(H/"R13-raw-verification.json")
 old_index={(r["arm"],r["cell"]):r for r in inventory["runs"] if r["population"]=="t38" and r["arm"] in ("U","C-30")}
 f=factors();rows=[]
 for arm in ("C-120","C-30","U"):
  for i,cell in enumerate(cells,1):
   rows.append(read_run(arm,cell,f,old_index))
   if i%8==0 or i==34:print(arm+" independently read "+str(i)+"/34",flush=True)
 totals={a:aggregate([r for r in rows if r["arm"]==a]) for a in ("C-120","C-30","U")}
 for arm,values in (("C-30",(2338,76,11,2262,2327,10,0)),("U",(2434,203,102,2231,2332,137,87))):
  a=totals[arm];n=a["frontier"]["naive"];fc=a["frontier"]["causal-no15"]
  require((a["served"],n["late60"],n["late120"],n["timely60"],n["timely120"],fc["late60"],fc["late120"])==values,"baseline reconstruction mismatch")
 sets={a:{(r["cell"],rid) for r in rows if r["arm"]==a for rid in r["served_ids"]} for a in totals}
 overlaps=[dict(left=a,right=b,common=len(sets[a]&sets[b]),left_only=len(sets[a]-sets[b]),right_only=len(sets[b]-sets[a])) for a,b in (("C-120","C-30"),("C-120","U"),("C-30","U"))]
 require((overlaps[2]["common"],overlaps[2]["left_only"],overlaps[2]["right_only"])==(2207,131,227),"baseline overlap mismatch")
 for cell in cells:
  m=[r for r in rows if r["cell"]==cell]
  require(len({r["manifest"]["binarySha256"] for r in m})==1,"cell binary mismatch")
 require(len({r["manifest"]["policyConfigurationHash"] for r in rows if r["arm"]=="C-120"})==1,"C120 policy hashes differ")
 a=totals["C-120"];n=a["frontier"]["naive"]
 unknown=sum(a["prune_classes"].get(k,0) for k in ("missing-witness","other-budget","unclassified"))
 predictions={"P1":dict(pass_=a["non_normal_decisions"]==0 and a["absolute_dispatch_overshoot_riders"]==0,all_summaries_pass=True,non_normal=a["non_normal_decisions"],overshoots=a["absolute_dispatch_overshoot_riders"]),
 "P2":dict(pass_=a["served"]>=2362,value=a["served"],threshold=2362),
 "P3":dict(pass_=76<n["late60"]<203,value=n["late60"],strict_bounds=[76,203]),
 "P4":dict(pass_=n["timely120"]>=2327,value=n["timely120"],threshold=2327),
 "P5":dict(pass_=(a["cumulative_only_records"]<=2 if unknown==0 else None),value=a["cumulative_only_records"],threshold=2,unclassified_or_other_budget=unknown)}
 result=dict(time_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),scope="102 completed archived/new runs; independent stdlib transcript reader and historical-factor integrator",totals=totals,overlaps=overlaps,predictions=predictions,runs=rows,inputs=INPUTS,limitations=["forecast is frozen display replay, no redispatch","recorded fail-fast witnesses do not enumerate all blockers or counterfactual routes","model projection attribution is not complete real-world causal identification","34 cells are dependent across five dates; no population guarantee","non-normal decisions are certificate counts; incident entries are reported separately"])
 text=["# R19 independent Stage 1a results","",result["time_utc"],"",json.dumps(predictions,indent=2),"","| Arm | Served | Forced/non-normal | Overshoot riders | Drop-exposed | >=2 changes | Recorded cumulative-only |","|---|---:|---:|---:|---:|---:|---:|"]
 for arm,v in totals.items():text.append("| "+arm+" | "+" | ".join(str(v[k]) for k in ("served","non_normal_decisions","absolute_dispatch_overshoot_riders","drop_exposed","two_or_more_nonzero_changes","cumulative_only_records"))+" |")
 text+=["","| Arm / quote | Late>60 | Late>120 | Late>300 | Timely60 / 3672 | Timely120 / 3672 | Mean extension s | Early>60 |","|---|---:|---:|---:|---:|---:|---:|---:|"]
 for arm,v in totals.items():
  for name,q in v["frontier"].items():text.append("| "+arm+" / "+name+" | "+" | ".join(str(q[k]) for k in ("late60","late120","late300"))+" | "+str(q["timely60"])+"/3672 | "+str(q["timely120"])+"/3672 | "+str(q["mean_quote_extension_s"])+" | "+str(q["early60"])+" |")
 text+=["","Served-set overlaps: "+json.dumps(overlaps),"",*result["limitations"]]
 with OUT_JSON.open("x",encoding="utf-8",newline="\n") as handle:json.dump(result,handle,indent=2);handle.write("\n")
 with OUT_MD.open("x",encoding="utf-8",newline="\n") as handle:handle.write("\n".join(text)+"\n")
 print("Analysis complete; exclusive-created "+OUT_JSON.name+" and "+OUT_MD.name,flush=True)
if __name__=="__main__":
 try:main()
 except (EvidenceError,ValueError,KeyError,OSError) as error:
  raise SystemExit(str(error))
