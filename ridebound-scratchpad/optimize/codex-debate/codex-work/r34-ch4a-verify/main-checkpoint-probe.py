from pathlib import Path
import json,base64,sys,hashlib
BASE=Path('E:/Code/Report_INT3508/ridebound-scratchpad'); DEST=BASE/'optimize/codex-debate/codex-work/r34-ch4a-verify'
def backwards(path):
 with path.open('rb') as f:
  pos=f.seek(0,2); pending=b''
  while pos:
   n=min(pos,262144);pos-=n;f.seek(pos); data=f.read(n)+pending;parts=data.split(b'\n');pending=parts[0]
   for line in reversed(parts[1:]):
    if line: yield line
  if pending: yield pending
with (DEST/'main-checkpoint-probe.txt').open('x',encoding='utf-8') as out:
 original=sys.stdout;sys.stdout=out
 p=Path('C:/RideBoundData/research/tier3-t38c120-v1/C-120-d20181114-s10-r3-w07/transcript-00.ndjson')
 for i,line in enumerate(backwards(p)):
  outer=json.loads(line);raw=base64.b64decode(outer['frameBase64']);env=json.loads(raw);print('TAIL',i,outer['ordinal'],env['messageType'])
  if env['messageType']=='checkpoint':
   print('HASH_MATCH',hashlib.sha256(raw).hexdigest()==outer['frameSha256']);st=env['payload']['content']['onlineState'];print('STATE_KEYS',list(st));print('REQUEST',st['requests'][0]);print('LEDGER',str(st['commitmentLedger'][0])[:5500]);break
 sys.stdout=original