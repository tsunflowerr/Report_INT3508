"""Exclusively create the final text and corrected verifier; preserve earlier files."""
from pathlib import Path
ROOT = Path(__file__).resolve().parent
text = (ROOT / "05-chuong1-v2.tex").read_text(encoding="utf-8")
before = "Với hãng xe và người đi xe, luật C cho biết mỗi khách có thể bị điều phối dời giờ trả tổng cộng nhiều nhất\nbao nhiêu, kể cả khi dự báo sai. Khóa luận kiểm giới hạn đó và đo cái giá bằng số lượt phục vụ cùng độ dài lời hứa."
assert text.count(before) == 1
text = text.replace(before, "Hãng xe và khách biết trần tổng độ dời giờ trả do điều phối của mỗi khách, kể cả khi dự báo sai;\nđổi lại có thể phục vụ ít hơn.")
start = text.index("Khóa luận đặc tả và cài đặt", text.index(r"\noindent\textbf{Đóng góp"))
end = text.index("\n% EV:", start)
contribution = r"""Khóa luận đặc tả và cài đặt luật C trong RideBound: kể từ lúc xác nhận đặt xe, mỗi khách có trần cố định cho
tổng độ lớn các lần điều phối dời giờ trả, cộng qua cả chuyến; phương án vượt trần bị loại. Mốc đo là giờ trả
của kế hoạch cũ tính lại ở cùng trạng thái, kế thừa Hörl và Zwick (2022)~\cite{horl2022}; luật C dùng trần chung
không nới theo tắc đường, cùng lời hứa theo hồ sơ lịch sử và sổ từng khách. Trên 34 kịch bản FleetPy với hệ số
tắc đường toàn thành phố từ dữ liệu Manhattan (3.672 yêu cầu mỗi cấu hình), trần 30 giây mất 96 lượt phục vụ
so với không trần, nhưng thêm 31 lượt không trễ quá một phút so với lời hứa đầu không dự báo. Luật hạn chót
30 giây phục vụ cùng số lượt, nhưng tính cả giao thông nên phá luật với ít nhất một khách ở 28 trong 34 kịch bản.
Luật C không tính phần này. Luật C không bị ép (phải dùng miễn trừ) nếu giả thiết (N) ở mục~\ref{muc:giunguyen}
được thỏa và phần trần đã dùng không vượt giới hạn; không trần cũng có 0 trong 20.760 quyết định bị ép.
So với lời hứa đầu không dự báo, ở ngưỡng trễ 30 giây, luật C có 292 trong 2.338 khách được phục vụ (12,5\%),
hạn chót có 289 trong 2.338 (12,4\%), gộp theo khách. Khi có dự báo, không trần đệm 30 giây hòa luật C ở ngưỡng
một phút và hơn ở hai phút; lời hứa dài thêm trung bình 37,2 thay vì 7,4 giây, gộp trên 2.434 và 2.338 khách
được phục vụ. Trong 132 lần chạy luật C đã kiểm toàn bộ bản ghi chặn, 3 trong 1.780 bản ghi chỉ bị chặn do
cộng dồn, đều ở trần 120 giây; tác dụng lên kết quả chưa được đo."""
text = text[:start] + contribution + text[end:]
changes = [
    ("Trên tập kiểm tra chính, khi điều phối không trần, 134", "Trên tập kiểm tra chính, khi điều phối không trần (vẫn khóa xe và điểm đón, trả), 134"),
    ("% EV: C21; C24; C4A-03", "% EV: A07; A08; C21; C24; C4A-03"),
    ("\\item Phục vụ: không trần 2.434 lượt; luật C và luật hạn chót ở mức 30 giây đều 2.338, có 2.332 lượt chung.",
     "\\item Phục vụ: không trần 2.434 lượt; luật C và hạn chót 30 giây đều 2.338, có 2.332 lượt chung."),
    ("\\item Chưa dự báo, không trễ quá một phút: không trần 2.231 lượt, luật C 2.262. Đi chung: 555 trong 2.434\nvà 313 trong 2.338 khách.",
     "\\item Chưa dự báo: không trễ quá một phút 2.231 lượt khi không trần, 2.262 với luật C; đi chung 555 trong\n2.434 và 313 trong 2.338 khách."),
    ("\\item Cộng dồn: 132 lần chạy đã kiểm gồm 98 lần cũ và 34 lần trần 120 giây; đối chứng mỗi lần một trần chưa chạy.",
     "\\item Cộng dồn: 132 lần chạy gồm 98 lần cũ và 34 lần trần 120 giây; đối chứng mỗi lần một trần chưa chạy."),
    ("Chèn khách động, giới hạn giờ đến, gán lại xe, tương đồng tuyến, cam kết tối thiểu, nhất quán thời gian, bảo vệ\ntừng khách, kiểm soát độ bất ổn và dự báo đều có tiền lệ. Luật C không bảo đảm giờ đến thực tế. Khóa luận\nkhông xác nhận lợi ích kinh doanh hay mức hài lòng của khách.",
     "Chèn khách động, giới hạn giờ đến, gán lại xe, tương đồng tuyến, cam kết tối thiểu và nhất quán thời gian đã\ncó tiền lệ. Luật C không bảo đảm giờ đến thực tế; khóa luận không xác nhận lợi ích kinh doanh hay mức hài lòng.")
]
for before, after in changes:
    assert text.count(before) == 1, before
    text = text.replace(before, after, 1)
with (ROOT / "05-chuong1-v3.tex").open("x", encoding="utf-8", newline="\n") as handle:
    handle.write(text)
verifier = (ROOT / "verify_ch1_v2.py").read_text(encoding="utf-8")
verifier = verifier.replace('"05-chuong1-v2.tex"', '"05-chuong1-v3.tex"').replace('"05-chuong1-v2-QA-v2.txt"', '"05-chuong1-v3-QA.txt"')
with (ROOT / "verify_ch1_v3.py").open("x", encoding="utf-8", newline="\n") as handle:
    handle.write(verifier)
message = "Created final 05-chuong1-v3.tex exclusively; preserved v1/v2. Corrected contribution counting is in verify_ch1_v3.py.\n"
with (ROOT / "make-ch1-v3-output.txt").open("x", encoding="utf-8", newline="\n") as handle:
    handle.write(message)
print(message, end="")
