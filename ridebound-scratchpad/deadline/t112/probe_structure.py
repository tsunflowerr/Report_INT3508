"""Dump the key tree of decision frames that carry commitment prune witnesses (read-only)."""
import base64
import json
import sys

path = sys.argv[1]


def tree(value, depth=0, limit=5):
    pad = "  " * depth
    if depth > limit:
        return
    if isinstance(value, dict):
        for key, sub in value.items():
            kind = type(sub).__name__
            size = f"[{len(sub)}]" if isinstance(sub, (list, dict)) else repr(sub)[:60]
            print(f"{pad}{key}: {kind} {size}")
            if isinstance(sub, dict):
                tree(sub, depth + 1, limit)
            elif isinstance(sub, list) and sub and isinstance(sub[0], dict):
                tree(sub[0], depth + 1, limit)


shown = 0
with open(path, encoding="utf-8") as handle:
    for line in handle:
        frame = json.loads(base64.b64decode(json.loads(line)["frameBase64"]))
        if frame.get("messageType") != "decision":
            continue
        text = json.dumps(frame)
        if "COMMITMENT_PHASE_LOCK" not in text:
            continue
        print("frame keys:", list(frame.keys()), "simTimeMs:", frame.get("simTimeMs"))
        tree(frame["payload"], 0, 6)
        shown += 1
        if shown >= 1:
            break
print("frames shown:", shown)
