"""R17 rebuttal (Claude side): independent check of (a) Codex R16's WP14r fixed-traffic table and (b) Claude R16's
first-order cost-first re-selection (q4_cost_first_reselect.py), on the existing WP14r v6 transcripts.

Read-only; no simulation/build; outputs created with mode "x"; 1 worker process.
(a) Per served rider (passengerAlighted with a ledger initialPromise): late_k = A - p0 > k s, timely_k = served - late_k,
    exposed (any later drop entry with c = published - exogenous != 0), repeated (>= 2), S = sum |c|.
(b) For every ACKNOWLEDGED decision frame (decisionApplied carries the decision hash) with a candidatePortfolio:
    eligible candidates per vehicle; exactly one candidate per vehicle; each new request in at most one candidate.
    Cost-first order = the recorded levels named forced-reference-count / accepted-request-count / operational-cost /
    candidate-id-rank:* in their recorded order (all 'sum'); exact optimum by a DP over vehicles keyed by the covered
    request set (own implementation).
    Independent validation (necessary conditions, not a re-solve of the stability order): the recorded selection is
    feasible; its accepted count equals the cost-first optimum's; and its FULL recorded-level vector (sum or max per
    level, sign by sense) is lexicographically <= that of the cost-first optimum (else the recorded plan would not be
    optimal under its own order).
    Reported: frames, frames with >= 1 considered new request, cost-first differs (and with strictly lower cost),
    accepted-count changes, aggregate and per-differing-frame plan-cost saving, extra plan-summed decision-induced drop
    movement (cost-first minus recorded, s), number of vehicles whose candidate changes, and for frames whose extra
    movement exceeds the arm's B: how many vehicles carry nonzero drop movement in the cost-first plan.
Usage: python -B r17_wp14r_check.py <out-prefix>"""
import base64
import collections
import json
import pathlib
import re
import sys

ROOT = pathlib.Path("E:/RideBoundData/wp14r/development-v6-ledger")
ARMS = (("b1-ref", "FREE", None), ("c1-nobudget", "LOCKS", None), ("c1-budget120", "C-120", 120_000),
        ("c1-budget60", "C-60", 60_000), ("c1-h6ref", "C-30", 30_000))
TYPE = re.compile(rb'"messageType":"([A-Za-z]+)"')
CF = ("forced-reference-count", "accepted-request-count", "operational-cost")


def frame_type(b64):
    m = TYPE.search(base64.b64decode(b64[:400]))
    if m:
        return m.group(1)
    m = TYPE.search(base64.b64decode(b64))
    return m.group(1) if m else b"?"


def dp(vehicles, cands, use, signs):
    """cands: vehicle -> [(cid, frozenset(new), contributions)]; minimise tuple(signs[k]*sum contrib[use[k]])."""
    states = {frozenset(): ((0,) * len(use), ())}
    for v in vehicles:
        nxt = {}
        for cov, (vec, ids) in states.items():
            for cid, new, oc in cands[v]:
                if new & cov:
                    continue
                key = cov | new
                vec2 = tuple(x + s * oc[i] for x, s, i in zip(vec, signs, use))
                old = nxt.get(key)
                if old is None or vec2 < old[0]:
                    nxt[key] = (vec2, ids + (cid,))
        states = nxt
    return min(states.values()) if states else None


def full_vector(ids, contrib, levels):
    out = []
    for i, (name, sense, agg) in enumerate(levels):
        vals = [contrib[c][i] for c in ids]
        x = max(vals) if agg == "maximum" else sum(vals)
        out.append(x if sense == "minimize" else -x)
    return tuple(out)


