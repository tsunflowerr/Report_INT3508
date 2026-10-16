"""Independent Round-10 saved-run inventory. No Claude scripts or tables imported.
Writes only beneath this script's directory, exclusive creation. Transcript head/final checkpoint
subtrees are read, not whole histories; full transcript hashes are NOT certified.
"""
from pathlib import Path
import json, csv, re, hashlib, base64, collections, os
ROOTS=[Path('E:/RideBoundData'),Path('C:/RideBoundData/research')]
OUT=Path(__file__).resolve().parent
SKIP={'envs','.git','node_modules','__pycache__','.venv','venv'}
files=[]; skipped=[]; errors=[]
for root in ROOTS:
    for dp,ds,ns in os.walk(root):
        for d in list(ds):
            if d in SKIP:
                skipped.append(str(Path(dp)/d));ds.remove(d)
        files.extend(Path(dp)/n for n in ns)
bydir=collections.defaultdict(list)
for p in files: bydir[p.parent].append(p)
def readj(p):
    try:return json.loads(p.read_text(encoding='utf-8-sig'))
    except Exception as e: return {'_read_error':str(e)}
def rootrel(p):
    for r in ROOTS:
        try:return r.as_posix(),p.relative_to(r).as_posix()
        except ValueError:pass
    return '',p.as_posix()
def frames_head(p):
    if not p or not p.exists():return []
    with p.open('rb') as f: raw=f.read(262144)
    result=[]
    for line in raw.splitlines()[:-1]:
        try:
            row=json.loads(line)
            fr=json.loads(base64.b64decode(row['frameBase64'])) if 'frameBase64' in row else row
            if isinstance(fr,dict):result.append(fr)
        except Exception:pass
    return result

def checkpoint_tail(p):
    if not p or not p.exists():return {},'absent'
    size=p.stat().st_size
    with p.open('rb') as f:
        f.seek(max(0,size-8388608));raw=f.read()
    # Whole short frames or a giant checkpoint frame whose JSON requests subtree is near its end.
    lines=raw.splitlines(); frames=[]
    for line in lines[-5:]:
        try:
            row=json.loads(line); fr=json.loads(base64.b64decode(row['frameBase64']))
            if fr.get('messageType')=='checkpoint':
                return fr['payload']['content']['onlineState'],'full-final-checkpoint-frame; hash-not-certified'
        except Exception:pass
    # Last giant frame can precede shutdown or can itself be final. Decode only its b64 tail.
    ends=list(re.finditer(rb'\",\"frameLengthBytes\":',raw))
    for end in reversed(ends):
        chunk=raw[:end.start()]
        # Base64 payload length is a multiple of four; discard an incomplete leading quartet.
        nl=chunk.rfind(b'\n')
        chunk=chunk[nl+1:]
        if b'\"frameBase64\":\"' in chunk:
            chunk=chunk.split(b'\"frameBase64\":\"',1)[1]
        chunk=chunk[len(chunk)%4:]
        try:decoded=base64.b64decode(chunk).decode('utf-8',errors='replace')
        except Exception:continue
        marker='\"requests\":['; start=decoded.rfind(marker)
        if start<0:continue
        try:
            req,consumed=json.JSONDecoder().raw_decode(decoded[start+len('\"requests\":'):])
            if not isinstance(req,list):continue
            tail=decoded[start+len('\"requests\":')+consumed:]
            tt=tail.find('\"travelTimes\":')
            vt=tail.find('\"vehicles\":')
            st={'requests':req}
            if tt>=0:st['travelTimes']=json.JSONDecoder().raw_decode(tail[tt+len('\"travelTimes\":'):])[0]
            if vt>=0:st['vehicles']=json.JSONDecoder().raw_decode(tail[vt+len('\"vehicles\":'):])[0]
            return st,'final-checkpoint-tail-subtrees; hash-not-certified'
        except Exception:pass
    return {},'not-extracted'

