"""Independent check of Codex round-1 numbers: served-rider overlap U vs C-30 over the 34 T3.8 test cells, and mean
ride / wait / door-to-door difference among common riders. Usage: python -B common_riders_check.py <out> (mode x)."""
import pathlib, statistics as st, sys
HERE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import forecast_family_a as fa
CELLS = fa.run_t38.PHASES["test"][1]
def served(arm, cell):
    t = fa.run_dir("test", arm, cell) / "transcript-00.ndjson"
    _, _, state = fa.audit_vep.load(t)
    _, alighted = fa.sweep_analyze.event_times(t)
    out = {}
    for r in state["requests"]:
        if r["requestId"] in alighted:
            pick = r["actualPickupTimeMs"]
            out[r["requestId"]] = ((pick - r["arrivalTimeMs"]) / 1000, (alighted[r["requestId"]] - pick) / 1000)
    return out
lines = ["# common_riders_check.py (34 T3.8 test cells)"]
for other in ("C-30", "Mplus-30"):
    common = only_u = only_o = 0
    dw, dr = [], []
    for cell in CELLS:
        u, o = served("U", cell), served(other, cell)
        c = set(u) & set(o)
        common += len(c); only_u += len(set(u) - c); only_o += len(set(o) - c)
        for r in c:
            dw.append(o[r][0] - u[r][0]); dr.append(o[r][1] - u[r][1])
    lines.append(f"U vs {other}: common {common}, only U {only_u}, only {other} {only_o}")
    lines.append(f"  common riders, {other} minus U: wait {st.mean(dw):+.3f} s, ride {st.mean(dr):+.3f} s, door {st.mean(dw)+st.mean(dr):+.3f} s;"
                 f" ride shorter for {sum(1 for x in dr if x < -1)} riders, longer for {sum(1 for x in dr if x > 1)}")
text = "\n".join(lines) + "\n"
open(sys.argv[1], "x", encoding="utf-8", newline="\n").write(text); print(text)
