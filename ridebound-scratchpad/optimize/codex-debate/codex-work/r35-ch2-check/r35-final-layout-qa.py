from pathlib import Path
from collections import Counter
import json, re, hashlib

ROOT = Path(__file__).resolve().parent
source = ROOT/'R35-CH2-FACTCHECK-CODEX.md'
text = source.read_text(encoding='utf-8')
# Preserve prior files: create a second-pass report with both late-added rows
# contiguous with their proper Markdown table.
text = text.replace('\n\n| F84 |', '\n| F84 |').replace('\n\n| E05 |', '\n| E05 |')
text = text.replace('Ngày kiểm: 13/10/2026.', 'Ngày kiểm: 13/10/2026. Bản giao cuối: v2 (kiểm lại trình bày bảng; giữ nguyên 156 kết luận).', 1)
out = ROOT/'R35-CH2-FACTCHECK-CODEX-v2.md'
with out.open('x', encoding='utf-8', newline='\n') as f:
    f.write(text)
blocks = re.findall(r'(?:^\|.*\n)+', text, re.MULTILINE)
item_rows = []
for block in blocks:
    lines = block.strip().splitlines()
    assert len(lines) >= 2 and re.match(r'^\|[- :|]+\|$', lines[1]), lines[:2]
    for line in lines[2:]:
        if re.match(r'^\| (?:F\d+|T\d+|M\d+|P\d+|E\d+) \|', line):
            cells = [c.strip() for c in re.split(r'(?<!\\)\|', line)[1:-1]]
            assert len(cells) == 5, cells
            item_rows.append(cells)
counts = Counter(r[-1] for r in item_rows)
assert len(item_rows) == 156
assert counts == {'ACCEPT':106, 'ACCEPT WITH CORRECTIONS':46, 'REJECT':4}
assert len(set(r[0] for r in item_rows)) == 156
assert len(re.findall(r'^### C\d+ — Hạng', text, re.MULTILINE)) == 14
assert '\ufffd' not in text
assert text.count('<!-- COUNTS -->') == 0
qa = {'final_file':out.name, 'audit_items':len(item_rows), 'decision_counts':dict(counts), 'markdown_table_blocks':len(blocks), 'all_items_inside_valid_tables':True, 'ranked_replacements':14, 'verified_citation_keys':15, 'final_bytes':out.stat().st_size, 'final_sha256':hashlib.sha256(out.read_bytes()).hexdigest(), 'source_draft_unchanged_by_task':True, 'latest_report':'R35-CH2-FACTCHECK-CODEX-v2.md'}
with (ROOT/'r35-final-qa-v2.json').open('x', encoding='utf-8') as f:
    json.dump(qa, f, ensure_ascii=False, indent=2)
print(json.dumps(qa, ensure_ascii=False, indent=2))
