"""Exclusively create a complete review-decision log from saved inputs and QA."""
from pathlib import Path
from collections import Counter
import json
import re

ROOT = Path(__file__).resolve().parent
WORK = ROOT.parent
SCRATCH = WORK.parents[2]
review = (SCRATCH / "rewrite-2026-10/reviews/R31-REVIEW-CH1-CLAUDE.md").read_text(encoding="utf-8")
qa = json.loads((ROOT / "05-chuong1-v4-QA-v2.json").read_text(encoding="utf-8"))
assert qa["errors"] == []
rows = []

def add(identifier, decision, evidence, change):
    assert decision in ("A", "M", "R", "CANNOT CHECK")
    rows.append((identifier, decision, evidence, change))

reader_rows = [
("A","A01; A13; v3:L7-8","Giải thích giờ trả; nêu rõ độ lệch giữa giờ tới thực tế và lời hứa đầu."),
("M","J17; B01; WRITING-BRIEF, ngôn ngữ","Nêu bộ điều phối là phần mềm; dùng định nghĩa tiếng Việt thay nhãn tiếng Anh."),
("A","A01; A02; A13","Tách việc thêm điểm dừng với thay đổi thời gian đi; định nghĩa lời hứa đầu lúc xác nhận."),
("A","A01; A02; v3:L16-17","Bỏ câu chuyển tiếp có đại từ mơ hồ; hai phần được giải thích trong đoạn và mục sau."),
("M","D06; N-30; Q4R:9","Giữ 307,3/99,1/208,2; gọi các phần là tổng qua cập nhật, không là giờ của một tuyến phản thực tế cả chuyến."),
("A","D06; N-30; W07:48-54","Giải thích kịch bản xây dựng phương pháp và mức cho dời 300 giây trước hình."),
("A","N-30; Q4R:3,9","Nói rõ hai khách khác nhau; hai số 99,1 chỉ trùng giá trị."),
("A","Q4R; v3:L29,42; tọa độ H1.1","Đổi tên hình trên; mốc giữa chỉ ghi +99,1."),
("M","C31; F01-F02","Tên hình dưới dùng lời hứa theo dự báo; không mô tả như cộng một mức tắc đường cố định quen thuộc."),
("A","Q4R; D06; chú thích H1.1","Bỏ tên sổ chưa giới thiệu; ghi các phần qua cập nhật lời hứa."),
("A","C31; EXAMPLE:1-3,60; X3-23/X3-24","Bỏ giờ đón 7:22:30 ở ví dụ; giữ giờ đặt/hứa/tới. Phạm vi giải thích cách tiếp tục kế hoạch cũ và ghi nhận đón muộn."),
("M","C31; F01-F02; Ch3:501-525","In cả 7:37:44, mức kéo dài 172,9 và lệch 17,6; nói mức tăng dự báo thay phép cộng trung bình đơn giản."),
("A","C31; REVIEW-DECISIONS-R20 LR-15","Nêu ví dụ cho thấy dự báo được gì, tốn gì; không là phép đo trần."),
("A","J28; J31; BIB-VERIFICATION-v2","Thêm khóa uberxshare/moiaexpress; khoảng giờ tới hẹp hơn, không là bảo đảm."),
("A","J24; C2-18","Nêu 1.006 người và giá trị của thời gian đi/mức ổn định bằng tiếng Việt dễ hiểu."),
("M","J23; C2-17","In 2,53 và 3,12 như hai cách hỏi, kèm 15/2 và 66/27; không biến thành một khoảng chung cho mọi khách."),
("A","I07; I10; C2-17/C2-18","Giữ giới hạn: nghiên cứu giờ tới không định giá trần của khóa luận."),
("A","B09; A07; A08","Giới thiệu tập chính 34 kịch bản, trỏ Phạm vi; nêu đầy đủ xe, điểm đón/trả và giờ đón đã xác nhận."),
("A","C21; C4A-03","Thay giao của hai tập bằng hai nhóm trùng nhau; không suy ra nguyên nhân trễ."),
("M","C24; C4A-03; owner rule về tỉ lệ","Dời số sau định nghĩa sổ; vẫn giữ gộp theo khách trong chữ in. Việc làm tròn chuyển vào EV."),
("A","C20; BUC:34-37","Nêu cực đại trong 2.434 khách; gọi 590,1 là tổng độ lớn, không gán vào riêng nhóm 203."),
("M","X3-37; X3-20; X3-27; Ch3:309-317","Dùng ví dụ dựng tay 9:10:00/9:10:40/9:11:10; giờ là phép tính kế hoạch, áp cả khách đang chờ đón."),
("A","A06; K43","Định nghĩa trần, tổng độ lớn cả chuyến, hai chiều và mức thử chính 30 giây."),
("M","F01-F02; Ch3:501-525","Diễn đạt hồ sơ/dự báo rõ hơn; không thay phép kéo thời gian và lấy max bằng cộng trung bình một khung."),
("M","X3-12; X3-25; Ch3:576-625","Sổ ghi cập nhật và hỗ trợ tính cả ba phần sau chạy, không chỉ lưu riêng phần còn lại."),
("M","X3-12; Ch3:576-625","Nhãn dự báo dễ đọc; nhãn sổ là tính phần còn lại. Chú thích nói cho phép tính cả ba phần."),
("A","K04; K19; X3-12","Nói phép tính trên mô hình mô phỏng, không là phép đo nguyên nhân."),
("A","OUTLINE câu hỏi CH1; K05","Tách CH1 thành hai câu; bỏ câu hỏi không suy ra; bỏ các con trỏ mục theo R40."),
("M","A09; C10; H01-H02; R40 §2","CH2 dùng ngưỡng một/hai phút và định nghĩa đối chứng; bỏ con trỏ; không nói không thể tách trần trong cùng bộ chọn."),
("A","F01; K19; I07; R40 §2","CH3 dùng lời hứa theo dự báo; phần độ lệch chưa giải thích; không suy phản ứng khách."),
("A","J06-J09; C2-06; C2-08","Nêu mức giờ hứa đổi, chặn khi chọn kế hoạch và giới hạn từng khách."),
("A","A01-A02; J01-J10; C2-15","Câu dẫn bảng nêu đại lượng và thời gian đi thay đổi."),
("M","C2-07/C2-08/C2-09; v3:L142-143","Bỏ chỉ dẫn nội bộ; thời gian đi cố định nghĩa là thời gian trên cạnh không đổi trong mô hình, không là không có tắc đường."),
("A","C2-15; v3:L149","Đổi tiêu đề cột thời gian đi thay đổi để khớp cả hàng dự báo."),
("A","C2-09; laupichler2026 trong BIB-v2","Ghi tác giả/năm và nói Mt-KaRRi là bộ điều phối."),
("R","J06; J08; C2-15; v3:Bảng1.1","Bác câu thay thế nói mọi cách đều bảo vệ lời hứa: hàng đo/dự báo không tự đặt nghĩa vụ từng khách. Viết các công trình đo hoặc giới hạn đại lượng khác nhau."),
("M","J05; C2-04/C2-05; K27; Ch4B-v10:445-446","Khác biệt là suy luận từ định nghĩa; không tính phần giữ kế hoạch nên không nới; chưa chạy đối chứng kiểu Hörl–Zwick."),
("A","A06; A22; C02; I10","Viết mục tiêu kiểm một giới hạn, không nói hãng xe/khách đã được thông báo hoặc biết trần."),
("A","B01; X3-15; Ch3:muc:kientruc","Giới thiệu RideBound trước khi dùng; tách câu đặc tả khỏi mô tả bộ mô phỏng."),
("A","J01/J03; C2-04; J35; C2-15","Nói dự báo có tiền lệ; luật C đi cùng dự báo/sổ, không nói dự báo là thành phần tính trần."),
("A","B01; X3-40; B06; B09; engelhardt2026","Nói FleetPy là bộ mô phỏng, thêm trích dẫn, chia câu thiết lập/số kết quả."),
("M","C4A-01; N-21; J10/J11","Định nghĩa hạn chót; 30 so với 900 giây; 28/34 in đối xứng cho cả C và hạn chót theo cùng thước."),
("A","A09/A10; A06","Nêu C chỉ giới hạn phần tính cho điều phối, không dùng phần này mơ hồ."),
("M","A22; X3-27; Ch3:366-385; X3-16","Viết bằng lời: giữ nguyên hợp lệ về cấu trúc, cùng phép chiếu và phần đã dùng trong trần ở đầu lượt; điều kiện mỗi lượt, không thay N bằng mọi kiểm tra khác."),
("A","C4A-01; N-21","Có vị ngữ 292 khách tới muộn trong 2.338 được phục vụ; 289/2.338; phần trăm gộp rõ."),
("A","C10; N-16/N-18; N4B-09","Viết đoạn cách đệm đầy đủ; hai ngưỡng, mẫu số, kéo dài lời hứa và tới sớm."),
("M","A23; N-15/N-08; E09","Bản ghi không bị chặn; phân biệt bản ghi loại phương án với khách/ứng viên duy nhất và kết quả cuối."),
("M","N-09; N-16; R40 §2","Bỏ danh sách và câu nhãn chung; nêu mẫu số từng nhóm trong văn bản kết quả."),
("M","C08; N-09/N-20; R40 §2","Chuyển +31/−5 và số đi chung vào đoạn kết quả; không đặt đi chung như tác dụng dự báo."),
("M","C10; N-16; N4B-09; R40 §2","Bỏ dòng kết quả lặp; số đệm, sớm và độ dài nằm trong đoạn so đệm."),
("M","E01; N-15; R18-verification:1","98 lần trước có các mức 30–300; 34 lần C120. Không coi 132 là toàn bộ lần chạy; luật từng lần chưa chạy."),
("M","J38; D03 §1-2; quy tắc ngôn ngữ","Không cần thêm ba nhãn tiếng Anh để dễ đọc; giữ tên Việt và giải thích nghĩa. Tiếng Anh một lần trong ngoặc được phép, không bị quy tắc cấm tuyệt đối."),
("A","B06/B07","Giải thích 0 giờ là nửa đêm, hệ số tốc độ gốc."),
("A","F03; X3-12","Nói phát lại trên các lần chạy đã ghi, không đổi xe nào chở ai."),
]
assert len(reader_rows) == 54
for index, values in enumerate(reader_rows, 1):
    add(f"P{index:02}", *values)

