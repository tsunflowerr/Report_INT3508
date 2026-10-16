"""R42 decision log writer. Reads saved checks and review; exclusive text outputs only."""
from pathlib import Path
from collections import Counter
import json
import re

ROOT = Path(__file__).resolve().parent
KIT = ROOT.parents[3]/'rewrite-2026-10'
review = (KIT/'reviews/R32-REVIEW-CH5-APPX-CLAUDE.md').read_text(encoding='utf-8')
checks = json.loads((ROOT/'r42-check-v3.json').read_text(encoding='utf-8'))
rows = []
def add(id,decision,evidence,change):
    assert decision in ['A','M','R','CANNOT CHECK']
    rows.append((id,decision,evidence,change))

h = [
('A','A06; B01; Ch4A:muc:c4-thietlap','Đổi đo trần thành đánh giá trên mô phỏng, nêu đối tượng.'),
('A','X3-12; Ch3:eq:so','Mở chương giới thiệu đủ ba phần của độ lệch so lời hứa đầu.'),
('A','A06; A13; Ch3:eq:luatc','Nêu khách đã được nhận, bộ điều phối dời và tổng cả chuyến.'),
('A','J01; J03; Ch3:muc:doichung','Nói mốc đã có ở Hörl–Zwick; giữ trích dẫn công thức 7.'),
('A','C08; Ch4A:243–245; check:numbers.main_raw_rows','Gọi tên luật C và điều phối không trần ở từng số.'),
('M','C4A-01; N-21; C04; Ch4A:355–360','Đặt 292/2.338 và 289/2.338, mỗi luật 28/34, cạnh nhau; chỉ kết luận ở ngưỡng30s, khác nhóm khách.'),
('A','N-08; L1a-06; E01; E09; Ch4A:muc:c4-congdon','Giải nghĩa bản ghi phương án bị trần loại; không suy tác dụng lên phục vụ.'),
('M','F17; N4B8-01; Ch4B:80–107','Nêu rõ khách C-30, mẫu số1.471, gộp theo khách; mỗi cách so với lời hứa đầu của chính nó.'),
('A','F03; Ch4B:80–83','Gọi rõ tính lại lời hứa, quyết định điều phối giữ nguyên.'),
('M','C10; N-16; Ch4B:bang:c4-dem','Giải nghĩa đệm; giữ cả điều kiện lời hứa theo dự báo.'),
('A','C10; N-18; check:U_forecast_pad30,C30_forecast','Gắn 37,2 với đệm, 7,4 với C, trung bình gộp theo khách.'),
('A','X3-12; F09; Ch4B:hinh:c4-so','Giải nghĩa sổ chia số giây trễ thành ba phần.'),
('M','N4B8-11; Ch4B:182; check:numbers.rounding','Thêm82s; nêu làm tròn riêng vì82+5.353+783=6.218, khác nhãn tổng6.217.'),
('A','F13; B20; Ch4B:muc:c4-tuyet','Thêm15/11/2018,8kịch bản và41→34/601.'),
('M','I01; I02; I04; B12; B05; Ch4B:muc:c4-thaoluan','Nối giới hạn với kết luận; không dùng chi tiết dừng0giây như đã kiểm mọi lần.'),
('A','H12; E09; Ch4B:459–464','Nêu bộ chọn ưu tiên chi phí chưa chạy đầy đủ; luật từng lần chưa cài.'),
('A','H02; K18; E09','Đổi giá trị tăng thêm sang câu hỏi phần cộng dồn có đổi kết quả không.'),
('M','J38; K30; K31','Viết khóa luận kế thừa, không định lượng phần lớn ý nền khi không có phép đếm.'),
('M','J06; J08; Ch2:muc:c2-dolech','Thu hẹp tiền lệ kiểm soát lời hứa giờ đón khi gán khách.'),
('A','J01; J03; Ch3:460–469','Đúng đại lượng giờ trả trên tuyến cũ; nói dùng mốc tương tự.'),
('A','H02; H12; OUTLINE §7.2; ROUND42','Giải nghĩa hai thứ tự ưu tiên, bốn tổ hợp, giữ đầu5.3 và trạng thái chưa chạy.'),
('A','I13; A28; Ch3:733–735','Nói một số kịch bản để đối chiếu, không gọi lẫn với tập kiểm tra chính.'),
('A','H10; H12','Viết câu hỏi đánh đổi còn giữ không khi bộ chọn đổi.'),
('A','E09; A22; J05','Dùng tên phần cộng dồn và mốc giữ nguyên; thêm dẫn tới B.'),
('A','F14; K20; K21','Chỉ dùng dữ liệu đã có tại thời điểm hứa.'),
('A','H10; D18; K11','Đòi mỗi cấu hình chạy mô phỏng đầy đủ, không suy lượt phục vụ từ sàng lọc.'),
('M','C4A-15; TEX08:136–137; K33; Ch4A:muc:c4-thamdo','A nêu30s và thành phần gói; giữ bỏ bảng kết quả tĩnh.'),
('A','A22; X3-27; Ch3:366–379','Tách p=e và phạm vi phép kiểm giờ trả; không suy mọi ràng buộc.'),
('M','J03; J05; A22; Ch3:460–469','Gọi biến thể do khóa luận dựng từ công thức7; suy luận, chưa chạy.'),
('M','A22; A10; A11; J03; J05','Tách chứng minh C và hạn chót nới; không quy mọi đổi của e riêng cho tắc đường.'),
('M','A06; A09; A11; X3-33; Ch3:428–458','Nêu tổng abs(c), tổng abs(z); hạn chót kiểm từng cập nhật, không chỉ cuối.'),
('A','B02; B08; SPLIT:15–65; check:scenario_lists','Giải nghĩa mã, mẫu10%, mọi cặp mẫu×khung.'),
('M','A26; B10; RUN38:42–44; Ch4A:107–110; C17','Chỉ nói vai trò trong khóa luận; không phủ nhận mục đích gốc đã có bằng chứng.'),
('A','B15; B17; RUNW07:33–34','Ghi rõ12–13/11 cho cả sáng và cố định.'),
('M','X3-19; DOC08:20–29; q4_cost_first_reselect.py:34','Giữ ánh xạ LOCKS/B1/C1 theo yêu cầu gốc; bổ sung năm mã thư mục.'),
('A','A28; N4B8-05; R26 Q8','Gọi tên bản bộ chạy, phiên bản nguồn và mã lõi.'),
('M','WP4:7; R26 Q8','Giữ tệp cấu hình và nghĩa luật phục hồi; diễn đạt gọn trong C.'),
('M','R26 Q1–Q2; actual_fleetpy_medium_preflight.py:569–581,595–637','Giữ đủ: hết yêu cầu tương lai, yêu cầu đang xử lý và hành trình xe.'),
('M','C06; C08; F06; N4B-14; ADD1:66–78','Viết câu; số lượt là hiệu hai số đếm, không chia thành tỉ lệ; so khớp chỉ các trường đã so.'),
('M','TESTRUN:14–18,35–56; fullrun log:1–6,27–71; check:test_attempts','Cập nhật13/10 full1.025/1.025, bản sao dùng lại, hai điều kiện và các lượt cũ.')]
assert len(h)==40
for i,(d,e,c) in enumerate(h,1): add(f'H{i}',d,e,c)
for row in [
('B1','M','TESTRUN:14–18,35–56; log fullrun:1–6,27–71','Nhận kết quả lượt4; nêu dùng lại bản sao lượt3, giữ đầy đủ các kết quả trước.'),
('B2','M','C4A-01; C08; N-20; C20; N-21; C04; E01; check:main_raw_rows','Thêm các vế bất lợi và vật so; giới hạn gần ngang ở30s và khác nhóm khách.'),
('B3','M','I06; C4A-11; I01–I05; B05; H12; E09','Nêu tính thăm dò và ảnh hưởng hạn chế; bỏ chi tiết dừng0s có phạm vi chưa đủ.'),
('B4','M','A26; B10; Ch4A:107–110; Ch3:725–735; I13; C17','Nêu15lần chỉ dùng kiểm sổ trong khóa luận; thêm điều kiện bản dựng lại, không phủ nhận mục đích lịch sử.'),
('B5','M','C4A-15; TEX08:136–137; K29,K33,K34','A đáp nguồn30s, sửa đích c4-thamdo; không nói khóa luận không dùng bất cứ số nào vì vẫn dùng30s.'),
('N1','M','N4B8-01,02,11; C10; N-19; F13; check:rounding','Ba phần dễ đọc; bổ sung mẫu số1.471 cho hạn chót và chú thích làm tròn.'),
('N2','M','RUN38:51–55; RUNW07:35–43; RW7X:35–40,77–79; LAD:1–6; R26Q8','Bổ sung đầu vào và mã thư mục; tên chứa mã trước-s7, không kết thúc bằng mã; giữ LOCKS/B1/C1.'),
('N3','M','A28; R26Q1–Q2,Q8; N4B-14; SPEC:28–63; C08','Viết đủ nghĩa; đúng điều kiện kết thúc, số đếm/mẫu số, giới hạn trường7159; không nhận kiểm kê chưa bao giờ làm lại.'),
('N4','M','J08; J01; J05; H10; H12; E09; A22; OUTLINE §7.2','Tiền lệ giờ đón được thu hẹp; hai thứ tự, năm hướng, tham chiếuB; giữ chưa chạy.'),
('N5','M','Ch3:374–379,428–469; A22; A06; A09; J05','Lr theo khách; tách hai phép chứng minh; C cộng abs(c), hạn chót kiểm từng cập nhật.')]: add(*row)

