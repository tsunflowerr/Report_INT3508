# CH2 — Nhật ký sửa Chương 2 theo bản kiểm nguồn Codex R35 và bản nhận xét R30 (2026-10-13)

**Bản dùng để ghép: `drafts/06-chuong2-v6.tex`.**
- `-v5.tex`: lượt sửa đủ mọi nhận xét dưới đây; tổng chữ 3.396 tiếng, tức +5,8% so với v4, vượt hạn 5% một chút.
  Không dùng.
- `-v6.tex`: v5 rút thêm năm câu (mở chương; câu giữ giờ đón ở mục 2.1; vế "Ngoài cửa sổ đón…" ở mục 2.3; câu Leonardi;
  câu TLC), không đổi nội dung sự kiện nào. Tổng 3.358 tiếng, +4,6%. **Bản ghép.**
- Ghi chú: `drafts/06-chuong2-v5-NOTES.md`, tên theo yêu cầu đầu ra, **nội dung mô tả v6**.

**Đầu vào.** Bản v4 (266 dòng). Hai bản nhận xét: Codex
`optimize/codex-debate/codex-work/r35-ch2-check/R35-CH2-FACTCHECK-CODEX-v2.md` (**CX**, 156 mục F, T, M, P, E; đề xuất
C1–C14) và `reviews/R30-READER-LECTURER-CH2-CLAUDE.md` (**RL**, phần bắt buộc B1–B5 và phần nên N1–N5).

**Cách kiểm.** Không nhận một nhận xét chỉ vì người nhận xét nói vậy. Tôi mở lại nguồn ở các trích đoạn của R35
(`r35-source-*.txt`, `agent-*-extract.txt`) và, cho các điểm quyết định, chính tệp PDF bằng `pdftotext` (chỉ đọc, ra
stdout): Hörl–Zwick `claude-work/pdf/hoerl-zwick-2022.pdf` PDF tr. 5, 8–9, 13; Alonso-Mora PDF tr. 3
(`E:/RideBoundData/literature-survey-2026-10-06/pdf/alonso-mora-pnas2017.pdf`); DeeprETA PDF tr. 3, 9, 10. Tóm tắt Yu
và cộng sự đọc từ JSON Crossref đã lưu (`SP5/ch2/dl-crossref/cr13.json`). **QĐ:** **A** = nhận; **M** = nhận có sửa (lý do
kèm); **R** = không nhận (lý do và trang kèm); **CC** = không kiểm được. "Dòng v4" là dòng của v4; "v6" chỉ chỗ trong v6.
Trang "tr." là trang in trên bài (Hörl–Zwick: PDF = trang in + 1; Elmi: PDF = trang in + 1; Schulz–Pfeiffer: trang in
541–586). Không mô phỏng, build, cài, xóa; không ghi vào thư mục luận văn, `E:/Code/RideBound*` hay `C:/Code/*`.

**Ràng buộc trang.** Bản dựng thử 13/10 đo v4 là 7 trang (ngân sách 6,5); yêu cầu là không tăng chữ quá 5%. Bộ đếm
`wc_ch3_v2.py` (cùng bộ đếm của v4): v4 = 2.575 văn xuôi + 634 trong bảng = 3.209; v6 = 2.749 + 609 = 3.358 (+4,6%;
văn xuôi +6,8%, bảng −3,9%). Vì vậy nhiều đề xuất làm dài thêm được nhận ở dạng rút gọn (M), và một số câu đúng của v4
bị cắt để lấy chỗ; mỗi chỗ cắt ghi ở hàng tương ứng.

---

## 1. Chỗ hai bản nhận xét khác nhau, hoặc khác văn bản, và cách giải bằng nguồn

