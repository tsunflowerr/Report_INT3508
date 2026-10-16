from pathlib import Path
import base64,collections,concurrent.futures,csv,hashlib,json,math,statistics
HERE=Path(__file__).resolve().parent
SCRATCH=Path("E:/Code/Report_INT3508/ridebound-scratchpad")
ROOTS={"w07":Path("C:/RideBoundData/research/tier3-w07-v1"),"w07x":Path("C:/RideBoundData/research/tier3-w07x-v1"),"t38":Path("C:/RideBoundData/research/tier3-t38-v1")}
W07CELLS=[f"d201811{d}-s10-r{rep}-w07" for d in (12,13) for rep in range(1,5)]
TEST=json.loads((SCRATCH/"tang3/t38/split-t38-v1.json").read_text(encoding="utf-8"))["test"]
JOBS=[]
for arm in ["U","C-30","C-60","C-90","C-120","C-150","C-180","C-240","C-300"]:
    family="w07x" if arm in {"C-90","C-150","C-180","C-240"} else "w07"
    JOBS += [("w07",arm,cell,ROOTS[family]/f"{arm}-{cell}") for cell in W07CELLS]
for arm in ["Mplus-30","Mplus-60","Mplus-90","Mplus-120","Mplus-150","Mplus-180","Mplus-240"]:
    family="w07x" if arm in {"Mplus-90","Mplus-150","Mplus-180","Mplus-240"} else "w07"
    JOBS += [("w07",arm,cell,ROOTS[family]/f"{arm}-{cell}") for cell in W07CELLS]
for arm in ["U","C-30"]:
    for cell in TEST:
        folder=ROOTS["t38"]/f"{arm}-{cell}"
        if not (folder/"summary.json").is_file():folder=ROOTS["t38"]/f"{arm}-{cell}-rerun1"
        JOBS.append(("t38",arm,cell,folder))