ranked = [
("M1","M","C4A-01; N-21; J10/J11; X3-16; Ch3:366-385","Áp sự công bằng 28/34 và 292/289; sửa điều kiện N và phần đã dùng; hạn nới là suy luận chưa chạy."),
("M2","M","J38; C2-04/06/08/15; C01/C08/C10; K05/K19","Khôi phục đủ tiền lệ và phần làm thêm; phạm vi từng so sánh, không phủ định chung C hơn về mọi ngưỡng."),
("M3","M","HZ:535-541,567-569; J03/J05; C2-04/05; K27","Suy luận khác biệt, chưa thử đối chứng, thiết lập Hamburg khác. Không giới hạn công thức7 vào chỉ nhóm trên xe của đoạn văn; không gọi tất cả hàng là bảo vệ lời hứa."),
("M4","M","B01; X3-40; A06; C02/C08; J35/C2-15","Mục tiêu, vai trò phần mềm, tiền lệ dự báo; giữ −96, +31, −5 và thêm mẫu số. Tách đoạn để đọc dễ."),
("M5","M","X3-37; X3-20/27; F01/F02; X3-12","Định nghĩa trước số; ví dụ dựng tay; cả khách đang chờ; cộng giữ dấu khác tổng độ lớn; sổ hỗ trợ tính sau chạy."),
("S6","M","C4A-11; B11; B12; B05; H01/H02; A08","Dữ liệu đã xem, tải hai khung đo khác, 0 dừng chỉ ba mẫu. Chưa biết kết quả với thứ tự chọn khác, không phủ định phép so cố định bộ chọn."),
("S7","M","C10; N-16/N-18; N-15/N-08; A23; E09","Cách đệm đủ ngưỡng và giá; thêm số tới sớm bị bỏ khi xóa danh sách; số chặn là bản ghi, không ứng viên duy nhất; 0 cộng dồn riêng ở30 trong tập."),
("S8","M","D06/N-30; Q4R; C31/EXAMPLE; A13; F01/F02","Lời hứa đầu rõ; hai số99,1 thuộc hai người; bỏ giờ đón, giữ giá dự báo. Không biến tổng cập nhật thành tuyến phản thực tế cả chuyến."),
("S9","M","J28/J31; BIB-v2; C2-17/C2-18","Thêm trích dẫn và số; Uber8 là trung bình, không cận mỗi người; Wardman hai dạng hỏi khác, không khoảng chung."),
("S10","M","OUTLINE CH1–CH3; A09; C10; H01/H02; R40 §2","Câu hỏi ngắn và dễ đọc; bỏ con trỏ; giới hạn về thứ tự chọn chuyển Phạm vi. Ý khớp bảng lộ trình, không sửa tệp Ch4 ngoài phạm vi."),
]
for row in ranked:
    add(*row)

