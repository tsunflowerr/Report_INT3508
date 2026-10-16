# Independent-B exploration probe: learn the frame layout of one transcript.
# Written from scratch for this verification. Reads only the raw transcript.
import base64, json, sys, collections

path = sys.argv[1]
counts = collections.Counter()
examples = {}
last_ckpt = None
with open(path, 'r', encoding='utf-8') as f:
    for line in f:
        rec = json.loads(line)
        env = json.loads(base64.b64decode(rec['frameBase64']))
        key = (rec['direction'], env.get('messageType'))
        counts[key] += 1
        if key not in examples:
            examples[key] = env
        if key == ('runnerToAdapter', 'checkpoint'):
            last_ckpt = env

for k, v in sorted(counts.items()):
    print(k, v)

def trunc(o, depth=0, maxd=4):
    if depth >= maxd:
        if isinstance(o, (dict, list)):
            return '<%s len=%d>' % (type(o).__name__, len(o))
        return o
    if isinstance(o, dict):
        return {k: trunc(v, depth + 1, maxd) for k, v in o.items()}
    if isinstance(o, list):
        return [trunc(v, depth + 1, maxd) for v in o[:2]] + (['...%d more' % (len(o) - 2)] if len(o) > 2 else [])
    return o

for k, env in examples.items():
    if k == ('runnerToAdapter', 'checkpoint'):
        continue
    print('=====', k)
    print(json.dumps(trunc(env, maxd=6), indent=1)[:4000])

print('===== last checkpoint keys')
st = last_ckpt['payload']['content']['onlineState']
print(list(st.keys()))
print(json.dumps(trunc(st['requests'], maxd=4), indent=1)[:3000])
print(json.dumps(trunc(st['commitmentLedger'], maxd=7), indent=1)[:6000])
