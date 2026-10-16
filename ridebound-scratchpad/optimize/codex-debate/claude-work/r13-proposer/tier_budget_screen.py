"""R13 proposer helper, first-order screen (zero-run, read-only): a TWO-TIER promise.
'Express' riders keep rule C with B = 30 s; 'standard' riders have no drop-change cap (locks kept, i.e. U-like).
Express membership is a deterministic pseudo-random draw: sha256(cell + requestId) mod 10000 < share * 10000.

Source of candidates: exactly as proportional_budget_screen.py / budget_block_diagnosis.py. For each request REJECTED
under C-30 on the 34 T3.8 test cells, every pruned candidate with code COMMITMENT_BUDGET_EXCEEDED passed the
structural checks and was stopped only by co-riders' budgets (witnesses). Under the two-tier rule such a candidate
would pass iff every blocking witness belongs to a STANDARD rider. Reports, per express share, the number of
budget-blocked requests with at least one passing candidate (and how many of those U served).
FIRST-ORDER ONLY: ignores cascades (a newly accepted rider changes later decisions), ignores that standard riders
could now be moved by more than 30 s and become late, and uses C-30's own candidate set.
Usage: python -B tier_budget_screen.py <out.txt>  (mode x)."""
import base64
import hashlib
import json
import pathlib
import sys

OPT = pathlib.Path(r"E:/Code/Report_INT3508/ridebound-scratchpad/optimize")
sys.path.insert(0, str(OPT))
import forecast_family_a as fa  # noqa: E402

CELLS = fa.run_t38.PHASES["test"][1]
SHARES = (0.0, 0.1, 0.2, 0.3, 0.5, 1.0)


def express(cell, rid, share):
    h = int(hashlib.sha256(f"{cell}|{rid}".encode()).hexdigest(), 16) % 10000
    return h < share * 10000


def main(out):
    cands, life_u = [], {}
    for cell in CELLS:
        t = fa.run_dir("test", "C-30", cell) / "transcript-00.ndjson"
        _, _, state = fa.audit_vep.load(t)
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
                                cands.append(((cell, r), cell, [w["requestId"] for w in ws]))
    blocked = {k for k, _, _ in cands}
    n_blockers = sorted(len(set(b)) for _, _, b in cands)
    lines = [f"# tier_budget_screen.py (34 T3.8 test cells, C-30 candidates; FIRST-ORDER): budget-blocked requests "
             f"{len(blocked)}; budget-pruned candidates {len(cands)}; distinct blocking co-riders per candidate: "
             f"1 -> {sum(x == 1 for x in n_blockers)}, 2 -> {sum(x == 2 for x in n_blockers)}, "
             f">=3 -> {sum(x >= 3 for x in n_blockers)}"]
    for s in SHARES:
        passed = {k for k, cell, bl in cands if all(not express(cell, b, s) for b in bl)}
        by_u = sum(1 for k in passed if life_u.get(k) == "completed")
        lines.append(f"  express share {s:.1f}: budget-blocked requests with a passing candidate {len(passed):3d} "
                     f"of {len(blocked)} (served by U: {by_u})")
    body = "\n".join(lines) + "\n"
    with open(out, "x", encoding="utf-8", newline="\n") as fh:
        fh.write(body)
    print(body)


if __name__ == "__main__":
    main(sys.argv[1])
