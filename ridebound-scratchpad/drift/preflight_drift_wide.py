"""Congestion drift AND a pickup window wide enough for the drift to fit in.

The first drift ladder (run_drift.py, 600 s window) produced a clean feasibility
result but a dirty service result, because of a wall that has nothing to do with
the commitment basis:

    RBWP7_RUNNER_PROTOCOL_ERROR: SCHEMA_VALIDATION_FAILED:
    Actual pickup time must remain inside the accepted pickup window.

With travel times 17-26% slower, a vehicle already en route arrives after the
request's latestPickup. The window was accepted under the old travel times, and
the runner's schema check is strict about it, so the run dies. That killed 11/20
conduct cells at k=1 -- not a commitment infeasibility, a physical one, and it
hits both bases equally.

(That is itself worth recording: a fixed pickup window accepted before a
congestion build-up is not honourable afterwards, whatever the dispatcher does.
ADR-045 already notes this class of problem "blocked WP9".)

To compare the two bases on service rather than on that wall, the window has to
have room for the drift. This combines the two overrides already built and
verified separately:

  * op_max_wait_time 600 -> 900, paired with the rewritten 900 s fixture
    (preflight_wide.py, verified against C1@900 = 1753)
  * the measured Manhattan factor schedule (preflight_drift.py, verified to
    raise per-rider exogenous drift p90 from 9.8 s to 69.9 s at k=2)

At a 900 s window a pickup planned near 600 s slips to about 700 s at k=1, so it
still lands inside the window and the wall does not fire.

The repository is not modified.

Usage: as the real preflight, plus
    RB_DRIFT_DAY        e.g. 2018-11-14
    RB_DRIFT_EXPONENT   0, 1, 2
    RB_MAX_WAIT_SECONDS default 900
"""

from __future__ import annotations

import importlib.util
import os
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from preflight_drift import factor_at, load_schedule  # noqa: E402

REPO = pathlib.Path(r"E:/Code/RideBound")
TARGET = REPO / "simulators/fleetpy-ridebound/actual_fleetpy_medium_preflight.py"
SEALED_MAX_WAIT = 600


def main() -> int:
    day = os.environ.get("RB_DRIFT_DAY")
    if not day:
        raise SystemExit("RB_DRIFT_DAY is required")
    # Fractional exponents are allowed: the wall described in run_drift_frac.py
    # fires somewhere between k=0 and k=1, so the usable drift level is not
    # an integer.
    exponent = float(os.environ.get("RB_DRIFT_EXPONENT", "1"))
    window = int(os.environ.get("RB_MAX_WAIT_SECONDS", "900"))
    schedule = load_schedule(day, exponent)

    spec = importlib.util.spec_from_file_location("rb_preflight_drift_wide", TARGET)
    if spec is None or spec.loader is None:
        raise SystemExit(f"cannot load {TARGET}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)

    # --- override 1: the simulator-side pickup window ---
    original_settings = module._operator_settings

    def patched_settings(*args, **kwargs):
        settings = original_settings(*args, **kwargs)
        found = settings.get("op_max_wait_time")
        if found != SEALED_MAX_WAIT:
            raise SystemExit(
                f"expected op_max_wait_time={SEALED_MAX_WAIT}, found {found!r}; "
                "refusing to override"
            )
        settings["op_max_wait_time"] = window
        return settings

    module._operator_settings = patched_settings

    # --- override 2: measured congestion drift ---
    original_trigger = module._trigger_and_resolve
    state = {"factor": None, "changes": 0}

    def patched_trigger(control, request_ids, request_db, simulation_time,
                        confirmed_ids, rejected_ids):
        wanted = factor_at(schedule, simulation_time)
        if wanted != state["factor"]:
            state["factor"] = wanted
            control.routing_engine._current_tt_factor = (
                None if wanted == 1.0 else wanted
            )
            control._rb_travel_arc_cache.clear()
            control._rb_travel_dirty = True
            state["changes"] += 1
        return original_trigger(control, request_ids, request_db,
                                simulation_time, confirmed_ids, rejected_ids)

    module._trigger_and_resolve = patched_trigger

    print(f"[driftwide] day={day} k={exponent} window={window}s "
          f"span={schedule[-1][1] / min(v for _, v in schedule):.3f}x", flush=True)
    result = module.main()
    print(f"[driftwide] factor changes applied: {state['changes']}", flush=True)
    return result


if __name__ == "__main__":
    raise SystemExit(main())
