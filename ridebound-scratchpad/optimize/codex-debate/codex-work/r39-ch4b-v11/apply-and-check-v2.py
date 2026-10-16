"""R39 targeted edit; exclusive small-text outputs, no build or simulation.

All original slices outside the declared edits are retained after LF normalization.
Only the pure word-count functions are selected by AST from the inspected R33 script.
The candidate is reviewed before its two final-name deliverables are exclusive-created.
"""
from pathlib import Path
import ast
import hashlib
import html
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
OUT = Path(__file__).resolve().parent
WORK = OUT.parent
S = WORK.parents[2]
KIT = S / 'rewrite-2026-10'
BASE = KIT / 'drafts/09-chuong4-phanB-v10.tex'
A = WORK / 'r36-ch4a-v5/08-chuong4-phanA-v5-v3.tex'
CH3 = WORK / 'r33-ch3v4/07-chuong3-v4-v3.tex'
APP = WORK / 'r31-ch5/11-phuluc-v2.tex'
BIB = WORK / 'r32-bib/10-tai-lieu-draft-v2.tex'
NUM = OUT / 'agent-numbers-v1.json'
nums = json.loads(NUM.read_text(encoding='utf-8'))
source = BASE.read_text(encoding='utf-8')
base_lines = source.splitlines(keepends=True)
assert len(base_lines) == 450
changes = []

def change(first, last, new, evidence):
    old = ''.join(base_lines[first-1:last]) if last >= first else ''
    assert old != new
    changes.append(dict(first=first, last=last, old=old, new=new, evidence=evidence))

def line_replacement(n, old, new, evidence):
    assert old in base_lines[n-1], (n, old)
    change(n, n, base_lines[n-1].replace(old, new), evidence)

change(2, 7, r'''% Chương 4, PHẦN B (mục 4.6–4.11) — bản sửa v11 (2026-10-13), BẢN DÙNG ĐỂ GHÉP.
% Sửa có mục tiêu từ drafts/09-chuong4-phanB-v10.tex theo R37 và brief R39; các bản trước giữ nguyên.
% Quyết định trước: reviews/CH4B-REVISION-LOG.md; ghi chú cũ: drafts/09-chuong4-phanB-v8-NOTES.md.
% Từng thay đổi, phép kiểm số mới và việc bàn giao: 09-chuong4-phanB-v11-CHANGES-v2.md bên cạnh.
% Nối ngay sau 08-chuong4-phanA-v5-v3.tex trong cùng \input{noi-dung/08-chuong4}; không có \chapter mới.
''', 'ROUND39-CH4B-V11-APPLY.md; R36 CHANGES-v3 §5; R37 §1; không đổi provenance của các dòng EV cũ.')
line_replacement(12, 'Không dùng gói mới: hình vẽ bằng TikZ thường; danh sách dùng enumitem như chương 3.',
                 'Không dùng gói mới: TikZ, enumitem và graphicx đã nạp trong main.tex; thu bảng/hình bằng resizebox.',
                 'main.tex:9,14,19; R39 yêu cầu sửa hai overfull, không đổi nội dung.')

table_old = ''.join(base_lines[38:58])
change(39, 58, '\\resizebox{\\linewidth}{!}{%\n' + table_old + '}\n',
       'R39; trial main.log:1832–1834 (29,17484 pt; B39–59 = bản ghép803–823); main.tex:9,28. Giữ nguyên toàn bộ tabular, kể cả hai multicolumn dài; bề rộng ngoài bằng linewidth.')
line_replacement(72, 'chương kết luận đặt phép thử này lên đầu các hướng phát triển.',
                 'phép thử này là một hướng phát triển còn mở.',
                 'R37 §1.6; H02,H10,K18,I12. Ch5 r31-v2:33 nay đã có, nên lý do cũ về thiếu Ch5 hết hiệu lực; vẫn áp câu thay được yêu cầu.')

