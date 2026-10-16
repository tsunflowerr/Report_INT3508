from pathlib import Path
import base64,collections,concurrent.futures,csv,hashlib,json
HERE=Path(__file__).resolve().parent
raw=json.loads((HERE/'R13-raw-verification.json').read_text(encoding='utf-8'))
u_rows=list(csv.DictReader((HERE/'R13-rider-budget.tsv').open(encoding='utf-8'),delimiter='\t'))
u_done={(r['cell'],r['request_id']) for r in u_rows if r['population']=='t38' and r['arm']=='U' and r['lifecycle']=='completed'}
jobs=[r for r in raw['runs'] if r['population']=='t38' and r['arm'] in ('U','C-30')]
def scan(run):
 last=None;candidates=[];first_objectives=None
 with Path(run['transcript']).open('rb') as f:
  for line in f:
   row=json.loads(line);e=json.loads(base64.b64decode(row['frameBase64']))
   if e.get('messageType')=='checkpoint' and row['direction']=='runnerToAdapter':last=e['payload']['content']['onlineState']
   if e.get('messageType')=='decision':
    evidence=((e['payload'].get('solver') or {}).get('executionEvidence') or {})
    if first_objectives is None:first_objectives=(e['payload'].get('solver') or {})
    if run['arm']=='C-30':
     for pc in evidence.get('prunedCandidates',[]):
      ws=[w for w in pc.get('commitmentWitnesses',[]) if w['code']=='COMMITMENT_BUDGET_EXCEEDED']
      if pc['code']=='COMMITMENT_BUDGET_EXCEEDED' and ws:
       candidates += [(rid,[w['requestId'] for w in ws]) for rid in pc.get('newRequestIds',[])]
 assert last
 rejected={r['requestId'] for r in last['requests'] if r['lifecycle']=='rejected'}
 candidates=[((run['cell'],rid),blockers) for rid,blockers in candidates if rid in rejected]
 stats=collections.Counter();witnesses=[]
 for ledger in last['commitmentLedger']:
  cs=[e['publishedPromise']['projection']['dropEtaMs']-e['exogenousProjection']['dropEtaMs'] for e in ledger['entries'] if e['kind']=='revision']
  stats['riders']+=1;stats['exposed']+=any(cs);stats['multi']+=sum(c!=0 for c in cs)>=2
  for b in (30,60,120,300):
   if max(map(abs,cs),default=0)<=b*1000<sum(map(abs,cs)):
    stats[f'cum_only_{b}']+=1
    if b==120:witnesses.append({'cell':run['cell'],'request':ledger['requestId'],'nonzero_signed_ms':[c for c in cs if c]})
 return run['arm'],stats,candidates,witnesses
pops=collections.defaultdict(collections.Counter);cands=[];wits=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
 for i,(arm,st,cc,ww) in enumerate(pool.map(scan,jobs),1):
  pops[arm].update(st);cands.extend(cc);wits.extend(ww)
  if i%8==0:print('Read existing transcripts',i,'/',len(jobs),flush=True)
shares=[]
for share in (0,.1,.2,.3,.5,1):
 passed={key for key,blockers in cands if all(int(hashlib.sha256(f'{key[0]}|{b}'.encode()).hexdigest(),16)%10000 >= share*10000 for b in blockers)}
 shares.append({'share':share,'passing_requests':len(passed),'served_U':len(passed&u_done)})
weekday=list(csv.DictReader(Path('E:/Code/Report_INT3508/ridebound-scratchpad/optimize/test-family-a-causal-no15-2026-10-06-cells.tsv').open(encoding='utf-8'),delimiter='\t'))
weekday=[r for r in weekday if r['arm']=='C-30' and r['cell'][1:9] in ('20181114','20181115','20181116')]
result={'analysis_only':True,'existing_transcripts_read':len(jobs),'populations':dict(pops),'U_cum120_witnesses':wits,'tier':{'blocked_requests':len({k for k,b in cands}),'candidate_records':len(cands),'blocker_counts':dict(collections.Counter(len(set(b)) for k,b in cands)),'shares':shares},'weekday':{'cells':len(weekday),'served':sum(int(r['served']) for r in weekday),'forecast_late':sum(float(r['Y_disp'])*int(r['served']) for r in weekday),'naive_late':sum(float(r['Y_naive'])*int(r['served']) for r in weekday)}}
print(json.dumps(result,indent=2),flush=True)
