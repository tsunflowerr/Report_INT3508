"""Exclusively create v4-v2 after final semantic checks; never overwrite."""
from pathlib import Path
ROOT = Path(__file__).resolve().parent
text = (ROOT / "05-chuong1-v4.tex").read_text(encoding="utf-8")
changes = [
    ("điều phối không trần cũng không phải dùng luật phục hồi\nở 0 trong 20.760 quyết định được xác nhận.",
     "điều phối không trần cũng không lần nào phải dùng luật phục hồi\n(0 trong 20.760 quyết định được xác nhận)."),
    ("Tập này gồm 98 lần chạy trước và 34 lần trần 120 giây, không\nbao gồm mọi lần chạy đã lưu.",
     "Tập này gồm 98 lần chạy với trần từ 30 đến 300 giây trước đó và 34 lần trần 120 giây, không\nbao gồm mọi lần chạy đã lưu."),
    ("có 2.338, ít hơn 96 lượt.", "có 2.338, ít hơn 96 lượt."),
    ("Khách đi chung giảm từ 555 trong 2.434 xuống 313 trong 2.338 khách.\n% EV: B01; X3-40; B06; B09; C01; C02; C06; C08; N-09; N-20.",
     "Khách đi chung giảm từ 555 trong 2.434 xuống 313 trong 2.338 khách.\nỞ lời hứa chưa dự báo, số khách tới sớm quá một phút là 7 trong 2.434 và 3 trong 2.338.\n% EV: B01; X3-40; B06; B09; C01; C02; C06; C08; N-09; N-20; C120R:16-19 (tới sớm)."),
    ("2.322 và 2.379 lượt trên 3.672 yêu cầu, với lời hứa dài thêm trung bình 7,3 giây trên 2.387 khách.\nĐiểm này không chỉ ra một mức trần tốt nhất.",
     "2.322 và 2.379 lượt trên 3.672 yêu cầu, với lời hứa dài thêm trung bình 7,3 giây trên 2.387 khách.\nCó 2 trong 2.387 khách tới sớm quá một phút. Điểm này không chỉ ra một mức trần tốt nhất."),
    ("giữ ít quyết định cố định\nđể còn lựa chọn về sau và giữ tính nhất quán về giờ phục vụ.",
     "trì hoãn cam kết\nkhi còn nhiều phương án và giữ tính nhất quán về giờ phục vụ."),
    ("D03:5-9,54-56,83,153-164 (giải thích thuật ngữ, không nhận là mới)",
     "D03:§1-2 (tiền lệ và giải thích thuật ngữ)")
]
applied = 0
for before, after in changes:
    if before == after:
        continue
    assert text.count(before) == 1, before
    text = text.replace(before, after, 1)
    applied += 1
with (ROOT / "05-chuong1-v4-v2.tex").open("x", encoding="utf-8", newline="\n") as handle:
    handle.write(text)
message = f"Created final 05-chuong1-v4-v2.tex exclusively; preserved v4 and all Round30 files; {applied} final clarity/scope changes.\n"
with (ROOT / "finalize-ch1-v4-output.txt").open("x", encoding="utf-8", newline="\n") as handle:
    handle.write(message)
print(message, end="")
