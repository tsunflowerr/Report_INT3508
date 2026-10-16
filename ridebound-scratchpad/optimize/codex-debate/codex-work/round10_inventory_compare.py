"""Compare Claude tables only after independently sealed inventory exists."""
from pathlib import Path
import csv,json,collections,re
OUT=Path(__file__).resolve().parent
CLAUDE=OUT.parent/'claude-work'
with (OUT/'data-inventory-runs-codex-audited-2026-10-08.tsv').open(encoding='utf-8',newline='') as f:own=list(csv.DictReader(f,delimiter='\t'))
with (CLAUDE/'data-inventory-runs-2026-10-08.tsv').open(encoding='utf-8',newline='') as f:cl=list(csv.DictReader(f,delimiter='\t'))
primary={str(Path(r['evidence_path']).parent.as_posix()).lower():r for r in own if r['kind']=='run-attempt' and r['attempt']=='0'}
def path_of(r):
    run=r['run'].replace('\\','/')
    if run.startswith('tier3-'):return ('C:/RideBoundData/research/'+run).lower()
    return ('E:/RideBoundData/'+run).lower()
clmap={path_of(r):r for r in cl}
missing=sorted(set(primary)-set(clmap));extra=sorted(set(clmap)-set(primary))
diffs=[]
for p in sorted(set(primary)&set(clmap)):
    a=primary[p];b=clmap[p]
    for af,bf in [('requests','req'),('vehicles','veh'),('accepted','acc'),('travel_snapshot_version','snap'),('status','status')]:
        if a[af]!=b[bf]:diffs.append(dict(path=p,field=af,own=a[af],claude=b[bf],type='value'))
    # E experiment fields are a relative prefix; C fields are corrupt in raw TSV.
    expected=a['experiment'] if a['root'].startswith('E:') else 'C:research/'+a['experiment']
    if expected!=b['exp']:diffs.append(dict(path=p,field='exp',own=expected,claude=b['exp'],type='grouping'))
bytext=(CLAUDE/'data-inventory-by-experiment-2026-10-08.txt').read_text(encoding='utf-8')
bycounts={}
for line in bytext.splitlines():
    m=re.match(r'^([^|]+) \| (\d+) \|',line)
    if m:bycounts[m.group(1).strip()]=int(m.group(2))
coarse=collections.Counter(('E:'+r['experiment']) if r['root'].startswith('E:') else ('C:research/'+r['experiment']) for r in primary.values())
expdiff=[{'experiment':k,'own':coarse.get(k,0),'claude':bycounts.get(k,0)} for k in sorted(set(coarse)|set(bycounts)) if coarse.get(k,0)!=bycounts.get(k,0)]
with (OUT/'data-inventory-claude-discrepancies-2026-10-08.tsv').open('x',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,['path','field','own','claude','type'],delimiter='\t');w.writeheader();w.writerows(diffs)
summary=dict(own_run00=len(primary),claude_run00=len(cl),own_experiments=len(coarse),claude_experiments=len(bycounts),missing_paths=missing,extra_paths=extra,comparable_value_mismatches=sum(r['type']=='value' for r in diffs),raw_tsv_grouping_mismatches=sum(r['type']=='grouping' for r in diffs),by_experiment_count_discrepancies=expdiff,claude_accepted_is_not_completed='Stored acc matches accepted IDs, not an independent lifecycle completion audit.',additional_own_categories=dict(collections.Counter(r['kind'] for r in own if not(r['kind']=='run-attempt' and r['attempt']=='0'))))
with (OUT/'data-inventory-claude-comparison-2026-10-08.json').open('x',encoding='utf-8') as f:json.dump(summary,f,indent=2)
print(json.dumps(summary,indent=2))