small = [
('A','main.tex:115–119; PL preamble','Ghi nơi ghép09-chuong5 và11-phuluc sau tài liệu; không thêm appendix lần nữa.'),
('A','OUTLINE §1; Ch3:bang:luat','Ký hiệu luật trong câu số lần chạy được viết bằng lời; mã thư mục giữ nguyên để tra cứu.'),
('A','STYLE §5.2(6); RUN38:51–55','Giải nghĩa gốc đường dẫn ngay đầu C.'),
('M','B17; một bản tin FREE cố định core38d517d; audit C','Xác nhận mã cũ trong LOG; văn bản giữ thông tin bộ chạy cũ, không thêm một mã không cần cho lập luận.'),
('M','run_forecast.py:44,67,71–74; q4_cost_first_reselect.py:32–35,178–182; ml_pilot_extract.py:9–28','Bổ sung gốc thí nghiệm phụ. Thư mục MplusF thứ17 là phép phát triểnS1, không phải kịch bản chính thứ17.'),
('M','ROUND42 inputs; check:input_files','Dùng Ch4A-v5-v3 và Ch4B-v11-v2, không lấyv10 làm bản ghép.'),
('CANNOT CHECK','ROUND42 §Length; ASSEMBLY trial build; check:word_counts','Đếm theo500tiếng/trang; không biên dịch nên chưa xác nhận số trang và vị trí bảng thật.'),
('A','OUTLINE §2(6)','Thống nhất tập kiểm tra chính.'),
('R','I11; F13; K19; K38; yêu cầu ba đoạn5.1','Bỏ hai câu tổng kết tùy chọn: lặp ba đoạn; chưa có cách hứa tốt cho ngày bất thường quá rộng so bằng chứng.'),
('A','J01; J05','Bổ sung EV cho mốc giữ nguyên và khác biệt theo định nghĩa.')]
for i,(d,e,c) in enumerate(small,1): add(f'S{i}',d,e,c)

