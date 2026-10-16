"""Exact two-sided 95% Clopper-Pearson intervals for the Tier-2 cell proportions (plan §8.2).

Pure Python: the bounds solve P(X >= x | p) = a/2 (lower) and P(X <= x | p) = a/2 (upper) by
bisection on the exact binomial tail, so no SciPy is needed. Self-check: 0/8 -> upper 0.3694,
known closed form 1 - (a/2)^(1/n). Read-only.
"""
import math


def tail_le(x, n, p):
    return sum(math.comb(n, k) * p ** k * (1 - p) ** (n - k) for k in range(x + 1))


def solve(f, target):
    lo, hi = 0.0, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if f(mid) > target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def clopper_pearson(x, n, alpha=0.05):
    lower = 0.0 if x == 0 else solve(lambda p: 1 - (1 - tail_le(x - 1, n, p)), 1 - alpha / 2)
    upper = 1.0 if x == n else solve(lambda p: tail_le(x, n, p), alpha / 2)
    return lower, upper


assert abs(clopper_pearson(0, 8)[1] - (1 - 0.025 ** (1 / 8))) < 1e-9
CASES = [("2A dl-30 k=1", 19, 20), ("2A dl-60 k=1", 13, 20), ("2A dl-120 k=1", 3, 20),
         ("2A V k=1", 19, 20), ("2A dl-* k=0 (60 runs)", 0, 60), ("conduct, all runs", 0, 56),
         ("2B sang dl-30", 4, 8), ("2B sang dl2-30", 4, 8), ("2B sang V", 8, 8),
         ("2B toi dl-30", 0, 8), ("2B toi dl2-30", 7, 8), ("2B toi V", 8, 8)]
for name, x, n in CASES:
    lo, hi = clopper_pearson(x, n)
    print(f"{name:<24} {x:>2}/{n:<2}  95% CI [{lo:.3f}, {hi:.3f}]")
