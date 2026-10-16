"""Task w07x driver (plan: W07X-PLAN.md, sealed in W07X-PLAN.sha256 and pushed before any job).

The 07:00-09:00 real-traffic cells of task B, at promise levels between the ones already run:
  arms C-<x>, Mplus-<x> for x in 90, 150, 180, 240 s and V-<x> for x in 90, 120, 150, 180, 240 s
  = 13 arms x 8 cells = 104 jobs. Configs from ./configs (make_configs_w07x.log).
Everything else is exactly task B's command (../w07/run_w07.command): world wrapper v1.2, the measured day of the
cell, recovery rule (b) (runner-tier3-v2 + wp4-tier3-v2), fixtures and drivers outside every repository, cwd
E:/Code/RideBound-deadline (never modified), --expected-repository-inventory-sha256. Only --label, --output and
--commitment-config change. C-120, Mplus-120, C-300, Mplus-300 and U are NOT rerun: task B ran them with configs
byte-identical to the regeneration in make_configs_w07x.log.

Safety as run_w07.py, plus: when the power reading is not AC, a job waits (re-checking every 30 s, up to 20 min)
before it is deferred, so that one bad reading no longer defers every remaining job (task B amendment A1).
Usage: python -B run_w07x.py plan | run | report
"""
from __future__ import annotations

import concurrent.futures
import hashlib
import json
import os
import pathlib
import subprocess
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
TANG3 = HERE.parent
sys.path.insert(0, str(TANG3 / "pilot"))
sys.path.insert(0, str(TANG3 / "w07"))

import run_pilot  # noqa: E402
import run_w07  # noqa: E402

ARMS = tuple(f"{family}-{x}" for x in (90, 150, 180, 240) for family in ("C", "Mplus")) + tuple(
    f"V-{x}" for x in (90, 120, 150, 180, 240))
CELLS = run_w07.CELLS
CONFIGS = HERE / "configs"
OUT_ROOT = pathlib.Path(r"C:/RideBoundData/research/tier3-w07x-v1")
LOG_ROOT = HERE / "logs"
STOP_FILE = HERE / "STOP"
POWER_WAIT_S = 1200
CONFIG_SHA256 = {  # make_configs_w07x.log
    "C-90": "bdd10e7faf1ebae2ff01048b156897a9effe89c423dfa78cd78a3251d3b5e9ec",
    "Mplus-90": "6c4f8f3bb7b38dcf38cd28dade0a537bad44ac79f6341b30f7f8edac38e01d29",
    "C-150": "964199b33365e61c1929a9757be8bd3a4b839e59c58425f4d3bb1c0bce2cae37",
    "Mplus-150": "e86b108731fb7f9bd1ced47b70e1b99d9e27584396586dc30270acfe31b689dc",
    "C-180": "2966555d99b9fb21184244e39c5d23d21b813564c2411cbe5f0b7483442c701c",
    "Mplus-180": "5bb12faad7f864a2e0ede8527970c87fe8976c9c9ee4df0753fa2be198a16736",
    "C-240": "4f27e5a69bee314552bd82fcdd84ae2194ba5c306cae9bdaa0483b4b0acc3c0e",
    "Mplus-240": "120592b9ae52b07156fb4e99aefe8ff19fa2dc286ce96b7119fdf03abb1e5242",
    "V-90": "490ea2bd61aa08adfa885d444994b04308bcc4d449cb9210bfcfc0566aba16ab",
    "V-120": "c8279056943dadd31c9e1e5e7a3b510ec13221931f0e51c1ea8c8e30f3fdc7fe",
    "V-150": "f4580d18b2f18ea7cdf540afd450ab796dad834e1d51284f13600896e095d935",
    "V-180": "8778cd80219318b88ad2471171a508a8e0c804aef9c5f8d04e8ee28f17dc21a4",
    "V-240": "f5f24511460d12ec8ceb4d23677de0ad4127869646769f961275d10e844efcf4",
}


