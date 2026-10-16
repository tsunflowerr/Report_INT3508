"""Create the resumed v2 script exclusively; preserve the interrupted v1 script."""
from pathlib import Path
import ast

out = Path(__file__).resolve().parent
source = (out/'apply-and-check-v1.py').read_text(encoding='utf-8')
replacements = {
    '09-chuong4-phanB-v11.tex': '09-chuong4-phanB-v11-v2.tex',
    '09-chuong4-phanB-v11-CHANGES.md': '09-chuong4-phanB-v11-CHANGES-v2.md',
    'agent-numbers-supplement-v1.json:weekday_ledger': 'agent-numbers-summary-v1.json:forecast_ledger',
    'candidate-v1.tex': 'candidate-v2.tex',
    'candidate-CHANGES-v1.md': 'candidate-CHANGES-v2.md',
    'root-changes-data-v1.json': 'root-changes-data-v2.json',
    'root-qa-v1.json': 'root-qa-v2.json',
}
for old,new in replacements.items():
    assert old in source, old
    source = source.replace(old,new)
start = source.index("notes = f'''# Round 39")
end = source.index("\noutputs = ",start)
source = source[:start] + '''notes = (OUT/'CHANGES-template-v2.md').read_text(encoding='utf-8')
for marker,value in {
    '@@CHANGE_COUNT@@':str(len(ordered)),
    '@@COUNT_TABLE@@':'\\n'.join(count_table),
    '@@CHANGE_ROWS@@':'\\n'.join(rows),
    '@@TABLE_SCALE@@':f"{qa['widths']['table_scale_from_old_overflow']:.6f}",
    '@@FIGURE_SCALE@@':f"{qa['widths']['figure_scale_from_old_overflow']:.6f}",
    '@@REF_COUNT@@':str(len(refs)),
    '@@REF_TARGETS@@':str(qa['distinct_ref_targets']),
}.items():
    assert marker in notes, marker
    notes = notes.replace(marker,value)
assert '@@' not in notes
''' + source[end:]
anchor = 'linewidth_pt = 16/2.54*72.27'
assert anchor in source
source = source.replace(anchor, '''# Root rechecks the weekday historical share on independently extracted riders.
cx_path = WORK/'R19-stage1a-analysis.json'
cx = json.loads(cx_path.read_text(encoding='utf-8'))
active = [r for r in cx['runs'] if r['arm']=='C-30' and r['cell'][7:9] in ['14','15','16']]
late = [x for r in active for x in r['riders'] if x['arrival']-x['P0']>60000]
total_s = sum(x['arrival']-x['P0'] for x in late)/1000
history_s = sum(x['forecast_quote']-x['P0'] for x in late)/1000
weekday_ledger = {'scenarios':len(active),'late_naive_count':len(late),
                  'total_s':total_s,'historical_s':history_s,'historical_pct':100*history_s/total_s}
assert len(active)==21 and len(late)==68
assert abs(total_s-6217.406)<1e-6 and round(weekday_ledger['historical_pct'],1)==86.1
assert abs(history_s-float(json.loads((OUT/'agent-numbers-summary-v1.json').read_text(encoding='utf-8'))['forecast_ledger']['components_s']['anticipated']))<1e-6
raw = cx_path.read_bytes()
inputs[str(cx_path)] = {'sha256':hashlib.sha256(raw).hexdigest()}
linewidth_pt = 16/2.54*72.27''')
source = source.replace("'no_build':True}","'no_build':True,'weekday_ledger':weekday_ledger}")
ast.parse(source)
with (out/'apply-and-check-v2.py').open('x',encoding='utf-8',newline='\n') as f:
    f.write(source)
print('Created apply-and-check-v2.py; v1 and prior numeric outputs preserved.')
