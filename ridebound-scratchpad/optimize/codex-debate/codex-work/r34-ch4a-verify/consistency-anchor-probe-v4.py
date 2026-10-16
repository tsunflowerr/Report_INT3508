from pathlib import Path
import re
outdir=Path('E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work/r34-ch4a-verify')
root=Path('E:/Code/Report_INT3508/ridebound-scratchpad/rewrite-2026-10/drafts')
paths={'A':root/'08-chuong4-phanA-v4.tex','B':root/'09-chuong4-phanB-v7.tex','Ch3':root/'07-chuong3-v3.tex'}
text=(outdir/'consistency-findings-v3.md').read_text(encoding='utf-8')
report=[]
for key,path in paths.items():
    wanted=set()
    for match in re.finditer(r'\b'+key+r':?(\d+)(?:[–-](\d+))?',text):
        start=int(match.group(1)); end=int(match.group(2) or match.group(1))
        if end-start<30:
            wanted.update(range(start,end+1))
    lines=path.read_text(encoding='utf-8-sig').splitlines()
    report.append(str(path))
    for n in sorted(wanted):
        if 1<=n<=len(lines): report.append(f'{key}:{n} {lines[n-1]}')
with (outdir/'consistency-anchor-probe-output-v4.txt').open('x',encoding='utf-8') as f: f.write('\n'.join(report)+'\n')
print('Saved exact anchor excerpt audit.')