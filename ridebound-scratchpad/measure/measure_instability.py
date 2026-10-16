"""Does the conclusion survive a change of instability measure?

Sridharan, Berry & Udayabhanu (1987) close by pointing at their companion paper
(Decision Sciences 19(1), 1988) on *measuring* schedule instability, noting that
such measures "permit different weights to be placed on MPS changes that occur
at different points in the planning horizon, as well as the use of linear and
quadratic expressions".

RideBound's ledger implements exactly one member of that family: an unweighted
linear sum of absolute ETA movement. If the ranking of the arms depends on that
choice, the choice is a finding and must be reported. If it does not, the result
is robust. Either way the question has to be asked, and it can be asked without
running anything new: the sealed transcripts already carry every publication.

Measures computed, all over decision-induced movement unless stated:

  linear      sum |d|                       (what the ledger charges today)
  quadratic   sum d^2, reported as sqrt     (penalises few large jumps)
  step        sum w_step(r) * |d|           (r = time left before the rider is
                                             served; 3x inside 5 min, 2x inside
                                             10 min, 1x beyond)
  proximity   sum w_prox(r) * |d|           (continuous: 300s/(300s + r))
  count       number of publications that moved the promise at all
  worstRider  max over riders of cumulative |d|   (distribution, not total)
  p95Rider    95th percentile of the same

Nothing is written into the repository.

Usage: measure_instability.py <label>=<glob> [<label>=<glob> ...]
"""

from __future__ import annotations

import base64
import json
import math
import pathlib
import sys
from collections import defaultdict

DIMS = ("pickupEtaTotalMs", "dropEtaTotalMs")


def weight_step(remaining_ms: int) -> float:
    if remaining_ms <= 300_000:
        return 3.0
    if remaining_ms <= 600_000:
        return 2.0
    return 1.0


def weight_prox(remaining_ms: int) -> float:
    return 300_000.0 / (300_000.0 + max(remaining_ms, 0))


def scan_run(run_dir: pathlib.Path) -> dict:
    totals = {
        "linear": 0.0, "quadratic": 0.0, "step": 0.0, "proximity": 0.0,
        "count": 0, "publications": 0, "linearVisible": 0.0,
        "linearExogenous": 0.0,
    }
    per_request: dict[str, float] = defaultdict(float)

    with (run_dir / "transcript-00.ndjson").open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            try:
                frame = json.loads(base64.b64decode(json.loads(line)["frameBase64"]))
            except Exception:
                continue
            if frame.get("messageType") != "decision":
                continue
            now = int(frame.get("simTimeMs", 0))
            for action in frame["payload"].get("actions", []):
                if action.get("decisionType") != "promisePublished":
                    continue
                payload = action["payload"]
                promise = payload["promise"]
                decision = payload.get("decisionDelta") or {}
                visible = payload.get("visibleDelta") or {}
                exogenous = payload.get("exogenousDelta") or {}

                d = sum(int(decision.get(k, 0)) for k in DIMS)
                v = sum(int(visible.get(k, 0)) for k in DIMS)
                e = sum(int(exogenous.get(k, 0)) for k in DIMS)

                # Time left before this rider is served: the pickup if it is
                # still ahead, otherwise the drop-off. Zero once both are past.
                pickup_left = int(promise["pickupEtaMs"]) - now
                drop_left = int(promise["dropEtaMs"]) - now
                remaining = pickup_left if pickup_left > 0 else max(drop_left, 0)

                totals["publications"] += 1
                totals["linear"] += d
                totals["linearVisible"] += v
                totals["linearExogenous"] += e
                totals["quadratic"] += float(d) * float(d)
                totals["step"] += weight_step(remaining) * d
                totals["proximity"] += weight_prox(remaining) * d
                if d > 0:
                    totals["count"] += 1
                per_request[promise["requestId"]] += d

    run = json.loads((run_dir / "run-00.json").read_text(encoding="utf-8"))
    totals["accepted"] = len(run["semantic"]["acceptedRequestIds"])
    totals["perRequest"] = sorted(per_request.values())
    return totals


