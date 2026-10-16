"""Mutation check for test_display_layer.py: every mutant of display_layer.py / promise_stretch.py must make it fail.
Usage: python -B mutate_display_layer.py
"""
from __future__ import annotations

import os
import pathlib
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
WORLD = HERE.parent / "tang3" / "world"
FILES = {name: (HERE / name).read_text(encoding="utf-8") for name in ("display_layer.py", "promise_stretch.py", "test_display_layer.py")}
MUTANTS = [
    ("display_layer.py", "one-sided floor removed",
     "return max(float(p_ms), ps.stretch(t_ms, p_ms - t_ms, ps.forecast_weight(prof, t_ms)))",
     "return ps.stretch(t_ms, p_ms - t_ms, ps.forecast_weight(prof, t_ms))"),
    ("display_layer.py", "scenario day allowed as causal source", 'days = [d for d in kind if d < day and d != INCIDENT]',
     'days = [d for d in kind if d <= day and d != INCIDENT]'),
    ("display_layer.py", "incident day not excluded", 'days = [d for d in kind if d < day and d != INCIDENT]',
     'days = [d for d in kind if d < day]'),
    ("display_layer.py", "minimum history 1", "MIN_SOURCES = 2", "MIN_SOURCES = 1"),
    ("promise_stretch.py", "growth applied inside the current bin",
     "return lambda b: 1.0 if b == b0 else level(b) / level(b0)", "return lambda b: level(b + 1) / level(b0)"),
    ("promise_stretch.py", "weight applied inversely", "covered = segment / w", "covered = segment * w"),
    ("promise_stretch.py", "hold ignored in forecast weight",
     "level = lambda b: profile[min(b, v13.HOLD_BIN)]  # noqa: E731\n    return lambda b: 1.0",
     "level = lambda b: profile[min(b, v13.HOLD_BIN)] * (1.05 if b > v13.HOLD_BIN else 1.0)  # noqa: E731\n    return lambda b: 1.0"),
    ("promise_stretch.py", "no early exit inside a bin", "        if covered >= remaining:\n", "        if covered >= remaining and b > 10**9:\n"),
]


def main() -> int:
    killed = 0
    for target, name, old, new in MUTANTS:
        source = FILES[target]
        if source.count(old) != 1:
            print(f"BAD MUTANT {name}: pattern count {source.count(old)}")
            return 2
        with tempfile.TemporaryDirectory() as tmp:
            for fname, text in FILES.items():
                (pathlib.Path(tmp) / fname).write_text(source.replace(old, new) if fname == target else text, encoding="utf-8")
            env = dict(os.environ, PYTHONPATH=str(WORLD), PYTHONIOENCODING="utf-8", PYTHONDONTWRITEBYTECODE="1")
            done = subprocess.run([sys.executable, "-B", str(pathlib.Path(tmp) / "test_display_layer.py")], capture_output=True,
                                  text=True, encoding="utf-8", errors="replace", env=env, timeout=600)
        dead = done.returncode != 0
        killed += dead
        last = (done.stdout.strip().splitlines() or [done.stderr.strip().splitlines()[-1] if done.stderr.strip() else "(no output)"])[-1]
        print(f"{'KILLED' if dead else 'SURVIVED'}: {name} -> {last}")
    print(f"{killed}/{len(MUTANTS)} mutants killed")
    return 0 if killed == len(MUTANTS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
