import csv,json
from pathlib import Path
ROOT=Path(r'E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work')
rows=list(csv.DictReader((ROOT/'round11-reproduce-metrics.tsv').open(newline='',encoding='utf8'),delimiter='\t'))
key=lambda r:(r['world'],r['arm'],r['day'],r['window'],r['cohort'],r['method'])
c={key(r):r for r in rows if r['version']=='canonical'};s={key(r):r for r in rows if r['version']=='stored'}
fields=['Y60_pct','early60_pct','symmetric_pct','mean_extension_s','p90_extension_s','mean_horizon_s']
summary={f:dict(zip(['key','canonical','stored','abs_difference'],max([(k,float(c[k][f]),float(s[k][f]),abs(float(c[k][f])-float(s[k][f]))) for k in c if k[4]=='own'],key=lambda t:t[3]))) for f in fields}
cal=list(csv.DictReader((ROOT/'round11-reproduce-calibration.tsv').open(newline='',encoding='utf8'),delimiter='\t'));ck=lambda r:(r['world'],r['arm'],r['method']);cc={ck(r):r for r in cal if r['version']=='canonical'};ss={ck(r):r for r in cal if r['version']=='stored'}
summary['rho_max_difference']=dict(zip(['key','canonical','stored','abs_difference'],max([(k,float(cc[k]['rho']),float(ss[k]['rho']),abs(float(cc[k]['rho'])-float(ss[k]['rho']))) for k in cc if cc[k]['rho']],key=lambda t:t[3])))
with (ROOT/'round11-reproduce-rounding-sensitivity.json').open('x',encoding='utf8') as h:json.dump(summary,h,indent=2)
print(json.dumps(summary,indent=2))
