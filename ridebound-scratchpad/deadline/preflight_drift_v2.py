"""Copy of drift/preflight_drift.py for the Tier-2 deadline experiment.

Differences from v1 (and nothing else):
  1. REPO points at the research worktree E:/Code/RideBound-deadline, so the preflight
     it wraps hashes and runs the worktree, not the user's main working tree.
  2. The window start is no longer hard-coded to 28800 (v1 line 73). It is read from
     RB_DRIFT_WINDOW_START_SECONDS, which is REQUIRED and must be 28800 (w08) or
     61200 (w17). With v1, an evening cell would silently receive the morning factors.
  3. An explicit guard that a factor row exists exactly at the window start (true for
     every day 12..18 at both starts; v1 relied on it implicitly).
v1 is left untouched because earlier runs reference it. check_preflight_v2.py proves
that v2 reproduces v1's schedule exactly at 28800 for every day.

Usage: identical to the real preflight, plus in the environment
    RB_DRIFT_DAY                    e.g. 2018-11-12
    RB_DRIFT_EXPONENT               0, 1, ...
    RB_DRIFT_WINDOW_START_SECONDS   28800 | 61200
"""

from __future__ import annotations

import csv
import importlib.util
import os
import pathlib
import sys

REPO = pathlib.Path(r"E:/Code/RideBound-deadline")
TARGET = REPO / "simulators/fleetpy-ridebound/actual_fleetpy_medium_preflight.py"
FACTORS = pathlib.Path(
    r"E:/RideBoundData/wp6/extracted/sha256/d9/"
    r"d9e86f33645e5eec287d387f8d63ad41ddf41d4ef648138b65d636482e2c599e/"
    r"FleetPy_Manhattan/networks/Manhattan_2019_corrected"
)
ALLOWED_WINDOW_STARTS = (28800, 61200)
# Matches normalizer-configuration.json: drainDurationMs = 7_200_000.
WINDOW_SECONDS = 7200


def window_start_from_environment() -> int:
    text = os.environ.get("RB_DRIFT_WINDOW_START_SECONDS")
    if text is None:
        raise SystemExit("RB_DRIFT_WINDOW_START_SECONDS is required (28800 or 61200)")
    try:
        value = int(text)
    except ValueError:
        raise SystemExit(f"RB_DRIFT_WINDOW_START_SECONDS must be an integer, got {text!r}")
    if value not in ALLOWED_WINDOW_STARTS:
        raise SystemExit(
            f"RB_DRIFT_WINDOW_START_SECONDS must be one of {ALLOWED_WINDOW_STARTS}, got {value}")
    return value


def load_schedule(day: str, exponent: float, window_start: int) -> list[tuple[int, float]]:
    """[(simTimeSeconds relative to the window, factor)], step-wise, factor(0) == 1.0."""
    if window_start not in ALLOWED_WINDOW_STARTS:
        raise SystemExit(f"unsupported window start {window_start}")
    path = FACTORS / f"{day}_tt_factors.csv"
    if not path.exists():
        raise SystemExit(f"no measured factors for {day}: {path}")
    rows = []
    with path.open(encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            seconds = int(row["simulation_time"])
            if window_start <= seconds <= window_start + WINDOW_SECONDS:
                rows.append((seconds, float(row["travel_time_factor"])))
    if not rows:
        raise SystemExit(f"{day}: no factor rows inside the window starting at {window_start}")
    rows.sort()
    if rows[0][0] != window_start:
        raise SystemExit(f"{day}: no factor row exactly at the window start {window_start}")
    base = rows[0][1]
    schedule = [
        (seconds - window_start, (factor / base) ** exponent)
        for seconds, factor in rows
    ]
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
    exponent = float(os.environ.get("RB_DRIFT_EXPONENT", "1"))
    window_start = window_start_from_environment()
    schedule = load_schedule(day, exponent, window_start)

    spec = importlib.util.spec_from_file_location("rb_preflight_drift_v2", TARGET)
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
            control.routing_engine._current_tt_factor = (
                None if wanted == 1.0 else wanted
            )
            control._rb_travel_arc_cache.clear()
            control._rb_travel_dirty = True
            state["changes"] += 1
            print(f"[drift] t={simulation_time:>6.0f}s factor={wanted:.4f}",
                  flush=True)
        return original(control, request_ids, request_db, simulation_time,
                        confirmed_ids, rejected_ids)

    module._trigger_and_resolve = patched
    span = schedule[-1][1] / min(value for _, value in schedule)
    print(f"[drift] day={day} k={exponent} windowStart={window_start} "
          f"steps={len(schedule)} span={span:.3f}x", flush=True)
    result = module.main()
    print(f"[drift] factor changes applied: {state['changes']}", flush=True)
    return result


if __name__ == "__main__":
    raise SystemExit(main())
