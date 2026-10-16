import json, base64, sys, collections

path = sys.argv[1]
counts = collections.Counter()
examples = {}
with open(path, "r", encoding="utf-8") as f:
    for i, line in enumerate(f):
        rec = json.loads(line)
        env = json.loads(base64.b64decode(rec["frameBase64"]))
        key = (rec["direction"], env.get("messageType"))
        counts[key] += 1
        if key not in examples:
            examples[key] = (list(rec.keys()), env)
for k, v in counts.items():
    print(k, v)
print("=====")
for k, (reckeys, env) in examples.items():
    s = json.dumps(env)
    print(k, reckeys, list(env.keys()))
    print(s[:3000])
    print("-----")