| # | Vấn đề | Ý kiến | Bằng chứng tôi kiểm | Kết luận |
|---|---|---|---|---|
| D1 | Hạn trả được nới của Hörl–Zwick là giờ nào, và khi nào | v4 dòng 156 "giờ trả cập nhật", dòng 158 "mức sớm nhất có thể"; RL B1: tự mâu thuẫn, hãy mở bài; CX F53, C1: nêu điều kiện vượt hạn | PDF tr. 9 (in tr. 8) dòng 8: "For strategy (B), for all requests that are assigned to the currently evaluated vehicle: t_required = max(t_updated, t_latest)" (7); in tr. 7 dòng 31–35: giờ cập nhật có "by traversing the routes" đang gán; dòng 37–39 "the absolute minimum, given current traffic conditions" là lời diễn giải của tác giả | Mốc là giờ trả cập nhật trên tuyến đang gán. Hạn chỉ được nới khi giờ này đã vượt giờ trả muộn nhất. v6 dòng 157–164 và ví dụ dòng 167–171 viết đúng như vậy; bỏ cụm "mức sớm nhất có thể". |
| D2 | "Thuật toán không rơi vào tình huống hết thứ tự trả khả thi" | RL B1 đề xuất gắn cho tác giả ("theo các tác giả, … luôn còn ít nhất một thứ tự"); CX F54: nói quá, còn cần công thức 8 và việc thêm tuyến đang gán | In tr. 7 dòng 8–17: bài nêu vấn đề ("may lead the algorithm to not finding any feasible sequence"); in tr. 8 dòng 24–27: thêm tuyến đang gán. Bài không viết câu bảo đảm "luôn còn" | Chỉ gắn cho bài phần vấn đề ("Bài chỉ ra rằng khi thời gian đi tăng, xe đang chở khách có thể không còn thứ tự trả khách nào…"). Không viết câu bảo đảm. |
| D3 | Ô "phần do tắc đường" của Schulz–Pfeiffer | v4: "khi thời gian đi đổi thì có"; RL B3: giữ, ghi "(suy từ định nghĩa)"; CX T211: REJECT | Schulz–Pfeiffer tr. 549: "Let t_jj′ be the travel time from location j to location j′" (thời gian đi cho trước); không có mô hình thời gian đi đổi | Theo CX: "Ngoài phạm vi: thời gian đi cho trước". Nói bài sẽ làm gì khi thời gian đi đổi là đoán, không phải suy từ định nghĩa. |
| D4 | Cột cuối Bảng 2.2 | v4 "Ghi riêng cho từng khách?" với hàng loạt ô "Không"; RL B3: "Có sổ ghi phần đã dùng của từng khách?"; CX C3: "Lưu tổng độ lớn các lần dời cho từng khách?" và ô "Bài không mô tả sổ này"; yêu cầu của người điều phối: tách dữ liệu riêng từng khách khỏi sổ cộng độ lớn | Các bài có hạn chót riêng (SP tr. 549–550), điểm và độ chùng riêng (Elmi tr. 5, 11–12), giờ cập nhật riêng (HZ tr. 7), thời gian chuyến đã chấp nhận riêng (MTK tr. 5) | Cột 5 hỏi "Cộng độ lớn các lần dời qua cả chuyến?" (Không / Có). Cột 6 đổi thành "Dữ liệu giữ riêng cho từng khách" và ghi đúng dữ liệu mỗi bài giữ; hàng luật C ghi "Phần trần đã dùng, ghi trong sổ". Như vậy không ô nào phủ nhận dữ liệu riêng của các bài. |
| D5 | Câu "1 mili giây" | RL B5: viết lại ("tình huống dời muộn rồi kéo về … gần như không xảy ra; khác biệt giữa hai cách đo hiện mới nằm ở định nghĩa"); CX F44, C9: giới hạn vào tác dụng của chiều sớm | ADD1 mục 0.2: mọi lần dời sớm do điều phối trên 34 kịch bản đúng −1 ms, "nên vế giá trị tuyệt đối thuộc định nghĩa"; không nêu nguyên nhân. Chương 3 v4 (r33) dòng 297–300 đã viết đúng phạm vi này | Câu của RL sai phạm vi: 1 ms nói về phần dời do điều phối, không về phần khách thấy, và khác biệt giữa thước đo của Fielbaum–Alonso-Mora với luật C còn ở mốc so và việc cộng qua cả chuyến. Bỏ câu khỏi Chương 2; Chương 3 giữ câu đúng. |
| D6 | Tỉ lệ lấy từ bài khác (Fielbaum–Alonso-Mora, Elmi) không có số đếm | CX C4, C8: thay bằng mô tả định tính; RL N3, N5: giữ và thêm số; người điều phối: "sửa 'cùng 29%' và phạm vi của tỉ lệ" | FAM tr. 17, bảng 5 (34,5%, 45,6%, 31,2%); tr. 9: 19.610 yêu cầu, nhưng tr. 9–10 ghi tỉ lệ phục vụ cơ sở 66,5% (bảng 1), không khớp 100% − 34,5%, nên không chắc bảng 5 dùng đúng mẫu đó. Elmi tr. 16: mỗi điểm là trung bình 10 ngày; tr. 19: 29,09% và 29,21%; tr. 18: 83,85% | Giữ tỉ lệ của bài khi nó mang lập luận, ghi nguồn bảng và cách gộp ("theo bảng 5 của bài"; "trung bình trên 10 ngày"); không dựng số đếm từ tỉ lệ đã làm tròn; không gắn mẫu số 19.610 vào bảng 5. Câu hỏi mở cho chủ nghiên cứu (NOTES mục 6). |
| D7 | Ký hiệu $c_{ko}$ | RL N4: bài gốc viết $c_{k0}$, đổi | Alonso-Mora PDF tr. 3 (pdftotext 13/10): "plus a large constant cko for each unassigned request", hai tập "Rok", "Rko" | Bài viết "ko" (cặp ok/ko). Giữ $c_{ko}$ (in nghiêng, không còn `\mathrm`) và thêm "(ký hiệu theo bài gốc)". |
| D8 | "Khách đã nhận" hay "khách đã xác nhận" không bị chuyển xe | RL G, N4: đổi thành "đã xác nhận đặt xe" theo khóa ở Chương 3 | X3-39: "Không cấu hình nào cho chuyển khách đã nhận sang xe khác: giữ khách đã nhận là ràng buộc cấu trúc" | Câu của v4 đúng và mạnh hơn khóa. Giữ nghĩa, viết "yêu cầu đã được nhận", khớp vòng đời "yêu cầu được nhận" của Chương 3 dòng 76. |
| D9 | Chữ "thường" trong câu TLC | RL N2: lời rào không có nguồn, bỏ | C2-16: trang TLC "typically with a two-month delay"; CX F67 mở lại trang ngày 13/10 | Giữ "thường"; thêm "hiện" để nói đây là lịch công bố hiện nay. Ngày truy cập ghi trong mục tài liệu, không đưa vào thân bài. |
| D10 | Điều kiện của "tác động nhỏ" ở Hörl–Zwick | RL B1: [kiểm với bài, tr. 14] | In tr. 12 dòng 26–37: kịch bản tốc độ thực đổi theo giờ (TomTom, tr. 10), tỉ lệ từ chối quanh 32%, độ trễ trung bình dưới 1 giây; tr. 14 dòng 12–15: "effects are minor in a scenario with realistic travel times" | v6 dòng 226–228: "với tốc độ thực đổi theo giờ, ảnh hưởng này nhỏ". |
| D11 | Con số 47,8% của Elmi (v4 NOTES: chưa rõ là điểm phần trăm hay giảm tương đối) | — | Elmi tr. 18: 63,17% xuống 15,39%, "an absolute reduction of 47.78%" | Là điểm phần trăm. Vẫn không dùng (ngân sách trang); ghi vào NOTES. |

---

## 2. Bản nhận xét RL (người đọc, giảng viên): B1–B5, N1–N5

