"""Does the conduct/outcome distinction matter once traffic actually drifts?

The prediction, written down BEFORE any of these runs:

  * conduct basis (A) stays feasible on 20/20 cells at EVERY drift level, because
    the no-op has p = e and is charged 0 no matter how large d grows (Theorem 1)
  * outcome basis (B) loses feasible cells as drift grows, because the no-op is
    still charged d (Theorem 2); it already fails 4/20 at d p50 = 4.9 s
  * the served-rider gap A - B widens with d, and with d only -- not with beta
    (Theorem 3 plus B = A + d)

If A ever loses a cell, Theorem 1 is wrong. If the gap does not widen with d,
the theorems are true but operationally empty, and the thesis must say so.

Design: one variable per axis.
  * drift level k in {0, 1, 2}: k=0 is the flat baseline, k=1 the measured
    Manhattan morning peak for that day, k=2 the same deviation doubled
  * basis in {conduct, visible}: the commitment config differs in exactly one
    leaf, budgetBasis (verified by diff)

Everything else -- runner, wp4 config, fixture, drivers, seed -- is the sealed
panel's. The k=0 conduct arm must reproduce sealed C1 = 1581 exactly; if it does
not, the harness changed something and no other number here can be trusted.

These runs inject drift, so they are NOT comparable to the sealed table and must
never be merged into it.

Nothing is written into the repository.

Usage:  run_drift.py --all | --smoke | <arm> ...   |   run_drift.py --report
        arm names: conduct-k0 visible-k0 conduct-k1 visible-k1 ...
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
PREFLIGHT = HERE / "preflight_drift.py"

FIXTURE_ROOT = REPO / (
    "benchmarks/fixtures/wp6/public/fleetpy-manhattan-v1/"
    "wp9-confirmatory-fixed-panel-v2"
)
DRIVER_ROOT = REPO / "benchmarks/scenarios/wp9-confirmatory"
OUT_ROOT = pathlib.Path(r"E:/RideBoundData/wp14/drift-v1")
SEALED = pathlib.Path(r"E:/RideBoundData/wp9/confirmatory-h6-panela-v2")

PYTHON = pathlib.Path(r"E:/RideBoundData/wp7/envs/fleetpy-1.0.2/python.exe")
FLEETPY = pathlib.Path(r"E:/RideBoundData/wp7/FleetPy-1.0.2")
RUNNER = pathlib.Path(r"E:/RideBoundData/wp9/runner/h6-confirmatory-v1")
DOTNET = pathlib.Path(r"C:/Program Files/dotnet/dotnet.exe")

# Basis is a property of the commitment policy, so the wp4 selection config is
# the same hard-vector one for both bases.
WP4 = CONFIGS / "wp9-fleetpy-ridebound-hard-vector-audited-v1.json"
BASIS = {
    "conduct": CONFIGS / "wp8-drop-eta-budget-tight-v1.json",
    "visible": HERE / "basis-customer-visible.json",
}
LEVELS = [0, 1, 2]

CELLS = [
    f"d201811{day}-s10-r{rep}"
    for day in (14, 15, 16, 17, 18)
    for rep in (1, 2, 3, 4)
]

SEALED_CONDUCT_K0 = 1581


def arm_name(basis: str, level: int) -> str:
    return f"{basis}-k{level}"


ARMS = [arm_name(b, k) for k in LEVELS for b in ("conduct", "visible")]


def day_of(cell: str) -> str:
    # d20181114-s10-r1 -> 2018-11-14
    stamp = cell[1:9]
    return f"{stamp[:4]}-{stamp[4:6]}-{stamp[6:8]}"


def accepted_of(output: pathlib.Path) -> int:
    run = json.loads((output / "run-00.json").read_text(encoding="utf-8"))
    return len(run["semantic"]["acceptedRequestIds"])


def run_cell(basis: str, level: int, cell: str) -> tuple[str, str, str, int | None]:
    arm = arm_name(basis, level)
    label = f"dr-{arm}-{cell}-s7"
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
        "--commitment-config", str(BASIS[basis]),
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
    env["RB_DRIFT_DAY"] = day_of(cell)
    env["RB_DRIFT_EXPONENT"] = str(level)
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
        # A basis that charges the no-op can leave a vehicle with no admissible
        # plan. That is the predicted result, not a crash.
        reason = ("infeasible" if "rejected every generated candidate" in text
                  else f"failed({completed.returncode})")
        return arm, cell, reason, None
    return arm, cell, "ok", accepted_of(output)


def collect(arm: str) -> tuple[int, int, int]:
    """(cells finished, riders served, cells attempted-but-not-finished)"""
    served = finished = missing = 0
    for cell in CELLS:
        output = OUT_ROOT / f"dr-{arm}-{cell}-s7"
        if (output / "summary.json").exists():
            finished += 1
            served += accepted_of(output)
        elif output.exists():
            missing += 1
    return finished, served, missing


def report() -> None:
    print("DRIFT LADDER -- real Manhattan congestion, injected. NOT comparable")
    print("to the sealed table.")
    print()
    head = (f"{'level':<7}{'conduct cells':>15}{'conduct served':>16}"
            f"{'visible cells':>15}{'visible served':>16}{'A - B':>8}")
    print(head)
    print("-" * len(head))
    for level in LEVELS:
        a_cells, a_served, _ = collect(arm_name("conduct", level))
        b_cells, b_served, _ = collect(arm_name("visible", level))
        if not a_cells and not b_cells:
            continue
        # Riders are only comparable on cells both bases finished.
        common = [
            cell for cell in CELLS
            if (OUT_ROOT / f"dr-conduct-k{level}-{cell}-s7"
                / "summary.json").exists()
            and (OUT_ROOT / f"dr-visible-k{level}-{cell}-s7"
                 / "summary.json").exists()
        ]
        gap = sum(
            accepted_of(OUT_ROOT / f"dr-conduct-k{level}-{c}-s7")
            - accepted_of(OUT_ROOT / f"dr-visible-k{level}-{c}-s7")
            for c in common
        )
        print(f"k={level:<5}{a_cells:>10}/20{a_served:>16}"
              f"{b_cells:>10}/20{b_served:>16}{gap:>+8}")
    print("-" * len(head))
    print("cells = how many of the 20 produced a run at all; a missing cell is")
    print("a cell where the basis left some vehicle with no admissible plan.")
    print("A - B is summed over cells BOTH bases finished, so it is a pure")
    print("service comparison with feasibility held out.")

    conduct_k0 = collect(arm_name("conduct", 0))
    if conduct_k0[0] == len(CELLS):
        verdict = ("reproduces sealed C1" if conduct_k0[1] == SEALED_CONDUCT_K0
                   else "DIFFERS FROM SEALED -- do not trust the other rows")
        print()
        print(f"control: conduct-k0 served {conduct_k0[1]}, "
              f"sealed C1 = {SEALED_CONDUCT_K0} -> {verdict}")


def main() -> int:
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 2
    if args[0] == "--report":
        report()
        return 0
    if args[0] == "--smoke":
        # Highest drift first: if the mechanism does nothing, it shows here.
        arm, cell, status, accepted = run_cell("conduct", 2, CELLS[0])
        print(f"smoke {arm} {cell}: {status} accepted={accepted}")
        return 0 if status in ("ok", "reused") else 1

    arms = ARMS if args[0] == "--all" else args
    unknown = [a for a in arms if a not in ARMS]
    if unknown:
        print(f"unknown arms: {unknown}; known {ARMS}")
        return 2

    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    started = time.time()
    for arm in arms:
        basis, _, level_text = arm.partition("-k")
        level = int(level_text)
        done = 0
        with concurrent.futures.ThreadPoolExecutor(6) as pool:
            futures = [pool.submit(run_cell, basis, level, c) for c in CELLS]
            for future in concurrent.futures.as_completed(futures):
                a, cell, status, accepted = future.result()
                done += 1
                print(f"[{time.time() - started:7.0f}s] {a:<12}{cell:<22}"
                      f"{status:<14} accepted={accepted}  ({done}/{len(CELLS)})",
                      flush=True)
        print(f"--- arm {arm} complete at {time.time() - started:.0f}s ---",
              flush=True)
    print()
    report()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
