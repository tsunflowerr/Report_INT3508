"""R21 Stage 1a (Claude analyst), step 2: tables and P1-P5 from the extraction files of extract_stage1a.py.

Reads <prefix>-riders.tsv and <prefix>-runs.json only (no transcript). Definitions (served riders = accepted riders
with a passengerAlighted event; lateness against the FIRST drop promise p0; requests = 3,672 per arm):
  naive late_k = A - p0 > k s; early60 = A - p0 < -60 s; timely_k = served - late_k (A - p0 <= k s), per request;
  forecast (causal-no15, D0 = display_layer.display(t0, p0, profile), naive in inactive cells) late_k = A - D0 > k s,
  timely_k = served - late_k, early60 = A - D0 < -60 s, mean quote extension = mean (D0 - p0) over served riders;
  dispatch use over ACCEPTED riders: S = sum |c| of later drop revisions, exposed = S > 0, k = revisions with c != 0;
  nearest-rank percentiles = budget_use_check.q; shared = another alighted rider on the same vehicle on board at an
  overlapping time.
Baselines are checked first (task brief); if any fails the report says so and stops before the C-120 tables.
Usage: python -B report_stage1a.py <prefix> <out.txt>   (out opened with mode "x")
"""
from __future__ import annotations

import collections
import json
import pathlib
import statistics
import sys

CW = pathlib.Path(r"E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/claude-work")
sys.path.insert(0, str(CW))
sys.path.insert(0, str(CW.parents[1]))
from budget_use_check import q  # noqa: E402  (nearest-rank percentile, reused)

ARMS = ("U", "C-30", "C-120")
BUDGET_MS = {"U": None, "C-30": 30_000, "C-120": 120_000}
REQ = 3672
WINDOWS = ("w07", "w08", "w17")
BASELINES = {  # task brief; (arm, metric) -> expected
    ("U", "served"): 2434, ("C-30", "served"): 2338,
    ("U", "late60"): 203, ("C-30", "late60"): 76,
    ("U", "late120"): 102, ("C-30", "late120"): 11,
    ("U", "timely60"): 2231, ("C-30", "timely60"): 2262,
    ("U", "timely120"): 2332, ("C-30", "timely120"): 2327,
    ("U", "fc_late60"): 137, ("C-30", "fc_late60"): 10,
    ("U", "fc_timely60"): 2297, ("C-30", "fc_timely60"): 2328,
}


def load(prefix):
    riders = collections.defaultdict(list)
    with open(f"{prefix}-riders.tsv", encoding="utf-8") as fh:
        header = fh.readline().rstrip("\n").split("\t")
        for line in fh:
            r = dict(zip(header, line.rstrip("\n").split("\t")))
            rec = {"cell": r["cell"], "id": r["requestId"], "life": r["lifecycle"], "t0": int(r["t0"]),
                   "p0": int(r["p0"]), "D0": float(r["D0"]), "A": int(r["A"]) if r["A"] else None,
                   "S": int(r["sumAbsC"]), "k": int(r["nonzeroC"]), "net": int(r["netC"]), "shared": r["shared"] == "1"}
            riders[r["arm"]].append(rec)
    runs = json.loads(pathlib.Path(f"{prefix}-runs.json").read_text(encoding="utf-8"))
    return riders, runs


def outcome(rs, requests):
    served = [r for r in rs if r["A"] is not None]
    n = len(served)
    m = {"requests": requests, "accepted": len(rs), "served": n}
    for k in (60, 120, 300):
        m[f"late{k}"] = sum(1 for r in served if r["A"] - r["p0"] > k * 1000)
        m[f"fc_late{k}"] = sum(1 for r in served if r["A"] - r["D0"] > k * 1000)
    m["early60"] = sum(1 for r in served if r["A"] - r["p0"] < -60_000)
    m["fc_early60"] = sum(1 for r in served if r["A"] - r["D0"] < -60_000)
    for k in (60, 120):
        m[f"timely{k}"] = n - m[f"late{k}"]
        m[f"fc_timely{k}"] = n - m[f"fc_late{k}"]
    m["fc_ext_s"] = statistics.mean(r["D0"] - r["p0"] for r in served) / 1000 if n else float("nan")
    m["shared"] = sum(1 for r in served if r["shared"])
    return m


def pct(a, b):
    return 100 * a / b if b else float("nan")


