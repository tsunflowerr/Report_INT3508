from pathlib import Path
import json,sys
BASE=Path('E:/Code/Report_INT3508/ridebound-scratchpad')
DEST=BASE/'optimize/codex-debate/codex-work/r34-ch4a-verify'
with (DEST/'main-source-probe-v2.txt').open('x',encoding='utf-8') as out:
 original=sys.stdout; sys.stdout=out
 p=BASE/'tang3/t38/independent/cache'; files=list(p.glob('*.json'))
 print('IVC',len(files)); print('filenames', [f.name for f in files[:16]])
 for pref in ['U-','C-30-','Mplus-30-','Mplus-60-','V-30-']:
  f=next((f for f in files if f.name.startswith(pref)),None)
  print('\nPREFIX',pref,'MATCH',f)
  if not f: continue
  o=json.loads(f.read_text(encoding='utf-8')); print('KEYS',list(o))
  for k,v in o.items():
   print('FIELD',k,'TYPE',type(v).__name__,'LEN',len(v) if hasattr(v,'__len__') else '')
   if isinstance(v,dict):
    print('keys',list(v)[:10]); kk=next(iter(v),None)
    if kk is not None: print('first',kk,str(v[kk])[:1500])
   elif isinstance(v,list): print('first',str(v[:1])[:1500])
   else: print(str(v)[:1000])
 f=BASE/'optimize/codex-debate/codex-work/R19-stage1a-analysis.json'; o=json.loads(f.read_text(encoding='utf-8'))
 print('\nSTAGE INPUTS',o['inputs'])
 print('RUN SCHEMA',list(o['runs'][0]))
 print('RIDERS SCHEMA',o['runs'][0]['riders'][0])
 for rel in ['tang3/t38/independent/iv_analyze.py','rewrite-2026-10/evidence/checks-ch4a-v2/check_ch4a_v2.py','rewrite-2026-10/evidence/checks-ch4a-v2/ledger_share_sums.py']:
  f=BASE/rel; print('\nSOURCE',f)
  for i,line in enumerate(f.read_text(encoding='utf-8').splitlines(),1):
   if rel.endswith('iv_analyze.py') and i>160: break
   print(f'{i}: {line}')
 sys.stdout=original