change(124, 127, r'''Lợi ích không riêng của luật C. Trên cùng 21 kịch bản, khi có dự báo, luật hạn chót 30 giây giảm từ 66 xuống 2 khách
trễ trong 1.471 khách được phục vụ; luật trần độ dời khách thấy 30 giây cũng giảm từ 66 xuống 2 trong 1.470 khách.
Điều phối không trần giảm từ 129 xuống 63 trong 1.512 khách. Riêng khung 17 giờ, 28 khách trễ trong 437 khách của điều
phối không trần không đổi, còn luật C có 0 trong 418 khách. Theo sổ, 86,1\% số giây trễ của 68 khách trễ khi không dự
báo thuộc phần được hồ sơ lịch sử giải thích (Hình~\ref{hinh:c4-so}); dự báo và trần nhắm vào hai phần khác nhau của sổ.
''', 'R37 §1.2; N4B8-02; F09; agent-numbers-v1.json:forecast; số U/C kiểm chéo bằng từng khách; 86,1% có phép kiểm bổ sung agent-numbers-summary-v1.json:forecast_ledger.')
line_replacement(130, 'Giá của dự báo là', 'Trên 21 kịch bản này, giá của dự báo là',
                 'R37 §1.2 (làm rõ nhóm); F06; agent-numbers-v1.json:forecast_oracle_and_price: 21, 13,6986668/27,7534291/3,1816808 giây trung bình theo kịch bản.')
change(135, 136, r'''đời. Tắc đường là một hệ số chung cho cả thành phố. Trên cả 34 kịch bản, với luật C, kéo dài lời hứa theo đúng hệ số
sẽ xảy ra cho giờ trả khớp trong vòng 2 giây ở cả 2.305 khách không bị điều phối dời. Phép kiểm giờ đón cũng chưa dùng
lời hứa này (mục~\ref{muc:c4-thaoluan}).
''', 'R37 §1.2; F10 (FA:28; RX:8); agent-numbers-v1.json:forecast_oracle_and_price (oracle_n = oracle_ok = 2.305 trên34; không phải1.471 khách của21). Giữ hai câu giới hạn.')

figure_old = ''.join(base_lines[140:170])
change(141, 170, '\\resizebox{\\linewidth}{!}{%\n' + figure_old + '}\n',
       'R39; trial main.log:1837–1839 (15,8002 pt; B170–174 = bản ghép934–938). Đây là hình TikZ; giữ mọi tọa độ, nhãn và caption, chỉ thu toàn bộ hộp về linewidth. graphicx đã nạp main.tex:9.')
line_replacement(177, 'các nhãn làm tròn độc lập, nên tổng của nhãn có thể lệch 0,1 s',
                 'các nhãn làm tròn đến giây độc lập, nên tổng ba nhãn là 6.218 s, lệch 1 s so với nhãn tổng 6.217 s',
                 'R37 §1.10; N4B8-11; agent-numbers-v1.json:figure_rounding (82+5.353+783=6.218; tổng chính xác6.217,406).')

mf = nums['morning_promise_breaks']['Mplus-30F']
mb = nums['morning_promise_breaks']['Mplus-30']
assert (mb['scenarios'],mb['late30'],mb['served'],mf['scenarios'],mf['late30'],mf['served']) == (8,170,442,8,45,439)
change(184, 187, r'''không có quyết định bị ép ở 14 lần chạy hoàn tất. Luật hạn chót bị ép ở 47,6\% lượt quyết định ở 15 lần chạy hoàn tất,
so với 62,8\% ở các lần chạy không đưa dự báo vào trên cùng 15 kịch bản. Tính gộp trên cùng 15 kịch bản, đó là 3.849
trong 8.496 lượt quyết định khi đưa dự báo vào, so với 5.121 trong 8.468 lượt khi không đưa vào; các tỉ lệ 47,6\% và
62,8\% ở trên là trung bình theo kịch bản. Tỉ lệ khách bị luật hạn chót phá lời hứa ở khung 7 giờ giảm từ 39,0\% xuống
11,0\%, trung bình trên cùng tám kịch bản. Tính gộp theo khách trên tám kịch bản này, đó là 170 trong 442 khách khi
không đưa dự báo vào, so với 45 trong 439 khách khi đưa vào. Vì vậy, các số của Bảng~\ref{bang:c4-nghiavu} phụ thuộc cách
hứa. Khóa luận chỉ dùng dự báo ở lời hứa báo cho khách; kết luận này chỉ áp cho cách đã thử.
''', 'R37 §1.4/CX-10; R36 §5 B184–186; agent-numbers-v1.json:dispatcher.paired (3.849/8.496,5.121/8.468; TB47,61589255/62,77032087%); morning_promise_breaks: đọc mới16 transcript khung7, TB39,04771018/10,99224586%, gộp170/442 và45/439. Không dùng cặp gộp làm tử/mẫu của TB.')
change(188, 188, base_lines[187].rstrip('\n') + '; R37 verify-numbers-v2.json:dispatcher; R39 agent-numbers-v1.json:dispatcher.paired, morning_promise_breaks (cùng15 hoàn tất; khung7 cùng8; số gộp tách khỏi trung bình theo kịch bản)\n',
       'Các nguồn của sửa B184–187; raw quyết định xác nhận/chứng chỉ không bình thường và ledger tới nơi; đối chiếu BIC từng kịch bản.')
