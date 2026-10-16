"""R16 evidence, Q2 (zero-run, read-only): the existing cap dial with lateness against the FIRST drop promise.

Populations (existing runs only; one episode per cell):
  w07  : 8 cells 07:00-09:00 on 12-13 Nov 2018, measured traffic (tier3-w07-v1: U, C-30, C-60, C-120, C-300, Mplus-30,
         Mplus-60, Mplus-120, Mplus-300, V-30; tier3-w07x-v1: C-90, C-150, C-180, C-240)
  t38  : 34 T3.8 test cells (U, C-30, Mplus-30, Mplus-60, V-30), split by window w07 / w08 / w17, for context
  wp14r: 16 cells w08 + w17 on 12-13 Nov, FIXED traffic (b1-ref FREE, c1-nobudget LOCKS, c1-budget120, c1-budget60,
         c1-h6ref = 30 s), no forecast (nothing to forecast)
Per served rider (passengerAlighted event; first drop promise = initialPromise drop p0 published at t0; reader
forecast_family_a.audit_vep.audit, unchanged):
  late_k  = A - p0 > k s (k = 60, 120, 300);  early60 = A - p0 < -60 s;
  timely_k per request = (served - late_k) / requests;
  drop-exposed = any later drop revision with dispatch part c = p - e != 0;
  shared = another served rider on the same vehicle with an overlapping on-board interval [actualPickupTimeMs, A]
           (same rule as wp14r_ladder_reanalysis.py).
Forecast quote D0 = display_layer.display(t0, p0, profile) (promise-only replay; vehicles unchanged):
  w07 cells (12/13 Nov): causal-no15 is INACTIVE (no prior weekday), so only the NON-CAUSAL sensitivity rule
  loo-no15 (sources 13,14,16 resp. 12,14,16 Nov) is shown; t38 cells: causal-no15 (primary rule), inactive cells = naive.
v2 (2026-10-10): forecast counts now include inactive cells at the naive promise (v1 counted only active cells;
its forecast lines for T3.8 are superseded; its w07 forecast lines are unaffected because all 8 w07 cells are active).
Usage: python -B q2_cap_dial.py <out.txt> [population ...]   (out opened with mode "x"; <= 4 processes)."""
import collections
import pathlib
import statistics
import sys
from concurrent.futures import ProcessPoolExecutor

OPT = pathlib.Path(r"E:/Code/Report_INT3508/ridebound-scratchpad/optimize")
sys.path.insert(0, str(OPT))
import display_layer as dl  # noqa: E402
import forecast_family_a as fa  # noqa: E402

W07 = pathlib.Path(r"C:/RideBoundData/research/tier3-w07-v1")
W07X = pathlib.Path(r"C:/RideBoundData/research/tier3-w07x-v1")
WP14R = pathlib.Path("E:/RideBoundData/wp14r/development-v6-ledger")
CELLS_W07 = [f"d201811{d}-s10-r{r}-w07" for d in ("12", "13") for r in (1, 2, 3, 4)]
ARMS_W07 = (("U", W07), ("C-30", W07), ("C-60", W07), ("C-90", W07X), ("C-120", W07), ("C-150", W07X),
            ("C-180", W07X), ("C-240", W07X), ("C-300", W07), ("Mplus-30", W07), ("Mplus-60", W07),
            ("Mplus-120", W07), ("Mplus-300", W07), ("V-30", W07))
ARMS_T38 = ("U", "C-30", "Mplus-30", "Mplus-60", "V-30")
ARMS_WP14R = (("b1-ref", "FREE"), ("c1-nobudget", "LOCKS"), ("c1-budget120", "C-120"), ("c1-budget60", "C-60"),
              ("c1-h6ref", "C-30"))
KS = (60, 120, 300)


def cell(job):
    pop, arm, transcript, day, window, rule = job
    _, _, state = fa.audit_vep.load(transcript)
    table, _ = fa.audit_vep.audit(transcript)
    _, alighted = fa.sweep_analyze.event_times(transcript)
    prof = dl.profile(day, window, rule) if rule else None
    first, exposed = {}, set()
    for r, coord, seq, kind, pub, v, e, p, x, cc, z, closed in table:
        if coord != "drop":
            continue
        if kind == "initialPromise":
            first[r] = (pub, p)
        elif cc != 0:
            exposed.add(r)
    reqs = state["requests"]
    life = {q["requestId"]: q["lifecycle"] for q in reqs}
    legs = collections.defaultdict(list)
    for q in reqs:
        if q["requestId"] in alighted:
            legs[q["assignedVehicleId"]].append((q["actualPickupTimeMs"], alighted[q["requestId"]], q["requestId"]))
    shared = set()
    for rs in legs.values():
        for a0, a1, rid in rs:
            if any(o != rid and b0 < a1 and a0 < b1 for b0, b1, o in rs):
                shared.add(rid)
    m = collections.Counter()
    m["requests"] = len(reqs)
    m["completed_lifecycle"] = sum(1 for v in life.values() if v == "completed")
    served = [r for r in alighted if r in first]
    m["served"] = len(served)
    m["served_without_promise"] = sum(1 for r in alighted if r not in first)
    m["shared"] = sum(1 for r in served if r in shared)
    m["exposed"] = sum(1 for r in served if r in exposed)
    ext = 0.0
    for r in served:
        t0, p0 = first[r]
        a = alighted[r]
        lat = a - p0
        for k in KS:
            m[f"late{k}"] += lat > k * 1000
        m["early60"] += lat < -60_000
        # v2 fix: an inactive cell (prof is None) displays the naive promise D0 = p0 and must still be counted
        d0 = dl.display(t0, p0, prof) if prof is not None else float(p0)
        ext += d0 - p0
        latf = a - d0
        for k in KS:
            m[f"fc_late{k}"] += latf > k * 1000
        m["fc_early60"] += latf < -60_000
    m["fc_active"] = int(prof is not None)
    m["fc_ext_ms"] = ext
    return pop, arm, window, m


