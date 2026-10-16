"""Unit tests for holdout_predict.predict and first_exceed. Run: python -B test_predict.py"""
import math

import holdout_predict as hp

failures = []


def check(name, condition):
    if not condition:
        failures.append(name)
        print("FAIL", name)


inf = math.inf
check("no exceedance, completed -> not infeasible",
      hp.predict(inf, inf) == ("not-commitment-infeasible", False))
check("no exceedance, died -> weak window-wall", hp.predict(inf, 5000) == ("window-wall", True))
check("exceed before death -> infeasible", hp.predict(1000, 5000) == ("commitment-infeasible", False))
check("exceed at last frame -> infeasible", hp.predict(5000, 5000) == ("commitment-infeasible", False))
check("exceed after death impossible input -> weak", hp.predict(6000, 5000) == ("window-wall", True))
check("exceed, completed -> infeasible", hp.predict(1000, inf) == ("commitment-infeasible", False))

# first_exceed: strict thresholds, running quantities, first time over all riders.
chains = {
    "a": [(0, 1000), (10, 1030), (20, 1031), (30, 1000)],   # M+ 31 at t=20, V 62 at t=30
    "b": [(0, 5000), (5, 4960)],                            # M 40 at t=5, V 40 at t=5
}
first = hp.first_exceed(chains, 30)
check("M+ strict: 30 not over, 31 at t=20", first["M+"] == 20)
check("M two-sided earliest over riders", first["M"] == 5)
check("V earliest", first["V"] == 5)
first = hp.first_exceed(chains, 100)
check("nothing over 100", first == {"M+": inf, "M": inf, "V": inf})

print(f"{len(failures)} failure(s)")
raise SystemExit(1 if failures else 0)
