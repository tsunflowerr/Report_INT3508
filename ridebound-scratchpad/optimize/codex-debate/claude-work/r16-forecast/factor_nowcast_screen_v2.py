"""R16 (2026-10-10) factor-level nowcast screen, v2. RETROSPECTIVE AND EXPLORATORY (all bundle days seen before).

Why a v2: v1 (factor_nowcast_screen.py, output factor-nowcast-screen-2026-10-10.txt, kept unchanged) showed that the
Round-12 damped-trend rule, with its parameters chosen on 12/13 Nov as R12 prescribes, selects beta = 0 (no trend), so
DT is identical to the current HIST display layer, and v1's REG gate (which switched to DT-pre) was therefore inert.
v2 adds, on the same quote grid and the same causal accessor (methods imported from v1):
  REGB-x   regime gate -> BLEND-pre when the current level exceeds the historical same-time level by x
           (f(k0)/m(k0) >= x); else HIST. Needs the ABSOLUTE level, i.e. a city-wide feed (prefix information).
           x in {1.1, 1.2, 1.3} chosen AFTER seeing the data (post hoc; sensitivity only).
  PAD@M    uniform pad D = t0 + W (1 + k) with k = mean extension of method M on the SAME population and W, divided
           by W (cost-matched from promises only; this favours the pad, which is told the event day's cost).
  DT grid  all 36 Round-12 triples on the HIST shape (in-window info), to show the snow-vs-weekday trade-off frontier
           that ANY fixed triple achieves (selection by looking at this table would be post hoc).
  gate     distribution of f(k0)/m(k0) over quote bins per population (separability of the regime signal).
Usage: python -B factor_nowcast_screen_v2.py <out-file>   (mode "x")
"""
from __future__ import annotations

import math
import pathlib
import statistics
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import factor_nowcast_screen as v1  # noqa: E402

ps = v1.ps
WORKS = (1200, 1800)


def weight(name, day, s, b0, m, params):
    if name.startswith("REGB-"):
        x = float(name.split("-")[1])
        if b0 >= v1.HOLD:
            return lambda b: 1.0
        k0 = s + b0
        level = v1.Obs(day, k0, v1.PRE_START)(k0)
        return v1.method_weight("BLEND-pre" if level / m[k0] >= x else "HIST", day, s, b0, m, params)
    return v1.method_weight(name, day, s, b0, m, params)


def quotes(members):
    for day, w in members:
        s = v1.WIN[w]
        for t0_s in range(0, 7200, 60):
            yield day, w, s, t0_s * 1000, (t0_s * 1000) // v1.BIN_MS


def run_method(name, members, work_s, params, pad_ref=None):
    errs, exts = [], []
    k = None
    if pad_ref is not None:
        k = statistics.mean(e for e in pad_ref) / work_s
    for day, w, s, t0, b0 in quotes(members):
        m = v1.mean_profile(v1.SRC[day])
        work = work_s * 1000
        a_true = ps.stretch(t0, work, v1.method_weight("ORACLE", day, s, b0, m, params))
        if k is not None:
            d = t0 + work * (1 + k)
        else:
            d = max(t0 + work, ps.stretch(t0, work, weight(name, day, s, b0, m, params)))
        errs.append((a_true - d) / 1000)
        exts.append((d - t0 - work) / 1000)
    n = len(errs)
    return {"n": n, "bias": statistics.mean(errs), "mae": statistics.mean(abs(e) for e in errs),
            "late": 100 * sum(e > 60 for e in errs) / n, "early": 100 * sum(e < -60 for e in errs) / n,
            "ext": statistics.mean(exts), "exts": exts}


def fmt(name, r):
    return (f"{name:<16} n={r['n']:>4} | bias {r['bias']:+7.1f} | MAE {r['mae']:6.1f} | late60 {r['late']:6.2f} | "
            f"early60 {r['early']:6.2f} | ext {r['ext']:6.1f}")


def main(out):
    sse, alpha, beta, phi = v1.fit_dt()
    params = (alpha, beta, phi)
    lines = ["# factor_nowcast_screen_v2.py (R16; RETROSPECTIVE exploratory screen on already-seen days; unsealed)",
             f"R12-fitted DT triple (in-sample 12/13 Nov): alpha={alpha} beta={beta} phi={phi} (beta=0 => DT == HIST)"]
    pops = v1.POPS
    names = ["NAIVE", "HIST", "DT-in", "MOM-in", "BLEND-in", "BLEND-pre", "BLEND-L1", "RTR-pre",
             "REGB-1.1", "REGB-1.2", "REGB-1.3", "ORACLE"]
    for pop, members in pops.items():
        for work_s in WORKS:
            lines.append(f"\n## {pop}; W = {work_s} s (bias = mean(A*-D) s; late/early in %; ext s)")
            res = {name: run_method(name, members, work_s, params) for name in names}
            for name in names:
                lines.append(fmt(name, res[name]))
            for ref in ("BLEND-in", "MOM-in", "ORACLE"):
                lines.append(fmt(f"PAD@{ref}", run_method("PAD", members, work_s, params, pad_ref=res[ref]["exts"])))
            hist, orc = res["HIST"], res["ORACLE"]
            for name in ("MOM-in", "BLEND-in", "BLEND-pre", "BLEND-L1", "REGB-1.2"):
                r = res[name]
                share = (hist["mae"] - r["mae"]) / hist["mae"] * 100 if hist["mae"] else float("nan")
                lines.append(f"   MAE share of HIST error removed by {name}: {share:5.1f}%  (late60 {hist['late']:.2f} -> {r['late']:.2f})")
    # DT grid frontier
    lines.append("\n## DT grid (all 36 R12 triples, in-window info, HIST shape): snow-afternoon vs weekday-sim, W = 1800 s")
    lines.append("alpha beta phi | SNOW late60 early60 ext | WEEKDAY-SIM late60 early60 ext")
    snow = pops["SNOW-AFT (15/11 w14,w15)"]
    wk = pops["WEEKDAY-SIM (cells simulated: 14,15,16 w07,w08; 14,16 w17)"]
    for triple in v1.GRID:
        a = run_method("DT-in", snow, 1800, triple)
        b = run_method("DT-in", wk, 1800, triple)
        lines.append(f"{triple[0]:.1f} {triple[1]:.1f} {triple[2]:.2f} | {a['late']:6.2f} {a['early']:6.2f} {a['ext']:6.1f} | "
                     f"{b['late']:6.2f} {b['early']:6.2f} {b['ext']:6.1f}")
    # gate statistic
    lines.append("\n## gate statistic f(k0)/m(k0) over quote bins b0 = 0..7 (m = causal-no15 history)")
    for pop, members in pops.items():
        vals = []
        for day, w in members:
            m = v1.mean_profile(v1.SRC[day])
            s = v1.WIN[w]
            vals += [v1.F[day][s + b] / m[s + b] for b in range(8)]
        vals.sort()
        lines.append(f"{pop}: min {vals[0]:.3f} median {statistics.median(vals):.3f} max {vals[-1]:.3f} (n={len(vals)})")
    text = "\n".join(lines) + "\n"
    with open(out, "x", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    raise SystemExit(main(sys.argv[1]))