runpaths=sorted([p for p in files if re.fullmatch(r'run-\d+\.json',p.name)],key=lambda p:p.as_posix().lower())
rows=[]
for index,p in enumerate(runpaths):
    j=readj(p); s=j.get('semantic',{}); root,rel=rootrel(p.parent)
    attempt=int(re.search(r'run-(\d+)',p.name).group(1))
    transcript=p.parent/('transcript-%02d.ndjson'%attempt)
    head=frames_head(transcript)
    init=next((f for f in head if f.get('messageType')=='initializeRun'),{})
    manifest=init.get('payload',{}).get('manifest',{})
    final,coverage=checkpoint_tail(transcript)
    life=collections.Counter(r.get('lifecycle','unknown') for r in final.get('requests',[]))
    req=s.get('requestCount','unknown'); vehicles=len(s['finalVehiclePositions']) if 'finalVehiclePositions' in s else len(final.get('vehicles',[])) or 'unknown'
    tv=s.get('travelSnapshotVersion',final.get('travelTimes',{}).get('version'))
    world='time-varying-observed' if isinstance(tv,int) and tv>1 else 'static-no-update-observed' if tv==1 else 'unknown'
    label=j.get('label',p.parent.name)
    cell=re.search(r'(d\d{8}-s\d+-r\d+(?:-w\d+)?)',p.parent.name)
    window=re.search(r'(?:^|-)(w\d+)(?:-|$)',p.parent.name)
    win=window.group(1) if window else 'unknown'
    mh=p.parent/'bundle-manifest.json'; bm=readj(mh) if mh.exists() else {}
    th=next((x.get('sha256','') for x in bm.get('files',[]) if x.get('path')==transcript.name),'')
    rows.append(dict(kind='run-attempt',root=root,experiment=rel.rsplit('/',1)[0] if '/' in rel else '.',logical_run=p.parent.name,attempt=attempt,arm=label,cell=cell.group(1) if cell else p.parent.name,window=win,vehicles=vehicles,requests=req,world=world,travel_snapshot_version=tv if tv is not None else 'unknown',runner_commit=manifest.get('coreCommitSha','unknown'),runner_binary_sha256=manifest.get('binarySha256','unknown'),policy_id=manifest.get('policyId','unknown'),policy_version=manifest.get('policyVersion','unknown'),completed_trips=life.get('completed',0) if final else 'unknown',accepted=len(s['acceptedRequestIds']) if 'acceptedRequestIds' in s else 'unknown',rejected=len(s['rejectedRequestIds']) if 'rejectedRequestIds' in s else 'unknown',lifecycle_counts=json.dumps(life,sort_keys=True),status=j.get('status','unknown'),source_scenario_sha256=s.get('sourceScenarioContentSha256','unknown'),semantic_hash=j.get('semanticHash','unknown'),run_json_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),declared_transcript_sha256=th,checkpoint_coverage=coverage,evidence_path=p.as_posix(),transcript_path=transcript.as_posix() if transcript.exists() else '',manifest_path=mh.as_posix() if mh.exists() else '',duplicate_group='',notes='window from directory token only; static means version 1, not simulator constant-world proof'))
    if index%200==0: print('inventoried',index+1,flush=True)
