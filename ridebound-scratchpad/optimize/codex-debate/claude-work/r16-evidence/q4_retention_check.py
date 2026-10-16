"""R16 evidence, Q4 add-on (zero-run, read-only): was candidate retention ever truncated in the WP14r runs used for the
cost-first re-selection?  Counts, over all decision frames, vehicleLosses entries with candidateCapApplied true,
omittedFeasibleCandidateCountByCap > 0, workBudgetExhausted true, and generation.omittedRequestCount > 0.
If retention never truncated, the retained portfolio equals every feasible generated candidate, so a selection-only
change sees the same set (the retention strategy cannot matter).
Usage: python -B q4_retention_check.py <out.txt>   (out opened with mode "x"; <= 4 processes)."""
import base64
import collections
import json
import pathlib
import sys
from concurrent.futures import ProcessPoolExecutor

ROOT = pathlib.Path("E:/RideBoundData/wp14r/development-v6-ledger")
ARMS = ("b1-ref", "c1-nobudget", "c1-budget120", "c1-budget60", "c1-h6ref")


def analyze(job):
    arm, path = job
    c = collections.Counter()
    with open(path, "rb") as fh:
        for line in fh:
            row = json.loads(line)
            if row["direction"] != "runnerToAdapter":
                continue
            frame = base64.b64decode(row["frameBase64"])
            if b'"decision"' not in frame[:160]:
                continue
            env = json.loads(frame)
            if env.get("messageType") != "decision":
                continue
            gen = env["payload"]["solver"]["executionEvidence"]["generation"]
            c["decisions"] += 1
            c["omittedRequests"] += gen.get("omittedRequestCount", 0)
            for vl in gen["vehicleLosses"]:
                c["capApplied"] += bool(vl.get("candidateCapApplied"))
                c["omittedByCap"] += vl.get("omittedFeasibleCandidateCountByCap", 0)
                c["workExhausted"] += bool(vl.get("workBudgetExhausted"))
    return arm, c


def main():
    out = sys.argv[1]
    jobs = [(arm, r / "attempt-01" / "output" / "transcript-00.ndjson")
            for arm in ARMS for r in sorted(ROOT.glob(f"w14-*-{arm}-s7"))
            if (r / "attempt-01" / "output" / "transcript-00.ndjson").exists()]
    with ProcessPoolExecutor(max_workers=4) as pool:
        res = list(pool.map(analyze, jobs))
    tot = collections.defaultdict(collections.Counter)
    for arm, c in res:
        tot[arm].update(c)
    lines = ["# q4_retention_check.py (WP14r v6, all decision frames)"]
    for arm in ARMS:
        c = tot[arm]
        lines.append(f"{arm}: decisions {c['decisions']}; candidateCapApplied {c['capApplied']}; omittedFeasibleCandidateCountByCap "
                     f"{c['omittedByCap']}; workBudgetExhausted {c['workExhausted']}; omittedRequestCount {c['omittedRequests']}")
    text = "\n".join(lines) + "\n"
    with open(out, "x", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print(text)


if __name__ == "__main__":
    main()
