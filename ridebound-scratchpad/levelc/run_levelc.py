"""Level C of promise-aware candidate generation: deliberate budget reservation.

THE IDEA
--------
Levels A and B of the plan -- rank insertion positions by their budget cost, and
prune branches early with a budget lower bound -- were killed by measurement
before any code was written: 96.0 % of vehicle-decisions have exactly ONE
feasible candidate, the candidate cap never binds (0 of 15,232), and no feasible
candidate is ever omitted. There is nothing to reorder and nothing to prune.

Level C is different. It does not touch the generator at all. It changes which
plan the fleet-wide set-packing ILP prefers, by inserting a warning layer into
the lexicographic objective:

    worst-hard-utilization  >  warning-excess  >  revision  >  cost

A candidate that is still inside the hard cap but already past a lower warning
threshold is demoted. The intended effect is to make the dispatcher spend a
rider's budget reluctantly, keeping headroom for a later request that may need
it -- deliberate reservation instead of first-come-first-spend.

Crucially this lever acts on the ILP over the whole fleet, not within a single
vehicle's candidate list, so the thin-choice-set finding does not neutralise it:
even with one candidate per vehicle, the ILP still chooses which vehicle serves
which request.

WHY THIS PAIRING
----------------
The warning threshold must be BELOW the hard cap; the runner rejects
warningLimit > hardLimit with INVALID_COMMITMENT_WARNING_LIMIT. The audited
soft-hybrid config carries warningLimit = 60 s on drop_eta_total_ms, so it
cannot be paired with the sealed 30 s cap. It pairs with the 120 s cap:

    treatment  soft-hybrid policy  +  wp14-c1-budget120  (warn 60 s, hard 120 s)
    control    hard-vector policy  +  wp14-c1-budget120  (hard 120 s only)

The control is already sealed: frontier-v1/fr-budget120-* served 1608 of 2160.
So only the 20 treatment cells are new. Same runner, fixtures, drivers, seed.

If the warning layer is worth anything, the treatment serves MORE than 1608
while keeping the same hard cap -- a free improvement, no relaxation of the
promise. If it serves the same, the reservation idea has no room to act.

Nothing is written into the repository.

Usage:  run_levelc.py --run | --report
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

OUT_ROOT = pathlib.Path(r"E:/RideBoundData/wp14/levelc-v1")
CONTROL_ROOT = pathlib.Path(r"E:/RideBoundData/wp9/frontier-v1")

WP4 = CONFIGS / "wp9-fleetpy-soft-hard-hybrid-audited-v1.json"
COMMITMENT = CONFIGS / "wp14-c1-budget120-v1.json"

CELLS = [
    f"d201811{day}-s10-r{rep}"
    for day in (14, 15, 16, 17, 18)
    for rep in (1, 2, 3, 4)
]
REQUESTS = 108 * len(CELLS)
B1 = 1735               # no promise at all, sealed
CONTROL = 1608          # hard cap 120 s, no warning layer, sealed


def accepted_of(output: pathlib.Path) -> int:
    run = json.loads((output / "run-00.json").read_text(encoding="utf-8"))
    return len(run["semantic"]["acceptedRequestIds"])


def run_cell(cell: str) -> tuple[str, str, int | None]:
    job = f"lc-{cell}-s7"
    output = OUT_ROOT / job
    if (output / "summary.json").exists():
        return cell, "reused", accepted_of(output)
    if output.exists():
        return cell, "blocked-existing-dir", None

    fixture = FIXTURE_ROOT / cell
    command = [
        str(PYTHON), "-B", str(PREFLIGHT),
        "--label", job,
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
    (HERE / "logs" / f"{job}.log").write_text(
        completed.stdout + completed.stderr, encoding="utf-8", newline="\n"
    )
    if completed.returncode != 0:
        text = completed.stdout + completed.stderr
        if "rejected every generated candidate" in text:
            reason = "infeasible"
        elif "INVALID_COMMITMENT_WARNING_LIMIT" in text:
            reason = "warning-gt-hard"
        else:
            reason = "failed-{}".format(completed.returncode)
        return cell, reason, None
    return cell, "ok", accepted_of(output)


def report() -> None:
    treat: list[int] = []
    control: list[int] = []
    paired: list[str] = []
    missing: list[str] = []
    for cell in CELLS:
        t = OUT_ROOT / "lc-{}-s7".format(cell)
        c = CONTROL_ROOT / "fr-budget120-{}-s7".format(cell)
        if (t / "summary.json").exists() and (c / "summary.json").exists():
            treat.append(accepted_of(t))
            control.append(accepted_of(c))
            paired.append(cell)
        else:
            missing.append(cell)

    print("MUC C -- DAT TRUOC NGAN SACH BANG TANG CANH BAO TRONG HAM MUC TIEU")
    print("Ca hai nhanh dung cung mot tran cung 120 s. Chi khac mot tang muc tieu.")
    print()
    line = "o do duoc: {}/{}".format(len(treat), len(CELLS))
    if missing:
        line += "   thieu: " + ", ".join(missing)
    print(line)
    if not treat:
        return
    print()
    head = "{:<22}{:>11}{:>9}{:>8}".format("o", "doi chung", "muc C", "chenh")
    print(head)
    print("-" * len(head))
    for cell, t, c in zip(paired, treat, control):
        mark = "" if t == c else ("  +" if t > c else "  -")
        print("{:<22}{:>11}{:>9}{:>+8}{}".format(cell, c, t, t - c, mark))
    print("-" * len(head))
    print("{:<22}{:>11}{:>9}{:>+8}".format(
        "TONG", sum(control), sum(treat), sum(treat) - sum(control)))
    print()
    if len(treat) == len(CELLS):
        p_c = 100.0 * (sum(control) - B1) / REQUESTS
        p_t = 100.0 * (sum(treat) - B1) / REQUESTS
        print("gia loi hua so voi B1={}:  doi chung {:+.2f} pp   "
              "muc C {:+.2f} pp   cai thien {:+.2f} pp".format(
                  B1, p_c, p_t, p_t - p_c))
        print()
        changed = sum(1 for t, c in zip(treat, control) if t != c)
        print("so o thay doi: {}/{}".format(changed, len(CELLS)))
        print("Nen nho san nhieu: +-7 khach / +-0,3 pp tren panel 20 o.")
        if abs(sum(treat) - sum(control)) <= 7:
            print("=> chenh lech nam trong san nhieu: tang canh bao khong "
                  "co tac dung do duoc.")


def main() -> int:
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 2
    if args[0] == "--report":
        report()
        return 0

    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    started = time.time()
    done = 0
    with concurrent.futures.ThreadPoolExecutor(6) as pool:
        futures = [pool.submit(run_cell, c) for c in CELLS]
        for future in concurrent.futures.as_completed(futures):
            cell, status, accepted = future.result()
            done += 1
            print("[{:7.0f}s] {:<22}{:<20}accepted={}  ({}/{})".format(
                time.time() - started, cell, status, accepted, done, len(CELLS)),
                flush=True)
    print("--- xong sau {:.0f}s ---".format(time.time() - started), flush=True)
    print()
    report()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
