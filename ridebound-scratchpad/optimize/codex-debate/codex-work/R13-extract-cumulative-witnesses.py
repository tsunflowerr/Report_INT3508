from pathlib import Path
import json, base64, hashlib, re
HERE=Path(__file__).resolve().parent
data=json.loads((HERE/"R13-extra-raw-verification.json").read_text())
for r in data["runs"]:
 r["nonzero_exogenous_ledger_entries"]=r.pop("nonzero_traffic_entries")
for r in data["summary"]:
 r["nonzero_exogenous_ledger_entries"]=r.pop("nonzero_traffic_entries")
data["interpretation_note"]="Nonzero x entries are ledger projection differences, NOT proof of speed changes. WP14r is fixed traffic; previously verified sub-second negative x reflects timing/rounding. Counts of nonzero c include any millisecond."
with (HERE/"R13-extra-raw-verification-v2.json").open("x",encoding="utf-8") as f:json.dump(data,f,indent=2)
targets=[]
for population,arm,predicate in [("WP14r","C-120",lambda r:r["two_or_more_changes"]>0),("WP14r","FREE",lambda r:r["single_step120_pass_cumulative120_fail"]>0),("synthetic","C-120",lambda r:r["two_or_more_changes"]>0)]:
 targets.append(next(r for r in data["runs"] if r["population"]==population and r["arm"]==arm and predicate(r)))
witnesses=[]
for row in targets:
 path=Path(row["path"]);h=hashlib.sha256();final=None
 for line in path.open("rb"):
  h.update(line);outer=json.loads(line)
  if outer["direction"]=="runnerToAdapter":
   raw=base64.b64decode(outer["frameBase64"])
   if b'"checkpoint"' in raw[:2048]:
    env=json.loads(raw)
    if env["messageType"]=="checkpoint":final=env["payload"]["content"]["onlineState"]
 assert h.hexdigest()==row["sha256"]
 for hist in final["commitmentLedger"]:
  cs=[e["publishedPromise"]["projection"]["dropEtaMs"]-e["exogenousProjection"]["dropEtaMs"] for e in hist["entries"][1:]]
  cs=[c for c in cs if c]
  s=sum(map(abs,cs));step=max(map(abs,cs),default=0)
  if (row["arm"]=="C-120" and len(cs)>=2) or (row["arm"]=="FREE" and step<=120000<s):
   witnesses.append({"population":row["population"],"arm":row["arm"],"path":str(path),"sha256":row["sha256"],"request_id":hist["requestId"],"nonzero_signed_c_ms":cs,"S_ms":s,"max_step_ms":step})
with (HERE/"R13-cumulative-witnesses.json").open("x",encoding="utf-8") as f:json.dump(witnesses,f,indent=2)
print(json.dumps(witnesses),flush=True)
