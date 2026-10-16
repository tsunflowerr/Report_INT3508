"""Sign split of the held-route component x on the sealed B1/C1 panel (drop dimension).

On a publication with decision delta A == 0 the decision component is zero, so the signed
visible change z = p_t - p_{t-1} equals x_t. Publications with A > 0 are counted apart (their
sign split needs signcheck.py). Also prints total |x| from exogenousDelta for cross-check
against thesis ch3 (6,719,286 ms B1; 6,694,740 ms C1). Read-only.
"""
import base64
import json
import os

ROOT = r"E:/RideBoundData/wp9/confirmatory-h6-panela-v2"
for tag in ("-b1-tight-s7", "-c1-tight-s7"):
    previous = {}
    positive = negative = 0
    n_pos = n_neg = n_zero = 0
    with_a = 0
    total_abs_x = 0
    for cell in sorted(d for d in os.listdir(ROOT) if tag in d):
        with open(os.path.join(ROOT, cell, "transcript-00.ndjson"), encoding="utf-8") as handle:
            for line in handle:
                frame = json.loads(base64.b64decode(json.loads(line)["frameBase64"]))
                if frame.get("messageType") != "decision":
                    continue
                for action in frame["payload"].get("actions", []):
                    if action["decisionType"] != "promisePublished":
                        continue
                    payload = action["payload"]
                    rider = (cell, payload["promise"]["requestId"])
                    p = payload["promise"]["dropEtaMs"]
                    a = payload["decisionDelta"]["dropEtaTotalMs"]
                    total_abs_x += payload["exogenousDelta"]["dropEtaTotalMs"]
                    v = previous.get(rider)
                    previous[rider] = p
                    if v is None:
                        continue
                    if a != 0:
                        with_a += 1
                        continue
                    z = p - v
                    if z > 0:
                        positive += z
                        n_pos += 1
                    elif z < 0:
                        negative += -z
                        n_neg += 1
                    else:
                        n_zero += 1
    print(f"=== {tag}")
    print(f"  total |x| from exogenousDelta = {total_abs_x:,} ms")
    print(f"  publications with A == 0: x>0 {n_pos}, x<0 {n_neg}, x==0 {n_zero}; with A>0 (excluded) {with_a}")
    print(f"  sum x+ = {positive/1000:,.1f} s   sum x- = {negative/1000:,.1f} s")
