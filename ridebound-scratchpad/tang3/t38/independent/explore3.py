import json,base64,sys,collections
p=sys.argv[1]
last=None; shown=0
for line in open(p,encoding='utf-8'):
    r=json.loads(line)
    env=json.loads(base64.b64decode(r['frameBase64']))
    if env['messageType']=='eventBatch':
        if any(e['eventType']=='passengerAlighted' for e in env['payload']['events']) and shown<1:
            shown+=1
            print({k:v for k,v in env.items() if k!='payload'}, [ (e['eventSeq'],e['eventType']) for e in env['payload']['events']], list(env['payload'].keys()))
    if env['messageType']=='runnerToAdapter' or (r['direction']=='runnerToAdapter' and env['messageType']=='checkpoint'): last=env
st=last['payload']['content']['onlineState']
print(collections.Counter(q['lifecycle'] for q in st['requests']))
for q in st['requests']:
    if q['lifecycle']=='completed': print(json.dumps(q)); break
print(st['simulationTimeMs'])
print(json.dumps(st['commitmentLedger'][0]['entries'][-1]['publishedPromise'])[:600])
print(st['commitmentLedger'][0].keys(), [e['kind'] for e in st['commitmentLedger'][0]['entries']])