# Keep artifacts with no run-*.json in separate rows; never pretend these are completed runs.
run_dirs={p.parent for p in runpaths}
for d,ps in sorted(bydir.items(),key=lambda x:x[0].as_posix().lower()):
    if d in run_dirs:continue
    names={p.name for p in ps}
    if not ({'bundle-manifest.json','transcript-00.ndjson','protocol-transcript.ndjson','summary.json'}&names):continue
    # A genuine summary/bundle/transcript directory is an auditable saved output even if partial.
    root,rel=rootrel(d)
    tr=d/'transcript-00.ndjson' if 'transcript-00.ndjson' in names else d/'protocol-transcript.ndjson' if 'protocol-transcript.ndjson' in names else None
    if tr and '/pkgs/' in tr.as_posix():continue
    kind='protocol-output-no-run-json' if 'protocol-transcript.ndjson' in names else 'partial-or-bundle-only'
    bm=readj(d/'bundle-manifest.json') if 'bundle-manifest.json' in names else {}
    sj=readj(d/'summary.json') if 'summary.json' in names else {}
    final,cov=checkpoint_tail(tr)
    life=collections.Counter(x.get('lifecycle','unknown') for x in final.get('requests',[]))
    head=frames_head(tr); ini=next((f for f in head if f.get('messageType')=='initializeRun'),{});man=ini.get('payload',{}).get('manifest',{})
    tv=final.get('travelTimes',{}).get('version')
    rows.append(dict(kind=kind,root=root,experiment=rel.rsplit('/',1)[0] if '/' in rel else '.',logical_run=d.name,attempt='unknown',arm=sj.get('label',d.name),cell=d.name,window='unknown',vehicles=len(final.get('vehicles',[])) or 'unknown',requests=len(final.get('requests',[])) or 'unknown',world='time-varying-observed' if isinstance(tv,int) and tv>1 else 'static-no-update-observed' if tv==1 else 'unknown',travel_snapshot_version=tv or 'unknown',runner_commit=man.get('coreCommitSha','unknown'),runner_binary_sha256=man.get('binarySha256','unknown'),policy_id=man.get('policyId','unknown'),policy_version=man.get('policyVersion','unknown'),completed_trips=life.get('completed',0) if final else 'unknown',accepted='unknown',rejected='unknown',lifecycle_counts=json.dumps(life,sort_keys=True),status=sj.get('status','no-run-json'),source_scenario_sha256=sj.get('sourceScenarioContentSha256','unknown'),semantic_hash=sj.get('semanticHash','unknown'),run_json_sha256='',declared_transcript_sha256=next((x.get('sha256','') for x in bm.get('files',[]) if tr and x.get('path')==tr.name),''),checkpoint_coverage=cov,evidence_path=(d/'bundle-manifest.json').as_posix() if 'bundle-manifest.json' in names else (d/'summary.json').as_posix() if 'summary.json' in names else tr.as_posix(),transcript_path=tr.as_posix() if tr else '',manifest_path=(d/'bundle-manifest.json').as_posix() if 'bundle-manifest.json' in names else '',duplicate_group='',notes='Excluded from primary run-00 experiment count; fixture/example/failed-attempt status not automatically inferred'))
# Transcript digests are declarations, not re-hashed full transcript proofs.
groups=collections.defaultdict(list)
for i,r in enumerate(rows):
    if r['declared_transcript_sha256']:groups[r['declared_transcript_sha256']].append(i)
for h,indices in groups.items():
    if len(indices)>1:
        for i in indices: rows[i]['duplicate_group']='declared-transcript:'+h
fields=list(rows[0])
with (OUT/'data-inventory-runs-codex-independent-2026-10-08.tsv').open('x',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)
primary=[r for r in rows if r['kind']=='run-attempt' and r['attempt']==0]
exp=collections.defaultdict(list)
for r in primary:exp[r['root']+'/'+r['experiment']].append(r)
meta=dict(roots=[r.as_posix() for r in ROOTS],enumerated_file_count=len(files),skipped_directories=skipped,read_errors=errors,counts_by_kind=dict(collections.Counter(r['kind'] for r in rows)),attempt_count=sum(r['kind']=='run-attempt' for r in rows),primary_run00_count=len(primary),primary_experiment_count=len(exp),completed_unknown=sum(r['completed_trips']=='unknown' for r in primary),era_unknown=sum(r['runner_commit']=='unknown' for r in primary),duplicate_declared_groups=sum(len(x)>1 for x in groups.values()),experiments={k:dict(runs=len(rs),vehicles=sorted({str(r['vehicles']) for r in rs}),requests=sorted({str(r['requests']) for r in rs}),worlds=dict(collections.Counter(r['world'] for r in rs)),completed_known=sum(r['completed_trips'] for r in rs if isinstance(r['completed_trips'],int)),completed_unknown=sum(r['completed_trips']=='unknown' for r in rs),arms=sorted({str(r['arm']) for r in rs}),evidence=rs[0]['evidence_path']) for k,rs in sorted(exp.items())})
with (OUT/'data-inventory-codex-independent-meta-2026-10-08.json').open('x',encoding='utf-8') as f:json.dump(meta,f,indent=2)
print(json.dumps({k:v for k,v in meta.items() if k not in ('experiments','skipped_directories')},indent=2),flush=True)
