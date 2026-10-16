from pathlib import Path
import json, sys
BASE=Path('E:/Code/Report_INT3508/ridebound-scratchpad')
DEST=BASE/'optimize/codex-debate/codex-work/r34-ch4a-verify'
OUT=DEST/'main-source-probe.txt'
with OUT.open('x',encoding='utf-8') as output:
 sys.stdout=output
 for name in ['rewrite-2026-10/drafts/08-chuong4-phanA-v4.tex','rewrite-2026-10/evidence/EVIDENCE-REGISTER.md','rewrite-2026-10/evidence/EVIDENCE-REGISTER-ADDENDUM-2-CH3.md']:
  p=BASE/name
  print('\nSOURCE',p)
  for i,line in enumerate(p.read_text(encoding='utf-8').splitlines(),1):
   if any(word in line for word in ['292','289','660','232','14,15','14,12','61','76','20.760','N11','N-11','X3-16','23.027','6.892','4.836','31.353','12.450']): print(f'{i}: {line}')
 p=BASE/'tang3/t38/independent/cache'
 files=list(p.glob('*.json'))
 print('\nIVC',p,'count',len(files))
 print('first filenames',[f.name for f in files[:15]])
 for pref in ['U-','C-30-','Mplus-30-','Mplus-60-','V-30-']:
  chosen=next((f for f in files if f.name.startswith(pref)),None)
  if chosen:
   obj=json.loads(chosen.read_text(encoding='utf-8'))
   print('SCHEMA',chosen, str(obj)[:9000])
 p=BASE/'optimize/codex-debate/codex-work/R19-stage1a-analysis.json'
 print('\nSTAGE JSON',p,'exists',p.exists())
 if p.exists():
  obj=json.loads(p.read_text(encoding='utf-8'))
  print('TOP KEYS',list(obj) if isinstance(obj,dict) else type(obj))
  print('SAMPLE',str(obj)[:16000])
print(OUT)