number_section = review.split("## Phần 3. Kiểm số", 1)[1].split("## Thay đổi xếp hạng", 1)[0]
number_rows = []
for line in number_section.splitlines():
    match = re.match(r"^\| (\d+) \|", line)
    if match:
        fields = [field.strip() for field in line.strip("|").split("|")]
        number_rows.append(fields)
assert len(number_rows) == 49
number_changes = {
    7: "Số gốc đúng; bỏ giờ đón khỏi ví dụ và giải thích cơ chế đón muộn ở Phạm vi.",
    9: "Sửa phép tính ở nhận xét: 0,6+99,1×0,031=3,6721; 0,6+307,3×0,031=10,1263. Tọa độ cũ vẫn lệch dưới0,002cm, không đổi số giây hay trục.",
    18: "Giữ +31 và thêm −5 ở120; cả hai trên3.672 yêu cầu.",
    20: "28/34 in cho cả hai luật với cùng ngưỡng; không là lợi thế C.",
    22: "Thêm vị ngữ tới muộn và mẫu số được phục vụ; không đọc như phục vụ292.",
    31: "Bỏ nhãn gộp chung và danh sách; mẫu số yêu cầu/khách được phục vụ ghi theo từng số.",
    32: "Giữ2434/2338/2338 trong văn xuôi;2332 lượt chung bỏ cùng danh sách vì không cần cho câu hỏi mở đầu.",
    37: "Giữ điểm C120 trong một đoạn riêng cuối kết quả.",
    38: "Số chưa dự báo2255/2366 đúng; bỏ khi rút danh sách, giữ điểm có dự báo.",
    41: "Giữ132=98+34; nói rõ phạm vi đã kiểm và mức30–300 của98 lần trước.",
    48: "Giữ định tính, thêm cite đã kiểm và cảnh báo8phút không là cận từng khách.",
}
for fields in number_rows:
    index = int(fields[0])
    decision = "M" if index in {9, 18, 20, 22, 31} else "A"
    add(f"N{index:02}", decision, fields[4], number_changes.get(index, "Số/định tính đúng; giữ khi cần và kiểm trên các nguồn đã chỉ."))

