"""R13 judge (Claude side): audit of the first-order proportional-budget screen used by Codex P1.

Zero-run: reads existing T3.8 C-30 / U test transcripts only. Re-derives the screen of
claude-work/proportional_budget_screen.py and adds four checks that screen does not make:
  A. who the blocking co-riders are (direct-time distribution vs the served-rider mean used to set kappa);
  B. how many budget witnesses each budget-pruned candidate carries (fail-fast evidence => 1 per candidate);
  C. kappa normalised on ALL requests (offered budget) instead of C-30 served riders;
  D. the LOSS side: C-30 accepted riders whose realised S_drop = sum|c| exceeds kappa*direct, i.e. insertions that
     C-30 accepted but a proportional rule at the same mean would have forbidden (first order).
Usage: python -B screen_audit.py <out.txt>   (output opened with mode "x")."""
import base64
import collections
import json
import pathlib
import statistics as st
import sys

OPT = pathlib.Path(r"E:/Code/Report_INT3508/ridebound-scratchpad/optimize")
sys.path.insert(0, str(OPT))
import forecast_family_a as fa  # noqa: E402

CELLS = list(fa.run_t38.PHASES["test"][1])


def q(xs, p):
    xs = sorted(xs)
    k = max(1, min(len(xs), int(-(-p * len(xs) // 1))))
    return xs[k - 1]


all_direct, served_direct, accepted_direct = [], [], []
directs, life_u = {}, {}
cands = []                      # ((cell, newRequest), [(after_ms, limit_ms, dimension, witnessRequest)])
wit_per_cand = collections.Counter()
wit_dims = collections.Counter()
s_drop = {}                     # (cell, rider) -> S_drop ms for C-30 accepted riders
n_requests = 0
for cell in CELLS:
    t = fa.run_dir("test", "C-30", cell) / "transcript-00.ndjson"
    _, _, state = fa.audit_vep.load(t)
    for r in state["requests"]:
        d = r["maxRideTimeMs"] / 1.5
        directs[(cell, r["requestId"])] = d
        all_direct.append(d)
        n_requests += 1
        if r["lifecycle"] == "completed":
            served_direct.append(d)
    rejected = {r["requestId"] for r in state["requests"] if r["lifecycle"] == "rejected"}
    _, _, su = fa.audit_vep.load(fa.run_dir("test", "U", cell) / "transcript-00.ndjson")
    for r in su["requests"]:
        life_u[(cell, r["requestId"])] = r["lifecycle"]
    table, _ = fa.audit_vep.audit(t)
    acc = set()
    sums = collections.defaultdict(float)
    for r, coord, seq, kind, pub, v, e, p, x, cc, z, closed in table:
        if coord != "drop":
            continue
        if kind == "initialPromise":
            acc.add(r)
            continue
        sums[r] += abs(cc)
    for r in acc:
        s_drop[(cell, r)] = sums[r]
        accepted_direct.append(directs[(cell, r)])
    with open(t, encoding="utf-8") as fh:
        for line in fh:
            env = json.loads(base64.b64decode(json.loads(line)["frameBase64"]))
            if env.get("messageType") != "decision":
                continue
            ev = ((env.get("payload") or {}).get("solver") or {}).get("executionEvidence") or {}
            for pc in ev.get("prunedCandidates", []):
                if pc["code"] != "COMMITMENT_BUDGET_EXCEEDED":
                    continue
                ws = [w for w in pc.get("commitmentWitnesses", []) if w["code"] == "COMMITMENT_BUDGET_EXCEEDED"]
                if not ws:
                    continue
                hit = [r for r in pc.get("newRequestIds", []) if r in rejected]
                if not hit:
                    continue
                wit_per_cand[len(ws)] += 1
                for w in ws:
                    wit_dims[w.get("dimension")] += 1
                for r in hit:
                    cands.append(((cell, r), [(w["after"], w["limit"], w.get("dimension"), w["requestId"]) for w in ws]))

blocked = {k for k, _ in cands}
blockers = {(k[0], w[3]) for k, ws in cands for w in ws}
blocker_direct = [directs[b] for b in blockers if b in directs]
new_direct = [directs[k] for k in blocked]
mean_served, mean_all = st.mean(served_direct), st.mean(all_direct)
out = ["# screen_audit.py (R13 judge, Claude side). 34 T3.8 test cells, arm C-30 (U for 'served by U')",
       f"requests {n_requests}; budget-blocked requests {len(blocked)}; budget-pruned candidate rows {len(cands)}",
       "",
       "## A. direct times (s; direct = maxRideTimeMs / 1.5)",
       f"  all requests      n={len(all_direct)} mean {mean_all/1000:.1f} median {st.median(all_direct)/1000:.1f}",
       f"  C-30 served       n={len(served_direct)} mean {mean_served/1000:.1f} median {st.median(served_direct)/1000:.1f}",
       f"  C-30 accepted     n={len(accepted_direct)} mean {st.mean(accepted_direct)/1000:.1f}",
       f"  blocking co-riders (distinct) n={len(blocker_direct)} mean {st.mean(blocker_direct)/1000:.1f} "
       f"median {st.median(blocker_direct)/1000:.1f} p25 {q(blocker_direct,0.25)/1000:.1f} p75 {q(blocker_direct,0.75)/1000:.1f}",
       f"  blocked new requests n={len(new_direct)} mean {st.mean(new_direct)/1000:.1f} median {st.median(new_direct)/1000:.1f}",
       f"  share of C-30 served riders with direct below the served mean: "
       f"{100*sum(d < mean_served for d in served_direct)/len(served_direct):.1f}%",
       "",
       "## B. budget witnesses per budget-pruned candidate row (fail-fast evidence would give exactly 1)",
       "  " + ", ".join(f"{k} witness(es): {v}" for k, v in sorted(wit_per_cand.items())),
       "  witness dimensions: " + ", ".join(f"{k}: {v}" for k, v in sorted(wit_dims.items(), key=str)),
       "",
       "## C/D. screen re-derived, with kappa normalised two ways, plus the loss side"]
for B in (60_000, 120_000):
    for norm_name, norm in (("served-mean", mean_served), ("all-request-mean", mean_all)):
        kappa = B / norm
        res = {}
        for name, ok in (("uniform", lambda a, d: a <= B),
                         ("proportional", lambda a, d: d is not None and a <= kappa * d)):
            passed = {k for k, ws in cands if all(ok(w[0], directs.get((k[0], w[3]))) for w in ws)}
            res[name] = (len(passed), sum(1 for k in passed if life_u.get(k) == "completed"))
        losses = [r for r, s in s_drop.items() if s > kappa * directs[r] + 1]
        thr = 30_000 / kappa
        short = sum(1 for d in accepted_direct if kappa * d < 30_000)
        out.append(f"  mean {B//1000} s, kappa on {norm_name} ({norm/1000:.1f} s) = {kappa:.4f}: "
                   f"uniform pass {res['uniform'][0]} (U served {res['uniform'][1]}); "
                   f"proportional pass {res['proportional'][0]} (U served {res['proportional'][1]}); "
                   f"gain-side difference {res['proportional'][0]-res['uniform'][0]} "
                   f"= {100*(res['proportional'][0]-res['uniform'][0])/n_requests:.2f} pp of {n_requests} requests")
        out.append(f"      loss side: C-30 accepted riders whose realised S_drop > kappa*direct: {len(losses)} "
                   f"(C-30 accepted riders whose proportional budget < 30 s, i.e. direct < {thr/1000:.0f} s: "
                   f"{short} of {len(accepted_direct)})")
text = "\n".join(out) + "\n"
with open(sys.argv[1], "x", encoding="utf-8", newline="\n") as fh:
    fh.write(text)
print(text)