# One row for every numbered number/identity group in the two review tables.
sec1 = review.split('### 3.1 Các số của Chương 5',1)[1].split('### 3.2 Các số và nhận dạng của phụ lục',1)[0]
sec2 = review.split('### 3.2 Các số và nhận dạng của phụ lục',1)[1].split('### 3.3 Nhãn',1)[0]
for section,prefix,expected in [(sec1,'Q5',22),(sec2,'QP',28)]:
    found = []
    for line in section.splitlines():
        if not re.match(r'^\| \d+ \|',line): continue
        p = [x.strip() for x in line.strip().strip('|').split('|')]
        # Some mathematical rows include escaped bars; keep the source column via the last cell.
        n = int(p[0]); evidence = p[-1]
        found.append(n)
        decision = 'A'
        change = 'Xác nhận lại với bản hiện hành và nguồn ghi ở cột bằng chứng; giữ số/nhận định đúng.'
        if prefix=='Q5' and n==7:
            decision='M';change='Số28/34 đúng; bổ sung292/289 và cùng mẫu số, tránh so nghĩa vụ khác nhau.'
        if prefix=='Q5' and n==10:
            decision='M';change='Giữ68→2/1.471, nêu rõ khách của luật C và lời hứa riêng của từng cách.'
        if prefix=='Q5' and n==14:
            decision='M';change='37,2vs7,4 đúng; chú thích review37,37 là hàng C có đệm, không phải C không đệm7,37.'
        if prefix=='Q5' and n==16:
            decision='M';change='Thêm82s và làm tròn độc lập; không ép ba nhãn nguyên cộng bằng nhãn tổng.'
        if prefix=='Q5' and n==18:
            decision='M';change='Các số đã làm tròn có tổng3.446,0, không bằng3.445,9 đúng tuyệt đối; giữ số và nêu làm tròn riêng.'
        if prefix=='Q5' and n==20:
            decision='M';change='Nói luật từng lần còn chưa cài đặt; bộ chọn chưa chạy mô phỏng đầy đủ.'
        if prefix=='QP' and n==12:
            decision='M';change='15lần C-30 đúng; chỉ mô tả vai trò kiểm sổ trong khóa luận, không kể phép hiệu chỉnh phụ.'
        if prefix=='QP' and n==13:
            change='Đã mở RW7X:35–40,77–79 và configs/C-90,150,180,240: không còn phần chưa kiểm.'
            evidence += '; RW7X:35–40,77–79; danh sách configs đã mở'
        if prefix=='QP' and n==15:
            change='LOCKS đã kiểm trực tiếp; giữ ánh xạ ngắn cùng tên thư mục.'
            evidence += '; q4_cost_first_reselect.py:34; r17-wp14r-check.txt:5'
        if prefix=='QP' and n==19:
            decision='M';change='Chọn tám thư mục đúng ngày15/11, r1–4×w14/15; không lấy mọi C-30 trong gốc.'
        if prefix=='QP' and n==26:
            decision='M';change='Giữ số lượt=phục vụ−trễ và mẫu số riêng; không biến số lượt thành thương.'
        if prefix=='QP' and n==27:
            decision='M';change='Số12/10 đúng lịch sử, không phải số sai; bổ sung lượt toàn bộ13/10 mới nhất, giữ các lượt trước.'
            evidence += '; check:numbers.test_attempts (cộng năm log thô)'
        add(f'{prefix}-{n:02d}',decision,evidence,change)
    assert sorted(found)==list(range(1,expected+1)),(prefix,found)

