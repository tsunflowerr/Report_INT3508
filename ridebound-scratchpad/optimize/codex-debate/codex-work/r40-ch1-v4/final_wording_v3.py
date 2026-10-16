"""Preserve v4/v4-v2 and exclusively create the final wording pass."""
from pathlib import Path
ROOT = Path(__file__).resolve().parent
text = (ROOT / "05-chuong1-v4-v2.tex").read_text(encoding="utf-8")
changes = [
    ("trị của độ tin cậy trong dịch vụ đi chung.", "trị của thời gian đi và mức ổn định của thời gian đó trong dịch vụ đi chung."),
    ("luật C có 292 trong 2.338 khách\n(12,5\\%), còn luật hạn chót có 289 trong 2.338 (12,4\\%), gộp theo khách.",
     "luật C có 292 khách tới muộn trong 2.338 khách được phục vụ\n(12,5\\%); luật hạn chót có 289 trong 2.338 (12,4\\%), gộp theo khách."),
    ("với tốc độ từ dữ liệu GPS của TomTom", "với tốc độ từ dữ liệu định vị của TomTom"),
]
for before, after in changes:
    assert text.count(before) == 1, before
    text = text.replace(before, after, 1)
with (ROOT / "05-chuong1-v4-v3.tex").open("x", encoding="utf-8", newline="\n") as handle:
    handle.write(text)
message = "Created final 05-chuong1-v4-v3.tex exclusively; explicit late-rider predicate, plain reliability wording, and positioning-data wording. Earlier files retained.\n"
with (ROOT / "final-wording-v3-output.txt").open("x", encoding="utf-8", newline="\n") as handle:
    handle.write(message)
print(message, end="")
