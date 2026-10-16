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
inventory['initial_ch2_files'] = [f.name for f in files if f.name.startswith('06-')]
with (OUT/'inventory-start.json').open('x',encoding='utf-8') as h: json.dump(inventory,h,ensure_ascii=False,indent=2)
print(json.dumps(inventory,ensure_ascii=False,indent=2))
exe = 'C:/Program Files/Git/mingw64/bin/pdftotext.exe'
pdfs = [('local-elsevier','C:/PDF/Paper/1-s2.0-S0191261522000716-main.pdf'),('owner-dacn','C:/Users/quang/Downloads/23020155_TranQuangThanh_Bao cao DACN.pdf')]
for name,path in pdfs:
    p = subprocess.run([exe,'-layout','-enc','UTF-8',path,'-'],check=True,capture_output=True)
    text = p.stdout.decode('utf-8')
    pages = text.split('\f')
    excerpts = ['SOURCE: '+path,'PDF pages: '+str(len([x for x in pages if x.strip()]))]
    for i,page in enumerate(pages,1):
        if i == 1 or any(w.lower() in page.lower() for w in ['strategy B','required drop','Tiếng Việt','Tiếng Anh','TÀI LIỆU THAM KHẢO']):
            excerpts += [f'\n[PDF page {i}]\n'+page]
    with (OUT/(name+'-excerpts.txt')).open('x',encoding='utf-8') as h:h.write('\n'.join(excerpts))
    print(name,excerpts[0:2]); print(pages[0][:4500])
