"""How much is the pickup window actually binding, and on whom?

The prune counters say PICKUP_WINDOW is the most common reason a candidate is
discarded. That is not the same as saying it is the reason a *request* is
rejected: a request is rejected only when every candidate for it fails, and a
candidate that fails the window might also have failed the ride-time bound had
the validator kept going (it returns on the first violation).

So this script separates two questions:

  1. Over all pruned candidates, how far past the window does the arrival land?
     This says whether widening is cheap or hopeless in general.

  2. For each request that was actually REJECTED, what is the smallest window
     excess among its own pruned candidates? That is the widening needed to give
     the request one admissible plan -- an OPTIMISTIC lower bound, because the
     same candidate may fail another constraint once the window stops binding.

Read-only. Nothing is written into the repository.
"""

from __future__ import annotations

import base64
import collections
import json
import pathlib
import sys

SEALED = pathlib.Path(r"E:/RideBoundData/wp9/confirmatory-h6-panela-v2")
CELLS = [
    f"d201811{day}-s10-r{rep}"
    for day in (14, 15, 16, 17, 18)
    for rep in (1, 2, 3, 4)
]


def percentile(values: list[float], q: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    index = min(len(ordered) - 1, max(0, int(round(q * (len(ordered) - 1)))))
    return ordered[index]


def frames(path: pathlib.Path):
    for line in path.open(encoding="utf-8"):
        outer = json.loads(line)
        blob = outer.get("frameBase64")
        if not blob:
            continue
        try:
            text = base64.b64decode(blob).decode("utf-8")
        except Exception:
            continue
        try:
            yield json.loads(text)
        except json.JSONDecodeError:
            continue


def walk(node, out: list) -> None:
    """Collect every prunedCandidates list, wherever it sits in the frame."""
    if isinstance(node, dict):
        if "prunedCandidates" in node:
            out.append(node["prunedCandidates"])
        for value in node.values():
            walk(value, out)
    elif isinstance(node, list):
        for value in node:
            walk(value, out)


def scan_cell(directory: pathlib.Path) -> dict:
    transcript = directory / "transcript-00.ndjson"
    run = json.loads((directory / "run-00.json").read_text(encoding="utf-8"))

    all_excess: list[int] = []
    code_counts: collections.Counter = collections.Counter()
    per_request: dict = collections.defaultdict(dict)
    per_request_codes: dict = collections.defaultdict(collections.Counter)
    # run-00 carries semantic ids, the transcript carries runner ids, so the
    # rejected set must come from the transcript's own actions to be joinable
    # against prunedCandidates.newRequestIds.
    rejected_ids: set = set()
    accepted_ids: set = set()

    for frame in frames(transcript):
        if frame.get("messageType") == "decision":
            for action in frame.get("payload", {}).get("actions", []):
                kind = action.get("decisionType")
                if kind == "requestRejected":
                    rejected_ids.add(action["payload"]["requestId"])
                elif kind == "requestAccepted":
                    accepted_ids.add(action["payload"]["requestId"])
        found: list = []
        walk(frame, found)
        for payload in found:
            for pruned in payload:
                code = pruned.get("code") or ""
                code_counts[code] += 1
                witness = pruned.get("physicalWitness") or {}
                expected = witness.get("expected")
                actual = witness.get("actual")
                new_ids = pruned.get("newRequestIds") or []
                for request_id in new_ids:
                    per_request_codes[request_id][code] += 1
                if code != "PICKUP_WINDOW" or expected is None or actual is None:
                    continue
                excess = int(actual) - int(expected)
                if excess <= 0:
                    continue
                all_excess.append(excess)
                for request_id in new_ids:
                    best = per_request[request_id].get(code)
                    if best is None or excess < best:
                        per_request[request_id][code] = excess

    # Cardinality cross-check against the sealed run file: if these disagree the
    # transcript scan missed actions and every downstream number is suspect.
    expected_rejected = len(run["semantic"]["rejectedRequestIds"])
    expected_accepted = len(run["semantic"]["acceptedRequestIds"])
    if (len(rejected_ids), len(accepted_ids)) != (
        expected_rejected,
        expected_accepted,
    ):
        raise SystemExit(
            f"{directory.name}: transcript gives "
            f"{len(accepted_ids)}/{len(rejected_ids)} accepted/rejected, "
            f"run-00 gives {expected_accepted}/{expected_rejected}"
        )

    return {
        "cell": directory.name,
        "rejectedIds": rejected_ids,
        "allExcess": all_excess,
        "codeCounts": code_counts,
        "perRequest": per_request,
        "perRequestCodes": per_request_codes,
        "accepted": expected_accepted,
    }


def main() -> int:
    arm = sys.argv[1] if len(sys.argv) > 1 else "b1"
    merged_excess: list[int] = []
    merged_codes: collections.Counter = collections.Counter()
    rejected_total = 0
    rejected_with_window = 0
    rejected_min_excess: list[int] = []
    rejected_no_candidate = 0
    rejected_code_profile: collections.Counter = collections.Counter()
    cells_done = 0

    for cell in CELLS:
        directory = SEALED / f"p-{cell}-{arm}-tight-s7"
        if not (directory / "summary.json").exists():
            continue
        result = scan_cell(directory)
        cells_done += 1
        merged_excess.extend(result["allExcess"])
        merged_codes.update(result["codeCounts"])

        for request_id in result["rejectedIds"]:
            rejected_total += 1
            codes = result["perRequestCodes"].get(request_id)
            if not codes:
                rejected_no_candidate += 1
                continue
            rejected_code_profile.update(codes)
            excess = result["perRequest"].get(request_id, {}).get("PICKUP_WINDOW")
            if excess is not None:
                rejected_with_window += 1
                rejected_min_excess.append(excess)

        print(f"scanned {cell} ({cells_done}/20)", flush=True)

    print()
    print(f"ARM {arm} -- {cells_done} cells")
    print()
    print("Q1. Every pruned candidate, by reason")
    total = sum(merged_codes.values())
    for code, count in merged_codes.most_common():
        share = 100.0 * count / total if total else 0.0
        print(f"  {code or 'NONE':<22}{count:>9,}{share:>9.2f}%")
    print(f"  {'TOTAL':<22}{total:>9,}")

    print()
    print("Q1b. How far past the window did those arrivals land?")
    if merged_excess:
        seconds = [value / 1000 for value in merged_excess]
        for q in (0.05, 0.10, 0.25, 0.50, 0.75, 0.90):
            print(f"  p{int(q * 100):<3} {percentile(seconds, q):>10,.1f} s")
        print(f"  max  {max(seconds):>10,.1f} s")
        print(f"  n    {len(seconds):>10,}")
        for widen in (30, 60, 120, 300, 600):
            got = sum(1 for value in seconds if value <= widen)
            print(f"  widening by {widen:>3} s admits {got:>7,} / "
                  f"{len(seconds):,} pruned candidates "
                  f"({100.0 * got / len(seconds):.2f}%)")

    print()
    print("Q2. REJECTED requests -- what actually blocked them")
    print(f"  rejected requests seen             {rejected_total:>7,}")
    print(f"  ... never had any pruned candidate {rejected_no_candidate:>7,}")
    print(f"  ... had a PICKUP_WINDOW candidate  {rejected_with_window:>7,}")
    if rejected_code_profile:
        print("  codes on rejected requests' own candidates:")
        for code, count in rejected_code_profile.most_common():
            print(f"    {code or 'NONE':<22}{count:>9,}")
    if rejected_min_excess:
        seconds = [value / 1000 for value in rejected_min_excess]
        print()
        print("  smallest window excess per rejected request")
        print("  (OPTIMISTIC lower bound on the widening needed):")
        for q in (0.05, 0.10, 0.25, 0.50, 0.75, 0.90):
            print(f"    p{int(q * 100):<3} {percentile(seconds, q):>10,.1f} s")
        print(f"    max  {max(seconds):>10,.1f} s")
        for widen in (30, 60, 120, 300, 600):
            got = sum(1 for value in seconds if value <= widen)
            print(f"    widening by {widen:>3} s could rescue at most {got:>5,}"
                  f" / {rejected_total:,} rejected "
                  f"({100.0 * got / rejected_total:.2f}%)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
