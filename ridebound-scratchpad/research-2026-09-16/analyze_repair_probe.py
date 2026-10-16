"""Validate external probe coverage/provenance and summarize; no dispatch logic."""
import hashlib,json
from collections import Counter
from pathlib import Path

root=Path(__file__).parent
capture=root/'retained-states-e1-rejected-r1'
receipt=json.loads((capture/'receipt.json').read_text())
probe_path=root/'retained-repair-rejected-probe.json'
probe=json.loads(probe_path.read_text())
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
source=Path(receipt['transcript'])
assert sha(source)==receipt['transcriptSha256']
assert receipt['rejectedOnly']
saved={r['epoch']:r for r in receipt['saved']}
rows={r['epoch']:r for r in probe['rows']}
assert len(saved)==len(receipt['saved']) and len(rows)==len(probe['rows'])
assert rows.keys()==saved.keys()
for epoch,r in saved.items():
    for suffix,key in [('before','beforeSha256'),('event','eventSha256'),('decision','decisionSha256')]:
        assert sha(capture/f"{r['prefix']}-{suffix}.json")==r[key]
    assert rows[epoch]['inputStateSha256']==r['beforeSha256']
    assert rows[epoch]['status']=='complete' and rows[epoch]['baselineAccept']==0
physical=Counter();hard=Counter()
for r in rows.values():
    physical.update(r['generatedPhysicalPrunes'])
    hard.update(r['retainedHardPrunes'])
result={
    'kind':'validated-same-state-waiting-pair-repair-negative-result',
    'captureReceiptSha256':sha(capture/'receipt.json'),
    'probeSha256':sha(probe_path),
    'transcriptSha256':receipt['transcriptSha256'],
    'exactMatchedResponses':receipt['matchedResponses'],
    'rejectedStates':len(rows),'epochs':sorted(rows),
    'completeGenerationStates':sum(r['generationComplete'] for r in rows.values()),
    'rescuedStates':sum(r['newAcceptOpportunity'] for r in rows.values()),
    'rawRetainedRepairCandidates':sum(r['rawRepairCandidateCount'] for r in rows.values()),
    'headScreenRemoved':sum(r['headScreenRemoved'] for r in rows.values()),
    'physicalFirstWitnessCounts':dict(physical),'hardFirstWitnessCounts':dict(hard),
    'limitations':['One previously observed C1tight run; not held-out or closed-loop.',
      'One waiting incumbent pair per repair; no onboard drop reordering, joint moves or reassignment.',
      'Conservative leading same-node block screen is not full FleetPy locked-leg validation.',
      'Fail-fast witness counts are neither minimal causes nor independent requests.',
      'No rescue does not establish DARP infeasibility or rule out a different earlier trajectory.']}
(root/'repair-probe-analysis.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
