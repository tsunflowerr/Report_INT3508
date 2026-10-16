"""R36 targeted edits and static QA. Create-only small text outputs; no build.

All input files are read only. Original physical line numbers identify each
replacement; text outside those spans is reassembled unchanged.
"""
from pathlib import Path
import ast
import difflib
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
BASE = KIT / 'drafts/08-chuong4-phanA-v4.tex'
TEX = OUT / '08-chuong4-phanA-v5-v2.tex'
NOTES = OUT / '08-chuong4-phanA-v5-CHANGES-v2.md'
QA = OUT / 'root-qa-v2.json'
DIFF = OUT / '08-chuong4-phanA-v5-v2.diff'
for p in (TEX, NOTES, QA, DIFF):
    assert not p.exists(), f'Never overwrite: {p}'
source_bytes = BASE.read_bytes()
source = source_bytes.decode('utf-8-sig').replace('\r\n', '\n')
lines = source.splitlines(keepends=True)
changes = []


def edit(first, last, new, reason, evidence):
    old = ''.join(lines[first-1:last])
    assert old != new
    changes.append(dict(first=first, last=last, old=old, new=new,
                        reason=reason, evidence=evidence))


edit(2, 9, r'''% Chương 4, PHẦN A (mở chương, mục 4.1–4.5) — bản sửa v5 (2026-10-13), BẢN DÙNG ĐỂ GHÉP.
% Sửa có mục tiêu từ drafts/08-chuong4-phanA-v4.tex theo R34-CH4A-V4-VERIFY-CODEX-v2.md và brief R36.
% Quyết định trước: reviews/CH4A-REVISION-LOG-v2.md; ghi chú cũ: drafts/08-chuong4-phanA-v2-NOTES.md.
% Bản v4 và mọi bản trước giữ nguyên. Tệp tiếp tục R36: 08-chuong4-phanA-v5-v2.tex;
% từng thay đổi, bằng chứng mới và việc bàn giao: 08-chuong4-phanA-v5-CHANGES-v2.md. Phần B v10 nối sau tệp này.
% Mỗi dòng "% EV:" trỏ tới EVIDENCE-REGISTER.md (A01…K52), các phụ lục 1 (N-xx, L1a-xx), 2 (X3-xx),
% 4 (C4A-xx), 6 (N4B8-xx), hoặc sổ bổ sung R36-A01…03 trong tệp CHANGES-v2.md bên cạnh.
% Không dùng gói mới: TikZ và array đã nạp trong main.tex; chỉ sửa độ rộng các bảng được brief chỉ ra.
''', 'Thông tin bản sửa, nhật ký quyết định đúng và sổ bằng chứng cục bộ.',
     'R34 §7.9; ROUND36-CH4A-V5-APPLY.md; main.tex:17,25.')

edit(66, 66, lines[65].replace('Thế giới mô phỏng', 'Mô phỏng'),
     'Bỏ thuật ngữ đã loại theo addendum.', 'Addendum R36 ý 2; B-v8-NOTES §8.2; GLOSSARY-VI-v2 §E.')

edit(101, 101, lines[100].replace('A24; ', ''),
     'Bỏ anchor cũ mâu thuẫn về giới hạn của cả lô yêu cầu.',
     'R34 §7.9; X3-32 (GEN:54–96); giữ X3-17 và C4A-18.')

edit(106, 109, r'''Chương này dùng bốn tập kịch bản (Bảng~\ref{bang:c4-taptu}). Từ các ngày 14--18/11/2018 dựng được 49 kịch bản, chia
theo cặp ngày và mẫu để ba khung giờ của một cặp nằm cùng một phía. 34 kịch bản làm tập kiểm tra chính; 15 kịch bản
còn lại không dùng để tính các kết quả phục vụ và đúng giờ của chương này. Các lần chạy trên 15 kịch bản đó chỉ tham
gia phép kiểm tính nhất quán của sổ ở mục~\ref{muc:kiemtra}. Ngày 14--16/11 là ngày thường, 17 và 18/11 là cuối tuần.
% EV: B08 (SPLIT: chia theo nhóm ngày, mẫu); C17 (15 kịch bản hiệu chỉnh khoảng dự phòng γ); B09; B21 (11/11/2018 là Chủ nhật); A26; RUN38; T38:99-106; chương 3 v4-v3:725-727 (185 lần chạy gồm 15 lần hiệu chỉnh)
''', 'Thu hẹp loại trừ dữ liệu hiệu chỉnh đúng phạm vi kết quả phục vụ/đúng giờ.',
     'R34 §7.3; Ch3 v4-v3:725–727; RUN38:9–10; T38:99–106; agent-consistency-v2-output.txt.')

edit(118, 118, '\\setlength{\\tabcolsep}{2.5pt}\n',
     'Thu bảng tập thử dưới bề rộng 16 cm, giữ nguyên các cột và nội dung.',
     'Addendum R36 ý 6; trial main.log:1751 (1,54718 pt); main.tex:28.')

edit(135, 136, r'''Như tập chính & 8\\
% EV: B20; N-26 (8 lần chạy C-30, 601 khách được phục vụ); C4A-06 (864 = 8 × 108, INV:14-15,17-22); N4B8-05 (CK8:65-72); R26 §Q8; agent-numeric-output-v2.txt (manifest, cấu hình phục hồi và DLL)
''', 'Thay lưu ý chưa kiểm bộ chạy chiều tuyết bằng kết quả đã kiểm.',
     'Addendum R36 ý 1; N4B8-05; CK8:65–72; R26 §Q8; agent-numeric-output-v2.txt.')

