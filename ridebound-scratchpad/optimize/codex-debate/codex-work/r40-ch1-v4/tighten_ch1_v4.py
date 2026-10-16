"""Final exclusive pass: proof scope, ledger semantics, and budget cuts."""
from pathlib import Path
ROOT = Path(__file__).resolve().parent
text = (ROOT / "05-chuong1-v4-v3.tex").read_text(encoding="utf-8")
changes = [
    ("Chương này giải thích vì sao giờ trả đã hứa, tức giờ khách được báo sẽ tới nơi, có thể bị dời trong dịch vụ đi\nchung xe. Chương chia độ lệch giữa giờ tới thực tế và lời hứa đầu thành ba phần, rồi nêu cách xử lý, câu hỏi\nnghiên cứu, đóng góp và phạm vi của khóa luận.",
     "Chương này giải thích vì sao giờ khách được báo sẽ tới nơi có thể bị dời. Chương chia độ lệch giữa giờ tới\nthực tế và lời hứa đầu thành ba phần, rồi nêu cách xử lý, câu hỏi nghiên cứu, đóng góp và phạm vi."),
    ("Hai khách trong Hình~\\ref{hinh:c1-loihua} minh họa hai chỗ cần xử lý: giới hạn việc\nđiều phối dời giờ trả và tính trước mức tăng thời gian đi.",
     "Hai khách trong Hình~\\ref{hinh:c1-loihua} minh họa phần tính cho điều phối và dự báo."),
    ("Các giờ đồng hồ làm tròn tới giây; độ lệch được tính trước khi làm tròn.", ""),
    ("Sổ theo từng khách: ghi phần còn lại", "Sổ theo từng khách: tính phần còn lại"),
    ("Sổ ghi cả ba phần;", "Sổ cho phép tính cả ba phần;"),
    ("Sổ theo từng khách ghi các lần cập nhật và cho phép tính cả ba phần, để biết dự báo đang dùng chưa giải\nthích được bao nhiêu.",
     "Sổ theo từng khách ghi các lần cập nhật. Sau lần chạy, sổ cho phép tính cả ba phần và phần dự báo chưa giải\nthích được."),
    ("Dời sớm hay dời muộn đều cộng vào; mức chính được thử là 30 giây.",
     "Dời sớm hay dời muộn đều cộng vào; mức chính được thử là 30 giây. Khi chia độ lệch, dời muộn cộng, dời sớm\ntrừ; riêng trần cộng độ lớn."),
    ("% EV: X3-37 (ví dụ dựng tay); A01; A02; A06; X3-27.",
     "% EV: X3-37 (ví dụ dựng tay); A01; A02; A06; X3-27; X3-12 (cộng giữ dấu khi chia độ lệch)."),
    ("khách bị dời nhiều nhất có tổng phần tính cho điều phối 590,1 giây", "khách bị dời nhiều nhất có tổng độ lớn phần tính cho điều phối 590,1 giây"),
    ("Các nghiên cứu trước đã đo mức giờ hứa thay đổi trong chuyến, chặn việc đổi giờ khi chọn kế hoạch và đặt\ngiới hạn riêng cho từng khách. Bảng~\\ref{bang:c1-chodung} so các cách đó ở hai điểm: đại lượng được xét và cách\nxử lý thời gian đi thay đổi. Chương~\\ref{chuong:coso} trình bày chi tiết.",
     "Các nghiên cứu trước đã đo mức giờ hứa thay đổi, chặn việc đổi giờ khi chọn kế hoạch và đặt giới hạn riêng\ntừng khách. Bảng~\\ref{bang:c1-chodung} so đại lượng được xét và cách xử lý thời gian đi thay đổi."),
    ("Tính lại tuyến cũ; nới hạn trả cho khách trên xe sắp trễ (công thức 7); phạt phần vượt hạn gốc",
     "Tính lại tuyến cũ; nới hạn trả theo giờ tính lại (công thức 7); phạt phần vượt hạn gốc"),
    ("Giới hạn này không bảo đảm giờ tới: khách vẫn có thể tới muộn khi thời gian đi tăng. Cái giá được đo bằng\nsố lượt phục vụ, số khách đi chung và độ dài lời hứa.",
     "Cái giá được đo bằng số lượt phục vụ, số khách đi chung và độ dài lời hứa."),
    ("Các số không trễ được xét trên 3.672 yêu cầu, gồm cả khách tới sớm; yêu cầu không\nđược phục vụ không được tính là kịp.",
     "Số không trễ tính trên toàn bộ 3.672 yêu cầu và gồm cả khách tới sớm."),
    ("ở mọi lượt xe có phương án giữ nguyên kế hoạch, giờ trả của phương án\nđó được tính bằng đúng cách tính mốc so sánh, và phần đã dùng chưa vượt trần",
     "ở mọi lượt xe có phương án giữ nguyên kế hoạch hợp lệ về cấu trúc, giờ trả của phương án\nđó được tính bằng đúng cách tính mốc so sánh, và phần đã dùng ở đầu lượt chưa vượt trần"),
    ("Một hạn chót nới tới giá trị lớn hơn giữa hạn cũ và giờ\ntrả tính lại cũng cho qua phương án giữ nguyên, theo định nghĩa; biến thể này chưa được chạy làm đối chứng.",
     "Theo định nghĩa, hạn chót nới tới giờ trả tính lại nếu giờ đó muộn hơn hạn cũ cũng cho qua phương án\ngiữ nguyên; biến thể này chưa được chạy làm đối chứng."),
    ("\\textbf{Khóa luận không nhận là mới.} Mốc tuyến cũ tính lại và việc nới hạn trả đã có ở Hörl và\nZwick~\\cite{horl2022}; đo, kiểm soát việc đổi giờ và đánh đổi với phục vụ đã có ở Fielbaum và\nAlonso-Mora~\\cite{fielbaum2020}. Bảo vệ từng khách, hạn chót từ lời mời và lời hứa theo dự báo đều có\ntiền lệ~\\cite{elmi2026,schulz2026,hu2022}.",
     "\\textbf{Khóa luận không nhận là mới.} Mốc tuyến cũ tính lại và nới hạn trả; đo, kiểm soát việc đổi giờ và\nđánh đổi với phục vụ; bảo vệ từng khách; hạn chót từ lời mời; lời hứa theo dự báo đều có\ntiền lệ~\\cite{horl2022,fielbaum2020,elmi2026,schulz2026,hu2022}."),
    ("\\textbf{Phần khóa luận làm} là đặc tả, cài đặt, kiểm trần riêng từng khách và đo đánh đổi. Trên tập đã đo,\nluật C phục vụ bằng luật hạn chót; so với cách đệm có dự báo, nó hòa ở ngưỡng một phút và kém ở hai phút.\nLuật C không bảo đảm giờ tới thực tế. Sổ không kết luận ai có lỗi, và phần còn lại không phải phần\nkhông thể biết trước. Kết quả không suy rộng sang thành phố, mức tải hay mạng đường khác, không xác nhận\nlợi ích kinh doanh hay mức hài lòng.",
     "\\textbf{Phần khóa luận làm} là đặc tả, cài đặt, kiểm trần từng khách và đo đánh đổi. Luật C phục vụ bằng\nluật hạn chót; so với cách đệm có dự báo, nó hòa ở một phút và kém ở hai phút. Luật C không bảo đảm giờ tới.\nSổ không kết luận ai có lỗi; phần còn lại không phải phần không thể biết trước. Kết quả không suy rộng\nsang thành phố, mức tải hay mạng khác, không xác nhận lợi ích kinh doanh hay mức hài lòng."),
]
for before, after in changes:
    assert text.count(before) == 1, before
    text = text.replace(before, after, 1)
with (ROOT / "05-chuong1-v4-v4.tex").open("x", encoding="utf-8", newline="\n") as handle:
    handle.write(text)
verifier = (ROOT / "verify_ch1_v4.py").read_text(encoding="utf-8")
verifier = verifier.replace('"05-chuong1-v4-v3.tex"', '"05-chuong1-v4-v4.tex"').replace('"05-chuong1-v4-QA.json"', '"05-chuong1-v4-QA-v2.json"')
verifier = verifier.replace('"phần đã dùng chưa vượt trần"', '"phần đã dùng ở đầu lượt chưa vượt trần"')
verifier = verifier.replace('for value in ["0.239", "0.191"]:\n    pass\n', '')
with (ROOT / "verify_ch1_v4_v2.py").open("x", encoding="utf-8", newline="\n") as handle:
    handle.write(verifier)
message = f"Created final 05-chuong1-v4-v4.tex and verifier exclusively; {len(changes)} scoped clarifications/cuts; prior files retained.\n"
with (ROOT / "tighten-ch1-v4-output.txt").open("x", encoding="utf-8", newline="\n") as handle:
    handle.write(message)
print(message, end="")
