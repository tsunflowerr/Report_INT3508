# R32. Chương 5 và phụ lục (bản v2 của Codex): người đọc ngoài ngành, giảng viên chấm, kiểm số

- **Tệp được nhận xét (chỉ đọc):** `S/optimize/codex-debate/codex-work/r31-ch5/10-chuong5-v2.tex` (47 dòng; gọi là
  "Ch5") và `11-phuluc-v2.tex` (121 dòng; gọi là "PL"); `r31-NOTES.md`. Không đọc hai tệp không hậu tố. Số dòng "L…" là
  số dòng của tệp tương ứng. Ch5 viết mỗi đoạn trên một dòng: L6 là đoạn mở, L12/L15/L18 là ba đoạn của 5.1, L24/L27 là
  5.2, L33/L36/L39/L42/L45 là năm hướng của 5.3.
- **Ngữ cảnh đã đọc:** `ROUND31-CH5-APPX-WRITER.md`; `CODEX-PARALLEL-RULES.md`; `WRITING-BRIEF.md`; `OUTLINE-V2.md`
  §0–3, §5 (Chương 4, Chương 5, Phụ lục), §6, §7; `ASSEMBLY-NOTES.md`; `style/STYLE-GUIDE-VI.md` (mục 1.13–1.14, quy tắc
  29–33, mục dung hòa 5–6); `style/GLOSSARY-VI-v2.md`; bản luận văn hiện tại `noi-dung/09-chuong5.tex:85-105`.
- **Nguồn kiểm số:** Ch4A **v5-v3** (`codex-work/r36-ch4a-v5/08-chuong4-phanA-v5-v3.tex`, đọc trọn); Ch4B **v10**
  (`drafts/09-chuong4-phanB-v10.tex`, đọc trọn); Ch3 v4-v3 (dòng 236–270, 360–470, 700–744); Ch1 v3 (dòng 200–273); sổ
  chính và phụ lục 1–4, 6 (các dòng được trỏ); `TESTRUN-45f8026-2026-10-12.md`; `R26-CH3-OPEN-QUESTIONS-CODEX.md` Q2,
  Q8; `E:/Code/RideBound/docs/08-algorithms-baselines-and-solver.md:15-32`; `codex-work/r32-bib/10-tai-lieu-draft-v2.tex`.
- **Mở thêm để kiểm (chỉ đọc):** `tang3/t38/split-t38-v1.json` (toàn bộ); `tang3/t38/run_t38.py:36-58`; log
  `C:/RideBoundData/research/testrun-45f8026-eollf-dirty-fullrun-2026-10-13.log` (cuối tệp: 9 dòng "Passed!", tổng
  10 + 191 + 138 + 108 + 82 + 201 + 14 + 133 + 148 = 1.025, `exit=0`, `2026-10-13T13:42:21+07:00`); danh sách thư mục
  `E:/RideBoundData/wp14r/development-v6-ledger/` (160 thư mục = 16 kịch bản × 10 cấu hình) và
  `C:/RideBoundData/research/tier3-forecast-v1/` (9 thư mục `C-30-…`, 16 `C-30F-…`, 17 `Mplus-30F-…`, 1 `Mplus-30-…`);
  sự tồn tại của `runner-tier3-v2`, `tier3-t38-v1`, `tier3-t38c120-v1`, `tier3-w07-v1`, `tier3-w07x-v1`,
  `fixtures-panelA-v1`, `fixtures-w07-v1`, `fixtures-snow-v1`.
- **Script chỉ đọc (scratchpad của phiên):** `r32/refs.py` gom mọi `\label` của Ch1 v3, Ch2 v4, Ch3 v4-v3, Ch4A v5-v3,
  Ch4B v10, Ch5 v2, PL v2 (bỏ dòng `%`), rồi giải mọi `\ref`/`\eqref` của Ch5 và PL: 0 nhãn trùng, 0 tham chiếu chưa định
  nghĩa. `r32/sentlen.py`: chỉ một câu dài hơn 35 tiếng (Ch5 L15, 39 tiếng). Cái khó của bản này không nằm ở độ dài câu
  mà ở mật độ thuật ngữ và lối viết ghi chú.

## Nhận định chung (năm dòng)

1. **Số liệu gần như sạch.** Trong khoảng 75 số và nhận dạng đã kiểm (50 nhóm ở Phần 3), chỉ **1 sai**: đoạn kiểm thử của Phụ lục C (PL
   L119) dùng kết quả cũ ngày 12/10 (1.024/1.025, cộng 1/1 khi chạy riêng). Bản ghi mới nhất là **1.025/1.025 trong một
   lần chạy ngày 13/10/2026** (TESTRUN:18; log đã mở). Chương 3 đã viết "cả 1.025 … đều đạt", nên phụ lục hiện mâu thuẫn
   với chính câu trỏ tới nó.
2. **Chỗ hỏng lớn nhất về độ trung thực nằm ở 5.1, đoạn đầu.** Đoạn nêu "luật hạn chót … phá lời hứa … ở 28 trong 34
   kịch bản" nhưng bỏ vế cân bằng mà Ch1 v3:212–213 và Ch4A:355–359 đều có: đo bằng cùng thước, luật C có 292 và luật
   hạn chót có 289 trong 2.338 khách tới muộn quá 30 giây, cả hai ở 28/34 kịch bản. Đoạn cũng nêu "+31 lượt ở một phút"
   nhưng bỏ "−5 lượt ở hai phút" (2.327 so với 2.332). Đoạn không có con số so sánh cho cái luật C mua được (29,2 giây so
   với 590,1 giây), và không nói đây là kết quả mô phỏng.
3. **Phụ lục chưa phục vụ đủ các câu trỏ tới nó.** Ch4A:226 trỏ Phụ lục A để nói mức 30 giây lấy từ tập tĩnh, nhưng A
   không nhắc 30 giây, lại trỏ sang `muc:c4-taptu`, mục không nói gì về tập tĩnh. Ch3:735 trỏ Phụ lục C cho yêu cầu "bản
   dựng lại phải cho đúng kết quả cũ", nhưng C không có câu nào về việc này. Phụ lục B không có câu nào trỏ tới.
4. **Người ngoài ngành đọc Chương 5 rất vất vả.** Câu ngắn, nhưng dày thuật ngữ chưa giải thích ở chương này: "phần
   tính cho điều phối", "sổ", "đệm", "vế cộng dồn", "bản ghi chặn", "quỹ đạo", "bộ chọn". Phụ lục C viết theo lối ghi chú
   ("Số dùng: chính 170 lần…", "Trễ dùng ngưỡng lớn hơn hẳn…"), kèm mã nội bộ LOCKS/B1/C1 không xuất hiện ở đâu khác.
5. **Các yêu cầu cứng đều đạt.** 5.3 có đúng 5 hướng, phép thử bộ chọn × trần đứng đầu, không có ước lượng giờ công.
   Không có chữ "niêm phong", "đăng ký trước", "dự đoán" hay "mong đợi". Có một chỗ gần với bộ máy kế hoạch: "chỉnh khoảng
   dự phòng trong phép thử riêng" (PL L84; REG C17 là phép thử độ phủ γ của kế hoạch T3.8), một phép thử không được báo ở
   đâu. Mọi đoạn có dòng `% EV:`. Mọi `\cite` (`horl2022`, `fielbaum2020`, `schulz2026`) có trong
   `r32-bib/10-tai-lieu-draft-v2.tex:20,27,34`.

---

## Phần 1. Người đọc ngoài ngành

Vai: sinh viên năm cuối ngành khác, đọc Chương 5 sau khi đã lướt Chương 4, rồi lật Phụ lục để kiểm.

**Nhận xét chung.**
- **Ba "phần" không được nhắc lại.** Ba đoạn 5.1 mở bằng "Với phần tính cho điều phối", "Với phần được hồ sơ tắc đường
  lịch sử giải thích", "Với phần còn lại". Đoạn mở chương (L6) không nói đó là ba phần của cái gì. Người đọc chỉ đọc
  Chương 5 (giám khảo thường làm vậy) không hiểu "phần còn lại" là phần nào.
- **Tiếng Anh và mã nội bộ.** Ch5 không có từ tiếng Anh. PL có các mã mà người đọc không giải được: LOCKS, B1, C1
  (L87); `runner-tier3-v2`, `45f8026`, `1ce15e92` (L110, không có chữ nào nói đây là tên bản bộ chạy và mã phiên bản mã
  nguồn); "LF" (L119); `s10` trong mã kịch bản (L63). Theo STYLE mục dung hòa 6, đường dẫn và tên mã được phép ở phụ
  lục; vấn đề là chúng **không được giải nghĩa**.
- **Lối ghi chú thay cho câu.** PL L113 và L116 gồm các mệnh đề cụt nối bằng dấu chấm phẩy. Người đọc phải tự đoán chủ
  ngữ và động từ.
- **Ký hiệu luật trong câu văn.** PL L113 viết "C-30 dùng bản thay thế…" và "thêm 34 lần C-120". OUTLINE §1 chỉ cho dùng
  ký hiệu luật trong bảng.

### Các chỗ khó (40 chỗ)

Mỗi mục: dòng; câu; vì sao khó; câu đề xuất (giữ nghĩa và số). Các đoạn cần viết lại cả đoạn được cho ở phần "Thay đổi
xếp hạng"; ở đây chỉ ghi câu thay thế ngắn.

**Chương 5**

- **H1. Ch5 L6.** «Khóa luận đã đặc tả, cài đặt và đo trần phần dời lời hứa giờ trả do điều phối của từng hành khách.»
  - Vì sao: chuỗi danh từ "trần phần dời lời hứa giờ trả do điều phối của từng hành khách" có sáu tầng. "Đo trần" có thể
    đọc là "đo cái trần" hay "đo dưới trần". Câu không nói đây là đánh giá trên mô phỏng.
  - Đề xuất: «Khóa luận đã đặc tả, cài đặt và đánh giá trên mô phỏng một trần cho phần giờ trả bị dời do điều phối của
    từng hành khách trong dịch vụ đi chung xe.»
- **H2. Ch5 L6.** «Chương này tổng kết kết quả, hạn chế và hướng phát triển.»
  - Vì sao: không giới thiệu ba phần mà ba đoạn 5.1 dùng làm khung.
  - Đề xuất: «Chương này tóm tắt kết quả theo ba phần của độ lệch giờ trả so với lời hứa đầu: phần tính cho điều phối,
    phần được hồ sơ tắc đường lịch sử giải thích và phần còn lại; sau đó nêu hạn chế và hướng phát triển.»
- **H3. Ch5 L12.** «Với phần tính cho điều phối, luật C giới hạn tổng độ lớn các lần dời giờ trả của mỗi khách qua cả
  chuyến.»
  - Vì sao: "Với phần…" là khung không rõ; câu không nói ai dời và dời trong giai đoạn nào.
  - Đề xuất: «Phần tính cho điều phối: luật C giới hạn, cho mỗi khách đã được nhận, tổng độ lớn các lần bộ điều phối
    dời giờ trả trong cả chuyến.»
- **H4. Ch5 L12.** «Mốc so sánh là giờ trả tính lại khi giữ nguyên kế hoạch cũ, tiếp nối mốc trong công thức 7 của Hörl
  và Zwick.»
  - Vì sao: "tiếp nối mốc" mơ hồ; người đọc không biết mốc này là của Hörl và Zwick hay của khóa luận.
  - Đề xuất: «Mỗi lần dời được đo so với giờ trả tính lại nếu xe giữ nguyên kế hoạch cũ; mốc này đã có trong công thức 7
    của Hörl và Zwick.»
