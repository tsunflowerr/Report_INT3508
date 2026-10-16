import sys, json, base64, collections

path = sys.argv[1]


def shrink(o):
    if isinstance(o, dict):
        return {k: shrink(v) for k, v in o.items()}
    if isinstance(o, list):
        if len(o) > 2:
            return [shrink(o[0]), shrink(o[1]), '...(%d items)' % len(o)]
        return [shrink(x) for x in o]
    return o


dtypes = collections.Counter()
shown_nonnormal = 0
env_keys = collections.Counter()
decision_hashes = []
acked = []
nonnormal = 0
wit_rules = collections.Counter()
prune_codes = collections.Counter()
cw_keys = set()
last_ckpt = None
promise_actions = collections.defaultdict(list)
with open(path, 'r', encoding='utf-8') as f:
    for line in f:
        rec = json.loads(line)
        env = json.loads(base64.b64decode(rec['frameBase64']))
        mt = env.get('messageType')
        env_keys[(rec['direction'], mt, 'simTimeMs' in env)] += 1
        if mt == 'decision':
            p = env['payload']
            decision_hashes.append(p['decisionHash'])
            for a in p['actions']:
                dtypes[a['decisionType']] += 1
                if a['decisionType'] == 'promisePublished':
                    pp = a['payload']
                    promise_actions[pp['promise']['requestId']].append((pp['promiseVersion'], pp['promise']['dropEtaMs'], pp['reasonCode'], env.get('simTimeMs')))
            body = p['certificate']['body']
            if body.get('normalOperation') is False:
                nonnormal += 1
                for w in body['witnesses']:
                    wit_rules[w.get('rule')] += 1
                if shown_nonnormal < 1:
                    shown_nonnormal += 1
                    print('=== NONNORMAL certificate', json.dumps(shrink(p['certificate']), indent=1)[:4000])
                    print('reasonCode', p.get('reasonCode'), 'status', p.get('status'))
            for pc in p['solver']['executionEvidence']['prunedCandidates']:
                prune_codes[pc['code']] += 1
                for cw in pc['commitmentWitnesses']:
                    cw_keys.add(tuple(sorted(cw.keys())))
        elif mt == 'decisionApplied':
            acked.append(env['payload']['decisionHash'])
        elif mt == 'checkpoint' and rec['direction'] == 'runnerToAdapter':
            last_ckpt = env
print(env_keys)
print(dtypes)
print('decisions', len(decision_hashes), 'acked', len(acked), 'acked==decs', acked == decision_hashes)
print('nonnormal', nonnormal, wit_rules)
print(prune_codes)
print(cw_keys)
os_ = last_ckpt['payload']['content']['onlineState']
print('lifecycles', collections.Counter(r['lifecycle'] for r in os_['requests']))
kinds = collections.Counter()
ekeys = set()
mism = 0
for L in os_['commitmentLedger']:
    ekeys.add(tuple(sorted(L.keys())))
    for e in L['entries']:
        kinds[(e['kind'], e.get('reasonCode'))] += 1
    # compare with promise actions
    rid = L['requestId']
    led = [(e['publishedPromise']['version'], e['publishedPromise']['projection']['dropEtaMs']) for e in L['entries']]
    act = [(v, d) for (v, d, rc, t) in promise_actions.get(rid, [])]
    if led != act:
        mism += 1
        if mism <= 3:
            print('MISMATCH', rid[:12], led[:5], act[:5], len(led), len(act))
print(kinds)
print(ekeys)
print('ledger requests', len(os_['commitmentLedger']), 'promise-action requests', len(promise_actions), 'mismatches', mism)
# print a non-initial non-ONLINE_REPLAN entry example
seen = set()
for L in os_['commitmentLedger']:
    for e in L['entries']:
        k = (e['kind'], e.get('reasonCode'))
        if k not in seen:
            seen.add(k)
            print('--- entry kind', k, sorted(e.keys()))
