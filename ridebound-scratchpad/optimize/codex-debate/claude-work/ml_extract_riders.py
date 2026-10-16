"""Rider-level dataset for the ML pilot (data preparation only; no model, no evaluation). Read-only on run outputs.
Sources (all existing runs):
  t38   : T3.8 test arms U and C-30 (34 cells) + C-30 calibration (15 cells), measured traffic (world v1.2)
  w07   : tier3-w07-v1 arms U and C-30 (8 dev cells, 12-13/11 07-09), measured traffic
  wp14r : WP14r v6 arms b1-ref (FREE), c1-nobudget (LOCKS), c1-budget120, c1-budget60, c1-h6ref (C-30), 16 cells, static
One row per served rider with a first drop promise. Features are known at the first drop promise time t0:
  bin, minute, horizon_s (P0-t0), direct_s (maxRide/1.5), room_s, wait_promised_s, fc_ext_s (D0-P0, causal-no15; 0 for
  static/wp14r or inactive cells), load_t0 (other riders on the same vehicle with t0_o <= t0 < alight_o),
  onboard_t0 (of those, already picked up before t0).
Targets / diagnostics (NOT features): y_s = A - P0; disp_sum_s (signed sum of c on drop), traf_sum_s (signed sum of x),
  exposed (any c != 0). Usage: python -B ml_extract_riders.py <out.csv> (mode x)."""
import csv, pathlib, sys
OPT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(OPT))
import display_layer as dl, forecast_family_a as fa
SOURCES = []
for cell in fa.run_t38.PHASES["test"][1]:
    for arm in ("U", "C-30"):
        SOURCES.append(("t38", arm, cell, fa.run_dir("test", arm, cell) / "transcript-00.ndjson", True))
for cell in fa.run_t38.PHASES["calib"][1]:
    SOURCES.append(("t38cal", "C-30", cell, fa.run_dir("calib", "C-30", cell) / "transcript-00.ndjson", True))
W07 = pathlib.Path("C:/RideBoundData/research/tier3-w07-v1")
for d in sorted(W07.glob("U-d2018*")) + sorted(W07.glob("C-30-d2018*")):
    arm, cell = ("U", d.name[2:]) if d.name.startswith("U-") else ("C-30", d.name[5:])
    SOURCES.append(("w07", arm, cell, d / "transcript-00.ndjson", True))
W14 = pathlib.Path("E:/RideBoundData/wp14r/development-v6-ledger")
NAMES = {"b1-ref": "FREE", "c1-nobudget": "LOCKS", "c1-budget120": "C-120", "c1-budget60": "C-60", "c1-h6ref": "C-30"}
for tag, arm in NAMES.items():
    for d in sorted(W14.glob(f"w14-*-{tag}-s7")):
        SOURCES.append(("wp14r", arm, d.name[4:].replace(f"-{tag}-s7", ""), d / "attempt-01" / "output" / "transcript-00.ndjson", False))
cols = ["source", "arm", "cell", "day", "sample", "window", "rider", "t0_ms", "bin", "minute", "horizon_s", "direct_s", "room_s",
        "wait_promised_s", "fc_ext_s", "load_t0", "onboard_t0", "y_s", "disp_sum_s", "traf_sum_s", "exposed"]
with open(sys.argv[1], "x", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh); w.writerow(cols); n = 0
    for src, arm, cell, t, traffic in SOURCES:
        if not t.exists():
            print("MISSING", src, arm, cell); continue
        day = fa.day_of(cell)
        _, _, state = fa.audit_vep.load(t)
        table, _ = fa.audit_vep.audit(t)
        _, alighted = fa.sweep_analyze.event_times(t)
        req = {r["requestId"]: r for r in state["requests"]}
        prof = dl.profile(day, cell[-3:], "causal-no15") if traffic else None
        first, disp, traf, exp = {}, {}, {}, set()
        for r, c, s, k, pub, v, e, p, x, cc, z, cl in table:
            if k == "initialPromise":
                first[(r, c)] = (pub, p)
            elif c == "drop":
                disp[r] = disp.get(r, 0) + cc; traf[r] = traf.get(r, 0) + x
                if cc != 0: exp.add(r)
        riders = [r for r in req if r in alighted and (r, "drop") in first and (r, "pickup") in first]
        t0s = {r: first[(r, "drop")][0] for r in riders}
        byveh = {}
        for r in riders:
            byveh.setdefault(req[r]["assignedVehicleId"], []).append(r)
        for r in riders:
            t0, p0 = first[(r, "drop")]; pk = first[(r, "pickup")][1]; q = req[r]
            others = [o for o in byveh[q["assignedVehicleId"]] if o != r and t0s[o] <= t0 < alighted[o]]
            onboard = sum(1 for o in others if req[o]["actualPickupTimeMs"] < t0)
            d0 = dl.display(t0, p0, prof) if prof else p0
            w.writerow([src, arm, cell, day, cell.split("-")[2], cell[-3:], r[:16], t0, t0 // 900000, round(t0 / 60000, 2),
                        (p0 - t0) / 1000, round(q["maxRideTimeMs"] / 1500, 1), (pk + q["maxRideTimeMs"] - p0) / 1000,
                        (pk - q["arrivalTimeMs"]) / 1000, round((d0 - p0) / 1000, 3), len(others), onboard,
                        (alighted[r] - p0) / 1000, disp.get(r, 0) / 1000, traf.get(r, 0) / 1000, int(r in exp)])
            n += 1
print("rows", n, "sources", len(SOURCES))
