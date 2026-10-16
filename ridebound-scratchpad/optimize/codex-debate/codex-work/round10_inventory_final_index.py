from pathlib import Path
import csv,collections,json
OUT=Path(__file__).resolve().parent
def read(p):
    with p.open(encoding='utf-8',newline='') as f:return list(csv.DictReader(f,delimiter='\t'))
rows=read(OUT/'data-inventory-runs-codex-final-2026-10-08.tsv')
index=read(OUT/'data-inventory-experiment-classification-2026-10-08.tsv')
groups=collections.defaultdict(list)
lineby={r['evidence_path']:i+2 for i,r in enumerate(rows)}
for r in rows:
    if r['kind']=='run-attempt' and r['attempt']=='0':groups[r['root']+'/'+r['experiment']].append(r)
for r in index:
    rs=groups[r['experiment']]
    r['arms']=';'.join(sorted({x['normalized_arm'] for x in rs}))
    r['windows']=';'.join(sorted({x['window'] for x in rs}))
    r['specified_worlds']=';'.join(sorted({x['specified_world'] for x in rs}))
    r['inventory_line']=lineby[r['evidence_path']]
with (OUT/'data-inventory-experiment-classification-final-2026-10-08.tsv').open('x',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,list(index[0]),delimiter='\t');w.writeheader();w.writerows(index)
print('51 family classifications updated from final TSV')
