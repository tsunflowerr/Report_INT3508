"""Add the promise-aware generator section to chapter 4, and make every
cross-reference in the report symbolic instead of hand-numbered.

Two jobs in one pass, because the first one shifts section numbers and would
otherwise break the second.

  1. Insert a new section documenting the three levels of promise-aware
     candidate generation and the reorder-capable generator, placed before the
     "directions tried and abandoned" round-up.

  2. Replace every hand-written "mục 4.x" with \\ref to a \\label. Several of
     the existing ones were already stale -- the welfare section is 4.10 but was
     cited as 4.8, the window-ceiling test is 4.8 but was cited as 4.9, the
     comparison with Fielbaum is 4.9 but was cited as 4.8. Symbolic references
     remove the whole class of error.

Every replacement asserts its expected occurrence count, so a silent miss fails
loudly instead of leaving half the document inconsistent.
"""

from __future__ import annotations

import pathlib
import sys

ROOT = pathlib.Path(r"E:/Code/Report_INT3508/ridebound/noi-dung")

# ---------------------------------------------------------------- labels ----

LABELS = {
    "08-chuong4.tex": [
        (r"\section{Thiết lập thực nghiệm}", "muc:thietlap"),
        (r"\section{Quy trách: ai gây ra xáo trộn}", "muc:quytrach"),
        (r"\section{Đường biên: giá của cam kết}", "muc:duongbien"),
        (r"\section{So sánh hai cơ sở tính}", "muc:haicoso"),
        (r"\section{Độ vững với cách đo}", "muc:dovung"),
        (r"\section{Thí nghiệm phụ: bảo đảm một chiều}", "muc:ratchet"),
        (r"\section{Thí nghiệm trôi dạt thật}", "muc:troidat"),
        (r"\section{Phép thử trần cửa sổ đón và một bất biến miền}", "muc:cuaso"),
        (r"\subsection{Mặt cong hai chiều}", "muc:matcong"),
        (r"\subsection{Một bất biến miền chặn tắc đường}", "muc:batbien"),
        (r"\section{Đối chiếu với Fielbaum và Alonso-Mora (2020)}", "muc:doichieu"),
        (r"\section{Phúc lợi: điểm hòa vốn}", "muc:phucloi"),
        (r"\section{Chứng cứ về tính không giả tạo}", "muc:chungcu"),
        (r"\section{Các hướng đã thử và lý do từ bỏ}", "muc:dathu"),
        (r"\section{Hạn chế của thực nghiệm}", "muc:hanche"),
    ],
}

# ------------------------------------------------------------ new section ----

