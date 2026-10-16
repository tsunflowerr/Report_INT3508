from pathlib import Path
import json,sys
BASE=Path('E:/Code/Report_INT3508/ridebound-scratchpad'); DEST=BASE/'optimize/codex-debate/codex-work/r34-ch4a-verify'
with (DEST/'main-source-probe-v3.txt').open('x',encoding='utf-8') as out:
 original=sys.stdout;sys.stdout=out
 p=BASE/'optimize/codex-debate/codex-work'; print('stage scripts',[str(x) for x in p.glob('*stage1a*')])
 for rel in ['tang3/t38/independent/iv_extract.py','optimize/codex-debate/codex-work/R19-stage1a-analysis.py']:
  p=BASE/rel;print('SOURCE',p,'exists',p.exists())
  if p.exists():
   for i,l in enumerate(p.read_text(encoding='utf-8').splitlines(),1):
    print(f'{i}: {l}')
 p=Path('C:/RideBoundData/research/tier3-t38c120-v1')
 print('C120 dirs first',[x.name for x in p.iterdir()][:5])
 p=next(p.glob('C-120-*/transcript-00.ndjson'))
 print('TRANSCRIPT',p)
 with p.open(encoding='utf-8') as fh:
  for i,l in enumerate(fh,1):
   o=json.loads(l)
   if i<3: print(i,str(o)[:2000])
   if any(s in l for s in ['promiseRevisions','oldPlanProjection','ledgerDelta']):
    print('REVISION FRAME',i,str(o)[:12000]);break
 for rel in ['rewrite-2026-10/drafts/08-chuong4-phanA-v4.tex','rewrite-2026-10/evidence/EVIDENCE-REGISTER-ADDENDUM-2-CH3.md']:
  p=BASE/rel; print('SNIPPET',p)
  for i,l in enumerate(p.read_text(encoding='utf-8').splitlines(),1):
   if rel.endswith('v4.tex') and (155<=i<=175 or 325<=i<=349 or 395<=i<=405 or 565<=i<=575): print(f'{i}: {l}')
   elif 'X3-16' in l: print(f'{i}: {l}')
 sys.stdout=original