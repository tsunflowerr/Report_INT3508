"""Rerun the sweep jobs that failed ONLY because the source tree changed mid-run (SWEEP-AMENDMENTS.md A2).

A job is rerun when its output has no summary.json AND its log contains the preflight's inventory-drift error.
Anything else is left alone and reported. The rerun uses exactly the job's command and label, with the output
<job>-rerun1 and the log logs/<job>-rerun1.log (mode "x"); an existing rerun output is never touched. Same safety
as run_sweep.py (AC power, STOP file, keep awake). Refuses to start while the main driver still runs.
Usage: python -B rerun_failed.py plan | run
"""
from __future__ import annotations

import concurrent.futures
import os
import subprocess
import sys
import time

import run_sweep
from run_sweep import LOG_ROOT, OUT_ROOT, run_pilot

DRIFT = "repository content inventory drifted during the matrix run"
SUFFIX = "-rerun1"


def failed_by_drift():
    """(rerun by drift, failed for another reason, output without a log yet = still running)."""
    out, other, running = [], [], []
    for name, arm, world, cell in run_sweep.jobs():
        if run_sweep.state_of(name) != "exists-no-summary":
            continue
        log = LOG_ROOT / f"{name}.log"
        if not log.exists():
            running.append((name, arm, world, cell))
            continue
        text = log.read_text(encoding="utf-8", errors="replace")
        (out if DRIFT in text else other).append((name, arm, world, cell))
    return out, other, running


def rerun(name, arm, world, cell):
    target = f"{name}{SUFFIX}"
    if (OUT_ROOT / target).exists():
        return target, "exists"
    if run_sweep.STOP_FILE.exists():
        return target, "deferred-stop"
    if not run_pilot.may_start_job():
        return target, "deferred-on-battery"
    command = run_sweep.command(name, arm, cell)
    command[command.index("--output") + 1] = str(OUT_ROOT / target)
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONIOENCODING="utf-8",
               RB_WORLD_CONFIG=str(run_pilot.world_file(world, cell)))
    started = time.time()
    completed = subprocess.run(command, cwd=str(run_pilot.REPO), check=False, capture_output=True, text=True,
                               encoding="utf-8", errors="replace", env=env)
    with open(LOG_ROOT / f"{target}.log", "x", encoding="utf-8", newline="\n") as handle:
        handle.write(f"returncode={completed.returncode} seconds={time.time() - started:.0f}\n"
                     + completed.stdout + completed.stderr)
    return target, run_sweep.state_of(target)


def main() -> int:
    if len(sys.argv) != 2 or sys.argv[1] not in ("plan", "run"):
        print(__doc__)
        return 2
    drift, other, running = failed_by_drift()
    print(f"failed by inventory drift: {len(drift)}; failed otherwise (NOT rerun): {len(other)}; "
          f"output without log (still running): {len(running)}")
    for name, *_ in drift:
        print(f"  rerun {name}")
    for name, *_ in other:
        print(f"  other {name}")
    for name, *_ in running:
        print(f"  running {name}")
    if sys.argv[1] == "plan":
        return 0
    if running:
        raise SystemExit("some jobs have no log yet; wait until the main driver has finished them")
    running = subprocess.run(["tasklist", "/FI", "IMAGENAME eq python.exe", "/V"], capture_output=True, text=True)
    if "run_sweep.py" in running.stdout:
        raise SystemExit("the main sweep driver is still running; wait for it to exit")
    run_pilot.keep_awake(True)
    started = time.time()
    try:
        with concurrent.futures.ThreadPoolExecutor(run_sweep.WORKERS) as pool:
            futures = [pool.submit(rerun, *item) for item in drift]
            for done, future in enumerate(concurrent.futures.as_completed(futures), start=1):
                target, label = future.result()
                print(f"[{time.time() - started:7.0f}s] {target:<52} {label:<22} ({done}/{len(drift)})", flush=True)
    finally:
        run_pilot.keep_awake(False)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
