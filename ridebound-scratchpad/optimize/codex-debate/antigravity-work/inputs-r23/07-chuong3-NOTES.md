# 07-chuong3 — NOTES của người viết (2026-10-11)

Tệp chương: `drafts/07-chuong3.tex` (662 dòng; `\input` được trong `main.tex`). Không ghi gì vào thư
mục luận văn hay nơi khác; không chạy mô phỏng, không build LaTeX, không cài, không xóa. Kiểm cú pháp chỉ bằng một script
đọc (cân ngoặc `{}`, cặp `\begin/\end`, số `$` chẵn theo đoạn): 0 lỗi. **Chưa biên dịch thử** (build bị cấm trong nhiệm
vụ); người ghép cần chạy `tectonic` một lần.

Đầu vào đã đọc: WRITING-BRIEF, OUTLINE-V2 (toàn bộ), REVIEW-DECISIONS-R20 (toàn bộ), STYLE-GUIDE-VI, GLOSSARY-VI,
EVIDENCE-REGISTER (toàn bộ), EVIDENCE-REGISTER-ADDENDUM-1 (toàn bộ, mục 0 đọc trước), chương 3 hiện tại
(`TEX/07-chuong3.tex`, chỉ đọc), `main.tex`, `10-tai-lieu.tex`, phần chương 3 của DACN (pdftotext), và mã nguồn chỉ đọc ở
`C:/Code/RideBound-noworse/` (xem mục 3).

---

## 1. Độ dài so với ngân sách trang

Đếm bằng script trong scratchpad phiên (`wc_ch3.py`): "tiếng" = token cách nhau bởi khoảng trắng, bỏ dòng chú thích `%`,
lệnh LaTeX, công thức `$…$`; chữ trong bảng/hình đếm riêng.

| Mục | Ngân sách (OUTLINE-V2) | Chữ văn xuôi | Chữ trong bảng/hình | Ước lượng trang (mật độ đo được, xem dưới) | Theo thước 330 tiếng/trang của brief |
|---|---:|---:|---:|---:|---:|
| Mở chương | 0,25 | 105 | 0 | ≈ 0,2 | ≈ 0,3 |
| 3.1 Phát biểu bài toán, một lượt quyết định | 2 | 391 | 485 (H3.1 + giả mã) | ≈ 1,7 | ≈ 2,2 |
| 3.2 Ba mốc giờ trả | 1,75 | 424 | 260 (Bảng ví dụ + H3.2) | ≈ 1,55 | ≈ 2,0 |
| 3.3 Luật C, Nhận xét 3.1 | 2,5 | 690 | 489 (bảng ràng buộc + giả mã kiểm trần) | ≈ 2,35 | ≈ 3,1 |
| 3.4 Luật đối chứng, bộ chọn | 1,5 | 669 | 241 (bảng luật) | ≈ 1,8 | ≈ 2,5 |
| 3.5 Lời hứa theo dự báo | 1,25 | 365 | 218 (giả mã) | ≈ 1,25 | ≈ 1,7 |
| 3.6 Sổ theo từng khách | 0,75 | 262 | 17 | ≈ 0,55 | ≈ 0,9 |
| 3.7 Cài đặt, kiểm thử, tái lập | 2,5 | 703 | 371 (bảng kiến trúc + H3.3) | ≈ 2,2 | ≈ 3,1 |
| Dự phòng | 0,5 | — | — | — | — |
| **Tổng** | **13** | **3.615** | **2.081** | **≈ 12 (+ tiêu đề)** | **≈ 15,8** |

**Hai thước, vì chúng lệch nhau.** Brief đặt mục tiêu ≈ 330 tiếng văn xuôi/trang. Đo trên `main.pdf` hiện tại (cùng mẫu
13 pt, giãn 1,5) bằng `pdftotext | wc -w`: trang gần như toàn chữ của chương 3 cũ có 585 (tr. 40) và 586 (tr. 44) tiếng;
toàn bộ chương 3 cũ (tr. 32–48, có bảng, định lý, một hình) có 7.748 tiếng trên ≈ 16,1 trang ≈ 481 tiếng/trang. Cột
"mật độ đo được" dùng ≈ 560 tiếng/trang cho văn xuôi cộng diện tích ước lượng cho từng bảng/hình (giả mã 16 dòng ≈ 0,65 tr.;
bảng 5–8 dòng ≈ 0,3–0,55 tr.; mỗi hình TikZ ≈ 0,35–0,55 tr.). Theo thước đó chương ≈ 12 trang, trong ngân sách 13; mục 3.4
vượt khoảng 0,3 trang, bù bởi 3.6 và 3.7. Theo thước 330 của brief thì chương ≈ 15,8 trang. Bản nháp đầu dài 5.220 tiếng
văn xuôi; tôi đã cắt hai lần xuống 3.615. Nếu bản dựng thật vượt 13 trang, xem các chỗ cắt tùy chọn ở mục 9.

