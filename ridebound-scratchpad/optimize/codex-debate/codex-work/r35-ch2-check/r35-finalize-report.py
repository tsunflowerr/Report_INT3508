from pathlib import Path
import json, re
from collections import Counter

ROOT = Path(__file__).resolve().parent
draft = Path('E:/Code/Report_INT3508/ridebound-scratchpad/rewrite-2026-10/drafts/06-chuong2-v4.tex').read_text(encoding='utf-8')
body = (ROOT/'r35-report-body.md').read_text(encoding='utf-8')

# Root's cross-check of the actual first pages supersedes unverified expanded names.
corrections = {
    'Ali Elmi; Elizabeth Moylan': 'Amir Elmi; Emily Moylan',
    'Arslan A. Syed; Chuhan Ding': 'Arslan Ali Syed; Chenhao Ding',
    'Yinan Zhang; Hussam Hamdy; Jonas Brodersen; Ziyuan Chen': 'Yunfei Zhang; Hoda Hamdy; Joel Brodersen; Zhipu Chen',
    'Karsten Kandler': 'Kim Kandler',
    'Pasquale Leonardi': 'Pierfrancesco Leonardi',
    'Nicolas Kühnel': 'Nico Kühnel',
    'Axel Schulz': 'Arne Schulz',
    'Amalia Mitrani; Kiran Neki; Richard M. Humphreys': 'Alex Mitrani; Kazuyuki Neki; Richard Martin Humphreys',
    'C đúng là tổng |p−e|, không tổng |p−v|': 'C đúng là tổng \\|p−e\\|, không tổng \\|p−v\\|',
    '| F39 | 126: chùng 0 nghĩa được bảo đảm không bị đổi giờ | ELMI nói chuyến tin cậy trong mô hình thời gian cạnh cố định. Nên chỉ rõ thời gian chờ/độ trễ không tăng do ghép thêm, tránh hiểu là bảo đảm mọi nguyên nhân ngoài đời (C4). | OVERSTATED | ACCEPT WITH CORRECTIONS |': '| F39 | 126: chùng 0 nghĩa được bảo đảm không bị đổi giờ | ELMI tr. bài 12–13 bảo đảm chuyến tin cậy trong mô hình thời gian cạnh cố định, đúng với giới hạn mà câu kế tiếp của chương đã nêu. C4 diễn đạt cụ thể hơn bằng thời gian chờ/độ trễ không tăng do ghép thêm. | AGREE | ACCEPT |',
    '| F73 | 242–244: không nhiễu ngẫu nhiên; “mức trần” cho dự báo theo giờ, không hiệu quả ngoài đời | REG I02 và báo cáo dự báo §6 ghi môi trường gần tất định, F10. “Mức trần” là cách diễn giải thuận lợi, không cận trên toán học đã chứng minh. Sửa C11. | OVERSTATED | ACCEPT WITH CORRECTIONS |': '| F73 | 242–244: không nhiễu ngẫu nhiên; “mức trần” cho dự báo theo giờ, không hiệu quả ngoài đời | REG I02; báo cáo dự báo §6; run_t38.py:8–9 có sigma = shockRate = 0; F10. Cách đọc giới hạn đúng theo sổ. C11 là lựa chọn diễn đạt rõ hơn, không phải bác số liệu hay yêu cầu chứng minh cận toán học mà bản nháp không nêu. | AGREE | ACCEPT |',
    'EV không tự làm suy luận thành thực nghiệm/khảo sát toàn ngành hay cận toán học. C6/C11/C12 tách đúng phạm vi.': 'EV không tự làm suy luận TLC thành thực nghiệm hay xác nhận phủ định chuẩn ngành toàn cầu. C6/C12 tách đúng phạm vi; C11 là làm rõ giới hạn dự báo đã có trong I02.',
    'Giữ EV C2-04; bổ sung `HZ tr. bài 8, dòng 24–27`': 'Câu mở đoạn có thể thu hẹp thành: “Trong các dạng ràng buộc đã xét, cách Hörl và Zwick xử lý thời gian đi thay đổi là tiền lệ gần với mốc giữ nguyên kế hoạch của luật C.”\n\nGiữ EV C2-04; bổ sung `HZ tr. bài 8, dòng 24–27`',
    'Toàn văn Yu chưa được kiểm; câu hiện tại đủ ở mức tóm tắt và phải giữ chú thích.': 'Khi ghép, cần thêm đủ 9 khóa mới đã được BIB đề nghị: `engelhardt2026`, `horl2022`, `hu2022`, `laupichler2026`, `leonardi2024`, `lu2024`, `molenbruch2017`, `wardman2026`, `yu2022`. Đây là việc tích hợp, không phải 9 lỗi siêu dữ liệu.\n\nToàn văn Yu chưa được kiểm; câu hiện tại đủ ở mức tóm tắt và phải giữ chú thích.',
}
for old, new in corrections.items():
    assert old in body, old
    body = body.replace(old, new)
extra = '| F84 | 153: “gần luật C nhất” | Đây là nhận xét so các dạng đã xét, không kết quả paper hay kết luận toàn văn liệu. Thêm phạm vi “trong các dạng ràng buộc đã xét” ở C1, phù hợp D03 và CH3. | AGREE | ACCEPT WITH CORRECTIONS |\n'
body = body.replace('\n## 2. Bảng 2.1', '\n'+extra+'\n## 2. Bảng 2.1')

with (ROOT/'r35-report-body-v2.md').open('x', encoding='utf-8', newline='\n') as f:
    f.write(body)

rows = []
for line in body.splitlines():
    if re.match(r'^\| (?:F\d+|T\d+|M\d+|P\d+|E\d+) \|', line):
        cells = re.split(r'(?<!\\)\|', line)[1:-1]
        cells = [c.strip() for c in cells]
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
assert len(ev_lines) == 33
for pattern in ['Axel Schulz','Ali Elmi; Elizabeth','Chuhan Ding','Karsten Kandler','Pasquale Leonardi','Nicolas Kühnel','Amalia Mitrani']:
    assert pattern not in body, pattern
for verdict in ['ACCEPT','ACCEPT WITH CORRECTIONS','REJECT']:
    counts.setdefault(verdict, 0)
count_text = f"**Đếm {len(rows)} mục:** {counts['ACCEPT']} ACCEPT; {counts['ACCEPT WITH CORRECTIONS']} ACCEPT WITH CORRECTIONS; {counts['REJECT']} REJECT. Đánh giá nguồn: " + '; '.join(f'{evidence_counts[v]} {v}' for v in ['AGREE','WRONG','OVERSTATED','CANNOT CHECK']) + '. Các số này đếm hàng kiểm, không đếm số paper và không cộng lại các ghi chú của tác vụ phụ.'
final = body.replace('<!-- COUNTS -->', count_text)
with (ROOT/'R35-CH2-FACTCHECK-CODEX.md').open('x', encoding='utf-8', newline='\n') as f:
    f.write(final)
qa = {'audit_items':len(rows), 'decision_counts':dict(counts), 'evidence_counts':dict(evidence_counts), 'cited_keys':keys, 'ev_count':len(ev_lines), 'ev_lines':ev_lines, 'metadata_rows':len(meta), 'unique_item_ids':len(set(ids)), 'table_columns_valid':True, 'final_file':'R35-CH2-FACTCHECK-CODEX.md', 'final_bytes':len(final.encode('utf-8'))}
with (ROOT/'r35-final-qa.json').open('x', encoding='utf-8') as f:
    json.dump(qa, f, ensure_ascii=False, indent=2)
print(json.dumps(qa, ensure_ascii=False, indent=2))
