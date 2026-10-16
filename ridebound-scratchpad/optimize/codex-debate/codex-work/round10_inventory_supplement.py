"""Independent supplemental ledger, legacy run-store, FleetPy CSV audit; no Claude imports."""
from pathlib import Path
import json,csv,re,hashlib,collections
OUT=Path(__file__).resolve().parent
snapshot=json.loads((OUT/'data-inventory-codex-file-paths-2026-10-08.json').read_text())
files=[Path(p) for p in snapshot['files']]; file_set=set(files)
rows=[]
def j(p):
    try:return json.loads(p.read_text(encoding='utf-8-sig'))
    except:return {}
def base(kind,p):
    root=next((r for r in snapshot['roots'] if p.as_posix().startswith(r+'/')),'')
    rel=p.parent.as_posix()[len(root)+1:]
    return dict(kind=kind,root=root,experiment=rel,logical_run=p.parent.name,attempt='unknown',arm='unknown',cell='unknown',window='unknown',vehicles='unknown',requests='unknown',world='unknown',runner_era='unknown',completed_trips='unknown',status='unknown',sha256=hashlib.sha256(p.read_bytes()).hexdigest(),duplicate_group='',evidence_path=p.as_posix(),linked_evidence='',notes='')
for p in sorted(files):
    if p.name=='attempt-start.json':
        x=j(p);term=p.parent/'attempt-terminal.json';t=j(term)
        r=base('ledger-attempt',p);r.update(experiment=r['experiment'].split('/ledger/')[0],logical_run=x.get('jobId',p.parent.parent.name),attempt=x.get('attemptNumber','unknown'),runner_era=x.get('freezeId','unknown'),status=t.get('exitClassification','no-terminal-record'),linked_evidence=term.as_posix() if term.exists() else '',notes='Ledger attempts are not experimental units. May overlap nested run-00 outputs; no completed-trip claim for mechanics tests.')
        rows.append(r)
    elif p.name=='run-record.json':
        x=j(p);r=base('legacy-run-store-record',p)
        r.update(experiment=r['experiment'].split('/run-store/')[0].split('/data/runs/')[0],logical_run=x.get('runId',p.parent.name),attempt=x.get('attemptIndex','unknown'),arm=x.get('armId','unknown'),cell=x.get('scenarioHash','unknown'),runner_era=x.get('runnerArtifactSha256','unknown'),status=x.get('terminalStatus','unknown'),notes='Legacy oracle/input-output experiment; completed trips not extracted from old output schema. Copies retained and exact record-byte duplicates labelled.')
        rows.append(r)
    elif p.name=='1_user-stats.csv':
        with p.open(encoding='utf-8-sig',newline='') as f:data=list(csv.DictReader(f))
        r=base('fleetpy-calibration-csv-run',p);conf=p.parent/'00_config.json';x=j(conf).get('scenario_parameters',{})
        final=p.parent/'final_state.csv'
        with final.open(encoding='utf-8-sig',newline='') as f:vehicles=len(list(csv.DictReader(f)))
        c=re.search(r'd\d{8}_s\d+_r\d+',p.parent.name)
        r.update(experiment=r['experiment'].rsplit('/',1)[0],arm=x.get('op_rp_batch_optimizer','unknown'),cell=c.group(0) if c else 'unknown',vehicles=vehicles,requests=len(data),world='NetworkBasic; no dynamic-network directory declared' if x.get('network_type')=='NetworkBasic' and not x.get('nw_dynamic_folder') else 'unknown',runner_era='FleetPy-1.0.2 calibration',completed_trips=sum(bool(z.get('dropoff_time','').strip()) for z in data),status='saved-CSV; no independent exit-status proof',linked_evidence=conf.as_posix(),notes='Completed means nonempty actual dropoff_time; independently count CSV rows. Simulated targets, not actual observed taxi rider travel times. Windows unknown from outputs alone.')
        rows.append(r)
    elif p.name=='final_state.csv' and p.parent/'1_user-stats.csv' not in file_set:
        r=base('fleetpy-initial-state-fixture',p)
        with p.open(encoding='utf-8-sig',newline='') as f:data=list(csv.DictReader(f))
        r.update(experiment=r['experiment'].rsplit('/',1)[0],vehicles=len(data),requests=0,completed_trips=0,status='fixture-only; no user-stats output',runner_era='FleetPy-1.0.2 calibration',notes='Initial positions, not a service-outcome run.')
        rows.append(r)
# Exact record-byte duplicates: declarations alone do not certify whole output equivalence.
groups=collections.defaultdict(list)
for r in rows:groups[(r['kind'],r['sha256'])].append(r)
for (kind,h),rs in groups.items():
    if len(rs)>1:
        for r in rs:r['duplicate_group']='exact-evidence-file:'+h
with (OUT/'data-inventory-supplement-codex-independent-2026-10-08.tsv').open('x',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
meta=dict(counts_by_kind=dict(collections.Counter(r['kind'] for r in rows)),exact_file_duplicate_groups=sum(len(rs)>1 for rs in groups.values()),missing_ledger_terminals=sum(r['kind']=='ledger-attempt' and r['status']=='no-terminal-record' for r in rows),fleetpy_completed_by_arm={a:sum(r['completed_trips'] for r in rows if r['kind']=='fleetpy-calibration-csv-run' and r['arm']==a) for a in sorted({r['arm'] for r in rows if r['kind']=='fleetpy-calibration-csv-run'})})
with (OUT/'data-inventory-supplement-codex-meta-2026-10-08.json').open('x',encoding='utf-8') as f:json.dump(meta,f,indent=2)
print(json.dumps(meta,indent=2))