change(191, 192, r'''mà 90\% khách giống vậy không vượt) từ thông tin đã có ở thời điểm hứa. Đó là mô hình cây quyết định tăng cường
(gradient boosting), mô hình ấy khi bỏ hai biến trạng thái xe (số khách khác đã gán và đang trên xe), và hồi quy phân vị
''', 'R37 §1.3; GLOSSARY-VI-v2; chỉ bỏ gradient ngoài ngoặc; giữ toàn bộ đặc trưng và mô hình còn lại.')
line_replacement(206, 'Không mô hình nào thỏa đủ bốn điều kiện. ',
                 'Không mô hình nào thỏa đủ bốn điều kiện. Các số đếm sau được suy từ tỉ lệ gộp theo khách đã làm tròn đến ba chữ số\nthập phân trong bảng kết quả; với mẫu số tương ứng, mỗi tỉ lệ chỉ ứng với một số nguyên. ',
                 'R37 §1.3; agent-numbers-v1.json:ml; ml_pilot_run.py:37–42,175–176. Suy số nguyên từ bảng, không đếm lại dự đoán từng khách.')
change(211, 211, base_lines[210].rstrip('\n') + '; R37 verify-numbers-v2.json:ml; R39 agent-numbers-v1.json:ml (xét mọi số nguyên, sai số 0,0005 điểm phần trăm); ml_pilot_run.py:37-42,175-176\n',
       'R37 §1.3; nguồn và chứng minh số đếm dùng trong B206–210; ghi chú cận làm tròn được đính chính ở mục2 của CHANGES mới.')

change(220, 222, r'''quyết định điều phối: vẫn có 174 khách bị điều phối dời giờ trả, với tổng độ dời lớn nhất là 590,1 giây (gần 10 phút).
Luật C trần 30 giây giới hạn tổng độ dời do điều phối của mỗi khách ở 30 giây dưới giả thiết (N); trên 34 kịch bản của
tập kiểm tra chính, mức lớn nhất đo được là 29,2 giây, kể cả ở các kịch bản cuối tuần không có dự báo. Đổi lại, luật C
phục vụ ít hơn 96 lượt.
''', 'R37 §1.1; C20,N-23,N-28,A06,A22,K05; agent-numbers-v1.json:padding,cohort_totals. Cận thiết kế30 khác mức đo29,239→29,2; U590,133→590,1; 2.434−2.338=96.')
change(223, 223, base_lines[222].replace('theo cách xây dựng;', 'dưới giả thiết (N);').replace('phần A v4', 'phần A v5-v3').rstrip('\n') + '; R37 verify-numbers-v2.json:padding; R39 agent-numbers-v1.json:padding,cohort_totals\n',
       'R37 §1.1; A-v5-v3 là bản ghép mới; thêm phép kiểm riêng30/29,2 và nhóm34.')
change(269, 271, r'''\textbf{Vai trò của từng thành phần.} Thứ nhất, ở mức kéo dài lời hứa gần bằng nhau, luật C trần 30 giây hơn cách đệm
ở ngưỡng một phút và kém ở ngưỡng hai phút: khi cùng đệm 30 giây, hai bên có 2.336 so với 2.328 lượt và 2.338 so với
2.366 lượt. Ở hàng đệm 30 giây, điều phối không trần đạt cùng 2.328 lượt không trễ quá một phút như luật C có dự báo
không đệm, với lời hứa dài thêm trung bình 37,18 so với 7,37 giây, tức khoảng năm lần.
''', 'R37 §1.1; N-16,N-17,N-18; agent-numbers-v1.json:padding,cohort_totals.extension_ratio_upad30_c30=5,047198. So phần kéo dài gần bằng, không toàn bộ lời hứa bằng và không cận đệm bắt buộc.')
change(272, 272, base_lines[271].rstrip('\n') + '; R37 verify-numbers-v2.json:padding; R39 agent-numbers-v1.json:padding,cohort_totals\n',
       'Phép kiểm các hàng đệm của sửa B269–271; không thay N-18 đầy đủ37,1833/7,3671.')
