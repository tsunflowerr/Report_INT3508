import json,sys
from pathlib import Path
import pypdfium2 as pdfium
root=Path(__file__).parent
inventory=json.loads((root/'corpus-inventory.json').read_text(encoding='utf-8'))
entry=next((x for x in inventory if x['id']==sys.argv[1]),None)
if entry is None:
 entry=json.loads((root/'corpus'/f'{sys.argv[1]}.source.json').read_text(encoding='utf-8'))
doc=pdfium.PdfDocument(entry['path'])
for page in map(int,sys.argv[2:]):
 dest=root/'renders'/f'{entry["id"]}-page-{page}.png'
 doc[page-1].render(scale=1.4).to_pil().save(dest)
 print(dest)
