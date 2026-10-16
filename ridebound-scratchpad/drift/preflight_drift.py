"""Run the repository preflight with real Manhattan congestion drift injected.

WHY
---
The three-anchor decomposition splits a promise move into the part the
dispatcher caused and the part the world caused. The second part, d, is what
separates the two ways of charging a budget:

    B (customer-visible) = A (decision-induced) + d

Theorem 1 says the conduct basis A is always satisfiable, because the no-op has
p = e and therefore delta 0 regardless of d. Theorem 2 says the outcome basis B
can be infeasible, because the no-op is still charged d. Theorem 3 says B's
feasible set is contained in A's, so B never serves more.

On the sealed panel those theorems are true but nearly empty: the fixture has a
single travel-time snapshot, so d comes only from execution lag and measures
p50 = 4.9 s. Both bases give essentially the same answer (1294 vs 1294 riders).

This makes d real, and predicts -- before measuring -- that the gap between the
bases grows with d while A stays feasible on every cell.

WHERE THE DRIFT COMES FROM
--------------------------
Not synthetic noise. The FleetPy Manhattan dataset ships measured 15-minute
travel-time factors per day. Over our 08:00-10:00 window the real morning peak
raises travel times by 17-26% depending on the day, monotonically.

    factor(t) = ( f_real(windowStart + t) / f_real(windowStart) ) ** k

k is the amplification. k=0 reproduces the flat baseline exactly; k=1 is the
real day; k=2 doubles the log-deviation. The ratio is taken against the window
start so that factor(0) = 1 exactly, which matters because the preflight asserts
at initialisation that the routing engine reproduces the fixture's arc travel
times ("metric closure drift"). Drift accumulates only after that check.

HOW IT IS INJECTED
------------------
FleetPy's NetworkBasic already supports a scalar travel-time factor: every
routing query multiplies by _current_tt_factor (NetworkBasic.py:348, :427).
Its own result store, _add_to_database, is a no-op in this class, so there is no
stale cache on the FleetPy side. The RideBound bridge does cache arc costs in
_rb_travel_arc_cache, and it already carries a _rb_travel_dirty flag that makes
it rebuild the snapshot and emit travelTimesUpdated (fleet_control.py:396).

So the whole mechanism is: set the factor, clear the bridge cache, raise the
dirty flag. All three happen on the objects the preflight already built, from
_trigger_and_resolve, which receives both the control and the simulation time.

The repository is not modified; it is hash-checked by the preflight.

Usage: identical to the real preflight, plus in the environment
    RB_DRIFT_DAY        e.g. 2018-11-14   (which day's measured factors)
    RB_DRIFT_EXPONENT   0, 1, 2, ...      (amplification k)
"""

from __future__ import annotations

import csv
import importlib.util
import os
import pathlib
import sys

REPO = pathlib.Path(r"E:/Code/RideBound")
TARGET = REPO / "simulators/fleetpy-ridebound/actual_fleetpy_medium_preflight.py"
FACTORS = pathlib.Path(
    r"E:/RideBoundData/wp6/extracted/sha256/d9/"
    r"d9e86f33645e5eec287d387f8d63ad41ddf41d4ef648138b65d636482e2c599e/"
    r"FleetPy_Manhattan/networks/Manhattan_2019_corrected"
)
# Matches normalizer-configuration.json: sourceWindowStartSeconds / drainDurationMs.
WINDOW_START_SECONDS = 28800
WINDOW_SECONDS = 7200


def load_schedule(day: str, exponent: float) -> list[tuple[int, float]]:
    """[(simTimeSeconds, factor)], step-wise, factor(0) == 1.0 exactly."""
    path = FACTORS / f"{day}_tt_factors.csv"
    if not path.exists():
        raise SystemExit(f"no measured factors for {day}: {path}")
    rows = []
    with path.open(encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            seconds = int(row["simulation_time"])
            if WINDOW_START_SECONDS <= seconds <= WINDOW_START_SECONDS + WINDOW_SECONDS:
                rows.append((seconds, float(row["travel_time_factor"])))
    if not rows:
        raise SystemExit(f"{day}: no factor rows inside the window")
    rows.sort()
    base = rows[0][1]
    schedule = [
        (seconds - WINDOW_START_SECONDS, (factor / base) ** exponent)
        for seconds, factor in rows
    ]
    # Guard the invariant the initialisation check depends on.
    if abs(schedule[0][1] - 1.0) > 1e-12:
        raise SystemExit("factor at window start must be exactly 1.0")
    return schedule


def factor_at(schedule: list[tuple[int, float]], simulation_time: float) -> float:
    current = schedule[0][1]
    for seconds, factor in schedule:
        if simulation_time >= seconds:
            current = factor
        else:
            break
    return current


def main() -> int:
    day = os.environ.get("RB_DRIFT_DAY")
    if not day:
        raise SystemExit("RB_DRIFT_DAY is required")
    # Fractional exponents are allowed: the wall described in run_drift_frac.py
    # fires somewhere between k=0 and k=1, so the usable drift level is not
    # an integer.
    exponent = float(os.environ.get("RB_DRIFT_EXPONENT", "1"))
    schedule = load_schedule(day, exponent)

    spec = importlib.util.spec_from_file_location("rb_preflight_drift", TARGET)
    if spec is None or spec.loader is None:
        raise SystemExit(f"cannot load {TARGET}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)

    original = module._trigger_and_resolve
    state = {"factor": None, "changes": 0}

    def patched(control, request_ids, request_db, simulation_time,
                confirmed_ids, rejected_ids):
        wanted = factor_at(schedule, simulation_time)
        if wanted != state["factor"]:
            state["factor"] = wanted
            # NetworkBasic treats None as "no factor" and takes a different code
            # path; keep exactly the baseline path while the factor is 1.
            control.routing_engine._current_tt_factor = (
                None if wanted == 1.0 else wanted
            )
            # The bridge memoises arc costs; they are now stale.
            control._rb_travel_arc_cache.clear()
            # Makes the bridge rebuild the snapshot and emit travelTimesUpdated.
            control._rb_travel_dirty = True
            state["changes"] += 1
            print(f"[drift] t={simulation_time:>6.0f}s factor={wanted:.4f}",
                  flush=True)
        return original(control, request_ids, request_db, simulation_time,
                        confirmed_ids, rejected_ids)

    module._trigger_and_resolve = patched
    span = schedule[-1][1] / min(value for _, value in schedule)
    print(f"[drift] day={day} k={exponent} steps={len(schedule)} "
          f"span={span:.3f}x", flush=True)
    result = module.main()
    print(f"[drift] factor changes applied: {state['changes']}", flush=True)
    return result


if __name__ == "__main__":
    raise SystemExit(main())
