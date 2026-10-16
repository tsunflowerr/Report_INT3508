"""Tier 3 task B driver (plan: W07-PLAN.md, sealed in W07-PLAN.sha256 before any job).

Real traffic only, 07:00-09:00 (the steepest part of the morning ramp), on 8 new development cells
d2018111{2,3}-s10-r{1..4}-w07 (grid tier3-development-w07-v1, grid-w07-v1.json):
  arms U; C-30/60/120/300; Mplus-30/60/120/300; V-30; M-30 = 11 arms x 8 cells = 88 jobs;
  world: the measured day of the cell (worlds/W5-<day>-w07.json, sigma = shockRate = 0), through the world
  wrapper v1.2 (../world/preflight_world_v1_2.py), which refuses a world whose day/window differs from the cell;
  recovery rule (b) for every arm: runner-tier3-v2 + ../configs/wp4-tier3-v2.json.
Fixtures and drivers live outside every repository (FIXTURE_ROOT, DRIVER_ROOT); the adapter and the medium
preflight run from E:/Code/RideBound-deadline (never modified), with --expected-repository-inventory-sha256.

Safety as run_sweep.py / run_vm.py: AC power only, STOP file next to this script, outputs never reused, logs mode
"x" (a pending job whose log exists is reported, not retried), Windows kept awake.
Usage: python -B run_w07.py plan | run | report
"""
from __future__ import annotations

import concurrent.futures
import hashlib
import json
import os
import pathlib
import subprocess
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
TANG3 = HERE.parent
sys.path.insert(0, str(TANG3 / "pilot"))

import run_pilot  # noqa: E402

ARMS = ("U",) + tuple(f"{family}-{x}" for x in (30, 60, 120, 300) for family in ("C", "Mplus")) + ("V-30", "M-30")
CELLS = tuple(f"d201811{day}-s10-r{r}-w07" for day in ("12", "13") for r in (1, 2, 3, 4))
OUT_ROOT = pathlib.Path(r"C:/RideBoundData/research/tier3-w07-v1")
FIXTURE_ROOT = pathlib.Path(r"C:/RideBoundData/research/fixtures-w07-v1")
DRIVER_ROOT = HERE / "drivers"
WORLDS = HERE / "worlds"
PREFLIGHT = TANG3 / "world" / "preflight_world_v1_2.py"
RUNNER = pathlib.Path(r"C:/RideBoundData/research/runner-tier3-v2")
RUNNER_TREE = "ac251ef32a4865ea3bd3d8d87b4b1bcaccc4462a9b80160b4d205b8d474cff3f"
WP4 = run_pilot.CONFIGS / "wp4-tier3-v2.json"
WP4_SHA256 = "66e9b59249d9491d520f3ed592e8c878a0d3b100e39432d5f4b73321617b4518"
LOG_ROOT = HERE / "logs"
STOP_FILE = HERE / "STOP"
EXPECTED_INVENTORY = "0da63eaf2b30ab332fba265a6b2b6e5c36b3ee78950cbac6d6267e60f81e4cbe"
WORKERS = run_pilot.WORKERS


def world_file(cell: str) -> pathlib.Path:
    return WORLDS / f"W5-{cell[:9]}-w07.json"


def jobs():
    # Cell by cell, so each cell's arms finish close together; U and C first in each cell.
    for cell in CELLS:
        for arm in ARMS:
            yield f"{arm}-{cell}", arm, cell


def state_of(name: str) -> str:
    output = OUT_ROOT / name
    if not output.exists():
        return "pending"
    summary = output / "summary.json"
    if summary.exists():
        return "status-" + json.loads(summary.read_text(encoding="utf-8")).get("status", "unknown")
    return "exists-no-summary"


