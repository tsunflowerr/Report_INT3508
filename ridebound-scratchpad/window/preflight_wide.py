"""Run the repository preflight with one simulator constant overridden.

The pickup window lives in two places that must agree:

  * the fixture -- each request's latestPickupMs (rewritten by
    build_wide_fixture.py to arrival + 900 s)
  * the simulator -- op_max_wait_time, hard-coded to 600 in
    simulators/fleetpy-ridebound/actual_fleetpy_medium_preflight.py

FleetPy clamps a PlanRequest's latest pickup with op_max_wait_time, and the
preflight then asserts the round trip is lossless, so raising only the fixture
fails with "FleetPy PlanRequest scalar round-trip drift". Both sides have to
move together.

Rather than edit the repository -- which must stay untouched, and which the
preflight itself hashes -- this imports the real module and replaces exactly one
value in exactly one function. Everything else, including __file__ and therefore
the derived repository root, git commit and inventory hash, is the repository's
own.

The override is deliberately loud: it prints what it changed, and the runs it
produces are kept in their own output root and must never be merged into the
sealed table.

Usage: identical to the real preflight, plus RB_MAX_WAIT_SECONDS in the
environment (default 900).
"""

from __future__ import annotations

import importlib.util
import os
import pathlib
import sys

REPO = pathlib.Path(r"E:/Code/RideBound")
TARGET = REPO / "simulators/fleetpy-ridebound/actual_fleetpy_medium_preflight.py"
SEALED_MAX_WAIT = 600


def main() -> int:
    window = int(os.environ.get("RB_MAX_WAIT_SECONDS", "900"))

    spec = importlib.util.spec_from_file_location("rb_preflight_wide", TARGET)
    if spec is None or spec.loader is None:
        raise SystemExit(f"cannot load {TARGET}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    # Guarded by `if __name__ == "__main__"`, so importing does not run it.
    spec.loader.exec_module(module)

    original = module._operator_settings

    def patched(*args, **kwargs):
        settings = original(*args, **kwargs)
        found = settings.get("op_max_wait_time")
        if found != SEALED_MAX_WAIT:
            # The constant moved in the repository; fail rather than silently
            # overriding something that is no longer what this patch assumes.
            raise SystemExit(
                f"expected op_max_wait_time={SEALED_MAX_WAIT} in the repository "
                f"preflight, found {found!r}; refusing to override"
            )
        settings["op_max_wait_time"] = window
        return settings

    module._operator_settings = patched
    print(f"[preflight_wide] op_max_wait_time {SEALED_MAX_WAIT} -> {window}",
          flush=True)
    return module.main()


if __name__ == "__main__":
    raise SystemExit(main())
