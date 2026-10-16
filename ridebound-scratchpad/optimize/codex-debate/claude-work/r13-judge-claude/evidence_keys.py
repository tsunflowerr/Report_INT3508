"""R13 judge helper: list the keys of solver executionEvidence in one existing T3.8 C-30 transcript, and sum any
numeric fields whose name suggests time/work, to see whether per-decision timing is recorded (for Codex P2).
Zero-run, read-only. Usage: python -B evidence_keys.py <transcript> <out.txt> (mode x)."""
import base64
import collections
import json
import sys

path, out = sys.argv[1], sys.argv[2]
keys = collections.Counter()
solver_keys = collections.Counter()
numeric = collections.defaultdict(list)
n_dec = 0


def walk(prefix, obj, depth=0):
    if depth > 3:
        return
    if isinstance(obj, dict):
        for k, v in obj.items():
            name = f"{prefix}.{k}" if prefix else k
            if isinstance(v, (int, float)) and not isinstance(v, bool):
                low = k.lower()
                if any(s in low for s in ("micro", "milli", "time", "work", "count", "units", "evaluated", "candidates")):
                    numeric[name].append(v)
            elif isinstance(v, (dict, list)):
                walk(name, v, depth + 1)
    elif isinstance(obj, list) and obj and isinstance(obj[0], dict):
        keys[prefix + "[]"] += 1


with open(path, encoding="utf-8") as fh:
    for line in fh:
        env = json.loads(base64.b64decode(json.loads(line)["frameBase64"]))
        if env.get("messageType") != "decision":
            continue
        n_dec += 1
        solver = (env.get("payload") or {}).get("solver") or {}
        for k in solver:
            solver_keys[k] += 1
        walk("solver", solver)
lines = [f"# evidence_keys.py on {path}", f"decisions {n_dec}",
         "solver top-level keys: " + ", ".join(f"{k}({v})" for k, v in sorted(solver_keys.items()))]
for name, vals in sorted(numeric.items()):
    lines.append(f"  {name}: n={len(vals)} sum={sum(vals)} max={max(vals)}")
text = "\n".join(lines) + "\n"
with open(out, "x", encoding="utf-8", newline="\n") as fh:
    fh.write(text)
print(text)
