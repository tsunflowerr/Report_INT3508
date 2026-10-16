"""Census of what the reorder-capable (repair) generator actually did.

Item 4 of the open-question list asks for a generator that may reorder an
incumbent's stops, not merely insert into them. The repository already has one:
repair.maximumRequestsConsideredPerVehicle in the WP4 runner config, backed by
WaitingIncumbentRepairSeedBuilder. The b4 arm switched it on with a budget of 4
requests per vehicle and died on 18 of 20 cells with

    RBWP7_LOCKED_LEG_MISMATCH at $.vehicles[N].activeLeg

This script answers three questions from the transcripts, for every cell:

  Q1  Did it in fact reorder?  Count publications whose mutable suffix is a
      permutation of the previous one rather than an extension of it, and read
      the incumbentOrderInversionCount dimension of the commitment ledger.

  Q2  Does the head of the mutable suffix -- the stop the vehicle is currently
      driving to -- change between consecutive publications?  That is the move
      the adapter refuses.

  Q3  Does the reordering oscillate?  Count publications whose suffix order
      equals the order two publications earlier (A -> B -> A churn).

Read-only.
"""

from __future__ import annotations

import base64
import collections
import json
import pathlib

ROOT = pathlib.Path(r"E:/RideBoundData/wp9/exploratory-b4-repair-v1")


def frames(path: pathlib.Path):
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                yield json.loads(base64.b64decode(json.loads(line)["frameBase64"]))


def key(stop) -> tuple:
    return (stop.get("kind"), stop.get("stopId") or stop.get("nodeId"),
            stop.get("requestId"))


def analyse(cell: pathlib.Path) -> dict:
    stat = collections.Counter()
    per_vehicle: dict[str, list[list]] = {}

    for frame in frames(cell / "transcript-00.ndjson"):
        if frame.get("messageType") != "decision":
            continue
        for action in frame.get("payload", {}).get("actions", []):
            dt = action.get("decisionType")
            if dt == "promisePublished":
                after = action["payload"]["budgetAfter"]
                before = action["payload"]["budgetBefore"]
                delta = (after.get("incumbentOrderInversionCount", 0)
                         - before.get("incumbentOrderInversionCount", 0))
                stat["publications"] += 1
                if delta:
                    stat["inversionCharges"] += 1
                    stat["inversionUnits"] += delta
            elif dt == "vehiclePlanUpdated":
                p = action["payload"]
                vid = p.get("vehicleId")
                suffix = [key(s) for s in (p["route"].get("mutableSuffix") or [])]
                per_vehicle.setdefault(vid, []).append(suffix)
                stat["planUpdates"] += 1

    for vid, series in per_vehicle.items():
        for i in range(1, len(series)):
            prev, cur = series[i - 1], series[i]
            shared_prev = [s for s in prev if s in cur]
            shared_cur = [s for s in cur if s in prev]
            if shared_prev != shared_cur:
                stat["reorderedPublications"] += 1
            # did the head move?
            if prev and cur and prev[0] != cur[0] and prev[0] in cur:
                stat["headDisplaced"] += 1
            if i >= 2 and series[i - 2] and cur == series[i - 2] and cur != prev:
                stat["oscillations"] += 1
    stat["vehicles"] = len(per_vehicle)
    return stat


def main() -> int:
    rows = []
    total = collections.Counter()
    for directory in sorted(ROOT.iterdir()):
        if not directory.is_dir():
            continue
        ok = (directory / "summary.json").exists()
        failure = directory / "failure-00.json"
        message = ""
        if failure.exists():
            message = json.loads(failure.read_text(encoding="utf-8"))["failureMessage"]
        stat = analyse(directory)
        total.update(stat)
        rows.append((directory.name, ok, message, stat))

    head = (f"{'o':<34}{'xong':>5}{'cong bo':>9}{'sap lai':>9}"
            f"{'doi dau':>9}{'dao qua lai':>12}{'bi tinh phi':>12}")
    print(head)
    print("-" * len(head))
    for name, ok, message, stat in rows:
        print(f"{name.replace('-b4-tight-s7',''):<34}"
              f"{('co' if ok else 'hong'):>5}"
              f"{stat['publications']:>9,}"
              f"{stat['reorderedPublications']:>9,}"
              f"{stat['headDisplaced']:>9,}"
              f"{stat['oscillations']:>12,}"
              f"{stat['inversionCharges']:>12,}")
    print("-" * len(head))
    print(f"{'TONG':<34}{'':>5}"
          f"{total['publications']:>9,}"
          f"{total['reorderedPublications']:>9,}"
          f"{total['headDisplaced']:>9,}"
          f"{total['oscillations']:>12,}"
          f"{total['inversionCharges']:>12,}")
    print()
    print(f"Tong don vi dao thu tu bi tinh phi: {total['inversionUnits']:,}")
    print(f"Tong lan cap nhat ke hoach xe:      {total['planUpdates']:,}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