| ID | Dòng v4 | Nhận xét | Bằng chứng đã kiểm | QĐ | Thay đổi (v6) |
|---|---|---|---|---|---|
| B1 | 153–160 | Đoạn Hörl–Zwick tự mâu thuẫn (156 với 158); ba tên mới trong một câu; "giờ trả muộn nhất" chưa định nghĩa; quan hệ nhân quả không gắn tác giả; điều kiện của "tác động nhỏ" chưa rõ | D1, D2, D10; HZ in tr. 4 dòng 34–35: giờ muộn nhất tính từ thời gian chờ tối đa và độ vòng cho phép | M | Viết lại dòng 157–164: định nghĩa giờ trả muộn nhất; vấn đề gắn cho bài; giờ trả cập nhật; công thức 7 cho "các yêu cầu đã gán cho xe đang xét"; ràng buộc cứng; phạt theo giây (11); câu điều kiện "chỉ được nới khi … đã vượt"; công thức 8. Kết luận của bài chuyển sang mục 2.4 (dòng 226–228) kèm điều kiện. Không dùng câu "theo các tác giả, … luôn còn ít nhất một thứ tự" (D2). Bỏ khoản phạt cố định β và việc thêm tuyến đang gán (đúng nguồn, cắt vì trang). |
| B2 | 206–211 | Câu định vị 58 tiếng, năm ý; "không nới theo tắc đường" mâu thuẫn bề ngoài với mốc đổi theo tắc đường; "cộng có dấu", "quay về" chưa giải thích | Ch3 r33 dòng 442–468 (eq:dongnhat, tiền lệ HZ); A12; J05; J11; D03 §10 | M | Dòng 211–219: "Bảng 2.2 cho thấy…" làm câu đọc bảng; tách ý: đại lượng bị giới hạn; trần chung cho mọi khách đã xác nhận; sổ; phần thay đổi khi giữ nguyên kế hoạch không bị tính, trần không được nới; giải thích "cộng có dấu" bằng "để các lần dời sớm, muộn bù trừ nhau"; dùng tên "luật hạn chót" (OUTLINE quy tắc 6) và thêm vế mượn thành phần hạn chót của Schulz–Pfeiffer (CX C10). Dùng "phần thay đổi khi giữ nguyên kế hoạch" thay cho "phần do tắc đường" của B2 (GLOSSARY-v2 mục C). Vế "trong khoảng còn lại tới giờ trả muộn nhất, bộ điều phối vẫn được dời giờ trả" của B2 đúng (D1) nhưng được nói bằng ví dụ dòng 167–171 cho đỡ chữ. |
| B3 | 165–204 | Bảng 2.2 tự mâu thuẫn: cột 5 với câu cộng có dấu; cột 6 với dòng Elmi; ô SP là suy luận; tên dòng HZ mang số công thức; ô "Áp cho ai" trộn "khi nào"; thiếu câu đọc bảng | D3, D4; HZ in tr. 8 dòng 8 | M | Cột 5 đổi tên đúng như B3; cột 6 theo D4 (khác B3); chú thích giải nghĩa "Không" và nói cột 3 là cách khóa luận đọc định nghĩa; ô SP theo D3 (không dùng biến thể "(suy từ định nghĩa)" của B3); tên dòng HZ "Hạn trả được nới (công thức 7)"; "Áp cho ai" = "Các yêu cầu đã gán cho xe đang xét" (đúng chữ công thức 7, không phải "khách trên xe" như B3); điều kiện chuyển sang cột 2–3. Không thêm "trần chung, ví dụ 30 giây" vào ô luật C (trang; trần đã định nghĩa ở đoạn mở và mục 2.5). Câu đọc bảng ở dòng 211; không dùng câu đọc bảng của B3 vì vế "cả hai không để riêng tắc đường làm tuyến bị loại" chỉ đúng cho HZ sau khi giờ cập nhật vượt hạn (CX T215). Bỏ dòng "Cửa sổ đón; ngồi xe" khỏi Bảng 2.2 (trùng Bảng 2.1), thay bằng một câu trong chú thích. |
| B4 | 242–244 | "Mức trần" trùng tên trần B và là khẳng định cận trên chưa chứng minh | I02 (chính sổ dùng chữ "mức trần"); F10; CX F73, C11 | A | Dòng 243–245: "thời gian đi trong mô phỏng có thể dễ dự báo hơn ngoài đời; kết quả … vì vậy có thể lạc quan hơn khi áp dụng thật". Hai vế ghi là suy luận trong dòng EV. |
| B5 | 134–136 | Câu "1 mili giây" khó hiểu, đưa kết quả Chương 4 vào chương cơ sở | D5; ADD1 mục 0.2; N-05 | M | Bỏ câu khỏi Chương 2 (dòng 138–142 chỉ còn cách đo của luật C và trỏ mục 3.2). Văn bản thay thế của B5 không dùng (sai phạm vi, D5). Hai điểm B5 dặn kiểm: (a) "mỗi lần" đúng cho U, C-30, C-120, M⁺-30 trên tập kiểm tra chính (ADD1 0.2); (b) nguyên nhân −1 ms chưa kiểm, ADD1 dặn không nêu. |
| N1 | sau 206–211 | Thêm ví dụ dựng tay so luật C với công thức 7 và hạn chót | HZ in tr. 8 (7), (10); định nghĩa luật C (Ch3 r33 dòng 309–326); số học tự kiểm: 8:32:00 → 8:32:20 → 8:32:40 dưới hạn 8:35:00; luật C 20 + 20 = 40 > 30 | M | Dòng 167–171, rút gọn; bỏ vế luật hạn chót (Chương 3 đã có ví dụ 9:10 cho luật này); **thêm vế ngược lại** cho công bằng: khi giờ giữ nguyên kế hoạch đã là 8:36:00, công thức 7 không cho dời thêm còn luật C vẫn cho dùng phần trần còn lại. |
| N2 | 233–235, 262–264 | Đánh dấu suy luận TLC và "chưa có chuẩn ngành"; bỏ "thường"; ghi ngày truy cập | D9; C2-16; D03:260; CX F68, F82 | M | Dòng 247–253: giả định ghi rõ ("đây là giả định của khóa luận, chưa được kiểm"), không còn suy "hãng xe phải có dữ liệu của chính mình" (thành "cần nguồn dữ liệu kịp thời hơn, ví dụ…"). Dòng 270–274: "khóa luận chưa có căn cứ bên ngoài để coi mức trần này là chuẩn dịch vụ" (theo CX C12, gọn hơn câu "chưa tìm thấy chuẩn ngành" của N2). **R** phần bỏ "thường" (D9). Ngày truy cập để ở mục tài liệu (BIB). Câu "Suy từ định nghĩa" của dòng 57–58 bị bỏ hẳn theo CX F18 thay vì được đánh dấu. |
| N3 | 117–121 | "Kịch bản" trùng nghĩa Chương 3; câu dài bốn số; "còn 31,2%" không nói so với gì; thiếu đơn vị chi phí | FAM tr. 17 (hai mức, bảng 5 "All times are in minutes"); tr. 18 bảng 6 (trọng số: một phút ngồi xe 1, một phút chờ 2, một lần từ chối 40) | M | Dòng 122–128: "mức" thay "kịch bản"; tách câu tỉ lệ và câu chi phí; đơn vị "quy ra phút ngồi xe theo trọng số của bài"; "còn 31,2%" đứng sau 34,5% của câu trước; thêm "nhưng không giữ độ vòng hay giờ trả" (CX C8). Giữ "khoảng 50%" của bài, không dùng số phút của CX (trang). |
| N4 | 40–53, 62–66 | Ký hiệu, "với", chỉ số $k$ lệch Chương 3; "bước chọn", "phương án", "bộ chọn", "thứ tự tiêu chí" chưa giải thích; "thay cho một tổng chi phí" lệch Bảng 3.2; "khách đã nhận" lệch mốc xác nhận | D7, D8; Ch3 r33 dòng 142–149 (tổng chi phí là tiêu chí 4); GLOSSARY-v2 mục H ("quy hoạch nguyên") | M | Dòng 41: "Bước thứ hai, bước chọn"; công thức tách bằng `aligned`, "thỏa" thay "với"; dòng 52–53 "(ký hiệu theo bài gốc)"; dòng 65–70: phương án, bộ chọn (selector), thứ tự tiêu chí với tổng chi phí là tiêu chí xếp sau. **R** ba điểm: $c_{k0}$ (D7); "quy hoạch tuyến tính nguyên" (GLOSSARY-v2 H và Chương 3 dùng "quy hoạch nguyên"); "đã xác nhận đặt xe" (D8). |
| N5 | 124–128 | Không định nghĩa điểm khả năng đi chung; phép so 83,9% không có vế đối; "cạnh" | Elmi tr. 1, 11 (điểm = số yêu cầu có thể ghép từ lúc gán tới lúc trả), tr. 12 (hai cách điều khiển), tr. 16–19 | M | Dòng 130–136: định nghĩa điểm một vế; độ chùng "tính riêng cho thời gian chờ và cho độ trễ" (bỏ chữ "hay" hai nghĩa); vế đối "còn cách siết đều gần như không bảo đảm được cho ai" (tr. 18 "cannot be provided to anybody"); "29,1% và 29,2%, trung bình trên 10 ngày" thay "cùng 29%"; "đoạn đường". |

