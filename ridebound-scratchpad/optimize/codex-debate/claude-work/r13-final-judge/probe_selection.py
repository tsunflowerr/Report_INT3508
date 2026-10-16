"""Read-only probe (R13 final judge): what does a decision's executionEvidence.selection / .generation record?
Prints the key tree (depth-limited, lists truncated to their first element) of the first decision frame that has
>= 2 candidates for some vehicle, plus the decision payload's top-level keys.
Usage: python -B probe_selection.py <transcript> <out> (out opened with mode "x")."""
import base64, json, sys

path, out = sys.argv[1], sys.argv[2]
lines = []


def tree(obj, prefix, depth):
    if depth > 7:
        return
    if isinstance(obj, dict):
        for k, v in obj.items():
            p = f"{prefix}.{k}" if prefix else k
            if isinstance(v, (dict, list)):
                lines.append(f"  {p}: {type(v).__name__}{'[' + str(len(v)) + ']' if isinstance(v, list) else ''}")
                tree(v, p, depth + 1)
            else:
                s = json.dumps(v)
                lines.append(f"  {p} = {s[:100]}")
    elif isinstance(obj, list) and obj:
        tree(obj[0], prefix + "[0]", depth + 1)


count = 0
with open(path, encoding="utf-8") as fh:
    for line in fh:
        row = json.loads(line)
        env = json.loads(base64.b64decode(row["frameBase64"]))
        if env.get("messageType") != "decision":
            continue
        payload = env["payload"]
        ev = ((payload.get("solver") or {}).get("executionEvidence") or {})
        sel = ev.get("selection") or {}
        text = json.dumps(sel)
        if text.count("candidateId") >= 3:
            count += 1
            if count == 3:
                lines.append("# decision payload keys: " + ", ".join(sorted(payload.keys())))
                lines.append("# solver keys: " + ", ".join(sorted((payload.get("solver") or {}).keys())))
                lines.append("# executionEvidence tree")
                tree(ev, "", 0)
                break
text = "\n".join(lines) + "\n"
with open(out, "x", encoding="utf-8", newline="\n") as f:
    f.write(text)
print(text[:12000])