def jobs():
    for cell in CELLS:
        for arm in ARMS:
            yield f"{arm}-{cell}", arm, cell


def state_of(name: str) -> str:
    output = OUT_ROOT / name
    if not output.exists():
        return "pending"
    summary = output / "summary.json"
    if summary.exists():
        return "status-" + json.loads(summary.read_text(encoding="utf-8")).get("status", "unknown")
    return "exists-no-summary"


def command(name: str, arm: str, cell: str) -> list[str]:
    base = run_w07.command(name, arm, cell)     # task B: v1.2 wrapper, runner v2, WP4 v2, fixtures, driver, inventory
    base[base.index("--label") + 1] = f"{name}-w07x"
    base[base.index("--output") + 1] = str(OUT_ROOT / name)
    base[base.index("--commitment-config") + 1] = str(CONFIGS / f"{arm}.json")
    return base


def wait_for_power() -> bool:
    deadline = time.time() + POWER_WAIT_S
    while not run_pilot.may_start_job():
        if time.time() > deadline or STOP_FILE.exists():
            return False
        time.sleep(30)
    return True


def run_job(name, arm, cell):
    if state_of(name) != "pending":
        return name, state_of(name)
    log = LOG_ROOT / f"{name}.log"
    if log.exists():
        return name, "log-exists-pending"
    if STOP_FILE.exists():
        return name, "deferred-stop"
    if not wait_for_power():
        return name, "deferred-on-battery"
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONIOENCODING="utf-8",
               RB_WORLD_CONFIG=str(run_w07.world_file(cell)))
    started = time.time()
    completed = subprocess.run(command(name, arm, cell), cwd=str(run_pilot.REPO), check=False, capture_output=True,
                               text=True, encoding="utf-8", errors="replace", env=env)
    with open(log, "x", encoding="utf-8", newline="\n") as handle:
        handle.write(f"returncode={completed.returncode} seconds={time.time() - started:.0f}\n"
                     + completed.stdout + completed.stderr)
    return name, state_of(name)


def check_inputs() -> list[str]:
    problems = run_w07.check_inputs()           # runner tree, WP4 v2, worlds, fixtures, drivers of task B
    for arm, expected in CONFIG_SHA256.items():
        path = CONFIGS / f"{arm}.json"
        if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            problems.append(f"config {arm} missing or SHA-256 mismatch")
    if set(CONFIG_SHA256) != set(ARMS):
        problems.append("arm list and config list differ")
    return problems


def main() -> int:
    if len(sys.argv) != 2 or sys.argv[1] not in ("plan", "run", "report"):
        print(__doc__)
        return 2
    items = list(jobs())
    if sys.argv[1] in ("plan", "report"):
        for name, *_ in items:
            print(f"{name}\t{state_of(name)}")
        states = [state_of(name) for name, *_ in items]
        print(len(items), {state: states.count(state) for state in sorted(set(states))})
        if sys.argv[1] == "plan":
            print("input problems:", check_inputs() or "none")
            print("example:", " ".join(command(*items[0])))
        return 0
    problems = check_inputs()
    if problems:
        raise SystemExit(f"input problems: {problems}")
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    LOG_ROOT.mkdir(parents=True, exist_ok=True)
    run_pilot.keep_awake(True)
    started = time.time()
    deferred = 0
    try:
        with concurrent.futures.ThreadPoolExecutor(run_pilot.WORKERS) as pool:
            futures = [pool.submit(run_job, *item) for item in items]
            for done, future in enumerate(concurrent.futures.as_completed(futures), start=1):
                name, label = future.result()
                deferred += label.startswith("deferred") or label == "log-exists-pending"
                print(f"[{time.time() - started:7.0f}s] {name:<34} {label:<22} ({done}/{len(items)})", flush=True)
    finally:
        run_pilot.keep_awake(False)
    return 3 if deferred else 0


if __name__ == "__main__":
    raise SystemExit(main())
