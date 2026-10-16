"""R36 counted morning service comparison supplement: reads raw final checkpoints.
Creates only new small text output beside script; no imports of previous probes.
"""
from pathlib import Path
import base64,json,hashlib,collections
S=Path('E:/Code/Report_INT3508/ridebound-scratchpad')
R=Path('C:/RideBoundData/research')
D=Path(__file__).resolve().parent

def reversed_lines(path):
    with path.open('rb') as f:
        pos=f.seek(0,2);pending=b''
        while pos:
            n=min(pos,1048576);pos-=n;f.seek(pos)
            parts=(f.read(n)+pending).split(b'\n');pending=parts[0]
            for line in reversed(parts[1:]):
                if line:yield line
        if pending:yield pending

def final(path):
    for line in reversed_lines(path):
        if not line.startswith(b'{"direction":"runnerToAdapter"'):continue
        encoded=line.split(b'"frameBase64":"',1)[1].split(b'"',1)[0]
        if b'"messageType":"checkpoint"' not in base64.b64decode(encoded[:256]):continue
        rec=json.loads(line);raw=base64.b64decode(rec['frameBase64'],validate=True)
        assert hashlib.sha256(raw).hexdigest()==rec['frameSha256']
        env=json.loads(raw)
        return env['payload']['content']['onlineState'],rec['ordinal'],rec['frameSha256']
    raise AssertionError(path)

with (D/'agent-numeric-supplement-output-v2.txt').open('x',encoding='utf-8',newline='\n') as out:
    def emit(text):out.write(text+'\n');out.flush();print(text,flush=True)
    split=json.loads((S/'tang3/t38/split-t38-v1.json').read_text(encoding='utf-8'))['test']
    for arm in ('C-30','Mplus-30'):
        count=0;served=0;late=0
        for cell in split:
            choices=[p for p in ((S/'tang3/t38/independent/cache')/(arm+'-'+cell+'.json'),(S/'tang3/t38/independent/cache')/(arm+'-'+cell+'-rerun1.json')) if p.exists()]
            assert len(choices)==1
            obj=json.loads(choices[0].read_text(encoding='utf-8'))
            n=sum(obj['alight'][rid]-q['p0_drop']>30000 for rid,q in obj['riders'].items())
            count+=n>0;served+=obj['served'];late+=n
        emit(f'MAIN_LATE30_SCENARIOS {arm}: {count}/34 scenarios; late riders={late}/{served}')
        assert count==28
    levels=(30,60,90,120,150,180,240,300)
    cells=[f'd201811{d}-s10-r{rep}-w07' for d in (12,13) for rep in (1,2,3,4)]
    for level in levels:
        root='tier3-w07-v1' if level in (30,60,120,300) else 'tier3-w07x-v1'
        totals=collections.Counter();differences=[]
        for cell in cells:
            counts={}
            for family in ('C','Mplus'):
                path=R/root/(f'{family}-{level}-'+cell)/'transcript-00.ndjson'
                state,ordinal,digest=final(path)
                assert len(state['requests'])==108
                completed=sum(q['lifecycle']=='completed' for q in state['requests'])
                counts[family]=completed;totals[family]+=completed
                out.write(f'RAW_SERVE {family}-{level} {cell}: completed={completed}; final_checkpoint_ordinal={ordinal}; frame_sha256={digest}; source={path}\n')
            differences.append(counts['C']-counts['Mplus'])
        emit(f'MORNING_SERVICE level={level}: C={totals["C"]}; Mplus={totals["Mplus"]}; pooled_difference={totals["C"]-totals["Mplus"]}; per_scenario_differences={differences}; max_abs_scenario_difference={max(map(abs,differences))}')
        assert abs(totals['C']-totals['Mplus'])<=2
    emit('CHECK PASS: at each of the eight displayed morning cap levels, pooled served counts differ by at most two.')