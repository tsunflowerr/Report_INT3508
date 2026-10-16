"""R16 evidence, Q4 (zero-run, read-only on transcripts): what would COST-FIRST selection under the SAME hard gates pick
at each recorded decision, first order (same state, same retained candidate set)?

Data: WP14r v6 (E:/RideBoundData/wp14r/development-v6-ledger), the only measured-family runs whose transcripts carry
executionEvidence.candidatePortfolio (evidenceVersion 1.2.0; T3.8 / w07 transcripts are 1.1.0 and carry no
portfolio; see probe-portfolio-presence.txt). Fields used per decision frame:
  candidatePortfolio.candidates[]: candidateId, vehicleId, newRequestIds, policyEligibility, objectiveContributions,
                                   schedule.operationalCost
  candidatePortfolio.selectionProblem.objectiveLevels[]: name, sense, aggregation (aligned with objectiveContributions)
  candidatePortfolio.selectionProblem.vehicleIds; candidatePortfolio.selectedCandidateIds
Selection model (SolverBackedFleetSelection.cs; OrToolsCandidateSelectionSolver.cs): exactly one candidate per vehicle,
each new request in at most one chosen candidate, lexicographic levels in the recorded order; 'sum' levels add,
'maximum' levels take the max over vehicles.
Step 1 (validation): re-solve each frame with ALL recorded levels over the eligible candidates by an exact dynamic
program (state = set of new requests already covered; 'maximum' levels handled by threshold filtering) and compare
with selectedCandidateIds.
Step 2 (counterfactual, first order): re-solve with the levels a cost-first objective keeps:
forced-reference-count (if present), accepted-request-count, operational-cost, candidate-id-rank:* (tie-break), i.e.
drop worst-hard-utilization-ppm and every revision:* level. Same eligible set = same hard gates.
Reported per arm: frames, frames with >= 1 new request considered, validation matches, frames where cost-first
differs, change in accepted count, operational-cost saving, and the revision levels of the cost-first plan minus the
recorded plan (drop / pickup ETA ms, material revisions, ...).
Only acknowledged decisions (decisionApplied hash) are counted.
Usage: python -B q4_cost_first_reselect.py <out.txt> [arm ...]   (out opened with mode "x"; <= 4 processes)."""
import base64
import collections
import json
import pathlib
import sys
from concurrent.futures import ProcessPoolExecutor

ROOT = pathlib.Path("E:/RideBoundData/wp14r/development-v6-ledger")
ARMS = ("c1-nobudget", "c1-budget120", "c1-budget60", "c1-h6ref", "b1-ref")
LABEL = {"b1-ref": "FREE (rolling-cost)", "c1-nobudget": "LOCKS (= T3.8 U config)", "c1-budget120": "C-120",
         "c1-budget60": "C-60", "c1-h6ref": "C-30"}
KEEP_COST_FIRST = ("forced-reference-count", "accepted-request-count", "operational-cost")


def lex_dp(vehicles, cands, idx, signs):
    """Exact lexicographic optimum over sum levels idx (list of level positions); signs: +1 minimize, -1 maximize.
    cands: vehicle -> list of (candidateId, newRequestIds frozenset, contributions list). Returns (vector, ids)."""
    best = {frozenset(): ((0,) * len(idx), ())}
    for v in vehicles:
        nxt = {}
        for state, (vec, ids) in best.items():
            for cid, req, contrib in cands[v]:
                if req & state:
                    continue
                s2 = state | req
                vec2 = tuple(a + signs[k] * contrib[i] for k, (a, i) in enumerate(zip(vec, idx)))
                cur = nxt.get(s2)
                if cur is None or vec2 < cur[0]:
                    nxt[s2] = (vec2, ids + (cid,))
        best = nxt
        if not best:
            return None
    return min(best.values())


