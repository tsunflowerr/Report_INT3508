"""Build the price-of-commitment frontier: service rate against promise stability.

One row per arm. The left half is what the arm costs (riders served); the right
half is what it buys (how much the dispatcher moved promises it had already
published). Sealed B1 and C1 are included as the fixed reference points.

Reads only finished runs, so it can be called while the sweep is still going;
incomplete arms are marked rather than silently averaged over fewer cells.

Nothing is written into the repository.
"""

from __future__ import annotations

import json
import math
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "measure"))
from measure_instability import percentile, scan_run  # noqa: E402

SEALED = pathlib.Path(r"E:/RideBoundData/wp9/confirmatory-h6-panela-v2")
FRONTIER = pathlib.Path(r"E:/RideBoundData/wp9/frontier-v1")
CELLS = [
    f"d201811{day}-s10-r{rep}"
    for day in (14, 15, 16, 17, 18)
    for rep in (1, 2, 3, 4)
]
REQUESTS = 108 * len(CELLS)

# label -> (directory template, human description of the promise it makes)
# Ladder 1 varies the drop-ETA budget with every lock held fixed.
# Ladder 2 varies how the pickup ETA is protected, with the drop-ETA budget
# held at 30 s. They cross at the sealed C1 point, which belongs to both.
ARMS: list[tuple[str, str, str]] = [
    ("B1  (no promise)", "SEALED:b1", "nothing is promised; the plan may move freely"),
    # -- ladder 1: how much may the drop ETA drift, in total, per rider? --
    ("nobudget", "FRONTIER:nobudget", "same vehicle and stops; drop ETA unbounded"),
    ("budget300", "FRONTIER:budget300", "... and drop ETA within 300 s in total"),
    ("budget120", "FRONTIER:budget120", "... and drop ETA within 120 s in total"),
    ("budget60", "FRONTIER:budget60", "... and drop ETA within 60 s in total"),
    ("C1  (sealed 30 s)", "SEALED:c1",
     "... and drop ETA within 30 s; pickup ETA fixed at confirmation"),
    # -- ladder 2: how is the pickup ETA protected? drop budget fixed at 30 s --
    ("nopickuplock", "FRONTIER:nopickuplock", "pickup ETA not protected at all"),
    ("freeze600", "FRONTIER:freeze600", "pickup ETA fixed once within 600 s of pickup"),
    ("freeze300", "FRONTIER:freeze300", "pickup ETA fixed once within 300 s of pickup"),
    ("ratchet", "FRONTIER:ratchet", "pickup ETA fixed at confirmation, may improve"),
    ("freeze300ratchet", "FRONTIER:freeze300ratchet",
     "pickup ETA fixed within 300 s, may improve"),
]


def run_dirs(spec: str) -> list[pathlib.Path]:
    kind, _, name = spec.partition(":")
    if kind == "SEALED":
        paths = [SEALED / f"p-{c}-{name}-tight-s7" for c in CELLS]
    else:
        paths = [FRONTIER / f"fr-{name}-{c}-s7" for c in CELLS]
    return [p for p in paths if (p / "summary.json").exists()]


def main() -> int:
    baseline = None
    rows = []

    for label, spec, promise in ARMS:
        directories = run_dirs(spec)
        if not directories:
            rows.append((label, promise, None))
            continue

        merged = {
            "linear": 0.0, "quadratic": 0.0, "count": 0, "accepted": 0,
            "linearExogenous": 0.0, "publications": 0, "step": 0.0,
            "proximity": 0.0, "linearVisible": 0.0,
        }
        riders: list[float] = []
        for directory in directories:
            one = scan_run(directory)
            for key in merged:
                merged[key] += one[key]
            riders.extend(one["perRequest"])
        riders.sort()
        merged["cells"] = len(directories)
        merged["worstRider"] = riders[-1] if riders else 0.0
        merged["p95Rider"] = percentile(riders, 0.95)
        merged["ridersMoved"] = sum(1 for r in riders if r > 0)
        rows.append((label, promise, merged))
        if label.startswith("B1"):
            baseline = merged
        print(f"scanned {label:<20} {len(directories):>2}/20 cells", flush=True)

    print()
    head = (f"{'arm':<20}{'cells':>6}{'served':>8}{'rate %':>9}{'vs B1 pp':>10}"
            f"{'decision s':>12}{'worst s':>9}{'moved':>7}{'exog s':>9}")
    print(head)
    print("-" * len(head))
    for label, _promise, merged in rows:
        if merged is None:
            print(f"{label:<20}{'-':>6}{'(not run yet)':>8}")
            continue
        served = merged["accepted"]
        cells = merged["cells"]
        # Rates are only comparable on a complete panel.
        if cells == len(CELLS) and baseline is not None:
            rate = 100.0 * served / REQUESTS
            delta = 100.0 * (served - baseline["accepted"]) / REQUESTS
            rate_text, delta_text = f"{rate:>9.4f}", f"{delta:>+10.4f}"
        else:
            rate_text, delta_text = f"{'partial':>9}", f"{'':>10}"
        print(f"{label:<20}{cells:>6}{served:>8}{rate_text}{delta_text}"
              f"{merged['linear'] / 1000:>12,.0f}"
              f"{merged['worstRider'] / 1000:>9,.0f}"
              f"{merged['ridersMoved']:>7}"
              f"{merged['linearExogenous'] / 1000:>9,.0f}")
    print("-" * len(head))
    print("decision s = operator-caused movement of already-published ETAs, summed")
    print("worst s    = the single worst-served rider's cumulative operator-caused move")
    print("moved      = riders who suffered any operator-caused move")
    print("exog s     = physical drift, the control: should be near-constant across arms")

    print()
    print("THE TRADE: service given up against promise stability bought")
    if baseline is not None:
        b_served, b_lin = baseline["accepted"], baseline["linear"]
        print(f"  {'arm':<20}{'riders lost':>13}{'seconds saved':>15}{'s saved / rider lost':>22}")
        for label, _promise, merged in rows:
            if merged is None or merged["cells"] != len(CELLS) or label.startswith("B1"):
                continue
            lost = b_served - merged["accepted"]
            saved = (b_lin - merged["linear"]) / 1000
            ratio = f"{saved / lost:,.0f}" if lost > 0 else "no riders lost"
            print(f"  {label:<20}{lost:>13}{saved:>15,.0f}{ratio:>22}")

    print()
    print("promise each arm makes:")
    for label, promise, _ in rows:
        print(f"  {label:<20} {promise}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
