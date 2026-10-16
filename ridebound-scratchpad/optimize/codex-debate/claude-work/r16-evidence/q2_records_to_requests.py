"""R16 evidence, Q2 (zero-run, read-only): the 1,256 drop-budget prune records on measured traffic are CANDIDATE
records. How many distinct requests do they concern, and how did those requests end in the same run?
Runs: T3.8 C-30 x 34 test cells; w07/w07x C-30, C-60, C-90, C-120, C-150, C-180, C-240, C-300 x 8 cells (98 runs, the
population of cumulative_decisive_check.py). Acknowledged decisions only; prunedCandidates[].code ==
COMMITMENT_BUDGET_EXCEEDED; newRequestIds; final lifecycle from the last checkpoint.
Usage: python -B q2_records_to_requests.py <out.txt>   (out opened with mode "x"; <= 4 processes)."""
import base64
import collections
import json
import pathlib
import sys
from concurrent.futures import ProcessPoolExecutor

OPT = pathlib.Path(r"E:/Code/Report_INT3508/ridebound-scratchpad/optimize")
sys.path.insert(0, str(OPT))
import forecast_family_a as fa  # noqa: E402


def jobs():
    js = [("T3.8 C-30", fa.run_dir("test", "C-30", c) / "transcript-00.ndjson") for c in fa.run_t38.PHASES["test"][1]]
    for root, arms in (("C:/RideBoundData/research/tier3-w07-v1", ("C-30", "C-60", "C-120", "C-300")),
                       ("C:/RideBoundData/research/tier3-w07x-v1", ("C-90", "C-150", "C-180", "C-240"))):
        for arm in arms:
            for p in sorted(pathlib.Path(root).glob(f"{arm}-d*-w07/transcript-00.ndjson")):
                js.append((f"w07 {arm}", p))
    return js


def analyze(job):
    label, path = job
    acked, recs, final = set(), [], None
    with open(path, "rb") as fh:
        for line in fh:
            row = json.loads(line)
            frame = base64.b64decode(row["frameBase64"])
            head = frame[:160]
            if row["direction"] == "adapterToRunner":
                if b'"decisionApplied"' in head:
                    acked.add(json.loads(frame)["payload"]["decisionHash"])
                continue
            if b'"checkpoint"' in head:
                final = frame
                continue
            if b'"decision"' not in head or b"COMMITMENT_BUDGET_EXCEEDED" not in frame:
                continue
            p = json.loads(frame)["payload"]
            for pc in (p.get("solver") or {}).get("executionEvidence", {}).get("prunedCandidates", []):
                if pc.get("code") == "COMMITMENT_BUDGET_EXCEEDED":
                    recs.append((p["decisionHash"], tuple(pc.get("newRequestIds", []))))
    life = {r["requestId"]: r["lifecycle"] for r in json.loads(final)["payload"]["content"]["onlineState"]["requests"]}
    recs = [(h, n) for h, n in recs if h in acked]
    reqs = {r for _, n in recs for r in n}
    return label, len(recs), len({h for h, _ in recs}), collections.Counter(life[r] for r in reqs), \
        sum(1 for _, n in recs if not n)


def main():
    out = sys.argv[1]
    with ProcessPoolExecutor(max_workers=4) as pool:
        res = list(pool.map(analyze, jobs()))
    agg = collections.OrderedDict()
    for label, n, d, life, empty in res:
        a = agg.setdefault(label, [0, 0, collections.Counter(), 0, 0])
        a[0] += n; a[1] += d; a[2].update(life); a[3] += empty; a[4] += 1
    lines = ["# q2_records_to_requests.py: drop-budget prune records -> distinct requests (per run, summed), 98 measured C runs", ""]
    tot = [0, 0, collections.Counter(), 0]
    for label, (n, d, life, empty, runs) in agg.items():
        lines.append(f"{label:<10} runs {runs:2d} | records {n:4d} | decisions with >=1 record {d:4d} | distinct requests {sum(life.values()):4d} "
                     f"(final: {dict(life)}) | records with no new request {empty}")
        tot[0] += n; tot[1] += d; tot[2].update(life); tot[3] += empty
    lines.append(f"TOTAL      runs {len(res)} | records {tot[0]} | decisions {tot[1]} | request-run pairs {sum(tot[2].values())} "
                 f"(final: {dict(tot[2])}) | records with no new request {tot[3]}")
    text = "\n".join(lines) + "\n"
    with open(out, "x", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print(text)


if __name__ == "__main__":
    main()
