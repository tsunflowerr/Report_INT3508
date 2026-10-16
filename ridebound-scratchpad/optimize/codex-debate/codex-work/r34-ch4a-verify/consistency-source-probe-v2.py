from pathlib import Path
import re
root=Path('E:/Code/Report_INT3508/ridebound-scratchpad')
outdir=root/'optimize/codex-debate/codex-work/r34-ch4a-verify'
files={
'A': ('rewrite-2026-10/drafts/08-chuong4-phanA-v4.tex', [(106,110),(229,234),(299,347),(543,549),(734,740)]),
'B': ('rewrite-2026-10/drafts/09-chuong4-phanB-v7.tex', [(79,82),(129,133),(185,192),(318,321),(392,418),(459,462)]),
'Ch3': ('rewrite-2026-10/drafts/07-chuong3-v3.tex', [(686,693),(704,722)]),
'T38': ('tang3/t38/T38-REPORT.md', [(87,107)]),
'W07X': ('tang3/w07x/W07X-REPORT.md', [(20,29),(48,62)]),
'W07XM': ('tang3/w07x/analysis/mechanism-2026-10-01.txt', [(1,17)]),
'BUDPY': ('optimize/codex-debate/claude-work/budget_block_diagnosis.py', [(1,52)]),
'BUD': ('optimize/codex-debate/claude-work/budget-block-diagnosis-2026-10-07.txt', [(1,12)]),
'NOTES': ('rewrite-2026-10/drafts/08-chuong4-phanA-v2-NOTES.md', [(1,160)]),
}
report=[]
for key,(relative,ranges) in files.items():
    path=root/relative
    report.append(f'=== {key}: {path} ===')
    if not path.exists():
        report.append('MISSING'); continue
    lines=path.read_text(encoding='utf-8-sig').splitlines()
    for start,end in ranges:
        for n in range(start,min(end,len(lines))+1): report.append(f'{key}:{n} {lines[n-1]}')
    report.append('')
regpath=root/'rewrite-2026-10/evidence/EVIDENCE-REGISTER.md'
for n,line in enumerate(regpath.read_text(encoding='utf-8-sig').splitlines(),1):
    if re.match(r'\| (?:C17|D04|D05|D13|D19|I05|I06|K39) \|',line): report.append(f'REG:{n} {line}')
for relative in ['rewrite-2026-10/evidence/EVIDENCE-REGISTER-ADDENDUM-1.md','rewrite-2026-10/style/GLOSSARY-VI-v2.md']:
    for n,line in enumerate((root/relative).read_text(encoding='utf-8-sig').splitlines(),1):
        if re.match(r'\| (?:L1a-04|N-21) \|',line) or 'bị ép' in line: report.append(f'{relative}:{n} {line}')
report.append('\nBIBLIOGRAPHY CITATION CHECK')
alltex=list((root/'rewrite-2026-10/drafts').glob('*.tex'))+list(Path('E:/Code/Report_INT3508/ridebound/noi-dung').glob('*.tex'))
for key in ['engelhardt2026','schulz2026','horl2022']:
    anchors=[]
    for path in alltex:
        for n,line in enumerate(path.read_text(encoding='utf-8-sig').splitlines(),1):
            if re.search(r'\\bibitem(?:\[[^]]*\])?\{'+key+r'\}',line): anchors.append(f'{path}:{n}')
    report.append(f'{key}: {anchors}')
with (outdir/'consistency-source-probe-output-v2.txt').open('x',encoding='utf-8') as f: f.write('\n'.join(report)+'\n')
print('Saved source probe output (UTF-8); no simulations or builds executed.')