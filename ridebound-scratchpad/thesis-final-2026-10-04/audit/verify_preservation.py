"""Verify original thesis bytes and the immutable blind-review packet."""
from pathlib import Path
import csv,hashlib,json
ROOT=Path(__file__).resolve().parent.parent
manifest=list(csv.DictReader((ROOT/'audit'/'original-hashes.csv').open(encoding='utf-8-sig')))
original_bad=[]
for entry in manifest:
    p=Path(entry['Path'])
    if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest().upper()!=entry['SHA256'].upper():original_bad.append(str(p))
print('Original thesis:',len(manifest),'files; mismatches:',original_bad)
packet=ROOT/'review-packet-v1'
entries=json.loads((packet/'MANIFEST.json').read_text(encoding='utf-8'))
bad=[]
for entry in entries:
    p=packet/entry['path']
    if hashlib.sha256(p.read_bytes()).hexdigest()!=entry['sha256']:bad.append(entry['path'])
print('Review packet:',len(entries),'files; mismatches:',bad)
result={'originalFiles':len(manifest),'originalMismatches':original_bad,
        'packetFiles':len(entries),'packetMismatches':bad}
(ROOT/'audit'/'preservation-check.json').write_text(json.dumps(result,indent=1),encoding='utf-8')
assert not original_bad and not bad