change(286, 287, r'''nghĩa vụ đó, tính trung bình theo kịch bản, nó bị ép ở 41,3\% lượt quyết định; tính gộp là 7.710 trong 20.103 lượt.
Luật hạn chót có khách tới muộn hơn lời hứa đầu không dự báo quá 30 giây ở 28 trong 34 kịch bản, còn luật C không có
quyết định bị ép hay khách vượt trần (Bảng~\ref{bang:c4-nghiavu}).
''', 'R37 §1.4; R36 §5; N-21,C13,X3-16,R36-A01; agent-numbers-v1.json:main_original_obligation (34 cache IVC mỗi luật, TB41,31136648%; gộp7.710/20.103;28/34). Giữ nguyên hai câu B284–285 về nghĩa vụ gốc và phát lại không đổi lần chạy; phù hợp bảng A báo số gộp.')
change(288, 288, base_lines[287].rstrip('\n') + '; R36-A01 (bảng A-v5-v3 dùng số gộp); R39 agent-numbers-v1.json:main_original_obligation\n',
       'Nguồn số gộp và phạm vi nghĩa vụ ở B286–287, không đánh đồng41,3% với7.710/20.103.')
change(295, 299, r'''\textbf{Khi nào chọn trần, khi nào chọn đệm.} Nếu hãng xe chỉ tính số lượt không trễ quá hai phút và chấp nhận lời hứa
dài hơn cùng nhiều khách tới sớm hơn, điều phối không trần có dự báo và đệm 30 giây đạt 2.366 lượt, so với 2.338 lượt
của luật C trần 30 giây có dự báo, trên 3.672 yêu cầu; điều phối không trần cũng phục vụ thêm 96 lượt. Nếu cần giới hạn
tổng độ dời do điều phối của từng khách, kể cả khi không có dự báo, luật C trần 30 giây làm được điều này dưới giả thiết
(N), đổi lại 96 lượt phục vụ và 242 khách đi chung. Hai cách dùng chung được; chọn cách nào là quyết định của hãng xe,
không phải kết luận của thực nghiệm.
''', 'R37 §1.1; N-19,C02,N-20,N-02,A22; agent-numbers-v1.json:padding,cohort_totals (trên3.672, phục vụ96, đi chung555−313=242 theo nguồn đã có một quy tắc đếm). Giữ B290–293 về C-120 để không suy rộng mọi trần.')
change(300, 300, base_lines[299].rstrip('\n') + '; A22 (giả thiết N); R37 verify-numbers-v2.json:padding; R39 agent-numbers-v1.json:padding,cohort_totals\n',
       'Nguồn của giới hạn30 theo điều kiện và các số trong B295–299; không biến đi chung thành phép đếm độc lập mới.')
change(347, 348, r'''Phép phát lại này tách số giây trễ theo cách cộng có giới hạn, khác phần có dấu của công thức~\eqref{eq:so}. Phần kéo
dài của mỗi khách được chặn trong khoảng từ 0 đến phần trễ còn lại sau khi trừ phần tính cho điều phối. Theo cách cộng
này, cách trộn
''', 'R37 §1.9; N4B8-07; rider_nowcast_replay.py:14–15,113–114: clip(D−P0,0,A−P0−dispatch). Giữ nguyên các số và các câu B349–351.')
change(360, 361, r'''đặt: với sổ hợp lệ $0 \le L_r \le B$ ở lượt đang xét và giả thiết (N), Nhận xét~\ref{nx:giunguyen} đã cho trước các
số 0 này; kết luận xuyên chuyến cần giả thiết (N) đúng ở mọi lượt. Điều phối không trần cũng có 0 trong 20.760 lượt.
''', 'R36 §5 B360; Ch3 v4-v3:374–385; A-v5-v3. Không đổi B358–359 (29,2/118,9/20.101/20.435); agent-numbers-v1.json:cohort_totals đối chiếu ba mẫu số0.')
change(362, 362, base_lines[361].replace('L_r ≤ B được giữ khi (N) đúng ở mọi lượt', '0 ≤ L_r ≤ B ở lượt đang xét; (N) đúng ở mọi lượt cho kết luận xuyên chuyến').rstrip('\n') + '; R39 agent-numbers-v1.json:cohort_totals\n',
       'R36 §5; Ch3:374–385 xác nhận điều kiện sổ và các lượt, nguồn số0 vẫn giữ nguyên.')
