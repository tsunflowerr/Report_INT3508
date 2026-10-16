"""ML pilot data extraction exactly per ML-PILOT-SEALED.md (SHA-256 93f6b968..., sealed 2026-10-08 22:46:17).
Causal state comes from the first published drop promise's projection.serviceOrder (vehicle's remaining plan at
publication). D0 uses the fixed 12/11 + 13/11 profile vintage (measured) or P0 (static). One row per first drop promise.
Usage: python -B ml_pilot_extract.py <out.csv> (mode x)."""
import csv, pathlib, sys
OPT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(OPT))
import display_layer as dl, forecast_family_a as fa, promise_stretch as ps
W07 = pathlib.Path("C:/RideBoundData/research/tier3-w07-v1")
W14 = pathlib.Path("E:/RideBoundData/wp14r/development-v6-ledger")
PROF = ps.v13.forecast_profile(["2018-11-12", "2018-11-13"], 25200)
RUNS = []  # (world, arm, cell, role, transcript, window_start_s, measured)
for arm in ("U", "C-30"):
    for day in ("12", "13"):
        for r in (1, 2, 3, 4):
            c = f"d201811{day}-s10-r{r}-w07"; RUNS.append(("measured", arm, c, "fit", W07 / f"{arm}-{c}" / "transcript-00.ndjson", 25200, True))
    for r in (3, 4):
        c = f"d20181114-s10-r{r}-w07"; RUNS.append(("measured", arm, c, "cal", fa.run_dir("test", arm, c) / "transcript-00.ndjson", 25200, True))
    for day in ("15", "16"):
        for r in (1, 2, 4):
            c = f"d201811{day}-s10-r{r}-w07"; RUNS.append(("measured", arm, c, f"test{day}", fa.run_dir("test", arm, c) / "transcript-00.ndjson", 25200, True))
TAGS = {"FREE": "b1-ref", "LOCKS": "c1-nobudget", "C-120": "c1-budget120", "C-60": "c1-budget60", "C-30": "c1-h6ref"}
for arm, tag in TAGS.items():
    for day, rs, role in (("12", (1, 2, 3), "fit"), ("12", (4,), "cal"), ("13", (1, 2, 3, 4), "test13")):
        for r in rs:
            for w, ws in (("w08", 28800), ("w17", 61200)):
                c = f"d201811{day}-s10-r{r}-{w}"
                RUNS.append(("static", arm, c, role, W14 / f"w14-{c}-{tag}-s7" / "attempt-01" / "output" / "transcript-00.ndjson", ws, False))
cols = ["world", "arm", "cell", "role", "window", "rider", "clock_min", "horizon_s", "pick_s", "fc_ext_s", "maxride_s", "room_s",
        "other_assigned", "other_onboard", "P0", "D0", "t0", "A", "resid_s"]
n = 0
with open(sys.argv[1], "x", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh); w.writerow(cols)
    for world, arm, cell, role, t, ws, measured in RUNS:
        if not t.exists():
            raise SystemExit(f"MISSING {world} {arm} {cell} {t}")
        _, _, state = fa.audit_vep.load(t)
        _, alighted = fa.sweep_analyze.event_times(t)
        req = {r["requestId"]: r for r in state["requests"]}
        for hist in state["commitmentLedger"]:
            rid = hist["requestId"]; e0 = hist["entries"][0]
            assert e0["kind"] == "initialPromise"
            pp = e0["publishedPromise"]; pr = pp["projection"]; t0 = pp["publishedAtMs"]
            p0, pick0 = pr["dropEtaMs"], pr["pickupEtaMs"]
            if rid not in alighted:
                raise SystemExit(f"promised rider not completed: {cell} {rid}")
            so = pr["serviceOrder"]; others = {s["requestId"] for s in so if s["requestId"] != rid}
            picked = {s["requestId"] for s in so if s["kind"] == "pickup"}
            onboard = sum(1 for o in others if o not in picked)
            d0 = dl.display(t0, p0, PROF) if measured else float(p0)
            mr = req[rid]["maxRideTimeMs"]
            w.writerow([world, arm, cell, role, cell[-3:], rid[:16], round((ws + t0 / 1000) / 60, 3), (p0 - t0) / 1000, (pick0 - t0) / 1000,
                        round((d0 - p0) / 1000, 3), mr / 1000, (pick0 + mr - p0) / 1000, len(others), onboard,
                        p0, round(d0, 1), t0, alighted[rid], round((alighted[rid] - d0) / 1000, 3)])
            n += 1
print("rows", n, "runs", len(RUNS))
