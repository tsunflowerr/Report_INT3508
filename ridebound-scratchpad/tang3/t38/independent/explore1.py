import json,base64,sys,collections
p=sys.argv[1]
cnt=collections.Counter(); last=None; ex={}
for line in open(p,encoding='utf-8'):
    r=json.loads(line)
    env=json.loads(base64.b64decode(r['frameBase64']))
    k=(r['direction'],env['messageType']); cnt[k]+=1
    if k not in ex: ex[k]=env
    if k==('runnerToAdapter','checkpoint'): last=env
print(cnt)
for k,e in ex.items():
    print(k, json.dumps(e)[:600])
st=last['payload']['content']['onlineState']
print(list(st.keys()))
print(json.dumps(st['commitmentLedger'][0])[:2500])
print(json.dumps(st['requests'][0])[:800])
print(json.dumps(st['incidentLedger'])[:300])