edit(141, 145, r'''Bản đã lưu là bản bộ chạy biên dịch và lưu lại, dùng chung cho tập kiểm tra chính, tập buổi sáng, các lần chạy trần
120 giây và chiều tuyết; bản cũ chưa có luật phục hồi (mục~\ref{muc:doichung}, \ref{muc:kiemtra}). Trừ ghép tự do, mọi
cấu hình dùng cùng bộ sinh, bộ kiểm và bộ chọn với luật C; điều phối không trần chỉ khác luật C trần 30 giây ở trần giờ
trả. Ghép tự do không khóa gì và không qua bộ kiểm cam kết.
% EV: A28; X3-10 (RW7:1-8; RW7X:6-8; R120:3-8); N4B8-05 (CK8:65-72); R26 §Q8; B17; NEW:13 (bộ chạy cũ không có commitmentRecovery); A08; H01; A17; K50; X3-38 (HO:109, b1-rolling-cost)
''', 'Bổ sung chiều tuyết vào danh sách dùng chung bản bộ chạy và bỏ lưu ý đã hết hiệu lực.',
     'Addendum R36 ý 1; N4B8-05; R26 §Q8; agent-numeric-output-v2.txt; Ch3 v4-v3:496–498,733–735.')

edit(161, 164, r'''Lời hứa đầu là giờ trả của kế hoạch lúc khách xác nhận đặt xe, tính với thời gian đi lúc đó. Tính từ lúc gọi xe, độ dài
trung bình của lời hứa là 14,15 phút trên 2.434 khách khi không trần và 14,12 phút trên 2.338 khách dưới luật C trần 30
giây, gộp theo khách được phục vụ. Hai giá trị trung bình gần nhau trên hai tập khách khác nhau; phép so này không nói
về độ dài lời hứa của từng khách.
% EV: A13; A05; B14 (BURD:5,11); R36-A03 (p0 trừ request.arrivalTimeMs, gộp theo khách); agent-numeric-output-v2.txt
''', 'Nêu mốc lúc gọi xe, mẫu số và giới hạn suy luận về hai trung bình.',
     'R34 §7.6; B14; MAIN:128–129; R36-A03; agent-numeric-output-v2.txt (68 checkpoint cuối).')

edit(206, 207, r'''(mục~\ref{muc:doichung}) & Chia cho số lượt quyết định đã được bộ mô phỏng xác nhận áp dụng; gộp theo
lượt quyết định, mỗi lượt đếm một lần & Luật có tự giữ được nghĩa vụ không\\
''', 'Định nghĩa cách gộp khớp bảng nghĩa vụ chuyển sang số đếm.',
     'R34 §7.2; C4A-10; X3-30; R36-A01.')

edit(209, 210, r'''$a - p_0 > B$; luật trần độ dời khách thấy: $\sum|z| > B$ & Chia cho số khách được phục vụ; gộp theo
khách & Luật có giữ được điều nó hứa không\\
''', 'Mẫu số của khách bị phá lời hứa khớp cách gộp đã chọn.',
     'R34 §7.2; N-21; R36-A01.')

edit(231, 231, lines[230].replace('các phép sàng lọc ở 120 giây', 'các phép tính thử ở 120 giây'),
     'Phân biệt phép tính thử trần với phép sàng lọc bộ chọn ở phần B.',
     'Addendum R36 ý 3; B-v8-NOTES §8.3; C4A-11; B-v10:24–29.')

edit(261, 265, r'''\small
\setlength{\tabcolsep}{4pt}
\begin{tabular}{@{}p{\dimexpr .12\linewidth-2\tabcolsep\relax}
>{\raggedleft\arraybackslash}p{\dimexpr .13\linewidth-2\tabcolsep\relax}
>{\raggedleft\arraybackslash}p{\dimexpr .16\linewidth-2\tabcolsep\relax}
>{\raggedleft\arraybackslash}p{\dimexpr .22\linewidth-2\tabcolsep\relax}
>{\raggedleft\arraybackslash}p{\dimexpr .23\linewidth-2\tabcolsep\relax}
>{\raggedleft\arraybackslash}p{\dimexpr .14\linewidth-2\tabcolsep\relax}@{}}
\toprule
\textbf{Cấu hình} & \textbf{Phục vụ} & \textbf{Trễ quá 60 s} & \textbf{Không trễ quá 60 s} &
\textbf{Không trễ quá 120 s} & \textbf{Khách đi chung}\\
''', 'Giới hạn bề rộng bảng chính bằng cột tự xuống dòng; mọi tiêu đề và ô giữ nguyên.',
     'Addendum R36 ý 6; trial main.log:1817 (33,99846 pt); array đã nạp ở main.tex:17.')

edit(302, 305, r'''\caption{Nghĩa vụ của chính từng luật trên tập kiểm tra chính (34 kịch bản). Hai cột đầu ghi số đếm gộp: số quyết
định bị ép trên số quyết định được xác nhận, và số khách bị phá lời hứa trên số khách được phục vụ. Cột cuối ghi số
kịch bản có ít nhất một khách bị phá lời hứa trên 34 kịch bản. Định nghĩa ở Bảng~\ref{bang:c4-chiso}. Ở hàng luật C,
các số 0 là số đo trên tập đã chạy, phù hợp với tính chất có điều kiện ở Nhận xét~\ref{nx:giunguyen}.}
''', 'Chú thích phân biệt số đếm gộp với trung bình theo kịch bản; số 0 là quan sát phù hợp tính chất có điều kiện.',
     'R34 §7.1–2; R36-A01; Ch3 v4-v3:371–390.')

