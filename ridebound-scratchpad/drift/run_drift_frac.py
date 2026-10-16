"""The service-rate comparison of the two bases, at the largest drift that fits.

WHY A FRACTIONAL LEVEL
----------------------
run_drift.py gave a clean FEASIBILITY result (conduct 0 commitment-infeasible at
every level; outcome 4/20 at k=0 and 19/20 at k=1) but no SERVICE result, because
a second wall fires at k=1:

    SCHEMA_VALIDATION_FAILED: Actual pickup time must remain inside the accepted
    pickup window.                                   (RideRequest.cs:266)

That is a domain invariant, not a commitment gate: with travel times 17-26%
slower, a vehicle already en route arrives after the latestPickup the request was
accepted under. It hits both bases equally and it killed 11/20 conduct cells, so
there was no common cell set left to compare rider counts on.

Widening the pickup window does not help -- that was tried and failed 20/20,
because the optimiser plans to the edge of whatever window it is given.

What is left is to find the largest drift the wall tolerates. The wall fires
somewhere strictly between k=0 (no drift, no failures) and k=1 (11/20 failures),
so the usable level is fractional. k=0.5 halves the log-deviation: the day factor
span drops from about 1.17-1.26 to about 1.08-1.12.

ORDER OF WORK
-------------
conduct first, alone. If it survives enough cells, visible is worth running; if
it does not, drop to k=0.25 and retry rather than spending 40 runs on a level
that cannot answer the question. Each arm is 20 runs, roughly 40 minutes.

WHAT THE RESULT MEANS
---------------------
Theorem 3 says the outcome basis never serves more than the conduct basis, for
any beta. On the flat panel that was true but empty (a difference of 0 and 1
rider) because drift was only execution lag. A measurable gap here turns the
theorem from true-but-empty into true-and-measured. A gap of zero at real drift
would be just as informative, and must be reported as such.

These runs inject drift, so they are NOT comparable to the sealed table.

Nothing is written into the repository.

Usage:  run_drift_frac.py --all | <arm> ...   |   run_drift_frac.py --report
        arm names: conduct-k05 visible-k05
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
OUT_ROOT = pathlib.Path(r"E:/RideBoundData/wp14/drift-frac-v1")

PYTHON = pathlib.Path(r"E:/RideBoundData/wp7/envs/fleetpy-1.0.2/python.exe")
FLEETPY = pathlib.Path(r"E:/RideBoundData/wp7/FleetPy-1.0.2")
RUNNER = pathlib.Path(r"E:/RideBoundData/wp9/runner/h6-confirmatory-v1")
DOTNET = pathlib.Path(r"C:/Program Files/dotnet/dotnet.exe")

WP4 = CONFIGS / "wp9-fleetpy-ridebound-hard-vector-audited-v1.json"
BASIS = {
    "conduct": CONFIGS / "wp8-drop-eta-budget-tight-v1.json",
    "visible": HERE / "basis-customer-visible.json",
}

# label -> exponent. The label avoids a dot in directory names.
LEVELS = {"k05": 0.5, "k025": 0.25}
ARMS = ["conduct-k05", "visible-k05"]

CELLS = [
    f"d201811{day}-s10-r{rep}"
    for day in (14, 15, 16, 17, 18)
    for rep in (1, 2, 3, 4)
]


def day_of(cell: str) -> str:
    stamp = cell[1:9]
    return f"{stamp[:4]}-{stamp[4:6]}-{stamp[6:8]}"


def accepted_of(output: pathlib.Path) -> int:
    run = json.loads((output / "run-00.json").read_text(encoding="utf-8"))
    return len(run["semantic"]["acceptedRequestIds"])


def classify(text: str) -> str:
    """Separate the commitment gate from the domain invariant from everything else."""
    if "rejected every generated candidate" in text:
        return "commitment"
    if "Actual pickup time must remain inside" in text:
        return "window-wall"
    return "other"


def run_cell(arm: str, cell: str) -> tuple[str, str, str, int | None]:
    basis, _, label = arm.partition("-")
    exponent = LEVELS[label]
    job = f"df-{arm}-{cell}-s7"
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
    env["RB_DRIFT_EXPONENT"] = str(exponent)
    completed = subprocess.run(
        command, cwd=str(REPO), check=False, capture_output=True,
        text=True, encoding="utf-8", errors="replace", env=env,
    )
    (HERE / "logs").mkdir(exist_ok=True)
    (HERE / "logs" / f"{job}.log").write_text(
        completed.stdout + completed.stderr, encoding="utf-8", newline="\n"
    )
    if completed.returncode != 0:
        return arm, cell, classify(completed.stdout + completed.stderr), None
    return arm, cell, "ok", accepted_of(output)


def survey(arm: str) -> dict:
    """Read every cell of an arm back, classifying the failures by real cause."""
    out = {"ok": [], "commitment": [], "window-wall": [], "other": [], "missing": []}
    for cell in CELLS:
        output = OUT_ROOT / f"df-{arm}-{cell}-s7"
        if (output / "summary.json").exists():
            out["ok"].append(cell)
            continue
        log = HERE / "logs" / f"df-{arm}-{cell}-s7.log"
        if not log.exists():
            out["missing"].append(cell)
            continue
        out[classify(log.read_text(encoding="utf-8", errors="replace"))].append(cell)
    return out


def report() -> None:
    print("FRACTIONAL DRIFT -- injected congestion, NOT comparable to the sealed table")
    print()
    head = (f"{'arm':<16}{'ok':>5}{'cam kết':>9}{'tường':>8}{'khác':>7}"
            f"{'chưa chạy':>11}{'phục vụ':>10}")
    print(head)
    print("-" * len(head))
    tables = {}
    for arm in ARMS:
        s = survey(arm)
        tables[arm] = s
        served = sum(accepted_of(OUT_ROOT / f"df-{arm}-{c}-s7") for c in s["ok"])
        print(f"{arm:<16}{len(s['ok']):>5}{len(s['commitment']):>9}"
              f"{len(s['window-wall']):>8}{len(s['other']):>7}"
              f"{len(s['missing']):>11}{served:>10}")
    print("-" * len(head))
    print("cam kết = tập phương án bị làm rỗng bởi ràng buộc cam kết (Định lý 2)")
    print("tường   = bất biến miền RideRequest.cs:266, đập vào cả hai cơ sở như nhau")

    if all(arm in tables for arm in ARMS):
        common = sorted(set(tables["conduct-k05"]["ok"]) & set(tables["visible-k05"]["ok"]))
        if common:
            a = sum(accepted_of(OUT_ROOT / f"df-conduct-k05-{c}-s7") for c in common)
            b = sum(accepted_of(OUT_ROOT / f"df-visible-k05-{c}-s7") for c in common)
            print()
            print(f"SO SÁNH TRÊN {len(common)} Ô CẢ HAI CƠ SỞ ĐỀU CHẠY ĐƯỢC")
            print(f"  cơ sở hành vi  {a}")
            print(f"  cơ sở kết quả  {b}")
            print(f"  chênh lệch     {a - b:+d}"
                  f"   ({'phù hợp Định lý 3' if a >= b else 'MÂU THUẪN Định lý 3'})")
        else:
            print()
            print("Không có ô nào cả hai cơ sở cùng chạy được -> chưa so được dịch vụ.")


def main() -> int:
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 2
    if args[0] == "--report":
        report()
        return 0

    arms = ARMS if args[0] == "--all" else args
    unknown = [a for a in arms if a.partition("-")[2] not in LEVELS
               or a.partition("-")[0] not in BASIS]
    if unknown:
        print(f"unknown arms: {unknown}")
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
                print(f"[{time.time() - started:7.0f}s] {a:<14}{cell:<22}"
                      f"{status:<16} accepted={accepted}  ({done}/{len(CELLS)})",
                      flush=True)
        print(f"--- arm {arm} complete at {time.time() - started:.0f}s ---", flush=True)
    print()
    report()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
