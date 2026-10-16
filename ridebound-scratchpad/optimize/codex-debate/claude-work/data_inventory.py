"""Complete read-only inventory of every saved simulation run on disk (2026-10-08).
Walks E:/RideBoundData and C:/RideBoundData/research, finds every run-00.json (one per run attempt with output),
and records: root experiment folder, run folder, requests, vehicles, accepted requests, travelSnapshotVersion
(1 = no travel-time update during the run), simulated span, presence of a transcript and its size, mtime.
Writes a per-run TSV and a per-experiment summary. Usage: python -B data_inventory.py <tsv-out> <summary-out> (mode x)."""
import collections, datetime, json, os, pathlib, sys
ROOTS = [pathlib.Path("E:/RideBoundData"), pathlib.Path("C:/RideBoundData/research")]
SKIP = {"literature-survey-2026-10-06", "wp6", "envs", "FleetPy-1.0.2"}
rows = []
for root in ROOTS:
    for base, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in SKIP and not d.startswith(".")]
        if "run-00.json" not in files:
            continue
        p = pathlib.Path(base)
        rel = p.relative_to(root)
        exp = (root.name if root.name == "research" and root.drive == "C:" else "") + "/".join(rel.parts[:2]) if rel.parts else str(root)
        try:
            d = json.loads((p / "run-00.json").read_text(encoding="utf-8"))
            s = d.get("semantic", {})
        except Exception as e:
            rows.append(dict(exp=exp, run=str(rel), err=type(e).__name__)); continue
        t = p / "transcript-00.ndjson"
        rows.append(dict(exp=exp, run=str(rel), status=d.get("status"), req=s.get("requestCount"),
                         veh=len(s.get("finalVehiclePositions") or []), acc=len(s.get("acceptedRequestIds") or []),
                         snap=s.get("travelSnapshotVersion"), span_h=round((s.get("finalSimulationTimeMs") or 0) / 3.6e6, 2),
                         tr_mb=round(t.stat().st_size / 1e6, 1) if t.exists() else 0,
                         mtime=datetime.datetime.fromtimestamp((p / "run-00.json").stat().st_mtime).strftime("%Y-%m-%d"), err=""))
keys = ["exp", "run", "status", "req", "veh", "acc", "snap", "span_h", "tr_mb", "mtime", "err"]
with open(sys.argv[1], "x", encoding="utf-8", newline="\n") as fh:
    fh.write("\t".join(keys) + "\n")
    for r in rows:
        fh.write("\t".join(str(r.get(k, "")) for k in keys) + "\n")
g = collections.defaultdict(list)
for r in rows:
    g[r["exp"]].append(r)
out = [f"# data_inventory.py: {len(rows)} run records (run-00.json) under {', '.join(map(str, ROOTS))}",
       "experiment | runs | with transcript | requests | vehicles | accepted total | snapshot versions (1 = static) | span h | dates"]
for exp, rs in sorted(g.items()):
    c = lambda k: dict(collections.Counter(r.get(k) for r in rs).most_common(4))  # noqa: E731
    out.append(f"{exp} | {len(rs)} | {sum(1 for r in rs if r.get('tr_mb'))} | {c('req')} | {c('veh')} | {sum(r.get('acc') or 0 for r in rs)} | "
               f"{dict(collections.Counter('static' if r.get('snap') == 1 else 'varying' if (r.get('snap') or 0) > 1 else str(r.get('snap')) for r in rs))} | "
               f"{c('span_h')} | {min(r.get('mtime', '') for r in rs)}..{max(r.get('mtime', '') for r in rs)}")
text = "\n".join(out) + "\n"
open(sys.argv[2], "x", encoding="utf-8", newline="\n").write(text); print(text)
