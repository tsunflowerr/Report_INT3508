"""Development-cell diagnostic (not a result): v1.2, v1.3 smoke, v1.4 naive/forecast on d20181112-s10-r1-w07, C-30.
Splits drop-ETA revisions into later (z > 0) and earlier (z < 0) and lateness vs first promise.
Usage: python -B smoke_breakdown.py <out> (mode x)"""
import pathlib, sys
TANG3 = pathlib.Path(__file__).resolve().parents[1] / "tang3"
for sub in ("sweep", "evidence", "t38", "w07"):
    sys.path.insert(0, str(TANG3 / sub))
import audit_vep, sweep_analyze, run_w07
import t38_rider_experience as rx
RUNS = {"v1.2": run_w07.OUT_ROOT / "C-30-d20181112-s10-r1-w07",
        **{n: pathlib.Path(r"C:/RideBoundData/research/tier3-forecast-checks-v1") / n for n in ("smoke-k2", "v14-naive-u300", "v14-fc-d900-u300", "v14-fc-d1800-u300")}}
out = []
for name, run in RUNS.items():
    t = run / "transcript-00.ndjson"
    table, _ = audit_vep.audit(t)
    _, alighted = sweep_analyze.event_times(t)
    up = sum(z for r, c, _, k, _, _, _, _, _, _, z, cl in table if c == "drop" and k != "initialPromise" and z > 0)
    down = -sum(z for r, c, _, k, _, _, _, _, _, _, z, cl in table if c == "drop" and k != "initialPromise" and z < 0)
    first = {r: p for r, c, _, k, _, _, _, p, _, _, _, _ in table if c == "drop" and k == "initialPromise"}
    lat = [alighted[r] - first[r] for r in first if r in alighted]
    m = rx.run_metrics(run); m.pop("_served_ids")
    out.append(f"{name}: served {m['served']}; drop revisions later {up/1000:.1f} s, earlier {down/1000:.1f} s; "
               f"lateness vs first promise: late>60s {sum(1 for a in lat if a > 60000)}, early>60s {sum(1 for a in lat if a < -60000)}, "
               f"mean {sum(lat)/len(lat)/1000:+.1f} s; visible60 {m['visible60']:.3f}; jump_share {m['jump_share']:.3f}")
text = "\n".join(out) + "\n"
open(sys.argv[1], "x", encoding="utf-8", newline="\n").write(text); print(text)
