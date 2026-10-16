"""Read-only independent recheck of final raw checkpoints and supplied extraction cache.

No simulator, runner or repository file is changed. Output stays beside this script.
"""
from pathlib import Path
import base64, collections, csv, hashlib, json, math, random, statistics

HERE = Path(__file__).resolve().parent
SRC = Path(r'E:\Code\Report_INT3508\ridebound-scratchpad\tang3\t38')
RAW = Path(r'C:\RideBoundData\research\tier3-t38-v1')
CACHE = SRC / 'independent' / 'cache'
ARMS = ['U', 'C-30', 'Mplus-30', 'Mplus-60', 'V-30']
manifest = json.loads((SRC / 'split-t38-v1.json').read_text(encoding='utf-8'))

def backward_lines(path, chunk=1024*1024):
    with path.open('rb') as f:
        f.seek(0, 2)
        pos, pending = f.tell(), b''
        while pos:
            n = min(chunk, pos)
            pos -= n
            f.seek(pos)
            parts = (f.read(n) + pending).split(b'\n')
            pending = parts[0]
            for line in reversed(parts[1:]):
                if line.strip():
                    yield line
        if pending.strip():
            yield pending

def final_state(path):
    for line in backward_lines(path):
        outer = json.loads(line)
        blob = base64.b64decode(outer['frameBase64'])
        env = json.loads(blob)
        if env['messageType'] == 'checkpoint' and outer['direction'] == 'runnerToAdapter':
            assert hashlib.sha256(blob).hexdigest() == outer['frameSha256']
            return env['payload']['content']['onlineState'], outer['frameSha256']
    raise AssertionError('no final checkpoint')

def xcv(q):
    return tuple(sum(abs(v[b]-v[a]) for v in q['rev']) for a,b in [('v_d','e_d'),('e_d','p_d'),('v_d','p_d')])

all_cache = {}
checks = []
figure_rows = []
for arm,cell in [('C-30',c) for c in manifest['calibration']] + [(a,c) for c in manifest['test'] for a in ARMS]:
    names = [f'{arm}-{cell}', f'{arm}-{cell}-rerun1']
    name = next(n for n in names if (RAW/n/'summary.json').exists())
    folder = RAW / name
    summary = json.loads((folder/'summary.json').read_text(encoding='utf-8'))
    cached = json.loads((CACHE/f'{name}.json').read_text(encoding='utf-8'))
    assert summary['status'] == cached['status'] == 'pass'
    state, frame_hash = final_state(folder/'transcript-00.ndjson')
    life = dict(collections.Counter(r['lifecycle'] for r in state['requests']))
    assert life == cached['lifecycle'] and life.get('completed',0) == cached['served']
    riders = {}
    for hist in state['commitmentLedger']:
        entries = hist['entries']
        p0 = entries[0]['publishedPromise']['projection']
        row = {'p0_drop':p0['dropEtaMs'], 'p0_pick':p0['pickupEtaMs'], 'rev':[]}
        for e in entries[1:]:
            v = e['previousPromise']['projection']; ex = e['exogenousProjection']; p = e['publishedPromise']['projection']
            row['rev'].append({'v_d':v['dropEtaMs'],'e_d':ex['dropEtaMs'],'p_d':p['dropEtaMs'],
                'dl_x':e['deltas']['exogenous']['dropEtaTotalMs'], 'dl_c':e['deltas']['decisionInduced']['dropEtaTotalMs'], 'dl_z':e['deltas']['visible']['dropEtaTotalMs']})
        riders[hist['requestId']] = row
    assert riders == cached['riders']
    mismatch = sum(abs(r['e_d']-r['v_d']) != r['dl_x'] or abs(r['p_d']-r['e_d']) != r['dl_c'] or abs(r['p_d']-r['v_d']) != r['dl_z'] for q in riders.values() for r in q['rev'])
    assert mismatch == 0
    sums = {r:xcv(q) for r,q in riders.items()}
    assert all(v <= c+x for x,c,v in sums.values())
    score = max((v[0] for v in sums.values()),default=0) if all(r in cached['alight'] for r in riders) else math.inf
    max_c = max((v[1] for v in sums.values()),default=0)
    max_v = max((v[2] for v in sums.values()),default=0)
    if arm == 'C-30':
        own_n = sum(v[1]>30000 for v in sums.values());own_den = len(riders)
    elif arm == 'V-30':
        own_n = sum(v[2]>30000 for v in sums.values());own_den = len(riders)
    elif arm.startswith('Mplus'):
        cap = 30000 if arm=='Mplus-30' else 60000
        own_n = sum(cached['alight'][r] - q['p0_drop'] > cap for r,q in riders.items() if r in cached['alight'])
        own_den = sum(r in cached['alight'] for r in riders)
    else:
        own_n,own_den = 0,len(riders)
    check = {'job':name,'arm':arm,'cell':cell,'phase':'calib' if cell in manifest['calibration'] else 'test',
        'frameSha256':frame_hash,'served':cached['served'],'requests':cached['requests'],'promised':len(riders),
        'revisionCount':sum(len(q['rev']) for q in riders.values()),'scoreMs':score,'maxCMs':max_c,'maxVMs':max_v,
        'ownBrokenCount':own_n,'ownBrokenDenominator':own_den,'ownBrokenShare':own_n/own_den if own_den else 0,
        'forcedCount':cached['nonNormalAcked'],'decisionCount':cached['acked'],
        'forcedShare':cached['nonNormalAcked']/cached['acked'],
        'E2':sum(v[2]>60000 for v in sums.values())/len(riders) if riders else 0,
        'summarySha256':hashlib.sha256((folder/'summary.json').read_bytes()).hexdigest(),
        'rawPath':str(folder/'transcript-00.ndjson')}
    checks.append(check); all_cache[(arm,cell)] = check
    print(len(checks), name, 'ok', flush=True)