def analyse_frame(cp, considered, budget_ms):
    levels = [(lv["name"], lv["sense"], lv["aggregation"]) for lv in cp["selectionProblem"]["objectiveLevels"]]
    names = [l[0] for l in levels]
    vehicles = list(cp["selectionProblem"]["vehicleIds"])
    cands = {v: [] for v in vehicles}
    contrib, veh_of = {}, {}
    for c in cp["candidates"]:
        if c.get("policyEligibility") != "eligible":
            continue
        cands[c["vehicleId"]].append((c["candidateId"], frozenset(c["newRequestIds"]), c["objectiveContributions"]))
        contrib[c["candidateId"]] = c["objectiveContributions"]
        veh_of[c["candidateId"]] = c["vehicleId"]
    rec = tuple(cp["selectedCandidateIds"])
    r = collections.Counter(frames=1, with_new=considered >= 1)
    # feasibility of the recorded plan
    seen_v, seen_r = set(), set()
    ok = all(cid in contrib for cid in rec)
    if ok:
        for cid in rec:
            v = veh_of[cid]
            new = next(n for c, n, _ in cands[v] if c == cid)
            ok &= v not in seen_v and not (new & seen_r)
            seen_v.add(v)
            seen_r |= new
        ok &= seen_v == set(vehicles)
    use = [i for i, n in enumerate(names) if n in CF or n.startswith("candidate-id-rank:")]
    signs = [1 if levels[i][1] == "minimize" else -1 for i in use]
    best = dp(vehicles, cands, use, signs)
    if not ok or best is None:
        r["invalid"] += 1
        return r, None
    cf = best[1]
    ia = names.index("accepted-request-count")
    ic = names.index("operational-cost")
    acc_rec = sum(contrib[c][ia] for c in rec)
    acc_cf = sum(contrib[c][ia] for c in cf)
    r["valid_accept_equal"] += acc_rec == acc_cf
    r["valid_full_order"] += full_vector(rec, contrib, levels) <= full_vector(cf, contrib, levels)
    cost_rec = sum(contrib[c][ic] for c in rec)
    cost_cf = sum(contrib[c][ic] for c in cf)
    r["cost_rec_total"] += cost_rec
    r["cost_cf_total"] += cost_cf
    detail = None
    if set(cf) != set(rec):
        r["differs"] += 1
        r["differs_with_new"] += considered >= 1
        r["differs_strictly_cheaper"] += cost_cf < cost_rec
        r["accepted_changes"] += acc_cf != acc_rec
        changed_vehicles = len(set(cf) - set(rec))
        extra = 0.0
        nz_veh = 0
        if "revision:drop_eta_total_ms" in names:
            idd = names.index("revision:drop_eta_total_ms")
            extra = (sum(contrib[c][idd] for c in cf) - sum(contrib[c][idd] for c in rec)) / 1000
            nz_veh = sum(contrib[c][idd] > 0 for c in cf)
            max_single = max(contrib[c][idd] for c in cf) / 1000
        else:
            max_single = 0.0
        detail = dict(rel_saving=(cost_rec - cost_cf) / cost_rec if cost_rec else 0.0, extra_drop_s=extra,
                      changed_vehicles=changed_vehicles, cf_vehicles_with_drop_move=nz_veh,
                      cf_max_single_candidate_drop_s=max_single,
                      over_budget=budget_ms is not None and extra * 1000 > budget_ms)
    return r, detail


def ledger(state, alighted):
    m = collections.Counter()
    smax = 0
    for led in state["commitmentLedger"]:
        es = led["entries"]
        rid = led["requestId"]
        if not es or es[0]["kind"] != "initialPromise" or rid not in alighted:
            continue
        p0 = es[0]["publishedPromise"]["projection"]["dropEtaMs"]
        a = alighted[rid]
        cs = [e["publishedPromise"]["projection"]["dropEtaMs"] - e["exogenousProjection"]["dropEtaMs"] for e in es[1:]]
        s = sum(abs(c) for c in cs)
        smax = max(smax, s)
        m["served"] += 1
        m["late60"] += a - p0 > 60_000
        m["late120"] += a - p0 > 120_000
        m["exposed"] += s > 0
        m["repeated"] += sum(c != 0 for c in cs) >= 2
        m["S_sum_ms"] += s
    m["requests"] = len(state["requests"])
    return m, smax


def scan(path, budget_ms):
    acked, results = set(), {}
    alighted, last = {}, None
    with path.open("rb") as fh:
        for line in fh:
            if not line.strip():
                continue
            rec = json.loads(line)
            t = frame_type(rec["frameBase64"])
            if t == b"eventBatch":
                env = json.loads(base64.b64decode(rec["frameBase64"]))
                for ev in env["payload"].get("events", []):
                    if ev.get("eventType") == "passengerAlighted":
                        alighted.setdefault(ev["payload"]["requestId"], env["simTimeMs"])
            elif t == b"decisionApplied":
                acked.add(json.loads(base64.b64decode(rec["frameBase64"]))["payload"]["decisionHash"])
            elif t == b"decision" and rec["direction"] == "runnerToAdapter":
                p = json.loads(base64.b64decode(rec["frameBase64"]))["payload"]
                ev = p.get("solver", {}).get("executionEvidence") or {}
                cp = ev.get("candidatePortfolio")
                if cp is not None:
                    results[p["decisionHash"]] = analyse_frame(cp, ev["generation"].get("consideredRequestCount", 0),
                                                               budget_ms)
            elif t == b"checkpoint" and rec["direction"] == "runnerToAdapter":
                last = rec["frameBase64"]
    state = json.loads(base64.b64decode(last))["payload"]["content"]["onlineState"]
    led, smax = ledger(state, alighted)
    c = collections.Counter()
    details = []
    for h, (r, d) in results.items():
        if h in acked:
            c.update(r)
            if d:
                details.append(d)
    c["unacked_portfolio_frames"] = sum(1 for h in results if h not in acked)
    return led, smax, c, details