def analyze(job):
    population,arm,cell,folder=job;path=folder/"transcript-00.ndjson"
    last=None;frames=decisions=forced=0;hasher=hashlib.sha256();manifest=None
    with path.open("rb") as stream:
        for rawline in stream:
            hasher.update(rawline)
            if not rawline.strip():continue
            row=json.loads(rawline);raw=base64.b64decode(row["frameBase64"],validate=True)
            assert hashlib.sha256(raw).hexdigest()==row["frameSha256"],(path,frames)
            frames+=1;e=json.loads(raw)
            if e.get("messageType")=="initializeRun":manifest=e["payload"]
            elif e.get("messageType")=="checkpoint" and row["direction"]=="runnerToAdapter":last=e["payload"]["content"]["onlineState"]
            elif e.get("messageType")=="decision":
                decisions+=1;forced+=not e["payload"]["certificate"]["body"]["normalOperation"]
    assert last is not None and manifest is not None,path
    requests={r["requestId"]:r for r in last["requests"]}
    ledgers=last["commitmentLedger"];ids=[r["requestId"] for r in ledgers];assert len(ids)==len(set(ids))
    riders=[]
    for h in ledgers:
        rid=h["requestId"];assert h["entries"] and h["entries"][0]["kind"]=="initialPromise"
        cs=[];ps=[];publications=set()
        for e in h["entries"]:
            assert e["publicationId"] not in publications;publications.add(e["publicationId"])
            if e["kind"]=="initialPromise":continue
            assert e["kind"]=="revision"
            pub=e["publishedPromise"]["projection"];ex=e["exogenousProjection"]
            c=pub["dropEtaMs"]-ex["dropEtaMs"];cp=pub["pickupEtaMs"]-ex["pickupEtaMs"]
            assert abs(c)==e["deltas"]["decisionInduced"]["dropEtaTotalMs"]
            assert abs(cp)==e["deltas"]["decisionInduced"]["pickupEtaTotalMs"]
            cs.append(c);ps.append(cp)
        riders.append({"population":population,"arm":arm,"cell":cell,"request_id":rid,"lifecycle":requests[rid]["lifecycle"],"S_drop_ms":sum(map(abs,cs)),"S_pickup_ms":sum(map(abs,ps)),"signed_drop_ms":sum(cs),"nonzero_drop_changes":sum(c!=0 for c in cs)})
    life=collections.Counter(r["lifecycle"] for r in requests.values());assert sum(life.values())==108
    assert all(r["lifecycle"] in {"completed","rejected"} for r in requests.values()),(path,life)
    assert len(riders)==life["completed"],(path,len(riders),life)
    row={"population":population,"arm":arm,"cell":cell,"folder":str(folder),"transcript":str(path),"sha256":hasher.hexdigest(),"verified_frames":frames,"requests":len(requests),"accepted_first_promises":len(riders),"completed":life["completed"],"decisions":decisions,"forced_decisions":forced,"forced_fraction":forced/decisions,"final_snapshot_version":last["travelTimes"]["version"],"initial_manifest_sha256":hashlib.sha256(json.dumps(manifest,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()}
    return row,riders

runs=[];riders=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
    for i,(run,rs) in enumerate(pool.map(analyze,JOBS),1):
        runs.append(run);riders.extend(rs)
        if i%8==0 or i==len(JOBS):print("verified",i,"of",len(JOBS),run["population"],run["arm"],flush=True)

summaries=[]
for population,arm in sorted(set((r["population"],r["arm"]) for r in riders)):
    rs=[r for r in riders if (r["population"],r["arm"])==(population,arm)];rr=[r for r in runs if (r["population"],r["arm"])==(population,arm)]
    vals=sorted(r["S_drop_ms"]/1000 for r in rs if r["S_drop_ms"]>0);n=len(rs)
    cap=None if not arm.startswith("C-") else int(arm[2:])
    nearest=lambda q:vals[math.ceil(q*len(vals))-1] if vals else None
    summaries.append({"population":population,"arm":arm,"runs":len(rr),"requests":sum(r["requests"] for r in rr),"riders":n,"exposed":len(vals),"exposed_percent":100*len(vals)/n,"S_exposed_mean_s":statistics.mean(vals) if vals else None,"S_exposed_median_conventional_s":statistics.median(vals) if vals else None,"S_exposed_p50_nearest_s":nearest(.5),"S_exposed_p90_nearest_s":nearest(.9),"S_exposed_max_s":max(vals,default=0),"at_least_90pct_cap":sum(r["S_drop_ms"]>=.9*cap*1000 for r in rs) if cap else None,"two_or_more_changes":sum(r["nonzero_drop_changes"]>=2 for r in rs),"max_changes":max(r["nonzero_drop_changes"] for r in rs),"pickup_exposed":sum(r["S_pickup_ms"]!=0 for r in rs),"forced_cell_mean_percent":100*statistics.mean(r["forced_fraction"] for r in rr),"over_cap":sum(r["S_drop_ms"]>cap*1000 for r in rs) if cap else None,"would_exceed_percent":{str(b):100*sum(r["S_drop_ms"]>b*1000 for r in rs)/n for b in [30,60,120,300]}})

comparisons=[]
def budget_vector(arm):return {(r["cell"],r["request_id"]):(r["S_drop_ms"],r["S_pickup_ms"],r["nonzero_drop_changes"]) for r in riders if r["population"]=="w07" and r["arm"]==arm}
for a,b in [("C-120","C-150"),("C-120","C-180"),("U","C-240"),("U","C-300")]:
    aa=budget_vector(a);bb=budget_vector(b);shared=set(aa)&set(bb)
    comparisons.append({"left":a,"right":b,"left_only":len(set(aa)-set(bb)),"right_only":len(set(bb)-set(aa)),"different_shared_vectors":sum(aa[k]!=bb[k] for k in shared),"exact_identity":aa==bb})
exists={"w07_C120_runs":sum(r["population"]=="w07" and r["arm"]=="C-120" for r in runs),"t38_C120_folders":len(list(ROOTS["t38"].glob("C-120-*"))),"synthetic_C120_transcripts":sum(1 for p in Path("E:/RideBoundData/research/tier3-sweep-v1").glob("C-120-*/transcript-00.ndjson"))}
result={"scope":"All metrics reconstructed from raw transcript final ledgers and requests; all frames SHA256 verified. No simulation/build.","runs":runs,"summaries":summaries,"budget_vector_identity":comparisons,"existence":exists,"total_verified_frames":sum(r["verified_frames"] for r in runs)}
with (HERE/"R13-raw-verification.json").open("x",encoding="utf-8",newline="\n") as out:json.dump(result,out,indent=2);out.write("\n")
with (HERE/"R13-rider-budget.tsv").open("x",encoding="utf-8",newline="") as out:
    writer=csv.DictWriter(out,fieldnames=list(riders[0]),delimiter="\t");writer.writeheader();writer.writerows(riders)
with (HERE/"R13-raw-verification.txt").open("x",encoding="utf-8",newline="\n") as out:
    out.write("# Independent Round 13 raw-transcript verification\n"+result["scope"]+"\n")
    out.write(f"Runs: {len(runs)}; verified frames: {result['total_verified_frames']}\n")
    for summary in summaries:out.write(json.dumps(summary)+"\n")
    for comparison in comparisons:out.write(json.dumps(comparison)+"\n")
    out.write(json.dumps(exists)+"\n")
print(json.dumps({"runs":len(runs),"frames":result["total_verified_frames"],"summaries":summaries,"identity":comparisons,"existence":exists}),flush=True)