assert len(rows) == 113
assert len({row[0] for row in rows}) == 113
counts_all = Counter(row[1] for row in rows)
counts_p = Counter(row[1] for row in rows if row[0].startswith("P"))
counts_ranked = Counter(row[1] for row in rows if row[0] in {value[0] for value in ranked})
counts_n = Counter(row[1] for row in rows if row[0].startswith("N"))

def show_counts(counter):
    return "; ".join(f"{key}={counter[key]}" for key in ["A","M","R","CANNOT CHECK"])

header = f"""# Round 40 — áp nhận xét Chương 1

## 1. Bản dùng để ghép, quyết định và phạm vi

**Bản dùng để ghép: 05-chuong1-v4-v4.tex.** Các bản 05-chuong1-v4.tex, -v2, -v3 và toàn bộ r30-ch1 được giữ nguyên. Tệp LOG được tạo một lần sau khi chốt bản cuối. Không ghi đè tệp, không sửa các chương khác, danh mục chung hay luận văn.

Đã đọc lại ROUND40-CH1-V4-APPLY.md sau khi tiếp tục; không thấy phụ lục mới. Áp CODEX-PARALLEL-RULES/WRITING-BRIEF, ngoại trừ thước ngân sách trang được ROUND40 cập nhật thành khoảng500tiếng văn xuôi/trang. Không mô phỏng, biên dịch hoặc cài đặt.

A: xác nhận và áp ý sửa; M: nhận phần đúng, sửa phạm vi/diễn đạt hoặc chuyển chỗ để đáp ứng ngân sách; R: bác nội dung câu đề xuất không được bằng chứng hỗ trợ. CANNOT CHECK chỉ dùng nếu không mở được bằng chứng. Một dòng M có thể vẫn giữ nguyên con số.

- 54 chỗ đọc khó (P01–P54): **{show_counts(counts_p)}**.
- 10 thay đổi xếp hạng (M1–M5/S6–S10): **{show_counts(counts_ranked)}**.
- 49 dòng kiểm số (N01–N49): **{show_counts(counts_n)}**.
- Tổng113dòng: **{show_counts(counts_all)}**.

Các nhóm trùng nhau về vị trí sửa: tổng113là số dòng kiểm/ra quyết định, không phải113chỉnh sửa độc lập. Không có số liệu khoa học sai trong bản gốc. N09 sửa số học trong lời nhận xét về tọa độ, không sửa các giây của hình.

**Bác P36:** câu thay thế nói mọi cách trong bảng đều bảo vệ lời hứa. Đo mức thay đổi và hiệu chỉnh giờ đến dự kiến không tự tạo một ràng buộc riêng cho từng khách (J06/J08/C2-15). Thay bằng câu các công trình đo hoặc giới hạn đại lượng khác nhau. Vẫn sửa điểm ngữ pháp của câu cũ.

Mọi quyết định dưới đây được đối chiếu với bản v3 và nguồn trước khi áp. Hỗ trợ đọc độc lập đã chỉ ra các điều kiện N, phạm vi khách đang chờ, sổ tính sau chạy, hai cách hỏi Wardman và giới hạn ba mẫu dừng; người viết mở lại nguồn và kiểm bản cuối.

## 2. Mỗi nhận xét và cách xử lý

"""

