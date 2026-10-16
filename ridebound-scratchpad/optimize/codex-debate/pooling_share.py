"""Share of served riders who shared the vehicle with at least one other rider during their ride (overlapping
[actual pickup, alight] intervals on the same assigned vehicle), and mean number of co-riders, 34 T3.8 test cells.
Usage: python -B pooling_share.py <out> (mode x)."""
import collections, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import forecast_family_a as fa
CELLS = fa.run_t38.PHASES["test"][1]
out = ["# pooling_share.py (34 T3.8 test cells; served riders pooled)"]
for arm in ("U", "C-30", "Mplus-30"):
    shared = total = 0
    co, by_w = [], collections.defaultdict(lambda: [0, 0])
    for cell in CELLS:
        t = fa.run_dir("test", arm, cell) / "transcript-00.ndjson"
        _, _, state = fa.audit_vep.load(t)
        _, alighted = fa.sweep_analyze.event_times(t)
        legs = collections.defaultdict(list)
        for r in state["requests"]:
            if r["requestId"] in alighted:
                legs[r["assignedVehicleId"]].append((r["actualPickupTimeMs"], alighted[r["requestId"]], r["requestId"]))
        for veh, rs in legs.items():
            for a0, a1, rid in rs:
                k = sum(1 for b0, b1, other in rs if other != rid and b0 < a1 and a0 < b1)
                total += 1; shared += k > 0; co.append(k)
                by_w[cell[-3:]][0] += k > 0; by_w[cell[-3:]][1] += 1
    out.append(f"{arm}: served {total}; shared ride {100 * shared / total:.1f}%; mean co-riders {sum(co) / len(co):.2f}; "
               + ", ".join(f"{w} {100 * s / n:.1f}% of {n}" for w, (s, n) in sorted(by_w.items())))
text = "\n".join(out) + "\n"
open(sys.argv[1], "x", encoding="utf-8", newline="\n").write(text); print(text)
