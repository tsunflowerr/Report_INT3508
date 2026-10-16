"""Read-only: how late, and how arm-dependent, the Tier 2 drift switch times were.

Tier 2 (deadline/preflight_drift_v2.py:110-124) applied each 900 s factor step at the first
`_trigger_and_resolve` at or after the step, exactly like tang3/world/preflight_world.py. This measures, on the
Tier 2 run logs, the lag after the nominal step and the spread of the switch time across families that shared
the same (k, cell, seed). A "-rerunN" log replaces its original (AMENDMENTS A2).
Usage: python -B tier2_switch_lag.py
"""
import pathlib
import re
import statistics

LOGS = pathlib.Path(r"E:/Code/Report_INT3508/ridebound-scratchpad/deadline/logs/runs")
NAME = re.compile(r"^(?P<family>.+?)-(?P<key>k\d+-d2018\d+-.+?)(?P<rerun>-rerun\d+)?\.log$")
SWITCH = re.compile(r"^\[drift\] t=\s*(?P<t>\d+)s factor=(?P<f>[\d.]+)$")
STEP_S = 900

groups = {}
for log in sorted(LOGS.glob("*.log")):
    match = NAME.match(log.name)
    if not match:
        print(f"skip {log.name}")
        continue
    times = [int(m["t"]) for line in log.read_text(encoding="utf-8", errors="replace").splitlines()
             if (m := SWITCH.match(line))]
    by_family = groups.setdefault(match["key"], {})
    if match["rerun"] or match["family"] not in by_family:
        by_family[match["family"]] = times

lags, spreads, worst = [], [], (0, None)
for key, by_family in sorted(groups.items()):
    if len(by_family) < 2:
        continue
    # Many Tier 2 runs stopped early, so compare each step over the families that reached it (>= 2), not only
    # over steps every family reached (a first version did that and covered 76 steps).
    for step in range(1, max(len(t) for t in by_family.values())):
        at = [t[step] for t in by_family.values() if len(t) > step]
        if len(at) < 2:
            continue
        lags.append(max(at) - step * STEP_S)
        spreads.append(max(at) - min(at))
        if spreads[-1] > worst[0]:
            worst = (spreads[-1], f"{key} step {step} families={sorted(by_family)}")
print(f"groups with >=2 families: {sum(1 for g in groups.values() if len(g) >= 2)}; "
      f"step comparisons (>= 2 families reached the step): {len(spreads)}")
print(f"switch lag after nominal step: max {max(lags)}s, median {statistics.median(lags)}s")
print(f"spread across families: max {max(spreads)}s, median {statistics.median(spreads)}s, "
      f"share of steps with spread > 60 s: {sum(1 for s in spreads if s > 60) / len(spreads):.3f}")
print(f"worst: {worst[0]}s at {worst[1]}")

# Per individual switch of every run with a changing schedule (not only groups with >= 2 families).
every = [t[step] - step * STEP_S for by_family in groups.values() for t in by_family.values()
         for step in range(1, len(t))]
runs = sum(1 for by_family in groups.values() for t in by_family.values() if len(t) > 1)
print(f"every switch of every run: runs with >1 switch {runs}, switches {len(every)}, "
      f"lag median {statistics.median(every)}s, max {max(every)}s, "
      f"share > 60 s {sum(1 for value in every if value > 60) / len(every):.3f}")
