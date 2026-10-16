"""R21 Stage 1a (Claude analyst), step 1: per-rider and per-run extraction, read-only on the runs.

Arms and runs (34 T3.8 test cells, tang3/t38/split-t38-v1.json "test"):
  U, C-30  : archived T3.8 runs, resolved by forecast_family_a.run_dir("test", arm, cell) (handles -rerun1)
  C-120    : C:/RideBoundData/research/tier3-t38c120-v1/C-120-<cell> (Stage 1a; plan tang3/t38c120/C120-PLAN.md)
Readers reused unchanged (imports only):
  tang3/evidence/audit_vep.py      load / audit: final checkpoint, signed ledger rows (v, e, p, x, c, z, closed),
                                   summary (lifecycle, nonNormalCertificates, forced breaches)
  tang3/sweep/sweep_analyze.py     event_times: first passengerBoarded / passengerAlighted adapter batch simTimeMs
  optimize/display_layer.py        causal-no15 profile + display(t0, p0, prof) exactly as cap_vs_pad_frontier.py
                                   (D0 = display of the FIRST drop promise; naive where the rule is inactive)
  r13-final-judge/cumulative_decisive_check.py  analyze(job): budget-pruned candidate classes of acknowledged
                                   decisions (per-step-also / cumulative-only / unclassified / lock-like)
The only wrapper: audit_vep.load is memoised for the current transcript so audit() does not parse it twice (the
function itself is unchanged). A second, own read of the prune records (from the same load() decisions) records the
drop-witness limit values and re-derives the classes as a cross-check of analyze().
Per rider (every request with a drop initialPromise = accepted):
  t0, p0 = publishedAtMs, p of the drop initialPromise; D0 = display(t0, p0, causal-no15 profile of the cell);
  A = passengerAlighted simTimeMs (empty if never alighted); S = sum |c| over later drop revisions (ms);
  k = number of later drop revisions with c != 0; net = sum c; shared = another alighted rider on the same vehicle
  with an overlapping on-board interval [actualPickupTimeMs, A) (rule of q2_cap_dial.py / wp14r_ladder_reanalysis.py).
Usage: python -B extract_stage1a.py <out-prefix>   -> <prefix>-riders.tsv, <prefix>-runs.json (mode "x"; 2 processes)
"""
from __future__ import annotations

import collections
import json
import pathlib
import sys
from concurrent.futures import ProcessPoolExecutor

OPT = pathlib.Path(r"E:/Code/Report_INT3508/ridebound-scratchpad/optimize")
JUDGE = OPT / "codex-debate" / "claude-work" / "r13-final-judge"
sys.path.insert(0, str(OPT))
sys.path.insert(0, str(JUDGE))
import display_layer as dl  # noqa: E402
import forecast_family_a as fa  # noqa: E402
import cumulative_decisive_check as cdc  # noqa: E402

C120_ROOT = pathlib.Path(r"C:/RideBoundData/research/tier3-t38c120-v1")
CELLS = tuple(fa.run_t38.PHASES["test"][1])
ARMS = ("U", "C-30", "C-120")

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


def own_prune_classes(decisions, acknowledged):
    """Same class rule as cumulative_decisive_check.analyze, read from audit_vep.load decisions; plus limits seen."""
    cls_count = collections.Counter()
    limits = collections.Counter()
    cum_detail = []
    for h, payload in decisions.items():
        if h not in acknowledged:
            continue
        ev = ((payload.get("solver") or {}).get("executionEvidence") or {})
        for pc in ev.get("prunedCandidates", []):
            if pc.get("code") != "COMMITMENT_BUDGET_EXCEEDED":
                continue
            ws = [w for w in pc.get("commitmentWitnesses", []) if w.get("code") == "COMMITMENT_BUDGET_EXCEEDED"]
            drop = [w for w in ws if w.get("dimension") == "drop_eta_total_ms"]
            other = [w for w in ws if w.get("dimension") != "drop_eta_total_ms"]
            for w in drop:
                limits[w["limit"]] += 1
            if drop:
                if any(w["delta"] > w["limit"] for w in drop):
                    cls = "per-step-also"
                elif all(w["before"] > 0 and w["delta"] <= w["limit"] < w["after"] for w in drop):
                    cls = "cumulative-only"
                    cum_detail.append({"decisionHash": h, "newRequestIds": pc.get("newRequestIds", []),
                                       "witness": [(w["requestId"], w["before"], w["delta"], w["after"], w["limit"])
                                                   for w in drop]})
                else:
                    cls = "unclassified"
            elif other:
                cls = "lock-like:" + ",".join(sorted({w["dimension"] for w in other}))
            else:
                cls = "no-witness"
            cls_count[cls] += 1
    return dict(cls_count), {str(k): v for k, v in limits.items()}, cum_detail


