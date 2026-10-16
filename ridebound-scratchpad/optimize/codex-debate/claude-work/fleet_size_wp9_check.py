"""Existing evidence on fewer vehicles: WP9 confirmatory H6 v2 runs, panel A (108 requests, 8 vehicles) vs panel B
(108 requests, 4 vehicles), arms b1 (rolling cost, no commitment) and c1 (hard vector, tight 30 s). Older Runner and
WP9 world; descriptive only. Per arm/panel: served share, shared-ride share (another rider on board), mean co-riders,
drop-exposed share (nonzero dispatch part c on the drop promise) when the ledger audit parses.
Usage: python -B fleet_size_wp9_check.py <out> (mode x)."""
import collections, pathlib, sys
OPT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(OPT))
import forecast_family_a as fa
ROOTS = {"A (8 veh)": pathlib.Path("E:/RideBoundData/wp9/confirmatory-h6-panela-v2"),
         "B (4 veh)": pathlib.Path("E:/RideBoundData/wp9/confirmatory-h6-panelb-v2")}
out = ["# fleet_size_wp9_check.py (WP9 H6 v2; older Runner; descriptive)"]
for panel, root in ROOTS.items():
    for arm in ("b1", "c1"):
        req = served = shared = exposed = audited = 0; co = 0; cells = 0; audit_fail = 0
        for run in sorted(root.glob(f"*-{arm}-*")):
            t = run / "transcript-00.ndjson"
            if not t.exists():
                continue
            cells += 1
            _, _, state = fa.audit_vep.load(t)
            _, alighted = fa.sweep_analyze.event_times(t)
            req += len(state["requests"])
            legs = collections.defaultdict(list)
            for r in state["requests"]:
                if r["requestId"] in alighted:
                    legs[r["assignedVehicleId"]].append((r["actualPickupTimeMs"], alighted[r["requestId"]], r["requestId"]))
            for rs in legs.values():
                for a0, a1, rid in rs:
                    k = sum(1 for b0, b1_, o in rs if o != rid and b0 < a1 and a0 < b1_)
                    served += 1; shared += k > 0; co += k
            try:
                table, _ = fa.audit_vep.audit(t)
                ex = {r for r, c, s, kk, pub, v, e, p, x, cc, z, cl in table if c == "drop" and cc != 0}
                exposed += len(ex & set(alighted)); audited += sum(1 for rs in legs.values() for _ in rs)
            except Exception:
                audit_fail += 1
        if cells:
            out.append(f"panel {panel} arm {arm}: cells {cells}, requests {req}, served {served} ({100 * served / req:.1f}%), "
                       f"shared {100 * shared / served:.1f}%, mean co-riders {co / served:.2f}, "
                       + (f"drop-exposed {100 * exposed / audited:.1f}%" if audited else "drop-exposed n/a")
                       + (f", audit failed on {audit_fail} runs" if audit_fail else ""))
text = "\n".join(out) + "\n"
open(sys.argv[1], "x", encoding="utf-8", newline="\n").write(text); print(text)
