import hashlib, json
from pathlib import Path
root=Path(__file__).parent
source=root/'retained-state-probe-all20.json'
data=json.loads(source.read_text())
rows=[]
for r in data['rows']:
    outcomes=r['outcomes']
    scores=[sum(f['feasible'] for f in a['futureResults']) for a in outcomes]
    recorded=[a for a in outcomes if a['isRecorded']]
    if outcomes and len(recorded)!=1: raise ValueError('Missing/duplicate recorded selection')
    patterns={tuple(f['sample'] for f in a['futureResults'] if f['feasible']) for a in outcomes}
    vehicle_patterns={tuple((f['sample'],tuple(f['vehicles'])) for f in a['futureResults']) for a in outcomes}
    rows.append({'epoch':r['epoch'],'alternatives':len(outcomes),'samples':r['sampleCount'],
        'minCoverage':min(scores,default=None),'maxCoverage':max(scores,default=None),
        'uniqueCoveredSampleSets':len(patterns),'uniqueVehicleCoveragePatterns':len(vehicle_patterns),
        'recordedCoverage':sum(f['feasible'] for f in recorded[0]['futureResults']) if recorded else None,
        'minEvaluationMs':min((a['elapsedMs'] for a in outcomes),default=None),
        'maxEvaluationMs':max((a['elapsedMs'] for a in outcomes),default=None)})
eligible=[r for r in rows if r['alternatives']>1 and r['samples']>0]
result={'source':str(source),'sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
    'capturedEpochs':len(rows),'multiAlternativeWithSamples':len(eligible),
    'coverageCountDistinguishes':sum(r['minCoverage']!=r['maxCoverage'] for r in eligible),
    'coverageSetDistinguishes':sum(r['uniqueCoveredSampleSets']>1 for r in eligible),
    'vehicleCoverageDistinguishes':sum(r['uniqueVehicleCoveragePatterns']>1 for r in eligible),
    'allAssignments':sum(r['alternatives'] for r in rows),'rows':rows}
(root/'retained-state-probe-analysis.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
