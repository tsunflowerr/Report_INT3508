import json,hashlib,sys
from pathlib import Path
from pypdf import PdfReader
root=Path(__file__).parent
source=root/'downloads'/sys.argv[2]
pages=[p.extract_text(extraction_mode='layout') for p in PdfReader(source).pages]
(root/'corpus'/f'{sys.argv[1]}.pages.json').write_text(json.dumps(pages,ensure_ascii=False),encoding='utf-8')
(root/'corpus'/f'{sys.argv[1]}.txt').write_text('\n\n'.join(pages),encoding='utf-8')
row={'id':sys.argv[1],'path':str(source),'url':sys.argv[3],'pages':len(pages),'sha256':hashlib.sha256(source.read_bytes()).hexdigest()}
(root/'corpus'/f'{sys.argv[1]}.source.json').write_text(json.dumps(row,indent=2),encoding='utf-8')
print(json.dumps(row))
