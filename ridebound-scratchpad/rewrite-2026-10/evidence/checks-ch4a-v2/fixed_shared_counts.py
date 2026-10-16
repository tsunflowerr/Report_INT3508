"""Read-only count of shared riders on the fixed-traffic set (WP14r v6, 16 cells; 2026-10-12).

Same rule as wp14r_ladder_reanalysis.py (CW, lines 32-39): a served rider (requestId with a passengerAlighted event)
is "shared" when another served rider of the same assigned vehicle has an overlapping [actual pickup, alight)
interval. State = the last runner checkpoint (onlineState); alight = simTimeMs of the first adapter eventBatch that
carries the rider's passengerAlighted event. Frame hashes are checked as in audit_vep.read_frames.
Purpose: give the exact numerators behind the rounded shares 53.1 / 21.8 / 19.4 / 17.3 / 15.7 % printed by LAD.
Inputs (read only): E:/RideBoundData/wp14r/development-v6-ledger/w14-*-<arm>-s7/attempt-01/output/transcript-00.ndjson
Usage: python -B -I fixed_shared_counts.py <out.txt>   (the output file is opened in mode "x")
"""
import base64
import collections
import hashlib
import json
import pathlib
import sys

ROOT = pathlib.Path("E:/RideBoundData/wp14r/development-v6-ledger")
ARMS = ("b1-ref", "c1-nobudget", "c1-budget120", "c1-budget60", "c1-h6ref")
LAD_SHARE = {"b1-ref": "53.1", "c1-nobudget": "21.8", "c1-budget120": "19.4", "c1-budget60": "17.3", "c1-h6ref": "15.7"}
LAD_SERVED = {"b1-ref": 1629, "c1-nobudget": 1584, "c1-budget120": 1563, "c1-budget60": 1540, "c1-h6ref": 1534}
out = ["# fixed_shared_counts.py (WP14r v6 fixed traffic, 5 arms, rule of wp14r_ladder_reanalysis.py)"]
fails = 0
for arm in ARMS:
    req = served = shared = cells = 0
    windows = collections.Counter()
    for run in sorted(ROOT.glob(f"w14-*-{arm}-s7")):
        t = run / "attempt-01" / "output" / "transcript-00.ndjson"
        if not t.exists():
            continue
        cells += 1
        windows[run.name.split("-")[4]] += 1
        final, alighted = None, {}
        with open(t, encoding="utf-8") as fh:
            for number, line in enumerate(fh):
                record = json.loads(line)
                frame = base64.b64decode(record["frameBase64"])
                if hashlib.sha256(frame).hexdigest() != record["frameSha256"]:
                    raise SystemExit(f"{t}: line {number}: frame hash mismatch")
                env = json.loads(frame)
                kind = env.get("messageType")
                if record["direction"] == "runnerToAdapter" and kind == "checkpoint":
                    final = env["payload"]["content"]["onlineState"]
                elif record["direction"] == "adapterToRunner" and kind == "eventBatch":
                    for ev in env["payload"].get("events", []):
                        if ev.get("eventType") == "passengerAlighted":
                            alighted.setdefault(ev["payload"]["requestId"], env["simTimeMs"])
        req += len(final["requests"])
        legs = collections.defaultdict(list)
        for r in final["requests"]:
            if r["requestId"] in alighted:
                legs[r["assignedVehicleId"]].append((r["actualPickupTimeMs"], alighted[r["requestId"]], r["requestId"]))
        for rs in legs.values():
            for a0, a1, rid in rs:
                served += 1
                shared += any(o != rid and b0 < a1 and a0 < b1 for b0, b1, o in rs)
    share = f"{100 * shared / served:.1f}"
    ok = served == LAD_SERVED[arm] and share == LAD_SHARE[arm]
    fails += (not ok)
    out.append(f"{arm:<13} cells {cells} {dict(windows)} | requests {req} | served {served} | shared {shared} "
               f"({share}% of served) | LAD served {LAD_SERVED[arm]}, shared {LAD_SHARE[arm]}% -> {'OK' if ok else 'FAIL'}")
out.append(f"FAIL count: {fails}")
text = "\n".join(out) + "\n"
with open(sys.argv[1], "x", encoding="utf-8", newline="\n") as fh:
    fh.write(text)
print(text)
