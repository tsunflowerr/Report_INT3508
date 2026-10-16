"""How thin is the choice set, over the whole sealed panel?

Levels A and B of the promise-aware generator plan were killed on a three-cell
measurement. Before that goes into the report it should be measured on all
twenty sealed cells of both arms, since a claim of the form "96 % of decisions
have exactly one candidate" carries the whole argument.

Source: payload/solver/executionEvidence/generation/vehicleLosses[], one entry
per vehicle per decision epoch. Fields used:

    uniqueFeasibleCandidateCountBeforeCap   how many survived physics/schedule
    retainedCandidateCount                  how many the retainer kept
    candidateCapApplied                     did the cap bind on this vehicle
    omittedFeasibleCandidateCountByCap      feasible candidates thrown away
    omittedUnexpandedCandidatePathCount     branches never expanded
    workBudgetExhausted                     did the generator run out of budget
    physicallyOrSchedulePrunedCount         rejected before the commitment gate

Read-only.
"""

from __future__ import annotations

import base64
import collections
import json
import pathlib
import sys

SEALED = pathlib.Path(r"E:/RideBoundData/wp9/confirmatory-h6-panela-v2")
CELLS = [
    "d201811{}-s10-r{}".format(day, rep)
    for day in (14, 15, 16, 17, 18)
    for rep in (1, 2, 3, 4)
]
ARMS = {"B1 (khong hua)": "p-{}-b1-tight-s7",
        "C1 (tran 30 s)": "p-{}-c1-tight-s7"}


def frames(path: pathlib.Path):
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                yield json.loads(base64.b64decode(json.loads(line)["frameBase64"]))


def losses_of(frame):
    payload = frame.get("payload", {})
    node = (payload.get("solver", {})
            .get("executionEvidence", {})
            .get("generation", {}))
    return node.get("vehicleLosses") or []


def scan(directory: pathlib.Path) -> tuple[collections.Counter, collections.Counter]:
    stat: collections.Counter = collections.Counter()
    histogram: collections.Counter = collections.Counter()
    transcript = directory / "transcript-00.ndjson"
    if not transcript.exists():
        return stat, histogram
    for frame in frames(transcript):
        if frame.get("messageType") != "decision":
            continue
        for entry in losses_of(frame):
            stat["decisions"] += 1
            unique = entry.get("uniqueFeasibleCandidateCountBeforeCap", 0)
            retained = entry.get("retainedCandidateCount", 0)
            stat["unique"] += unique
            stat["retained"] += retained
            stat["physSched"] += entry.get("physicallyOrSchedulePrunedCount", 0)
            stat["omittedByCap"] += entry.get(
                "omittedFeasibleCandidateCountByCap", 0)
            stat["omittedUnexpanded"] += entry.get(
                "omittedUnexpandedCandidatePathCount", 0)
            if entry.get("candidateCapApplied"):
                stat["capApplied"] += 1
            if entry.get("workBudgetExhausted"):
                stat["workExhausted"] += 1
            histogram[min(retained, 10)] += 1
    return stat, histogram


def main() -> int:
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else len(CELLS)
    for name, pattern in ARMS.items():
        total: collections.Counter = collections.Counter()
        histogram: collections.Counter = collections.Counter()
        cells = 0
        for cell in CELLS[:limit]:
            directory = SEALED / pattern.format(cell)
            stat, hist = scan(directory)
            if not stat:
                continue
            cells += 1
            total.update(stat)
            histogram.update(hist)
            print("  quet {} {}".format(name.split()[0], cell), flush=True)

        decisions = max(total["decisions"], 1)
        print()
        print("=== {} -- {} o, {:,} quyet dinh cap xe ===".format(
            name, cells, total["decisions"]))
        print("  ung vien kha thi truoc tran / xe   {:.3f}".format(
            total["unique"] / decisions))
        print("  ung vien duoc giu lai / xe         {:.3f}".format(
            total["retained"] / decisions))
        print("  bi loai vi vat ly/lich trinh / xe  {:.3f}".format(
            total["physSched"] / decisions))
        print("  cham tran so ung vien              {:,}".format(total["capApplied"]))
        print("  can ngan sach tinh toan            {:,}".format(total["workExhausted"]))
        print("  ung vien kha thi bi bo do tran     {:,}".format(total["omittedByCap"]))
        print("  nhanh chua khai trien bi bo        {:,}".format(
            total["omittedUnexpanded"]))
        print("  phan bo so ung vien giu lai:")
        for k in sorted(histogram):
            share = 100.0 * histogram[k] / decisions
            label = "{:>2}".format(k) if k < 10 else ">=10"
            print("     {} ung vien: {:>9,}  ({:5.2f} %)".format(
                label, histogram[k], share))
        multi = sum(v for k, v in histogram.items() if k >= 2)
        print("  co tu 2 ung vien tro len: {:,} ({:.2f} %)".format(
            multi, 100.0 * multi / decisions))
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
