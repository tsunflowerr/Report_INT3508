"""Does the shipped insertion-only generator ever displace the in-flight stop?

Background. The reorder-capable generator in the repository (the b4 repair arm)
crashes 18 of 20 cells with

    RBWP7_LOCKED_LEG_MISMATCH at $.vehicles[N].activeLeg

because FleetPy locks the leg a vehicle has departed on, while RideBound's
RoutePlan freezes a stop only when it is REACHED (AdvanceReachedStop). Between
departure and arrival the target stop sits at MutableSuffix[0] and is, as far as
the domain model is concerned, still editable.

That raises an obvious question: why does the shipped insertion-only generator
never trip the same check? Two possibilities.

  (i)  Insertion cannot displace the head by construction.  False on its face --
       inserting a new pickup at mutable index 0 would displace it.
  (ii) It can, but never does, because the schedule feasibility test almost
       always rejects an insertion that delays the stop the vehicle is already
       driving to.

This script settles it by measuring head displacement on the SEALED panel, using
exactly the definition that matters: consecutive publications for the same
vehicle where the first element of the mutable suffix changes while the old first
element is still somewhere in the new plan (i.e. it was demoted, not served).

Arms compared:
    B1  rolling cost, no promise constraint   (most freedom, insertion-only)
    C1  hard vector, 30 s cap                 (insertion-only, gated)
    b4  no-reassignment-repair, cap 4         (reorder-capable, uncommitted)

Read-only.
"""

from __future__ import annotations

import base64
import collections
import json
import pathlib

PANELS = {
    "B1 (khong hua)": (pathlib.Path(r"E:/RideBoundData/wp9/confirmatory-h6-panela-v2"),
                       "p-{cell}-b1-tight-s7"),
    "C1 (tran 30 s)": (pathlib.Path(r"E:/RideBoundData/wp9/confirmatory-h6-panela-v2"),
                       "p-{cell}-c1-tight-s7"),
    "b4 (sap lai)":   (pathlib.Path(r"E:/RideBoundData/wp9/exploratory-b4-repair-v1"),
                       "x-{cell}-b4-tight-s7"),
}

CELLS = [
    "d201811{}-s10-r{}".format(day, rep)
    for day in (14, 15, 16, 17, 18)
    for rep in (1, 2, 3, 4)
]


def frames(path: pathlib.Path):
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                yield json.loads(base64.b64decode(json.loads(line)["frameBase64"]))


def key(stop) -> tuple:
    return (stop.get("kind"), stop.get("stopId") or stop.get("nodeId"),
            stop.get("requestId"))


def analyse(directory: pathlib.Path) -> collections.Counter:
    stat: collections.Counter = collections.Counter()
    per_vehicle: dict[str, list[list]] = {}
    transcript = directory / "transcript-00.ndjson"
    if not transcript.exists():
        return stat
    for frame in frames(transcript):
        if frame.get("messageType") != "decision":
            continue
        for action in frame.get("payload", {}).get("actions", []):
            if action.get("decisionType") != "vehiclePlanUpdated":
                continue
            payload = action["payload"]
            route = payload["route"]
            suffix = [key(s) for s in (route.get("mutableSuffix") or [])]
            per_vehicle.setdefault(payload.get("vehicleId"), []).append(
                (route.get("executedStopCount"), len(route.get("frozenPrefix") or []),
                 suffix))
            stat["planUpdates"] += 1

    for series in per_vehicle.values():
        for i in range(1, len(series)):
            (_, pf_prev, prev) = series[i - 1]
            (ex_cur, pf_cur, cur) = series[i]
            if pf_cur != ex_cur:
                stat["frozenAheadOfExecuted"] += 1
            if not prev or not cur:
                continue
            shared_prev = [s for s in prev if s in cur]
            shared_cur = [s for s in cur if s in prev]
            if shared_prev != shared_cur:
                stat["reordered"] += 1
            if prev[0] != cur[0]:
                stat["headChanged"] += 1
                if prev[0] in cur:
                    stat["headDemoted"] += 1      # the refused move
                else:
                    stat["headConsumed"] += 1     # served or dropped: legal
    stat["vehicles"] = len(per_vehicle)
    return stat


def main() -> int:
    head = ("{:<18}{:>7}{:>10}{:>11}{:>10}{:>11}{:>12}".format(
        "nhanh", "o", "cap nhat", "sap lai", "doi dau", "dau bi day", "dong bang som"))
    print(head)
    print("-" * len(head))
    for name, (root, pattern) in PANELS.items():
        total: collections.Counter = collections.Counter()
        cells = 0
        for cell in CELLS:
            directory = root / pattern.format(cell=cell)
            if not (directory / "transcript-00.ndjson").exists():
                continue
            cells += 1
            total.update(analyse(directory))
        print("{:<18}{:>7}{:>10,}{:>11,}{:>10,}{:>11,}{:>12,}".format(
            name, cells, total["planUpdates"], total["reordered"],
            total["headChanged"], total["headDemoted"],
            total["frozenAheadOfExecuted"]))
    print("-" * len(head))
    print()
    print("'dau bi day' = chang xe dang chay den bi day xuong sau trong ke hoach moi.")
    print("Day dung la nuoc di ma FleetPy tu choi (RBWP7_LOCKED_LEG_MISMATCH).")
    print("'dong bang som' = so lan frozenPrefix dai hon executedStopCount, tuc la")
    print("he thong da dong bang mot chang TRUOC khi xe den. Neu bang 0 thi mo hinh")
    print("mien chua he dung kha nang do, du kieu du lieu cho phep.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
