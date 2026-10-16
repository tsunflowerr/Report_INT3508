"""R16 evidence, Q2 (zero-run, read-only): what the 'budget-only blocked' requests of C-30 would get from a larger B.
A FIRST-ORDER SCREEN on the recorded C-30 path, not a policy result.

For every request REJECTED under C-30 and every recorded budget-pruned candidate carrying it in newRequestIds
(prunedCandidates[].code == COMMITMENT_BUDGET_EXCEEDED, acknowledged decisions only) the candidate's drop-budget
witnesses (dimension drop_eta_total_ms: requestId = blocking co-rider, before, delta, after = before + delta, limit)
are read. The candidate 'passes at B' if every reported drop witness has after <= B. A request passes at B if one of
its candidates does; the passing candidate with the smallest max(after) is kept (closest to what a stability-first
ranking would take). Candidates with any non-drop budget witness are not used (counted).
Caveats: (1) fail-fast validator (CommitmentDecisionValidator.cs:222-239): only the first failing rider is reported,
so an unreported co-rider may still block -> passes are optimistic; (2) the schedule after an extra acceptance
changes every later decision (R15 correction 4): no count here is an upper or lower bound on served riders.
First-order lateness cost: the blocking co-rider(s) of the kept candidate get their drop ETA pushed by delta; their
realised C-30 lateness vs their first drop promise (A - p0) plus delta is compared with 60/120/300 s.
Calibration: the same screen is run on the 8 w07 C-30 cells, where C-60 ... C-300 were actually run; the realised
served gain is read from q2-cap-dial-2026-10-10.txt / W07X-REPORT.md and compared in the report.
Usage: python -B q2_budget_screen.py <out.txt>   (out opened with mode "x"; <= 4 processes)."""
import base64
import collections
import json
import pathlib
import statistics
import sys
from concurrent.futures import ProcessPoolExecutor

OPT = pathlib.Path(r"E:/Code/Report_INT3508/ridebound-scratchpad/optimize")
sys.path.insert(0, str(OPT))
import forecast_family_a as fa  # noqa: E402

W07 = pathlib.Path(r"C:/RideBoundData/research/tier3-w07-v1")
CELLS_W07 = [f"d201811{d}-s10-r{r}-w07" for d in ("12", "13") for r in (1, 2, 3, 4)]
BS = (60, 90, 120, 150, 180, 240, 300)


def lateness(transcript):
    """served rider -> A - p0 (ms), lifecycle map."""
    _, _, state = fa.audit_vep.load(transcript)
    table, _ = fa.audit_vep.audit(transcript)
    _, alighted = fa.sweep_analyze.event_times(transcript)
    p0 = {r: p for r, c, s, k, pub, v, e, p, x, cc, z, cl in table if c == "drop" and k == "initialPromise"}
    late = {r: alighted[r] - p0[r] for r in alighted if r in p0}
    return late, {q["requestId"]: q["lifecycle"] for q in state["requests"]}


