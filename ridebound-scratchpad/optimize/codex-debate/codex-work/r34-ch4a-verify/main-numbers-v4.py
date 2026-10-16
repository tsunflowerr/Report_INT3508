"""R34 independent read-only main-set recomputation; all writes exclusive in brief folder.
Inputs: IVC per-rider extraction (170 runs), Codex R19 v4 independent rider JSON (102 runs),
raw final checkpoints (102 runs). Does not execute or import earlier probes.
Strict lateness A-p0 > threshold; strict early A-p0 < -60000; signed c=p-e.
"""
from pathlib import Path
import json,base64,hashlib,csv,sys,statistics,collections,traceback
BASE=Path('E:/Code/Report_INT3508/ridebound-scratchpad')
DEST=BASE/'optimize/codex-debate/codex-work/r34-ch4a-verify'
CACHE=BASE/'tang3/t38/independent/cache'
STAGE=BASE/'optimize/codex-debate/codex-work/R19-stage1a-analysis.json'
SPLIT=BASE/'tang3/t38/split-t38-v1.json'

def backwards(path):
 with path.open('rb') as f:
  pos=f.seek(0,2);pending=b''
  while pos:
   n=min(pos,262144);pos-=n;f.seek(pos);parts=(f.read(n)+pending).split(b'\n');pending=parts[0]
   for line in reversed(parts[1:]):
    if line: yield line
  if pending: yield pending

def checkpoint(path):
 for line in backwards(path):
  o=json.loads(line);raw=base64.b64decode(o['frameBase64']);env=json.loads(raw)
  assert hashlib.sha256(raw).hexdigest()==o['frameSha256']
  if env['messageType']=='checkpoint' and o['direction']=='runnerToAdapter':
   return env['payload']['content']['onlineState'],o['ordinal'],o['frameSha256']
 raise RuntimeError('no checkpoint '+str(path))

