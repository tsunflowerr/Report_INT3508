"""R16 evidence (read-only probe): for one transcript print
(a) the initializeRun payload with long lists truncated (policy configuration as the Runner received it);
(b) the key tree of the first decision frame that considers >= 1 new request and has >= 1 non-initial ledger effect
    (any action of type other than requestAccepted/requestRejected), with the distinct action decisionTypes seen;
(c) one non-initial commitment-ledger entry of the final checkpoint (keys and the deltas block).
Usage: python -B probe_init_and_ledger.py <transcript> <out>   (out opened with mode "x")."""
import base64
import collections
import json
import sys

path, out = sys.argv[1], sys.argv[2]
lines = [f"# probe_init_and_ledger.py {path}"]


def trunc(obj, depth=0):
    if isinstance(obj, dict):
        return {k: trunc(v, depth + 1) for k, v in obj.items()}
    if isinstance(obj, list):
        return [trunc(v, depth + 1) for v in obj[:2]] + ([f"... {len(obj)} items"] if len(obj) > 2 else [])
    return obj


def tree(obj, prefix, depth):
    if depth > 9:
        return
    if isinstance(obj, dict):
        for k, v in obj.items():
            p = f"{prefix}.{k}" if prefix else k
            if isinstance(v, (dict, list)):
                lines.append(f"  {p}: {type(v).__name__}" + (f"[{len(v)}]" if isinstance(v, list) else ""))
                tree(v, p, depth + 1)
            else:
                lines.append(f"  {p} = {json.dumps(v)[:120]}")
    elif isinstance(obj, list) and obj:
        tree(obj[0], prefix + "[0]", depth + 1)


init_done = dec_done = False
kinds = collections.Counter()
final = None
with open(path, encoding="utf-8") as fh:
    for line in fh:
        row = json.loads(line)
        env = json.loads(base64.b64decode(row["frameBase64"]))
        mt = env.get("messageType")
        if mt == "initializeRun" and not init_done:
            lines.append(f"# (a) initializeRun ({row['direction']}), truncated")
            lines.append(json.dumps(trunc(env.get("payload")), indent=1)[:12000])
            init_done = True
        elif mt == "decision" and row["direction"] == "runnerToAdapter":
            acts = env["payload"].get("actions", [])
            for a in acts:
                kinds[a.get("decisionType")] += 1
            other = [a for a in acts if a.get("decisionType") not in ("requestAccepted", "requestRejected", "promisePublished")]
            if not dec_done and other:
                lines.append("# (b) first decision frame with an action outside accept/reject/promise")
                tree(env["payload"], "", 0)
                lines.append("  example other action: " + json.dumps(other[0])[:3000])
                dec_done = True
        elif mt == "checkpoint" and row["direction"] == "runnerToAdapter":
            final = env["payload"]["content"]["onlineState"]
lines.append(f"# action decisionType counts over all decision frames: {dict(kinds)}")
if final is not None:
    lines.append("# onlineState keys: " + ", ".join(sorted(final.keys())))
    lines.append("# request record keys: " + ", ".join(sorted(final["requests"][0].keys())))
    for hist in final["commitmentLedger"]:
        entries = [e for e in hist["entries"] if e["kind"] != "initialPromise"]
        if entries:
            lines.append("# (c) one non-initial ledger entry")
            lines.append(json.dumps(entries[0], indent=1)[:6000])
            break
text = "\n".join(lines) + "\n"
with open(out, "x", encoding="utf-8", newline="\n") as f:
    f.write(text)
print(text[:40000])
