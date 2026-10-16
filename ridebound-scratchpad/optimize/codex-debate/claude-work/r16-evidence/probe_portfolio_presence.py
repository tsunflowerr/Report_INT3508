"""R16 evidence (read-only probe): which existing transcripts record executionEvidence.candidatePortfolio (the
retained candidate set with per-candidate objective contributions and operational cost)?
For each transcript given: decision frames, frames whose decoded bytes contain "candidatePortfolio", evidenceVersion
values, the manifest policyId / coreCommitSha, and (first portfolio frame) objectiveProfile + objective level names.
Usage: python -B probe_portfolio_presence.py <out> <transcript> [<transcript> ...]   (out opened with mode "x")."""
import base64
import collections
import json
import sys

out, paths = sys.argv[1], sys.argv[2:]
lines = ["# probe_portfolio_presence.py"]
for path in paths:
    dec = port = 0
    versions = collections.Counter()
    manifest = {}
    levels = None
    with open(path, "rb") as fh:
        for line in fh:
            row = json.loads(line)
            frame = base64.b64decode(row["frameBase64"])
            head = frame[:160]
            if b'"initializeRun"' in head and not manifest:
                m = json.loads(frame)["payload"].get("manifest", {})
                manifest = {k: m.get(k) for k in ("policyId", "policyVersion", "coreCommitSha", "policyConfigurationHash")}
                continue
            if row["direction"] != "runnerToAdapter" or b'"decision"' not in head:
                continue
            dec += 1
            if b'"evidenceVersion"' in frame:
                i = frame.find(b'"evidenceVersion"')
                versions[frame[i:i + 32].decode("utf-8", "replace")] += 1
            if b'"candidatePortfolio"' in frame:
                port += 1
                if levels is None:
                    ev = json.loads(frame)["payload"]["solver"]["executionEvidence"]["candidatePortfolio"]
                    levels = (ev.get("objectiveProfile"),
                              [(lv.get("name"), lv.get("sense"), lv.get("aggregation"))
                               for lv in ev["selectionProblem"]["objectiveLevels"]])
    lines.append(f"## {path}")
    lines.append(f"  manifest {manifest}")
    lines.append(f"  decision frames {dec}; with candidatePortfolio {port}; evidenceVersion {dict(versions)}")
    lines.append(f"  first portfolio: {levels}")
text = "\n".join(lines) + "\n"
with open(out, "x", encoding="utf-8", newline="\n") as f:
    f.write(text)
print(text)
