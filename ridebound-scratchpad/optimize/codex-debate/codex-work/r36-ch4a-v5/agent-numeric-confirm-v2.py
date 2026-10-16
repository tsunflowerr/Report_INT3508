"""Resolve a stale expected morning denominator with independent saved-run semantic check.
Reads prior raw-counter rows, then rereads all 64 run-00/summary JSONs. Create-only.
"""
from pathlib import Path
import collections,json
D=Path(__file__).resolve().parent
source=D/'agent-numeric-output-v2.txt'
rows=[json.loads(s.split(' ',1)[1]) for s in source.read_text(encoding='utf-8').splitlines() if s.startswith('MORNING_ROW ')]
assert len(rows)==64 and len({(r['arm'],r['cell']) for r in rows})==64
assert sum(r['acked'] for r in rows)==44270 and sum(r['forced'] for r in rows)==0
assert sum(r['sha256_checked_frames'] for r in rows)==88540
with (D/'agent-numeric-confirm-output-v2.txt').open('x',encoding='utf-8',newline='\n') as out:
    def emit(s):out.write(s+'\n');out.flush();print(s,flush=True)
    emit('CONFIRM: initial expected 55,963 was not supported; preserved first probe failed only its final hardcoded expected denominator assertion after all 64 raw morning runs.')
    emit('RAW_COUNTER_REAGGREGATION: 64 C-arm runs; forced 0 / acknowledged 44,270; 88,540 parsed decision/decisionApplied frame SHA256 checks.')
    count=semantic_total=0;by_arm=collections.defaultdict(collections.Counter)
    for row in rows:
        folder=Path(row['source']).parent
        run=json.loads((folder/'run-00.json').read_text(encoding='utf-8'))
        summary=json.loads((folder/'summary.json').read_text(encoding='utf-8'))
        assert run['status']=='succeeded' and summary['status']=='pass'
        count+=1;semantic_acks=run['semantic']['nextEpoch']-1
        assert semantic_acks==row['acked'],(folder,semantic_acks,row['acked'])
        semantic_total+=semantic_acks
        by_arm[row['arm']].update({'acked':row['acked'],'forced':row['forced'],'runs':1})
        emit(f'SEMANTIC_ROW {row["arm"]} {row["cell"]}: nextEpoch={run["semantic"]["nextEpoch"]}; raw_ack_count={row["acked"]}; summary_status=pass; source={folder/"run-00.json"}')
    for arm in sorted(by_arm,key=lambda s:int(s[2:])):emit('ARM_TOTAL '+arm+' '+json.dumps(dict(by_arm[arm]),sort_keys=True))
    assert count==64 and semantic_total==44270
    emit('CONFIRM_CHECK PASS: all 64 saved semantic epoch counts independently agree with raw acknowledged counts; denominator 44,270 confirmed.')