for row in [
('LAB-1','A','check:labels; Ch1→chuong:ketluan','Giữ nhãn chương, có câu trỏ và giải được.'),
('LAB-2','M','check:labels; Ch4A:muc:c4-thamdo; C4A-15','A tồn tại và nay đáp nguồn trần30s.'),
('LAB-3','M','check:labels.new_references_to_B','Giữ B và thêm câu trỏ từ hướng thứ hai của5.3.'),
('LAB-4','M','Ch3:724,735; Ch4B:398–401; TESTRUN lượt4','C đáp bản dựng lại và kiểm thử mới; ghi riêng ngày cũ Ch3 phải sửa khi ghép.'),
('LAB-5','A','check:labels','Ba nhãn mục5.1–5.3 không trùng; không bắt buộc phải có câu trỏ.'),
('LAB-6','A','check:labels; PL preamble','Ba bảng có nhãn, dẫn và đích liên kết riêng; A/B/C và B.1,C.1,C.2 giữ nguyên.'),
('REF-1','A','Ch4B:muc:c4-thaoluan; check:labels','Dẫn hạn chế đúng nội dung.'),
('REF-2','M','Ch4A:muc:c4-thamdo; C4A-15','Đổi A từ c4-taptu sang c4-thamdo.'),
('REF-3','A','PL:bang:pl-giunguyen','Câu dẫn bảng B đúng.'),
('REF-4','A','Ch3:muc:giunguyen','Dẫn đúng giả thiết(N).'),
('REF-5','A','Ch3:muc:bamoc','Dẫn đúng v,e,p trong chú thích.'),
('REF-6','A','PL:bang:pl-danhsach','Dẫn đúng danh sách đã so khớp34/15.'),
('REF-7','A','PL:bang:pl-goc','Dẫn đúng gốc/cấu hình.'),
('REF-8','A','BIB bibitem horl2022,fielbaum2020,schulz2026; check:labels','Ba khóa trích dẫn đều có ở danh mục hiện hành.')]: add(*row)

