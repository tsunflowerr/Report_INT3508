"""Aggregate the extracted promise movement over the H6 panel-A cells and turn
the price of commitment into a break-even statement.

The service loss of the commitment arm is already known (C1 serves fewer riders
than B1). What was never quantified is the other side of that trade: how much
announced-ETA movement the commitment actually spares the riders who are served,
and how much of that movement the operator itself was causing.

No new simulation is run. This reads only what the sealed transcripts recorded.
"""

from __future__ import annotations

import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "out"

CELLS = [
    f"d201811{day}-s10-r{rep}"
    for day in (14, 15, 16, 17, 18)
    for rep in (1, 2, 3, 4)
]
KEYS = (
    "visibleDelta.pickupEtaTotalMs",
    "visibleDelta.dropEtaTotalMs",
    "decisionDelta.pickupEtaTotalMs",
    "decisionDelta.dropEtaTotalMs",
    "exogenousDelta.pickupEtaTotalMs",
    "exogenousDelta.dropEtaTotalMs",
)


def load(cell: str, arm: str) -> dict | None:
    path = OUT / f"p-{cell}-{arm}-tight-s7.json"
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    arms = {"b1": {k: 0 for k in KEYS}, "c1": {k: 0 for k in KEYS}}
    served = {"b1": 0, "c1": 0}
    pubs = {"b1": 0, "c1": 0}
    requests = 0
    integrity = []
    peak = {"b1": {}, "c1": {}}

    for cell in CELLS:
        for arm in ("b1", "c1"):
            data = load(cell, arm)
            if data is None:
                integrity.append(f"{cell}/{arm}: MISSING")
                continue
            if not (data["acceptedCountAgreesWithRun"]
                    and data["rejectedCountAgreesWithRun"]
                    and data["publications"] == data["publicationCountFromRun"]):
                integrity.append(f"{cell}/{arm}: COUNT MISMATCH")
            served[arm] += data["acceptedCount"]
            pubs[arm] += data["publications"]
            for key in KEYS:
                arms[arm][key] += data["totalsAcceptedOnly"][key]
            for key, value in data["peakBudgetConsumed"].items():
                peak[arm][key] = max(peak[arm].get(key, 0), value)
        head = load(cell, "b1")
        if head:
            requests += head["requestCount"]

    print("integrity:", "all cells agree with run-00.json"
          if not integrity else integrity)
    print(f"requests over panel: {requests}")
    print()

    header = f"{'quantity':<44}{'B1':>14}{'C1':>14}{'C1 - B1':>14}"
    print(header)
    print("-" * len(header))
    print(f"{'riders served':<44}{served['b1']:>14,}{served['c1']:>14,}"
          f"{served['c1'] - served['b1']:>+14,}")
    print(f"{'service rate (%)':<44}{100 * served['b1'] / requests:>14.4f}"
          f"{100 * served['c1'] / requests:>14.4f}"
          f"{100 * (served['c1'] - served['b1']) / requests:>+14.4f}")
    print(f"{'promise publications':<44}{pubs['b1']:>14,}{pubs['c1']:>14,}"
          f"{pubs['c1'] - pubs['b1']:>+14,}")
    print("-" * len(header))
    for key in KEYS:
        b, c = arms["b1"][key], arms["c1"][key]
        print(f"{key + '  (s)':<44}{b / 1000:>14,.0f}{c / 1000:>14,.0f}"
              f"{(c - b) / 1000:>+14,.0f}")
    print("-" * len(header))
    for key in KEYS:
        b = arms["b1"][key] / 1000 / served["b1"]
        c = arms["c1"][key] / 1000 / served["c1"]
        print(f"{key + '  (s/rider served)':<44}{b:>14.2f}{c:>14.2f}{c - b:>+14.2f}")
    print()

    print("peak budget consumed (max over all publications):")
    for arm in ("b1", "c1"):
        interesting = {k: v for k, v in sorted(peak[arm].items()) if v}
        print(f"  {arm}: {interesting if interesting else 'all zero'}")
    print()

    # --- attribution -------------------------------------------------------
    total_visible_b1 = (arms["b1"]["visibleDelta.pickupEtaTotalMs"]
                        + arms["b1"]["visibleDelta.dropEtaTotalMs"])
    total_decision_b1 = (arms["b1"]["decisionDelta.pickupEtaTotalMs"]
                         + arms["b1"]["decisionDelta.dropEtaTotalMs"])
    total_visible_c1 = (arms["c1"]["visibleDelta.pickupEtaTotalMs"]
                        + arms["c1"]["visibleDelta.dropEtaTotalMs"])
    total_decision_c1 = (arms["c1"]["decisionDelta.pickupEtaTotalMs"]
                         + arms["c1"]["decisionDelta.dropEtaTotalMs"])
    print("ATTRIBUTION — share of the ETA movement riders see that the "
          "dispatcher itself caused:")
    print(f"  B1: {100 * total_decision_b1 / total_visible_b1:.2f}%  "
          f"({total_decision_b1 / 1000:,.0f} s of {total_visible_b1 / 1000:,.0f} s)")
    if total_visible_c1:
        print(f"  C1: {100 * total_decision_c1 / total_visible_c1:.2f}%  "
              f"({total_decision_c1 / 1000:,.0f} s of "
              f"{total_visible_c1 / 1000:,.0f} s)")
    print()

    # --- break-even --------------------------------------------------------
    avoided_seconds = (total_visible_b1 - total_visible_c1) / 1000
    lost_riders = served["b1"] - served["c1"]
    print("BREAK-EVEN")
    print(f"  unexpected ETA movement avoided by committing : "
          f"{avoided_seconds:,.0f} s  ({avoided_seconds / 3600:,.2f} h)")
    print(f"  riders not served because of committing       : {lost_riders:,}")
    print(f"  avoided movement per rider sacrificed         : "
          f"{avoided_seconds / lost_riders:,.1f} s")
    print()
    print("  A pooled trip has to be worth MORE than the value of that much")
    print("  unexpected time for the unconstrained arm to win on welfare:")
    print(f"  {'value of unexpected time':<34}{'break-even worth of one trip':>30}")
    for rate in (7.88, 10.80, 15.00, 20.00, 25.00):
        euros = avoided_seconds / 3600 * rate / lost_riders
        print(f"  {rate:>8.2f} EUR/h {'':<20}{euros:>26.2f} EUR")
    print()
    print("  (7.88-10.80 = in-vehicle VOT for pooled on-demand, Alonso-Gonzalez")
    print("   et al. 2020; 20-25 = unexpected waiting time, Gerzinic et al. 2023.)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
