"""Checks for display_layer.py and promise_stretch.py (no simulation). Exits 1 on a failure or a wrong check count.
Usage: python -B test_display_layer.py
"""
from __future__ import annotations

import importlib.util
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import promise_stretch as ps  # noqa: E402  (imports the world folder, which goes first on sys.path)


def load(name):
    spec = importlib.util.spec_from_file_location(f"{name}_under_test", HERE / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


dl = load("display_layer")
pst = load("promise_stretch")
EXPECTED_CHECKS = 23
results = []


def check(name, ok, detail=""):
    results.append(bool(ok))
    print(f"{'PASS' if ok else 'FAIL'} {name} {detail}")


B = 900_000
flat = (3.0,) * 9
rising = (2.0, 2.2, 2.6, 3.0, 3.1, 3.1, 3.2, 3.3, 3.5)
falling = (3.0, 2.8, 2.5, 2.4, 2.3, 2.2, 2.1, 2.0, 1.9)

# stretch
check("stretch with weight 1 is the identity", pst.stretch(100_000, 1_000_000, lambda b: 1.0) == 1_100_000)
check("stretch inside the current bin is unchanged", pst.stretch(0, 500_000, pst.forecast_weight(rising, 0)) == 500_000)
expected = B + (1_200_000 - B) * (2.2 / 2.0)
check("stretch across one boundary: rest at m1/m0", abs(pst.stretch(0, 1_200_000, pst.forecast_weight(rising, 0)) - expected) < 1e-6)
w2 = pst.forecast_weight(rising, 0)
work = B + (B / (2.2 / 2.0)) + 100_000
exp2 = 2 * B + 100_000 * (2.6 / 2.0)
check("stretch across two boundaries", abs(pst.stretch(0, work, w2) - exp2) < 1e-6)
tw = lambda b: [1.0, 1.1, 1.3][min(b, 2)]  # noqa: E731
check("true-weight style path: integral of 1/w equals the work", abs(pst.stretch(0, B + 1000, tw) - (B + 1100)) < 1e-6)

# display
check("flat profile (g = 1) returns p", dl.display(100_000, 1_800_000, flat) == 1_800_000.0)
check("inactive (no profile) returns p", dl.display(100_000, 1_800_000, None) == 1_800_000.0)
d1 = dl.display(50_000, 1_500_000, rising)
d2 = dl.display(800_000, 1_500_000, rising)
check("within-bin invariance: same p at two times in one bin -> same D", abs(d1 - d2) < 1e-6, f"{d1} {d2}")
check("rising traffic lengthens the promise", d1 > 1_500_000)
check("one-sided floor: falling traffic never shortens", dl.display(0, 1_700_000, falling) == 1_700_000.0)
check("hold: published in bin 9 -> unchanged", dl.display(9 * B + 10_000, 9 * B + 1_500_000, rising) == 9 * B + 1_500_000)
check("hold: published in bin 8, crossing into bin 9 -> unchanged", dl.display(8 * B + 100_000, 9 * B + 300_000, rising) == 9 * B + 300_000)
check("past or current time (p <= t) returns p", dl.display(1_000_000, 900_000, rising) == 900_000.0)

# source-day rules
s = dl.sources
check("causal-no15: 14/11 <- 12,13", s("2018-11-14", "causal-no15") == ("2018-11-12", "2018-11-13"))
check("causal-no15: 15/11 <- 12,13,14", s("2018-11-15", "causal-no15") == ("2018-11-12", "2018-11-13", "2018-11-14"))
check("causal-no15: 16/11 <- 12,13,14 (15 excluded)", s("2018-11-16", "causal-no15") == ("2018-11-12", "2018-11-13", "2018-11-14"))
check("causal-no15: 12/11, 13/11, 17/11, 18/11 inactive",
      all(s(d, "causal-no15") == () for d in ("2018-11-12", "2018-11-13", "2018-11-17", "2018-11-18")))
check("loo-no15: 16/11 <- 12,13,14; 18/11 <- 17", s("2018-11-16", "loo-no15") == ("2018-11-12", "2018-11-13", "2018-11-14")
      and s("2018-11-18", "loo-no15") == ("2018-11-17",))
check("causal-no12: 14/11 inactive, 16/11 <- 13,14", s("2018-11-14", "causal-no12") == () and s("2018-11-16", "causal-no12") == ("2018-11-13", "2018-11-14"))
check("causal-with15: 16/11 <- 12,13,14,15", s("2018-11-16", "causal-with15") == ("2018-11-12", "2018-11-13", "2018-11-14", "2018-11-15"))
check("no rule ever uses the scenario day",
      all(d not in s(d, r) for d in dl.WEEKDAYS + dl.WEEKEND for r in ("causal-no15", "causal-with15", "causal-no12", "loo-no15")))
p14 = dl.profile("2018-11-14", "w07", "causal-no15")
a12, a13 = ps.v13.absolute_profile("2018-11-12", 25200), ps.v13.absolute_profile("2018-11-13", 25200)
check("profile = mean of source days' absolute factors", all(abs(p14[i] - (a12[i] + a13[i]) / 2) < 1e-12 for i in range(9)))
check("inactive day has no profile", dl.profile("2018-11-17", "w08", "causal-no15") is None)

failures = results.count(False)
print(f"{len(results)} checks, {failures} failure(s)")
raise SystemExit(1 if failures or len(results) != EXPECTED_CHECKS else 0)
