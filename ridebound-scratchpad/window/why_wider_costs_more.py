"""Why does a wider pickup window make the SAME promise more expensive?

The measured fact (section 4.9 of the report): going from a 600 s to a 900 s
pickup window raises the price of a 30 s promise from 7.13 to 8.56 percentage
points of service. The promise did not change. The window is not part of the
promise. So the extra cost has to come from somewhere else.

Three candidate explanations, only one of which survives measurement:

  H1  MORE CHOICES.  A wider window makes more insertions physically legal, so
      each decision has a bigger candidate set. A bigger set contains more plans
      that would move an existing promise, so the commitment gate deletes more.
      Prediction: candidates generated and commitment-prunes both rise.

  H2  BIGGER MOVES.  The same number of candidates, but each one displaces
      promises further, so each one is more likely to exceed the cap.
      Prediction: candidate count flat, per-candidate displacement rises.

  H3  MORE EXPOSURE.  Riders sit in the "promise open" state longer (waits rose
      from 407 s to 636 s), so each rider is exposed to more decision epochs and
      accumulates budget over a longer life.
      Prediction: publications per rider rises.

These are not mutually exclusive; the point is to find which one carries the
effect. Read-only; nothing is written into the repository.

Usage:  why_wider_costs_more.py [cells]      (default 6 cells)
"""

from __future__ import annotations

import base64
import collections
import json
import pathlib
import sys

SEALED = pathlib.Path(r"E:/RideBoundData/wp9/confirmatory-h6-panela-v2")
WIDE = pathlib.Path(r"E:/RideBoundData/wp14/wide-window-v1")

CELLS = [
    f"d201811{day}-s10-r{rep}"
    for day in (14, 15, 16, 17, 18)
    for rep in (1, 2, 3, 4)
]


def walk_pruned(node, out: list) -> None:
    if isinstance(node, dict):
        if "prunedCandidates" in node:
            out.append(node["prunedCandidates"])
        if "vehicleAssessments" in node:
            out.append(("assess", node["vehicleAssessments"]))
        for value in node.values():
            walk_pruned(value, out)
    elif isinstance(node, list):
        for value in node:
            walk_pruned(value, out)


def scan(directory: pathlib.Path) -> dict:
    stat = collections.Counter()
    per_request_pubs: collections.Counter = collections.Counter()
    retained: list[int] = []
    unique_before_cap: list[int] = []

    with (directory / "transcript-00.ndjson").open(encoding="utf-8") as handle:
        for line in handle:
            frame = json.loads(base64.b64decode(json.loads(line)["frameBase64"]))
            if frame.get("messageType") != "decision":
                continue
            for action in frame.get("payload", {}).get("actions", []):
                if action.get("decisionType") == "promisePublished":
                    payload = action["payload"]
                    stat["publications"] += 1
                    per_request_pubs[payload["promise"]["requestId"]] += 1
                    delta = payload["decisionDelta"]
                    stat["decisionMs"] += (delta["dropEtaTotalMs"]
                                           + delta["pickupEtaTotalMs"])
            found: list = []
            walk_pruned(frame, found)
            for item in found:
                if isinstance(item, tuple):
                    for entry in item[1]:
                        stat["vehicleDecisions"] += 1
                        r = entry.get("retainedCandidateCount")
                        u = entry.get("uniqueFeasibleCandidateCountBeforeCap")
                        p = entry.get("physicallyOrSchedulePrunedCount")
                        if r is not None:
                            retained.append(r)
                        if u is not None:
                            unique_before_cap.append(u)
                        if p is not None:
                            stat["physSchedPruned"] += p
                    continue
                for pruned in item:
                    stat["prunedTotal"] += 1
                    code = pruned.get("code") or ""
                    if pruned.get("commitmentWitnesses"):
                        stat["prunedByCommitment"] += 1
                    elif code:
                        stat["prunedByPhysical"] += 1

    run = json.loads((directory / "run-00.json").read_text(encoding="utf-8"))
    stat["accepted"] = len(run["semantic"]["acceptedRequestIds"])
    stat["riders"] = len(per_request_pubs)
    stat["retainedSum"] = sum(retained)
    stat["retainedN"] = len(retained)
    stat["uniqueSum"] = sum(unique_before_cap)
    stat["uniqueN"] = len(unique_before_cap)
    return stat


def main() -> int:
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    cells = CELLS[:n]
    totals = {"600 s": collections.Counter(), "900 s": collections.Counter()}
    for cell in cells:
        for label, directory in (
            ("600 s", SEALED / f"p-{cell}-c1-tight-s7"),
            ("900 s", WIDE / f"ww-c1-{cell}-s7"),
        ):
            if not (directory / "summary.json").exists():
                print(f"thieu: {directory.name}")
                continue
            totals[label].update(scan(directory))
        print(f"  quet xong {cell}", flush=True)

    print()
    print(f"Ca hai cau hinh deu la C1 (tran 30 s). Chi khac cua so don. {len(cells)} o.")
    print()
    rows = [
        ("Khach duoc phuc vu", "accepted", 1, "{:,.0f}"),
        ("Tong lan cong bo loi hua", "publications", 1, "{:,.0f}"),
        ("Lan cong bo / khach", None, None, None),
        ("Tong quyet dinh cap xe", "vehicleDecisions", 1, "{:,.0f}"),
        ("Ung vien bi loai (tong)", "prunedTotal", 1, "{:,.0f}"),
        ("  - do rang buoc vat ly", "prunedByPhysical", 1, "{:,.0f}"),
        ("  - do cong cam ket", "prunedByCommitment", 1, "{:,.0f}"),
        ("Ung vien giu lai / xe", None, None, None),
        ("Xao tron do quyet dinh (s)", "decisionMs", 1000, "{:,.1f}"),
    ]
    head = f"{'Dai luong':<30}{'600 s':>14}{'900 s':>14}{'thay doi':>12}"
    print(head)
    print("-" * len(head))
    for label, key, div, fmt in rows:
        if key is None:
            if "cong bo / khach" in label:
                a = totals["600 s"]["publications"] / max(totals["600 s"]["riders"], 1)
                b = totals["900 s"]["publications"] / max(totals["900 s"]["riders"], 1)
            else:
                a = totals["600 s"]["retainedSum"] / max(totals["600 s"]["retainedN"], 1)
                b = totals["900 s"]["retainedSum"] / max(totals["900 s"]["retainedN"], 1)
            print(f"{label:<30}{a:>14.2f}{b:>14.2f}{100*(b/a-1) if a else 0:>11.1f}%")
            continue
        a = totals["600 s"][key] / div
        b = totals["900 s"][key] / div
        change = f"{100*(b/a-1):>11.1f}%" if a else f"{'--':>12}"
        print(f"{label:<30}{fmt.format(a):>14}{fmt.format(b):>14}{change:>12}")

    print()
    print("Doc ket qua:")
    print("  H1 dung neu 'ung vien giu lai / xe' va 'loai do cong cam ket' cung tang.")
    print("  H2 dung neu ung vien khong tang ma xao tron moi lan cong bo tang.")
    print("  H3 dung neu 'lan cong bo / khach' tang manh.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
