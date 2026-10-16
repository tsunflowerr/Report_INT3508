"""First-order screen: uniform vs trip-length-proportional dispatch budgets, from C-30's budget-pruned candidates.
For each C-30-rejected request with budget-pruned candidates (see budget_block_diagnosis.py), a candidate would pass a
budget rule if every blocking witness satisfies after <= budget(co-rider). Uniform: budget = B. Proportional:
budget = kappa * direct(co-rider), direct = maxRideTimeMs / 1.5, with kappa chosen so the MEAN budget over all C-30
served riders equals B (equal average generosity). Counts requests with at least one passing candidate. First-order
only: it ignores cascades, other structural checks re-run under new plans, and what the extra delay does to lateness.
Usage: python -B proportional_budget_screen.py <out> (mode x)."""
import base64, json, pathlib, statistics as st, sys
OPT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(OPT))
import forecast_family_a as fa
CELLS = fa.run_t38.PHASES["test"][1]
cands, directs, life_u = [], {}, {}
served_direct = []
for cell in CELLS:
    t = fa.run_dir("test", "C-30", cell) / "transcript-00.ndjson"
    _, _, state = fa.audit_vep.load(t)
    for r in state["requests"]:
        directs[(cell, r["requestId"])] = r["maxRideTimeMs"] / 1.5
        if r["lifecycle"] == "completed":
            served_direct.append(r["maxRideTimeMs"] / 1.5)
    rejected = {r["requestId"] for r in state["requests"] if r["lifecycle"] == "rejected"}
    _, _, su = fa.audit_vep.load(fa.run_dir("test", "U", cell) / "transcript-00.ndjson")
    for r in su["requests"]:
        life_u[(cell, r["requestId"])] = r["lifecycle"]
    with open(t, encoding="utf-8") as fh:
        for line in fh:
            env = json.loads(base64.b64decode(json.loads(line)["frameBase64"]))
            if env.get("messageType") != "decision":
                continue
            ev = ((env.get("payload") or {}).get("solver") or {}).get("executionEvidence") or {}
            for pc in ev.get("prunedCandidates", []):
                ws = [w for w in pc.get("commitmentWitnesses", []) if w["code"] == "COMMITMENT_BUDGET_EXCEEDED"]
                if pc["code"] == "COMMITMENT_BUDGET_EXCEEDED" and ws:
                    for r in pc.get("newRequestIds", []):
                        if r in rejected:
                            cands.append(((cell, r), [(w["after"], directs.get((cell, w["requestId"]))) for w in ws]))
mean_direct = st.mean(served_direct)
out = [f"# proportional_budget_screen.py (C-30 test runs; first-order); mean direct of served riders {mean_direct / 1000:.1f} s; "
       f"budget-blocked requests {len({k for k, _ in cands})}"]
for B in (60_000, 120_000, 300_000):
    kappa = B / mean_direct
    for name, ok in (("uniform", lambda a, d: a <= B), ("proportional", lambda a, d: d is not None and a <= kappa * d)):
        passed = {k for k, ws in cands if all(ok(a, d) for a, d in ws)}
        by_u = sum(1 for k in passed if life_u.get(k) == "completed")
        out.append(f"  mean budget {B // 1000:>3d} s, {name:<12} (kappa {kappa:.3f}): requests with a passing candidate {len(passed):3d} (served by U: {by_u})")
text = "\n".join(out) + "\n"
open(sys.argv[1], "x", encoding="utf-8", newline="\n").write(text); print(text)
