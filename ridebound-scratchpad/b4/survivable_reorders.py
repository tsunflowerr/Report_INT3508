"""If the in-flight stop were frozen, how much reordering would survive?

The reorder-capable arm dies because it demotes the stop a vehicle is already
driving to. The proposed fix is to freeze that stop: move MutableSuffix[0] into
FrozenPrefix on departure rather than on arrival. RoutePlan already permits the
resulting state (ExecutedStopCount < FrozenPrefix.Count).

That fix is only worth doing if a useful part of the reorder neighbourhood
survives it. This script partitions the reorderings actually observed in the b4
arm into two classes:

    LEGAL   the head of the mutable suffix is unchanged; the reordering happens
            strictly behind the stop the vehicle is driving to. A head freeze
            would still allow it.
    BLOCKED the head changed while the old head is still in the plan, i.e. the
            stop was demoted. A head freeze would forbid it -- and today it is
            exactly what crashes the run.

The split is the upper bound on what step 1 of the three-step fix would leave
to work with. Read-only.
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


def main() -> int:
    stat: collections.Counter = collections.Counter()
    for directory in sorted(ROOT.iterdir()):
        transcript = directory / "transcript-00.ndjson"
        if not transcript.exists():
            continue
        per_vehicle: dict[str, list[list]] = {}
        for frame in frames(transcript):
            if frame.get("messageType") != "decision":
                continue
            for action in frame.get("payload", {}).get("actions", []):
                if action.get("decisionType") != "vehiclePlanUpdated":
                    continue
                payload = action["payload"]
                per_vehicle.setdefault(payload.get("vehicleId"), []).append(
                    [key(s) for s in
                     (payload["route"].get("mutableSuffix") or [])])

        for series in per_vehicle.values():
            for i in range(1, len(series)):
                prev, cur = series[i - 1], series[i]
                if not prev or not cur:
                    continue
                shared_prev = [s for s in prev if s in cur]
                shared_cur = [s for s in cur if s in prev]
                if shared_prev == shared_cur:
                    continue                      # not a reordering
                stat["reorderings"] += 1
                if prev[0] == cur[0]:
                    stat["legalUnderFreeze"] += 1
                elif prev[0] in cur:
                    stat["blockedByFreeze"] += 1  # head demoted
                else:
                    stat["headConsumed"] += 1     # head was served, not demoted

    total = max(stat["reorderings"], 1)
    print("SAP XEP LAI QUAN SAT DUOC TRONG NHANH b4")
    print()
    print("  tong so lan sap xep lai              {:>6,}".format(stat["reorderings"]))
    print("  van hop le neu dong bang chang dau   {:>6,}  ({:5.1f} %)".format(
        stat["legalUnderFreeze"], 100.0 * stat["legalUnderFreeze"] / total))
    print("  bi chan neu dong bang chang dau      {:>6,}  ({:5.1f} %)".format(
        stat["blockedByFreeze"], 100.0 * stat["blockedByFreeze"] / total))
    print("  chang dau da duoc phuc vu xong       {:>6,}  ({:5.1f} %)".format(
        stat["headConsumed"], 100.0 * stat["headConsumed"] / total))
    print()
    print("Dong 2 la phan con lai de lam viec sau khi sua buoc 1.")
    print("Dong 3 la phan dang lam sap chuong trinh hom nay.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
