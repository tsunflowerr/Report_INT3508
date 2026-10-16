"""Per-rider decision-induced drop change C (sum of |c|) for chosen pilot jobs (read-only).

Checks the defense statement "each rider's decision-caused drop-time change stays <= beta" on the
real pilot data, and reports how much traffic moved the same riders (X), for contrast.
Usage: python -B per_rider_c.py <jobName> [<jobName> ...]
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "evidence"))
import audit_vep  # noqa: E402
from run_pilot import OUT_ROOT  # noqa: E402

for name in sys.argv[1:]:
    table, summary = audit_vep.audit(OUT_ROOT / name / "transcript-00.ndjson")
    kinds = sorted({row[3] for row in table})
    c, x, pickup_c = {}, {}, {}
    for request, coordinate, _, kind, _, _, _, _, xv, cv, _, closed in table:
        if kind == "initialPromise" or closed:
            continue
        if coordinate == "pickup":
            pickup_c[request] = pickup_c.get(request, 0) + abs(cv)
            continue
        c[request] = c.get(request, 0) + abs(cv)
        x[request] = x.get(request, 0) + abs(xv)
    riders = len({row[0] for row in table if row[1] == "drop"})
    over60 = sum(1 for value in x.values() if value > 60_000)
    print(f"{name}: kinds={kinds} riders={riders} maxDropC={max(c.values(), default=0) / 1000:.1f}s "
          f"ridersC>0={sum(1 for v in c.values() if v > 0)} maxPickupC="
          f"{max(pickup_c.values(), default=0) / 1000:.1f}s maxX={max(x.values(), default=0) / 1000:.1f}s "
          f"ridersX>60s={over60} forced={(summary.get('breaches') or {}).get('forcedReference', 0)}")
