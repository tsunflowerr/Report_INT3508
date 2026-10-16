"""R16 (2026-10-10) factor-level nowcast screen. RETROSPECTIVE AND EXPLORATORY: all 7 bundle days were inspected
before (optimize/day-profiles-2026-10-06.txt, r13-ml-data-samples/growth-predictor-screen-2026-10-09.txt). Nothing
here is sealed; results must be labelled "retrospective screen on already-seen days".

Read-only on the FleetPy bundle factor files (column travel_time_factor, 15-min rows). Output file opened with mode "x".

Question: for a promise quoted at time t0 (inside a simulated 2-h window that starts at absolute bin s) with naive
remaining time W (the current-snapshot ETA assumes the current bin's factor persists), how close is the displayed
promise D = max(t0 + W, stretch(t0, W, g)) to the arrival A* = stretch(t0, W, true path), for different causal
growth paths g? The world holds the factor from window-relative bin 8 on (preflight_world_v1_3.HOLD_BIN); every
method holds its forecast there too, and a quote made at relative bin >= 8 gets g = 1 (as in the Round-12 protocol).
Stretch = optimize/promise_stretch.stretch (the integrator used by the sealed display layer).

Information rules (asserted in code by an accessor that refuses bins after the quote bin k0 = s + b0):
  in-window ("-in")  : only factors of bins s..k0 of the scenario day (what the Runner's snapshots reveal;
                       Round-12 protocol: reset at the window start, no same-day prefix);
  prefix ("-pre")    : same-day factors from 06:00 (bin 24) to k0 (an operator with a city-wide traffic feed);
  lag-1 ("-L1")      : prefix, but the TREND uses bins <= k0-1 only (the factor of bin k is built from trips that
                       START in k, so it is not complete at the start of k: r13 factor-definition-checks); the
                       anchor is still the current snapshot level, as in the simulator.
  history            : other days only. HIST = causal-no15 sources (display_layer.sources): 14 <- 12,13;
                       15 <- 12,13,14; 16 <- 12,13,14. HIST12 = the Round-12 vintage (12, 13 Nov).

Methods (all anchored on the current level, current-bin multiplier exactly 1):
  NAIVE    g = 1 (the Runner's own promise).
  HIST     g(b) = m(b)/m(b0)  (the current sealed display layer).
  HIST12   same, m = mean(12, 13).
  MOM      raw momentum: g(b) = (f(k0)/f(k0-1))^(b-b0); -in falls back to HIST at b0 = 0.
  BLEND    sqrt(HIST * MOM) (R13 screen).
  RTR      profile growth x undamped trend of the log residual r = log(f/m): g = m(b)/m(b0) * exp(h * dr).
  DT       Gardner-McKenzie damped trend on the log residual (Round-12 protocol R2): l,v recursions; parameters
           (alpha, beta, phi) chosen ONCE from the R12 grid by squared one-step error on 12/13 Nov (windows 07, 08,
           14, 15, 17 h, reset at each window start, M = HIST12 shape) -- in-sample, as R12 says. DT12 = on HIST12
           (R12 exact); DT = same parameters on the HIST (causal-no15) shape.
  REG-x    regime gate (THRESHOLD CHOSEN AFTER SEEING THE DATA -> post hoc): DT-pre if f(k0)/m(k0) >= x else HIST.
  ORACLE   true path (leaky; the ceiling).
Population metrics per (population, W): n quotes, bias = mean(A* - D) s, MAE s, late60 (A* - D > 60 s) %, early60 %,
mean extension D - (t0 + W) s. Quote grid: t0 = window start + 0, 60, ..., 7140 s; W in {600, 1200, 1800} s.
Usage: python -B factor_nowcast_screen.py <out-file>
"""
from __future__ import annotations

import csv
import itertools
import math
import pathlib
import statistics
import sys

HERE = pathlib.Path(__file__).resolve().parent
OPT = HERE.parents[2]                      # .../optimize
sys.path.insert(0, str(OPT))
import promise_stretch as ps  # noqa: E402

NET = pathlib.Path("E:/RideBoundData/wp6/extracted/sha256/d9/"
                   "d9e86f33645e5eec287d387f8d63ad41ddf41d4ef648138b65d636482e2c599e/"
                   "FleetPy_Manhattan/networks/Manhattan_2019_corrected")