## 2. Số dòng `% EV:` và các dòng sổ được dùng

- **53 dòng** bắt đầu bằng `% EV` (mỗi đoạn có sự kiện một dòng; mỗi nhóm dòng của bảng/giả mã một dòng).
- Dòng sổ chính được trỏ: A01, A02, A04–A19, A21–A24, A26–A28; B01, B03, B05, B06, B10, B15–B17, B20; C04, C19, C23;
  D01, D04; E01, E08; F01–F04, F06, F07, F09, F10, F12; H01, H02, H13; I01, I08, I09, I13; J01, J03, J05, J10, J11, J18,
  J21, J35; K02, K04, K05, K18, K19, K26, K27, K33, K41, K43, K50.
- Dòng phụ lục 1: N-03, N-05 (CORRECTED), N-06, N-07, N-16, N-21, N-25, N-26, N-28, L1a-01; mục 0.1–0.2.
- Mã X3-01…X3-19 = dữ kiện mã nguồn tôi mở trong phiên này (mục 3).

## 3. Dữ kiện mã nguồn đã xác minh (chỉ đọc), không có sẵn trong sổ — đề nghị thêm vào sổ

`SRC` = `C:/Code/RideBound-noworse/src/`; `SCR` = `E:/Code/Report_INT3508/ridebound-scratchpad/`.

