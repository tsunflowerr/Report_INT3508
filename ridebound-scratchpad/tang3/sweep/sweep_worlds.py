"""Sweep validity checks 1, 3 and 4 of SWEEP-PLAN.md §5 (read-only on the sweep logs and outputs).

Per job: returncode 0; world v1.1 config line with the SHA-256 of the world file on disk; bins 0..k in order;
every bin applied at exactly bin * 900 s; bin 0 = [1, 1]; "bin changes applied" equals the number of bin lines.
Per (world, cell): identical bin -> factor-range sequence on the bins all arms reached, and identical
sourceScenarioContentSha256 across arms. Jobs without a log yet are listed, not counted as failures.
Usage: python -B sweep_worlds.py
"""
import hashlib
import json
import re
import sys

from run_sweep import ARMS, CELLS, LOG_ROOT, OUT_ROOT, WORLD_IDS, effective, run_pilot

sys.path.insert(0, str(run_pilot.TANG3 / "world"))
from world_v1 import BIN_S  # noqa: E402

CONFIG = re.compile(r"^\[world\] version=v1\.1 config=(?P<path>.+?) sha256=(?P<sha>[0-9a-f]{64}) seed=(?P<seed>\d+)$")
BIN = re.compile(r"^\[world\] t=\s*(?P<t>\d+)s bin=(?P<bin>\d+) edges=(?P<edges>\d+) "
                 r"factor=\[(?P<lo>[\d.]+), (?P<hi>[\d.]+)\]$")
APPLIED = re.compile(r"^\[world\] bin changes applied: (?P<n>\d+);")


def main() -> int:
    problems, pending, sequences, scenario = [], [], {}, {}
    checked = 0
    for world in WORLD_IDS:
        for cell in CELLS:
            expected = hashlib.sha256(run_pilot.world_file(world, cell).read_bytes()).hexdigest()
            for arm in ARMS:
                # A job failed by the A2 inventory drift is judged by its `-rerun1`.
                name = effective(f"{arm}-{world}-{cell}")
                log = LOG_ROOT / f"{name}.log"
                if not log.exists():
                    pending.append(name)
                    continue
                checked += 1
                lines = log.read_text(encoding="utf-8", errors="replace").splitlines()
                if not lines or not lines[0].startswith("returncode=0 "):
                    problems.append(f"{name}: {lines[0] if lines else 'empty log'}")
                configs = [m for line in lines if (m := CONFIG.match(line))]
                if len(configs) != 1 or configs[0]["sha"] != expected:
                    problems.append(f"{name}: world v1.1 config line missing or SHA-256 mismatch")
                bins = [(int(m["bin"]), int(m["t"]), m["lo"], m["hi"]) for line in lines if (m := BIN.match(line))]
                if [b[0] for b in bins] != list(range(len(bins))):
                    problems.append(f"{name}: bins not 0..k")
                if any(t != b * BIN_S for b, t, _, _ in bins):
                    problems.append(f"{name}: a bin was not applied at exactly bin * {BIN_S} s")
                if not bins or (bins[0][2], bins[0][3]) != ("1.0000", "1.0000"):
                    problems.append(f"{name}: bin 0 not anchored")
                applied = [int(m["n"]) for line in lines if (m := APPLIED.match(line))]
                if applied != [len(bins)]:
                    problems.append(f"{name}: applied {applied} vs {len(bins)} bin lines")
                sequences.setdefault((world, cell), {})[arm] = [(b, lo, hi) for b, _, lo, hi in bins]
                summary = OUT_ROOT / name / "summary.json"
                if summary.exists():
                    scenario.setdefault((world, cell), {})[arm] = json.loads(
                        summary.read_text(encoding="utf-8")).get("sourceScenarioContentSha256")
    for key, by_arm in sorted(sequences.items()):
        common = min(len(s) for s in by_arm.values())
        if len({tuple(s[:common]) for s in by_arm.values()}) != 1:
            problems.append(f"{key}: factors differ across arms on common bins")
    for key, by_arm in sorted(scenario.items()):
        if len(set(by_arm.values())) != 1:
            problems.append(f"{key}: sourceScenarioContentSha256 differs across arms")
    cells_seen = {cell: {v for (w, c), by in scenario.items() if c == cell for v in by.values()} for cell in CELLS}
    print(f"checked {checked} logs, pending {len(pending)}; scenario hashes per cell: "
          f"{ {c: len(v) for c, v in cells_seen.items()} }")
    print(f"problems: {len(problems)}")
    for problem in problems:
        print("  " + problem)
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
