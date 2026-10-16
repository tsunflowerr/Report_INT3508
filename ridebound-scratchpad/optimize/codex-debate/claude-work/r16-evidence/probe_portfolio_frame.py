"""R16 evidence (read-only probe): dump executionEvidence.candidatePortfolio of one decision frame (the skip-th frame
that considers >= 1 new request and has >= 3 eligible candidates), with route stop lists shortened, plus the
selection objective bounds and the frame's prunedCandidates codes. Also counts, over the whole transcript, the
distinct objective-level name sequences and policyEligibility values.
Usage: python -B probe_portfolio_frame.py <transcript> <out> [skip]   (out opened with mode "x")."""
import base64
import collections
import json
import sys

path, out = sys.argv[1], sys.argv[2]
skip = int(sys.argv[3]) if len(sys.argv) > 3 else 0
lines = [f"# probe_portfolio_frame.py {path} skip={skip}"]
level_seqs = collections.Counter()
elig = collections.Counter()
contrib_len = collections.Counter()
seen = 0
dumped = False
with open(path, "rb") as fh:
    for line in fh:
        row = json.loads(line)
        if row["direction"] != "runnerToAdapter":
            continue
        frame = base64.b64decode(row["frameBase64"])
        if b'"candidatePortfolio"' not in frame:
            continue
        env = json.loads(frame)
        ev = env["payload"]["solver"]["executionEvidence"]
        cp = ev["candidatePortfolio"]
        names = tuple(lv["name"] if not lv["name"].startswith("candidate-id-rank") else "candidate-id-rank*"
                      for lv in cp["selectionProblem"]["objectiveLevels"])
        names = tuple(dict.fromkeys(names))
        level_seqs[names] += 1
        for c in cp["candidates"]:
            elig[c.get("policyEligibility")] += 1
            contrib_len[len(c.get("objectiveContributions", []))] += 1
        if dumped or ev["generation"].get("consideredRequestCount", 0) < 1:
            continue
        if sum(1 for c in cp["candidates"] if c.get("policyEligibility") == "eligible") < 3:
            continue
        if seen < skip:
            seen += 1
            continue
        dumped = True
        short = json.loads(json.dumps(cp))
        for c in short["candidates"]:
            for key in ("route", "schedule"):
                if key in c:
                    for k2, v2 in list(c[key].items()):
                        if isinstance(v2, list) and len(v2) > 1:
                            c[key][k2] = v2[:1] + [f"... {len(v2)} items"]
        lines.append(f"# simTimeMs {env.get('simTimeMs')} decisionHash {env['payload']['decisionHash']}")
        lines.append("# candidatePortfolio (shortened)")
        lines.append(json.dumps(short, indent=1)[:20000])
        lines.append("# selection.finalSolverDiagnostics.objectiveBounds (name, incumbent, bestBound)")
        for b in (ev["selection"].get("finalSolverDiagnostics") or {}).get("objectiveBounds", []):
            lines.append(f"  {b['objectiveName']}: {b['incumbentValue']} / {b['bestBound']}")
        lines.append("# prunedCandidates codes: " + json.dumps(collections.Counter(p["code"] for p in ev.get("prunedCandidates", []))))
lines.append("# objective-level name sequences over all portfolio frames:")
for k, v in level_seqs.most_common():
    lines.append(f"  {v}: {list(k)}")
lines.append(f"# policyEligibility values: {dict(elig)}; objectiveContributions lengths: {dict(contrib_len)}")
text = "\n".join(lines) + "\n"
with open(out, "x", encoding="utf-8", newline="\n") as f:
    f.write(text)
print(text[:40000])
