"""Round11 read-only original source-trip gate check; no ML imports/fits. Outputs exclusive."""
import csv,hashlib,json,zipfile,io,sys
from pathlib import Path
from collections import defaultdict
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
ARCHIVE=Path('E:/RideBoundData/wp6/objects/sha256/d9/d9e86f33645e5eec287d387f8d63ad41ddf41d4ef648138b65d636482e2c599e/FleetPy_Manhattan.zip')
FIX=Path('E:/Code/RideBound/benchmarks/fixtures/wp6/public/fleetpy-manhattan-v1/wp14-development-panel-v1')
records=[];fixtures=[]
with zipfile.ZipFile(ARCHIVE) as z:
    for sample in (1,2,3,4):
        cache=None
        for window in ('w08','w17'):
            cell=f'd20181112-s10-r{sample}-{window}';d=FIX/cell
            conf=json.loads((d/'normalizer-configuration.json').read_text());raw=(d/'scenario-content.json').read_bytes();scenario=json.loads(raw)
            events=[e for e in scenario['events'] if e['eventType']=='requestArrived']
            member=conf['demandMemberPath']
            if cache is None:
                with z.open(member) as p:cache=list(csv.DictReader(io.TextIOWrapper(p,encoding='utf-8')))
            offsets=[]
            for off in (0,1):
                ok=True
                for e in events:
                    original=cache[e['sourceRecordOrdinal']-off]
                    time=json.loads(bytes.fromhex(e['payloadCanonicalJsonHex']))['request']['arrivalTimeMs']
                    if abs((float(original['rq_time'])-conf['sourceWindowStartSeconds'])*1000-time)>0.1:ok=False;break
                if ok:offsets.append(off)
            if len(offsets)!=1:raise ValueError(f'{cell} ordinal offset ambiguous {offsets}')
            off=offsets[0]
            fixtures.append({'cell':cell,'scenario_sha256':hashlib.sha256(raw).hexdigest(),'member':member,'zip_member_crc':z.getinfo(member).CRC,'source_ordinal_offset':off,'selected':len(events)})
            for e in events:
                o=cache[e['sourceRecordOrdinal']-off]
                digest=hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
                records.append({'cell':cell,'role':'cal' if sample==4 else 'fit','member':member,'original_request_id':o['request_id'],'full_source_row_sha256':digest,'ordinal':e['sourceRecordOrdinal'],'stable_subject':e['stableSubjectId'],'source_row':o})
fit=defaultdict(list);cal=defaultdict(list)
for r in records:(fit if r['role']=='fit' else cal)[r['original_request_id']].append(r)
overlap=[]
for key in sorted(fit.keys()&cal.keys()):
    for a in fit[key]:
        for b in cal[key]:
            overlap.append({'request_id':key,'fit_cell':a['cell'],'cal_cell':b['cell'],'fit_stable_subject':a['stable_subject'],'cal_stable_subject':b['stable_subject'],'fit_ordinal':a['ordinal'],'cal_ordinal':b['ordinal'],'full_source_row_equal':a['source_row']==b['source_row'],'fit_source_row_sha256':a['full_source_row_sha256'],'cal_source_row_sha256':b['full_source_row_sha256'],'fit_member':a['member'],'cal_member':b['member']})
summary={'archive':str(ARCHIVE),'archive_sha256_not_recomputed':'d9e86f33645e5eec287d387f8d63ad41ddf41d4ef648138b65d636482e2c599e path identity only','fixtures':fixtures,'fit_selected_rows':sum(r['role']=='fit' for r in records),'cal_selected_rows':sum(r['role']=='cal' for r in records),'fit_unique_original_ids':len(fit),'cal_unique_original_ids':len(cal),'overlap_original_ids':len(fit.keys()&cal.keys()),'overlap_pairs':overlap,'full_source_row_equality_pairs':sum(r['full_source_row_equal'] for r in overlap),'scope':'Selected-demand provenance only; served-label inclusion requires runtime/source mapping. Source trip IDs/rows recovered directly from original zip member using event sourceRecordOrdinal and validated arrival-time offset.'}
with (HERE/'round11-extraction-provenance-codex.json').open('x',encoding='utf-8') as out:json.dump(summary,out,indent=2)
with (HERE/'round11-extraction-provenance-codex.tsv').open('x',encoding='utf-8',newline='') as out:
    keys=list(overlap[0]) if overlap else ['request_id','fit_cell','cal_cell'];w=csv.DictWriter(out,fieldnames=keys,delimiter='\t');w.writeheader();w.writerows(overlap)
print(json.dumps(summary,indent=2))