def solve(vehicles, cands, levels, use):
    """Lexicographic solve over level positions `use` (in order). 'maximum' levels (minimize) by threshold filtering."""
    allowed = {v: list(cs) for v, cs in cands.items()}
    sum_idx, signs = [], []
    for i in use:
        sense, agg = levels[i][1], levels[i][2]
        if agg == "maximum":
            if sense != "minimize":
                raise ValueError(f"unsupported level {levels[i]}")
            ref = lex_dp(vehicles, allowed, sum_idx, signs)
            if ref is None:
                return None
            values = sorted({c[2][i] for v in vehicles for c in allowed[v]})
            for t in values:
                trial = {v: [c for c in allowed[v] if c[2][i] <= t] for v in vehicles}
                if any(not trial[v] for v in vehicles):
                    continue
                got = lex_dp(vehicles, trial, sum_idx, signs)
                if got is not None and got[0] == ref[0]:
                    allowed = trial
                    break
            else:
                raise RuntimeError("no threshold reproduces the reference optimum")
        else:
            sum_idx.append(i)
            signs.append(1 if sense == "minimize" else -1)
    return lex_dp(vehicles, allowed, sum_idx, signs)


def analyze(job):
    arm, path = job
    acked, frames = set(), []
    with open(path, "rb") as fh:
        for line in fh:
            row = json.loads(line)
            frame = base64.b64decode(row["frameBase64"])
            if row["direction"] == "adapterToRunner":
                if b'"decisionApplied"' in frame[:160]:
                    acked.add(json.loads(frame)["payload"]["decisionHash"])
                continue
            if b'"candidatePortfolio"' not in frame:
                continue
            env = json.loads(frame)
            p = env["payload"]
            ev = p["solver"]["executionEvidence"]
            frames.append((p["decisionHash"], ev["generation"].get("consideredRequestCount", 0), ev["candidatePortfolio"]))
    c = collections.Counter()
    deltas = collections.defaultdict(float)
    diff_examples = []
    cost_saving_rel = []
    drop_add = []
    for h, considered, cp in frames:
        if h not in acked:
            continue
        c["frames"] += 1
        c["with_new_request"] += considered >= 1
        levels = [(lv["name"], lv["sense"], lv["aggregation"]) for lv in cp["selectionProblem"]["objectiveLevels"]]
        names = [lv[0] for lv in levels]
        vehicles = list(cp["selectionProblem"]["vehicleIds"])
        cands = {v: [] for v in vehicles}
        contrib_of = {}
        for cand in cp["candidates"]:
            if cand.get("policyEligibility") != "eligible":
                c["ineligible_candidates"] += 1
                continue
            oc = cand["objectiveContributions"]
            if len(oc) != len(levels):
                raise ValueError(f"{path}: contributions/levels length mismatch")
            cands[cand["vehicleId"]].append((cand["candidateId"], frozenset(cand["newRequestIds"]), oc))
            contrib_of[cand["candidateId"]] = oc
        if any(not cands[v] for v in vehicles):
            c["vehicle_without_eligible"] += 1
            continue
        full = solve(vehicles, cands, levels, list(range(len(levels))))
        recorded = set(cp["selectedCandidateIds"])
        if full is None or set(full[1]) != recorded:
            c["validation_mismatch"] += 1
            continue
        c["validation_match"] += 1
        has_rev = any(n.startswith("revision:") for n in names)
        c["frames_with_revision_levels"] += has_rev
        use = [i for i, n in enumerate(names) if n in KEEP_COST_FIRST or n.startswith("candidate-id-rank:")]
        cf = solve(vehicles, cands, levels, use)
        if set(cf[1]) == recorded:
            continue
        c["cost_first_differs"] += 1
        c["cost_first_differs_with_new_request"] += considered >= 1
        def tot(ids, i):
            vals = [contrib_of[x][i] for x in ids]
            return max(vals) if levels[i][2] == "maximum" else sum(vals)
        for i, n in enumerate(names):
            if n.startswith("candidate-id-rank:"):
                continue
            deltas[n] += tot(cf[1], i) - tot(recorded, i)
        ic = names.index("operational-cost")
        rc = tot(recorded, ic)
        if rc:
            cost_saving_rel.append((rc - tot(cf[1], ic)) / rc)
        ia = names.index("accepted-request-count")
        c["accepted_changes"] += tot(cf[1], ia) != tot(recorded, ia)
        if "revision:drop_eta_total_ms" in names:
            idd = names.index("revision:drop_eta_total_ms")
            c["cf_moves_drop_more"] += tot(cf[1], idd) > tot(recorded, idd)
            drop_add.append((tot(cf[1], idd) - tot(recorded, idd)) / 1000)
        if len(diff_examples) < 3:
            diff_examples.append({n: (tot(recorded, i), tot(cf[1], i)) for i, n in enumerate(names)
                                  if not n.startswith("candidate-id-rank:")})
    total_cost = 0
    for h, considered, cp in frames:
        if h in acked:
            names = [lv["name"] for lv in cp["selectionProblem"]["objectiveLevels"]]
            ic = names.index("operational-cost")
            sel = set(cp["selectedCandidateIds"])
            total_cost += sum(cand["objectiveContributions"][ic] for cand in cp["candidates"] if cand["candidateId"] in sel)
    return arm, str(path), dict(c), dict(deltas), cost_saving_rel, diff_examples, total_cost, drop_add


