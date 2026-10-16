"""R17 independent narrow re-computation. Read-only inputs; one process.
Checks decoded-frame/file hashes against earlier Codex inventory where available.
Reconstructs Q2 requests/screens, snow quotations and R12 fit; sums saved metadata.
No simulation/build/install. Outputs exclusive-created under codex-work.
"""
import base64,collections,csv,hashlib,importlib.util,json,math,pathlib,re,statistics,sys
HERE=pathlib.Path(__file__).resolve().parent
C=HERE.parent/"claude-work";OPT=HERE.parents[2];ROOT=HERE.parents[3]
sys.path[:0]=[str(C/"r16-forecast"),str(OPT)]
import factor_nowcast_screen as fs
import factor_nowcast_screen_v2 as fsv2
import display_layer as dl
import promise_stretch as ps
inv=json.loads((HERE/"R13-raw-verification.json").read_text(encoding="utf-8"))["runs"]
idx={str(pathlib.Path(r["transcript"]).resolve()).lower():r for r in inv}
frames=0;reads=0
def read(p):
    global frames,reads
    ack=set();prunes=[];last=None;alights={};pubs={};actions={};dg=hashlib.sha256()
    with p.open("rb") as f:
        for line in f:
            dg.update(line)
            if not line.strip():continue
            row=json.loads(line);raw=base64.b64decode(row["frameBase64"],validate=True)
            assert hashlib.sha256(raw).hexdigest()==row["frameSha256"]
            assert len(raw)==row["frameLengthBytes"]
            frames+=1
            typ=re.search(rb'"messageType":"([^"]+)"',raw[:256]).group(1)
            if typ==b"decisionApplied":
                ack.add(json.loads(raw)["payload"]["decisionHash"])
            elif typ==b"decision":
                d=json.loads(raw)["payload"];h=d["decisionHash"]
                actions[h]=d["actions"]
                prunes += [(h,x) for x in ((d.get("solver") or {}).get("executionEvidence") or {}).get("prunedCandidates",[])
                            if x.get("code")=="COMMITMENT_BUDGET_EXCEEDED"]
            elif typ==b"eventBatch":
                e=json.loads(raw)
                for a in e["payload"].get("events",[]):
                    if a.get("eventType")=="passengerAlighted":alights[a["payload"]["requestId"]]=e["simTimeMs"]
            elif typ==b"checkpoint" and row["direction"]=="runnerToAdapter":last=raw
    state=json.loads(last)["payload"]["content"]["onlineState"]
    life={r["requestId"]:r["lifecycle"] for r in state["requests"]}
    riders={}
    for history in state["commitmentLedger"]:
        rid=history["requestId"];es=history["entries"];e=es[0];assert e["kind"]=="initialPromise"
        p0=e["publishedPromise"]["projection"]["dropEtaMs"]
        disp=sum(x["publishedPromise"]["projection"]["dropEtaMs"]-x["exogenousProjection"]["dropEtaMs"] for x in es[1:])
        if rid in alights:riders[rid]=dict(t0=e["publishedPromise"]["publishedAtMs"],P0=p0,A=alights[rid],dispatch=disp)
    known=idx.get(str(p.resolve()).lower())
    if known:assert dg.hexdigest()==known["sha256"]
    reads+=1
    return life,riders,[(h,x) for h,x in prunes if h in ack],state
jobs=[r for r in inv if (r["population"]=="t38" and r["arm"] in ("C-30","U"))
    or (r["population"]=="w07" and (r["arm"]=="U" or r["arm"].startswith("C-")))]
data={}
for n,r in enumerate(jobs):
    data[(r["population"],r["arm"],r["cell"])]=read(pathlib.Path(r["transcript"]))
    if n%16==0:print("Q2 inputs",n+1,"of",len(jobs),flush=True)
