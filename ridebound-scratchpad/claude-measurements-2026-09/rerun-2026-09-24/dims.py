"""Per-rider decision-induced burden by ETA dimension on the sealed B1/C1 panel.

Question: the thesis table bang:taptrung reports B1 total 74,443 s and worst rider
840.9 s, while equity.py (drop dimension only) reports 64,863 s and 573.5 s.
Hypothesis to check: the table sums the pickup and drop dimensions.
Read-only.
"""
import base64
import collections
import json
import os

ROOT = r"E:/RideBoundData/wp9/confirmatory-h6-panela-v2"
for tag in ("-b1-tight-s7", "-c1-tight-s7"):
    pick = collections.Counter()
    drop = collections.Counter()
    moves = 0
    for cell in sorted(d for d in os.listdir(ROOT) if tag in d):
        path = os.path.join(ROOT, cell, "transcript-00.ndjson")
        with open(path, encoding="utf-8") as handle:
            for line in handle:
                frame = json.loads(base64.b64decode(json.loads(line)["frameBase64"]))
                if frame.get("messageType") != "decision":
                    continue
                for action in frame["payload"].get("actions", []):
                    if action["decisionType"] != "promisePublished":
                        continue
                    payload = action["payload"]
                    rider = (cell, payload["promise"]["requestId"])
                    delta = payload.get("decisionDelta") or {}
                    p = delta.get("pickupEtaTotalMs", 0)
                    d = delta.get("dropEtaTotalMs", 0)
                    pick[rider] += p
                    drop[rider] += d
                    if p or d:
                        moves += 1
    riders = set(pick) | set(drop)
    both = {r: pick[r] + drop[r] for r in riders}
    print(f"=== {tag} riders={len(riders)} publications-with-any-A={moves}")
    print(f"  total pickup A = {sum(pick.values())/1000:,.1f} s   max rider = {max(pick.values())/1000:,.1f} s")
    print(f"  total drop   A = {sum(drop.values())/1000:,.1f} s   max rider = {max(drop.values())/1000:,.1f} s")
    print(f"  total both     = {sum(both.values())/1000:,.1f} s   max rider = {max(both.values())/1000:,.1f} s")
    print(f"  riders with any A>0 = {sum(1 for v in both.values() if v > 0)}")