for row in [
('G1','M','TESTRUN lượt4; check:test_attempts','Nhận yêu cầu cập nhật; các số12/10 vẫn đúng lịch sử, không gọi chúng là phép đếm sai.'),
('G2','M','C4A-01; C08; C20; N-20','Thêm vế công bằng, vế bất lợi và mô phỏng; giới hạn ngưỡng so sánh.'),
('G3','A','Ch4A→A; Ch3→C; check:labels','Đáp câu trỏ A/C; thêm câu trỏ B.'),
('G4','A','H1–H40 đối chiếu bản nền; STYLE §2','Giải nghĩa ba phần, đệm, sổ, bộ chọn và mã; sửa lối câu cụt.'),
('G5','M','Ch5 cấu trúc; C17; Ch4A:107–110; BIB','Giữ năm hướng và EV/khóa; bỏ mục đích phụ vì phạm vi, không vì câu đó chứa từ chủ sở hữu cấm.'),
('L2.1-D','M','C4A-01; C08; C20; N-20; C04','Đoạn điều phối có đủ vật so, −96/−242/−5, cùng thước292/289; không bảo đảm giờ đến.'),
('L2.1-F','M','N4B8-01,02; N-19; C10','Dự báo không riêng C, mẫu số riêng; đệm hơn ở120s đi cùng phục vụ thêm.'),
('L2.1-L','M','N4B8-11; F13; N4B-05','Đủ ba thành phần và41→34; nêu làm tròn riêng.'),
('L2.2','M','I06; C4A-11; E09; J05; B05; J08','Thăm dò, ảnh hưởng kết luận, chưa cài luật từng lần; thu hẹp tiền lệ/chi tiết dừng.'),
('L2.3','A','OUTLINE §7.2; ROUND42; check:structure','Giữ đúng năm hướng; selector×cap đầu, không có giờ công.'),
('L2.4','M','SPLIT; RUN38; R26; N4B-14; TESTRUN; I13','C đủ bảy nội dung; sửa phạm vi người đọc/đếm/số mới, bổ sung đầu vào và thí nghiệm phụ.'),
('L2.5','M','C4A-15; K29,K33,K34; r31-NOTES §5A','Giữ A làm nguồn tham số; tiếp tục bỏ bảng tĩnh thiếu output.'),
('L2.6','M','A22; J05; A06; A09; Ch3:374–469','B giữ điều kiện, đúng ghi công, tổng cả chuyến và hạn chót từng lượt; có câu trỏ.'),
('L2.7','M','C4A-01; C08; N-20; A22; C17; STYLE','Khắc phục bỏ sót và cách gọi phần cộng dồn; không coi mục đích hiệu chỉnh lịch sử là dữ kiện sai.'),
('ALT-A','R','ROUND42 labels; Ch4A→phuluc:A; C4A-15','Bác phương án bỏ A rồi đổi chữ B/C: A còn cần để đáp nguồn30s; không sửa ngoài thư mục.'),
('P1-NODAY','R','F13; B20; Ch4B:muc:c4-tuyet','Bác câu chưa có ngày sự kiện: đã có chiều tuyết15/11 với8kịch bản; chỉ thiếu nhiều sự kiện độc lập mới.'),
('B2-BRIEF','R','ROUND31 brief nguyên văn §Content; ROUND42 fairness','Bác lý do briefR31 nêu đích danh toàn bộ vế thêm: R31 chỉ chỉ rõ−96vàđệm hòa; vẫn áp dụng vế thêm vì bằng chứng vàR42.')]: add(*row)

