"""Fixture travel snapshot is scaled by the factor at travelFactorAtSeconds (0 = midnight for all 49 panel-A fixtures);
the world wrapper then multiplies by f(t)/f(window start). So simulated arc time at the window start = edges x f(0),
whereas the measured absolute level is edges x f(window start). This prints f(0), f(start) and their ratio per day
and window. Usage: python -B factor_anchor_check.py <out> (mode x)."""
import csv, json, pathlib, sys
F = pathlib.Path("E:/RideBoundData/wp6/extracted/sha256/d9/d9e86f33645e5eec287d387f8d63ad41ddf41d4ef648138b65d636482e2c599e/"
                 "FleetPy_Manhattan/networks/Manhattan_2019_corrected")
FIX = pathlib.Path("C:/RideBoundData/research/fixtures-panelA-v1")
anchors = {json.loads((d / "normalizer-configuration.json").read_text(encoding="utf-8"))["travelFactorAtSeconds"]
           for d in FIX.iterdir() if d.is_dir()}
out = [f"# factor_anchor_check.py; travelFactorAtSeconds over panel-A fixtures: {sorted(anchors)}",
       "day        f(00:00)  f(07:00)  f(08:00)  f(17:00)  f(0)/f(07) f(0)/f(08) f(0)/f(17)  min f  (time)   max f  (time)"]
for day in ("2018-11-12", "2018-11-13", "2018-11-14", "2018-11-15", "2018-11-16", "2018-11-17", "2018-11-18"):
    rows = {}
    with (F / f"{day}_tt_factors.csv").open(encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            rows[int(r["simulation_time"])] = float(r["travel_time_factor"])
    f0, f7, f8, f17 = rows[0], rows[25200], rows[28800], rows[61200]
    lo = min(rows, key=rows.get); hi = max(rows, key=rows.get)
    out.append(f"{day} {f0:8.3f} {f7:9.3f} {f8:9.3f} {f17:9.3f}  {f0/f7:9.3f} {f0/f8:10.3f} {f0/f17:10.3f}  {rows[lo]:6.3f} ({lo/3600:4.1f}h) {rows[hi]:6.3f} ({hi/3600:4.1f}h)")
text = "\n".join(out) + "\n"
open(sys.argv[1], "x", encoding="utf-8", newline="\n").write(text); print(text)
