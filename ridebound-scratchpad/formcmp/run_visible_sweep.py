"""Beta sweep for the customer-visible guarantee basis.

At beta = 30 s the visible basis is infeasible on 4 of 20 cells: every candidate
for some vehicle is rejected, including the no-op, because exogenous drift alone
consumes the budget. This sweep finds the beta at which the visible basis becomes
satisfiable again, and what it then costs in service.

Only the four cells that failed are swept, because those are the ones that decide
the threshold. Once a feasible beta is known the full 20-cell panel is run at it.

Nothing is written into the repository.
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
BASE_COMMITMENT = REPO / "benchmarks/configurations/wp8-drop-eta-budget-tight-v1.json"
WP4 = REPO / "benchmarks/configurations/wp9-fleetpy-ridebound-hard-vector-audited-v1.json"
OUT_ROOT = pathlib.Path(r"E:/RideBoundData/wp9/exploratory-visible-sweep-v1")

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

# The four cells on which the visible basis had no feasible plan at beta = 30 s.
FAILING = [
    "d20181116-s10-r2",
    "d20181116-s10-r4",
    "d20181117-s10-r1",
    "d20181117-s10-r3",
]
ALL_CELLS = [
    f"d201811{day}-s10-r{rep}"
    for day in (14, 15, 16, 17, 18)
    for rep in (1, 2, 3, 4)
]


def commitment_config(beta_ms):
    """Write (once) a customer-visible commitment policy with the given budget."""
    path = HERE / f"commit-visible-{beta_ms}.json"
    if path.exists():
        return path
    data = json.loads(BASE_COMMITMENT.read_text(encoding="utf-8"))
    policy = data["policies"][0]
    assert policy["budgetBasis"] == "decisionInduced"
    policy["budgetBasis"] = "customerVisible"
    found = False
    for limit in policy["limits"]:
        if limit["dimension"] == "drop_eta_total_ms":
            assert limit["hardLimit"] == 30000
            limit["hardLimit"] = beta_ms
            found = True
    if not found:
        raise RuntimeError("drop_eta_total_ms limit not found")
    path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8", newline="\n",
    )
    return path


def sealed_accepted(cell, arm):
    path = SEALED / f"p-{cell}-{arm}-tight-s7" / "run-00.json"
    if not path.exists():
        return None
    return len(
        json.loads(path.read_text(encoding="utf-8"))["semantic"]["acceptedRequestIds"]
    )


def run_cell(cell, beta_ms):
    label = f"s-{cell}-visible{beta_ms}-s7"
    output = OUT_ROOT / label
    if (output / "summary.json").exists():
        return cell, beta_ms, "reused", accepted_of(output)
    if output.exists():
        return cell, beta_ms, "blocked", None

    fixture = FIXTURE_ROOT / cell
    command = [
        str(PYTHON), "-B", str(PREFLIGHT),
        "--label", label,
        "--fleetpy-root", str(FLEETPY),
        "--runner-root", str(RUNNER),
        "--dotnet", str(DOTNET),
        "--commitment-config", str(commitment_config(beta_ms)),
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
        reason = "infeasible" if "rejected every generated candidate" in text \
            else f"failed({completed.returncode})"
        return cell, beta_ms, reason, None
    return cell, beta_ms, "ok", accepted_of(output)


def accepted_of(output):
    run = json.loads((output / "run-00.json").read_text(encoding="utf-8"))
    return len(run["semantic"]["acceptedRequestIds"])


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "sweep"
    parallelism = 4
    OUT_ROOT.mkdir(parents=True, exist_ok=True)

    if mode == "sweep":
        betas = [60000, 120000, 300000, 600000]
        cells = FAILING
    else:
        betas = [int(mode)]
        cells = ALL_CELLS

    jobs = [(cell, beta) for beta in betas for cell in cells]
    results = {}
    with concurrent.futures.ThreadPoolExecutor(parallelism) as pool:
        futures = [pool.submit(run_cell, cell, beta) for cell, beta in jobs]
        for future in concurrent.futures.as_completed(futures):
            cell, beta, status, accepted = future.result()
            results[(cell, beta)] = (status, accepted)
            print(f"beta={beta // 1000:>4}s  {cell:<22} {status:<14} "
                  f"accepted={accepted}", flush=True)

    print()
    header = f"{'cell':<22}{'B1':>5}{'C1(D)':>7}" + "".join(
        f"{'V@' + str(b // 1000) + 's':>12}" for b in betas
    )
    print(header)
    print("-" * len(header))
    for cell in cells:
        line = (f"{cell:<22}{sealed_accepted(cell, 'b1') or '-':>5}"
                f"{sealed_accepted(cell, 'c1') or '-':>7}")
        for beta in betas:
            status, accepted = results.get((cell, beta), ("missing", None))
            line += f"{(accepted if accepted is not None else status):>12}"
        print(line)
    print("-" * len(header))

    for beta in betas:
        oks = [results.get((c, beta), ("", None))[1] for c in cells]
        if all(v is not None for v in oks):
            print(f"beta = {beta // 1000}s : feasible on all {len(cells)} cells, "
                  f"total accepted = {sum(oks)}")
        else:
            bad = sum(1 for v in oks if v is None)
            print(f"beta = {beta // 1000}s : INFEASIBLE on {bad}/{len(cells)} cells")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
