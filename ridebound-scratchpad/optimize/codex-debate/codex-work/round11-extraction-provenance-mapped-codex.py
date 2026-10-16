"""Map proven static source duplicates to actual causal CSV rows; own typed-string SHA registry formula, no Claude imports."""
import csv,hashlib,json,sys
from pathlib import Path
from collections import Counter
sys.dont_write_bytecode=True
H=Path(__file__).resolve().parent
meta=json.loads((H/'round11-extraction-provenance-codex.json').read_text())
CSV=Path('C:/RideBoundData/research/ml-pilot-v1/riders-causal-2026-10-08.csv')
rows=list(csv.DictReader(CSV.read_text().splitlines()))
index={(r['world'],r['arm'],r['cell'],r['rider']):{**r,'csv_line':i} for i,r in enumerate(rows,2)}
TAGS={'FREE':'b1-ref','LOCKS':'c1-nobudget','C-120':'c1-budget120','C-60':'c1-budget60','C-30':'c1-h6ref'}
def runtime(stable):
    val=stable.encode('utf-8');return 'rq-'+hashlib.sha256(b's'+len(val).to_bytes(8,'big')+val).hexdigest()
checks=[];missing=[];hashbad=[];prefixbad=[]
for f in meta['fixtures']:
    cell=f['cell'];fixture=Path('E:/Code/RideBound/benchmarks/fixtures/wp6/public/fleetpy-manhattan-v1/wp14-development-panel-v1')/cell
    sc=json.loads((fixture/'scenario-content.json').read_text());allowed={runtime(e['stableSubjectId'])[:16] for e in sc['events'] if e['eventType']=='requestArrived'}
    for arm,tag in TAGS.items():
        p=Path('E:/RideBoundData/wp14r/development-v6-ledger')/f'w14-{cell}-{tag}-s7/attempt-01/output/run-00.json';run=json.loads(p.read_text())
        if run['semantic']['sourceScenarioContentSha256']!=f['scenario_sha256']:hashbad.append({'cell':cell,'arm':arm})
        bad=[r['rider'] for r in rows if r['world']=='static' and r['arm']==arm and r['cell']==cell and r['rider'] not in allowed]
        if bad:prefixbad.append({'cell':cell,'arm':arm,'bad':bad})
for p in meta['overlap_pairs']:
    fitrid=runtime(p['fit_stable_subject']);calrid=runtime(p['cal_stable_subject'])
    for arm in TAGS:
        a=index.get(('static',arm,p['fit_cell'],fitrid[:16]));b=index.get(('static',arm,p['cal_cell'],calrid[:16]))
        row={'original_request_id':p['request_id'],'arm':arm,'fit_cell':p['fit_cell'],'cal_cell':p['cal_cell'],'fit_runtime_id':fitrid,'cal_runtime_id':calrid,'fit_csv_line':a['csv_line'] if a else None,'cal_csv_line':b['csv_line'] if b else None,'in_fit_and_cal_csv':bool(a and b),'full_source_row_equal':p['full_source_row_equal'],'full_source_row_sha256':p['fit_source_row_sha256']}
        checks.append(row)
summary={'base_evidence':'round11-extraction-provenance-codex.json','original_overlap_trip_ids':meta['overlap_original_ids'],'verified_fixture_source_hashes':len(meta['fixtures'])*len(TAGS),'source_scenario_hash_mismatches':hashbad,'csv_prefix_identity_mismatches':prefixbad,'typed_identity_formula':'rq- + SHA256(s + 8-byte big-endian UTF8 length + stableSubjectId UTF8); mapping.py lines20-41 and65-67. All selected static fit/cal CSV prefixes confirmed in source fixture identity set.','actual_fit_cal_csv_overlap_pairs':sum(r['in_fit_and_cal_csv'] for r in checks),'actual_fit_cal_csv_overlap_by_arm':dict(Counter(r['arm'] for r in checks if r['in_fit_and_cal_csv'])),'mapping_checks':checks,'warning':'Original source rows overlap despite different HMAC fixture request IDs and opaque runtime IDs. New extractor retains all these fit/calibration rows without provenance purge.'}
with (H/'round11-extraction-provenance-mapped-codex.json').open('x',encoding='utf-8') as out:json.dump(summary,out,indent=2)
with (H/'round11-extraction-provenance-mapped-codex.tsv').open('x',encoding='utf-8',newline='') as out:
    w=csv.DictWriter(out,fieldnames=list(checks[0]),delimiter='\t');w.writeheader();w.writerows(checks)
print(json.dumps({k:v for k,v in summary.items() if k!='mapping_checks'},indent=2))
