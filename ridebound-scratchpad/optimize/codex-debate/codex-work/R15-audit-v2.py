"""Independent R15 audit: read existing transcripts; no simulation, build or external imports.
All outputs are exclusive-created beside this script. No existing file is modified.
"""
import base64,collections,concurrent.futures,csv,hashlib,json,pathlib,statistics
HERE=pathlib.Path(__file__).resolve().parent
MAIN=json.loads((HERE/"R13-raw-verification.json").read_text(encoding="utf-8"))
FACTOR=pathlib.Path("E:/RideBoundData/wp6/extracted/sha256/d9/d9e86f33645e5eec287d387f8d63ad41ddf41d4ef648138b65d636482e2c599e/FleetPy_Manhattan/networks/Manhattan_2019_corrected")
PROFILE={}
for day in ("2018-11-12","2018-11-13","2018-11-14"):
 for w,start in (("w07",25200),("w08",28800),("w17",61200)):
  rows=list(csv.DictReader((FACTOR/(day+"_tt_factors.csv")).open(encoding="utf-8")))
  f={int(r["simulation_time"]):float(r["travel_time_factor"]) for r in rows}
  PROFILE[day,w]=tuple(f[start+900*b] for b in range(9))
def quote(t,p,cell):
 day="2018-11-"+cell[7:9]
 sources=[d for d in ("2018-11-12","2018-11-13","2018-11-14") if d<day] if day in ("2018-11-14","2018-11-15","2018-11-16") else []
 if len(sources)<2 or p<=t:return float(p)
 profiles=[PROFILE[d,cell[-3:]] for d in sources]
 f=[sum(v[b] for v in profiles)/len(profiles) for b in range(9)]
 b0=int(t//900000);at=float(t);remaining=float(p-t)
 while remaining>0:
  b=int(at//900000);factor=1.0 if b==b0 else f[min(b,8)]/f[min(b0,8)]
  available=(b+1)*900000-at
  if available/factor>=remaining:
   at+=remaining*factor;break
  remaining-=available/factor;at=(b+1)*900000
 return max(float(p),at)
def jobs():
 out=[]
 for r in MAIN["runs"]:
  if (r["population"]=="t38" and r["arm"] in ("U","C-30")) or (r["population"]=="w07" and r["arm"].startswith("C-")):
   out.append(dict(pop=r["population"],arm=r["arm"],cell=r["cell"],path=r["transcript"]))
 for r in [r for r in MAIN["runs"] if r["population"]=="t38" and r["arm"]=="U"]:
  root=pathlib.Path("C:/RideBoundData/research/tier3-t38-v1")/("Mplus-30-"+r["cell"])
  if not (root/"summary.json").exists() and (root.parent/(root.name+"-rerun1")).exists():root=root.parent/(root.name+"-rerun1")
  out.append(dict(pop="t38",arm="Mplus-30",cell=r["cell"],path=str(root/"transcript-00.ndjson")))
 for arm,slug in (("C-30","c1-h6ref"),("C-60","c1-budget60"),("C-120","c1-budget120")):
  for p in sorted(pathlib.Path("E:/RideBoundData/wp14r/development-v6-ledger").glob("w14-*-"+slug+"-s7/attempt-01/output/transcript-00.ndjson")):
   out.append(dict(pop="fixed",arm=arm,cell=p.parents[2].name,path=str(p)))
 for p in sorted(pathlib.Path("E:/RideBoundData/research/tier3-sweep-v1").glob("C-120-*/transcript-00.ndjson")):
  out.append(dict(pop="synthetic",arm="C-120",cell=p.parent.name,path=str(p)))
 return out
def scan(job):
 final=None;manifest=None;acked=set();decisions={};obj=collections.Counter();alighted={};cumulative=[];frame_count=0;selection_fingerprint=hashlib.sha256()
 for line in pathlib.Path(job["path"]).open("rb"):
  if not line.strip():continue
  record=json.loads(line);raw=base64.b64decode(record["frameBase64"],validate=True)
  assert len(raw)==record["frameLengthBytes"] and hashlib.sha256(raw).hexdigest()==record["frameSha256"]
  frame_count+=1
  env=json.loads(raw);typ=env.get("messageType");p=env.get("payload",{})
  if typ=="initializeRun":manifest=p.get("manifest",p)
  if typ=="eventBatch":
   for e in p.get("events",[]):
    if e.get("eventType")=="passengerAlighted":alighted.setdefault(e["payload"]["requestId"],env["simTimeMs"])
  if typ=="decisionApplied":acked.add(p["decisionHash"])
  if typ=="checkpoint" and record["direction"]=="runnerToAdapter":final=p["content"]["onlineState"]
  if typ!="decision" or record["direction"]!="runnerToAdapter":continue
  h=p["decisionHash"];assert h not in decisions
  ev=(p.get("solver") or {}).get("executionEvidence",{})
  rows=[]
  for c in ev.get("prunedCandidates",[]):
   if c.get("code")!="COMMITMENT_BUDGET_EXCEEDED":continue
   ws=[w for w in c.get("commitmentWitnesses",[]) if w.get("code")=="COMMITMENT_BUDGET_EXCEEDED"]
   drop=[w for w in ws if w.get("dimension")=="drop_eta_total_ms"]
   if not drop:kind="other-budget" if ws else "missing-witness"
   elif any(w["delta"]>w["limit"] for w in drop):kind="step-fails"
   elif all(0<w["before"] and w["delta"]<=w["limit"]<w["after"] for w in drop):kind="cumulative-reported"
   else:kind="unclassified"
   for w in drop:assert w["before"]+w["delta"]==w["after"]
   rows.append(dict(kind=kind,candidate=c["candidateId"],new=c.get("newRequestIds",[]),witnesses=drop))
  decisions[h]=rows
  selection_fingerprint.update(json.dumps(p.get("actions"),sort_keys=True).encode())
  gen=ev.get("generation",{})
  obj["decision_frames"]+=1
  for v in gen.get("vehicleLosses",[]):
   obj["cap_applied"]+=bool(v.get("candidateCapApplied"))
   obj["omitted_by_cap"]+=v.get("omittedFeasibleCandidateCountByCap",0)
   obj["work_exhausted"]+=bool(v.get("workBudgetExhausted"))
  obj["omitted_requests"]+=gen.get("omittedRequestCount",0)
  if gen.get("consideredRequestCount",0)>0:
   obj["with_new"]+=1
   bounds=((ev.get("selection") or {}).get("finalSolverDiagnostics") or {}).get("objectiveBounds",[])
   for bound in bounds:
    if bound["objectiveName"]=="worst-hard-utilization-ppm":
     obj["util_present"]+=1
     obj["incumbent_1e6"]+=bound["incumbentValue"]==1000000
     obj["bound_1e6"]+=bound["bestBound"]==1000000
 assert final is not None and manifest is not None,job
 assert set(decisions)<=acked,(job["path"],"unacknowledged")
 life={r["requestId"]:r["lifecycle"] for r in final["requests"]}
 assert set(life.values())<=set(("completed","rejected")),job
 served={rid for rid,state in life.items() if state=="completed"}
 classes=collections.Counter();cum_decisions=0;cum_new=set()
 for h,rows in decisions.items():
  found=False
  for c in rows:
   classes[c["kind"]]+=1
   if c["kind"]=="cumulative-reported":
    found=True;cum_new.update(c["new"]);cumulative.append(dict(decision=h,**c))
  cum_decisions+=found
 stats=collections.Counter();front=collections.defaultdict(collections.Counter);complete_ids=[]
 for ledger in final["commitmentLedger"]:
  rid=ledger["requestId"];assert rid in served
  entries=ledger["entries"];assert entries[0]["kind"]=="initialPromise"
  cs=[e["publishedPromise"]["projection"]["dropEtaMs"]-e["exogenousProjection"]["dropEtaMs"] for e in entries[1:]]
  for e,c in zip(entries[1:],cs):assert abs(c)==e["deltas"]["decisionInduced"]["dropEtaTotalMs"]
  used=sum(map(abs,cs));stats["served"]+=1;stats["exposed"]+=used>0;stats["repeated"]+=sum(c!=0 for c in cs)>1
  stats["S_sum_exposed_ms"]+=used;stats["S_max_ms"]=max(stats["S_max_ms"],used)
  if job["arm"].startswith("C-"):
   cap=int(job["arm"][2:])*1000;assert used<=cap;stats["near90"]+=used>=.9*cap
  complete_ids.append(rid)
  if job["pop"]=="t38":
   assert rid in alighted,(job["path"],rid)
   initial=entries[0];t=initial["publishedPromise"]["publishedAtMs"];p0=initial["publishedPromise"]["projection"]["dropEtaMs"];a=alighted[rid]
   fc=quote(t,p0,job["cell"])
   for name,q in (("naive",p0),("fc",fc),("fc_pad30",fc+30000),("fc_pad60",fc+60000)):
    s=front[name];s["served"]+=1;s["late60"]+=a-q>60000;s["late120"]+=a-q>120000;s["late300"]+=a-q>300000;s["late600"]+=a-q>600000;s["early60"]+=a-q< -60000;s["ext_sum_ms"]+=q-p0
   stats["late60_and_exposed"]+=a-p0>60000 and used>0
 result={**job,"frames":frame_count,"requests":len(life),"acknowledged":len(decisions),"budget_candidates":dict(classes),"cum_decisions":cum_decisions,"cum_new":len(cum_new),"cum_finally_rejected":sum(life[r]=="rejected" for r in cum_new),"cumulative_witnesses":cumulative,"objective":dict(obj),"ledger":dict(stats),"frontier":{k:dict(v) for k,v in front.items()},"complete_ids":complete_ids,"action_fingerprint":selection_fingerprint.hexdigest(),"core_commit":manifest.get("coreCommitSha"),"policy":manifest.get("policyId")}
 return result
def main():
 plan=jobs();results=[]
 assert len(plan)==227,len(plan)
 with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
  for i,r in enumerate(pool.map(scan,plan),1):
   results.append(r)
   if i%8==0:print("Read and hash-checked existing transcripts",i,"/",len(plan),flush=True)
 groups=[]
 for pop,arm in sorted({(r["pop"],r["arm"]) for r in results}):
  rows=[r for r in results if (r["pop"],r["arm"])==(pop,arm)]
  candidates=collections.Counter();obj=collections.Counter();front=collections.defaultdict(collections.Counter);ledger=collections.Counter()
  for r in rows:
   candidates.update(r["budget_candidates"]);obj.update(r["objective"])
   for k,v in r["frontier"].items():front[k].update(v)
   for k,v in r["ledger"].items():
    if k=="S_max_ms":ledger[k]=max(ledger[k],v)
    else:ledger[k]+=v
  groups.append(dict(pop=pop,arm=arm,runs=len(rows),requests=sum(r["requests"] for r in rows),acknowledged=sum(r["acknowledged"] for r in rows),candidates=dict(candidates),cum_decisions=sum(r["cum_decisions"] for r in rows),cum_new=sum(r["cum_new"] for r in rows),cum_finally_rejected=sum(r["cum_finally_rejected"] for r in rows),objective=dict(obj),ledger=dict(ledger),frontier={k:dict(v) for k,v in front.items()}))
 sets={a:{(r["cell"],rid) for r in results if r["pop"]=="t38" and r["arm"]==a for rid in r["complete_ids"]} for a in ("U","C-30","Mplus-30")}
 overlaps=[dict(left=a,right=b,common=len(sets[a]&sets[b]),left_only=len(sets[a]-sets[b]),right_only=len(sets[b]-sets[a])) for a,b in (("U","C-30"),("C-30","Mplus-30"))]
 synthetic=[r for r in results if r["pop"]=="synthetic" and r["cum_decisions"]]
 original=next(r for r in synthetic if r["cell"]=="C-120-W4-d20181112-s10-r1-w08")
 rerun=next(r for r in synthetic if r["cell"]==original["cell"]+"-rerun1")
 duplicate_fields=("complete_ids","ledger","budget_candidates","cum_decisions","cum_new","cum_finally_rejected","action_fingerprint")
 duplicates={k:original[k]==rerun[k] for k in duplicate_fields}
 output=dict(scope="227 existing transcripts; independent witness classification and integration/counting; all frame hashes checked; no simulation/build/install",groups=groups,overlaps=overlaps,synthetic_duplicate=duplicates,runs=[{k:v for k,v in r.items() if k!="complete_ids"} for r in results])
 with (HERE/"R15-audit.json").open("x",encoding="utf-8",newline="\n") as f:json.dump(output,f,indent=2);f.write("\n")
 lines=["# R15 independent existing-transcript audit","No simulation/build/install. All outputs exclusive-created."]
 for g in groups:lines.append(json.dumps(g,sort_keys=True))
 lines.extend(json.dumps(o,sort_keys=True) for o in overlaps);lines.append("synthetic_duplicate "+json.dumps(duplicates,sort_keys=True))
 with (HERE/"R15-audit-summary.txt").open("x",encoding="utf-8",newline="\n") as f:f.write("\n".join(lines)+"\n")
 print("\n".join(lines),flush=True)
if __name__=="__main__":main()
