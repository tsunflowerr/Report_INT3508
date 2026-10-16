"""Snapshot all docs with exact paragraph deduplication and source provenance.
Extraction is not reading; chunks need explicit review in docs-reading-progress.json.
"""
from pathlib import Path
import hashlib, json, re

root = Path('E:/Code/RideBound/docs')
out = Path(__file__).parent / 'docs-reading'
out.mkdir(exist_ok=True)
records = []
by_text = {}
files = []
for path in sorted(root.rglob('*')):
    if not path.is_file():
        continue
    raw = path.read_bytes()
    content = raw.decode('utf-8-sig')
    files.append({'path': str(path), 'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)})
    lines = content.splitlines()
    start = 0
    for end in range(len(lines) + 1):
        if end < len(lines) and lines[end].strip():
            continue
        if end > start:
            block = '\n'.join(lines[start:end])
            # Preserve every nonblank character; identical paragraphs can be read once.
            key = hashlib.sha256(block.encode()).hexdigest()
            occurrence = {'path': str(path.relative_to(root)), 'startLine': start+1, 'endLine': end}
            if key in by_text:
                by_text[key]['occurrences'].append(occurrence)
            else:
                record = {'id': len(records)+1, 'sha256': key, 'text': block, 'occurrences': [occurrence]}
                records.append(record)
                by_text[key] = record
        start = end+1

# Large JSON paragraphs are segmented without dropping content.
chunks = []
buffer = ''
part_ids = []
for record in records:
    text = record['text']
    for offset in range(0, len(text), 18000):
        source = record['occurrences'][0]
        segment = f"\n[BLOCK {record['id']} OFFSET {offset}; {source['path']}:{source['startLine']}; occurrences={len(record['occurrences'])}]\n" + text[offset:offset+18000] + '\n'
        if buffer and len(buffer) + len(segment) > 24000:
            chunks.append({'text': buffer, 'parts': part_ids})
            buffer, part_ids = '', []
        buffer += segment
        part_ids.append({'block': record['id'], 'offset': offset, 'length': min(18000, len(text)-offset)})
if buffer:
    chunks.append({'text': buffer, 'parts': part_ids})
manifest = []
for i, chunk in enumerate(chunks, 1):
    filename = f'chunk-{i:03d}.txt'
    (out / filename).write_text(chunk['text'], encoding='utf-8')
    manifest.append({'file': filename, 'chars': len(chunk['text']), 'parts': chunk['parts']})
(out / 'index.json').write_text(json.dumps({'files': files, 'records': records, 'chunks': manifest}, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({'files': len(files), 'uniqueBlocks': len(records), 'occurrences': sum(len(r['occurrences']) for r in records), 'chunks': len(chunks), 'uniqueChars': sum(len(r['text']) for r in records)}, indent=2))
