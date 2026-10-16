"""R16 (2026-10-10) zero-run rider-level replay of causal nowcast variants on SAVED C-30 runs. RETROSPECTIVE AND
EXPLORATORY: these runs, days and outcomes were all inspected before (FORECAST-REPORT.md). Unsealed. Read-only on the
runs (uses forecast_family_a.riders, the sealed Family-A reader); output file opened with mode "x".

Populations (the same as the sealed report):
  SNOW    : the 8 C-30 forecast-off runs of 15/11 w14, w15 (tier3-forecast-v1; family_snow.py);
  WEEKDAY : the 21 active weekday C-30 test cells of T3.8 (14-16/11 w07, w08; 14, 16/11 w17), causal-no15.
Per served rider (first drop promise P0 published at t0; A = alight time; dispatch = sum of p - e revisions):
  D_M = max(P0, stretch(t0, P0 - t0, g_M)) with g_M from factor_nowcast_screen(_v2) (causal accessor), and
  Y60 = share A - D > 60 s, E60 = share A - D < -60 s, ext = mean D - P0 (quote cost), late riders = count.
  HIST must reproduce the sealed display layer (sanity check printed: max |D_HIST - D0_sealed|).
Pads (cost-matched from PROMISES ONLY, as FORECAST-PLAN A3): PAD@M has k = sum(D_M - P0) / sum(P0 - t0) over the
population's riders; PAD-wk@BLEND-in uses the WEEKDAY k on the SNOW population (a deployable fixed pad).
Ledger (riders late > 60 s vs P0): explained_M = sum clip(D_M - P0, 0, A - P0 - dispatch); remainder = total -
dispatch - explained_M.
Usage: python -B rider_nowcast_replay.py <out-file>
"""
from __future__ import annotations

import pathlib
import statistics
import sys

HERE = pathlib.Path(__file__).resolve().parent
OPT = HERE.parents[2]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(OPT))
import factor_nowcast_screen as v1  # noqa: E402
import factor_nowcast_screen_v2 as v2  # noqa: E402
import forecast_family_a as fa  # noqa: E402  (adds tang3 paths; read-only reader)
import display_layer as dl  # noqa: E402
import run_forecast as rf  # noqa: E402
import run_t38  # noqa: E402
import t38_calibrate  # noqa: E402

ps = v1.ps
METHODS = ["NAIVE", "HIST", "MOM-in", "BLEND-in", "BLEND-pre", "BLEND-L1", "RTR-pre",
           "REGB-1.1", "REGB-1.2", "REGB-1.3", "ORACLE"]
PROFILES = {d: v1.mean_profile(src) for d, src in v1.SRC.items()}


def cells():
    snow = [(c, rf.OUT_ROOT / f"C-30-{c}") for c in rf.SNOW]
    test = list(run_t38.PHASES["test"][1])
    wk = [c for c in test if fa.day_of(c) in dl.WEEKDAYS and dl.sources(fa.day_of(c), "causal-no15")]
    weekday = [(c, run_t38.OUT_ROOT / t38_calibrate.effective(f"C-30-{c}")) for c in wk]
    return {"SNOW": snow, "WEEKDAY": weekday}


