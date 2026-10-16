"""Pipeline check before the controls stage: run ONE job into a separate pilot root.

The pilot output is never used as evidence for any Tier-2 claim. It exists so that a broken
pipeline cannot leave 40 failed-recorded directories in the real output root, which the
no-deletion rule would make permanent. Usage: pilot_one.py <stage> <job-name>
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import run_deadline as rd

rd.OUT_ROOT = Path(r"E:/RideBoundData/research/deadline-v1-pilot")
rd.LOG_ROOT = rd.HERE / "logs" / "pilot"


def main() -> int:
    stage, wanted = sys.argv[1], sys.argv[2]
    for item in rd.jobs(stage):
        if item[0] == wanted:
            if not (rd.RUNNER / "RideBound.Runner.dll").exists():
                raise SystemExit(f"runner not published at {rd.RUNNER}")
            rd.OUT_ROOT.mkdir(parents=True, exist_ok=True)
            started = time.time()
            job, label = rd.run_job(*item)
            print(f"{job}\t{label}\t{time.time() - started:.0f}s\t{rd.OUT_ROOT / job}")
            return 0
    raise SystemExit(f"job {wanted!r} not in stage {stage!r}")


if __name__ == "__main__":
    raise SystemExit(main())
