"""Extra context checks (not part of the claims): Mplus vs V fleet sequences; decisions per run."""
import glob
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
RUNS = {}
for p in glob.glob(os.path.join(HERE, "runs", "*.json")):
    with open(p, "r", encoding="utf-8") as f:
        d = json.load(f)
    RUNS[(d["arm"], d["cell"])] = d
CELLS = sorted(set(c for _, c in RUNS))
out = []
for L in (30, 90, 120, 150, 180, 240):
    diffs = []
    for c in CELLS:
        m = [x["fa_full"] for x in RUNS[("Mplus-%d" % L, c)]["decisions"]]
        v = [x["fa_full"] for x in RUNS[("V-%d" % L, c)]["decisions"]]
        if m != v:
            diffs.append(c)
    out.append("Mplus-%d vs V-%d fleet-action sequences differ in cells: %s" % (L, L, diffs))
# decision-count per arm/cell for the three divergent pairs
for (L, c) in ((90, "d20181112-s10-r1-w07"), (120, "d20181112-s10-r1-w07"), (120, "d20181113-s10-r1-w07")):
    out.append("n acked decisions at (%d,%s): C %d Mplus %d V %d" % (
        L, c, RUNS[("C-%d" % L, c)]["n_acked_decisions"], RUNS[("Mplus-%d" % L, c)]["n_acked_decisions"],
        RUNS[("V-%d" % L, c)]["n_acked_decisions"]))
# max A_r and max V_r per arm (seconds)
for arm in ("C-90", "Mplus-90", "V-90", "Mplus-150", "V-150", "Mplus-240", "V-240"):
    amax = max((r["alight"] - r["first_drop"]) for c in CELLS for r in RUNS[(arm, c)]["riders"].values() if r["life"] == "completed")
    vmax = max(r["V"] for c in CELLS for r in RUNS[(arm, c)]["riders"].values())
    vdmax = max(r["Vdec"] for c in CELLS for r in RUNS[(arm, c)]["riders"].values())
    out.append("%-10s max A_r %.1f s, max V_r %.1f s, max sum|p-e| %.1f s" % (arm, amax / 1000, vmax / 1000, vdmax / 1000))
print("\n".join(out))
with open(os.path.join(HERE, "extra_output.txt"), "x", encoding="utf-8") as f:
    f.write("\n".join(out) + "\n")