| ID | Dữ kiện dùng trong chương | Anchor |
|---|---|---|
| X3-01 | Lô sự kiện gồm: yêu cầu mới, xác nhận đặt xe, từ chối lời mời, hủy, tiến độ xe, xe tới điểm dừng, khách lên, khách xuống, cập nhật bảng giờ đi, nhịp thời gian, sự cố | `SRC/RideBound.Contracts/Protocol/EventBatchMessages.cs:42-61` |
| X3-02 | Trường của yêu cầu (điểm đón/trả, giờ đón sớm nhất/muộn nhất, thời gian ngồi xe tối đa, chính sách cam kết), của xe (sức chứa, ghế đã dùng, vị trí, khách trên xe, khách đã nhận, kế hoạch), của bảng giờ đi | `SRC/RideBound.Contracts/Protocol/OnlineEventModels.cs:144-153, 172-178, 181` |
| X3-03 | Bộ sinh dựng phương án giữ nguyên kế hoạch trước tiên; nếu kế hoạch đang chạy vi phạm ràng buộc vật lý cấu trúc thì trả lỗi cho xe đó; chèn đón/trả của yêu cầu mới vào mọi cặp vị trí (đón trước trả) của phần kế hoạch còn đổi được, giữ thứ tự điểm cũ | `SRC/RideBound.Algorithms/Candidates/InsertionCandidateGenerator.cs:161-164, 171-182, 196-229, 548-575, 691-693` |
| X3-04 | Bộ kiểm quyết định: kiểm vật lý và lịch trước; duyệt các khách đã nhận còn hoạt động trên xe đang xét theo thứ tự mã; mốc $e$ = kế hoạch cũ chiếu trên trạng thái sau lô sự kiện với bảng giờ đi hiện tại; kiểm khóa; tính ba hiệu; chọn cơ sở (decisionInduced / visible); gọi phép kiểm trần. Phạm vi xe: `ScopedVehicleId = set.VehicleId` | `SRC/RideBound.Application/Commitments/CommitmentDecisionValidator.cs:201-214, 233-239, 355-361, 404-411, 494-499, 512-520`; `SRC/RideBound.Algorithms/Commitments/HardVectorCandidateAssessor.cs:171` |
| X3-05 | Phép kiểm trần: before + delta, so từng chiều trong 10 chiều với `hardLimit` nếu chiều áp cho giai đoạn hiện tại; loại khi after > hardLimit (bằng thì qua); giai đoạn = Accepted / WaitingPickup / Onboard; bản ghi chặn gồm khách, chiều, trần, trước, phần dời, sau. Độ lệch giờ trả lấy trị tuyệt đối | `SRC/RideBound.Domain/Commitments/CommitmentBudgetEvaluator.cs:6-12, 72-104, 107-114`; `SRC/RideBound.Application/Promises/PromiseDeltaCalculator.cs:139, 259-262` |
| X3-06 | Khóa xe luôn bật; khách trên xe: khóa xe, điểm đón, giờ đón; khách chờ đón: các khóa xác nhận cuối từ cấu hình (xe, điểm đón, giờ đón); khóa so với phép chiếu $e$; giờ đón bị khóa nghĩa là phải **bằng** giờ đón khi giữ nguyên kế hoạch (không có ratchet trong cấu hình) | `SRC/RideBound.Domain/Commitments/CommitmentLockEvaluator.cs:42-60, 156-161, 186, 204-207`; `SCR/tang3/configs/C-30.json:94-98` |
| X3-07 | Thứ tự mục tiêu: số phương án bị ép (chỉ khi có), số yêu cầu nhận, mức dùng trần lớn nhất (ppm) rồi tổng phần sửa lời hứa do điều phối theo từng chiều (khi có trần cứng), chi phí kế hoạch, thứ hạng mã phương án; trần 0 với mức dùng 0 được tính là 1.000.000 ppm | `SRC/RideBound.Algorithms/Policies/SolverBackedFleetSelection.cs:271-303, 319-330, 365-385, 510-522`; `HardVectorCandidateAssessor.cs:612-626` |
| X3-09 | Hai luật phục hồi: giữ phương án giữ nguyên làm phương án bị ép khi mọi lỗi là lỗi hạn chót/trần; "không tệ hơn" giữ thêm phương án bị loại không làm lỗi đó tệ hơn | `HardVectorCandidateAssessor.cs:79-99, 257-310`; `SRC/RideBound.Algorithms/Policies/SolverBackedRidePoolingPolicy.cs:322-334` |
| X3-10 | Tập chỉnh trần buổi sáng (w07, w07x) và lần chạy trần 120 giây trên tập chính dùng cùng bộ chạy lưu trữ và WP4 có luật phục hồi (b) như T3.8 | `SCR/tang3/w07/run_w07.py:8`; `SCR/tang3/w07x/run_w07x.py:7`; `SCR/tang3/t38c120/run_t38c120.py:3-8` |
| X3-11 | Lời hứa hiển thị $D = \max(p, S)$; quy tắc ngày nguồn causal-no15; $g = 1$ trong khung hiện tại, $m(b)/m(b_0)$ sau đó; vòng lặp kéo dãn | `SCR/optimize/display_layer.py:1-16, 34-57, 60-64`; `SCR/optimize/promise_stretch.py:1-12, 25-39, 49-52` |
| X3-12 | $D_0$ = lời hứa hiển thị đầu; $q$ = tổng **có dấu** $(p - e)$ trên các lần sửa giờ trả; ba phần của sổ cộng trên khách trễ > 60 s | `SCR/optimize/forecast_family_a.py:86, 91, 93, 134-138` (sổ và RD ghi 133-136: lệch 1–2 dòng) |
| X3-13 | Trạng thái cuối = bản tin checkpoint cuối; sổ có dòng `initialPromise` rồi các dòng `revision` với $v$, $e$, $p$; dòng đầu $v = e = p$; chuỗi liên tục $v_t = p_{t-1}$ | `SCR/tang3/evidence/METRICS-SPEC.md:35-50, 62-63` |
| X3-14 | C# trên .NET 10; Domain không tham chiếu gì; Application → Domain; Algorithms → Application, Domain; Solvers.OrTools → Application, Domain + Google.OrTools 9.15.6755; kiểm thử kiến trúc kiểm các luật phụ thuộc và việc OR-Tools chỉ ở cầu nối bộ giải | `C:/Code/RideBound-noworse/Directory.Build.props`; `SRC/*/*.csproj`; `C:/Code/RideBound-noworse/tests/RideBound.ArchitectureTests/DependencyRuleTests.cs:11-29, 95-110, 137-166` |
| X3-15 | Các loại bản tin (hello, helloAck, initializeRun, initialized, checkpoint, restore, finalizeRun, runSummary, eventBatch, decision, decisionApplied, shutdown, error); bộ chạy đọc/ghi luồng vào/ra chuẩn, dạng NDJSON; từ chối lô mới khi quyết định trước chưa được xác nhận; bộ chuyển đổi Python (FleetPy 1.0.2 ghim phiên bản) khởi động bộ chạy như tiến trình con | `SRC/RideBound.Contracts/Protocol/ProtocolPrimitives.cs:104-124`; `SRC/RideBound.Runner/Protocol/RunnerSession.cs:203-207, 448-455, 543`; `SRC/RideBound.Runner/Program.cs:104-105`; `SRC/RideBound.Runner/Protocol/NdjsonReader.cs`, `NdjsonWriter.cs`; `C:/Code/RideBound-noworse/simulators/fleetpy-ridebound/README.md:1-12`; `…/ridebound_fleetpy/runner_client.py:133-135` |
| X3-16 | Trên 34 kịch bản chính: điều phối không trần 0 quyết định bị ép trong 20.760; trần 30 giây 0 trong 20.101 | `SCR/optimize/codex-debate/claude-work/r21-stage1a/stage1a-report-2026-10-10.txt:42-43` |
| X3-17 | Giới hạn khối lượng: thăm dò 10.000, sinh 10.000, kiểm 10.000, bộ giải 100.000 đơn vị, thời gian tất định 1.000.000 µs, hạt giống 7 | `SCR/tang3/configs/wp4-tier3-v2.json:9-23` |
| X3-18 | B1 = không cam kết, tối ưu tự do, không sổ, không trần (vẫn không chuyển khách sang xe khác); C1 = trần 30 giây giờ trả, khóa xe và hai điểm dừng, cố định giờ đón | `E:/Code/Report_INT3508/ridebound/noi-dung/08-chuong4.tex:128-136` (chỉ đọc) |
| X3-19 | Tên cấu hình trong tệp thời gian chạy: b1-ref = ghép tự do, c1-nobudget = LOCKS, c1-h6ref = trần 30 giây (theo REG H13) | `SCR/optimize/codex-debate/claude-work/r17-rebuttal/r17-wp14r-elapsed-2026-10-10.txt:2-6` |

