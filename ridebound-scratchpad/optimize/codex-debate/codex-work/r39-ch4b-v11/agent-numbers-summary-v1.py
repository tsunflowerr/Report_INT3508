"""R39 compact numeric summary and fresh forecast-ledger arithmetic.
Read only inputs, exclusive output in this directory, no fitting/build/simulation.
"""
import csv
import json
import statistics
from decimal import Decimal
from pathlib import Path

S=Path('E:/Code/Report_INT3508/ridebound-scratchpad')
O=Path(__file__).resolve().parent
primary=json.loads((O/'agent-numbers-v1.json').read_text(encoding='utf-8'))
report={'dispatcher_morning':{}}
for name,arm in [('forecast','Mplus-30F'),('baseline','Mplus-30')]:
    p=primary['morning_promise_breaks'][arm]
    report['dispatcher_morning'][name]={'scenarios':p['scenarios'],'served':p['served'],
        'broken':p['late30'],'scenario_mean_pct':p['scenario_mean_pct'],
        'pooled_pct':100*p['late30']/p['served'],'source':'agent-numbers-v1.json:morning_promise_breaks.'+arm}
report['dispatcher_paired']={k:{field:val for field,val in p.items() if field!='raw_run_counts'}
    for k,p in primary['dispatcher']['paired'].items()}
with (S/'optimize/test-family-a-causal-no15-2026-10-06-cells.tsv').open(encoding='utf-8',newline='') as f:
    rows=list(csv.DictReader(f,delimiter='\t'))
active=[r for r in rows if r['arm']=='C-30' and r['cell'][7:9] in ['14','15','16']]
assert len(active)==21 and sum(int(r['served']) for r in active)==1471
components={name:sum(Decimal(r['ledger_'+name+'_s']) for r in active)
    for name in ['dispatch','anticipated','unanticipated','total']}
assert all(round(components[k],3)==Decimal(v) for k,v in [
    ('dispatch','81.742'),('anticipated','5352.646'),('unanticipated','783.018'),('total','6217.406')])
assert abs(sum(components[k] for k in ['dispatch','anticipated','unanticipated'])-components['total'])<Decimal('0.000001')
late=sum(round(float(r['Y_naive'])*int(r['served'])) for r in active)
assert late==68
share=components['anticipated']/components['total']*100
assert round(share,1)==Decimal('86.1')
report['forecast_ledger']={'scenarios':len(active),'served':1471,'late_naive_count':late,
    'components_s':{k:str(v) for k,v in components.items()},'historical_pct':str(share),
    'integer_labels':[round(components[k]) for k in ['dispatch','anticipated','unanticipated']],
    'integer_total_label':round(components['total']),
    'integer_components_sum':sum(round(components[k]) for k in ['dispatch','anticipated','unanticipated']),
    'source':'S/optimize/test-family-a-causal-no15-2026-10-06-cells.tsv: C-30 days14-16 ledger_* columns'}
assert report['forecast_ledger']['integer_components_sum']==6218 and report['forecast_ledger']['integer_total_label']==6217
ml_source=S/'optimize/codex-debate/claude-work/ml_pilot_run.py'
ml=ml_source.read_text(encoding='utf-8')
assert 'Y60=100 * float(np.sum(lat > 60)) / n' in ml
assert 'early60=100 * float(np.sum(lat < -60)) / n' in ml
assert 'round(mm["Y60"], 3), round(mm["early60"], 3)' in ml
halfwidth=max(Decimal(metric['count_halfwidth']) for r in primary['ml'] for metric in [r['Y60'],r['early60']])
assert halfwidth==Decimal('0.004035')
report['ml_count_provenance']={'derived_from_rounded_percentage':True,'rounding_halfwidth_pct':'0.0005',
    'max_count_halfwidth':str(halfwidth),'method':'every integer 0..n enumerated; exactly one compatible in each used row',
    'rows':len(primary['ml']),'source':str(ml_source)+':37-42,175-176',
    'limitation':'arithmetic compatibility only, no retraining or per-rider prediction revalidation'}
report['test_attempt4']={k:v for k,v in primary['test_attempt4'].items() if k not in ['project_log_rows','attempt4_evidence_row']}
with (O/'agent-numbers-summary-v1.json').open('x',encoding='utf-8',newline='\n') as f:
    json.dump(report,f,ensure_ascii=False,indent=2)
with (O/'agent-numbers-summary-v1.txt').open('x',encoding='utf-8',newline='\n') as f:
    f.write(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=True,indent=2))
