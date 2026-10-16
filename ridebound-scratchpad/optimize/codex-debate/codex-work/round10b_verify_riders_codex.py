"""Round 10B independent CSV timing audit. No Claude code imports; no fitting/simulation.
Source files read-only; all newly created outputs use exclusive mode x.
"""
from __future__ import annotations
import base64
from collections import Counter, defaultdict
import csv
import hashlib
import json
from pathlib import Path
import math
import re
import sys
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
CSV = Path('C:/RideBoundData/research/ml-pilot-v1/riders-2026-10-08.csv')
REPORT = HERE/'round10b-rider-spotcheck-codex.txt'
TSV = HERE/'round10b-rider-spotcheck-codex.tsv'
META = HERE/'round10b-rider-spotcheck-codex.json'
FACTORS = Path('E:/RideBoundData/wp6/extracted/sha256/d9/d9e86f33645e5eec287d387f8d63ad41ddf41d4ef648138b65d636482e2c599e/FleetPy_Manhattan/networks/Manhattan_2019_corrected')
STARTS = {'w07':25200,'w08':28800,'w17':61200}
TAGS = {'FREE':'b1-ref','LOCKS':'c1-nobudget','C-120':'c1-budget120','C-60':'c1-budget60','C-30':'c1-h6ref'}
KIND = re.compile(rb'"messageType"\s*:\s*"([^"]+)"')

def source_path(row):
    src, arm, cell = row['source'], row['arm'], row['cell']
    if src == 'wp14r':
        return Path('E:/RideBoundData/wp14r/development-v6-ledger')/f'w14-{cell}-{TAGS[arm]}-s7/attempt-01/output/transcript-00.ndjson'
    root = Path('C:/RideBoundData/research/tier3-w07-v1' if src == 'w07' else 'C:/RideBoundData/research/tier3-t38-v1')
    original=root/f'{arm}-{cell}'
    effective=original
    if not (original/'summary.json').exists() and (root/f'{arm}-{cell}-rerun1'/'summary.json').exists():
        effective=root/f'{arm}-{cell}-rerun1'
    return effective/'transcript-00.ndjson'