edit(307, 317, r'''\small
\setlength{\tabcolsep}{4pt}
\begin{tabular}{@{}p{\dimexpr .12\linewidth-2\tabcolsep\relax}
>{\raggedleft\arraybackslash}p{\dimexpr .28\linewidth-2\tabcolsep\relax}
>{\raggedleft\arraybackslash}p{\dimexpr .31\linewidth-2\tabcolsep\relax}
>{\raggedleft\arraybackslash}p{\dimexpr .29\linewidth-2\tabcolsep\relax}@{}}
\toprule
\textbf{Cấu hình} & \textbf{Quyết định bị ép / được xác nhận} &
\textbf{Khách bị phá lời hứa / được phục vụ} &
\textbf{Kịch bản có khách bị phá / tổng kịch bản}\\
\midrule
C-30 & 0 / 20.101 & 0 / 2.338 & 0 / 34\\
M$^{+}$-30 & 7.710 / 20.103 & 289 / 2.338 & 28 / 34\\
M$^{+}$-60 & 4.031 / 20.163 & 79 / 2.347 & 22 / 34\\
V-30 & 10.442 / 20.090 & 456 / 2.336 & 34 / 34\\
''', 'Thay bốn hàng phần trăm thiếu cặp đếm bằng số đếm có mẫu số; khai báo rõ cách gộp.',
     'R34 §7.2 (phương án ngắn); R36-A01; agent-numeric-output-v2.txt (170 tệp IVC).')

edit(321, 321, '% EV: R36-A01 (sổ bổ sung trong CHANGES-v2.md; 170 tệp IVC và đối chiếu PAIRS); N-21; X3-30; A22\n',
     'Đăng ký và dẫn trực tiếp các tổng mới; không gán chúng cho một mã sổ cũ không có.',
     'R34 §7.2; R36-A01; agent-numeric-output-v2.txt.')

edit(323, 325, r'''Cách đọc bảng: luật hạn chót 30 giây có 7.710 trong 20.103 lượt quyết định bị ép và 289 trong 2.338 khách tới muộn
hơn lời hứa đầu quá 30 giây; những khách này nằm ở 28 trong 34 kịch bản.
% EV: N-21; R36-A01
''', 'Câu đọc bảng theo số đếm gộp, không giữ tỉ lệ trung bình cũ.', 'R34 §7.2; N-21; R36-A01.')

edit(327, 332, r'''Trên cả 34 kịch bản đã chạy, luật C không có quyết định bị ép và không khách nào vượt trần. Theo Nhận
xét~\ref{nx:giunguyen}, nếu giả thiết (N) đúng ở lượt đang xét và mọi khách có lời hứa của xe có $0 \le L_r \le B$,
phương án giữ nguyên không thêm phần dời do điều phối nên vẫn qua kiểm tra trần. Khi (N) đúng ở mọi lượt, trần được
giữ từ lúc xác nhận. Các số đo ở đây phù hợp với tính chất đó; nhận xét không bảo đảm giờ trả thực tế. Điều phối không
trần cũng có 0 trong 20.760 quyết định bị ép. Luật hạn chót so giờ trả mới với lời hứa đầu, nên phần thay đổi khi giữ
nguyên kế hoạch vẫn có thể làm xe bị ép (mục~\ref{muc:doichung}).
% EV: A21; A22; N-21; X3-16 (U 0 / 20.760); X3-30; A10; K05; Ch3 v4-v3:371-390; R36-A01
''', 'Khôi phục điều kiện sổ hợp lệ ở lượt đang xét và (N) ở mọi lượt; tách số đo khỏi hệ quả có điều kiện.',
     'R34 §7.1; Ch3 v4-v3:371–390; A22; R36-A01.')

edit(334, 340, r'''Tính gộp, luật hạn chót 30 giây bị ép ở 7.710 trong 20.103 lượt quyết định (38,4\%) và phá lời hứa với 289 trong 2.338
khách (12,4\%). Gánh nặng dồn vào khung 7 giờ: cả 9 kịch bản có khách bị phá lời hứa, với 181 trong 509 khách được phục
vụ và 3.447 trong 4.564 lượt quyết định bị ép. Ở khung 17 giờ, 5 trong 11 kịch bản có khách bị phá, với 8 trong 852
khách và 328 trong 7.163 lượt quyết định bị ép. Các số này được gộp theo từng khung giờ. Ở mức 60 giây, các tỉ lệ toàn
tập giảm nhưng không về 0. Luật trần độ dời khách thấy bị ép nhiều nhất, phù hợp với định nghĩa: tổng độ lớn các lần
cập nhật mà nó kiểm không nhỏ hơn độ lùi so với lời hứa đầu (công thức~\eqref{eq:dongnhat}).
% EV: N-21 (gộp 7.710/20.103 và 289/2.338); R36-A02 (cặp đếm theo khung giờ, sổ bổ sung trong CHANGES-v2.md); C14; C13; R36-A01; A11; A12; X3-33 (eq:dongnhat: Σ|z| ≥ |Σz| = |p_n − p_0|)
''', 'Thay trung bình theo khung giờ thiếu tử số bằng cặp đếm và nêu cách gộp.',
     'R34 §7.2; R36-A02; agent-numeric-output-v2.txt; đối chiếu SUPP:17–19.')

edit(344, 347, r'''hứa đầu quá 30 giây, luật C có 292 trong 2.338 khách (12,5\%), so với 289 khách (12,4\%) của luật hạn chót. Cả hai
luật đều có khách tới muộn hơn lời hứa đầu quá 30 giây ở 28 trong 34 kịch bản. Vậy về độ đúng giờ, hai luật gần như
ngang nhau; luật C khác ở chỗ chỉ hứa phần mà bộ điều phối kiểm soát được, nên giữ được lời hứa đó.
% EV: C13; K05; C4A-01 (C-30 292/2.338 = 12,49%, 28/34); N-21; R36-A01
''', 'Bỏ hai trung bình không có cặp đếm, giữ cặp gộp và bổ sung 28 trên 34.',
     'R34 §7.2; C4A-01; N-21; R36-A01.')

