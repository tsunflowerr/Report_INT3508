"""Audit existing outputs; never execute or change a RideBound policy."""
import base64
import collections
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
GROUPS = {
 'h6-b1': ('E:/RideBoundData/wp9/confirmatory-h6-panela-v2','p-*-b1-tight-s7'),
 'h6-c1': ('E:/RideBoundData/wp9/confirmatory-h6-panela-v2','p-*-c1-tight-s7'),
 'budget120': ('E:/RideBoundData/wp9/frontier-v1','fr-budget120-*-s7'),
 'hybrid120': ('E:/RideBoundData/wp14/levelc-v1','lc-*-s7'),
}

def scan(path):
    counts=collections.Counter()
    objective_values=collections.defaultdict(collections.Counter)
    objective_indices=collections.defaultdict(collections.Counter)
    witnesses=[]
    digest=hashlib.sha256()
    for line in path.open('rb'):
        digest.update(line)
        if not line.strip(): continue
        frame=json.loads(base64.b64decode(json.loads(line)['frameBase64']))
        if frame.get('messageType')!='decision': continue
        counts['decisions']+=1
        evidence=frame['payload'].get('solver',{}).get('executionEvidence',{})
        gen=evidence.get('generation',{})
        pending=gen.get('totalPendingRequestCount',0)>0
        counts['pendingEpochs']+=pending
        any_choice=False
        for loss in gen.get('vehicleLosses',[]):
            multi=loss['retainedCandidateCount']>1
            any_choice |= multi
            for prefix in ['all', 'pending' if pending else 'noPending']:
                counts[prefix+'VehicleEpochs']+=1
                counts[prefix+'MultipleCandidates']+=multi
                counts[prefix+'EvaluatedPaths']+=loss['evaluatedCandidatePathCount']
                counts[prefix+'PrunedPhysical']+=loss['physicallyOrSchedulePrunedCount']
        counts['pendingEpochsWithAnyVehicleChoice']+=pending and any_choice
        for b in evidence.get('selection',{}).get('finalSolverDiagnostics',{}).get('objectiveBounds',[]):
            name=b['objectiveName']
            if name.startswith('candidate-id'): continue
            objective_values[name][str(b['incumbentValue'])]+=1
            objective_indices[name][str(b['levelIndex'])]+=1
        for action in frame['payload']['actions']:
            if action['decisionType']!='promisePublished': continue
            p=action['payload']
            counts['publications']+=1
            for dim in ['pickupEtaTotalMs','dropEtaTotalMs']:
                a=p.get('decisionDelta',{}).get(dim,0)
                d=p.get('exogenousDelta',{}).get(dim,0)
                b=p.get('visibleDelta',{}).get(dim,0)
                counts['conductMs']+=a
                counts['driftMs']+=d
                counts['visibleMs']+=b
                counts['nonAdditiveEtaCoordinates']+=(b!=a+d)
                counts['visibleLessThanConductCoordinates']+=(b<a)
                if b<a and len(witnesses)<3:
                    witnesses.append({'epoch':frame['epochId'],'dimension':dim,'a':a,'d':d,'b':b,'publication':p})
    return {'path':str(path),'sha256':digest.hexdigest(),'counts':dict(counts),'objectiveValues':dict(objective_values),'objectiveIndices':dict(objective_indices),'counterexamples':witnesses}

report={}
for group,(root,pattern) in GROUPS.items():
    runs=[]
    for directory in sorted(Path(root).glob(pattern)):
        if not (directory/'summary.json').exists(): continue
        run=scan(directory/'transcript-00.ndjson')
        summary=json.loads((directory/'summary.json').read_text(encoding='utf-8'))
        semantic=json.loads((directory/'run-00.json').read_text(encoding='utf-8'))['semantic']
        run['status']=summary.get('status')
        run['repositoryInventorySha256']=summary.get('repositoryInventorySha256')
        run['accepted']=len(semantic['acceptedRequestIds'])
        runs.append(run)
    counts=collections.Counter()
    objs=collections.defaultdict(collections.Counter)
    for run in runs:
        counts.update(run['counts'])
        for name,values in run['objectiveValues'].items(): objs[name].update(values)
    report[group]={'runs':runs,'counts':dict(counts),'objectiveValues':dict(objs),'accepted':sum(r['accepted'] for r in runs)}
    (ROOT/'evidence-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(group,len(runs),dict(counts),'worstUtilization',dict(objs.get('worst-hard-utilization-ppm',{})),flush=True)
