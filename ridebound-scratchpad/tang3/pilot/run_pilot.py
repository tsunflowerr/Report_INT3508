"""T3.7 pilot driver (exploratory; plan: ../T3.7-KE-HOACH-THI-DIEM.md).

5 arms x 2 development cells x 6 worlds = 60 jobs, each the repository medium preflight run inside a
world through ../world/preflight_world.py, with the Runner published at runner-tier3-v1.

Safety, as in the Tier-2 driver (deadline/run_deadline.py):
  * a job starts only on AC power (or battery above RB_ALLOW_BATTERY_MIN_PERCENT if the owner set it);
  * while the file STOP exists next to this script, nothing new starts (running jobs finish);
  * an existing output directory is never touched again (state "exists"); nothing is deleted;
  * every log is opened with mode "x"; Windows is asked not to idle-sleep while jobs run.

Usage: python -B run_pilot.py plan | run | report
"""
from __future__ import annotations

import concurrent.futures
import ctypes
import json
import os
import pathlib
import subprocess
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
TANG3 = HERE.parent
REPO = pathlib.Path(r"E:/Code/RideBound-deadline")
PYTHON = pathlib.Path(r"E:/RideBoundData/wp7/envs/fleetpy-1.0.2/python.exe")
FLEETPY = pathlib.Path(r"E:/RideBoundData/wp7/FleetPy-1.0.2")
RUNNER = pathlib.Path(r"E:/RideBoundData/research/runner-tier3-v1")
DOTNET = pathlib.Path(r"C:/Program Files/dotnet/dotnet.exe")
OUT_ROOT = pathlib.Path(r"E:/RideBoundData/research/tier3-pilot-v1")
LOG_ROOT = HERE / "logs"
PREFLIGHT = TANG3 / "world" / "preflight_world.py"
CONFIGS = TANG3 / "configs"
WORLDS = HERE / "worlds"
WP4 = CONFIGS / "wp4-tier3-v1.json"
FIXTURES = REPO / "benchmarks/fixtures/wp6/public/fleetpy-manhattan-v1/wp14-development-panel-v1"
DRIVERS = REPO / "benchmarks/scenarios/wp14-development"
STOP_FILE = HERE / "STOP"
BATTERY_ENV = "RB_ALLOW_BATTERY_MIN_PERCENT"
WORKERS = 6

ARMS = ("U", "C-30", "V-30", "Mplus-30", "M-30")
CELLS = ("d20181112-s10-r1-w08", "d20181112-s10-r1-w17")
WORLD_IDS = ("W0", "W1", "W2", "W3", "W4", "W5")


def world_file(world: str, cell: str) -> pathlib.Path:
    # W5 is the measured day, whose base depends on the cell's window.
    return WORLDS / (f"W5-{cell[-3:]}.json" if world == "W5" else f"{world}.json")


def jobs():
    for cell in CELLS:
        for world in WORLD_IDS:
            for arm in ARMS:
                yield f"{arm}-{world}-{cell}", arm, world, cell


def power_status():
    class SystemPowerStatus(ctypes.Structure):
        _fields_ = [("ACLineStatus", ctypes.c_ubyte), ("BatteryFlag", ctypes.c_ubyte),
                    ("BatteryLifePercent", ctypes.c_ubyte), ("SystemStatusFlag", ctypes.c_ubyte),
                    ("BatteryLifeTime", ctypes.c_ulong), ("BatteryFullLifeTime", ctypes.c_ulong)]

    status = SystemPowerStatus()
    if not ctypes.windll.kernel32.GetSystemPowerStatus(ctypes.byref(status)):
        return None
    return status.ACLineStatus, status.BatteryLifePercent


def may_start_job() -> bool:
    status = power_status()
    if status is None:
        return False
    ac_line, percent = status
    if ac_line == 1:
        return True
    minimum = os.environ.get(BATTERY_ENV)
    return minimum is not None and percent != 255 and percent >= int(minimum)