**Các mục đánh số 1–67 của Phần 1 RL** không phải phạm vi bắt buộc; những mục được làm cùng lúc: 2 (tập trung vào giờ
trả), 4 (sức chứa từng xe), 5 (định nghĩa DARP), 6, 7, 10, 12–14 (qua CX C5), 17, 18 (Molenbruch, FleetPy 40%), 19 (đơn
vị, bỏ "8 xe" khỏi ô sức chứa), 22–24 (độ vòng được định nghĩa), 28, 31, 36, 46, 55, 56, 61, 63–66. Mục 3 làm một nửa:
đoạn mở có định nghĩa một câu của luật C. Các mục 9, 25, 43, 45, 57 (ví dụ, chi tiết thêm) không làm vì ngân sách trang.

---

## 3. Bản kiểm nguồn CX (156 mục)

Với mục CX đã ACCEPT và không đòi sửa, "A" nghĩa là tôi đồng ý và v6 giữ đúng sự kiện; cột bằng chứng ghi nguồn tôi đã
mở lại, hoặc "dựa vào kiểm của CX" khi tôi không mở lại.

### 3.1 Câu văn và công thức (F01–F84)

| ID | Dòng v4 | Nhận xét CX | Bằng chứng đã kiểm | QĐ | Thay đổi (v6) |
|---|---|---|---|---|---|
| F01 | 24–25 | ACCEPT: yêu cầu, sức chứa | SP tr. 549 | A | Dòng 26–27, "mỗi xe … không quá số chỗ" (RL 4). |
| F02 | 25–26 | ACCEPT: nhiệm vụ bộ điều phối | dựa vào kiểm của CX | A | Không đổi. |
| F03 | 26–28 | ACCEPT: định nghĩa DARP | MOL PDF tr. 3 | A | Dòng 28–30, lời gọn hơn (RL 5). |
| F04 | 28 | ACCEPT: yêu cầu chỉ biết khi gửi | SP tr. 549 "not known beforehand" | A | Không đổi. |
| F05 | 28–29 | ACCEPT: giải lại mỗi lượt | dựa vào kiểm của CX | A | Không đổi. |
| F06 | 32 | ACCEPT: AM17 gán theo lô | AM17 tr. 3–4 | A | "cho dịch vụ đi chung xe" (RL 7). |
| F07 | 33 | ACCEPT: lô 30 giây | AM17 tr. 4–5 | A | Không đổi. |
| F08 | 34–35 | ACCEPT: dựng RV, RTV | AM17 tr. 3 | A | Gộp thành một câu "Bước thứ nhất dựng đồ thị…". |
| F09 | 35–37 | ACCEPT: điều kiện nhóm con | AM17 tr. 3 | A | Câu điều kiện nhóm con bị cắt (trang); giữ "các nhóm được dựng dần từ nhỏ đến lớn". |
| F10 | 37 | ACCEPT: HZ và FleetPy dùng AM17 | HZ in tr. 4–5; FLEET tr. 11 | A | Không đổi. |
| F11 | 40–48 | ACCEPT: ILP đúng | AM17 tr. 3–4 | A | Công thức tách ba dòng bằng `aligned`, nghĩa không đổi (sửa tràn 80,5 pt). |
| F12 | 49–50 | ACCEPT: c_ij gồm khách trên xe | AM17 tr. 3, công thức (1) | A | Không đổi. |
| F13 | 50–51 | ACCEPT: c_ko | AM17 PDF tr. 3 (D7) | A | Thêm "(ký hiệu theo bài gốc)". |
| F14 | 51–52 | ACCEPT: định nghĩa độ trễ | AM17 tr. 3 | A | Không đổi. |
| F15 | 52–53 | ACCEPT: hai ràng buộc | AM17 tr. 4 | A | Không đổi. |
| F16 | 56–57 | OVERSTATED: không phải mọi lần ghép đều làm tăng độ trễ khách cũ | AM17 tr. 3–4 | A | Dòng 59–60 theo C5: "có tính độ trễ của khách đang trên xe, nhưng chỉ như một khoản chi phí…". |
| F17 | 57–58 | ACCEPT, cảnh báo đừng suy rộng rằng AM17 không bảo vệ lời hứa | AM17 tr. 4: giờ đón muộn nhất hạ về giờ đón dự kiến | A | Giữ giờ đón của AM17 nêu ở mục 2.3 (dòng 149–151) và Bảng 2.2 (dòng 188). |
| F18 | 58 | WRONG/REJECT: "miễn là mỗi lần tổng chi phí nhỏ hơn" | AM17 tr. 4: ILP chọn trong cùng lượt; không có điều kiện giảm so lượt trước | A | Bỏ vế; thay bằng "ngoài độ trễ tối đa, bài không đặt trần riêng lên tổng độ lớn các lần dời giờ trả của từng khách" (dòng 60–61; C5). |
| F19 | 59 | ACCEPT | AM17 tr. 3 | A | Dòng 61–62, lời gọn. |
| F20 | 62 | ACCEPT | X3-03, X3-22 | A | Không đổi. |
| F21 | 63–64 | ACCEPT | X3-03 | A | Lời gọn. |
| F22 | 64–66 | ACCEPT | X3-07, X3-39; Ch3 r33 Bảng 3.2 | A | Sửa "thay cho một tổng chi phí" (RL N4); "yêu cầu đã được nhận" (D8). |
| F23 | 96–98 | ACCEPT | AM17 tr. 5; PPV:594 | A | Dòng 100–102, thêm "kể cả cửa sổ đón rộng hơn các giá trị đã trích". |
| F24 | 104–106 | ACCEPT | FAM tr. 4 | A | Không đổi về nghĩa. |
| F25 | 106–107 | ACCEPT | FAM tr. 5 | A | "Với mỗi khách" (RL 23). |
| F26 | 107–108 | ACCEPT | FAM tr. 5, 7 | A | Định nghĩa độ vòng theo FAM tr. 5 ("Real detour … difference between tv(r) and the time required by the shortest path"). |
| F27 | 111–112 | ACCEPT | FAM tr. 9 | A | Bỏ số nút, cạnh và đội xe (RL H, trang); giữ 19.610 yêu cầu, khung giờ, ngày. |
| F28 | 112 | ACCEPT | FAM tr. 9 | A | "vì thời gian đi khá ổn định". |
| F29 | 112–114 | AGREE nhưng sửa: thay "hơn một phần ba" bằng mô tả định tính | FAM tr. 1 (tóm tắt) | M | Giữ "hơn một phần ba" của tóm tắt, với đúng phạm vi ("khi không hạn chế việc chuyển khách", "số yêu cầu không bị từ chối ngay"); D6; câu hỏi mở. |
| F30 | 113–114 | OVERSTATED: "tương đương" → "cùng cỡ" | FAM tr. 1 "comparable" | A | Vế này bị cắt (trang), nên không còn nói quá. |
| F31 | 117 | ACCEPT | FAM tr. 17 | A | "Ở mục 6, họ đưa việc kiểm soát vào bước gán xe" (RL 28). |
| F32 | 117–118 | ACCEPT, thêm giới hạn của mức "hoàn toàn" | FAM tr. 17: chỉ hạ thời gian chờ tối đa; bảng 5: độ vòng 0,65 → 0,94 | A | Thêm "nhưng không giữ độ vòng hay giờ trả" (dòng 123). |
| F33 | 118–119 | AGREE; bỏ tỉ lệ vì thiếu số đếm, giữ chi phí | FAM tr. 17 bảng 5; tr. 18 bảng 6 | M | Giữ 34,5% → 45,6% với nguồn "theo bảng 5 của bài" (D6); tách câu; thêm đơn vị chi phí. |
| F34 | 119–120 | AGREE; dùng số phút thay "khoảng 50%", bỏ tỉ lệ | FAM tr. 17: "increased in about 50% on average" | M | Giữ 31,2% và "khoảng 50%" (lời của bài, là mức tăng của trung bình, không phải tỉ lệ khách); không thêm số phút (trang). |
| F35 | 120–121 | ACCEPT | FAM tr. 18 | A | Câu hỏi mở thêm "độ trễ hay thời gian chờ" (C8). Câu "kết luận có đánh đổi" bỏ vì "Đổi lại" đã nói. |
| F36 | 124 | ACCEPT | Elmi tr. 1–2 | A | Không đổi. |
| F37 | 124–125 | ACCEPT | Elmi tr. 5 công thức (2) | A | "tính riêng cho thời gian chờ và cho độ trễ" (RL 33). |
| F38 | 125–126 | ACCEPT | Elmi tr. 12 | A | Không đổi về nghĩa. |
| F39 | 126 | ACCEPT | Elmi tr. 13 | A | Phạm vi thời gian đi cố định đặt cuối câu so sánh. |
| F40 | 126–128 | OVERSTATED: "cùng 29%"; trung bình 10 ngày | Elmi tr. 16, 18, 19 (D6) | M | "ở tỉ lệ từ chối gần bằng nhau (29,1% và 29,2%, trung bình trên 10 ngày)"; giữ 83,9% kèm vế đối, thay vì câu định tính của C4. |
| F41 | 128 | ACCEPT | Elmi tr. 2, 5 | A | Thành vế "trong mô hình có thời gian đi trên mỗi đoạn đường không đổi"; Bảng 2.2 giữ "Ngoài phạm vi". |
| F42 | 131–132 | ACCEPT: ví dụ dựng tay đúng | FAM tr. 5, 7 | A | Ghi rõ "trong một ví dụ dựng tay" (RL 37). |
| F43 | 133–134 | ACCEPT có sửa: "lần sửa" không chỉ là thông báo khách thấy (C9) | X3-25; Ch3 r33 dòng 316–317 | M | Bỏ chữ "lần sửa"; viết "ở từng lượt so giờ trả của phương án với giờ trả khi xe giữ nguyên kế hoạch, rồi cộng độ lớn phần chênh". Không thêm vế "kể cả khi giờ công bố không đổi" (trang; Chương 3 có phản ví dụ). |
| F44 | 134–136 | OVERSTATED: chỉ tác dụng của chiều sớm | D5 | M | Bỏ câu khỏi Chương 2 (D5). |
| F45 | 143–145 | ACCEPT | dựa vào kiểm của CX | A | "Phần lớn chúng giữ cố định một giờ đã báo: …" liệt kê ba mốc. |
| F46 | 145–146 | ACCEPT | AM17 tr. 4 | A | Vế "chỉ chuyển sang xe khác nếu thời gian chờ không tăng" bị cắt (trang). |
| F47 | 146–147 | ACCEPT | LUK tr. 4 | A | Lu–Kühnel còn một vế trong văn xuôi; chi tiết 2–3 phút ở Bảng 2.2. |
| F48 | 147–149 | ACCEPT có sửa: thêm "trong thiết lập của bài" (C2) | SP tr. 549, 562, 569 (mục 6.3.5, Finding 5) | A | "với thời gian đi cho trước"; nêu đánh đổi giữa tỉ lệ từ chối và sức hấp dẫn với khách đã nhận (RL 44). |
| F49 | 149–150 | ACCEPT | MTK tr. 5, 27 | A | Mt-KaRRi còn một vế; con số ở Bảng 2.2. |
| F50 | 153–154 | ACCEPT | HZ in tr. 10 | A | "nhu cầu lịch sử của dịch vụ MOIA" (đúng chữ "historical requests"). |
| F51 | 154–155 | ACCEPT | HZ in tr. 7 | A | Không đổi về nghĩa. |
| F52 | 155–157 | ACCEPT có sửa: "yêu cầu đã gán cho xe", không "trên xe"; phạt có β | HZ in tr. 8 (7), (11) | A | "với các yêu cầu đã gán cho xe đang xét". Không thêm β (trang; ghi trong EV). |
| F53 | 157–159 | OVERSTATED: chỉ khi giờ cập nhật vượt hạn | D1 | A | "giờ trả chỉ được nới khi giờ trả cập nhật đã vượt giờ trả muộn nhất" và ví dụ hai chiều. |
| F54 | 158–159 | OVERSTATED: không quy toàn bộ cho (7) | D2 | A | Bỏ vế "nên thuật toán không rơi vào…"; chỉ gắn vấn đề cho bài; giữ công thức 8. |
| F55 | 159–160 | ACCEPT | HZ in tr. 12, 14 (D10) | A | Chuyển sang mục 2.4 kèm điều kiện. |
| F56 | 206–208 | ACCEPT có sửa (C3, C9) | CH3 r33 dn:luatc; X3-25 | A | Dòng 211–215; vế "phần dời do điều phối vẫn tính với thời gian đi hiện tại" ở ô luật C của Bảng 2.2. |
| F57 | 208–210 | ACCEPT | A12; Ch3 r33 eq:dongnhat | A | Lời giải thích "để các lần dời sớm, muộn bù trừ nhau" (B2). |
| F58 | 210 | ACCEPT có sửa: nói đối chứng hẹp (C10) | J11; D03:214-217; Ch3 r33 dòng 442–445 | A | "chỉ mượn thành phần hạn chót của Schulz và Pfeiffer với các mức trần như luật C thay cho 900 giây". |
| F59 | 210–211 | ACCEPT | D03 §1, §10 | A | Không đổi. |
| F60 | 218–220 | OVERSTATED: dùng "có thể" | A05; F10 | A | "có thể sớm hơn". |
| F61 | 219–220 | ACCEPT | HZ in tr. 10 | A | Chi tiết "mỗi 60 phút" chuyển vào EV (trang). |
| F62 | 223 | ACCEPT | DRE tr. 1 "ride-hailing platforms" | A | "Giờ đến dự kiến có vai trò quan trọng ở các nền tảng gọi xe" (RL 56). |
| F63 | 223–226 | ACCEPT | DRE tr. 1, 3 | A | Bỏ danh sách đặc trưng (RL H, trang). |
| F64 | 226–228 | OVERSTATED: phạm vi "hơn 90%" | LEO PDF tr. 2 ("above reasonable levels of flexibility"), tr. 4 | A | Bỏ "hơn 90%" (C11). |
| F65 | 228–229 | ACCEPT | DRE; LEO | A | Không đổi. |
| F66 | 232–233 | ACCEPT | F02; Ch3 r33 dòng 517–519, 547–552 | A | Viết là quy tắc của khóa luận ("Dự báo cho lời hứa trong khóa luận chỉ dựa vào…", RL D). |
| F67 | 233–235 | ACCEPT | C2-16 (D9) | A | Thêm "hiện". |
| F68 | 234–235 | OVERSTATED: viết thành giả định vận hành (C6) | C2-16; F03 | A | Dòng 250–253: giả định ghi rõ, kèm phạm vi phát lại. |
| F69 | 238 | ACCEPT | FLEET tr. 10 | A | Không đổi. |
| F70 | 239–240 | ACCEPT | FLEET tr. 10 | A | Lời gọn. |
| F71 | 240 | ACCEPT | C2-11 (tệp 96 dòng) | A | Không đổi. |
| F72 | 241–242 | ACCEPT | B06 | A | Không đổi. |
| F73 | 242–244 | ACCEPT (C11 là lựa chọn lời) | I02; F10 | A | Như B4. |
| F74 | 251 | OVERSTATED: thu hẹp chủ ngữ | WAR tr. 3 mục 14–15, tr. 10 | A | Bỏ câu khái quát; câu Wardman nêu đúng hai cách hỏi. |
| F75 | 252–253 | ACCEPT: "quan sát" là giá trị ước lượng | WAR tr. 10 bảng 5 | A | "(15 giá trị, 2 nghiên cứu)". |
| F76 | 254–255 | ACCEPT | AGZ tr. 1 | A | Thêm cách đo độ tin cậy (RL 65). |
| F77 | 255–256 | OVERSTATED: thêm "có hệ thống" | AGZ tr. 11 "unannounced yet systematic" | A | Đã thêm. |
| F78 | 256 | ACCEPT | AGZ tr. 13 | A | Không đổi. |
| F79 | 256–258 | ACCEPT có sửa: "tần suất cập nhật" | CRX cr13 (tóm tắt) | A | "Theo phần tóm tắt, …"; "tần suất cập nhật"; bỏ chú thích chân trang vì câu đã nói rõ. |
| F80 | 261–262 | ACCEPT | dựa vào kiểm của CX | A | Không đổi. |
| F81 | 262 | ACCEPT | — | A | Lời gọn. |
| F82 | 262–263 | CANNOT CHECK/REJECT: "chưa có chuẩn ngành" | D03:260 chỉ nói chưa có căn cứ WTP/ROI | A | Thay bằng "khóa luận chưa có căn cứ bên ngoài để coi mức trần này là chuẩn dịch vụ" (C12). |
| F83 | 263–264 | ACCEPT | K52 | A | Không đổi. |
| F84 | 153 | ACCEPT có sửa: giới hạn "gần luật C nhất" | — | A | "Trong các cách ở Bảng 2.2, gần luật C nhất là…" (dòng 157). |