records=collections.defaultdict(collections.Counter);screen=collections.defaultdict(lambda:collections.Counter())
co_ids=collections.defaultdict(set);details=[]
BS=(60,90,120,150,180,240,300)
for (pop,arm,cell),(life,riders,prunes,state) in data.items():
    if not arm.startswith("C-"):continue
    touched={r for h,c in prunes for r in c["newRequestIds"]}
    records[(pop,arm)].update(records=len(prunes),decisions=len({h for h,c in prunes}),
        pairs=len(touched),completed=sum(life[r]=="completed" for r in touched),rejected=sum(life[r]=="rejected" for r in touched))
    if arm!="C-30":continue
    blocked=collections.defaultdict(list)
    for h,c in prunes:
        ws=[w for w in c["commitmentWitnesses"] if w["code"]=="COMMITMENT_BUDGET_EXCEEDED"]
        assert ws and all(w["dimension"]=="drop_eta_total_ms" for w in ws)
        for rid in c["newRequestIds"]:
            if life[rid]=="rejected":blocked[rid].append(ws)
    for b in BS:
        st=screen[(pop,b)]
        for rid,options in blocked.items():
            ok=[ws for ws in options if max(w["after"] for w in ws)<=b*1000]
            if not ok:continue
            ws=min(ok,key=lambda w:max(x["after"] for x in w));st["pass"]+=1
            for w in ws:
                co=w["requestId"];base=riders[co]["A"]-riders[co]["P0"];delta=w["delta"]
                co_ids[(pop,b)].add((cell,co));st["witness_occurrences"]+=1;st["delta_ms"]+=delta
                for k in (60,120,300):st["new_late"+str(k)]+=base<=k*1000<base+delta
            details.append(dict(pop=pop,B=b,cell=cell,new_request=rid,witnesses=ws))
idn=collections.Counter()
for (pop,arm,cell),(life,rs,pcs,_) in data.items():
    if pop!="w07" or arm!="C-30":continue
    lb=data[(pop,"C-120",cell)][0]
    idn["gained"]+=sum(l=="completed" and life[r]=="rejected" for r,l in lb.items())
    idn["lost"]+=sum(l!="completed" and life[r]=="completed" for r,l in lb.items())
# Independent R12 fit, explicit recursions and all 36 grid triples.
m={k:statistics.mean(fs.F[d][k] for d in ("2018-11-12","2018-11-13")) for k in range(96)}
fit=[]
for a in (.2,.5,.8,1.):
 for beta in (0.,.1,.3):
  for phi in (.8,.9,.98):
   loss=0;targets=0
   for day in ("2018-11-12","2018-11-13"):
    for start in (28,32,56,60,68):
     r=[math.log((fs.F[day][start+b]/fs.F[day][start])/(m[start+b]/m[start])) for b in range(9)]
     level=trend=0.
     for b in range(8):
      if b:
       prev=level;level=a*r[b]+(1-a)*(level+phi*trend)
       trend=beta*(level-prev)+(1-beta)*phi*trend
      loss+=(r[b+1]-(level+phi*trend))**2;targets+=1
   fit.append((loss,a,beta,phi,targets))