def forecast(t0, p0, day, window, static):
    sources=[f'2018-11-{d:02d}' for d in (12,13,14,16) if f'2018-11-{d:02d}'<day]
    if static or day in ('2018-11-17','2018-11-18') or len(sources)<2:
        return float(p0)
    profiles=[]
    start=STARTS[window]
    for source in sources:
        with (FACTORS/f'{source}_tt_factors.csv').open(encoding='utf-8') as handle:
            pairs=sorted((int(r['simulation_time']),float(r['travel_time_factor'])) for r in csv.DictReader(handle))
        values=[]
        for b in range(9):
            ts=start+900*b
            eligible=[v for t,v in pairs if start<=t<=ts]
            if not eligible: raise ValueError('No exact source-window factor')
            values.append(eligible[-1])
        profiles.append(values)
    m=[sum(p[b] for p in profiles)/len(profiles) for b in range(9)]
    b0=t0//900000
    level0=m[min(b0,8)]
    t=float(t0); work=float(p0-t0)
    while work>0:
        b=int(t//900000)
        weight=1.0 if b==b0 else m[min(b,8)]/level0
        end=(b+1)*900000
        consumed=(end-t)/weight
        if consumed>=work:
            t+=work*weight;break
        work-=consumed;t=end
    return max(float(p0),t)

def extract(path, prefixes):
    vehicles={}; requests={}; first={}; alights={}; pickups={}
    final_state=None; frames=0; digest=hashlib.sha256(); capture={}
    prior_promises={}; pending={}; checked_apply=0
    events=Counter(); source_before=path.stat()
    def ensure_vehicle(vid):
        return vehicles.setdefault(vid,{'accepted':set(),'onboard':set()})
    def forget(rid):
        for state in vehicles.values():
            state['accepted'].discard(rid);state['onboard'].discard(rid)
    def apply(action):
        kind=action['decisionType']; data=action['payload']
        if kind=='requestAccepted':
            rid=data['requestId'];vid=data['vehicleId'];forget(rid)
            ensure_vehicle(vid)['accepted'].add(rid)
        elif kind in ('requestRejected','requestCancelled'):
            forget(data['requestId'])
        elif kind=='vehiclePlanUpdated':
            ensure_vehicle(data['vehicleId'])['route']=data['route']
    with path.open('rb') as handle:
        for line_number, raw in enumerate(handle,1):
            digest.update(raw); outer=json.loads(raw)
            frame=base64.b64decode(outer['frameBase64'],validate=True)
            if len(frame)!=outer['frameLengthBytes'] or hashlib.sha256(frame).hexdigest()!=outer['frameSha256']:
                raise ValueError(f'Invalid raw frame {path}:{line_number}')
            frames+=1
            match=KIND.search(frame[:2048])
            kind=match[1].decode() if match else json.loads(frame)['messageType']
            if kind not in ('eventBatch','decision','decisionApplied','checkpoint'): continue
            env=json.loads(frame); time=env.get('simTimeMs')
            if kind=='eventBatch' and outer['direction']=='adapterToRunner':
                for event in env['payload'].get('events',[]):
                    typ=event['eventType'];data=event['payload'];events[typ]+=1
                    if typ=='vehicleAdvanced':
                        v=data['vehicle']; vehicles[v['vehicleId']]={'accepted':set(v.get('acceptedRequestIds',[])),
                            'onboard':set(v.get('onboardRequestIds',[])),'route':v.get('route',{})}
                    elif typ=='requestArrived':
                        r=data['request'];requests[r['requestId']]=r
                    elif typ=='passengerBoarded':
                        rid=data['requestId'];vid=data['vehicleId'];pickups.setdefault(rid,time)
                        ensure_vehicle(vid)['onboard'].add(rid);ensure_vehicle(vid)['accepted'].add(rid)
                    elif typ=='passengerAlighted':
                        rid=data['requestId'];alights.setdefault(rid,time);forget(rid)
                    elif typ in ('requestCancelled','bookingCancelled'):
                        forget(data['requestId'])
            elif kind=='decision' and outer['direction']=='runnerToAdapter':
                actions=env['payload'].get('actions',[])
                pending[env['payload']['decisionHash']]=actions
                # All selected plan actions in this same message are known at publication.
                # Earlier decisions are already applied; this adds no later frame or event.
                publication_vehicles={vid:{'accepted':set(v['accepted']),'onboard':set(v['onboard'])} for vid,v in vehicles.items()}
                for action in actions:
                    if action['decisionType']=='requestAccepted':
                        rid=action['payload']['requestId'];vid=action['payload']['vehicleId']
                        for v in publication_vehicles.values():v['accepted'].discard(rid);v['onboard'].discard(rid)
                        publication_vehicles.setdefault(vid,{'accepted':set(),'onboard':set()})['accepted'].add(rid)
                for action in actions:
                    if action['decisionType']!='promisePublished':continue
                    p=action['payload'];projection=p['promise'];rid=projection['requestId']
                    if p['reasonCode']!='INITIAL_BOOKING_CONFIRMATION' or rid in first:continue
                    vid=projection['vehicleId'];v=publication_vehicles.get(vid)
                    if v is None:raise ValueError('Missing initial vehicle state')
                    first[rid]={'time':time,'projection':projection,'line':line_number}
                    if any(rid.startswith(prefix) for prefix in prefixes):
                        capture[rid]={'load':len(v['accepted']-{rid}),'onboard':len(v['onboard']-{rid}),
                            'accepted_ids':sorted(v['accepted']-{rid}),'onboard_ids':sorted(v['onboard']-{rid}),
                            'first_vehicle':vid,'line':line_number,'epoch':env.get('epochId'),
                            'known_prior_promised_load':sum(o!=rid and o in v['accepted'] for o in prior_promises)}
                    prior_promises[rid]=time
            elif kind=='decisionApplied' and outer['direction']=='adapterToRunner':
                actions=pending.pop(env['payload']['decisionHash'],None)
                if actions is None:raise ValueError('Applied unknown decision')
                for action in actions:apply(action)
                checked_apply+=1
            elif kind=='checkpoint' and outer['direction']=='runnerToAdapter':
                final_state=env['payload']['content']['onlineState']
    after=path.stat()
    if (source_before.st_size,source_before.st_mtime_ns)!=(after.st_size,after.st_mtime_ns):raise ValueError('Changed source')
    if final_state is None:raise ValueError('No final checkpoint')
    final_requests={r['requestId']:r for r in final_state['requests']}
    histories={h['requestId']:h['entries'] for h in final_state['commitmentLedger']}
    return {'requests':requests,'first':first,'alights':alights,'pickups':pickups,
            'capture':capture,'final_requests':final_requests,'histories':histories,
            'sha256':digest.hexdigest(),'frames':frames,'applied':checked_apply,'events':dict(events)}

def main():
    for output in (REPORT,TSV,META):
        if output.exists():raise FileExistsError(output)
    raw=CSV.read_bytes(); csv_sha=hashlib.sha256(raw).hexdigest()
    with CSV.open(newline='',encoding='utf-8') as handle:rows=list(csv.DictReader(handle))
    groups=defaultdict(list)
    for i,row in enumerate(rows,2): row['_line']=i;groups[(row['source'],row['arm'])].append(row)
    duplicate_keys=Counter((r['source'],r['arm'],r['cell'],r['rider']) for r in rows)
    source_counts=Counter(r['source'] for r in rows)
    selected=[]
    for key,group in sorted(groups.items()):
        first_cell=group[0]['cell']; pool=[r for r in group if r['cell']==first_cell]
        choice=[min(pool,key=lambda r:(int(r['t0_ms']),r['rider'])),
                max(pool,key=lambda r:(int(r['load_t0']),int(r['onboard_t0']),r['rider'])),
                sorted(pool,key=lambda r:r['rider'])[len(pool)//2]]
        used=set()
        for row in choice:
            if row['rider'] not in used:selected.append(row);used.add(row['rider'])
        for row in pool:
            if len(used)>=3:break
            if row['rider'] not in used:selected.append(row);used.add(row['rider'])
    by_path=defaultdict(list)
    for row in selected:by_path[source_path(row)].append(row)
    results=[]; sources=[]; mismatches=Counter(); causal_mismatches=Counter()
    for run_number,(path,run_rows) in enumerate(sorted(by_path.items(),key=lambda x:str(x[0])),1):
        data=extract(path,[r['rider'] for r in run_rows]);sources.append({'path':str(path),'sha256':data['sha256'],
             'frames':data['frames'],'applied_decisions':data['applied'],'promised':len(data['first']),
             'completed_promised':sum(r in data['alights'] for r in data['first']),
             'unfinished_promised':sum(r not in data['alights'] for r in data['first'])})
        for row in run_rows:
            matches=[r for r in data['first'] if r.startswith(row['rider'])]
            if len(matches)!=1:raise ValueError('Prefix ambiguous or missing')
            rid=matches[0];first=data['first'][rid];t0=first['time'];proj=first['projection'];p0=proj['dropEtaMs'];pk=proj['pickupEtaMs']
            q=data['requests'][rid];history=data['histories'][rid]
            # Validate event-time capture independently against final recorded initial publication.
            ledger_first=history[0]['publishedPromise']
            if ledger_first['publishedAtMs']!=t0 or ledger_first['projection']!=proj:raise ValueError('Initial publication/ledger mismatch')
            if rid not in data['alights']:raise ValueError('CSV row is not completed')
            cs=[e['publishedPromise']['projection']['dropEtaMs']-e['exogenousProjection']['dropEtaMs'] for e in history[1:]]
            xs=[e['exogenousProjection']['dropEtaMs']-e['previousPromise']['projection']['dropEtaMs'] for e in history[1:]]
            final_vid=data['final_requests'][rid]['assignedVehicleId']
            old_others=[o for o in data['alights'] if o!=rid and o in data['first']
                and data['final_requests'][o].get('assignedVehicleId')==final_vid
                and data['first'][o]['time']<=t0<data['alights'][o]]
            old_onboard=sum(data['pickups'].get(o,math.inf)<t0 for o in old_others)
            d0=forecast(t0,p0,row['day'],row['window'],row['source']=='wp14r')
            expected={'t0_ms':t0,'bin':t0//900000,'minute':round(t0/60000,2),'horizon_s':(p0-t0)/1000,
                'direct_s':round(q['maxRideTimeMs']/1500,1),'room_s':(pk+q['maxRideTimeMs']-p0)/1000,
                'wait_promised_s':(pk-q['arrivalTimeMs'])/1000,'fc_ext_s':round((d0-p0)/1000,3),
                'load_t0':len(old_others),'onboard_t0':old_onboard,'y_s':(data['alights'][rid]-p0)/1000,
                'disp_sum_s':sum(cs)/1000,'traf_sum_s':sum(xs)/1000,'exposed':int(any(cs))}
            bad=[key for key,val in expected.items() if abs(float(row[key])-float(val))>0.0000001]
            mismatches.update(bad)
            cap=data['capture'][rid]
            cbad=[]
            if int(row['load_t0'])!=cap['load']:cbad.append('load_t0')
            if int(row['onboard_t0'])!=cap['onboard']:cbad.append('onboard_t0')
            causal_mismatches.update(cbad)
            results.append({'csv_line':row['_line'],'source':row['source'],'arm':row['arm'],'cell':row['cell'],
                'rider_prefix':row['rider'],'transcript':str(path),'publication_line':first['line'],'t0_ms':t0,
                'csv_load_t0':int(row['load_t0']),'retrospective_load_t0':len(old_others),'causal_assigned_others':cap['load'],
                'csv_onboard_t0':int(row['onboard_t0']),'retrospective_onboard_t0':old_onboard,'causal_onboard_others':cap['onboard'],
                'initial_vehicle_equals_final':proj['vehicleId']==final_vid,'derived_field_mismatches':','.join(bad) or 'NONE',
                'causal_count_mismatches':','.join(cbad) or 'NONE','wait_from_publication_s':(pk-t0)/1000,
                'request_arrival_to_publication_s':(t0-q['arrivalTimeMs'])/1000,'checked_fields':json.dumps(expected,sort_keys=True)})
        print(f'Checked run {run_number}/{len(by_path)}; {len(run_rows)} rows: {path}',flush=True)
    summary={'csv_sha256':csv_sha,'rows':len(rows),'unique_runs':len({(r['source'],r['arm'],r['cell']) for r in rows}),
        'source_rows':dict(source_counts),'source_arm_groups':len(groups),'duplicate_prefix_keys':sum(n-1 for n in duplicate_keys.values() if n>1),
        'checked_rows':len(results),'checked_runs':len(sources),'checks_per_row':14,'derived_field_mismatch_counts':dict(mismatches),
        'causal_count_mismatch_counts':dict(causal_mismatches),'rows_with_causal_count_mismatch':sum(r['causal_count_mismatches']!='NONE' for r in results),
        'rows_with_initial_final_vehicle_change':sum(not r['initial_vehicle_equals_final'] for r in results),
        'sources':sources,'selection_rule':'Three deterministic rows from first cell of every source-arm group: earliest publication, highest CSV load/onboard, median rider; replace duplicates with first remaining rider.',
        'structural_warning':'CSV loader uses completed cohort, final assignment and later alight; exact agreement with causal counts in a sample does not validate general timing.'}
    with TSV.open('x',encoding='utf-8',newline='') as handle:
        writer=csv.DictWriter(handle,fieldnames=list(results[0]),delimiter='\t');writer.writeheader();writer.writerows(results)
    with META.open('x',encoding='utf-8') as handle:json.dump(summary,handle,indent=2)
    lines=['# Independent Round 10B rider check; own raw-frame parser and feature/profile arithmetic; no Claude imports.',
        f'CSV={CSV}',f'CSV_SHA256={csv_sha}',f'CSV_ROWS={len(rows)} UNIQUE_SOURCE_ARM_CELL_RUNS={summary["unique_runs"]} PREFIX_DUPLICATE_KEYS={summary["duplicate_prefix_keys"]}',
        f'SPOTCHECK_ROWS={len(results)} RUNS={len(sources)} FIELDS_PER_ROW=14',
        'DERIVED_FIELD_MISMATCHES='+json.dumps(dict(mismatches),sort_keys=True),
        'CAUSAL_COUNT_MISMATCHES='+json.dumps(dict(causal_mismatches),sort_keys=True),
        f'ROWS_WITH_CAUSAL_MISMATCH={summary["rows_with_causal_count_mismatch"]} INITIAL_FINAL_VEHICLE_CHANGES={summary["rows_with_initial_final_vehicle_change"]}',
        'Every raw frame SHA256/length checked; complete transcript SHA256 recorded; initial ledger/publication equality checked.',
        'Causal counts include all presently assigned/onboard riders, with source-order event and applied-plan reconstruction.',
        'Retrospective arithmetic matches do not prove absence of completed-cohort/final-vehicle/future-alight leakage.',
        'CSV minute/bin are window-relative; wait uses pickup minus arrival; direct is rounded maxRide/1.5 proxy.',
        'No model fitting, no simulation/dispatch execution, no installs; every output uses mode x.']
    with REPORT.open('x',encoding='utf-8') as handle:handle.write('\n'.join(lines)+'\n')
    print('\n'.join(lines),flush=True)
if __name__=='__main__':main()
