"""Read-only snow configuration/source anchors; exclusive small output."""
import base64,hashlib,json,pathlib
SCRATCH=pathlib.Path('E:/Code/Report_INT3508/ridebound-scratchpad')
HERE=pathlib.Path(__file__).resolve().parent
OUT=HERE/'extra-snow-scope-output.txt'
FILES={
 'run_forecast.py':SCRATCH/'optimize/run_forecast.py',
 'snow-w14':SCRATCH/'optimize/snow/worlds/W5-d20181115-w14.json',
 'snow-w15':SCRATCH/'optimize/snow/worlds/W5-d20181115-w15.json',
 'wp4':SCRATCH/'tang3/configs/wp4-tier3-v2.json',
 'draft':SCRATCH/'rewrite-2026-10/drafts/08-chuong4-phanA-v4.tex',
}
with OUT.open('x',encoding='utf-8',newline='\n') as out:
 def emit(x):out.write(x+'\n');out.flush();print(x)
 for key,path in FILES.items():
  lines=path.read_text(encoding='utf-8').splitlines()
  for i,line in enumerate(lines,1):
   if key in ('snow-w14','snow-w15') or (
       key=='run_forecast.py' and (87<=i<=115 or i in (59,151))) or (
       key=='wp4' and any(s in line for s in ('commitmentRecovery','lateBoarding','policyVersion'))) or (
       key=='draft' and (any(s in line for s in ('136','192','864','1.075','nhiễu ngẫu nhiên')))):
    emit(f'{path}:{i}: {line}')
 root=pathlib.Path('C:/RideBoundData/research/tier3-forecast-v1')
 for run in sorted(root.glob('C-30-d20181115-s10-r*-w1[45]')):
  t=run/'transcript-00.ndjson'
  with t.open('rb') as handle:
   for line in handle:
    rec=json.loads(line);raw=base64.b64decode(rec['frameBase64'])
    env=json.loads(raw)
    if env.get('messageType')=='initializeRun':
     assert hashlib.sha256(raw).hexdigest()==rec['frameSha256']
     m=env['payload']['manifest']
     emit(f'{t}: initializeRun manifest keys: '+json.dumps(list(m)))
     chosen={k:v for k,v in m.items() if any(s in k.lower() for s in ('world','policy','config','recovery','seed'))}
     emit(json.dumps(chosen,ensure_ascii=False,sort_keys=True))
     break
