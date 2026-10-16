"""Synthetic checks of the cluster inference in forecast_family_a.py. Exits 1 on a failure or wrong count.
Usage: python -B test_family_a_stats.py"""
import importlib.util, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import promise_stretch  # noqa: F401
spec = importlib.util.spec_from_file_location("fa_under_test", HERE / "forecast_family_a.py")
fa = importlib.util.module_from_spec(spec); spec.loader.exec_module(fa)
results = []
def check(name, ok, detail=""):
    results.append(bool(ok)); print(f"{'PASS' if ok else 'FAIL'} {name} {detail}")
const = {f"d20181114-s10-r{r}-w07": -0.05 for r in (1, 2)} | {f"d20181115-s10-r{r}-w08": -0.05 for r in (1, 2, 3)}
p, lo, hi = fa.strat_boot(const)
check("constant differences: point = lo = hi", abs(p + 0.05) < 1e-12 and abs(lo + 0.05) < 1e-12 and abs(hi + 0.05) < 1e-12)
two = {"d20181114-s10-r1-w07": -0.1, "d20181114-s10-r2-w07": -0.1, "d20181116-s10-r1-w07": 0.0,
       "d20181114-s10-r1-w08": 0.2, "d20181116-s10-r2-w08": 0.4}
p, lo, hi = fa.strat_boot(two)
check("point = cell-weighted stratum means", abs(p - ((3 / 5) * (-0.2 / 3) + (2 / 5) * 0.3)) < 1e-12, f"{p}")
check("bootstrap interval brackets the point", lo <= p <= hi, f"[{lo}, {hi}]")
w07_only = {"d20181114-s10-r1-w07": -0.1, "d20181116-s10-r1-w07": 0.0}
p, lo, hi = fa.strat_boot(w07_only)
check("two single-cell clusters: bootstrap range is [-0.1, 0]", abs(lo + 0.1) < 1e-12 and abs(hi) < 1e-12, f"[{lo}, {hi}]")
tp, tlo, thi, df = fa.cluster_t(w07_only)
check("cluster-t two clusters: df 1, half width 12.706 * |a-b|/2", df == 1 and abs((thi - tp) - 12.706 * 0.05) < 1e-9, f"{tlo} {thi}")
tp, tlo, thi, df = fa.cluster_t(const)
check("cluster-t constant: zero width", abs(thi - tlo) < 1e-12 and df == 0)
check("same seed gives the same interval", fa.strat_boot(two) == fa.strat_boot(two))
print(f"{len(results)} checks, {results.count(False)} failure(s)")
raise SystemExit(1 if results.count(False) or len(results) != 7 else 0)
