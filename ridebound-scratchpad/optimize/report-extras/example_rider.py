"""One real rider for the plain-language explanation: C-30 run d20181115-s10-r1-w07 (test cell), the rider whose id
starts rq-30b7e083c7b (late 190.5 s in contract-split-check). Prints request time, first drop promise (naive and
displayed with the causal-no15 forecast), every displayed revision and the alight time. Usage: python -B example_rider.py <out>"""
import pathlib, sys
HERE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import display_layer as dl, forecast_family_a as fa
cell = "d20181115-s10-r1-w07"
prof = dl.profile("2018-11-15", "w07", "causal-no15")
run = fa.run_dir("test", "C-30", cell)
transcript = run / "transcript-00.ndjson"
_, _, state = fa.audit_vep.load(transcript)
table, _ = fa.audit_vep.audit(transcript)
_, alighted = fa.sweep_analyze.event_times(transcript)
rid = next(r for r in alighted if r.startswith("rq-30b7e083c7b"))
req = next(r for r in state["requests"] if r["requestId"] == rid)
clock = lambda ms: f"{7 + int(ms // 3_600_000)}:{int(ms % 3_600_000 // 60_000):02d}:{int(ms % 60_000 // 1000):02d}"  # noqa: E731
out = [f"# example_rider.py {cell} {rid[:14]}", f"request at {clock(req['arrivalTimeMs'])}, picked up at {clock(req['actualPickupTimeMs'])}, alighted at {clock(alighted[rid])}"]
rows = sorted((s, k, pub, p) for r, c, s, k, pub, v, e, p, x, cc, z, closed in table if r == rid and c == "drop")
for s, k, pub, p in rows:
    out.append(f"  drop promise #{s} published {clock(pub)}: system {clock(p)} | displayed with forecast {clock(dl.display(pub, p, prof))}")
p0, d0, a = rows[0][3], dl.display(rows[0][2], rows[0][3], prof), alighted[rid]
out.append(f"late vs first promise: naive {(a - p0) / 1000:+.1f} s; displayed {(a - d0) / 1000:+.1f} s; first promise lengthened by {(d0 - p0) / 1000:.1f} s")
out.append(f"visible drop change: naive {sum(abs(rows[i][3] - rows[i-1][3]) for i in range(1, len(rows))) / 1000:.1f} s; displayed "
           f"{sum(abs(dl.display(rows[i][2], rows[i][3], prof) - dl.display(rows[i-1][2], rows[i-1][3], prof)) for i in range(1, len(rows))) / 1000:.1f} s")
text = "\n".join(out) + "\n"
open(sys.argv[1], "x", encoding="utf-8", newline="\n").write(text); print(text)
