"""R13 final judge, read-only: what do the recorded objective levels of the SELECTED fleet plan show, T3.8 U and C-30
(34 test cells each)?  Per decision that has new requests to consider:
  - worst-hard-utilization-ppm: incumbent value and best bound (proven optimal) -> is the level saturated (1e6)?
  - revision:drop_eta_total_ms incumbent > 0?  (the selected plan moves some incumbent's drop ETA by dispatch)
  - candidate retention: any candidateCapApplied / omittedFeasibleCandidateCountByCap > 0 / workBudgetExhausted.
Usage: python -B objective_levels_check.py <out.txt> (mode "x")."""
import base64, collections, json, pathlib, sys
from concurrent.futures import ProcessPoolExecutor

OPT = pathlib.Path("E:/Code/Report_INT3508/ridebound-scratchpad/optimize")


def runs():
    sys.path.insert(0, str(OPT))
    import forecast_family_a as fa  # noqa: E402
    cells = list(fa.run_t38.PHASES["test"][1])
    return [(arm, fa.run_dir("test", arm, c) / "transcript-00.ndjson") for arm in ("U", "C-30") for c in cells]


def analyze(job):
    arm, path = job
    c = collections.Counter()
    with open(path, "rb") as fh:
        for line in fh:
            row = json.loads(line)
            if row["direction"] != "runnerToAdapter":
                continue
            frame = base64.b64decode(row["frameBase64"])
            if b'"decision"' not in frame[:120]:
                continue
            env = json.loads(frame)
            if env.get("messageType") != "decision":
                continue
            ev = env["payload"]["solver"]["executionEvidence"]
            gen = ev["generation"]
            c["decisions"] += 1
            for vl in gen["vehicleLosses"]:
                c["capApplied"] += bool(vl.get("candidateCapApplied"))
                c["omittedByCap"] += vl.get("omittedFeasibleCandidateCountByCap", 0)
                c["workExhausted"] += bool(vl.get("workBudgetExhausted"))
            c["omittedRequests"] += gen.get("omittedRequestCount", 0)
            if gen.get("consideredRequestCount", 0) < 1:
                continue
            c["with_new_request"] += 1
            levels = {b["objectiveName"]: b for b in (ev["selection"].get("finalSolverDiagnostics") or {}).get("objectiveBounds", [])}
            w = levels.get("worst-hard-utilization-ppm")
            if w is None:
                c["no_util_level"] += 1
            else:
                c["util_level"] += 1
                c["util_saturated_incumbent"] += w["incumbentValue"] == 1_000_000
                c["util_saturated_bound"] += w["bestBound"] == 1_000_000
            d = levels.get("revision:drop_eta_total_ms")
            if d is not None and d["incumbentValue"] > 0:
                c["selected_plan_moves_drop"] += 1
    return arm, c


def main():
    out = sys.argv[1]
    with ProcessPoolExecutor(max_workers=4) as pool:
        res = list(pool.map(analyze, runs()))
    tot = collections.defaultdict(collections.Counter)
    for arm, c in res:
        tot[arm].update(c)
    lines = ["# objective_levels_check.py (T3.8, 34 test cells per arm; all decision frames)"]
    for arm in ("U", "C-30"):
        c = tot[arm]
        lines.append(f"## {arm}: decisions {c['decisions']}; with >=1 new request considered {c['with_new_request']}")
        lines.append(f"  worst-hard-utilization level present {c['util_level']} (absent {c['no_util_level']}); "
                     f"incumbent == 1e6: {c['util_saturated_incumbent']}; best bound == 1e6: {c['util_saturated_bound']}")
        lines.append(f"  selected plan has revision:drop_eta_total_ms > 0: {c['selected_plan_moves_drop']}")
        lines.append(f"  retention: candidateCapApplied {c['capApplied']}; omittedFeasibleCandidateCountByCap {c['omittedByCap']}; "
                     f"workBudgetExhausted {c['workExhausted']}; omittedRequestCount {c['omittedRequests']}")
    text = "\n".join(lines) + "\n"
    with open(out, "x", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
