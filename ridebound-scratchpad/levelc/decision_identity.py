"""Are the two arms making the same decisions, or only scoring the same?

Level C's sealed semanticHash differs from its control on every cell, yet every
one of the nine instability measures, the publication count and the served count
come out bit-identical. Two readings:

  (i)  the warning layer changes which plan is chosen, and the changes happen to
       cancel on every aggregate measure -- implausible but checkable;
  (ii) the hash differs only because the soft-hybrid arm RECORDS more (a
       different policy id, warning assessments attached to each candidate),
       while the chosen plans are the same. Then the warning layer is inert.

The discriminator is the chosen plan itself. Candidate ids are content-derived
fingerprints of a route, so if the two arms pick the same plans the id sequences
match exactly. This compares, per cell:

    the ordered sequence of (vehicleId, candidateId) actually assigned
    the ordered sequence of published promise ETAs

Read-only.
"""

from __future__ import annotations

import base64
import json
import pathlib

CONTROL = pathlib.Path(r"E:/RideBoundData/wp9/frontier-v1")
TREAT = pathlib.Path(r"E:/RideBoundData/wp14/levelc-v1")
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


def trace(directory: pathlib.Path) -> tuple[list, list, list]:
    """Plans assigned, promises published, and the reason code, per decision.

    Promises are collected as a SORTED group per decision frame. The order in
    which a frame emits its publications is an artefact of how the policy walks
    its candidates, and the soft-hybrid path walks them differently; comparing
    the raw sequence therefore reports a difference where there is none. What
    matters is which promises a frame published, not in what order.
    """
    plans: list = []
    promises: list = []
    reasons: list = []
    for frame in frames(directory / "transcript-00.ndjson"):
        if frame.get("messageType") != "decision":
            continue
        reasons.append(frame.get("payload", {}).get("reasonCode"))
        group: list = []
        for action in frame.get("payload", {}).get("actions", []):
            kind = action.get("decisionType")
            payload = action.get("payload", {})
            if kind == "vehiclePlanUpdated":
                plans.append((payload.get("vehicleId"),
                              payload.get("candidateId")))
            elif kind == "promisePublished":
                promise = payload["promise"]
                group.append((promise["requestId"],
                              promise["pickupEtaMs"],
                              promise["dropEtaMs"]))
        promises.append(sorted(group))
    return plans, promises, reasons


def main() -> int:
    head = "{:<22}{:>9}{:>9}{:>12}{:>12}{:>10}".format(
        "o", "ke hoach", "loi hua", "ke hoach", "loi hua", "ly do")
    print("So sanh tung quyet dinh giua doi chung (tran 120 s) va muc C")
    print("Hai cot dau: so luong. Ba cot sau: co giong het khong.")
    print()
    print(head)
    print("-" * len(head))
    verdicts: list[bool] = []
    for cell in CELLS:
        a = CONTROL / "fr-budget120-{}-s7".format(cell)
        b = TREAT / "lc-{}-s7".format(cell)
        if not ((a / "summary.json").exists() and (b / "summary.json").exists()):
            continue
        pa, qa, ra = trace(a)
        pb, qb, rb = trace(b)
        same_plan = pa == pb
        same_promise = qa == qb
        same_reason = ra == rb
        verdicts.append(same_plan and same_promise and same_reason)
        print("{:<22}{:>9,}{:>9,}{:>12}{:>12}{:>10}".format(
            cell, len(pb), sum(len(g) for g in qb),
            "giong" if same_plan else "KHAC",
            "giong" if same_promise else "KHAC",
            "giong" if same_reason else "KHAC"))
    print("-" * len(head))
    print()
    if verdicts and all(verdicts):
        print("Moi quyet dinh trung khop tren {} o.".format(len(verdicts)))
        print("=> Tang canh bao KHONG doi mot quyet dinh nao. Bam ngu nghia khac")
        print("   nhau chi vi nhanh soft-hybrid ghi them chung cu canh bao.")
    elif verdicts:
        print("Co {}/{} o quyet dinh trung khop -- tang canh bao co tac dong thuc.".format(
            sum(verdicts), len(verdicts)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
