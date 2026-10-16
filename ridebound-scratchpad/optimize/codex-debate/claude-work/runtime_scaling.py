"""Runtime vs scenario size over all saved run records (run-00.json) of past experiments. Read-only.
Per run: requests, vehicles, simulated span, decision epochs (nextEpoch), events (nextEventSeq), publications, user+system
CPU of the measured process, wall time, transcript size. Grouped by (requests, vehicles). Usage: python -B runtime_scaling.py <out> (mode x)."""
import collections, json, pathlib, statistics as st, sys
ROOTS = [pathlib.Path(p) for p in ("E:/RideBoundData/wp7", "E:/RideBoundData/wp8", "E:/RideBoundData/wp9", "E:/RideBoundData/wp13",
                                   "E:/RideBoundData/wp14", "E:/RideBoundData/research", "C:/RideBoundData/research")]
rows = []
for root in ROOTS:
    for f in root.rglob("run-00.json"):
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
            s, r = d["semantic"], d["resources"]
        except Exception:
            continue
        if d.get("status") not in (None, "pass", "succeeded") or "requestCount" not in s:
            continue
        tr = f.parent / "transcript-00.ndjson"
        rows.append(dict(src=str(f.parent.relative_to(root.parent)).split("\\")[0].split("/")[0], req=s["requestCount"],
                         veh=len(s["finalVehiclePositions"]), span_h=s["finalSimulationTimeMs"] / 3.6e6, epochs=s["nextEpoch"],
                         events=s["nextEventSeq"], pubs=s.get("publicationCount", 0),
                         cpu=(r["userCpuMilliseconds"] + r["systemCpuMilliseconds"]) / 1000, wall=r["wallMilliseconds"] / 1000,
                         mb=tr.stat().st_size / 1e6 if tr.exists() else float("nan")))
g = collections.defaultdict(list)
for x in rows:
    g[(x["req"], x["veh"])].append(x)
out = [f"# runtime_scaling.py: {len(rows)} run records with status pass or succeeded", "requests vehicles runs | span_h med | epochs med | events med | CPU s med (p90) | wall s med | CPU ms per epoch med | transcript MB med"]
for (q, v), xs in sorted(g.items()):
    m = lambda k: st.median(x[k] for x in xs)  # noqa: E731
    cpus = sorted(x["cpu"] for x in xs)
    out.append(f"{q:>8} {v:>8} {len(xs):>4} | {m('span_h'):6.1f} | {m('epochs'):7.0f} | {m('events'):7.0f} | {m('cpu'):7.1f} ({cpus[int(.9*(len(cpus)-1))]:7.1f}) | "
               f"{m('wall'):7.1f} | {st.median(1000 * x['cpu'] / max(1, x['epochs']) for x in xs):7.1f} | {m('mb'):7.1f}")
text = "\n".join(out) + "\n"
open(sys.argv[1], "x", encoding="utf-8", newline="\n").write(text); print(text)