NEW_SECTION = r"""\section{Bộ sinh phương án biết đến lời hứa}
\label{muc:bosinh}

Toàn bộ kết quả từ đầu chương đến đây đều dùng một bộ sinh phương án \emph{không} biết gì về
lời hứa: nó sinh ra các phương án theo tiêu chí vật lý và lịch trình, rồi cổng cam kết mới xóa
đi những phương án vi phạm. Câu hỏi tự nhiên tiếp theo là liệu có thu được gì nếu bộ sinh biết
trước về ngân sách, thay vì để cổng dọn dẹp phía sau. Mục này trả lời bằng phép đo, và câu trả
lời phần lớn là không --- nhưng lý do \emph{tại sao} không lại là một kết quả có giá trị riêng.

\subsection{Ba mức can thiệp và điều kiện để chúng có ý nghĩa}

Chúng tôi tách ý tưởng ``sinh phương án có ý thức về cam kết'' thành ba mức, xếp theo mức độ
xâm lấn tăng dần, vì mỗi mức đòi hỏi một điều kiện khác nhau của dữ liệu để có tác dụng.

\textbf{Mức A --- xếp hạng vị trí chèn.} Bộ sinh vẫn sinh đủ, nhưng ưu tiên những vị trí chèn
làm tiêu ít ngân sách nhất. Mức này chỉ có ý nghĩa nếu mỗi quyết định thực sự có nhiều hơn một
phương án để xếp hạng.

\textbf{Mức B --- cắt tỉa sớm.} Bộ sinh tính một cận dưới cho chi phí ngân sách của cả một
nhánh và bỏ nhánh đó ngay nếu cận dưới đã vượt trần. Mức này chỉ có ý nghĩa nếu hiện có phương
án bị bỏ sót vì hết thời gian hoặc hết chỗ, hoặc nếu tốc độ đang là vấn đề.

\textbf{Mức C --- đặt trước ngân sách.} Không động vào bộ sinh; thay vào đó chèn một tầng
\emph{cảnh báo} vào hàm mục tiêu từ điển của bài toán đóng gói tập hợp, để một phương án còn
trong trần cứng nhưng đã vượt ngưỡng cảnh báo thấp hơn sẽ bị hạ bậc. Ý đồ là làm hệ thống tiêu
ngân sách một cách dè dặt, để dành chỗ cho yêu cầu đến sau.

\subsection{Tập lựa chọn mỏng đến mức nào}

Điều kiện của mức A và mức B đều là mệnh đề về dữ liệu, nên đo được trước khi viết một dòng mã
nào. Hệ thống đã ghi sẵn chẩn đoán cần thiết cho mỗi xe ở mỗi vòng quyết định, trong nhánh
\texttt{executionEvidence/generation/vehicleLosses}. Bảng \ref{bang:mong} tổng hợp trên toàn bộ
panel 20 ô đã niêm phong, cả hai nhánh, tổng cộng $217.736$ quyết định cấp xe.

\begin{table}[htbp]
\centering
\caption{Độ mỏng của tập lựa chọn trên toàn panel niêm phong}
\label{bang:mong}
\small
\begin{tabular}{@{}lrr@{}}
\toprule
\textbf{Đại lượng} & \textbf{B1 (không hứa)} & \textbf{C1 (trần 30 s)}\\
\midrule
Số quyết định cấp xe & 113.064 & 104.672\\
Ứng viên khả thi trước trần / xe & 1,044 & 1,047\\
Ứng viên được giữ lại / xe & 1,044 & 1,047\\
Bị loại vì vật lý hoặc lịch trình / xe & 1,057 & 0,956\\
\midrule
Số lần chạm trần số ứng viên & 0 & 0\\
Số lần cạn ngân sách tính toán & 0 & 0\\
Ứng viên khả thi bị bỏ do trần & 0 & 0\\
Nhánh chưa khai triển bị bỏ & 0 & 0\\
\midrule
Quyết định chỉ có \emph{một} ứng viên & $96{,}04\%$ & $95{,}87\%$\\
Quyết định có từ hai ứng viên trở lên & $3{,}96\%$ & $4{,}13\%$\\
\bottomrule
\end{tabular}
\end{table}

Hai dòng quan trọng nhất là hai dòng bằng nhau: số ứng viên trước trần và số ứng viên sau trần
giống hệt nhau tới ba chữ số thập phân. Bộ giữ ứng viên có cài đặt một trần số lượng, nhưng
trần ấy \emph{chưa bao giờ} chạm trong hai trăm nghìn quyết định.

Hệ quả rất trực tiếp. Mức A là phép toán rỗng: với một ứng viên thì không có gì để xếp hạng, và
việc xếp hạng chỉ có thể tác động lên khoảng bốn phần trăm số quyết định, nơi mà chín phần mười
trường hợp tập chỉ có đúng hai phần tử. Mức B cũng là phép toán rỗng: không có ứng viên khả thi
nào từng bị bỏ, không có nhánh nào chưa được khai triển, nên cắt tỉa sớm không tiết kiệm được
gì; và không có lần nào cạn ngân sách tính toán, nên cũng không có vấn đề tốc độ để giải quyết.

Điều này cũng trả lời một câu hỏi bỏ ngỏ từ chương 3: các kết quả của khóa luận có phải là hệ
quả của việc tìm kiếm bị cắt ngắn hay không. Câu trả lời là không --- tìm kiếm chưa bao giờ bị
cắt. Ràng buộc siết chặt nằm ở tầng vật lý, đúng như phân tích nguyên nhân bị loại đã chỉ ra.

\subsection{Bộ sinh biết sắp xếp lại: một bất biến thứ hai}

Mục 4 của danh sách hướng mở là một bộ sinh có thể \emph{sắp xếp lại} thứ tự các điểm dừng của
hành khách cũ, chứ không chỉ chèn thêm vào giữa. Hóa ra hệ thống đã có sẵn cơ chế ấy: một bộ
dựng mầm sửa chữa lấy một hành khách đang chờ, gỡ cả cặp đón--trả của người đó ra khỏi đuôi khả
biến, rồi chèn lại cặp ấy vào mọi vị trí còn giữ được thứ tự đón trước trả. Một nhánh thực
nghiệm với hạn mức bốn hành khách mỗi xe đã được chạy trên cùng panel, cùng bộ chạy, cùng hạt
giống.

Trước hết, cơ chế này \emph{thực sự} sắp xếp lại, và đó không phải điều hiển nhiên: bộ sinh chèn
thuần chưa một lần đảo thứ tự trong toàn bộ dữ liệu của khóa luận. Bảng \ref{bang:sapxep} cho
thấy sự khác biệt.

\begin{table}[htbp]
\centering
\caption{Hành vi của bộ sinh chèn thuần và bộ sinh biết sắp xếp lại}
\label{bang:sapxep}
\small
\begin{tabular}{@{}lrrrrr@{}}
\toprule
\textbf{Nhánh} & \textbf{Ô} & \textbf{Cập nhật} & \textbf{Sắp lại} & \textbf{Đẩy chặng đầu} & \textbf{Đóng băng sớm}\\
\midrule
B1 --- chèn thuần & 20 & 5.328 & 0 & 57 \ ($1{,}07\%$) & 0\\
C1 --- chèn thuần, trần 30 s & 20 & 4.864 & 0 & 17 \ ($0{,}35\%$) & 0\\
b4 --- biết sắp xếp lại & 20 & 1.978 & 245 & 150 \ ($7{,}58\%$) & 0\\
\bottomrule
\end{tabular}
\end{table}

Chiều \texttt{incumbentOrderInversionCount} của vector ngân sách, vốn luôn bằng không trong mọi
thực nghiệm trước, nay bị tính phí 116 lần với tổng 120 đơn vị. Cơ chế hoạt động đúng như thiết
kế.

Nhưng nhánh này \textbf{hỏng trên 18 trên 20 ô}, với cùng một mã lỗi:
\texttt{LOCKED\_LEG\_MISMATCH} tại chặng đang chạy của một xe. Nguyên nhân là một bất biến thứ
hai của mô hình, khác với bất biến cửa sổ đón ở mục \ref{muc:batbien}, và đáng ghi lại vì nó
phản ánh một bất đồng khái niệm chứ không phải một lỗi cài đặt.

Phía mô hình miền, một điểm dừng chuyển từ đuôi khả biến sang tiền tố đóng băng \emph{khi xe
tới nơi}. Không có chuyển trạng thái nào cho tình huống ``xe đã xuất phát hướng tới''. Phía bộ
mô phỏng, chặng đang chạy bị khóa ngay khi xe lăn bánh, và mọi kế hoạch thay thế có chặng đầu
khác đi đều bị từ chối. Giữa lúc xuất phát và lúc tới, điểm dừng đích nằm ở vị trí đầu của đuôi
khả biến, và bộ sinh biết sắp xếp lại coi nó là sửa được.

Cột cuối của bảng \ref{bang:sapxep} xác nhận điều này ở dạng trực tiếp nhất: trên $12.170$ lần
cập nhật kế hoạch của cả ba nhánh, hệ thống \emph{chưa một lần} đóng băng một điểm dừng trước
khi xe tới, mặc dù kiểu dữ liệu lộ trình cho phép trạng thái đó. Bộ sinh chèn thuần không bao
giờ làm lộ bất đồng này vì nó đẩy chặng đầu rất hiếm --- khoảng một phần trăm số lần cập nhật.
Bộ sinh biết sắp xếp lại đẩy chặng đầu bảy phần trăm, và với khoảng một trăm lần cập nhật mỗi
ô thì việc bắt gặp một chiếc xe đang giữa đường gần như chắc chắn xảy ra.

Trên ô duy nhất chạy trọn vẹn, kết quả cũng đáng ghi: nhánh biết sắp xếp lại phục vụ 99 hành
khách, đúng bằng B1, trong khi C1 phục vụ 92. Cần nói rõ rằng nhánh này chạy với toàn bộ trần
cam kết bị tháo bỏ --- hàm chọn chính sách đưa nó về hồ sơ mục tiêu chi phí thuần và dựng lại
mọi chính sách với trần rỗng --- nên nó so được với B1 chứ không so được với C1. Đọc như vậy thì
kết luận là: thêm khả năng sắp xếp lại vào một bộ điều phối vốn đã tự do hoàn toàn thu được đúng
không hành khách nào. Cỡ mẫu một ô nên đây là chỉ dấu chứ chưa phải kết luận, nhưng nó phù hợp
với phát hiện trung tâm rằng ràng buộc siết chặt là cửa sổ đón chứ không phải thứ tự điểm dừng.

Cuối cùng, tổ hợp mà mục 4 thực sự cần --- sắp xếp lại \emph{cộng với} lời hứa có biên --- hiện
không diễn đạt được: bộ đọc cấu hình từ chối trường sửa chữa khi chính sách không phải nhánh
b4. Muốn trả lời câu hỏi ấy phải sửa mã nguồn ở ba chỗ theo đúng thứ tự: thêm chuyển trạng thái
đóng băng chặng đang bay ở tầng miền, cho chính sách vector cứng nhận hạn mức sửa chữa, và nới
điều kiện kiểm tra cấu hình. Chúng tôi chuyển việc này sang chương hướng phát triển, kèm ghi chú
rằng bằng chứng ở đoạn trên gợi ý phần thưởng nhiều khả năng bằng không.

"""

