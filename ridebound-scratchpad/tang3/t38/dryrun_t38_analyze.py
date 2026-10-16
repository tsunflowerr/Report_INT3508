"""Dry run of t38_analyze.py on task B outputs (8 cells 07:00-09:00, arms U, C-30, Mplus-30, Mplus-60, V-30 exist there),
with a made-up gamma of 150 s, only to exercise every code path before the real test runs. Not a result.
Usage: python -B dryrun_t38_analyze.py <out-prefix-in-a-temp-folder>
"""
from __future__ import annotations

import json
import pathlib
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / "w07"))

import run_t38  # noqa: E402
import run_w07  # noqa: E402
import t38_analyze  # noqa: E402
import w07x_analyze  # noqa: E402

prefix = sys.argv[1]
policy = w07x_analyze.policy_hash(run_w07.OUT_ROOT / f"C-30-{run_w07.CELLS[0]}" / "transcript-00.ndjson")
gamma = pathlib.Path(tempfile.mkdtemp()) / "GAMMA.json"
gamma.write_text(json.dumps({"betaMs": 30000, "gammaMs": 150000, "infinite": False, "n": 15, "k": 15,
                             "reason": "dry run", "policyConfigurationHash": policy}), encoding="utf-8")
run_t38.OUT_ROOT, run_t38.state_of, run_t38.LOG_ROOT = run_w07.OUT_ROOT, run_w07.state_of, run_w07.LOG_ROOT
run_t38.world_file, run_t38.window_start, run_t38.GAMMA_FILE = run_w07.world_file, (lambda cell: 25200), gamma
t38_analyze.TEST, t38_analyze.CALIBRATION = run_w07.CELLS, ()
sys.argv = ["t38_analyze.py", prefix]
raise SystemExit(t38_analyze.main())