edit(435, 438, r'''dời lớn nhất của một khách là 29,2 giây ở trần 30 giây và 116,5 giây ở trần 120 giây. Trên 8 kịch bản chiều tuyết,
8 trong 601 khách được phục vụ bị dời, lớn nhất 25,2 giây; không ai vượt trần và không quyết định nào bị ép trong
5.067 lượt.
% EV: F03; X3-11 (D chỉ tính sau khi chạy); N-28; N-26 (thay anchor F13 của RD §8 mục 4, ADDENDUM-1 mục 0.4); N4B8-05 (CK8:65-72); R26 §Q8
''', 'Bỏ lưu ý bộ chạy chiều tuyết chưa kiểm; giữ nguyên tất cả số đo.',
     'Addendum R36 ý 1; N4B8-05; R26 §Q8; N-26.')

edit(444, 446, r'''ở đúng ba chỗ cùng kiểu, ở mức 90 hoặc 120 giây; mỗi chỗ luật C nhận thêm một khách. Đây là phép so hai luật trên
giờ trả dự kiến tại cùng một trạng thái của mô hình, không phải phép đo nhân quả.
% EV: D05 (79,0 + 68,3 s; 60,9 + 61,2 s); C4A-12 (W07XM:6,11,16: "sum x 79.0, sum c 0.0, p_last − p_first 79.0", c = 68,3 s, x = 0,1 s; W07X:54-62: "khách đang có", giai đoạn chờ đón hay trên xe không ghi); K04
''', 'Khôi phục phạm vi so hai luật tại cùng trạng thái dự kiến.', 'R34 §7.7; D05; C4A-12 (W07XM:6,11,16).')

edit(453, 454, lines[452] + 'Các số đếm theo yêu cầu trong đoạn này tính theo từng cặp kịch bản và yêu cầu.\n' + lines[453],
     'Nêu khóa đếm kịch bản/yêu cầu của nhóm từ chối và bản ghi chặn.',
     'R34 §7.7; D13; D16; C4A-09 (BUDPY:29–44); BUDPY.')

edit(546, 549, r'''không trễ quá 60 giây. Luật C không có quyết định bị ép trong 64 lần chạy của tám mức trần này. Ở cả tám mức, hai
luật phục vụ chênh nhau không quá 2 lượt.
% EV: D01; K12; D03 (+6 / +4 / +2); D04; X3-28 (tám mức 30–300 s); E01 (64 lần C, 0 bị ép); agent-numeric-output-v2.txt (0 / 44.270 lượt quyết định)
''', 'Bỏ dãy trung bình thiếu cặp đếm; giữ kết luận có số lần chạy xác định.',
     'R34 §7.2; E01; D04; A-v4:719; agent-numeric-output-v2.txt (64 transcript buổi sáng).')

edit(712, 716, r'''\small
\setlength{\tabcolsep}{4pt}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{\dimexpr .38\linewidth-2\tabcolsep\relax}
>{\raggedleft\arraybackslash}p{\dimexpr .11\linewidth-2\tabcolsep\relax}
>{\raggedleft\arraybackslash}p{\dimexpr .16\linewidth-2\tabcolsep\relax}
>{\raggedleft\arraybackslash}p{\dimexpr .16\linewidth-2\tabcolsep\relax}
>{\raggedleft\arraybackslash}p{\dimexpr .19\linewidth-2\tabcolsep\relax}@{}}
\toprule
\textbf{Lần chạy} & \textbf{Số lần chạy} & \textbf{Bản ghi chặn} & \textbf{Chỉ do cộng dồn} &
\textbf{Khách phục vụ bị dời từ hai lần}\\
''', 'Thu bảng kiểm bản ghi chặn bằng cột tự xuống dòng; giữ nguyên tiêu đề và ô số.',
     'Addendum R36 ý 6; trial main.log:1827 (60,8016 pt); main.tex:17,28.')

edit(724, 724, lines[723].replace('X3-10 (bộ chạy chưa kiểm)', 'N4B8-05 (bộ chạy chiều tuyết đã kiểm, CK8:65-72); R26 §Q8'),
     'Xóa thêm lưu ý chiều tuyết hết hiệu lực trong EV của bảng cộng dồn.',
     'Addendum R36 ý 1; N4B8-05; R26 §Q8.')

ordered = sorted(changes, key=lambda c: c['first'])
assert all(a['last'] < b['first'] for a, b in zip(ordered, ordered[1:]))
parts, cursor = [], 0
for c in ordered:
    parts.append(''.join(lines[cursor:c['first']-1]))
    parts.append(c['new'])
    cursor = c['last']
parts.append(''.join(lines[cursor:]))
target = ''.join(parts)

# Import only reviewed pure counting/syntax functions; never execute the R33
# patch script or its output-writing top-level statements.
counter_path = WORK / 'r33-ch3v4/patch_and_check-v3.py'
tree = ast.parse(counter_path.read_text(encoding='utf-8-sig'))
names = {'comments_removed', 'brace_arg', 'figure_words_text', 'count_words', 'counts', 'latex_checks'}
namespace = {'re': re}
pure = ast.Module(body=[n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name in names], type_ignores=[])
assert len(pure.body) == len(names)
exec(compile(pure, str(counter_path), 'exec'), namespace)
old_counts = namespace['counts'](source)
new_counts = namespace['counts'](target)
assert len(old_counts) == len(new_counts) == 6
for count_list in (old_counts, new_counts):
    for i, row in enumerate(count_list):
        row['section'] = 'Mở chương' if i == 0 else f'4.{i}'
old_prose = sum(r['prose'] for r in old_counts)
new_prose = sum(r['prose'] for r in new_counts)
old_visible = sum(r['prose']+r['floats'] for r in old_counts)
new_visible = sum(r['prose']+r['floats'] for r in new_counts)
print(json.dumps(dict(change_count=len(changes), old_counts=old_counts, new_counts=new_counts,
                     prose_growth_percent=100*(new_prose/old_prose-1),
                     visible_growth_percent=100*(new_visible/old_visible-1)), ensure_ascii=False, indent=2))
