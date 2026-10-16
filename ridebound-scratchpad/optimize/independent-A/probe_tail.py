"""Exploration probe: entries published at/after alight; W<=0 cases; dispatch parts (independent verifier)."""
import base64
import collections
import json
import sys

path = sys.argv[1]
last_cp = None
alights = collections.defaultdict(list)
with open(path, "r", encoding="utf-8") as fh:
    for line in fh:
        rec = json.loads(line)
        env = json.loads(base64.b64decode(rec["frameBase64"]))
        mt = env.get("messageType")
        if rec["direction"] == "runnerToAdapter" and mt == "checkpoint":
            last_cp = env
        if rec["direction"] == "adapterToRunner" and mt == "eventBatch":
            for ev in env["payload"]["events"]:
                if ev.get("eventType") == "passengerAlighted":
                    alights[ev["payload"]["requestId"]].append(env["simTimeMs"])

st = last_cp["payload"]["content"]["onlineState"]
led = st["commitmentLedger"]
c = collections.Counter()
for k, h in enumerate(led):
    es = h["entries"]
    A = alights[h["requestId"]][0] if h["requestId"] in alights else None
    for i, e in enumerate(es):
        t = e["publishedPromise"]["publishedAtMs"]
        p = e["publishedPromise"]["projection"]["dropEtaMs"]
        if p - t <= 0:
            c["W<=0"] += 1
            if A is not None and t >= A:
                c["W<=0 and t>=A"] += 1
        if A is not None and t >= A:
            c["t>=A"] += 1
            c[("t-A", t - A, "p-A", p - A, "isLast", i == len(es) - 1)] += 1
        if i > 0:
            ex = e["exogenousProjection"]["dropEtaMs"]
            if p != ex:
                c["revisions with p!=e"] += 1
    if k < 2:
        print("rider", k, "A", A, [(e["publishedPromise"]["publishedAtMs"], e["publishedPromise"]["projection"]["dropEtaMs"]) for e in es][:6], "...", [(e["publishedPromise"]["publishedAtMs"], e["publishedPromise"]["projection"]["dropEtaMs"]) for e in es][-3:])
for k, v in sorted(c.items(), key=lambda kv: str(kv[0]))[:40]:
    print(k, v)
print("checkpoint simTimeMs", last_cp["payload"]["content"]["simTimeMs"])