def job(arg):
    arm, cell = arg
    run = run_dir(arm, cell)
    transcript = run / "transcript-00.ndjson"
    summary_json = json.loads((run / "summary.json").read_text(encoding="utf-8"))
    run00 = json.loads((run / "run-00.json").read_text(encoding="utf-8"))
    decisions, acknowledged, state = fa.audit_vep.load(transcript)
    table, summary = fa.audit_vep.audit(transcript)
    if table is None:
        raise SystemExit(f"{run}: no final checkpoint")
    _, alighted = fa.sweep_analyze.event_times(transcript)
    prof = dl.profile(fa.day_of(cell), cell[-3:], "causal-no15")
    first, s_drop, k_drop, net = {}, collections.defaultdict(int), collections.defaultdict(int), collections.defaultdict(int)
    first_kind_check = {}
    for r, coord, seq, kind, pub, v, e, p, x, cc, z, closed in table:
        if coord != "drop":
            continue
        first_kind_check.setdefault(r, (seq, kind))
        if seq < first_kind_check[r][0]:
            first_kind_check[r] = (seq, kind)
        if kind == "initialPromise":
            if r in first:
                raise SystemExit(f"{run}: {r} has two drop initialPromise rows")
            first[r] = (pub, p)
            continue
        s_drop[r] += abs(cc)
        k_drop[r] += cc != 0
        net[r] += cc
    bad_first = [r for r, (seq, kind) in first_kind_check.items() if kind != "initialPromise"]
    if bad_first:
        raise SystemExit(f"{run}: first drop entry not initialPromise for {bad_first[:3]}")
    if sum(s_drop.values()) != summary["sumDropC"]:
        raise SystemExit(f"{run}: per-rider sum |c| {sum(s_drop.values())} != audit sumDropC {summary['sumDropC']}")
    reqs = state["requests"]
    legs = collections.defaultdict(list)
    for q in reqs:
        if q["requestId"] in alighted:
            legs[q["assignedVehicleId"]].append((q["actualPickupTimeMs"], alighted[q["requestId"]], q["requestId"]))
    shared = set()
    for rs in legs.values():
        for a0, a1, rid in rs:
            if any(o != rid and b0 < a1 and a0 < b1 for b0, b1, o in rs):
                shared.add(rid)
    life = {q["requestId"]: q["lifecycle"] for q in reqs}
    rows = []
    for r in sorted(first):
        t0, p0 = first[r]
        d0 = dl.display(t0, p0, prof)
        rows.append((arm, cell, r, life.get(r, ""), t0, p0, repr(d0), alighted.get(r, ""), s_drop[r], k_drop[r],
                     net[r], int(r in shared)))
    own_cls, limits, cum_detail = own_prune_classes(decisions, acknowledged)
    judged = cdc.analyze(("stage1a", arm, transcript))
    rec = {
        "arm": arm, "cell": cell, "run": str(run), "summaryStatus": summary_json.get("status"),
        "run00Status": run00.get("status"), "repositoryInventorySha256": summary_json.get("repositoryInventorySha256"),
        "requests": summary["requests"], "lifecycle": summary["lifecycle"], "promisedRiders": summary["promisedRiders"],
        "alighted": len(alighted), "alightedWithoutPromise": sum(1 for r in alighted if r not in first),
        "decisionsAcknowledged": summary["decisionsAcknowledged"], "decisionFrames": len(decisions),
        "nonNormalCertificates": summary["nonNormalCertificates"], "ridersWithForcedBreach": summary["ridersWithForcedBreach"],
        "breaches": summary["breaches"], "latePickups": summary["latePickups"], "sumDropC": summary["sumDropC"],
        "forecastActive": prof is not None,
        "pruneClassesOwn": own_cls, "dropWitnessLimits": limits, "cumulativeOnlyOwn": cum_detail,
        "pruneClassesJudge": judged["candidates"], "judgeAckedDecisions": judged["acked_decisions"],
        "judgeDecisionsWithCumulativeOnly": judged["decisions_with_cumulative_only"],
        "judgeRequestsWithCumulativeOnly": judged["requests_with_cumulative_only_candidate"],
        "judgeOfWhichFinallyRejected": judged["of_which_finally_rejected"], "judgeServed": judged["served"],
        "judgeExamples": judged["examples"],
    }
    _cache.clear()
    return rows, rec


def main(prefix: str) -> int:
    items = [(arm, cell) for arm in ARMS for cell in CELLS]
    with ProcessPoolExecutor(max_workers=2) as pool:
        results = list(pool.map(job, items))
    riders_path = pathlib.Path(f"{prefix}-riders.tsv")
    runs_path = pathlib.Path(f"{prefix}-runs.json")
    with open(riders_path, "x", encoding="utf-8", newline="\n") as fh:
        fh.write("arm\tcell\trequestId\tlifecycle\tt0\tp0\tD0\tA\tsumAbsC\tnonzeroC\tnetC\tshared\n")
        for rows, _ in results:
            for row in rows:
                fh.write("\t".join(str(x) for x in row) + "\n")
    with open(runs_path, "x", encoding="utf-8", newline="\n") as fh:
        json.dump([rec for _, rec in results], fh, indent=1)
    print(f"written {riders_path} ({sum(len(r) for r, _ in results)} rider rows) and {runs_path} ({len(results)} runs)")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    raise SystemExit(main(sys.argv[1]))
