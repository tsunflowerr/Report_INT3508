import json, base64, sys, collections

path = sys.argv[1]
atypes = collections.Counter()
aexample = {}
certkeys = collections.Counter()
witness_example = None
nonnormal = 0
evtypes = collections.Counter()
evexample = {}
last_ckpt = None
with open(path, "r", encoding="utf-8") as f:
    for line in f:
        rec = json.loads(line)
        env = json.loads(base64.b64decode(rec["frameBase64"]))
        mt = env.get("messageType")
        d = rec["direction"]
        if d == "runnerToAdapter" and mt == "decision":
            p = env["payload"]
            for a in p["actions"]:
                atypes[a["decisionType"]] += 1
                if a["decisionType"] not in aexample or (a["decisionType"] == "vehiclePlanUpdated" and len(json.dumps(a)) > len(json.dumps(aexample[a["decisionType"]])) and len(json.dumps(a)) < 4000):
                    aexample[a["decisionType"]] = a
            body = p["certificate"]["body"]
            for k in body:
                certkeys[k] += 1
            if body.get("witnesses") and witness_example is None:
                witness_example = (env.get("simTimeMs"), body["witnesses"][:5], {k: v for k, v in body.items() if k != "witnesses"})
            if body.get("normalOperation") is False:
                nonnormal += 1
        if d == "adapterToRunner" and mt == "eventBatch":
            for e in env["payload"]["events"]:
                evtypes[e["eventType"]] += 1
                if e["eventType"] not in evexample and e["eventType"] != "travelTimesUpdated":
                    evexample[e["eventType"]] = e
        if d == "runnerToAdapter" and mt == "checkpoint":
            last_ckpt = env
print("action types", atypes)
for k, v in aexample.items():
    print(k, json.dumps(v)[:2500])
    print("--")
print("certkeys", certkeys)
print("nonnormal", nonnormal)
print("witness example", json.dumps(witness_example)[:3000])
print("event types", evtypes)
for k, v in evexample.items():
    print(k, json.dumps(v)[:1500])
os_ = last_ckpt["payload"]["content"]["onlineState"]
print("content keys", list(last_ckpt["payload"]["content"].keys()))
print("onlineState keys", list(os_.keys()))
for k, v in os_.items():
    if isinstance(v, list):
        print(k, "list len", len(v), json.dumps(v[0])[:2500] if v else None)
    else:
        print(k, json.dumps(v)[:300])
print("lifecycles", collections.Counter(r.get("lifecycle") for r in os_["requests"]))
