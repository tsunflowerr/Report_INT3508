"""R42 read-only evidence, number, syntax, label and citation checks; no builds."""
from pathlib import Path
from collections import Counter
import json
import re

ROOT = Path(__file__).resolve().parent
CW = ROOT.parent
S = ROOT.parents[3]
KIT = S / 'rewrite-2026-10'
inputs = {
 'Ch1':CW/'r40-ch1-v4/05-chuong1-v4-v4.tex',
 'Ch2':KIT/'drafts/06-chuong2-v6.tex',
 'Ch3':CW/'r33-ch3v4/07-chuong3-v4-v3.tex',
 'Ch4A':CW/'r36-ch4a-v5/08-chuong4-phanA-v5-v3.tex',
 'Ch4B':CW/'r39-ch4b-v11/09-chuong4-phanB-v11-v2.tex',
 'Ch5':ROOT/'10-chuong5-v3.tex',
 'PL':ROOT/'11-phuluc-v3.tex',
 'BIB':CW/'r32-bib/10-tai-lieu-draft-v2.tex'
}
texts = {k:p.read_text(encoding='utf-8') for k,p in inputs.items()}

def no_comments(s):
    return re.sub(r'(?<!\\)%[^\n]*', '', s)

def word_count(s):
    s = no_comments(s)
    s = re.sub(r'\$[^$]*\$', '', s)
    s = re.sub(r'\\(?:chapter\*?|section|label|cite|ref|eqref|addcontentsline|renewcommand|setcounter)\{[^}]*\}(?:\{[^}]*\})*', '', s)
    s = re.sub(r'\\(?:nolinkurl|texttt|textbf|textit|emph)\{([^}]*)\}',r'\1',s)
    s = re.sub(r'\\(?:begin|end)\{[^}]*\}(?:\[[^\]]*\])?', '', s)
    s = re.sub(r'\\(?:appendix|item|centering|toprule|midrule|bottomrule)\b', '', s)
    s = re.sub(r'\\caption\{([^}]*)\}',r'\1',s)
    s = s.replace('~',' ').replace('&',' ').replace('\\\\',' ')
    return len(s.split())

report = {'input_files':{k:str(p) for k,p in inputs.items()},'word_counts':{},'syntax':{},'labels':{},'numbers':{},'integration_notes':[]}
all_labels = []
for k,t in texts.items():
    all_labels += [(m,k) for m in re.findall(r'\\label\{([^}]+)\}',no_comments(t))]
label_counts = Counter(x[0] for x in all_labels)
known_labels = set(label_counts)
report['labels']['duplicates'] = sorted(x for x,n in label_counts.items() if n>1)
report['labels']['missing_by_file'] = {}
for k,t in texts.items():
    refs = re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',no_comments(t))
    report['labels']['missing_by_file'][k] = sorted(set(refs)-known_labels)
bibkeys = set(re.findall(r'\\bibitem(?:\[[^]]*\])?\{([^}]+)\}',no_comments(texts['BIB'])))
report['labels']['missing_citations'] = {}
for k,t in texts.items():
    keys = [x.strip() for g in re.findall(r'\\cite(?:\[[^]]*\])?\{([^}]+)\}',no_comments(t)) for x in g.split(',')]
    report['labels']['missing_citations'][k] = sorted(set(keys)-bibkeys)
report['labels']['new_references_to_B'] = {k:len(re.findall(r'\\ref\{phuluc:B\}',no_comments(t))) for k,t in texts.items()}

for k in ['Ch5','PL']:
    t = texts[k]
    clean = no_comments(t)
    stack = []
    env_errors = []
    for action,env in re.findall(r'\\(begin|end)\{([^}]+)\}',clean):
        if action=='begin': stack.append(env)
        elif not stack or stack.pop()!=env: env_errors.append(env)
    env_errors += stack
    depth = 0
    braces = []
    for m in re.finditer(r'(?<!\\)[{}]',clean):
        depth += 1 if m.group(0)=='{' else -1
        if depth<0: braces.append(m.start())
    if depth: braces.append(depth)
    prohibited = ['niêm phong','tiền đăng ký','dự đoán trước','kết quả mong đợi','duy nhất','vượt trội','đột phá','tối ưu','chúng tôi','quy trách']
    missing_ev = []
    for block in re.split(r'\n\s*\n',t.strip()):
        p = no_comments(block).strip()
        if p and not p.startswith('\\') and '% EV:' not in block: missing_ev.append(p[:80])
    report['syntax'][k] = {'environment_errors':env_errors,'brace_errors':braces,'math_even':clean.count('$')%2==0,'prohibited_hits':[w for w in prohibited if w in clean.lower()],'missing_ev':missing_ev}
    sections = re.split(r'\\section\{([^}]+)\}',t)
    rows = []
    for i in range(1,len(sections),2):
        title,body = sections[i:i+2]
        tables = re.findall(r'\\begin\{table\}.*?\\end\{table\}',body,re.S)
        prose = re.sub(r'\\begin\{table\}.*?\\end\{table\}','',body,flags=re.S)
        rows.append({'title':title,'prose_words':word_count(prose),'table_words':sum(word_count(x) for x in tables),'table_count':len(tables)})
    report['word_counts'][k] = {'opening_words':word_count(sections[0]) if k=='Ch5' else 0,'sections':rows,'prose_total':sum(x['prose_words'] for x in rows)+(word_count(sections[0]) if k=='Ch5' else 0)}
