"""Independent R37 read-only probes. No imports from experiment scripts; no simulation or fitting.
Only small report files are exclusive-created in this script's directory.
"""
import base64
import csv
import hashlib
import json
import math
import statistics
from collections import Counter
from decimal import Decimal
from pathlib import Path

S = Path('E:/Code/Report_INT3508/ridebound-scratchpad')
R = Path('C:/RideBoundData/research')
O = Path(__file__).parent
log = (O / 'verify-numbers-v2.txt').open('x', encoding='utf-8')
report = {}
lines = []

def say(s):
    lines.append(s)
    log.write(s + '\n')
    log.flush()
    print(s, flush=True)

def table(p, delimiter=','):
    with p.open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter=delimiter))

def frames(p):
    with p.open(encoding='utf-8') as f:
        for line in f:
            outer = json.loads(line)
            raw = base64.b64decode(outer['frameBase64'])
            assert hashlib.sha256(raw).hexdigest() == outer['frameSha256'], str(p)
            yield outer['direction'], json.loads(raw)

def manifest(p):
    with p.open(encoding='utf-8') as f:
        for i, line in enumerate(f):
            outer = json.loads(line)
            raw = base64.b64decode(outer['frameBase64'])
            assert hashlib.sha256(raw).hexdigest() == outer['frameSha256']
            frame = json.loads(raw)
            if frame.get('messageType') == 'initializeRun':
                return frame['payload']['manifest']
            assert i < 8, str(p)
    raise ValueError(str(p))

def raw_run(p, need_ledger=False):
    decisions, acknowledged, arrivals, state = {}, set(), {}, None
    for direction, frame in frames(p):
        kind, payload = frame.get('messageType'), frame.get('payload', {})
        if direction == 'runnerToAdapter' and kind == 'decision':
            decisions[payload['decisionHash']] = (payload.get('certificate', {}).get('body') or {}).get('normalOperation') is False
        elif direction == 'adapterToRunner' and kind == 'decisionApplied':
            acknowledged.add(payload['decisionHash'])
        elif need_ledger and direction == 'adapterToRunner' and kind == 'eventBatch':
            for event in payload.get('events', []):
                if event.get('eventType') == 'passengerAlighted':
                    arrivals.setdefault(event['payload']['requestId'], frame['simTimeMs'])
        elif need_ledger and direction == 'runnerToAdapter' and kind == 'checkpoint':
            state = payload['content']['onlineState']
    assert acknowledged <= set(decisions), str(p)
    answer = {'ack': len(acknowledged), 'forced': sum(decisions[h] for h in acknowledged)}
    if need_ledger:
        assert state is not None
        riders = []
        for history in state['commitmentLedger']:
            request = history['requestId']
            if request not in arrivals:
                continue
            entries = history['entries']
            assert entries[0]['kind'] == 'initialPromise'
            initial = entries[0]['publishedPromise']
            changes = []
            for e in entries[1:]:
                c = e['publishedPromise']['projection']['dropEtaMs'] - e['exogenousProjection']['dropEtaMs']
                assert abs(c) == e['deltas']['decisionInduced']['dropEtaTotalMs']
                changes.append(c)
            riders.append({'request': request, 't0': initial['publishedAtMs'],
                           'P0': initial['projection']['dropEtaMs'], 'A': arrivals[request],
                           'dispatch': sum(changes), 'absolute_dispatch': sum(map(abs, changes))})
        answer['riders'] = riders
    return answer

say('A. Family-A exact saved cell shares, independently inverted per cell')
rows = table(S / 'optimize/test-family-a-causal-no15-2026-10-06-cells.tsv', '\t')
report['forecast'] = []
metrics = ['Y_naive', 'Y_pad', 'Y_disp', 'E_naive', 'E_pad', 'E_disp']
for arm in ['C-30', 'Mplus-30', 'V-30', 'U']:
    active = [r for r in rows if r['arm'] == arm and r['cell'][7:9] in ['14', '15', '16']]
    for window in ['all', 'w07', 'w08', 'w17']:
        rs = active if window == 'all' else [r for r in active if r['cell'].endswith(window)]
        result = {'arm': arm, 'window': window, 'scenarios': len(rs), 'served': sum(int(r['served']) for r in rs)}
        for metric in metrics:
            values = [Decimal(r[metric]) * int(r['served']) for r in rs]
            counts = [int(v.to_integral_value()) for v in values]
            residual = max(abs(v-k) for v,k in zip(values,counts))
            assert residual < Decimal('1e-10')
            result[metric] = sum(counts)
            result[metric+'_scenario_mean_pct'] = statistics.mean(float(r[metric])*100 for r in rs)
        report['forecast'].append(result)
        say(f"{arm} {window}: n={result['served']}, scenarios={len(rs)}, counts={[result[m] for m in metrics]}")
