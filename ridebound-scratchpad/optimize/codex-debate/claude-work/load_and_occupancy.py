"""Load and occupancy descriptors for the 34 T3.8 test cells, to compare with FleetPy ETRR 2026 (avg occupancy ~1.33).
- lambda = requests per second over the 2-h window; tau = mean direct ride time (maxRideTimeMs / 1.5, simulation
  scale at the window start); B = vehicles. Molkenthin et al. 2020 load x = lambda * tau / B.
- occupancy <O> = onboard passenger-seconds / vehicle-seconds over the scored horizon [0, 7200 s], counting idle
  vehicles (riders' onboard intervals clipped to the horizon). Whether FleetPy's 1.33 counts idle vehicles: not checked.
Usage: python -B load_and_occupancy.py <out> (mode x)."""
import pathlib, statistics as st, sys
OPT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(OPT))
import forecast_family_a as fa
CELLS = fa.run_t38.PHASES["test"][1]
H = 7_200_000
out = ["# load_and_occupancy.py (34 T3.8 test cells)"]
for arm in ("U", "C-30"):
    xs, occ = [], []
    for cell in CELLS:
        t = fa.run_dir("test", arm, cell) / "transcript-00.ndjson"
        _, _, state = fa.audit_vep.load(t)
        _, alighted = fa.sweep_analyze.event_times(t)
        reqs = state["requests"]; B = len(state["vehicles"])
        tau = st.mean(r["maxRideTimeMs"] / 1.5 for r in reqs) / 1000
        lam = len(reqs) / 7200
        xs.append(lam * tau / B)
        onboard = sum(max(0, min(alighted[r["requestId"]], H) - min(r["actualPickupTimeMs"], H))
                      for r in reqs if r["requestId"] in alighted)
        occ.append(onboard / (B * H))
    out.append(f"{arm}: cells {len(CELLS)}; load x = lambda*tau/B: mean {st.mean(xs):.3f} (min {min(xs):.3f}, max {max(xs):.3f}); "
               f"occupancy over [0, 2 h] incl. idle: mean {st.mean(occ):.3f} (min {min(occ):.3f}, max {max(occ):.3f})")
text = "\n".join(out) + "\n"
open(sys.argv[1], "x", encoding="utf-8", newline="\n").write(text); print(text)
