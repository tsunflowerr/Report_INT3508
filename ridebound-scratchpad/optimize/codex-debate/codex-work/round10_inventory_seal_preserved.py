"""Seal preserved independent streamed records plus all no-run-json marker directories.
No Claude inputs. No-run-json outcomes remain unknown rather than inferring trips from attempts.
"""
from pathlib import Path
import json,csv,collections,re,base64,hashlib
OUT=Path(__file__).resolve().parent
snap=json.loads((OUT/'data-inventory-codex-file-paths-2026-10-08.json').read_text())
files=[Path(p) for p in snap['files']]
with (OUT/'data-inventory-runs-codex-streamed-2026-10-08.tsv').open(encoding='utf-8',newline='') as f:rows=list(csv.DictReader(f,delimiter='\t'))
assert len(rows)==2008
fields=list(rows[0]);dirs=collections.defaultdict(list)
for p in files:dirs[p.parent].append(p)
run_dirs={Path(r['evidence_path']).parent for r in rows}
def readj(p):
    try:return json.loads(p.read_text(encoding='utf-8-sig'))
    except:return {}
def head_manifest(p):
    if not p or not p.exists():return {}
    with p.open('rb') as f:raw=f.read(262144)
    for line in raw.splitlines()[:-1]:
        try:
            z=json.loads(line);fr=json.loads(base64.b64decode(z['frameBase64']))
            if fr.get('messageType')=='initializeRun':return fr.get('payload',{}).get('manifest',{})
        except:pass
    return {}
for d,ps in sorted(dirs.items(),key=lambda t:t[0].as_posix().lower()):
    if d in run_dirs:continue
    names={p.name for p in ps}
    if not ({'bundle-manifest.json','transcript-00.ndjson','protocol-transcript.ndjson','summary.json'}&names):continue
    tr=d/'transcript-00.ndjson' if 'transcript-00.ndjson' in names else d/'protocol-transcript.ndjson' if 'protocol-transcript.ndjson' in names else None
    if tr and '/pkgs/' in tr.as_posix():continue
    root=next(r for r in snap['roots'] if d.as_posix().startswith(r+'/'))
    rel=d.as_posix()[len(root)+1:]
    exp='/'.join(rel.split('/')[:1 if root.endswith('/research') else 2])
    sj=readj(d/'summary.json');bm=readj(d/'bundle-manifest.json');man=head_manifest(tr)
    kind='protocol-output-no-run-json' if 'protocol-transcript.ndjson' in names else 'partial-or-bundle-only'
    r={k:'' for k in fields}
    evidence=d/'bundle-manifest.json' if 'bundle-manifest.json' in names else d/'summary.json' if 'summary.json' in names else tr
    r.update(kind=kind,root=root,experiment=exp,logical_run=d.name,attempt='unknown',arm=sj.get('label',d.name),cell=d.name,window='unknown',vehicles='unknown',requests='unknown',world='unknown',travel_snapshot_version='unknown',runner_commit=man.get('coreCommitSha','unknown'),runner_binary_sha256=man.get('binarySha256','unknown'),policy_id=man.get('policyId','unknown'),policy_version=man.get('policyVersion','unknown'),completed_trips='unknown',accepted='unknown',rejected='unknown',lifecycle_counts='{}',status=sj.get('status','no-run-json'),source_scenario_sha256=sj.get('sourceScenarioContentSha256','unknown'),semantic_hash=sj.get('semanticHash','unknown'),declared_transcript_sha256=next((x.get('sha256','') for x in bm.get('files',[]) if tr and x.get('path')==tr.name),''),checkpoint_coverage='not audited: no run-json terminal record',evidence_path=evidence.as_posix(),transcript_path=tr.as_posix() if tr else '',manifest_path=(d/'bundle-manifest.json').as_posix() if 'bundle-manifest.json' in names else '',notes='Marker directory retained; partial/fixture/helper status requires inspection; no completed or accepted trip inference.')
    rows.append(r)
groups=collections.defaultdict(list)
for r in rows:
    if r['declared_transcript_sha256']:groups[r['declared_transcript_sha256']].append(r)
for h,rs in groups.items():
    if len(rs)>1:
        for r in rs:r['duplicate_group']='declared-transcript:'+h
with (OUT/'data-inventory-runs-codex-independent-2026-10-08.tsv').open('x',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)
primary=[r for r in rows if r['kind']=='run-attempt' and r['attempt']=='0']
meta=dict(enumerated_file_count=len(files),counts_by_kind=dict(collections.Counter(r['kind'] for r in rows)),explicit_repeat_records=2008,primary_run00_count=len(primary),primary_experiment_count=len({r['root']+'/'+r['experiment'] for r in primary}),completed_unknown=sum(r['completed_trips']=='unknown' for r in primary),duplicate_declared_groups=sum(len(rs)>1 for rs in groups.values()),notes='Preserved all streamed explicit rows after interrupted no-run-json extraction. Every no-run-json marker directory retained with outcome unknown, not omitted.')
with (OUT/'data-inventory-codex-independent-meta-2026-10-08.json').open('x',encoding='utf-8') as f:json.dump(meta,f,indent=2)
print(json.dumps(meta,indent=2))
