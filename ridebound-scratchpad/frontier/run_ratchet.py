"""Secondary experiment: the one-sided (ratchet) pickup-ETA guarantee.

The sealed runner (h6-confirmatory-v1, built 2026-08-22, sha256 8445f053...)
predates RatchetLocks, which entered the source on 2026-09-04. It therefore dies
at the handshake when handed a ratchet policy. Running the ratchet arms needs a
newer runner, and a newer runner cannot be compared against the sealed B1/C1
numbers -- different binary, different semantic hashes, and the freeze receipt
would no longer match.

So this is a deliberately separate experiment on its own runner
(ratchet-secondary-v1, sha256 931114e2...). Its numbers must never be merged
into the sealed frontier table.

Two of the four arms exist on both runners. They are the control: if this runner
reproduces the sealed results for reference and nopickuplock, then the ratchet
numbers can be read on the same scale with confidence. If it does not, ratchet
may only be compared against the reference arm measured here.

Nothing is written into the repository.

Usage:  run_ratchet.py --all | <arm> ...   |   run_ratchet.py --report
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

# Separate runner and separate output root, so nothing can be confused with the
# sealed frontier results.
RUNNER = pathlib.Path(r"E:/RideBoundData/wp14/runner/ratchet-secondary-v1")
OUT_ROOT = pathlib.Path(r"E:/RideBoundData/wp14/ratchet-secondary-v1")

PYTHON = pathlib.Path(r"E:/RideBoundData/wp7/envs/fleetpy-1.0.2/python.exe")
PREFLIGHT = REPO / "simulators/fleetpy-ridebound/actual_fleetpy_medium_preflight.py"
FLEETPY = pathlib.Path(r"E:/RideBoundData/wp7/FleetPy-1.0.2")
DOTNET = pathlib.Path(r"C:/Program Files/dotnet/dotnet.exe")
FIXTURE_ROOT = REPO / (
    "benchmarks/fixtures/wp6/public/fleetpy-manhattan-v1/"
    "wp9-confirmatory-fixed-panel-v2"
)
DRIVER_ROOT = REPO / "benchmarks/scenarios/wp9-confirmatory"
SEALED = pathlib.Path(r"E:/RideBoundData/wp9/confirmatory-h6-panela-v2")
FRONTIER = pathlib.Path(r"E:/RideBoundData/wp9/frontier-v1")

CELLS = [
    f"d201811{day}-s10-r{rep}"
    for day in (14, 15, 16, 17, 18)
    for rep in (1, 2, 3, 4)
]

ARMS: dict[str, pathlib.Path] = {
    # Control arms: already measured on the sealed runner.
    "reference": CONFIGS / "wp14-c1-h6-reference-v1.json",
    "nopickuplock": CONFIGS / "wp14-c1-nopickuplock-v1.json",
    # Treatment arms: only runnable here.
    "ratchet": CONFIGS / "wp14-c1-f2-ratchet-v1.json",
    "freeze300ratchet": CONFIGS / "wp14-c1-f1f2-freeze300-ratchet-v1.json",
}
ORDER = ["ratchet", "reference", "nopickuplock", "freeze300ratchet"]

# What each control arm produced on the sealed runner, for the equivalence check.
SEALED_EXPECTATION = {"reference": 1581, "nopickuplock": 1583}


def accepted_of(output: pathlib.Path) -> int:
    run = json.loads((output / "run-00.json").read_text(encoding="utf-8"))
    return len(run["semantic"]["acceptedRequestIds"])


def run_cell(arm: str, cell: str) -> tuple[str, str, str, int | None]:
    label = f"rt-{arm}-{cell}-s7"
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
    (HERE / "logs-ratchet").mkdir(exist_ok=True)
    (HERE / "logs-ratchet" / f"{label}.log").write_text(
        completed.stdout + completed.stderr, encoding="utf-8", newline="\n"
    )
    if completed.returncode != 0:
        text = completed.stdout + completed.stderr
        reason = ("infeasible" if "rejected every generated candidate" in text
                  else f"failed({completed.returncode})")
        return arm, cell, reason, None
    return arm, cell, "ok", accepted_of(output)


def report() -> None:
    print("SECONDARY EXPERIMENT -- new runner 931114e2, NOT comparable to sealed")
    print()
    head = f"{'arm':<20}{'cells':>7}{'served':>9}{'sealed':>9}{'delta':>8}   note"
    print(head)
    print("-" * len(head))
    for arm in ARMS:
        rows = [accepted_of(OUT_ROOT / f"rt-{arm}-{c}-s7")
                for c in CELLS
                if (OUT_ROOT / f"rt-{arm}-{c}-s7" / "summary.json").exists()]
        if not rows:
            continue
        served = sum(rows)
        expected = SEALED_EXPECTATION.get(arm)
        if len(rows) == len(CELLS) and expected is not None:
            delta = served - expected
            note = ("runner reproduces sealed result" if delta == 0
                    else "RUNNER DIFFERS from sealed")
            print(f"{arm:<20}{len(rows):>7}{served:>9}{expected:>9}{delta:>+8}   {note}")
        elif len(rows) == len(CELLS):
            print(f"{arm:<20}{len(rows):>7}{served:>9}{'-':>9}{'':>8}   treatment arm")
        else:
            print(f"{arm:<20}{len(rows):>7}{served:>9}{'-':>9}{'':>8}   partial")


def main() -> int:
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 2
    if args[0] == "--report":
        report()
        return 0
    arms = ORDER if args[0] == "--all" else args
    unknown = [a for a in arms if a not in ARMS]
    if unknown:
        print(f"unknown arms: {unknown}; known {list(ARMS)}")
        return 2

    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    started = time.time()
    for arm in arms:
        done = 0
        with concurrent.futures.ThreadPoolExecutor(6) as pool:
            futures = [pool.submit(run_cell, arm, c) for c in CELLS]
            for future in concurrent.futures.as_completed(futures):
                a, cell, status, accepted = future.result()
                done += 1
                print(f"[{time.time() - started:7.0f}s] {a:<18}{cell:<22}"
                      f"{status:<14} accepted={accepted}  ({done}/{len(CELLS)})",
                      flush=True)
        print(f"--- arm {arm} complete at {time.time() - started:.0f}s ---",
              flush=True)
    print()
    report()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
