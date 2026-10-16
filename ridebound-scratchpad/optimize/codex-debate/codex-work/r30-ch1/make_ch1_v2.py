"""Preserve v1 and exclusively create the shorter, clarified v2."""
from pathlib import Path
ROOT = Path(__file__).resolve().parent
text = (ROOT / "05-chuong1.tex").read_text(encoding="utf-8")
changes = [
    ("Mốc giữ kế hoạch\\\\99,1", "Tổng phần giữ kế hoạch\\\\99,1"),
    ("Hình trên thuộc kịch bản phát triển ngày 13/11/2018, khung 7:00--9:00; mốc giữ kế hoạch được tính lại trong mô hình.",
     "Hình trên thuộc kịch bản phát triển ngày 13/11/2018, khung 7:00--9:00; hai đoạn là tổng các phần ghi trong sổ."),
    ("Mục tiêu là đặt một giới hạn mà bộ điều phối kiểm được trước khi chọn kế hoạch, rồi đo giới hạn ấy được gì\nvà mất gì. Với hãng xe và người đi xe, luật C cho biết mỗi khách có thể bị điều phối dời giờ trả tổng cộng\nnhiều nhất bao nhiêu, kể cả khi dự báo sai; đổi lại, bộ điều phối có thể nhận ít yêu cầu hơn.",
     "Với hãng xe và người đi xe, luật C cho biết mỗi khách có thể bị điều phối dời giờ trả tổng cộng nhiều nhất\nbao nhiêu, kể cả khi dự báo sai. Khóa luận kiểm giới hạn đó và đo cái giá bằng số lượt phục vụ cùng độ dài lời hứa."),
    ("Khóa luận đặc tả và cài đặt trong RideBound luật C: mỗi khách đã được nhận, kể từ khi xác nhận đặt xe,\ncó một trần cố định cho tổng độ lớn các lần dời giờ trả do điều phối trong cả chuyến; phương án vượt trần bị\nloại.",
     "Khóa luận đặc tả và cài đặt luật C trong RideBound: mỗi khách từ khi xác nhận đặt xe có một trần cố định\ncho tổng độ lớn các lần dời giờ trả do điều phối cả chuyến; phương án vượt trần bị loại."),
    ("Luật đi cùng lời hứa theo hồ sơ lịch sử và sổ theo từng khách. Trên 34 kịch bản FleetPy với hệ số tắc đường\ntoàn thành phố từ dữ liệu Manhattan, cùng 3.672 yêu cầu mỗi cấu hình, trần 30 giây phục vụ ít hơn điều phối\nkhông trần 96 lượt, nhưng thêm 31 lượt không trễ quá một phút so với lời hứa đầu không dự báo.",
     "Luật đi cùng lời hứa theo hồ sơ lịch sử và sổ theo từng khách. Trên 34 kịch bản FleetPy với hệ số tắc đường\ntoàn thành phố từ dữ liệu Manhattan (3.672 yêu cầu mỗi cấu hình), trần 30 giây mất 96 lượt phục vụ so với không\ntrần, nhưng thêm 31 lượt không trễ quá một phút so với lời hứa đầu không dự báo."),
    ("Tính không bị ép của\nluật C cần giả thiết (N) ở mục~\\ref{muc:giunguyen} và phần trần đã dùng không vượt giới hạn; điều phối không\ntrần cũng có 0 trong 20.760 quyết định bị ép. Luật C không giữ lời hứa đầu tốt hơn:",
     "Luật C không bị ép, tức không phải dùng miễn trừ để chọn kế hoạch, dưới giả thiết (N) ở\nmục~\\ref{muc:giunguyen} và khi phần trần đã dùng chưa vượt giới hạn; không trần cũng có 0 trong 20.760 quyết\nđịnh bị ép. Trên tập này, luật C không giữ lời hứa đầu tốt hơn:"),
    ("Các kết quả chính dưới đây là số đếm gộp, không phải trung bình theo kịch bản. Mọi số lượt phục vụ hay không trễ\nđều xét trên cùng 3.672 yêu cầu; “không trễ” gồm cả khách tới sớm.",
     "Kết quả chính gộp trên 3.672 yêu cầu; số không trễ gồm cả khách tới sớm:"),
    ("\\item Phục vụ: không trần 2.434 lượt; luật C và luật hạn chót, cùng trần 30 giây, đều 2.338 lượt, có 2.332 lượt chung.",
     "\\item Phục vụ: không trần 2.434 lượt; luật C và luật hạn chót ở mức 30 giây đều 2.338, có 2.332 lượt chung."),
    ("\\item Không trễ quá một phút, chưa dự báo: không trần 2.231 lượt, luật C 2.262; khách trễ là 203 trong 2.434 và\n76 trong 2.338; khách đi chung là 555 trong 2.434 và 313 trong 2.338.",
     "\\item Chưa dự báo, không trễ quá một phút: không trần 2.231 lượt, luật C 2.262. Đi chung: 555 trong 2.434\nvà 313 trong 2.338 khách."),
    ("\\item Có dự báo: luật C và không trần đệm 30 giây cùng 2.328 lượt không trễ quá một phút; ở hai phút là 2.338\nvà 2.366. Tới sớm quá một phút là 4 trong 2.338 và 44 trong 2.434 khách.",
     "\\item Có dự báo, luật C và không trần đệm 30 giây cùng 2.328 lượt không trễ quá một phút; ở hai phút là\n2.338 và 2.366. Sớm quá một phút: 4 trong 2.338 và 44 trong 2.434 khách."),
    ("\\item Trần 120 giây: phục vụ 2.387 lượt; không trễ quá một và hai phút là 2.255 và 2.366; có dự báo là 2.322 và\n2.379, với lời hứa dài thêm trung bình 7,3 giây trên 2.387 khách.",
     "\\item Trần 120 giây phục vụ 2.387 lượt; không trễ quá một và hai phút: 2.255 và 2.366; có dự báo: 2.322 và\n2.379, lời hứa dài thêm trung bình 7,3 giây trên 2.387 khách."),
    ("\\item Cộng dồn: tập 132 lần chạy đã kiểm gồm 98 lần cũ và 34 lần trần 120 giây; chưa chạy đối chứng mỗi lần một trần.",
     "\\item Cộng dồn: 132 lần chạy đã kiểm gồm 98 lần cũ và 34 lần trần 120 giây; đối chứng mỗi lần một trần chưa chạy."),
    ("Chèn khách động, giới hạn giờ đến, gán lại xe, tương đồng tuyến, cam kết tối thiểu, nhất quán thời gian, đo và\nkiểm soát độ bất ổn, bảo vệ từng khách và lời hứa theo dự báo đều có tiền lệ. Phần khóa luận làm là đặc tả,\ncài đặt và kiểm trần đã nêu, cùng sổ và phép đo đánh đổi. Luật C không bảo đảm giờ đến thực tế; các kết quả\nkhông xác nhận lợi ích kinh doanh hay mức hài lòng của khách.",
     "Chèn khách động, giới hạn giờ đến, gán lại xe, tương đồng tuyến, cam kết tối thiểu, nhất quán thời gian, bảo vệ\ntừng khách, kiểm soát độ bất ổn và dự báo đều có tiền lệ. Luật C không bảo đảm giờ đến thực tế. Khóa luận\nkhông xác nhận lợi ích kinh doanh hay mức hài lòng của khách.")
]
for before, after in changes:
    assert text.count(before) == 1, before
    text = text.replace(before, after, 1)
with (ROOT / "05-chuong1-v2.tex").open("x", encoding="utf-8", newline="\n") as handle:
    handle.write(text)
message = "Created 05-chuong1-v2.tex exclusively; preserved 05-chuong1.tex; applied " + str(len(changes)) + " edits.\n"
with (ROOT / "make-ch1-v2-output.txt").open("x", encoding="utf-8", newline="\n") as handle:
    handle.write(message)
print(message, end="")
