from pathlib import Path
import base64, hashlib, json, collections, concurrent.futures
HERE=Path(__file__).resolve().parent
DATA=Path("E:/RideBoundData/wp14r/development-v6-ledger")
jobs=[]
for label,slug in [("C-120","c1-budget120"),("FREE","b1-ref")]:
 jobs += [("WP14r",label,p) for p in sorted(DATA.glob(f"w14-*-{slug}-s7/attempt-01/output/transcript-00.ndjson"))]
jobs += [("synthetic","C-120",p) for p in sorted(Path("E:/RideBoundData/research/tier3-sweep-v1").glob("C-120-*/transcript-00.ndjson"))]
def analyze(job):
 population,arm,path=job; final=None;hasher=hashlib.sha256();frames=0
 for line in path.open("rb"):
  hasher.update(line)
  if not line.strip():continue
  row=json.loads(line);frame=base64.b64decode(row["frameBase64"],validate=True)
  assert hashlib.sha256(frame).hexdigest()==row["frameSha256"]
  assert len(frame)==row["frameLengthBytes"]
  frames+=1
  if row["direction"]=="runnerToAdapter" and b'"checkpoint"' in frame[:2048]:
   env=json.loads(frame)
   if env["messageType"]=="checkpoint":final=env["payload"]["content"]["onlineState"]
 assert final is not None,path
 life=collections.Counter(r["lifecycle"] for r in final["requests"])
 assert not (set(life)-{"completed","rejected"}),(path,life)
 ledgers=final["commitmentLedger"];S=[];changes=[];xnonzero=0;singleok_cumfail=0;pickupexposed=0
 for h in ledgers:
  cs=[];ps=[]
  for e in h["entries"][1:]:
   p=e["publishedPromise"]["projection"];ex=e["exogenousProjection"];v=e["previousPromise"]["projection"]
   c=p["dropEtaMs"]-ex["dropEtaMs"];cp=p["pickupEtaMs"]-ex["pickupEtaMs"]
   assert abs(c)==e["deltas"]["decisionInduced"]["dropEtaTotalMs"]
   cs.append(c);ps.append(cp);xnonzero+=ex["dropEtaMs"]!=v["dropEtaMs"]
  S.append(sum(map(abs,cs)));changes.append(sum(c!=0 for c in cs));pickupexposed+=any(ps)
  singleok_cumfail+=bool(cs) and max(map(abs,cs))<=120000 and sum(map(abs,cs))>120000
 assert len(ledgers)==life["completed"]
 if arm=="C-120":assert max(S,default=0)<=120000
 return {"population":population,"arm":arm,"path":str(path),"sha256":hasher.hexdigest(),"verified_frames":frames,"requests":sum(life.values()),"served":life["completed"],"exposed":sum(s>0 for s in S),"two_or_more_changes":sum(n>=2 for n in changes),"max_changes":max(changes,default=0),"max_S_ms":max(S,default=0),"nonzero_traffic_entries":xnonzero,"pickup_exposed":pickupexposed,"single_step120_pass_cumulative120_fail":int(singleok_cumfail)}
records=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
 for i,row in enumerate(pool.map(analyze,jobs),1):
  records.append(row)
  if i%4==0:print("verified",i,"of",len(jobs),row["population"],row["arm"],flush=True)
totals=[]
for pop,arm in sorted(set((r["population"],r["arm"]) for r in records)):
 rows=[r for r in records if (r["population"],r["arm"])==(pop,arm)]
 totals.append({"population":pop,"arm":arm,"runs":len(rows),**{k:sum(r[k] for r in rows) for k in ["requests","served","exposed","two_or_more_changes","nonzero_traffic_entries","single_step120_pass_cumulative120_fail"]},"max_changes":max(r["max_changes"] for r in rows),"max_S_ms":max(r["max_S_ms"] for r in rows)})
result={"runs":records,"summary":totals,"verified_frames":sum(r["verified_frames"] for r in records)}
with (HERE/"R13-extra-raw-verification.json").open("x",encoding="utf-8") as f:json.dump(result,f,indent=2)
print(json.dumps(result["summary"]),flush=True)
