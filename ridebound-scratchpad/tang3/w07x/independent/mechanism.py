"""Independent check of claim 7 (mechanism at level 90, cell d20181112-s10-r1-w07)."""
import base64
import json
import os
import sys

NEW_ROOT = r"C:\RideBoundData\research\tier3-w07x-v1"
FLEET = {"vehiclePlanUpdated", "requestAccepted", "requestRejected", "requestDeferred"}
CELL = sys.argv[1] if len(sys.argv) > 1 else "d20181112-s10-r1-w07"
LEVEL = sys.argv[2] if len(sys.argv) > 2 else "90"
HERE = os.path.dirname(os.path.abspath(__file__))
out = []


def P(*a):
    s = " ".join(str(x) for x in a)
    out.append(s)
    print(s)


def canon(o):
    return json.dumps(o, sort_keys=True, separators=(",", ":"))


def load(arm):
    folder = os.path.join(NEW_ROOT, "%s-%s" % (arm, CELL))
    if not os.path.exists(folder):
        folder = os.path.join(r"C:\RideBoundData\research\tier3-w07-v1", "%s-%s" % (arm, CELL))
    P("reading", folder)
    decs, acked, ckpt = [], set(), None
    with open(os.path.join(folder, "transcript-00.ndjson"), "r", encoding="utf-8") as f:
        for line in f:
            rec = json.loads(line)
            env = json.loads(base64.b64decode(rec["frameBase64"]))
            mt = env.get("messageType")
            if rec["direction"] == "runnerToAdapter" and mt == "decision":
                decs.append(env)
            elif rec["direction"] == "adapterToRunner" and mt == "decisionApplied":
                acked.add(env["payload"]["decisionHash"])
            elif rec["direction"] == "runnerToAdapter" and mt == "checkpoint":
                ckpt = env
    decs = [d for d in decs if d["payload"]["decisionHash"] in acked]
    return decs, ckpt


def fleet(d):
    return [{"decisionType": a["decisionType"], "payload": a["payload"]} for a in d["payload"]["actions"] if a["decisionType"] in FLEET]


def brief(a):
    p = a["payload"]
    if a["decisionType"] == "vehiclePlanUpdated":
        return "%s %s %s" % (a["decisionType"], p["vehicleId"][:14], p["candidateId"][:26])
    return "%s %s %s" % (a["decisionType"], p["requestId"][:16], p.get("reasonCode", ""))


C, Cck = load("C-" + LEVEL)
M, Mck = load("Mplus-" + LEVEL)
P("C-%s acked decisions %d; Mplus-%s acked decisions %d" % (LEVEL, len(C), LEVEL, len(M)))
idx = None
for i, (a, b) in enumerate(zip(C, M)):
    if canon(fleet(a)) != canon(fleet(b)):
        idx = i
        break
dc, dm = C[idx], M[idx]
P("first differing acknowledged decision index (0-based):", idx)
P("simTimeMs C / M:", dc.get("simTimeMs"), dm.get("simTimeMs"), " epochId C / M:", dc.get("epochId"), dm.get("epochId"))
P("all earlier decisions have identical fleet actions:", all(canon(fleet(C[j])) == canon(fleet(M[j])) for j in range(idx)))
P("C fleet actions:")
for a in fleet(dc):
    P("   ", brief(a))
P("Mplus fleet actions:")
for a in fleet(dm):
    P("   ", brief(a))
