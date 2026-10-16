import csv,json,math
from pathlib import Path
import numpy as np
ROOT=Path(r'E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work')
rows=list(csv.DictReader((ROOT/'round11-reproduce-rider-quotes.tsv').open(newline='',encoding='utf8'),delimiter='\t'))
for r in rows:
    for k in ['F_ms','A_ms','P0_ms','D0_ms','error_s','extension_s']:r[k]=float(r[k])
def metrics(rr):
    n=len(rr);e=np.array([r['error_s'] for r in rr]);x=np.array([r['extension_s'] for r in rr])
    return dict(n=n,late60=int(np.sum(e>60)),early60=int(np.sum(e< -60)),within60=int(np.sum(np.abs(e)<=60)),Y60_pct=float(np.mean(e>60)*100),early60_pct=float(np.mean(e< -60)*100),symmetric_pct=float(np.mean(np.abs(e)<=60)*100),mean_extension_s=float(np.mean(x)),p90_extension_s=float(np.sort(x)[math.ceil(.9*n)-1]))
out=[]; verdict=[]
for ver in ['canonical','stored']:
    for world,arm,day in [('measured','U',d) for d in ['2018-11-15','2018-11-16']]+[('static',a,'2018-11-13') for a in ['FREE','LOCKS']]:
        ref={(r['cell'],r['rider']):r for r in rows if (r['version'],r['world'],r['arm'],r['day'],r['method'])==(ver,world,'C-30',day,'fc+uniform')}
        for model in ['HGB','HGB-nostate','LinQR']:
            learner={(r['cell'],r['rider']):r for r in rows if (r['version'],r['world'],r['arm'],r['day'],r['method'])==(ver,world,arm,day,model)}
            keys=sorted(set(ref)&set(learner));assert keys,(world,arm,day)
            m=metrics([learner[k] for k in keys]);c=metrics([ref[k] for k in keys])
            out.append(dict(version=ver,world=world,pair_policy=arm,day=day,method=model,reference_method='C-30/fc+uniform',reference_n=c['n'],reference_Y60_pct=c['Y60_pct'],reference_symmetric_pct=c['symmetric_pct'],reference_mean_extension_s=c['mean_extension_s'],reference_p90_extension_s=c['p90_extension_s'],own_policy_n=len(learner),reference_own_n=len(ref),**m))
            verdict.append(dict(version=ver,world=world,arm=arm,day=day,method=model,n=len(keys),matches_y=m['Y60_pct']<=c['Y60_pct'],matches_symmetric=m['symmetric_pct']>=c['symmetric_pct'],jointly_matches=m['Y60_pct']<=c['Y60_pct'] and m['symmetric_pct']>=c['symmetric_pct'],mean_extension_difference_s=m['mean_extension_s']-c['mean_extension_s'],p90_extension_difference_s=m['p90_extension_s']-c['p90_extension_s']))
with (ROOT/'round11-reproduce-common-pairwise.tsv').open('x',newline='',encoding='utf8') as h:
    w=csv.DictWriter(h,fieldnames=list(out[0]),delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(out)
with (ROOT/'round11-reproduce-common-pairwise-verdicts.json').open('x',encoding='utf8') as h:json.dump(verdict,h,indent=2)
print('pairwise supplement saved',len(out))
