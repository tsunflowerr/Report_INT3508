"""Calibration backtest exactly as CALIB-BACKTEST-PLAN.md (sealed 2026-10-07 15:29, SHA-256 6175d2c1...).
Zero-run replay of saved T3.8 test runs U and C-30, weekday cells only. Run once.
Usage: python -B calib_backtest.py <out> (mode x)."""
import itertools, pathlib, statistics as st, sys
OPT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(OPT))
import display_layer as dl, forecast_family_a as fa
CELLS = fa.run_t38.PHASES["test"][1]
DAYS = ("2018-11-14", "2018-11-15", "2018-11-16")
FAM = {"none": [()],
       "uniform": [(b,) for b in (15, 30, 45, 60, 90, 120, 180)],
       "horizon": [(a,) for a in (0.02, 0.04, 0.06, 0.08, 0.10, 0.15, 0.20)],
       "direct": [(a,) for a in (0.05, 0.10, 0.15, 0.20, 0.30, 0.40)],
       "room": [(a, b) for a in (0.25, 0.5, 1.0) for b in (30, 60, 90, 120, 180)]}
def q(fam, par, r):
    if fam == "none": return 0.0
    if fam == "uniform": return par[0]
    if fam == "horizon": return par[0] * r["h"]
    if fam == "direct": return par[0] * r["direct"]
    return min(par[1], par[0] * r["room"])
def riders(arm):
    out = {d: [] for d in DAYS}
    for cell in CELLS:
        day = fa.day_of(cell)
        if day not in out: continue
        t = fa.run_dir("test", arm, cell) / "transcript-00.ndjson"
        _, _, state = fa.audit_vep.load(t)
        table, _ = fa.audit_vep.audit(t)
        _, alighted = fa.sweep_analyze.event_times(t)
        req = {r["requestId"]: r for r in state["requests"]}
        prof = dl.profile(day, cell[-3:], "causal-no15")
        first = {}
        for r, c, s, k, pub, v, e, p, x, cc, z, closed in table:
            if k == "initialPromise": first[(r, c)] = (pub, p)
        for r in req:
            if r in alighted and (r, "drop") in first:
                t0, p0 = first[(r, "drop")]
                out[day].append(dict(p0=p0 / 1000, d0=dl.display(t0, p0, prof) / 1000, A=alighted[r] / 1000,
                                     h=(p0 - t0) / 1000, direct=req[r]["maxRideTimeMs"] / 1500,
                                     room=max(0.0, (first[(r, "pickup")][1] + req[r]["maxRideTimeMs"] - p0) / 1000)))
    return out
def metrics(rs, lam, fam, par):
    ext = [lam * (r["d0"] - r["p0"]) + q(fam, par, r) for r in rs]
    lat = [r["A"] - r["p0"] - e for r, e in zip(rs, ext)]; n = len(rs)
    sh = lambda f: 100 * sum(1 for v in lat if f(v)) / n  # noqa: E731
    return dict(n=n, ext=st.mean(ext), p90=sorted(ext)[min(n - 1, int(.9 * n))], timely=sum(1 for v in lat if v <= 60),
                Y30=sh(lambda v: v > 30), Y60=sh(lambda v: v > 60), Y120=sh(lambda v: v > 120),
                early60=sh(lambda v: v < -60), two60=sh(lambda v: abs(v) <= 60))
def select(train, fam, E):
    best = None
    for lam, par in itertools.product((0, 1), FAM[fam]):
        m = metrics(train, lam, fam, par)
        if m["ext"] <= E:
            key = (-m["timely"], m["ext"], m["p90"])
            if best is None or key < best[0]: best = (key, lam, par, m)
    return best
out = ["# calib_backtest.py (plan CALIB-BACKTEST-PLAN.md, sealed SHA-256 6175d2c1...; chronological backtest)"]
fmt = lambda m: (f"Y30 {m['Y30']:5.2f} Y60 {m['Y60']:5.2f} Y120 {m['Y120']:5.2f} early60 {m['early60']:5.1f} "  # noqa: E731
                 f"two60 {m['two60']:5.1f} ext {m['ext']:6.1f} p90 {m['p90']:6.1f} timely {m['timely']}/{m['n']}")
for arm in ("U", "C-30"):
    data = riders(arm)
    for fold, tr, tests in (("fold 1", ["2018-11-14"], ["2018-11-15", "2018-11-16"]), ("fold 2", ["2018-11-14", "2018-11-15"], ["2018-11-16"])):
        train = [r for d in tr for r in data[d]]
        out.append(f"\n== {arm} {fold}: train {tr} ({len(train)} riders)")
        for E in (15, 30, 60):
            for fam in FAM:
                sel = select(train, fam, E)
                if sel is None:
                    out.append(f"  E {E:>2d} {fam:<8}: no rule within budget"); continue
                _, lam, par, mtr = sel
                line = f"  E {E:>2d} {fam:<8} lam {lam} par {par}: train Y60 {mtr['Y60']:5.2f} ext {mtr['ext']:5.1f}"
                for d in tests:
                    line += f" || TEST {d[-5:]}: " + fmt(metrics(data[d], lam, fam, par))
                out.append(line)
text = "\n".join(out) + "\n"
open(sys.argv[1], "x", encoding="utf-8", newline="\n").write(text); print(text)