### 3.2 Bảng 2.1 (T101–T116)

| ID | Dòng v4 | Nhận xét CX | Bằng chứng | QĐ | Thay đổi (v6) |
|---|---|---|---|---|---|
| T101 | 80–82 | ACCEPT 2/5/7 phút | AM17 tr. 5 | A | Không đổi. |
| T102 | 81 | ACCEPT 5 phút | FAM bảng 6 | A | Không đổi. |
| T103 | 81 | ACCEPT 5 phút | Elmi tr. 15 | A | Không đổi. |
| T104 | 81–82 | ACCEPT 480 s | FLEET tr. 11 | A | Viết "8 phút" cho cùng đơn vị (RL 19); 480 s ở EV. |
| T105 | 82 | ACCEPT 600 s | B03 | A | Viết "10 phút kể từ lúc gọi", khớp Bảng 3.2 của Chương 3. |
| T106 | 84–85 | OVERSTATED: "bằng" → "không quá" | AM17 tr. 3, 5 | A | "không quá hai lần cửa sổ đón" (C7). |
| T107 | 85 | ACCEPT | FAM bảng 6 | A | "độ trễ tổng tối đa 10 phút". |
| T108 | 85 | ACCEPT | Elmi tr. 15 | A | Như T107. |
| T109 | 86 | ACCEPT | MOL PDF tr. 5 | A | "một phần vượt tính bằng tỉ lệ của thời gian đi thẳng" (RL 18). |
| T110 | 86 | ACCEPT 40% | FLEET tr. 11 "maximum relative detour time of 40%" | A | "thời gian đi vòng thêm tối đa 40% thời gian đi thẳng". |
| T111 | 86–87 | ACCEPT 1,5 lần | B03; PPV:594 | A | Không đổi. |
| T112 | 89 | ACCEPT | AM17 tr. 5 | A | Không đổi. |
| T113 | 89–90 | ACCEPT | FLEET tr. 11 | A | Không đổi. |
| T114 | 90 | ACCEPT | SP tr. 562 | A | Không đổi. |
| T115 | 90 | ACCEPT "4 chỗ; 8 xe" | B03 | A | Sự kiện đúng; "8 xe mỗi kịch bản" bỏ khỏi ô sức chứa (RL 19; có ở Bảng 4.1). Cột 3 hẹp 5,9 → 5,7 cm để hết tràn 1,9 pt. |
| T116 | 71–73 | ACCEPT chú thích | D03 §12 | A | "một tuyến xe" thay "một phương án" (từ của RideBound, RL C). |

