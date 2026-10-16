from pathlib import Path
import re, json, subprocess, datetime
OUT = Path(__file__).resolve().parent
KIT = Path('E:/Code/Report_INT3508/ridebound-scratchpad/rewrite-2026-10')
DRAFTS = KIT/'drafts'
names = ['07-chuong3-v3.tex','08-chuong4-phanA-v4.tex','09-chuong4-phanB-v7.tex']
files = [DRAFTS/n for n in names] + sorted(DRAFTS.glob('06-chuong2*.tex'))
def cite_keys(text):
    text = re.sub(r'(?<!\\)%[^\n]*', '', text)
    return sorted({k.strip() for block in re.findall(r'\\cite\w*\*?(?:\[[^\]]*\])*\{([^}]+)\}', text) for k in block.split(',') if k.strip()})
inventory = {'scan_time':datetime.datetime.now().astimezone().isoformat(),'files':[]}
for f in files:
    inventory['files'].append({'path':f.as_posix(),'keys':cite_keys(f.read_text(encoding='utf-8'))})
bib = Path('E:/Code/Report_INT3508/ridebound/noi-dung/10-tai-lieu.tex').read_text(encoding='utf-8')
inventory['legacy_keys'] = re.findall(r'\\bibitem\{([^}]+)\}',bib)
inventory['cited_keys'] = sorted({k for f in inventory['files'] for k in f['keys']})
inventory['current_ch2_keys'] = cite_keys((DRAFTS/'06-chuong2-v4.tex').read_text(encoding='utf-8'))
with (OUT/'inventory-resume-v2.json').open('x',encoding='utf-8') as h:json.dump(inventory,h,ensure_ascii=False,indent=2)
output = [json.dumps(inventory,ensure_ascii=False,indent=2)]
exe = 'C:/Program Files/Git/mingw64/bin/pdftotext.exe'
path = 'E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/claude-work/pdf/hoerl-zwick-2022.pdf'
p = subprocess.run([exe,'-layout','-enc','UTF-8',path,'-'],check=True,capture_output=True)
pages=p.stdout.decode('utf-8').split('\f')
output += ['SOURCE: '+path,'PDF pages: '+str(len([x for x in pages if x.strip()]))]
for i in [1,2,8,9]:output += [f'\n[PDF page {i}]\n'+pages[i-1]]
with (OUT/'inventory-and-horl-probe-output-v2.txt').open('x',encoding='utf-8') as h:h.write('\n'.join(output))
print(inventory['cited_keys']);print('Current Ch2:',inventory['current_ch2_keys']);print('Horl PDF page 9:');print(pages[8])