(X3-08 gộp vào X3-07.)

## 4. Sửa theo phụ lục 1 và các chỗ lệch trong nguồn

- **N-05 / mục 0.1–0.2 áp dụng:** không viết "≈ 0,56 s" hay "dữ liệu cho thấy dời sớm". Câu trong 3.2: trị tuyệt đối thuộc
  định nghĩa; trên các lần chạy, mọi lần dời sớm hơn chỉ đúng 1 ms; không nêu nguyên nhân của −1 ms.
- Phụ lục 1 mục 0.3 (phạm vi cộng dồn) và 0.4 không đụng tới chương 3 (kiểm toán cộng dồn để ở 4.5). Tôi **bỏ** ví dụ bản
  ghi cộng dồn thật (25,844 + 99,027 = 124,871 s, N-27) khỏi chương 3 trong lần cắt để tránh trùng 4.5; nếu cần minh họa
  "cả chuyến" bằng số thật, câu đó có sẵn ở N-08/N-27.
- Số dòng sổ của FFA: phần sổ ở dòng 134-138 (sổ chính và RD ghi 133-136); $D_0$ ở dòng 86, 93.
- Mệnh đề "C không bao giờ bị ép" dùng số mới: 0 / 20.101 (trần 30 giây, X3-16, N-21) và 0 / 20.435 (trần 120 giây,
  N-07); chiều tuyết 0 / 5.067 (N-26) chỉ để trong dòng EV của bảng luật.
- Bão hòa tiêu chí 3: thêm 3.504 / 3.504 của trần 120 giây (N-25).

## 5. Bằng chứng còn thiếu (nên không viết)

- Chi phí riêng của phép kiểm trần ở mỗi lượt quyết định: chưa đo; chương chỉ ghi thời gian cả lần chạy (H13) và câu "chưa
  đo riêng".
- Ghép tự do có cho đổi xe hay không trên tập tắc đường cố định: chưa kiểm (GLOSSARY ghi "chưa kiểm"); bảng chỉ ghi "Không
  khóa".
