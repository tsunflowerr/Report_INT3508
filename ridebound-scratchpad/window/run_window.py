"""Ceiling test: what does service do when the pickup window stops binding?

Same sealed runner, same wp4 configs, same commitment config, same drivers, same
master seed as the sealed H6 panel-A run. The ONLY thing that differs is the
fixture: latestPickup moves from arrival + 600 s to arrival + 900 s.

Arms are exactly the sealed panel's two:
  b1  rolling-cost      -- no commitment gate at all
  c1  hard-vector       -- 30 s decision-induced drop-ETA budget

The four numbers that matter afterwards:

    B1@600 = 1735   (sealed)        C1@600 = 1581   (sealed)
    B1@900 = ?                      C1@900 = ?

  * C1@900 vs B1@600 is the dominance test. If a certified promise with a
    renegotiated window serves more than no promise with a tight window, the
    trade-off framing is wrong and RideBound wins on both axes at once.
  * B1@900 vs B1@600 is the control: it says what the window alone buys, so the
    promise cost can be separated from the window effect.
  * If B1@900 is barely above B1@600, the fleet -- not the window -- is the
    binding constraint, and the whole direction dies cheaply.

These runs use a rewritten fixture, so they are NOT comparable to the sealed
table and must never be merged into it.

Nothing is written into the repository.

Usage:  run_window.py --all | --smoke | <arm> ...   |   run_window.py --report
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

# Rewritten fixture and its drivers, both outside the repository.
FIXTURE_ROOT = pathlib.Path(r"E:/RideBoundData/wp14/wide-window-fixture")
OUT_ROOT = pathlib.Path(r"E:/RideBoundData/wp14/wide-window-v1")

PYTHON = pathlib.Path(r"E:/RideBoundData/wp7/envs/fleetpy-1.0.2/python.exe")
# Wrapper around the repository preflight that also raises the simulator-side
# op_max_wait_time, which otherwise clamps the widened fixture window back to
# 600 s and trips the round-trip assertion. The repository is not modified.
PREFLIGHT = HERE / "preflight_wide.py"
WINDOW_SECONDS = 900
FLEETPY = pathlib.Path(r"E:/RideBoundData/wp7/FleetPy-1.0.2")
RUNNER = pathlib.Path(r"E:/RideBoundData/wp9/runner/h6-confirmatory-v1")
DOTNET = pathlib.Path(r"C:/Program Files/dotnet/dotnet.exe")
SEALED = pathlib.Path(r"E:/RideBoundData/wp9/confirmatory-h6-panela-v2")

# The panel-A plan names wp8-drop-eta-budget-tight-v1; that file is byte-for-byte
# equivalent to wp14-c1-h6-reference-v1 (diffed: 0 leaves differ), which the
# frontier sweep already reproduced sealed C1 with on this runner.
COMMITMENT = CONFIGS / "wp8-drop-eta-budget-tight-v1.json"

# arm -> wp4 selection-policy config. The plan lists two per arm: the wp13-e1
# "retained" file and the "audited" source it was retained from. The retained
# files target the wp13 runner and make this one exit at the handshake
# (RBWP7_RUNNER_EOF on helloAck), so use the audited sources, which are what the
# frontier sweep ran against this same runner.
ARMS: dict[str, pathlib.Path] = {
    "b1": CONFIGS / "wp9-fleetpy-rolling-cost-audited-v1.json",
    "c1": CONFIGS / "wp9-fleetpy-ridebound-hard-vector-audited-v1.json",
}
ORDER = ["c1", "b1"]

CELLS = [
    f"d201811{day}-s10-r{rep}"
    for day in (14, 15, 16, 17, 18)
    for rep in (1, 2, 3, 4)
]

SEALED_TOTAL = {"b1": 1735, "c1": 1581}


def accepted_of(output: pathlib.Path) -> int:
    run = json.loads((output / "run-00.json").read_text(encoding="utf-8"))
    return len(run["semantic"]["acceptedRequestIds"])


def sealed_accepted(cell: str, arm: str) -> int | None:
    path = SEALED / f"p-{cell}-{arm}-tight-s7" / "run-00.json"
    if not path.exists():
        return None
    return len(
        json.loads(path.read_text(encoding="utf-8"))["semantic"]["acceptedRequestIds"]
    )


def run_cell(arm: str, cell: str) -> tuple[str, str, str, int | None]:
    label = f"ww-{arm}-{cell}-s7"
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
        "--commitment-config", str(COMMITMENT),
        "--wp4-config", str(ARMS[arm]),
        "--scenario", str(fixture / "scenario-content.json"),
        "--derivative-manifest", str(fixture / "derivative-manifest.json"),
        "--normalization-report", str(fixture / "normalization-report.json"),
        "--selection-frame", str(fixture / "selection-frame.json"),
        "--driver", str(FIXTURE_ROOT / f"{cell}.driver.json"),
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
    (HERE / "logs" / f"{label}.log").write_text(
        completed.stdout + completed.stderr, encoding="utf-8", newline="\n"
    )
    if completed.returncode != 0:
        text = completed.stdout + completed.stderr
        reason = ("infeasible" if "rejected every generated candidate" in text
                  else f"failed({completed.returncode})")
        return arm, cell, reason, None
    return arm, cell, "ok", accepted_of(output)


def report() -> None:
    requests = 108 * len(CELLS)
    print("WIDE-WINDOW CEILING TEST -- rewritten fixture (900 s), "
          "NOT comparable to the sealed table")
    print()
    head = (f"{'arm':<16}{'cells':>6}{'served':>8}{'rate %':>9}"
            f"{'sealed@600':>12}{'delta':>8}{'pp':>9}")
    print(head)
    print("-" * len(head))
    rows = {}
    for arm in ORDER:
        got = [accepted_of(OUT_ROOT / f"ww-{arm}-{c}-s7")
               for c in CELLS
               if (OUT_ROOT / f"ww-{arm}-{c}-s7" / "summary.json").exists()]
        if not got:
            continue
        served = sum(got)
        rows[arm] = served
        base = SEALED_TOTAL[arm]
        if len(got) == len(CELLS):
            print(f"{arm + '@900':<16}{len(got):>6}{served:>8}"
                  f"{100.0 * served / requests:>9.4f}{base:>12}"
                  f"{served - base:>+8}{100.0 * (served - base) / requests:>+9.2f}")
        else:
            print(f"{arm + '@900':<16}{len(got):>6}{served:>8}"
                  f"{'partial':>9}{base:>12}")
    print("-" * len(head))
    if len(rows) == 2:
        print()
        print("DOMINANCE TEST")
        c1_900, b1_600 = rows["c1"], SEALED_TOTAL["b1"]
        verdict = ("DOMINATES -- certified promise + wide window beats "
                   "no promise + tight window"
                   if c1_900 > b1_600 else
                   "does not dominate")
        print(f"  C1@900 = {c1_900}   vs   B1@600 = {b1_600}   "
              f"({c1_900 - b1_600:+d})  -> {verdict}")
        print()
        print("WHAT THE WINDOW ALONE BUYS (control)")
        print(f"  B1@600 = {SEALED_TOTAL['b1']}  ->  B1@900 = {rows['b1']}   "
              f"({rows['b1'] - SEALED_TOTAL['b1']:+d} riders, "
              f"{100.0 * (rows['b1'] - SEALED_TOTAL['b1']) / requests:+.2f} pp)")
        print()
        print("PRICE OF THE PROMISE, AT EACH WINDOW")
        print(f"  at 600 s: {SEALED_TOTAL['c1'] - SEALED_TOTAL['b1']:+d} riders "
              f"({100.0 * (SEALED_TOTAL['c1'] - SEALED_TOTAL['b1']) / requests:+.2f} pp)")
        print(f"  at 900 s: {rows['c1'] - rows['b1']:+d} riders "
              f"({100.0 * (rows['c1'] - rows['b1']) / requests:+.2f} pp)")


def main() -> int:
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 2
    if args[0] == "--report":
        report()
        return 0
    if args[0] == "--smoke":
        # One cell, one arm, before committing to the full panel.
        arm, cell, status, accepted = run_cell("c1", CELLS[0])
        print(f"smoke {arm} {cell}: {status} accepted={accepted} "
              f"(sealed@600 was {sealed_accepted(cell, 'c1')})")
        return 0 if status in ("ok", "reused") else 1

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
                print(f"[{time.time() - started:7.0f}s] {a:<6}{cell:<22}"
                      f"{status:<14} accepted={accepted}  ({done}/{len(CELLS)})",
                      flush=True)
        print(f"--- arm {arm} complete at {time.time() - started:.0f}s ---",
              flush=True)
    print()
    report()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
