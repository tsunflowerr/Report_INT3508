"""Tier-2 driver: deadline families under measured Manhattan drift (plan T2.6).

Stages (run in this order; see PLAN below):
  controls     ctl-conduct-k0, ctl-visible-k0 on panel A (new runner must reproduce drift-v1)
  smoke        conduct-30, k=1, one evening development cell
  2b-conduct   conduct-30, k=1, all 16 development cells
  2a-base-conduct  conduct-30, k=1, panel A (amendment: the drift-v1 failure artifacts of
               this arm no longer exist; re-run on the new runner so the reference
               trajectory and death time of all 20 cells are available)
  -- predictions are sealed here (holdout_predict.py + PREREGISTRATION) --
  2a           dl-30, dl-60, dl-120 x k in {0,1} x 20 panel-A cells
  2b-rest      visible-30, dl-30, dl-60, dl-120, dl2-30, k=1, 16 development cells
  2a-base-visible  visible-30, k=1, panel A (not predicted; re-run for classifiable artifacts)

Every job writes E:/RideBoundData/research/deadline-v1/<job>/. A job is skipped when its
output already holds summary.json ("reused") or failure-00.json ("failed-recorded"). A
directory holding neither is REPORTED and the job is not started (trap 12.8): nothing is
ever deleted by this script.

Usage:
  run_deadline.py plan [stage ...]      list jobs and their state, run nothing
  run_deadline.py run <stage> [...]     run the stage(s)
  run_deadline.py report [stage ...]    classify every existing output
"""
from __future__ import annotations

import concurrent.futures
import json
import os
import subprocess
import sys
import time
from pathlib import Path

import classify

HERE = Path(__file__).resolve().parent
REPO = Path(r"E:/Code/RideBound-deadline")
PREFLIGHT = HERE / "preflight_drift_v2.py"
CONFIGS = HERE / "configs"
OUT_ROOT = Path(r"E:/RideBoundData/research/deadline-v1")
LOG_ROOT = HERE / "logs" / "runs"
PYTHON = Path(r"E:/RideBoundData/wp7/envs/fleetpy-1.0.2/python.exe")
FLEETPY = Path(r"E:/RideBoundData/wp7/FleetPy-1.0.2")
RUNNER = Path(r"E:/RideBoundData/research/runner-deadline-v1")
DOTNET = Path(r"C:/Program Files/dotnet/dotnet.exe")
WP4 = REPO / "benchmarks/configurations/wp9-fleetpy-ridebound-hard-vector-audited-v1.json"
WORKERS = 6

PANEL_A = {
    "fixtures": REPO / "benchmarks/fixtures/wp6/public/fleetpy-manhattan-v1/wp9-confirmatory-fixed-panel-v2",
    "drivers": REPO / "benchmarks/scenarios/wp9-confirmatory",
    "cells": [f"d201811{d}-s10-r{r}" for d in (14, 15, 16, 17, 18) for r in (1, 2, 3, 4)],
}
PANEL_DEV = {
    "fixtures": REPO / "benchmarks/fixtures/wp6/public/fleetpy-manhattan-v1/wp14-development-panel-v1",
    "drivers": REPO / "benchmarks/scenarios/wp14-development",
    "cells": [f"d201811{d}-s10-r{r}-w{w}" for d in (12, 13) for r in (1, 2, 3, 4) for w in ("08", "17")],
}
ARM_CONFIG = {
    "ctl-conduct": "conduct-30", "ctl-visible": "visible-30",
    "conduct-30": "conduct-30", "visible-30": "visible-30",
    "dl-30": "dl-30", "dl-60": "dl-60", "dl-120": "dl-120", "dl2-30": "dl2-30",
}


def jobs(stage: str):
    """Yield (job, arm, k, panel, cell)."""
    if stage == "controls":
        for arm in ("ctl-conduct", "ctl-visible"):
            for cell in PANEL_A["cells"]:
                yield f"{arm}-k0-{cell}-s7", arm, 0, PANEL_A, cell
    elif stage == "smoke":
        cell = "d20181112-s10-r1-w17"
        yield f"conduct-30-k1-{cell}-s7", "conduct-30", 1, PANEL_DEV, cell
    elif stage == "2b-conduct":
        for cell in PANEL_DEV["cells"]:
            yield f"conduct-30-k1-{cell}-s7", "conduct-30", 1, PANEL_DEV, cell
    elif stage == "2a-base-conduct":
        for cell in PANEL_A["cells"]:
            yield f"conduct-30-k1-{cell}-s7", "conduct-30", 1, PANEL_A, cell
    elif stage == "2a-base-visible":
        for cell in PANEL_A["cells"]:
            yield f"visible-30-k1-{cell}-s7", "visible-30", 1, PANEL_A, cell
    elif stage == "2a":
        for arm in ("dl-30", "dl-60", "dl-120"):
            for k in (0, 1):
                for cell in PANEL_A["cells"]:
                    yield f"{arm}-k{k}-{cell}-s7", arm, k, PANEL_A, cell
    elif stage == "2b-rest":
        for arm in ("visible-30", "dl-30", "dl-60", "dl-120", "dl2-30"):
            for cell in PANEL_DEV["cells"]:
                yield f"{arm}-k1-{cell}-s7", arm, 1, PANEL_DEV, cell
    else:
        raise SystemExit(f"unknown stage {stage!r}")