assert new_prose <= old_prose * 1.03, 'Running-text growth exceeds 3%'
assert new_visible <= old_visible * 1.03, 'All-visible-text growth exceeds 3%'
base_checks = namespace['latex_checks'](source)
target_checks = namespace['latex_checks'](target)
assert base_checks['labels'] == target_checks['labels']
assert base_checks['references'] == target_checks['references']
assert base_checks['cite_keys'] == target_checks['cite_keys']
clean = namespace['comments_removed'](target)
for phrase in ('niêm phong','tiền đăng ký','preregistration','dự đoán trước','kết quả mong đợi',
               'duy nhất','đầu tiên','vượt trội','tối ưu','đột phá','chúng tôi','phải phục hồi',
               'Thế giới','các phép sàng lọc ở 120 giây','không dùng trong khóa luận'):
    assert phrase.casefold() not in clean.casefold(), phrase
assert not re.search(r'chiều tuyết.{0,120}chưa kiểm|bộ chạy chiều tuyết chưa kiểm', target, re.S)
assembly = {
    'A-v5-v2': target,
    'Ch1-v3': (WORK/'r30-ch1/05-chuong1-v3.tex').read_text(encoding='utf-8-sig'),
    'Ch2-v4': (KIT/'drafts/06-chuong2-v4.tex').read_text(encoding='utf-8-sig'),
    'Ch3-v4-v3': (WORK/'r33-ch3v4/07-chuong3-v4-v3.tex').read_text(encoding='utf-8-sig'),
    'B-v10': (KIT/'drafts/09-chuong4-phanB-v10.tex').read_text(encoding='utf-8-sig'),
    'Appx-v2': (WORK/'r31-ch5/11-phuluc-v2.tex').read_text(encoding='utf-8-sig'),
}
label_sources = {}
for name, text in assembly.items():
    for label in re.findall(r'\\label\{([^{}]+)\}', namespace['comments_removed'](text)):
        label_sources.setdefault(label, []).append(name)
assert not [k for k, owners in label_sources.items() if len(owners) > 1]
assert all(ref in label_sources for ref in target_checks['references'])
paired_refs = {}
for name in ('B-v10','Ch3-v4-v3'):
    paired_refs[name] = sorted(set(re.findall(r'\\(?:eqref|ref)\{(bang:c4-[^{}]+|hinh:c4-[^{}]+|muc:c4-[^{}]+)\}', assembly[name])))
    assert all(ref in label_sources for ref in paired_refs[name])
bib = (WORK/'r32-bib/10-tai-lieu-draft.tex').read_text(encoding='utf-8-sig')
assert all(re.search(r'\\bibitem(?:\[[^\]]*\])?\{'+re.escape(key)+r'\}', bib) for key in target_checks['cite_keys'])
numeric_path = OUT/'agent-numeric-output-v2.txt'
assert numeric_path.exists(), 'Fresh numerical verification must finish before delivery'
numeric = numeric_path.read_text(encoding='utf-8-sig')
confirm = (OUT/'agent-numeric-confirm-output-v2.txt').read_text(encoding='utf-8-sig')
supplement = (OUT/'agent-numeric-supplement-output-v2.txt').read_text(encoding='utf-8-sig')
assert 'CONFIRM_CHECK PASS' in confirm and 'CHECK PASS' in supplement
assert (OUT/'agent-numeric-report-v2.md').exists()
# Initial numeric probe failed only its stale denominator expectation; confirmed independently.

assert BASE.read_bytes() == source_bytes

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

table_widths = {
    'scenario-set': dict(column_cm=15, intercolumn_spaces=10, tabcolsep_pt=2.5,
                         width_cm=15+25/72.27*2.54, available_cm=16),
    'main-results': dict(fractions=[.12,.13,.16,.22,.23,.14], columns=6),
    'obligations': dict(fractions=[.12,.28,.31,.29], columns=4),
    'cumulative': dict(fractions=[.38,.11,.16,.16,.19], columns=5),
}
for key, row in table_widths.items():
    if 'fractions' in row:
        assert abs(sum(row['fractions'])-1) < 1e-9
        row['outer_width'] = 'linewidth - 2 tabcolsep = linewidth - 8 pt'
assert table_widths['scenario-set']['width_cm'] < 16


def cell(text):
    return '<code>' + html.escape(text.strip()).replace('|','&#124;').replace('\n','<br>') + '</code>'


notes = [
    '# Round 36 — Chương 4 phần A v5, tiếp tục v2',
    '',
    f'**Bản giao: `08-chuong4-phanA-v5-v2.tex`; {len(changes)} thay đổi có phạm vi dòng xác định.** '
    'Áp R34 v2 và addendum 13/10/2026. Tên `-v2` theo yêu cầu tiếp tục; không ghi đè, '
    'không sửa đầu vào, phần B hay chương khác. Không có tệp R36 trước đó khi kiểm thư mục.',
    '',
    '`S` = `E:/Code/Report_INT3508/ridebound-scratchpad/`; `K` = `S/rewrite-2026-10/`; '
    '`W` = `S/optimize/codex-debate/codex-work/`. Dòng dưới đây là dòng vật lý, bắt đầu từ 1, của A-v4.',
    '',
    '## 1. Độ dài và bố cục',
    '',
    'Đếm “tiếng” bằng các hàm thuần đã đọc của `W/r33-ch3v4/patch_and_check-v3.py`: bỏ comment, '
    'lệnh và đối số cấu trúc, công thức nội dòng; đếm token có chữ/số cách nhau bằng khoảng trắng. '
    'Văn xuôi tách khỏi bảng/hình; chú thích thuộc khối bảng/hình, tiêu đề mục không tính. '
    'Dùng cùng bộ đếm cho cả hai bản; đây không phải bộ đếm thất lạc đã cho 4.522 tiếng trong NOTES cũ.',
    '',
    '| Mục | Văn xuôi v4 | Văn xuôi v5-v2 | Bảng/hình v4 | Bảng/hình v5-v2 | Δ văn xuôi |',
    '|---|---:|---:|---:|---:|---:|',
]
for old, new in zip(old_counts, new_counts):
    notes.append(f"| {old['section']} | {old['prose']} | {new['prose']} | {old['floats']} | {new['floats']} | {new['prose']-old['prose']:+d} |")
