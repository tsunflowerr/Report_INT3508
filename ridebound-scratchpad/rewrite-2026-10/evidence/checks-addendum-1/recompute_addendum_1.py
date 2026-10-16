"""Evidence-register addendum 1 (rewrite-2026-10, 2026-10-11): recompute, from the raw run transcripts, every N-row and
every derived ([A]) number of OUTLINE-V2.md / REVIEW-DECISIONS-R20.md that rests on the 34 T3.8 test cells.

Read-only on every input; no simulation, build or install. Exactly 2 processes: the main process and ONE worker process
each read half of the runs. Outputs are created with mode "x" next to this script.

Runs (34 T3.8 test cells = run_t38.PHASES["test"][1], i.e. tang3/t38/split-t38-v1.json "test"):
  U, C-30, Mplus-30 : archived T3.8 runs; folder = forecast_family_a.run_dir("test", arm, cell) (handles -rerun1)
  C-120             : Stage 1a runs, C:/RideBoundData/research/tier3-t38c120-v1/C-120-<cell>
Readers reused unchanged (imports only):
  tang3/evidence/audit_vep.py    load (decisions, acknowledged, final state); audit (signed v/e/p rows + summary)
  tang3/sweep/sweep_analyze.py   event_times (A = simTimeMs of the first adapter batch with passengerAlighted)
  optimize/display_layer.py      profile(day, window, "causal-no15"); D0 = display(t0, p0, prof) (naive if inactive)
  claude-work/cap_vs_pad_frontier.py   padding rule only (restated, not imported: it runs at import): fc+pad k
                                 D = D0 + k s; pad k (naive) D = p0 + k s
  r13-final-judge/cumulative_decisive_check.py   analyze(job): judge of the budget-prune classes (C-30, C-120)
The only wrapper: audit_vep.load is memoised for the current transcript (as r21-stage1a/extract_stage1a.py does), so
audit() does not parse the transcript twice; the function itself is unchanged.

Definitions (served rider = has a drop initialPromise and a passengerAlighted event; all vs the FIRST drop promise):
  late T   : A - D > T          early60 : A - D < -60 s        within60 : -60 s <= A - D <= 60 s
  timely T : served - late T, reported per 3,672 requests (a rejected request is never timely)
  ext      : D - p0 (mean over served riders)
  c        : p - e of each later drop revision (audit_vep column c); S = sum |c|; net = sum c; k = #revisions c != 0
  exposed  : S > 0 (accepted riders = riders with a drop initialPromise)
  shared   : another alighted rider on the same vehicle with an overlapping [actualPickupTimeMs, A)  (extract rule)
  Mplus-30 own-promise break : completed rider with A - p0 > 30 s (sweep_analyze M3_shareA_gt_x, used by t38_analyze)
  C-30 / C-120 own-promise break : accepted rider with S > B (sweep_analyze M4_shareC_gt_x)
  forced share of a cell : nonNormalCertificates / decisionsAcknowledged (sweep_analyze M5_nonNormalShare)
  prune classes (acknowledged decisions, COMMITMENT_BUDGET_EXCEEDED, drop witnesses): per-step-also if some
  delta > limit; cumulative-only if every drop witness has before > 0 and delta <= limit < after; else unclassified.
Cross-checks printed with OK/DIFF: Codex R15 audit summary (A, JSON lines 3-17); Codex Stage 1a JSON
(R19-stage1a-analysis.json: totals and every served rider); Claude Stage 1a riders TSV (every accepted rider).
Usage: E:/RideBoundData/wp7/envs/fleetpy-1.0.2/python.exe -B recompute_addendum_1.py
"""
from __future__ import annotations

import collections
import json
import math
import pathlib
import statistics
import sys
from concurrent.futures import ProcessPoolExecutor

HERE = pathlib.Path(__file__).resolve().parent
SCR = pathlib.Path(r"E:/Code/Report_INT3508/ridebound-scratchpad")
OPT = SCR / "optimize"
DEB = OPT / "codex-debate"
JUDGE = DEB / "claude-work" / "r13-final-judge"
sys.path.insert(0, str(OPT))
sys.path.insert(0, str(JUDGE))
import display_layer as dl  # noqa: E402
import forecast_family_a as fa  # noqa: E402
import cumulative_decisive_check as cdc  # noqa: E402

OUT_TXT = HERE / "recompute-addendum-1-2026-10-11.txt"
OUT_JSON = HERE / "recompute-addendum-1-2026-10-11.json"
C120_ROOT = pathlib.Path(r"C:/RideBoundData/research/tier3-t38c120-v1")
CELLS = tuple(fa.run_t38.PHASES["test"][1])
ARMS = ("U", "C-30", "C-120", "Mplus-30")
CAP = {"C-30": 30_000, "C-120": 120_000}
REQ = 3672
A_SUMMARY = DEB / "codex-work" / "R15-audit-summary.txt"
CODEX_S1A = DEB / "codex-work" / "R19-stage1a-analysis.json"
CLAUDE_TSV = DEB / "claude-work" / "r21-stage1a" / "stage1a-2026-10-10-riders.tsv"
QUOTES = ("naive", "pad30", "fc", "fc+30", "fc+60")

_orig_load = fa.audit_vep.load
_cache: dict = {}


def _cached_load(path):
    key = str(path)
    if key not in _cache:
        _cache.clear()
        _cache[key] = _orig_load(path)
    return _cache[key]


fa.audit_vep.load = _cached_load  # audit() resolves load() through the module global


def run_dir(arm: str, cell: str) -> pathlib.Path:
    if arm == "C-120":
        return C120_ROOT / f"C-120-{cell}"
    return fa.run_dir("test", arm, cell)