### 3.3 Bảng 2.2 (T201–T228)

| ID | Dòng v4 | Nhận xét CX | Bằng chứng | QĐ | Thay đổi (v6) |
|---|---|---|---|---|---|
| T201 | 176 | ACCEPT mốc cửa sổ đón | AM17 tr. 3 | A | Dòng cửa sổ đón và ngồi xe bỏ khỏi Bảng 2.2 (trùng Bảng 2.1; trang); một câu trong chú thích thay. |
| T202 | 176 | OVERSTATED "Có" → "không tách nguồn" | AM17 tr. 4 (thời gian cạnh trung bình ngày) | M | Câu chú thích: "Cửa sổ đón và giới hạn ngồi xe ở Bảng 2.1 không tách nguồn, nên phần do tắc đường bị tính", và chú thích nói cột 3 là cách đọc định nghĩa, không phải kết quả đo. |
| T203 | 176 | OVERSTATED cột ghi riêng | D4 | A | Dòng bị bỏ; cột 6 đổi (D4). |
| T204 | 178–179 | ACCEPT | AM17 tr. 3; MOL tr. 5 | A | Như T201. |
| T205 | 178 | OVERSTATED như T202 | — | M | Như T202. |
| T206 | 178–179 | OVERSTATED cột ghi riêng | D4 | A | Như T203. |
| T207 | 181–182 | ACCEPT | AM17 tr. 4; LUK tr. 4 | A | Thêm `fielbaum2020` vào dòng này: mức kiểm soát hoàn toàn hạ thời gian chờ tối đa về giá trị dự kiến (FAM tr. 17; RL C mục 8). |
| T208 | 182 | ACCEPT có sửa: "không tách nguồn; đệm cho bất định" | LUK tr. 4 | M | "Có, vì không tách nguồn; đệm chừa cho bất định". Giữ chữ "Có" để cột trả lời được câu hỏi; lý do đi kèm. |
| T209 | 182 | OVERSTATED cột ghi riêng | D4 | A | Cột 6: "Giờ đón đã báo". |
| T210 | 184–186 | ACCEPT | SP tr. 549–551, 562 | A | "Giờ trả trong lời mời cộng độ chùng 900 giây". |
| T211 | 184–185 | OVERSTATED/REJECT "khi thời gian đi đổi thì có" | SP tr. 549 (D3) | A | "Ngoài phạm vi: thời gian đi cho trước"; bỏ A10 khỏi EV (E02). |
| T212 | 185 | ACCEPT | SP tr. 550 | A | Cột 5 "Không". |
| T213 | 185–186 | OVERSTATED "Không; mỗi khách một hạn chót" | D4 | A | Cột 6: "Hạn chót". |
| T214 | 188–190 | ACCEPT cấu trúc | HZ in tr. 8 | A | "Áp cho ai": "Các yêu cầu đã gán cho xe đang xét". |
| T215 | 189 | OVERSTATED "riêng tắc đường không làm tuyến bị loại" | D1; HZ in tr. 8 (7), (11) | M | "Có, tới khi giờ cập nhật vượt hạn; phần vượt sau đó chỉ bị phạt": đọc hai chế độ của công thức 7 và 11, gọn hơn câu C1 và không nói gì về toàn tuyến. |
| T216 | 190 | ACCEPT | HZ in tr. 8 (11) | A | Cột 5 "Không". |
| T217 | 190 | OVERSTATED cột ghi riêng | D4 | A | Cột 6: "Giờ trả muộn nhất, giờ trả cập nhật". |
| T218 | 192–194 | ACCEPT | Elmi tr. 5, 12–13 | A | Ô gọn: "Khách điểm thấp: độ chùng 0; khách khác: toàn bộ". |
| T219 | 192–193 | ACCEPT | Elmi tr. 2, 5 | A | "Ngoài phạm vi: thời gian đi cố định". |
| T220 | 193–194 | ACCEPT | Elmi (2) | A | Cột 5 "Không". |
| T221 | 194 | OVERSTATED "chỉ chọn khách theo điểm" | D4 | A | Cột 6: "Điểm, độ chùng". |
| T222 | 196–197 | ACCEPT | MTK tr. 5, 27 | A | Không đổi. |
| T223 | 197 | ACCEPT | MTK tr. 4 | A | "thời gian đi cố định". |
| T224 | 197 | ACCEPT | MTK tr. 5 | A | Cột 5 "Không". |
| T225 | 197 | OVERSTATED cột ghi riêng | D4 | A | Cột 6: "Thời gian chuyến đã báo". |
| T226 | 199–200 | ACCEPT | X3-20, X3-25 | A | Không đổi về nghĩa. |
| T227 | 199–200 | OVERSTATED "Không" trần trụi | A01; A06 | A | "Không; phần dời do điều phối vẫn tính với thời gian đi hiện tại". |
| T228 | 165–167 | ACCEPT có sửa: đổi tiêu đề (C3) | D4 | M | Tiêu đề cột 5 như RL B3; cột 6 theo D4 thay cho tiêu đề "Lưu tổng độ lớn…" của C3 và ô "Bài không mô tả sổ này" (dài, và dữ liệu riêng của từng bài là điều người đọc cần thấy). Chú thích nêu "hạn chót cố định vẫn giới hạn phần dời ròng". |

