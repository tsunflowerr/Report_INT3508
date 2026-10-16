import json, base64, sys, collections

path = sys.argv[1]
last_ckpt = None
dec_keys = collections.Counter()
reason = collections.Counter()
promise_keys = collections.Counter()
promise_null_drop = 0
applied_types = collections.Counter()
other_a2r = collections.Counter()
n = 0
with open(path, "r", encoding="utf-8") as f:
    for line in f:
        rec = json.loads(line)
        env = json.loads(base64.b64decode(rec["frameBase64"]))
        mt = env.get("messageType")
        d = rec["direction"]
        if d == "runnerToAdapter" and mt == "decision":
            p = env["payload"]
            for k in p:
                dec_keys[k] += 1
            if n == 0:
                print("decision payload non-action keys:", {k: v for k, v in p.items() if k not in ("actions", "certificate")})
                print("certificate keys:", list(p["certificate"].keys()))
            n += 1
            for a in p["actions"]:
                if a["decisionType"] == "promisePublished":
                    pp = a["payload"]
                    reason[pp.get("reasonCode")] += 1
                    for k in pp["promise"]:
                        promise_keys[k] += 1
                    if pp["promise"].get("dropEtaMs") is None:
                        promise_null_drop += 1
        if d == "adapterToRunner" and mt == "decisionApplied":
            applied_types[tuple(sorted(env["payload"].keys()))] += 1
        if d == "runnerToAdapter" and mt == "checkpoint":
            last_ckpt = env
print("decision payload keys", dec_keys)
print("reason codes", reason)
print("promise keys", promise_keys)
print("promise null drop", promise_null_drop)
print("decisionApplied payload keysets", applied_types)
os_ = last_ckpt["payload"]["content"]["onlineState"]
cl = os_["commitmentLedger"]
print("commitmentLedger item keys", collections.Counter(tuple(sorted(x.keys())) for x in cl))
e0 = cl[0]
print({k: (v if k != "entries" else len(v)) for k, v in e0.items()})
print("entry keys", collections.Counter(tuple(sorted(e.keys())) for x in cl for e in x["entries"]))
ent = cl[0]["entries"][-1]
print(json.dumps({k: v for k, v in ent.items() if k not in ("budgetAfter", "budgetBefore", "deltas")})[:3000])
il = os_["incidentLedger"]
print("incidentLedger keys", list(il.keys()), {k: len(v) if isinstance(v, list) else v for k, v in il.items()})
if il.get("breaches"):
    print(json.dumps(il["breaches"][0])[:2000])
