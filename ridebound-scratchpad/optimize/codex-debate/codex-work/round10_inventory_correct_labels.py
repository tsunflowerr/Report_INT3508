"""Correct filename-derived labels; retain pre-comparison evidence snapshot unchanged."""
from pathlib import Path
import csv,re,json,collections
OUT=Path(__file__).resolve().parent
with (OUT/'data-inventory-runs-codex-audited-2026-10-08.tsv').open(encoding='utf-8',newline='') as f:rows=list(csv.DictReader(f,delimiter='\t'))
corrections=[]
for r in rows:
    old={k:r.get(k) for k in ('normalized_arm','cell','window')}
    p=Path(r['evidence_path'])
    candidates=[r.get('arm',''),r.get('logical_run','')]+[x.name for x in p.parents]
    job=next((s for s in candidates if re.search(r'd\d{8}(?:-s\d+)?-r\d+',s)),r.get('arm','unknown'))
    r['logical_job']=job
    r['physical_directory']=p.parent.as_posix()
    cm=re.search(r'd\d{8}(?:[-_]s\d+)?[-_]r\d+(?:[-_]w\d+)?',job)
    if cm:
        cell=cm.group(0);r['cell']=cell
        wm=re.search(r'[-_]w\d+$',cell)
        r['window']=wm.group(0)[1:] if wm else 'unknown-source-window'
        prefix=job[:cm.start()].rstrip('-_');suffix=job[cm.end():].strip('-_')
        suffix=re.sub(r'[-_]s\d+(?:[-_].*)?$','',suffix)
        prefix=re.sub(r'-W[0-5]$','',prefix)
        if re.match(r'^(?:U|C-\d+|Mplus-\d+|M-\d+|V-\d+|fr-|dl-|dl2-|conduct-|dr-|dw-|df-|sf-|rt-)',prefix):normal=prefix
        elif re.search(r'^(?:b\d|c\d|visible\d+)',suffix):normal=suffix
        elif prefix=='lc':normal='lc-warning60-hard120'
        elif prefix=='ww':normal=suffix or prefix
        elif prefix.startswith('f-') and suffix:normal=suffix
        else:normal=prefix if prefix not in ('s','x','w14','p') else suffix or 'unknown-policy'
        r['normalized_arm']=normal
        r['normalized_arm_provenance']='canonical job label/path syntax; cell-local window token; no policy-equivalence inference'
    if old!={k:r.get(k) for k in old}:corrections.append({'path':r['evidence_path'],'before':old,'after':{k:r.get(k) for k in old}})
fields=list(rows[0])
for r in rows:
    for k in r:
        if k not in fields:fields.append(k)
with (OUT/'data-inventory-runs-codex-corrected-2026-10-08.tsv').open('x',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)
primary=[r for r in rows if r['kind']=='run-attempt' and r['attempt']=='0']
groups=collections.defaultdict(list)
for r in primary:groups[r['root']+'/'+r['experiment']].append(r)
meta={'correction_count':len(corrections),'record_count':len(rows),'primary_experiment_count':len(groups),'experiments':{k:{'runs':len(rs),'arms':sorted({r['normalized_arm'] for r in rs}),'windows':sorted({r['window'] for r in rs}),'vehicles':sorted({r['vehicles'] for r in rs}),'requests':sorted({r['requests'] for r in rs}),'completed_known':sum(int(r['completed_trips']) for r in rs if r['completed_trips'].isdigit()),'completed_unknown':sum(r['completed_trips']=='unknown' for r in rs),'example_path':rs[0]['evidence_path']} for k,rs in sorted(groups.items())},'corrections':corrections}
with (OUT/'data-inventory-codex-corrected-meta-2026-10-08.json').open('x',encoding='utf-8') as f:json.dump(meta,f,indent=2)
print(json.dumps({'records':len(rows),'corrections':len(corrections),'wp14r_v6':meta['experiments']['E:/RideBoundData/wp14r/development-v6-ledger']},indent=2))
