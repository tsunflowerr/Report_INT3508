"""Tests for sweep_analyze.py on real T3.7 pilot outputs (read-only) and on a synthetic audit table.

Run: python -B test_sweep_analyze.py   (fails if fewer checks ran than expected)
"""
from __future__ import annotations

import base64
import json
import pathlib

import sweep_analyze as sa

PILOT = pathlib.Path(r"E:/RideBoundData/research/tier3-pilot-v1")
failures, checks = [], 0


def check(name, condition):
    global checks
    checks += 1
    if not condition:
        failures.append(name)
        print("FAIL", name)


def final_state(transcript):
    final, last_promise = None, {}
    with open(transcript, encoding="utf-8") as handle:
        for line in handle:
            record = json.loads(line)
            envelope = json.loads(base64.b64decode(record["frameBase64"]))
            if record["direction"] == "runnerToAdapter" and envelope.get("messageType") == "checkpoint":
                final = envelope["payload"]["content"]["onlineState"]
    for history in final["commitmentLedger"]:
        last_promise[history["requestId"]] = history["entries"][-1]["publishedPromise"]["projection"]["dropEtaMs"]
    return final, last_promise


# 1. The batch-time rule reproduces the Runner's actual pickup times, and drop times sit near the last promise.
transcript = PILOT / "U-W0-d20181112-s10-r1-w08" / "transcript-00.ndjson"
boarded, alighted = sa.event_times(transcript)
final, last_promise = final_state(transcript)
pick = {q["requestId"]: q["actualPickupTimeMs"] for q in final["requests"] if q.get("actualPickupTimeMs") is not None}
check("every boarding time equals actualPickupTimeMs", pick and all(boarded.get(r) == t for r, t in pick.items()))
completed = {q["requestId"] for q in final["requests"] if q["lifecycle"] == "completed"}
check("every completed rider has an alighting time", completed == set(alighted))
gaps = sorted(abs(alighted[r] - last_promise[r]) for r in completed)
print(f"|actual drop - last published drop| over {len(gaps)} riders: median {gaps[len(gaps) // 2]} ms, max {gaps[-1]} ms")
check("actual drop is close to the last published promise (median < 60 s)", gaps[len(gaps) // 2] < 60_000)

# 2. rider_values on a synthetic table: initial p is the anchor, |c| summed over open drop revisions only.
table = [
    ("r1", "drop", 0, "initialPromise", 0, 100, 100, 100, 0, 0, 0, 0),
    ("r1", "drop", 1, "revision", 10, 100, 130, 150, 30, 20, 50, 0),
    ("r1", "drop", 2, "revision", 20, 150, 140, 130, -10, -10, -20, 0),
    ("r1", "pickup", 1, "revision", 10, 50, 50, 90, 0, 40, 40, 0),
    ("r2", "drop", 0, "initialPromise", 0, 500, 500, 500, 0, 0, 0, 0),
]
first, c = sa.rider_values(table)
check("first promise is the initial drop p", first == {"r1": 100, "r2": 500})
check("C_r sums |c| over drop revisions, pickup ignored", c == {"r1": 30, "r2": 0})

# 3. job_row on pilot jobs reproduces known numbers (pilot table, independently verified).
sa.OUT_ROOT = PILOT
sa.state_of = lambda name: "test"
c30 = sa.job_row("C-30-W4-d20181112-s10-r1-w08", "C-30", "W4", "d20181112-s10-r1-w08")
check("audit ok", c30.get("audit") == "ok")
check("C-30 W4 w08 completed 94", c30["M1_completed"] == 94)
check("C-30 W4 w08 max C 19118 ms", c30["M4_maxC_ms"] == 19118)
check("C-30 keeps its own promise (no rider C > 30 s)", c30["M4_shareC_gt_x"] == 0)
check("C-30 has no forced breach", c30["M5_forcedBreaches"] == 0)
mp = sa.job_row("Mplus-30-W4-d20181112-s10-r1-w08", "Mplus-30", "W4", "d20181112-s10-r1-w08")
check("Mplus-30 W4 w08 completed 92", mp["M1_completed"] == 92)
check("Mplus-30 W4 w08 has forced breaches", mp["M5_forcedBreaches"] > 0)
check("lateness shares are within [0, 1]",
      all(0 <= mp[k] <= 1 for k in mp if k.startswith("M3_shareA")) and all(0 <= c30[k] <= 1 for k in c30 if k.startswith("M3_shareA")))
print({k: c30[k] for k in ("M3_meanA_ms", "M3_p95A_ms", "M3_maxA_ms", "M3_shareA_gt_x")},
      {k: mp[k] for k in ("M3_meanA_ms", "M3_p95A_ms", "M3_maxA_ms", "M3_shareA_gt_x")})
check("M3 max A equals the max of the per-rider A map", c30["M3_maxA_ms"] == max(c30["_A"].values()))

print(f"{checks} checks, {len(failures)} failure(s)")
raise SystemExit(1 if failures or checks < 14 else 0)
