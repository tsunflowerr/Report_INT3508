"""Two end-to-end checks of world wrapper v1.3 on the DEVELOPMENT cell d20181112-s10-r1-w07 (task B), arm C-30:
  control-off : v1.3 with the forecast OFF; must reproduce task B's v1.2 run C-30-d20181112-s10-r1-w07 decision by decision
  smoke-k2    : v1.3 with the forecast ON (horizonBins 2, source days 13-16/11); must pass and log one ratio per snapshot
Everything else is task B's command (run_w07.command): runner v2, WP4 v2, fixture, driver, world file, inventory;
only the wrapper path, --label and --output change, plus RB_FORECAST_CONFIG for the smoke run.
Outputs: C:/RideBoundData/research/tier3-forecast-checks-v1/<name> (never reused); logs ./checks-logs/<name>.log (mode x).
AC power required (run_pilot.may_start_job). No test cell is touched.
Usage: python -B run_v13_checks.py
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
TANG3 = HERE.parent / "tang3"
for sub in ("pilot", "w07"):
    sys.path.insert(0, str(TANG3 / sub))
import run_pilot  # noqa: E402
import run_w07  # noqa: E402

CELL = "d20181112-s10-r1-w07"
WRAPPER = TANG3 / "world" / "preflight_world_v1_3.py"
OUT_ROOT = pathlib.Path(r"C:/RideBoundData/research/tier3-forecast-checks-v1")
LOG_ROOT = HERE / "checks-logs"
FORECAST = HERE / "forecast-check-k2.json"
JOBS = {"control-off": None, "smoke-k2": FORECAST}


def command(name: str) -> list[str]:
    base = run_w07.command(f"C-30-{CELL}", "C-30", CELL)
    base[base.index(str(run_w07.PREFLIGHT))] = str(WRAPPER)
    base[base.index("--label") + 1] = f"C-30-{CELL}-{name}-v13check"
    base[base.index("--output") + 1] = str(OUT_ROOT / name)
    return base


def run(name: str):
    if (OUT_ROOT / name).exists():
        return name, "exists"
    if not run_pilot.may_start_job():
        return name, "deferred-on-battery"
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONIOENCODING="utf-8", RB_WORLD_CONFIG=str(run_w07.world_file(CELL)))
    env.pop("RB_FORECAST_CONFIG", None)
    if JOBS[name]:
        env["RB_FORECAST_CONFIG"] = str(JOBS[name])
    started = time.time()
    done = subprocess.run(command(name), cwd=str(run_pilot.REPO), capture_output=True, text=True, encoding="utf-8",
                          errors="replace", env=env)
    with open(LOG_ROOT / f"{name}.log", "x", encoding="utf-8", newline="\n") as handle:
        handle.write(f"returncode={done.returncode} seconds={time.time() - started:.0f}\n" + done.stdout + done.stderr)
    summary = OUT_ROOT / name / "summary.json"
    return name, json.loads(summary.read_text(encoding="utf-8")).get("status") if summary.exists() else "no-summary"


def main() -> int:
    if not FORECAST.exists():
        with open(FORECAST, "x", encoding="utf-8", newline="\n") as handle:
            json.dump({"forecastVersion": "forecast-v1", "horizonBins": 2,
                       "sourceDays": ["2018-11-13", "2018-11-14", "2018-11-15", "2018-11-16"]}, handle)
            handle.write("\n")
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    LOG_ROOT.mkdir(exist_ok=True)
    run_pilot.keep_awake(True)
    try:
        with concurrent.futures.ThreadPoolExecutor(2) as pool:
            for name, state in pool.map(run, JOBS):
                print(name, state, flush=True)
    finally:
        run_pilot.keep_awake(False)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
