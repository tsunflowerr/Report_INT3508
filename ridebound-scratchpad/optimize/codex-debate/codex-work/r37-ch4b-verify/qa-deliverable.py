"""Read-only final deliverable coverage and artifact checks; no rendering/build."""
import json
import re
from pathlib import Path

O=Path(__file__).parent
P=O/'R37-CH4B-V10-VERIFY-CODEX.md'
text=P.read_text(encoding='utf-8')
numeric=json.loads((O/'verify-numbers-v2.json').read_text(encoding='utf-8'))
supplement=json.loads((O/'verify-supplement.json').read_text(encoding='utf-8'))
cx=[f'CX-{n:02}' for n in range(1,25)]
rejects=['CX-10','B47','L-02','L-04','L-15','L-23','L-26','L-27','L-31','L-33/L-52','L-34','L-40','L-50','L-60']
assert all(re.search(r'\| '+re.escape(row)+r'\b',text) for row in cx)
assert all(row in text for row in rejects)
assert '**Verdict: ACCEPT WITH CORRECTIONS.**' in text
assert numeric['dispatcher']['paired']['Mplus-30F']['forced']==3849
assert numeric['dispatcher']['paired']['Mplus-30F']['ack']==8496
assert numeric['dispatcher']['paired']['Mplus-30']['forced']==5121
assert numeric['dispatcher']['paired']['Mplus-30']['ack']==8468
assert numeric['snow']['dispatch_s']==8.566
assert supplement['common_served_cohort']['common']==2207
assert supplement['undefined']==[{'line':382,'target':'phuluc:C','definitions':[]}]
assert 'All numeric assertions passed' in (O/'verify-numbers-v2.txt').read_text(encoding='utf-8')
A=Path('E:/Code/Report_INT3508/ridebound-scratchpad/rewrite-2026-10/drafts/08-chuong4-phanA-v4.tex')
assert r'\label{muc:c4-thamdo}' in A.read_text(encoding='utf-8')
report={'deliverable':P.name,'bytes':P.stat().st_size,'r29_rows':len(cx),'rejected_comments_checked':len(rejects),
        'numeric_probe_finished':True,'common_cohort_verified':True,'suggested_new_reference_defined':True,
        'status':'PASS; source-level review only, no layout build'}
with (O/'qa-deliverable.json').open('x',encoding='utf-8') as f:
    json.dump(report,f,indent=2)
print(json.dumps(report,indent=2))
