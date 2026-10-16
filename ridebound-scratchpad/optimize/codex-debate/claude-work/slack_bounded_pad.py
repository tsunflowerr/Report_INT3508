"""Risk-aware padding, zero-run replay of U and C-30 on the 34 T3.8 test cells.
Pickup promises are never moved by dispatch (exposure-check-2026-10-06.txt), and the max-ride-time constraint bounds
how late a later insertion can push a rider's drop. So at the first drop promise the 'insertion room' is known:
  room = first pickup promise + maxRideTimeMs - first drop promise   (>= 0 by feasibility; seconds)
(1) Exposure (any nonzero dispatch part c on the drop promise) and lateness by room bucket.
(2) Pad policies on top of the forecast display D (causal-no15), compared at equal mean extension:
    uniform:   D + k
    bounded:   D + min(k, a * room)     (pad never exceeds a share a of the insertion room)
Metrics as in cap_vs_pad_frontier.py. Usage: python -B slack_bounded_pad.py <out> (mode x)."""
import collections, pathlib, statistics as st, sys
OPT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(OPT))
import display_layer as dl, forecast_family_a as fa
CELLS = fa.run_t38.PHASES["test"][1]
REQ = 3672
def riders(arm):
    rs = []
    for cell in CELLS:
        t = fa.run_dir("test", arm, cell) / "transcript-00.ndjson"
        _, _, state = fa.audit_vep.load(t)
        table, _ = fa.audit_vep.audit(t)
        _, alighted = fa.sweep_analyze.event_times(t)
        req = {r["requestId"]: r for r in state["requests"]}
        prof = dl.profile(fa.day_of(cell), cell[-3:], "causal-no15")
        first, exposed = {}, collections.defaultdict(bool)
        for r, c, s, k, pub, v, e, p, x, cc, z, closed in table:
            if k == "initialPromise":
                first[(r, c)] = (pub, p)
            elif c == "drop" and cc != 0:
                exposed[r] = True
        for r in req:
            if r not in alighted or (r, "drop") not in first:
                continue
            t0, p0 = first[(r, "drop")]
            room = (first[(r, "pickup")][1] + req[r]["maxRideTimeMs"] - p0) / 1000
            rs.append(dict(t0=t0, p0=p0, d=dl.display(t0, p0, prof), a=alighted[r], room=room, exp=exposed[r]))
    return rs
def metrics(rs, f):
    lat = [x["a"] - f(x) for x in rs]; ext = [f(x) - x["p0"] for x in rs]; n = len(rs)
    y60 = sum(1 for v in lat if v > 60000) / n
    return y60, st.mean(ext) / 1000, sum(1 for v in lat if v < -60000) / n, n * (1 - y60)
out = ["# slack_bounded_pad.py (34 T3.8 test cells; promise-only replay)"]
for arm in ("U", "C-30"):
    rs = riders(arm)
    out.append(f"\n== {arm}: {len(rs)} served; room (s): p10 {sorted(x['room'] for x in rs)[len(rs)//10]:.0f}, median {st.median(x['room'] for x in rs):.0f}, p90 {sorted(x['room'] for x in rs)[9*len(rs)//10]:.0f}")
    for lo, hi in ((0, 60), (60, 120), (120, 240), (240, 1e9)):
        g = [x for x in rs if lo <= x["room"] < hi]
        if g:
            late = sum(1 for x in g if x["a"] - x["p0"] > 60000)
            out.append(f"  room [{lo:>4.0f}, {hi:>5.0f}) s: riders {len(g):5d}; exposed {100 * sum(x['exp'] for x in g) / len(g):5.1f}%; naive Y60 {100 * late / len(g):5.1f}% ({late})")
    out.append("  policy                      Y60     ext(s)  early60  timely")
    for k in (30, 60, 90, 120, 180):
        y, e, er, tm = metrics(rs, lambda x, k=k: x["d"] + 1000 * k)
        out.append(f"  fc + uniform {k:>3d}s         {100 * y:5.2f}%  {e:6.1f}   {100 * er:5.1f}%  {tm:6.0f}")
        for a in (0.25, 0.5, 1.0):
            y, e, er, tm = metrics(rs, lambda x, k=k, a=a: x["d"] + 1000 * min(k, a * max(0.0, x["room"])))
            out.append(f"  fc + min({k:>3d}s, {a:.2f} room)  {100 * y:5.2f}%  {e:6.1f}   {100 * er:5.1f}%  {tm:6.0f}")
text = "\n".join(out) + "\n"
open(sys.argv[1], "x", encoding="utf-8", newline="\n").write(text); print(text)
