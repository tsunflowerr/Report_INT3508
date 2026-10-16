"""R16 evidence (read-only probe): print the key tree of decision frames so that the fields used later are cited
from the data, not assumed. For one transcript it prints (a) the payload / solver / executionEvidence key tree of the
first decision frame that considers >= 1 new request (lists shown with their length and first element), and
(b) a JSON excerpt of executionEvidence.selection and .generation of that frame.
Usage: python -B probe_decision_tree.py <transcript> <out> [skip]   (out opened with mode "x"; skip = number of such
frames to skip before printing)."""
import base64
import json
import sys

path, out = sys.argv[1], sys.argv[2]
skip = int(sys.argv[3]) if len(sys.argv) > 3 else 0
lines = [f"# probe_decision_tree.py {path} skip={skip}"]


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


seen = 0
with open(path, encoding="utf-8") as fh:
    for line in fh:
        row = json.loads(line)
        if row["direction"] != "runnerToAdapter":
            continue
        env = json.loads(base64.b64decode(row["frameBase64"]))
        if env.get("messageType") != "decision":
            continue
        ev = ((env["payload"].get("solver") or {}).get("executionEvidence") or {})
        gen = ev.get("generation") or {}
        if gen.get("consideredRequestCount", 0) < 1:
            continue
        if seen < skip:
            seen += 1
            continue
        lines.append(f"# envelope keys: {sorted(env.keys())}; simTimeMs={env.get('simTimeMs')}")
        lines.append("# key tree of payload")
        tree(env["payload"], "", 0)
        lines.append("# selection excerpt")
        lines.append(json.dumps(ev.get("selection"))[:6000])
        lines.append("# generation excerpt")
        lines.append(json.dumps(gen)[:3000])
        break
text = "\n".join(lines) + "\n"
with open(out, "x", encoding="utf-8", newline="\n") as f:
    f.write(text)
print(text[:30000])
