# Independent-B probe 2: ledger entry fields, request fields, event types, alight events.
import base64, json, sys, collections

path = sys.argv[1]
evtypes = collections.Counter()
alight_example = None
last_ckpt = None
promise_action_example = None
with open(path, 'r', encoding='utf-8') as f:
    for line in f:
        rec = json.loads(line)
        env = json.loads(base64.b64decode(rec['frameBase64']))
        mt = env.get('messageType')
        if rec['direction'] == 'adapterToRunner' and mt == 'eventBatch':
            for ev in env['payload']['events']:
                evtypes[ev['eventType']] += 1
                if ev['eventType'] == 'passengerAlighted' and alight_example is None:
                    alight_example = (env.get('simTimeMs'), ev)
        if rec['direction'] == 'runnerToAdapter' and mt == 'checkpoint':
            last_ckpt = env
        if rec['direction'] == 'runnerToAdapter' and mt == 'decision' and promise_action_example is None:
            for a in env['payload'].get('actions', []):
                if a.get('decisionType') == 'promisePublished':
                    promise_action_example = (env.get('simTimeMs'), a)
                    break

print('event types', dict(evtypes))
print('alight example', json.dumps(alight_example, indent=1)[:1500])
print('promise action example', json.dumps(promise_action_example, indent=1)[:2000])
st = last_ckpt['payload']['content']['onlineState']
print('checkpoint simTimeMs', last_ckpt.get('simTimeMs'), 'state simTime', st.get('simulationTimeMs'))
lc = collections.Counter(r['lifecycle'] for r in st['requests'])
print('lifecycle', dict(lc))
keys = collections.Counter()
for r in st['requests']:
    for k in r:
        keys[k] += 1
print('request keys', dict(keys))
comp = [r for r in st['requests'] if r['lifecycle'] == 'completed'][0]
print('completed example', json.dumps(comp, indent=1))
L = st['commitmentLedger']
print('ledger histories', len(L))
h = max(L, key=lambda h: len(h['entries']))
print('history keys', list(h.keys()), 'n entries', len(h['entries']))
for i, e in enumerate(h['entries'][:3]):
    e2 = {k: v for k, v in e.items() if k not in ('budgetAfter', 'budgetBefore', 'deltas')}
    for k in ('exogenousProjection', 'publishedPromise', 'previousPromise'):
        if k in e2 and isinstance(e2[k], dict):
            e2[k] = {kk: (vv if not isinstance(vv, (list, dict)) else '<%s>' % type(vv).__name__) for kk, vv in e2[k].items()}
            if 'projection' in e[k]:
                e2[k]['projection'] = {kk: vv for kk, vv in e[k]['projection'].items() if not isinstance(vv, (list, dict))}
    print('entry', i, json.dumps(e2, indent=1)[:3000])
    print('deltas.visible', e['deltas']['visible'].get('dropEtaTotalMs'), 'decisionInduced', e['deltas']['decisionInduced'].get('dropEtaTotalMs'), 'exogenous', e['deltas']['exogenous'].get('dropEtaTotalMs'))
print('incidentLedger keys', list(st['incidentLedger'].keys()))