report['structure'] = {'three_summary_paragraphs':texts['Ch5'].count('\\textbf{Phần ')==3,'five_future_directions':len(re.findall(r'^Thứ (?:nhất|hai|ba|tư|năm),',texts['Ch5'],re.M))==5,'selector_first':bool(re.search(r'Thứ nhất,[\s\S]*?ưu tiên ổn định[\s\S]*?ưu tiên chi phí',texts['Ch5']))}

raw = (KIT/'evidence/checks-addendum-1/recompute-addendum-1-2026-10-11.txt').read_text(encoding='utf-8')
armrows = {}
for line in raw.splitlines():
    match = re.match(r'^(U|C-30|C-120|Mplus-30)\s+(naive|fc|fc\+30)\s*\|',line)
    if not match: continue
    p = line.split('|')
    late = [int(x) for x in p[2].split()]
    served = int(p[1])
    armrows[tuple(match.groups())] = {'served':served,'late30':late[0],'late60':late[1],'late120':late[2],'early60':int(p[3]),'timely60':served-late[1],'timely120':served-late[2],'extension_s':float(p[-1].strip())}
U,C,M,C120 = [armrows[(x,'naive')] for x in ['U','C-30','Mplus-30','C-120']]
FCP = armrows[('U','fc+30')]
FCC = armrows[('C-30','fc')]
assert [U['served'],C['served'],M['served'],C120['served']]==[2434,2338,2338,2387]
assert [C['late30'],M['late30']]==[292,289]
assert [C['timely60'],U['timely60'],C['timely120'],U['timely120']]==[2262,2231,2327,2332]
assert [C120['timely60'],C120['timely120']]==[2255,2366]
assert [FCP['timely60'],FCC['timely60'],FCP['timely120'],FCC['timely120']]==[2328,2328,2366,2338]
assert [FCP['early60'],FCC['early60']]==[44,4]
assert round(FCP['extension_s'],1)==37.2 and round(FCC['extension_s'],1)==7.4
report['numbers']['main_raw_rows'] = {'U':U,'C30':C,'Mplus30':M,'C120':C120,'U_forecast_pad30':FCP,'C30_forecast':FCC}
report['numbers']['differences'] = {'served':C['served']-U['served'],'timely60':C['timely60']-U['timely60'],'timely120':C['timely120']-U['timely120'],'shared':313-555,'padding_timely120':FCP['timely120']-FCC['timely120']}
assert report['numbers']['differences']=={'served':-96,'timely60':31,'timely120':-5,'shared':-242,'padding_timely120':28}
assert '292' in texts['Ch4A'] and '289' in texts['Ch4A'] and '28 trong 34' in texts['Ch4A']
assert '66 xuống 2' in texts['Ch4B'] and '1.471' in texts['Ch4B']
assert '590,1' in texts['Ch4A'] and '29,2' in texts['Ch4A']
assert '845' in texts['Ch4A'] and '524' in texts['Ch4A']
report['numbers']['current_source_checks'] = {'fairness_28_of34':True,'deadline_forecast66_to2_on1471':True,'dispatch_max29_2_vs590_1':True,'prune_records845_524':True}
report['numbers']['rounding'] = {'weekday_raw_parts_s':[81.742,5352.646,783.018],'raw_sum_s':81.742+5352.646+783.018,'rounded_parts_sum_s':82+5353+783,'rounded_total_s':6217,'independent_rounding_stated':'Các thành phần và tổng được làm tròn riêng.' in texts['Ch5'],'snow_raw_residual_s':3445.933-8.566-251.496}
for token in ['81,742','5.352,646','783,018','6.217,406']:
    assert token in texts['Ch4B']
