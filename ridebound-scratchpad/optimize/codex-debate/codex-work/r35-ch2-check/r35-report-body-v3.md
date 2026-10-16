# R35 — Kiểm nguồn Chương 2 v4 (Codex)

Ngày kiểm: 13/10/2026. Đối tượng duy nhất: `rewrite-2026-10/drafts/06-chuong2-v4.tex`; số dòng dưới đây thuộc tệp này. **Kết luận toàn chương: ACCEPT WITH CORRECTIONS.** Giữ cấu trúc và phạm vi đóng góp; sửa các cách diễn đạt được chỉ rõ trước khi ghép. Bảng 2.1 có đúng ba giá trị của RideBound: 600 giây, thời gian ngồi xe ≤ 1,5 lần thời gian đi thẳng, 4 chỗ.

<!-- COUNTS -->

## Cách đọc kết quả và phạm vi kiểm

- Mỗi hàng là một câu, một mệnh đề có thể kiểm riêng trong bảng/công thức, một khóa trích dẫn, hoặc một yêu cầu định vị. Hai cột kết luận tách nhau: **AGREE / WRONG / OVERSTATED / CANNOT CHECK** là đánh giá bằng chứng; **ACCEPT / ACCEPT WITH CORRECTIONS / REJECT** là quyết định cho mục đang kiểm. `REJECT` áp cho mệnh đề không nên giữ nguyên, không phải cho cả bài hay cả chương. Các mục thay thế ở phần cuối không được đếm thêm lần nữa.
- Đã đọc quy tắc phiên, WRITING-BRIEF, ADDENDUM-1 §0, sổ chính §J–K, ADDENDUM-5, ghi chú người viết, ranh giới đóng góp và Chương 3 v3. Hai tác vụ độc lập kiểm định nghĩa trong bảng và siêu dữ liệu; người phụ trách đã mở lại các đoạn nguồn quyết định trước khi kết luận. Siêu dữ liệu được nhận dạng từ nguồn sơ cấp trước khi tác vụ siêu dữ liệu so với BIB của người viết.
- Đọc trực tiếp PDF; các trích đoạn do phiên này tạo có số **trang vật lý PDF** trong `r35-source-*.txt` và `agent-*-extract.txt`. Khi ghi `tr. bài`, đó là số in trên trang. HZ: trang PDF = trang bài + 1; SP: trang PDF = trang bài − 540; ELMI: trang PDF = trang bài + 1. AM17 dùng bản Early Edition 6 trang. MOL dùng bản e-offprint có bìa; trang PDF 3 là trang mở đầu nội dung. Không chuyển số trang giữa các phiên bản.
- Bảng 5 của FAM được kiểm cả trên ảnh trang 17 có sẵn; cách trích chữ có thể xếp nhầm nhãn hàng. Các số đúng là Base 34,5% / 9,56; Intermediate 31,2% / 10,3; Fully controlled 45,6% / 11,6. Đây là số nguồn báo cáo, không phải số đếm khách do phiên này dựng lại.
- Chưa đọc toàn văn Yu; chỉ kiểm tóm tắt của nhà xuất bản qua DOI/Crossref. Không tuyên bố đã kiểm phương trình hay kết quả chi tiết của bài đó. Không chạy mô phỏng, xây dựng phần mềm hay cài công cụ. Không sửa bản nháp, mã nguồn, sổ bằng chứng hoặc thư mục luận văn.

### Nguồn viết tắt

