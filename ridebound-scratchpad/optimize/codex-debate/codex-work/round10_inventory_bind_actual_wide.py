from pathlib import Path
import csv,json,hashlib,collections
OUT=Path(__file__).resolve().parent
with (OUT/'data-inventory-runs-codex-final-2026-10-08.tsv').open(encoding='utf-8',newline='') as f:rows=list(csv.DictReader(f,delimiter='\t'))
wide=Path('E:/RideBoundData/wp14/wide-window-fixture');mapping={}
for p in wide.glob('*/scenario-content.json'):
    cpath=p.parent/'normalizer-configuration.json';c=json.loads(cpath.read_text(encoding='utf-8-sig'))
    actual=hashlib.sha256(p.read_bytes()).hexdigest()
    d=json.loads((p.parent/'derivative-manifest.json').read_text(encoding='utf-8-sig'))
    mapping[actual]=(c,cpath,p,d.get('scenarioContentSha256'))
wide_filled=0;csv_filled=0
for r in rows:
    r['simulation_window_seconds']='unknown'
    r['fixture_metadata_note']=''
    h=r.get('source_scenario_sha256','')
    if h in mapping:
        c,cp,p,declared=mapping[h];start=c['sourceWindowStartSeconds'];end=c['sourceWindowEndSeconds']
        r['source_window_seconds']=str(start)+'..'+str(end);r['window']='w%02d'%(int(start)//3600)
        r['window_provenance']=cp.as_posix()+':1; ACTUAL scenario-content file SHA matches run; builder changes pickup window only'
        r['fixture_metadata_note']='Copied derivative scenario hash is stale; config pickupWindowMs is stale. Source-window fields copied unchanged; see E:/Code/Report_INT3508/ridebound-scratchpad/window/build_wide_fixture.py:11.'
        wide_filled+=1
    if r['kind']=='fleetpy-calibration-csv-run':
        cp=Path(r['evidence_path']).parent/'00_config.json';s=json.loads(cp.read_text(encoding='utf-8-sig'))['scenario_parameters']
        r['simulation_window_seconds']=str(s['start_time'])+'..'+str(s['end_time'])
        r['window']='relative-simulation-window; source-clock-unknown'
        r['window_provenance']=cp.as_posix()+':1; relative simulation horizon includes drain; no source-clock inference'
        csv_filled+=1
fields=list(rows[0])
with (OUT/'data-inventory-runs-codex-final-v2-2026-10-08.tsv').open('x',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)
primary=[r for r in rows if r['kind']=='run-attempt' and r['attempt']=='0']
meta={'rows':len(rows),'primary_records':len(primary),'wide_actual_file_hash_bindings':wide_filled,'fleetpy_relative_windows_filled':csv_filled,'unknown_primary_windows':sum(r['window'].startswith('unknown') for r in primary),'configured_world_unknown_primary':sum(r['specified_world'].startswith('unknown') for r in primary),'rows_sha256':hashlib.sha256((OUT/'data-inventory-runs-codex-final-v2-2026-10-08.tsv').read_bytes()).hexdigest()}
with (OUT/'data-inventory-codex-final-v2-meta-2026-10-08.json').open('x',encoding='utf-8') as f:json.dump(meta,f,indent=2)
with (OUT/'data-inventory-experiment-classification-final-v2-2026-10-08.tsv').open(encoding='utf-8',newline='') as f:index=list(csv.DictReader(f,delimiter='\t'))
groups=collections.defaultdict(list)
for r in primary:groups[r['root']+'/'+r['experiment']].append(r)
for r in index:r['windows']=';'.join(sorted({z['window'] for z in groups[r['experiment']]}))
with (OUT/'data-inventory-experiment-classification-final-v3-2026-10-08.tsv').open('x',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,list(index[0]),delimiter='\t');w.writeheader();w.writerows(index)
print(json.dumps(meta,indent=2))
