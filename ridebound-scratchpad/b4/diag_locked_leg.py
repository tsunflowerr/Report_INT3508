"""Why does the repair (reorder-capable) arm crash?

The b4 arm switches on repair.maximumRequestsConsideredPerVehicle = 4, which
lets the generator rebuild an incumbent vehicle's stop order instead of only
inserting into it. 18 of 20 cells die with

    RBWP7_LOCKED_LEG_MISMATCH at $.vehicles[N].activeLeg

The adapter refuses a replacement plan whose FIRST leg is not byte-identical to
the leg the vehicle is already executing (status, destination, boarding rids,
alighting rids, lock flag, duration, earliest start, earliest end).

Two very different readings:
  (a) the repaired plan genuinely sends the vehicle to a different next stop
      while it is mid-leg  ->  physically impossible, the wall is real;
  (b) the next stop is the same and only a timing field differs  ->  the wall
      is an adapter strictness artefact and could be relaxed.

This script reads the transcript of a failing cell, finds the last decision,
and prints the incumbent vs proposed stop order for the offending vehicle.
Read-only.
"""

from __future__ import annotations

import base64
import json
import pathlib
import re
import sys


def frames(path: pathlib.Path):
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            outer = json.loads(line)
            yield json.loads(base64.b64decode(outer["frameBase64"]))


def stop_order(plan) -> list:
    out = []
    for stop in plan.get("stops", []) or []:
        out.append((
            stop.get("locationId") or stop.get("nodeId") or stop.get("location"),
            tuple(sorted(stop.get("boardingRequestIds", []) or [])),
            tuple(sorted(stop.get("alightingRequestIds", []) or [])),
        ))
    return out


def main() -> int:
    cell = sys.argv[1] if len(sys.argv) > 1 else "x-d20181114-s10-r2-b4-tight-s7"
    root = pathlib.Path(r"E:/RideBoundData/wp9/exploratory-b4-repair-v1") / cell
    failure = json.loads((root / "failure-00.json").read_text(encoding="utf-8"))
    match = re.search(r"vehicles\[(\d+)\]", failure["failureMessage"])
    vid = match.group(1) if match else None
    print(f"o: {cell}")
    print(f"loi: {failure['failureMessage']}")
    print(f"xe: {vid}")
    print()

    transcript = root / "transcript-00.ndjson"
    decisions = []
    observations = []
    for frame in frames(transcript):
        kind = frame.get("messageType")
        if kind == "decision":
            decisions.append(frame)
        elif kind in ("observation", "event", "state"):
            observations.append(frame)
    print(f"khung decision: {len(decisions)}   khung khac: {len(observations)}")
    if not decisions:
        print("khong co khung decision -> hong ngay truoc quyet dinh dau tien")
        return 0

    last = decisions[-1]
    print(f"decision cuoi: t={last.get('simulationTimeMs')}  "
          f"seq={last.get('sequence')}")
    keys = sorted(last.get("payload", {}).keys())
    print(f"payload keys: {keys}")

    # dump the assignment actions of the final decision
    for action in last.get("payload", {}).get("actions", []):
        dt = action.get("decisionType")
        body = json.dumps(action.get("payload", {}))[:400]
        print(f"  {dt}: {body}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