# Order matters for the preregistration: everything up to 2a-base-conduct contains no
# outcome of a predicted arm; predictions are sealed after it; the rest is predicted.
STAGES = ["controls", "smoke", "2b-conduct", "2a-base-conduct",
          "2a", "2b-rest", "2a-base-visible"]


HOST_FAILURES_FILE = HERE / "HOST_FAILURES.txt"
# Pause switch: while this file exists no new job is started (running jobs finish normally).
STOP_FILE = HERE / "STOP"


def host_failures() -> set[str]:
    """Output names recorded as host-caused failures (AMENDMENTS.md A2); never outcomes."""
    if not HOST_FAILURES_FILE.exists():
        return set()
    return {line.strip() for line in HOST_FAILURES_FILE.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.startswith("#")}


def effective_name(job: str) -> str:
    """The output name that counts for `job`: the job itself, or its latest rerun when the
    earlier run is a recorded host failure (job -> job-rerun1 -> job-rerun2 ...)."""
    failures = host_failures()
    name, attempt = job, 0
    while name in failures:
        attempt += 1
        name = f"{job}-rerun{attempt}"
    return name


def effective_output(job: str) -> Path:
    return OUT_ROOT / effective_name(job)


def keep_awake(active: bool) -> None:
    """Ask Windows not to idle-sleep while jobs run (SetThreadExecutionState). This changes no
    machine setting and cannot stop a lid close or a manual sleep."""
    import ctypes
    ES_CONTINUOUS, ES_SYSTEM_REQUIRED = 0x80000000, 0x00000001
    flags = ES_CONTINUOUS | (ES_SYSTEM_REQUIRED if active else 0)
    ctypes.windll.kernel32.SetThreadExecutionState(flags)


def day_of(cell: str) -> str:
    stamp = cell[1:9]
    return f"{stamp[:4]}-{stamp[4:6]}-{stamp[6:8]}"


def window_of(fixture: Path) -> int:
    config = json.loads((fixture / "normalizer-configuration.json").read_text(encoding="utf-8"))
    if config["drainDurationMs"] != 7_200_000:
        raise SystemExit(f"{fixture}: drainDurationMs {config['drainDurationMs']} != 7200000")
    start = config["sourceWindowStartSeconds"]
    if start not in (28800, 61200):
        raise SystemExit(f"{fixture}: unsupported sourceWindowStartSeconds {start}")
    return start


def state_of(output: Path) -> str:
    if (output / "summary.json").exists():
        return "reused"
    if (output / "failure-00.json").exists():
        return "failed-recorded"
    if output.exists():
        return "blocked-existing-dir"
    return "pending"


BATTERY_ENV = "RB_ALLOW_BATTERY_MIN_PERCENT"


def power_status():
    """(ac_line_status, battery_percent) from Win32 GetSystemPowerStatus; None if unavailable."""
    import ctypes

    class SystemPowerStatus(ctypes.Structure):
        _fields_ = [("ACLineStatus", ctypes.c_ubyte), ("BatteryFlag", ctypes.c_ubyte),
                    ("BatteryLifePercent", ctypes.c_ubyte), ("SystemStatusFlag", ctypes.c_ubyte),
                    ("BatteryLifeTime", ctypes.c_ulong), ("BatteryFullLifeTime", ctypes.c_ulong)]

    status = SystemPowerStatus()
    if not ctypes.windll.kernel32.GetSystemPowerStatus(ctypes.byref(status)):
        return None
    return status.ACLineStatus, status.BatteryLifePercent


def may_start_job() -> bool:
    """AC power, or battery allowed by the owner (env RB_ALLOW_BATTERY_MIN_PERCENT) with at least
    that charge left. A job takes up to ~15 min, so the minimum leaves room for running jobs to
    finish before the battery is empty; below it nothing new starts."""
    status = power_status()
    if status is None:
        return False
    ac_line, percent = status
    if ac_line == 1:
        return True
    minimum = os.environ.get(BATTERY_ENV)
    return minimum is not None and percent != 255 and percent >= int(minimum)


def on_ac_power() -> bool:
    """True when the host runs on AC power (Win32 GetSystemPowerStatus ACLineStatus == 1).

    A job that dies because the laptop ran out of battery would leave an output directory that
    must not be deleted, so jobs are only STARTED on AC power. Unknown status counts as not AC.
    """
    import ctypes

    class SystemPowerStatus(ctypes.Structure):
        _fields_ = [("ACLineStatus", ctypes.c_ubyte), ("BatteryFlag", ctypes.c_ubyte),
                    ("BatteryLifePercent", ctypes.c_ubyte), ("SystemStatusFlag", ctypes.c_ubyte),
                    ("BatteryLifeTime", ctypes.c_ulong), ("BatteryFullLifeTime", ctypes.c_ulong)]

    status = SystemPowerStatus()
    if not ctypes.windll.kernel32.GetSystemPowerStatus(ctypes.byref(status)):
        return False
    return status.ACLineStatus == 1