LEVELC_PLACEHOLDER = r"""\subsection{Đặt trước ngân sách: nhánh duy nhất chạy được}

[CHO KET QUA MUC C]

"""

# --------------------------------------------------------- reference fixes ----

REPLACEMENTS = {
    "06-chuong2.tex": [
        ("được dùng ở mục 4.8 để quy đổi",
         r"được dùng ở mục \ref{muc:phucloi} để quy đổi", 1),
        ("Mục 4.8 sẽ dùng khoảng",
         r"Mục \ref{muc:phucloi} sẽ dùng khoảng", 1),
    ],
    "07-chuong3.tex": [
        ("và kết quả ở mục 4.6 khá bất ngờ",
         r"và kết quả ở mục \ref{muc:ratchet} khá bất ngờ", 1),
        ("điểm sẽ được kiểm chứng ở mục 4.9.",
         r"điểm sẽ được kiểm chứng ở mục \ref{muc:bosinh}.", 1),
        ("đã tỏ ra thiết yếu trong mục 4.6",
         r"đã tỏ ra thiết yếu trong mục \ref{muc:ratchet}", 1),
    ],
    "08-chuong4.tex": [
        ("con số quy trách ở mục 4.2",
         r"con số quy trách ở mục \ref{muc:quytrach}", 1),
        ("hai thang đo được mô tả ở mục 4.3.",
         r"hai thang đo được mô tả ở mục \ref{muc:duongbien}.", 1),
        ("ở mục 4.9, nên có thiên lệch sống sót",
         r"ở mục \ref{muc:batbien}, nên có thiên lệch sống sót", 1),
        ("của mô hình, mô tả ở mục 4.9",
         r"của mô hình, mô tả ở mục \ref{muc:batbien}", 1),
        ("khá trực tiếp và khớp với mục 4.3.4:",
         r"khá trực tiếp và khớp với hình dạng đường biên ở mục \ref{muc:duongbien}:", 1),
        ("chính là cơ chế ratchet ở mục 4.6",
         r"chính là cơ chế ratchet ở mục \ref{muc:ratchet}", 1),
        ("Phép thử trần ở mục 4.9 cho thấy",
         r"Phép thử trần ở mục \ref{muc:cuaso} cho thấy", 1),
        ("Như mục 4.7 đã nêu, panel gốc",
         r"Như mục \ref{muc:troidat} đã nêu, panel gốc", 1),
        ("Bất biến miền ở mục 4.9 chặn phần",
         r"Bất biến miền ở mục \ref{muc:batbien} chặn phần", 1),
    ],
    "09-chuong5.tex": [
        ("mặt cong hai chiều ở mục 4.9.3 cho thấy",
         r"mặt cong hai chiều ở mục \ref{muc:matcong} cho thấy", 1),
        ("Như mục 4.8 đã trình bày chi",
         r"Như mục \ref{muc:doichieu} đã trình bày chi", 1),
        ("Mục 4.7 cho thấy phép so",
         r"Mục \ref{muc:troidat} cho thấy phép so", 1),
        ("Mục 4.9.3 đã dựng mặt cong",
         r"Mục \ref{muc:matcong} đã dựng mặt cong", 1),
        ("Như mục 4.12 đã nêu, hướng này",
         r"Như mục \ref{muc:dathu} đã nêu, hướng này", 1),
        ("Phát hiện ở mục 4.9 --- rằng hệ thống",
         r"Phát hiện ở mục \ref{muc:batbien} --- rằng hệ thống", 1),
    ],
}


