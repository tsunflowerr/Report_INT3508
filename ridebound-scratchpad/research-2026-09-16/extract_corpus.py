"""Read-only PDF extraction with source hashes and page coverage."""
import hashlib
import json
from pathlib import Path
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent
out = ROOT / 'corpus'
out.mkdir(exist_ok=True)
inventory = []
for i, path in enumerate(sorted(Path('C:/PDF/Paper').glob('*.pdf')), 1):
    reader = PdfReader(path)
    pages = [p.extract_text(extraction_mode='layout') for p in reader.pages]
    name = f'{i:02d}'
    (out / f'{name}.txt').write_text('\n'.join(f'\n===== PAGE {j} =====\n{t}' for j,t in enumerate(pages,1)), encoding='utf-8')
    (out / f'{name}.pages.json').write_text(json.dumps(pages,ensure_ascii=False),encoding='utf-8')
    record = {'id':name,'path':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'pages':len(pages),'chars':sum(map(len,pages)),'emptyPages':[j for j,t in enumerate(pages,1) if len(t.strip())<40], 'firstPage':pages[0][:5000]}
    inventory.append(record)
    print(name, path.name, len(pages), record['chars'], flush=True)
(ROOT/'corpus-inventory.json').write_text(json.dumps(inventory,ensure_ascii=False,indent=2),encoding='utf-8')