best=min(fit);assert best[:4]==fs.fit_dt()
params=best[1:4];methods=("NAIVE","HIST","BLEND-in","BLEND-pre","BLEND-L1","REGB-1.3","ORACLE")
snow=[];bycell=[];ledger=collections.Counter();tot=0;disp=0;hist=0
snow_root=pathlib.Path("C:/RideBoundData/research/tier3-forecast-v1")
paths=sorted(snow_root.glob("C-30-d20181115-*-w1[45]/transcript-00.ndjson"));assert len(paths)==8,len(paths)
for p in paths:
 life,rs,_,_=read(p);cell=p.parent.name;win=cell[-3:];start=fs.WIN[win]
 prof=dl.profile("2018-11-15",win,"causal-no15");mean=fs.mean_profile(fs.SRC["2018-11-15"])
 for rid,r in rs.items():
  b0=int(r["t0"]//900000)
  r["D"]={n:max(r["P0"],ps.stretch(r["t0"],r["P0"]-r["t0"],fsv2.weight(n,"2018-11-15",start,b0,mean,params))) for n in methods}
  assert abs(r["D"]["HIST"]-dl.display(r["t0"],r["P0"],prof))<.00001
  r.update(cell=cell,request=rid);snow.append(r)
  if r["A"]-r["P0"]>60000:
   tot+=(r["A"]-r["P0"])/1000;disp+=r["dispatch"]/1000
   for n in methods:ledger[n]+=max(0,min(r["D"][n]-r["P0"],r["A"]-r["P0"]-r["dispatch"]))/1000
 bycell.append({n:dict(late60=sum(r["A"]-r["D"][n]>60000 for r in rs.values()),
     ext_s=statistics.mean(r["D"][n]-r["P0"] for r in rs.values())/1000) for n in methods})
snowstat={n:dict(late60=sum(r["A"]-r["D"][n]>60000 for r in snow),
    mean_cell_extension_s=statistics.mean(c[n]["ext_s"] for c in bycell)) for n in methods}
# Saved monthly size sums, decimal GB; no mass network retrieval.
sizes={}
for name in ("tlc-yellow-sizes-2009-2015-2026-10-10.tsv","tlc-yellow-sizes-2016h1-2026-10-10.tsv"):
 for row in (C/"r16-forecast"/name).read_text().splitlines():
  date,n=row.split("\t");sizes[date]=int(n)
year_sizes={y:sum(n for d,n in sizes.items() if d.startswith(str(y))) for y in range(2009,2017)}
# Saved NOAA: first Central Park row mentioning snow on Nov15, not citywide onset.
with (C/"r16-forecast"/"noaa-lcd-centralpark-2018-11-15-16.csv").open(encoding="utf-8-sig") as f:wx=list(csv.DictReader(f))
wx_snow=[r for r in wx if r["DATE"].startswith("2018-11-15") and "SN" in r.get("HourlyPresentWeatherType","")]
first_wx=min(wx_snow,key=lambda r:r["DATE"])
# Recovery-b independent arithmetic from the saved run-level tables.
sw={ (r["arm"],r["world"],r["cell"]):r for r in csv.DictReader((ROOT/"tang3/sweep/sweep-jobs-2026-09-26.tsv").open(encoding="utf-8"),delimiter="\t")}
nw=[r for r in csv.DictReader((ROOT/"tang3/sweep/noworse-jobs-2026-09-26.tsv").open(encoding="utf-8"),delimiter="\t") if r["kind"]=="treatment"]
assert len(nw)==22
recovery=dict(treatments=len(nw),b=sum(int(r["M1_completed"]) for r in nw),
    a=sum(int(r["a_M1_completed"]) for r in nw),
    C=sum(int(sw[("C-"+r["level"],r["world"],r["cell"])]["M1_completed"]) for r in nw),
    equal=sum(int(r["M1_completed"])==int(sw[("C-"+r["level"],r["world"],r["cell"])]["M1_completed"]) for r in nw))
lines=["R17 independent screen/forecast arithmetic; single process."]
for key,r in sorted(records.items()):lines.append("RECORDS "+str(key)+" "+json.dumps(dict(r),sort_keys=True))
totrec=collections.Counter()
for r in records.values():totrec.update(r)
lines.append("RECORDS TOTAL "+json.dumps(dict(totrec),sort_keys=True))
for key,r in sorted(screen.items()):lines.append("SCREEN "+str(key)+" "+json.dumps(dict(r),sort_keys=True)+" unique_blocking_riders="+str(len(co_ids[key])))
lines+=["W07 IDENTITY B120 "+json.dumps(dict(idn)), "R12 FIT "+str(best),
 "SNOW "+json.dumps(snowstat,sort_keys=True),"SNOW LEDGER "+json.dumps(dict(total_s=tot,dispatch_s=disp,explained_s=dict(ledger)),sort_keys=True),
 "NOAA FIRST SNOW ROW "+json.dumps(first_wx,sort_keys=True),"SIZE BY YEAR bytes "+json.dumps(year_sizes,sort_keys=True),
 "RECOVERY table re-computation "+json.dumps(recovery,sort_keys=True),"INPUTS reads="+str(reads)+" verified_frames="+str(frames)]
with (HERE/"R17-screen-forecast-verification.txt").open("x",encoding="utf-8") as f:f.write("\n".join(lines)+"\n")
with (HERE/"R17-screen-forecast-verification.json").open("x",encoding="utf-8") as f:json.dump(dict(screen_details=details,snow=snow,fit_grid=fit),f,indent=2)
print("\n".join(lines),flush=True)

