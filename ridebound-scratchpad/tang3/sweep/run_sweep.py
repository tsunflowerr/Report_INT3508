"""Sweep driver (plan: SWEEP-PLAN.md, sealed in SWEEP-PLAN.sha256 before any job).

13 arms (U; C-x and Mplus-x for x in 30, 60, 120, 300, 600, 900 s) x 6 worlds (the T3.7 world files) x 2
development cells = 156 jobs, each the repository medium preflight inside world v1.1
(../world/preflight_world_v1_1.py), with the Runner published at runner-tier3-v1.

Safety is the T3.7 driver's (imported from ../pilot/run_pilot.py): AC power only (or the owner's battery override),
a STOP file next to this script defers new jobs, an existing output is never touched again, logs use mode "x",
Windows is asked not to idle-sleep. Order: world by world (W0 first), so the no-noise checks come first.

Usage: python -B run_sweep.py plan | run | report
"""
from __future__ import annotations

import concurrent.futures
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

OUT_ROOT = pathlib.Path(r"E:/RideBoundData/research/tier3-sweep-v1")
LOG_ROOT = HERE / "logs"
PREFLIGHT = TANG3 / "world" / "preflight_world_v1_1.py"
STOP_FILE = HERE / "STOP"
LEVELS = (30, 60, 120, 300, 600, 900)
ARMS = ("U",) + tuple(f"{family}-{x}" for x in LEVELS for family in ("C", "Mplus"))
CELLS = run_pilot.CELLS
WORLD_IDS = run_pilot.WORLD_IDS
WORKERS = run_pilot.WORKERS


def jobs():
    for world in WORLD_IDS:
        for cell in CELLS:
            for arm in ARMS:
                yield f"{arm}-{world}-{cell}", arm, world, cell


def state_of(name: str) -> str:
    output = OUT_ROOT / name
    if not output.exists():
        return "pending"
    summary = output / "summary.json"
    if summary.exists():
        return "status-" + json.loads(summary.read_text(encoding="utf-8")).get("status", "unknown")
    return "exists-no-summary"


def effective(name: str) -> str:
    """The output to analyse for a job: its `-rerun1` (SWEEP-AMENDMENTS.md A2) when that finished with a summary."""
    rerun = f"{name}-rerun1"
    return rerun if (OUT_ROOT / rerun / "summary.json").exists() else name


def command(name: str, arm: str, cell: str) -> list[str]:
    base = run_pilot.command(name, arm, cell)
    assert base[2] == str(run_pilot.PREFLIGHT)
    base[2] = str(PREFLIGHT)
    base[base.index("--output") + 1] = str(OUT_ROOT / name)
    return base


def run_job(name, arm, world, cell):
    if state_of(name) != "pending":
        return name, state_of(name)
    if STOP_FILE.exists():
        return name, "deferred-stop"
    if not run_pilot.may_start_job():
        return name, "deferred-on-battery"
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONIOENCODING="utf-8",
               RB_WORLD_CONFIG=str(run_pilot.world_file(world, cell)))
    started = time.time()
    completed = subprocess.run(command(name, arm, cell), cwd=str(run_pilot.REPO), check=False,
                               capture_output=True, text=True, encoding="utf-8", errors="replace", env=env)
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
        print(len(items), {state: states.count(state) for state in sorted(set(states))})
        return 0
    configs = run_pilot.CONFIGS
    missing = [path for path in [run_pilot.RUNNER / "RideBound.Runner.dll", PREFLIGHT, run_pilot.WP4]
               + [configs / f"{arm}.json" for arm in ARMS]
               + [run_pilot.world_file(w, c) for w in WORLD_IDS for c in CELLS]
               + [run_pilot.FIXTURES / c for c in CELLS] if not path.exists()]
    if missing:
        raise SystemExit(f"missing inputs: {missing}")
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
                deferred += label.startswith("deferred")
                print(f"[{time.time() - started:7.0f}s] {name:<44} {label:<22} ({done}/{len(items)})", flush=True)
    finally:
        run_pilot.keep_awake(False)
    return 3 if deferred else 0


if __name__ == "__main__":
    raise SystemExit(main())
