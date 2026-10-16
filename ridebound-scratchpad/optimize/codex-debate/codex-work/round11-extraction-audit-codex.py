"""Round11 independent causal extraction audit. Own Round10B parser, no Claude imports; no fitting/simulation. All output writes x."""
import csv, hashlib, json, sys, math
from pathlib import Path
from collections import Counter,defaultdict
sys.dont_write_bytecode=True
import round10b_verify_riders_codex as own
HERE=Path(__file__).resolve().parent
CSV=Path('C:/RideBoundData/research/ml-pilot-v1/riders-causal-2026-10-08.csv')
PREFIX=HERE/'round11-extraction-audit-codex'

def source(row):
    if row['world']=='static':
        return Path('E:/RideBoundData/wp14r/development-v6-ledger')/f"w14-{row['cell']}-{own.TAGS[row['arm']]}-s7/attempt-01/output/transcript-00.ndjson"
    root=Path('C:/RideBoundData/research/tier3-w07-v1' if row['role']=='fit' else 'C:/RideBoundData/research/tier3-t38-v1')
    initial=root/f"{row['arm']}-{row['cell']}"
    effective=initial
    if not (initial/'summary.json').exists() and (root/f"{row['arm']}-{row['cell']}-rerun1").exists():
        effective=root/f"{row['arm']}-{row['cell']}-rerun1"
    return effective/'transcript-00.ndjson'

# Independent arithmetic from original factor CSVs, fixed Nov12+Nov13 for every measured role.
profiles=[]; factor_sources=[]
for day in ('2018-11-12','2018-11-13'):
    p=own.FACTORS/f'{day}_tt_factors.csv';raw=p.read_bytes()
    factor_sources.append({'path':str(p),'sha256':hashlib.sha256(raw).hexdigest()})
    rows=sorted((int(r['simulation_time']),float(r['travel_time_factor'])) for r in csv.DictReader(raw.decode().splitlines()) if 25200<=int(r['simulation_time'])<=32400)
    profiles.append([max((t,v) for t,v in rows if t<=25200+b*900)[1] for b in range(9)])