def q(xs, p):
    xs = sorted(xs)
    return xs[int(p * (len(xs) - 1))] if xs else float("nan")


def main():
    prefix = sys.argv[1]
    lines = ["# r17_wp14r_check.py (Claude R17 rebuttal): WP14r v6 fixed traffic, 16 cells per arm; read-only"]
    dump = {}
    for slug, label, budget in ARMS:
        runs = sorted(ROOT.glob(f"w14-*-{slug}-s7"))
        led, c, det, smax = collections.Counter(), collections.Counter(), [], 0
        for run in runs:
            t = run / "attempt-01" / "output" / "transcript-00.ndjson"
            l, s, cc, d = scan(t, budget)
            led.update(l)
            c.update(cc)
            det += d
            smax = max(smax, s)
            print(f"{label} {run.name} done", flush=True)
        n = led["served"]
        mean_s = led["S_sum_ms"] / led["exposed"] / 1000 if led["exposed"] else 0.0
        lines.append(f"## {label} ({slug}): runs {len(runs)} requests {led['requests']} served {n} late60 {led['late60']} "
                     f"late120 {led['late120']} timely60 {n - led['late60']} timely120 {n - led['late120']} exposed "
                     f"{led['exposed']} repeated {led['repeated']} meanS_exposed {mean_s:.1f}s maxS {smax / 1000:.1f}s")
        agg_save = (c["cost_rec_total"] - c["cost_cf_total"]) / c["cost_rec_total"] if c["cost_rec_total"] else 0
        lines.append(f"  acked portfolio frames {c['frames']} (unacked {c['unacked_portfolio_frames']}); with>=1 new request "
                     f"{c['with_new']}; invalid {c['invalid']}; validation accept-equal {c['valid_accept_equal']}, "
                     f"recorded<=cost-first on full recorded order {c['valid_full_order']}")
        if c["with_new"]:
            lines.append(f"  cost-first differs {c['differs']} ({100 * c['differs'] / c['with_new']:.1f}% of new-request frames; "
                         f"with new request {c['differs_with_new']}); strictly cheaper {c['differs_strictly_cheaper']}; "
                         f"accepted changes {c['accepted_changes']}; aggregate plan-cost saving over ALL acked frames "
                         f"{100 * agg_save:.3f}%")
        if det:
            rel = [d["rel_saving"] for d in det]
            ex = [d["extra_drop_s"] for d in det]
            lines.append(f"  per differing frame: cost saving mean {100 * sum(rel) / len(rel):.2f}% median {100 * q(rel, .5):.2f}%; "
                         f"extra plan-summed drop movement median {q(ex, .5):.1f}s p90 {q(ex, .9):.1f}s max {max(ex):.1f}s; "
                         f"frames >30s {sum(x > 30 for x in ex)} >60s {sum(x > 60 for x in ex)}; changed vehicles "
                         f"distribution {dict(sorted(collections.Counter(d['changed_vehicles'] for d in det).items()))}")
            if budget:
                ob = [d for d in det if d["over_budget"]]
                lines.append(f"  frames whose extra plan-summed movement exceeds B={budget // 1000}s: {len(ob)}; "
                             + "; ".join(f"extra {d['extra_drop_s']:.1f}s, cost-first vehicles with drop move "
                                         f"{d['cf_vehicles_with_drop_move']}, largest single-candidate drop total "
                                         f"{d['cf_max_single_candidate_drop_s']:.1f}s" for d in ob[:5]))
        dump[label] = dict(ledger=dict(led), S_max_ms=smax, counts=dict(c), details=det)
    text = "\n".join(lines) + "\n"
    with open(prefix + ".txt", "x", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    with open(prefix + ".json", "x", encoding="utf-8", newline="\n") as fh:
        json.dump(dump, fh, indent=1)
    print(text, flush=True)


if __name__ == "__main__":
    main()