assert report['numbers']['rounding']['independent_rounding_stated']
report['numbers']['illustrations'] = {'ce1':[600-600,660-600,660-600],'ce4':[600-600,abs(660-600)+abs(600-660)],'ce5':[720-600,abs(660-600)+abs(720-660)],'ce6_witness':[abs(-30+60),abs(60)]}

split = json.loads((S/'tang3/t38/split-t38-v1.json').read_text(encoding='utf-8'))
groups = {'test':[(14,[3,4],[7,8,17]),(15,[1,2,4],[7,8]),(16,[1,2,4],[7,8,17]),(17,[1,2],[8,17]),(17,[3],[7,8,17]),(18,[2,3,4],[8,17])], 'calibration':[(14,[1,2],[7,8,17]),(15,[3],[7,8]),(16,[3],[7,8,17]),(17,[4],[8,17]),(18,[1],[8,17])]}
report['numbers']['scenario_lists'] = {}
for part,g in groups.items():
    expanded = [f'd201811{d:02d}-s10-r{r}-w{w:02d}' for d,rs,ws in g for r in rs for w in ws]
    assert set(expanded)==set(split[part]) and len(expanded)==len(set(expanded))
    report['numbers']['scenario_lists'][part] = {'count':len(expanded),'exact_match':True}
report['numbers']['snow_selection'] = [f'C-30-d20181115-s10-r{r}-w{w}' for r in range(1,5) for w in [14,15]]
for name in report['numbers']['snow_selection']:
    assert (Path('C:/RideBoundData/research/tier3-forecast-v1')/name).is_dir()
report['numbers']['run_counts'] = {'main_original':34*5,'main_C120':34,'morning_used':8*(1+8*2),'morning_stored':88+104,'fixed_per_configuration':16,'snow':8,'riders_compared':2434+2338+2387}
assert report['numbers']['run_counts']['riders_compared']==7159

logs = {'1':'testrun-45f8026-2026-10-12.log','2':'testrun-45f8026-lf-2026-10-12.log','3':'testrun-45f8026-eollf-2026-10-12.log','3b':'testrun-45f8026-eollf-dirtycheck-2026-10-12.log','4':'testrun-45f8026-eollf-dirty-fullrun-2026-10-13.log'}
report['numbers']['test_attempts'] = {}
for key,name in logs.items():
    t = (Path('C:/RideBoundData/research')/name).read_text(encoding='utf-8')
    totals = re.findall(r'(?:Passed!|Failed!)\s*-\s*Failed:\s*(\d+),\s*Passed:\s*(\d+),\s*Skipped:\s*(\d+),\s*Total:\s*(\d+)',t)
    assert totals, key
    vals = [sum(int(row[i]) for row in totals) for i in range(4)]
    report['numbers']['test_attempts'][key] = {'failed':vals[0],'passed':vals[1],'skipped':vals[2],'total':vals[3],'projects':len(totals),'log':name}
    if key=='4':
        assert '2026-10-13T13:39' in t and 'autocrlf=false eol=lf' in t and '?? DIRTY-MARKER-' in t and 'exit=0' in t
for key,expected in [('1',(1020,1025,5)),('2',(1020,1025,5)),('3',(1024,1025,1)),('3b',(1,1,0)),('4',(1025,1025,0))]:
    r=report['numbers']['test_attempts'][key]
    assert (r['passed'],r['total'],r['failed'])==expected
if re.search(r'ngày 12/10/2026,[\s\S]{0,150}LF',texts['Ch3']):
    report['integration_notes'].append('Ch3 current file still dates the full 1025 result 12/10; assembly must use 13/10 as TESTRUN attempt4 and Ch4B already do.')

assert not report['labels']['duplicates']
assert not any(report['labels']['missing_by_file'].values())
assert not any(report['labels']['missing_citations'].values())
for r in report['syntax'].values():
    assert not r['environment_errors'] and not r['brace_errors'] and r['math_even']
    assert not r['prohibited_hits'] and not r['missing_ev']
assert all(report['structure'].values())
report['status'] = 'PASS; read-only checks, no build or simulation'
with (ROOT/'r42-check.json').open('x',encoding='utf-8') as f:
    json.dump(report,f,ensure_ascii=False,indent=2)
print(json.dumps({'status':report['status'],'words':report['word_counts'],'labels':report['labels'],'test_attempts':report['numbers']['test_attempts'],'integration_notes':report['integration_notes']},ensure_ascii=False,indent=2))