def percentile(values: list[float], q: float) -> float:
    if not values:
        return 0.0
    index = min(len(values) - 1, max(0, int(math.ceil(q * len(values))) - 1))
    return values[index]


def main() -> int:
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 2

    results = {}
    for spec in args:
        label, _, pattern = spec.partition("=")
        directories = sorted(pathlib.Path().glob(pattern))
        directories = [d for d in directories if (d / "run-00.json").exists()]
        if not directories:
            print(f"{label}: no runs matched {pattern}")
            continue

        merged = {
            "linear": 0.0, "quadratic": 0.0, "step": 0.0, "proximity": 0.0,
            "count": 0, "publications": 0, "accepted": 0,
            "linearVisible": 0.0, "linearExogenous": 0.0,
        }
        riders: list[float] = []
        for directory in directories:
            one = scan_run(directory)
            for key in merged:
                merged[key] += one[key]
            riders.extend(one["perRequest"])
        riders.sort()
        merged["cells"] = len(directories)
        merged["riders"] = len(riders)
        merged["worstRider"] = riders[-1] if riders else 0.0
        merged["p95Rider"] = percentile(riders, 0.95)
        merged["p99Rider"] = percentile(riders, 0.99)
        merged["ridersNonZero"] = sum(1 for r in riders if r > 0)
        results[label] = merged
        print(f"{label}: {len(directories)} cells scanned", flush=True)

    print()
    header = f"{'measure':<26}" + "".join(f"{k:>16}" for k in results)
    print(header)
    print("-" * len(header))

    def row(name: str, key: str, scale: float = 1.0, unit: str = "") -> None:
        line = f"{name:<26}"
        for label in results:
            value = results[label][key] * scale
            line += f"{value:>16,.1f}" if scale != 1.0 else f"{value:>16,.0f}"
        print(line + unit)

    row("accepted (riders)", "accepted")
    row("publications", "publications")
    print("-" * len(header))
    row("linear  sum|d|  (s)", "linear", 1e-3)
    # sqrt of the sum of squares, in seconds; printed from its own row below
    # because it needs a square root rather than a scale factor.
    line = f"{'quadratic sqrt   (s)':<26}"
    for label in results:
        line += f"{math.sqrt(results[label]['quadratic']) / 1000:>16,.1f}"
    print(line)
    row("step-weighted    (s)", "step", 1e-3)
    row("proximity-wtd    (s)", "proximity", 1e-3)
    row("count of moves", "count")
    print("-" * len(header))
    row("worst rider      (s)", "worstRider", 1e-3)
    row("p99 rider        (s)", "p99Rider", 1e-3)
    row("p95 rider        (s)", "p95Rider", 1e-3)
    row("riders moved (n)", "ridersNonZero")
    print("-" * len(header))
    row("exogenous sum    (s)", "linearExogenous", 1e-3)
    row("visible sum      (s)", "linearVisible", 1e-3)

    print()
    print("quadratic, reported as sqrt(sum d^2) in seconds:")
    for label in results:
        print(f"  {label:<20} {math.sqrt(results[label]['quadratic']) / 1000:>14,.1f}")

    if len(results) >= 2:
        labels = list(results)
        base = labels[0]
        print()
        print(f"ratio to {base} (lower = more stable):")
        keys = ["linear", "quadratic", "step", "proximity", "count",
                "worstRider", "p95Rider"]
        head = f"  {'measure':<20}" + "".join(f"{l:>14}" for l in labels[1:])
        print(head)
        for key in keys:
            line = f"  {key:<20}"
            for label in labels[1:]:
                denominator = results[base][key]
                ratio = (results[label][key] / denominator) if denominator else float("nan")
                line += f"{ratio:>14.4f}"
            print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