def table(values):
    value = "| ID | Quyết định | Bằng chứng | Thay đổi / lý do |\n|---|---|---|---|\n"
    for row in values:
        value += "| " + " | ".join(str(field).replace("|", "/").replace("\n", " ") for field in row) + " |\n"
    return value

content = header + "### 2.1. Chỗ đọc khó\n\n" + table(rows[:54])
content += "\n### 2.2. Thay đổi xếp hạng\n\n" + table(rows[54:64])
content += "\n### 2.3. Dòng kiểm số của nhận xét\n\n" + table(rows[64:])
word_counts = qa["words_opening_sections_1_to_6"]
titles = ["Mở chương","1.1 Bối cảnh","1.2 Ba phần và câu hỏi","1.3 Công trình gần nhất","1.4 Mục tiêu và đóng góp","1.5 Phạm vi","1.6 Cấu trúc"]
content += "\n## 3. Độ dài, bù trang và phần sẽ cắt nếu bố cục vượt\n\n"
content += "| Phần | Tiếng văn xuôi bản cuối | Trang văn xuôi theo500tiếng/trang |\n|---|---:|---:|\n"
for title, number in zip(titles, word_counts):
    content += f"| {title} | {number} | {number/500:.2f} |\n"
content += f"| **Tổng** | **{sum(word_counts)}** | **{sum(word_counts)/500:.2f}** |\n"
content += """

Đếm tiếng cách nhau bởi khoảng trắng, bỏ tiêu đề, hình/bảng, dòng EV, lệnh cite/ref/label; giữ danh sách và khung. Cùng phương pháp của Round30, nên số văn xuôi có thể so được:1.700→2.835tiếng. Bỏ toàn bộ danh sách năm dòng kết quả và con trỏ mục trong CH1–CH3 như ROUND40 yêu cầu. Chuyển các số cần giữ vào đoạn kết quả; giữ điểm C120 ngắn, số khách tới sớm và số đi chung để không làm so sánh một phía. Đoạn đóng góp v3 duy nhất được tách thành các đoạn mục tiêu, đặc tả, kết quả và đối chiếu.

Theo thước500của brief, văn xuôi khoảng5,67trang. Ước riêng hai hình/caption và bảng khoảng1,1–1,3trang, tiêu đề/khoảng cách khoảng0,25–0,35trang: tổng khoảng**7,0–7,3trang**, dưới trần mục tiêu7,5. Đây là ước lượng từ nguồn và thước brief, **không phải số trang PDF đã đo**. Không đổi cỡ chữ thân bài hay giãn dòng để ép trang; giữ cỡ bảng và hình từ bản gốc.

Nếu người ghép dựng ra hơn7,5trang, thứ tự cắt tiếp: (1) rút đoạn khảo sát/định giá ở1.1, đưa số quan sát và chi tiết hai cách hỏi về Chương2, giữ hai trích dẫn và giới hạn giá trị trần; (2) rút điểm C120 còn câu dẫn tới Chương4, giữ120giây trong câu kiểm cộng dồn; (3) bỏ chi tiết nguồn GPS/định vịHamburg ở1.3, giữ khác biệt thiết lập và chưa chạy đối chứng. Có thể tiết kiệm khoảng100–150tiếng. Không cắt sự đối xứng28/34,292/289,−96,+31/−5,37,2/7,4, mẫu số, điều kiện trần hoặc tính thăm dò.

## 4. Kiểm số, cú pháp, nhãn và khóa trích dẫn

Đầu ra đúng cuối:05-chuong1-v4-QA-v2.json; script verify_ch1_v4_v2.py. Script chỉ đọc chương/đích tham chiếu, tính lại số học và ghi đầu ra mới. Mọi ngoặc và môi trường khớp; không có nhãn trùng hoặc cụm bị cấm. Có2hình,1bảng. Kiểm đủ mỗi khối có số và EV; các số mới về ví dụ dựng tay, các ngưỡng, dữ liệu đã xem, mẫu dừng, mức tải và nguồn sản phẩm đều có EV.

Tính lại:C−không trần phục vụ2434→2338, mất96; không trễ60giây2231→2262, thêm31; không trễ120giây2332→2327, giảm5.292/2338=12,5% và289/2338=12,4% sau làm tròn một chữ số;23027,239/31353,407=73,4%. Dự báo+C và dự báo+đệm đều2328lượt ở60giây; đệm2366ở120giây. C120có2322/2379khi dự báo.132=98+34 và1780=1256+524. Số tới sớm7/2434,3/2338,4/2338,44/2434,2/2387 được mở lại ở C120-RESULTS và N-16/N-06/N4B-09. Mẫu số trên yêu cầu và trên khách được phục vụ không trộn.

Nguồn số lưu sẵn: EVIDENCE-REGISTER và các phụ lục1–5; Q4R=S/tang3/w07/analysis/q4-rider-2026-09-30.txt; EXAMPLE=S/optimize/report-extras/example-rider-2026-10-06.txt; C120R=S/tang3/t38c120/C120-RESULTS.md; LOAD=claude-work/load-and-occupancy-2026-10-07.txt; SERV=S/optimize/codex-debate/service-duration-check-2026-10-06.txt. D03 là tệp ranh giới claim được mở trực tiếp. HZ là bản trích Hörl–Zwick được sổ chỉ. Các dòngCh3/4chỉ theo tệp đích của ROUND40.

N09:3,673và10,127là tọa độ xấp xỉ của hình cũ; đúng số học với0,031là3,6721và10,1263. Sai lệch lần lượt0,0009/0,0007cm, không vượt0,002cm của kiểm nguồn. Hình giữ tọa độ cũ và số giây, vì hình có tỉ lệ riêng/xấp xỉ và thay đổi nhỏ không mang ý nghĩa số liệu. Không chép phương trình làm tròn sai của nhận xét như số học chính xác.

Nhãn định nghĩa:chuong:modau;muc:c1-boicanh;muc:c1-cauhoi;muc:c1-lienquan;muc:c1-donggop;muc:c1-phamvi;muc:c1-cautruc;hinh:c1-loihua;hinh:c1-baphan;bang:c1-chodung.

"""
content += "| Ref dùng trong bản cuối | Tệp đã kiểm định nghĩa |\n|---|---|\n"
for ref, path in qa["every_ref"].items():
    content += f"| {ref} | {path} |\n"