change(380, 380, r'''
Phép kiểm số đếm học máy chỉ đối chiếu số học của bảng kết quả; nó không kiểm lại quá trình học hay dự đoán của mô hình.
% EV: R37 §1.8; R39 agent-numbers-v1.py phần C; agent-numbers-v1.json:ml; ml_pilot_run.py:37-42,175-176

''', 'R37 §1.8/L-23; script chỉ xét số nguyên tương thích tỉ lệ bảng, không thực thi mô hình. Giữ toàn bộ đoạn kiểm chính/snow và EV B374–379.')
change(381, 383, r'''Chạy lại trên đúng mã nguồn đã dựng bộ chạy, cả 1.025 trong 1.025 kiểm thử tự động đạt trong một lần chạy đầy đủ ngày
13/10/2026, với kiểu xuống dòng LF và một tệp chưa ghi nhận trong cây làm việc (Phụ lục~\ref{phuluc:C}). Các phép kiểm
trên không cho biết mô phỏng giống thực tế đến đâu.
''', 'R39/R36 §5; TESTRUN-45f8026-2026-10-12.md:18, attempt4; log fullrun13/10 (9 dự án,0 lỗi/1.025 đạt/0 bỏ qua/1.025 tổng,exit0); agent-numbers-v1.json:test_attempt4. AppendixC thật có tại r31:60; giữ ref.')
change(384, 384, r'''% EV: TESTRUN-45f8026-2026-10-12.md:18 (attempt 4: LF và tệp chưa ghi nhận, 1.025/1.025 trong một lần chạy ngày 13/10/2026); C:/RideBoundData/research/testrun-45f8026-eollf-dirty-fullrun-2026-10-13.log; R39 agent-numbers-v1.json:test_attempt4; I13; A28; I01; K41
''', 'Lượt4 thay lời về lượt3/3b, không sửa các tệp evidence/appendix/Ch3 ngoài phạm vi.')
change(408, 411, r'''\item Thời gian dừng đón, trả bằng 0 giây (kiểm trên 3 lần chạy mẫu), so với 30 giây mỗi khách trong nghiên cứu điển hình
của FleetPy~\cite{engelhardt2026}, và đồ thị rút gọn chỉ có 96 nút. Phần dời do điều phối và cái giá 96 lượt vì vậy chỉ áp cho
thiết lập này.
''', 'R37 §1.7 và §7 hạng1: yêu cầu bỏ riêng câu giả thuyết chưa kiểm. Giữ nguyên câu thời gian dừng/đồ thị/phạm vi; B05,B03,J18,K48. Không cắt ngân sách hay gộp nhóm hạn chế.')
line_replacement(415, '; câu giả thuyết không có dòng sổ (OUTLINE 4.11 cho phép một câu, ghi rõ là giả thuyết)', '',
                 'B410–411 đã bỏ theo R37; xóa đúng phần EV hết hiệu lực, giữ mọi anchor cho các câu còn lại.')
change(421, 420, r'''\item Chưa kiểm độ nhạy theo hạt giống của bộ giải, nên chưa biết các chênh lệch có giữ nguyên khi đổi hạt giống.
% EV: R37 §1.8/L-26; B09; B11; chương 3 v4-v3 muc:gioihan (hạt giống cố định 7, một lần chạy mỗi kịch bản)
''', 'R37 §1.8; Ch3:704–710; B09/B11 và thiết kế mỗi kịch bản một lần; không có mô phỏng độ nhạy mới.')
line_replacement(423, 'chính tập kiểm tra chính. Chiều tuyết',
                 'chính tập kiểm tra chính, kể cả các phép tính thử ở 120 giây (mục~\\ref{muc:c4-thamdo}). Chiều tuyết',
                 'R36 §5 B421–423; R37 §1.7 (giữ disclosure qua ref thật); A-v5-v3:231–235; I06,C4A-11,I11,K42. Giữ từng câu B421–423, chỉ thêm phạm vi và ref.')
