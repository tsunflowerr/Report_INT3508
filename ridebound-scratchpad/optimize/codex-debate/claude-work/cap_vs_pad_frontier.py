"""Cap vs pad frontier, zero-run replay of the 34 T3.8 test cells (served riders pooled; 3,672 requests per arm).
For each arm and promise policy, the rider is shown D for the first DROP promise (p0 published at t0) and arrives at A:
  naive          D = p0
  pad k          D = p0 + k                          (k seconds for every rider)
  fc             D = display(t0, p0)                 (causal-no15 forecast display layer; naive where inactive)
  fc+pad k       D = display(t0, p0) + k
  fc+prop a      D = t0 + (display(t0, p0) - t0) * (1 + a)
Metrics: Y60 = share A - D > 60 s; Y120; early60 = share A - D < -60 s; ext = mean (D - p0) s;
timely = served riders with A - D <= 60 s, per request (served share x (1 - Y60)). Vehicles never change: this is a
promise-only replay. Usage: python -B cap_vs_pad_frontier.py <out> (mode x)."""
import pathlib, statistics as st, sys
OPT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(OPT))
import display_layer as dl, forecast_family_a as fa
CELLS = fa.run_t38.PHASES["test"][1]
REQ = 3672
def riders(arm):
    rs = []
    for cell in CELLS:
        t = fa.run_dir("test", arm, cell) / "transcript-00.ndjson"
        table, _ = fa.audit_vep.audit(t)
        _, alighted = fa.sweep_analyze.event_times(t)
        prof = dl.profile(fa.day_of(cell), cell[-3:], "causal-no15")
        for r, c, s, k, pub, v, e, p, x, cc, z, closed in table:
            if k == "initialPromise" and c == "drop" and r in alighted:
                rs.append((pub, p, dl.display(pub, p, prof), alighted[r]))
    return rs
def row(name, rs, f):
    lat = [a - f(t, p, d) for t, p, d, a in rs]
    ext = [f(t, p, d) - p for t, p, d, a in rs]
    n = len(rs)
    y60 = sum(1 for x in lat if x > 60000) / n
    return (f"{name:<22} served {n:5d}  Y60 {100 * y60:6.2f}%  Y120 {100 * sum(1 for x in lat if x > 120000) / n:5.2f}%  "
            f"early60 {100 * sum(1 for x in lat if x < -60000) / n:5.2f}%  ext {st.mean(ext) / 1000:6.1f} s  "
            f"timely/request {100 * n * (1 - y60) / REQ:6.2f}%  (timely {round(n * (1 - y60))})")
out = ["# cap_vs_pad_frontier.py (34 T3.8 test cells, 3,672 requests per arm; promise-only replay)"]
for arm in ("U", "C-30", "Mplus-30"):
    rs = riders(arm)
    out.append(f"\n== {arm}")
    out.append(row("naive", rs, lambda t, p, d: p))
    for k in (15, 30, 60, 90, 120, 180, 240):
        out.append(row(f"pad {k}s", rs, lambda t, p, d, k=k: p + 1000 * k))
    out.append(row("fc", rs, lambda t, p, d: d))
    for k in (15, 30, 60, 90, 120, 180):
        out.append(row(f"fc+pad {k}s", rs, lambda t, p, d, k=k: d + 1000 * k))
    for a in (0.05, 0.10, 0.20, 0.30):
        out.append(row(f"fc+prop {a:.2f}", rs, lambda t, p, d, a=a: t + (d - t) * (1 + a)))
text = "\n".join(out) + "\n"
open(sys.argv[1], "x", encoding="utf-8", newline="\n").write(text); print(text)