def main(prefix, out):
    riders, runs = load(prefix)
    L = []
    say = L.append
    say(f"# report_stage1a.py prefix={pathlib.Path(prefix).name}; arms {ARMS}; 34 T3.8 test cells; {REQ} requests per arm")
    by_arm = collections.defaultdict(list)
    for rec in runs:
        by_arm[rec["arm"]].append(rec)
    # 0. validity of the inputs
    say("\n## 0. Input validity (per arm)")
    for arm in ARMS:
        rs = by_arm[arm]
        status = collections.Counter(r["summaryStatus"] for r in rs)
        run00 = collections.Counter(r["run00Status"] for r in rs)
        inv = sorted({r["repositoryInventorySha256"] for r in rs})
        req = sum(r["requests"] for r in rs)
        life = collections.Counter()
        for r in rs:
            life.update(r["lifecycle"])
        own_eq = all(r["pruneClassesOwn"] == r["pruneClassesJudge"] for r in rs)
        limits = collections.Counter()
        for r in rs:
            limits.update({int(k): v for k, v in r["dropWitnessLimits"].items()})
        promised = sum(r["promisedRiders"] for r in rs)
        alight_np = sum(r["alightedWithoutPromise"] for r in rs)
        served_rows = sum(1 for x in riders[arm] if x["A"] is not None)
        say(f"- {arm}: runs {len(rs)}; summary status {dict(status)}; run-00 status {dict(run00)}; inventory {[i[:8] for i in inv]}; "
            f"requests {req}; lifecycle {dict(sorted(life.items()))}; promised riders {promised} (rider rows {len(riders[arm])}); "
            f"served rows {served_rows} vs lifecycle completed {life.get('completed', 0)}; alighted without promise {alight_np}; "
            f"forecast-active cells {sum(r['forecastActive'] for r in rs)}; prune classes own == judge in every run: {own_eq}; "
            f"drop-witness limit values {dict(sorted(limits.items()))}")
    reqs = {arm: sum(r["requests"] for r in by_arm[arm]) for arm in ARMS}
    req_w = {arm: {w: sum(r["requests"] for r in by_arm[arm] if r["cell"].endswith(w)) for w in WINDOWS} for arm in ARMS}
    M = {arm: outcome(riders[arm], reqs[arm]) for arm in ARMS}
    # 1. baselines
    say("\n## 1. Baseline reproduction (archived T3.8 U and C-30; task brief values)")
    ok_all = True
    for (arm, key), want in BASELINES.items():
        got = M[arm][key]
        ok = got == want
        ok_all &= ok
        say(f"- {arm:<5} {key:<12} expected {want:5d} got {got:5d}  {'OK' if ok else 'MISMATCH'}")
    say(f"BASELINES {'ALL REPRODUCED' if ok_all else 'NOT REPRODUCED -> STOP'}")
    if not ok_all:
        write(out, L)
        return 1
    # 2. outcomes
    say("\n## 2. Outcomes vs the FIRST drop promise (served riders; per-request shares over 3,672)")
    say("arm   | served (share req) | naive late>60 | late>120 | late>300 | early>60 | timely<=60 (per req) | timely<=120 (per req)")
    for arm in ARMS:
        m = M[arm]
        n = m["served"]
        say(f"{arm:<5} | {n:5d} ({pct(n, m['requests']):5.2f}%) | {m['late60']:4d} ({pct(m['late60'], n):5.2f}%) | "
            f"{m['late120']:4d} ({pct(m['late120'], n):4.2f}%) | {m['late300']:3d} ({pct(m['late300'], n):4.2f}%) | "
            f"{m['early60']:3d} ({pct(m['early60'], n):4.2f}%) | {m['timely60']:5d} ({pct(m['timely60'], m['requests']):5.2f}%) | "
            f"{m['timely120']:5d} ({pct(m['timely120'], m['requests']):5.2f}%)")
    say("forecast quote (causal-no15, D0 = display(t0, p0); naive in inactive cells):")
    say("arm   | fc late>60 | fc late>120 | fc late>300 | fc early>60 | fc timely<=60 (per req) | fc timely<=120 (per req) | mean quote extension")
    for arm in ARMS:
        m = M[arm]
        n = m["served"]
        say(f"{arm:<5} | {m['fc_late60']:4d} ({pct(m['fc_late60'], n):4.2f}%) | {m['fc_late120']:3d} ({pct(m['fc_late120'], n):4.2f}%) | "
            f"{m['fc_late300']:3d} | {m['fc_early60']:3d} ({pct(m['fc_early60'], n):4.2f}%) | "
            f"{m['fc_timely60']:5d} ({pct(m['fc_timely60'], m['requests']):5.2f}%) | "
            f"{m['fc_timely120']:5d} ({pct(m['fc_timely120'], m['requests']):5.2f}%) | {m['fc_ext_s']:5.2f} s")
    # 3. dispatch-budget use
    say("\n## 3. Dispatch changes of the drop promise (ACCEPTED riders; S = sum |c| of later drop revisions)")
    D = {}
    for arm in ARMS:
        rs = riders[arm]
        n = len(rs)
        exp = [r["S"] / 1000 for r in rs if r["S"] > 0]
        exp_served = sum(1 for r in rs if r["S"] > 0 and r["A"] is not None)
        k2 = sum(1 for r in rs if r["k"] >= 2)
        kmax = max((r["k"] for r in rs), default=0)
        neg = sum(1 for r in rs if r["S"] > 0 and r["net"] < 0)
        b = BUDGET_MS[arm]
        d = {"n": n, "exposed": len(exp), "k2": k2, "kmax": kmax, "max_s": max(exp) if exp else 0.0}
        line = (f"- {arm}: accepted {n}; drop-exposed {len(exp)} ({pct(len(exp), n):.2f}%; served among them {exp_served}); "
                f"riders with >=2 nonzero c {k2} (max k {kmax}); S among exposed: mean {statistics.mean(exp) if exp else float('nan'):.1f} s, "
                f"p50 {q(exp, 0.5):.1f}, p90 {q(exp, 0.9):.1f}, max {max(exp) if exp else float('nan'):.1f}; "
                f"exposed with net signed c < 0: {neg}")
        if b:
            ge90 = sum(1 for r in rs if r["S"] >= 0.9 * b)
            over = sum(1 for r in rs if r["S"] > b)
            over_tol = sum(1 for r in rs if r["S"] > b + 1)
            d.update(ge90=ge90, over=over, over_tol=over_tol)
            line += (f"; S >= 0.9 B ({0.9 * b / 1000:.0f} s): {ge90}; S >= 0.5 B: {sum(1 for r in rs if r['S'] >= 0.5 * b)}; "
                     f"overshoots S > B: {over} (S > B + 1 ms: {over_tol})")
        else:
            line += ("; (no budget) S >= 27 s: " + str(sum(1 for r in rs if r["S"] >= 27_000))
                     + ", S > 30 s: " + str(sum(1 for r in rs if r["S"] > 30_000))
                     + ", S >= 108 s: " + str(sum(1 for r in rs if r["S"] >= 108_000))
                     + ", S > 120 s: " + str(sum(1 for r in rs if r["S"] > 120_000)))
        D[arm] = d
        say(line)
    # 4. prune records, non-normal decisions
    say("\n## 4. Budget prune records (acknowledged decisions; recorded first-failing drop witness only) and forced decisions")
    P = {}
    for arm in ARMS:
        rs = by_arm[arm]
        cls = collections.Counter()
        for r in rs:
            cls.update(r["pruneClassesJudge"])
        dec_cum = sum(r["judgeDecisionsWithCumulativeOnly"] for r in rs)
        req_cum = sum(r["judgeRequestsWithCumulativeOnly"] for r in rs)
        rej_cum = sum(r["judgeOfWhichFinallyRejected"] for r in rs)
        nn = sum(r["nonNormalCertificates"] for r in rs)
        acked = sum(r["decisionsAcknowledged"] for r in rs)
        forced = sum(r["ridersWithForcedBreach"] for r in rs)
        fref = sum((r["breaches"] or {}).get("forcedReference", 0) for r in rs)
        runs_cum = [r["cell"] for r in rs if r["pruneClassesJudge"].get("cumulative-only")]
        P[arm] = {"cls": cls, "nonnormal": nn}
        say(f"- {arm}: budget-pruned candidates {sum(cls.values())} by class {dict(sorted(cls.items()))}; "
            f"single-step (per-step-also) {cls.get('per-step-also', 0)}; cumulative-only {cls.get('cumulative-only', 0)} "
            f"in runs {runs_cum}; decisions with >=1 cumulative-only {dec_cum}; distinct new requests in them {req_cum}, "
            f"finally rejected {rej_cum}; acknowledged decisions {acked}; non-normal (forced) decisions {nn}; "
            f"riders with forced-reference breach {forced}; forcedReference breaches {fref}")
        for r in rs:
            for det in r["cumulativeOnlyOwn"]:
                say(f"    cumulative-only record: {arm} {r['cell']} new {det['newRequestIds']} witness "
                    f"(rider, before_ms, delta_ms, after_ms, limit_ms) {det['witness']}")
    # 5. shared rides
    say("\n## 5. Shared rides (served rider with another rider on board at an overlapping time, same vehicle)")
    for arm in ARMS:
        m = M[arm]
        say(f"- {arm}: shared completions {m['shared']} of {m['served']} served ({pct(m['shared'], m['served']):.2f}%); "
            f"per request {pct(m['shared'], m['requests']):.2f}%")
    # 6. served-set overlap
    say("\n## 6. Served-set overlap ((cell, requestId) of served riders)")
    sets = {arm: {(r["cell"], r["id"]) for r in riders[arm] if r["A"] is not None} for arm in ARMS}
    for a, b in (("C-120", "C-30"), ("C-120", "U"), ("U", "C-30")):
        sa, sb = sets[a], sets[b]
        say(f"- {a} vs {b}: common {len(sa & sb)}; only {a} {len(sa - sb)}; only {b} {len(sb - sa)}")
    only_both = sets["C-120"] - sets["C-30"]
    say(f"  C-120-only (vs C-30) riders also served by U: {len(only_both & sets['U'])} of {len(only_both)}")
    # 7. per window
    say("\n## 7. Per window (served; naive late>60; timely<=60 per window requests; forecast late>60 / timely<=60)")
    W = {}
    for w in WINDOWS:
        for arm in ARMS:
            rs = [r for r in riders[arm] if r["cell"].endswith(w)]
            m = outcome(rs, req_w[arm][w])
            W[(arm, w)] = m
            say(f"- {w} {arm:<5}: requests {m['requests']}; served {m['served']}; late>60 {m['late60']} "
                f"({pct(m['late60'], m['served']):.2f}%); timely<=60 {m['timely60']} ({pct(m['timely60'], m['requests']):.2f}%); "
                f"timely<=120 {m['timely120']}; fc late>60 {m['fc_late60']}; fc timely<=60 {m['fc_timely60']}")
    # per cell served comparison
    say("\n## 8. Per cell served, C-120 vs C-30 and vs U (counts of cells)")
    cell_served = {arm: collections.Counter(r["cell"] for r in riders[arm] if r["A"] is not None) for arm in ARMS}
    cells = sorted({r["cell"] for r in runs})
    for other in ("C-30", "U"):
        gt = sum(1 for c in cells if cell_served["C-120"][c] > cell_served[other][c])
        eq = sum(1 for c in cells if cell_served["C-120"][c] == cell_served[other][c])
        lt = sum(1 for c in cells if cell_served["C-120"][c] < cell_served[other][c])
        say(f"- C-120 vs {other}: more served in {gt} cells, equal in {eq}, fewer in {lt}")
    # extra validation against earlier outputs
    say("\n## 9. Extra validation against earlier Claude outputs (not stop rules)")
    say(f"- U/C-30 drop-exposed {D['U']['exposed']}/{D['C-30']['exposed']} (budget-use-check-2026-10-09.txt: 174/33); "
        f"C-30 S >= 0.9 B {D['C-30']['ge90']} (4); U max S {D['U']['max_s']:.1f} s (590.1); C-30 max S {D['C-30']['max_s']:.1f} s (29.2)")
    say(f"- C-30 prune classes {dict(P['C-30']['cls'])} (cumulative-decisive-check-2026-10-10.txt: per-step-also 845)")
    say(f"- shared U {pct(M['U']['shared'], M['U']['served']):.2f}% / C-30 {pct(M['C-30']['shared'], M['C-30']['served']):.2f}% "
        f"(q2-cap-dial-t38-v2-2026-10-10.txt: 22.80% / 13.39%)")
    say(f"- forecast mean extension U {M['U']['fc_ext_s']:.1f} s / C-30 {M['C-30']['fc_ext_s']:.1f} s (cap-vs-pad-frontier: 7.2 / 7.4)")
    # P1-P5
    say("\n## 10. Predictions of C120-PLAN.md (sealed), evaluated as written")
    c = by_arm["C-120"]
    all_pass = all(r["summaryStatus"] == "pass" for r in c) and len(c) == 34
    p1 = all_pass and P["C-120"]["nonnormal"] == 0 and D["C-120"]["over"] == 0
    say(f"P1 {'PASS' if p1 else 'FAIL'}: jobs with status pass {sum(r['summaryStatus'] == 'pass' for r in c)}/34; "
        f"non-normal (forced) decisions {P['C-120']['nonnormal']}; riders with sum|c| > 120 s {D['C-120']['over']}")
    s = M["C-120"]["served"]
    say(f"P2 {'PASS' if s >= 2362 else 'FAIL'}: served {s} (needs >= 2,362; C-30 {M['C-30']['served']}, U {M['U']['served']}; "
        f"gap recovered {s - M['C-30']['served']} of {M['U']['served'] - M['C-30']['served']})")
    l60 = M["C-120"]["late60"]
    say(f"P3 {'PASS' if 76 < l60 < 203 else 'FAIL'}: naive late>60 {l60} (needs strictly between 76 and 203)")
    t120 = M["C-120"]["timely120"]
    say(f"P4 {'PASS' if t120 >= 2327 else 'FAIL'}: timely<=120 {t120} (needs >= 2,327)")
    cum = P["C-120"]["cls"].get("cumulative-only", 0)
    say(f"P5 {'PASS' if cum <= 2 else 'FAIL'}: recorded cumulative-only drop-budget prune records {cum} (needs <= 2)")
    write(out, L)
    return 0


def write(out, lines):
    text = "\n".join(lines) + "\n"
    with open(out, "x", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    sys.stdout.write(text)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    raise SystemExit(main(sys.argv[1], sys.argv[2]))