assert len({x[0] for x in rows})==len(rows)
counts = Counter(x[1] for x in rows)
assert len(rows)==141,len(rows)
header = '''# R42 — Chương 5 và phụ lục v3: quyết định đã kiểm

Bản dùng để ghép: **10-chuong5-v3-v3.tex**, **11-phuluc-v3-v3.tex**. Hai tệp `-v3.tex` đáp tên đầu ra của brief và được giữ như lượt đầu; `-v3-v2.tex` là lượt rút gọn; `-v3-v3.tex` là bản cuối. Không ghi đè bản nào, kể cả R31. Lượt cuối chỉ thu hẹp 30–60giây về tập kiểm tra chính và cho dãy tám mức trần xuống dòng tự nhiên trong ô bảng.

A = nhận nội dung sau đối chiếu; M = nhận mục tiêu nhưng sửa phạm vi/cách viết; R = bác phần nêu trong dòng; CANNOT CHECK = chưa kiểm được. A ở các dòng kiểm số/nhãn có thể là xác nhận và giữ nguyên, không phải thêm một kết quả. Các nhận xét trùng nội dung vẫn có dòng riêng theo ID của review.

Đã đọc toàn bộ R32, baseR31/NOTES, ROUND42, quy tắc song song, brief chủ sở hữu, ADDENDUM-1 §0, ASSEMBLY và các bản hiện hành. H1–H40, B1–B5, N1–N5 dùng ID có sẵn; S1–S10 là mười sửa nhỏ; Q5/QP là50 nhóm số ở §3.1/§3.2; LAB/REF là từng hàng ở §3.3/§3.4. G1–G5 và L2.x bao quát các nhận định chung/giảng viên. ALT-A, P1-NODAY và B2-BRIEF tách các đề xuất/lý do phụ cần bác. Các nhận định người đọc không có ID về thuật ngữ, câu cụt, mã và các vế kết quả đã được đối chiếu tương ứng ở H1–H40 và L2.1; không tạo một thống kê trùng nữa.

Neo ngắn: Ch1 = r40-ch1-v4/05-chuong1-v4-v4.tex; Ch2 = rewrite-2026-10/drafts/06-chuong2-v6.tex; Ch3 = r33-ch3v4/07-chuong3-v4-v3.tex; Ch4A = r36-ch4a-v5/08-chuong4-phanA-v5-v3.tex; Ch4B = r39-ch4b-v11/09-chuong4-phanB-v11-v2.tex; BIB = r32-bib/10-tai-lieu-draft-v2.tex. Đường dẫn r… tính từ codex-work. `check:` là trường trong r42-check-v3.json, tạo bởi r42-check-v3.py; số dòng review cũ không thay cho các neo bản hiện hành. Các mã REG/ADD1/X3/N4B/C4A/N4B8 theo sổ chính và phụ lục1–6. Các khóa RUN38, RUNW07, RW7X, R120, SPEC, LAD, DOC08, TEX07/TEX08, R26 như R31-NOTES và sổ.

TESTRUN là evidence/TESTRUN-45f8026-2026-10-12.md. Log lượt4 là C:/RideBoundData/research/testrun-45f8026-eollf-dirty-fullrun-2026-10-13.log; lượt1,2,3,3b đã được cộng riêng trong output kiểm. Không chạy lại dotnet test ở R42; chỉ đọc log. Hai kiểm độc lập theo Ch5/A/B và C đã đối chiếu nguồn rồi đọc bản rút gọn; root kiểm lại các thay đổi trước khi ghép.

## Quyết định

'''
summary = f"Tổng {len(rows)} dòng: **A {counts['A']} / M {counts['M']} / R {counts['R']} / CANNOT CHECK {counts['CANNOT CHECK']}**. Các số này đếm cả nhận xét sửa chữ lẫn hàng xác nhận số/nhãn, không phải số đoạn thay đổi.\n\n"
parts = [header,summary,'| ID | Quyết định | Bằng chứng đã đối chiếu | Thay đổi hoặc lý do |\n|---|---|---|---|\n']
for r in rows:
    parts.append('| '+' | '.join(x.replace('|','/').replace('\n',' ') for x in r)+' |\n')