def run_job(job, arm, k, panel, cell):
    name = effective_name(job)
    output = OUT_ROOT / name
    state = state_of(output)
    if state != "pending":
        return name, state
    if STOP_FILE.exists():
        # Clean pause requested: start nothing new; running jobs finish normally.
        return name, "deferred-stop"
    if not may_start_job():
        # Nothing is created, so the job stays "pending" and a later run picks it up.
        return name, "deferred-on-battery"
    fixture = panel["fixtures"] / cell
    command = [
        str(PYTHON), "-B", str(PREFLIGHT),
        "--label", name,
        "--fleetpy-root", str(FLEETPY),
        "--runner-root", str(RUNNER),
        "--dotnet", str(DOTNET),
        "--commitment-config", str(CONFIGS / f"{ARM_CONFIG[arm]}.json"),
        "--wp4-config", str(WP4),
        "--scenario", str(fixture / "scenario-content.json"),
        "--derivative-manifest", str(fixture / "derivative-manifest.json"),
        "--normalization-report", str(fixture / "normalization-report.json"),
        "--selection-frame", str(fixture / "selection-frame.json"),
        "--driver", str(panel["drivers"] / f"{cell}.driver.json"),
        "--output", str(output),
        "--repeats", "1",
        "--master-seed", "7",
    ]
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env["PYTHONIOENCODING"] = "utf-8"
    env["RB_DRIFT_DAY"] = day_of(cell)
    env["RB_DRIFT_EXPONENT"] = str(k)
    env["RB_DRIFT_WINDOW_START_SECONDS"] = str(window_of(fixture))
    started = time.time()
    completed = subprocess.run(
        command, cwd=str(REPO), check=False, capture_output=True,
        text=True, encoding="utf-8", errors="replace", env=env)
    LOG_ROOT.mkdir(parents=True, exist_ok=True)
    # Named by the output (a rerun gets its own log); mode "x" so no log is ever overwritten.
    with open(LOG_ROOT / f"{name}.log", "x", encoding="utf-8", newline="\n") as handle:
        handle.write(f"returncode={completed.returncode} seconds={time.time() - started:.0f}\n"
                     + completed.stdout + completed.stderr)
    return name, classify.classify_output(output)


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    command, stages = sys.argv[1], sys.argv[2:] or STAGES
    for stage in stages:
        if stage not in STAGES:
            raise SystemExit(f"unknown stage {stage!r}; known {STAGES}")
    if command == "plan":
        for stage in stages:
            items = list(jobs(stage))
            states = [state_of(effective_output(job)) for job, *_ in items]
            print(f"{stage}: {len(items)} jobs; "
                  + ", ".join(f"{s}={states.count(s)}" for s in sorted(set(states))))
        return 0
    if command == "report":
        for stage in stages:
            for job, *_ in jobs(stage):
                output = effective_output(job)
                if output.exists():
                    print(f"{stage}\t{output.name}\t{classify.classify_output(output)}")
        return 0
    if command != "run":
        raise SystemExit(f"unknown command {command!r}")
    if not (RUNNER / "RideBound.Runner.dll").exists():
        raise SystemExit(f"runner not published at {RUNNER}")
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    keep_awake(True)
    try:
        return run_stages(stages)
    finally:
        keep_awake(False)


def run_stages(stages) -> int:
    started = time.time()
    for stage in stages:
        items = list(jobs(stage))
        blocked = [job for job, *_ in items
                   if state_of(effective_output(job)) == "blocked-existing-dir"]
        if blocked:
            print(f"{stage}: {len(blocked)} incomplete output dir(s) block the stage; "
                  f"inspect them, nothing is deleted: {blocked[:5]}")
            return 1
        done = 0
        deferred = 0
        with concurrent.futures.ThreadPoolExecutor(WORKERS) as pool:
            futures = [pool.submit(run_job, *item) for item in items]
            for future in concurrent.futures.as_completed(futures):
                job, label = future.result()
                done += 1
                deferred += label in ("deferred-on-battery", "deferred-stop")
                print(f"[{time.time() - started:7.0f}s] {stage:<10} {job:<44} {label:<40} "
                      f"({done}/{len(items)})", flush=True)
        if deferred:
            # Stage order matters for the preregistration: never start the next stage
            # while this one still has jobs that were not run.
            print(f"--- stage {stage} INCOMPLETE: {deferred} job(s) deferred (battery or STOP "
                  f"file); later stages not started ---", flush=True)
            return 3
        print(f"--- stage {stage} complete at {time.time() - started:.0f}s ---", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
