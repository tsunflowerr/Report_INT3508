"""R16 evidence, Q3 (zero-run, read-only): who are the riders with >= 2 nonzero dispatch changes of the drop promise
in UNCAPPED arms, and in which regime would a CUMULATIVE budget (sum |c| <= B) act differently from a PER-STEP cap
(max |c| <= B)?  Descriptive exposure on observed paths; under an enforced cap the paths would differ.

Populations (existing runs; reader forecast_family_a.audit_vep.audit, unchanged):
  t38 U       : 34 T3.8 test cells, measured traffic, 8 vehicles  (C:/RideBoundData/research/tier3-t38-v1)
  w07 U       : 8 cells 07-09h, measured traffic, 8 vehicles     (tier3-w07-v1)
  wp14r FREE  : b1-ref (rolling-cost, cost-first, no locks), fixed traffic, 16 cells, 8 vehicles
  wp14r LOCKS : c1-nobudget (= T3.8 U commitment config), fixed traffic, 16 cells, 8 vehicles
  wp9 A b1    : panel A b1-tight-s7 (rolling-cost), older runner, fixed traffic, 20 cells, 8 vehicles
  wp9 B b1    : panel B b1-tight-s7 (rolling-cost), older runner, fixed traffic, 20 cells, 4 vehicles
Per accepted rider (drop initialPromise exists): c_j = p - e of every later drop revision with c != 0 (ms), with its
publishedAtMs; k = number of such changes. For served riders also: direct-time proxy = maxRideTimeMs / 1.5
(maximumRideTimePermille 1500 in every grid), ride duration = A - actualPickupTimeMs, booking time t0 (minutes after
window start), co-riders = distinct other served riders whose on-board interval overlaps on the same vehicle,
whether each change came before or after boarding.
Usage: python -B q3_multi_change_riders.py <out.txt>   (out opened with mode "x"; <= 4 processes)."""
import collections
import pathlib
import statistics
import sys
from concurrent.futures import ProcessPoolExecutor

OPT = pathlib.Path(r"E:/Code/Report_INT3508/ridebound-scratchpad/optimize")
sys.path.insert(0, str(OPT))
import forecast_family_a as fa  # noqa: E402

WP14R = pathlib.Path("E:/RideBoundData/wp14r/development-v6-ledger")
WP9 = pathlib.Path("E:/RideBoundData/wp9")
W07 = pathlib.Path(r"C:/RideBoundData/research/tier3-w07-v1")
CELLS_W07 = [f"d201811{d}-s10-r{r}-w07" for d in ("12", "13") for r in (1, 2, 3, 4)]
BS = (30, 60, 90, 120, 180, 300)


def pops():
    return [
        ("t38 U (measured, 8 veh)", [fa.run_dir("test", "U", c) / "transcript-00.ndjson" for c in fa.run_t38.PHASES["test"][1]]),
        ("w07 U (measured, 8 veh)", [W07 / f"U-{c}" / "transcript-00.ndjson" for c in CELLS_W07]),
        ("wp14r FREE b1-ref (fixed, 8 veh)", [r / "attempt-01" / "output" / "transcript-00.ndjson" for r in sorted(WP14R.glob("w14-*-b1-ref-s7"))]),
        ("wp14r LOCKS c1-nobudget (fixed, 8 veh)", [r / "attempt-01" / "output" / "transcript-00.ndjson" for r in sorted(WP14R.glob("w14-*-c1-nobudget-s7"))]),
        ("wp9 A b1 rolling-cost (fixed, 8 veh)", [r / "transcript-00.ndjson" for r in sorted((WP9 / "confirmatory-h6-panela-v2").glob("*-b1-tight-s7")) if r.is_dir()]),
        ("wp9 B b1 rolling-cost (fixed, 4 veh)", [r / "transcript-00.ndjson" for r in sorted((WP9 / "confirmatory-h6-panelb-v2").glob("*-b1-tight-s7")) if r.is_dir()]),
    ]


def analyze(job):
    label, transcript = job
    _, _, state = fa.audit_vep.load(transcript)
    table, _ = fa.audit_vep.audit(transcript)
    _, alighted = fa.sweep_analyze.event_times(transcript)
    reqs = {q["requestId"]: q for q in state["requests"]}
    accepted, t0, changes = set(), {}, collections.defaultdict(list)
    for r, coord, seq, kind, pub, v, e, p, x, cc, z, closed in table:
        if coord != "drop":
            continue
        if kind == "initialPromise":
            accepted.add(r)
            t0[r] = pub
        elif cc != 0:
            changes[r].append((pub, cc / 1000.0))
    legs = collections.defaultdict(list)
    for r in alighted:
        q = reqs[r]
        legs[q["assignedVehicleId"]].append((q["actualPickupTimeMs"], alighted[r], r))
    co = {}
    for rs in legs.values():
        for a0, a1, rid in rs:
            co[rid] = sum(1 for b0, b1, o in rs if o != rid and b0 < a1 and a0 < b1)
    rows = []
    for r in accepted:
        q = reqs[r]
        cs = sorted(changes.get(r, []))
        served = r in alighted
        board = q.get("actualPickupTimeMs")
        rows.append({
            "k": len(cs),
            "sizes": [abs(c) for _, c in cs],
            "signed": [c for _, c in cs],
            "gaps_min": [(cs[i][0] - cs[i - 1][0]) / 60000 for i in range(1, len(cs))],
            "pre_board": sum(1 for t, _ in cs if board is None or t < board),
            "served": served,
            "direct_min": q["maxRideTimeMs"] / 1.5 / 60000,
            "ride_min": (alighted[r] - board) / 60000 if served and board is not None else None,
            "t0_min": t0[r] / 60000,
            "co": co.get(r),
        })
    return label, rows


