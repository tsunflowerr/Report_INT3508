# Supplementary robustness checks (independent code). Writes supplementary-output.txt (mode "x").
# (a) Claim 6 under stricter sequence definitions: each fleet action tagged with its decision's simTimeMs,
#     and fleet actions grouped per acknowledged decision (empty groups kept).
# (b) Claim 5 means at full precision (recomputed from runs-extracted.json).
import base64
import hashlib
import json
import os
from multiprocessing import Pool

DATA = r"C:\RideBoundData\research\tier3-w07-v1"
OUT = os.path.dirname(os.path.abspath(__file__))
CELLS = ["d201811%d-s10-r%d-w07" % (d, r) for d in (12, 13) for r in (1, 2, 3, 4)]
PAIRS = [("Mplus-30", "C-30"), ("Mplus-60", "C-60"), ("Mplus-120", "C-120"), ("Mplus-300", "C-300"), ("V-30", "C-30")]
FLEET = {"vehiclePlanUpdated", "requestAccepted", "requestRejected"}


def canon(o):
    return json.dumps(o, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def strict(folder):
    acked = set()
    decs = []
    with open(os.path.join(DATA, folder, "transcript-00.ndjson"), "rb") as fh:
        for raw in fh:
            rec = json.loads(raw)
            env = json.loads(base64.b64decode(rec["frameBase64"]))
            mt = env.get("messageType")
            if rec["direction"] == "adapterToRunner" and mt == "decisionApplied":
                acked.add(env["payload"]["decisionHash"])
            elif rec["direction"] == "runnerToAdapter" and mt == "decision":
                decs.append((env["payload"]["decisionHash"], env.get("simTimeMs"), env["payload"].get("actions") or []))
    tagged = hashlib.sha256()
    grouped = hashlib.sha256()
    n_dec = 0
    for h, sim, acts in decs:
        if h not in acked:
            continue
        n_dec += 1
        fa = [canon(a) for a in acts if a.get("decisionType") in FLEET]
        for s in fa:
            tagged.update(("%s|%s\n" % (sim, s)).encode("utf-8"))
        grouped.update(("D%s[%s]\n" % (sim, "|".join(fa))).encode("utf-8"))
    return folder, tagged.hexdigest(), grouped.hexdigest(), n_dec


def main():
    folders = sorted({"%s-%s" % (a, c) for p in PAIRS for a in p for c in CELLS})
    with Pool(6) as pool:
        res = {f: (t, g, n) for f, t, g, n in pool.map(strict, folders, chunksize=1)}
    out = []
    for a, b in PAIRS:
        t_eq = [c[7:9] + "r" + c[15] for c in CELLS if res["%s-%s" % (a, c)][0] == res["%s-%s" % (b, c)][0]]
        g_eq = [c[7:9] + "r" + c[15] for c in CELLS if res["%s-%s" % (a, c)][1] == res["%s-%s" % (b, c)][1]]
        nd = ["%s:%d/%d" % (c[7:9] + "r" + c[15], res["%s-%s" % (a, c)][2], res["%s-%s" % (b, c)][2]) for c in CELLS]
        out.append("%s vs %s: time-tagged equal %d/8 %s; per-decision grouped equal %d/8 %s; acked decisions %s"
                   % (a, b, len(t_eq), t_eq, len(g_eq), g_eq, " ".join(nd)))
    D = json.load(open(os.path.join(OUT, "runs-extracted.json"), "r", encoding="utf-8"))["runs"]
    for arm, thr in (("Mplus-60", 60.0), ("Mplus-30", 30.0)):
        sh = []
        for c in CELLS:
            v = list(D["%s-%s" % (arm, c)]["a_r"].values())
            sh.append(sum(x > thr for x in v) / len(v))
        out.append("%s mean share(A_r > %.0f s) over 8 cells = %.6f" % (arm, thr, sum(sh) / len(sh)))
    txt = "\n".join(out) + "\n"
    print(txt)
    with open(os.path.join(OUT, "supplementary-output.txt"), "x", encoding="utf-8") as fh:
        fh.write(txt)


if __name__ == "__main__":
    main()