def analyze(job):
    pop, cell, c_dir, u_dir = job
    tc = c_dir / "transcript-00.ndjson"
    late_c, life_c = lateness(tc)
    late_u, life_u = lateness(u_dir / "transcript-00.ndjson")
    rejected = {r for r, l in life_c.items() if l == "rejected"}
    acked, cands = set(), []
    with open(tc, "rb") as fh:
        for line in fh:
            row = json.loads(line)
            frame = base64.b64decode(row["frameBase64"])
            if row["direction"] == "adapterToRunner":
                if b'"decisionApplied"' in frame[:160]:
                    acked.add(json.loads(frame)["payload"]["decisionHash"])
                continue
            if b'"decision"' not in frame[:160] or b"COMMITMENT_BUDGET_EXCEEDED" not in frame:
                continue
            env = json.loads(frame)
            if env.get("messageType") != "decision":
                continue
            p = env["payload"]
            for pc in (p.get("solver") or {}).get("executionEvidence", {}).get("prunedCandidates", []):
                if pc.get("code") != "COMMITMENT_BUDGET_EXCEEDED":
                    continue
                ws = [w for w in pc.get("commitmentWitnesses", []) if w.get("code") == "COMMITMENT_BUDGET_EXCEEDED"]
                cands.append((p["decisionHash"], tuple(pc.get("newRequestIds", [])),
                              [(w["requestId"], w["dimension"], w["before"], w["delta"], w["after"], w["limit"]) for w in ws]))
    out = collections.Counter()
    per_b = {b: collections.Counter() for b in BS}
    co_late = {b: collections.Counter() for b in BS}
    overshoot = []
    blocked = {}
    for h, newreq, ws in cands:
        if h not in acked:
            continue
        out["budget_pruned_candidates"] += 1
        if any(d != "drop_eta_total_ms" for _, d, *_ in ws) or not ws:
            out["candidates_with_non_drop_or_no_witness"] += 1
            continue
        for r in newreq:
            if r in rejected:
                blocked.setdefault(r, []).append(ws)
    out["rejected"] = len(rejected)
    out["budget_blocked_requests"] = len(blocked)
    out["budget_blocked_served_by_U"] = sum(1 for r in blocked if life_u.get(r) == "completed")
    out["structural_only"] = len(rejected) - len(blocked)
    out["structural_only_served_by_U"] = sum(1 for r in rejected if r not in blocked and life_u.get(r) == "completed")
    for r, wss in blocked.items():
        best = min(max(w[4] for w in ws) for ws in wss)
        overshoot.append((best - 30_000) / 1000)
        for b in BS:
            ok = [ws for ws in wss if max(w[4] for w in ws) <= b * 1000]
            if not ok:
                continue
            ws = min(ok, key=lambda x: max(w[4] for w in x))
            per_b[b]["pass"] += 1
            per_b[b]["pass_served_by_U"] += life_u.get(r) == "completed"
            if r in late_u:
                per_b[b]["pass_U_late60"] += late_u[r] > 60_000
            for co, _, before, delta, after, limit in ws:
                co_late[b]["co_riders"] += 1
                co_late[b]["delta_ms"] += delta
                if co not in late_c:
                    co_late[b]["co_not_served_in_C"] += 1
                    continue
                base, new = late_c[co], late_c[co] + delta
                for k in (60, 120, 300):
                    co_late[b][f"new_late{k}"] += base <= k * 1000 < new
    return pop, cell, dict(out), {b: dict(v) for b, v in per_b.items()}, {b: dict(v) for b, v in co_late.items()}, overshoot


def jobs():
    js = [("t38", c, fa.run_dir("test", "C-30", c), fa.run_dir("test", "U", c)) for c in fa.run_t38.PHASES["test"][1]]
    js += [("w07", c, W07 / f"C-30-{c}", W07 / f"U-{c}") for c in CELLS_W07]
    return js


def main():
    out = sys.argv[1]
    with ProcessPoolExecutor(max_workers=4) as pool:
        res = list(pool.map(analyze, jobs()))
    lines = ["# q2_budget_screen.py: first-order screen of C-30 budget-only-blocked requests at larger B (NOT a policy result)", ""]
    for pop, title in (("t38", "T3.8 C-30, 34 test cells, 3,672 requests"), ("w07", "w07 C-30, 8 cells 07-09h, 864 requests")):
        rs = [r for r in res if r[0] == pop]
        tot = collections.Counter()
        pb = {b: collections.Counter() for b in BS}
        cl = {b: collections.Counter() for b in BS}
        ov = []
        for _, _, o, p, c, s in rs:
            tot.update(o)
            for b in BS:
                pb[b].update(p.get(b, {}))
                cl[b].update(c.get(b, {}))
            ov += s
        lines.append(f"## {title}: cells {len(rs)}")
        lines.append(f"  acknowledged budget-pruned candidate records {tot['budget_pruned_candidates']} "
                     f"(with a non-drop or missing witness: {tot['candidates_with_non_drop_or_no_witness']}); rejected requests {tot['rejected']}")
        lines.append(f"  budget-only blocked requests {tot['budget_blocked_requests']} (served by U {tot['budget_blocked_served_by_U']}); "
                     f"structural-only {tot['structural_only']} (served by U {tot['structural_only_served_by_U']})")
        if ov:
            s = sorted(ov)
            lines.append(f"  smallest overshoot over 30 s (s): median {statistics.median(s):.1f}, p25 {s[len(s) // 4]:.1f}, "
                         f"p75 {s[3 * len(s) // 4]:.1f}, max {s[-1]:.1f}")
        for b in BS:
            p, c = pb[b], cl[b]
            lines.append(f"  B={b:>3d} s: pass {p['pass']:4d} (served by U {p['pass_served_by_U']:4d}; of those late>60 under U "
                         f"{p['pass_U_late60']}) | blocking co-riders pushed {c['co_riders']} (mean push {c['delta_ms'] / c['co_riders'] / 1000 if c['co_riders'] else 0:.1f} s; "
                         f"not served in C {c['co_not_served_in_C']}) -> newly late vs first promise >60 s {c['new_late60']}, "
                         f">120 s {c['new_late120']}, >300 s {c['new_late300']}")
        lines.append("")
    text = "\n".join(lines) + "\n"
    with open(out, "x", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print(text)


if __name__ == "__main__":
    main()
