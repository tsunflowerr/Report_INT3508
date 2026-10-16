"""R36 targeted numeric verification, read-only inputs, create-only output.
No simulations/builds/import of older probes. IVC are independently extracted JSONs,
not rerun simulator output. Raw promise checkpoints and morning counters re-read.
"""
from pathlib import Path
import base64,collections,csv,hashlib,json,statistics,concurrent.futures
S=Path('E:/Code/Report_INT3508/ridebound-scratchpad')
R=Path('C:/RideBoundData/research')
D=Path(__file__).resolve().parent
CACHE=S/'tang3/t38/independent/cache'
CELLS=json.loads((S/'tang3/t38/split-t38-v1.json').read_text(encoding='utf-8'))['test']
assert len(CELLS)==34 and len(set(CELLS))==34
OUTPUT=D/'agent-numeric-output-v2.txt'
ROWS=[]

def decode(line):
    record=json.loads(line)
    raw=base64.b64decode(record['frameBase64'],validate=True)
    assert hashlib.sha256(raw).hexdigest()==record['frameSha256']
    assert len(raw)==record['frameLengthBytes']
    return record,json.loads(raw)

def prefix(line):
    encoded=line.split(b'"frameBase64":"',1)[1].split(b'"',1)[0][:256]
    return base64.b64decode(encoded)

def tail_lines(path):
    with path.open('rb') as f:
        pos=f.seek(0,2);suffix=b''
        while pos:
            size=min(pos,1048576);pos-=size;f.seek(pos)
            parts=(f.read(size)+suffix).split(b'\n');suffix=parts[0]
            for line in reversed(parts[1:]):
                if line:yield line
        if suffix:yield suffix

def checkpoint(path):
    for line in tail_lines(path):
        if not line.startswith(b'{"direction":"runnerToAdapter"'):continue
        if b'"messageType":"checkpoint"' not in prefix(line):continue
        record,envelope=decode(line)
        return envelope['payload']['content']['onlineState'],record['ordinal'],record['frameSha256']
    raise AssertionError('no final checkpoint '+str(path))

def manifest(path):
    with path.open('rb') as f:
        for line in f:
            record,envelope=decode(line)
            if envelope['messageType']=='initializeRun':
                found=[]
                def walk(value):
                    if isinstance(value,dict):
                        if 'binarySha256' in value:found.append(value)
                        for v in value.values():walk(v)
                    elif isinstance(value,list):
                        for v in value:walk(v)
                walk(envelope['payload'])
                assert len(found)==1,(path,found)
                m=found[0]
                fields=('binarySha256','coreCommitSha','policyId','policyVersion','policyConfigurationHash')
                return tuple(m[x] for x in fields),record['ordinal'],record['frameSha256']
    raise AssertionError('no manifest '+str(path))