def command(name: str, arm: str, cell: str) -> list[str]:
    fixture = FIXTURE_ROOT / cell
    return [
        str(run_pilot.PYTHON), "-B", str(PREFLIGHT),
        "--label", f"{name}-w07",
        "--fleetpy-root", str(run_pilot.FLEETPY),
        "--runner-root", str(RUNNER),
        "--dotnet", str(run_pilot.DOTNET),
        "--commitment-config", str(run_pilot.CONFIGS / f"{arm}.json"),
        "--wp4-config", str(WP4),
        "--scenario", str(fixture / "scenario-content.json"),
        "--derivative-manifest", str(fixture / "derivative-manifest.json"),
        "--normalization-report", str(fixture / "normalization-report.json"),
        "--selection-frame", str(fixture / "selection-frame.json"),
        "--driver", str(DRIVER_ROOT / f"{cell}.driver.json"),
        "--output", str(OUT_ROOT / name),
        "--repeats", "1",
        "--master-seed", "7",
        "--expected-repository-inventory-sha256", EXPECTED_INVENTORY,
    ]


def run_job(name, arm, cell):
    if state_of(name) != "pending":
        return name, state_of(name)
    log = LOG_ROOT / f"{name}.log"
    if log.exists():
        return name, "log-exists-pending"
    if STOP_FILE.exists():
        return name, "deferred-stop"
    if not run_pilot.may_start_job():
        return name, "deferred-on-battery"
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONIOENCODING="utf-8", RB_WORLD_CONFIG=str(world_file(cell)))
    started = time.time()
    completed = subprocess.run(command(name, arm, cell), cwd=str(run_pilot.REPO), check=False, capture_output=True,
                               text=True, encoding="utf-8", errors="replace", env=env)
    with open(log, "x", encoding="utf-8", newline="\n") as handle:
        handle.write(f"returncode={completed.returncode} seconds={time.time() - started:.0f}\n"
                     + completed.stdout + completed.stderr)
    return name, state_of(name)


def check_inputs() -> list[str]:
    problems = []
    if not PREFLIGHT.exists():
        problems.append(f"missing {PREFLIGHT}")
    if hashlib.sha256(WP4.read_bytes()).hexdigest() != WP4_SHA256:
        problems.append("WP4 v2 SHA-256 mismatch")
    sys.path.insert(0, str(TANG3))
    import runner_manifest
    tree = hashlib.sha256("\n".join(runner_manifest.body(RUNNER)).encode("utf-8")).hexdigest()
    if tree != RUNNER_TREE:
        problems.append(f"runner tree {tree}")
    for arm in ARMS:
        if not (run_pilot.CONFIGS / f"{arm}.json").exists():
            problems.append(f"missing arm config {arm}")
    for cell in CELLS:
        fixture = FIXTURE_ROOT / cell
        driver = DRIVER_ROOT / f"{cell}.driver.json"
        if not world_file(cell).exists():
            problems.append(f"missing world {world_file(cell)}")
        if not fixture.exists() or not driver.exists():
            problems.append(f"missing fixture or driver for {cell}")
            continue
        declared = json.loads(driver.read_text(encoding="utf-8"))["sourceScenarioContentSha256"]
        if hashlib.sha256((fixture / "scenario-content.json").read_bytes()).hexdigest() != declared:
            problems.append(f"{cell}: fixture scenario SHA-256 differs from the driver")
    return problems


def main() -> int:
    if len(sys.argv) != 2 or sys.argv[1] not in ("plan", "run", "report"):
        print(__doc__)
        return 2
    items = list(jobs())
    if sys.argv[1] in ("plan", "report"):
        for name, *_ in items:
            print(f"{name}\t{state_of(name)}")
        states = [state_of(name) for name, *_ in items]
        print(len(items), {state: states.count(state) for state in sorted(set(states))})
        if sys.argv[1] == "plan":
            print("input problems:", check_inputs() or "none")
        return 0
    problems = check_inputs()
    if problems:
        raise SystemExit(f"input problems: {problems}")
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    LOG_ROOT.mkdir(parents=True, exist_ok=True)
    run_pilot.keep_awake(True)
    started = time.time()
    deferred = 0
    try:
        with concurrent.futures.ThreadPoolExecutor(WORKERS) as pool:
            futures = [pool.submit(run_job, *item) for item in items]
            for done, future in enumerate(concurrent.futures.as_completed(futures), start=1):
                name, label = future.result()
                deferred += label.startswith("deferred") or label == "log-exists-pending"
                print(f"[{time.time() - started:7.0f}s] {name:<34} {label:<22} ({done}/{len(items)})", flush=True)
    finally:
        run_pilot.keep_awake(False)
    return 3 if deferred else 0


if __name__ == "__main__":
    raise SystemExit(main())
