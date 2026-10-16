"""Independent R34 raw probe, faster second pass; no source mutation/import.

Only parsed relevant frames are SHA256 checked. Unused decision frames are
skipped. Output is small, flushed per run, and exclusively created beside script.
"""
import base64,collections,concurrent.futures,hashlib,json,pathlib,sys
HERE=pathlib.Path(__file__).resolve().parent
OUT=HERE/'extra-probe-output-v3.txt'
FIXED=pathlib.Path('E:/RideBoundData/wp14r/development-v6-ledger')
RESEARCH=pathlib.Path('C:/RideBoundData/research')
SCRATCH=pathlib.Path('E:/Code/Report_INT3508/ridebound-scratchpad')
LEVELS=(30,60,90,120,150,180,240,300)
CELLS=tuple(f'd201811{d}-s10-r{r}-w07' for d in (12,13) for r in (1,2,3,4))

def reversed_lines(path):
    with path.open('rb') as handle:
        position=handle.seek(0,2);suffix=b''
        while position:
            n=min(position,1024*1024);position-=n;handle.seek(position)
            pieces=(handle.read(n)+suffix).split(b'\n');suffix=pieces[0]
            for line in reversed(pieces[1:]):
                if line:yield line
        if suffix:yield suffix

def frame(line,path):
    record=json.loads(line);raw=base64.b64decode(record['frameBase64'],validate=True)
    assert len(raw)==record['frameLengthBytes']
    assert hashlib.sha256(raw).hexdigest()==record['frameSha256'],path
    return json.loads(raw),record

# Interior encoded code markers for all three byte alignments. This only skips
# frames without the exact code before expensive decoding/parsing. Actual counts
# inspect the JSON candidates/witnesses, not these substring matches.
BUD_MARKERS=tuple(base64.b64encode(b'X'*offset+b'COMMITMENT_BUDGET_EXCEEDED')[4 if offset else 0:-4]
                  for offset in range(3))

def head(line):
    prefix=line.split(b'"frameBase64":"',1)[1][:256]
    return base64.b64decode(prefix.split(bytes([34]),1)[0])

def scan(path,budget=False):
    final=None;alight={};blocked=set();frames=0
    for line in reversed_lines(path):
        if not line.startswith(b'{"direction":"runnerToAdapter"'):continue
        if b'"messageType":"checkpoint"' not in head(line):continue
        env,_=frame(line,path);frames+=1
        final=env['payload']['content']['onlineState'];break
    assert final is not None,path
    with path.open('rb') as handle:
        for line in handle:
            adapter=line.startswith(b'{"direction":"adapterToRunner"')
            budget_present=budget and not adapter and any(marker in line for marker in BUD_MARKERS)
            if not adapter and not budget_present:continue
            if adapter and b'"messageType":"eventBatch"' not in head(line):continue
            env,_=frame(line,path);frames+=1
            if adapter:
                for ev in env['payload'].get('events',[]):
                    if ev.get('eventType')=='passengerAlighted':
                        alight.setdefault(ev['payload']['requestId'],env['simTimeMs'])
            elif env.get('messageType')=='decision':
                evidence=env.get('payload',{}).get('solver',{}).get('executionEvidence',{})
                for candidate in evidence.get('prunedCandidates',[]):
                    if candidate.get('code')=='COMMITMENT_BUDGET_EXCEEDED' and any(
                        w.get('code')=='COMMITMENT_BUDGET_EXCEEDED'
                        for w in candidate.get('commitmentWitnesses',[])):
                        blocked.update(candidate.get('newRequestIds',[]))
    life={r['requestId']:r['lifecycle'] for r in final['requests']}
    assert set(alight)=={rid for rid,v in life.items() if v=='completed'},path
    return final,alight,blocked,frames

def outcome(state,alight):
    promises={};moved=set()
    for ledger in state['commitmentLedger']:
        rid=ledger['requestId'];entries=ledger['entries']
        initial=[entry for entry in entries if entry['kind']=='initialPromise']
        assert len(initial)==1,rid
        promises[rid]=initial[0]['publishedPromise']['projection']['dropEtaMs']
        for entry in entries:
            if entry['kind']=='revision':
                delta=(entry['publishedPromise']['projection']['dropEtaMs']-
                       entry['exogenousProjection']['dropEtaMs'])
                if delta!=0:moved.add(rid)
    late60=sum(alight[rid]-promises[rid]>60000 for rid in alight)
    late120=sum(alight[rid]-promises[rid]>120000 for rid in alight)
    shared=set();events=collections.defaultdict(list)
    # Independent event sweep: endings before beginnings implement half-open
    # actual pickup/alight intervals, instead of pairwise interval comparisons.
    for request in state['requests']:
        rid=request['requestId']
        if rid in alight:
            assert request['actualPickupTimeMs']<alight[rid]
            events[request['assignedVehicleId']].extend((
                (request['actualPickupTimeMs'],1,rid),(alight[rid],0,rid)))
    for evs in events.values():
        onboard=set()
        for instant,kind,rid in sorted(evs):
            if kind==0:onboard.remove(rid)
            else:
                onboard.add(rid)
                if len(onboard)>1:shared.update(onboard)
        assert not onboard
    served=len(alight)
    return dict(requests=len(state['requests']),served=served,late60=late60,
                timely60=served-late60,timely120=served-late120,shared=len(shared),
                moved=len(moved & set(alight)),moved_all_accepted=len(moved))