change(428, 428, base_lines[427].replace('phần A v4', 'phần A v5-v3').rstrip('\n') + '; K42 (kể cả các phép tính thử ở 120 giây); chương 3 v4-v3 muc:gioihan (hạt giống7; chưa có kiểm độ nhạy)\n',
       'R36 §5; A-v5-v3:231–235; nguồn giới hạn hạt giống vừa bổ sung. Giữ preview snow/ML và mọi số tải/chuyến.')

ordered = sorted(changes, key=lambda c: (c['first'],c['last']))
for left,right in zip(ordered,ordered[1:]):
    assert left['last'] < right['first'], (left,right)
parts = []
cursor = 0
unchanged_chars = 0
for c in ordered:
    untouched = ''.join(base_lines[cursor:c['first']-1])
    parts.extend([untouched,c['new']])
    unchanged_chars += len(untouched)
    cursor = max(cursor,c['last'])
parts.append(''.join(base_lines[cursor:]))
unchanged_chars += len(parts[-1])
target = ''.join(parts)

# Audit reverse reconstruction, not a merely visual diff.
restored = []
offset = 0
cursor = 0
for c in ordered:
    unchanged = ''.join(base_lines[cursor:c['first']-1])
    assert target[offset:offset+len(unchanged)] == unchanged
    restored.append(unchanged)
    offset += len(unchanged)
    assert target[offset:offset+len(c['new'])] == c['new']
    restored.append(c['old'])
    offset += len(c['new'])
    cursor = max(cursor,c['last'])
restored.append(target[offset:])
assert ''.join(restored) == source
assert table_old in target and figure_old in target

# Load only the four reviewed pure helpers; never execute the R33 editing script.
counter_source = (WORK/'r33-ch3v4/patch_and_check-v3.py').read_text(encoding='utf-8')
module = ast.parse(counter_source)
names = {'comments_removed','brace_arg','figure_words_text','count_words'}
helpers = [n for n in module.body if isinstance(n,ast.FunctionDef) and n.name in names]
assert len(helpers) == 4
ns = {'re':re}
exec(compile(ast.Module(body=helpers,type_ignores=[]),'reviewed-pure-word-counter','exec'),ns)

def counts(text):
    clean = ns['comments_removed'](text)
    starts = [m.start() for m in re.finditer(r'\\section\{',clean)]
    result = []
    for number,(start,end) in enumerate(zip(starts,starts[1:]+[len(clean)]),6):
        section = clean[start:end]
        title = re.search(r'\\section\{([^}]+)\}',section)[1]
        floats = re.findall(r'\\begin\{(table|figure)\}(.*?)\\end\{\1\}',section,re.S)
        prose = re.sub(r'\\begin\{(table|figure)\}.*?\\end\{\1\}','',section,flags=re.S)
        result.append({'section':f'4.{number}','title':title,'prose':ns['count_words'](prose),
                       'floats':sum(ns['count_words'](b if k=='table' else ns['figure_words_text'](b)) for k,b in floats)})
    assert len(result) == 6
    return result

def syntax(text):
    clean = ns['comments_removed'](text)
    depth = 0
    for i,ch in enumerate(clean):
        if ch in '{}' and (i == 0 or clean[i-1] != '\\'):
            depth += 1 if ch == '{' else -1
            assert depth >= 0, i
    assert depth == 0
    stack = []
    envs = {}
    for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',clean):
        if m[1] == 'begin':
            stack.append(m[2]); envs[m[2]] = envs.get(m[2],0)+1
        else:
            assert stack and stack.pop() == m[2], (m.group(),m.start())
    assert not stack
    dollars = re.findall(r'(?<!\\)\$',clean)
    assert len(dollars)%2 == 0
    forbidden = ['niêm phong','dự đoán trước','kết quả mong đợi','duy nhất','đầu tiên','vượt trội','đột phá','tối ưu','gradient ngoài']
    assert not [w for w in forbidden if w in clean.lower()]
    assert clean.count('gradient') == 1 and '(gradient boosting)' in clean
    return {'balanced_braces':True,'environment_counts':envs,'math_dollar_count':len(dollars),'forbidden_hits':[]}

