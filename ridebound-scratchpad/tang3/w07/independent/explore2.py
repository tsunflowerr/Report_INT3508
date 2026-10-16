# Independent exploration 2: action types, event types, non-normal certificate example.
import base64, json, sys, collections

path = sys.argv[1]
dtypes = collections.Counter()
etypes = collections.Counter()
dex = {}
eex = {}
nonnormal_ex = None
nonnormal_n = 0
acks = 0
dec_n = 0
with open(path, "r", encoding="utf-8") as fh:
    for line in fh:
        rec = json.loads(line)
        env = json.loads(base64.b64decode(rec["frameBase64"]))
        mt = env.get("messageType")
        if rec["direction"] == "runnerToAdapter" and mt == "decision":
            dec_n += 1
            p = env["payload"]
            for a in p.get("actions", []):
                dtypes[a["decisionType"]] += 1
                if a["decisionType"] not in dex:
                    dex[a["decisionType"]] = a
            body = (p.get("certificate") or {}).get("body") or {}
            if body.get("normalOperation") is False:
                nonnormal_n += 1
                if nonnormal_ex is None:
                    nonnormal_ex = {"certificate": p.get("certificate"), "status": p.get("status"), "reasonCode": p.get("reasonCode"), "simTimeMs": env.get("simTimeMs")}
            if "normalOperation" not in body:
                print("decision without normalOperation:", p.get("status"), p.get("reasonCode"), list((p.get("certificate") or {}).keys()))
        if rec["direction"] == "adapterToRunner" and mt == "eventBatch":
            for e in env["payload"]["events"]:
                etypes[e["eventType"]] += 1
                if e["eventType"] not in eex and e["eventType"] != "travelTimesUpdated":
                    eex[e["eventType"]] = e
        if rec["direction"] == "adapterToRunner" and mt == "decisionApplied":
            acks += 1
print("decisions", dec_n, "acks", acks, "nonnormal", nonnormal_n)
print(dtypes)
print(etypes)
for k, v in dex.items():
    print("== action", k)
    print(json.dumps(v, indent=1)[:3000])
for k, v in eex.items():
    print("== event", k)
    print(json.dumps(v, indent=1)[:1500])
print("== nonnormal example")
print(json.dumps(nonnormal_ex, indent=1)[:5000])
