from pathlib import Path
import re
from collections import defaultdict
root = Path('E:/Code/Report_INT3508/ridebound-scratchpad/rewrite-2026-10')
outdir = Path('E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/r34-ch4a-verify')
pinned = {'A': root/'drafts/08-chuong4-phanA-v4.tex', 'B': root/'drafts/09-chuong4-phanB-v7.tex', 'Ch3': root/'drafts/07-chuong3-v3.tex'}
texts = {key: path.read_text(encoding='utf-8-sig') for key,path in pinned.items()}
lines = {key: val.splitlines() for key,val in texts.items()}
report=[]
def emit(s=''):
    report.append(str(s))
def body(line):
    return re.split(r'(?<!\\)%',line,maxsplit=1)[0]
labels=defaultdict(list)
for key,src in lines.items():
    for n,line in enumerate(src,1):
        for label in re.findall(r'\\label\{([^}]+)\}',body(line)):
            labels[label].append(f'{key}:{n}')
emit('PINNED LABELS AND REFS')
for key in ['A','B']:
    for n,line in enumerate(lines[key],1):
        for kind,target in re.findall(r'\\(eqref|ref)\{([^}]+)\}',body(line)):
            if target not in labels: emit(f'{key}:{n} unresolved in pinned A+B+Ch3: {target}')
for label, locs in labels.items():
    if len(locs)>1: emit(f'duplicate {label}: {locs}')
alltex = list((root/'drafts').glob('*.tex')) + list(Path('E:/Code/Report_INT3508/ridebound/noi-dung').glob('*.tex'))
projectlabels=defaultdict(list)
for path in alltex:
    for n,line in enumerate(path.read_text(encoding='utf-8-sig').splitlines(),1):
        for label in re.findall(r'\\label\{([^}]+)\}',body(line)):
            projectlabels[label].append(f'{path.name}:{n}')
for target in ['muc:c1-cauhoi','phuluc:A','phuluc:C']:
    emit(f'project definition {target}: {projectlabels.get(target,[])}')
emit('\nFORBIDDEN PHRASE SCAN')
for key in ['A','B']:
    for n,line in enumerate(lines[key],1):
        for phrase in ['niêm phong','preregistration','tiền đăng ký','dự đoán trước','kết quả mong đợi','duy nhất','đầu tiên','vượt trội','đột phá','tối ưu','byte','phải phục hồi','dữ liệu phát triển']:
            if phrase.casefold() in line.casefold(): emit(f'{key}:{n} [{phrase}] {line}')
emit('\nA/B SCOPE AND SHARED NUMERICAL CLUSTERS')
patterns=[r'hiệu chỉnh',r'382\.006',r'7\.159',r'68 khách',r'41 khách',r'76',r'14,15',r'7,37',r'13,7',r'6\.217',r'6\.892',r'6\.891',r'82 s',r'20\.101',r'20\.435',r'20\.760',r'192',r'136',r'1\.991',r'21 kịch bản',r'601',r'41,3',r'47,6',r'62,8',r'100\\%',r'0,17',r'LF']
for key in ['A','B','Ch3']:
    for n,line in enumerate(lines[key],1):
        if any(re.search(pattern,line) for pattern in patterns): emit(f'{key}:{n} {line}')
emit('\nA PERCENT LINES (manual denominator review)')
for n,line in enumerate(lines['A'],1):
    if '\\%' in body(line): emit(f'A:{n} {line}')
emit('\nCH4A LOG PARTIALS AND REJECTIONS')
log=(root/'reviews/CH4A-REVISION-LOG-v2.md').read_text(encoding='utf-8-sig').splitlines()
for n,line in enumerate(log,1):
    if '| M |' in line or '| R |' in line or n >= 221: emit(f'Log:{n} {line}')
emit('\nDIRECT STYLE/OUTLINE ANCHORS')
for filename in ['style/STYLE-GUIDE-VI.md','OUTLINE-V2.md','style/GLOSSARY-VI-v2.md']:
    for n,line in enumerate((root/filename).read_text(encoding='utf-8-sig').splitlines(),1):
        if any(token in line for token in ['26. **','7. **','22. **','24. **','3 trang','3.0 trang','4.8','4.7','trung bình theo','bị ép','phục hồi']): emit(f'{filename}:{n} {line}')
output='\n'.join(report)+'\n'
with (outdir/'consistency-audit-output.txt').open('x',encoding='utf-8') as handle:
    handle.write(output)
print(output)