- Bộ chạy và luật phục hồi của 8 lần chạy chiều tuyết: chưa kiểm; không nêu trong mục tái lập.
- Nguyên nhân của các lần dời sớm −1 ms: chưa kiểm (phụ lục 1, 0.2); không nêu.
- Nơi đăng chính thức của Hörl và Zwick (2022): bản PDF là "Conference Paper" trong ETH Research Collection; hội nghị cụ thể
  (có thể là TRB 2022) **chưa kiểm**.
- Mô tả chế độ "ghi nhận đón muộn" (`lateBoarding: record-v1`, WP4:8) chưa có trong sổ; không dùng.
- Ví dụ một khách thật cho ba mốc $v$, $e$, $p$ (STYLE quy tắc 19 ưu tiên khách thật) chưa có dòng sổ nào ghi đủ ba mốc của
  một lần sửa; chương dùng ví dụ dựng tay 9:10:00 / 9:10:40 / 9:11:10 như OUTLINE-V2 yêu cầu.

## 6. Tài liệu tham khảo mới (khóa dùng trong chương)

| Khóa | Mục | Xác minh |
|---|---|---|
| `horl2022` | S. Hörl and F. Zwick. *Traffic uncertainty in on-demand high-capacity ride-pooling.* Conference paper, 2022 (nộp 27/10/2021). ETH Zurich Research Collection. https://doi.org/10.3929/ethz-b-000561639 | REG J01–J05 (văn bản HZ:1-20, 529-606 tôi đã mở lại: chiến lược B, công thức 5–11). Tên hội nghị chưa kiểm. |
| `engelhardt2026` | R. Engelhardt, F. Dandl, A. A. Syed, C. Ding, S. Alvarez-Ossorio Martinez, Y. Zhang, H. Hamdy, J. Brodersen, Z. Chen and K. Bogenberger. *FleetPy: an open source simulator for reproducible research on mobility-on-demand services.* European Transport Research Review 18:52, 2026. https://doi.org/10.1186/s12544-026-00823-3 | REG J18; FLEET:1-12 (đầu bài), FLEET:474 ("we used FleetPy version 1.0.2"). Có thể thay khóa cũ `fleetpy2022` (bản arXiv). |

Khóa có sẵn được dùng: `schulz2026`, `ortools`. Không dùng khóa nào khác.

## 7. Nhãn cần chương khác định nghĩa (đặt tên theo quy ước của tôi; người ghép đổi nếu khác)

`chuong:thucnghiem` (Ch. 4), `muc:c4-thietlap` (§4.1), `muc:c4-vaitro` (§4.6, bộ chọn), `muc:c4-dubao` (§4.7),
`muc:c4-hople` (§4.10), `muc:c2-dubao` (§2.4), `phuluc:A`, `phuluc:B`, `phuluc:C`.
Nhãn chương này cung cấp: `chuong:phuongphap`, `muc:baitoan`, `muc:baitoan-phatbieu`, `muc:luotquyetdinh`, `muc:bamoc`,
`muc:luatc`, `muc:giunguyen`, `muc:doichung`, `muc:dubao`, `muc:so`, `muc:caidat`, `muc:kientruc`, `muc:gioihan`,
`muc:kiemtra`, `dn:luatc`, `nx:giunguyen`, `eq:bamoc`, `eq:luatc`, `eq:dongnhat`, `eq:keodan`, `eq:so`,
`bang:luotquyetdinh`, `bang:vidu-bamoc`, `bang:rangbuoc`, `bang:kiemtran`, `bang:luat`, `bang:dubao`, `bang:kientruc`,
`hinh:vongquyetdinh`, `hinh:bamoc`, `hinh:bantin`.

## 8. Mẫu LaTeX

- **Môi trường mới `nhanxet`** (Nhận xét 3.1). Đầu tệp chương có định nghĩa có điều kiện; nên chuyển lên `main.tex`:
  `\theoremstyle{definition}\newtheorem{nhanxet}{Nhận xét}[chapter]` (đặt sau `dinhnghia`).
- Không dùng môi trường `proof` của amsthm vì mẫu chưa đổi `\proofname` (sẽ in "Proof."); chứng minh viết tay
  "*Chứng minh.* … □". Nếu thêm `\renewcommand{\proofname}{Chứng minh}` vào mẫu thì có thể đổi sang `proof`.