old_counts,new_counts = counts(source),counts(target)
assert [x['floats'] for x in old_counts] == [x['floats'] for x in new_counts]
checks = syntax(target)
inputs = {}
for p in [BASE,A,CH3,APP,BIB,NUM,KIT/'evidence/TESTRUN-45f8026-2026-10-12.md',KIT/'ASSEMBLY-NOTES.md']:
    raw = p.read_bytes()
    inputs[str(p)] = {'sha256':hashlib.sha256(raw).hexdigest(),'lines':len(raw.decode('utf-8-sig').splitlines())}
label_places = {}
for p,t in [(OUT/'09-chuong4-phanB-v11-v2.tex',target)] + [(p,p.read_text(encoding='utf-8-sig')) for p in [A,CH3,APP]]:
    for n,line in enumerate(t.splitlines(),1):
        clean = ns['comments_removed'](line)
        for m in re.finditer(r'\\label\{([^}]+)\}',clean):
            label_places.setdefault(m[1],[]).append(f'{p}:{n}')
duplicates = {k:v for k,v in label_places.items() if len(v)>1}
assert not duplicates, duplicates
refs = []
for n,line in enumerate(target.splitlines(),1):
    for m in re.finditer(r'\\(?:ref|eqref|pageref|autoref)\{([^}]+)\}',ns['comments_removed'](line)):
        refs.append({'line':n,'target':m[1],'definitions':label_places.get(m[1],[])})
assert all(x['definitions'] for x in refs), [x for x in refs if not x['definitions']]
old_labels = set(re.findall(r'\\label\{([^}]+)\}',ns['comments_removed'](source)))
new_labels = set(re.findall(r'\\label\{([^}]+)\}',ns['comments_removed'](target)))
assert old_labels == new_labels and len(new_labels) == 11
cites = set(re.findall(r'\\cite\{([^}]+)\}',ns['comments_removed'](target)))
old_cites = set(re.findall(r'\\cite\{([^}]+)\}',ns['comments_removed'](source)))
bib_keys = set(re.findall(r'\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}',BIB.read_text(encoding='utf-8')))
assert cites == old_cites and cites <= bib_keys, (cites,bib_keys)

# Recheck the arithmetic of reviewed numeric output, with means kept separate.
for arm,k,n,rounded in [('Mplus-30F',3849,8496,47.6),('Mplus-30',5121,8468,62.8)]:
    paired = nums['dispatcher']['paired'][arm]
    assert (paired['runs'],paired['forced'],paired['ack']) == (15,k,n)
    assert round(sum(100*x['forced']/x['ack'] for x in paired['raw_run_counts'])/15,1) == rounded
for x,expected in [(mb,39.0),(mf,11.0)]:
    assert sum(r['late30'] for r in x['per_run']) == x['late30']
    assert sum(r['served'] for r in x['per_run']) == x['served']
    assert round(sum(100*r['late30']/r['served'] for r in x['per_run'])/8,1) == expected
main = nums['main_original_obligation']['Mplus-30']
assert (main['forced'],main['ack'],main['positive_breach_scenarios']) == (7710,20103,28)
assert round(sum(100*x['forced']/x['ack'] for x in main['per_run'])/34,1) == 41.3
assert nums['test_attempt4']['passed'] == nums['test_attempt4']['total'] == 1025
assert nums['test_attempt4']['failed'] == 0

# Root rechecks the weekday historical share on independently extracted riders.
cx_path = WORK/'R19-stage1a-analysis.json'
cx = json.loads(cx_path.read_text(encoding='utf-8'))
active = [r for r in cx['runs'] if r['arm']=='C-30' and r['cell'][7:9] in ['14','15','16']]
late = [x for r in active for x in r['riders'] if x['arrival']-x['P0']>60000]
total_s = sum(x['arrival']-x['P0'] for x in late)/1000
history_s = sum(x['forecast_quote']-x['P0'] for x in late)/1000
weekday_ledger = {'scenarios':len(active),'late_naive_count':len(late),
                  'total_s':total_s,'historical_s':history_s,'historical_pct':100*history_s/total_s}