def main_counts(emit):
    emit('MAIN: freshly read all 170 IVC extraction JSONs for five arms x 34 held-out scenarios; strict A-p0 thresholds; V sum |p-v|, C sum |p-e|.')
    for arm in ('U','C-30','Mplus-30','Mplus-60','V-30'):
        ar=[]
        for cell in CELLS:
            paths=[p for p in (CACHE/(arm+'-'+cell+'.json'),CACHE/(arm+'-'+cell+'-rerun1.json')) if p.exists()]
            assert len(paths)==1,(arm,cell)
            path=paths[0];data=json.loads(path.read_text(encoding='utf-8'))
            assert data['status']=='pass' and data['requests']==108
            riders=data['riders'];alight=data['alight']
            assert set(riders)==set(alight) and len(riders)==data['served']
            late={t:sum(alight[rid]-q['p0_drop']>t*1000 for rid,q in riders.items()) for t in (30,60,120)}
            if arm=='U':breach=0
            elif arm=='C-30':breach=sum(sum(abs(v['p_d']-v['e_d']) for v in q['rev'])>30000 for q in riders.values())
            elif arm=='V-30':breach=sum(sum(abs(v['p_d']-v['v_d']) for v in q['rev'])>30000 for q in riders.values())
            else:breach=late[int(arm.split('-')[1])]
            row=dict(arm=arm,cell=cell,served=len(riders),breach=breach,forced=data['nonNormalAcked'],acked=data['acked'],late30=late[30],late60=late[60],late120=late[120],source=str(path),job=data['job'])
            ROWS.append(row);ar.append(row)
            emit('MAIN_ROW '+json.dumps(row,sort_keys=True))
        total={k:sum(x[k] for x in ar) for k in ('served','breach','forced','acked','late30','late60','late120')}
        positive=sum(x['breach']>0 for x in ar)
        total['positive_breach_scenarios']=positive;total['scenarios']=len(ar)
        total['breach_mean_percent']=statistics.mean(x['breach']/x['served'] for x in ar)*100
        total['forced_mean_percent']=statistics.mean(x['forced']/x['acked'] for x in ar)*100
        emit('MAIN_TOTAL '+arm+' '+json.dumps(total,sort_keys=True))
    for window in ('w07','w08','w17'):
        subset=[x for x in ROWS if x['arm']=='Mplus-30' and x['cell'].endswith(window)]
        total={k:sum(x[k] for x in subset) for k in ('served','breach','forced','acked')}
        total['positive_breach_scenarios']=sum(x['breach']>0 for x in subset);total['scenarios']=len(subset)
        emit('MAIN_WINDOW '+window+' '+json.dumps(total,sort_keys=True))
    expected={'C-30':(0,20101,0,2338,0),'Mplus-30':(7710,20103,289,2338,28),'Mplus-60':(4031,20163,79,2347,22),'V-30':(10442,20090,456,2336,34)}
    for arm,want in expected.items():
        rr=[x for x in ROWS if x['arm']==arm]
        got=(sum(x['forced'] for x in rr),sum(x['acked'] for x in rr),sum(x['breach'] for x in rr),sum(x['served'] for x in rr),sum(x['breach']>0 for x in rr))
        assert got==want,(arm,got,want)
    emit('MAIN_EXPECTED_CHECK PASS all four R34 pooled table rows and Mplus-30 windows agree; U forced=0/20760.')
    assert sum(x['acked'] for x in ROWS if x['arm']=='U')==20760 and sum(x['forced'] for x in ROWS if x['arm']=='U')==0

def promise_counts(emit):
    emit('PROMISE: freshly reread 68 final raw checkpoints; sum first promised drop ETA minus request arrivalTimeMs, completed riders only, pooled by rider.')
    for arm,want in (('U',(2434,2065946452)),('C-30',(2338,1980192800))):
        count=duration_sum=0
        for row in [r for r in ROWS if r['arm']==arm]:
            path=R/'tier3-t38-v1'/row['job']/'transcript-00.ndjson'
            state,ordinal,digest=checkpoint(path)
            requests={q['requestId']:q for q in state['requests']}
            done={rid for rid,q in requests.items() if q['lifecycle']=='completed'}
            ledgers={q['requestId']:q['entries'] for q in state['commitmentLedger']}
            assert set(ledgers)==done and len(done)==row['served']
            this_sum=0
            for rid in done:
                first=[e for e in ledgers[rid] if e['kind']=='initialPromise'];assert len(first)==1
                p0=first[0]['publishedPromise']['projection']['dropEtaMs']
                this_sum+=p0-requests[rid]['arrivalTimeMs']
            duration_sum+=this_sum;count+=len(done)
            emit(f'PROMISE_ROW {arm} {row["cell"]} count={len(done)} duration_sum_ms={this_sum} checkpoint_ordinal={ordinal} sha256={digest} source={path}')
        assert (count,duration_sum)==want,(arm,count,duration_sum)
        emit(f'PROMISE_TOTAL {arm}: count={count}; duration_sum_ms={duration_sum}; mean_min={duration_sum/count/60000:.10f}; rounded={duration_sum/count/60000:.2f}')

