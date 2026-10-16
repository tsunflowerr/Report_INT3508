"""Read-only probe (R13 final judge). Prints, for one transcript:
(1) the policy-related keys of the initializeRun frame (policyId, retentionStrategy, objective-like keys);
(2) the first budget-pruned candidate record (keys + witness) found in a decision frame.
Usage: python -B probe_structure.py <transcript> <out> (out opened with mode "x")."""
import base64, json, sys

path, out = sys.argv[1], sys.argv[2]
lines = []


def walk(obj, prefix, depth, keep):
    if depth > 6:
        return
    if isinstance(obj, dict):
        for k, v in obj.items():
            p = f"{prefix}.{k}" if prefix else k
            if any(s in k.lower() for s in keep) and not isinstance(v, (dict, list)):
                lines.append(f"  {p} = {v}")
            walk(v, p, depth + 1, keep)
    elif isinstance(obj, list):
        for i, v in enumerate(obj[:3]):
            walk(v, f"{prefix}[{i}]", depth + 1, keep)


init_done = pruned_done = False
with open(path, encoding="utf-8") as fh:
    for line in fh:
        if not line.strip():
            continue
        row = json.loads(line)
        env = json.loads(base64.b64decode(row["frameBase64"]))
        mt = env.get("messageType")
        if mt == "initializeRun" and not init_done:
            lines.append(f"# initializeRun ({row['direction']})")
            walk(env.get("payload"), "", 0, ["policyid", "retention", "objective", "profile", "commit", "binary", "kind"])
            init_done = True
        if mt == "decision" and not pruned_done:
            ev = ((env.get("payload") or {}).get("solver") or {}).get("executionEvidence") or {}
            for pc in ev.get("prunedCandidates", []):
                if pc.get("code") == "COMMITMENT_BUDGET_EXCEEDED":
                    lines.append("# first budget-pruned candidate")
                    lines.append("  keys: " + ", ".join(sorted(pc.keys())))
                    lines.append("  record: " + json.dumps(pc)[:1500])
                    lines.append("  executionEvidence keys: " + ", ".join(sorted(ev.keys())))
                    pruned_done = True
                    break
        if init_done and pruned_done:
            break
text = "\n".join(lines) + "\n"
with open(out, "x", encoding="utf-8", newline="\n") as f:
    f.write(text)
print(text)
