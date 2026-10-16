"""Create revised implementation, preserving the unexecuted v2 script."""
from pathlib import Path

D = Path(__file__).resolve().parent
p = D/'apply-and-check-v2.py'
s = p.read_text(encoding='utf-8')
replacements = [
    ('agent-numeric-v2-output.txt', 'agent-numeric-output-v2.txt'),
    ('55.963', '44.270'),
    ('apply-and-check-v2.py', 'apply-and-check-v3.py'),
    ('B-v10:421–423 đã nói chọn 120 giây sau khi xem tập chính, gồm phép tính thử; giữ tiết lộ ở A231 và A687. Không sửa B.',
     'B-v10:421–423 đã nói chọn 120 giây sau khi xem tập chính, nhưng còn thiếu mệnh đề kể cả phép tính thử ở 120 giây; bàn giao bổ sung ở mục 5. Giữ tiết lộ đầy đủ trong A.'),
    ('B184–185:** 47,6%/62,8% ở phép thử', 'B184–185:** 47,6%/62,8% và 39,0%/11,0% ở phép thử'),
    ('B374–376 vẫn có mẫu số', 'B359–361 vẫn có mẫu số'),
]
for old, new in replacements:
    assert old in s, old
    s = s.replace(old,new)
old = "    'Chương 1 `W/r30-ch1/05-chuong1-v3.tex:192–194` cũng cần đồng bộ nếu giữ câu kiểm thử cũ; '\n    'xem `agent-consistency-v2-output.txt` cho nguồn chính xác trước khi sửa.',"
assert old in s
s = s.replace(old,"    'Chương 1 v3 không có câu kiểm thử cần sửa.',")
old = "    '- **B7:** đổi comment ghép sang tên bản A được giao `08-chuong4-phanA-v5-v2.tex`.',"
assert old in s
s = s.replace(old,"    '- **B421–423:** giữ tiết lộ đã có về việc xem tập chính trước khi chọn mức 120 giây, và thêm '\n    '`kể cả các phép tính thử ở 120 giây` để áp đủ R34 §7.4. A231 hiện đã giữ ý này; '\n    'bằng chứng I06/C4A-11/I11/K42. Giữ ý các ngày kiểm học máy đã xem của B-v10.',\n"+old)
s = s.replace("    'Các mục B đã giải quyết, không yêu cầu sửa lại: B421–423 tiết lộ dùng lại tập chính/120 giây; '\n",
              "    'Các mục B đã giải quyết: lõi tiết lộ dùng lại tập chính/120 giây (B421–423); '\n")
old = "assert 'FINAL' in numeric or 'PASS' in numeric, 'Read the completed numeric report before delivery'"
assert old in s
s = s.replace(old,"confirm = (OUT/'agent-numeric-confirm-output-v2.txt').read_text(encoding='utf-8-sig')\nsupplement = (OUT/'agent-numeric-supplement-output-v2.txt').read_text(encoding='utf-8-sig')\nassert 'CONFIRM_CHECK PASS' in confirm and 'CHECK PASS' in supplement\nassert (OUT/'agent-numeric-report-v2.md').exists()\n# Initial numeric probe failed only its stale denominator expectation; confirmed independently.\n")
needle = 'assert BASE.read_bytes() == source_bytes\n\ntable_widths'
assert needle in s
addition = r'''assert BASE.read_bytes() == source_bytes

# Root: reaggregate saved per-run rows and directly reread all 170 IVC JSONs.
main_rows = [json.loads(line.split(' ',1)[1]) for line in numeric.splitlines() if line.startswith('MAIN_ROW ')]
assert len(main_rows) == 170
import csv
with (WORK/'r34-ch4a-verify/main-obligations-v4.tsv').open(encoding='utf-8-sig',newline='') as f:
    prior_rows = list(csv.DictReader(f,delimiter='\t'))
root_main_totals = {}
for arm in ('U','C-30','Mplus-30','Mplus-60','V-30'):
    selected = [r for r in main_rows if r['arm'] == arm]
    assert len(selected) == 34
    for row in selected:
        obj = json.loads(Path(row['source']).read_text(encoding='utf-8-sig'))
        assert obj['acked'] == row['acked'] and obj['nonNormalAcked'] == row['forced']
        assert obj['served'] == row['served'] == len(obj['riders']) == len(obj['alight'])
        if arm in ('Mplus-30','Mplus-60'):
            threshold = int(arm.split('-')[1])*1000
            breach = sum(obj['alight'][rid]-rider['p0_drop'] > threshold for rid,rider in obj['riders'].items())
        elif arm == 'C-30':
            breach = sum(sum(abs(q['p_d']-q['e_d']) for q in rider['rev']) > 30000 for rider in obj['riders'].values())
        elif arm == 'V-30':
            breach = sum(sum(abs(q['p_d']-q['v_d']) for q in rider['rev']) > 30000 for rider in obj['riders'].values())
        else:
            breach = 0
        assert breach == row['breach']
        prior = [q for q in prior_rows if q['arm'] == arm and q['cell'] == row['cell']]
        assert len(prior) == 1
        for key in ('served','breach','forced','acked'):
            assert int(prior[0][key]) == row[key]
    root_main_totals[arm] = {key:sum(r[key] for r in selected) for key in ('served','breach','forced','acked')}
root_morning_rows = [json.loads(line.split(' ',1)[1]) for line in numeric.splitlines() if line.startswith('MORNING_ROW ')]
assert len(root_morning_rows) == 64
assert sum(r['acked'] for r in root_morning_rows) == 44270
assert sum(r['forced'] for r in root_morning_rows) == 0
assert 20101 + 44270 == 64371  # Existing E01/A736 total for all 98 C runs.
for arm, sum_ms, count in (('U',2065946452,2434),('C-30',1980192800,2338)):
    rr = re.findall(r'PROMISE_ROW '+arm+r' .*?count=(\d+) duration_sum_ms=(\d+)',numeric)
    assert len(rr) == 34
    assert sum(int(n) for n,_ in rr) == count
    assert sum(int(v) for _,v in rr) == sum_ms
    assert round(sum_ms/count/60000,2) == (14.15 if arm=='U' else 14.12)

table_widths'''
s = s.replace(needle, addition)
s = s.replace('source_unchanged=True)',
              'source_unchanged=True, root_main_totals=root_main_totals,\n          root_morning_count=dict(runs=64,forced=0,acked=44270),\n          preserved_numeric_probe_failure="stale denominator expectation; reconciled by confirm output")')
with (D/'apply-and-check-v3.py').open('x',encoding='utf-8',newline='\n') as f:
    f.write(s)
print('Created apply-and-check-v3.py; previous script kept.')