def q(xs, p):
    xs = sorted(xs)
    return xs[min(len(xs) - 1, int(p * (len(xs) - 1)))] if xs else float("nan")


def describe(rows, name):
    if not rows:
        return f"    {name}: n=0"
    d = [r["direct_min"] for r in rows]
    ride = [r["ride_min"] for r in rows if r["ride_min"] is not None]
    t0 = [r["t0_min"] for r in rows]
    co = [r["co"] for r in rows if r["co"] is not None]
    return (f"    {name}: n={len(rows)} | direct-time proxy min median {statistics.median(d):.1f} (p25 {q(d, .25):.1f}, p75 {q(d, .75):.1f}) | "
            f"ride min median {statistics.median(ride) if ride else float('nan'):.1f} (p75 {q(ride, .75):.1f}) | booking min after window start "
            f"median {statistics.median(t0):.0f} (p25 {q(t0, .25):.0f}, p75 {q(t0, .75):.0f}) | co-riders on board mean "
            f"{statistics.mean(co) if co else float('nan'):.2f}, share >= 2: {100 * sum(x >= 2 for x in co) / len(co) if co else float('nan'):.1f}%")


def main():
    out = sys.argv[1]
    js = [(label, t) for label, ts in pops() for t in ts if t.exists()]
    with ProcessPoolExecutor(max_workers=4) as pool:
        res = list(pool.map(analyze, js))
    lines = ["# q3_multi_change_riders.py: riders with >= 2 nonzero dispatch changes of the drop promise (uncapped arms)", ""]
    for label, ts in pops():
        rows = [r for lb, rs in res if lb == label for r in rs]
        n = len(rows)
        k2 = [r for r in rows if r["k"] >= 2]
        k1 = [r for r in rows if r["k"] == 1]
        k0 = [r for r in rows if r["k"] == 0]
        lines.append(f"## {label}: runs {sum(1 for t in ts if t.exists())}; accepted riders {n}; exposed (k>=1) {len(k1) + len(k2)} "
                     f"({100 * (len(k1) + len(k2)) / n:.2f}%); k>=2 {len(k2)} ({100 * len(k2) / n:.2f}%); max k {max(r['k'] for r in rows)}")
        lines.append(describe([r for r in k2 if r["served"]], "k>=2 served"))
        lines.append(describe([r for r in k1 if r["served"]], "k=1 served"))
        lines.append(describe([r for r in k0 if r["served"]], "k=0 served"))
        if k2:
            first = [r["sizes"][0] for r in k2]
            later = [s for r in k2 for s in r["sizes"][1:]]
            single = [r["sizes"][0] for r in k1]
            sums = [sum(r["sizes"]) for r in k2]
            gaps = [g for r in k2 for g in r["gaps_min"]]
            neg = sum(1 for r in k2 for c in r["signed"] if c < 0)
            lines.append(f"    k>=2 change sizes (s): first median {statistics.median(first):.1f} (p25 {q(first, .25):.1f}, p75 {q(first, .75):.1f}); "
                         f"later median {statistics.median(later):.1f} (p25 {q(later, .25):.1f}, p75 {q(later, .75):.1f}); sum median "
                         f"{statistics.median(sums):.1f} (min {min(sums):.1f}, max {max(sums):.1f}); minutes between changes median "
                         f"{statistics.median(gaps):.1f}; changes before boarding {sum(r['pre_board'] for r in k2)} of {sum(r['k'] for r in k2)}; "
                         f"earlier-moving changes {neg}")
            lines.append(f"    k=1 single change size (s): median {statistics.median(single):.1f} (p25 {q(single, .25):.1f}, p75 {q(single, .75):.1f})" if single else "    k=1: none")
            small = {b: sum(1 for r in k2 if max(r["sizes"]) <= b) for b in BS}
            lines.append("    k>=2 riders whose EVERY change is <= B (a per-step cap would allow all): " +
                         ", ".join(f"B={b}: {small[b]}" for b in BS))
        cum = {b: sum(1 for r in rows if r["sizes"] and max(r["sizes"]) <= b < sum(r["sizes"])) for b in BS}
        per = {b: sum(1 for r in rows if r["sizes"] and max(r["sizes"]) > b) for b in BS}
        lines.append("    cumulative-ONLY riders (max <= B < sum) / per-step-exceed riders, per 1,000 accepted: " +
                     ", ".join(f"B={b}: {cum[b]} / {per[b]} ({1000 * cum[b] / n:.2f} / {1000 * per[b] / n:.1f})" for b in BS))
        lines.append("")
    text = "\n".join(lines) + "\n"
    with open(out, "x", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print(text)


if __name__ == "__main__":
    main()
