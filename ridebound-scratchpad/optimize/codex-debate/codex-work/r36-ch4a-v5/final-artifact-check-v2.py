"""Read-only check of final artifacts; only a new small QA result is written."""
from pathlib import Path
import hashlib
import json
import re
D=Path(__file__).resolve().parent
tex=(D/'08-chuong4-phanA-v5-v3.tex').read_text(encoding='utf-8')
notes=(D/'08-chuong4-phanA-v5-CHANGES-v3.md').read_text(encoding='utf-8')
qa=json.loads((D/'root-qa-v3.json').read_text(encoding='utf-8'))
checks={
    '25_change_rows':len(re.findall(r'^\| \d+ \|',notes,re.M))==qa['change_count']==25,
    'correct_attempt4_anchor': 'TESTRUN-45f8026-2026-10-12.md:18' in notes and 'TESTRUN-45f8026-2026-10-12.md:21' not in notes,
    'correct_calibration_anchor':'RUN38:5–6,42–44' in notes and 'RUN38:9–10' not in notes,
    'correct_runner_anchor':'Ch3 v4-v3:733–735' in notes and '496–498' not in notes,
    'separate_B_cohorts':'trên cùng 15 kịch bản' in notes and 'trên tám kịch bản khung 7 giờ' in notes,
    'part_B_120s_handoff':'B421–423' in notes and 'kể cả các phép tính thử ở 120 giây' in notes,
    'word_growth_lt_3':qa['prose_growth_percent']<3 and qa['visible_growth_percent']<3,
    '40_resolved_refs':len(qa['reference_owners'])==40 and all(qa['reference_owners'].values()),
    'source_preserved':qa['source_unchanged'],
    'body_tables_retained':tex.count('\\begin{table}')==12 and tex.count('\\begin{figure}')==1,
    'prior_v2_retained':all((D/f).exists() for f in ('08-chuong4-phanA-v5-v2.tex','08-chuong4-phanA-v5-CHANGES-v2.md','root-qa-v2.json')),
    'tex_hash_matches':hashlib.sha256(tex.encode('utf-8')).hexdigest()==qa['output_sha256'],
    'no_build_or_simulation':qa['builds_run'] is False and qa['simulations_run'] is False,
}
assert all(checks.values()),checks
with (D/'final-artifact-qa-v2.json').open('x',encoding='utf-8',newline='\n') as f:
    json.dump(dict(checks=checks,tex_sha256=qa['output_sha256'],
                   notes_sha256=hashlib.sha256(notes.encode('utf-8')).hexdigest(),
                   change_count=25,new_counts=qa['new_counts']),f,ensure_ascii=False,indent=2)
    f.write('\n')
print('Final artifact checks PASS: 25 changes, 40 references, growth below 3%, prior files preserved.')
