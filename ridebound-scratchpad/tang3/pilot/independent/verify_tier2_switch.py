"""Independent check of the Tier 2 drift switch timing (lag after the nominal 900 s step, spread across families).

Written from scratch; reads only E:/Code/Report_INT3508/ridebound-scratchpad/deadline/logs/runs/*.log.
Imports no author module (tier2_switch_lag.py was read for context only).

Definitions (coordinator brief):
  * log name <family>-<key>[-rerunN].log, key = k<n>-<cell>-s<seed>; a -rerunN log replaces the log of the same
    family and key (highest N wins).
  * switch lines "[drift] t=  <sec>s factor=<f>"; the j-th switch line (0-based) is step j, nominal time j*900 s.
  * (a) over every run with > 1 switch line: switches = lines with step >= 1, lag = t - step*900.
  * (b) group runs by key; for each group with >= 2 families and each step >= 1 reached by >= 2 families,
        spread = max t - min t over the families that reached that step.
Usage: python -B verify_tier2_switch.py [--write]   (--write creates TIER2-RESULT.md with mode "x")
"""
from __future__ import annotations

import collections
import pathlib
import re
import statistics
import sys
import time

RUNS = pathlib.Path(r"E:/Code/Report_INT3508/ridebound-scratchpad/deadline/logs/runs")
HERE = pathlib.Path(__file__).resolve().parent
FAMILIES = ("conduct-30", "visible-30", "dl-30", "dl-60", "dl-120", "dl2-30", "ctl-conduct", "ctl-visible")
STEP_S = 900
SWITCH = re.compile(r"^\[drift\] t=\s*(?P<t>\d+)s factor=(?P<f>\S+)\s*$")
KEY = re.compile(r"^k\d+-d\d{8}-.+-s\d+$")
RERUN = re.compile(r"^(?P<base>.+)-rerun(?P<n>\d+)$")

CLAIM_A = {"runs": 196, "switches": 865, "median": 22, "max": 210, "share>60": "0.147"}
CLAIM_B = {"comparisons": 208, "max": 70, "where": ("k1-d20181114-s10-r1-s7", 4), "median": 0, "share>60": "0.014"}


def split_name(stem):
    """(family, key, rerun N or 0) by longest known-family prefix; None if the name does not fit."""
    rerun = 0
    m = RERUN.match(stem)
    if m:
        stem, rerun = m["base"], int(m["n"])
    for family in sorted(FAMILIES, key=len, reverse=True):
        if stem.startswith(family + "-") and KEY.match(stem[len(family) + 1:]):
            return family, stem[len(family) + 1:], rerun
    return None