def jobs():
    out = []
    for arm, root in ARMS_W07:
        for c in CELLS_W07:
            out.append(("w07", arm, root / f"{arm}-{c}" / "transcript-00.ndjson", fa.day_of(c), "w07", "loo-no15"))
    for arm in ARMS_T38:
        for c in fa.run_t38.PHASES["test"][1]:
            out.append(("t38", arm, fa.run_dir("test", arm, c) / "transcript-00.ndjson", fa.day_of(c), c[-3:],
                        "causal-no15"))
    for slug, _ in ARMS_WP14R:
        for r in sorted(WP14R.glob(f"w14-*-{slug}-s7")):
            t = r / "attempt-01" / "output" / "transcript-00.ndjson"
            if t.exists():
                out.append(("wp14r", slug, t, None, r.name.split("-")[4], None))
    return out


def fmt(label, m, fc):
    n, req = m["served"], m["requests"]
    s = (f"{label:<14} req {req:5d} | served {n:5d} | late>60 {m['late60']:4d} ({100 * m['late60'] / n:5.2f}%) "
         f">120 {m['late120']:4d} ({100 * m['late120'] / n:5.2f}%) >300 {m['late300']:3d} ({100 * m['late300'] / n:4.2f}%) | "
         f"timely60/req {n - m['late60']:5d} ({100 * (n - m['late60']) / req:5.2f}%) timely120/req {n - m['late120']:5d} "
         f"({100 * (n - m['late120']) / req:5.2f}%) | early>60 {m['early60']:3d} ({100 * m['early60'] / n:4.2f}%) | "
         f"exposed {100 * m['exposed'] / n:5.2f}% | shared {100 * m['shared'] / n:5.2f}%")
    if fc:
        s += (f"\n{'':<14}   forecast quote: late>60 {m['fc_late60']:4d} ({100 * m['fc_late60'] / n:5.2f}%) >120 {m['fc_late120']:3d} "
              f">300 {m['fc_late300']:3d} | timely60/req {n - m['fc_late60']:5d} ({100 * (n - m['fc_late60']) / req:5.2f}%) "
              f"timely120/req {n - m['fc_late120']:5d} | early>60 {m['fc_early60']:3d} ({100 * m['fc_early60'] / n:4.2f}%) | "
              f"mean quote extension {m['fc_ext_ms'] / n / 1000:5.1f} s | active cells {m['fc_active']}")
    return s


def main():
    out = sys.argv[1]
    only = set(sys.argv[2:])  # optional population filter (w07 / t38 / wp14r)
    js = [j for j in jobs() if not only or j[0] in only]
    with ProcessPoolExecutor(max_workers=4) as pool:
        res = list(pool.map(cell, js, chunksize=2))
    agg = collections.defaultdict(collections.Counter)
    for pop, arm, window, m in res:
        agg[(pop, arm, "all")].update(m)
        agg[(pop, arm, window)].update(m)
    lines = ["# q2_cap_dial.py: served vs lateness against the FIRST drop promise, existing runs only", ""]
    lines.append("## w07/w07x: 8 cells, 07:00-09:00, 12-13 Nov 2018, measured traffic, 864 requests per arm; "
                 "forecast = loo-no15 (NON-CAUSAL sensitivity; causal-no15 inactive on these days)")
    for arm, _ in ARMS_W07:
        if agg[("w07", arm, "all")]["served"]:
            lines.append(fmt(arm, agg[("w07", arm, "all")], True))
    lines.append("")
    lines.append("## T3.8: 34 test cells, measured traffic; forecast = causal-no15 (primary; inactive cells shown naive)")
    for window in ("all", "w07", "w08", "w17"):
        lines.append(f"### window {window}")
        for arm in ARMS_T38:
            if agg[("t38", arm, window)]["served"]:
                lines.append(fmt(arm, agg[("t38", arm, window)], True))
    lines.append("")
    lines.append("## WP14r v6: 16 cells (w08 + w17, 12-13 Nov), FIXED traffic, older runner 38d517d; no forecast")
    for slug, name in ARMS_WP14R:
        if not agg[("wp14r", slug, "all")]["served"]:
            continue
        lines.append(fmt(f"{name} ({slug})", agg[("wp14r", slug, "all")], False))
        for window in ("w08", "w17"):
            lines.append(fmt(f"  {window}", agg[("wp14r", slug, window)], False))
    lines.append("")
    chk = [(k, v["completed_lifecycle"], v["served"], v["served_without_promise"]) for k, v in agg.items() if k[2] == "all"]
    lines.append("# check: lifecycle 'completed' vs alighted-with-promise vs alighted-without-promise per (population, arm): "
                 + "; ".join(f"{k[0]}/{k[1]} {a}/{b}/{c}" for k, a, b, c in chk))
    text = "\n".join(lines) + "\n"
    with open(out, "x", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print(text)


if __name__ == "__main__":
    main()