parts.append('\n## Các phần bác và các M quan trọng\n\n')
for id,d,e,c in rows:
    if d=='R': parts.append(f'- **{id}:** {c} Nguồn: {e}.\n')
parts.append('''
Các M không hạ bớt vế bất lợi: giữ −96 lượt phục vụ, −242 khách đi chung, −5 ở hai phút, 292/2.338 so289/2.338 và28/34 cho mỗi luật. Gần ngang chỉ nói ở ngưỡng30giây, hai nhóm khách khác nhau. Dự báo hạn chót66→2 mang mẫu số riêng1.471. Tổng sổ ngày thường6.217 và các phần82/5.353/783 được làm tròn độc lập; không tuyên bố tổng nhãn bằng đúng nhãn tổng.

Hạn chót nới là suy luận do khóa luận dựng, chưa chạy; nó qua nhờ e≤max(p0+B,e), khác lý do c=0 của C. C cộng tổng trị tuyệt đối qua chuyến, không chỉ một c; hạn chót kiểm ở từng lượt. Số lượt không trễ là hiệu hai số đếm, còn tổng yêu cầu là mẫu số nếu lấy tỉ lệ. Tệp cố định chứa mã cấu hình trước phần-s7, không kết thúc tại mã. Đối chiếu7.159khách chỉ xác nhận các trường đã so.

Mục đích gốc của15kịch bản có C17 làm bằng chứng, nhưng không cần kể phép thử phụ chưa trình bày trong khóa luận; C chỉ nói vai trò của15lần ấy trong phép kiểm sổ. A vẫn nêu nguồn tham số30giây từ C4A-15; không khôi phục các bảng số liệu tĩnh chưa có ánh xạ output.

## Kiểm tra và độ dài

''')
parts.append('| Phần | Tiếng văn xuôi | Chữ bảng/chú thích bảng |\n|---|---:|---:|\n')
parts.append(f"| Mở Chương 5 | {checks['word_counts']['Ch5']['opening_words']} | 0 |\n")
for prefix,k in [('5','Ch5'),('Phụ lục','PL')]:
    for i,r in enumerate(checks['word_counts'][k]['sections'],1):
        label = f'5.{i}' if k=='Ch5' else 'ABC'[i-1]
        parts.append(f"| {label}. {r['title']} | {r['prose_words']} | {r['table_words']} |\n")