content += "\nKiểm mọi ref trên Ch2-v4, Ch3-v4-v3, Ch4A-v5-v3, Ch4B-v10 đúng brief. Thêm Ch5-v2 để xác nhận chuong:ketluan nay đã có. Không còn ref chờ định nghĩa. Phần B-v11 chưa phải tệp đã chốt trong thời điểm kiểm; không nhập số/khẳng định từ candidate-v2. Nhãn phần B mục c4 dùng trong câu hỏi đã được bỏ nên không thêm phụ thuộc.\n"
content += "\nCác khóa cite đều có ở r32-bib/10-tai-lieu-draft-v2.tex: " + ", ".join(qa["citation_keys"]) + ". Không có khóa mới hoặc sửa danh mục chung. uberxshare/moiaexpress/engelhardt2026 được bổ sung vào lời văn; dùng metadata đã kiểm của Round32. Không có chi tiết nơi công bố Hörl–Zwick trong chương.\n"
content += """

## 5. Giới hạn áp nhận xét và việc ghép

- M1:không lấy phép kiểm khác nói chung làm định nghĩaN. Điều kiện trong bản cuối là phương án giữ nguyên hợp lệ về cấu trúc, cùng cách tính giờ trả, phần đã dùng trong trần ở đầu lượt, áp mọi lượt. Không dùng0bị ép như lợi thế C trước không trần.
- M2:không viết C không đúng giờ hơn như khẳng định chung; giữ phạm vi từng đối chứng/ngưỡng. Trước không trần,Cthêm31ở60nhưng mất5ở120.
- M3:đoạn văn HZ bàn khách trên xe sắp trễ nhưng lời dẫn công thức7áp các yêu cầu đã gán cho xe; không áp nhóm hẹp đó cho toàn bộ công thức. Thể hiện mốc kế thừa/nới hạn và phần phạt; không nhận một so sánh chưa chạy là kết quả thực nghiệm.
- M5:sổ lưu các cập nhật; phép chia độ lệch cuối chuyến được tính sau chạy. Các lần dời cộng giữ dấu khi chia độ lệch; trần cộng độ lớn. Bao gồm cả khách đang chờ đã có lời hứa.
- S6:0,535là trung bình theo34kịch bản trên[0,2giờ], còn1,33thuộc thiết lập/ngày đo khác.0giây dừng chỉ được đọc trên3mẫu. U/Cđã cùng bộ chọn, chỉ khác trần; câu hỏi còn mở là thứ tự chọn khác và tương tác với trần.
- S7:các bản ghi chặn không đồng nhất với số ứng viên duy nhất hoặc khách bị từ chối; tập132không gồm mọi thư mục chạy.0cộng dồn riêng ở30chỉ trong tập đã kiểm.
- P52:tiếng Anh lần đầu trong ngoặc được quy tắc cho phép. Không bổ sung ở đây vì nhãn tiếng Anh không tự giúp người ngoài ngành hiểu; dùng giải thích Việt, không viện lý do cấm tiếng Anh tuyệt đối.

Ba câu hỏi vẫn cùng nội dung với bang:c4-lotrinh của phần A:đo/kiểm trần; đánh đổi trước các đối chứng; dự báo/phần còn lại. Chương1viết ngắn và định nghĩa đối chứng, không giữ những câu trỏ mục. Nếu cần đồng nhất chữ tuyệt đối, người ghép có thể dùng chữ CH1–CH3 của bản này cho ô câu hỏi trong bảng lộ trình; không đổi các mục trả lời/đại lượng, và không sửa phần A trong Round40.

Chưa biên dịch hoặc xem PDF theo luật phiên. Không nói bản đã qua kiểm trực quan. Các thay đổi từng lượt được lưu bằng script tạo mới, có đầu ra; tất cả chỉ trong r40-ch1-v4.
"""
with (ROOT / "05-chuong1-v4-LOG.md").open("x", encoding="utf-8", newline="\n") as handle:
    handle.write(content)
summary = {
    "final_file": "05-chuong1-v4-v4.tex",
    "log": "05-chuong1-v4-LOG.md",
    "reader_54": dict(counts_p),
    "ranked_10": dict(counts_ranked),
    "numeric_49": dict(counts_n),
    "all_113": dict(counts_all),
    "words_opening_sections_1_to_6": word_counts,
    "total_words": sum(word_counts),
    "rejected": ["P36: unsupported blanket that all rows protect a promise"],
    "QA_errors": qa["errors"],
}
with (ROOT / "review-log-summary.json").open("x", encoding="utf-8", newline="\n") as handle:
    json.dump(summary, handle, ensure_ascii=False, indent=2)
    handle.write("\n")
print(json.dumps(summary, ensure_ascii=False))
