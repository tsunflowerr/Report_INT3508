"""R13 proposer helper (read-only probe): which message types / event kinds does a transcript carry, and is there any
vehicle distance or busy-time field usable for an operator-cost metric (VKT or vehicle-hours per served rider)?
Prints counts and the key sets of the first example of each event kind. Writes nothing except its own output (mode x).
Usage: python -B probe_event_kinds.py <transcript.ndjson> <out.txt>"""
import base64
import collections
import json
import sys


def walk_keys(obj, prefix="", depth=0, out=None):
    out = out if out is not None else set()
    if depth > 3:
        return out
    if isinstance(obj, dict):
        for k, v in obj.items():
            out.add(prefix + k)
            walk_keys(v, prefix + k + ".", depth + 1, out)
    elif isinstance(obj, list) and obj:
        walk_keys(obj[0], prefix + "[].", depth + 1, out)
    return out


def main(path, out):
    types = collections.Counter()
    kinds = collections.Counter()
    examples = {}
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            env = json.loads(base64.b64decode(json.loads(line)["frameBase64"]))
            mt = env.get("messageType")
            types[mt] += 1
            payload = env.get("payload") or {}
            for ev in payload.get("events", []) if isinstance(payload, dict) else []:
                k = ev.get("kind") or ev.get("type") or ev.get("eventType")
                kinds[k] += 1
                if k not in examples:
                    examples[k] = sorted(walk_keys(ev))
            if mt not in examples:
                examples[mt] = sorted(walk_keys(payload))[:80]
    lines = ["# message types"] + [f"{k}: {v}" for k, v in types.most_common()]
    lines += ["# event kinds"] + [f"{k}: {v}" for k, v in kinds.most_common()]
    lines += ["# key sets (first example)"] + [f"{k}: {examples[k]}" for k in examples]
    body = "\n".join(lines) + "\n"
    with open(out, "x", encoding="utf-8", newline="\n") as fh:
        fh.write(body)
    print(body[:6000])


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
