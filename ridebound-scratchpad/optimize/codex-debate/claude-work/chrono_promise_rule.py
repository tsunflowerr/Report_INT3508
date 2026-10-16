"""Chronological out-of-sample test of promise-padding rules (zero-run replay; written after the in-sample screen
slack-bounded-pad-2026-10-07.txt, before any held-out number was computed; run once).

Rule family on the first DROP promise: F = P0 + lam * (D0 - P0) + min(b, a * room)
  D0 = causal-no15 forecast display (naive where inactive), room = first pickup promise + maxRideTime - P0 (s, >= 0).
  uniform family: a = inf; bounded family: a in {0.25, 0.5, 1.0}.  lam in {0, 0.5, 1, 1.5}; b in {0,15,...,240} s.
Selection (fixed in advance): on TRAIN riders, for target T, pick in each family the rule with the smallest mean
extension (F - P0) whose Y60 = share(A - F > 60 s) <= T; ties -> smaller p90 extension. Then report it on TEST.
Folds (weekday cells only; the forecast is active on 14-16/11):
  fold 1: train 14/11, test 15/11 + 16/11;   fold 2: train 14/11 + 15/11, test 16/11.
Arms U and C-30; targets T = 1%, 2%, 3%. Metrics on TEST: Y60, mean / p90 extension, early60, n.
Usage: python -B chrono_promise_rule.py <out> (mode x)."""
import itertools, math, pathlib, statistics as st, sys
OPT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(OPT))
import display_layer as dl, forecast_family_a as fa
CELLS = fa.run_t38.PHASES["test"][1]
LAMS = (0.0, 0.5, 1.0, 1.5)
BS = (0, 15, 30, 45, 60, 90, 120, 180, 240)
AS = (0.25, 0.5, 1.0, math.inf)
def riders(arm):
    out = {}
    for cell in CELLS:
        day = fa.day_of(cell)
        t = fa.run_dir("test", arm, cell) / "transcript-00.ndjson"
        _, _, state = fa.audit_vep.load(t)
        table, _ = fa.audit_vep.audit(t)
        _, alighted = fa.sweep_analyze.event_times(t)
        req = {r["requestId"]: r for r in state["requests"]}
        prof = dl.profile(day, cell[-3:], "causal-no15")
        first = {}
        for r, c, s, k, pub, v, e, p, x, cc, z, closed in table:
            if k == "initialPromise":
                first[(r, c)] = (pub, p)
        for r in req:
            if r in alighted and (r, "drop") in first:
                t0, p0 = first[(r, "drop")]
                room = max(0.0, (first[(r, "pickup")][1] + req[r]["maxRideTimeMs"] - p0) / 1000)
                out.setdefault(day, []).append((p0, dl.display(t0, p0, prof), alighted[r], room))
    return out
def evaluate(rs, lam, b, a):
    ext = [lam * (d - p0) / 1000 + min(b, a * room) for p0, d, A, room in rs]
    late = [(A - p0) / 1000 - e for (p0, d, A, room), e in zip(rs, ext)]
    n = len(rs)
    return dict(Y=sum(1 for v in late if v > 60) / n, ext=st.mean(ext), p90=sorted(ext)[min(n - 1, int(.9 * n))],
                early=sum(1 for v in late if v < -60) / n, n=n)
def choose(train, T, bounded):
    best = None
    for lam, b, a in itertools.product(LAMS, BS, AS):
        if bounded != (a != math.inf) and b > 0:
            continue
        m = evaluate(train, lam, b, a)
        if m["Y"] <= T and (best is None or (m["ext"], m["p90"]) < (best[0]["ext"], best[0]["p90"])):
            best = (m, (lam, b, a))
    return best
out = ["# chrono_promise_rule.py (weekday T3.8 test cells; chronological out-of-sample)"]
for arm in ("U", "C-30"):
    by_day = riders(arm)
    for name, tr_days, te_days in (("fold 1", ["2018-11-14"], ["2018-11-15", "2018-11-16"]),
                                   ("fold 2", ["2018-11-14", "2018-11-15"], ["2018-11-16"])):
        train = [x for d in tr_days for x in by_day[d]]; test = [x for d in te_days for x in by_day[d]]
        base = evaluate(test, 0, 0, math.inf); fc = evaluate(test, 1, 0, math.inf)
        out.append(f"\n== {arm} {name}: train {len(train)} riders {tr_days}, test {len(test)} riders {te_days}")
        out.append(f"  test naive: Y60 {100 * base['Y']:.2f}%;  test fc only: Y60 {100 * fc['Y']:.2f}%, ext {fc['ext']:.1f} s")
        for T in (0.01, 0.02, 0.03):
            for fam, bounded in (("uniform", False), ("bounded", True)):
                pick = choose(train, T, bounded)
                if pick is None:
                    out.append(f"  T {100 * T:.0f}% {fam:<8}: no rule meets the target on train"); continue
                m, (lam, b, a) = pick; te = evaluate(test, lam, b, a)
                out.append(f"  T {100 * T:.0f}% {fam:<8}: rule lam {lam}, b {b}, a {a} | train Y60 {100 * m['Y']:.2f}% ext {m['ext']:.1f} | "
                           f"TEST Y60 {100 * te['Y']:.2f}% ext {te['ext']:.1f} s p90 {te['p90']:.0f} s early60 {100 * te['early']:.1f}%")
text = "\n".join(out) + "\n"
open(sys.argv[1], "x", encoding="utf-8", newline="\n").write(text); print(text)
