"""Read-only Round 12 checks; outputs exclusive inside codex-work; no simulations."""
from pathlib import Path
import csv, json, statistics as st, hashlib, importlib.util
from concurrent.futures import ThreadPoolExecutor
ROOT=Path('E:/Code/Report_INT3508/ridebound-scratchpad')
HERE=Path(__file__).resolve().parent
FACTORS=Path('E:/RideBoundData/wp6/extracted/sha256/d9/d9e86f33645e5eec287d387f8d63ad41ddf41d4ef648138b65d636482e2c599e/FleetPy_Manhattan/networks/Manhattan_2019_corrected')
series={}; meta=[]
for day in range(11,19):
    name=f'2018-11-{day}'
    path=FACTORS/(name+('_tt_factors_hourly.csv' if day==11 else '_tt_factors.csv'))
    rows=list(csv.DictReader(path.open(encoding='utf-8')))
    series[name]={int(r['simulation_time']):float(r['travel_time_factor']) for r in rows}
    times=sorted(series[name])
    meta.append(dict(day=name,rows=len(rows),cadence=sorted(set(b-a for a,b in zip(times,times[1:]))),path=str(path),sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
err=[]
for window,start in [('07:00-09:00',25200),('08:00-10:00',28800),('17:00-19:00',61200)]:
    for h in (1,2,3):
        naive=[]; forecast=[]
        for day in range(12,19):
            name=f'2018-11-{day}'
            others=[f'2018-11-{d}' for d in range(12,19) if d!=day and (d>=17)==(day>=17)]
            for b in range(9-h):
                t=start+b*900;t2=t+h*900
                actual=series[name][t2]/series[name][t]
                pred=st.mean(series[d][t2] for d in others)/st.mean(series[d][t] for d in others)
                naive.append(100*abs(1-actual));forecast.append(100*abs(pred-actual))
        err.append(dict(window=window,horizon_minutes=h*15,n=len(naive),naive_mean=st.mean(naive),forecast_mean=st.mean(forecast),naive_max=max(naive),forecast_max=max(forecast)))
split=json.loads((ROOT/'tang3/t38/split-t38-v1.json').read_text(encoding='utf-8'))
cells=split['test']; assert len(cells)==34
spec=importlib.util.spec_from_file_location('r12_ind_extract',ROOT/'optimize/independent-A/ind_extract.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
records={}; missing=[]; cached=[]
for arm in ['C-30','U']:
    for cell in cells:
        path=ROOT/'optimize/independent-A/extracted'/f'{arm}-{cell}.json'
        if path.exists():
            records[(arm,cell)]=json.loads(path.read_text(encoding='utf-8'))
            cached.append(dict(path=str(path),sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
        else:missing.append((arm,cell))
with ThreadPoolExecutor(max_workers=4) as pool:
    for res in pool.map(module.extract,missing):
        assert res['badSha']==0 and res['finalCheckpoint']
        records[(res['arm'],res['cell'])]=res
        print('raw checked',res['arm'],res['cell'],res['frames'],flush=True)
results=[]
for arm in ['C-30','U']:
    n=exposed=positive_riders=negative_riders=0; shifts=[];positive_events=negative_events=0
    for cell in cells:
        res=records[(arm,cell)]
        assert res['badSha']==0 and res['finalCheckpoint']
        for rider in res['riders']:
            if rider['A'] is None:continue
            cs=[e['p']-e['e'] for e in rider['entries'] if 'e' in e]
            n+=1;exposed+=any(cs);positive_riders+=any(c>0 for c in cs);negative_riders+=any(c<0 for c in cs)
            positive_events+=sum(c>0 for c in cs);negative_events+=sum(c<0 for c in cs)
            shifts.extend(abs(c)/1000 for c in cs if c)
    vals=sorted(shifts)
    results.append(dict(arm=arm,completed=n,exposed=exposed,exposure_percent=100*exposed/n,positive_riders=positive_riders,positive_rider_percent=100*positive_riders/n,negative_riders=negative_riders,nonzero_events=len(vals),positive_events=positive_events,negative_events=negative_events,median_s=st.median(vals),p90_nearest_rank_s=vals[(9*len(vals)+9)//10-1],maximum_s=max(vals)))
out=dict(factor_files=meta,total_observations=sum(x['rows'] for x in meta),factor_errors=err,t38=results,cached_extractions=cached,new_raw_cells=[list(j) for j in missing],new_raw_frames=sum(records[j]['frames'] for j in missing),scope='C-30 uses 34 pre-existing independently checked extractions; U uses 21 cached plus 13 freshly frame-hashed raw transcripts; no simulation executed.')
with (HERE/'round12-evidence-audit.json').open('x',encoding='utf-8') as h:json.dump(out,h,indent=2)
lines=['# Round 12 independent arithmetic and source checks',out['scope'],'Factor observations: '+str(out['total_observations']),'']
for row in results:lines.append(json.dumps(row))
lines.append('')
for row in err:lines.append(json.dumps(row))
with (HERE/'round12-evidence-audit.txt').open('x',encoding='utf-8') as h:h.write('\n'.join(lines)+'\n')
print(json.dumps(results,indent=2),flush=True)
print('factor table reproduced, observations',out['total_observations'],flush=True)