def own_prunes(decisions, acknowledged):
    classes, limits, cum = collections.Counter(), collections.Counter(), []
    for h, payload in decisions.items():
        if h not in acknowledged:
            continue
        ev = ((payload.get("solver") or {}).get("executionEvidence") or {})
        for pc in ev.get("prunedCandidates", []):
            if pc.get("code") != "COMMITMENT_BUDGET_EXCEEDED":
                continue
            ws = [w for w in pc.get("commitmentWitnesses", []) if w.get("code") == "COMMITMENT_BUDGET_EXCEEDED"]
            drop = [w for w in ws if w.get("dimension") == "drop_eta_total_ms"]
            for w in drop:
                limits[w["limit"]] += 1
                if w["before"] + w["delta"] != w["after"]:
                    raise SystemExit(f"witness arithmetic broken in {h}")
            if not drop:
                cls = "other-budget" if ws else "no-witness"
            elif any(w["delta"] > w["limit"] for w in drop):
                cls = "per-step-also"
            elif all(w["before"] > 0 and w["delta"] <= w["limit"] < w["after"] for w in drop):
                cls = "cumulative-only"
                cum.append({"decisionHash": h, "newRequestIds": list(pc.get("newRequestIds", [])),
                            "witness": [[w["requestId"], w["before"], w["delta"], w["after"], w["limit"]] for w in drop]})
            else:
                cls = "unclassified"
            classes[cls] += 1
    return dict(classes), {str(k): v for k, v in limits.items()}, cum


def objective(decisions, acknowledged):
    """Generator / objective counters, same fields as Codex R15-audit-v2.py scan() (acknowledged decisions only)."""
    obj = collections.Counter()
    for h, payload in decisions.items():
        if h not in acknowledged:
            continue
        ev = ((payload.get("solver") or {}).get("executionEvidence") or {})
        gen = ev.get("generation", {})
        obj["decision_frames"] += 1
        for v in gen.get("vehicleLosses", []):
            obj["cap_applied"] += bool(v.get("candidateCapApplied"))
            obj["omitted_by_cap"] += v.get("omittedFeasibleCandidateCountByCap", 0)
            obj["work_exhausted"] += bool(v.get("workBudgetExhausted"))
        obj["omitted_requests"] += gen.get("omittedRequestCount", 0)
        if gen.get("consideredRequestCount", 0) > 0:
            obj["with_new"] += 1
            bounds = ((ev.get("selection") or {}).get("finalSolverDiagnostics") or {}).get("objectiveBounds", [])
            for bound in bounds:
                if bound["objectiveName"] == "worst-hard-utilization-ppm":
                    obj["util_present"] += 1
                    obj["incumbent_1e6"] += bound["incumbentValue"] == 1_000_000
                    obj["bound_1e6"] += bound["bestBound"] == 1_000_000
    return dict(obj)


def job(arg):
    arm, cell = arg
    run = run_dir(arm, cell)
    tr = run / "transcript-00.ndjson"
    summary_json = json.loads((run / "summary.json").read_text(encoding="utf-8"))
    run00 = json.loads((run / "run-00.json").read_text(encoding="utf-8"))
    decisions, acknowledged, state = fa.audit_vep.load(tr)
    table, summary = fa.audit_vep.audit(tr)
    if table is None:
        raise SystemExit(f"{run}: no final checkpoint")
    _, alighted = fa.sweep_analyze.event_times(tr)
    prof = dl.profile(fa.day_of(cell), cell[-3:], "causal-no15")
    first, revs = {}, collections.defaultdict(list)
    for r, coord, seq, kind, pub, v, e, p, x, c, z, closed in table:
        if coord != "drop":
            continue
        if kind == "initialPromise":
            if r in first or seq != 0:
                raise SystemExit(f"{run}: {r} drop initialPromise not unique or not first")
            first[r] = (pub, p)
        else:
            revs[r].append((seq, c))
    if set(revs) - set(first):
        raise SystemExit(f"{run}: revisions without an initial promise")
    life = {q["requestId"]: q["lifecycle"] for q in state["requests"]}
    legs = collections.defaultdict(list)
    for q in state["requests"]:
        if q["requestId"] in alighted:
            legs[q["assignedVehicleId"]].append((q["actualPickupTimeMs"], alighted[q["requestId"]], q["requestId"]))
    shared = set()
    for rs in legs.values():
        for a0, a1, rid in rs:
            if any(o != rid and b0 < a1 and a0 < b1 for b0, b1, o in rs):
                shared.add(rid)
    riders = []
    for r in sorted(first):
        t0, p0 = first[r]
        cs = [c for _, c in sorted(revs.get(r, []))]
        riders.append({
            "rid": r, "life": life.get(r, ""), "t0": t0, "p0": p0, "D0": dl.display(t0, p0, prof),
            "A": alighted.get(r), "S": sum(abs(c) for c in cs), "k": sum(1 for c in cs if c != 0),
            "net": sum(cs), "neg": sum(-c for c in cs if c < 0), "nz": [c for c in cs if c != 0],
            "shared": r in shared})
    if sum(x["S"] for x in riders) != summary["sumDropC"]:
        raise SystemExit(f"{run}: per-rider sum |c| != audit sumDropC")
    classes, limits, cum = own_prunes(decisions, acknowledged)
    judged = cdc.analyze(("addendum-1", arm, tr)) if arm in CAP else None
    rec = {
        "arm": arm, "cell": cell, "folder": run.name, "summaryStatus": summary_json.get("status"),
        "repeatCount": summary_json.get("repeatCount"), "run00Status": run00.get("status"),
        "requests": summary["requests"], "lifecycle": summary["lifecycle"], "promisedRiders": summary["promisedRiders"],
        "decisionsAcknowledged": summary["decisionsAcknowledged"], "decisionFrames": len(decisions),
        "unacknowledged": len(set(decisions) - acknowledged),
        "nonNormal": summary["nonNormalCertificates"], "ridersWithForcedBreach": summary["ridersWithForcedBreach"],
        "breaches": summary["breaches"], "sumDropC": summary["sumDropC"], "forecastActive": prof is not None,
        "alightedWithoutPromise": sum(1 for r in alighted if r not in first),
        "life": life, "riders": riders, "pruneOwn": classes, "dropLimits": limits, "cumOnly": cum,
        "objective": objective(decisions, acknowledged),
        "judge": None if judged is None else {k: judged[k] for k in (
            "candidates", "acked_decisions", "decisions_with_cumulative_only",
            "requests_with_cumulative_only_candidate", "of_which_finally_rejected", "served")},
    }
    _cache.clear()
    return rec


