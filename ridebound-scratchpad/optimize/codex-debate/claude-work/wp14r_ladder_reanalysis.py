"""Zero-run re-analysis of the existing WP14r v6 commitment ladder (160 runs, older Runner and world; 16 cells x 10
arms; RB-WP14R-009). For the five distinct arms b1-ref (free), c1-nobudget (locks), c1-budget120, c1-budget60,
c1-h6ref (30 s): served, shared share (another rider on board), drop exposure (any nonzero dispatch part c), size of
nonzero dispatch drop revisions, lateness vs FIRST drop promise (>60/120/300 s), travel snapshot versions (to tell
whether the world had time-varying traffic). Usage: python -B wp14r_ladder_reanalysis.py <out> (mode x)."""
import collections, json, pathlib, statistics as st, sys
OPT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(OPT))
import forecast_family_a as fa
ROOT = pathlib.Path("E:/RideBoundData/wp14r/development-v6-ledger")
ARMS = ("b1-ref", "c1-nobudget", "c1-budget120", "c1-budget60", "c1-h6ref")
out = ["# wp14r_ladder_reanalysis.py (WP14r v6, 160 runs exist; 5 distinct arms analysed)"]
for arm in ARMS:
    req = served = shared = exposed = late60 = late120 = late300 = 0
    moves, snaps, cells, windows = [], collections.Counter(), 0, collections.Counter()
    for run in sorted(ROOT.glob(f"w14-*-{arm}-s7")):
        t = run / "attempt-01" / "output" / "transcript-00.ndjson"
        if not t.exists():
            continue
        cells += 1; windows[run.name.split("-")[4]] += 1
        sem = json.loads((t.parent / "run-00.json").read_text(encoding="utf-8"))["semantic"]
        snaps[sem.get("travelSnapshotVersion")] += 1
        _, _, state = fa.audit_vep.load(t)
        table, _ = fa.audit_vep.audit(t)
        _, alighted = fa.sweep_analyze.event_times(t)
        req += len(state["requests"])
        first, exp = {}, set()
        for r, c, s, k, pub, v, e, p, x, cc, z, cl in table:
            if c != "drop": continue
            if k == "initialPromise": first[r] = p
            elif cc != 0: exp.add(r); moves.append(abs(cc) / 1000)
        legs = collections.defaultdict(list)
        for r in state["requests"]:
            if r["requestId"] in alighted:
                legs[r["assignedVehicleId"]].append((r["actualPickupTimeMs"], alighted[r["requestId"]], r["requestId"]))
        for rs in legs.values():
            for a0, a1, rid in rs:
                served += 1
                shared += any(o != rid and b0 < a1 and a0 < b1_ for b0, b1_, o in rs)
                exposed += rid in exp
                if rid in first:
                    lat = a1 - first[rid]
                    late60 += lat > 60000; late120 += lat > 120000; late300 += lat > 300000
    mv = sorted(moves)
    out.append(f"{arm:<13} cells {cells} {dict(windows)} | served {served}/{req} ({100 * served / req:.1f}%) | shared {100 * shared / served:.1f}% | "
               f"exposed {100 * exposed / served:.1f}% | nonzero dispatch moves n {len(mv)} median {st.median(mv) if mv else 0:.1f} s p90 {mv[int(.9 * (len(mv) - 1))] if mv else 0:.1f} s | "
               f"late vs first promise >60 s {100 * late60 / served:.2f}% >120 s {100 * late120 / served:.2f}% >300 s {100 * late300 / served:.2f}% | "
               f"travelSnapshotVersion {dict(snaps)}")
text = "\n".join(out) + "\n"
open(sys.argv[1], "x", encoding="utf-8", newline="\n").write(text); print(text)