assert len(active)==21 and len(late)==68
assert abs(total_s-6217.406)<1e-6 and round(weekday_ledger['historical_pct'],1)==86.1
assert abs(history_s-float(json.loads((OUT/'agent-numbers-summary-v1.json').read_text(encoding='utf-8'))['forecast_ledger']['components_s']['anticipated']))<1e-6
raw = cx_path.read_bytes()
inputs[str(cx_path)] = {'sha256':hashlib.sha256(raw).hexdigest()}
linewidth_pt = 16/2.54*72.27
qa = {'changes':len(ordered),'unaffected_characters_preserved':unchanged_chars,'reverse_reconstruction':True,
      'float_contents_preserved':True,'old_counts':old_counts,'new_counts':new_counts,'syntax':checks,
      'references':refs,'distinct_ref_targets':len({x['target'] for x in refs}),'undefined':[],
      'duplicate_labels':duplicates,'labels_preserved':sorted(new_labels),'existing_citation_keys':sorted(cites),
      'inputs':inputs,'numeric_arithmetic_rechecked':True,
      'widths':{'linewidth_cm':16,'linewidth_pt':linewidth_pt,'table_scale_from_old_overflow':linewidth_pt/(linewidth_pt+29.17484),
                'figure_scale_from_old_overflow':linewidth_pt/(linewidth_pt+15.8002),'both_outer_widths':'linewidth'},
      'no_build':True,'weekday_ledger':weekday_ledger}

def cell(text):
    return '<code>' + html.escape(text.rstrip('\n')).replace('|','&#124;').replace('\n','<br>') + '</code>' if text else '— (chèn tại đây)'

rows = ['| # | Dòng v10 | Cũ | Mới | Bằng chứng / phạm vi |','|---:|---|---|---|---|']
for i,c in enumerate(ordered,1):
    where = str(c['first']) if c['first']==c['last'] else (f"Trước {c['first']}" if c['last']<c['first'] else f"{c['first']}–{c['last']}")
    rows.append(f"| {i} | {where} | {cell(c['old'])} | {cell(c['new'])} | {c['evidence']} |")
count_table = ['| Mục | Văn xuôi v10 | Văn xuôi v11 | Bảng/hình v11 | Δ văn xuôi |','|---|---:|---:|---:|---:|']
for old,new in zip(old_counts,new_counts):
    count_table.append(f"| {new['section']} | {old['prose']} | {new['prose']} | {new['floats']} | {new['prose']-old['prose']:+d} |")
old_total = sum(x['prose'] for x in old_counts)
new_total = sum(x['prose'] for x in new_counts)
float_total = sum(x['floats'] for x in new_counts)
count_table.append(f'| **Tổng** | **{old_total}** | **{new_total}** | **{float_total}** | **{new_total-old_total:+d}** |')
notes = (OUT/'CHANGES-template-v2.md').read_text(encoding='utf-8')
for marker,value in {
    '@@CHANGE_COUNT@@':str(len(ordered)),
    '@@COUNT_TABLE@@':'\n'.join(count_table),
    '@@CHANGE_ROWS@@':'\n'.join(rows),
    '@@TABLE_SCALE@@':f"{qa['widths']['table_scale_from_old_overflow']:.6f}",
    '@@FIGURE_SCALE@@':f"{qa['widths']['figure_scale_from_old_overflow']:.6f}",
    '@@REF_COUNT@@':str(len(refs)),
    '@@REF_TARGETS@@':str(qa['distinct_ref_targets']),
}.items():
    assert marker in notes, marker
    notes = notes.replace(marker,value)
assert '@@' not in notes

outputs = {'candidate-v2.tex':target,'candidate-CHANGES-v2.md':notes,
           'root-changes-data-v2.json':json.dumps(ordered,ensure_ascii=False,indent=2)+'\n',
           'root-qa-v2.json':json.dumps(qa,ensure_ascii=False,indent=2)+'\n'}
assert all(not (OUT/name).exists() for name in outputs)
for name,text in outputs.items():
    with (OUT/name).open('x',encoding='utf-8',newline='\n') as f:
        f.write(text)
print(json.dumps({'changes':len(ordered),'words':new_counts,'references':len(refs),'distinct_targets':qa['distinct_ref_targets'],'syntax':checks,'outputs':list(outputs)},ensure_ascii=False,indent=2))