- **H5. Ch5 L12.** «So với lời hứa đầu không dự báo, số lượt không trễ quá một phút là 2.262 thay vì 2.231 trên 3.672
  yêu cầu.»
  - Vì sao: thiếu chủ ngữ (2.262 là của luật nào?); "thay vì" khiến người đọc phải đoán số nào thuộc luật nào.
  - Đề xuất: «So với lời hứa đầu không dự báo, luật C có 2.262 lượt không trễ quá một phút, điều phối không trần có
    2.231, trên 3.672 yêu cầu.»
- **H6. Ch5 L12.** «Luật hạn chót 30 giây phục vụ cùng số lượt, nhưng có khách bị phá lời hứa của chính luật ở 28 trong
  34 kịch bản.»
  - Vì sao: "khách bị phá lời hứa của chính luật" là cấu trúc bị động lồng sở hữu, khó đọc. Câu còn gợi ý luật C đúng
    giờ hơn (xem Phần 2).
  - Đề xuất: «Luật hạn chót 30 giây cũng phục vụ 2.338 lượt nhưng không giữ được lời hứa của chính nó với ít nhất một
    khách ở 28 trong 34 kịch bản.»
- **H7. Ch5 L12.** «Vế cộng dồn chỉ riêng nó giải thích 3 trong 524 bản ghi chặn ở mức này; tác dụng lên kết quả phục
  vụ chưa được đo.»
  - Vì sao: "vế" là từ của công thức, không phải tên khái niệm. ASSEMBLY dòng 6 đã đổi thành "phần cộng dồn". "Bản ghi
    chặn" chưa được giải thích ở Chương 5. "Chỉ riêng nó giải thích" nghe như quan hệ nhân quả.
  - Đề xuất: «Ở mức này, trong 524 bản ghi phương án bị trần loại, 3 bản ghi chỉ vượt trần khi cộng thêm phần trần khách
    đã dùng trước đó. Phần cộng dồn có đổi kết quả phục vụ hay không thì chưa đo.»
- **H8. Ch5 L15.** «Với phần được hồ sơ tắc đường lịch sử giải thích, lời hứa theo dự báo giảm số khách trễ quá một phút
  từ 68 xuống 2 trong 1.471 khách của 21 kịch bản ngày thường, gộp theo khách.»
  - Vì sao: 39 tiếng, câu dài nhất chương. Câu không nói đây là khách của luật C. Nhãn "gộp theo khách" treo ở cuối.
  - Đề xuất: «Phần được hồ sơ tắc đường lịch sử giải thích: với luật C trần 30 giây trên 21 kịch bản ngày thường, lời
    hứa theo dự báo giảm số khách trễ quá một phút từ 68 xuống 2 trong 1.471 khách được phục vụ.»
- **H9. Ch5 L15.** «Trên cả 3.672 yêu cầu của tập chính, luật C có dự báo cho 2.328 lượt không trễ quá một phút.»
  - Vì sao: "luật C có dự báo" dễ hiểu thành bộ điều phối dùng dự báo, trong khi đây chỉ là tính lại lời hứa.
  - Đề xuất: «Trên cả 3.672 yêu cầu của tập kiểm tra chính, khi tính lại lời hứa theo dự báo, luật C có 2.328 lượt
    không trễ quá một phút.»
- **H10. Ch5 L15.** «Điều phối không trần có dự báo và đệm thêm 30 giây cũng cho đúng 2.328 lượt; …»
  - Vì sao: "đệm" xuất hiện lần đầu ở Chương 5 mà không có giải thích.
  - Đề xuất: «Cách đệm 30 giây, tức cộng thêm 30 giây vào mọi lời hứa của điều phối không trần, cũng cho đúng 2.328
    lượt; …»
- **H11. Ch5 L15.** «Đổi lại, lời hứa dài thêm trung bình 37,2 giây thay vì 7,4 giây, gộp theo khách được phục vụ.»
  - Vì sao: không nói lời hứa của cách nào dài hơn; "thay vì" lại phải đoán.
  - Đề xuất: «Đổi lại, lời hứa của cách đệm dài thêm trung bình 37,2 giây, so với 7,4 giây của luật C (trung bình gộp
    theo khách được phục vụ).»
- **H12. Ch5 L18.** «Với phần còn lại, sổ theo từng khách cho biết dự báo đang dùng chưa giải thích được bao nhiêu độ
  trễ.»
  - Vì sao: "sổ" chưa được giải thích ở Chương 5.
  - Đề xuất: «Phần còn lại: sổ theo từng khách chia số giây trễ của mỗi khách thành ba phần trên, nên cho biết dự báo
    đang dùng còn chưa giải thích được bao nhiêu.»
- **H13. Ch5 L18.** «Trong 6.217 giây trễ của 68 khách ngày thường nói trên, phần được hồ sơ lịch sử giải thích là
  5.353 giây, phần còn lại là 783 giây.»
  - Vì sao: 5.353 + 783 = 6.136 ≠ 6.217. Người đọc cộng thử sẽ nghĩ số sai, vì thiếu 82 giây tính cho điều phối.
  - Đề xuất: «Với 68 khách ngày thường nói trên, trong 6.217 giây trễ có 82 giây tính cho điều phối, 5.353 giây được hồ
    sơ lịch sử giải thích và 783 giây còn lại.»
- **H14. Ch5 L18.** «Ở chiều tuyết, 41 trong 601 khách trễ quá một phút so với lời hứa đầu không dự báo.»
  - Vì sao: "chiều tuyết" không có ngày và số kịch bản. Câu bỏ con số chính của mục 4.9: dự báo chỉ giảm từ 41 xuống 34.
  - Đề xuất: «Chiều tuyết 15/11/2018 (8 kịch bản) là trường hợp dự báo không đủ: lời hứa theo dự báo chỉ giảm số khách
    trễ quá một phút từ 41 xuống 34 trong 601 khách được phục vụ.»
- **H15. Ch5 L24.** «Mô phỏng có tải thấp và một hệ số tắc đường chung cho cả thành phố; chưa đo phản ứng của khách hay
  giá trị của trần với hãng xe.»
  - Vì sao: hai ý không liên quan dính trong một câu. Câu không nói kết luận nào bị ảnh hưởng, trái STYLE quy tắc 32
    ("điều gì chưa làm → ảnh hưởng tới kết luận nào").
  - Đề xuất: xem thay đổi bắt buộc B3.
- **H16. Ch5 L24.** «Đổi bộ chọn và luật mỗi lần một trần chưa được chạy trên quỹ đạo.»
  - Vì sao: câu cụt. "Đổi bộ chọn" không nói đổi sang gì. "Trên quỹ đạo" là biệt ngữ (GLOSSARY v2:175 đã đề nghị bỏ
    "độ nhạy quỹ đạo"). Câu cũng nói nhẹ hơn 4.11, nơi luật mỗi lần một trần "chưa được cài đặt".
  - Đề xuất: «Hai phép thử chưa được chạy thành lần mô phỏng đầy đủ: đổi bộ chọn sang ưu tiên chi phí kế hoạch, và luật
    giới hạn từng lần dời thay cho tổng, vốn còn chưa được cài đặt.»
- **H17. Ch5 L24.** «Chưa tách được phần của bộ chọn và chưa đo giá trị tăng thêm của vế cộng dồn.»
  - Vì sao: "giá trị tăng thêm" dễ đọc thành giá trị kinh doanh; lại có "vế".
  - Đề xuất: «Vì vậy chưa biết bao nhiêu phần của đánh đổi đến từ trần, bao nhiêu từ bộ chọn, và phần cộng dồn có đổi
    kết quả hay không.»
- **H18. Ch5 L27.** «Đóng góp còn giới hạn bởi phần kế thừa.»
  - Vì sao: câu không tự nhiên; "phần kế thừa" không rõ là kế thừa của ai.
  - Đề xuất: «Phần lớn ý nền của khóa luận đã có trong nghiên cứu trước, nên đóng góp hẹp.»
- **H19. Ch5 L27.** «Fielbaum và Alonso-Mora đã đo và kiểm soát bất ổn trước quyết định.»
  - Vì sao: "bất ổn trước quyết định" có thể hiểu là "độ bất ổn có trước quyết định". Ý đúng là kiểm soát ngay lúc ra
    quyết định (J08).
  - Đề xuất: «Fielbaum và Alonso-Mora đã đo mức thay đổi của giờ hứa với từng khách và kiểm soát nó ngay khi ra quyết
    định gán khách.»
- **H20. Ch5 L27.** «Hörl và Zwick đã tính lại tuyến cũ theo tắc đường.»
  - Vì sao: thứ được tính lại là giờ trả trên tuyến, không phải tuyến (J01). Câu cũng không nói đây chính là mốc khóa
    luận dùng.
  - Đề xuất: «Hörl và Zwick đã tính lại giờ trả trên tuyến đang gán theo tắc đường hiện tại, chính là mốc khóa luận
    dùng.»
- **H21. Ch5 L33.** «Thứ nhất, cần thử kết hợp hai thứ tự ưu tiên của bộ chọn với hai cấu hình không trần và trần 30
  giây trên tập kiểm tra chính.»
  - Vì sao: người đọc không biết hai thứ tự ưu tiên là gì.
  - Đề xuất: xem thay đổi nên làm N4.
- **H22. Ch5 L33.** «Bộ chạy mới phải tái lập kết quả cũ trên các kịch bản kiểm tra trước khi so sánh.»
  - Vì sao: "các kịch bản kiểm tra" dễ lẫn với "tập kiểm tra chính".
  - Đề xuất: «Trước khi so, bộ chạy dựng lại phải cho đúng kết quả đã lưu trên một số kịch bản.»
- **H23. Ch5 L33.** «… để đo sự phụ thuộc của đánh đổi vào bộ chọn.»
  - Vì sao: chuỗi danh từ hóa.
  - Đề xuất: «… để biết đánh đổi giữa phục vụ và đúng giờ còn giữ không khi bộ chọn đổi.»
