# Independent exploration of transcript format (read-only). Prints structure only.
import base64, json, sys, collections

path = sys.argv[1]
types = collections.Counter()
examples = {}
with open(path, "r", encoding="utf-8") as fh:
    for i, line in enumerate(fh):
        rec = json.loads(line)
        env = json.loads(base64.b64decode(rec["frameBase64"]))
        key = (rec["direction"], env.get("messageType"))
        types[key] += 1
        if key not in examples:
            examples[key] = (list(rec.keys()), env)
for k, v in types.items():
    print(k, v)
print("-----")
def trunc(o, depth=0):
    if depth > 6:
        return "..."
    if isinstance(o, dict):
        return {k: trunc(v, depth + 1) for k, v in list(o.items())[:25]}
    if isinstance(o, list):
        return [trunc(x, depth + 1) for x in o[:2]] + (["...(%d)" % len(o)] if len(o) > 2 else [])
    if isinstance(o, str) and len(o) > 80:
        return o[:80] + "..."
    return o
for k, (reckeys, env) in examples.items():
    print("=====", k, "record keys:", reckeys)
    print(json.dumps(trunc(env), indent=1)[:6000])
