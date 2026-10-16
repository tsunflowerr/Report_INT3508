"""Exclusive-create the reviewed R39 final deliverables and a compact final QA."""
from pathlib import Path
import hashlib
import html
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
out = Path(__file__).resolve().parent
work = out.parent
qa = json.loads((out/'root-qa-v2.json').read_text(encoding='utf-8'))
edits = json.loads((out/'root-changes-data-v2.json').read_text(encoding='utf-8'))
tex = (out/'candidate-v2.tex').read_text(encoding='utf-8')
notes = (out/'candidate-CHANGES-v2.md').read_text(encoding='utf-8')
audit = (out/'agent-final-audit-v2.md').read_text(encoding='utf-8')
assert len(edits) == qa['changes'] == 33
assert len(qa['references']) == 25 and qa['distinct_ref_targets'] == 21
assert not qa['undefined'] and not qa['duplicate_labels']
assert len(re.findall(r'^\| \d+ \|',notes,re.M)) == 33
assert '09-chuong4-phanB-v11-CHANGES-v2.md' in tex
assert 'agent-numbers-supplement-v1' not in notes

# Preserve the TeX candidate exactly. Only localize two decimal numbers in notes.
note_edits = {'**0.939774**':'**0,939774**','**0.966457**':'**0,966457**'}
for old,new in note_edits.items():
    assert notes.count(old) == 1
    notes = notes.replace(old,new)

# No numerical or chapter input has changed since the successful root check.
for filename,metadata in qa['inputs'].items():
    assert hashlib.sha256(Path(filename).read_bytes()).hexdigest() == metadata['sha256'], filename

# Independently scan final source references and check captions/content of floats.
def visible(text):
    return re.sub(r'(?<!\\)%[^\n]*','',text)

labels = {}
prescribed = [work/'r36-ch4a-v5/08-chuong4-phanA-v5-v3.tex',
              work/'r33-ch3v4/07-chuong3-v4-v3.tex',work/'r31-ch5/11-phuluc-v2.tex']
for name,text in [('B-v11-v2',tex)] + [(str(p),p.read_text(encoding='utf-8')) for p in prescribed]:
    for key in re.findall(r'\\label\{([^}]+)\}',visible(text)):
        assert key not in labels, key
        labels[key] = name
refs = re.findall(r'\\(?:ref|eqref|pageref|autoref)\{([^}]+)\}',visible(tex))
assert len(refs)==25 and all(key in labels for key in refs)
base = Path(next(p for p in qa['inputs'] if p.endswith('09-chuong4-phanB-v10.tex'))).read_text(encoding='utf-8')
base_lines = base.splitlines(keepends=True)
assert ''.join(base_lines[38:58]) in tex and ''.join(base_lines[140:170]) in tex
assert tex.count('\\resizebox{\\linewidth}{!}{%') == 2
assert 'giới hạn phần dời này của từng khách ở nhiều nhất 29,2' not in tex
assert 'mức lớn nhất đo được là 29,2' in tex
assert 'Các số đếm sau được suy từ tỉ lệ gộp theo khách' in tex
assert '1.025 trong 1.025' in tex and '13/10/2026' in tex

outputs = {'09-chuong4-phanB-v11-v2.tex':tex,'09-chuong4-phanB-v11-CHANGES-v2.md':notes}
assert all(not (out/name).exists() for name in outputs)
assert not (out/'final-qa-v2.json').exists()
for name,text in outputs.items():
    with (out/name).open('x',encoding='utf-8',newline='\n') as f:
        f.write(text)
final = {'deliverables':{name:{'sha256':hashlib.sha256((out/name).read_bytes()).hexdigest(),
                             'bytes':(out/name).stat().st_size} for name in outputs},
         'changes':33,'word_counts':qa['new_counts'],'total_prose':sum(r['prose'] for r in qa['new_counts']),
         'tex_identical_to_reviewed_candidate':True,'notes_decimal_localization':note_edits,
         'input_hashes_unchanged':True,'references':len(refs),'distinct_ref_targets':len(set(refs)),
         'undefined':[],'two_float_contents_preserved':True,'no_build':True,
         'independent_audit':{'file':'agent-final-audit-v2.md','sha256':hashlib.sha256(audit.encode('utf-8')).hexdigest()},
         'handoff':['Ch3 counter scope, test date/evidence and cumulative terminology',
                    'Appendix C attempt-4 single-run results',
                    'Assembly notes, final input paths and build layout verification']}
with (out/'final-qa-v2.json').open('x',encoding='utf-8',newline='\n') as f:
    json.dump(final,f,ensure_ascii=False,indent=2)
print(json.dumps(final,ensure_ascii=False,indent=2))
