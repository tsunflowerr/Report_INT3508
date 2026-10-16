"""R17 audit of existing evidence only. Single process, no simulations/builds/installs.
Re-executes audited Claude selector; independently exhaustively enumerates the
C30 >30s fleet-sum case and derives per-rider movement from candidate route/schedule.
Outputs exclusive-created under this script's directory. Python -B.
"""
import base64,collections,hashlib,importlib.util,itertools,json,pathlib,re,statistics,sys,time
HERE=pathlib.Path(__file__).resolve().parent
E=HERE.parent/"claude-work"/"r16-evidence"
def module(name):
    p=E/(name+".py");sp=importlib.util.spec_from_file_location(name,p)
    m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
q=module("q4_cost_first_reselect")
lines=["R17 verification: audited-code re-execution, single process; independent special-case enumeration."]
results=[];t=time.monotonic()
for arm in q.ARMS:
    agg=collections.Counter();d=collections.Counter();rel=[];drops=[];cost=0
    paths=sorted(q.ROOT.glob("w14-*-"+arm+"-s7/attempt-01/output/transcript-00.ndjson"))
    assert len(paths)==16
    for n,p in enumerate(paths):
        a,path,c,delta,rr,ex,tc,dd=q.analyze((arm,p))
        agg.update(c);d.update(delta);rel+=rr;drops+=dd;cost+=tc
        print(arm,n+1,"of",len(paths),flush=True)
    ds=sorted(drops);rr=sorted(rel)
    r=dict(arm=arm,runs=len(paths),counts=dict(agg),deltas=dict(d),selected_plan_cost_sum=cost,
        mean_changed_frame_cost_saving_pct=100*statistics.mean(rr) if rr else None,
        upper_median_drop_s=ds[len(ds)//2] if ds else None,
        p90_drop_s=ds[int(.9*(len(ds)-1))] if ds else None,max_drop_s=max(ds) if ds else None)
    results.append(r);lines.append(json.dumps(r,sort_keys=True))
assert sum(r["counts"]["validation_match"] for r in results)==62837
assert not any(r["counts"].get("validation_mismatch",0) for r in results)
# Independent Cartesian enumeration with incremental request-exclusivity pruning.
def enum_solve(cp,use):
    lev=cp["selectionProblem"]["objectiveLevels"];vs=cp["selectionProblem"]["vehicleIds"]
    opts=[[c for c in cp["candidates"] if c["vehicleId"]==v and c["policyEligibility"]=="eligible"] for v in vs]
    best=None;leaves=0
    def visit(k,seen,chosen):
        nonlocal best,leaves
        if k==len(vs):
            leaves+=1;vec=[]
            for i in use:
                values=[c["objectiveContributions"][i] for c in chosen]
                val=max(values) if lev[i]["aggregation"]=="maximum" else sum(values)
                vec.append(val if lev[i]["sense"]=="minimize" else -val)
            key=tuple(vec)
            if best is None or key<best[0]:best=(key,tuple(c["candidateId"] for c in chosen))
            return
        for c in opts[k]:
            req=set(c["newRequestIds"])
            if not req & seen:visit(k+1,seen|req,chosen+[c])
    visit(0,set(),[])
    return best,leaves
special=[]
for p in sorted(q.ROOT.glob("w14-*-c1-h6ref-s7/attempt-01/output/transcript-00.ndjson")):
    for rawline in p.open("rb"):
        row=json.loads(rawline);raw=base64.b64decode(row["frameBase64"])
        if row["direction"]!="runnerToAdapter" or b'"candidatePortfolio"' not in raw:continue
        payload=json.loads(raw)["payload"];cp=payload["solver"]["executionEvidence"]["candidatePortfolio"]
        levels=[(lv["name"],lv["sense"],lv["aggregation"]) for lv in cp["selectionProblem"]["objectiveLevels"]]
        names=[lv[0] for lv in levels]
        if "revision:drop_eta_total_ms" not in names:continue
        vehicles=cp["selectionProblem"]["vehicleIds"];cands={v:[] for v in vehicles}
        byid={}
        for c in cp["candidates"]:
            if c["policyEligibility"]=="eligible":
                cands[c["vehicleId"]].append((c["candidateId"],frozenset(c["newRequestIds"]),c["objectiveContributions"]))
                byid[c["candidateId"]]=c
        use=[i for i,n in enumerate(names) if n in q.KEEP_COST_FIRST or n.startswith("candidate-id-rank:")]
        cf=q.solve(vehicles,cands,levels,use)
        ix=names.index("revision:drop_eta_total_ms")
        recorded=cp["selectedCandidateIds"]
        a=sum(byid[c]["objectiveContributions"][ix] for c in recorded)
        b=sum(byid[c]["objectiveContributions"][ix] for c in cf[1])
        if b-a<=30000:continue
        full,leaves=enum_solve(cp,list(range(len(levels))));cf2,leaves2=enum_solve(cp,use)
        assert set(full[1])==set(recorded) and set(cf2[1])==set(cf[1])
        case=dict(path=str(p),decisionHash=payload["decisionHash"],recorded_drop_ms=a,
            cf_drop_ms=b,extra_ms=b-a,enumerated_full_leaves=leaves,enumerated_cf_leaves=leaves2,
            cf_selected=[byid[c] for c in cf[1]],recorded_selected=[byid[c] for c in recorded])
        special.append(case)
assert len(special)==1
lines.append("SPECIAL C30 fleet-sum >30s: "+json.dumps({k:v for k,v in special[0].items() if not k.endswith("_selected")},sort_keys=True))
g=module("q4_free_gate_decomposition")
for arm in g.ARMS:
    counts=collections.Counter();sec=collections.Counter()
    for p in sorted(g.ROOT.glob("w14-*-"+arm+"-s7/attempt-01/output/transcript-00.ndjson")):
        a,c,s,n=g.analyze((arm,p));counts.update(c);sec.update(s)
    lines.append("GATE "+json.dumps(dict(arm=arm,counts=dict(counts),seconds=dict(sec)),sort_keys=True))
lines.append("elapsed_s="+str(round(time.monotonic()-t,1)))
body=dict(reselection=results,special=special)
with (HERE/"R17-portfolio-verification.json").open("x",encoding="utf-8") as f:json.dump(body,f,indent=2)
with (HERE/"R17-portfolio-verification.txt").open("x",encoding="utf-8") as f:f.write("\n".join(lines)+"\n")
print("\n".join(lines),flush=True)