gamma = sorted(all_cache[('C-30',c)]['scoreMs'] for c in manifest['calibration'])[14]
sealed = json.loads((SRC/'GAMMA-t38-v1.json').read_text(encoding='utf-8'))
assert gamma == sealed['gammaMs'] == 222259
tests = manifest['test']
scores_bad = [c for c in tests if all_cache[('C-30',c)]['scoreMs'] > gamma]
visible_bad = [c for c in tests if all_cache[('C-30',c)]['maxVMs'] > gamma + 30000]
summary_out = {'verifiedRuns':len(checks),'revisionCount':sum(r['revisionCount'] for r in checks),
    'gammaMs':gamma, 'visibleBoundMs':gamma+30000, 'scoreCoverage':[len(tests)-len(scores_bad),len(tests)],
    'actualVisibleCoverage':[len(tests)-len(visible_bad),len(tests)],'scoreViolations':scores_bad,'actualVisibleViolations':visible_bad,
    'maxCAll49Ms':max(r['maxCMs'] for r in checks if r['arm']=='C-30'),
    'requestDenominatorPerTestArm':sum(all_cache[('C-30',c)]['requests'] for c in tests), 'arms':{}}
for a in ARMS:
    rows = [all_cache[(a,c)] for c in tests]
    summary_out['arms'][a] = {'served':sum(r['served'] for r in rows),'meanOwnBrokenShare':statistics.mean(r['ownBrokenShare'] for r in rows),
        'pooledOwnBrokenNumerator':sum(r['ownBrokenCount'] for r in rows),'pooledOwnBrokenDenominator':sum(r['ownBrokenDenominator'] for r in rows),
        'pooledOwnBrokenShare':sum(r['ownBrokenCount'] for r in rows)/sum(r['ownBrokenDenominator'] for r in rows),
        'meanForcedShare':statistics.mean(r['forcedShare'] for r in rows),
        'pooledForcedShare':sum(r['forcedCount'] for r in rows)/sum(r['decisionCount'] for r in rows), 'meanE2':statistics.mean(r['E2'] for r in rows)}
summary_out['gapServicePp']=100*(summary_out['arms']['U']['served']-summary_out['arms']['C-30']['served'])/summary_out['requestDenominatorPerTestArm']
summary_out['gapRelativeToUPercent']=100*(summary_out['arms']['U']['served']-summary_out['arms']['C-30']['served'])/summary_out['arms']['U']['served']
(HERE/'t38-raw-checkpoint-recheck.json').write_text(json.dumps({'summary':summary_out,'runs':checks},ensure_ascii=False,indent=1),encoding='utf-8')
with (HERE/'t38-per-episode-figure-data.csv').open('w',encoding='utf-8',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=list(checks[0]));writer.writeheader();writer.writerows(checks)
print(json.dumps(summary_out,indent=2),flush=True)
