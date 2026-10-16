"""Coverage, combinatorial checks and signed timing witnesses for route audit."""
import hashlib,json
from pathlib import Path
from collections import Counter

root=Path(__file__).parent
path=root/'retained-all-order-witnesses.json'
probe=json.loads(path.read_text())
receipt=json.loads((root/'retained-states-e1-rejected-r1/receipt.json').read_text())
saved={r['epoch']:r for r in receipt['saved']}
assert probe['allOrders'] and probe['auditHead']
assert len(probe['rows'])==len(saved)==16
assert {r['epoch'] for r in probe['rows']}==saved.keys()
physical=Counter(); witness_rows=[]
for r in probe['rows']:
    assert r['inputStateSha256']==saved[r['epoch']]['beforeSha256']
    assert r['total']==r['expectedAllOrders'] and r['maxSuffix']<=6
    assert r['baselineAccept']==r['controlAccept']==0
    assert r['physicalPass']==len(r['hardRejectedRoutes'])+r['validCount']
    assert r['total']==sum(v for k,v in r['firstWitnessCounts'].items() if k.startswith('physical:'))+r['physicalPass']
    physical.update({k:v for k,v in r['firstWitnessCounts'].items() if k.startswith('physical:')})
    for c in r['hardRejectedRoutes']:
        old={s['StopId']['Value']:s['ServiceStartTime']['Milliseconds'] for s in c['beforeSchedule']['Stops']}
        new={s['StopId']['Value']:s['ServiceStartTime']['Milliseconds'] for s in c['afterSchedule']['Stops']}
        w=c['witnesses'][0]
        kind='DropOff' if w['Dimension']=='drop_eta_total_ms' else 'Pickup'
        stop=next(s for s in c['route'] if s['request']==w['RequestId']['Value'] and s['kind']==kind)
        delta=new[stop['stop']]-old[stop['stop']]
        if w['Code']=='COMMITMENT_BUDGET_EXCEEDED':
            assert abs(delta)==w['Delta'] and w['After']==w['Before']+w['Delta']>w['Limit']
        witness_rows.append({'epoch':r['epoch'],'unchangedIncumbentOrder':c['Control'],
            'preservesHead':c['preservesHead'],'code':w['Code'],'dimension':w['Dimension'],
            'signedServiceStartShiftMs':delta,'limit':w['Limit'],'budgetBefore':w['Before']})
out={'kind':'bounded-all-orders-original-core-negative-audit',
    'sourceSha256':hashlib.sha256(path.read_bytes()).hexdigest(),
    'states':len(probe['rows']),'routesEnumerated':sum(r['total'] for r in probe['rows']),
    'maximumIncumbentMutableStops':max(r['maxSuffix'] for r in probe['rows']),
    'physicalPassRoutes':sum(r['physicalPass'] for r in probe['rows']),
    'newIncumbentOrderPhysicalPassRoutes':sum(not r['unchangedIncumbentOrder'] for r in witness_rows),
    'fullContractAcceptances':sum(r['validCount'] for r in probe['rows']),
    'firstPhysicalWitnessCounts':dict(physical),'hardWitnesses':witness_rows,
    'scope':'All incumbent suffix permutations plus one pending pickup/drop pair on each vehicle independently; existing vehicle assignments/frozen prefix/travel remain fixed; earliest-feasible schedules; no active-head screen in this final audit.',
    'notEstablished':['Global DARP infeasibility','No benefit from different earlier decisions','Closed-loop performance or held-out generalization','Optimal waiting-time scheduling','Cross-vehicle reassignment feasibility']}
(root/'all-order-probe-analysis.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