def main():
    write = "--write" in sys.argv[1:]
    files = sorted(p for p in RUNS.iterdir() if p.is_file())
    unparsed, non_log = [], [p.name for p in files if p.suffix != ".log"]
    chosen = {}  # (family, key) -> (rerun N, path)
    returncodes = collections.Counter()
    for path in files:
        if path.suffix != ".log":
            continue
        parts = split_name(path.stem)
        if parts is None:
            unparsed.append(path.name)
            continue
        family, key, rerun = parts
        if (family, key) not in chosen or rerun > chosen[(family, key)][0]:
            chosen[(family, key)] = (rerun, path)
    reruns_used = sorted(p.name for n, p in chosen.values() if n > 0)
    reruns_found = sorted(p.name for p in files if RERUN.match(p.stem))

    times = {}
    index_vs_floor = 0
    first_not_zero = 0
    for (family, key), (_, path) in chosen.items():
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        rc = re.match(r"^returncode=(-?\d+)", lines[0]) if lines else None
        returncodes[rc.group(1) if rc else "missing"] += 1
        ts = [int(m["t"]) for line in lines if (m := SWITCH.match(line))]
        times[(family, key)] = ts
        if ts and ts[0] != 0:
            first_not_zero += 1
        if [t // STEP_S for t in ts] != list(range(len(ts))):
            index_vs_floor += 1

    # (a)
    multi = {fk: ts for fk, ts in times.items() if len(ts) > 1}
    lags = [(ts[i] - i * STEP_S, fk, i) for fk, ts in multi.items() for i in range(1, len(ts))]
    lag_values = [x[0] for x in lags]
    a = {"runs": len(multi), "switches": len(lags), "median": statistics.median(lag_values),
         "max": max(lag_values), "above60": sum(1 for v in lag_values if v > 60)}
    a["share>60"] = a["above60"] / a["switches"]
    a_where = sorted(f"{f}-{k} step {i}" for v, (f, k), i in lags if v == a["max"])

    # (b)
    groups = collections.defaultdict(dict)
    for (family, key), ts in times.items():
        groups[key][family] = ts
    comparisons = []  # (spread, key, step, n families reached, max-t lag)
    for key, by_family in sorted(groups.items()):
        if len(by_family) < 2:
            continue
        for step in range(1, max(len(ts) for ts in by_family.values())):
            at = [ts[step] for ts in by_family.values() if len(ts) > step]
            if len(at) >= 2:
                comparisons.append((max(at) - min(at), key, step, len(at), max(at) - step * STEP_S,
                                    len(at) == len(by_family)))
    spreads = [c[0] for c in comparisons]
    b = {"groups>=2": sum(1 for g in groups.values() if len(g) >= 2), "comparisons": len(comparisons),
         "max": max(spreads), "median": statistics.median(spreads), "above60": sum(1 for s in spreads if s > 60)}
    b["share>60"] = b["above60"] / b["comparisons"]
    b_where = sorted((c[1], c[2]) for c in comparisons if c[0] == b["max"])
    # informational variants
    common = [c for c in comparisons if c[5]]          # steps reached by EVERY family of the group
    max_t_lags = [c[4] for c in comparisons]           # lag of the latest family per comparison

    rows = []

    def check(label, claimed, got, ok):
        rows.append(f"- {'MATCH' if ok else 'MISMATCH'}: {label}: claimed `{claimed}`, computed `{got}`")

    check("(a) runs with > 1 switch line", CLAIM_A["runs"], a["runs"], a["runs"] == CLAIM_A["runs"])
    check("(a) switches (step >= 1)", CLAIM_A["switches"], a["switches"], a["switches"] == CLAIM_A["switches"])
    check("(a) median lag (s)", CLAIM_A["median"], a["median"], a["median"] == CLAIM_A["median"])
    check("(a) max lag (s)", CLAIM_A["max"], f"{a['max']} at {', '.join(a_where)}", a["max"] == CLAIM_A["max"])
    check("(a) share of switches with lag > 60 s (3 dp)", CLAIM_A["share>60"],
          f"{a['share>60']:.3f} ({a['above60']}/{a['switches']} = {a['share>60']!r})",
          f"{a['share>60']:.3f}" == CLAIM_A["share>60"])
    check("(b) (group, step) comparisons", CLAIM_B["comparisons"], b["comparisons"],
          b["comparisons"] == CLAIM_B["comparisons"])
    check("(b) max spread (s)", CLAIM_B["max"], b["max"], b["max"] == CLAIM_B["max"])
    check("(b) where the max spread is", f"{CLAIM_B['where'][0]} step {CLAIM_B['where'][1]}",
          "; ".join(f"{k} step {s}" for k, s in b_where), b_where == [CLAIM_B["where"]])
    check("(b) median spread (s)", CLAIM_B["median"], b["median"], b["median"] == CLAIM_B["median"])
    check("(b) share of comparisons with spread > 60 s (3 dp)", CLAIM_B["share>60"],
          f"{b['share>60']:.3f} ({b['above60']}/{b['comparisons']} = {b['share>60']!r})",
          f"{b['share>60']:.3f}" == CLAIM_B["share>60"])

    worst = [c for c in comparisons if c[0] == b["max"]]
    wk = worst[0][1] if worst else None
    worst_detail = "; ".join(f"{fam}: {groups[wk][fam][worst[0][2]] if len(groups[wk][fam]) > worst[0][2] else '-'}"
                             for fam in sorted(groups[wk])) if wk else ""
    lines = [
        "# Independent check: Tier 2 drift switch timing", "",
        f"- Script: `{pathlib.Path(__file__).resolve()}` (from scratch; no author module imported)",
        f"- Input: `{RUNS}`; run at {time.strftime('%Y-%m-%d %H:%M:%S')} local",
        "- Step j = the j-th `[drift] t=` line (0-based), nominal j*900 s. Shares compared at 3 dp (as claimed); "
        "all other numbers exactly. Medians are `statistics.median` (mean of the two middle values when even).", "",
        "## Verdicts", "", *rows, "",
        "## Input facts", "",
        f"- files in runs/: {len(files)}; non-.log files: {non_log or 'none'}; unparsed .log names: {unparsed or 'none'}",
        f"- runs after the rerun rule: {len(chosen)}; `-rerunN` logs found: {reruns_found or 'none'} "
        "(deadline/AMENDMENTS.md A4 says the five A2 reruns wrote their stdout under the ORIGINAL log name, so the "
        "rule is a no-op here and those five logs are the rerun logs)",
        f"- families: {dict(sorted(collections.Counter(f for f, _ in chosen).items()))}",
        f"- first-line returncode over the chosen logs: {dict(returncodes)} (returncode 1 = run stopped early; "
        "such runs are included, as the definition asks for every run with > 1 switch line)",
        f"- switch-line count distribution: {dict(sorted(collections.Counter(len(t) for t in times.values()).items()))}",
        f"- logs whose line index differs from floor(t/900): {index_vs_floor}; logs whose first switch line is not "
        f"t=0: {first_not_zero}",
        f"- groups (keys): {len(groups)}; groups with >= 2 families: {b['groups>=2']}",
        f"- the max-spread comparison, switch time per family: {worst_detail}", "",
        "## Side variants (informational; not the claimed definitions)", "",
        f"- comparisons restricted to steps EVERY family of the group reached: {len(common)}, max spread "
        f"{max((c[0] for c in common), default=None)} s, median {statistics.median([c[0] for c in common]) if common else None} s",
        f"- per-comparison lag of the latest family (max t - step*900) over the {len(comparisons)} comparisons: "
        f"median {statistics.median(max_t_lags)} s, max {max(max_t_lags)} s",
        f"- same latest-family lag over the {len(common)} every-family-reached comparisons: median "
        f"{statistics.median([c[4] for c in common]) if common else None} s, max "
        f"{max((c[4] for c in common), default=None)} s",
        "- The T3.7 report section 2.1 cites Tier 2 as 'trễ trung vị 22,5 s, lớn nhất 210 s ... lệch giữa các họ lớn "
        "nhất chỉ 16 s, trung vị 0 s, trên 76 lần đổi bước' and section 0 says 'lệch giữa các họ <= 16 s'; compare "
        "those figures with the lines above.", ""]
    print("\n".join(lines))
    if write:
        with open(HERE / "TIER2-RESULT.md", "x", encoding="utf-8", newline="\n") as handle:
            handle.write("\n".join(lines) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
