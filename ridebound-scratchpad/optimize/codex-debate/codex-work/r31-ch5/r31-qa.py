"""R31 read-only text QA. Writes only a new JSON report next to this script."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parent
S = ROOT.parents[3]
DRAFTS = S / 'rewrite-2026-10' / 'drafts'
NAMES = ['10-chuong5.tex', '11-phuluc.tex']

def comments_off(s):
    return re.sub(r'(?<!\\)%[^\n]*', '', s)

def words(s):
    s = comments_off(s)
    s = re.sub(r'\$[^$]*\$', '', s)
    s = re.sub(r'\\(?:chapter\*?|section|label|cite|ref|addcontentsline|renewcommand|setcounter)\{[^}]*\}(?:\{[^}]*\})*', '', s)
    s = re.sub(r'\\(?:nolinkurl|texttt|textbf|textit|emph)\{([^}]*)\}', r'\1', s)
    s = re.sub(r'\\(?:begin|end)\{[^}]*\}(?:\[[^\]]*\])?', '', s)
    s = re.sub(r'\\(?:appendix|item|centering|toprule|midrule|bottomrule)\b', '', s)
    s = re.sub(r'\\caption\{([^}]*)\}', r'\1', s)
    s = s.replace('~', ' ').replace('&', ' ').replace('\\\\', ' ')
    return len(s.split())

texts = {n: (ROOT / n).read_text(encoding='utf-8') for n in NAMES}
source_names = ['07-chuong3-v3.tex', '08-chuong4-phanA-v4.tex', '09-chuong4-phanB-v7.tex']
source_texts = [(DRAFTS / n).read_text(encoding='utf-8') for n in source_names]
labels = []
for s in texts.values():
    labels += re.findall(r'\\label\{([^}]+)\}', s)
known_labels = set(labels)
for s in source_texts:
    known_labels.update(re.findall(r'\\label\{([^}]+)\}', s))
report = {'files': {}, 'unresolved_references': [], 'duplicate_labels': sorted({x for x in labels if labels.count(x)>1})}
for name, text in texts.items():
    clean = comments_off(text)
    stack = []
    env_errors = []
    for m in re.finditer(r'\\(begin|end)\{([^}]+)\}', clean):
        action, env = m.groups()
        if action == 'begin': stack.append(env)
        elif not stack or stack.pop() != env: env_errors.append(m.group(0))
    env_errors += stack
    depth = 0
    brace_errors = []
    for m in re.finditer(r'(?<!\\)[{}]', clean):
        depth += 1 if m.group(0) == '{' else -1
        if depth < 0: brace_errors.append(m.start())
    if depth: brace_errors.append(depth)
    sections = re.split(r'\\section\{([^}]+)\}', text)
    section_info = []
    for index in range(1, len(sections), 2):
        title, body = sections[index:index+2]
        tables = re.findall(r'\\begin\{table\}.*?\\end\{table\}', body, re.S)
        prose = re.sub(r'\\begin\{table\}.*?\\end\{table\}', '', body, flags=re.S)
        section_info.append({'title': title, 'prose_words': words(prose), 'table_text_words': sum(words(x) for x in tables), 'tables':len(tables)})
    refs = re.findall(r'\\(?:ref|eqref)\{([^}]+)\}', clean)
    missing = sorted(set(refs) - known_labels)
    forbidden = ['niêm phong','tiền đăng ký','dự đoán trước','kết quả mong đợi','duy nhất','vượt trội','đột phá','tối ưu','chúng tôi','quy trách']
    forbidden_hits = [x for x in forbidden if x in clean.lower()]
    blocks = re.split(r'\n\s*\n', text.strip())
    no_ev = []
    for b in blocks:
        plain = comments_off(b).strip()
        if not plain or plain.startswith('\\'): continue
        if '% EV:' not in b: no_ev.append(plain[:100])
    report['files'][name] = {'opening_words': words(sections[0]), 'sections':section_info,
        'prose_total':words(re.sub(r'\\begin\{table\}.*?\\end\{table\}', '', text, flags=re.S)),
        'brace_errors':brace_errors,'environment_errors':env_errors,'math_delimiters_even':clean.count('$')%2==0,
        'forbidden_hits':forbidden_hits,'paragraphs_without_ev':no_ev,'ev_comments':text.count('% EV:')}
    report['unresolved_references'] += missing

split_path = S / 'tang3' / 't38' / 'split-t38-v1.json'
split = json.loads(split_path.read_text(encoding='utf-8'))
grouped = {
 'test': [(14,[3,4],[7,8,17]),(15,[1,2,4],[7,8]),(16,[1,2,4],[7,8,17]),(17,[1,2],[8,17]),(17,[3],[7,8,17]),(18,[2,3,4],[8,17])],
 'calibration': [(14,[1,2],[7,8,17]),(15,[3],[7,8]),(16,[3],[7,8,17]),(17,[4],[8,17]),(18,[1],[8,17])]
}
report['scenario_list_checks'] = {}
for part, groups in grouped.items():
    expanded = [f'd201811{d:02d}-s10-r{r}-w{w:02d}' for d,rs,ws in groups for r in rs for w in ws]
    report['scenario_list_checks'][part] = {'count':len(expanded),'exact_set_match':set(expanded)==set(split[part]),'no_duplicates':len(expanded)==len(set(expanded))}
report['illustrative_arithmetic'] = {'ce1':{'x':600-600,'c':660-600,'z':660-600},'ce4':{'endpoint':600-600,'variation':abs(660-600)+abs(600-660)},'ce5':{'endpoint':720-600,'variation':abs(660-600)+abs(720-660)}}
chapter_sections = re.split(r'\\section\{[^}]+\}', texts[NAMES[0]])
report['summary_paragraph_count'] = len(re.findall(r'^Với phần', chapter_sections[1], re.M))
report['future_direction_count'] = len(re.findall(r'^Thứ (?:nhất|hai|ba|tư|năm),', chapter_sections[3], re.M))
assert not report['duplicate_labels']
assert not report['unresolved_references'], report['unresolved_references']
for r in report['files'].values():
    assert not r['brace_errors'] and not r['environment_errors'] and r['math_delimiters_even']
    assert not r['forbidden_hits'] and not r['paragraphs_without_ev']
assert report['summary_paragraph_count'] == 3
assert report['future_direction_count'] == 5
assert all(x['exact_set_match'] and x['no_duplicates'] for x in report['scenario_list_checks'].values())
report['status'] = 'PASS (static checks only; no build or simulation)'
with (ROOT / 'r31-qa.json').open('x', encoding='utf-8') as f:
    json.dump(report, f, ensure_ascii=False, indent=2)
print(json.dumps(report, ensure_ascii=False, indent=2))