out=(DEST/'main-numbers-v4.txt').open('x',encoding='utf-8');original=sys.stdout;sys.stdout=out
try:
 cells=json.loads(SPLIT.read_text(encoding='utf-8'))['test']; assert len(cells)==34 and len(set(cells))==34
 print('01 SCOPE: 34 test scenarios, 3672 requests; test cells loaded from',SPLIT)
 print('02 DEFINITIONS: served=alighted-and-promised; strict late A-p0>T*1000; early A-p0<-60000; signed c=p-e; signed share among late60 riders')
 print('03 INDEPENDENCE: reaggregate existing IVC and Codex R19 independent per-rider extractions; raw final checkpoints verify every p0,t0,ledger for U/C30/C120, all frame hashes checked')
 stage=json.loads(STAGE.read_text(encoding='utf-8'));SR={(r['arm'],r['cell']):r for r in stage['runs']}; rows=[]; stats={};keys={};allcache={}
 for arm in ['U','C-30','Mplus-30','Mplus-60','V-30']:
  ar=[];keys[arm]=set()
  for cell in cells:
   candidates=[CACHE/(arm+'-'+cell+'.json'),CACHE/(arm+'-'+cell+'-rerun1.json')]
   present=[p for p in candidates if p.exists()]; assert len(present)==1,(arm,cell,present)
   r=json.loads(present[0].read_text(encoding='utf-8'));assert r['status']=='pass';assert r['requests']==108
   completed={rid:q for rid,q in r['riders'].items() if rid in r['alight']};assert len(completed)==r['served']==len(r['alight'])==len(r['riders'])
   allcache[(arm,cell)]=r
   late={t:sum(r['alight'][rid]-q['p0_drop']>t*1000 for rid,q in completed.items()) for t in [30,60,120,300,600]}
   signed=sum(sum(v['p_d']-v['e_d'] for v in q['rev']) for rid,q in completed.items() if r['alight'][rid]-q['p0_drop']>60000)
   lat_sum=sum(r['alight'][rid]-q['p0_drop'] for rid,q in completed.items() if r['alight'][rid]-q['p0_drop']>60000)
   early=sum(r['alight'][rid]-q['p0_drop']<-60000 for rid,q in completed.items())
   worst=max((r['alight'][rid]-q['p0_drop'],cell,rid) for rid,q in completed.items())
   own=0 if arm=='U' else (sum(sum(abs(v['p_d']-v['e_d']) for v in q['rev'])>30000 for q in completed.values()) if arm=='C-30' else (late[30] if arm=='Mplus-30' else (late[60] if arm=='Mplus-60' else sum(sum(abs(v['p_d']-v['v_d']) for v in q['rev'])>30000 for q in completed.values()))))
   row=dict(arm=arm,cell=cell,served=len(completed),late30=late[30],late60=late[60],late120=late[120],early60=early,promise_breach=own,forced=r['nonNormalAcked'],acked=r['acked'])
   rows.append(row);ar.append(dict(row,late=late,signed=signed,lat_sum=lat_sum,worst=worst));keys[arm].update((cell,rid) for rid in completed)
  s=dict(served=sum(x['served'] for x in ar),late={t:sum(x['late'][t] for x in ar) for t in [30,60,120,300,600]},early=sum(x['early60'] for x in ar),signed=sum(x['signed'] for x in ar),lat_sum=sum(x['lat_sum'] for x in ar),worst=max(x['worst'] for x in ar),forced=sum(x['forced'] for x in ar),acked=sum(x['acked'] for x in ar),late30mean=statistics.mean(x['late30']/x['served'] for x in ar)*100,ownmean=statistics.mean(x['promise_breach']/x['served'] for x in ar)*100,forcedmean=statistics.mean(x['forced']/x['acked'] for x in ar)*100)
  stats[arm]=s
  print(f'ARM {arm}: served {s["served"]}; late30/60/120/300/600 '+str([s['late'][t] for t in [30,60,120,300,600]])+f'; timely60 {s["served"]-s["late"][60]}; timely120 {s["served"]-s["late"][120]}; early60 {s["early"]}; late30_mean_percent {s["late30mean"]:.8f}; late30_scenarios {sum(x["late30"]>0 for x in ar)}/34')
  print(f'LEDGER {arm}: signed dispatch seconds {s["signed"]/1000:.3f}; lateness seconds {s["lat_sum"]/1000:.3f}; share percent {s["signed"]/s["lat_sum"]*100:.8f}; late60 cohort {s["late"][60]}')
  print(f'WORST {arm}: {s["worst"][0]/1000:.3f} s; cell {s["worst"][1]}; request {s["worst"][2]}')
  print(f'OBLIGATIONS {arm}: own_breach {sum(x["promise_breach"] for x in ar)}/{s["served"]}; own_mean_percent {s["ownmean"]:.8f}; own_scenarios {sum(x["promise_breach"]>0 for x in ar)}/34; forced {s["forced"]}/{s["acked"]}; forced_mean_percent {s["forcedmean"]:.8f}')
 print('N11 C30 late60 by window',dict((w,sum(x['late60'] for x in rows if x['arm']=='C-30' and x['cell'].endswith(w))) for w in ['w07','w08','w17']))
 print('COHORT C30/Mplus30 common',len(keys['C-30']&keys['Mplus-30']),'C30 only',len(keys['C-30']-keys['Mplus-30']),'Mplus30 only',len(keys['Mplus-30']-keys['C-30']))
 raw_acc={a:dict(count=0,quote_sum=0,signed_late=0,lat_sum=0,late60=0,early60=0,late30=0,raw_mismatches=0) for a in ['U','C-30','C-120']}
 for arm in ['U','C-30','C-120']:
  for cell in cells:
   sr=SR[(arm,cell)];riders={r['request']:r for r in sr['riders']};parent=Path('C:/RideBoundData/research/tier3-t38c120-v1' if arm=='C-120' else 'C:/RideBoundData/research/tier3-t38-v1')
   name=arm+'-'+cell
   if arm=='C-30': name=allcache[(arm,cell)]['job']
   path=parent/name/'transcript-00.ndjson';st,ordinal,h=checkpoint(path)
   requests={q['requestId']:q for q in st['requests']}; ledger={q['requestId']:q for q in st['commitmentLedger']}
   completed={rid for rid,q in requests.items() if q['lifecycle']=='completed'};assert completed==set(riders)==set(ledger),(arm,cell)
   acc=raw_acc[arm]
   for rid in completed:
    q=requests[rid];ent=ledger[rid]['entries'];assert ent[0]['kind']=='initialPromise' and all(e['kind']=='revision' for e in ent[1:])
    p0=ent[0]['publishedPromise']['projection']['dropEtaMs'];t0=q['arrivalTimeMs'];rr=riders[rid]
    assert p0==rr['P0'] and ent[0]['publishedPromise']['publishedAtMs']==rr['t0'];acc['count']+=1;acc['quote_sum']+=p0-t0
    abs_c=sum(abs(e['publishedPromise']['projection']['dropEtaMs']-e['exogenousProjection']['dropEtaMs']) for e in ent[1:]);assert abs_c==rr['absolute_dispatch_ms']
    signed=sum(e['publishedPromise']['projection']['dropEtaMs']-e['exogenousProjection']['dropEtaMs'] for e in ent[1:]);lat=rr['arrival']-p0
    if arm in ['U','C-30']:
     iv=allcache[(arm,cell)];assert rr['arrival']==iv['alight'][rid];assert signed==sum(v['p_d']-v['e_d'] for v in iv['riders'][rid]['rev'])
    acc['early60']+=lat<-60000;acc['late60']+=lat>60000;acc['late30']+=lat>30000
    if lat>60000:acc['signed_late']+=signed;acc['lat_sum']+=lat
   print(f'RAW {arm}/{cell}: completed {len(completed)}; final checkpoint ordinal {ordinal}; frame sha256 {h}; p0/publication_time/absolute_c agreement with independent R19 JSON yes')
 for arm,acc in raw_acc.items():
  print(f'RAW_TOTAL {arm}: served {acc["count"]}; first_promise_sum_ms {acc["quote_sum"]}; first_promise_mean_min {acc["quote_sum"]/acc["count"]/60000:.10f}; late30 {acc["late30"]}; late60 {acc["late60"]}; early60 {acc["early60"]}; signed_late_seconds {acc["signed_late"]/1000:.3f}; lateness_seconds {acc["lat_sum"]/1000:.3f}; share_percent {acc["signed_late"]/acc["lat_sum"]*100:.8f}')
 with (DEST/'main-obligations-v4.tsv').open('x',encoding='utf-8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=['arm','cell','served','late30','late60','late120','early60','promise_breach','forced','acked'],delimiter='\t');w.writeheader();w.writerows(rows)
 print('OUTPUT main-obligations-v4.tsv: one row per arm/scenario; counts and denominators for mean-of-scenarios obligations rates')
 print('CHECK all 170 IVC runs passed; all 102 raw checkpoints frame hashes verified; all raw p0,publication_time,absolute_c matched existing independent R19 rider JSON; no unserved-in-served cohort, and every initial-promise ledger rider completed')
except Exception:
 traceback.print_exc(file=out)
 raise
finally:
 sys.stdout=original;out.close()