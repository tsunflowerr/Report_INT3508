"""Read-only timestamp audit; no dispatcher, simulator, or schedule implementation."""
import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).parent
CAPTURE = ROOT / 'retained-states-e1-rejected-r1'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


receipt_path = CAPTURE / 'receipt.json'
receipt = json.loads(receipt_path.read_text(encoding='utf-8-sig'))
rows = []
types = Counter()
for record in receipt['saved']:
    files = {name: CAPTURE / (record['prefix'] + '-' + name + '.json')
             for name in ('before', 'event', 'decision')}
    for name, path in files.items():
        assert sha(path) == record[name + 'Sha256'], (record['epoch'], name)
    before = json.loads(files['before'].read_text())
    event = json.loads(files['event'].read_text())
    now = event['simTimeMs']
    assert now >= before['simulationTimeMs']
    requests = list(before['requests'])
    for item in event['payload']['events']:
        types[item['eventType']] += 1
        if item['eventType'] == 'requestArrived':
            requests.append(item['payload']['request'])
    future_openings = [r['requestId'] for r in requests if r['earliestPickupMs'] > now]
    rows.append({'epoch': record['epoch'], 'simTimeMs': now,
                 'requestsExaminedIncludingHistorical': len(requests),
                 'maximumEarliestPickupMinusNowMs': max(r['earliestPickupMs'] - now for r in requests),
                 'futurePickupOpeningRequestIds': future_openings,
                 'beforeSha256': record['beforeSha256'], 'eventSha256': record['eventSha256']})

result = {'kind': 'timestamp-only-waiting-opportunity-audit',
          'sourceSha256': sha(Path(__file__)), 'captureReceiptSha256': sha(receipt_path),
          'stateCount': len(rows), 'eventTypes': dict(types),
          'allKnownPickupWindowsAlreadyOpen': all(not r['futurePickupOpeningRequestIds'] for r in rows),
          'scope': 'All before-state requests plus newly arrived requests, including inactive historical requests; no state reduction or simulation performed.',
          'limitation': 'Does not test forecast value of waiting, execution adapter behavior, or another demand regime.',
          'rows': rows}
out = ROOT / 'waiting-opportunity-audit.json'
with out.open('x', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
print(json.dumps({k: v for k, v in result.items() if k != 'rows'}, indent=2))
