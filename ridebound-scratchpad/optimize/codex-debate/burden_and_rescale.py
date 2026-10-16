"""Zero-run analyses for debate round 2 (34 T3.8 test cells, served riders pooled).
(1) Burden inside the first promise: promised door-to-door (first drop promise - request time), promised wait,
    promised ride / direct ride (direct = maxRideTimeMs / 1.5 at snapshot scale; promised ride also contains the traffic
    ratio at publication, so this ratio is an upper estimate of detour), versus lateness after the promise.
(2) Rescaling sensitivity: the fixtures scale arcs by the factor at 00:00 and the world multiplies by f(t)/f(start), so
    simulated times are f(0)/f(start) of the measured absolute level. Lateness x f(start)/f(0) per cell gives the order of
    magnitude if all times were at the measured level AND every decision stayed the same. Not a simulation.
Usage: python -B burden_and_rescale.py <out> (mode x)."""
import csv, pathlib, statistics as st, sys
HERE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import forecast_family_a as fa
CELLS = fa.run_t38.PHASES["test"][1]
F = pathlib.Path("E:/RideBoundData/wp6/extracted/sha256/d9/d9e86f33645e5eec287d387f8d63ad41ddf41d4ef648138b65d636482e2c599e/"
                 "FleetPy_Manhattan/networks/Manhattan_2019_corrected")
START = {"w07": 25200, "w08": 28800, "w17": 61200}
def factor(day, sec):
    with (F / f"{day}_tt_factors.csv").open(encoding="utf-8") as fh:
        rows = {int(r["simulation_time"]): float(r["travel_time_factor"]) for r in csv.DictReader(fh)}
    return rows[sec] / rows[0]
def q(xs, p):
    xs = sorted(xs); return xs[min(len(xs) - 1, int(p * len(xs)))]
out = ["# burden_and_rescale.py (34 T3.8 test cells; served riders pooled)"]
scales = {}
for cell in CELLS:
    day = f"{cell[1:5]}-{cell[5:7]}-{cell[7:9]}"
    scales[cell] = factor(day, START[cell[-3:]])
out.append("rescale factor f(start)/f(0) per cell: min %.3f, median %.3f, max %.3f" % (min(scales.values()), st.median(scales.values()), max(scales.values())))
for arm in ("U", "C-30"):
    door0, wait0, ratio, late, late_s = [], [], [], [], []
    for cell in CELLS:
        t = fa.run_dir("test", arm, cell) / "transcript-00.ndjson"
        _, _, state = fa.audit_vep.load(t)
        table, _ = fa.audit_vep.audit(t)
        _, alighted = fa.sweep_analyze.event_times(t)
        req = {r["requestId"]: r for r in state["requests"]}
        first = {}
        for r, c, s, k, pub, v, e, p, x, cc, z, closed in table:
            if k == "initialPromise":
                first[(r, c)] = p
        for r in req:
            if r not in alighted or (r, "drop") not in first:
                continue
            a = req[r]["arrivalTimeMs"]; p_pick = first[(r, "pickup")]; p_drop = first[(r, "drop")]
            direct = req[r]["maxRideTimeMs"] / 1.5
            door0.append((p_drop - a) / 60000); wait0.append((p_pick - a) / 60000)
            ratio.append((p_drop - p_pick) / direct)
            lm = (alighted[r] - p_drop) / 60000
            late.append(lm); late_s.append(lm * scales[cell])
    n = len(late)
    share = lambda xs, t: 100 * sum(1 for x in xs if x > t) / len(xs)  # noqa: E731
    out.append(f"\n== {arm}: {n} served riders")
    out.append(f"  promised door-to-door (min): mean {st.mean(door0):.2f}, p90 {q(door0, .9):.2f}; promised wait mean {st.mean(wait0):.2f}, p90 {q(wait0, .9):.2f}")
    out.append(f"  promised ride / direct ride: mean {st.mean(ratio):.3f}, p50 {q(ratio, .5):.3f}, p90 {q(ratio, .9):.3f}, share > 1.3 {share(ratio, 1.3):.2f}%")
    out.append(f"  lateness after first promise (min): mean {st.mean(late):+.3f} = {100 * st.mean(late) / st.mean(door0):.2f}% of mean promised door-to-door")
    out.append(f"  RESCALED lateness (decisions fixed): mean {st.mean(late_s):+.2f}, p99 {q(late_s, .99):+.2f}, max {max(late_s):+.2f}; "
               f"share > 1 / 2 / 5 / 10 min: {share(late_s, 1):.2f} / {share(late_s, 2):.2f} / {share(late_s, 5):.2f} / {share(late_s, 10):.2f} %")
text = "\n".join(out) + "\n"
open(sys.argv[1], "x", encoding="utf-8", newline="\n").write(text); print(text)
