import json,base64,sys,collections
p=sys.argv[1]
evt=collections.Counter(); exs={}; dec=None; decs=0
for line in open(p,encoding='utf-8'):
    r=json.loads(line)
    env=json.loads(base64.b64decode(r['frameBase64']))
    if env['messageType']=='eventBatch':
        for e in env['payload']['events']:
            evt[e['eventType']]+=1
            if e['eventType'] not in exs and e['eventType']!='travelTimesUpdated': exs[e['eventType']]=e
    if env['messageType']=='decision':
        pl=env['payload']
        if 'certificate' in pl and dec is None and any(a['decisionType']=='promisePublished' for a in pl['actions']): dec=env
print(evt)
for k,e in exs.items(): print(k,json.dumps(e)[:500])
print(list(dec['payload'].keys()))
print(json.dumps(dec['payload']['certificate'])[:1500])
for a in dec['payload']['actions']:
    if a['decisionType']=='promisePublished': print(json.dumps(a)[:800]);break
