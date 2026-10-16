"""Arm V of the guarantee-form comparison.

Identical to the sealed H6 panel-A C1 arm in every respect except one key:
    budgetBasis: decisionInduced  ->  customerVisible

decisionInduced charges (proposed - exogenous): the operator's own contribution.
customerVisible charges (proposed - previous): everything the rider sees move,
including drift the operator did not cause.

Nothing is written into the repository. Same runner, same wp4 config, same
fixtures and drivers as the sealed run, so the numbers are directly comparable.
"""

from __future__ import annotations

import concurrent.futures
import json
import os
import pathlib
import subprocess
import sys

REPO = pathlib.Path(r"E:/Code/RideBound")
HERE = pathlib.Path(__file__).resolve().parent
COMMITMENT = HERE / "commit-visible-tight-v1.json"
WP4 = REPO / "benchmarks/configurations/wp9-fleetpy-ridebound-hard-vector-audited-v1.json"
OUT_ROOT = pathlib.Path(r"E:/RideBoundData/wp9/exploratory-visible-basis-v1")

PYTHON = pathlib.Path(r"E:/RideBoundData/wp7/envs/fleetpy-1.0.2/python.exe")
PREFLIGHT = REPO / "simulators/fleetpy-ridebound/actual_fleetpy_medium_preflight.py"
FLEETPY = pathlib.Path(r"E:/RideBoundData/wp7/FleetPy-1.0.2")
RUNNER = pathlib.Path(r"E:/RideBoundData/wp9/runner/h6-confirmatory-v1")
DOTNET = pathlib.Path(r"C:/Program Files/dotnet/dotnet.exe")
FIXTURE_ROOT = REPO / (
    "benchmarks/fixtures/wp6/public/fleetpy-manhattan-v1/"
    "wp9-confirmatory-fixed-panel-v2"
)
DRIVER_ROOT = REPO / "benchmarks/scenarios/wp9-confirmatory"
SEALED = pathlib.Path(r"E:/RideBoundData/wp9/confirmatory-h6-panela-v2")

CELLS = [
    f"d201811{day}-s10-r{rep}"
    for day in (14, 15, 16, 17, 18)
    for rep in (1, 2, 3, 4)
]


def sealed_accepted(cell, arm):
    path = SEALED / f"p-{cell}-{arm}-tight-s7" / "run-00.json"
    if not path.exists():
        return None
    return len(
        json.loads(path.read_text(encoding="utf-8"))["semantic"]["acceptedRequestIds"]
    )


def run_cell(cell):
    label = f"v-{cell}-c1visible-s7"
    output = OUT_ROOT / label
    if (output / "summary.json").exists():
        return cell, "reused", accepted_of(output)
    if output.exists():
        return cell, "blocked-existing-dir", None

    fixture = FIXTURE_ROOT / cell
    command = [
        str(PYTHON), "-B", str(PREFLIGHT),
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
        command, cwd=str(REPO), check=False, capture_output=True,
        text=True, encoding="utf-8", errors="replace", env=env,
    )
    (HERE / "logs").mkdir(exist_ok=True)
    (HERE / "logs" / f"{label}.log").write_text(
        completed.stdout + completed.stderr, encoding="utf-8", newline="\n"
    )
    if completed.returncode != 0:
        return cell, f"failed({completed.returncode})", None
    return cell, "ok", accepted_of(output)


def accepted_of(output):
    run = json.loads((output / "run-00.json").read_text(encoding="utf-8"))
    return len(run["semantic"]["acceptedRequestIds"])


def main():
    parallelism = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    results = {}
    with concurrent.futures.ThreadPoolExecutor(parallelism) as pool:
        futures = [pool.submit(run_cell, cell) for cell in CELLS]
        for future in concurrent.futures.as_completed(futures):
            cell, status, accepted = future.result()
            results[cell] = (status, accepted)
            print(f"{cell:<22} {status:<20} accepted={accepted}", flush=True)

    print()
    header = (f"{'cell':<22}{'B1':>6}{'C1 (Delta)':>12}"
              f"{'C1 (Visible)':>14}{'V-Delta':>10}")
    print(header)
    print("-" * len(header))
    tb = td = tv = 0
    counted = 0
    for cell in CELLS:
        status, visible = results.get(cell, ("missing", None))
        b1 = sealed_accepted(cell, "b1")
        delta = sealed_accepted(cell, "c1")
        gap = "" if (visible is None or delta is None) else f"{visible - delta:+d}"
        print(f"{cell:<22}{b1 if b1 is not None else '-':>6}"
              f"{delta if delta is not None else '-':>12}"
              f"{visible if visible is not None else status:>14}{gap:>10}")
        if None not in (b1, delta, visible):
            tb += b1
            td += delta
            tv += visible
            counted += 1
    print("-" * len(header))
    print(f"{'TOTAL (' + str(counted) + ')':<22}{tb:>6}{td:>12}{tv:>14}"
          f"{tv - td:>+10d}")
    if counted:
        n = counted * 108
        print()
        print(f"B1              : {tb:>5}  ({100.0 * tb / n:.4f}%)")
        print(f"C1  conduct  (D): {td:>5}  ({100.0 * td / n:.4f}%)   "
              f"vs B1 {100.0 * (td - tb) / n:+.4f} pp")
        print(f"C1  visible  (V): {tv:>5}  ({100.0 * tv / n:.4f}%)   "
              f"vs B1 {100.0 * (tv - tb) / n:+.4f} pp")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