def main() -> int:
    errors: list[str] = []
    texts: dict[str, str] = {}

    for name in set(list(LABELS) + list(REPLACEMENTS) + ["08-chuong4.tex"]):
        texts[name] = (ROOT / name).read_text(encoding="utf-8")

    # 1. labels
    for name, entries in LABELS.items():
        text = texts[name]
        for heading, label in entries:
            if text.count(heading) != 1:
                errors.append("tieu de khong duy nhat: {} trong {} ({} lan)".format(
                    heading, name, text.count(heading)))
                continue
            text = text.replace(
                heading, heading + "\n\\label{" + label + "}", 1)
        texts[name] = text

    # 2. new section, placed before the round-up of abandoned directions
    anchor = "\\section{Các hướng đã thử và lý do từ bỏ}"
    text = texts["08-chuong4.tex"]
    if text.count(anchor) != 1:
        errors.append("khong tim thay diem chen cho muc moi")
    else:
        text = text.replace(
            anchor, NEW_SECTION + LEVELC_PLACEHOLDER + anchor, 1)
        texts["08-chuong4.tex"] = text

    # 3. references
    for name, entries in REPLACEMENTS.items():
        text = texts[name]
        for old, new, expected in entries:
            found = text.count(old)
            if found != expected:
                errors.append("thay the hong trong {}: '{}' xuat hien {} lan, "
                              "mong doi {}".format(name, old[:50], found, expected))
                continue
            text = text.replace(old, new, expected)
        texts[name] = text

    if errors:
        print("KHONG GHI GI CA. Loi:")
        for line in errors:
            print("  -", line)
        return 1

    for name, text in texts.items():
        (ROOT / name).write_text(text, encoding="utf-8", newline="\n")
        print("da ghi", name)

    leftover = []
    for name in texts:
        for i, line in enumerate((ROOT / name).read_text(encoding="utf-8")
                                 .splitlines(), 1):
            if "mục 4." in line or "Mục 4." in line:
                leftover.append("{}:{}: {}".format(name, i, line.strip()[:90]))
    print()
    if leftover:
        print("Con lai tham chieu so cung (can kiem tra bang tay):")
        for line in leftover:
            print("  ", line)
    else:
        print("Khong con tham chieu so cung nao trong cac file da sua.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
