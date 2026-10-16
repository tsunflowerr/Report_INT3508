"""No-worse recovery runs (SWEEP-AMENDMENTS.md A1), with the Runner built from research/tier3-no-worse.

Jobs, all with ../configs/wp4-tier3-v2.json (commitmentRecovery: no-worse-than-reference-v1) and runner-tier3-v2:
  treatment  every Mplus-x of the sweep with forced breaches > 0 (read from the final sweep jobs table), so no arm
             is picked by its outcome;
  controls   C-30 in W2 and W4 (both cells) and Mplus-900 in W2-w08 and W4-w17, which never had a forced breach:
             no-worse recovery must not change their fleet actions (compared by content, since the WP4 hash differs).
Everything else is the sweep's: preflight wrapper v1.1, worlds, fixtures, arm configs, adapter code in the frozen
worktree. Outputs go to C: (E: must keep >= 40 GB free); labels are `<job>-nw`. Same safety as run_sweep.py.
Usage: python -B run_noworse.py plan|run <sweep-jobs.tsv>
"""
from __future__ import annotations

import concurrent.futures
import csv
import json
import os
import pathlib
import subprocess
import sys
import time

import run_sweep
from run_sweep import run_pilot

OUT_ROOT = pathlib.Path(r"C:/RideBoundData/research/tier3-sweep-noworse-v1")
RUNNER = pathlib.Path(r"C:/RideBoundData/research/runner-tier3-v2")
WP4 = run_pilot.CONFIGS / "wp4-tier3-v2.json"
LOG_ROOT = run_sweep.HERE / "logs-noworse"
CONTROLS = [("C-30", "W2", "d20181112-s10-r1-w08"), ("C-30", "W2", "d20181112-s10-r1-w17"),
            ("C-30", "W4", "d20181112-s10-r1-w08"), ("C-30", "W4", "d20181112-s10-r1-w17"),
            ("Mplus-900", "W2", "d20181112-s10-r1-w08"), ("Mplus-900", "W4", "d20181112-s10-r1-w17")]


def jobs(table: str):
    rows = list(csv.DictReader(open(table, encoding="utf-8"), delimiter="\t"))
    treatment = sorted((r["arm"], r["world"], r["cell"]) for r in rows
                       if r["family"] == "Mplus" and int(r["M5_forcedBreaches"] or 0) > 0)
    return [("treatment", *item) for item in treatment] + [("control", *item) for item in CONTROLS]


def state_of(name: str) -> str:
    output = OUT_ROOT / name
    if not output.exists():
        return "pending"
    summary = output / "summary.json"
    if summary.exists():
        return "status-" + json.loads(summary.read_text(encoding="utf-8")).get("status", "unknown")
    return "exists-no-summary"


def command(job: str, arm: str, cell: str) -> list[str]:
    base = run_sweep.command(job, arm, cell)          # sweep command: v1.1 wrapper, arm config, fixtures
    base[base.index("--label") + 1] = f"{job}-nw"
    base[base.index("--runner-root") + 1] = str(RUNNER)
    base[base.index("--wp4-config") + 1] = str(WP4)
    base[base.index("--output") + 1] = str(OUT_ROOT / job)
    return base


def run_job(kind, arm, world, cell):
    job = f"{arm}-{world}-{cell}"
    if state_of(job) != "pending":
        return job, kind, state_of(job)
    if run_sweep.STOP_FILE.exists():
        return job, kind, "deferred-stop"
    if not run_pilot.may_start_job():
        return job, kind, "deferred-on-battery"
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONIOENCODING="utf-8",
               RB_WORLD_CONFIG=str(run_pilot.world_file(world, cell)))
    started = time.time()
    completed = subprocess.run(command(job, arm, cell), cwd=str(run_pilot.REPO), check=False, capture_output=True,
                               text=True, encoding="utf-8", errors="replace", env=env)
    with open(LOG_ROOT / f"{job}.log", "x", encoding="utf-8", newline="\n") as handle:
        handle.write(f"returncode={completed.returncode} seconds={time.time() - started:.0f}\n"
                     + completed.stdout + completed.stderr)
    return job, kind, state_of(job)


def main() -> int:
    if len(sys.argv) != 3 or sys.argv[1] not in ("plan", "run"):
        print(__doc__)
        return 2
    items = jobs(sys.argv[2])
    print(f"{len(items)} jobs: {sum(1 for i in items if i[0] == 'treatment')} treatment, "
          f"{sum(1 for i in items if i[0] == 'control')} control")
    for kind, arm, world, cell in items:
        print(f"  {kind:<9} {arm}-{world}-{cell}\t{state_of(f'{arm}-{world}-{cell}')}")
    if sys.argv[1] == "plan":
        return 0
    missing = [p for p in (RUNNER / "RideBound.Runner.dll", WP4) if not p.exists()]
    if missing:
        raise SystemExit(f"missing inputs: {missing}")
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    LOG_ROOT.mkdir(parents=True, exist_ok=True)
    run_pilot.keep_awake(True)
    started = time.time()
    try:
        with concurrent.futures.ThreadPoolExecutor(run_sweep.WORKERS) as pool:
            futures = [pool.submit(run_job, *item) for item in items]
            for done, future in enumerate(concurrent.futures.as_completed(futures), start=1):
                job, kind, label = future.result()
                print(f"[{time.time() - started:7.0f}s] {kind:<9} {job:<40} {label:<22} ({done}/{len(items)})",
                      flush=True)
    finally:
        run_pilot.keep_awake(False)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
