"""Why does C-30 reject riders that U serves? Zero-run diagnosis on the 34 T3.8 test cells.
For every request REJECTED under C-30, scan C-30 decision frames: a pruned candidate carrying the request in
newRequestIds with code COMMITMENT_BUDGET_EXCEEDED passed the structural checks (pickup window, max ride time) and
was stopped only by some co-rider's dispatch budget. For such 'budget-blocked' requests record the smallest overshoot
over their budget-pruned candidates (max over witnesses of after - limit), and whether the blocking co-rider had
already spent part of its budget before (witness 'before' > 0). Cross with U: was the request served under U?
Usage: python -B budget_block_diagnosis.py <out> (mode x)."""
import base64, collections, json, pathlib, statistics as st, sys
OPT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(OPT))
import forecast_family_a as fa
CELLS = fa.run_t38.PHASES["test"][1]
def final_state(arm, cell):
    t = fa.run_dir("test", arm, cell) / "transcript-00.ndjson"
    _, _, state = fa.audit_vep.load(t)
    return t, {r["requestId"]: r["lifecycle"] for r in state["requests"]}
tot = collections.Counter(); over = []; spent_before = collections.Counter()
for cell in CELLS:
    tc, life_c = final_state("C-30", cell)
    _, life_u = final_state("U", cell)
    rejected = {r for r, l in life_c.items() if l == "rejected"}
    best = {}  # request -> (min overshoot ms, before>0 flag of that candidate)
    with open(tc, encoding="utf-8") as fh:
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
                o = max(w["after"] - w["limit"] for w in ws); before = any(w["before"] > 0 for w in ws)
                for r in pc.get("newRequestIds", []):
                    if r in rejected and (r not in best or o < best[r][0]):
                        best[r] = (o, before)
    for r in rejected:
        u = "served by U" if life_u.get(r) == "completed" else "rejected by U too"
        if r in best:
            tot[("budget-blocked", u)] += 1; over.append(best[r][0] / 1000); spent_before[best[r][1]] += 1
        else:
            tot[("structural only", u)] += 1
lines = ["# budget_block_diagnosis.py (34 T3.8 test cells, arm C-30)"]
for k in sorted(tot): lines.append(f"  {k[0]:<16} | {k[1]:<18}: {tot[k]}")
if over:
    s = sorted(over)
    lines.append(f"  budget-blocked smallest overshoot (s): median {st.median(s):.1f}, p25 {s[len(s)//4]:.1f}, p75 {s[3*len(s)//4]:.1f}, max {s[-1]:.1f}")
    for t in (30, 90, 270):
        lines.append(f"    overshoot <= {t:>3d} s (would pass a cap of {30 + t} s): {sum(1 for x in s if x <= t)} of {len(s)}")
    lines.append(f"  blocking co-rider had already spent budget before this candidate: {spent_before[True]} of {len(s)}")
text = "\n".join(lines) + "\n"
open(sys.argv[1], "x", encoding="utf-8", newline="\n").write(text); print(text)
