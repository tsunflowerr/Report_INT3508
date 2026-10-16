"""Run the stock-FleetPy baseline over every H6 panel-A cell and tabulate it
against RideBound's sealed B1 and C1 results."""

from __future__ import annotations

import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
PYTHON = pathlib.Path(r"E:/RideBoundData/wp7/envs/fleetpy-1.0.2/python.exe")
REPO = pathlib.Path(r"E:/Code/RideBound")
FLEETPY = pathlib.Path(r"E:/RideBoundData/wp7/FleetPy-1.0.2")
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
    data = json.loads(path.read_text(encoding="utf-8"))
    return len(data["semantic"]["acceptedRequestIds"])


def run_cell(cell, optimizer):
    scenario = f"{cell.replace('-', '_')}_{optimizer}"
    results = FLEETPY / "studies" / "calib" / "results" / scenario
    if (results / "1_user-stats.csv").exists():
        return read_result(results), "reused"
    command = [
        str(PYTHON), "-B", str(HERE / "build_fleetpy_case.py"),
        "--cell", cell, "--optimizer", optimizer,
    ]
    completed = subprocess.run(
        command, cwd=str(REPO), capture_output=True, text=True,
        encoding="utf-8", errors="replace",
        env={**__import__("os").environ,
             "PYTHONIOENCODING": "utf-8", "PYTHONDONTWRITEBYTECODE": "1"},
    )
    (HERE / "logs").mkdir(exist_ok=True)
    (HERE / "logs" / f"{scenario}.log").write_text(
        completed.stdout + completed.stderr, encoding="utf-8", newline="\n"
    )
    if completed.returncode != 0:
        return None, f"failed({completed.returncode})"
    if not (results / "1_user-stats.csv").exists():
        return None, "no-output"
    return read_result(results), "ok"


def read_result(results):
    import csv
    served = 0
    total = 0
    with (results / "1_user-stats.csv").open("r", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            total += 1
            if row.get("operator_id", "") not in ("", "-1", "None"):
                served += 1
    return {"total": total, "served": served}


def main():
    optimizer = sys.argv[1] if len(sys.argv) > 1 else "InsertionHeuristic"
    rows = []
    for cell in CELLS:
        result, status = run_cell(cell, optimizer)
        b1 = sealed_accepted(cell, "b1")
        c1 = sealed_accepted(cell, "c1")
        served = result["served"] if result else None
        rows.append((cell, b1, c1, served, status))
        print(f"{cell:<22} b1={b1} c1={c1} {optimizer}={served} [{status}]",
              flush=True)

    print()
    header = f"{'cell':<22}{'B1':>6}{'C1':>6}{optimizer:>22}{'FleetPy-B1':>12}"
    print(header)
    print("-" * len(header))
    tb = tc = tf = 0
    counted = 0
    for cell, b1, c1, served, status in rows:
        gap = "" if (served is None or b1 is None) else f"{served - b1:+d}"
        print(f"{cell:<22}{b1 if b1 is not None else '-':>6}"
              f"{c1 if c1 is not None else '-':>6}"
              f"{served if served is not None else status:>22}{gap:>12}")
        if served is not None and b1 is not None and c1 is not None:
            tb += b1
            tc += c1
            tf += served
            counted += 1
    print("-" * len(header))
    print(f"{'TOTAL (' + str(counted) + ' cells)':<22}{tb:>6}{tc:>6}{tf:>22}"
          f"{tf - tb:>+12d}")
    if counted:
        print()
        print(f"B1        : {tb} served  ({100.0 * tb / (counted * 108):.4f}%)")
        print(f"C1        : {tc} served  ({100.0 * tc / (counted * 108):.4f}%)")
        print(f"{optimizer:<10}: {tf} served  ({100.0 * tf / (counted * 108):.4f}%)")
        print()
        print(f"B1 - {optimizer} = {tb - tf:+d} riders "
              f"({100.0 * (tb - tf) / (counted * 108):+.4f} pp)")
        print(f"C1 - {optimizer} = {tc - tf:+d} riders "
              f"({100.0 * (tc - tf) / (counted * 108):+.4f} pp)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
