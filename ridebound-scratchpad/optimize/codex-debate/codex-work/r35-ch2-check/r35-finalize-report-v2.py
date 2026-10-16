from pathlib import Path
import json, re, hashlib
from collections import Counter

ROOT = Path(__file__).resolve().parent
draft_path = Path('E:/Code/Report_INT3508/ridebound-scratchpad/rewrite-2026-10/drafts/06-chuong2-v4.tex')
draft = draft_path.read_text(encoding='utf-8')
body = (ROOT/'r35-report-body-v2.md').read_text(encoding='utf-8')
body = body.replace('| E01 | 33 dòng `% EV:` của v4 | Có đường dẫn bằng chứng cho mọi đoạn dữ kiện/bảng; số đếm và 15 khóa trích khớp.', '| E01 | 31 dòng bắt đầu `% EV:` của v4 | Có đường dẫn bằng chứng cho các đoạn dữ kiện/bảng; 15 khóa trích khớp. Số thực đếm là 31 chú thích bằng chứng; 33 trong brief/NOTES không khớp tệp hiện tại.')
extra = '| E05 | Brief/NOTES nói v4 có 33 dòng `% EV` | Kiểm trực tiếp cho 31 dòng bắt đầu `% EV:`; thêm một dòng header chứa chuỗi này, tổng 32 dòng chứa chuỗi. Đây là sai số đếm ghi chú, không phải hai đoạn bằng chứng mất tích. C14 sửa mô tả ghi chú. | WRONG | ACCEPT WITH CORRECTIONS |\n'
body = body.replace('\n## 6. Các sửa ưu tiên', '\n'+extra+'\n## 6. Các sửa ưu tiên')
body = body.replace('## 7. Giới hạn còn lại và điều kiện ghép', '### C14 — Hạng 14: sửa số đếm chú thích trong ghi chú ghép\n\nThay mô tả “cùng 33 dòng `% EV`” bằng:\n\n> Bản v4 giữ cùng tập khóa trích dẫn với v3; trong tệp v4 hiện tại có 31 dòng chú thích bằng chứng bắt đầu bằng `% EV:`.\n\nKhông tự thêm hai dòng trống để làm đủ một con số trong ghi chú.\n\n## 7. Giới hạn còn lại và điều kiện ghép')
body = body.replace('Sau C1–C13, chương', 'Sau các sửa C1–C14, chương')
with (ROOT/'r35-report-body-v3.md').open('x', encoding='utf-8', newline='\n') as f:
    f.write(body)

rows = []
for line in body.splitlines():
    if re.match(r'^\| (?:F\d+|T\d+|M\d+|P\d+|E\d+) \|', line):
        cells = [c.strip() for c in re.split(r'(?<!\\)\|', line)[1:-1]]
        assert len(cells) == 5, (cells[0], len(cells))
        assert cells[-2] in {'AGREE','WRONG','OVERSTATED','CANNOT CHECK'}, cells
        assert cells[-1] in {'ACCEPT','ACCEPT WITH CORRECTIONS','REJECT'}, cells
        rows.append(cells)
ids = [r[0] for r in rows]
assert len(ids) == len(set(ids))
counts = Counter(r[-1] for r in rows)
evidence_counts = Counter(r[-2] for r in rows)
keys = sorted(set(k.strip() for c in re.findall(r'\\cite\{([^}]+)\}', draft) for k in c.split(',')))
meta = [r for r in rows if r[0].startswith('M')]
assert len(meta) == len(keys) == 15
assert sorted(r[1].strip('`') for r in meta) == keys
ev_lines = [n for n, line in enumerate(draft.splitlines(), 1) if line.startswith('% EV:')]
ev_mentions = [n for n, line in enumerate(draft.splitlines(), 1) if '% EV:' in line]
assert len(ev_lines) == 31 and len(ev_mentions) == 32
assert len([r for r in rows if r[0].startswith('F')]) == 84
assert len([r for r in rows if r[0].startswith('T1')]) == 16
assert len([r for r in rows if r[0].startswith('T2')]) == 28
for pattern in ['Axel Schulz','Ali Elmi; Elizabeth','Chuhan Ding','Karsten Kandler','Pasquale Leonardi','Nicolas Kühnel','Amalia Mitrani','<!-- COUNTS --> missing']:
    assert pattern not in body, pattern
count_text = f"**Đếm {len(rows)} mục:** {counts['ACCEPT']} ACCEPT; {counts['ACCEPT WITH CORRECTIONS']} ACCEPT WITH CORRECTIONS; {counts['REJECT']} REJECT. Đánh giá nguồn: " + '; '.join(f'{evidence_counts[v]} {v}' for v in ['AGREE','WRONG','OVERSTATED','CANNOT CHECK']) + '. Các số này đếm hàng kiểm, không đếm số paper và không cộng lại các ghi chú của tác vụ phụ.'
final = body.replace('<!-- COUNTS -->', count_text)
assert '<!-- COUNTS -->' not in final
final_path = ROOT/'R35-CH2-FACTCHECK-CODEX.md'
with final_path.open('x', encoding='utf-8', newline='\n') as f:
    f.write(final)
assert final_path.read_text(encoding='utf-8') == final
qa = {'audit_items':len(rows), 'decision_counts':dict(counts), 'evidence_counts':dict(evidence_counts), 'groups':dict(Counter(re.sub(r'\d+', '', r[0]) if not r[0].startswith('T') else r[0][:2] for r in rows)), 'cited_keys':keys, 'ev_count':len(ev_lines), 'ev_lines':ev_lines, 'ev_mention_count':len(ev_mentions), 'metadata_rows':len(meta), 'unique_item_ids':len(set(ids)), 'table_columns_valid':True, 'draft_sha256':hashlib.sha256(draft_path.read_bytes()).hexdigest(), 'final_file':final_path.name, 'final_sha256':hashlib.sha256(final_path.read_bytes()).hexdigest(), 'final_bytes':len(final.encode('utf-8'))}
with (ROOT/'r35-final-qa.json').open('x', encoding='utf-8') as f:
    json.dump(qa, f, ensure_ascii=False, indent=2)
print(json.dumps(qa, ensure_ascii=False, indent=2))
