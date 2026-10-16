"""Why do the two rules behave alike on real traffic? Read-only checks.

A. Real factor files: largest relative rise over 60/120-minute windows (any start time) per day, next to the two windows used.
B. C-30 runs (system-caused part <= 30 s): per rider, net exogenous drift sum(x) and A (actual - first promise); shares above 30/60/120 s.
C. Decision structure of C-30 runs: how many decisions offer a real choice, how many change any route.
"""
import base64
import collections
import csv
import json
import pathlib
import statistics
import sys

TANG3 = pathlib.Path(r"E:/Code/Report_INT3508/ridebound-scratchpad/tang3")
for sub in ("evidence", "pilot", "sweep"):
    sys.path.insert(0, str(TANG3 / sub))
import audit_vep  # noqa: E402
import choice_metrics  # noqa: E402
import run_sweep  # noqa: E402
from sweep_analyze import event_times, rider_values  # noqa: E402

ROOT = pathlib.Path(r"E:/RideBoundData/wp6/extracted/sha256/d9/d9e86f33645e5eec287d387f8d63ad41ddf41d4ef648138b65d636482e2c599e/FleetPy_Manhattan/networks/Manhattan_2019_corrected")

print("== A. real factor files (all times of day)")
for day in ("2018-11-12", "2018-11-13", "2018-11-14", "2018-11-15", "2018-11-16", "2018-11-17", "2018-11-18"):
    rows = list(csv.DictReader(open(ROOT / f"{day}_tt_factors.csv")))
    f = [float(r["travel_time_factor"]) for r in rows]
    t = [int(float(r["simulation_time"])) for r in rows]
    out = []
    for span in (4, 8):  # 60 and 120 minutes = 4 and 8 bins
        best = max(((f[i + span] / f[i] - 1), t[i]) for i in range(len(f) - span))
        out.append(f"{span * 15}min max rise {best[0]:+.1%} starting {best[1] // 3600:02d}:{best[1] % 3600 // 60:02d}")
    def window(start, end):
        idx = [i for i in range(len(t)) if start <= t[i] <= end]
        return max(f[i] / f[idx[0]] - 1 for i in idx)
    print(f"{day}: " + " | ".join(out) + f" | used windows: 08-10 peak rise {window(28800, 36000):+.1%}, 17-19 peak rise {window(61200, 68400):+.1%}")

print("\n== B. C-30 runs: exogenous drift per rider vs the M+ deadline (x = 30 / 60 / 120 s)")
print("world cell  riders | share sum(x)>30/60/120 | share A>30/60/120 | median A, max A (s)")
for world in ("W0", "W1", "W2", "W3", "W4", "W5"):
    for cell in ("d20181112-s10-r1-w08", "d20181112-s10-r1-w17"):
        name = run_sweep.effective(f"C-30-{world}-{cell}")
        path = run_sweep.OUT_ROOT / name / "transcript-00.ndjson"
        table, _ = audit_vep.audit(path)
        first, _ = rider_values(table)
        net = collections.defaultdict(float)
        for req, coord, seq, kind, at, v, e, p, x, c, z, closed in table:
            if coord == "drop" and not closed and kind != "initialPromise":
                net[req] += x
        _, alighted = event_times(path)
        done = [r for r in first if r in alighted]
        A = [(alighted[r] - first[r]) / 1000 for r in done]
        X = [net[r] / 1000 for r in done]
        sh = lambda vals, k: sum(1 for a in vals if a > k) / len(vals) if vals else 0  # noqa: E731
        print(f"{world} {cell[-3:]}  {len(done):>3} | {sh(X,30):.3f} {sh(X,60):.3f} {sh(X,120):.3f} | {sh(A,30):.3f} {sh(A,60):.3f} {sh(A,120):.3f} | {statistics.median(A):6.1f} {max(A):6.1f}", flush=True)

print("\n== C. decision structure of C-30 (per job): decisions, with a pending request, offering >=2 options, changing routes")
for world in ("W0", "W2", "W5"):
    for cell in ("d20181112-s10-r1-w08",):
        name = run_sweep.effective(f"C-30-{world}-{cell}")
        path = run_sweep.OUT_ROOT / name / "transcript-00.ndjson"
        cm = choice_metrics.measure(path)
        types = collections.Counter()
        changed = 0
        n = 0
        for payload in choice_metrics.decisions(path):
            n += 1
            kinds = {a.get("decisionType") for a in payload.get("actions", [])}
            types.update(kinds)
        print(f"{world} {cell[-3:]}: decisions {cm['decisionsAcknowledged']}, with pending {cm['decisionsWithPending']}, "
              f"raw choice share {cm['rawChoiceShare']:.3f}, gated choice share {cm['gatedChoiceShare']:.3f}; action types {dict(types)}", flush=True)
