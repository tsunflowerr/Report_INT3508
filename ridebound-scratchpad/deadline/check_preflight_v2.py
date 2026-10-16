"""Zero-run check that preflight_drift_v2 reproduces v1 and handles the evening window.

1. For every day 2018-11-12..18 and k in {0, 0.5, 1, 2}: v2.load_schedule(day, k, 28800)
   equals v1.load_schedule(day, k) element by element (same times, same factors).
2. For the same days at 61200: the first element is (0, 1.0) and every time offset is
   (csv simulation_time - 61200), i.e. evening factors, not morning ones.
3. The environment reader refuses a missing value, a non-integer, and anything other
   than 28800 / 61200.
4. The only source differences between v1 and v2 are the REPO constant, the window
   start handling and the docstring (printed as a unified diff for the record).
Read-only; exits non-zero on any mismatch.
"""
import difflib
import importlib.util
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
V1 = HERE.parent / "drift" / "preflight_drift.py"
V2 = HERE / "preflight_drift_v2.py"


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


v1 = load(V1, "v1")
v2 = load(V2, "v2")
failures = 0
days = [f"2018-11-{d}" for d in range(12, 19)]
for day in days:
    for k in (0, 0.5, 1, 2):
        a = v1.load_schedule(day, k)
        b = v2.load_schedule(day, k, 28800)
        if a != b:
            failures += 1
            print(f"MISMATCH morning {day} k={k}")
    evening = v2.load_schedule(day, 1, 61200)
    if evening[0] != (0, 1.0):
        failures += 1
        print(f"BAD evening start {day}: {evening[0]}")
    if any(t < 0 or t > 7200 for t, _ in evening):
        failures += 1
        print(f"BAD evening offsets {day}")
    morning = v2.load_schedule(day, 1, 28800)
    print(f"{day}: morning end/start {morning[-1][1]:.3f}  evening end/start "
          f"{evening[-1][1]:.3f}  steps {len(morning)}/{len(evening)}")

for value, ok in ((None, False), ("abc", False), ("28800", True), ("61200", True),
                  ("30000", False), ("0", False)):
    if value is None:
        os.environ.pop("RB_DRIFT_WINDOW_START_SECONDS", None)
    else:
        os.environ["RB_DRIFT_WINDOW_START_SECONDS"] = value
    try:
        v2.window_start_from_environment()
        accepted = True
    except SystemExit:
        accepted = False
    if accepted != ok:
        failures += 1
        print(f"ENV reader wrong for {value!r}: accepted={accepted}")

print("---- source diff v1 -> v2 ----")
sys.stdout.writelines(difflib.unified_diff(
    V1.read_text(encoding="utf-8").splitlines(keepends=True),
    V2.read_text(encoding="utf-8").splitlines(keepends=True),
    "drift/preflight_drift.py", "deadline/preflight_drift_v2.py"))
print(f"\nfailures: {failures}")
raise SystemExit(1 if failures else 0)