# ---------------------------------------------------------------- aggregation helpers
def q_nearest(xs, p):
    xs = sorted(xs)
    if not xs:
        return float("nan")
    k = max(1, min(len(xs), int(-(-p * len(xs) // 1))))
    return xs[k - 1]


def quote_value(x, name):
    if name == "naive":
        return x["p0"]
    if name == "pad30":
        return x["p0"] + 30_000
    if name == "fc":
        return x["D0"]
    if name == "fc+30":
        return x["D0"] + 30_000
    if name == "fc+60":
        return x["D0"] + 60_000
    raise ValueError(name)


def frontier(served, name):
    lat = [x["A"] - quote_value(x, name) for x in served]
    n = len(served)
    m = {"served": n}
    for t in (30, 60, 120, 300, 600):
        m[f"late{t}"] = sum(1 for v in lat if v > t * 1000)
    m["early60"] = sum(1 for v in lat if v < -60_000)
    m["within60_direct"] = sum(1 for v in lat if -60_000 <= v <= 60_000)
    m["within60_arith"] = n - m["late60"] - m["early60"]
    m["timely60"] = n - m["late60"]
    m["timely120"] = n - m["late120"]
    m["ext_sum_ms"] = sum(quote_value(x, name) - x["p0"] for x in served)
    m["ext_mean_s"] = m["ext_sum_ms"] / n / 1000 if n else 0.0
    return m


def pct(a, b):
    return 100.0 * a / b if b else float("nan")


def main() -> int:
    items = [(arm, cell) for arm in ARMS for cell in CELLS]
    worker_items, main_items = items[0::2], items[1::2]
    with ProcessPoolExecutor(max_workers=1) as pool:          # main + 1 worker = 2 processes
        futures = [pool.submit(job, it) for it in worker_items]
        mine = [job(it) for it in main_items]
        theirs = [f.result() for f in futures]
    R = {(r["arm"], r["cell"]): r for r in mine + theirs}
    if len(R) != len(items):
        raise SystemExit("missing runs")

    out, J = [], {}
    say = out.append
    say("# recompute_addendum_1.py (evidence-register addendum 1, 2026-10-11); 34 T3.8 test cells x U, C-30, C-120, Mplus-30")
    say(f"# runs read: {len(R)}; processes: 2 (main + 1 worker); every output mode 'x'")

    # 0. validity
    say("\n## 0. Input validity per arm")
    served_of, accepted_of = {}, {}
    for arm in ARMS:
        rs = [R[(arm, c)] for c in CELLS]
        statuses = collections.Counter(r["summaryStatus"] for r in rs)
        run00 = collections.Counter(r["run00Status"] for r in rs)
        reruns = [r["folder"] for r in rs if r["folder"].endswith("-rerun1")]
        life = collections.Counter()
        for r in rs:
            life.update(r["lifecycle"])
        acc = [(r["cell"], x) for r in rs for x in r["riders"]]
        srv = [(c, x) for c, x in acc if x["A"] is not None]
        bad = sum(1 for c, x in acc if (x["A"] is not None) != (x["life"] == "completed"))
        accepted_of[arm], served_of[arm] = acc, srv
        say(f"- {arm}: runs {len(rs)}; summary status {dict(statuses)}; repeatCount {sorted({r['repeatCount'] for r in rs})}; "
            f"run-00 {dict(run00)}; rerun folders {reruns}; requests {sum(r['requests'] for r in rs)}; lifecycle {dict(life)}; "
            f"accepted (drop initialPromise) {len(acc)}; served (alighted) {len(srv)}; alighted<->completed mismatches {bad}; "
            f"alighted without promise {sum(r['alightedWithoutPromise'] for r in rs)}; acknowledged decisions "
            f"{sum(r['decisionsAcknowledged'] for r in rs)}; unacknowledged decision frames {sum(r['unacknowledged'] for r in rs)}; "
            f"non-normal (forced) decisions {sum(r['nonNormal'] for r in rs)}; riders with forced breach "
            f"{sum(r['ridersWithForcedBreach'] for r in rs)}; forecast-active cells {sum(r['forecastActive'] for r in rs)}")

    # 1. frontier
    say("\n## 1. Outcomes vs the first drop promise (served riders pooled; timely per 3,672 requests)")
    say("arm      quote  | served | late30 late60 late120 late300 late600 | early60 | within60 direct = served-late60-early60 | "
        "timely60 timely120 | ext_sum_ms | ext_mean_s")
    F = {}
    for arm in ARMS:
        served = [x for _, x in served_of[arm]]
        for name in QUOTES:
            m = frontier(served, name)
            F[(arm, name)] = m
            say(f"{arm:<8} {name:<6} | {m['served']:5d} | {m['late30']:5d} {m['late60']:5d} {m['late120']:6d} {m['late300']:6d} "
                f"{m['late600']:6d} | {m['early60']:6d} | {m['within60_direct']:5d} {'=' if m['within60_direct'] == m['within60_arith'] else '!='} "
                f"{m['within60_arith']:5d} | {m['timely60']:5d} {m['timely120']:5d} | {m['ext_sum_ms']:.4f} | {m['ext_mean_s']:.6f}")
    J["frontier"] = {f"{a}|{q}": m for (a, q), m in F.items()}

    # 1b. cross-check vs Codex A (R15 audit summary)
    say("\n## 1b. Cross-check vs Codex R15 audit summary (A:7-9, pop t38; quotes naive / fc / fc_pad30 / fc_pad60)")
    A = {}
    for i, line in enumerate(A_SUMMARY.read_text(encoding="utf-8").splitlines(), 1):
        if line.startswith("{") and '"arm"' in line and '"pop"' in line:
            A[(json.loads(line)["pop"], json.loads(line)["arm"])] = (i, json.loads(line))
    amap = {"naive": "naive", "fc": "fc", "fc_pad30": "fc+30", "fc_pad60": "fc+60"}
    diffs = 0
    for arm in ("U", "C-30", "Mplus-30"):
        line_no, g = A[("t38", arm)]
        for an, mine_name in amap.items():
            for key in ("served", "late60", "late120", "late300", "late600", "early60"):
                ok = g["frontier"][an][key] == F[(arm, mine_name)][key]
                diffs += not ok
                if not ok:
                    say(f"  DIFF {arm} {an} {key}: A:{line_no} {g['frontier'][an][key]} vs mine {F[(arm, mine_name)][key]}")
            d = abs(g["frontier"][an]["ext_sum_ms"] - F[(arm, mine_name)]["ext_sum_ms"])
            say(f"  {arm:<8} {an:<9} A:{line_no} counts {'OK' if all(g['frontier'][an][k] == F[(arm, mine_name)][k] for k in ('served', 'late60', 'late120', 'late300', 'late600', 'early60')) else 'DIFF'}; "
                f"ext_sum_ms A {g['frontier'][an]['ext_sum_ms']:.4f} vs mine {F[(arm, mine_name)]['ext_sum_ms']:.4f} (|diff| {d:.6f} ms)")
        for key in ("exposed", "repeated", "S_max_ms", "S_sum_exposed_ms", "served", "late60_and_exposed"):
            say(f"  {arm:<8} ledger {key} A:{line_no} {g['ledger'].get(key)}")
    say(f"  count mismatches vs A: {diffs}")

    # 1c. cross-check vs Codex Stage 1a JSON (totals and per served rider)
    say("\n## 1c. Cross-check vs Codex Stage 1a JSON (R19-stage1a-analysis.json): totals and every served rider")
    cx = json.loads(CODEX_S1A.read_text(encoding="utf-8"))
    for arm in ("U", "C-30", "C-120"):
        tot = cx["totals"][arm]
        for cq, mq in (("naive", "naive"), ("causal-no15", "fc")):
            f = tot["frontier"][cq]
            parts = []
            for key in ("served", "late60", "late120", "late300", "early60", "timely60", "timely120"):
                parts.append(f"{key} {f[key]}{'' if f[key] == F[(arm, mq)][key] else ' DIFF mine ' + str(F[(arm, mq)][key])}")
            parts.append(f"ext_sum_ms |diff| {abs(f['quote_extension_sum_ms'] - F[(arm, mq)]['ext_sum_ms']):.6f}")
            say(f"  {arm:<6} {cq:<11} " + "; ".join(parts))
        say(f"  {arm:<6} totals: acknowledged {tot['acknowledged_decisions']}, non-normal {tot['non_normal_decisions']}, "
            f"drop_exposed {tot['drop_exposed']}, >=2 changes {tot['two_or_more_nonzero_changes']}, max |dispatch| ms "
            f"{tot['max_absolute_dispatch_ms']}, prune classes {tot.get('prune_classes')}, cumulative-only records "
            f"{tot.get('cumulative_only_records')} in decisions {tot.get('cumulative_only_decisions')}")
    by_cx = collections.defaultdict(dict)
    for run in cx["runs"]:
        for rr in run["riders"]:
            by_cx[(run["arm"], run["cell"])][rr["request"]] = rr
    mism = collections.Counter()
    maxdq = 0.0
    n_cmp = 0
    for arm in ("U", "C-30", "C-120"):
        for cell in CELLS:
            mine_served = {x["rid"]: x for x in R[(arm, cell)]["riders"] if x["A"] is not None}
            theirs_ = by_cx[(arm, cell)]
            if set(mine_served) != set(theirs_):
                mism["served-set"] += 1
            for rid, x in mine_served.items():
                y = theirs_.get(rid)
                if y is None:
                    continue
                n_cmp += 1
                mism["t0"] += x["t0"] != y["t0"]
                mism["P0"] += x["p0"] != y["P0"]
                mism["A"] += x["A"] != y["arrival"]
                mism["S"] += x["S"] != y["absolute_dispatch_ms"]
                mism["k"] += x["k"] != y["nonzero_changes"]
                maxdq = max(maxdq, abs(x["D0"] - y["forecast_quote"]))
    say(f"  per-rider comparison on {n_cmp} served riders (U, C-30, C-120): mismatches {dict(mism) or 'none'}; "
        f"max |D0 mine - forecast_quote Codex| = {maxdq:.6f} ms")
    J["codex_rider_mismatches"] = dict(mism)
    J["codex_max_D0_diff_ms"] = maxdq

    # 1d. cross-check vs Claude Stage 1a riders TSV (every accepted rider)
    lines = CLAUDE_TSV.read_text(encoding="utf-8").splitlines()
    head = lines[0].split("\t")
    tsv = {}
    for line in lines[1:]:
        v = dict(zip(head, line.split("\t")))
        tsv[(v["arm"], v["cell"], v["requestId"])] = v
    tm = collections.Counter()
    n_t = 0
    for arm in ("U", "C-30", "C-120"):
        for cell in CELLS:
            for x in R[(arm, cell)]["riders"]:
                v = tsv.get((arm, cell, x["rid"]))
                if v is None:
                    tm["missing"] += 1
                    continue
                n_t += 1
                tm["life"] += v["lifecycle"] != x["life"]
                tm["t0"] += int(v["t0"]) != x["t0"]
                tm["p0"] += int(v["p0"]) != x["p0"]
                tm["D0"] += float(v["D0"]) != x["D0"]
                tm["A"] += (v["A"] or None) != (None if x["A"] is None else str(x["A"]))
                tm["S"] += int(v["sumAbsC"]) != x["S"]
                tm["k"] += int(v["nonzeroC"]) != x["k"]
                tm["net"] += int(v["netC"]) != x["net"]
                tm["shared"] += (v["shared"] == "1") != x["shared"]
    extra = sum(1 for key in tsv if key[0] in ("U", "C-30", "C-120")) - n_t
    say(f"\n## 1d. Cross-check vs Claude Stage 1a riders TSV: {n_t} accepted riders compared; field mismatches "
        f"{ {k: v for k, v in tm.items() if v} or 'none'}; TSV rows not matched {extra}")

    # 2. the N-01 ... N-04 rows and the "honest answer" arithmetic
    say("\n## 2. N-01..N-04 and the RD section 8 arithmetic")
    u30, c_fc, c30, u_fc, c120 = F[("U", "fc+30")], F[("C-30", "fc")], F[("C-30", "fc+30")], F[("U", "fc")], F[("C-120", "fc")]
    say(f"N-01 tail late>120/300/600 s: U+fc+30 {u30['late120']} / {u30['late300']} / {u30['late600']}; "
        f"C-30+fc {c_fc['late120']} / {c_fc['late300']} / {c_fc['late600']}")
    say(f"N-02 C-30+fc+30: served {c30['served']}, late60 {c30['late60']}, early60 {c30['early60']}, ext_sum_ms "
        f"{c30['ext_sum_ms']:.4f} / {c30['served']} = {c30['ext_mean_s']:.4f} s")
    say(f"N-03 U+fc: late60 {u_fc['late60']}, late120 {u_fc['late120']}, early60 {u_fc['early60']}, ext {u_fc['ext_mean_s']:.4f} s")
    for label, arm, qn in (("C-30+fc", "C-30", "fc"), ("U+fc+30", "U", "fc+30"), ("U+fc", "U", "fc"),
                           ("C-30+fc+30", "C-30", "fc+30"), ("C-120+fc", "C-120", "fc"), ("U+fc+60", "U", "fc+60"),
                           ("C-30 naive", "C-30", "naive"), ("U naive", "U", "naive")):
        m = F[(arm, qn)]
        say(f"N-04 within +-60 s, {label:<11}: direct {m['within60_direct']} ; served {m['served']} - late60 {m['late60']} - "
            f"early60 {m['early60']} = {m['within60_arith']} ; per 3,672 requests {pct(m['within60_direct'], REQ):.2f}%")
    say(f"   late60 and early60 are disjoint by definition (A-D > 60 s vs A-D < -60 s); direct == arithmetic in every row "
        f"above: {all(F[k]['within60_direct'] == F[k]['within60_arith'] for k in F)}")
    say(f"RD8.1 equal promise length, no pad: timely60 C-30+fc {c_fc['timely60']} vs U+fc {u_fc['timely60']}; timely120 "
        f"{c_fc['timely120']} vs {u_fc['timely120']}; ext {c_fc['ext_mean_s']:.4f} vs {u_fc['ext_mean_s']:.4f} s")
    say(f"RD8.1 both +30 s: timely60 C-30+fc+30 {c30['timely60']} vs U+fc+30 {u30['timely60']}; timely120 {c30['timely120']} vs "
        f"{u30['timely120']}; ext {c30['ext_mean_s']:.4f} vs {u30['ext_mean_s']:.4f} s")
    say(f"RD8.1 ratio of extensions U+fc+30 / C-30+fc = {u30['ext_mean_s']:.4f} / {c_fc['ext_mean_s']:.4f} = "
        f"{u30['ext_mean_s'] / c_fc['ext_mean_s']:.4f}")
    say(f"RD8.2 early60: C-30+fc {c_fc['early60']}/{c_fc['served']} = {pct(c_fc['early60'], c_fc['served']):.3f}%; "
        f"U+fc+30 {u30['early60']}/{u30['served']} = {pct(u30['early60'], u30['served']):.3f}%")
    say(f"RD8.3 timely120 lead U+fc+30 - C-30+fc = {u30['timely120']} - {c_fc['timely120']} = {u30['timely120'] - c_fc['timely120']}; "
        f"served difference {u30['served'] - c_fc['served']}; late120 {u30['late120']} vs {c_fc['late120']}")
    say(f"RD8.6 C-120+fc timely60 {c120['timely60']}, timely120 {c120['timely120']}, ext {c120['ext_mean_s']:.4f} s; "
        f"ext ratio C-120+fc / U+fc+30 = {c120['ext_mean_s'] / u30['ext_mean_s']:.4f}; served U - C-120 = "
        f"{F[('U', 'naive')]['served'] - F[('C-120', 'naive')]['served']}")
    say(f"C10 tie: U+fc+30 timely60 {u30['timely60']} = 2434 - {u30['late60']}; C-30+fc timely60 {c_fc['timely60']} = 2338 - "
        f"{c_fc['late60']}; at 120 s {u30['timely120']} vs {c_fc['timely120']}; ext {u30['ext_mean_s']:.4f} vs {c_fc['ext_mean_s']:.4f} s")
    mp = F[("Mplus-30", "fc")]
    say(f"RD8.5 Mplus-30: served {mp['served']}, fc timely60 {mp['timely60']}, fc timely120 {mp['timely120']}; naive late60 "
        f"{F[('Mplus-30', 'naive')]['late60']}")
    say("Bang 4.6 / C28 per 100 requests (naive): " + "; ".join(
        f"{arm} late60/120/300/600 = " + " / ".join(f"{100 * F[(arm, 'naive')][f'late{t}'] / REQ:.2f}" for t in (60, 120, 300, 600))
        for arm in ("U", "C-30")) + f"; C-30+fc late60 per 100 = {100 * c_fc['late60'] / REQ:.2f}")

    # 3. exposure (N-05, N-07, Bang 4.8)
    say("\n## 3. Dispatch changes of the drop promise (accepted riders; S = sum |c|)")
    EX = {}
    for arm in ARMS:
        acc = [x for _, x in accepted_of[arm]]
        exp = [x for x in acc if x["S"] > 0]
        Ss = [x["S"] / 1000 for x in exp]
        changes = [abs(c) / 1000 for x in acc for c in x["nz"]]
        late = [x for _, x in served_of[arm] if x["A"] - x["p0"] > 60_000]
        e = {"accepted": len(acc), "exposed": len(exp), "k2": sum(1 for x in acc if x["k"] >= 2),
             "maxk": max((x["k"] for x in acc), default=0), "S_max_ms": max((x["S"] for x in acc), default=0),
             "S_sum_ms": sum(x["S"] for x in acc), "net_sum_ms": sum(x["net"] for x in acc),
             "neg_sum_ms": sum(x["neg"] for x in acc), "net_negative": sum(1 for x in exp if x["net"] < 0),
             "net_positive": sum(1 for x in exp if x["net"] > 0), "riders_with_any_negative_c": sum(1 for x in acc if x["neg"] > 0),
             "S_mean_s": statistics.mean(Ss) if Ss else 0, "S_p50_s": q_nearest(Ss, 0.5), "S_p90_s": q_nearest(Ss, 0.9),
             "changes": len(changes), "change_median_s": statistics.median(changes) if changes else 0,
             "late60": len(late), "late60_and_exposed": sum(1 for x in late if x["S"] > 0),
             "ledger_dispatch_share_late60": (sum(x["net"] for x in late) / sum(x["A"] - x["p0"] for x in late)) if late else 0}
        if arm in CAP:
            b = CAP[arm]
            e.update({"overshoot": sum(1 for x in acc if x["S"] > b), "ge90": sum(1 for x in acc if x["S"] >= 0.9 * b),
                      "ge50": sum(1 for x in acc if x["S"] >= 0.5 * b),
                      "own_break_cells": sum(1 for c in CELLS if any(x["S"] > b for x in R[(arm, c)]["riders"]))})
        EX[arm] = e
        say(f"- {arm}: " + "; ".join(f"{k} {round(v, 4) if isinstance(v, float) else v}" for k, v in e.items()))
        say(f"    exposed share of accepted {pct(e['exposed'], e['accepted']):.2f}%; net-earlier riders listed: " + str(
            [(c, x["rid"][:13], x["nz"]) for c, x in accepted_of[arm] if x["S"] > 0 and x["net"] < 0]))
    J["exposure"] = EX
    c30e = EX["C-30"]
    say(f"N-05 C-30 earlier total (sum of -c over c < 0) = {c30e['neg_sum_ms']} ms; check (sum|c| - sum c)/2 = "
        f"({c30e['S_sum_ms']} - {c30e['net_sum_ms']})/2 = {(c30e['S_sum_ms'] - c30e['net_sum_ms']) / 2}; "
        f"rounding bound from the two 10.9 s means: sum|c|/33 = {c30e['S_sum_ms'] / 33 / 1000:.4f} s, signed mean "
        f"{c30e['net_sum_ms'] / 33 / 1000:.4f} s")
    for arm in ("C-30", "C-120"):
        wk = [x["S"] for c in CELLS if c[7:9] in ("17", "18") for x in R[(arm, c)]["riders"]]
        ina = [x["S"] for c in CELLS if not R[(arm, c)]["forecastActive"] for x in R[(arm, c)]["riders"]]
        say(f"{arm}: max S on weekend cells (17-18/11, {sum(1 for c in CELLS if c[7:9] in ('17', '18'))} cells) {max(wk) / 1000:.3f} s; "
            f"on forecast-inactive cells ({sum(1 for c in CELLS if not R[(arm, c)]['forecastActive'])} cells) {max(ina) / 1000:.3f} s")
    rep = [(c, x["rid"][:13], x["nz"]) for c, x in accepted_of["U"] if x["k"] >= 2]
    say(f"U riders with >= 2 nonzero c ({len(rep)}): {rep}")
    say(f"  U rider with exactly the changes 25844 and 99027 ms present: "
        f"{[(c, r) for c, r, nz in rep if 25844 in nz and 99027 in nz]}")

    # 4. forced decisions (N-07) and generator counters
    say("\n## 4. Forced decisions and generator / objective counters (acknowledged decisions)")
    OB = {}
    for arm in ARMS:
        o = collections.Counter()
        for c in CELLS:
            o.update(R[(arm, c)]["objective"])
        OB[arm] = dict(o)
        say(f"- {arm}: forced (non-normal) {sum(R[(arm, c)]['nonNormal'] for c in CELLS)} of "
            f"{sum(R[(arm, c)]['decisionsAcknowledged'] for c in CELLS)} acknowledged decisions; counters {dict(o)}")
    J["objective"] = OB

    # 5. prune records (N-08, N-15)
    say("\n## 5. Budget prune records (acknowledged decisions)")
    PR = {}
    for arm in ARMS:
        own = collections.Counter()
        lim = collections.Counter()
        judge = collections.Counter()
        jd = jr = jrej = 0
        cum = []
        for c in CELLS:
            r = R[(arm, c)]
            own.update(r["pruneOwn"])
            lim.update(r["dropLimits"])
            cum.extend((c, d) for d in r["cumOnly"])
            if r["judge"]:
                judge.update(r["judge"]["candidates"])
                jd += r["judge"]["decisions_with_cumulative_only"]
                jr += r["judge"]["requests_with_cumulative_only_candidate"]
                jrej += r["judge"]["of_which_finally_rejected"]
        PR[arm] = {"own": dict(own), "limits": dict(lim), "judge": dict(judge), "cum_decisions": len({(c, d["decisionHash"]) for c, d in cum}),
                   "cum_records": len(cum), "total": sum(own.values())}
        say(f"- {arm}: own classes {dict(own)} (total {sum(own.values())}); drop-witness limits {dict(lim)}; judge "
            f"(cumulative_decisive_check) {dict(judge) if judge else '-'}; judge decisions with cumulative-only {jd}, "
            f"requests {jr}, finally rejected {jrej}; own cumulative-only records {len(cum)} in "
            f"{len({(c, d['decisionHash']) for c, d in cum})} decisions")
        for c, d in cum:
            news = d["newRequestIds"]
            fates = {a: [R[(a, c)]["life"].get(n, "absent") for n in news] for a in ("C-120", "C-30", "U")}
            wit = d["witness"][0]
            wx = next((x for x in R[(arm, c)]["riders"] if x["rid"] == wit[0]), None)
            say(f"    {c} decision {d['decisionHash'][:12]} new {[n[:13] for n in news]} witness before {wit[1]} + delta {wit[2]}"
                f" = after {wit[3]} > limit {wit[4]}; final lifecycle of the new request(s): {fates}; witness rider final "
                f"S {wx['S'] if wx else None} ms, k {wx['k'] if wx else None}, life {wx['life'] if wx else None}")
    J["prunes"] = PR
    a_lines = {k: v for k, v in A.items()}
    w07_runs = sum(g["runs"] for (pop, arm), (_, g) in a_lines.items() if pop == "w07")
    w07_step = sum(g["candidates"].get("step-fails", 0) for (pop, arm), (_, g) in a_lines.items() if pop == "w07")
    w07_cum = sum(g["candidates"].get("cumulative-reported", 0) for (pop, arm), (_, g) in a_lines.items() if pop == "w07")
    t38_line, t38g = a_lines[("t38", "C-30")]
    say(f"N-15: A:{t38_line} T3.8 C-30 runs {t38g['runs']} step-fails {t38g['candidates'].get('step-fails', 0)} "
        f"cumulative {t38g['candidates'].get('cumulative-reported', 0)}; A w07 (lines "
        f"{sorted(i for (pop, _), (i, _) in a_lines.items() if pop == 'w07')}) runs {w07_runs} step-fails {w07_step} cumulative {w07_cum}; "
        f"earlier measured-traffic C runs {t38g['runs'] + w07_runs}, records {t38g['candidates'].get('step-fails', 0) + w07_step + w07_cum}")
    total_runs = t38g["runs"] + w07_runs + len(CELLS)
    total_rec = t38g["candidates"].get("step-fails", 0) + w07_step + w07_cum + PR["C-120"]["total"]
    say(f"N-15: + Stage 1a C-120 runs {len(CELLS)} records {PR['C-120']['total']} (cumulative-only {PR['C-120']['own'].get('cumulative-only', 0)}) "
        f"=> runs {total_runs}, records {total_rec}, cumulative-only {w07_cum + t38g['candidates'].get('cumulative-reported', 0) + PR['C-120']['own'].get('cumulative-only', 0)}; "
        f"my C-30 recount {PR['C-30']['total']} vs A {t38g['candidates'].get('step-fails', 0)}")

    # 6. shared rides (N-09)
    say("\n## 6. Shared completions (served riders)")
    for arm in ARMS:
        srv = [x for _, x in served_of[arm]]
        sh = sum(1 for x in srv if x["shared"])
        say(f"- {arm}: {sh} of {len(srv)} served ({pct(sh, len(srv)):.2f}%); per request {pct(sh, REQ):.2f}%")
    say(f"  U - C-30 shared = {sum(1 for _, x in served_of['U'] if x['shared']) - sum(1 for _, x in served_of['C-30'] if x['shared'])}")

    # 7. overlaps (N-10)
    say("\n## 7. Served-set overlaps ((cell, requestId))")
    S = {arm: {(c, x["rid"]) for c, x in served_of[arm]} for arm in ARMS}
    for a, b in (("C-120", "C-30"), ("C-120", "U"), ("U", "C-30"), ("C-30", "Mplus-30")):
        say(f"- {a} vs {b}: common {len(S[a] & S[b])}; only {a} {len(S[a] - S[b])}; only {b} {len(S[b] - S[a])}")
    say(f"  C-120-only (vs C-30) also served by U: {len((S['C-120'] - S['C-30']) & S['U'])} of {len(S['C-120'] - S['C-30'])}")

    # 8. per window and per cell (N-11, C30, Bang 4.7)
    say("\n## 8. Per window (requests = 108 x cells)")
    for w in ("w07", "w08", "w17"):
        cs = [c for c in CELLS if c.endswith(w)]
        for arm in ARMS:
            srv = [x for c, x in served_of[arm] if c.endswith(w)]
            nv, fc_ = frontier(srv, "naive"), frontier(srv, "fc")
            say(f"- {w} ({len(cs)} cells, {108 * len(cs)} requests) {arm:<8}: served {nv['served']}; late60 {nv['late60']}; timely60 "
                f"{nv['timely60']}; timely120 {nv['timely120']}; fc late60 {fc_['late60']}; fc timely60 {fc_['timely60']}")
    def served_cell(arm, c):
        return sum(1 for x in R[(arm, c)]["riders"] if x["A"] is not None)
    def late_cell(arm, c, qn="naive"):
        return sum(1 for x in R[(arm, c)]["riders"] if x["A"] is not None and x["A"] - quote_value(x, qn) > 60_000)
    for a, b in (("C-120", "C-30"), ("C-120", "U"), ("U", "C-30")):
        d = [served_cell(a, c) - served_cell(b, c) for c in CELLS]
        say(f"  per cell served {a} vs {b}: more {sum(v > 0 for v in d)}, equal {sum(v == 0 for v in d)}, fewer {sum(v < 0 for v in d)}")
    say("\n## 8b. Per cell late60 (naive) U vs C-30, by window (REG C30 fallback)")
    for w in ("w07", "w08", "w17"):
        cs = [c for c in CELLS if c.endswith(w)]
        d = [late_cell("U", c) - late_cell("C-30", c) for c in cs]
        say(f"- {w}: cells {len(cs)}; U more late {sum(v > 0 for v in d)}, equal {sum(v == 0 for v in d)}, U fewer {sum(v < 0 for v in d)}")
    say("\n## 8c. Day x window, C-30 minus U (naive quote; counts summed over the cells of the group) [table for Bang 4.7]")
    say("day   window cells | late60 U  C-30  C-U | timely60 U  C-30  C-U | served U C-30 C-U | cells C late60 <=U | cells C timely60 >=U")
    T47 = []
    for day in ("14", "15", "16", "17", "18"):
        for w in ("w07", "w08", "w17"):
            cs = [c for c in CELLS if c[7:9] == day and c.endswith(w)]
            if not cs:
                continue
            lu, lc = sum(late_cell("U", c) for c in cs), sum(late_cell("C-30", c) for c in cs)
            su, sc = sum(served_cell("U", c) for c in cs), sum(served_cell("C-30", c) for c in cs)
            tu, tc = su - lu, sc - lc
            nl = sum(1 for c in cs if late_cell("C-30", c) <= late_cell("U", c))
            nt = sum(1 for c in cs if served_cell("C-30", c) - late_cell("C-30", c) >= served_cell("U", c) - late_cell("U", c))
            T47.append({"day": day, "window": w, "cells": len(cs), "late60_U": lu, "late60_C30": lc, "timely60_U": tu,
                        "timely60_C30": tc, "served_U": su, "served_C30": sc, "cells_C_late_le_U": nl, "cells_C_timely_ge_U": nt})
            say(f"11-{day} {w}    {len(cs):2d}   | {lu:4d} {lc:4d} {lc - lu:+4d} | {tu:5d} {tc:5d} {tc - tu:+4d} | {su:4d} {sc:4d} {sc - su:+4d} | "
                f"{nl}/{len(cs)} | {nt}/{len(cs)}")
    say(f"  totals: late60 C-U {sum(t['late60_C30'] - t['late60_U'] for t in T47)}; timely60 C-U "
        f"{sum(t['timely60_C30'] - t['timely60_U'] for t in T47)}; cells with C late60 <= U {sum(t['cells_C_late_le_U'] for t in T47)}/34; "
        f"cells with C timely60 >= U {sum(t['cells_C_timely_ge_U'] for t in T47)}/34")
    J["table_4_7"] = T47

    # 9. own-rule obligations (28 of 34; Bang 4.5 subset for Mplus-30)
    say("\n## 9. Own-rule obligations per cell")
    own_m = {}
    for c in CELLS:
        rs = [x for x in R[("Mplus-30", c)]["riders"] if x["A"] is not None]
        own_m[c] = (sum(1 for x in rs if x["A"] - x["p0"] > 30_000), len(rs))
    forced = {c: R[("Mplus-30", c)]["nonNormal"] / R[("Mplus-30", c)]["decisionsAcknowledged"] for c in CELLS}
    for group, cs in (("all", list(CELLS)), ("w07", [c for c in CELLS if c.endswith("w07")]),
                      ("w08", [c for c in CELLS if c.endswith("w08")]), ("w17", [c for c in CELLS if c.endswith("w17")])):
        shares = [own_m[c][0] / own_m[c][1] for c in cs]
        say(f"- Mplus-30 {group} ({len(cs)} cells): cells with >= 1 own-promise break {sum(1 for c in cs if own_m[c][0] > 0)}; "
            f"cell-mean break share {100 * statistics.mean(shares):.2f}%; pooled {sum(own_m[c][0] for c in cs)}/"
            f"{sum(own_m[c][1] for c in cs)} = {pct(sum(own_m[c][0] for c in cs), sum(own_m[c][1] for c in cs)):.2f}%; "
            f"cell-mean forced share {100 * statistics.mean(forced[c] for c in cs):.2f}%; pooled forced "
            f"{sum(R[('Mplus-30', c)]['nonNormal'] for c in cs)}/{sum(R[('Mplus-30', c)]['decisionsAcknowledged'] for c in cs)} = "
            f"{pct(sum(R[('Mplus-30', c)]['nonNormal'] for c in cs), sum(R[('Mplus-30', c)]['decisionsAcknowledged'] for c in cs)):.2f}%")
    say(f"- C-30: cells with >= 1 rider S > 30 s: {EX['C-30']['own_break_cells']}; forced decisions "
        f"{sum(R[('C-30', c)]['nonNormal'] for c in CELLS)}; C-120: cells with >= 1 rider S > 120 s: {EX['C-120']['own_break_cells']}")

    # 10. Stage 1a text arithmetic (section 7.1 of OUTLINE-V2)
    say("\n## 10. Stage 1a arithmetic (C-120 minus C-30 unless stated)")
    n120, n30, nu = F[("C-120", "naive")], F[("C-30", "naive")], F[("U", "naive")]
    f120, f30 = F[("C-120", "fc")], F[("C-30", "fc")]
    say(f"served {n120['served']} - {n30['served']} = {n120['served'] - n30['served']}; late60 {n120['late60'] - n30['late60']:+d}; "
        f"timely60 {n120['timely60'] - n30['timely60']:+d}; timely120 {n120['timely120'] - n30['timely120']:+d}; "
        f"fc timely60 {f120['timely60'] - f30['timely60']:+d}; fc timely120 {f120['timely120'] - f30['timely120']:+d}; "
        f"ext {f120['ext_mean_s']:.4f} vs {f30['ext_mean_s']:.4f} s")
    say(f"C-120 timely120 {n120['timely120']} vs U {nu['timely120']} and C-30 {n30['timely120']}; C-120 served {n120['served']} "
        f"between C-30 {n30['served']} and U {nu['served']}; late>300 C-120 {n120['late300']}; early60 C-120 naive "
        f"{n120['early60']} fc {f120['early60']}")
    for arm in ("U", "C-30", "C-120"):
        say(f"  {arm}: naive late60/120/300 {F[(arm, 'naive')]['late60']} / {F[(arm, 'naive')]['late120']} / {F[(arm, 'naive')]['late300']}; "
            f"timely60/120 {F[(arm, 'naive')]['timely60']} / {F[(arm, 'naive')]['timely120']}; fc timely60/120 "
            f"{F[(arm, 'fc')]['timely60']} / {F[(arm, 'fc')]['timely120']}; fc ext {F[(arm, 'fc')]['ext_mean_s']:.4f} s")

    text = "\n".join(out) + "\n"
    with open(OUT_TXT, "x", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    with open(OUT_JSON, "x", encoding="utf-8", newline="\n") as fh:
        json.dump(J, fh, indent=1, sort_keys=True, default=str)
    sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
