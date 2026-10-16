import csv,json,math,re
from pathlib import Path
import numpy as np
ROOT=Path(r'E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work')
CLAUDE=ROOT.parent/'claude-work'
q=list(csv.DictReader((ROOT/'round11-reproduce-rider-quotes.tsv').open(newline='',encoding='utf8'),delimiter='\t'))
source=list(csv.DictReader(Path(r'C:/RideBoundData/research/ml-pilot-v1/riders-causal-2026-10-08.csv').open(newline='',encoding='utf8')))
lookup={(r['world'],r['arm'],r['cell'],r['rider']):r for r in source}
own=list(csv.DictReader((ROOT/'round11-reproduce-metrics.tsv').open(newline='',encoding='utf8'),delimiter='\t'))
for r in q:
    for k in ['F_ms','D0_ms']:r[k]=float(r[k])
original=list(csv.DictReader((CLAUDE/'ml-pilot-rows-2026-10-08.tsv').open(newline='',encoding='utf8')))
comparisons=[]; stylemetrics=[]
fields={'n':'n','Y60':'Y60_pct','early60':'early60_pct','sym':'symmetric_pct','ext':'mean_extension_s','p90':'p90_extension_s','hor':'mean_horizon_s'}
for r in original:
    if int(r['E'])!=30:continue
    day='2018-11-'+r['test'][4:];window='ALL' if r['window']=='all' else r['window']
    key=(r['world'],r['arm'],day,window,r['method'])
    selected=[x for x in q if x['version']=='stored' and (x['world'],x['arm'],x['day'],x['method'])==(r['world'],r['arm'],day,r['method']) and (window=='ALL' or x['window']==window)]
    lat=[];ext=[];hor=[]
    for x in selected:
        src=lookup[(x['world'],x['arm'],x['cell'],x['rider'])];add=(x['F_ms']-x['D0_ms'])/1000
        dlt=float(src['fc_ext_s']);h=float(src['horizon_s']);target=float(src['resid_s'])
        if x['method']=='uniform':lat.append(target+dlt-30);ext.append(30);hor.append(h+30)
        else:lat.append(target-add);ext.append(dlt+add);hor.append(h+dlt+add)
    lat=np.array(lat);ext=np.array(ext);hor=np.array(hor);n=len(selected)
    val=dict(n=n,Y60=100*float(np.sum(lat>60))/n,early60=100*float(np.sum(lat< -60))/n,sym=100*float(np.sum(np.abs(lat)<=60))/n,ext=float(np.mean(ext)),p90=float(np.sort(ext)[math.ceil(.9*n)-1]),hor=float(np.mean(hor)))
    stylemetrics.append(dict(world=r['world'],arm=r['arm'],test=r['test'],window=r['window'],E=30,method=r['method'],**val))
    for version in ['canonical','stored','stored-reported-formula']:
        match=next(x for x in own if x['version']==version and x['cohort']=='own' and (x['world'],x['arm'],x['day'],x['window'],x['method'])==key) if version!='stored-reported-formula' else None
        for field,mapped in fields.items():
            ourvalue=val[field] if version=='stored-reported-formula' else float(match[mapped]);reported=float(r[field]);rounded=round(ourvalue,3)
            comparisons.append(dict(version=version,world=r['world'],arm=r['arm'],test=r['test'],window=r['window'],method=r['method'],field=field,reported=reported,reproduced=ourvalue,reproduced_rounded=rounded,difference=ourvalue-reported,rounded_matches=abs(rounded-reported)<1e-9))
with (ROOT/'round11-reproduce-comparison.tsv').open('x',newline='',encoding='utf8') as h:
    w=csv.DictWriter(h,fieldnames=list(comparisons[0]),delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(comparisons)
with (ROOT/'round11-reproduce-reported-formula-metrics.tsv').open('x',newline='',encoding='utf8') as h:
    w=csv.DictWriter(h,fieldnames=list(stylemetrics[0]),delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(stylemetrics)
report=(CLAUDE/'ml-pilot-report-2026-10-08.txt').read_text(encoding='utf8')
ours=json.loads((ROOT/'round11-reproduce-verdicts.json').read_text(encoding='utf8'))
verdicts={k:re.search((r'  ML3.*-> (TRUE|FALSE)' if k=='ML3' else r'  '+k+r' (TRUE|FALSE)'),report).group(1)=='TRUE' for k in ['ML1','ML2','ML3','ML4','ML5']}
summary=dict(E30_rows=len(stylemetrics),numeric_comparisons_per_version=len(stylemetrics)*7,versions={v:dict(mismatches=sum(not x['rounded_matches'] for x in comparisons if x['version']==v),max_abs_difference=max(abs(x['difference']) for x in comparisons if x['version']==v)) for v in ['canonical','stored','stored-reported-formula']},verdicts=verdicts,all_verdicts_match=all(ours['stored'][k]==v for k,v in verdicts.items()),kill_match=ours['stored']['kill'] and 'KILL (ML2 and ML3 both fail): YES' in report)
with (ROOT/'round11-reproduce-comparison-summary.json').open('x',encoding='utf8') as h:json.dump(summary,h,indent=2)
print(json.dumps(summary,indent=2))