### 3.4 Siêu dữ liệu (M01–M15)

| ID | Khóa | Nhận xét CX | Bằng chứng | QĐ | Thay đổi |
|---|---|---|---|---|---|
| M01 | alonsomora2017 | ACCEPT | CRX cr5; PDF tr. 1 | A | Không đổi. |
| M02 | alonsogonzalez2020 | WRONG ở `10-tai-lieu.tex` cũ (van Cranenburgh; thiếu Hoogendoorn-Lanser) | C2-18; AGZ PDF tr. 1 | A | Không ghi vào thư mục luận văn; mục sửa giữ trong BIB và NOTES mục 3, áp khi ghép. |
| M03 | elmi2026 | ACCEPT | CRX cr10 | A | Không đổi. |
| M04 | engelhardt2026 | ACCEPT | CRX cr6 | A | Không đổi. |
| M05 | fielbaum2020 | ACCEPT | CRX cr3 | A | Không đổi. |
| M06 | horl2022 | ACCEPT; không tự thêm tên hội nghị | DataCite; PDF tr. 1 | A | Không đổi. |
| M07 | hu2022 | ACCEPT | arXiv; DRE PDF | A | Không đổi. |
| M08 | laupichler2026 | ACCEPT | arXiv | A | Không đổi. |
| M09 | leonardi2024 | ACCEPT; có bản Transportmetrica A 2026, DOI 10.1080/23249935.2026.2650136 | Theo CX; tôi chưa mở bản tạp chí | A | Giữ bản arXiv đã đọc; ghi bản tạp chí là câu hỏi mở (NOTES). |
| M10 | lu2024 | ACCEPT; có bản Case Studies on Transport Policy 21 (2025) 101499 | Theo CX; tôi chưa mở | A | Như M09. |
| M11 | molenbruch2017 | ACCEPT | CRX cr7 | A | Không đổi. |
| M12 | schulz2026 | ACCEPT; có thể thêm số (2) | CRX cr4 | A | BIB đã có 48(2). |
| M13 | tlc | ACCEPT | C2-16 | A | Không đổi. |
| M14 | wardman2026 | ACCEPT | CRX cr1 | A | Không đổi. |
| M15 | yu2022 | ACCEPT; chỉ tóm tắt | CRX cr13 (tôi đọc lại tóm tắt) | A | Thân bài viết "Theo phần tóm tắt". |

