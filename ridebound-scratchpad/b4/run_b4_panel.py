"""Exploratory: run the b4 (no-reassignment-repair) arm over the H6 panel-A cells.

Descriptive only. Nothing is written into the repository: the wp4 config lives in
the scratchpad and the output root is a fresh directory under RideBoundData. The
runner, commitment config, fixtures and drivers are exactly the ones the sealed
H6 panel-A run used, so served counts are directly comparable to b1 and c1.
"""

from __future__ import annotations

import concurrent.futures
import json
import os
import pathlib
import subprocess
import sys

REPO = pathlib.Path(r"E:/Code/RideBound")
SCRATCH = pathlib.Path(
    r"C:/Users/quang/AppData/Local/Temp/claude/e--Code-RideBound"
    r"/c0a62edb-0448-4938-91bf-6a1fb8378ce9/scratchpad/b4"
)
WP4 = SCRATCH / "wp9-fleetpy-no-reassignment-repair-explore-v1.json"
LOGS = SCRATCH / "logs"
OUT_ROOT = pathlib.Path(r"E:/RideBoundData/wp9/exploratory-b4-repair-v1")

PYTHON = pathlib.Path(r"E:/RideBoundData/wp7/envs/fleetpy-1.0.2/python.exe")
PREFLIGHT = REPO / "simulators/fleetpy-ridebound/actual_fleetpy_medium_preflight.py"
FLEETPY = pathlib.Path(r"E:/RideBoundData/wp7/FleetPy-1.0.2")
RUNNER = pathlib.Path(r"E:/RideBoundData/wp9/runner/h6-confirmatory-v1")
DOTNET = pathlib.Path(r"C:/Program Files/dotnet/dotnet.exe")
COMMITMENT = REPO / "benchmarks/configurations/wp8-drop-eta-budget-tight-v1.json"
FIXTURE_ROOT = REPO / (
    "benchmarks/fixtures/wp6/public/fleetpy-manhattan-v1/"
    "wp9-confirmatory-fixed-panel-v2"
)
DRIVER_ROOT = REPO / "benchmarks/scenarios/wp9-confirmatory"

CELLS = [
    f"d201811{day}-s10-r{rep}"
    for day in (14, 15, 16, 17, 18)
    for rep in (1, 2, 3, 4)
]


def job_label(cell):
    return f"x-{cell}-b4-tight-s7"


def run_cell(cell):
    label = job_label(cell)
    output = OUT_ROOT / label
    if (output / "summary.json").exists():
        return cell, "reused", None
    if output.exists():
        return cell, "blocked-existing-dir", None

    fixture = FIXTURE_ROOT / cell
    command = [
        str(PYTHON),
        "-B",
        str(PREFLIGHT),
        "--label", label,
        "--fleetpy-root", str(FLEETPY),
        "--runner-root", str(RUNNER),
        "--dotnet", str(DOTNET),
        "--commitment-config", str(COMMITMENT),
        "--wp4-config", str(WP4),
        "--scenario", str(fixture / "scenario-content.json"),
        "--derivative-manifest", str(fixture / "derivative-manifest.json"),
        "--normalization-report", str(fixture / "normalization-report.json"),
        "--selection-frame", str(fixture / "selection-frame.json"),
        "--driver", str(DRIVER_ROOT / f"{cell}.driver.json"),
        "--output", str(output),
        "--repeats", "1",
        "--master-seed", "7",
    ]
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env["PYTHONIOENCODING"] = "utf-8"
    completed = subprocess.run(
        command,
        cwd=str(REPO),
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        env=env,
    )
    LOGS.mkdir(parents=True, exist_ok=True)
    (LOGS / f"{label}.log").write_text(
        completed.stdout + completed.stderr, encoding="utf-8", newline="\n"
    )
    if completed.returncode != 0:
        return cell, f"failed({completed.returncode})", None
    summary = json.loads((output / "summary.json").read_text(encoding="utf-8"))
    run = json.loads((output / "run-00.json").read_text(encoding="utf-8"))
    accepted = len(run["semantic"]["acceptedRequestIds"])
    return cell, summary["status"], accepted


def main():
    parallelism = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    results = {}
    with concurrent.futures.ThreadPoolExecutor(parallelism) as pool:
        futures = {pool.submit(run_cell, c): c for c in CELLS}
        for future in concurrent.futures.as_completed(futures):
            cell, status, accepted = future.result()
            results[cell] = (status, accepted)
            print(f"{cell:<24} {status:<22} accepted={accepted}", flush=True)

    print()
    print(f"{'cell':<24} {'status':<14} {'b4_accepted':>11}")
    for cell in CELLS:
        status, accepted = results.get(cell, ("missing", None))
        print(f"{cell:<24} {status:<14} {str(accepted):>11}")
    total = sum(a for _, a in results.values() if isinstance(a, int))
    ok = sum(1 for s, _ in results.values() if s == "pass")
    print()
    print(f"pass {ok}/{len(CELLS)}   b4 total accepted = {total}")
    print("baseline (sealed H6 panel A): b1 = 1735   c1 = 1581")


if __name__ == "__main__":
    raise SystemExit(main())
