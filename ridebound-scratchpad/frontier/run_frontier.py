"""Sweep the commitment design space over the sealed H6 panel-A cells.

The sealed evidence gives one point on the price-of-commitment curve: a 30 s
decision-induced drop-ETA budget costs 7.13 pp of service rate. That is the
tightest setting in the family, and reporting it alone is like reporting only
the fully-frozen case in Sridharan, Berry & Udayabhanu (1987): the shape of the
curve, not its endpoint, is the result.

Every arm below is already implemented and configured in the repository; none
had ever been run against the sealed panel. Same runner, same wp4 config, same
fixtures, drivers and seed as the sealed run, so the numbers land on the same
axes as B1 and C1.

Nothing is written into the repository.

Usage:  run_frontier.py <arm> [<arm> ...]   |   run_frontier.py --all
        run_frontier.py --report
"""

from __future__ import annotations

import concurrent.futures
import json
import os
import pathlib
import subprocess
import sys
import time

REPO = pathlib.Path(r"E:/Code/RideBound")
HERE = pathlib.Path(__file__).resolve().parent
CONFIGS = REPO / "benchmarks/configurations"
WP4 = CONFIGS / "wp9-fleetpy-ridebound-hard-vector-audited-v1.json"
OUT_ROOT = pathlib.Path(r"E:/RideBoundData/wp9/frontier-v1")

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

# Arm -> commitment policy configuration. Ordered so that the budget frontier,
# which is the core result, completes before the mechanism comparison.
ARMS: dict[str, pathlib.Path] = {
    "reference": CONFIGS / "wp14-c1-h6-reference-v1.json",
    "nobudget": CONFIGS / "wp14-c1-nobudget-v1.json",
    "budget300": HERE / "commit-budget300.json",
    "budget120": CONFIGS / "wp14-c1-budget120-v1.json",
    "budget60": CONFIGS / "wp14-c1-budget60-v1.json",
    "nopickuplock": CONFIGS / "wp14-c1-nopickuplock-v1.json",
    "freeze300": CONFIGS / "wp14-c1-f1-freeze300-v1.json",
    "freeze600": CONFIGS / "wp14-c1-f1-freeze600-v1.json",
    "ratchet": CONFIGS / "wp14-c1-f2-ratchet-v1.json",
    "freeze300ratchet": CONFIGS / "wp14-c1-f1f2-freeze300-ratchet-v1.json",
}

# Two controlled ladders crossing at the sealed C1 point. The budget ladder
# varies the drop-ETA cap with every lock held fixed; the lock ladder varies how
# the pickup ETA is protected with the drop-ETA cap held at 30 s. nopickuplock
# is the floor of the second ladder and says what the pickup-ETA lock costs at
# all -- without it the other three lock arms have nothing to be measured from.
BUDGET_ORDER = ["nobudget", "budget300", "budget120", "budget60"]
MECHANISM_ORDER = [
    "nopickuplock", "freeze300", "freeze600", "ratchet", "freeze300ratchet",
]


def sealed_accepted(cell: str, arm: str) -> int | None:
    path = SEALED / f"p-{cell}-{arm}-tight-s7" / "run-00.json"
    if not path.exists():
        return None
    return len(
        json.loads(path.read_text(encoding="utf-8"))["semantic"]["acceptedRequestIds"]
    )


def accepted_of(output: pathlib.Path) -> int:
    run = json.loads((output / "run-00.json").read_text(encoding="utf-8"))
    return len(run["semantic"]["acceptedRequestIds"])


def run_cell(arm: str, cell: str) -> tuple[str, str, str, int | None]:
    label = f"fr-{arm}-{cell}-s7"
    output = OUT_ROOT / label
    if (output / "summary.json").exists():
        return arm, cell, "reused", accepted_of(output)
    if output.exists():
        return arm, cell, "blocked-existing-dir", None

    fixture = FIXTURE_ROOT / cell
    command = [
        str(PYTHON), "-B", str(PREFLIGHT),
        "--label", label,
        "--fleetpy-root", str(FLEETPY),
        "--runner-root", str(RUNNER),
        "--dotnet", str(DOTNET),
        "--commitment-config", str(ARMS[arm]),
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
        text = completed.stdout + completed.stderr
        # A hard commitment gate can leave a vehicle with no admissible plan at
        # all. That is a result, not a crash, so it is recorded distinctly.
        reason = ("infeasible" if "rejected every generated candidate" in text
                  else f"failed({completed.returncode})")
        return arm, cell, reason, None
    return arm, cell, "ok", accepted_of(output)


def report() -> None:
    requests = 108 * len(CELLS)
    b1 = sum(sealed_accepted(c, "b1") or 0 for c in CELLS)
    c1 = sum(sealed_accepted(c, "c1") or 0 for c in CELLS)

    print(f"{'arm':<20}{'cells':>7}{'served':>9}{'rate %':>10}"
          f"{'vs B1 pp':>10}{'vs C1':>8}   note")
    print("-" * 78)
    print(f"{'B1 (sealed)':<20}{len(CELLS):>7}{b1:>9}"
          f"{100.0 * b1 / requests:>10.4f}{0.0:>10.4f}{b1 - c1:>+8}")
    print(f"{'C1 (sealed, 30s)':<20}{len(CELLS):>7}{c1:>9}"
          f"{100.0 * c1 / requests:>10.4f}"
          f"{100.0 * (c1 - b1) / requests:>10.4f}{0:>+8}")
    print("-" * 78)

    for arm in list(ARMS):
        rows = []
        bad = []
        for cell in CELLS:
            output = OUT_ROOT / f"fr-{arm}-{cell}-s7"
            if (output / "summary.json").exists():
                rows.append(accepted_of(output))
            elif output.exists():
                bad.append(cell)
        if not rows and not bad:
            continue
        served = sum(rows)
        # Only a complete panel is comparable to the sealed totals.
        if len(rows) == len(CELLS):
            print(f"{arm:<20}{len(rows):>7}{served:>9}"
                  f"{100.0 * served / requests:>10.4f}"
                  f"{100.0 * (served - b1) / requests:>10.4f}"
                  f"{served - c1:>+8}")
        else:
            note = f"partial; {len(bad)} unfinished/failed" if bad else "partial"
            print(f"{arm:<20}{len(rows):>7}{served:>9}{'':>10}{'':>10}{'':>8}   {note}")


def main() -> int:
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 2
    if args[0] == "--report":
        report()
        return 0

    arms = (BUDGET_ORDER + MECHANISM_ORDER) if args[0] == "--all" else args
    unknown = [a for a in arms if a not in ARMS]
    if unknown:
        print(f"unknown arms: {unknown}\nknown: {list(ARMS)}")
        return 2

    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    started = time.time()
    for arm in arms:
        jobs = [(arm, cell) for cell in CELLS]
        done = 0
        with concurrent.futures.ThreadPoolExecutor(6) as pool:
            futures = [pool.submit(run_cell, a, c) for a, c in jobs]
            for future in concurrent.futures.as_completed(futures):
                a, cell, status, accepted = future.result()
                done += 1
                print(f"[{time.time() - started:7.0f}s] {a:<18}{cell:<22}"
                      f"{status:<14} accepted={accepted}  ({done}/{len(jobs)})",
                      flush=True)
        print(f"--- arm {arm} complete at {time.time() - started:.0f}s ---",
              flush=True)
    print()
    report()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