DAYS = [f"2018-11-{d}" for d in range(12, 19)]
F: dict[str, dict[int, float]] = {}
for _d in DAYS:
    with (NET / f"{_d}_tt_factors.csv").open(encoding="utf-8") as _h:
        F[_d] = {int(r["simulation_time"]) // 900: float(r["travel_time_factor"]) for r in csv.DictReader(_h)}
    assert sorted(F[_d]) == list(range(96)), _d
WIN = {"w07": 28, "w08": 32, "w14": 56, "w15": 60, "w17": 68}
HOLD = 8
PRE_START = 24                              # 06:00
SRC = {"2018-11-14": ("2018-11-12", "2018-11-13"),
       "2018-11-15": ("2018-11-12", "2018-11-13", "2018-11-14"),
       "2018-11-16": ("2018-11-12", "2018-11-13", "2018-11-14")}
SRC12 = ("2018-11-12", "2018-11-13")
BIN_MS = 900_000


def mean_profile(src):
    return {k: statistics.mean(F[o][k] for o in src) for k in range(96)}


class Obs:
    """Causal accessor to the scenario day's factors: refuses any bin after k_now (and before k_min)."""

    def __init__(self, day, k_now, k_min):
        self.day, self.k_now, self.k_min = day, k_now, k_min

    def __call__(self, k):
        if k > self.k_now or k < self.k_min:
            raise AssertionError(f"leak: bin {k} outside [{self.k_min}, {self.k_now}]")
        return F[self.day][k]


# ---------- damped trend (Round-12 R2) ----------
GRID = list(itertools.product((0.2, 0.5, 0.8, 1.0), (0.0, 0.1, 0.3), (0.8, 0.9, 0.98)))


def dt_filter(residuals, alpha, beta, phi):
    """residuals r_0..r_n (r_0 = 0 by construction); returns (l, v) after the last observation."""
    l, v = 0.0, 0.0
    for r in residuals[1:]:
        l_new = alpha * r + (1 - alpha) * (l + phi * v)
        v = beta * (l_new - l) + (1 - beta) * phi * v
        l = l_new
    return l, v


def dt_ahead(l, v, phi, h):
    return l + sum(phi ** j for j in range(1, h + 1)) * v


def fit_dt():
    m12 = mean_profile(SRC12)
    best = None
    for alpha, beta, phi in GRID:
        sse = 0.0
        for day in SRC12:
            for s in WIN.values():
                r = [math.log((F[day][s + b] / F[day][s]) / (m12[s + b] / m12[s])) for b in range(HOLD + 1)]
                for b in range(HOLD):                      # one-step forecast of r_{b+1} made after observing r_b
                    l, v = dt_filter(r[:b + 1], alpha, beta, phi)
                    sse += (r[b + 1] - dt_ahead(l, v, phi, 1)) ** 2
        key = (sse, alpha, beta, phi)
        if best is None or key < best:
            best = key
    return best


# ---------- methods: each returns weight(b) for window-relative bins b >= b0 ----------
def method_weight(name, day, s, b0, m, params):
    alpha, beta, phi = params
    if b0 >= HOLD:                                          # quote in drain: hold, multiplier 1
        return lambda b: 1.0
    k0 = s + b0
    hb = lambda b: min(b, HOLD)                              # noqa: E731
    hist = lambda b: 1.0 if b == b0 else m[s + hb(b)] / m[k0]  # noqa: E731
    if name in ("HIST", "HIST12"):
        return hist
    if name == "NAIVE":
        return lambda b: 1.0
    if name == "ORACLE":
        f = F[day]
        return lambda b: f[s + hb(b)] / f[k0]
    pre = name.endswith("-pre") or name.endswith("-L1") or name.startswith("REG")
    obs = Obs(day, k0, PRE_START if pre else s)
    if name.startswith("REG"):
        x = float(name.split("-")[1])
        return method_weight("DT-pre", day, s, b0, m, params) if obs(k0) / m[k0] >= x else hist
    base = name.split("-")[0]
    lag = 1 if name.endswith("-L1") else 0
    if not pre and b0 == 0 and base in ("MOM", "BLEND", "RTR", "DT", "DT12"):
        return hist                                         # no in-window trend information at b0 = 0
    if base in ("MOM", "BLEND"):
        step = obs(k0 - lag) / obs(k0 - lag - 1)
        mom = lambda b: 1.0 if b == b0 else step ** (hb(b) - b0)  # noqa: E731
        if base == "MOM":
            return mom
        return lambda b: math.sqrt(hist(b) * mom(b))
    start = PRE_START if pre else s
    res = lambda k: math.log(obs(k) / m[k]) - math.log(obs(start) / m[start])  # noqa: E731
    if base == "RTR":
        dr = res(k0 - lag) - res(k0 - lag - 1)
        return lambda b: 1.0 if b == b0 else m[s + hb(b)] / m[k0] * math.exp(dr * (hb(b) - b0))
    if base in ("DT", "DT12"):
        last = k0 - lag
        r = [res(k) for k in range(start, last + 1)]
        l, v = dt_filter(r, alpha, beta, phi)
        if lag == 0:
            r0 = r[-1]
            return lambda b: 1.0 if b == b0 else m[s + hb(b)] / m[k0] * math.exp(dt_ahead(l, v, phi, hb(b) - b0) - r0)
        rhat0 = dt_ahead(l, v, phi, 1)                       # predicted current residual from bin k0-1
        return lambda b: 1.0 if b == b0 else m[s + hb(b)] / m[k0] * math.exp(dt_ahead(l, v, phi, hb(b) - b0 + 1) - rhat0)
    raise ValueError(name)


METHODS = ["NAIVE", "HIST", "HIST12", "MOM-in", "BLEND-in", "RTR-in", "DT-in", "DT12-in",
           "MOM-pre", "BLEND-pre", "RTR-pre", "DT-pre", "MOM-L1", "BLEND-L1", "DT-L1",
           "REG-1.1", "REG-1.2", "REG-1.3", "ORACLE"]
POPS = {
    "SNOW-AFT (15/11 w14,w15)": [("2018-11-15", "w14"), ("2018-11-15", "w15")],
    "STORM-EVE (15/11 w17)": [("2018-11-15", "w17")],
    "WEEKDAY (14,16 all 5 windows; 15 w07,w08)": [(d, w) for d in ("2018-11-14", "2018-11-16") for w in WIN]
    + [("2018-11-15", "w07"), ("2018-11-15", "w08")],
    "WEEKDAY-SIM (cells simulated: 14,15,16 w07,w08; 14,16 w17)": [(d, w) for d in ("2018-11-14", "2018-11-15", "2018-11-16")
                                                                   for w in ("w07", "w08")] + [("2018-11-14", "w17"), ("2018-11-16", "w17")],
}
WORKS = (600, 1200, 1800)


def evaluate(params):
    rows = {}
    for pop, members in POPS.items():
        for work_s in WORKS:
            for name in METHODS:
                errs, exts = [], []
                for day, w in members:
                    s = WIN[w]
                    m = mean_profile(SRC12 if name in ("HIST12", "DT12-in") else SRC[day])
                    for t0_s in range(0, 7200, 60):
                        t0 = t0_s * 1000
                        b0 = t0 // BIN_MS
                        work = work_s * 1000
                        a_true = ps.stretch(t0, work, method_weight("ORACLE", day, s, b0, m, params))
                        d = max(t0 + work, ps.stretch(t0, work, method_weight(name, day, s, b0, m, params)))
                        errs.append((a_true - d) / 1000)
                        exts.append((d - t0 - work) / 1000)
                n = len(errs)
                rows[(pop, work_s, name)] = (n, statistics.mean(errs), statistics.mean(abs(e) for e in errs),
                                             100 * sum(e > 60 for e in errs) / n, 100 * sum(e < -60 for e in errs) / n,
                                             statistics.mean(exts))
    return rows


def main(out):
    sse, alpha, beta, phi = fit_dt()
    params = (alpha, beta, phi)
    lines = ["# factor_nowcast_screen.py (R16; RETROSPECTIVE exploratory screen on already-seen bundle days; unsealed)",
             f"DT parameters from the Round-12 grid, fitted in-sample on 12/13 Nov (80 one-step targets): alpha={alpha} beta={beta} phi={phi} sse={sse:.6f}"]
    # leakage self-test: an in-window method must refuse a future bin
    try:
        Obs("2018-11-15", 60, 56)(61)
        lines.append("LEAK TEST FAILED")
    except AssertionError:
        lines.append("leak test: accessor refuses a future bin (ok)")
    rows = evaluate(params)
    for pop in POPS:
        for work_s in WORKS:
            lines.append(f"\n## {pop}; W = {work_s} s  (cols: n | bias=mean(A*-D) s | MAE s | late60 % | early60 % | mean ext s)")
            for name in METHODS:
                n, bias, mae, late, early, ext = rows[(pop, work_s, name)]
                lines.append(f"{name:<10} n={n:>4} | bias {bias:+7.1f} | MAE {mae:6.1f} | late60 {late:6.2f} | early60 {early:6.2f} | ext {ext:6.1f}")
    text = "\n".join(lines) + "\n"
    with open(out, "x", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    raise SystemExit(main(sys.argv[1]))
