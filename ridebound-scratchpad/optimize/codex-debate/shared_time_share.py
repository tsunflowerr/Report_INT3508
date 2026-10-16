"""Shared passenger-minutes as a share of total onboard passenger-minutes, five T3.8 arms, 34 test cells
(same overlap definition as exposure_check.py). Usage: python -B shared_time_share.py <out> (mode x)."""
import collections, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import forecast_family_a as fa
CELLS = fa.run_t38.PHASES["test"][1]
out = ["# shared_time_share.py (34 T3.8 test cells)"]
for arm in ("U", "C-30", "Mplus-30", "Mplus-60", "V-30"):
    shared = onboard = 0.0
    for cell in CELLS:
        t = fa.run_dir("test", arm, cell) / "transcript-00.ndjson"
        _, _, state = fa.audit_vep.load(t)
        _, alighted = fa.sweep_analyze.event_times(t)
        legs = collections.defaultdict(list)
        for r in state["requests"]:
            if r["requestId"] in alighted:
                legs[r["assignedVehicleId"]].append((r["actualPickupTimeMs"], alighted[r["requestId"]], r["requestId"]))
        for rs in legs.values():
            for a0, a1, rid in rs:
                onboard += (a1 - a0) / 60000
                ov = sorted((max(a0, b0), min(a1, b1)) for b0, b1, o in rs if o != rid and b0 < a1 and a0 < b1)
                if ov:
                    tot, cs, ce = 0, *ov[0]
                    for s0, s1 in ov[1:]:
                        if s0 > ce: tot += ce - cs; cs, ce = s0, s1
                        else: ce = max(ce, s1)
                    shared += (tot + ce - cs) / 60000
    out.append(f"{arm}: onboard passenger-min {onboard:.0f}; shared passenger-min {shared:.0f}; share {100 * shared / onboard:.1f}%")
text = "\n".join(out) + "\n"
open(sys.argv[1], "x", encoding="utf-8", newline="\n").write(text); print(text)