### 3.5 Định vị, thuật ngữ, đường dẫn bằng chứng (P01–P08, E01–E05)

| ID | Nhận xét CX | Bằng chứng | QĐ | Thay đổi (v6) |
|---|---|---|---|---|
| P01 | Định vị với HZ: nêu điều kiện vượt hạn, đúng tuyến giữ nguyên (C1) | D1 | A | Dòng 157–171, 211–215. |
| P02 | Định vị với SP: đối chứng chỉ mượn hạn chót, trần nhỏ hơn (C2/C10) | J11; D03 §10 | A | Dòng 215–217. |
| P03 | Định vị với FAM: mức "hoàn toàn" không giữ mọi giờ trả (C8) | FAM tr. 17 | A | Dòng 123. |
| P04 | Định vị với Elmi: không coi "ghi riêng từng khách" là điều trước đây không có | D4 | A | Cột 6 Bảng 2.2; câu ranh giới "Bảo vệ từng khách … đã có". |
| P05 | Định vị với MTK | MTK tr. 5 | A | Không đổi. |
| P06 | Ranh giới mới (chèn, ETA, gán lại, tương đồng tuyến, cam kết tối thiểu, nhất quán thời gian, hài lòng); câu C10 gọn | D03 §1, J38, K47 | A | Giữ câu ranh giới cho các ý mà chương có trích (dòng 217–219). Không thêm "tương đồng tuyến, cam kết tối thiểu, nhất quán thời gian": chương không giải thích các thuật ngữ đó và hộp "không nhận là mới" của Chương 1 (OUTLINE §6.4) liệt kê đủ. |
| P07 | Nhất quán CH3 về v/e/p, sổ cộng cả khi p = v (C9) | X3-25 | M | Như F43: bỏ "lần sửa", không thêm vế "kể cả khi giờ công bố không đổi" (trang). |
| P08 | Lời hứa dự báo là phát lại, không vào quyết định chính (C6) | Ch3 r33 dòng 554–556; F03 | A | Dòng 251–253. |
| E01 | 31 dòng `% EV:` ở v4 | Đếm lại | A | v6 có 32 dòng bắt đầu bằng `% EV` (mỗi đoạn có sự kiện một dòng, mỗi nhóm hàng bảng một dòng); NOTES ghi đúng số này. |
| E02 | A10 không làm bằng chứng cho SP | A10 là đối chứng RideBound | A | Bỏ A10 khỏi EV dòng SP. |
| E03 | ADD5 ghi DRE 3 trang; PDF có 9 trang | `pdftotext` DRE: trang 9 có chữ, trang 10 rỗng | A | Không sửa ADD5 (đầu vào chỉ đọc); ghi chỉnh ở NOTES mục 3. |
| E04 | EV không biến suy luận thành sự thật | — | A | Các vế "có thể" và giả định TLC ghi rõ trong câu và trong EV. |
| E05 | NOTES v4 ghi 33 dòng EV, thực tế 31 | — | A | NOTES v5 ghi số của v6 (32) và cách đếm. |

---

## 4. Tổng hợp

| Người nhận xét | Số nhận xét | A | M | R | CC |
|---|---:|---:|---:|---:|---:|
| CX (R35) | 156 | 144 | 12 | 0 | 0 |
| RL (R30), B1–B5, N1–N5 | 10 | 1 | 9 | 0 | 0 |

M của CX: F29, F33, F34, F40, F43, F44, T202, T205, T208, T215, T228, P07. Bốn mục CX REJECT (F18, F82, T211, E02) đều
được nhận (A): cả bốn mệnh đề bị bác đã bỏ hay sửa.

**Phần đề xuất không nhận (R) bên trong các nhận xét M của RL**, kèm lý do:
1. N4: đổi $c_{ko}$ thành $c_{k0}$ — bài viết "cko", hai tập "Rok"/"Rko" (Alonso-Mora PDF tr. 3).
2. N4: "quy hoạch tuyến tính nguyên" — GLOSSARY-v2 mục H và Chương 3 dùng "quy hoạch nguyên".
3. N4/G: "khách đã xác nhận đặt xe không bị chuyển" — X3-39: không cấu hình nào chuyển yêu cầu đã nhận; câu v4 đúng và
   mạnh hơn.
4. N2: bỏ chữ "thường" — trang TLC viết "typically" (C2-16).
5. B3: ô Schulz–Pfeiffer "nếu thời gian đi đổi, phần do tắc đường sẽ bị tính (suy từ định nghĩa)" — bài không có thời
   gian đi đổi (SP tr. 549), câu đó là đoán.
6. B3: câu đọc bảng "cả hai … không để riêng tắc đường làm tuyến bị loại" — chỉ đúng với HZ sau khi giờ cập nhật vượt
   hạn (HZ in tr. 8; CX T215).
7. B5: văn bản thay thế — sai phạm vi (ADD1 mục 0.2; D5).
8. B1: "theo các tác giả, … bài toán luôn còn ít nhất một thứ tự trả khách" — bài không viết câu bảo đảm đó (HZ in tr.
   7–8; D2).

*Hết nhật ký. Viết bởi Claude (người sửa Chương 2), 2026-10-13. Chỉ tạo tệp này trong `reviews/`.*
