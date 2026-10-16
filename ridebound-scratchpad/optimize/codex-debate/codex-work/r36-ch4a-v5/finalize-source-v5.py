"""Create final script; preserve delivered v2 while correcting note anchors."""
from pathlib import Path
D = Path(__file__).resolve().parent
s = (D/'apply-and-check-v4.py').read_text(encoding='utf-8')
for old, new in [
    ('08-chuong4-phanA-v5-v2', '08-chuong4-phanA-v5-v3'),
    ('08-chuong4-phanA-v5-CHANGES-v2', '08-chuong4-phanA-v5-CHANGES-v3'),
    ('CHANGES-v2.md', 'CHANGES-v3.md'),
    ('root-qa-v2.json', 'root-qa-v3.json'),
    ('apply-and-check-v4.py', 'apply-and-check-v5.py'),
    ('RUN38:9–10', 'RUN38:5–6,42–44'),
    ('Ch3 v4-v3:496–498,733–735', 'Ch3 v4-v3:733–735'),
    ('TESTRUN-45f8026-2026-10-12.md:21', 'TESTRUN-45f8026-2026-10-12.md:18'),
    ('B184–185:** 47,6%/62,8% và 39,0%/11,0% ở phép thử đưa dự báo vào bộ điều phối vẫn chỉ có trung bình theo 15 kịch bản;',
     'B184–186:** ở phép thử đưa dự báo vào bộ điều phối, tỉ lệ bị ép 47,6%/62,8% là trung bình trên cùng 15 kịch bản, còn tỉ lệ khách bị phá lời hứa 39,0%/11,0% là trung bình trên tám kịch bản khung 7 giờ;'),
    ('Không gắn một cặp gộp vào hai trung bình ấy.', 'Không gắn cặp gộp vào các trung bình theo kịch bản ấy.'),
]:
    assert old in s, old
    s = s.replace(old,new)
# Short identifiers and count headings not prefixed by full filenames.
s = s.replace('A-v5-v2', 'A-v5-v3').replace('v5-v2', 'v5-v3')
old = "    'Áp R34 v2 và addendum 13/10/2026. Tên `-v2` theo yêu cầu tiếp tục; không ghi đè, '\n"
new = "    'Áp R34 v2 và addendum 13/10/2026. Giữ nguyên hai deliverable `-v2`; bản `-v3` chỉ đính chính '\n    'bốn chi tiết ghi chú sau kiểm cuối và đồng bộ tên trong comment của TeX. Không ghi đè, '\n"
assert old in s
s = s.replace(old,new)
needle = "outputs = {\n    TEX: target,"
assert needle in s
s = s.replace(needle,"previous = (OUT/'08-chuong4-phanA-v5-v2.tex').read_text(encoding='utf-8')\nassert namespace['comments_removed'](previous) == namespace['comments_removed'](target), 'Final pass changes comments only in TeX'\n"+needle)
with (D/'apply-and-check-v5.py').open('x',encoding='utf-8',newline='\n') as f:
    f.write(s)
print('Final script created; all prior artifacts preserved.')
