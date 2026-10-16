"""Read-only source inspection; output exclusive-created beside this script."""
import base64
import json
from pathlib import Path

S = Path('E:/Code/Report_INT3508/ridebound-scratchpad')
O = Path(__file__).parent
report = {}
for name, p in {
    'CXJ': S / 'optimize/codex-debate/codex-work/R19-stage1a-analysis.json',
    'BI': S / 'optimize/independent-B/b_results.json',
}.items():
    obj = json.loads(p.read_text(encoding='utf-8'))
    report[name] = {'path': str(p), 'type': type(obj).__name__, 'keys': list(obj)[:15]}
    if isinstance(obj, dict):
        for k, v in list(obj.items())[:6]:
            if isinstance(v, dict):
                report[name][k] = {'keys': list(v)[:15], 'first': repr(next(iter(v.values()), None))[:1000]}
            elif isinstance(v, list):
                report[name][k] = {'len': len(v), 'first': repr(v[:1])[:1500]}
            else:
                report[name][k] = v
p = Path('C:/RideBoundData/research/tier3-forecast-v1/C-30-d20181115-s10-r1-w14/transcript-00.ndjson')
last_checkpoint = None
types = {}
events = None
with p.open(encoding='utf-8') as f:
    for line in f:
        outer = json.loads(line)
        frame = json.loads(base64.b64decode(outer['frameBase64']))
        kind = frame.get('messageType')
        types[kind] = types.get(kind, 0) + 1
        if kind == 'initializeRun':
            report['initializeRun'] = frame['payload']
        elif kind == 'checkpoint' and outer['direction'] == 'runnerToAdapter':
            last_checkpoint = frame['payload']['content']['onlineState']
        elif kind == 'eventBatch' and events is None:
            events = frame['payload']
report['snow_types'] = types
report['event_example'] = events
report['state_keys'] = list(last_checkpoint)
report['request_example'] = last_checkpoint['requests'][:1]
report['ledger_example'] = last_checkpoint['commitmentLedger'][:1]
with (O / 'probe-source-schema-v2.json').open('x', encoding='utf-8') as f:
    json.dump(report, f, ensure_ascii=False, indent=2)
print(json.dumps(report, ensure_ascii=True, indent=2))