- Chỉ dùng thư viện TikZ đã nạp (`arrows.meta`, `positioning`); không cần pgfplots; không thêm gói nào. Giả mã viết bằng
  `tabular` trong `table` như DACN (Bảng 3.2/3.4/3.5 của DACN), từ khóa tiếng Việt ("hàm", "với mỗi … thực hiện",
  "nếu … thì", "trả về"), tên hàm in đậm.

## 9. Chỗ lệch so với OUTLINE-V2 và lý do; chỗ có thể cắt thêm

1. **Giả mã đánh số như Bảng, không phải "Giải thuật 3.x"**: mẫu không có gói `algorithm`; DACN cũng để giả mã trong bảng.
   Thứ tự số bảng vì vậy là 3.1 giả mã một lượt; 3.2 ví dụ ba mốc; 3.3 ràng buộc và thứ tự tiêu chí; 3.4 giả mã kiểm trần;
   3.5 các luật; 3.6 giả mã dự báo; 3.7 kiến trúc (outline đánh 3.1–3.4 khác).
2. **Thêm giả mã phép kiểm trần** (yêu cầu của coordinator), ngoài hai giả mã của outline.
3. **Thứ tự tiêu chí của bộ chọn nằm trong bảng ràng buộc kiểu DACN (Bảng 3.3)**, như OUTLINE-V2 §3.3 ghi; bảng luật
   (Bảng 3.5) có 6 cột đúng như outline. Văn bản §3.4 giải thích điều kiện bật và độ bão hòa.
4. **Câu "hạn chót nới kiểu Hörl–Zwick cũng có tính chất này"** đặt ở §3.4 (đoạn Hörl–Zwick) thay vì ngay dưới Nhận xét ở
   §3.3, để không nói về các luật đối chứng trước khi định nghĩa chúng; đoạn giới hạn của Nhận xét trỏ sang §3.4.
5. **§3.7 gộp** kiến trúc và luồng bản tin thành một tiểu mục để tiết kiệm trang; không ghi số dòng mã (CX-37).
6. Không đưa luật hạn chót hai phía (M-30, chỉ chạy ở tập buổi sáng) vào bảng luật; nếu Chương 4 dùng nó thì thêm một hàng.
7. Ví dụ dựng tay xuất hiện ở bảng, hình và một câu văn (outline đòi cả Bảng 3.1 và H3.2); văn xuôi rút còn một câu để không
   lặp ba lần (STYLE quy tắc 20).
8. Tên "sổ theo dõi từng khách / sổ theo từng khách" theo OUTLINE-V2, không dùng "sổ cái" của GLOSSARY.
9. Thuật ngữ có tiếng Anh ở lần đầu trong chương (decision epoch, candidate plan, solver, insertion-only candidate
   generator, keep-route option, forced decision, recovery rule, cap, selector, lexicographic order, forecast-aware promise,
   replay, per-rider ledger): nếu Chương 1–2 đã giới thiệu, người ghép bỏ phần tiếng Anh ở đây.

**Có thể cắt nếu bản dựng vượt 13 trang (≈ 400 tiếng):** câu Hörl–Zwick ở §3.2 (đã có ở §3.4); đoạn "Điều phối không trần
và luật C … chưa được kiểm" ở §3.4 (lặp với §4.6); đoạn bão hòa tiêu chí 3 (giữ một câu, chuyển số sang §4.10); mục "Kiểm
thử phần mềm" ở §3.7 (số lịch sử); câu về khối lượng tính ở §3.7.

## 10. Câu hỏi mở cho chủ nghiên cứu / coordinator

1. Có chấp nhận nêu tên "Claude và Codex" ở §3.7 (ai đã viết chương trình kiểm) không? Câu này theo GLOSSARY F ("mô tả
   trung thực ai đã kiểm") và R19; nếu muốn, đổi thành "các tác tử phần mềm dựa trên mô hình ngôn ngữ lớn".
2. Mục "Tái lập" nói bản dựng lại phải cho đúng kết quả cũ trước khi dùng (REG I13). Đây là quy tắc quy trình, không phải
   kết quả; giữ hay chuyển sang Phụ lục C?
3. 15 lần chạy hiệu chỉnh (trong 185 lần chạy của phép kiểm 382.006 lần sửa) không có tên tập trong outline; tôi viết "15 lần
   chạy hiệu chỉnh cùng đợt". Phụ lục C nên định nghĩa tập này một lần.
4. Hai nhãn ngoài chương và tên hội nghị của Hörl–Zwick (mục 5–7).