assert [r for r in report['forecast'] if r['arm']=='C-30' and r['window']=='all'][0]['Y_pad'] == 22

say('B. Independent Codex per-rider extraction: active U/C counts and padding opening')
cx = json.loads((S / 'optimize/codex-debate/codex-work/R19-stage1a-analysis.json').read_text(encoding='utf-8'))
report['padding'] = []
for arm in ['U','C-30','C-120']:
    runs = [r for r in cx['runs'] if r['arm']==arm]
    riders = [x for r in runs for x in r['riders']]
    for pad in [0, 30, 60]:
        late = lambda x, threshold: x['arrival']-x['forecast_quote']-1000*pad > threshold*1000
        early = sum(x['arrival']-x['forecast_quote']-1000*pad < -60000 for x in riders)
        item = {'arm':arm,'pad_s':pad,'served':len(riders),'late60':sum(late(x,60) for x in riders),
                'late120':sum(late(x,120) for x in riders),'late300':sum(late(x,300) for x in riders),
                'late600':sum(late(x,600) for x in riders),'early60':early,
                'mean_extension_s':statistics.mean((x['forecast_quote']-x['P0'])/1000+pad for x in riders),
                'exposed':sum(x['absolute_dispatch_ms']>0 for x in riders),
                'max_dispatch_s':max(x['absolute_dispatch_ms'] for x in riders)/1000}
        item['timely60']=len(riders)-item['late60']
        item['timely120']=len(riders)-item['late120']
        report['padding'].append(item)
        say(str(item))
    if arm in ['U','C-30']:
        for window in ['all','w07','w08','w17']:
            active=[r for r in runs if r['cell'][7:9] in ['14','15','16'] and (window=='all' or r['cell'].endswith(window))]
            people=[x for r in active for x in r['riders']]
            check={'arm':arm,'window':window,'n':len(people),'naive':sum(x['arrival']-x['P0']>60000 for x in people),
                   'forecast':sum(x['arrival']-x['forecast_quote']>60000 for x in people)}
            say('independent rider check '+str(check))
            matching=next(r for r in report['forecast'] if r['arm']==arm and r['window']==window)
            assert [check['n'],check['naive'],check['forecast']]==[matching['served'],matching['Y_naive'],matching['Y_disp']]
            if arm=='C-30':
                k=sum(x['forecast_quote']-x['P0'] for x in people)/sum(x['P0']-x['t0'] for x in people) if window!='all' else None
                if k is not None:
                    count=sum(x['arrival']-x['P0']-k*(x['P0']-x['t0'])>60000 for x in people)
                    assert count==matching['Y_pad']
                    say(f'independent proportional-pad check {window}: k={k:.12f}, late={count}')

say('C. ML counts: enumerate every integer compatible with 3-decimal percentage rounding')
ml=table(S/'optimize/codex-debate/claude-work/ml-pilot-rows-a1-2026-10-08.tsv')
want={('measured','U','test15'),('measured','U','test16'),('measured','C-30','test15'),('measured','C-30','test16'),('static','FREE','test13')}
report['ml']=[]
for r in ml:
    if (r['world'],r['arm'],r['test']) not in want or r['window']!='all' or r['E']!='30':
        continue
    item={k:r[k] for k in ['world','arm','test','method','n','ext','p90']}
    n=int(r['n'])
    for column in ['Y60','early60']:
        rate=Decimal(r[column])
        compatible=[k for k in range(n+1) if abs(Decimal(100)*k/n-rate)<=Decimal('0.0005')]
        assert len(compatible)==1,(r,compatible)
        item[column]={'rate_pct':str(rate),'unique_count':compatible[0],
                      'count_halfwidth':str(Decimal('0.0005')*n/100),
                      'center_residual':str(abs(rate*n/100-compatible[0]))}
    report['ml'].append(item)
    say(f"{r['world']} {r['arm']} {r['test']} {r['method']}: {item['Y60']['unique_count']}/{n} late, {item['early60']['unique_count']}/{n} early")