def keep_awake(active: bool) -> None:
    ES_CONTINUOUS, ES_SYSTEM_REQUIRED = 0x80000000, 0x00000001
    ctypes.windll.kernel32.SetThreadExecutionState(
        ES_CONTINUOUS | (ES_SYSTEM_REQUIRED if active else 0))


def state_of(name: str) -> str:
    output = OUT_ROOT / name
    if not output.exists():
        return "pending"
    summary = output / "summary.json"
    if summary.exists():
        return "status-" + json.loads(summary.read_text(encoding="utf-8")).get("status", "unknown")
    return "exists-no-summary"


def command(name: str, arm: str, cell: str) -> list[str]:
    fixture = FIXTURES / cell
    return [
        str(PYTHON), "-B", str(PREFLIGHT),
        "--label", name,
        "--fleetpy-root", str(FLEETPY),
        "--runner-root", str(RUNNER),
        "--dotnet", str(DOTNET),
        "--commitment-config", str(CONFIGS / f"{arm}.json"),
        "--wp4-config", str(WP4),
        "--scenario", str(fixture / "scenario-content.json"),
        "--derivative-manifest", str(fixture / "derivative-manifest.json"),
        "--normalization-report", str(fixture / "normalization-report.json"),
        "--selection-frame", str(fixture / "selection-frame.json"),
        "--driver", str(DRIVERS / f"{cell}.driver.json"),
        "--output", str(OUT_ROOT / name),
        "--repeats", "1",
        "--master-seed", "7",
    ]


def run_job(name, arm, world, cell):
    if state_of(name) != "pending":
        return name, state_of(name)
    if STOP_FILE.exists():
        return name, "deferred-stop"
    if not may_start_job():
        return name, "deferred-on-battery"
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONIOENCODING="utf-8",
               RB_WORLD_CONFIG=str(world_file(world, cell)))
    started = time.time()
    completed = subprocess.run(command(name, arm, cell), cwd=str(REPO), check=False,
                               capture_output=True, text=True, encoding="utf-8",
                               errors="replace", env=env)
    with open(LOG_ROOT / f"{name}.log", "x", encoding="utf-8", newline="\n") as handle:
        handle.write(f"returncode={completed.returncode} seconds={time.time() - started:.0f}\n"
                     + completed.stdout + completed.stderr)
    return name, state_of(name)


def main() -> int:
    if len(sys.argv) != 2 or sys.argv[1] not in ("plan", "run", "report"):
        print(__doc__)
        return 2
    items = list(jobs())
    if sys.argv[1] in ("plan", "report"):
        for name, *_ in items:
            print(f"{name}\t{state_of(name)}")
        states = [state_of(name) for name, *_ in items]
        print({state: states.count(state) for state in sorted(set(states))})
        return 0
    missing = [path for path in [RUNNER / "RideBound.Runner.dll", PREFLIGHT, WP4]
               + [CONFIGS / f"{arm}.json" for arm in ARMS]
               + [world_file(w, c) for w in WORLD_IDS for c in CELLS]
               + [FIXTURES / c for c in CELLS] if not path.exists()]
    if missing:
        raise SystemExit(f"missing inputs: {missing}")
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    LOG_ROOT.mkdir(parents=True, exist_ok=True)
    keep_awake(True)
    started = time.time()
    deferred = 0
    try:
        with concurrent.futures.ThreadPoolExecutor(WORKERS) as pool:
            futures = [pool.submit(run_job, *item) for item in items]
            for done, future in enumerate(concurrent.futures.as_completed(futures), start=1):
                name, label = future.result()
                deferred += label.startswith("deferred")
                print(f"[{time.time() - started:7.0f}s] {name:<44} {label:<22} ({done}/{len(items)})",
                      flush=True)
    finally:
        keep_awake(False)
    return 3 if deferred else 0


if __name__ == "__main__":
    raise SystemExit(main())
