"""Tier 3 task A driver (plan: VM-PLAN.md, sealed in VM-PLAN.sha256 before any job).

V-30 and M-30 under both recovery rules on world v1.1, to compare with C-30 of the sweep:
  2 arms (V-30, M-30) x 6 worlds (W0-W5) x 2 development cells (w08, w17) x 2 recovery variants = 48 jobs;
  variant a: runner-tier3-v1 + ../configs/wp4-tier3-v1.json (commitmentRecovery forced-reference-v1);
  variant b: runner-tier3-v2 + ../configs/wp4-tier3-v2.json (commitmentRecovery no-worse-than-reference-v1).
Everything else is the sweep's command (../sweep/run_sweep.command): world wrapper v1.1, arm config, fixtures,
driver files, cwd E:/Code/RideBound-deadline (never modified here). Every job also passes
--expected-repository-inventory-sha256 of the sweep, so a job fails before creating its output if the source
tree changed.

Safety as run_sweep.py: AC power only, the STOP file next to this script defers new jobs, an existing output is
never touched again, logs are opened with mode "x" (a pending job whose log already exists is NOT retried; it is
reported as "log-exists-pending" for a person to look at), Windows is asked not to idle-sleep.
Order: world by world, W0 first (the recovery-control jobs), both variants of a (world, cell) next to each other.

Usage: python -B run_vm.py plan | run | report
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
sys.path.insert(0, str(TANG3 / "sweep"))
sys.path.insert(0, str(TANG3 / "pilot"))

import run_sweep  # noqa: E402
from run_sweep import run_pilot  # noqa: E402

ARMS = ("V-30", "M-30")
WORLD_IDS = run_pilot.WORLD_IDS
CELLS = run_pilot.CELLS
VARIANTS = {
    "a": {"out": pathlib.Path(r"C:/RideBoundData/research/tier3-vm-v11-a"),
          "runner": pathlib.Path(r"E:/RideBoundData/research/runner-tier3-v1"),
          "runnerManifest": TANG3 / "runner-tier3-v1.sha256.tsv",
          "wp4": run_pilot.CONFIGS / "wp4-tier3-v1.json"},
    "b": {"out": pathlib.Path(r"C:/RideBoundData/research/tier3-vm-v11-b"),
          "runner": pathlib.Path(r"C:/RideBoundData/research/runner-tier3-v2"),
          "runnerManifest": TANG3 / "runner-tier3-v2.sha256.tsv",
          "wp4": run_pilot.CONFIGS / "wp4-tier3-v2.json"},
}
LOG_ROOT = HERE / "logs"
STOP_FILE = HERE / "STOP"
EXPECTED_INVENTORY = "0da63eaf2b30ab332fba265a6b2b6e5c36b3ee78950cbac6d6267e60f81e4cbe"
# SHA-256 of every input file, as recorded in configs/make_configs_t3.log, configs/make_wp4_v2.log and the sweep.
EXPECTED_SHA256 = {
    run_pilot.CONFIGS / "V-30.json": "2462484ab8d7e61efc36de8dc1cd00054dd258e9ec0276f734e9a01212f005d5",
    run_pilot.CONFIGS / "M-30.json": "34e1f263e612bd7e50650286e51168e517c50561c0a6a9b3ac68224ac8bc6bfd",
    run_pilot.CONFIGS / "wp4-tier3-v1.json": "d132e9d315d514ad2026a47d09136c4fc4b9389bce91b211b3d48aa232e71d5b",
    run_pilot.CONFIGS / "wp4-tier3-v2.json": "66e9b59249d9491d520f3ed592e8c878a0d3b100e39432d5f4b73321617b4518",
    TANG3 / "world" / "preflight_world_v1_1.py": "7df4a458210fbd4a12956489f5786f20bb1bcae734f93000acc1132f4bfe7725",
    TANG3 / "world" / "preflight_world.py": "9467611cd0b691996abb7da16469402b03b9904ea991425d568d005ee43f396d",
    TANG3 / "world" / "world_v1.py": "40830b3419f4a38d48ce7469eabc6915c384084c46842bbf96425ed30c1dc6da",
}
RUNNER_TREES = {"a": "5049f6d390a8be2b482d3f05214cd3103953d7570a852446f7c8bdb94852c5cb",
                "b": "ac251ef32a4865ea3bd3d8d87b4b1bcaccc4462a9b80160b4d205b8d474cff3f"}


def jobs():
    for world in WORLD_IDS:
        for cell in CELLS:
            for arm in ARMS:
                for variant in VARIANTS:
                    yield variant, f"{arm}-{world}-{cell}", arm, world, cell


def state_of(variant: str, name: str) -> str:
    output = VARIANTS[variant]["out"] / name
    if not output.exists():
        return "pending"
    summary = output / "summary.json"
    if summary.exists():
        return "status-" + json.loads(summary.read_text(encoding="utf-8")).get("status", "unknown")
    return "exists-no-summary"


def log_path(variant: str, name: str) -> pathlib.Path:
    return LOG_ROOT / f"{variant}-{name}.log"


def command(variant: str, name: str, arm: str, cell: str) -> list[str]:
    base = run_sweep.command(name, arm, cell)   # v1.1 wrapper, arm config, fixtures, driver, seed 7, 1 repeat
    spec = VARIANTS[variant]
    base[base.index("--label") + 1] = f"{name}-vm{variant}"
    base[base.index("--runner-root") + 1] = str(spec["runner"])
    base[base.index("--wp4-config") + 1] = str(spec["wp4"])
    base[base.index("--output") + 1] = str(spec["out"] / name)
    return base + ["--expected-repository-inventory-sha256", EXPECTED_INVENTORY]


def run_job(variant, name, arm, world, cell):
    if state_of(variant, name) != "pending":
        return variant, name, state_of(variant, name)
    if log_path(variant, name).exists():
        return variant, name, "log-exists-pending"
    if STOP_FILE.exists():
        return variant, name, "deferred-stop"
    if not run_pilot.may_start_job():
        return variant, name, "deferred-on-battery"
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONIOENCODING="utf-8",
               RB_WORLD_CONFIG=str(run_pilot.world_file(world, cell)))
    started = time.time()
    completed = subprocess.run(command(variant, name, arm, cell), cwd=str(run_pilot.REPO), check=False,
                               capture_output=True, text=True, encoding="utf-8", errors="replace", env=env)
    with open(log_path(variant, name), "x", encoding="utf-8", newline="\n") as handle:
        handle.write(f"returncode={completed.returncode} seconds={time.time() - started:.0f}\n"
                     + completed.stdout + completed.stderr)
    return variant, name, state_of(variant, name)


def check_inputs() -> list[str]:
    problems = []
    for path, expected in EXPECTED_SHA256.items():
        if not path.exists():
            problems.append(f"missing {path}")
        elif hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            problems.append(f"SHA-256 mismatch {path}")
    sys.path.insert(0, str(TANG3))
    import runner_manifest
    for variant, spec in VARIANTS.items():
        lines = runner_manifest.body(spec["runner"])
        tree = hashlib.sha256("\n".join(lines).encode("utf-8")).hexdigest()
        if tree != RUNNER_TREES[variant]:
            problems.append(f"runner {variant} tree {tree} != {RUNNER_TREES[variant]}")
    for world in WORLD_IDS:
        for cell in CELLS:
            if not run_pilot.world_file(world, cell).exists():
                problems.append(f"missing world {world} {cell}")
    for cell in CELLS:
        if not (run_pilot.FIXTURES / cell).exists():
            problems.append(f"missing fixture {cell}")
    return problems


def main() -> int:
    if len(sys.argv) != 2 or sys.argv[1] not in ("plan", "run", "report"):
        print(__doc__)
        return 2
    items = list(jobs())
    if sys.argv[1] in ("plan", "report"):
        for variant, name, *_ in items:
            print(f"{variant}\t{name}\t{state_of(variant, name)}")
        states = [state_of(variant, name) for variant, name, *_ in items]
        print(len(items), {state: states.count(state) for state in sorted(set(states))})
        if sys.argv[1] == "plan":
            print("input problems:", check_inputs() or "none")
            print("example command (b):", " ".join(command("b", *items[1][1:3], items[1][4])))
        return 0
    problems = check_inputs()
    if problems:
        raise SystemExit(f"input problems: {problems}")
    for spec in VARIANTS.values():
        spec["out"].mkdir(parents=True, exist_ok=True)
    LOG_ROOT.mkdir(parents=True, exist_ok=True)
    run_pilot.keep_awake(True)
    started = time.time()
    deferred = 0
    try:
        with concurrent.futures.ThreadPoolExecutor(run_sweep.WORKERS) as pool:
            futures = [pool.submit(run_job, *item) for item in items]
            for done, future in enumerate(concurrent.futures.as_completed(futures), start=1):
                variant, name, label = future.result()
                deferred += label.startswith("deferred") or label == "log-exists-pending"
                print(f"[{time.time() - started:7.0f}s] {variant} {name:<36} {label:<22} ({done}/{len(items)})",
                      flush=True)
    finally:
        run_pilot.keep_awake(False)
    return 3 if deferred else 0


if __name__ == "__main__":
    raise SystemExit(main())
