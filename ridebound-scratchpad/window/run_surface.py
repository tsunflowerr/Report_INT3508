"""The second dimension of the price-of-commitment surface.

WHAT IS ALREADY KNOWN
---------------------
The budget ladder was measured once, at the sealed 600 s pickup window:

    nobudget 1655 | 300 s 1641 | 120 s 1608 | 60 s 1579 | 30 s 1581   (B1 = 1735)

Separately, two points were measured at a 900 s window:

    B1@900 = 1938 | C1@900 (30 s) = 1753

From those two points came the observation that the price of a promise is not a
constant but grows with how much freedom the operator has: -7.13 pp at the tight
window, -8.56 pp at the wide one. Two points is an observation, not a law.

WHAT THIS ADDS
--------------
Running the whole budget ladder at the wide window turns the observation into a
surface: the cost of a promise as a function of BOTH the cap beta and the
operator's freedom. That answers a question the single ladder cannot: given a
level of freedom, where should the cap be set?

Four arms are needed; the fifth point, 30 s, is already measured (C1@900 = 1753).

Same sealed runner, same wp4 config, same drivers, same seed as everything else.
Only two things differ from the sealed table: the fixture's pickup window (900 s
instead of 600 s) and the simulator-side op_max_wait_time that must match it.
Both overrides are the ones already verified in preflight_wide.py.

These runs use a rewritten fixture, so they are NOT comparable to the sealed
table and must never be merged into it.

Nothing is written into the repository.

Usage:  run_surface.py --all | <arm> ...   |   run_surface.py --report
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
FRONTIER = HERE.parent / "frontier"

PREFLIGHT = HERE / "preflight_wide.py"
WINDOW_SECONDS = 900

FIXTURE_ROOT = pathlib.Path(r"E:/RideBoundData/wp14/wide-window-fixture")
DRIVER_ROOT = FIXTURE_ROOT
OUT_ROOT = pathlib.Path(r"E:/RideBoundData/wp14/surface-v1")
WIDE = pathlib.Path(r"E:/RideBoundData/wp14/wide-window-v1")

PYTHON = pathlib.Path(r"E:/RideBoundData/wp7/envs/fleetpy-1.0.2/python.exe")
FLEETPY = pathlib.Path(r"E:/RideBoundData/wp7/FleetPy-1.0.2")
RUNNER = pathlib.Path(r"E:/RideBoundData/wp9/runner/h6-confirmatory-v1")
DOTNET = pathlib.Path(r"C:/Program Files/dotnet/dotnet.exe")

# The budget ladder varies the COMMITMENT config; the selection policy is the
# hard-vector one throughout, exactly as in the 600 s ladder.
WP4 = CONFIGS / "wp9-fleetpy-ridebound-hard-vector-audited-v1.json"
ARMS: dict[str, pathlib.Path] = {
    "nobudget": CONFIGS / "wp14-c1-nobudget-v1.json",
    "budget300": FRONTIER / "commit-budget300.json",
    "budget120": CONFIGS / "wp14-c1-budget120-v1.json",
    "budget60": CONFIGS / "wp14-c1-budget60-v1.json",
}
ORDER = ["nobudget", "budget300", "budget120", "budget60"]

CELLS = [
    f"d201811{day}-s10-r{rep}"
    for day in (14, 15, 16, 17, 18)
    for rep in (1, 2, 3, 4)
]
REQUESTS = 108 * len(CELLS)

# Measured elsewhere, on the same fixture and runner.
B1_900 = 1938
C1_900 = 1753
# The 600 s ladder, for the second row of the surface.
LADDER_600 = {"B1": 1735, "nobudget": 1655, "budget300": 1641,
              "budget120": 1608, "budget60": 1579, "budget30": 1581}


def accepted_of(output: pathlib.Path) -> int:
    run = json.loads((output / "run-00.json").read_text(encoding="utf-8"))
    return len(run["semantic"]["acceptedRequestIds"])


def run_cell(arm: str, cell: str) -> tuple[str, str, str, int | None]:
    job = f"sf-{arm}-{cell}-s7"
    output = OUT_ROOT / job
    if (output / "summary.json").exists():
        return arm, cell, "reused", accepted_of(output)
    if output.exists():
        return arm, cell, "blocked-existing-dir", None

    fixture = FIXTURE_ROOT / cell
    command = [
        str(PYTHON), "-B", str(PREFLIGHT),
        "--label", job,
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
    env["RB_MAX_WAIT_SECONDS"] = str(WINDOW_SECONDS)
    completed = subprocess.run(
        command, cwd=str(REPO), check=False, capture_output=True,
        text=True, encoding="utf-8", errors="replace", env=env,
    )
    (HERE / "logs").mkdir(exist_ok=True)
    (HERE / "logs" / f"{job}.log").write_text(
        completed.stdout + completed.stderr, encoding="utf-8", newline="\n"
    )
    if completed.returncode != 0:
        text = completed.stdout + completed.stderr
        reason = ("infeasible" if "rejected every generated candidate" in text
                  else f"failed({completed.returncode})")
        return arm, cell, reason, None
    return arm, cell, "ok", accepted_of(output)


def served(arm: str) -> tuple[int, int]:
    rows = [accepted_of(OUT_ROOT / f"sf-{arm}-{c}-s7")
            for c in CELLS
            if (OUT_ROOT / f"sf-{arm}-{c}-s7" / "summary.json").exists()]
    return len(rows), sum(rows)


def report() -> None:
    print("MAT CONG GIA CUA CAM KET -- fixture viet lai (900 s), khong tron vao bang niem phong")
    print()
    head = (f"{'tran beta':<12}{'cua so 600 s':>14}{'vs B1@600':>11}"
            f"{'cua so 900 s':>14}{'vs B1@900':>11}")
    print(head)
    print("-" * len(head))

    rows = [
        ("khong tran", LADDER_600["nobudget"], "nobudget"),
        ("300 s", LADDER_600["budget300"], "budget300"),
        ("120 s", LADDER_600["budget120"], "budget120"),
        ("60 s", LADDER_600["budget60"], "budget60"),
        ("30 s", LADDER_600["budget30"], None),
    ]
    for label, v600, arm in rows:
        p600 = 100.0 * (v600 - LADDER_600["B1"]) / REQUESTS
        if arm is None:
            n, v900 = len(CELLS), C1_900
        else:
            n, v900 = served(arm)
        if n == len(CELLS):
            p900 = 100.0 * (v900 - B1_900) / REQUESTS
            print(f"{label:<12}{v600:>14}{p600:>+11.2f}{v900:>14}{p900:>+11.2f}")
        else:
            print(f"{label:<12}{v600:>14}{p600:>+11.2f}{'(' + str(n) + '/20)':>14}")

    print("-" * len(head))
    print(f"B1 (khong hua gi): 600 s -> {LADDER_600['B1']},  900 s -> {B1_900}")
    print()
    done = [a for a in ORDER if served(a)[0] == len(CELLS)]
    if len(done) == len(ORDER):
        print("GIA CUA LOI HUA O HAI MUC TU DO")
        for label, v600, arm in rows:
            v900 = C1_900 if arm is None else served(arm)[1]
            p600 = 100.0 * (v600 - LADDER_600["B1"]) / REQUESTS
            p900 = 100.0 * (v900 - B1_900) / REQUESTS
            print(f"  tran {label:<12} 600 s: {p600:+6.2f} pp   "
                  f"900 s: {p900:+6.2f} pp   chenh {p900 - p600:+6.2f} pp")
        print()
        print("Neu cot chenh am o moi dong -> gia cua lai hua tang theo muc tu do")
        print("tren TOAN BO thang, khong chi o mot diem.")


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
                print(f"[{time.time() - started:7.0f}s] {a:<12}{cell:<22}"
                      f"{status:<14} accepted={accepted}  ({done}/{len(CELLS)})",
                      flush=True)
        print(f"--- arm {arm} complete at {time.time() - started:.0f}s ---", flush=True)
    print()
    report()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
