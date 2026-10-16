"""Exposure to later dispatch changes, all five T3.8 arms, 34 test cells, served riders pooled.
- shared: another rider on board during my ride (same assigned vehicle, overlapping [pickup, alight]);
- drop-exposed: at least one drop-promise revision with a nonzero dispatch part c = p - e (this also counts insertions
  made before I board, which shift my drop promise without any onboard overlap);
- pickup-exposed: same for the pickup promise;
- Y = actual drop more than 60 s after the first drop promise, split by drop exposure;
- shared passenger-minutes = sum over riders of minutes with at least one co-rider on board.
Usage: python -B exposure_check.py <out> (mode x)."""
import collections, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import forecast_family_a as fa
CELLS = fa.run_t38.PHASES["test"][1]
out = ["# exposure_check.py (34 T3.8 test cells; served riders pooled)"]
for arm in ("U", "C-30", "Mplus-30", "Mplus-60", "V-30"):
    n = shared = dexp = pexp = 0
    late = collections.Counter(); grp = collections.Counter(); shared_min = 0.0
    for cell in CELLS:
        t = fa.run_dir("test", arm, cell) / "transcript-00.ndjson"
        _, _, state = fa.audit_vep.load(t)
        table, _ = fa.audit_vep.audit(t)
        _, alighted = fa.sweep_analyze.event_times(t)
        first, touched = {}, collections.defaultdict(bool)
        for r, c, s, k, pub, v, e, p, x, cc, z, closed in table:
            if k == "initialPromise":
                first[(r, c)] = p
            elif cc != 0:
                touched[(r, c)] = True
        legs = collections.defaultdict(list)
        for r in state["requests"]:
            if r["requestId"] in alighted:
                legs[r["assignedVehicleId"]].append((r["actualPickupTimeMs"], alighted[r["requestId"]], r["requestId"]))
        for veh, rs in legs.items():
            for a0, a1, rid in rs:
                n += 1
                ov = [(max(a0, b0), min(a1, b1)) for b0, b1, o in rs if o != rid and b0 < a1 and a0 < b1]
                shared += bool(ov)
                if ov:  # union length of overlap intervals
                    ov.sort(); tot, cs, ce = 0, *ov[0]
                    for s0, s1 in ov[1:]:
                        if s0 > ce: tot += ce - cs; cs, ce = s0, s1
                        else: ce = max(ce, s1)
                    shared_min += (tot + ce - cs) / 60000
                de = touched[(rid, "drop")]; dexp += de; pexp += touched[(rid, "pickup")]
                g = "exposed" if de else "unexposed"
                grp[g] += 1; late[g] += (a1 - first[(rid, "drop")]) > 60000
    yl = lambda g: f"{100 * late[g] / grp[g]:.2f}% of {grp[g]}" if grp[g] else "n/a"  # noqa: E731
    out.append(f"{arm}: served {n}; shared {100 * shared / n:.1f}%; drop-exposed {100 * dexp / n:.1f}%; pickup-exposed {100 * pexp / n:.1f}%; "
               f"Y exposed {yl('exposed')}, unexposed {yl('unexposed')}; late riders that are exposed "
               f"{late['exposed']}/{late['exposed'] + late['unexposed']}; shared passenger-minutes {shared_min:.0f}")
text = "\n".join(out) + "\n"
open(sys.argv[1], "x", encoding="utf-8", newline="\n").write(text); print(text)
