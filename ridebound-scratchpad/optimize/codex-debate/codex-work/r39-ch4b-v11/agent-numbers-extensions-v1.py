"""Additional R39 checks injected before report serialization by the create-only generator.
Uses names/functions from the inspected R37 pure read-only probe; no external writes.
"""
import re

say('G. R39 matched morning promise-break counts from raw transcript ledgers')
report['morning_promise_breaks'] = {}
for arm in ['Mplus-30', 'Mplus-30F']:
    members = [x for x in morning_count_rows if x['arm'] == arm]
    assert len(members) == 8 and len({x['cell'] for x in members}) == 8
    aggregate = {'scenarios': len(members), 'served': sum(x['served'] for x in members),
                 'late30': sum(x['late30'] for x in members),
                 'scenario_mean_pct': statistics.mean(100*x['late30']/x['served'] for x in members),
                 'per_run': members}
    report['morning_promise_breaks'][arm] = aggregate
    say(arm+' morning '+json.dumps(aggregate, ensure_ascii=True, sort_keys=True))
assert {x['cell'] for x in report['morning_promise_breaks']['Mplus-30']['per_run']} == {x['cell'] for x in report['morning_promise_breaks']['Mplus-30F']['per_run']}
assert round(report['morning_promise_breaks']['Mplus-30']['scenario_mean_pct'], 1) == 39.0
assert round(report['morning_promise_breaks']['Mplus-30F']['scenario_mean_pct'], 1) == 11.0

say('H. R39 34-scenario original obligation from independently extracted IVC cache')
cells_main=json.loads((S/'tang3/t38/split-t38-v1.json').read_text(encoding='utf-8'))['test']
assert len(cells_main)==34 and len(set(cells_main))==34
cache=S/'tang3/t38/independent/cache'
report['main_original_obligation']={}
for arm in ['Mplus-30', 'C-30']:
    members=[]
    for cell in cells_main:
        paths=[p for p in (cache/(arm+'-'+cell+'.json'),cache/(arm+'-'+cell+'-rerun1.json')) if p.exists()]
        assert len(paths)==1
        data=json.loads(paths[0].read_text(encoding='utf-8'))
        assert data['status']=='pass' and data['requests']==108 and set(data['riders'])==set(data['alight'])
        late30=sum(data['alight'][rid]-rider['p0_drop']>30000 for rid,rider in data['riders'].items())
        breach=late30 if arm=='Mplus-30' else sum(sum(abs(v['p_d']-v['e_d']) for v in q['rev'])>30000 for q in data['riders'].values())
        members.append({'cell':cell,'served':data['served'],'ack':data['acked'],'forced':data['nonNormalAcked'],
                        'breach':breach,'source':str(paths[0])})
    aggregate={'scenarios':len(members),'requests':34*108, 'served':sum(x['served'] for x in members),
               'ack':sum(x['ack'] for x in members),'forced':sum(x['forced'] for x in members),
               'breach':sum(x['breach'] for x in members),'positive_breach_scenarios':sum(x['breach']>0 for x in members),
               'forced_scenario_mean_pct':statistics.mean(100*x['forced']/x['ack'] for x in members), 'per_run':members}
    report['main_original_obligation'][arm]=aggregate
    say(arm+' main original '+json.dumps(aggregate,ensure_ascii=True,sort_keys=True))
assert [report['main_original_obligation']['Mplus-30'][k] for k in ['served','ack','forced','positive_breach_scenarios']] == [2338,20103,7710,28]
assert round(report['main_original_obligation']['Mplus-30']['forced_scenario_mean_pct'],1)==41.3
assert report['main_original_obligation']['C-30']['forced']==report['main_original_obligation']['C-30']['breach']==0

say('I. R39 padding cohort totals, derived differences and forecast oracle cohort')
byarm={arm:[r for r in cx['runs'] if r['arm']==arm] for arm in ['U','C-30','C-120']}
counts={arm:{'scenarios':len(rr),'requests':sum(r['requests'] for r in rr),'served':sum(len(r['riders']) for r in rr),
             'exposed':sum(x['absolute_dispatch_ms']>0 for r in rr for x in r['riders']),
             'max_absolute_dispatch_s':max(x['absolute_dispatch_ms'] for r in rr for x in r['riders'])/1000,
             'forced':sum(r['non_normal_decisions'] for r in rr),
             'ack':sum(r['acknowledged_decisions'] for r in rr)} for arm,rr in byarm.items()}
