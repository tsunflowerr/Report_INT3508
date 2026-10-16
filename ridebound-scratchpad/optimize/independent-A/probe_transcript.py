"""Exploration probe: summarise the structure of one transcript (independent verifier, Family A)."""
import base64
import collections
import json
import sys

path = sys.argv[1]
counts = collections.Counter()
last_cp = None
first_batch = None
alight_example = None
event_types = collections.Counter()
with open(path, "r", encoding="utf-8") as fh:
    for line in fh:
        rec = json.loads(line)
        env = json.loads(base64.b64decode(rec["frameBase64"]))
        mt = env.get("messageType")
        counts[(rec["direction"], mt)] += 1
        if rec["direction"] == "runnerToAdapter" and mt == "checkpoint":
            last_cp = env
        if rec["direction"] == "adapterToRunner" and mt == "eventBatch":
            evs = env.get("payload", {}).get("events", [])
            for ev in evs:
                event_types[ev.get("eventType")] += 1
                if ev.get("eventType") == "passengerAlighted" and alight_example is None:
                    alight_example = (env.get("simTimeMs"), ev)
            if first_batch is None:
                first_batch = env

print("record keys:", list(rec.keys()))
for k, v in sorted(counts.items(), key=lambda kv: str(kv[0])):
    print(k, v)
print("event types:", dict(event_types))
print("alight example:", json.dumps(alight_example)[:800])
print("first batch keys:", list(first_batch.keys()), "payload keys:", list(first_batch["payload"].keys()))
print("last checkpoint envelope keys:", list(last_cp.keys()), "simTimeMs", last_cp.get("simTimeMs"))
pl = last_cp["payload"]
print("checkpoint payload keys:", list(pl.keys()))
content = pl.get("content", {})
print("content keys:", list(content.keys()))
st = content.get("onlineState", {})
print("onlineState keys:", list(st.keys()))
led = st.get("commitmentLedger")
print("ledger len:", len(led))
print("ledger[0]:", json.dumps(led[0])[:3000])
reqs = st.get("requests")
print("requests type:", type(reqs).__name__, "len", len(reqs))
print("request[0]:", json.dumps(reqs[0] if isinstance(reqs, list) else next(iter(reqs.items())))[:1500])