parts.append(f"| **Chương 5 tổng** | **{checks['word_counts']['Ch5']['prose_total']}** | **0** |\n")
parts.append(f"| **Phụ lục tổng** | **{checks['word_counts']['PL']['prose_total']}** | **{sum(r['table_words'] for r in checks['word_counts']['PL']['sections'])}** |\n")
parts.append('''
“Tiếng” là đơn vị cách nhau bởi khoảng trắng sau khi bỏ chú thích, lệnh cấu trúc, trích dẫn/tham chiếu và biểu thức toán. Không tính tiêu đề; bảng và chú thích bảng tính riêng. Dùng thước ROUND42 mới ≈500tiếng văn xuôi/trang, thay thước330 của brief chung: Chương5 có1.480tiếng≈2,96trang trước khoảng tiêu đề; phụ lục991tiếng≈1,98trang văn xuôi, cộng ba bảng4/5/4hàng dữ liệu, dự kiến khoảng3trang. Không thu phông; dãy tám mức trong bảng C dùng chữ số bình thường có điểm ngắt, không ép cả dãy trong một công thức rộng. Trang thật và chỗ xuống dòng chỉ kiểm được khi ghép và biên dịch, nên S7 là CANNOT CHECK về bố cục, không phải thiếu số liệu.

r42-check-v3.json PASS: ngoặc/môi trường/dấu toán khớp; các đoạn và nhóm hàng có EV; đúng ba đoạn5.1 và năm hướng5.3. Kiểm trên toàn bộ các bản hiện hành ở brief và hai tệp cuối: không nhãn trùng, không tham chiếu chưa định nghĩa, không khóa trích dẫn thiếu. Có câu từ5.3 trỏ B; A nay trỏ đúng c4-thamdo; C đáp yêu cầu bản dựng lại.

Kiểm số từ ADD1: phục vụ2.434/2.338/2.387, đúng giờ một/hai phút, fairness292/289, đệm2.328hòa và2.366vs2.338, sớm44/4, độ dài37,2/7,4. Danh sách tóm tắt mở rộng đúng34/15 và chọn đúng8thư mục tuyết. Các log kiểm thử cộng riêng: lượt1,2 đạt1.020/1.025 vàhỏng5; lượt3 đạt1.024/1.025 vàhỏng1;3b đạt1/1;4 đạt1.025/1.025,hỏng0,exit0. Các phép kiểm chỉ đọc, không mô phỏng/biên dịch/cài đặt. Mọi script và output tạo mới trong r42-ch5-v3; các bản trước giữ nguyên.

## Ghi chú ghép và nội dung không phục hồi

- Bản dùng cuối là hai tệp `-v3-v3.tex`; các hậu tố trước là lịch sử đọc lại được, không bị ghi đè. Khi ghép, nội dung Ch5 vào noi-dung/09-chuong5.tex; phụ lục vào11-phuluc sau tài liệu tham khảo. Phụ lục đã chứa appendix.
- **Ch3 hiện hành:724 còn ngày12/10/2026 cho toàn bộ1.025kiểm thử.** Phải sửa ngày thành13/10/2026 khi ghép theo TESTRUN lượt4 và ASSEMBLY; Ch4B:398–401 đã đúng13/10. Không sửa Ch3 trong R42 vì ngoài thư mục được phép.
- Sổ N4B-13 chỉ phủ lượt3/3b; EV của C dùng trực tiếp hồ sơ TESTRUN cập nhật và log lượt4 đã mở. Người quản lý sổ có thể thêm dòng cho lượt4, nhưng không cần giả nhận N4B-13 đã phủ nó.
- Phép chọn ưu tiên chi phí×trần vẫn chưa chạy. Sự đồng ý của chủ sở hữu sau khi bộ kiểm chạy sẵn sàng không phải kết quả. Giữ hướng này đầu5.3; nếu có số đã kiểm trước nộp, cần cập nhật5.3 và phần kết luận tương ứng.
- Không khôi phục bảng kết quả tĩnh, bảng kết quả ngày×khung hoặc CE-6 như sự kiện quan sát. Lý do R31 vẫn giữ: thiếu ánh xạ output tĩnh, ngân sách trang, chưa kiểm lại bản ghi CE-6. A chỉ thêm nguồn tham số30giây được C4A-15 xác nhận.
- Không thêm khóa trích dẫn mới. Các khóa horl2022/fielbaum2020/schulz2026 có đủ trong BIB hiện hành; không dùng metadata tên tạp chí cho Hörl–Zwick.
- Phần mềm, nhu cầu, và các tập thử có đủ neo trong EV; các con số không suy ra giá trị kinh doanh hoặc hài lòng của khách.
''')
with (ROOT/'r42-LOG.md').open('x',encoding='utf-8') as f: f.write(''.join(parts))
with (ROOT/'r42-decisions.json').open('x',encoding='utf-8') as f:
    json.dump({'counts':dict(counts),'rows':[dict(zip(['id','decision','evidence','change'],r)) for r in rows]},f,ensure_ascii=False,indent=2)
print(json.dumps({'rows':len(rows),'counts':dict(counts),'final_words':checks['word_counts'],'outputs':['r42-LOG.md','r42-decisions.json']},ensure_ascii=False,indent=2))
