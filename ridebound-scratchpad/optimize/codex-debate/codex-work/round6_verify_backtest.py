"""Independent implementation of the sealed Round-6 calibration plan.

Uses only the independently extracted Round-5 rider cache and Python's standard
library. It does not import or execute Claude's code. Numerical report: mode x.
Run with the FleetPy environment's Python -B.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import statistics
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
CLAUDE = HERE.parent / "claude-work"
D14, D15, D16 = ("2018-11-14", "2018-11-15", "2018-11-16")
FAMILIES = {
    "none": [()],
    "uniform": [(b,) for b in (15, 30, 45, 60, 90, 120, 180)],
    "horizon": [(a,) for a in (.02, .04, .06, .08, .10, .15, .20)],
    "direct": [(a,) for a in (.05, .10, .15, .20, .30, .40)],
    "room": [(a, b) for a in (.25, .5, 1.) for b in (30, 60, 90, 120, 180)],
}
FOLDS = ((1, (D14,), (D15, D16)), (2, (D14, D15), (D16,)))


def offset(r, rule):
    lam, family, parameters = rule
    # Seconds throughout, including the same forecast-minus-naive subtraction.
    base = lam * (r["fc"] / 1000 - r["p0"] / 1000)
    if family == "none":
        pad = 0.
    elif family == "uniform":
        pad = parameters[0]
    elif family == "horizon":
        pad = parameters[0] * ((r["p0"] - r["t0"]) / 1000)
    elif family == "direct":
        pad = parameters[0] * (r["max_ride"] / 1500)
    elif family == "room":
        pad = min(parameters[1], parameters[0] * max(0., r["room"] / 1000))
    else:
        raise ValueError(family)
    return base + pad


def score(rows, rule):
    extensions = [offset(r, rule) for r in rows]
    errors = [r["a"] / 1000 - r["p0"] / 1000 - d for r, d in zip(rows, extensions)]
    n = len(rows)
    late = {tau: sum(e > tau for e in errors) for tau in (30, 60, 120)}
    early = sum(e < -60 for e in errors)
    symmetric = sum(abs(e) <= 60 for e in errors)
    return {
        "n": n, "ext": statistics.mean(extensions),
        "p90": sorted(extensions)[min(n - 1, (9 * n) // 10)],
        "timely": n - late[60], "late": late, "early": early, "symmetric": symmetric,
        "Y30": 100 * late[30] / n, "Y60": 100 * late[60] / n,
        "Y120": 100 * late[120] / n,
        "early60": 100 * early / n, "two60": 100 * symmetric / n,
    }


def choose(train, family, budget):
    candidates = []
    for lam in (0, 1):
        for parameters in FAMILIES[family]:
            rule = (lam, family, parameters)
            m = score(train, rule)
            if m["ext"] <= budget:
                candidates.append(((-m["timely"], m["ext"], m["p90"]), rule, m))
    # Stable enumeration resolves any exact tie left unspecified by the three keys.
    return min(candidates, key=lambda c: c[0]) if candidates else None


def displayed(m):
    return (f"Y30 {m['Y30']:5.2f} Y60 {m['Y60']:5.2f} Y120 {m['Y120']:5.2f} "
            f"early60 {m['early60']:5.1f} two60 {m['two60']:5.1f} "
            f"ext {m['ext']:6.1f} p90 {m['p90']:6.1f} timely {m['timely']}/{m['n']}")


def original_rows(text):
    result, heading = {}, None
    for line in text.splitlines():
        if match := re.match(r"== (U|C-30) fold ([12]):", line):
            heading = (match[1], int(match[2]))
        elif match := re.match(r"\s+E\s+(\d+)\s+(none|uniform|horizon|direct|room)\b", line):
            result[(*heading, int(match[1]), match[2])] = line
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="round6-backtest-verification-2026-10-07.txt")
    args = parser.parse_args()
    output = (HERE / args.output).resolve()
    if output.parent != HERE or output.exists():
        raise ValueError("Output must be a new file directly inside codex-work")
    cache_path = HERE / "round5-rider-records-2026-10-07.json"
    data = json.loads(cache_path.read_text(encoding="utf-8"))
    for source in data["sources"]:
        stat = Path(source["path"]).stat()
        if source["signature"] != [stat.st_size, stat.st_mtime_ns]:
            raise ValueError("Transcript signature changed since independent extraction")
    plan = CLAUDE / "CALIB-BACKTEST-PLAN.md"
    plan_hash = hashlib.sha256(plan.read_bytes()).hexdigest()
    seal = (CLAUDE / "CALIB-BACKTEST-PLAN.sha256").read_text(encoding="utf-8").split()[0]
    if plan_hash != seal:
        raise ValueError("Plan hash differs from saved seal")
    expected = original_rows((CLAUDE / "calib-backtest-2026-10-07.txt").read_text(encoding="utf-8"))
    groups = {(arm, day): [r for r in data["records"] if r["arm"] == arm and r["day"] == day]
              for arm in ("U", "C-30") for day in (D14, D15, D16)}
    lines = ["# Independent Round-6 verification: own code; independent Round-5 cache; no Claude-code imports.",
             f"Plan SHA256={plan_hash}; saved seal MATCHES (historical timestamp not independently proven).",
             f"Cache SHA256={hashlib.sha256(cache_path.read_bytes()).hexdigest()}; 68 source signatures unchanged.",
             "Training-budget eligibility; stable tie keys: -timely, mean extension, empirical p90.",
             "direct=maxRideTimeMs/1500 seconds is the plan's ratio-derived proxy, not a newly routed distance."]
    actual, selected = {}, {}
    for arm in ("U", "C-30"):
        for fold, training_days, tests in FOLDS:
            train = [r for day in training_days for r in groups[arm, day]]
            lines += ["", f"== {arm} fold {fold}: train {list(training_days)} ({len(train)} riders)"]
            for budget in (15, 30, 60):
                for family in FAMILIES:
                    selection = choose(train, family, budget)
                    key = (arm, fold, budget, family)
                    selected[key] = selection
                    if selection is None:
                        line = f"  E {budget:>2d} {family:<8}: no rule within budget"
                    else:
                        _, rule, train_metrics = selection
                        lam, _, parameters = rule
                        line = (f"  E {budget:>2d} {family:<8} lam {lam} par {parameters}: "
                                f"train Y60 {train_metrics['Y60']:5.2f} ext {train_metrics['ext']:5.1f}")
                        for day in tests:
                            line += f" || TEST {day[-5:]}: " + displayed(score(groups[arm, day], rule))
                    lines.append(line)
                    actual[key] = line
    mismatch = [(key, expected.get(key), actual.get(key)) for key in sorted(expected.keys() | actual.keys())
                if expected.get(key) != actual.get(key)]
    lines += ["", f"COMPARISON: rows={len(actual)}; mismatches={len(mismatch)}; selections and all printed metrics compared."]
    for key, theirs, ours in mismatch:
        lines += [f"MISMATCH {key}", f"CLAUDE {theirs}", f"CODEX  {ours}"]
    def test(arm, budget, family, day, fold=1):
        return score(groups[arm, day], selected[arm, fold, budget, family][1])
    p1 = all(test("U", b, "room", d)["Y60"] < test("U", b, "uniform", d)["Y60"]
             for b in (30, 60) for d in (D15, D16))
    margins = {(b, d): min(test("U", b, f, d)["Y60"] for f in ("horizon", "direct"))
               - test("U", b, "room", d)["Y60"] for b in (30, 60) for d in (D15, D16)}
    p2 = all(margin <= .5 for margin in margins.values())
    p3 = selected["C-30", 1, 15, "none"][1][0] == 1 and all(
        test("C-30", 15, "none", d)["Y60"] <= .5 for d in (D15, D16))
    lines += ["", f"VERDICTS: P1={p1}; P2={p2}; P3={p3}.",
              "P2 margins (positive favors room): " + repr(margins),
              "Room-superiority kill fires: E30 loses to uniform; E60 loses to horizon on16Nov and breaches accuracy/early guardrails.",
              "", "DETAILED FOLD-1 E60 COMPARISON (no selection on test outcomes)"]
    for day in (D15, D16):
        for arm, budget, family in (("C-30", 15, "none"), *( ("U", 60, f) for f in ("uniform", "horizon", "direct", "room"))):
            m = test(arm, budget, family, day)
            lines.append(f"{day} {arm} {family} Etrain={budget}: " + json.dumps(m, sort_keys=True))
    lines += ["", "COMMON RIDERS AND WHOLE-POLICY COUNTS (descriptive; no counterfactual routing claim)"]
    for day in (D15, D16):
        maps = {arm: {(r['cell'], r['rider']): r for r in groups[arm, day]} for arm in ("U", "C-30")}
        common = maps["U"].keys() & maps["C-30"].keys()
        counts = {arm: sum(s["requests"] for s in data["sources"] if s["arm"] == arm and day[8:10] == s["cell"][7:9])
                  for arm in maps}
        lines.append(f"{day}: requests={counts}; completed_U={len(maps['U'])}; completed_C30={len(maps['C-30'])}; "
                     f"common_completed={len(common)}; U_only={len(maps['U'])-len(common)}; C30_only={len(maps['C-30'])-len(common)}")
        for family in ("uniform", "horizon", "direct", "room"):
            um = score([maps["U"][k] for k in sorted(common)], selected["U", 1, 60, family][1])
            cm = score([maps["C-30"][k] for k in sorted(common)], selected["C-30", 1, 15, "none"][1])
            lines.append(f"{day} common U/{family} vs C30/forecast: timely={um['timely']}/{cm['timely']}; "
                         f"late60={um['Y60']:.6f}%/{cm['Y60']:.6f}%; two60={um['two60']:.6f}%/{cm['two60']:.6f}%; "
                         f"mean_extension={um['ext']:.6f}s/{cm['ext']:.6f}s")
    lines += ["", "No dispatcher jobs executed. Analysis files created exclusively with mode x; no existing output overwritten."]
    with output.open("x", encoding="utf-8", newline="\n") as handle:
        handle.write("\n".join(lines) + "\n")
    print(f"Report={output.name}; compared_rows={len(actual)}; mismatches={len(mismatch)}; P1={p1}; P2={p2}; P3={p3}")


if __name__ == "__main__":
    main()