def main():
    out = sys.argv[1]
    arms = sys.argv[2:] or list(ARMS)
    jobs = [(arm, r / "attempt-01" / "output" / "transcript-00.ndjson")
            for arm in arms for r in sorted(ROOT.glob(f"w14-*-{arm}-s7"))
            if (r / "attempt-01" / "output" / "transcript-00.ndjson").exists()]
    with ProcessPoolExecutor(max_workers=4) as pool:
        res = list(pool.map(analyze, jobs))
    lines = ["# q4_cost_first_reselect.py: first-order cost-first re-selection on recorded WP14r candidate portfolios",
             "# same eligible candidates (same hard gates); levels kept: forced-reference, accepted, operational-cost, id-rank", ""]
    for arm in arms:
        rs = [r for r in res if r[0] == arm]
        c = collections.Counter()
        d = collections.defaultdict(float)
        rel, ex = [], []
        tc = 0
        da = []
        for _, _, cc, dd, rr, ee, t, dad in rs:
            da += dad
            c.update(cc)
            for k, v in dd.items():
                d[k] += v
            rel += rr
            ex += ee
            tc += t
        lines.append(f"## {arm} = {LABEL[arm]}: runs {len(rs)}")
        lines.append(f"  acknowledged portfolio frames {c['frames']}; with >=1 new request considered {c['with_new_request']}; "
                     f"frames with revision levels {c['frames_with_revision_levels']}; ineligible (pruned) candidates listed {c['ineligible_candidates']}; "
                     f"frames with a vehicle lacking eligible candidates {c['vehicle_without_eligible']}")
        lines.append(f"  VALIDATION re-solve with recorded levels: match {c['validation_match']}, mismatch {c['validation_mismatch']}")
        lines.append(f"  cost-first selection differs from recorded: {c['cost_first_differs']} frames "
                     f"({100 * c['cost_first_differs'] / c['validation_match'] if c['validation_match'] else float('nan'):.3f}% of validated); "
                     f"of which with >=1 new request {c['cost_first_differs_with_new_request']}; accepted count changes {c['accepted_changes']}; "
                     f"cost-first plan moves incumbents' drop ETA more: {c['cf_moves_drop_more']}")
        if rel:
            rs_ = sorted(rel)
            lines.append(f"  operational-cost saving where it differs (share of recorded plan cost): mean {100 * sum(rs_) / len(rs_):.3f}%, "
                         f"median {100 * rs_[len(rs_) // 2]:.3f}%, max {100 * rs_[-1]:.3f}%; total saving over all acknowledged frames "
                         f"{-d.get('operational-cost', 0):.0f} of {tc} summed selected-plan cost units ({100 * -d.get('operational-cost', 0) / tc if tc else float('nan'):.4f}%)")
        if da:
            ds = sorted(da)
            lines.append(f"  extra incumbent drop-ETA dispatch movement of the cost-first plan per differing frame (s): "
                         f"median {ds[len(ds) // 2]:.1f}, p90 {ds[int(0.9 * (len(ds) - 1))]:.1f}, max {ds[-1]:.1f}; "
                         f"> 0: {sum(x > 0 for x in ds)}, > 30: {sum(x > 30 for x in ds)}, > 60: {sum(x > 60 for x in ds)}, "
                         f"> 120: {sum(x > 120 for x in ds)}, < 0: {sum(x < 0 for x in ds)} (of {len(ds)})")
        if d:
            lines.append("  summed (cost-first minus recorded) over differing frames: " +
                         ", ".join(f"{k} {v:+.0f}" for k, v in sorted(d.items())))
        for e in ex[:2]:
            lines.append(f"    example (recorded, cost-first): {e}")
    text = "\n".join(lines) + "\n"
    with open(out, "x", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print(text)


if __name__ == "__main__":
    main()