PROFILE=[sum(p[b] for p in profiles)/2 for b in range(9)]
def display(t0,p0,static):
    if static or p0<=t0:return float(p0)
    b0=int(t0//900000);level=PROFILE[min(b0,8)];t=float(t0);work=float(p0-t0)
    while work>0:
        b=int(t//900000);weight=1 if b==b0 else PROFILE[min(b,8)]/level
        available=((b+1)*900000-t)/weight
        if available>=work:return max(float(p0),t+work*weight)
        work-=available;t=(b+1)*900000
    return max(float(p0),t)

raw=CSV.read_bytes();rows=list(csv.DictReader(raw.decode().splitlines()))
for i,r in enumerate(rows,2):r['_line']=i
expected=set()
for arm in ('U','C-30'):
    for d in (12,13):
        for n in (1,2,3,4):expected.add(('measured',arm,f'd201811{d}-s10-r{n}-w07','fit'))
    for n in (3,4):expected.add(('measured',arm,f'd20181114-s10-r{n}-w07','cal'))
    for d in (15,16):
        for n in (1,2,4):expected.add(('measured',arm,f'd201811{d}-s10-r{n}-w07',f'test{d}'))
for arm in own.TAGS:
    for d,ns,role in ((12,(1,2,3),'fit'),(12,(4,),'cal'),(13,(1,2,3,4),'test13')):
        for n in ns:
            for window in ('w08','w17'):expected.add(('static',arm,f'd201811{d}-s10-r{n}-{window}',role))
actual={(r['world'],r['arm'],r['cell'],r['role']) for r in rows}
keys=Counter((r['world'],r['arm'],r['cell'],r['rider']) for r in rows)
counts=Counter((r['world'],r['arm'],r['role']) for r in rows)
profile_mismatch=Counter()
for r in rows:
    t0,p0=float(r['t0']),float(r['P0']);d0=display(t0,p0,r['world']=='static')
    values={'D0':round(d0,1),'fc_ext_s':round((d0-p0)/1000,3),'resid_s':round((float(r['A'])-d0)/1000,3)}
    for key,val in values.items():
        if abs(float(r[key])-val)>1e-7:profile_mismatch[key]+=1
run_metadata=[]
for world,arm,cell,role in sorted(actual):
    rr=next(r for r in rows if (r['world'],r['arm'],r['cell'],r['role'])==(world,arm,cell,role));p=source(rr)
    run=json.loads((p.parent/'run-00.json').read_text());s=json.loads((p.parent/'summary.json').read_text())
    n=sum((r['world'],r['arm'],r['cell'],r['role'])==(world,arm,cell,role) for r in rows)
    run_metadata.append({'world':world,'arm':arm,'cell':cell,'role':role,'path':str(p),'csv_rows':n,'accepted':len(run['semantic']['acceptedRequestIds']),'summary':s})
# One highest state-count rider per world/arm/role: 23 rows, covering every role in every arm/world.
groups=defaultdict(list)
for r in rows:groups[(r['world'],r['arm'],r['role'])].append(r)
selected=[max(g,key=lambda r:(int(r['other_assigned']),int(r['other_onboard']),float(r['fc_ext_s']),r['rider'])) for _,g in sorted(groups.items())]
by_path=defaultdict(list)
for r in selected:by_path[source(r)].append(r)
checked=[];sources=[];mismatch=Counter();state_mismatch=Counter();service_state_disagreement=Counter();structural=Counter()
for ix,(p,rrs) in enumerate(sorted(by_path.items(),key=lambda z:str(z[0])),1):
    data=own.extract(p,[r['rider'] for r in rrs])
    sources.append({'path':str(p),'sha256':data['sha256'],'frames':data['frames'],'promised':len(data['first']),'completed':sum(r in data['alights'] for r in data['first'])})
    for r in rrs:
        ids=[i for i in data['first'] if i.startswith(r['rider'])]
        if len(ids)!=1:raise ValueError('Ambiguous rider prefix')
        rid=ids[0];first=data['first'][rid];pr=first['projection'];t0=first['time'];p0=pr['dropEtaMs'];pick0=pr['pickupEtaMs'];q=data['requests'][rid];a=data['alights'][rid]
        pp=data['histories'][rid][0]['publishedPromise']
        if pp['publishedAtMs']!=t0 or pp['projection']!=pr:raise ValueError('Initial ledger/publication mismatch')
        so=pr['serviceOrder'];other={s['requestId'] for s in so if s['requestId']!=rid};picks={s['requestId'] for s in so if s['kind']=='pickup'};drops={s['requestId'] for s in so if s['kind']=='drop'}
        onboard=(other & drops)-picks
        if any(s['kind'] not in ('pickup','drop') for s in so):structural['non-pickup/drop stop']+=1
        if other-drops:structural['other IDs without drop stop']+=1
        cap=data['capture'][rid]
        if len(other)!=cap['load']:service_state_disagreement['assigned count']+=1
        if len(onboard)!=cap['onboard']:service_state_disagreement['onboard count']+=1
        d0=display(t0,p0,r['world']=='static');mr=q['maxRideTimeMs'];ws=own.STARTS[r['window']]
        values={'clock_min':round((ws+t0/1000)/60,3),'horizon_s':(p0-t0)/1000,'pick_s':(pick0-t0)/1000,'fc_ext_s':round((d0-p0)/1000,3),'maxride_s':mr/1000,'room_s':(pick0+mr-p0)/1000,'other_assigned':len(other),'other_onboard':len(onboard),'P0':p0,'D0':round(d0,1),'t0':t0,'A':a,'resid_s':round((a-d0)/1000,3)}
        bad=[k for k,v in values.items() if abs(float(r[k])-v)>1e-7];mismatch.update(bad)
        stbad=[k for k in ('other_assigned','other_onboard') if k in bad];state_mismatch.update(stbad)
        checked.append({'csv_line':r['_line'],'world':r['world'],'arm':r['arm'],'role':r['role'],'cell':r['cell'],'rider':r['rider'],'transcript':str(p),'publication_line':first['line'],'projection_vehicle':pr['vehicleId'],'service_other_assigned':len(other),'event_other_assigned':cap['load'],'service_other_onboard':len(onboard),'event_other_onboard':cap['onboard'],'other_ids':';'.join(sorted(other)),'onboard_ids':';'.join(sorted(onboard)),'numeric_mismatches':','.join(bad) or 'NONE','expected_features':json.dumps(values,sort_keys=True)})
    print(f'Checked {ix}/{len(by_path)}: {p}',flush=True)
summary={'csv_path':str(CSV),'csv_sha256':hashlib.sha256(raw).hexdigest(),'csv_rows':len(rows),'unique_run_cells':len(actual),'expected_run_cells':len(expected),'missing_cells':sorted(expected-actual),'extra_cells':sorted(actual-expected),'duplicate_prefix_keys':sum(v-1 for v in keys.values() if v>1),'counts':[{'world':k[0],'arm':k[1],'role':k[2],'riders':v} for k,v in sorted(counts.items())],'all_csv_fixed_profile_mismatch':dict(profile_mismatch),'fixed_profile':PROFILE,'factor_sources':factor_sources,'checked_rows':len(checked),'checked_runs':len(sources),'numeric_fields_per_row':13,'numeric_mismatch_counts':dict(mismatch),'service_state_csv_mismatch_counts':dict(state_mismatch),'service_state_vs_source_event_counts_disagreement':dict(service_state_disagreement),'service_order_structural_warning_counts':dict(structural),'all112_accepted_csv_count_mismatches':sum(r['csv_rows']!=r['accepted'] for r in run_metadata),'rerun_cells':[r for r in run_metadata if '-rerun' in r['path']],'run_metadata':run_metadata,'sources':sources,'selection_rule':'Highest service-assigned/onboard then forecast-extension rider in each world/arm/role; selected before transcript parsing.','scope':'Checks numerical and causal timing of selected rows; does not recover source-trip groups or certify global provenance.'}
with Path(str(PREFIX)+'.tsv').open('x',encoding='utf-8',newline='') as out:
    w=csv.DictWriter(out,fieldnames=list(checked[0]),delimiter='	');w.writeheader();w.writerows(checked)
with Path(str(PREFIX)+'.json').open('x',encoding='utf-8') as out:json.dump(summary,out,indent=2)
with Path(str(PREFIX)+'.txt').open('x',encoding='utf-8') as out:
    out.write(json.dumps({k:v for k,v in summary.items() if k not in ('sources','run_metadata')},indent=2)+'
')
print(json.dumps({k:v for k,v in summary.items() if k not in ('sources','run_metadata')},indent=2),flush=True)
