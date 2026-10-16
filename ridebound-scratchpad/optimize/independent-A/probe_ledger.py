"""Exploration probe: ledger entry shapes, revision statistics, request fields (independent verifier)."""
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
reqs = {r["requestId"]: r for r in st["requests"]}
print("lifecycles:", collections.Counter(r["lifecycle"] for r in st["requests"]))
print("request keys union:", sorted(set(k for r in st["requests"] for k in r)))
done = [r for r in st["requests"] if r["lifecycle"] == "completed"]
if done:
    print("completed request example:", json.dumps(done[0])[:1500])

kinds = collections.Counter()
n_rev = 0
n_rev_drop_same = 0
n_rev_after_alight = 0
shown = False
for h in led:
    es = h["entries"]
    for i, e in enumerate(es):
        kinds[(i == 0, e["kind"])] += 1
        if i > 0:
            n_rev += 1
            if e["publishedPromise"]["projection"]["dropEtaMs"] == es[i - 1]["publishedPromise"]["projection"]["dropEtaMs"]:
                n_rev_drop_same += 1
            a = alights.get(h["requestId"])
            if a and e["publishedPromise"]["publishedAtMs"] >= a[0]:
                n_rev_after_alight += 1
            if not shown:
                shown = True
                slim = {k: v for k, v in e.items() if k not in ("budgetAfter", "budgetBefore")}
                print("revision example:", json.dumps(slim)[:4000])
print("entry kinds (is_first, kind):", dict(kinds))
print("revisions:", n_rev, "drop-unchanged revisions:", n_rev_drop_same, "revisions at/after first alight:", n_rev_after_alight)
print("multi-alight riders:", sum(1 for v in alights.values() if len(v) > 1))
print("ledger riders:", len(led), "alighted riders:", len(alights),
      "ledger riders alighted:", sum(1 for h in led if h["requestId"] in alights),
      "alighted not in ledger:", sum(1 for r in alights if r not in {h['requestId'] for h in led}))
print("initial entry publishedPromise keys:", list(led[0]["entries"][0]["publishedPromise"].keys()))