notes += [
    f'| **Tổng** | **{old_prose}** | **{new_prose}** | **{old_visible-old_prose}** | **{new_visible-new_prose}** | **{new_prose-old_prose:+d}** |',
    '',
    f'Văn xuôi tăng **{100*(new_prose/old_prose-1):.2f}%**; toàn bộ chữ nhìn thấy tăng '
    f'**{100*(new_visible/old_visible-1):.2f}%** ({old_visible} → {new_visible}). Cả hai dưới 3%. '
    'Giữ 12 bảng, 1 hình và cấu trúc 4.1–4.5. Ngân sách brief khoảng 13,5 trang; NOTES v4 ước '
    '13,0–14,4 trang. Chưa đo số trang của v5-v2.',
    '',
    'Đã đọc `C:/RideBoundData/research/thesis-trial-build-2026-10-13/main.log`: '
    'dòng 1751/1817/1827 xác nhận ba bảng A-v4 vượt 1,54718/33,99846/60,8016 pt. '
    'Bảng tập thử giữ tổng cột 15 cm, giảm `tabcolsep` từ 3 xuống 2,5 pt: '
    f"rộng {table_widths['scenario-set']['width_cm']:.4f} cm, dưới bề rộng 16 cm của `main.tex:28`. "
    'Bảng chính và cộng dồn dùng cột `p` theo `linewidth`, tổng bề rộng ngoài bằng '
    '`linewidth − 8 pt`; bảng nghĩa vụ chuyển cách báo cũng dùng công thức đó. '
    'Nội dung ba bảng được chỉ ra trong addendum không đổi. Gói `array` đã nạp (`main.tex:17`). '
    'Đây là kiểm tra bề rộng khai báo, chưa phải xác nhận không còn overfull trong bản dựng. '
    'Luật song song cấm build; người ghép cần dựng kiểm lại số trang và xuống dòng trong ô.',
    '',
    '## 2. Sổ bằng chứng bổ sung R36',
    '',
    'Các mã dưới đây được định nghĩa thật tại đây, không giả làm mã của sổ chính. '
    'Tổng mới của M⁺-60/V-30 và cặp theo khung được đăng ký trước khi giao; registrar có thể '
    'chuyển nguyên hàng vào addendum kế tiếp. Script và output `agent-numeric-v2*` chỉ đọc nguồn. '
    'Root đã đọc mã, kết quả, kiểm lại phép gộp và đối chiếu R34; xem `root-qa-v2.json`.',
    '',
    '| ID | Giá trị, cách gộp | Nguồn đã đọc / phép kiểm lại |',
    '|---|---|---|',
    '| R36-A01 | 34 kịch bản mỗi cấu hình. C-30: bị ép 0/20.101 quyết định, phá 0/2.338 khách, 0/34 kịch bản. M⁺-30: 7.710/20.103, 289/2.338, 28/34. M⁺-60: 4.031/20.163, 79/2.347, 22/34. V-30: 10.442/20.090, 456/2.336, 34/34. U: bị ép 0/20.760. Tất cả là số đếm gộp. | `agent-numeric-v2.py`, `agent-numeric-output-v2.txt`: đọc mới 170 tệp IVC chọn theo test split; đối chiếu `W/r34-ch4a-verify/main-obligations-v4.tsv`, `main-numbers-v4.txt:7–23`. N-21/X3-16 cho các tổng đã có. |',
    '| R36-A02 | M⁺-30 theo khung giờ: 7 giờ có 181/509 khách bị phá, 3.447/4.564 quyết định bị ép, 9/9 kịch bản có khách bị phá; 17 giờ có 8/852, 328/7.163, 5/11. Số đếm gộp riêng theo khung; không gắn cặp gộp vào trung bình cũ. | `agent-numeric-output-v2.txt` (IVC mới); đối chiếu `W/r34-ch4a-verify/root-supplement-output-v2.txt:17–19` và TSV 170 hàng. |',
    '| R36-A03 | Độ dài lời hứa đầu tính từ lúc gọi xe: U 2.065.946.452 ms / 2.434 / 60.000 = 14,14644243 phút → 14,15; C-30 1.980.192.800 ms / 2.338 / 60.000 = 14,11600228 phút → 14,12. Gộp theo khách được phục vụ, hai tập khách khác nhau. | `agent-numeric-output-v2.txt`: 68 checkpoint cuối, `p0 − request.arrivalTimeMs`; B14/BURD:5,11; MAIN:128–129. |',
    '',
    'Bộ chạy chiều tuyết: đã kiểm R26 §Q8; N4B8-05; '
    '`K/evidence/checks-ch4b-v8/ch4b-v8-check-2026-10-12.txt:65–72`; '
    '`agent-numeric-output-v2.txt` đọc lại 8 manifest, binding cấu hình, DLL đã lưu. '
    'Cùng bản bộ chạy đã lưu và luật phục hồi không tệ hơn. Các số 8/601, 25,2 giây, '
    '0/5.067 quyết định, 163 bản ghi giữ nguyên (N-26); không biến kiểm binary thành bằng chứng '
    'chạy lại mô phỏng cho kết quả cũ.',
    '',
    '## 3. Một hàng cho mỗi thay đổi',
    '',
    '| # | Dòng A-v4 | Cũ | Mới | Lý do, bằng chứng |',
    '|---:|---|---|---|---|',
]
for i, c in enumerate(ordered, 1):
    span = str(c['first']) if c['first'] == c['last'] else f"{c['first']}–{c['last']}"
    notes.append(f"| {i} | {span} | {cell(c['old'])} | {cell(c['new'])} | {c['reason']} {c['evidence']} |")