def mapped(task):
    group,arm,path=task;state,alight,_,frames=scan(path)
    return group,arm,path,outcome(state,alight),frames

def main():
    with OUT.open('x',encoding='utf-8',newline='\n') as output:
        def emit(value):
            line=value if isinstance(value,str) else json.dumps(value,ensure_ascii=False,sort_keys=True)
            output.write(line+'\n');output.flush();print(line,flush=True)
        emit('R34 v3 remaining independent raw probe; relevant parsed frames hash checked; half-open sharing; strict A-p0 thresholds.')
        tasks=[];fixed_arms=('b1-ref','c1-nobudget','c1-budget120','c1-budget60','c1-h6ref')
        for arm in fixed_arms:
            runs=sorted(FIXED.glob(f'w14-*-{arm}-s7'));assert len(runs)==16,(arm,len(runs))
            pass # all80 fixed raw results retained in extra-probe-output-v2.txt
        for arm in ('U',)+tuple(f'C-{x}' for x in LEVELS):
            family='tier3-w07-v1' if arm=='U' or int(arm[2:]) in (30,60,120,300) else 'tier3-w07x-v1'
            tasks.extend(('morning',arm,RESEARCH/family/f'{arm}-{cell}/transcript-00.ndjson') for cell in CELLS)
        snow=sorted((RESEARCH/'tier3-forecast-v1').glob('C-30-d20181115-s10-r*-w1[45]'))
        assert len(snow)==8,('snow',len(snow))
        tasks.extend(('snow','C-30',p/'transcript-00.ndjson') for p in snow)
        counts=collections.defaultdict(collections.Counter);run_counts=collections.Counter();frames_total=0
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
            for group,arm,path,stats,frames in pool.map(mapped,tasks):
                counts[(group,arm)].update(stats);run_counts[(group,arm)]+=1;frames_total+=frames
                emit(dict(group=group,arm=arm,source=str(path),**stats))
        for group,arms in (('morning',('U',)+tuple(f'C-{x}' for x in LEVELS)),('snow',('C-30',))):
            for arm in arms:emit(dict(group=group+'-total',arm=arm,runs=run_counts[(group,arm)],**counts[(group,arm)]))
        emit(dict(parsed_relevant_frames_sha256_verified=frames_total))
        archived=[];chosen=[];other=[]
        for family in ('tier3-w07-v1','tier3-w07x-v1'):
            valid=[p for p in sorted((RESEARCH/family).iterdir()) if p.is_dir() and (p/'summary.json').exists()]
            statuses=collections.Counter(json.loads((p/'summary.json').read_text(encoding='utf-8'))['status'] for p in valid)
            emit(dict(group='archive-root',source=str(RESEARCH/family),run_directories=len(valid),summary_statuses=dict(statuses)))
            for run in valid:
                arm=run.name.split('-d201811',1)[0];archived.append(run)
                if arm=='U' or arm in {f'{f}-{x}' for f in ('C','Mplus') for x in LEVELS}:chosen.append(run)
                else:other.append(arm)
        emit(dict(group='morning-archive',archived=len(archived),chosen=len(chosen),
                  chosen_arms=dict(collections.Counter(p.name.split('-d201811',1)[0] for p in chosen)),
                  other_arms=dict(collections.Counter(other))))
        split=json.loads((SCRATCH/'tang3/t38/split-t38-v1.json').read_text(encoding='utf-8'))
        cells=split['test'];assert len(cells)==34
        budget_tot=collections.Counter()
        for cell in cells:
            c_name=f'C-30-{cell}'+('-rerun1' if cell=='d20181114-s10-r3-w17' else '')
            state_c,_,blocked,fc=scan(RESEARCH/'tier3-t38-v1'/c_name/'transcript-00.ndjson',True)
            state_u,_,_,fu=scan(RESEARCH/'tier3-t38-v1'/f'U-{cell}'/'transcript-00.ndjson')
            life_u={r['requestId']:r['lifecycle'] for r in state_u['requests']}
            rejected={r['requestId'] for r in state_c['requests'] if r['lifecycle']=='rejected'}
            for rid in rejected:budget_tot[('has-record' if rid in blocked else 'no-record')+':'+life_u[rid]]+=1
            emit(dict(group='budget-cell',cell=cell,rejected=len(rejected),recorded=len(rejected & blocked)))
            frames_total+=fc+fu
        emit(dict(group='budget-rejection',runs=len(cells),counts=dict(budget_tot)))
        emit(dict(all_parsed_relevant_frames_sha256_verified=frames_total))

if __name__=='__main__':main()