def displayed(name, day, window, t0, p0, params):
    if p0 <= t0:
        return float(p0)
    s = v1.WIN[window]
    b0 = int(t0 // v1.BIN_MS)
    g = v2.weight(name, day, s, b0, PROFILES[day], params)
    return max(float(p0), ps.stretch(t0, p0 - t0, g))


def main(out):
    sse, alpha, beta, phi = v1.fit_dt()
    params = (alpha, beta, phi)
    lines = ["# rider_nowcast_replay.py (R16; RETROSPECTIVE zero-run replay on already-inspected runs; unsealed)",
             f"DT triple from R12 grid on 12/13 Nov: {params} (beta=0 => DT == HIST; DT not replayed separately)"]
    data = {}
    for pop, members in cells().items():
        for cell, run in members:
            day, window = fa.day_of(cell), cell[-3:]
            prof = dl.profile(day, window, "causal-no15")
            rs = fa.riders(run, cell, prof)
            for r in rs:
                r["D"] = {m: displayed(m, day, window, r["t0"], r["P0"], params) for m in METHODS}
            data[(pop, cell)] = rs
    gap = max(abs(r["D"]["HIST"] - r["D0"]) for rs in data.values() for r in rs)
    lines.append(f"sanity: max |D_HIST - D0_sealed| over all riders = {gap:.3f} ms (must be ~0)")
    pads = {}
    for pop in ("SNOW", "WEEKDAY"):
        rs = [r for (p, _), v in data.items() if p == pop for r in v]
        for ref in ("BLEND-in", "BLEND-pre", "MOM-in", "REGB-1.2"):
            pads[(pop, ref)] = sum(r["D"][ref] - r["P0"] for r in rs) / sum(r["P0"] - r["t0"] for r in rs)
    lines.append("pads k (promises only): " + ", ".join(f"{p}/{ref} {k:.5f}" for (p, ref), k in pads.items()))

    def show(r, name, pop):
        if name.startswith("PAD-wk@"):
            k = pads[("WEEKDAY", name[7:])]
            return r["P0"] + k * (r["P0"] - r["t0"])
        if name.startswith("PAD@"):
            k = pads[(pop, name[4:])]
            return r["P0"] + k * (r["P0"] - r["t0"])
        return r["D"][name]

    for pop in ("SNOW", "WEEKDAY"):
        members = [c for (p, c) in data if p == pop]
        names = METHODS + ["PAD@BLEND-in", "PAD@BLEND-pre", "PAD@REGB-1.2", "PAD@MOM-in"] + (["PAD-wk@BLEND-in", "PAD-wk@REGB-1.2"] if pop == "SNOW" else [])
        served = sum(len(data[(pop, c)]) for c in members)
        lines.append(f"\n## {pop}: {len(members)} cells, {served} served riders (cell means; late = rider count)")
        for name in names:
            ys, es, xs, late = [], [], [], 0
            for c in members:
                rs = data[(pop, c)]
                n = len(rs)
                ys.append(sum(r["A"] - show(r, name, pop) > 60_000 for r in rs) / n)
                es.append(sum(r["A"] - show(r, name, pop) < -60_000 for r in rs) / n)
                xs.append(statistics.mean(show(r, name, pop) - r["P0"] for r in rs) / 1000)
                late += sum(r["A"] - show(r, name, pop) > 60_000 for r in rs)
            lines.append(f"{name:<16} Y60 {100 * statistics.mean(ys):6.2f}% | E60 {100 * statistics.mean(es):5.2f}% | "
                         f"ext {statistics.mean(xs):6.1f} s | late riders {late:>3}")
        # ledger
        late_rs = [r for c in members for r in data[(pop, c)] if r["A"] - r["P0"] > 60_000]
        total = sum(r["A"] - r["P0"] for r in late_rs) / 1000
        disp = sum(r["dispatch"] for r in late_rs) / 1000
        lines.append(f"ledger ({len(late_rs)} riders late > 60 s vs P0): total {total:.0f} s, dispatch {disp:.0f} s")
        for name in METHODS:
            expl = sum(max(0.0, min(r["D"][name] - r["P0"], r["A"] - r["P0"] - r["dispatch"])) for r in late_rs) / 1000
            over = sum(max(0.0, (r["D"][name] - r["P0"]) - (r["A"] - r["P0"] - r["dispatch"])) for r in late_rs) / 1000
            lines.append(f"   {name:<10} explained {expl:7.0f} s ({100 * expl / total:5.1f}%) | remainder {total - disp - expl:7.0f} s | overshoot {over:6.0f} s")
        # W distribution
        ws = sorted((r["P0"] - r["t0"]) / 1000 for c in members for r in data[(pop, c)])
        lines.append(f"W = P0 - t0 (s): p10 {ws[len(ws) // 10]:.0f}, median {statistics.median(ws):.0f}, p90 {ws[9 * len(ws) // 10]:.0f}")
    text = "\n".join(lines) + "\n"
    with open(out, "x", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    raise SystemExit(main(sys.argv[1]))
