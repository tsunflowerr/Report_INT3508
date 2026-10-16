"""What do riders actually experience under each arm?

Serving more riders by widening the pickup window is only a gain if the riders
who were already being served do not pay for it in waiting time. The window is
an upper bound, not a realisation: it is entirely possible for a wider bound to
unlock better matches without most riders waiting any longer, and it is equally
possible for the optimiser to spend the whole extra 300 s on detours.

Alonso-Gonzalez et al. (2020) measured the value of reliability at BELOW the
value of time for exactly this setting, so trading waiting time for reliability
is not automatically a good deal. Which way it goes here is an empirical
question, and this answers it.

Realised times come from the last published projection, as in
fielbaum_measure.py: the panel has one travel-time snapshot, so a projection of
the route actually executed differs from the realisation only by execution lag
(measured at p50 = 4.9 s).

    waiting(r)   = lastPickupEta - arrivalTime
    inVehicle(r) = lastDropEta   - lastPickupEta

Read-only. Nothing is written into the repository.

Usage:  service_quality.py
"""

from __future__ import annotations

import base64
import json
import pathlib

SEALED = pathlib.Path(r"E:/RideBoundData/wp9/confirmatory-h6-panela-v2")
WIDE = pathlib.Path(r"E:/RideBoundData/wp14/wide-window-v1")
CELLS = [
    f"d201811{day}-s10-r{rep}"
    for day in (14, 15, 16, 17, 18)
    for rep in (1, 2, 3, 4)
]

ARMS = [
    ("B1@600", lambda c: SEALED / f"p-{c}-b1-tight-s7"),
    ("C1@600", lambda c: SEALED / f"p-{c}-c1-tight-s7"),
    ("B1@900", lambda c: WIDE / f"ww-b1-{c}-s7"),
    ("C1@900", lambda c: WIDE / f"ww-c1-{c}-s7"),
]


def percentile(values: list[float], q: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    index = min(len(ordered) - 1, max(0, int(round(q * (len(ordered) - 1)))))
    return ordered[index]


def scan_cell(directory: pathlib.Path) -> tuple[list[float], list[float]]:
    arrivals: dict[str, int] = {}
    last_pickup: dict[str, int] = {}
    last_drop: dict[str, int] = {}
    version: dict[str, int] = {}
    boarded: set[str] = set()

    with (directory / "transcript-00.ndjson").open(encoding="utf-8") as handle:
        for line in handle:
            frame = json.loads(base64.b64decode(json.loads(line)["frameBase64"]))
            kind = frame.get("messageType")
            if kind == "eventBatch":
                for event in frame["payload"]["events"]:
                    if event["eventType"] == "requestArrived":
                        request = event["payload"]["request"]
                        arrivals[request["requestId"]] = request["arrivalTimeMs"]
                    elif event["eventType"] == "passengerBoarded":
                        boarded.add(event["payload"]["requestId"])
            elif kind == "decision":
                for action in frame["payload"].get("actions", []):
                    if action.get("decisionType") != "promisePublished":
                        continue
                    payload = action["payload"]
                    promise = payload["promise"]
                    request_id = promise["requestId"]
                    seen = payload["promiseVersion"]
                    if version.get(request_id, -1) <= seen:
                        version[request_id] = seen
                        last_pickup[request_id] = promise["pickupEtaMs"]
                        last_drop[request_id] = promise["dropEtaMs"]

    waits: list[float] = []
    rides: list[float] = []
    # Only riders who were actually picked up have a realised experience.
    for request_id in boarded:
        if request_id not in last_pickup or request_id not in arrivals:
            continue
        waits.append((last_pickup[request_id] - arrivals[request_id]) / 1000)
        rides.append((last_drop[request_id] - last_pickup[request_id]) / 1000)
    return waits, rides


def main() -> int:
    print("Realised service quality per arm. 'Realised' = last published")
    print("projection; the panel has a single travel-time snapshot.")
    print()
    head = (f"{'arm':<10}{'cells':>6}{'riders':>8}{'wait p50':>10}"
            f"{'wait mean':>11}{'wait p90':>10}{'wait max':>10}"
            f"{'ride p50':>10}{'ride mean':>11}")
    print(head)
    print("-" * len(head))

    table = {}
    for label, resolve in ARMS:
        waits: list[float] = []
        rides: list[float] = []
        cells = 0
        for cell in CELLS:
            directory = resolve(cell)
            if not (directory / "summary.json").exists():
                continue
            cell_waits, cell_rides = scan_cell(directory)
            waits.extend(cell_waits)
            rides.extend(cell_rides)
            cells += 1
        if not waits:
            print(f"{label:<10}{'-':>6}  (not run yet)")
            continue
        table[label] = (cells, waits, rides)
        print(f"{label:<10}{cells:>6}{len(waits):>8}"
              f"{percentile(waits, 0.50):>10.1f}{sum(waits) / len(waits):>11.1f}"
              f"{percentile(waits, 0.90):>10.1f}{max(waits):>10.1f}"
              f"{percentile(rides, 0.50):>10.1f}"
              f"{sum(rides) / len(rides):>11.1f}")
    print("-" * len(head))
    print("all figures in seconds")

    # The comparison that decides how the headline is written: does the wider
    # window make already-served riders wait longer, or does it only add riders?
    if "C1@600" in table and "C1@900" in table:
        _, w600, r600 = table["C1@600"]
        _, w900, r900 = table["C1@900"]
        print()
        print("C1: what the extra 300 s of window actually cost riders")
        print(f"  riders served        {len(w600):>8} -> {len(w900):>8} "
              f"({len(w900) - len(w600):+d})")
        print(f"  median wait          {percentile(w600, 0.50):>8.1f} -> "
              f"{percentile(w900, 0.50):>8.1f} s "
              f"({percentile(w900, 0.50) - percentile(w600, 0.50):+.1f})")
        print(f"  mean wait            {sum(w600) / len(w600):>8.1f} -> "
              f"{sum(w900) / len(w900):>8.1f} s "
              f"({sum(w900) / len(w900) - sum(w600) / len(w600):+.1f})")
        print(f"  p90 wait             {percentile(w600, 0.90):>8.1f} -> "
              f"{percentile(w900, 0.90):>8.1f} s "
              f"({percentile(w900, 0.90) - percentile(w600, 0.90):+.1f})")
        print(f"  mean in-vehicle      {sum(r600) / len(r600):>8.1f} -> "
              f"{sum(r900) / len(r900):>8.1f} s "
              f"({sum(r900) / len(r900) - sum(r600) / len(r600):+.1f})")
        over600 = sum(1 for value in w900 if value > 600)
        print(f"  riders waiting >600 s under C1@900: {over600} "
              f"({100.0 * over600 / len(w900):.1f}%) "
              f"-- these could not have been served at all at 600 s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
