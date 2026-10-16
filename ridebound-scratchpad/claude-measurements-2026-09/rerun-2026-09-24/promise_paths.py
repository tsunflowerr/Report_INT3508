import base64, json, os, sys, time, pickle

def scan(path):
    """rider -> list of (simTimeMs, pickupEta, dropEta, dA_drop, dE_drop, dV_drop, dA_pick, dE_pick, dV_pick)"""
    riders = {}
    with open(path, encoding="utf-8") as h:
        for line in h:
            fr = json.loads(base64.b64decode(json.loads(line)["frameBase64"]))
            if fr.get("messageType") != "decision":
                continue
            t = fr.get("simTimeMs", 0)
            for a in fr["payload"].get("actions", []):
                if a["decisionType"] != "promisePublished":
                    continue
                p = a["payload"]
                pr = p["promise"]
                rid = pr["requestId"]
                dd = p["decisionDelta"]; ed = p["exogenousDelta"]; vd = p["visibleDelta"]
                riders.setdefault(rid, []).append((
                    t, pr["pickupEtaMs"], pr["dropEtaMs"],
                    dd["dropEtaTotalMs"], ed["dropEtaTotalMs"], vd["dropEtaTotalMs"],
                    dd["pickupEtaTotalMs"], ed["pickupEtaTotalMs"], vd["pickupEtaTotalMs"],
                ))
    return riders

if __name__ == "__main__":
    root = sys.argv[1]; pat = sys.argv[2]; out = sys.argv[3]
    cells = sorted(d for d in os.listdir(root) if pat in d)
    all_ = {}
    t0 = time.time()
    for i, c in enumerate(cells):
        p = os.path.join(root, c, "transcript-00.ndjson")
        if not os.path.exists(p):
            print("MISSING", c); continue
        all_[c] = scan(p)
        print(f"[{i+1}/{len(cells)}] {c}: {len(all_[c])} riders  ({time.time()-t0:.0f}s)", flush=True)
    with open(out, "wb") as h:
        pickle.dump(all_, h)
    print("wrote", out)