say('D. Snow identity: every manifest, actual DLL and canonical recovery configuration binding')
snowdirs=sorted((R/'tier3-forecast-v1').glob('C-30-d20181115-s10-r?-w1[45]'))
maindirs=sorted(p for p in (R/'tier3-t38-v1').iterdir() if p.is_dir() and p.name.startswith('C-30-'))
fields=['binarySha256','coreCommitSha','policyId','policyVersion','policyConfigurationHash']
keys={label:Counter(tuple(manifest(p/'transcript-00.ndjson')[k] for k in fields) for p in folders)
      for label,folders in [('snow',snowdirs),('main',maindirs)]}
assert len(snowdirs)==8 and len(maindirs)==51
assert len(keys['snow'])==len(keys['main'])==1 and list(keys['snow'])==list(keys['main'])
key=next(iter(keys['snow']))
dll=hashlib.sha256((R/'runner-tier3-v2/RideBound.Runner.dll').read_bytes()).hexdigest()
assert dll==key[0]
canonical=lambda p:hashlib.sha256(json.dumps(json.loads(p.read_text(encoding='utf-8')),sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).digest()
wp4=S/'tang3/configs/wp4-tier3-v2.json'
policy=S/'tang3/configs/C-30.json'
binding=hashlib.sha256(b'RideBound.Wp4RunnerConfigurationBinding.v1\x00'+canonical(policy)+canonical(wp4)).hexdigest()
assert binding==key[4]
recovery=json.loads(wp4.read_text(encoding='utf-8'))['commitmentRecovery']
report['identity']={'snow_runs':8,'main_folders':51,'manifest':dict(zip(fields,key)), 'dll_matches':True,
                    'canonical_binding_recomputed':binding,'recovery':recovery}
say(str(report['identity']))

say('E. Snow ledger: own streaming transcript decoder and own historical-factor integrator')
factors=Path('E:/RideBoundData/wp6/extracted/sha256/d9/d9e86f33645e5eec287d387f8d63ad41ddf41d4ef648138b65d636482e2c599e/FleetPy_Manhattan/networks/Manhattan_2019_corrected/tt_factors')
if not factors.exists():
    world=(S/'tang3/world/preflight_world.py').read_text(encoding='utf-8')
    import re
    match=re.search(r'FACTORS = pathlib.Path\((.*?)\)',world,re.S)
    factors=Path(''.join(re.findall(r'r?"([^"]+)"',match.group(1))))

def profile(day,start):
    rows=sorted((int(r['simulation_time'])-start,float(r['travel_time_factor'])) for r in table(factors/f'{day}_tt_factors.csv') if start<=int(r['simulation_time'])<=start+7200)
    assert rows[0][0]==0
    return [next(v for t,v in reversed(rows) if t<=b*900) for b in range(9)]

def historical(t,p,prof):
    b0=int(t//900000)
    remaining=float(p-t)
    if remaining<=0:
        return float(p)
    now=float(t)
    while True:
        b=int(now//900000)
        multiplier=1 if b==b0 else prof[min(b,8)]/prof[min(b0,8)]
        end=(b+1)*900000
        work=(end-now)/multiplier
        if work>=remaining:
            return max(p,now+remaining*multiplier)
        remaining-=work
        now=float(end)

snow=[]
perrun=[]
for p in snowdirs:
    raw=raw_run(p/'transcript-00.ndjson',True)
    start={'w14':50400,'w15':54000}[p.name[-3:]]
    prof=[statistics.mean([profile(d,start)[b] for d in ['2018-11-12','2018-11-13','2018-11-14']]) for b in range(9)]
    riders=raw.pop('riders')
    for x in riders:
        x['D0']=historical(x['t0'],x['P0'],prof)
    snow.extend(riders)
    item={'run':p.name,'served':len(riders),'late_naive':sum(x['A']-x['P0']>60000 for x in riders),
          'late_forecast':sum(x['A']-x['D0']>60000 for x in riders),**raw}
    perrun.append(item)
late=[x for x in snow if x['A']-x['P0']>60000]
total=sum(x['A']-x['P0'] for x in late)/1000
dispatch=sum(x['dispatch'] for x in late)/1000
explain=sum(x['D0']-x['P0'] for x in late)/1000
report['snow']={'per_run':perrun,'served':len(snow),'late_naive':len(late),'late_forecast':sum(x['A']-x['D0']>60000 for x in snow),
                 'late_naive_scenario_mean_pct':statistics.mean(100*x['late_naive']/x['served'] for x in perrun),
                 'late_forecast_scenario_mean_pct':statistics.mean(100*x['late_forecast']/x['served'] for x in perrun),
                 'total_s':total,'dispatch_s':dispatch,'dispatch_pct':100*dispatch/total,
                 'historical_s':explain,'residual_s':total-dispatch-explain,
                 'max_absolute_dispatch_s':max(x['absolute_dispatch'] for x in snow)/1000}
assert len(snow)==601 and len(late)==41 and total==3445.933 and dispatch==8.566
say(str(report['snow']))

say('F. K=2, completion census, paired forced-decision counts from raw runs and BIC')
cells=[f'd201811{day}-s10-r{rep}-{window}' for window in ['w07','w08'] for day,reps in [('14',[3,4]),('15',[1,2,4]),('16',[1,2,4])] for rep in reps]
bic=table(S/'optimize/independent-B/b_cells.tsv','\t')
completed={arm:[c for c in cells if (R/'tier3-forecast-v1'/f'{arm}F-{c}'/'summary.json').exists()] for arm in ['C-30','Mplus-30']}
assert [len(completed[a]) for a in ['C-30','Mplus-30']]==[14,15]
configs={day:json.loads((S/f'optimize/configs/forecast-k2-2018-11-{day}.json').read_text(encoding='utf-8')) for day in ['14','15','16']}
assert all(x['horizonBins']==2 for x in configs.values())
report['dispatcher']={'K':2,'completed':{a:len(v) for a,v in completed.items()},'configurations':configs,'paired':{}}
for arm in ['C-30','Mplus-30']:
    for suffix in ['', 'F']:
        matched=[r for r in bic if r['arm']==arm+suffix and r['cell'] in completed[arm]]
        assert len(matched)==len(completed[arm])
        aggregate={'runs':len(matched),'ack':sum(int(x['ack']) for x in matched),'forced':sum(int(x['nonNormal']) for x in matched),
                   'scenario_mean_pct':statistics.mean(int(x['nonNormal'])/int(x['ack'])*100 for x in matched)}
        if suffix or arm=='Mplus-30':
            raw_counts=[]
            for x in matched:
                folder=R/('tier3-forecast-v1' if suffix else 'tier3-t38-v1')/f"{arm}{suffix}-{x['cell']}"
                if not suffix and not (folder / 'summary.json').exists() and (folder.parent / (folder.name + '-rerun1')).exists():
                    folder = folder.parent / (folder.name + '-rerun1')
                if not folder.exists():
                    candidates=list(folder.parent.glob(folder.name+'*'))
                    raise ValueError(f'Need effective run directory: {folder}; {candidates}')
                raw=raw_run(folder/'transcript-00.ndjson')
                assert raw=={'ack':int(x['ack']),'forced':int(x['nonNormal'])}, (folder,raw,x)
                raw_counts.append({'cell':x['cell'],**raw})
            aggregate['raw_run_counts']=raw_counts
        report['dispatcher']['paired'][arm+suffix]=aggregate
        say(f'{arm}{suffix}: {aggregate["forced"]}/{aggregate["ack"]}, scenario mean {aggregate["scenario_mean_pct"]:.8f}%')

report['figure_rounding']={'sum_integer_labels':82+5353+783,'total_integer_label':6217,
                         'sum_one_decimal_labels':float(Decimal('81.7')+Decimal('5352.6')+Decimal('783.0')),
                         'full_precision_sum':float(Decimal('81.742')+Decimal('5352.646')+Decimal('783.018'))}
with (O/'verify-numbers-v2.json').open('x',encoding='utf-8') as f:
    json.dump(report,f,ensure_ascii=False,indent=2)
log.flush()
say('All numeric assertions passed; saved verify-numbers-v2.json and verify-numbers-v2.txt')