assert counts['U']['scenarios']==counts['C-30']['scenarios']==34
assert counts['U']['requests']==counts['C-30']['requests']==3672
assert counts['U']['served']==2434 and counts['C-30']['served']==2338
assert counts['U']['exposed']==174 and round(counts['U']['max_absolute_dispatch_s'],1)==590.1
assert round(counts['C-30']['max_absolute_dispatch_s'],1)==29.2
assert counts['C-30']['forced']==0 and counts['C-30']['ack']==20101
assert counts['C-120']['forced']==0 and counts['C-120']['ack']==20435
same=0
u_bycell={r['cell']:r for r in byarm['U']}
for r in byarm['C-30']:
    same+=len(set(r['served_ids']) & set(u_bycell[r['cell']]['served_ids']))
assert same==2207
unpad=next(x for x in report['padding'] if x['arm']=='C-30' and x['pad_s']==0)
upad=next(x for x in report['padding'] if x['arm']=='U' and x['pad_s']==30)
ratio=upad['mean_extension_s']/unpad['mean_extension_s']
assert round(ratio,2)==5.05
shared_path=S/'rewrite-2026-10/evidence/checks-addendum-1/recompute-addendum-1-2026-10-11.txt'
shared_text=shared_path.read_text(encoding='utf-8')
shared={arm:tuple(map(int,re.search(r'^- '+re.escape(arm)+r': (\d+) of (\d+) served',shared_text,re.M).groups())) for arm in ['U','C-30']}
assert shared=={'U':(555,2434),'C-30':(313,2338)}
report['cohort_totals']={'by_arm':counts,'served_difference':counts['U']['served']-counts['C-30']['served'],
    'common_served':same,'extension_ratio_upad30_c30':ratio,'shared_read_counts':shared,
    'shared_difference':shared['U'][0]-shared['C-30'][0], 'shared_source':str(shared_path)+':136-140'}
assert report['cohort_totals']['served_difference']==96 and report['cohort_totals']['shared_difference']==242
all_c=[r for r in rows if r['arm']=='C-30']
active_c=[r for r in all_c if r['cell'][7:9] in ['14','15','16']]
oracle={'scenarios':len(all_c),'oracle_n':sum(int(r['oracle_n']) for r in all_c),'oracle_ok':sum(int(r['oracle_ok']) for r in all_c),
        'active_scenarios':len(active_c),'active_oracle_n':sum(int(r['oracle_n']) for r in active_c),
        'ext_mean_scenario_s':statistics.mean(float(r['ext_mean_s']) for r in active_c),
        'ext_morning_mean_scenario_s':statistics.mean(float(r['ext_mean_s']) for r in active_c if r['cell'].endswith('w07')),
        'pick_ext_mean_scenario_s':statistics.mean(float(r['pick_ext_mean_s']) for r in active_c)}
assert oracle['scenarios']==34 and oracle['oracle_n']==oracle['oracle_ok']==2305 and oracle['active_oracle_n']==1452
assert round(oracle['ext_mean_scenario_s'],1)==13.7 and round(oracle['ext_morning_mean_scenario_s'],1)==27.8 and round(oracle['pick_ext_mean_scenario_s'],1)==3.2
report['forecast_oracle_and_price']=oracle
say('cohort totals '+json.dumps(report['cohort_totals'],ensure_ascii=True,sort_keys=True))
say('forecast oracle/price '+json.dumps(oracle,sort_keys=True))

say('J. R39 test attempt 4: read saved full-run log only')
test_log=R/'testrun-45f8026-eollf-dirty-fullrun-2026-10-13.log'
test_text=test_log.read_text(encoding='utf-8-sig')
matches=list(re.finditer(r'^Passed!\s+- Failed:\s+(\d+), Passed:\s+(\d+), Skipped:\s+(\d+), Total:\s+(\d+).*$',test_text,re.M))
totals=[sum(int(m.group(i)) for m in matches) for i in range(1,5)]
assert len(matches)==9 and totals==[0,1025,0,1025] and re.search(r'^exit=0$',test_text,re.M)
assert '2026-10-13T13:42:21+07:00' in test_text
evidence_path=S/'rewrite-2026-10/evidence/TESTRUN-45f8026-2026-10-12.md'
evidence=evidence_path.read_text(encoding='utf-8')
attempt4=next(line for line in evidence.splitlines() if line.startswith('| 4 (2026-10-13'))
assert '1.025 / 1.025' in attempt4 and 'untracked marker present' in attempt4 and 'full suite in ONE run' in attempt4
assert '| 3 | `core.autocrlf=false`, `core.eol=lf`' in evidence
report['test_attempt4']={'log':str(test_log),'evidence':str(evidence_path)+':18','project_rows':len(matches),
    'failed':totals[0],'passed':totals[1],'skipped':totals[2],'total':totals[3],'exit':0,'completion':'2026-10-13T13:42:21+07:00',
    'conditions':['LF checkout','untracked marker present'],'attempt4_evidence_row':attempt4,
    'project_log_rows':[m.group(0) for m in matches]}
say('test attempt 4 '+json.dumps(report['test_attempt4'],ensure_ascii=True,sort_keys=True))