notes += [
    '',
    '## 4. Đối chiếu đủ chín sửa bắt buộc của R34 v2',
    '',
    '| R34 §7 | Xử lý R36 |',
    '|---|---|',
    '| 1 — điều kiện giữ nguyên | Sửa chú thích bảng và đoạn A327–332; đủ (N), 0 ≤ Lr ≤ B, (N) ở mọi lượt và giới hạn giờ trả thực tế. |',
    '| 2 — số đếm/mẫu số | Dùng phương án bảng gộp có cặp đếm; sửa định nghĩa gộp, câu đọc bảng, khung giờ, 28/34; bỏ dãy trung bình buổi sáng thiếu cặp. Đăng ký tổng mới R36-A01/02. |',
    '| 3 — hiệu chỉnh | Thu hẹp câu A106–109; 15 lần chỉ tham gia kiểm nhất quán sổ, không tham gia số phục vụ/đúng giờ. |',
    '| 4 — tiết lộ 120 s ở B | B-v10:421–423 đã nói chọn 120 giây sau khi xem tập chính, nhưng còn thiếu mệnh đề kể cả phép tính thử ở 120 giây; bàn giao bổ sung ở mục 5. Giữ tiết lộ đầy đủ trong A. |',
    '| 5 — ba nhãn ngoài A | Cả ba có target thật trong bản Ch1/phụ lục mới; giữ tham chiếu, không tạo nhãn rỗng hay dùng câu fallback. Chi tiết mục 5. |',
    '| 6 — suy luận lời hứa | Sửa A161–164 theo trung bình gộp, mẫu số và mốc lúc gọi xe; bỏ kết luận cho từng khách. |',
    '| 7 — phạm vi ví dụ/khóa đếm | Sửa A444–446, thêm khóa đếm sau A453. Không thêm câu 116/96 vì review ghi tùy chọn. |',
    '| 8 — phần B | Tên bị ép và tương phản chỉ trần đã sửa trong B-v10; residual trung bình/cross-reference bàn giao ở mục 5. |',
    '| 9 — provenance | Bỏ A24 tại A101, sửa đường dẫn nhật ký ở đầu A; bình luận tên ghép A của B bàn giao. |',
    '',
    'Addendum: áp kiểm bộ chạy chiều tuyết ở cả thân và EV; bỏ “Thế giới”; đổi “phép sàng lọc” của A '
    'thành “phép tính thử”; A không có câu kiểm thử để sửa; kiểm đủ nhãn của B-v10; sửa bề rộng ba bảng, giữ chữ và số.',
    '',
    '## 5. Việc thuộc phần B và chương khác (không sửa tệp của họ)',
    '',
    '**Phần B v10.** Các dòng là dòng vật lý của `K/drafts/09-chuong4-phanB-v10.tex` đã đọc trong vòng này:',
    '',
    '- **B286–287:** vẫn nêu 41,3% trung bình và trỏ `bang:c4-nghiavu`; bảng A nay báo số đếm gộp. '
    'Thay đoạn tương ứng bằng: `Khác biệt là bộ điều phối của luật hạn chót có 7.710 trong 20.103 lượt quyết định bị ép '
    'và có khách tới muộn hơn lời hứa đầu không dự báo quá 30 giây ở 28 trong 34 kịch bản, còn luật C không có quyết định '
    'bị ép (Bảng~\\ref{bang:c4-nghiavu}). Các bộ đếm này thuộc các lần chạy gốc; việc phát lại lời hứa theo dự báo không đổi chúng.` '
    'Bằng chứng R36-A01/N-21; đây là câu thay của R34 §7.8, phù hợp bảng A đã chọn.',
    '- **B184–185:** 47,6%/62,8% và 39,0%/11,0% ở phép thử đưa dự báo vào bộ điều phối vẫn chỉ có trung bình theo 15 kịch bản; '
    'cần cặp đếm thành phần hoặc chuyển hẳn sang số gộp được kiểm. Không gắn một cặp gộp vào hai trung bình ấy. '
    'R34 §7.8; B-v8-NOTES §9.8 nói 3.849/8.496 và 5.121/8.468 chưa được người sửa B kiểm; '
    'các tổng B-only đó chưa được R36 chứng nhận.',
    '- **B360:** khi viện Nhận xét giữ nguyên, thêm sổ hợp lệ `0 \\le L_r \\le B` ở lượt đang xét và '
    'giả thiết (N) ở mọi lượt cho kết luận xuyên chuyến; xem Ch3 v4-v3:371–390 và A-v5-v2.',
    '- **B381–384:** thay kết quả 1.024/1.025 cộng kiểm riêng bằng **1.025/1.025 trong một lần chạy đầy đủ ngày 13/10/2026**, '
    'vẫn giữ hai điều kiện LF và tệp chưa ghi nhận. `K/evidence/TESTRUN-45f8026-2026-10-12.md:21`, '
    'attempt 4; log `C:/RideBoundData/research/testrun-45f8026-eollf-dirty-fullrun-2026-10-13.log` (0 lỗi, 1.025 đạt). '
    'A không có câu về kiểm thử, nên không thêm một câu mới vào A.',
    '- **B421–423:** giữ tiết lộ đã có về việc xem tập chính trước khi chọn mức 120 giây, và thêm '
    '`kể cả các phép tính thử ở 120 giây` để áp đủ R34 §7.4. A231 hiện đã giữ ý này; '
    'bằng chứng I06/C4A-11/I11/K42. Giữ ý các ngày kiểm học máy đã xem của B-v10.',
    '- **B7:** đổi comment ghép sang tên bản A được giao `08-chuong4-phanA-v5-v2.tex`.',
    '',
    'Các mục B đã giải quyết: lõi tiết lộ dùng lại tập chính/120 giây (B421–423); '
    'B19–21 tương phản chỉ thay trần; các câu đã dùng “quyết định bị ép”; đoạn đồng nhất tệp cũ của B409–410 (v7) '
    'đã bỏ trong v10. B359–361 vẫn có mẫu số 20.101/20.435 cho hai số 0. '
    'Nếu đổi câu tiết lộ thêm lần nữa, dùng “các phép tính thử ở 120 giây” như A, để giữ một tên cho một việc.',
    '',
    '**Nhãn ngoài phần A:**',
    '',
    '| Target giữ nguyên | Chương phải định nghĩa | Định nghĩa thật đã kiểm |',
    '|---|---|---|',
    '| `muc:c1-cauhoi` (A20) | Chương 1 | `W/r30-ch1/05-chuong1-v3.tex:81`, phần câu hỏi nghiên cứu. |',
    '| `phuluc:A` (A224) | Phụ lục A | `W/r31-ch5/11-phuluc-v2.tex:12`, phần tập kịch bản tĩnh thực sự. |',
    '| `phuluc:C` (A148) | Phụ lục C | `W/r31-ch5/11-phuluc-v2.tex:60`, kiểm kê/tái lập thực sự. |',
    '',
    'Người ghép cần dùng đúng các tệp trên; không nhãn nào trong ba nhãn này thuộc phần A. '
    'Toàn bộ 40 target phân biệt của A resolve, kể cả năm target của B: '
    '`muc:c4-vaitro` (B17), `muc:c4-dubao` (B77), `muc:c4-dem` (B215), '
    '`muc:c4-tuyet` (B304), `muc:c4-hople` (B356). Ch2 v4 không có target được A gọi trực tiếp; '
    'không phát hiện xung đột label trong bộ Ch1 + Ch2 + Ch3 + A + B + phụ lục.',
    '',
    '**Kiểm thử ở chương khác:** Ch3 `W/r33-ch3v4/07-chuong3-v4-v3.tex:723–724,737` '
    'còn ngày 12/10 và evidence lượt 3 + 3b; phụ lục `W/r31-ch5/11-phuluc-v2.tex:117–122` '
    'còn cách cộng lượt kiểm. Sửa sang attempt 4, một lần chạy ngày 13/10/2026, cùng điều kiện LF/tệp chưa ghi nhận. '
    'Chương 1 v3 không có câu kiểm thử cần sửa.',
    '',
    '**Danh mục:** `engelhardt2026` và `schulz2026` đã có trong `W/r32-bib/10-tai-lieu-draft.tex`; '
    'không thêm key hay metadata mới trong R36. Người ghép cần nạp danh mục này '
    '(có cả `horl2022` của B). **Registrar:** nhập R36-A01/02/03 nếu cần; '
    'xem N4B8-05 để cập nhật lưu ý chiều tuyết cũ và giữ đính chính X3-32/C4A-09 cho A24/D13/D19.',
    '',
    '## 6. Kiểm tra và giới hạn',
    '',
    'Script `apply-and-check-v3.py` tạo bản sửa bằng nối các lát cắt A-v4. '
    'Các ký tự ngoài 26 vùng khai báo giữ nguyên trong văn bản đã chuẩn hóa xuống dòng. '
    'Ngoặc lồng, thứ tự begin/end, dấu toán `$`, label duy nhất, nhãn/cite không bị mất đều đạt; '
    '40 target của A và target Ch4 được Ch3/B gọi đều có định nghĩa thật. '
    'Các số được thay cách trình bày/đưa mới đã đọc lại và đối chiếu trong output số mới; '
    'không có số kết quả phải đổi do sai phép tính. Các từ cấm và lưu ý chiều tuyết hết hiệu lực không còn trong A.',
    '',
    'Chưa chứng nhận compile, page count hay bản ghép cuối; luật song song cấm build, mô phỏng và cài đặt. '
    'Phần tắc đường cố định vẫn giữ ngoại lệ bộ chạy cũ, không phục hồi và giới hạn chưa kiểm. '
    'Không suy nguyên nhân −1 ms, không suy tác dụng nhân quả, không thêm kết quả cho phương án chưa chạy. '
    'Các ghi chú R34/A-v2 trước đây được giữ nguyên; chỗ hết hiệu lực được đính chính trong ghi chú R36 này.',
    '',
]
notes_text = '\n'.join(notes)
notes_text = notes_text.replace('ngoài 26 vùng khai báo', f'ngoài {len(changes)} vùng khai báo')
qa = dict(change_count=len(changes), edits=ordered,
          base_sha256=hashlib.sha256(source_bytes).hexdigest(),
          output_sha256=hashlib.sha256(target.encode('utf-8')).hexdigest(),
          old_counts=old_counts,new_counts=new_counts,
          prose_growth_percent=100*(new_prose/old_prose-1),
          visible_growth_percent=100*(new_visible/old_visible-1),
          syntax=target_checks, reference_owners={r:label_sources[r] for r in target_checks['references']},
          paired_ch4_refs=paired_refs,table_widths=table_widths,
          builds_run=False, simulations_run=False, source_unchanged=True, root_main_totals=root_main_totals,
          root_morning_count=dict(runs=64,forced=0,acked=44270),
          preserved_numeric_probe_failure="stale denominator expectation; reconciled by confirm output")
outputs = {
    TEX: target,
    NOTES: notes_text,
    QA: json.dumps(qa, ensure_ascii=False, indent=2)+'\n',
    DIFF: ''.join(difflib.unified_diff(source.splitlines(keepends=True),target.splitlines(keepends=True),
                                     fromfile='08-chuong4-phanA-v4.tex',tofile=TEX.name)),
}
for path, content in outputs.items():
    with path.open('x', encoding='utf-8', newline='\n') as f:
        f.write(content)
assert BASE.read_bytes() == source_bytes
print('Create-only deliverables and static QA completed:', ', '.join(p.name for p in outputs))
