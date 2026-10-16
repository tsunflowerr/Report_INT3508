"""Keep official university brand assets as received, with provenance."""
from pathlib import Path
import urllib.request,hashlib,json
root=Path(__file__).resolve().parent/'branding';root.mkdir(exist_ok=True)
records=[]
for name,url in [('Logo1.png','https://2679558515.e.cdneverest.net/uet.edu.vn/2026/01/Logo1.png'),
 ('Layer_1.svg','https://2679558515.e.cdneverest.net/uet.edu.vn/2026/01/Layer_1.svg')]:
    data=urllib.request.urlopen(url,timeout=15).read();(root/name).write_bytes(data)
    records.append({'file':name,'url':url,'sourcePage':'https://uet.vnu.edu.vn/','sha256':hashlib.sha256(data).hexdigest()})
(root/'provenance.json').write_text(json.dumps(records,indent=1),encoding='utf-8')
from PIL import Image
print('Logo1',Image.open(root/'Logo1.png').size)
print((root/'Layer_1.svg').read_text(encoding='utf-8')[:200])
