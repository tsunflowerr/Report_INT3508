"""Complete configured-world/source-window provenance without changing recorded outcomes."""
from pathlib import Path
import csv,json,re,collections,hashlib
OUT=Path(__file__).resolve().parent
with (OUT/'data-inventory-runs-codex-corrected-2026-10-08.tsv').open(encoding='utf-8',newline='') as f:rows=list(csv.DictReader(f,delimiter='\t'))
snap=json.loads((OUT/'data-inventory-codex-file-paths-2026-10-08.json').read_text())
configs=[Path(p) for p in snap['files'] if p.endswith('/normalizer-configuration.json')]
fixture_root=Path('C:/Code/RideBound-noworse/benchmarks/fixtures/wp6/public/fleetpy-manhattan-v1')
configs+=list(fixture_root.rglob('normalizer-configuration.json'))
source_map={}
for p in configs:
    try:
        c=json.loads(p.read_text(encoding='utf-8-sig'));d=json.loads((p.parent/'derivative-manifest.json').read_text(encoding='utf-8-sig'))
        h=d['scenarioContentSha256'];source_map[h]=(c,p)
    except:pass
matched=0
for r in rows:
    r['specified_world_source']=''
    job=r.get('logical_job','')
    km=re.search(r'(?:^|-)k(025|05|0|1|2)(?:-|$)',job)
    if km and ('deadline-v1' in r['experiment'] or '/drift' in '/'+r['experiment']):
        k=km.group(1)
        r['specified_world']='static flat configuration (k0)' if k=='0' else 'time-varying injected measured-profile configuration (k'+k+')'
        fname='deadline/run_deadline.py:1' if 'deadline-v1' in r['experiment'] else 'drift/run_drift_frac.py:20' if 'drift-frac' in r['experiment'] else 'drift/run_drift.py:16'
        r['specified_world_source']='E:/Code/Report_INT3508/ridebound-scratchpad/'+fname
    h=r.get('source_scenario_sha256','')
    r['source_window_seconds']='unknown'
    r['window_provenance']='canonical job token only' if not r.get('window','unknown').startswith('unknown') else 'unknown'
    if h in source_map:
        c,p=source_map[h];start=c.get('sourceWindowStartSeconds');end=c.get('sourceWindowEndSeconds')
        if start is not None and end is not None:
            r['source_window_seconds']=str(start)+'..'+str(end)
            r['window']='w%02d'%(int(start)//3600) if int(start)%3600==0 else str(start)+'..'+str(end)
            r['window_provenance']=p.as_posix()+':1; derivative scenarioContentSha256 matches run source scenario'
            matched+=1
fields=list(rows[0])
for r in rows:
    for k in r:
        if k not in fields:fields.append(k)
with (OUT/'data-inventory-runs-codex-final-2026-10-08.tsv').open('x',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)
primary=[r for r in rows if r['kind']=='run-attempt' and r['attempt']=='0']
meta={'rows':len(rows),'primary_records':len(primary),'source_hash_window_matches':matched,'unknown_primary_windows':sum(r['window'].startswith('unknown') for r in primary),'configured_world_unknown_primary':sum(r['specified_world'].startswith('unknown') for r in primary),'source_configurations':len(configs),'rows_sha256':hashlib.sha256((OUT/'data-inventory-runs-codex-final-2026-10-08.tsv').read_bytes()).hexdigest()}
with (OUT/'data-inventory-codex-final-meta-2026-10-08.json').open('x',encoding='utf-8') as f:json.dump(meta,f,indent=2)
print(json.dumps(meta,indent=2))
