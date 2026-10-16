"""Enrich and combine independently sealed inventory before Claude comparison. Exclusive outputs."""
from pathlib import Path
import csv,json,re,collections,hashlib
OUT=Path(__file__).resolve().parent
main=OUT/'data-inventory-runs-codex-independent-2026-10-08.tsv'
supp=OUT/'data-inventory-supplement-codex-independent-2026-10-08.tsv'
def read(p):
    with p.open(encoding='utf-8',newline='') as f:return list(csv.DictReader(f,delimiter='\t'))
rows=read(main)+read(supp)
for r in rows:
    label=r.get('arm','unknown');logical=r['logical_run'];exp=r['experiment'];search=logical+' '+label
    cm=re.search(r'd\d{8}(?:-s\d+)?-r\d+(?:-w\d+)?',search)
    wm=re.search(r'(?:^|[- ])(w\d+)(?:[- ]|$)',search)
    if cm and (r.get('cell')=='unknown' or r.get('kind')=='ledger-attempt' or not re.search(r'd\d{8}',r.get('cell',''))):r['cell']=cm.group(0)
    if wm and r.get('window')=='unknown':r['window']=wm.group(1)
    before=re.split(r'-d\d{8}',logical,1)[0]
    policy=re.search(r'(?:^|-)((?:b1|c1|c2)(?:-[A-Za-z0-9]+)*)',before)
    if not policy:policy=re.search(r'(?:^|-)((?:b1|c1|c2)(?:-[A-Za-z0-9]+)*)',logical)
    normal=policy.group(1) if policy else re.split(r'-d\d{8}',label,1)[0]
    normal=re.sub(r'-s\d+$','',normal);normal=re.sub(r'-W[0-5]$','',normal)
    if r['kind']=='ledger-attempt' and not cm:
        normal='N/A-mechanics-or-helper';r['cell']='N/A-mechanics-or-helper';r['window']='N/A-mechanics-or-helper'
    if r['kind']=='legacy-run-store-record':
        for key in ('vehicles','requests','world','completed_trips'):r[key]='N/A-protocol-or-oracle-run; physical-trip-target-unverified'
    r['normalized_arm']=normal
    r['normalized_arm_provenance']='filename/label syntax; no new causal equivalence claim'
    r['summary_status']='N/A'
    r['summary_path']=''
    if r['kind']=='run-attempt':
        sp=Path(r['evidence_path']).parent/'summary.json'
        if sp.exists():
            try:sj=json.loads(sp.read_text(encoding='utf-8-sig'));r['summary_status']=sj.get('status','unknown');r['summary_path']=sp.as_posix()
            except Exception as e:r['summary_status']='parse-error:'+str(e)
        else:r['summary_status']='absent'
    elif r['kind']=='partial-or-bundle-only':
        ep=Path(r['evidence_path']);sp=ep.parent/'summary.json'
        if sp.exists():
            sj=json.loads(sp.read_text(encoding='utf-8-sig'));r['summary_status']=sj.get('status','unknown');r['summary_path']=sp.as_posix()
    if r.get('world')=='time-varying-observed':r['world']='multiple-snapshot-updates-observed; numeric-variation-not-audited'
    elif r.get('world')=='static-no-update-observed':r['world']='final-snapshot-version-1; numeric-constancy-not-audited'
    m=re.search(r'(?:^|-)W([0-5])(?:-|$)',logical)
    r['specified_world']='unknown; inspect source driver'
    if m:r['specified_world']='W0 static with repeated snapshots' if m.group(1)=='0' else 'W'+m.group(1)+' time-varying specified world; source sweep design'
    elif r.get('world','').startswith('final-snapshot-version-1'):r['specified_world']='single-snapshot execution; static-world candidate'
    elif 'NetworkBasic' in r.get('world',''):r['specified_world']='static NetworkBasic configuration; no dynamic folder declared'
    elif r.get('root')=='C:/RideBoundData/research' and 'tier3-' in exp and r.get('travel_snapshot_version','unknown') not in ('unknown','1'):
        r['specified_world']='time-varying measured-profile configuration; actual numeric changes not independently certified'
    if r.get('completed_trips')=='unknown':r['notes']=r.get('notes','')+'; completed lifecycle unavailable: retained final checkpoint not extracted or transcript absent; accepted is not substituted'
fields=[]
for r in rows:
    for k in r:
        if k not in fields:fields.append(k)
with (OUT/'data-inventory-runs-codex-audited-2026-10-08.tsv').open('x',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)
prim=[r for r in rows if r['kind']=='run-attempt' and r['attempt']=='0']
exps=collections.defaultdict(list)
for r in prim:exps[r['root']+'/'+r['experiment']].append(r)
meta=dict(combined_rows=len(rows),counts_by_kind=dict(collections.Counter(r['kind'] for r in rows)),primary_run00_count=len(prim),primary_experiment_count=len(exps),primary_field_unknown={k:sum(r.get(k,'unknown')=='unknown' for r in prim) for k in ('vehicles','requests','world','runner_commit','completed_trips')},primary_summary_status=dict(collections.Counter(r['summary_status'] for r in prim)),completed_unknown_paths=[r['evidence_path'] for r in prim if r['completed_trips']=='unknown'],input_snapshots={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (main,supp)},experiments={k:dict(runs=len(rs),arms=sorted({r['normalized_arm'] for r in rs}),vehicles=sorted({r['vehicles'] for r in rs}),requests=sorted({r['requests'] for r in rs}),windows=sorted({r['window'] for r in rs}),world_observations=dict(collections.Counter(r['world'] for r in rs)),specified_worlds=sorted({r['specified_world'] for r in rs}),summary_status=dict(collections.Counter(r['summary_status'] for r in rs)),completed_known=sum(int(r['completed_trips']) for r in rs if r['completed_trips'].isdigit()),completed_unknown=sum(r['completed_trips']=='unknown' for r in rs),example_path=rs[0]['evidence_path']) for k,rs in sorted(exps.items())})
with (OUT/'data-inventory-codex-audited-meta-2026-10-08.json').open('x',encoding='utf-8') as f:json.dump(meta,f,indent=2)
print(json.dumps({k:v for k,v in meta.items() if k!='experiments'},indent=2))
