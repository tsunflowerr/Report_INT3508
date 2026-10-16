"""Offline analysis of recorded feasibility graphs, not a dispatcher.

Maximum matching with at most one hypothetical new request per vehicle is a
conditional lower bound; actual pooling could serve multiple on one vehicle.
Enumerate unordered pairs of distinct observed OD/service types uniformly.
"""
import hashlib, itertools, json
from pathlib import Path
root=Path(__file__).parent
source=root/'retained-state-probe-all20.json'
data=json.loads(source.read_text())
rows=[]
for row in data['rows']:
    outcomes=[]
    for a in row['outcomes']:
        pairs=[]
        for x,y in itertools.combinations(a['futureResults'],2):
            vx,vy=set(x['vehicles']),set(y['vehicles'])
            served=2 if vx and vy and len(vx|vy)>1 else int(bool(vx|vy))
            pairs.append({'samples':[x['sample'],y['sample']], 'served':served,
                          'bothIndividuallyFeasible':bool(vx and vy)})
        outcomes.append({'ordinal':a['ordinal'],'isRecorded':a['isRecorded'],
                         'pairCount':len(pairs),'sumServed':sum(p['served'] for p in pairs),
                         'fullyServedPairs':sum(p['served']==2 for p in pairs),
                         'competingPairs':sum(p['bothIndividuallyFeasible'] and p['served']<2 for p in pairs),
                         'pairs':pairs})
    recorded=next((o for o in outcomes if o['isRecorded']),None)
    scores=[o['sumServed'] for o in outcomes]
    rows.append({'epoch':row['epoch'],'outcomes':outcomes,
                 'scoreVaries':len(set(scores))>1,
                 'recordedBelowMaximum':bool(recorded and scores and recorded['sumServed']<max(scores)),
                 'maximum':max(scores,default=None),'minimum':min(scores,default=None),
                 'recorded':recorded['sumServed'] if recorded else None})
result={'scope':'Conditional distinct-vehicle matching lower bound; no joint pooling or future forecast claim',
        'sourceSha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'epochs':len(rows),'scoreVariesEpochs':sum(r['scoreVaries'] for r in rows),
        'recordedBelowMaximumEpochs':sum(r['recordedBelowMaximum'] for r in rows),'rows':rows}
(root/'pair-competition-analysis.json').write_text(json.dumps(result,indent=2))
print(json.dumps({**{k:v for k,v in result.items() if k!='rows'},'rows':[{k:v for k,v in r.items() if k!='outcomes'} for r in rows]},indent=2))