| Mã | Bản nguồn đã mở / vị trí |
|---|---|
| AM17 | `E:/RideBoundData/literature-survey-2026-10-06/pdf/alonso-mora-pnas2017.pdf`, Early Edition; DOI [PNAS](https://doi.org/10.1073/pnas.1611675114). |
| FAM | `C:/PDF/Paper/Unreliability_in_ridesharing_systems_Measuring_cha.pdf`; DOI [TR-C](https://doi.org/10.1016/j.trc.2020.102831). |
| HZ | `E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/claude-work/pdf/hoerl-zwick-2022.pdf`; [ETH](https://doi.org/10.3929/ethz-b-000561639). Tệp `1-s2.0-S0191261522000716-main.pdf` là Sharif Azadeh và cộng sự, không dùng thay HZ. |
| SP | `C:/PDF/Paper/s00291-026-00847-0.pdf`; [OR Spectrum](https://doi.org/10.1007/s00291-026-00847-0). |
| ELMI | `C:/Users/quang/AppData/Local/Temp/claude/e--Code-RideBound/4f238113-dd3b-4bd1-b13f-53613b57f0e6/scratchpad/ch2/dl-elmi/elmi2026.pdf`, bản xuất bản có bìa kho; [TR-C](https://doi.org/10.1016/j.trc.2026.105897). |
| MTK | `C:/Users/quang/AppData/Local/Temp/claude/e--Code-RideBound/4f238113-dd3b-4bd1-b13f-53613b57f0e6/scratchpad/judge-dl-mtkarri/mtkarri.pdf`; [arXiv v1](https://arxiv.org/abs/2605.11798v1). |
| FLEET | `claude-work/pdf/fleetpy-etrr-2026.pdf`; [ETRR](https://doi.org/10.1186/s12544-026-00823-3). |
| MOL | `C:/PDF/Paper/OperationalEffectsofServiceLevelVariations-publication151005.pdf`; [CEJOR](https://doi.org/10.1007/s10100-015-0422-7). |
| LUK / LEO | `claude-work/pdf/lu-kuehnel-2024.pdf` / `leonardi-2024.pdf`; [DepositOnce](https://doi.org/10.14279/depositonce-21472) / [arXiv v1](https://arxiv.org/abs/2411.11899v1). `claude-work/` ở đường dẫn tuyệt đối như hàng HZ. |
| DRE | `.../scratchpad/ch2/dl-deepreta/2206.02127.pdf` với tiền tố Temp như ELMI; [arXiv v1](https://arxiv.org/abs/2206.02127v1). PDF này có 9 trang. |
| WAR / AGZ | `C:/PDF/Paper/1-s2.0-S0965856426000662-main.pdf` / `Value_of_time_and_reliability_for_urban_pooled_on-.pdf`; [Wardman](https://doi.org/10.1016/j.tra.2026.104925) / [Alonso-González](https://doi.org/10.1016/j.trc.2020.102621). |
| YU / TLC | [Tóm tắt Management Science](https://doi.org/10.1287/mnsc.2022.4448) / [trang chính thức TLC](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page), mở 13/10/2026. |
| REG / ADD1 / ADD2 / ADD5 | Sổ chính / phụ lục 1 / `EVIDENCE-REGISTER-ADDENDUM-2-CH3.md` / phụ lục 5 trong `S/rewrite-2026-10/evidence/`; `S` = `E:/Code/Report_INT3508/ridebound-scratchpad/`. |
| D03 / CH3 / SRC | `E:/Code/RideBound/docs/03-related-work-and-claim-boundary.md` / `S/rewrite-2026-10/drafts/07-chuong3-v3.tex` / `C:/Code/RideBound-noworse/src/`. |

## 1. Câu văn và công thức, kiểm từng mục

| ID | Dòng / mệnh đề đang kiểm | Bằng chứng và kết luận cụ thể | Kiểm nguồn | Quyết định |
|---|---|---|---|---|
| F01 | 24–25: yêu cầu có điểm đón, trả, thời điểm đặt; xe có sức chứa | SP tr. bài 549; AM17 tr. 3. Mô tả đúng lớp bài toán được dùng. | AGREE | ACCEPT |
| F02 | 25–26: bộ điều phối nhận/từ chối, gán xe, xếp điểm dừng | SP §3.1–3.2, tr. 549–551; CH3 phần phát biểu bài toán. | AGREE | ACCEPT |
| F03 | 26–28: định nghĩa DARP tối thiểu hóa chi phí tuyến có mức dịch vụ | MOL PDF tr. 3, tóm tắt. Đúng định nghĩa; năm in 2017, không đổi thành 2015 trong khóa trích. | AGREE | ACCEPT |
| F04 | 28: yêu cầu động chỉ biết khi khách gửi | SP tr. 549: chi tiết yêu cầu không biết trước. | AGREE | ACCEPT |
| F05 | 28–29: giải lại ở từng lượt với trạng thái hiện tại | SP §3.2, tr. 550–551, công thức (3); AM17 tr. 4. Không phải mọi thuật toán dùng cùng chu kỳ cố định. | AGREE | ACCEPT |
| F06 | 32: AM17 đề xuất gán theo lô cho đi chung sức chứa lớn | AM17 tr. 3–4, đồ thị và ILP. | AGREE | ACCEPT |
| F07 | 33: lô 30 giây trong thí nghiệm AM17 | AM17 tr. 5 nêu trực tiếp 30 giây; tr. 4 đưa ví dụ 30 giây. | AGREE | ACCEPT |
| F08 | 34–35: nối yêu cầu–yêu cầu, yêu cầu–xe rồi dựng RTV | AM17 tr. 3, phần RV/RTV. | AGREE | ACCEPT |
| F09 | 35–37: chuyến là nhóm yêu cầu; chỉ kiểm nếu mọi nhóm con bớt một yêu cầu khả thi cùng xe | AM17 tr. 3. Điều kiện cần cho phép dựng tăng dần; chương không nói đây là điều kiện đủ. | AGREE | ACCEPT |
| F10 | 37: HZ và FleetPy dùng thuật toán AM17 | HZ tr. bài 9 (PDF 10), phần cài trong MATSim; FLEET tr. 11 §4.1. | AGREE | ACCEPT |
| F11 | 40–48: ILP, biến nhị phân, hàm mục tiêu và hai ràng buộc | AM17 tr. 3 và Giải thuật 1 tr. 4. Công thức của chương là cách viết lại đúng trên tập cạnh hiện có; mỗi xe ≤ 1, mỗi yêu cầu được gán hoặc bỏ qua. | AGREE | ACCEPT |
| F12 | 49–50: c_ij là tổng độ trễ kể cả khách trên xe | AM17 tr. 3, công thức (1), chi phí cạnh lấy trên khách đang trên xe và nhóm yêu cầu mới. | AGREE | ACCEPT |
| F13 | 50–51: c_ko lớn, phạt yêu cầu không phục vụ | AM17 tr. 3; biến χ mô tả quyết định bỏ qua, không phải chứng minh không xe nào có thể chở. Câu hiện tại chỉ nói không được phục vụ nên đúng. | AGREE | ACCEPT |
| F14 | 51–52: độ trễ = giờ trả − giờ tới sớm nhất khi đi thẳng ngay lúc gọi; gồm chờ | AM17 tr. 3: t* = giờ gọi + thời gian đi thẳng; δ gồm chờ và độ vòng. | AGREE | ACCEPT |
| F15 | 52–53: mỗi xe nhiều nhất một chuyến; mỗi yêu cầu đúng một chuyến hoặc không phục vụ | AM17 tr. 4, Giải thuật 1 dòng 3–4. | AGREE | ACCEPT |
| F16 | 56–57: chi phí tính khách cũ, vì ghép thêm làm độ trễ tăng | Thành phần chi phí đúng, nhưng AM17 cho phép gán lại và đổi tuyến; không phải mọi lần ghép đều tăng độ trễ mọi khách cũ. Sửa C5. | OVERSTATED | ACCEPT WITH CORRECTIONS |
| F17 | 57–58: số hạng mềm, cộng qua khách, đo so đi thẳng, không so giờ đã báo | AM17 tr. 3 công thức (1). Ràng buộc giữ giờ đón ở tr. 4 vẫn tồn tại; không được suy rộng rằng cả phương pháp không bảo vệ lời hứa. | AGREE | ACCEPT |
| F18 | 58: có thể dời nhiều lần miễn mỗi lần tổng chi phí nhỏ hơn | ILP so các phương án của cùng lượt, không đòi chi phí giảm đơn điệu so lượt trước. Mệnh đề “miễn là” sai nếu hiểu là điều kiện thuật toán. Sửa C5. | WRONG | REJECT |
| F19 | 59: hàm mục tiêu không định giá sửa lời hứa; FAM đã đo và kiểm soát | AM17 công thức (1) không có lịch sử độ dời; FAM §3 và §6. Nhận xét chỉ về hàm mục tiêu này là đúng. | AGREE | ACCEPT |
| F20 | 62: RideBound giữ bước chọn dạng gán, không dựng RTV | ADD2 X3-03, X3-22; SRC `OrToolsCandidateSelectionSolver.cs` và CH3 công thức chọn phương án. | AGREE | ACCEPT |
| F21 | 63–64: giữ nguyên kế hoạch hoặc chèn đón–trả, giữ thứ tự điểm cũ | SRC `InsertionCandidateGenerator.cs`:196–246, 548–575; ADD2 X3-03. Không phải vét cạn không giới hạn. | AGREE | ACCEPT |
| F22 | 64–66: đúng một phương án/xe, thứ tự tiêu chí, không chuyển khách cũ sang xe khác | ADD2 X3-22, X3-39; SRC `SolverBackedFleetSelection.cs`:271–385; CH3. | AGREE | ACCEPT |
| F23 | 96–98: AM17 gồm chờ, RideBound chỉ giới hạn ngồi xe; chưa hiệu chỉnh theo sở thích khách | AM17 tr. 3/5; SRC `PhysicalPlanValidator.cs`:594; D03 §12. | AGREE | ACCEPT |
| F24 | 104–106: FAM phân nguồn khách/hãng xe và tập trung nguồn hãng xe | FAM tr. 4, định nghĩa 1–2 và đoạn giới hạn phạm vi. | AGREE | ACCEPT |
| F25 | 106–107: giá trị báo đầu nếu tuyến giữ nguyên từ lần gán đầu | FAM tr. 4–5, định nghĩa các thành phần báo đầu. | AGREE | ACCEPT |
| F26 | 107–108: đo hiệu thực tế − ban đầu, âm về 0; đếm lần dự kiến tăng | FAM tr. 5 và định nghĩa 9 tr. 7. Không nhầm hiệu cuối–đầu với tổng độ lớn qua các lượt. | AGREE | ACCEPT |
| F27 | 111–112: Manhattan 4.091 nút, 9.453 cạnh, 2.000 xe 4 chỗ, 19.610 yêu cầu, 13–15 giờ 15/01/2013 | FAM tr. 9 §5–5.1. Đây là kịch bản bất ổn trong một lần đi; nghiên cứu còn có phần lặp qua mười ngày, nhưng chương không tuyên bố đã mô tả mọi thí nghiệm. | AGREE | ACCEPT |
| F28 | 112: chọn thấp điểm để bỏ qua bất ổn giao thông | FAM tr. 9, tác giả nêu thời gian đi tương đối ổn định là lý do. | AGREE | ACCEPT |
| F29 | 112–114: hơn một phần ba gặp thay đổi khi không hạn chế chuyển xe | FAM tóm tắt tr. 1 xác nhận phạm vi và nội dung. Chưa có số đếm/tổng tương ứng trong câu hay nguồn trích; theo quy tắc chủ sở hữu, thay tỷ lệ bằng mô tả định tính C8. | AGREE | ACCEPT WITH CORRECTIONS |
| F30 | 113–114: phần tăng chờ tương đương chờ trung bình toàn hệ thống | FAM tr. 1 dùng quan hệ cùng cỡ, không khẳng định hai trung bình bằng nhau. Dùng “có độ lớn cùng cỡ” ở C8. | OVERSTATED | ACCEPT WITH CORRECTIONS |
| F31 | 117: FAM §6 kiểm soát bất ổn ngay trong quyết định | FAM tr. 17 §6, hai thay đổi quy tắc trước khi gán. Không chỉ đo sau chuyến. | AGREE | ACCEPT |
| F32 | 117–118: kiểm soát hoàn toàn cấm từ chối lại và hạ chờ tối đa về dự kiến | FAM tr. 17, mục 1. “Hoàn toàn” là tên kịch bản, không xóa bất ổn thời gian ngồi xe/giờ trả; thêm câu giới hạn C8 để tránh đọc rộng. | AGREE | ACCEPT WITH CORRECTIONS |
| F33 | 118–119: từ chối 34,5% → 45,6%; chi phí khách 9,56 → 11,6 | FAM Bảng 5 tr. 17, đã xem ảnh bảng. Số đúng; tỷ lệ thiếu số đếm/tổng theo quy tắc chủ sở hữu. Giữ chi phí, bỏ tỷ lệ trong C8. | AGREE | ACCEPT WITH CORRECTIONS |
| F34 | 119–120: trung gian chỉ cấm từ chối lại; từ chối 31,2%; chờ và vòng tăng khoảng 50% | FAM tr. 17, mục 2 và Bảng 5. Các giá trị đúng; dùng trực tiếp trung bình 1,01 → 1,51 phút và 0,65 → 1,01 phút, bỏ tỷ lệ khách thiếu số đếm (C8). | AGREE | ACCEPT WITH CORRECTIONS |
| F35 | 120–121: đánh đổi tin cậy–chất lượng, câu hỏi kiểm soát không tăng từ chối | FAM tr. 17–18. Câu hỏi mở còn nhắc độ trễ/chờ trung bình; câu hiện tại là phần đúng của câu hỏi, không phủ nhận phần còn lại. | AGREE | ACCEPT |
| F36 | 124: Elmi tiếp tục kiểm soát theo từng khách | ELMI tr. bài 1–2, §2.1 và §2.4; không nhận bảo vệ cá nhân là mới. | AGREE | ACCEPT |
| F37 | 124–125: độ chùng = chờ/trễ tối đa − giá trị dự kiến lúc gán | ELMI tr. bài 5, công thức (2), hai đại lượng riêng ω và φ. | AGREE | ACCEPT |
| F38 | 125–126: điểm thấp chùng 0, khách còn lại giữ toàn bộ chùng | ELMI tr. bài 12–13 §2.4, ngưỡng điểm: tỷ lệ chùng 0 hoặc 1. | AGREE | ACCEPT |
| F39 | 126: chùng 0 nghĩa được bảo đảm không bị đổi giờ | ELMI tr. bài 12–13 bảo đảm chuyến tin cậy trong mô hình thời gian cạnh cố định, đúng với giới hạn mà câu kế tiếp của chương đã nêu. C4 diễn đạt cụ thể hơn bằng thời gian chờ/độ trễ không tăng do ghép thêm. | AGREE | ACCEPT |
| F40 | 126–128: “cùng tỉ lệ từ chối 29%”, bảo đảm 83,9% | Tóm tắt làm tròn, nhưng Bảng 2 tr. bài 19 là 29,09% và 29,21%; tr. 18 là 83,85%. Các chỉ số trung bình qua mười ngày (§3.1.3), không phải tỷ lệ gộp theo khách. Không có số đếm đủ để viết đúng quy tắc chủ sở hữu. Sửa định tính C4. | OVERSTATED | ACCEPT WITH CORRECTIONS |
| F41 | 128: Elmi cố định thời gian từng cạnh, không xét nguồn giao thông | ELMI tr. bài 2 và 5 §2.1.1. | AGREE | ACCEPT |
| F42 | 131–132: ví dụ muộn 5 phút rồi trở lại giờ cũ cho hiệu cuối–đầu 0; đếm lần tăng không độ lớn | Suy luận dựng tay đúng từ FAM tr. 5/7, đã ghi là ví dụ. Không phải quỹ đạo đo được của RideBound. | AGREE | ACCEPT |
| F43 | 133–134: kế thừa kiểm soát trước quyết định, so từng lần với kế hoạch giữ nguyên rồi cộng độ lớn | FAM §6; CH3 `muc:bamoc`, `dn:luatc`, ADD2 X3-25. Sổ cộng cả khi p = v nếu c khác 0; “lần sửa” không chỉ là thông báo khách thấy. Sửa C9. | AGREE | ACCEPT WITH CORRECTIONS |
| F44 | 134–136: các lần sớm chỉ 1 ms nên “khác biệt này ... chưa thấy ở kết quả” | ADD1 §0.2 và output ADD1:104–112 xác nhận 1 ms. Kết luận phải giới hạn riêng tác dụng chiều sớm, không toàn bộ khác biệt cộng dồn hay tách mốc (C9). | OVERSTATED | ACCEPT WITH CORRECTIONS |
| F45 | 143–145: nghiên cứu trước ràng buộc lời hứa; nhiều cách giữ giờ báo | AM17 tr. 4, LUK công thức (3), SP tr. 549–551, MTK tr. 5. | AGREE | ACCEPT |
| F46 | 145–146: AM17 khóa giờ đón muộn nhất về dự kiến; đổi xe chỉ nếu chờ không tăng | AM17 tr. 4. Chỉ trước khi lên xe; đã lên xe không đổi xe. | AGREE | ACCEPT |
| F47 | 146–147: Lu–Kühnel giới hạn giờ đón so giờ hẹn ban đầu, gợi ý 2–3 phút | LUK tr. 4 công thức (3) lấy min với giới hạn từ lúc gọi; 2–3 phút là gợi ý vận hành, không kết quả hiệu chỉnh. | AGREE | ACCEPT |
| F48 | 147–149: SP hạn trả từ lời mời + chùng, 900 s; quét tới 30 phút, 10–15 phút hợp lý | SP tr. bài 549–551, 562, 569 §6.3.5. Đúng trong thiết lập của họ; nên thêm “trong thiết lập của bài” (C2). | AGREE | ACCEPT WITH CORRECTIONS |
| F49 | 149–150: Mt-KaRRi ≤ 1,4 lần thời gian chuyến được nhận + 10 phút | MTK tr. 5, bất khả thi khi vượt αT_t + β; α = 1,4, β = 10 phút ở tr. 27 §B.2. | AGREE | ACCEPT |
| F50 | 153–154: HZ xét thời gian đi đổi, MATSim và nhu cầu thật MOIA Hamburg | HZ tr. bài 9–10. Nhu cầu lịch sử thật trong mô phỏng, không phải thử bộ điều phối trên chuyến xe thật. | AGREE | ACCEPT |
| F51 | 154–155: đầu lượt duyệt lại tuyến gán với thời gian đi hiện tại | HZ tr. bài 7, dòng 31–35. Đây là tiền lệ cho mốc e. | AGREE | ACCEPT |
| F52 | 155–157: công thức 7 là max(cập nhật, hạn); ràng buộc cứng 9–10; phạt 11 | HZ tr. bài 8. Phải viết “yêu cầu đã gán cho xe”, tránh “trên xe” thành chỉ khách đang ngồi. Phạt (11) còn có hằng số β khi có vi phạm; mô tả phạt theo giây đúng nhưng có thể thêm rõ (C1). | AGREE | ACCEPT WITH CORRECTIONS |
| F53 | 157–159: nhận thêm miễn khách không muộn hơn “mức sớm nhất có thể” | Chỉ khi e vượt hạn gốc mới có p ≤ e. Nếu e < hạn thì p có thể nằm giữa e và hạn. e được tính trên tuyến cũ, không phải cực tiểu trên mọi tuyến. Sửa C1. | OVERSTATED | ACCEPT WITH CORRECTIONS |
| F54 | 158–159: không hết thứ tự trả khả thi; giờ đón tương tự công thức 8 | HZ tr. bài 7–8. Giờ đón cần công thức (8); giữ yêu cầu trong đồ thị còn cần bổ sung tuyến gán cũ ở tr. 8 dòng 24–27. Không quy toàn bộ bảo vệ cho riêng (7); C1/C3. | OVERSTATED | ACCEPT WITH CORRECTIONS |
| F55 | 159–160: ước lượng thấp buộc chọn từ chối muộn hoặc trả muộn; tác động nhỏ với thời gian thực tế | HZ kết luận tr. bài 14. Giữ phạm vi kịch bản của bài; “tác động nhỏ” không có con số suy thêm. | AGREE | ACCEPT |
| F56 | 206–208: C dùng lại mốc HZ; cùng trần mỗi khách, cộng độ lớn, không nới theo tắc đường, có sổ | CH3 `dn:luatc`, SRC `CommitmentBudgetEvaluator.cs`:41–105. Phần trần còn lại độc lập với x, nhưng c vẫn tính trên thời gian đi hiện tại. Sửa rõ C3/C9. | AGREE | ACCEPT WITH CORRECTIONS |
| F57 | 208–210: cộng có dấu x + c trở về hạn từ lời hứa đầu; cộng độ lớn z là luật V | CH3 công thức `eq:dongnhat` với v_j = p_(j−1), REG A12. Đây là suy luận theo định nghĩa, đúng. | AGREE | ACCEPT |
| F58 | 210: hai luật đó làm đối chứng | CH3 bảng các luật, `muc:doichung`. Đối chứng hình thức trên cùng hệ, không tái lập toàn bộ thuật toán các bài. Thêm câu C10. | AGREE | ACCEPT WITH CORRECTIONS |
| F59 | 210–211: bảo vệ cá nhân, ETA, chèn động, chuyển xe đã có, không nhận mới | D03 §1–2, §7, §10; AM17 tr. 4, SP, ELMI, MTK. Không có tuyên bố ưu tiên tuyệt đối trong v4. | AGREE | ACCEPT |
| F60 | 218–220: dùng thời gian đi hiện tại có thể hứa sớm khi đường đông lên dù giữ tuyến | REG A05/F10; HZ tr. bài 10/14. Dùng “có thể” để tránh mọi chuyến đều trễ (C11). | OVERSTATED | ACCEPT WITH CORRECTIONS |
| F61 | 219–220: HZ cập nhật tốc độ GPS mỗi 60 phút | HZ tr. bài 10 (PDF 11), TomTom; không phải thời gian giữa hai lượt gán. | AGREE | ACCEPT |
| F62 | 223: dự báo giờ đến từ dữ liệu là thực hành nền tảng gọi xe | DRE tr. 1. Nguồn sơ cấp đủ cho Uber; không suy rộng rằng mọi nền tảng dùng đúng mô hình này. | AGREE | ACCEPT |
| F63 | 223–226: Uber dùng ETA cho giá/đón/trả/ghép; DeeprETA hiệu chỉnh bộ tìm đường; đặc trưng thời gian/tốc độ; phân vị có thể cần | DRE tr. 1 và tr. 3 Bảng 1, công thức (3). Không khẳng định phân vị là cấu hình triển khai duy nhất. | AGREE | ACCEPT |
| F64 | 226–228: Leonardi học từ chuyến mô phỏng, khoảng dự báo đúng hơn 90%, đề xuất định cỡ | LEO PDF tr. 2/4 và §3 PDF 8–10. Đúng trong các cấu hình đủ linh hoạt, không bảo đảm mọi cấu hình/ngày mới. Tỷ lệ thiếu số đếm/tổng; dùng C11. | OVERSTATED | ACCEPT WITH CORRECTIONS |
| F65 | 228–229: hứa theo dự báo không phải ý mới | DRE tr. 1/3; LEO PDF tr. 4. Đủ cho ranh giới không nhận ý chung là mới; không nói hai bài đã dùng đúng phép kéo dãn của khóa luận. | AGREE | ACCEPT |
| F66 | 232–233: dự báo dùng cho lời hứa chỉ được dùng thông tin đã có | Là điều kiện thiết kế để không dùng tương lai, không kết quả thực nghiệm của paper; CH3 `muc:dubao`, REG F02. Cần phân biệt ngày dữ liệu và ngày công bố. | AGREE | ACCEPT |
| F67 | 233–235: TLC công bố tháng, thường trễ khoảng hai tháng | Trang chính thức TLC, mục liên kết tải dữ liệu, xác nhận trực tiếp. Giữ câu; không cần cắt. | AGREE | ACCEPT |
| F68 | 234–235: “vì vậy giả định hãng xe có sẵn dữ liệu chuyến của chính mình” | Độ trễ TLC không chứng minh quyền truy cập dữ liệu hãng, và đây là phát lại dữ liệu lịch sử. Giả định vận hành có thể dùng nhưng phải viết điều kiện, không coi là chứng cứ đã triển khai (C6). | OVERSTATED | ACCEPT WITH CORRECTIONS |
| F69 | 238: FleetPy Manhattan dùng tuần 11–18/11/2018 | FLEET tr. 10. Không nhầm với FAM ngày 2013. | AGREE | ACCEPT |
| F70 | 239–240: so thời lượng chuyến với đường nhanh nhất ở tốc độ tối đa, hệ số theo giờ | FLEET tr. 10. Nguồn nêu bình quân trong từng giờ; không mô tả thuật toán tính tệp 15 phút. | AGREE | ACCEPT |
| F71 | 240: gói có tệp hệ số theo 15 phút từng ngày | Đã mở `2018-11-14_tt_factors.csv`: 96 hàng dữ liệu, 0–85.500 giây bước 900; SRC ngoài chương qua PREF:51–93 đọc tệp cùng dạng. ADD5 C2-11. | AGREE | ACCEPT |
| F72 | 241–242: khóa luận dùng một hệ số thành phố, không tốc độ từng đoạn | REG B06/I02; PREF:67–93; mô hình quy về hệ số chung. | AGREE | ACCEPT |
| F73 | 242–244: không nhiễu ngẫu nhiên; “mức trần” cho dự báo theo giờ, không hiệu quả ngoài đời | REG I02; báo cáo dự báo §6; run_t38.py:8–9 có sigma = shockRate = 0; F10. Cách đọc giới hạn đúng theo sổ. C11 là lựa chọn diễn đạt rõ hơn, không phải bác số liệu hay yêu cầu chứng minh cận toán học mà bản nháp không nêu. | AGREE | ACCEPT |
| F74 | 251: khách coi tới muộn nặng hơn ngồi xe | WAR tr. 10 hỗ trợ trung bình của hai cấu trúc đo tới muộn cụ thể, không mọi khách/mọi nghĩa “tin cậy”. Thu hẹp chủ ngữ C12. | OVERSTATED | ACCEPT WITH CORRECTIONS |
| F75 | 252–253: Wardman 2,53 (15/2) và 3,12 (66/27), so IVT, hai cách hỏi | WAR tr. 2/3/10 Bảng 5: MeanLate-Distn và MeanLate-X/Y. Đúng; các “quan sát” là ước lượng hệ số, không 15/66 khách. | AGREE | ACCEPT |
| F76 | 254–255: AGZ khảo sát lựa chọn 1.006 người Hà Lan, tỷ số ≈ 0,5 | AGZ tr. 1. Tỷ số là VOR/VOT, không tỷ lệ khách và không giá mỗi phút trễ tới đích. | AGREE | ACCEPT |
| F77 | 255–256: khoản trễ nhỏ không báo trước được định giá thấp hơn thời gian đã báo | AGZ tr. 11 nói thêm “có hệ thống”; đây là displacement trong thiết kế lựa chọn. Thêm từ này để tránh mọi trễ bất ngờ (C12). | OVERSTATED | ACCEPT WITH CORRECTIONS |
| F78 | 256: người trả lời AGZ không ở tình huống tới muộn | AGZ tr. 13 §4: không nêu giờ đến mong muốn; phân biệt dao động thời gian và lateness. | AGREE | ACCEPT |
| F79 | 256–258: Yu thí nghiệm thực địa 1.425.745 chuyến, độ lớn và lần cập nhật ảnh hưởng bỏ yêu cầu | Tóm tắt nhà xuất bản xác nhận quy mô và hai tác động; chính xác hơn là “tần suất cập nhật”. Chưa kiểm toàn văn; giữ chú thích hạn chế và sửa C12. | AGREE | ACCEPT WITH CORRECTIONS |
| F80 | 261–262: ba nghiên cứu đo ba cấu trúc khác nhau | WAR tr. 3, AGZ tr. 13, YU tóm tắt. Đúng, không quy đổi trực tiếp sang ngân sách C. | AGREE | ACCEPT |
| F81 | 262: không kết quả nào cho giá tiền của trần C 30 giây | Ba nguồn đo đại lượng khác và không nghiên cứu C. Phát biểu giới hạn trong ba nguồn đúng. | AGREE | ACCEPT |
| F82 | 262–263: “chưa có chuẩn ngành cho loại trần này” | D03:260 chỉ cho phép nói khóa luận chưa có căn cứ WTP/ROI; không đủ chứng minh toàn ngành không có chuẩn. Thu hẹp C12. | CANNOT CHECK | REJECT |
| F83 | 263–264: mức trần là điểm đánh đổi, không ngưỡng cảm nhận; sang đặc tả CH3 | REG K36/K52, D03 §12, CH3. Không tự gán giá trị hành vi/người dùng cho 30 giây. | AGREE | ACCEPT |

| F84 | 153: “gần luật C nhất” | Đây là nhận xét so các dạng đã xét, không kết quả paper hay kết luận toàn văn liệu. Thêm phạm vi “trong các dạng ràng buộc đã xét” ở C1, phù hợp D03 và CH3. | AGREE | ACCEPT WITH CORRECTIONS |

## 2. Bảng 2.1 — từng nhóm số của từng nguồn

| ID | Ô / dữ kiện | Nguồn và cách hiểu | Kiểm nguồn | Quyết định |
|---|---|---|---|---|
| T101 | 80–82: AM17 chờ 2/5/7 phút | AM17 tr. 5: Ω = 120/300/420 s từ lúc gọi. | AGREE | ACCEPT |
| T102 | 81: FAM chờ 5 phút | FAM tr. 18 Bảng 6. | AGREE | ACCEPT |
| T103 | 81: ELMI chờ 5 phút | ELMI tr. bài 15 §3.1.1. | AGREE | ACCEPT |
| T104 | 81–82: FLEET chờ 480 s | FLEET tr. 11, ví dụ ứng dụng; không chuẩn mặc định mọi nghiên cứu. | AGREE | ACCEPT |
| T105 | 82: RideBound 600 s kể từ lúc gọi | REG B03; cấu hình gốc có `pickupWindowMs=600000`; SRC NORM:444 lấy giờ gửi + cửa sổ. | AGREE | ACCEPT |
| T106 | 84–85: AM17 trễ tổng tối đa bằng hai lần cửa sổ đón, gồm chờ | AM17 tr. 3/5: δ ≤ Δ, Δ = 2Ω. “Bằng” phải sửa thành “không quá” vì bảng mô tả giới hạn, không thời gian mọi khách (C7). | OVERSTATED | ACCEPT WITH CORRECTIONS |
| T107 | 85: FAM trễ tổng tối đa 10 phút | FAM tr. 18 Bảng 6; trễ = chờ + vòng ở tr. 5. | AGREE | ACCEPT |
| T108 | 85: ELMI trễ tổng tối đa 10 phút | ELMI tr. bài 15 §3.1.1, trễ gồm chờ và vòng ở §2.1.2. | AGREE | ACCEPT |
| T109 | 86: MOL phần vượt thời gian đi thẳng theo tỷ lệ | MOL PDF tr. 5: ngồi xe tối đa = đi thẳng + phần vượt theo tỷ lệ. Không gán riêng giá trị 1,5 cho bài này. | AGREE | ACCEPT |
| T110 | 86: FLEET độ vòng tương đối tối đa 40% | FLEET tr. 11. Không tự thay bằng trễ tổng gồm chờ 40%. | AGREE | ACCEPT |
| T111 | 86–87: RideBound thời gian ngồi xe ≤ 1,5 lần đi thẳng | REG B03; cấu hình `maximumRideTimePermille=1500`; NORM:430–445; PPV:594 lấy trả − đón, không gồm chờ. | AGREE | ACCEPT |
| T112 | 89: AM17 sức chứa 1/2/4/10 | AM17 tr. 5. | AGREE | ACCEPT |
| T113 | 89–90: FLEET 4 chỗ | FLEET tr. 11 §4.1: 180 xe, mỗi xe 4 chỗ. | AGREE | ACCEPT |
| T114 | 90: SP 6 chỗ | SP tr. bài 562, thiết lập thực nghiệm. | AGREE | ACCEPT |
| T115 | 90: RideBound 4 chỗ, 8 xe/kịch bản | REG B03; cấu hình gốc `vehicleCapacity=4`, `vehicleCount=8`. | AGREE | ACCEPT |
| T116 | 71–73: cấu hình thử không chuẩn ngành; mốc khác không so trực tiếp | D03 §12; AM17 δ gồm chờ, RideBound ngồi xe, MOL giới hạn tương đối. | AGREE | ACCEPT |

## 3. Bảng 2.2 — kiểm riêng hai cột dễ sai và các ô còn lại

`Không` ở cột cộng dồn hiện có chú thích đúng: không cộng **độ lớn từng lần sửa**. Một hạn chót cố định vẫn giới hạn phần dời ròng so mốc đầu sau nhiều lượt; không được diễn giải `Không` là mỗi lượt cấp lại độ chùng hay không bảo vệ qua cả chuyến. Cột ghi riêng phải được đổi tên theo C3 trước khi giữ các ô `Không`.

| ID | Hàng / ô đang kiểm | Nguồn, phương trình và kết luận | Kiểm nguồn | Quyết định |
|---|---|---|---|---|
| T201 | 176: cửa sổ đón — mốc gọi xe, tới lúc lên xe | AM17 tr. 3: ω = đón − gọi ≤ Ω. | AGREE | ACCEPT |
| T202 | 176: cửa sổ đón — giao thông “Có” | Phương trình không tách nguồn chờ; nhưng thí nghiệm AM17 dùng thời gian cạnh trung bình ngày (tr. 4), không đánh giá giao thông đổi trong chuyến. Viết “Không tách nguồn của thời gian chờ” (C3), ghi là đọc từ định nghĩa. | OVERSTATED | ACCEPT WITH CORRECTIONS |
| T203 | 176: cửa sổ đón — cộng “Không”; ghi riêng “Không” | Không có tổng độ lớn sửa, đúng. “Ghi riêng” quá rộng vì ràng buộc vốn theo yêu cầu; đổi tiêu đề, dùng “Bài không mô tả sổ này” (C3). | OVERSTATED | ACCEPT WITH CORRECTIONS |
| T204 | 178–179: ngồi xe/trễ — mốc đi thẳng, mọi khách | AM17 tr. 3; MOL PDF tr. 5. Hai loại đại lượng phải giữ phân biệt như Bảng 2.1. | AGREE | ACCEPT |
| T205 | 178: ngồi xe/trễ — giao thông “Có” | Định nghĩa không tách nguồn làm tăng thời gian; không phải thí nghiệm riêng về đổi tốc độ trong một chuyến. Sửa ô thành “Không tách nguồn của thời gian tăng thêm” (C3). | OVERSTATED | ACCEPT WITH CORRECTIONS |
| T206 | 178–179: ngồi xe/trễ — cộng và ghi riêng “Không” | Không cộng độ lớn sửa đúng; không lưu dữ liệu cá nhân là suy rộng sai. C3 sửa tiêu đề/ô ghi sổ. | OVERSTATED | ACCEPT WITH CORRECTIONS |
| T207 | 181–182: giữ giờ đón — mốc và nhóm khách trước khi lên xe | AM17 tr. 4; LUK tr. 4 (3). Mốc AM17 là kỳ vọng đã gán; LUK là min của hạn từ gọi và hạn hẹn + đệm. | AGREE | ACCEPT |
| T208 | 182: giữ giờ đón — giao thông/đệm | LUK nêu đệm để chừa bất định giao thông và vận hành. Đây là gợi ý, không bảo đảm traffic ≤ đệm. Sửa “Không tách nguồn gây muộn; LUK gợi ý đệm cho bất định” (C3). | AGREE | ACCEPT WITH CORRECTIONS |
| T209 | 182: giữ giờ đón — cộng và ghi riêng “Không” | Không cộng độ lớn đúng; cột ghi riêng cần đổi tên C3. | OVERSTATED | ACCEPT WITH CORRECTIONS |
| T210 | 184–186: SP — hạn từ lời mời + 900 s, áp cho khách đã nhận | SP tr. bài 549–551: l_i− = B_i− + l; l = 900 s ở 562. Hạn không được cấp lại theo B_i− mới sau mỗi lần chèn. | AGREE | ACCEPT |
| T211 | 184–185: SP — “khi thời gian đi đổi thì có” | SP chỉ cho t_jj′ giữa cặp điểm, tr. 549; không mô hình thời gian đổi. A10 là đối chứng RideBound, không bằng chứng thuộc paper. Cắt mệnh đề mở rộng, dùng C2. | OVERSTATED | REJECT |
| T212 | 185: SP — không cộng độ lớn, so giờ trả mới với lời mời | SP tr. 550 l_i− cố định. Đúng; nhiều lần chèn vẫn bị cùng hạn ròng, không mỗi lần được thêm 900 s. | AGREE | ACCEPT |
| T213 | 185–186: SP — “Không; mỗi khách một hạn chót” | Paper có đối tượng và hạn riêng cho từng yêu cầu. Với tiêu đề hiện tại, `Không` gây sai nghĩa. Đổi tiêu đề/ô theo C3. | OVERSTATED | ACCEPT WITH CORRECTIONS |
| T214 | 188–190: HZ — mốc, xe đang xét, tác dụng nới khi e vượt hạn | HZ tr. bài 8 (7): t_required = max(t_updated,t_latest) cho yêu cầu đã gán cho xe đang xét. Cấu trúc đúng; “trên xe” không thu hẹp thành onboard-only. | AGREE | ACCEPT |
| T215 | 189: HZ — riêng tắc đường không làm tuyến bị loại | (7) bảo vệ giờ trả tuyến cũ; (8) cho giờ đón; thêm tuyến đã gán vào đồ thị tr. 8 dòng 24–27. Chỉ có (7) không bảo đảm toàn tuyến đi qua mọi bước. Dùng ô chỉ nói ràng buộc giờ trả (C1/C3). | OVERSTATED | ACCEPT WITH CORRECTIONS |
| T216 | 190: HZ — không cộng độ lớn; phạt vượt hạn gốc | HZ tr. 8 (11) phạt vi phạm tuyến ở lượt xét, không tổng trị tuyệt đối p−e qua vòng đời khách. | AGREE | ACCEPT |
| T217 | 190: HZ — ghi riêng “Không” | Các t_k và khoản phạt theo yêu cầu có thật; chưa thấy sổ ngân sách cộng dồn C. Sửa C3, tránh phủ nhận mọi dữ liệu riêng từng khách. | OVERSTATED | ACCEPT WITH CORRECTIONS |
| T218 | 192–194: ELMI — mốc ban đầu, chọn điểm thấp, chùng khách khác | ELMI tr. bài 5 (2), 12–13 §2.4. Đúng với ngưỡng điểm trong mô hình. | AGREE | ACCEPT |
| T219 | 192–193: ELMI — giao thông ngoài phạm vi | ELMI tr. 2/5: thời gian cạnh cố định. | AGREE | ACCEPT |
| T220 | 193–194: ELMI — không cộng độ lớn, so giá trị lúc gán | ELMI (2), giới hạn chùng từ thời điểm gán. Đúng; không đồng nghĩa chùng được cấp lại mỗi lượt. | AGREE | ACCEPT |
| T221 | 194: ELMI — “Không; chỉ chọn khách theo điểm” | Paper ghi chùng/điểm theo từng khách. Sửa tiêu đề và ô sổ C3; tránh “chỉ” làm mất nội dung bảo vệ cá nhân. | OVERSTATED | ACCEPT WITH CORRECTIONS |
| T222 | 196–197: MTK — mốc 1,4 T_đã nhận + 10 phút; mọi khách nhận | MTK tr. 5 và 27 §B.2. | AGREE | ACCEPT |
| T223 | 197: MTK — thời gian cạnh cố định | MTK tr. 4 §3.1. Đúng với mô hình bộ điều phối, không suy rằng mọi thành phần mô phỏng vận tải là tất định. | AGREE | ACCEPT |
| T224 | 197: MTK — không cộng độ lớn; mốc không đổi | MTK tr. 5 nêu mốc chuyến được nhận ban đầu. Đúng; vẫn giới hạn kết quả sau nhiều lần chèn. | AGREE | ACCEPT |
| T225 | 197: MTK — ghi riêng “Không” | T_p/T_t theo khách đã nhận được dùng; không thấy sổ tổng độ lớn sửa. Đổi tên/ô C3. | OVERSTATED | ACCEPT WITH CORRECTIONS |
| T226 | 199–200: C — so kế hoạch giữ nguyên, mọi khách xác nhận, cộng độ lớn, sổ từng khách | CH3 `dn:luatc`, ADD2 X3-20/X3-25: chờ đón và trên xe, khởi tạo lúc xác nhận; đúng. | AGREE | ACCEPT |
| T227 | 199–200: C — giao thông “Không”, không nới trần | C không cộng x = e−v vào ngân sách; c = p−e vẫn phụ thuộc thời gian đi hiện tại. `Không` trần trụi có thể gây hiểu sai độc lập hoàn toàn với giao thông. Sửa C3. | OVERSTATED | ACCEPT WITH CORRECTIONS |
| T228 | 165–167: chú thích `Không` = không cộng độ lớn sửa | Đúng với các định nghĩa trên và nhất quán CH3 `eq:dongnhat`. Đổi tiêu đề thành câu hỏi về tổng độ lớn để dễ đọc (C3). | AGREE | ACCEPT WITH CORRECTIONS |

## 4. Siêu dữ liệu: cả 15 khóa, kiểm độc lập BIB

Các mục dưới đây nhận dạng đúng phiên bản được dùng cho số trang. BIB mới của người viết đúng về 15 danh tính; lỗi tác giả nằm trong mục AGZ của thư mục luận văn hiện tại. Các bản tạp chí muộn hơn của Lu/Leonardi không làm trích bản tiền ấn đã đọc trở thành sai.

| ID | Khóa | Siêu dữ liệu đã xác nhận và nguồn sơ cấp | Kiểm nguồn | Quyết định |
|---|---|---|---|---|
| M01 | `alonsomora2017` | Javier Alonso-Mora; Samitha Samaranayake; Alex Wallar; Emilio Frazzoli; Daniela Rus. *On-demand high-capacity ride-sharing via dynamic trip-vehicle assignment*. PNAS 114(3), 462–467 (2017). DOI [10.1073/pnas.1611675114](https://doi.org/10.1073/pnas.1611675114); trang đầu PDF/nhà xuất bản. BIB đúng. | AGREE | ACCEPT |
| M02 | `alonsogonzalez2020` | María J. Alonso-González; Niels van Oort; Oded Cats; Sascha Hoogendoorn-Lanser; Serge Hoogendoorn. *Value of time and reliability for urban pooled on-demand services*. TR-C 115, 102621 (2020). DOI [10.1016/j.trc.2020.102621](https://doi.org/10.1016/j.trc.2020.102621); PDF tr. 1. BIB mới đúng; `10-tai-lieu.tex` cũ có van Cranenburgh và thiếu Hoogendoorn-Lanser: phải thay khi ghép, C13. | WRONG | ACCEPT WITH CORRECTIONS |
| M03 | `elmi2026` | Amir Elmi; Emily Moylan; Javier Alonso-Mora; Andrés Fielbaum. *Improving ridepooling reliability using shareability shadows*. TR-C 192, 105897 (2026). DOI [10.1016/j.trc.2026.105897](https://doi.org/10.1016/j.trc.2026.105897); trang đầu PDF cuối từ kho TU Delft/Crossref. | AGREE | ACCEPT |
| M04 | `engelhardt2026` | Roman Engelhardt; Florian Dandl; Arslan Ali Syed; Chenhao Ding; Santiago Alvarez-Ossorio Martinez; Yunfei Zhang; Hoda Hamdy; Joel Brodersen; Zhipu Chen; Klaus Bogenberger. *FleetPy: an open source simulator for reproducible research on mobility-on-demand services*. European Transport Research Review 18(1), bài 52 (2026), công bố 15/07/2026. DOI [10.1186/s12544-026-00823-3](https://doi.org/10.1186/s12544-026-00823-3). | AGREE | ACCEPT |
| M05 | `fielbaum2020` | Andrés Fielbaum; Javier Alonso-Mora. *Unreliability in ridesharing systems: Measuring changes in users’ times due to new requests*. TR-C 121, 102831 (2020). DOI [10.1016/j.trc.2020.102831](https://doi.org/10.1016/j.trc.2020.102831); PDF tr. 1. | AGREE | ACCEPT |
| M06 | `horl2022` | Sebastian Hörl; Felix Zwick. *Traffic uncertainty in on-demand high-capacity ride-pooling*. Conference paper, ETH Zurich Research Collection (2022). DOI [10.3929/ethz-b-000561639](https://doi.org/10.3929/ethz-b-000561639). Bản thảo ghi ngày nộp 27/10/2021; đó không phải lý do đổi năm lưu trữ 2022. Không tự thêm tên hội nghị khi nguồn metadata chưa xác nhận. | AGREE | ACCEPT |
| M07 | `hu2022` | Xinyu Hu; Tanmay Binaykiya; Eric Frank; Olcay Cirit. *DeeprETA: An ETA Post-processing System at Scale*. arXiv:2206.02127v1, 05/06/2022. DOI [10.48550/arXiv.2206.02127](https://doi.org/10.48550/arXiv.2206.02127); PDF tr. 1 và arXiv. BIB đúng; không gán venue chưa kiểm. | AGREE | ACCEPT |
| M08 | `laupichler2026` | Moritz Laupichler; Robin Andre; Kim Kandler; Peter Sanders; Peter Vortisch. *Advancing Dynamic Ride-Pooling Simulation – A Highly Scalable Dispatcher*. arXiv:2605.11798v1, 12/05/2026. DOI [10.48550/arXiv.2605.11798](https://doi.org/10.48550/arXiv.2605.11798); arXiv/PDF. | AGREE | ACCEPT |
| M09 | `leonardi2024` | Pierfrancesco Leonardi; Vincenza Torrisi; Andrea Araldo; Matteo Ignaccolo. *Data-driven assessment for the predictability of On-Demand Responsive Transit*. arXiv:2411.11899v1, 14/11/2024; DOI [10.48550/arXiv.2411.11899](https://doi.org/10.48550/arXiv.2411.11899). BIB trích đúng bản 2024 đã đọc. Có bản Transportmetrica A 2026, DOI 10.1080/23249935.2026.2650136, tên có thay đổi; không trộn metadata bản đó với số trang bản 2024. | AGREE | ACCEPT |
| M10 | `lu2024` | Chengqi Lu; Nico Kühnel. *To Wait or to Cruise: The Trade-Off Between Waiting Time and Detours for Service Efficiency in Ride-pooling Systems*. Submitted preprint, TU Berlin DepositOnce, 01/10/2024; DOI [10.14279/depositonce-21472](https://doi.org/10.14279/depositonce-21472). BIB đúng bản đã đọc. Bản tạp chí là Case Studies on Transport Policy 21 (2025), 101499, DOI 10.1016/j.cstp.2025.101499; không buộc đổi trích dẫn hiện tại. | AGREE | ACCEPT |
| M11 | `molenbruch2017` | Yves Molenbruch; Kris Braekers; An Caris. *Operational effects of service level variations for the dial-a-ride problem*. CEJOR 25(1), 71–90 (2017); trực tuyến 05/10/2015. DOI [10.1007/s10100-015-0422-7](https://doi.org/10.1007/s10100-015-0422-7). Không nhầm bài typology/review cùng nhóm tác giả. | AGREE | ACCEPT |
| M12 | `schulz2026` | Arne Schulz; Christian Pfeiffer. *Efficient insertion and reoptimization algorithms for a customer-oriented dynamic dial-a-ride problem*. OR Spectrum 48(2), 541–586 (2026); trực tuyến 02/02/2026. DOI [10.1007/s00291-026-00847-0](https://doi.org/10.1007/s00291-026-00847-0). BIB đúng; có thể bổ sung số (2) cho mục cũ. | AGREE | ACCEPT |
| M13 | `tlc` | New York City Taxi & Limousine Commission. *TLC Trip Record Data*. [Trang chính thức](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page). Ngày truy cập người viết 12/10/2026 hợp với bản lưu C2-16; phiên kiểm mở lại 13/10/2026. Không cần giả DOI/năm xuất bản. | AGREE | ACCEPT |
| M14 | `wardman2026` | Mark Wardman; Paul Murphy; Manuel Ojeda-Cabral; Alex Mitrani; Kazuyuki Neki; Richard Martin Humphreys. *Value of time multipliers for walk time, wait time, service headway, displacement time, reliability and congested travel time: review and meta-analysis of worldwide evidence*. TR-A 207, 104925 (2026). DOI [10.1016/j.tra.2026.104925](https://doi.org/10.1016/j.tra.2026.104925). | AGREE | ACCEPT |
| M15 | `yu2022` | Qiuping Yu; Yiming Zhang; Yong-Pin Zhou. *Delay Information in Virtual Queues: A Large-Scale Field Experiment on a Major Ride-Sharing Platform*. Management Science 68(8), 5745–5757 (2022). DOI [10.1287/mnsc.2022.4448](https://doi.org/10.1287/mnsc.2022.4448). Metadata và tóm tắt kiểm được; không toàn văn. | AGREE | ACCEPT |

## 5. Định vị, thuật ngữ và đường dẫn bằng chứng

| ID | Mục kiểm | Kết luận và bằng chứng | Kiểm nguồn | Quyết định |
|---|---|---|---|---|
| P01 | Định vị với HZ | Đã nhận mốc cập nhật, ràng buộc cứng và phạt là tiền lệ; không lấy “cứng thay mềm” làm mới (K26). Cần điều kiện e vượt hạn và gọi đúng tuyến giữ nguyên (C1), không tuyên bố lịch sử cộng dồn đã có tác dụng rộng. | AGREE | ACCEPT WITH CORRECTIONS |
| P02 | Định vị với SP | Đã nêu 900 s; cần nói đối chứng chỉ mượn hạn chót trên cùng hệ, dùng trần nhỏ hơn, không tái lập thuật toán hay kiểm giao thông của paper (CH3 `muc:doichung`, D03 §10). C2/C10. | AGREE | ACCEPT WITH CORRECTIONS |
| P03 | Định vị với FAM | Công bằng vì đã nêu cả §3 đo và §6 kiểm soát. Cần nêu kịch bản “hoàn toàn” giữ giờ đón/cấm từ chối lại, không giữ mọi giờ trả (C8). | AGREE | ACCEPT WITH CORRECTIONS |
| P04 | Định vị với ELMI | Có đúng tiền lệ bảo đảm riêng từng khách; khác ở phân chùng chọn lọc và mô hình cố định, C một ngân sách cho mọi khách xác nhận. Không xem “ghi riêng từng khách” là điều trước đây không có (C3/C4). | AGREE | ACCEPT WITH CORRECTIONS |
| P05 | Định vị với MTK | Đã nhận hạn từ chuyến được nhận, không cấp lại. So khác đại lượng với tổng độ lớn dời; không nhận chèn động hay ETA riêng lẻ là mới. | AGREE | ACCEPT |
| P06 | Ranh giới mới: chèn, ETA, gán lại, tương đồng tuyến, cam kết tối thiểu, nhất quán thời gian, hài lòng | V4 không nhận mới các mục này; 210–211 còn chủ động từ chối bốn ý. Không bắt chương phải thêm bài chưa đọc chỉ để liệt kê đủ; thêm câu ranh giới gọn C10. D03 §1–2/§7, REG K47. | AGREE | ACCEPT |
| P07 | Nhất quán CH3 về v/e/p, khách xác nhận, sổ | C đúng là tổng \|p−e\|, không tổng \|p−v\|; e chứa mọi thay đổi khi giữ kế hoạch, không chỉ tắc đường; cộng cả khi p=v. C9 làm rõ điểm này, phù hợp CH3 `muc:bamoc`, X3-25. | AGREE | ACCEPT WITH CORRECTIONS |
| P08 | Nhất quán lời hứa dự báo với CH3 | CH3 nêu lời hứa D tính sau chạy từ bản ghi, không đi vào quyết định chính. Ch2 chưa nói ngược nhưng suy luận vận hành dễ bị đọc thành triển khai thời gian thực. Thêm câu C6. | AGREE | ACCEPT WITH CORRECTIONS |
| E01 | 31 dòng bắt đầu `% EV:` của v4 | Có đường dẫn bằng chứng cho các đoạn dữ kiện/bảng; 15 khóa trích khớp. Số thực đếm là 31 chú thích bằng chứng; 33 trong brief/NOTES không khớp tệp hiện tại. Mục cần sửa tập trung ở các nhóm EV dòng 60, 129, 151, 161, 177–201, 212, 221, 230, 236, 245, 259, 265, không phải mất EV. | AGREE | ACCEPT |
| E02 | EV dòng 187 lấy REG A10 để nói traffic của SP | A10 chỉ mô tả hạn chót của RideBound. Không dùng nó để gán kết quả cho SP. Sửa bình luận EV cùng ô C2. | WRONG | REJECT |
| E03 | ADD5 mô tả DRE là PDF 3 trang | PDF local có 9 trang; arXiv cũng hiển thị 9. C2-15 tr. 1/3 vẫn là vị trí hợp lệ. Sửa đúng một mô tả anchor, C13. | WRONG | ACCEPT WITH CORRECTIONS |
| E04 | Câu thiếu căn cứ “chuẩn ngành”, suy luận TLC, “mức trần” dự báo | EV không tự làm suy luận TLC thành thực nghiệm hay xác nhận phủ định chuẩn ngành toàn cầu. C6/C12 tách đúng phạm vi; C11 là làm rõ giới hạn dự báo đã có trong I02. | OVERSTATED | ACCEPT WITH CORRECTIONS |

| E05 | Brief/NOTES nói v4 có 33 dòng `% EV` | Kiểm trực tiếp cho 31 dòng bắt đầu `% EV:`; thêm một dòng header chứa chuỗi này, tổng 32 dòng chứa chuỗi. Đây là sai số đếm ghi chú, không phải hai đoạn bằng chứng mất tích. C14 sửa mô tả ghi chú. | WRONG | ACCEPT WITH CORRECTIONS |

## 6. Các sửa ưu tiên, với câu tiếng Việt thay trực tiếp

### C1 — Hạng 1: đoạn Hörl–Zwick và ô thời gian trả của Bảng 2.2

Thay câu 155–159 bằng:

> Theo công thức 7 của bài, giờ trả bắt buộc của các yêu cầu đã gán cho xe đang xét bằng giá trị lớn hơn giữa giờ trả trên tuyến cũ đã tính lại và giờ trả muộn nhất gốc. Tuyến mới phải thỏa ràng buộc cứng trên giờ này (ràng buộc 10); phần vượt giờ gốc chịu phạt theo thời gian, kèm một khoản phạt khi có vi phạm (công thức 11). Khi giờ trả cập nhật đã vượt hạn gốc, ghép thêm khách không được làm khách cũ tới muộn hơn giờ trả trên tuyến cũ đã tính lại. Khi giờ cập nhật chưa vượt hạn, phần thời gian còn lại tới hạn vẫn có thể dùng cho ghép thêm. Giờ đón của khách đang chờ được nới tương tự theo công thức 8 và ràng buộc 9; bài còn thêm tuyến đang gán vào danh sách phương án để yêu cầu không bị mất khỏi đồ thị.

Ô giao thông của hàng HZ thay bằng:

> Hạn trả được nới tới giờ trả cập nhật của tuyến cũ; riêng phần tăng này không làm tuyến cũ vi phạm ràng buộc giờ trả.

Câu mở đoạn có thể thu hẹp thành: “Trong các dạng ràng buộc đã xét, cách Hörl và Zwick xử lý thời gian đi thay đổi là tiền lệ gần với mốc giữ nguyên kế hoạch của luật C.”

Giữ EV C2-04; bổ sung `HZ tr. bài 8, dòng 24–27` cho câu về đồ thị. Không gọi giờ e là giờ tối ưu trên mọi tuyến.

### C2 — Hạng 2: Schulz–Pfeiffer, không gán mô hình giao thông đổi cho bài

Ô giao thông 184–185 thay bằng:

> Ngoài phạm vi: thời gian đi giữa các điểm được cho trước.

Câu văn 147–149 thay bằng:

> Schulz và Pfeiffer đặt hạn chót trả bằng giờ trả trong lời mời cộng một độ chùng, mặc định 900 giây. Trong thiết lập của bài với thời gian đi giữa các điểm được cho trước, họ thấy khoảng 10–15 phút là một đánh đổi hợp lý khi quét độ chùng tới 30 phút.

EV hàng này chỉ giữ C2-07/J10 về paper; bỏ A10 khỏi chứng cứ cho ô giao thông. A10 dùng khi bàn riêng đối chứng RideBound ở CH3.

### C3 — Hạng 3: sửa ý nghĩa hai cột Bảng 2.2 và ô C

Đổi ba tiêu đề cho chính xác:

> Phần thay đổi khi giữ nguyên kế hoạch được xử lý thế nào?
>
> Cộng độ lớn từng lần dời qua cả chuyến?
>
> Lưu tổng độ lớn các lần dời cho từng khách?

Thay chú thích bảng bằng:

> Các dạng ràng buộc lời hứa ở nghiên cứu trước và luật C. “Không” ở cột cộng độ lớn nghĩa là bài dùng giới hạn trên thời gian chờ, thời gian chuyến hoặc giờ trả so với một mốc; không cộng độ lớn của từng lần sửa. Một hạn chót cố định vẫn giới hạn phần dời ròng sau nhiều lượt. “Bài không mô tả sổ này” chỉ nói về sổ tổng độ lớn sửa theo từng khách, không phủ nhận việc bài có hạn chót hay độ chùng riêng cho từng khách. Các ô về nguồn thay đổi là cách đọc từ định nghĩa ràng buộc; chúng không phải kết quả đo riêng về giao thông.

Ở cột nguồn thay đổi, thay lần lượt:

| Hàng | Văn bản mới |
|---|---|
| Cửa sổ đón | Không tách nguồn của thời gian chờ. |
| Ngồi xe/trễ tổng | Không tách nguồn của thời gian tăng thêm. |
| Giữ giờ đón | Không tách nguồn gây muộn; Lu và Kühnel gợi ý đệm cho bất định giao thông và vận hành. |
| SP | Ngoài phạm vi: thời gian đi giữa các điểm được cho trước. |
| HZ | Hạn trả được nới tới giờ trả cập nhật của tuyến cũ; riêng phần tăng này không làm tuyến cũ vi phạm ràng buộc giờ trả. |
| ELMI / MTK | Ngoài phạm vi: thời gian đi trên mỗi cạnh cố định. |
| C | Không cộng phần thay đổi khi giữ nguyên kế hoạch; phần dời do điều phối vẫn tính với thời gian đi hiện tại. |

Tất cả hàng nghiên cứu trước ở cột cuối: **“Bài không mô tả sổ này.”** Hàng C: **“Có: sổ tổng độ lớn phần dời do điều phối.”** Cột cộng độ lớn giữ `Không` ở các bài trước, `Có` ở C. Nếu vẫn giữ tiêu đề cũ “Ghi riêng cho từng khách?”, không được giữ hàng loạt ô `Không`.

### C4 — Hạng 4: Elmi, không biến số làm tròn và trung bình qua ngày thành tỷ lệ chính xác chung

Thay câu 125–128 bằng:

> Khách có điểm khả năng đi chung thấp nhận độ chùng bằng 0; các khách còn lại giữ toàn bộ độ chùng. Trong mô hình thời gian đi cố định, cách này ngăn thời gian chờ và độ trễ của nhóm được bảo vệ tăng thêm do ghép khách mới. Ở mức từ chối xấp xỉ nhau với cách siết đều cho mọi khách, cơ chế theo điểm bảo đảm ngay lúc gán rằng phần lớn khách không bị tăng thời gian chuyến.

Không lấy “cùng 29%” làm sự bằng nhau chính xác: Bảng 2 tr. 19 là 29,09% / 29,21%. Tóm tắt 83,9% làm tròn giá trị 83,85% ở tr. 18; §3.1.3 nói trung bình qua mười ngày. Chưa có số đếm/tổng cho từng ngày để viết đúng yêu cầu tỷ lệ của chủ sở hữu, nên câu thay dùng định tính. Đây không phải bác số tóm tắt.

### C6 — Hạng 5: TLC, giữ sự thật công bố trễ và viết giả định vận hành rõ ràng

Giữ câu công bố theo tháng, thường trễ hai tháng, với nguồn [TLC chính thức](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page). Thay câu 234–235 và bổ sung một câu phạm vi bằng:

> Nếu dùng hồ sơ từ vài ngày ngay trước để lập lời hứa trong lúc vận hành, hãng xe cần có dữ liệu kịp thời; khóa luận giả định hãng xe có dữ liệu chuyến của chính mình. Các kết quả chính ở đây là phát lại lời hứa trên bản ghi mô phỏng đã lưu, chưa kiểm khả năng thu thập và xử lý dữ liệu như vậy trong vận hành thực tế.

EV thêm `CH3 mục muc:dubao; F03; X3-11` cho câu phát lại. Ghi câu đầu là giả định về sử dụng thực tế, không suy ra duy nhất dữ liệu hãng từ độ trễ TLC. Không cần cắt câu TLC đã kiểm được.

### C5 — Hạng 6: bỏ điều kiện giảm chi phí đơn điệu trong giải thích AM17

Thay đoạn 56–59 bằng:

> Hàm mục tiêu này có tính độ trễ của khách đang trên xe, nhưng cộng chung độ trễ trên mọi khách và đo so với chuyến đi thẳng, không so với giờ đã báo. Ở mỗi lượt, bài toán chọn trong các phương án khả thi theo trạng thái hiện tại; nó không đặt một trần riêng lên tổng độ lớn các lần dời giờ trả của từng khách. Phần giữ giờ đón đã báo được xử lý bằng ràng buộc của thuật toán, còn Fielbaum và Alonso-Mora đã nghiên cứu thêm cách đo và kiểm soát độ bất ổn.

Không viết “miễn mỗi lần tổng chi phí nhỏ hơn” nếu chưa nói nhỏ hơn phương án nào; không chứng minh được giảm so lượt trước.

### C7 — Hạng 7: Bảng 2.1, giữ ba số đúng và dùng đúng dấu giới hạn

Ô AM17 ở dòng 84–85 thay bằng:

> Độ trễ tổng, gồm thời gian chờ, không quá hai lần cửa sổ đón.

Các ô RideBound giữ nguyên: **“600 giây kể từ lúc gọi”; “Thời gian ngồi trên xe không quá 1,5 lần thời gian đi thẳng”; “4 chỗ; 8 xe mỗi kịch bản”.** Không đổi thành trễ tổng 1,5 lần hay tính thêm chờ vào giới hạn ngồi xe.

### C8 — Hạng 8: FAM, giữ §6 và phạm vi kiểm soát, tuân thủ quy tắc tỷ lệ

Thay câu 112–114 bằng:

> Khi không hạn chế việc chuyển khách sang xe khác, nhiều yêu cầu không bị từ chối ngay vẫn gặp ít nhất một thay đổi. Trong các thí nghiệm của bài, khi thời gian chờ tăng, phần tăng có độ lớn cùng cỡ với thời gian chờ trung bình của hệ thống.

Thay đoạn 117–121 bằng:

> Ở mục 6 của bài, họ kiểm soát độ bất ổn ngay trong quyết định. Kịch bản được bài gọi là kiểm soát hoàn toàn cấm từ chối lại khách đã nhận và hạ thời gian chờ tối đa về giá trị dự kiến; kịch bản này không bảo đảm thời gian ngồi xe hay giờ trả không tăng. So với cơ sở, tỉ lệ từ chối tăng và chi phí trung bình của khách theo mô hình tăng từ 9,56 lên 11,6. Kịch bản trung gian chỉ cấm từ chối lại: tỉ lệ từ chối giảm, nhưng thời gian chờ trung bình tăng từ 1,01 lên 1,51 phút, và độ vòng trung bình tăng từ 0,65 lên 1,01 phút. Bài nêu đánh đổi giữa độ tin cậy và các chỉ số chất lượng khác, đồng thời để ngỏ cách kiểm soát bất ổn mà không tăng từ chối, độ trễ hay thời gian chờ trung bình.

Các tỷ lệ nguồn hiện đúng, nhưng chưa có số đếm cho cả ba hàng Bảng 5 trong bộ bằng chứng đã mở; không dựng số khách bằng nhân tỷ lệ đã làm tròn với 19.610. Nếu chủ sở hữu cho phép trích tỷ lệ văn liệu không số đếm, vẫn phải ghi rõ mẫu và nguồn; phiên này dùng cách thay an toàn theo quy tắc hiện hành.

### C9 — Hạng 9: thuật ngữ C, không nhầm sửa trong sổ với thay giờ khách thấy

Thay câu 133–136 bằng:

> Khóa luận kế thừa ý kiểm soát thay đổi do quyết định của hãng xe trước khi quyết định. Ở mỗi lượt được ghi vào sổ, hệ thống so giờ trả của phương án được chọn với giờ trả khi giữ nguyên kế hoạch, rồi cộng độ lớn phần dời này qua cả chuyến; phần đã dùng vẫn tăng nếu hai giờ đó khác nhau, kể cả khi giờ công bố cho khách không đổi. Trên tập kiểm tra chính, mọi lần điều phối dời giờ trả sớm hơn chỉ sớm 1 mili giây, nên chưa thấy tác dụng đáng kể riêng của việc tính cả chiều dời sớm.

Thay câu 206–208 bằng:

> Luật C dùng lại mốc giờ trả cập nhật trên tuyến cũ của Hörl và Zwick, nhưng giới hạn tổng độ lớn phần dời do điều phối qua cả chuyến, với cùng một trần ban đầu cho mọi khách đã xác nhận và sổ riêng cho từng khách. Phần thay đổi khi giữ nguyên kế hoạch không được cộng vào ngân sách; phần dời do điều phối vẫn được tính theo thời gian đi hiện tại, còn trần không được nới khi tắc đường tăng.

EV `A01; A06; X3-25; J01; J03; ADD1:104–112`. Mốc e chứa tiến độ/sự kiện mới và thời gian đi mới; phép tách theo mô hình không nhận diện tác động nhân quả ngoài đời.

### C10 — Hạng 10: đối chứng hẹp và không nhận các thành phần đã có là mới

Sau câu đối chứng 210, thêm:

> Luật hạn chót chỉ mượn thành phần hạn chót tính từ lời hứa đầu và dùng cùng mức trần với luật C trên cùng hệ RideBound; phép so này không tái lập toàn bộ thuật toán của Schulz và Pfeiffer.

Thay câu 210–211 về ranh giới bằng:

> Bảo vệ từng khách, giới hạn giờ đến, chèn động, chuyển khách sang xe khác, tương đồng tuyến, cam kết tối thiểu và tính nhất quán thời gian đều đã có tiền lệ; khóa luận không nhận các ý đó là mới, cũng không suy ra sự hài lòng của khách từ kết quả mô phỏng.

EV `J11; J38; K38; K47; D03 §1–2, §10–12; CH3 muc:doichung`. Không cần đưa paper chưa mở vào câu mới; đây là giới hạn phạm vi của dự án.

### C11 — Hạng 11: dự báo, phạm vi của Leonardi và “mức trần”

Ở 218–219 thay bằng:

> Khi đường đông dần, giờ tính theo thời gian đi lúc ra quyết định có thể sớm hơn giờ xe thực sự tới, dù xe giữ nguyên kế hoạch.

Thay câu Leonardi 226–228 bằng:

> Leonardi và cộng sự học từ các chuyến quan sát trong mô phỏng để dựng khoảng dự báo thời gian ngồi xe, và đề xuất dùng khả năng dự báo làm tiêu chí định cỡ dịch vụ đáp ứng theo nhu cầu. Kết quả được báo cáo cho các cấu hình mô phỏng của bài, không phải bảo đảm độ phủ cho mọi cấu hình hay ngày mới.

Thay câu 242–244 bằng:

> Vì mô phỏng dùng một hệ số chung cho cả thành phố và gần như tất định, đây là môi trường thuận lợi cho loại dự báo theo giờ trong ngày. Kết quả ở Chương thực nghiệm chưa xác nhận hiệu quả ngoài đời hay một cận trên toán học cho mọi phương pháp dự báo.

Khi ghép LaTeX, viết `Chương~\ref{chuong:thucnghiem}` ở vị trí “Chương thực nghiệm”. Không giữ từ “mức trần” nếu người đọc có thể hiểu là định lý cận trên; có thể để cách diễn giải này trong ghi chú giới hạn.

### C12 — Hạng 12: giá trị độ tin cậy, không chuyển sang ngưỡng C hay phủ định chuẩn ngành toàn cầu

Câu mở 251 thay bằng:

> Trong hai cách đo thời gian tới đích muộn mà Wardman và cộng sự tổng hợp, giá trị mỗi phút muộn trung bình cao hơn giá trị mỗi phút ngồi xe.

AGZ thêm đúng phạm vi:

> Một khoản thời gian tăng thêm nhỏ, không báo trước nhưng có hệ thống, được định giá thấp hơn thời gian đã báo trong khảo sát này; người trả lời không được đặt vào tình huống tới muộn.

YU dùng đúng đại lượng:

> Trong một thí nghiệm thực địa trên 1.425.745 chuyến, Yu và cộng sự thấy độ lớn của thông tin thời gian chờ ban đầu và tần suất cập nhật đều ảnh hưởng tới việc khách bỏ yêu cầu.

Giữ chú thích chỉ đọc tóm tắt. Thay câu 262–264 bằng:

> Ba nghiên cứu này không cung cấp giá tiền hay ngưỡng cảm nhận cho trần 30 giây trên phần dời giờ trả do điều phối. Khóa luận chưa có căn cứ bên ngoài để coi mức trần này là chuẩn dịch vụ, nên trình bày mỗi mức trần như một điểm trên đường đánh đổi.

### C13 — Hạng 13: siêu dữ liệu khi ghép và anchor DRE

Danh sách tác giả đúng cho mục `alonsogonzalez2020`:

> M. J. Alonso-González, N. van Oort, O. Cats, S. Hoogendoorn-Lanser và S. Hoogendoorn.

Giữ title, TR-C 115:102621 (2020), DOI 10.1016/j.trc.2020.102621. Không giữ van Cranenburgh trong mục này. Đây là sửa cho bibliography của thư mục luận văn khi ghép; BIB người viết đã nêu đúng.

Trong ADD5, mô tả DRE thay bằng:

> arXiv 2206.02127v1, 9 trang.

Giữ năm/bản 2024 cho LUK và LEO nếu tiếp tục trích đúng PDF đã kiểm; chỉ chuyển sang bản tạp chí sau khi mở lại chính bản đó và cập nhật anchor. HZ giữ tên kho và loại Conference Paper đã xác nhận, không tự điền tên hội nghị.

### C14 — Hạng 14: sửa số đếm chú thích trong ghi chú ghép

Thay mô tả “cùng 33 dòng `% EV`” bằng:

> Bản v4 giữ cùng tập khóa trích dẫn với v3; trong tệp v4 hiện tại có 31 dòng chú thích bằng chứng bắt đầu bằng `% EV:`.

Không tự thêm hai dòng trống để làm đủ một con số trong ghi chú.

## 7. Giới hạn còn lại và điều kiện ghép

Khi ghép, cần thêm đủ 9 khóa mới đã được BIB đề nghị: `engelhardt2026`, `horl2022`, `hu2022`, `laupichler2026`, `leonardi2024`, `lu2024`, `molenbruch2017`, `wardman2026`, `yu2022`. Đây là việc tích hợp, không phải 9 lỗi siêu dữ liệu.

Toàn văn Yu chưa được kiểm; câu hiện tại đủ ở mức tóm tắt và phải giữ chú thích. Số đếm đứng sau các tỷ lệ FAM/ELMI/LEO chưa được phục hồi; không được bịa số nguyên từ tỷ lệ làm tròn. Câu thay định tính đáp ứng quy tắc chủ sở hữu mà không phủ nhận kết quả các bài.

Sau các sửa C1–C14, chương định vị luật C công bằng và hẹp: tiếp nối mốc cập nhật của HZ; nhận cả đo lẫn kiểm soát trước quyết định của FAM; phân biệt hạn từ lời mời SP, chùng chọn lọc ELMI và giới hạn chuyến đã nhận MTK với tổng độ lớn phần dời do điều phối của C. Không có căn cứ trong chương này để nhận quyền ưu tiên toàn văn liệu, giá trị thương mại, sự hài lòng khách hay hiệu quả vận hành thực tế. Bản nháp và toàn bộ nguồn ngoài `codex-work/r35-ch2-check/` được giữ nguyên.
