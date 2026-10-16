"""Implement the unreliability measures of Fielbaum & Alonso-Mora (2020) on the
RideBound panel, so their measure and ours can be read off the same runs.

Their definitions (TR-C 121:102831, Section 3):

    t1_w(r)   first-announced waiting time
    t_w(r)    real waiting time
    D_t_w(r)  = t_w  - t1_w            (Definition 5)
    D_t_d(r)  = t_d  - t1_d            (Definition 6, detour)
    D_D(r)    = D_t_w + D_t_d          (Definition 7, delay)
    NC_*(r)   how many times the prediction INCREASES over the chain of
              assignments, from the first until pick-up / drop-off (Definition 9)

    "In the remainder of the paper we consider the positive values for these
     indices, and truncate to zero those that are negative."

Two conveniences make this exact rather than approximate:

  * Waiting time is measured from the request time, which is the same constant
    in both terms, so it cancels:  D_t_w = pickupLast - pickupFirst.
    Detour is in-vehicle minus the direct time, and the direct time is also
    constant, so it cancels too. No request-time join is needed, which matters
    because run-00 and the transcript use different id spaces.

  * The panel has one travel-time snapshot for the whole run, so the last
    published projection is the realisation up to execution lag (measured
    elsewhere at p50 = 4.9 s). "Real" below therefore means "last published",
    and that approximation is stated in the output.

What this buys: their measure compares two endpoints, ours accumulates the whole
chain. The same runs scored both ways say exactly how much movement an endpoint
measure cannot see.

Read-only. Nothing is written into the repository.

Usage:  fielbaum_measure.py [arm ...]        (default: b1 c1)
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


def scan_cell(directory: pathlib.Path) -> dict:
    chains: dict[str, list[tuple[int, int, int]]] = collections.defaultdict(list)
    accepted: set[str] = set()
    rejected: set[str] = set()
    became_rejected: set[str] = set()

    with (directory / "transcript-00.ndjson").open(encoding="utf-8") as handle:
        for line in handle:
            frame = json.loads(
                base64.b64decode(json.loads(line)["frameBase64"])
            )
            if frame.get("messageType") != "decision":
                continue
            for action in frame["payload"].get("actions", []):
                kind = action.get("decisionType")
                payload = action["payload"]
                if kind == "requestAccepted":
                    accepted.add(payload["requestId"])
                elif kind == "requestRejected":
                    request_id = payload["requestId"]
                    rejected.add(request_id)
                    # Definition 8: accepted first, rejected later.
                    if request_id in accepted:
                        became_rejected.add(request_id)
                elif kind == "promisePublished":
                    promise = payload["promise"]
                    chains[promise["requestId"]].append(
                        (
                            payload["promiseVersion"],
                            promise["pickupEtaMs"],
                            promise["dropEtaMs"],
                        )
                    )

    rows = []
    for request_id, entries in chains.items():
        entries.sort()
        pickups = [value[1] for value in entries]
        drops = [value[2] for value in entries]
        detours = [drop - pickup for pickup, drop in zip(pickups, drops)]

        # -- Fielbaum & Alonso-Mora: two endpoints, negatives truncated --
        delta_wait = max(0, pickups[-1] - pickups[0])
        delta_detour = max(0, detours[-1] - detours[0])
        delta_delay_sum = delta_wait + delta_detour
        delta_delay_endpoint = max(0, drops[-1] - drops[0])

        # -- Definition 9: how many times the prediction increases --
        increases_wait = sum(
            1 for i in range(1, len(pickups)) if pickups[i] > pickups[i - 1]
        )
        increases_detour = sum(
            1 for i in range(1, len(detours)) if detours[i] > detours[i - 1]
        )
        increases_delay = sum(
            1 for i in range(1, len(drops)) if drops[i] > drops[i - 1]
        )

        # -- RideBound: the whole chain, both directions --
        path_pickup = sum(
            abs(pickups[i] - pickups[i - 1]) for i in range(1, len(pickups))
        )
        path_drop = sum(
            abs(drops[i] - drops[i - 1]) for i in range(1, len(drops))
        )

        rows.append(
            {
                "publications": len(entries),
                "deltaWait": delta_wait,
                "deltaDetour": delta_detour,
                "deltaDelaySum": delta_delay_sum,
                "deltaDelayEndpoint": delta_delay_endpoint,
                "ncWait": increases_wait,
                "ncDetour": increases_detour,
                "ncDelay": increases_delay,
                "pathPickup": path_pickup,
                "pathDrop": path_drop,
            }
        )

    return {
        "rows": rows,
        "accepted": len(accepted),
        "rejected": len(rejected),
        "becameRejected": len(became_rejected),
    }


def summarise(arm: str) -> None:
    rows: list[dict] = []
    accepted = rejected = became_rejected = cells = 0
    for cell in CELLS:
        directory = SEALED / f"p-{cell}-{arm}-tight-s7"
        if not (directory / "summary.json").exists():
            continue
        result = scan_cell(directory)
        rows.extend(result["rows"])
        accepted += result["accepted"]
        rejected += result["rejected"]
        became_rejected += result["becameRejected"]
        cells += 1

    if not rows:
        print(f"arm {arm}: no runs found")
        return

    n = len(rows)
    print(f"=============== ARM {arm.upper()} "
          f"({cells} cells, {n} riders with a published promise) ===============")
    print()

    print("A. Fielbaum & Alonso-Mora (2020) measures")
    print(f"   {'index':<26}{'P(D>0)':>10}{'E(D|D>0)':>12}{'mean':>10}"
          f"{'p90 of D>0':>13}{'max':>10}")
    for label, key in (
        ("D t_w  (waiting)", "deltaWait"),
        ("D t_d  (detour)", "deltaDetour"),
        ("D D    (delay, sum form)", "deltaDelaySum"),
        ("D D    (delay, endpoint)", "deltaDelayEndpoint"),
    ):
        values = [row[key] / 1000 for row in rows]
        positive = [value for value in values if value > 0]
        probability = len(positive) / n
        conditional = (sum(positive) / len(positive)) if positive else 0.0
        print(f"   {label:<26}{probability:>10.4f}{conditional:>12.1f}"
              f"{sum(values) / n:>10.1f}{percentile(positive, 0.90):>13.1f}"
              f"{max(values):>10.1f}")
    print("   (seconds; U(x) in their Eq. 3 is P(D>0) x E(D|D>0), the two "
          "columns above)")
    print()

    print("B. Definition 9 -- number of times the prediction increases")
    for label, key in (
        ("NC t_w", "ncWait"),
        ("NC t_d", "ncDetour"),
        ("NC D", "ncDelay"),
    ):
        values = [row[key] for row in rows]
        print(f"   {label:<10}mean {sum(values) / n:>6.3f}   "
              f"share with >=1 {sum(1 for v in values if v) / n:>7.4f}   "
              f"max {max(values):>3}")
    print()

    print("C. Definition 8 -- became rejected after being accepted")
    print(f"   accepted {accepted}, rejected {rejected}, "
          f"became-rejected {became_rejected}")
    print()

    print("D. Their endpoint measure vs the RideBound chain measure")
    their_wait = sum(row["deltaWait"] for row in rows) / 1000
    their_delay = sum(row["deltaDelayEndpoint"] for row in rows) / 1000
    our_pickup = sum(row["pathPickup"] for row in rows) / 1000
    our_drop = sum(row["pathDrop"] for row in rows) / 1000
    print(f"   {'quantity':<44}{'seconds':>12}")
    print(f"   {'pickup: their |last - first|, truncated':<44}{their_wait:>12,.0f}")
    print(f"   {'pickup: our sum |step| over the chain':<44}{our_pickup:>12,.0f}")
    if their_wait > 0:
        print(f"   {'-> chain / endpoint':<44}{our_pickup / their_wait:>11,.1f}x")
    else:
        print(f"   {'-> endpoint sees nothing at all':<44}{'':>12}")
    print(f"   {'drop:   their |last - first|, truncated':<44}{their_delay:>12,.0f}")
    print(f"   {'drop:   our sum |step| over the chain':<44}{our_drop:>12,.0f}")
    if their_delay > 0:
        print(f"   {'-> chain / endpoint':<44}{our_drop / their_delay:>11,.1f}x")
    missed = sum(
        1
        for row in rows
        if row["deltaDelayEndpoint"] == 0
        and row["deltaWait"] == 0
        and (row["pathPickup"] > 0 or row["pathDrop"] > 0)
    )
    print(f"   riders their measure scores as 0 but who were "
          f"moved: {missed} ({100.0 * missed / n:.2f}%)")
    print()


def main() -> int:
    arms = sys.argv[1:] or ["b1", "c1"]
    print("Measures of Fielbaum & Alonso-Mora (2020) applied to the sealed "
          "RideBound panel.")
    print("'Real' = last published projection; the panel has a single travel-time")
    print("snapshot, so this differs from the realisation only by execution lag.")
    print()
    for arm in arms:
        summarise(arm)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
