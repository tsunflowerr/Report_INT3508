import sys, json, base64

path = sys.argv[1]
want_dec_idx = int(sys.argv[2]) if len(sys.argv) > 2 else 300


def shrink(o, depth=0):
    if isinstance(o, dict):
        return {k: shrink(v, depth + 1) for k, v in o.items()}
    if isinstance(o, list):
        if len(o) > 2:
            return [shrink(o[0], depth + 1), shrink(o[1], depth + 1), '...(%d items)' % len(o)]
        return [shrink(x, depth + 1) for x in o]
    return o


dec_i = -1
ev_shown = set()
with open(path, 'r', encoding='utf-8') as f:
    for line in f:
        rec = json.loads(line)
        env = json.loads(base64.b64decode(rec['frameBase64']))
        mt = env.get('messageType')
        if mt == 'decision':
            dec_i += 1
            if dec_i == want_dec_idx:
                print('===== DECISION', dec_i)
                print(json.dumps(shrink(env), indent=1)[:20000])
        elif mt == 'eventBatch':
            for ev in env['payload']['events']:
                t = ev.get('eventType')
                if t not in ev_shown and t != 'travelTimesUpdated':
                    ev_shown.add(t)
                    print('===== EVENT', t, 'env simTimeMs', env.get('simTimeMs'))
                    print(json.dumps(shrink(ev), indent=1)[:3000])
        elif mt == 'checkpoint' and rec['direction'] == 'runnerToAdapter':
            print('===== CHECKPOINT')
            c = env['payload']['content']
            print(list(c.keys()))
            os_ = c['onlineState']
            print(list(os_.keys()))
            print(json.dumps(shrink(os_['requests'][0]), indent=1)[:5000])
            led = os_['commitmentLedger']
            print('ledger len', len(led))
            print(json.dumps(shrink(led[0]), indent=1)[:12000])