def snow_check(emit):
    emit('SNOW: freshly read initializeRun manifest of all eight forecast-off snow runs and 51 archived main C-30 folders; compare five fields; hash archived DLL and canonical configs.')
    snow=sorted((R/'tier3-forecast-v1').glob('C-30-d20181115-s10-r*-w1[45]'))
    main=sorted((R/'tier3-t38-v1').glob('C-30-*'))
    main=[p for p in main if p.is_dir() and (p/'transcript-00.ndjson').exists()]
    assert len(snow)==8 and len(main)==51,(len(snow),len(main))
    values={}
    for kind,runs in (('snow',snow),('main-C30-archive',main)):
        groups=collections.Counter()
        for folder in runs:
            value,ordinal,digest=manifest(folder/'transcript-00.ndjson');groups[value]+=1
            emit(f'MANIFEST_ROW {kind} {folder.name}: ordinal={ordinal}; frame_sha256={digest}; tuple={value}')
        assert len(groups)==1;values[kind]=next(iter(groups))
        emit(f'MANIFEST_TOTAL {kind}: folders={len(runs)}; distinct_five_field_tuples={len(groups)}; tuple={values[kind]}')
    assert values['snow']==values['main-C30-archive']
    dll=R/'runner-tier3-v2/RideBound.Runner.dll'
    dll_hash=hashlib.sha256(dll.read_bytes()).hexdigest();assert dll_hash==values['snow'][0]
    emit(f'DLL_CHECK {dll}: SHA256={dll_hash}; matches all manifests')
    configs=[]
    for name in ('C-30.json','wp4-tier3-v2.json'):
        path=S/'tang3/configs'/name
        obj=json.loads(path.read_text(encoding='utf-8'))
        raw=json.dumps(obj,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode('utf-8')
        digest=hashlib.sha256(raw).digest();configs.append(digest)
        emit(f'CONFIG_CANONICAL {path}: sha256={digest.hex()}')
        if name.startswith('wp4'):assert obj['commitmentRecovery']=='no-worse-than-reference-v1'
    bind=hashlib.sha256(b'RideBound.Wp4RunnerConfigurationBinding.v1\0'+b''.join(configs)).hexdigest()
    assert bind==values['snow'][4],bind
    emit(f'CONFIG_BINDING_CHECK {bind}: matches all 59 manifest policyConfigurationHash values; WP4 config line 7 commitmentRecovery=no-worse-than-reference-v1.')

def morning_raw(task):
    arm,cell=task
    root='tier3-w07-v1' if int(arm[2:]) in (30,60,120,300) else 'tier3-w07x-v1'
    path=R/root/(arm+'-'+cell)/'transcript-00.ndjson'
    decisions={};acked=set();frames=0
    with path.open('rb') as f:
        for line in f:
            head=prefix(line)
            is_decision=b'"messageType":"decision"' in head
            is_ack=b'"messageType":"decisionApplied"' in head
            if not is_decision and not is_ack:continue
            record,envelope=decode(line);frames+=1
            pl=envelope['payload'];h=pl['decisionHash']
            if is_decision:
                assert record['direction']=='runnerToAdapter'
                body=pl.get('certificate',{}).get('body',{})
                assert 'normalOperation' in body,(path,record['ordinal'])
                normal=body['normalOperation'];assert isinstance(normal,bool)
                decisions.setdefault(h,(normal,record['ordinal']))
            else:
                assert record['direction']=='adapterToRunner'
                assert h in decisions and decisions[h][1]<record['ordinal'],(path,h)
                acked.add(h)
    forced=sum(not decisions[h][0] for h in acked)
    return dict(arm=arm,cell=cell,forced=forced,acked=len(acked),sha256_checked_frames=frames,source=str(path))

def morning_check(emit):
    levels=(30,60,90,120,150,180,240,300)
    cells=[f'd201811{day}-s10-r{rep}-w07' for day in (12,13) for rep in (1,2,3,4)]
    tasks=[(f'C-{b}',c) for b in levels for c in cells]
    total=collections.Counter();by_arm=collections.defaultdict(collections.Counter)
    emit('MORNING: reread all 64 C-arm transcripts; hash-check every parsed decision and decisionApplied frame; distinct acknowledgements only; forced iff acknowledged certificate body.normalOperation=false.')
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        for row in pool.map(morning_raw,tasks):
            emit('MORNING_ROW '+json.dumps(row,sort_keys=True))
            total.update({k:row[k] for k in ('forced','acked','sha256_checked_frames')})
            by_arm[row['arm']].update({k:row[k] for k in ('forced','acked')})
    for arm in sorted(by_arm,key=lambda x:int(x[2:])):emit('MORNING_ARM '+arm+' '+json.dumps(dict(by_arm[arm]),sort_keys=True))
    assert total['forced']==0 and total['acked']==55963,total
    emit('MORNING_TOTAL '+json.dumps(dict(total),sort_keys=True)+'; runs=64; levels=8; scenarios_per_level=8; expected_0/55963=PASS')

with OUTPUT.open('x',encoding='utf-8',newline='\n') as out:
    def emit(line):
        out.write(line+'\n');out.flush()
        if not any(line.startswith(k) for k in ('MAIN_ROW ','PROMISE_ROW ','MANIFEST_ROW ')):print(line,flush=True)
    emit('R36 numeric check v2, independent read-only reaggregation; no simulations, no builds, no installs; output created exclusively.')
    main_counts(emit)
    promise_counts(emit)
    snow_check(emit)
    morning_check(emit)
    emit('ALL_CHECKS PASS')