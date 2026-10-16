"""Read-only intersection, reference and source-integrity checks for the R37 review."""
import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path

S=Path('E:/Code/Report_INT3508/ridebound-scratchpad')
O=Path(__file__).parent
D=S/'rewrite-2026-10/drafts'
files=[D/'09-chuong4-phanB-v10.tex',D/'08-chuong4-phanA-v4.tex',
       S/'optimize/codex-debate/codex-work/r33-ch3v4/07-chuong3-v4-v3.tex',D/'06-chuong2-v4.tex']
report={'inputs':{},'references':[],'duplicates':{},'forbidden':[]}
labels=defaultdict(list)
texts={}
for p in files:
    raw=p.read_bytes()
    text=raw.decode('utf-8-sig')
    texts[p]=text
    report['inputs'][str(p)]={'sha256':hashlib.sha256(raw).hexdigest(),'physical_lines':len(text.splitlines())}
    for n,line in enumerate(text.splitlines(),1):
        visible=re.split(r'(?<!\\)%',line,1)[0]
        for match in re.finditer(r'\\label\{([^}]+)\}',visible):
            labels[match[1]].append(f'{p}:{n}')
for label, places in labels.items():
    if len(places)>1:
        report['duplicates'][label]=places
for n,line in enumerate(texts[files[0]].splitlines(),1):
    visible=re.split(r'(?<!\\)%',line,1)[0]
    for match in re.finditer(r'\\(?:eqref|ref|pageref|autoref|cref)\{([^}]+)\}',visible):
        report['references'].append({'line':n,'target':match[1],'definitions':labels.get(match[1],[])})
    for word in ['niêm phong','dự đoán trước','kết quả mong đợi','duy nhất','đầu tiên','vượt trội','đột phá','tối ưu']:
        if word in visible.lower():
            report['forbidden'].append({'line':n,'word':word})
report['undefined']=[x for x in report['references'] if not x['definitions']]
report['removed_label_inbound']=[str(p) for p,t in texts.items() if p!=files[0] and 'bang:c4-haiphia' in t]
assert len(report['references'])==24 and report['undefined']==[{'line':382,'target':'phuluc:C','definitions':[]}]
assert not report['duplicates'] and not report['forbidden'] and not report['removed_label_inbound']

cx=json.loads((S/'optimize/codex-debate/codex-work/R19-stage1a-analysis.json').read_text(encoding='utf-8'))
runs={(r['arm'],r['cell']):r for r in cx['runs']}
count={'common':0,'U_forecast_pad30':{'late60':0,'late120':0,'early60':0},
       'C30_forecast':{'late60':0,'late120':0,'early60':0}}
for cell in sorted(c for a,c in runs if a=='U'):
    u={x['request']:x for x in runs[('U',cell)]['riders']}
    c={x['request']:x for x in runs[('C-30',cell)]['riders']}
    common=set(u)&set(c)
    count['common']+=len(common)
    for name,table,pad in [('U_forecast_pad30',u,30000),('C30_forecast',c,0)]:
        for request in common:
            rider=table[request]
            delay=rider['arrival']-rider['forecast_quote']-pad
            count[name]['late60']+=delay>60000
            count[name]['late120']+=delay>120000
            count[name]['early60']+=delay<-60000
for name in ['U_forecast_pad30','C30_forecast']:
    count[name]['timely60']=count['common']-count[name]['late60']
    count[name]['timely120']=count['common']-count[name]['late120']
assert count['common']==2207
report['common_served_cohort']=count

report['ch5_rewrite_candidates']=[str(p) for p in D.glob('*chuong5*')]
report['page_ruler']={'prose_tokens_from_notes':3483,'table_figure_pages_from_notes':2.55,
                     'pages':3483/330+2.55,'cut_tokens_needed_for_11':3483+(2.55-11)*330,
                     'all_notes_section4_cut_tokens':45+25+15+30+170+80+25+45+35+30+40,
                     'pages_after_all_nominal_cuts':(3483-540)/330+2.55}
for p in [S/'rewrite-2026-10/reviews/CH4B-REVISION-LOG.md',S/'rewrite-2026-10/evidence/EVIDENCE-REGISTER-ADDENDUM-6-CH4B-v8.md',
          S/'rewrite-2026-10/evidence/checks-ch4b-v8/ADDENDUM-6-ERRATA-2026-10-12.md']:
    raw=p.read_bytes()
    report['inputs'][str(p)]={'sha256':hashlib.sha256(raw).hexdigest(),'physical_lines':len(raw.decode('utf-8-sig').splitlines())}

with (O/'verify-supplement.json').open('x',encoding='utf-8') as f:
    json.dump(report,f,ensure_ascii=False,indent=2)
summary={'references':len(report['references']),'undefined':report['undefined'],'common_cohort':count,
         'ch5':report['ch5_rewrite_candidates'],'page_ruler':report['page_ruler']}
with (O/'verify-supplement.txt').open('x',encoding='utf-8') as f:
    f.write(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(summary,ensure_ascii=True,indent=2))