acc_c = [a["payload"]["requestId"] for a in fleet(dc) if a["decisionType"] == "requestAccepted"]
rej_m = [a["payload"]["requestId"] for a in fleet(dm) if a["decisionType"] == "requestRejected"]
P("C accepts:", acc_c, " Mplus rejects:", rej_m)
P("normalOperation C / M:", dc["payload"]["certificate"]["body"]["normalOperation"], dm["payload"]["certificate"]["body"]["normalOperation"])
P("certificate witnesses M:", dm["payload"]["certificate"]["body"].get("witnesses"))
veh_cands = [(a["payload"]["vehicleId"], a["payload"]["candidateId"]) for a in fleet(dc) if a["decisionType"] == "vehiclePlanUpdated"]
P("C vehiclePlanUpdated:", [(v[:14], c[:30]) for v, c in veh_cands])
target_rid = None
for v, cand in veh_cands:
    hits = [pc for pc in dm["payload"]["solver"]["executionEvidence"]["prunedCandidates"] if pc["candidateId"] == cand]
    P("C candidate for %s found in Mplus prunedCandidates: %d hit(s)" % (v[:14], len(hits)))
    for h in hits:
        P("   code:", h["code"], " vehicleId:", h.get("vehicleId", "")[:14], " newRequestIds:", [r[:16] for r in h.get("newRequestIds", [])])
        for w in h["commitmentWitnesses"]:
            P("   witness:", json.dumps(w))
            target_rid = target_rid or w.get("requestId")
    # also: is the candidate present anywhere in C's pruned list (should not be)
    P("   candidate in C's own prunedCandidates:", any(pc["candidateId"] == cand for pc in dc["payload"]["solver"]["executionEvidence"]["prunedCandidates"]))

# witness rider history in the C run
P("\nwitness rider:", target_rid)
pub_to_dec = {}
for i, d in enumerate(C):
    for a in d["payload"]["actions"]:
        if a["decisionType"] == "promisePublished":
            pub_to_dec[a["payload"]["publicationId"]] = (i, a["payload"])
ledger = [L for L in Cck["payload"]["content"]["onlineState"]["commitmentLedger"] if L["requestId"] == target_rid][0]["entries"]
exo_before = dec_before = 0
n_before = 0
at = []
for e in ledger:
    i, act = pub_to_dec[e["publicationId"]]
    p = e["publishedPromise"]["projection"]["dropEtaMs"]
    if e["kind"] == "initialPromise":
        P("  initial promise at decision %d (epoch %s, publishedAtMs %s): drop %d" % (i, e["publishedPromise"]["publishedEpoch"], e["publishedPromise"]["publishedAtMs"], p))
        continue
    v = e["previousPromise"]["projection"]["dropEtaMs"]
    ex = e["exogenousProjection"]["dropEtaMs"]
    if i < idx:
        exo_before += ex - v
        dec_before += p - ex
        n_before += 1
    elif i == idx:
        at.append((v, ex, p, e["publishedPromise"]["publishedEpoch"], e["publishedPromise"]["publishedAtMs"],
                   act.get("decisionDelta", {}).get("dropEtaTotalMs"), act.get("exogenousDelta", {}).get("dropEtaTotalMs")))
P("  revisions before decision %d: %d; sum(e-v) = %.3f s; sum(p-e) = %.3f s" % (idx, n_before, exo_before / 1000, dec_before / 1000))
for (v, ex, p, ep, t, dd, xd) in at:
    P("  at decision %d (epoch %s, t=%s): v=%d e=%d p=%d -> e-v = %.3f s, p-e = %.3f s  (action decisionDelta.dropEtaTotalMs=%s, exogenousDelta=%s)"
      % (idx, ep, t, v, ex, p, (ex - v) / 1000, (p - ex) / 1000, dd, xd))
P("  (ledger publishedEpoch of decision-%d revisions equals decision epochId %s)" % (idx, dc.get("epochId")))
# same rider in the Mplus run at that decision
for a in dm["payload"]["actions"]:
    if a["decisionType"] == "promisePublished" and a["payload"]["promise"]["requestId"] == target_rid:
        P("  Mplus decision %d promise for witness rider: decisionDelta.drop=%s exogenousDelta.drop=%s dropEta=%s" % (
            idx, a["payload"]["decisionDelta"]["dropEtaTotalMs"], a["payload"]["exogenousDelta"]["dropEtaTotalMs"], a["payload"]["promise"]["dropEtaMs"]))
# does V behave like Mplus at the same index?
if len(sys.argv) > 3 and sys.argv[3] == "--write":
    with open(os.path.join(HERE, "mechanism_output_%s_%s.txt" % (LEVEL, CELL)), "x", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
