"""Count alternatives in recorded portfolios; no policy/simulator implementation."""
import base64
import collections
import hashlib
import itertools
import json
import math
from pathlib import Path

ROOT=Path(__file__).resolve().parent
rows=[]
for arm in ['b1','c1']:
 for directory in sorted(Path('E:/RideBoundData/wp13/e1-retained-portfolio-panel-a').glob(f'p-*-{arm}-tight-s7')):
  c=collections.Counter()
  examples=[]
  digest=hashlib.sha256()
  for line in (directory/'transcript-00.ndjson').open('rb'):
   digest.update(line)
   frame=json.loads(base64.b64decode(json.loads(line)['frameBase64']))
   ev=frame.get('payload',{}).get('solver',{}).get('executionEvidence',{})
   if not ev.get('generation',{}).get('totalPendingRequestCount',0): continue
   c['pendingEpochs']+=1
   p=ev['candidatePortfolio']
   groups=collections.defaultdict(list)
   for candidate in p['candidates']:
    if candidate['policyEligibility']=='eligible': groups[candidate['vehicleId']].append(candidate)
   if len(groups)!=len(p['selectionProblem']['vehicleIds']): raise ValueError('missing vehicle')
   count=math.prod(len(g) for g in groups.values())
   c['largestCartesianProduct']=max(c['largestCartesianProduct'],count)
   if count>200000:
    c['notEnumeratedOver200000']+=1
    continue
   c['enumeratedEpochs']+=1
   max_count=-1
   optimal=0
   util_values=set()
   semantic_assignments=set()
   levels=p['selectionProblem']['objectiveLevels']
   ui=next((i for i,l in enumerate(levels) if l['name']=='worst-hard-utilization-ppm'),None)
   for combo in itertools.product(*groups.values()):
    reqs=[r for x in combo for r in x['newRequestIds']]
    if len(set(reqs))!=len(reqs): continue
    score=len(reqs)
    if score<max_count: continue
    if score>max_count:
     max_count=score; optimal=0; util_values=set(); semantic_assignments=set()
    optimal+=1
    semantic_assignments.add(tuple(sorted((x['vehicleId'],json.dumps({k:x[k] for k in ['newRequestIds','route','schedule']},sort_keys=True,separators=(',',':'))) for x in combo)))
    if ui is not None: util_values.add(max(x['objectiveContributions'][ui] for x in combo))
   selected_ids=set(p['selectedCandidateIds'])
   selected=[x for x in p['candidates'] if x['candidateId'] in selected_ids]
   selected_count=sum(len(x['newRequestIds']) for x in selected)
   if max_count!=selected_count: raise ValueError('recorded optimum mismatch')
   c['epochsAcceptingAtLeastOne']+=(max_count>0)
   c['epochsWithMultipleMaxAcceptanceAssignments']+=(optimal>1)
   c['acceptingEpochsWithMultipleAssignments']+=(max_count>0 and optimal>1)
   c['acceptingEpochsWithMultipleSemanticAssignments']+=(max_count>0 and len(semantic_assignments)>1)
   c['epochsWithUtilizationObjective']+=(ui is not None)
   c['utilizationConstantAcrossMaxAcceptanceAssignments']+=(ui is not None and len(util_values)==1)
   c['utilizationCanDistinguishMaxAcceptanceAssignments']+=(len(util_values)>1)
   if max_count>0 and optimal>1 and len(examples)<2:
    examples.append({'epoch':frame['epochId'],'accepted':max_count,'alternatives':optimal,'utilizationValues':sorted(util_values)})
  rows.append({'arm':arm,'directory':str(directory),'transcriptSha256':digest.hexdigest(),'counts':dict(c),'examples':examples})
  (ROOT/'portfolio-choice-audit.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
  print(arm,directory.name,dict(c),flush=True)