- **H24. Ch5 L36.** «Hai phép so này kiểm riêng vai trò của lịch sử các lần dời và của mốc thời gian cập nhật.»
  - Vì sao: "lịch sử các lần dời" và "mốc thời gian cập nhật" là hai cách gọi mới, không khớp thuật ngữ đã dùng ("phần
    cộng dồn"; "giờ trả tính lại khi giữ kế hoạch").
  - Đề xuất: xem thay đổi nên làm N4.
- **H25. Ch5 L39.** «… bằng dữ liệu có đúng tại thời điểm hứa …»
  - Vì sao: sai ngữ pháp; ý là dữ liệu đã có sẵn tại thời điểm hứa.
  - Đề xuất: «… chỉ dùng dữ liệu đã có tại thời điểm hứa …»
- **H26. Ch5 L45.** «Kết quả phải đo trên quỹ đạo mô phỏng của từng cấu hình, thay vì suy số khách được phục vụ từ phép
  sàng lọc.»
  - Vì sao: lại là biệt ngữ "quỹ đạo".
  - Đề xuất: «Mỗi cấu hình cần được chạy mô phỏng đầy đủ, không suy số khách được phục vụ từ phép sàng lọc trên các lần
    chạy cũ.»

**Phụ lục**

- **H27. PL L14.** «Phép so cấu hình cam kết đầy đủ với ghép tự do xét cả gói cam kết.»
  - Vì sao: câu vòng ("cam kết đầy đủ … cả gói cam kết"). Không nói gói gồm gì, không nói mức 30 giây mà Ch4A:226 trỏ
    tới.
  - Đề xuất: xem thay đổi bắt buộc B5.
- **H28. PL L21.** «Phương án giữ nguyên có $p=e$; được phép qua riêng luật giờ trả chưa bảo đảm các ràng buộc khác đều
  hợp lệ.»
  - Vì sao: vế sau sai trật tự cú pháp, không có chủ ngữ.
  - Đề xuất: «Với phương án này, $p = e$. Qua được phép kiểm giờ trả không có nghĩa là phương án qua mọi ràng buộc
    khác.»
- **H29. PL L38.** «Đây là cách viết lại theo Hörl và Zwick, chưa được chạy.»
  - Vì sao: có thể đọc thành luật này có trong bài của Hörl và Zwick. Ch3:463–464 nói rõ hơn: "một cách viết lại của
    khóa luận". J05 lưu ý rằng thay $p_0 + B$ vào là biến thể suy luận.
  - Đề xuất: «Đây là biến thể khóa luận dựng từ công thức 7 của Hörl và Zwick, không phải luật trong bài của họ; chưa
    được chạy.»
- **H30. PL L44.** «Cách đọc bảng: giữ kế hoạch không thêm phần dời do điều phối.»
  - Vì sao: câu không đọc bảng mà nhắc lại một tính chất.
  - Đề xuất: «Cách đọc bảng: luật C và hạn chót nới luôn cho phương án giữ nguyên qua, vì phương án này không thêm phần
    dời do điều phối; luật hạn chót và luật trần độ dời khách thấy có thể loại cả phương án không đổi gì, chỉ vì tắc
    đường làm $e$ lùi.»
- **H31. PL L47–55.** «Các ví dụ sau là phép tính minh họa…»; «…có độ lệch hai đầu bằng 0…»
  - Vì sao: không nói các ví dụ minh họa điều gì. "Độ lệch hai đầu" chưa được định nghĩa ở Ch3 hay PL.
  - Đề xuất: xem thay đổi nên làm N5.
- **H32. PL L63.** «Bảng C.1 viết gọn tang3/t38/split-t38-v1.json … Lấy mọi cặp trong mỗi tích; mã có dạng
  d20181114-s10-r3-w07, với $r$ là mẫu, $w$ là giờ bắt đầu.»
  - Vì sao: "viết gọn" nghĩa là "tóm tắt"; "tích" là thuật ngữ tập hợp; `s10` không được giải thích.
  - Đề xuất: «Bảng C.1 tóm tắt tệp chia tập … Mỗi ô của bảng ghi một nhóm mẫu và một nhóm khung giờ; mọi tổ hợp mẫu và
    khung trong ô là một kịch bản, ví dụ ô ngày 14 của tập chính có 2 × 3 = 6 kịch bản. Mã kịch bản như
    d20181114-s10-r3-w07 đọc là: ngày 14/11/2018, mẫu 10\% số chuyến, mẫu thứ 3, khung bắt đầu lúc 7 giờ.»
- **H33. PL L84.** «15 kịch bản hiệu chỉnh chạy luật C trần 30 giây để chỉnh khoảng dự phòng trong phép thử riêng; không
  dùng để lập các bảng kết quả chính.»
  - Vì sao: "khoảng dự phòng" không xuất hiện ở Ch3 hay Ch4. "Phép thử riêng" là một phép thử không được báo ở đâu.
    Câu cũng khác Ch4A:107–109, nơi các lần chạy này "chỉ tham gia phép kiểm tính nhất quán của sổ".
  - Đề xuất: xem thay đổi bắt buộc B4.
- **H34. PL L84.** «… cố định cùng ngày, khung 8 và 17; …»
  - Vì sao: "cùng ngày" không rõ cùng với ngày nào.
  - Đề xuất: «… tập tắc đường cố định cũng dùng ngày 12–13/11/2018, khung 8 và 17 giờ; …»
- **H35. PL L87.** «LOCKS tương ứng điều phối không trần; B1 là chính sách ghép tự do; C1 là họ chính sách kiểm trần
  cứng.»
  - Vì sao: ba mã không xuất hiện ở bất kỳ chương nào (đã grep Ch1–Ch4B) và không có trong Bảng C.2. "Trần cứng" là
    biệt ngữ. Thứ người tái lập thật sự cần là tên thư mục của tập cố định (`b1-ref`, `c1-nobudget`…).
  - Đề xuất: xem thay đổi nên làm N2.
- **H36. PL L110.** «Trừ tập cố định dùng bộ chạy cũ không phục hồi, các tập dùng runner-tier3-v2, dựng từ 45f8026; bản
  tin khởi tạo ghi lõi 1ce15e92, FleetPy 1.0.2, hạt giống 7.»
  - Vì sao: "bộ chạy cũ không phục hồi" thiếu chữ "luật". `45f8026` và `1ce15e92` không được gọi tên là mã phiên bản.
    "Bản tin khởi tạo ghi lõi" khó hiểu.
  - Đề xuất: xem thay đổi nên làm N3.
- **H37. PL L110.** «wp4-tier3-v2.json dùng phục hồi không tệ hơn kế hoạch giữ.»
  - Vì sao: tên tệp làm chủ ngữ; "kế hoạch giữ" là cụm cắt cụt.
  - Đề xuất: «Tệp cấu hình wp4-tier3-v2.json bật luật phục hồi không tệ hơn phương án giữ nguyên kế hoạch.»
- **H38. PL L110.** «Đồng hồ tiến theo sự kiện, kết thúc khi hết yêu cầu và hành trình đang hoạt động; khung nhu cầu hai
  tiếng không phải thời lượng cố định.»
  - Vì sao: "hành trình đang hoạt động" dịch sát từ tiếng Anh.
  - Đề xuất: «Mô phỏng chạy theo sự kiện và dừng khi mọi yêu cầu đã được xử lý và mọi khách đã xuống xe; khung giờ hai
    tiếng chỉ là khoảng phát sinh yêu cầu, không phải độ dài lần chạy.»
- **H39. PL L113 và L116.** «Số dùng: chính 170 lần và thêm 34 lần C-120; sáng 136 trong 192; …»; «Trễ dùng ngưỡng lớn
  hơn hẳn; không trễ bằng phục vụ trừ trễ trên mọi yêu cầu. Độ dài thêm gộp theo khách; trung bình theo kịch bản tính
  riêng.»
  - Vì sao: lối ghi chú, không thành câu; có ký hiệu luật trong câu văn.
  - Đề xuất: xem thay đổi nên làm N3.
- **H40. PL L119.** «Ngày 12/10/2026, toàn bộ kiểm thử trên 45f8026 với kiểu xuống dòng LF đạt 1.024 trong 1.025.»
  - Vì sao: "toàn bộ … đạt 1.024 trong 1.025" tự mâu thuẫn. `45f8026` không được giải thích. Số liệu cũng đã cũ (Phần 3).
  - Đề xuất: xem thay đổi bắt buộc B1.

(Đếm: 26 chỗ ở Chương 5 (H1–H26) và 14 chỗ ở phụ lục (H27–H40), tổng **40 chỗ khó**. H39 gộp hai dòng PL L113 và L116
vì cùng một lỗi viết kiểu ghi chú.)

### Sau Chương 5, người đọc nói được gì đã đạt và chưa đạt?

**Nói được, nhưng phải gắng.**
- Đạt: luật C trần 30 giây không để khách nào vượt trần, lớn nhất 29,2 giây. Nó phục vụ ít hơn 96 lượt nhưng có thêm 31
  lượt không trễ quá một phút. Lời hứa theo dự báo giảm khách trễ từ 68 xuống 2. Cách đệm hòa ở một phút và hơn ở hai
  phút, với lời hứa dài gấp khoảng năm lần.
- Chưa đạt (rải ở 5.2 và 5.3): chưa thử bộ chọn ưu tiên chi phí, chưa thử luật mỗi lần một trần, chưa có ngày sự kiện,
  chưa có dữ liệu hãng xe.

**Người đọc sẽ hiểu sai bốn điều.**
- (a) Luật C đúng giờ hơn luật hạn chót. Câu 28/34 không có vế 292 so với 289.
- (b) Luật C đúng giờ hơn điều phối không trần ở mọi ngưỡng. Câu không có "−5 ở hai phút".
- (c) Không biết trần đổi được gì so với không trần. Câu không có 590,1 giây.
- (d) Kết quả là phép kiểm trên dữ liệu chưa xem. Chương 5 không nói kết quả là thăm dò, không nói là mô phỏng.

**Thiếu một câu tóm "đạt / chưa đạt".** Nên thêm hai câu cuối 5.1 (xem "Sửa nhỏ" mục 9).

---

## Phần 2. Giảng viên chấm

### 2.1 Mục 5.1: mỗi phần có con số chính, mẫu số và cái giá trung thực không?

| Phần | Con số chính và mẫu số | Cái giá trung thực | Nhận xét |
|---|---|---|---|
| Phần tính cho điều phối (L12) | Có: 2.338 so với 2.434 trên 3.672; 2.262 so với 2.231 trên 3.672; 2.387/2.255/2.366 trên 3.672 | Có −96 lượt. **Thiếu** −5 lượt ở hai phút (2.327 so với 2.332; Ch4A:244–245). **Thiếu** −242 khách đi chung (Ch4A:244; 4.11:391). **Thiếu** vế 292 so với 289, cùng 28/34 (Ch4A:357–358; Ch1:212–213) | **Không đạt.** Câu 28/34 đứng một mình là nói quá bằng cách bỏ sót. Phần lợi cũng thiếu vật so: 29,2 giây không kèm 590,1 giây. Đoạn cũng không nói luật C không bảo đảm giờ đến (K05) |
| Phần được hồ sơ lịch sử giải thích (L15) | Có: 68 → 2 trên 1.471 gộp theo khách; 2.328 = 2.328; 2.366 so với 2.338; 37,2 so với 7,4 giây gộp theo khách; sớm 44/2.434 so với 4/2.338 | Có: đệm hòa ở một phút và hơn ở hai phút | **Đạt phần lớn.** Thiếu "không riêng của luật C" (luật hạn chót cũng 66 → 2; Ch4B:124–125). Thiếu "đệm hơn ở hai phút vì phục vụ thêm 96 lượt" (N-19; Ch4B:280–281). Câu 68 → 2 không nói là khách của luật C |
| Phần còn lại (L18) | Có: 6.217/5.353/783 giây; 41/601; 3.445,9/8,6/251,5/3.185,9 giây | Có câu "phần còn lại không phải phần không thể biết trước" | **Đạt một nửa.** Thiếu 82 giây, nên ba số ngày thường không cộng ra 6.217. Thiếu con số chính của 4.9: dự báo chỉ giảm từ 41 xuống 34 |

Hörl và Zwick được trích lại ở L12 (đúng yêu cầu brief). Nhưng "tiếp nối mốc" nên đổi thành "mốc này đã có trong công
thức 7 của Hörl và Zwick", đúng tinh thần OUTLINE §6.1.

### 2.2 Mục 5.2 có khớp 4.11 không?

**Không mâu thuẫn, nhưng thiếu điều quan trọng nhất.**
- Từng câu của 5.2 đều có trong 4.11: 34 kịch bản phụ thuộc, 5 ngày, một lần chạy; tải thấp; hệ số tắc đường chung; không
  có phản ứng khách; không đo giá trị với hãng xe; bộ chọn ưu tiên chi phí và luật mỗi lần một trần chưa chạy.
- **Thiếu tính thăm dò.** 4.11:421–423 có cả một gạch đầu dòng: ngưỡng, cách chia tập và mức 120 giây được chọn sau khi
  xem dữ liệu, "nên mọi kết quả là thăm dò" (I06; C4A-11). Đây là hạn chế mà giảng viên sẽ hỏi đầu tiên. Nó phải có ở
  phần kết luận theo STYLE quy tắc 32 ("Giới hạn chung gom vào một mục cuối chương thực nghiệm và một mục trong kết
  luận").
- 5.2 không nối hạn chế với kết luận bị ảnh hưởng (quy tắc 32). 4.11 thì có, ví dụ "cái giá 96 lượt vì vậy chỉ áp cho
  thiết lập này".
- Nói nhẹ hơn 4.11 một chỗ: Ch5 viết luật mỗi lần một trần "chưa được chạy", còn 4.11:441–442 và E09 viết "chưa được cài
  đặt".
- Các ý của 4.11 về tích hợp (phép kiểm giờ đón dùng giờ không dự báo; bản dựng lại phải khớp) được chuyển sang 5.3 hướng
  1 và hướng 5. Chấp nhận được.
- Đoạn chồng lấn với công trình trước (L27) đúng tinh thần bản cũ `09-chuong5.tex:94-100`: nêu Fielbaum và Alonso-Mora,
  Schulz và Pfeiffer, thêm Hörl và Zwick. Không nhắc Elmi, đúng vì J12 UNVERIFIED. Câu "Khóa luận cài đặt, kiểm tra một
  nghĩa vụ cụ thể và đo cái giá của nó" đúng K31 nhưng chưa nêu ba khác biệt với Hörl và Zwick (J05: một trần cho mọi
  khách, không nới theo tắc đường, cộng qua cả chuyến). Nên thêm (N4).

### 2.3 Mục 5.3: tối đa 5 hướng, bộ chọn × trần đứng đầu, không ước lượng giờ?

**Đạt cả ba.**
- Đúng 5 hướng, đánh "Thứ nhất … Thứ năm".
- Hướng 1 là phép thử {hai thứ tự tiêu chí} × {không trần, trần 30 giây}. Đúng OUTLINE §7.2 và Ch4B v10:71–72 ("chương
  kết luận đặt phép thử này lên đầu các hướng phát triển").
- Không có số giờ, số job hay "Giai đoạn 1b". Câu về điều kiện tái lập ("phải tái lập kết quả cũ … trước khi so sánh")
  mô tả Gate 0 bằng lời thường, không có chữ kế hoạch.
- Codex gộp hai hướng (1) và (2) của OUTLINE (luật mỗi lần một trần; hạn chót nới kiểu Hörl và Zwick) thành "Thứ hai" để
  còn 5 hướng. Cách gộp hợp lý.
- Điểm trừ là cách viết. Hướng 1 không nói hai thứ tự tiêu chí là gì. Hướng 2 dùng hai tên mới. Hướng 5 dùng "quỹ đạo"
  (H21–H26).

### 2.4 Phụ lục C: có đủ bảy nội dung tái lập, không có chữ kế hoạch?

| Nội dung | Có? | Nhận xét |
|---|---|---|
| Tập kiểm tra và danh sách kịch bản | Có | Bảng C.1 khớp **chính xác** tệp chia tập (tôi mở lại `split-t38-v1.json`: 34 mã kiểm tra, 15 mã hiệu chỉnh, theo khung 9/14/11). Ba tập khác được nêu bằng lời. **Lỗi:** câu về 15 kịch bản hiệu chỉnh (H33) |
| Cấu hình | Có | Bảng C.2 và hai thư mục cấu hình. Câu LOCKS/B1/C1 chỉ gây nhiễu (H35) |
| Danh tính bộ chạy | Có | `runner-tier3-v2`, nguồn 45f8026, lõi 1ce15e92, FleetPy 1.0.2, hạt giống 7, luật phục hồi: đúng A28 và R26 Q8. Nhưng viết như ghi chú (H36–H37). Không nói bộ chạy cũ của tập cố định là gì (B17 có lõi 38d517d, VERIFIED-by-Codex R15) |
| Gốc kết quả | Một phần | Hai lỗ hổng. **(1)** Gốc tập cố định chứa 160 thư mục của 10 cấu hình, nhưng phụ lục không nói 5 cấu hình dùng tên thư mục nào. Ánh xạ này chỉ có trong NOTES §5. **(2)** Gốc `tier3-forecast-v1/` của chiều tuyết còn chứa 34 thư mục khác: một `C-30-d20181115-s10-r2-w07` không phải tuyết, cùng các lần chạy dự báo trong bộ điều phối. Người tái lập đếm `C-30-*` sẽ ra 9, không phải 8. **Thiếu** đường dẫn đầu vào (fixtures, drivers, worlds), dù NOTES §5 có và tôi đã thấy chúng tồn tại |
| Quy tắc đếm lần chạy | Có | Đúng số. Viết cụt (H39). Nên nói bản kiểm kê 1.991 có trước 34 lần chạy trần 120 giây (C4A-20 ghi chú; L1a-01 ngày 10/10) |
| Cách tính lại số | Có một nửa | Có định nghĩa ngưỡng và mẫu số. **Thiếu** kết quả đối chiếu: hai bộ đọc khớp từng khách trên 7.159 khách (N4B-14). Thiếu câu nói các chương trình kiểm do mô hình ngôn ngữ lớn viết, điều Ch3:729–731 đã công bố |
| Chạy lại kiểm thử | **Sai** | Dùng kết quả cũ ngày 12/10 (Phần 3). ASSEMBLY dòng 3 yêu cầu 1.025/1.025 ngày 13/10/2026 |
| Chữ kế hoạch, niêm phong | Không có chữ cấm | Nhưng "chỉnh khoảng dự phòng trong phép thử riêng" trỏ ngầm tới phép thử độ phủ γ của kế hoạch T3.8 (REG C17: "2/34 ô kiểm vượt γ, cận trên Clopper–Pearson"). Nên bỏ |
| Câu trỏ từ Ch3:735 | **Thiếu** | Ch3: "Bản dựng lại, nếu có, phải cho đúng kết quả cũ trên một số kịch bản trước khi dùng (Phụ lục C)". C không có câu này |

### 2.5 Phụ lục A: phần bị bỏ có được xử lý gọn không?

**Gần gọn, nhưng câu còn lại không phục vụ câu trỏ duy nhất tới nó.**
- Codex làm đúng điều kiện của brief: không có ánh xạ E12 tới tệp output thì không in số. Lý do được ghi ở NOTES §5 A và
  §7, kể cả việc chưa tìm được output tổng hợp cho 89,06%, ±0,3 điểm và 774/1.581. Không tự tính lại để lấp chỗ trống.
- Việc giữ một mục 40 tiếng thay vì bỏ hẳn là lệch nhẹ khỏi brief ("Otherwise write a one-line placeholder in the
  NOTES"). Lý do chấp nhận được: brief cũng đòi định nghĩa `phuluc:A`, và Ch4A:226 trỏ tới nó.
- **Nhưng** câu trỏ Ch4A:225–226 nói "Trần chính B = 30 giây là trần giờ trả của cấu hình có trần ở tập kịch bản tĩnh
  … (Phụ lục A)", còn Phụ lục A không nhắc 30 giây. C4A-15 (VERIFIED-by-me, TEX08:136-137) cho phép viết đúng câu này.
  Hơn nữa, A trỏ tới `muc:c4-taptu` (Ch4A:104–151), mục về bốn tập thử, không nói gì về tập tĩnh. Mục đúng là
  `muc:c4-thamdo` (Ch4A:222–228).
- Câu "Phép so cấu hình cam kết đầy đủ với ghép tự do xét cả gói cam kết" có ý của K33/K34 nhưng không đọc được (H27).
- Cách khác, gọn hơn: bỏ hẳn A, đổi B thành A và C thành B (nhãn giữ nguyên tên, chỉ chữ cái in ra đổi). Câu Ch4A:226
  khi đó bỏ phần trỏ và giữ C4A-15 trong dòng `% EV`. Tôi **không** khuyên cách này vì phải sửa thêm Ch4A. Thay đổi bắt
  buộc B5 giữ A và làm A trả lời đúng câu trỏ.

### 2.6 Phụ lục B có trung thực không?

**Có.**
- Bảng chỉ xét phép kiểm giờ trả, nêu giả thiết (N) và điều kiện sổ hợp lệ. Bảng ghi "Có, theo suy luận" và "chưa được
  chạy" cho hạn chót nới.
- Bảng không có kiểm đếm dự đoán, không có định lý bốn họ. CE-6 được giữ ở dạng tính chất đại số, không nhận là bản ghi
  thực nghiệm (NOTES §5 B).
- Ba ví dụ số đúng (Phần 3).

**Bốn điểm cần sửa.**
- (a) Câu "cách viết lại theo Hörl và Zwick" có thể bị đọc thành luật của họ (H29). Ch3:464 đã viết "của khóa luận".
- (b) Các ví dụ không nói minh họa điều gì; "độ lệch hai đầu" chưa định nghĩa (H31).
- (c) Ký hiệu $L$ trong bảng khác $L_r$ của Ch3:374–379 và Nhận xét 3.1. $L^{\mathrm{V}}$ là ký hiệu mới, chỉ định nghĩa
  trong chú thích bảng.
- (d) Không có câu nào trong thân bài trỏ tới `phuluc:B`, vì Ch3 v4-v3 không có `\ref{phuluc:B}`. Thay đổi nên làm N4
  thêm một câu trỏ từ 5.3.

### 2.7 Nói quá, từ cấm, nhắc tới kế hoạch

- **Nói quá bằng cách bỏ sót** (đều ở 5.1, L12):
  - 28/34 không kèm 292 so với 289;
  - +31 không kèm −5 ở hai phút;
  - thiếu −242 khách đi chung;
  - thiếu "không bảo đảm giờ đến";
  - thiếu "trên mô phỏng" (STYLE quy tắc 32: "Kết luận chỉ áp cho môi trường đã đánh giá").
- **Câu gần nhân quả:** "Vế cộng dồn chỉ riêng nó giải thích 3 trong 524 bản ghi chặn". Ch4A:711 viết đúng hơn: "chỉ
  vượt trần khi cộng thêm phần trần đã dùng trước đó".
- **Ghi công lệch:** PL L38 (H29).
- **Từ cấm** ("niêm phong", "đăng ký trước", "dự đoán", "mong đợi", "tối ưu", "duy nhất", "đầu tiên", "vượt trội",
  "chứng nhận", "gây ra", "quy trách"): **không có**, kể cả trong các dòng `%`. "Hành khách" ở L6 đúng GLOSSARY v2:40
  (dùng ở lần đầu mỗi chương).
- **Nhắc tới kế hoạch, đăng ký trước, dự đoán:** không có chữ nào. Chỗ gần nhất là PL L84 (khoảng dự phòng γ, C17). Nên
  bỏ (B4).
- **Kết luận cho Phần 2:**
  - Chương 5 **chưa** đạt ở 5.1 đoạn 1 và 5.2.
  - Phụ lục C **chưa** đạt vì đoạn kiểm thử cũ và vì thiếu câu bộ chạy dựng lại mà Ch3:735 trỏ tới.
  - Phụ lục A, B đạt sau các sửa nhỏ.

---

## Phần 3. Kiểm số và nhãn

Mã sổ theo sổ chính (A…K), PL1 (N-, L1a-), PL2 (X3-), PL3 (N4B-), PL4 (C4A-), PL6 (N4B8-). "Ch4A" là v5-v3, "Ch4B" là
v10.

### 3.1 Các số của Chương 5

| # | Dòng | Số hoặc nhận định | Kết quả | Nguồn |
|---|---|---|---|---|
| 1 | L12 | Công thức 7 của Hörl và Zwick là mốc giờ trả tính lại | AGREE | J01, J03; Ch3:459–461; ASSEMBLY (R32: công thức 7 khớp bản thảo tr. 8) |
| 2 | L12 | 34 kịch bản; 3.672 yêu cầu | AGREE | B09; Ch4A:125 |
| 3 | L12 | Luật C trần 30 giây phục vụ 2.338; không trần 2.434; ít hơn 96 | AGREE | C01, C02; Ch4A:243–244, 275–276 |
| 4 | L12 | Không khách nào trong 2.338 vượt trần; lớn nhất 29,2 giây | AGREE | C20, N-21; Ch4A:242, 426 |
| 5 | L12 | Không trễ quá một phút 2.262 so với 2.231, trên 3.672 | AGREE | C08; Ch4A:275–276 |
| 6 | L12 | Luật hạn chót 30 giây "cùng số lượt" (2.338) | AGREE | C01; Ch4A:277 |
| 7 | L12 | 28 trong 34 kịch bản có khách bị luật hạn chót phá lời hứa | AGREE (thiếu vế 292/289, cùng 28/34: C4A-01; Ch4A:357–358) | N-21; Ch4A:327 |
| 8 | L12 | Trần 120 giây: 2.387 phục vụ; 2.255 và 2.366 không trễ quá một và hai phút, trên 3.672 | AGREE | N-06, L1a-02; Ch4A:580, 585–586 |
| 9 | L12 | 3 trong 524 bản ghi chặn chỉ do cộng dồn, ở trần 120 giây | AGREE | N-08, L1a-06; Ch4A:739 |
| 10 | L15 | 68 → 2 trong 1.471 khách, 21 kịch bản ngày thường, gộp theo khách | AGREE (là khách của luật C trần 30 giây) | F17, F04, N4B8-01; Ch4B:79–80, 100 |
| 11 | L15 | Luật C có dự báo: 2.328 không trễ quá một phút trên 3.672 | AGREE | C09, N-16; Ch4A:593; Ch4B:249 |
| 12 | L15 | Không trần + dự báo + đệm 30 giây: 2.328 | AGREE | C10, N-16; Ch4B:254 |
| 13 | L15 | Hai phút: 2.366 (đệm) so với 2.338 (luật C) | AGREE | C10, N-16; Ch4B:249, 254 |
| 14 | L15 | Dài thêm 37,2 so với 7,4 giây, gộp theo khách được phục vụ | AGREE (37,18 và 37,37 trong bảng; 37,1833 và 7,3671 ở N-18) | C10, N-18; Ch4B:219 |
| 15 | L15 | Tới sớm quá một phút 44/2.434 so với 4/2.338 | AGREE | C10, N-16; Ch4B:249, 254 |
| 16 | L18 | 6.217 giây; 68 khách; 5.353; 783 | AGREE (thiếu 82 giây tính cho điều phối, nên không cộng ra tổng) | F09, N4B8-11; Ch4B:147–151 |
| 17 | L18 | Chiều tuyết: 41 trong 601 trễ quá một phút | AGREE | F13, B20; Ch4B:306–307 |
| 18 | L18 | 3.445,9 = 8,6 + 251,5 + 3.185,9 giây | AGREE (3.445,933 − 8,566 − 251,496 = 3.185,871) | F13, N4B-05; Ch4B:156–162, 308–309 |
| 19 | L24 | 34 kịch bản phụ thuộc, 5 ngày, mỗi kịch bản một lần | AGREE | I05, B11; Ch4B:419–420 |
| 20 | L24 | Bộ chọn ưu tiên chi phí và luật mỗi lần một trần chưa chạy | AGREE (nhưng luật mỗi lần một trần còn "chưa được cài đặt": E09; Ch4B:441–442) | H12, E09 |
| 21 | L27 | Fielbaum và Alonso-Mora đo và kiểm soát; Hörl và Zwick tính lại; Schulz và Pfeiffer hạn chót từ lời hứa đầu | AGREE | J06, J08, J01, J10, J38 |
| 22 | L33 | Phép thử hai thứ tự × hai cấu hình, trần 30 giây | AGREE (là đề xuất; không có số kết quả) | H12; OUTLINE §7.2; Ch4B:19–22, 71–72 |

**Chương 5: 22 nhóm, 22 AGREE, 0 WRONG, 0 CANNOT CHECK.** Bốn nhóm (7, 10, 16, 20) đúng số nhưng thiếu vế, đã ghi trong
cột kết quả.

### 3.2 Các số và nhận dạng của phụ lục

| # | Dòng | Số hoặc nhận định | Kết quả | Nguồn |
|---|---|---|---|---|
| 1 | B L32 | $L + \lvert e-e \rvert = L \le B$ khi $0 \le L \le B$ | AGREE | A06, A22; Ch3:374–379 |
| 2 | B L34 | Luật hạn chót: có thể $e - p_0 > B$ dù kế hoạch không đổi | AGREE | A10; Ch3:455–456 |
| 3 | B L36 | Trần độ dời khách thấy: $L^{\mathrm{V}} + \lvert e - v \rvert$ có thể vượt $B$ | AGREE (phương án giữ nguyên có $z = e - v = x$) | A11, A12; Ch3:428–433 |
| 4 | B L38 | $p = e \le \max(p_0 + B, e)$; suy luận, chưa chạy | AGREE | A22, J05, K27; Ch3:463–466 |
| 5 | B L49 | $v = e = 600$, $p = 660$ ⇒ $x = 0$, $c = z = 60$ | AGREE (số học) | A01 |
| 6 | B L51 | 600 → 660 → 600: hai đầu 0, $\sum\lvert z\rvert = 120$ | AGREE (60 + 60) | A01, A12 |
| 7 | B L53 | 600 → 660 → 720: hai đầu 120, $\sum\lvert z\rvert = 120$ | AGREE | A01, A12 |
| 8 | B L55 | $x$, $c$ trái dấu ⇒ $\lvert x + c \rvert$ có thể nhỏ hơn $\lvert c \rvert$ | AGREE (ví dụ $x = -30$, $c = 60$ cho $\lvert z \rvert = 30$) | đại số |
| 9 | C L74–78 | Bảng C.1, từng ô | AGREE (tôi mở lại SPLIT:14–65; 34 + 15 = 49; khung 7/8/17 của tập chính là 9/14/11, khớp B09) | B08, B09 |
| 10 | C L68 | Tháng 11/2018, ngày 14–18 | AGREE | B08 |
| 11 | C L84 | Buổi sáng 12–13/11, khung 7; cố định 12–13/11, khung 8 và 17; tuyết 15/11, khung 14 và 15; mẫu 1–4 | AGREE (8 = 2×4×1; 16 = 2×4×2; 8 = 1×4×2; thư mục `development-v6-ledger` có r1–r4 của 12 và 13/11; thư mục tuyết có r1–r4 × w14, w15) | B15, B17, B20; Ch4A:129–135 |
| 12 | C L84 | 15 kịch bản hiệu chỉnh chạy luật C trần 30 giây | AGREE (số); mục đích "chỉnh khoảng dự phòng" đúng theo C17 nhưng không được viết (Phần 2) | C17, RUN38:42–44 |
| 13 | C L87 | `tang3/configs/`; `tang3/w07x/configs/` | AGREE ở mức R26 Q8 (`S/tang3/configs/C-30.json`, `wp4-tier3-v2.json`); CANNOT CHECK `w07x/configs` (không mở) | R26 Q8; RW7X:35–40 |
| 14 | C L87 | B1 là ghép tự do; C1 là họ "kiểm trần cứng" | AGREE (DOC08:27: B1 `rolling-cost`, C1 `ridebound-hard-vector`; X3-19) | DOC08:20–29; X3-19 |
| 15 | C L87 | LOCKS là điều phối không trần | CANNOT CHECK ngoài OUTLINE Bảng 4.9a; X3-19 xác nhận `c1-nobudget` là điều phối không trần, không xác nhận tên LOCKS | OUTLINE §5 4.4 |
| 16 | C L98 | Tập chính: U, C-30, M⁺-30, M⁺-60, V-30; C-120 ở gốc riêng | AGREE (thư mục tồn tại; `run_t38.py:42–44,51`) | B10, L1a-01 |
| 17 | C L100 | Buổi sáng: U; C và M⁺ ở tám mức 30–300 | AGREE | B15, B16, X3-28, C4A-07 |
| 18 | C L102 | Cố định: FREE, U, C-30, C-60, C-120 trong `development-v6-ledger/…/attempt-01/output/` | AGREE (`attempt-01` có trong thư mục `…-c1-h6ref-s7`) nhưng thiếu ánh xạ tên thư mục | B17, X3-19 |
| 19 | C L104 | Chiều tuyết: C-30 trong `tier3-forecast-v1/` | AGREE nhưng **mơ hồ**: gốc có 9 thư mục `C-30-…` (8 tuyết + `C-30-d20181115-s10-r2-w07`) và 34 thư mục khác | B20, N-26, R26 Q8 |
| 20 | C L110 | `runner-tier3-v2`, nguồn 45f8026, lõi 1ce15e92, FleetPy 1.0.2, hạt giống 7 | AGREE | A28; R26 Q8 (cả 8 bản tin khởi tạo của tuyết); Ch4A:58, 94 |
| 21 | C L110 | `wp4-tier3-v2.json` bật phục hồi không tệ hơn | AGREE | R26 Q8 (WP4:7) |
| 22 | C L110 | Đồng hồ theo sự kiện; dừng khi hết yêu cầu và chuyến; khung hai tiếng không phải độ dài | AGREE | R26 Q2 (34 lần chạy C-120 dài 118,0–154,9 phút mô phỏng) |
| 23 | C L113 | 170 + 34; 136 trong 192; 16 mỗi cấu hình; 8 | AGREE | B10, L1a-01, C4A-07, H13, B20; Ch4A:127–136 |
| 24 | C L113 | Bản thay thế `C-30-d20181114-s10-r3-w17-rerun1` | AGREE | C4A-17; ADD1:6 |
| 25 | C L113 | 1.991, kiểm kê 08/10/2026 | AGREE (C4A-20 ghi chú: chưa kiểm kê lại sau 34 lần C-120) | B19, C4A-20; Ch4A:149 |
| 26 | C L116 | Trễ dùng ">"; không trễ = phục vụ − trễ, trên mọi yêu cầu; độ dài thêm gộp theo khách | AGREE | C06, C08, F06; Ch4A:156–160, 183–184 |
| 27 | C L119 | "Ngày 12/10/2026 … đạt 1.024 trong 1.025 … còn lại đạt 1 trong 1 khi chạy riêng" | **WRONG (cũ, mâu thuẫn Ch3)**. Đúng: **ngày 13/10/2026, cả 1.025/1.025 đạt trong một lần chạy**, với kiểu xuống dòng LF và một tệp chưa ghi nhận. Các lần 12/10: 1.020/1.025 với CRLF; 1.024/1.025 với LF trên cây sạch; 1/1 khi chạy riêng | TESTRUN:14–18, 53–56; log `…-dirty-fullrun-2026-10-13.log` (9 dòng Passed, tổng 1.025, `exit=0`); ASSEMBLY dòng 1–3 |
| 28 | C L119 | Kiểm thử còn lại đòi cây làm việc có tệp chưa ghi nhận | AGREE | TESTRUN:43–49; `StrictBagItBundleTests.cs:32` |

**Phụ lục: 28 nhóm.**
- 25 AGREE, kể cả hai nhóm "AGREE nhưng thiếu hoặc mơ hồ".
- 1 **WRONG**: nhóm 27.
- 2 CANNOT CHECK, hoặc một phần: nhóm 13 (`w07x/configs`) và nhóm 15 (tên LOCKS).

**Tổng cộng 50 nhóm: 1 WRONG.**

### 3.3 Nhãn

| Nhãn | Định nghĩa | Kết quả |
|---|---|---|
| `chuong:ketluan` | Ch5 L4 | Có, duy nhất. Ch1 v3:272 trỏ tới, giải được |
| `phuluc:A` | PL L12 | Có, duy nhất. Ch4A:226 trỏ tới, giải được nhưng nội dung không đáp câu trỏ (2.5) |
| `phuluc:B` | PL L18 | Có, duy nhất. **Không có câu nào trỏ tới** |
| `phuluc:C` | PL L60 | Có, duy nhất. Ch3:724, Ch3:735, Ch4A:149, Ch4B:382 trỏ tới, giải được. Ch3:735 chưa được đáp; Ch3:724 và Ch4B:382 trỏ tới đoạn kiểm thử cũ |
| `muc:c5-tongket`, `muc:c5-hanche`, `muc:c5-huongphattrien` | Ch5 L10, L22, L31 | Có; chưa có câu nào trỏ tới (không bắt buộc) |
| `bang:pl-giunguyen`, `bang:pl-danhsach`, `bang:pl-goc` | PL L27, L69, L93 | Có; mỗi nhãn được trỏ một lần trong PL |

`r32/refs.py` trên bảy tệp: **0 nhãn trùng.**

Đánh số trong LaTeX: lớp `report` đặt lại bộ đếm `section` khi gặp `\appendix`, nên `\section` đầu tiên sau
`\chapter*{Phụ lục}` thành A, rồi B, C. Bảng in thành B.1, C.1, C.2, và `\theH…` tránh trùng đích liên kết. Đúng như
NOTES §3 nói.

### 3.4 Các `\ref` của Chương 5 và phụ lục

| Tệp:dòng | Tham chiếu | Giải tới | Nội dung có khớp câu? |
|---|---|---|---|
| Ch5 L24 | `muc:c4-thaoluan` | Ch4B v10:388 | Khớp |
| PL L14 | `muc:c4-taptu` | Ch4A:104 | **Không khớp**: mục về bốn tập thử, không nói về tập tĩnh; nên là `muc:c4-thamdo` (Ch4A:223) |
| PL L21 | `bang:pl-giunguyen` | PL L27 | Khớp |
| PL L21 | `muc:giunguyen` | Ch3:364 | Khớp: giả thiết (N) ở Ch3:366–369 |
| PL L26 | `muc:bamoc` | Ch3:244 | Khớp: $v$, $e$, $p$ ở Ch3:249–257 |
| PL L63 | `bang:pl-danhsach` | PL L69 | Khớp |
| PL L87 | `bang:pl-goc` | PL L93 | Khớp |
| Ch5 L12, L27; PL L38 | `\cite{horl2022}`, `fielbaum2020`, `schulz2026` | `r32-bib/10-tai-lieu-draft-v2.tex:20,27,34` | Có khóa |

---

## Thay đổi xếp hạng

Văn bản dán thẳng vào LaTeX. Mọi số trong văn bản đề xuất đã kiểm ở Phần 3. Dòng `% EV:` đi kèm.

### Bắt buộc

**B1. Phụ lục C, đoạn kiểm thử (PL L119): thay bằng kết quả ngày 13/10/2026.** Hiện là số WRONG duy nhất, và mâu thuẫn
với Ch3:723–724 ("cả 1.025 … đều đạt").

Thay L119–120 bằng:

```latex
Để kiểm phần mềm, bộ kiểm thử tự động được chạy lại trên một bản sao mới của đúng phiên bản mã nguồn 45f8026 đã dựng
bộ chạy. Ngày 13/10/2026, cả 1.025 kiểm thử đều đạt trong một lần chạy, với hai điều kiện môi trường: các tệp văn bản
dùng kiểu xuống dòng LF, và cây làm việc có một tệp chưa ghi nhận, vì một kiểm thử đòi điều kiện này. Các lần chạy
ngày 12/10/2026 cho thấy vì sao cần hai điều kiện đó: với kiểu xuống dòng CRLF mặc định của Windows, 5 kiểm thử không
đạt; với kiểu LF nhưng cây làm việc sạch, 1 kiểm thử không đạt.
% EV: TESTRUN-45f8026-2026-10-12.md:14-18 (lượt 1–4), 35-49 (nguyên nhân); testrun-45f8026-eollf-dirty-fullrun-2026-10-13.log (9 dự án, 1.025 đạt, exit=0, 13/10/2026 13:42); N4B-13 (lượt 3, 3b); A28
```

Kèm theo khi ghép:
- Ch4B v10:381–382 đổi thành «Chạy lại trên đúng mã nguồn đã dựng bộ chạy, cả 1.025 kiểm thử tự động đều đạt trong một
  lần chạy, với hai điều kiện môi trường nêu ở Phụ lục~\ref{phuluc:C}.» (ASSEMBLY dòng 2).
- Ch3:724 đổi "12/10/2026" thành "13/10/2026" (ASSEMBLY dòng 1).
- Thêm một dòng sổ cho lượt 4, vì N4B-13 chỉ phủ lượt 3 và 3b (ASSEMBLY dòng 3).

**B2. Mục 5.1, đoạn phần tính cho điều phối (Ch5 L12–13): thêm các vế bất lợi và vật so.** Đoạn hiện thiếu 292 so với
289 (cùng 28/34), thiếu −5 ở hai phút, thiếu −242 khách đi chung, thiếu 590,1 giây, thiếu "mô phỏng" và "không bảo đảm
giờ đến". Brief của Ch5 nêu đích danh các vế này; Ch1 v3:212–213 đã có.

Thay L12–13 bằng:

```latex
\textbf{Phần tính cho điều phối:} luật C giới hạn, cho mỗi khách đã được nhận, tổng độ lớn các lần bộ điều phối dời
giờ trả trong cả chuyến. Mỗi lần dời được đo so với giờ trả tính lại nếu xe giữ nguyên kế hoạch cũ; mốc này đã có
trong công thức 7 của Hörl và Zwick~\cite{horl2022}. Trên mô phỏng FleetPy với 34 kịch bản và 3.672 yêu cầu của tập
kiểm tra chính, luật C trần 30 giây không để khách nào vượt trần: tổng dời lớn nhất của một khách là 29,2 giây, so với
590,1 giây khi không trần. Đổi lại, luật C phục vụ 2.338 lượt, ít hơn điều phối không trần 96 lượt, và có ít hơn 242
khách đi chung. So với lời hứa đầu không dự báo, luật C có 2.262 lượt không trễ quá một phút, nhiều hơn 31 lượt so với
2.231 của điều phối không trần, nhưng ở ngưỡng hai phút lại ít hơn 5 lượt (2.327 so với 2.332); các số này tính trên
3.672 yêu cầu. Luật hạn chót 30 giây cũng phục vụ 2.338 lượt nhưng không giữ được lời hứa của chính nó với ít nhất một
khách ở 28 trong 34 kịch bản. Đo bằng thước của luật hạn chót, tức tới muộn hơn lời hứa đầu quá 30 giây, luật C có 292
và luật hạn chót có 289 trong 2.338 khách được phục vụ, cả hai đều ở 28 kịch bản; về đúng giờ, hai luật gần như ngang
nhau. Trần chỉ giới hạn phần do điều phối và không bảo đảm giờ đến thực tế. Nới trần lên 120 giây cho 2.387 lượt phục
vụ, 2.255 lượt không trễ quá một phút và 2.366 lượt không trễ quá hai phút trên 3.672 yêu cầu; đây là một điểm đo thêm
trên đường đánh đổi, không phải mức trần tốt nhất. Ở mức này, trong 524 bản ghi phương án bị trần loại, 3 bản ghi chỉ
vượt trần khi cộng thêm phần trần khách đã dùng trước đó; với trần 30 giây, không có bản ghi nào như vậy trong 845 bản
ghi. Phần cộng dồn có đổi kết quả phục vụ hay không thì chưa đo.
% EV: A06; A13; A01; A02; J01; J03; B01; B09; C20; N-21; C01; C02; N-20; N-09; C08; C4A-01 (292/2.338, 289/2.338, 28/34 cả hai); K05; N-06; L1a-02; K36; N-08; L1a-06; E01 (845 bản ghi C-30 tập chính, 0 chỉ do cộng dồn); E09
```

**B3. Mục 5.2, đoạn đầu (Ch5 L24–25): thêm tính thăm dò và nối mỗi hạn chế với kết luận bị ảnh hưởng.** 4.11:421–423
và STYLE quy tắc 32 đòi điều này. Bản hiện tại bỏ hạn chế mà giảng viên sẽ hỏi đầu tiên.

Thay L24–25 bằng:

```latex
Mục~\ref{muc:c4-thaoluan} trình bày đủ các hạn chế; dưới đây là những hạn chế ảnh hưởng nhiều nhất tới cách đọc kết
luận. Mọi số đến từ một bộ mô phỏng có tải thấp, một hệ số tắc đường chung cho cả thành phố và thời gian dừng đón, trả
bằng 0, nên cái giá 96 lượt phục vụ và mức trễ còn lại sau dự báo chỉ áp cho thiết lập này. Tập kiểm tra chính có 34
kịch bản thuộc 5 ngày, phụ thuộc nhau, mỗi kịch bản chạy một lần; ngưỡng phân tích, cách chia tập và mức 120 giây đều
được chọn sau khi đã xem dữ liệu, nên các kết quả là thăm dò, không phải phép kiểm trên dữ liệu chưa từng xem. Khóa
luận chưa đo phản ứng của khách hay giá trị của trần với hãng xe. Hai phép thử chưa được chạy thành lần mô phỏng đầy
đủ: đổi bộ chọn sang ưu tiên chi phí kế hoạch, và luật giới hạn từng lần dời thay cho tổng, vốn còn chưa được cài đặt.
Vì vậy chưa biết bao nhiêu phần của đánh đổi đến từ trần, bao nhiêu từ bộ chọn, và phần cộng dồn có đổi kết quả hay
không.
% EV: I01; I02; B06; B05 (kiểm trên 3 lần chạy mẫu); B12; I04; I05; B11; I06; C4A-11; I07; I10; D20; H02; H12; K18; E09; K08
```

**B4. Phụ lục C: mọi câu trỏ vào C phải được đáp, và bỏ câu "khoảng dự phòng" (PL L84 và sau L110).** "Khoảng dự
phòng … phép thử riêng" là thuật ngữ chưa định nghĩa, trỏ ngầm tới phép thử γ của kế hoạch (C17), và lệch Ch4A:107–109.
Ch3:735 hứa C có câu về bản dựng lại, nhưng C chưa có.

(a) Trong PL L84, thay câu thứ hai «15 kịch bản hiệu chỉnh chạy luật C trần 30 giây … không dùng để lập các bảng kết quả
chính.» bằng:

```latex
15 kịch bản hiệu chỉnh chỉ được chạy với luật C trần 30 giây; các lần chạy này chỉ tham gia phép kiểm tính nhất quán
của sổ (mục~\ref{muc:kiemtra}) và không dùng để tính kết quả phục vụ hay đúng giờ.
```

Sửa dòng EV L85: bỏ `C17`, thêm `A26; B10 (170 + 15); Ch4A v5-v3:107-109; Ch3 v4-v3:725-727`.

(b) Thêm vào cuối đoạn L110 (sau câu về đồng hồ) câu:

```latex
Nếu dựng lại bộ chạy từ mã nguồn, bản mới phải cho đúng kết quả đã lưu trên một số kịch bản trước khi được dùng để so
với các số trong khóa luận, vì bản dựng lại có thể khác bản đã lưu.
% EV: I13; A28 (R18 B24); Ch3 v4-v3:733-735; Ch4B v10:434-435
```

**B5. Phụ lục A (PL L11–15): đáp câu trỏ Ch4A:226 và sửa đích tham chiếu.** Ch4A trỏ A để nói mức 30 giây lấy từ tập
tĩnh. A hiện không nhắc 30 giây và trỏ nhầm sang `muc:c4-taptu`.

Thay L11–15 bằng:

```latex
\section{Tập kịch bản tĩnh của đợt thử trước}
\label{phuluc:A}

Tập kịch bản tĩnh thuộc một đợt thử trước, trong đó thời gian đi giữa các điểm không đổi suốt lần chạy. Ở tập này,
cấu hình có trần dùng trần 30 giây cho tổng độ dời giờ trả của mỗi khách, cùng với khóa xe, khóa hai điểm dừng và giữ
cố định giờ đón từ lúc xác nhận. Vì vậy phép so cấu hình này với ghép tự do đo tác dụng của cả gói cam kết, không riêng
của trần. Mức 30 giây được giữ nguyên cho tập kiểm tra chính (mục~\ref{muc:c4-thamdo}). Khóa luận không dùng các kết
quả số của tập này.
% EV: C4A-15 (TEX08:136-137: trần 30 giây, khóa cứng xe và hai điểm dừng, giờ đón cố định); K29 (thời gian đi tĩnh); K33 (cả gói C1 so với B1); K34; E12 không được dùng (NOTES §5 A)
```

### Nên làm

**N1. Câu mở chương và hai đoạn sau của 5.1 (Ch5 L6, L15, L18).** Mục đích: giới thiệu ba phần, định nghĩa "đệm" và
"sổ", nói lợi ích dự báo không riêng của luật C, thêm 82 giây và 41 → 34.

Thay L6 bằng:

```latex
Khóa luận đã đặc tả, cài đặt và đánh giá trên mô phỏng một trần cho phần giờ trả bị dời do điều phối của từng hành
khách trong dịch vụ đi chung xe. Chương này tóm tắt kết quả theo ba phần của độ lệch giờ trả so với lời hứa đầu: phần
tính cho điều phối, phần được hồ sơ tắc đường lịch sử giải thích và phần còn lại; sau đó nêu hạn chế và hướng phát
triển.
% EV: A01; A06; X3-12; B01
```

Thay L15–16 bằng:

```latex
\textbf{Phần được hồ sơ tắc đường lịch sử giải thích:} với luật C trần 30 giây trên 21 kịch bản ngày thường, lời hứa
theo dự báo giảm số khách tới muộn hơn lời hứa đầu quá một phút từ 68 xuống 2 trong 1.471 khách được phục vụ. Kết quả
này tính lại lời hứa trên các lần chạy đã ghi, và không riêng của luật C: với luật hạn chót 30 giây, số khách trễ cũng
giảm từ 66 xuống 2. Trên cả 3.672 yêu cầu của tập kiểm tra chính, khi tính lại lời hứa theo dự báo, luật C có 2.328
lượt không trễ quá một phút. Cách đệm 30 giây, tức cộng thêm 30 giây vào mọi lời hứa của điều phối không trần, cũng cho
đúng 2.328 lượt; ở ngưỡng hai phút, cách đệm cho 2.366 lượt, nhiều hơn 2.338 của luật C, vì phục vụ nhiều hơn 96 lượt
chứ không phải vì ít khách trễ hơn. Đổi lại, lời hứa của cách đệm dài thêm trung bình 37,2 giây, so với 7,4 giây của
luật C (gộp theo khách được phục vụ), và 44 trong 2.434 khách tới sớm hơn lời hứa quá một phút, so với 4 trong 2.338
khách của luật C. Vì vậy, số lượt không trễ ở một ngưỡng chưa đủ để chọn giữa trần và đệm.
% EV: F17; F04; N4B8-01; F03; N4B8-02 (luật hạn chót 66 → 2 trên 1.471); C09; C10; N-16; N-18; N-19; K06; K51
```

Thay L18–19 bằng:

```latex
\textbf{Phần còn lại:} sổ theo từng khách chia số giây trễ của mỗi khách thành ba phần trên, nên cho biết dự báo đang
dùng còn chưa giải thích được bao nhiêu. Với 68 khách ngày thường nói trên, trong 6.217 giây trễ có 82 giây tính cho
điều phối, 5.353 giây được hồ sơ lịch sử giải thích và 783 giây còn lại. Chiều tuyết 15/11/2018 (8 kịch bản) là trường
hợp dự báo không đủ: lời hứa theo dự báo chỉ giảm số khách trễ quá một phút từ 41 xuống 34 trong 601 khách được phục
vụ. Trong 3.445,9 giây trễ của 41 khách đó, 8,6 giây tính cho điều phối, 251,5 giây được hồ sơ lịch sử giải thích và
3.185,9 giây còn lại. Sổ là phép chia theo mô hình và theo dự báo đang dùng; phần còn lại không nên hiểu là phần không
thể biết trước, và sổ không cho biết ai có lỗi.
% EV: F09; N4B8-11 (81,742 + 5.352,646 + 783,018 = 6.217,406 s); F13; B20; N4B-05; K04; K19; X3-12
```

**N2. Phụ lục C, Bảng C.2 và câu về tệp cấu hình (PL L87, L102, L104): ghi tên thư mục và đầu vào thay cho
LOCKS/B1/C1.** LOCKS/B1/C1 không xuất hiện ở bất kỳ chương nào. Người tái lập cần biết thư mục nào ứng với cấu hình nào.

Thay L87 bằng:

```latex
Bảng~\ref{bang:pl-goc} ghi cấu hình và gốc kết quả. Tệp luật của tập kiểm tra chính, tập buổi sáng và chiều tuyết nằm
ở \nolinkurl{tang3/configs/}; các mức thêm của tập buổi sáng ở \nolinkurl{tang3/w07x/configs/}. Đầu vào của các lần chạy
nằm ở \nolinkurl{C:/RideBoundData/research/fixtures-panelA-v1/}, \nolinkurl{fixtures-w07-v1/},
\nolinkurl{fixtures-snow-v1/} và ở các thư mục \nolinkurl{drivers/}, \nolinkurl{worlds/} tương ứng trong
\nolinkurl{tang3/calib/panelA/}, \nolinkurl{tang3/w07/} và \nolinkurl{optimize/snow/}.
% EV: R26 Q8 (tang3/configs/C-30.json, wp4-tier3-v2.json); RW7X:35-40; RUN38:51-54 (FIXTURE_ROOT, DRIVER_ROOT, WORLDS); RUNW07:35-39; run_forecast.py:85-87
```

Thay hàng "Cố định" (L102) bằng:

```latex
Cố định & FREE, U, C-30, C-60, C-120 & \nolinkurl{E:/RideBoundData/wp14r/development-v6-ledger/}; tên thư mục mỗi lần chạy có đuôi \nolinkurl{b1-ref}, \nolinkurl{c1-nobudget}, \nolinkurl{c1-h6ref}, \nolinkurl{c1-budget60}, \nolinkurl{c1-budget120} lần lượt cho FREE, U, C-30, C-60, C-120; kết quả trong \nolinkurl{attempt-01/output/} \\
% EV: B17; X3-19 (b1-ref, c1-nobudget, c1-h6ref); LAD:1-6; danh sách thư mục: 160 = 16 kịch bản × 10 cấu hình, chỉ 5 cấu hình được dùng
```

Thay hàng "Chiều tuyết" (L104) bằng:

```latex
Chiều tuyết & C-30 & \nolinkurl{tier3-forecast-v1/}, tám thư mục \nolinkurl{C-30-d20181115-s10-r1-w14} đến \nolinkurl{C-30-d20181115-s10-r4-w15}; các thư mục khác trong gốc này không thuộc tập \\
% EV: B20; N-26; R26 Q8 (SNOW/C-30-d20181115-s10-r{1,2,3,4}-w{14,15}); danh sách thư mục (9 C-30, 16 C-30F, 17 Mplus-30F, 1 Mplus-30)
```

Bảng C.2 có cột 6,8 cm cho đường dẫn dài. Cần kiểm bố cục sau khi biên dịch. Nếu tràn, chuyển ánh xạ tên thư mục của tập
cố định thành một câu dưới bảng.

**N3. Phụ lục C, ba đoạn ghi chú (PL L110, L113, L116): viết thành câu.**

Thay hai câu đầu của L110 («Cách đọc bảng: … hạt giống 7. wp4-tier3-v2.json dùng phục hồi không tệ hơn kế hoạch giữ.»)
và câu về đồng hồ bằng:

```latex
Cách đọc bảng: các lần chạy trần 120 giây của tập kiểm tra chính nằm ở một gốc riêng. Trừ tập tắc đường cố định, vốn
dùng bộ chạy cũ chưa có luật phục hồi, mọi tập dùng cùng bản bộ chạy đã biên dịch và lưu ở
\nolinkurl{C:/RideBoundData/research/runner-tier3-v2}, dựng từ phiên bản mã nguồn 45f8026 của RideBound. Bản tin khởi
tạo ở đầu mỗi lần chạy ghi mã phiên bản lõi 1ce15e92, FleetPy 1.0.2 và hạt giống ngẫu nhiên 7. Tệp cấu hình
\nolinkurl{wp4-tier3-v2.json} bật luật phục hồi không tệ hơn phương án giữ nguyên kế hoạch (mục~\ref{muc:doichung}). Mô
phỏng chạy theo sự kiện và dừng khi mọi yêu cầu đã được xử lý và mọi khách đã xuống xe; khung giờ hai tiếng chỉ là
khoảng phát sinh yêu cầu, không phải độ dài lần chạy.
% EV: A28; X3-10; N4B8-05; R26 Q1-Q2, Q8; WP4:7; B17; NEW:13
```

(Câu B4(b) nối ngay sau đoạn này.)

Thay L113 bằng:

```latex
Một lần chạy là một cặp kịch bản và cấu hình, mỗi cặp chạy một lần. Khi một lần chạy hỏng vì lỗi hạ tầng, phân tích
dùng bản chạy lại hoàn tất; ở tập kiểm tra chính có đúng một trường hợp như vậy, bản
\nolinkurl{C-30-d20181114-s10-r3-w17-rerun1}. Số lần chạy được dùng là: tập kiểm tra chính 170 lần chạy của năm cấu
hình và 34 lần chạy trần 120 giây; tập buổi sáng 136 trong 192 lần chạy đã lưu; tập tắc đường cố định 16 lần chạy mỗi
cấu hình; chiều tuyết 8 lần chạy. Bản kiểm kê kho dữ liệu ngày 08/10/2026 ghi 1.991 bản ghi lần chạy, gồm cả các đợt
không dùng trong khóa luận; bản kiểm kê này có trước 34 lần chạy trần 120 giây (10/10/2026) và chưa được làm lại.
% EV: B10; L1a-01 (34 lần chạy, 10/10/2026); C4A-07; B17; H13; B20; C4A-17; ADD1:6; B19; C4A-20 (ghi chú: chưa kiểm kê lại sau C-120)
```

Thay L116 bằng:

```latex
Các số đếm chính của Chương~\ref{chuong:thucnghiem} được tính lại từ bản ghi thô của lần chạy bằng các chương trình
đọc dữ liệu: các mốc $v$, $e$, $p$, phần dời và lời hứa theo dự báo. Một khách trễ quá $T$ khi tới muộn hơn lời hứa
quá $T$ giây, tức lớn hơn hẳn; số lượt không trễ quá $T$ bằng số lượt phục vụ trừ số lượt trễ, chia cho mọi yêu cầu.
Độ dài thêm của lời hứa là trung bình gộp theo khách; tỉ lệ trung bình theo kịch bản được ghi rõ ở nơi dùng. Phép phát
lại lời hứa theo dự báo giữ nguyên mọi quyết định và giờ trả thực tế của lần chạy. Hai chương trình đọc viết riêng cho
cùng kết quả trên từng khách trong 7.159 khách được phục vụ của điều phối không trần và luật C trần 30, 120 giây; các
chương trình kiểm này do mô hình ngôn ngữ lớn viết và chạy (mục~\ref{muc:kiemtra}).
% EV: A26; C19; N4B-14 (7.159 = 2.434 + 2.338 + 2.387, 0 lệch); SPEC:28-63; C06; C08; C09; C10; F06; N-16; K41; Ch3 v4-v3:729-731
```

**N4. Mục 5.3 hướng 1, 2, 3, 5 và đoạn chồng lấn của 5.2 (Ch5 L27, L33, L36, L39, L45).** Mục đích: bỏ biệt ngữ, giải
nghĩa hai thứ tự tiêu chí, và cho `phuluc:B` một câu trỏ.

Thay L27 bằng:

```latex
Phần lớn ý nền của khóa luận đã có trong nghiên cứu trước, nên đóng góp hẹp. Fielbaum và Alonso-Mora~\cite{fielbaum2020}
đã đo mức thay đổi của giờ hứa với từng khách và kiểm soát nó ngay khi ra quyết định gán khách. Hörl và
Zwick~\cite{horl2022} đã tính lại giờ trả trên tuyến đang gán theo tắc đường hiện tại, chính là mốc khóa luận dùng.
Schulz và Pfeiffer~\cite{schulz2026} đã đặt hạn chót trả tính từ lời hứa đầu. Chèn khách động và đánh đổi giữa phục vụ
với độ ổn định của lời hứa cũng đã có tiền lệ. Phần của khóa luận là đặc tả, cài đặt và kiểm một trần chung cho mọi
khách đã nhận trên tổng phần dời do điều phối trong cả chuyến, không nới theo tắc đường, kèm sổ theo từng khách, và đo
cái giá của trần đó.
% EV: J06; J08; J01; J03; J05; J10; J38; K30; K31
```

Thay L33 bằng:

```latex
Thứ nhất, cần chạy đủ bốn tổ hợp giữa hai thứ tự tiêu chí của bộ chọn, ưu tiên ổn định như hiện nay và ưu tiên chi phí
kế hoạch, với hai cấu hình, điều phối không trần và luật C trần 30 giây, trên 34 kịch bản của tập kiểm tra chính.
Trước khi so, bộ chạy dựng lại phải cho đúng kết quả đã lưu trên một số kịch bản. Phép thử cần báo lượt phục vụ, lượt
trễ, lượt không trễ và số khách đi chung, để biết đánh đổi giữa phục vụ và đúng giờ còn giữ không khi bộ chọn đổi; phép
sàng lọc ở mục~\ref{muc:c4-vaitro} chưa trả lời được câu hỏi này.
```

Thay L36 bằng:

```latex
Thứ hai, cần cài đặt và chạy luật giới hạn từng lần dời cạnh luật C, để biết việc cộng dồn các lần dời có đổi kết quả
hay không. Cũng cần chạy làm đối chứng hạn chót nới theo giờ trả tính lại khi giữ kế hoạch, dựng từ công thức 7 của
Hörl và Zwick (Phụ lục~\ref{phuluc:B}), để biết việc đo từ mốc này thay vì từ lời hứa đầu có đổi kết quả hay không.
```

Trong L39, thay «bằng dữ liệu có đúng tại thời điểm hứa» bằng «chỉ dùng dữ liệu đã có tại thời điểm hứa».

Trong L45, thay câu thứ hai bằng «Mỗi cấu hình cần được chạy mô phỏng đầy đủ, không suy số khách được phục vụ từ phép
sàng lọc trên các lần chạy cũ.»

Giữ nguyên các dòng EV hiện có; thêm `H10` cho L33 và `A22; J05` cho L36.

**N5. Phụ lục B (PL L21, L26, L32, L38, L44, L47): khung cho các ví dụ, ghi công đúng, câu đọc bảng thật, ký hiệu khớp
Ch3.**

Thay L21 bằng:

```latex
Bảng~\ref{bang:pl-giunguyen} xét riêng phép kiểm giờ trả của từng luật đối với phương án giữ nguyên kế hoạch, dưới giả
thiết (N) ở mục~\ref{muc:giunguyen} và khi phần trần đã dùng của mỗi khách nằm giữa 0 và $B$. Với phương án này,
$p = e$. Qua được phép kiểm giờ trả không có nghĩa là phương án qua mọi ràng buộc khác.
```

Trong chú thích bảng (L26), thay "$L$ là phần trần đã dùng" bằng "$L_r$ là phần trần khách $r$ đã dùng", và "$L^{\mathrm{V}}$
là tổng độ dời khách thấy đã dùng" bằng "$L^{\mathrm{V}}_r$ là tổng $|z|$ đã tính cho khách $r$". Đổi tương ứng ở L32
(«Có, khi $0\le L_r\le B$ & $L_r+|e-e|=L_r\le B$ (Nhận xét~\ref{nx:giunguyen}).») và L36 («$L^{\mathrm{V}}_r+|e-v|$ có
thể vượt $B$.»).

Trong L38, thay câu thứ hai bằng «Đây là biến thể khóa luận dựng từ công thức 7 của Hörl và Zwick~\cite{horl2022},
không phải luật trong bài của họ; chưa được chạy.»

Thay L44 bằng:

```latex
Cách đọc bảng: luật C và hạn chót nới luôn cho phương án giữ nguyên qua, vì phương án này không thêm phần dời do điều
phối; luật hạn chót và luật trần độ dời khách thấy có thể loại cả phương án không đổi gì, chỉ vì tắc đường làm $e$ lùi.
```

Thay L47 bằng:

```latex
Các ví dụ dựng tay sau, mọi mốc tính bằng giây, cho thấy ba đại lượng mà ba luật kiểm không thay được cho nhau: phần
dời do điều phối $c$ của luật C, độ lệch hai đầu $p_n - p_0$ của luật hạn chót (công thức~\eqref{eq:dongnhat}) và tổng
độ dời khách thấy $\sum|z|$:
```

### Sửa nhỏ, không xếp hạng, và ghi chú khi ghép

1. **Tên tệp khi ghép.** Ch5 vào `noi-dung/09-chuong5.tex` (main.tex:117), không phải `10-…`. PL đã chứa `\appendix`, nên
   khi `\input{noi-dung/11-phuluc}` sau `10-tai-lieu`, không bọc thêm `\appendix`. Bọc thêm cũng vô hại, nhưng thừa.
2. **Ký hiệu luật trong câu văn** (PL L113): "C-30", "C-120" → "luật C trần 30 giây", "trần 120 giây". N3 đã làm việc
   này.
3. **Đường dẫn có `ridebound-scratchpad`** (PL L63). Theo STYLE mục dung hòa 6, đường dẫn được phép ở phụ lục. Nên thêm
   một câu đầu Phụ lục C: «Các đường dẫn dưới đây là đường dẫn trên máy chạy thực nghiệm.»
4. **Bộ chạy cũ của tập cố định.** Có thể thêm «bộ chạy cũ ghi mã lõi 38d517d» (B17, VERIFIED-by-Codex R15). Không bắt
   buộc.
5. **Các lần chạy khác của Chương 4 chưa có gốc trong C:**
   - phép thử đưa dự báo vào bộ điều phối (thư mục `C-30F-…`, `Mplus-30F-…` trong `tier3-forecast-v1`; Ch4B:181–188);
   - phép học máy (Ch4B:190–211);
   - phép sàng lọc bộ chọn (Ch4B:25–29).

   Một câu "các phép thử phụ ở mục 4.6–4.7 dùng các lần chạy đã ghi của …" đủ dùng. Riêng con số 17 thư mục `Mplus-30F`
   so với 16 kịch bản tôi không kiểm (CANNOT CHECK).
6. **NOTES §4** ghi nguồn là Ch4A v4 và Ch4B v7. Bản ghép là v5-v3 và v10. Tôi đã kiểm lại mọi số Ch5 trên hai bản mới:
   không đổi.
7. **Ngân sách trang.**
   - Sau B2, B3 và N1, Ch5 tăng khoảng 250 tiếng: từ 963 lên khoảng 1.210 tiếng (đếm bằng `r32/sentlen.py`).
   - Theo thước 330 tiếng/trang, thế là khoảng 3,7 trang. Theo mật độ đo ở bản biên dịch thử (khoảng 500 tiếng/trang,
     ASSEMBLY "Trial build"), thế là khoảng 2,4 trang. Vẫn trong 3 trang.
   - Nếu cần cắt, cắt hướng 4 của 5.3 xuống một câu. Không cắt các vế bất lợi.
8. **Thuật ngữ đồng nhất.** Ch5 dùng "tập chính" (L15, L24) và "tập kiểm tra chính" (L33). Dùng một tên "tập kiểm tra
   chính" (OUTLINE §2 quy tắc 6).
9. **Câu tóm "đạt / chưa đạt"** (tùy chọn, cuối 5.1):

   «Tóm lại, khóa luận đã đặc tả, cài đặt và kiểm một trần cho phần dời do điều phối, đo được cái giá của nó trên một
   mô phỏng, và tách được phần dự báo lịch sử giải thích được. Khóa luận chưa cho biết trần có giá trị với khách hay hãng
   xe, chưa tách vai trò của bộ chọn, và chưa có cách hứa tốt cho ngày bất thường.»

   Dòng EV: `I10; H02; H12; F13; K38`.
10. **Dòng `% EV:` của L12** đang trỏ `A02; J03` cho câu Hörl và Zwick. Nên thêm `J01` (mốc tính lại trên tuyến đang gán)
    và `J05` (khác biệt suy từ định nghĩa).
