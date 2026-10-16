"""Stage 1a driver: stability-first C-120 on the 34 T3.8 test cells (plan: C120-PLAN.md, sealed in C120-PLAN.sha256).

Reuses ../t38/run_t38.py unchanged. Only these module globals are overridden before calling its main():
  PHASES     -> {"c120": (("C-120",), <the 34 test cells of split-t38-v1.json>)}
  CONFIG_SHA256["C-120"] -> SHA-256 of ../configs/C-120.json (checked by run_t38.check_inputs)
  OUT_ROOT   -> C:/RideBoundData/research/tier3-t38c120-v1
  LOG_ROOT, STOP_FILE -> this folder (logs/, STOP)
Runner, WP4 config, world wrapper, fixtures, drivers, seed, cwd and the power/keep-awake safety are run_t38.py's.
Usage: python -B run_t38c120.py plan|run|report c120
"""
import hashlib
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
SEAL = HERE / "C120-PLAN.sha256"
sys.path.insert(0, str(HERE.parent / "t38"))
import run_t38 as t  # noqa: E402

C120_SHA256 = "ac0f97589427919c5175e9cc952849305702ced45313a5a2db88167dff030520"

t.PHASES = {"c120": (("C-120",), tuple(t.SPLIT["test"]))}
t.CONFIG_SHA256["C-120"] = C120_SHA256
t.OUT_ROOT = pathlib.Path(r"C:/RideBoundData/research/tier3-t38c120-v1")
t.LOG_ROOT = HERE / "logs"
t.STOP_FILE = HERE / "STOP"


def sealed() -> bool:
    if not SEAL.exists():
        return False
    expected = SEAL.read_text(encoding="utf-8").split()[0]
    return hashlib.sha256((HERE / "C120-PLAN.md").read_bytes()).hexdigest() == expected


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == "run" and not sealed():
        raise SystemExit("refused: C120-PLAN.md is not sealed (C120-PLAN.sha256 missing or mismatched)")
    raise SystemExit(t.main())
