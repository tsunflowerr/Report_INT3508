"""Aggregate candidate-generation evidence from a wire transcript.

Answers one question: when repair is switched on, does it actually enlarge the
candidate pool, and does anything downstream consume the extra candidates?
"""

from __future__ import annotations

import base64
import json
import pathlib
import sys
from collections import Counter

FIELDS = [
    "eligibleRepairRequestCount",
    "consideredRepairRequestCount",
    "omittedRepairRequestCount",
    "evaluatedCandidatePathCount",
    "uniqueFeasibleCandidateCountBeforeCap",
    "retainedCandidateCount",
    "physicallyOrSchedulePrunedCount",
    "omittedFeasibleCandidateCountByCap",
    "omittedUnexpandedCandidatePathCount",
    "explorationWorkUnits",
]
FLAGS = ["candidateCapApplied", "workBudgetExhausted", "omissionCountWasSaturated"]


def analyze(path):
    totals = Counter()
    flags = Counter()
    decisions = 0
    vehicle_frames = 0
    prune_codes = Counter()
    prune_dims = Counter()
    selected_candidates = 0
    consumed_gen = 0
    consumed_val = 0

    with open(path, "r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            envelope = json.loads(line)
            if envelope["direction"] != "runnerToAdapter":
                continue
            frame = json.loads(
                base64.b64decode(envelope["frameBase64"]).decode("utf-8")
            )
            if frame.get("messageType") != "decision":
                continue
            payload = frame["payload"]
            decisions += 1
            selected_candidates += len(payload.get("actions") or [])

            evidence = (payload.get("solver") or {}).get("executionEvidence") or {}
            selection = evidence.get("selection") or {}
            consumed_gen = max(
                consumed_gen, selection.get("consumedGenerationWorkUnits") or 0
            )
            consumed_val = max(
                consumed_val, selection.get("consumedValidationWorkUnits") or 0
            )

            generation = evidence.get("generation") or {}
            for loss in generation.get("vehicleLosses") or []:
                vehicle_frames += 1
                for field in FIELDS:
                    value = loss.get(field)
                    if isinstance(value, int):
                        totals[field] += value
                for flag in FLAGS:
                    if loss.get(flag):
                        flags[flag] += 1

            for pruned in evidence.get("prunedCandidates") or []:
                code = pruned.get("code") or pruned.get("reasonCode") or "?"
                prune_codes[code] += 1
                dim = pruned.get("dimension")
                if dim:
                    prune_dims[dim] += 1

    return {
        "decisions": decisions,
        "vehicleFrames": vehicle_frames,
        "selectedActions": selected_candidates,
        "consumedGenerationWorkUnits": consumed_gen,
        "consumedValidationWorkUnits": consumed_val,
        "totals": dict(totals),
        "flags": dict(flags),
        "pruneCodes": dict(prune_codes),
        "pruneDimensions": dict(prune_dims),
    }


def main():
    labelled = []
    for spec in sys.argv[1:]:
        name, _, path = spec.partition("=")
        labelled.append((name, pathlib.Path(path)))

    results = {}
    for name, path in labelled:
        print(f"scanning {name} ...", file=sys.stderr, flush=True)
        results[name] = analyze(path)

    names = [n for n, _ in labelled]
    width = max(38, max(len(n) for n in names) + 2)

    def row(label, getter):
        cells = "".join(f"{str(getter(results[n])):>16}" for n in names)
        print(f"{label:<{width}}{cells}")

    print(f"{'metric':<{width}}" + "".join(f"{n:>16}" for n in names))
    print("-" * (width + 16 * len(names)))
    for key in ("decisions", "vehicleFrames", "selectedActions",
                "consumedGenerationWorkUnits", "consumedValidationWorkUnits"):
        row(key, lambda r, k=key: r[k])
    print()
    for field in FIELDS:
        row(field, lambda r, f=field: r["totals"].get(f, 0))
    print()
    for flag in FLAGS:
        row(flag + " (frames)", lambda r, f=flag: r["flags"].get(f, 0))
    print()
    codes = sorted({c for r in results.values() for c in r["pruneCodes"]})
    for code in codes:
        row("prune:" + code, lambda r, c=code: r["pruneCodes"].get(c, 0))
    dims = sorted({d for r in results.values() for d in r["pruneDimensions"]})
    for dim in dims:
        row("pruneDim:" + dim, lambda r, d=dim: r["pruneDimensions"].get(d, 0))


if __name__ == "__main__":
    raise SystemExit(main())
