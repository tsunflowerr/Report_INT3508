"""Are the 108 selected requests per panel-A fixture shorter than the eligible requests of the same window?
Direct time = shortest path on the full FleetPy Manhattan base network (edges.csv travel_time, before any traffic
factor). sourceRecordOrdinal = 0-based data-row index of the demand CSV (checked on d20181114-s10-r1-w08: ordinal 20862
is row '3791876,32631,173,565', matching the fixture request with arrival 3,831,000 ms after 08:00, nodes 173 -> 565).
Usage: python -B selection_length_check.py <out> (mode x)."""
import csv, json, pathlib, statistics as st, sys
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra
B = pathlib.Path("E:/RideBoundData/wp6/extracted/sha256/d9/d9e86f33645e5eec287d387f8d63ad41ddf41d4ef648138b65d636482e2c599e/FleetPy_Manhattan")
FIX = pathlib.Path("C:/RideBoundData/research/fixtures-panelA-v1")
rows, cols, w = [], [], []
with (B / "networks/Manhattan_2019_corrected/base/edges.csv").open(encoding="utf-8") as fh:
    for r in csv.DictReader(fh):
        rows.append(int(r["from_node"])); cols.append(int(r["to_node"])); w.append(float(r["travel_time"]))
n = max(max(rows), max(cols)) + 1
G = csr_matrix((w, (rows, cols)), shape=(n, n))
demand_cache, dist_cache = {}, {}
def demand(path):
    if path not in demand_cache:
        with (B / path).open(encoding="utf-8") as fh:
            demand_cache[path] = [(int(r["start"]), int(r["end"])) for r in csv.DictReader(fh)]
    return demand_cache[path]
def direct(o, d):
    if o not in dist_cache:
        dist_cache[o] = dijkstra(G, indices=o)
    return dist_cache[o][d]
def q(xs, p):
    xs = sorted(xs); return xs[min(len(xs) - 1, int(p * len(xs)))]
out = ["# selection_length_check.py (49 panel-A fixtures; direct = base free-flow shortest path, seconds)"]
sel_all, eli_all, rank = [], [], []
by_w = {}
for fx in sorted(p for p in FIX.iterdir() if p.is_dir()):
    cfg = json.loads((fx / "normalizer-configuration.json").read_text(encoding="utf-8"))
    rowsd = demand(cfg["demandMemberPath"].split("FleetPy_Manhattan/")[1])
    frame = json.loads((fx / "selection-frame.json").read_text(encoding="utf-8"))
    sel = [direct(*rowsd[x["sourceRecordOrdinal"]]) for x in frame if x["disposition"] == "selected"]
    eli = [direct(*rowsd[x["sourceRecordOrdinal"]]) for x in frame]
    sel_all += sel; eli_all += eli
    bw = by_w.setdefault(fx.name[-3:], ([], []))
    bw[0].extend(sel); bw[1].extend(eli)
    rank.append(st.median(sel) / st.median(eli))
out.append(f"selected {len(sel_all)}: mean {st.mean(sel_all):.1f}, p25 {q(sel_all, .25):.1f}, median {q(sel_all, .5):.1f}, p75 {q(sel_all, .75):.1f}, p90 {q(sel_all, .9):.1f}")
out.append(f"eligible {len(eli_all)}: mean {st.mean(eli_all):.1f}, p25 {q(eli_all, .25):.1f}, median {q(eli_all, .5):.1f}, p75 {q(eli_all, .75):.1f}, p90 {q(eli_all, .9):.1f}")
out.append(f"per-fixture median(selected)/median(eligible): min {min(rank):.3f}, median {st.median(rank):.3f}, max {max(rank):.3f}; fixtures below 1: {sum(1 for r in rank if r < 1)}/{len(rank)}")
for k, (s, e) in sorted(by_w.items()):
    out.append(f"  {k}: selected median {q(s, .5):.1f} (n {len(s)}), eligible median {q(e, .5):.1f} (n {len(e)})")
text = "\n".join(out) + "\n"
open(sys.argv[1], "x", encoding="utf-8", newline="\n").write(text); print(text)
