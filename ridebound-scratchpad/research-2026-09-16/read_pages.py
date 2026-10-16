import json,re,sys
from pathlib import Path
root=Path(__file__).parent
pages=json.loads((root/'corpus'/f'{sys.argv[1]}.pages.json').read_text(encoding='utf-8'))
start=int(sys.argv[2]); end=int(sys.argv[3])
for i in range(start-1,min(end,len(pages))):
 print(f'\n--- PDF {sys.argv[1]} PAGE {i+1} ---')
 print(re.sub(r'[ \t]+',' ',pages[i]))
