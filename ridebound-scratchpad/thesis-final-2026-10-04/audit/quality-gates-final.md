# Quality gates của bản bàn giao

Ngày05/10/2026. Tệp duy nhất bàn giao chính: `thesis_final.pdf`,68trang vật lý,
594610bytes, SHA-256
`e7a4712663ad2167f2bbbffd7330fa0c64a580964cff558b3d3dc2ecba14454c`.
PDF này có cùng bytes với bản dựng được kiểm qua68ảnh `final-layout-v4`.

| Gate | Kết quả | Chứng cứ và phạm vi |
|---|---|---|
| 1 Scientific integrity | PASS | `claim-evidence-matrix.csv`34claim, `evidence-audit.md`, ba phản biện niêm phong và kiểm hậu phản biện. Giữ H6FAIL, giả thiếtH có điều kiện, không nhận phép chiếu là nhân quả thuần hoặc T38 là bảo đảm quần thể. |
| 2 Citation integrity | PASS | `literature-audit.md`/metadata nguồn chính;24mục hiện dùng đều được trích, không thiếu/trùng. Metadata27mục gốc đã đối chiếu, chỉ giữ nguồn phục vụ bản cuối. DatasetZenodo bổ sung được kiểm riêng. |
| 3 Numerical consistency | PASS | `forensic-consistency.json`:123/123; `numerical-consistency.csv`:13thước đo truy vị trí; `all-numbers-final-pdf.csv`:1869token số/ngữ cảnh. Phân biệt giây/ms, pp/phần trăm, trung bình ô/tỉ lệ gộp, điểm phủ/biên thực. Không còn mâu thuẫn số trung tâm. |
| 4 Novelty | PASS | Fielbaum2020, Elmi2026, Schulz2026, Haferkamp2024 và các nguồn nhất quán/ổn định được ghi đúng phạm vi. Không nhận dynamicinsertion, ETA, reassignment, leastcommitment hoặc phục hồi là mới. |
| 5 Readability | PASS | Ch1nêu vấn đề/RQ/phạm vi; Ch2tiền lệ; Ch3ba mốc từ ví dụ rồi định nghĩa/định lý/thuật toán; Ch4tách mức bằng chứng; Ch5trả lời RQ và giới hạn. `defense-questions.md`32câu đều có vị trí căn cứ bản cuối. |
| 6 Vietnamese | PASS | Kiểm tiếng Việt sau phản biện, sửa Proof/thuatngu/56lượt chạy; thuật ngữ Anh còn ở định nghĩa lần đầu, mã nguồn, tiêu đề chính thức hoặc Abstract/bìa Anh. Không tùy tiện dùng panel/runner/adapter trong văn xuôi đã có tên Việt. |
| 7 Figures | PASS | Năm hình có nhiệm vụ giải thích cơ chế, chi phí phục vụ, dự đoán khả thi, chênh ghép cặp và điểm T38. Dữ liệu figure lấy từ bảng đã kiểm; một hình ví dụ dựng được ghi rõ. Vector, Times≥11pt, không đụng nhãn; Times là lựa chọn theo chuẩn người dùng, không ép sans-serif của validator Nature. |
| 8 Tables | PASS |14bảng đánh số, đều có lời gọi; hai bảng thuật ngữ không đánh số. Rõ đơn vị, mẫu số, cách gộp, phiên bản và nguồn; kiểm từng trang không có overflow/chồng/cắt ô. |
| 9 Page count | PASS |68trang vật lý≤80, kể cả hai bìa/phần đầu/ba trang tài liệu. Không tăng trang chỉ để chạm khoảng ưu tiên72–78. |
| 10 PDF visual QA | PASS | Root001–012+066–068:15trang; A013–030:18; B031–048:18; C049–065:17. Tổng68/68 ảnh riêng kích thước đầy đủ, cùng SHA, không phát hiện lỗi bố cục. Các trang đuôi chương gần trắng đã được sửa. |

`final-pdf-integrity.json` xác nhận22font đều nhúng,237liên kết có đích hợp lệ,
92bookmark, footerliên tục và A4. `tex-final-consistency.json` xác nhận Times
NewRoman13pt, giãn1,5, lề3/2/2/2cm,40label/46refs. LogTeX không có error,
overfull, underfull, undefinedcitation/reference, missingglyph hoặc duplicateanchor.
Các cảnh báo môi trường Tectonic về đường dẫn font Windows/Fontconfig được giữ
minh bạch; không ảnh hưởng font nhúng hoặc kết quả hiển thị đã kiểm.

Bản gốc18/18tệp, packet76/76tệp và ba báo cáo phản biện giữ băm. Báo cáoA có
lỗi encoding trong tệp trả về, đã được ghi ở synthesis; không sửa báo cáo hoặc
dựng lại một bản phản biện giả. Lượt kiểm sau phản biện tách khỏi ba lượt độc lập.
Không chạy lại mô phỏng, đổi bộ thực thi ghim, xóa dữ liệu/kết quả hoặc nhận
baseline kiểm thử implementation mới.

**Thông tin hành chính còn thiếu:** tên/học hàm người hướng dẫn trên hai bìa.
Giữ chỗ `[chờ bổ sung]`/`[to be filled]` đã công bố; cần tác giả điền trước nộp
chính thức. Đây không phải một quality gate khoa học được giả vờ đã giải quyết.
