from pathlib import Path
import json
outdir=Path('E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/r34-ch4a-verify')
codepath=Path('C:/Code/RideBound-noworse/src/RideBound.Benchmarking/Normalization/FleetPyManhattanNormalizer.cs')
lines=codepath.read_text(encoding='utf-8-sig').splitlines()
report=[str(codepath)]
for a,b in [(111,134),(581,604),(618,626),(659,684),(735,757)]:
    for n in range(a,b+1): report.append(f'NORM:{n} {lines[n-1]}')
fixture=Path('C:/RideBoundData/research/fixtures-panelA-v1/d20181114-s10-r3-w08/normalizer-configuration.json')
data=json.loads(fixture.read_text(encoding='utf-8-sig'))
report.append(str(fixture))
report.append(json.dumps({key: data[key] for key in ['sourceWindowStartSeconds','sourceWindowEndSeconds','requestTarget','maximumNodeCount','demandMemberPath'] if key in data},ensure_ascii=False,sort_keys=True))
report.append('Scope: one fixture plus current source; not a cross-fixture regeneration or version-equivalence check.')
with (outdir/'consistency-normalizer-probe-output-v3.txt').open('x',encoding='utf-8') as f: f.write('\n'.join(report)+'\n')
print('Saved read-only normalizer source probe.')