"""Write the v1.3 forecast configs (causal-no15 sources, horizonBins 2), the E2 K=1 sham config, and the sealed
expected ratio table configs/r-table.json for every tier1/tier2 cell (ratio per bin 0..8 = v13.ratio(profile, b, 2)).
Input-only: reads factor files, never a run. All files mode x. Usage: python -B make_forecast_configs.py <log>"""
import hashlib, json, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import run_forecast as rf, display_layer as dl, preflight_world_v1_3 as v13
cfg = HERE / "configs"; cfg.mkdir(exist_ok=True)
lines = ["# make_forecast_configs.py"]
for d in ("14", "15", "16"):
    day = f"2018-11-{d}"
    src = list(dl.sources(day, "causal-no15"))
    for k in (2, 1):
        if k == 1 and day != rf.day(rf.E2_CELL):
            continue
        path = cfg / f"forecast-k{k}-{day}.json"
        text = json.dumps({"forecastVersion": "forecast-v1", "horizonBins": k, "sourceDays": src}) + "\n"
        with open(path, "x", encoding="utf-8", newline="\n") as h:
            h.write(text)
        lines.append(f"{path.name}: sources {src}; sha256 {hashlib.sha256(text.encode()).hexdigest()}")
table = {}
for c in rf.W07 + rf.W08:
    prof = v13.forecast_profile(list(dl.sources(rf.day(c), "causal-no15")), dl.WINDOW_STARTS[c[-3:]])
    table[c] = [round(v13.ratio(prof, b, 2), 6) for b in range(9)]
text = json.dumps(table, indent=1) + "\n"
with open(cfg / "r-table.json", "x", encoding="utf-8", newline="\n") as h:
    h.write(text)
lines.append(f"r-table.json sha256 {hashlib.sha256(text.encode()).hexdigest()}")
for c, rs in table.items():
    lines.append(f"  {c}: {rs}")
lines.append(f"E1 cell {rf.E1_CELL}; E2 cell {rf.E2_CELL}")
out = "\n".join(lines) + "\n"
open(sys.argv[1], "x", encoding="utf-8", newline="\n").write(out); print(out)
