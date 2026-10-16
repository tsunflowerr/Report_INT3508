# RideBound — Bàn giao toàn bộ bối cảnh cho phiên AI mới (phiên kết thúc 2026-09-23)

**Viết cho:** một trợ lý AI (hoặc lập trình viên) **chưa từng đọc hội thoại nào trước đây**, sẽ tiếp
tục công việc và **thực hiện kế hoạch từng bước**. Tài liệu tự chứa. Mọi khẳng định về mã và số liệu
dưới đây đều đã được kiểm trực tiếp trong mã nguồn hoặc bằng script trên dữ liệu niêm phong; chỗ nào
chưa kiểm được thì ghi rõ ⚠️.

**Cập nhật 2026-09-24 00:15 (sau khi viết tài liệu):** một phiên khác (`ridebound-ef`) **đã bắt đầu
Tầng 2**: đã tạo worktree `E:\Code\RideBound-deadline` (nhánh `research/deadline-gate` từ `41a4e11`), gặp
bẫy CRLF khi tạo worktree và đã khôi phục byte bằng `ridebound-scratchpad\deadline\restore_index_bytes.py`,
đang lập baseline test (nhật ký ở `ridebound-scratchpad\deadline\logs\`). Lúc cập nhật, **chưa có thay đổi
nào trong `src/` hay `tests/`** của worktree. ⟹ Trước khi làm gì ở Tầng 2, **kiểm xem có phiên nào khác đang
làm trong worktree không** (`ListAgents`, thời điểm sửa của `logs\`), đọc nhật ký, và **không làm trùng/đè
lên việc của phiên kia**. Đồng thời: `E:\RideBoundData` thực tế **90 GB** (đo bằng `du` ngày 24/09), không
phải 33,6 GB — con số 33,62 GB trong bàn giao 16/09 là phần tính vào hạn mức cũ.

**Tài liệu có thẩm quyền cao nhất về kế hoạch:** `E:\Code\Report_INT3508\KE-HOACH-HOP-NHAT-2026-09-23.md`
(1.751 dòng, "Sửa đổi 1"). Tài liệu này là **bản đồ và luật chơi**; kế hoạch kia là **đặc tả chi tiết**.
Khi hai tài liệu mâu thuẫn về chi tiết kỹ thuật của kế hoạch, **kế hoạch thắng**; khi mâu thuẫn về ràng
buộc của người dùng, **tài liệu này thắng** (vì nó mới hơn — xem §2).

---

## 0. Đọc cái gì, theo thứ tự nào — BẮT BUỘC trước khi làm bất cứ việc gì

Không được viết một dòng mã, sửa một dòng LaTeX, hay chạy một mô phỏng nào trước khi đọc xong nhóm A.

### Nhóm A — bắt buộc, đọc hết

| # | Tệp | Vì sao |
|---|---|---|
| A1 | **Tài liệu này** | Luật chơi, bối cảnh, ràng buộc |
| A2 | `E:\Code\RideBound\AGENTS.md` | Luật của kho, ghi đè mọi mặc định |
| A3 | `E:\Code\RideBound\docs\00-index.md` | Theo `AGENTS.md` |
| A4 | `E:\Code\RideBound\docs\01-research-charter.md` | Theo `AGENTS.md` |
| A5 | `E:\Code\RideBound\docs\18-status-and-decision-log.md` | Nguồn sự thật sống của kho, có lệnh test và số đếm baseline. ⚠️ Lạc hậu so với commit `41a4e11` (ghi `009_MATRIX_HALTED_40_OF_160`, trong khi bằng chứng đã commit là 160/160) |
| A6 | `E:\Code\RideBound\docs\16-roadmap-and-work-packages.md` — work package đang hoạt động | Theo `AGENTS.md` |
| A7 | `E:\Code\RideBound\docs\03-related-work-and-claim-boundary.md` | Ranh giới claim được phép |
| A8 | `E:\Code\Report_INT3508\KE-HOACH-HOP-NHAT-2026-09-23.md` — **toàn bộ**, tối thiểu §1, §2 (sổ kiểm chứng K1–K22), §2.1, §5.2, §5.6, §6 Tầng 0–2, §7, §8, §9, §10 | Kế hoạch có thẩm quyền |
| A9 | `E:\Code\RideBound\docs\tasks\47-wp15-lifecycle-commitment-refinement.md` | Ràng buộc WP15 đã khóa mà kế hoạch viện dẫn (#2, #3, #4, #7) |

### Nhóm B — đọc khi làm tới phần liên quan

| Tệp | Khi nào |
|---|---|
| `E:\Code\Report_INT3508\RIDEBOUND-BAN-GIAO-CONTEXT.md` (bàn giao 2026-09-16, 1.168 dòng) | Trước khi đề xuất bất kỳ hướng mới nào: **§8 (tám hướng đã chết và bằng chứng)**, **§12 (bẫy 12.1–12.10)**, §5 (hạ tầng chạy, cách đọc transcript), §7 (toàn bộ 558 lần chạy), §13 (ràng buộc cũ), §17 (những gì không được tuyên bố) |
| `E:\Code\Report_INT3508\ridebound-scratchpad\CONTEXT-handoff.md` (bàn giao 2026-09-08) | Lịch sử cũ hơn; tám ứng viên đã loại |
| `E:\Code\Report_INT3508\KE-HOACH-NGHIEN-CUU-2026-09-22.md` | Kế hoạch cũ của Claude — **đã bị thay thế**, chỉ để tra lịch sử |
| `E:\Code\Report_INT3508\ridebound-scratchpad\conduct-outcome-plan-2026-09-22\KE-HOACH-END-TO-END-CONDUCT-OUTCOME-STOCHASTIC.md` | Kế hoạch của Codex — **đã bị thay thế**, nhưng backlog §14–15 (ticket C01–C08, A01–A07, P01–P08, S01–S07, E01–E06; ma trận test M/G/W/Q) là nguồn chi tiết cho **Tầng 3** |
| `…\conduct-outcome-plan-2026-09-22\SOURCE-FINDINGS.md`, `WEB-RESEARCH-NOTES.md` | Khảo sát mã và văn liệu của Codex (ký hiệu 📎 trong kế hoạch) |
| `E:\Code\Report_INT3508\ridebound-scratchpad\research-2026-09-16\*.md` | Ghi chép đọc tài liệu, kiểm định tính mới (`KIEM-DINH-TINH-MOI-2026-09-20.md`), đánh giá conduct/stochastic (`DANH-GIA-CONDUCT-STOCHASTIC-2026-09-21.md`), `IDEA-FALSIFICATION.md`, `SHAREABILITY-SHADOWS-18-NOTES.md` (Elmi 2026), `MULTIPLE-PLAN-16-NOTES.md` |
| `E:\Code\Report_INT3508\ridebound-scratchpad\session-2026-09-23-archive\` | Bản trích văn bản các bài báo và ba báo cáo khảo sát của phiên này (xem §3.5) |
| Báo cáo LaTeX `E:\Code\Report_INT3508\ridebound\noi-dung\*.tex` | Trước khi làm Tầng 0 |

### Nhóm C — bài báo gốc (đọc khi viết phần văn liệu hoặc khi cần trích)

Xem §3.5. Bài quan trọng nhất: **Elmi và cs. 2026** (đối thủ gần nhất về "bảo đảm lời hứa") và
**Schulz & Pfeiffer 2026** (đối thủ gần nhất về "trần dịch chuyển/hạn chót").

---

## 1. Người dùng, đề tài, mục tiêu

- **Người dùng:** Trần Quang Thành — MSSV 23020155 — lớp K68I-IT2 — Trường ĐH Công nghệ (UET), ĐHQGHN.
  Viết tiếng Việt, muốn giải thích **đơn giản, dễ hiểu, có ví dụ thực tế từ chính hệ thống**, đủ để
  trình bày lại cho người khác. Gọi đại từ trung tính khi nhắc tới người dùng.
- **Đề tài:** khóa luận tốt nghiệp về **RideBound** — hệ điều phối xe đi chung (ride-pooling) có cơ chế
  **"lời hứa có biên được chứng nhận"** (certified bounded promises): mỗi khách nhận một lời hứa ETA, và
  hệ thống giới hạn có kiểm chứng mức độ lời hứa bị dời trong suốt vòng đời chuyến.
- **Tên cán bộ hướng dẫn:** **chưa biết** — `noi-dung/00-bia.tex` còn `[chờ bổ sung]`. **Phải hỏi người
  dùng**, không được tự điền.
- **Tiêu chí chấm KLTN người dùng đặt ra (nguyên văn):**
  - *"Bài toán thực tế không? Quan trọng không? Đáng làm không?"*
  - *"Giải pháp có hợp lý không? Phương pháp/Lý luận → Mới hơn so với đối thủ hoặc có các giới hạn tốt
    hơn (chi phí rẻ hơn/thời gian nhanh hơn…)"*
  - *"Minh chứng thông qua kết quả: Định lượng (Nghiên cứu) / Định tính (Demo)"*
- **Mong muốn gốc của người dùng (đầu phiên):** hệ thống đang *"rất giống với 1 hệ thống khác về cùng
  chung lời hứa"*; người dùng muốn **"khác biệt"** thật — một cách tiếp cận, cách giải, thuật toán hay
  đánh đổi khác — chứ không chỉ khác nhau về thước đo.
- **Kết luận của phiên về câu hỏi đó:** chỗ khác biệt chứng minh được **không** nằm ở "có bảo đảm lời
  hứa" (Elmi 2026 đã có) hay "chặn tổng biến thiên" (trên hệ này trùng với chặn hai đầu), mà ở **Định
  lý 4**: trong các họ ràng buộc lời hứa (theo hành vi, theo hạn chót, theo kết quả nhìn thấy), **chỉ
  ràng buộc theo hành vi không bao giờ là nguyên nhân làm rỗng tập phương án khi thế giới trôi dạt**, và
  họ nào hỏng phụ thuộc **chiều** trôi. Chi tiết ở §7.

---

## 2. Ràng buộc bắt buộc — còn hiệu lực (cập nhật 2026-09-23)

### 2.1 Ràng buộc của người dùng

1. **Không xóa bất kỳ tệp nào của người dùng** — kể cả tệp trông "linh tinh", tệp tạm, kết quả cũ,
   corpus, dữ liệu tải về, vendor checkout, artifact kết quả. *"Không tùy tiện xóa file quan trọng gây hư
   hại máy."* Nếu thấy cần xóa, **hỏi trước**.
2. **Dung lượng đĩa — CHÍNH SÁCH MỚI (người dùng nói ngày 2026-09-23):** *"việc quá dung lượng thì không
   sợ miễn không xóa các file linh tinh trong máy của tôi, đảm bảo máy vẫn đủ dung lượng thoải mái không
   gây ảnh hưởng nghiêm trọng đến máy tính, còn đâu toàn bộ do AI lúc đó có thể quyết định."*
   ⟹ Giới hạn cũ "< 30 GB" **không còn là rào cản**. Thay bằng: giữ **ổ E: còn ≥ 40 GB trống** và **ổ C:
   còn ≥ 50 GB trống** (mức "thoải mái" do AI phiên này đề xuất; ngày 23/09 E: còn **77,4 GB** trống, C:
   còn **114,2 GB** trống; `E:\RideBoundData` tổng cộng **90 GB** theo `du` ngày 24/09 — con số 33,62 GB
   trong bàn giao 16/09 chỉ là phần tính vào hạn mức cũ). Tầng 2 cần thêm ~5–15 GB —
   an toàn. Kiểm dung lượng trước và sau mỗi đợt chạy lớn bằng PowerShell `Get-PSDrive` (đừng dùng
   `du -sh E:/RideBoundData` — chạy quá 5 phút).
3. **Quyền quyết định:** cùng câu trên, người dùng giao *"còn đâu toàn bộ do AI lúc đó có thể quyết định"*
   và yêu cầu AI phiên sau **thực hiện từng bước trong kế hoạch, kể cả viết mã**. Diễn giải của phiên này:
   AI phiên sau **được phép** thực hiện Tầng 0–2 của kế hoạch, gồm sửa mã RideBound **trong một git
   worktree riêng** (§8.3), với các mặc định ở §10. Vẫn phải **hỏi người dùng** khi: cần xóa tệp; cần
   push/commit lên remote hoặc thao tác ra ngoài máy; cần điền tên cán bộ hướng dẫn; muốn làm ngược một
   quyết định đã chốt trong kế hoạch; muốn bắt đầu Tầng 3.
4. **Không đụng cây làm việc chính của kho `E:\Code\RideBound`.** Nó có thay đổi chưa commit của người
   dùng: `docs/benchmarking/wp14r-013-v6-matrix-and-h6-rerun-2026-09-05.md` (sửa 38 dòng) và
   `docs/benchmarking/Kết quả benchmark.md` (chưa theo dõi). **Giữ nguyên tuyệt đối.** Mọi sửa đổi mã làm
   trong worktree `E:\Code\RideBound-deadline` (chưa tạo — §8.3). Các script, cấu hình thử nghiệm, kết quả
   trung gian đặt ngoài kho: `E:\Code\Report_INT3508\ridebound-scratchpad\...` và `E:\RideBoundData\...`.
5. **Báo tiến độ mỗi 1 giờ** khi có job dài đang chạy.
6. **Người dùng đã tự xóa các mục 4–7 trong bản báo cáo tiếng Việt cũ của họ — TUYỆT ĐỐI KHÔNG thêm
   lại.** Ràng buộc này áp cho tài liệu cũ, **không** áp cho bản LaTeX khóa luận `ridebound/`.
7. **Không đụng báo cáo thực tập** ở gốc `E:\Code\Report_INT3508\` (`main.tex`, `noi-dung/00-bia.tex` …
   `09-trang-danh-gia.tex`, `Baocaothuctap_23020155_TranQuangThanh.pdf`, và bản
   `C:\Users\quang\Downloads\Baocaothuctap_23020155_TranQuangThanh.docx`). Đó là báo cáo thực tập tại
   KiotViet, **khác** khóa luận, và đang có thay đổi chưa commit của người dùng.
8. **Không gửi email người dùng** (`thanh.tq2@kiotviet.com`) cho bất kỳ dịch vụ ngoài nào.
9. **Đảm bảo tốt cho hệ thống:** không cài phần mềm hệ thống, không đổi cấu hình máy, không tắt tiến
   trình của người dùng. (Ràng buộc cũ cho phép tắt chương trình ngầm không dùng nếu thiếu RAM — chỉ làm
   khi thật cần và nói rõ đã tắt gì.)

### 2.2 Ràng buộc của kho (`AGENTS.md` — ghi đè mọi mặc định)

- Trước khi sửa: đọc `docs/00`, `docs/01`, `docs/18`, work package đang hoạt động ở `docs/16`, tài liệu
  chủ đề liên quan.
- **Mọi thay đổi mã: chạy `dotnet test RideBound.slnx`.**
- Khi một việc đổi trạng thái cài đặt, hợp đồng, claim, baseline, metric, ranh giới kho hay việc tiếp
  theo: cập nhật `docs/18-status-and-decision-log.md`, decision entry liên quan, và
  `docs/19-requirement-traceability.md` — **làm trong worktree/nhánh nghiên cứu**, không làm trong cây
  chính (xem §8.3, bước cuối).
- Không chép cây mã BeGo/OptiGo vào kho.
- Domain và Application không phụ thuộc OptiGo, EF Core, ASP.NET, map provider, OR-Tools, thư viện mô
  phỏng. Adapter mô phỏng phải gọi **cùng runner có phiên bản**; không cài lại RideBound bằng Python/C++.
- **Không tuyên bố là mới:** dynamic insertion, ETA limits, reassignment, route similarity,
  least-commitment, time consistency, user satisfaction.
- Giữ thay đổi của người dùng và thay đổi không liên quan. Không xóa corpus, dữ liệu tải về, vendor
  checkout, artifact kết quả, cấu hình cục bộ như thao tác dọn dẹp.

### 2.3 Kỷ luật trung thực — không thương lượng

- **Không bịa.** Không bịa số, không bịa kết quả chạy, không bịa dòng mã, không bịa trích dẫn, không bịa
  nội dung bài báo. Không biết thì đọc; không đọc được thì ghi ⚠️ "chưa kiểm".
- Mọi khẳng định về mã phải kèm `tệp:dòng` **đã đọc trong phiên hiện tại**. Số dòng trong kế hoạch có
  thể lệch vài dòng — **grep lại trước khi sửa**.
- Mọi con số đưa vào khóa luận phải truy được về một script + một tệp dữ liệu, hoặc một mục/bảng của
  bài báo đã đọc.
- Test đỏ thì báo đỏ, kèm output. Bước nào bỏ qua thì nói bỏ qua. Kết quả âm là kết quả hợp lệ — ghi lại
  như kết quả dương (ràng buộc WP15 #7).
- Không nói quá: xem danh sách ❌ ở §7.6.

---

## 3. Bản đồ tệp và môi trường

### 3.1 Kho mã

| Đường dẫn | Ghi chú |
|---|---|
| `E:\Code\RideBound` | Kho chính, nhánh `main`, HEAD `41a4e11` ("Add comprehensive tests for commitment and optimization features"). Từ 23/09 ~23:57 có worktree `E:\Code\RideBound-deadline` (nhánh `research/deadline-gate`) do phiên `ridebound-ef` tạo — xem ghi chú cập nhật đầu tài liệu |
| `E:\Code\RideBound\RideBound.slnx` | Solution; lệnh test baseline `dotnet test RideBound.slnx` |
| `src\RideBound.Domain`, `src\RideBound.Application`, `src\RideBound.Algorithms`, `src\RideBound.Runner`, `src\RideBound.Contracts`, `src\RideBound.Benchmarking` | Các tầng (xem §12.2 của kế hoạch cho bản đồ `tệp:dòng`) |
| `simulators\fleetpy-ridebound\` | Adapter FleetPy (Python): `ridebound_fleetpy\fleet_control.py`, `session.py`, `mapping.py`; `actual_fleetpy_medium_preflight.py`, `actual_fleetpy_medium_verify.py` |
| `benchmarks\configurations\` | Cấu hình: `wp14-c1-h6-reference-v1.json` (C1 tham chiếu), `wp9-fleetpy-ridebound-hard-vector-audited-v1.json` (`--wp4-config`) |
| `benchmarks\fixtures\wp6\public\fleetpy-manhattan-v1\wp9-confirmatory-fixed-panel-v2\` | **Panel A** (20 ô `d201811{14..18}-s10-r{1..4}`, khung sáng 08–10h) |
| `benchmarks\fixtures\wp6\public\fleetpy-manhattan-v1\wp14-development-panel-v1\` | **Panel phát triển** (16 ô `d201811{12,13}-s10-r{1..4}-w{08,17}`) — tập giữ lại của Tầng 2B |
| `benchmarks\scenarios\wp9-confirmatory\<ô>.driver.json`, `benchmarks\scenarios\wp14-development\<ô>.driver.json` | Driver |

### 3.2 Dữ liệu và công cụ

| Đường dẫn | Ghi chú |
|---|---|
| `E:\RideBoundData\` | Toàn bộ dữ liệu, môi trường và kết quả thực nghiệm (**90 GB**, `du` 24/09). **Không xóa gì** |
| `E:\RideBoundData\wp9\confirmatory-h6-panela-v2\` | Các lần chạy panel A tĩnh (B1 `*-b1-tight-s7`, C1…) |
| `E:\RideBoundData\wp14\drift-v1\` | Các lần chạy trôi dạt (`dr-conduct-k0/k1`, …) |
| `E:\RideBoundData\wp9\runner\h6-confirmatory-v1` | Runner niêm phong dùng cho các lần chạy trôi dạt (`run_drift.py:59`) |
| `E:\RideBoundData\wp7\envs\fleetpy-1.0.2\python.exe` | **Trình thông dịch Python duy nhất dùng được** (`python` không có trong PATH của Git Bash) |
| `E:\RideBoundData\wp7\FleetPy-1.0.2` | FleetPy |
| `C:\Program Files\dotnet\dotnet.exe` | .NET |
| `E:\RideBoundData\wp6\extracted\sha256\d9\d9e86f33…\FleetPy_Manhattan\networks\Manhattan_2019_corrected\2018-11-{11..18}_tt_factors.csv` | Hệ số thời gian di chuyển đo thật, bước 15 phút, cột `simulation_time, time_interval, travel_time_factor, …` — **dùng cột `travel_time_factor`** (đã có lần đọc nhầm cột `time_interval`) |
| `E:\Code\Report_INT3508\tools\tectonic.exe` | Biên dịch LaTeX. **Không có poppler/pdftotext** trong `tools\` — kiểm tham chiếu treo bằng log |

### 3.3 Báo cáo khóa luận LaTeX

- Vị trí: `E:\Code\Report_INT3508\ridebound\` (thư mục con của repo git riêng của người dùng
  `E:\Code\Report_INT3508`, không phải kho RideBound).
- Build: `cd E:\Code\Report_INT3508\ridebound` rồi `..\tools\tectonic.exe -X compile main.tex --outdir .`
- Tệp: `noi-dung/00-bia.tex` (bìa, **thiếu tên CBHD**), `01-loi-cam-on`, `02-tom-tat`, `03-muc-luc`,
  `04-viet-tat`, `05-chuong1` (Đặt vấn đề, có mục "Chỗ đứng so với công trình gần nhất"), `06-chuong2`
  (Cơ sở lý thuyết), `07-chuong3` (Phương pháp + định lý), `08-chuong4` (Thực nghiệm, mục 4.1–4.14 có
  `\label`), `09-chuong5` (Kết luận + hướng phát triển), `10-tai-lieu`.
- Môi trường định lý: `dinhly` (đếm theo chương), `hequa` dùng chung bộ đếm với `dinhly`, `dinhnghia` bộ
  đếm **riêng**. Luôn dùng `\label`/`\ref`, không đánh số tay (bẫy 12.9).
- Trạng thái sau lần sửa 23/09: biên dịch sạch, 0 tham chiếu treo.

### 3.4 Kế hoạch, bàn giao, script

| Đường dẫn | Nội dung |
|---|---|
| `E:\Code\Report_INT3508\KE-HOACH-HOP-NHAT-2026-09-23.md` | **Kế hoạch có thẩm quyền** |
| `E:\Code\Report_INT3508\BAN-GIAO-PHIEN-2026-09-23.md` | Tài liệu này |
| `E:\Code\Report_INT3508\ridebound-scratchpad\claude-measurements-2026-09\` | **18 script đo** của phiên này + cache `b1_paths.pkl`, `equity.pkl` (xem §5.3) |
| `E:\Code\Report_INT3508\ridebound-scratchpad\drift\` | `preflight_drift.py`, `run_drift.py`, `run_drift_frac.py` (có `classify()` ở dòng 101–107), `basis-customer-visible.json` |
| `E:\Code\Report_INT3508\ridebound-scratchpad\levelc\decision_identity.py` | So **từng quyết định** giữa hai lần chạy (dùng cho đối chứng runner) |
| `E:\Code\Report_INT3508\ridebound-scratchpad\session-2026-09-23-archive\` | Lưu trữ của phiên này: `papers-text\` (16 bản trích văn bản bài báo), `survey-reports\` (3 báo cáo khảo sát), `tier2-v2-draft.md` (bản nháp Tầng 2 đã ghép vào kế hoạch) |

### 3.5 Bài báo

**Thư mục người dùng cung cấp:** `C:\PDF\Paper\` (13 PDF). Bản trích văn bản của cả 13 tệp nằm ở
`…\session-2026-09-23-archive\papers-text\` cùng tên, đuôi `.txt`.

| Tệp trong `C:\PDF\Paper\` | Bài (theo khảo sát của phiên) |
|---|---|
| `s00291-026-00847-0.pdf` | **Schulz & Pfeiffer 2026**, OR Spectrum 48:541–586 — hạn chót `l` tính từ lời hứa đầu; chèn trực tiếp hoặc chèn sau khi dời một khách sang tour khác (tiền tính giữa hai yêu cầu), **không** phải LNS |
| `s00291-025-00812-3.pdf` | Rauh, Ahrens, Büsing, Comis & Engelhardt 2025, OR Spectrum — *The dial-a-ride problem in primary care with flexible scheduling* (đóng băng tiền tố lịch "trước `τ_i`", không có ngân sách) |
| `1-s2.0-S0191261522000716-main.pdf` | Sharif Azadeh, Atasoy, Ben-Akiva, Bierlaire & Maknoon 2022, TR-B 161:128–149 — *Choice-driven dial-a-ride problem* (hộp tĩnh: cửa sổ + `L^Max`) |
| `Unreliability_in_ridesharing_systems_Measuring_cha.pdf` | **Fielbaum & Alonso-Mora 2020**, TR-C 121:102831 (đo bất ổn; kịch bản §6 đóng băng) |
| `Scale_analysis_for_on-demand_ridepooling_systems_a.pdf` | Fielbaum, Tirachini & Alonso-Mora — phân tích quy mô ride-pooling so với giao thông công cộng |
| `Value_of_time_and_reliability_for_urban_pooled_on-.pdf` | Alonso-González, van Oort, Cats, Hoogendoorn-Lanser… 2020, TR-C 115:102621 — giá trị thời gian và độ tin cậy |
| `1-s2.0-S0965856426000662-main.pdf` | Wardman, Murphy, Ojeda-Cabral… 2026, TR-A 207:104925 — meta-analysis hệ số giá trị thời gian (chờ, độ tin cậy…) |
| `Networks - 2014 - Kovacs - …consistency…survey.pdf` | Kovacs, Golden, Hartl & Parragh 2014, Networks — khảo sát VRP nhất quán |
| `OperationalEffectsofServiceLevelVariations-publication151005.pdf` | Molenbruch, Braekers & Caris, CEJOR, DOI 10.1007/s10100-015-0422-7 — ⚠️ liên quan việc kiểm mục `gerzinic2023` (T0.2.8) |
| `2508.04811v1.pdf` | Jiang, Yang & Wang 2025, arXiv — *HCRide* (công bằng hành khách + ưu tiên tài xế) |
| `FreezingtheMPSMgtScipaper.pdf` | Sridharan, Berry & Udayabhanu 1987, Management Science 33(9) — đóng băng lịch sản xuất chính (gốc ý tưởng "freeze horizon") |
| `BregniA._DAvinoM.SchiraldiM.M.pdf` | Bregni, D'Avino & Schiraldi, DAAAM 2011 (sản xuất) |
| `21020283-3476 (1).pdf` | Khóa luận UET của một sinh viên khác (Phạm Xuân Bách, QH-2021) — *Nghiên cứu tối ưu lịch trình cho bài toán chia sẻ chuyến đi*; tham khảo hình thức |

Ackermann & Rieck 2025 (multiple-plan DARP, least-commitment) **không** có trong thư mục này — chỉ biết qua `docs/03`.

**Tải về trong các phiên trước:** `E:\Code\Report_INT3508\ridebound-scratchpad\research-2026-09-16\downloads\`:
- `elmi-2026-shareability-shadows.pdf` — **Elmi, Moylan, Alonso-Mora & Fielbaum 2026**, *Improving
  ridepooling reliability using shareability shadows*, TR-C 192:105897, SHA-256 `5a68817a…fe728a5`
  (bản trích: `papers-text\elmi2026.txt`);
- `sivagnanam-2026-prompt-confirmation-v2.pdf` — Sivagnanam và cs. 2026, ICCPS (bản trích `sivagnanam2026.txt`);
- `fielbaum-2021-anticipatory-arxiv.pdf`, `fielbaum-2022-anticipatory-download.bin`, `rubinstein-2012-incremental-darp.pdf`.
- Zalesak, Hu & Samaranayake 2025, arXiv:2504.10649 — bản trích `papers-text\zalesak2025.txt`.

**Báo cáo khảo sát** (`session-2026-09-23-archive\survey-reports\`):
- `lit-extraction-schulz-rauh-molenbruch-kovacs.md` — trích nguyên văn cơ chế và ngữ nghĩa sửa lời
  hứa của 4 bài (Schulz & Pfeiffer 2026, Rauh và cs. 2025, Molenbruch và cs., Kovacs và cs. 2014);
- `lit-extraction-unreliability-scale-vot.md` — 3 bài đi chung (Fielbaum 2020, scale, value-of-time);
- `code-survey-config-runner-freeze-preflight.md` — khảo sát schema cấu hình cam kết, runner niêm phong,
  công cụ freeze, preflight.

---

## 4. Hệ thống RideBound trong một trang (đủ để hiểu kế hoạch)

**Ba mốc cho mỗi khách ở mỗi lần công bố `t`** (tọa độ mặc định: giờ trả khách):

| Ký hiệu | Nghĩa | Trong mã |
|---|---|---|
| `v_t` | lời hứa đang hiệu lực trước quyết định | `priorHistory.Current.PublishedPromise.Projection` |
| `e_t` | ETA khi **giữ nguyên tuyến** nhưng chiếu trên trạng thái đã giảm **toàn bộ lô sự kiện** của kỷ nguyên (mốc phản thực, "exogenous") | `CommitmentDecisionValidator.cs:316-340` (dùng `context.ReducedState`) |
| `p_t` | ETA trong phương án được chọn | `candidateProjection` |
| `p_0` | lời hứa **đầu tiên** | `history.Entries[0]`, luôn là `InitialPromise` |

- `A = |p − e|` — phần do **quyết định** gây ra. **Đối xứng** (`PromiseDeltaCalculator.cs:75-78`,
  `AbsoluteDifference` ở `:259-262`). ⚠️ Tài liệu `wp14r-013` giải thích sai là "một chiều".
- `d = |e − v|` — phần thay đổi khi **chiếu lại tuyến giữ nguyên** trên trạng thái mới. **Không** được gọi
  là "tác động thuần của giao thông" — nó gồm tiến độ thực của xe, độ trễ thực thi, cập nhật thời gian di
  chuyển, sự kiện vòng đời khác.
- `B = |p − v|` — cái khách **nhìn thấy**.
- **`B ≤ A + d` là bất đẳng thức, không phải đẳng thức.** Đồng nhất đúng là bản có dấu `z = x + c`.
- **Sổ cái cam kết** cộng dồn theo khách, 10 chiều. **Cơ sở hành vi** (`decisionInduced`, cơ chế C1)
  cộng `A`; **cơ sở kết quả** (`customerVisible`) cộng `B`.
- **No-op** = phương án giữ nguyên tuyến của một xe; có `p = e` nên `A = 0`. Mô hình chọn và kiểm bằng
  chứng **đòi đúng một no-op hợp lệ mỗi xe** (`CandidateSelectionModel.cs:276-279`;
  `DecisionMessages.cs:1113-1121`).
- **Bộ sinh phương án chèn thuần**: không bao giờ kéo lời hứa khách cũ sớm hơn `e` (đo: dấu `p − e` dương
  ở 479/479 lần có `A > 0` trong B1; 0/11 kéo sớm trong C1).
- **Nhánh chuẩn:** B1 `rolling-cost` (không cam kết), C1 `ridebound-hard-vector` (trần hành vi). Panel:
  108 yêu cầu / 8 xe mỗi ô; "Manhattan" thực chất là **bao đóng metric OD trên ≤ 96 nút đã chọn, tọa độ
  tổng hợp** (`actual_fleetpy_medium_preflight.py:113-139`) — nhu cầu là thật, mạng thì không.
- **Trôi dạt**: `preflight_drift.py` bơm hệ số thời gian di chuyển đo thật (vô hướng toàn mạng) theo lịch
  `(factor(t)/factor(khung_đầu))^k`; `k ∈ {0, 1}` (0 = tĩnh). Các lần chạy trôi dạt **chưa qua verifier**
  của dự án (verifier đòi `travelSnapshotVersion == 1`) ⟹ nhãn **thăm dò**.
- Bất biến miền quan trọng: `RideRequest.Board()` từ chối nếu đón ngoài cửa sổ
  (`RideRequest.cs:266-273`, *"Actual pickup time must remain inside the accepted pickup window."*).
  ADR-045/047 miễn cửa sổ dịch vụ cho **no-op ở bước sinh** (`ServiceQualityAllowance`), nên cái chết do
  đón muộn xảy ra ở `Board()`, không ở cổng cam kết.

---

## 5. Diễn biến và kết quả của chuỗi phiên 16/09 → 23/09

### 5.1 Việc đã làm, theo thời gian

1. Đọc bàn giao cũ, bài báo trong `C:\PDF\Paper`, khảo sát web; nhận diện đối thủ gần nhất là Elmi 2026
   và Schulz & Pfeiffer 2026.
2. Codex đề xuất một hướng khác ("conduct–outcome–stochastic"); đã đánh giá phê phán; sổ kiểm chứng
   K1–K16 phân xử từng điểm (Codex đúng ở K1, K3, K4, K8, K9; Claude đúng ở K2, K6, K10, K15, K16 và sai ở
   K5, K7, K12).
3. Giải thích đơn giản cho người dùng về `B ≤ A + d`, ví dụ thật (CE-6).
4. **Tầng 0 phần đầu** (sửa LaTeX) — xem §5.4.
5. Viết kế hoạch siêu chi tiết, rồi **hợp nhất** với kế hoạch của Codex thành
   `KE-HOACH-HOP-NHAT-2026-09-23.md`.
6. Đánh giá một phê bình của ChatGPT; chấp nhận có chọn lọc; **Sửa đổi 1** của kế hoạch (23/09): Định lý 4
   có điều kiện, Hệ quả 4.3, Tầng 2 tách 2A/2B, nhánh hạn chót hai chiều, thay đổi mã chẩn đoán số 6, sổ
   cái "chỉ tính phần gây hại" thành hướng phát triển. Kiểm chứng mới K17–K22.

### 5.2 Các lỗi đã mắc và đã sửa (để phiên sau không lặp lại)

| Lỗi | Sửa |
|---|---|
| Viết vào Chương 3 rằng `A` là "một chiều" (tin prose `wp14r-013`) | Mã tính `|p − e|` đối xứng; đã sửa Chương 3 ngày 23/09 kèm phản ví dụ CE-3 |
| Kiểm định DKW với `n = 1.581` khách | Giả lặp: khách trong một ô không độc lập. Đơn vị là **ô/episode**; dùng conformal theo episode |
| "Nhánh hạn chót chặn 60 khách" | Sai cơ chế: khi no-op vi phạm hạn chót một chiều thì mọi phương án vi phạm ⟹ **ô vô nghiệm** (fail-closed), không phải chặn khách |
| "Sửa khiếm khuyết ppm trước" | Sai: khiếm khuyết làm mọi nhánh cùng xếp hạng "nhận khách → chi phí", tức hàm mục tiêu khớp nhau; sửa ppm là ablation độc lập |
| "96% tập lựa chọn chỉ một ứng viên" | Mẫu số sai; đúng là **73,84% trên các epoch hoạt động** |
| Chứng minh ĐL 3.3 giả định `A ≤ B` | Đo được 228 vi phạm (0,42%) ⟹ ĐL 3.3 có điều kiện (H) |
| Gọi 9 ô k=1 và kiểm hồi tố 4/4 là "xác nhận" | Chỉ là giải thích hậu nghiệm / bằng chứng hồi tố; xác nhận thật là Tầng 2B |
| Định lý 4 bản đầu "chỉ cổng hành vi không bao giờ làm rỗng tập phương án" | Quá mạnh: nhánh hành vi chết 11/20 ô vì `Board()`. Viết lại có điều kiện |
| Tin rằng thông điệp fail-closed nói lý do của no-op | Nó trích ứng viên **đầu tiên theo id băm** ⟹ thêm thay đổi 6 |
| Ghi hệ số tối ×0,82–0,87 / sáng ×1,15–1,23 | Đọc lại: sáng ×1,14–1,26; tối ngày 16–17/11 gần phẳng; đầu khung tối nhích lên |
| Khẳng định lỗi dấu phẩy động trong `ceil((n+1)(1−α))` | Sai: kiểm 0 ca lệch; bẫy thật là **hàm quantile có nội suy** (`numpy.quantile` mặc định) |
| Đọc nhầm cột CSV (`time_interval` thay `travel_time_factor`) | Luôn in header trước |
| Heredoc bash cho văn bản tiếng Việt dài | `ENAMETOOLONG`/hỏng chuỗi ⟹ dùng công cụ Write/Edit |

### 5.3 Script đo (`…\claude-measurements-2026-09\`, 18 tệp)

Chạy: `PYTHONIOENCODING=utf-8 E:/RideBoundData/wp7/envs/fleetpy-1.0.2/python.exe -B <script>.py`
(cd vào thư mục script trước, vì `analyze1.py`, `analyze2.py` đọc `b1_paths.pkl` theo đường dẫn tương đối;
`b1_paths.pkl` sinh bởi `promise_paths.py <root> <pattern> b1_paths.pkl`, đã sao sẵn vào thư mục).
Mọi script chỉ **đọc** `E:/RideBoundData/...`.

| Script | Đo gì | Dữ liệu |
|---|---|---|
| `promise_paths.py` | Trích quỹ đạo lời hứa từ transcript | tham số dòng lệnh |
| `identity.py` | Độ khít `A + d` vs `B` | panel A |
| `aleb.py` | Điều kiện (H) | panel A |
| `signcheck.py` | Dấu `p − e` | panel A |
| `tvcheck.py` | Chuỗi đại lượng; `V` theo khách | panel A |
| `endpoint.py`, `drifttv.py` | Hai đầu / chuỗi / hành vi; tĩnh và trôi dạt | panel A, `wp14/drift-v1` |
| `cellpred.py` | Dự đoán khả thi theo ô cho hạn chót | `E:/RideBoundData/wp14/drift-v1` |
| `retrodict.py` | Kiểm hồi tố Định lý 4 họ `V` | `E:/RideBoundData/wp9/confirmatory-h6-panela-v2` |
| `equity.py` | Đuôi, CVaR, Gini | panel A |
| `analyze1.py`, `analyze2.py`, `analyze3.py`, `excess.py` | Thời điểm gánh nặng; phân bổ ngân sách; độ lớn từng lần dời; phần vượt trần | `b1_paths.pkl` / panel A |
| `choiceset.py` | Độ mỏng tập lựa chọn, mẫu số đúng | panel A |
| `objorder.py` | Thứ tự tầng mục tiêu thật | panel A |
| `realcase.py` | Trích ca `v/e/p` thật (CE-6) | panel A |
| `harmledger.py` | Sổ cái "chỉ tính phần gây hại" | B1 `-b1-tight-s7` + `dr-conduct-k1` |

**Kiểm tái lập nhanh trước khi dùng script:** chạy lại `harmledger.py` phải ra B1: tổng `A` 64.863,1 s,
tổng `h` 64.821,2 s, 403 khách, chênh 41,9 s (0,06%), `h ≠ A` ở 158/479 lần (đã chạy lại ngày 23/09, khớp).

### 5.4 Báo cáo LaTeX — đã sửa (Tầng 0 phần T0.1)

| Tệp | Thay đổi | Ngày |
|---|---|---|
| `07-chuong3.tex` | "Đẳng thức trung tâm" → "Phân rã cộng tính và độ khít"; `B = A + d` → `B ≤ A + d`; bảng `bang:khit-tung-lan` | 21/09 |
| `07-chuong3.tex` | ĐL 3.3 viết lại trên tập quỹ đạo + chính sách tối ưu, điều kiện (H) có đo, bảng `bang:dieukien-h`; nhãn `dl:tapcon`, `eq:phanra`, `eq:dieukien` | 21/09 |
| `08-chuong4.tex` | Tiêu đề bảng độ khít; đoạn nối sang kết quả mịn | 21/09 |
| `07-chuong3.tex` | Bỏ "quy ước một chiều của `A`"; thay bằng "`A` là đại lượng đối xứng" + CE-3 (`v=600, e=720, p=600` ⟹ `A=120, B=0`) + số đo 0/479 | 23/09 |
| `07-chuong3.tex` | Đoạn giả dược: `d` là "phần thay đổi khi chiếu lại tuyến giữ nguyên trên trạng thái mới"; tính bất biến theo chính sách là tính chất **thực nghiệm** (0,37% so với 507×) | 23/09 |

**Chưa** đưa Định lý 4 bản có điều kiện vào `07-chuong3.tex` (việc T0.2.2).

---

## 6. Số liệu đã kiểm chứng — dùng được trong khóa luận (kèm nguồn)

| Kết quả | Số | Nguồn |
|---|---|---|
| Dữ liệu niêm phong | 558 lần chạy | bàn giao 16/09 §7 |
| WP14R-013 | 160/160 job `terminalSuccess`, verifier độc lập 160/160 | commit `41a4e11`, JSON `designedJobCount=160, observedJobCount=160, missingJobCount=0` |
| Độ khít `B ≤ A + d` | dấu bằng đúng ở 99,58% lần công bố; hỏng ở 47,9% số lần cả `A` lẫn `d` khác 0; hụt toàn cục 0,0748%; khi trôi dạt thuận chiều, phần hụt = `2d` | `identity.py` |
| Điều kiện (H) `|p−e| ≤ |p−v|` | hỏng 0,42% (228 lần) ở B1 | `aleb.py` |
| Dấu `p − e` | 0/479 kéo sớm ở B1; 0/11 ở C1; dấu xác định ở 476/476 ca `A, d > 0` | `signcheck.py` |
| Tính bất biến của `d` theo chính sách | chênh 0,37% so với chênh 507× của `A` | Chương 3 (đoạn giả dược) |
| Mệnh đề 2 (chuỗi ≈ hai đầu) | 369 vs 369 khách bị chặn; chênh ≤ 1 trên 1.735 ở mọi ngưỡng 30/60/120/300 s | `endpoint.py` |
| Đuôi gánh nặng (panel A, giờ trả) | tổng `A`: B1 64.863 s, C1 128 s; `A_r = 0`: 76,8% vs 99,3%; cực đại 573,5 vs 27,6 s; CVaR₉₅ 336,5 vs 1,6; CVaR₉₉ 473,4 vs 8,0; Gini 0,8569 vs **0,9963** (bẫy Gini) | `equity.py` |
| Biến động nhìn thấy dưới C1 | p90 8,1 s, p99 21,0 s, cực đại **38,7 s**; 4/1.581 khách (0,3%) vượt 30 s ⟹ 99,7% dưới 30 s — **quan sát mô tả trên panel tĩnh, không phải bảo đảm** | `tvcheck.py` |
| Giá của cam kết | C1 phục vụ ít hơn B1 **7,13 pp**; xóa **99,8%** tổng gánh nặng; CVaR₉₅ giảm ~210 lần | bàn giao 16/09 + `equity.py` |
| Thời điểm gánh nặng | 83,8% trước khi đón | `analyze1.py` |
| Độ lớn từng lần dời | trung vị 115,6 s / lần | `analyze3.py`, `excess.py` |
| Độ mỏng tập lựa chọn | **73,84%** tập lựa chọn xe chỉ một ứng viên trên epoch hoạt động (2.142/14.133 = 15,2% epoch có nhận/từ chối khách); 80,4% epoch hoạt động có ≥ 1 xe với ≥ 2 ứng viên | `choiceset.py` |
| Thứ tự tầng mục tiêu | `accepted-request-count` (L0) → `worst-hard-utilization-ppm` (L1, **hằng 1.000.000**) → `revision:*` (L2–11, khác 0 **0/7.430**) → `operational-cost` → `candidate-id-rank` | `objorder.py` |
| Trôi dạt k=1: cực đại `D⁺` theo ô (9 ô sống sót dưới C1) | 54, 60, 63, 78, 81, 85, 85, 87, 102 s ⟹ hạn chót 30 s khả thi 0/9, 60 s 2/9, 120 s 9/9 — **giải thích hậu nghiệm** | `cellpred.py` |
| Trôi dạt k=0 | `D⁺` ≤ 28 s ở cả 20 ô | `cellpred.py` |
| Nhánh hành vi 30 s ở k=1 | chết **11/20 ô** vì `window-wall` (`Board()`), **0 ô** vô nghiệm do cam kết | `wp14/drift-v1` |
| Cơ sở kết quả 30 s | chết 4/20 ô (k0), 19/20 ô (k1) | `wp14/drift-v1`, `exploratory-visible-basis-v1` |
| Kiểm hồi tố họ `V` | dự đoán `{d20181116-s10-r2, d20181116-s10-r4, d20181117-s10-r1, d20181117-s10-r3}` = tập vô nghiệm thật, **4/4**; ô sát ngưỡng: `V` max 29,8/29,4/27,8 s → khả thi (đúng); 32,0/32,5/34,2/38,7 s → vô nghiệm (đúng) — **bằng chứng hồi tố** | `retrodict.py` |
| `d` dưới trôi dạt k=1 | p90 47,4 s, cực đại 150,7 s | kế hoạch §9 |
| Sổ cái chỉ tính phần gây hại | chênh 0,06% tổng; cùng 403 khách; `h ≠ A` ở 33% lần công bố | `harmledger.py` |
| Hệ số giao thông (tỉ số cuối/đầu khung) | sáng 08–10h: ×1,14 (12/11), ×1,15 (13/11), ×1,17–1,26 (14–18/11); tối 17–19h: ×0,84 (12/11), ×0,87 (13/11), ×0,82 / ×0,80 / ×0,86 (14, 15, 18/11), gần phẳng ×0,99 / ×1,04 (16, 17/11); đầu khung tối nhích +0,5–1,6% trong 15–30 phút | đọc trực tiếp CSV ngày 23/09 |
| Ca thật CE-6 | ô `d20181114-s10-r1`, khách `rq-acbbcd86c…`: `v=15:09.943, e=15:09.253, p=16:39.497` ⟹ `A=90,244; d=0,690; B=89,554`; hụt `2d = 1,380` | `realcase.py` |
| Elmi 2026 | giảm số khách bị đụng 4,1 lần nhưng gánh nặng người bị đụng tăng **4,5 lần**; viết rằng bảo đảm *"would not be possible if even a single change were allowed"*; mạng tĩnh; nhận 16/01/2026, chấp nhận 24/07/2026, trực tuyến 04/08/2026 | `elmi2026.txt` |

---

## 7. Đóng góp đã chốt, định lý, ranh giới claim

### 7.1 Định lý 4 — bản có điều kiện (Sửa đổi 1, đang có hiệu lực)

- **Giả thiết (N):** tại kỷ nguyên đang xét, no-op của xe đã qua mọi kiểm tra **không thuộc cam kết**.
- **Bốn họ cổng:** `C` (sổ cái hành vi `Σ A ≤ κ` — RideBound C1), `M⁺` (hạn chót một chiều `p − p_0 ≤ κ` —
  Schulz & Pfeiffer 2026), `M` (hạn chót hai chiều `|p − p_0| ≤ κ` — cửa sổ quanh lời hứa đầu, gần "hộp
  tĩnh" của Sharif Azadeh 2022), `V` (sổ cái kết quả `Σ B ≤ κ` — cơ sở `customerVisible`).
- **(a) Mọi quỹ đạo:** dưới (N), với mọi `κ ≥ 0`, cổng `C` không bao giờ loại no-op ⟹ **cổng hành vi không
  bao giờ là nguyên nhân làm rỗng tập phương án**. Chứng minh: no-op có `c_t = 0` nên `C_t = C_{t−1} ≤ κ`.
- **(b) Quỹ đạo dự phòng** (luôn giữ tuyến): `κ*_C = 0 ≤ κ*_{M⁺} = M⁺_noop ≤ κ*_M = M_noop ≤ κ*_V = X`;
  bước `M ≤ V` cần chuỗi công bố liên tục.
- **Hệ quả 4.3 (chiều trôi):** trên quỹ đạo dự phòng `p_t − p_0 = Σ_{s≤t} x_s`. Trôi bất lợi (mọi
  `x_s ≥ 0`, sáng): `M⁺ = M = V`, ba họ cùng hỏng. Trôi thuận lợi (mọi `x_s ≤ 0`, tối): `M⁺ = 0` — hạn chót
  một chiều **an toàn** — còn `M = V` vẫn lớn nên hạn chót hai chiều và cổng kết quả **vẫn** hỏng. Trên hệ
  thật `x_s` không thuần dấu ⟹ chỉ gần đúng.
- **Hệ quả phụ:** buổi tối hạn chót một chiều cho phép **tiêu phần trôi thuận lợi** để dời khách, có thể
  phục vụ nhiều khách hơn trần hành vi — đánh đổi thật, phải báo cáo.
- **Câu được viết:** *"Cổng hành vi không bao giờ là nguyên nhân khiến tập phương án rỗng."*
  **Không** viết *"hệ thống dùng cổng hành vi không bao giờ kẹt"*.
- **Chứng minh sơ cấp** — nói thẳng; giá trị ở khung so sánh và kiểm chứng thực nghiệm.

Các kết quả khác: Mệnh đề 1 (chuỗi `D⁺ ≤ M⁺ ≤ M ≤ V ≤ C + X`, kiến thức cơ bản, không phải đóng góp);
ĐL 3.1 (cơ sở hành vi không làm rỗng do cam kết), ĐL 3.2 (cơ sở kết quả có thể làm rỗng), ĐL 3.3 (có
điều kiện (H)); Mệnh đề 2 (bộ sinh đơn điệu ⟹ chuỗi ≈ hai đầu — **đừng dùng tổng biến thiên làm điểm
phân biệt**); Mệnh đề 3 (biên hai lớp, chỉ để báo cáo, ràng buộc vận hành vẫn tất định). Phản ví dụ
CE-1…CE-6 ở kế hoạch §5.3.

### 7.2 Tương ứng lý thuyết (từ vựng, không phải kết quả tỉ số cạnh tranh)

`p_t = v_t + x_t + c_t`, `v_{t+1} = p_t` là dạng `s_{t+1} = s_t + w_t + u_t` của **điều khiển trực tuyến
với nhiễu** (Agarwal, Bullins, Hazan, Kakade & Singh, ICML 2019): cơ sở hành vi = phạt **nỗ lực điều
khiển**; cơ sở kết quả = phạt **dịch chuyển trạng thái** (gồm cả nhiễu). SOCO (Chen, Goel & Wierman, COLT
2018) và hệ nhiệm vụ metric (Borodin, Linial & Saks, J. ACM 39(4) 1992) không có trôi ngoại sinh nên hai
cơ sở trùng nhau.

### 7.3 Định vị văn liệu (tóm tắt — đầy đủ ở kế hoạch §5.5)

| Công trình | Khác RideBound ở đâu |
|---|---|
| Fielbaum & Alonso-Mora 2020 | chỉ đo bất ổn; kịch bản đóng băng nhị phân ≈ họ `C` với `κ = 0` |
| **Elmi và cs. 2026** | bảo đảm bằng **cấm tuyệt đối** cho một nhóm + phân phối lại gánh nặng; mạng tĩnh nên không có phần trôi dạt để tách |
| **Schulz & Pfeiffer 2026** | hạn chót `l` tính từ lời hứa đầu = họ `M⁺`; có thể vô nghiệm dưới trôi dạt bất lợi. ⚠️ Chưa đối chiếu giả thiết thời gian di chuyển trong toàn văn trước khi phát biểu Hệ quả 4.1 "về bài của họ" |
| Sharif Azadeh 2022 | hộp tĩnh, gần họ `M` |
| Zalesak và cs. 2025 | ổn định **bộ giải**, không phải lời hứa ("LRP" = *Limit and Recall Prefix*; `freez` xuất hiện 0 lần) |
| Sivagnanam 2026, Haferkamp 2024, Schmidt và cs. 2026 (TSP-SC), Ackermann & Rieck 2025 | không có sổ cái cộng dồn, không quy trách |
| *Anticipatory walking* 2026 (TR-C, S0968090X26001336) | cơ chế no-worse so với lịch tham chiếu cho **một** lần cập nhật — làm hẹp claim "no-worse"; ⚠️ chưa đọc toàn văn |

### 7.4 Được tuyên bố (theo tổ hợp `docs/03` đã khóa: per-passenger + path-dependent + multi-dimensional
+ cumulative/switch budget + multi-epoch rolling insertion + machine-checkable certificate), cộng thêm:

1. Phân rã `v/e/p` bằng một **phản thực khả thi** (`e` là phương án có thật trong tập lựa chọn).
2. **Định lý 4 bản có điều kiện** + Hệ quả 4.3. Mức claim theo tiến độ: trước Tầng 2 *"chứng minh +
   giải thích hậu nghiệm"*; sau 2A *"xác nhận cơ chế có đối chứng"*; sau 2B *"xác nhận trên tập giữ lại,
   cả hai chiều trôi"*.
3. Bảo đảm có mức cho mọi khách — trái với nhận định của Elmi rằng bảo đảm chỉ có khi cấm tuyệt đối.

### 7.5 KHÔNG được tuyên bố (❌) — tổng hợp

- Lần đầu có bảo đảm ETA từng khách / lần đầu kiểm soát bất ổn — Elmi 2026.
- Chặn tổng biến thiên là điểm phân biệt — Mệnh đề 2.
- `B = A + d` là đẳng thức. `d` là tác động thuần của giao thông.
- Trì hoãn cam kết, least-commitment, time consistency, dynamic insertion, ETA limit, reassignment, route
  similarity, user satisfaction là mới.
- Vượt trội về tỉ lệ phục vụ (mọi cấu hình có cam kết phục vụ ít hơn).
- Mạnh hơn Fielbaum 2020; "tốt hơn 585 lần"; so số tuyệt đối với văn liệu.
- Gini cho gánh nặng nhiều số 0; khoảng tin cậy tính trên số khách.
- Kết quả trên "mạng đường Manhattan"; kết quả trôi dạt "đã được kiểm chứng" (chưa qua verifier).
- Dùng "+7,1 pp của Zalesak" để bù "−7,13 pp".
- "Hệ thống dùng cổng hành vi không bao giờ kẹt / vô nghiệm".
- Gọi 9 ô k=1 hay kiểm hồi tố 4/4 là "xác nhận".
- Giá trị p McNemar làm bằng chứng chính của Tầng 2.
- Sổ cái "chỉ tính phần gây hại" là mới.
- Chứng minh Định lý 4 là khó/sâu.
- "Cận dưới" khi so với baseline cho đổi xe; trôi dạt trên panel chính là "cận dưới" chỉ được nói kèm giải thích.

---

## 8. Kế hoạch — tóm tắt và trạng thái (chi tiết: `KE-HOACH-HOP-NHAT-2026-09-23.md` §6)

### 8.1 Bốn tầng — dừng ở tầng nào cũng có khóa luận hoàn chỉnh

| Tầng | Nội dung | Lần chạy | Trạng thái |
|---|---|---|---|
| **0** | Sửa hồ sơ LaTeX (T0.2.1–T0.2.11) | 0 | T0.1 xong; T0.2.* **chưa làm** |
| **1** | Phân tích bổ sung trên dữ liệu niêm phong | 0 | T1.1–T1.11, T1.13, T1.14 **xong** (script có); **T1.12 chưa viết** |
| **2** | Thí nghiệm xác nhận Định lý 4: **2A** (panel A, 20 ô, `dl-30/60/120` × k∈{0,1}) + **2B** (panel phát triển 16 ô, k=1, `conduct-30`, `visible-30`, `dl-30`, `dl-120`, `dl2-30`) | ~240 | **đã bắt đầu ở phiên `ridebound-ef`** (24/09): worktree đã tạo, đang lập baseline; chưa sửa mã. Các quyết định cổng đã giải quyết ở §2.1 và §10 |
| **3** | Lõi nhận biết thất bại + thế giới ngẫu nhiên + conformal theo episode | nhiều | chỉ khi Tầng 2 có tín hiệu; **hỏi người dùng trước khi bắt đầu** |
| **4** | Thiết kế lại đối tượng lời hứa (WP15) | — | bài báo riêng, chờ ADR |

### 8.2 Tầng 0 — việc còn lại (đọc kế hoạch §6 Tầng 0 cho nội dung đầy đủ)

- **T0.2.1** Định vị Chương 1 quanh Elmi 2026 và Định lý 4 (bỏ câu kiểu "Fielbaum 2020 kêu gọi… khóa luận
  trả lời"; dựng không gian thiết kế 4 họ; mốc thời gian Elmi).
- **T0.2.2** Thêm Định lý 4 (bản Sửa đổi 1, đủ 4 yếu tố: (N) + 11/20 ô; tách (a)/(b); Hệ quả 4.3; câu
  "chứng minh sơ cấp"), Mệnh đề 2, bảng phản ví dụ vào Chương 3, ngay sau `\begin{hequa}[Dải khác biệt
  rộng tối đa $d$]…\end{hequa}`. `cellpred` và kiểm hồi tố vào Chương 4 với nhãn hậu nghiệm/hồi tố.
- **T0.2.3** Kết nối lý thuyết (§7.2) vào Chương 2.
- **T0.2.4** Hạn chế mới vào `muc:hanche` (bao đóng metric OD; một snapshot thời gian; trôi dạt vô hướng,
  chưa qua verifier; nhánh hành vi chết 11/20 ô vì `Board()`).
- **T0.2.5** Sửa bảng thứ tự hàm mục tiêu và giải thích "mức C trơ" ở `muc:dathu`.
- **T0.2.6** Đổi khung §8.5/8.6 thành "phép đo độ mỏng tập lựa chọn", mẫu số đúng 73,84%.
- **T0.2.7** Bỏ chữ "cận dưới" khi so với baseline cho đổi xe.
- **T0.2.8** Sửa trích dẫn: arXiv:2504.10649 là Zalesak, Hu & Samaranayake 2025; DOI hoán đổi giữa
  time-consistent DARP (`10.1002/net.22063`) và multiple-plan DARP (`10.1007/s00291-025-00809-y`); ⚠️ đối
  chiếu mục `gerzinic2023` (tiêu đề đang trùng bài Molenbruch, Braekers & Caris).
- **T0.2.9** Thêm tài liệu tham khảo: Elmi 2026; Schulz & Pfeiffer 2026; Sivagnanam 2026; Haferkamp 2024;
  Schmidt 2026; Zalesak 2025; Agarwal 2019; Chen–Goel–Wierman 2018; Borodin–Linial–Saks 1992.
- **T0.2.10** Tên CBHD — **hỏi người dùng**.
- **T0.2.11** Sổ cái "chỉ tính phần gây hại" vào Chương 5 (4 ý; đọc toàn văn *anticipatory walking* trước).

⚠️ Những đoạn Tầng 0 nói về **kết quả Tầng 2** (ví dụ câu T2.10) chỉ viết **sau** khi Tầng 2 có kết quả.
Trước đó, Chương 4 chỉ có bảng hậu nghiệm với nhãn đúng.

### 8.3 Tầng 2 — quy trình thực thi (tóm tắt; đặc tả đầy đủ và mã mẫu ở kế hoạch T2.0–T2.10)

1. **Worktree:** `cd E:\Code\RideBound` → `git worktree add ..\RideBound-deadline -b research/deadline-gate 41a4e11`.
   Mọi sửa đổi trong `E:\Code\RideBound-deadline`. Không đụng cây chính.
2. **Baseline trước khi sửa:** trong worktree chạy `dotnet test RideBound.slnx`, **ghi số test pass/fail**.
   Nếu đỏ đúng test `StrictBagItBundleTests` kỳ vọng `GitDirty = true` (📎 theo Codex) — xác nhận trên cây
   chính là hiện tượng có sẵn, ghi lại, **không sửa test**.
3. **Sáu thay đổi mã (T2.1):**
   (1) `CommitmentVector.cs` — mã `DeadlineExceeded`, `SafetyNoOpRejected`;
   (2) `CommitmentPolicy.cs` — tham số tùy chọn `dropEtaDeadlineSlack`, `dropEtaDeadlineTwoSided` (+ kiểm
   "two-sided cần slack");
   (3) `CommitmentLockEvaluator.cs` — tham số `anchor` (lời hứa đầu), witness `deadline_cap` /
   `deadline_floor`, ném lỗi khi thiếu anchor;
   (4) `CommitmentDecisionValidator.cs` — truyền `Entries[0]` (kiểm `Kind == InitialPromise`), ánh xạ
   witness với thông điệp riêng;
   (5) `CommitmentPolicyConfiguration.cs` — khóa `dropEtaDeadlineSlackMs`, `dropEtaDeadlineTwoSided`;
   (6) `HardVectorCandidateAssessor.cs` — **chỉ chẩn đoán**: fail-closed trích lý do của **no-op** nếu có;
   no-op bị loại mà còn phương án khác ⟹ lỗi `SafetyNoOpRejected` có kiểu (hôm nay trạng thái này chết
   muộn với `SOLVER_MODEL_MAPPING_FAILED`, nên không đổi lần chạy thành công nào).
   ⚠️ Grep xem `CommitmentPolicy` có bị tuần tự hóa vào checkpoint/canonical state không
   (`OnlineStateCanonicalizer.cs`, `OnlineStateCheckpointCodec.cs`) — xác nhận, đừng giả định.
4. **Test (T2.2):** 6 tệp test, ca (a)–(k) cho lock evaluator, policy, configuration, EffectivePolicy
   fairness (B1–B4 không nhận hạn chót — bẫy `EffectivePolicies`), validator, assessor (đường K20 và
   fail-closed có no-op). Chạy `dotnet test RideBound.slnx` sau **mỗi** thay đổi.
5. **Review:** xem §9 (bắt buộc).
6. **Build runner:** `dotnet publish src\RideBound.Runner\RideBound.Runner.csproj -c Release -o E:\RideBoundData\research\runner-deadline-v1`; đối chiếu bố cục với `h6-confirmatory-v1`; gốc publish không được đổi trong lúc chạy.
7. **Hai đối chứng (T2.4):** `ctl-conduct-k0` (20/20, số khách nhận trùng `wp14/drift-v1`) và
   `ctl-visible-k0` (đúng 4 ô vô nghiệm đã biết). So **quyết định** bằng `levelc/decision_identity.py`,
   so **nhãn và tập ô**, không so văn bản thông điệp. Lệch quyết định dù một ô ⟹ **dừng, điều tra**.
8. **Script scratchpad** trong `ridebound-scratchpad/deadline/` (chưa tồn tại): `preflight_drift_v2.py`
   (đọc mốc khung từ `RB_DRIFT_WINDOW_START_SECONDS`, chỉ nhận 28800/61200) + `check_preflight_v2.py`
   (lịch v2 trùng v1 ở 28800 cho cả 7 ngày); `run_deadline.py`; `holdout_predict.py`; `classify.py` + test.
   **Không sửa `drift/preflight_drift.py` gốc.**
9. **Thứ tự chạy:** đối chứng (40) → **chạy thử 1 ô tối** `d20181112-s10-r1-w17` `conduct-30` k=1 (kiểm
   hệ số đúng khung, không lỗi đến sớm) → 2B `conduct-30` 16 ô → **dự đoán theo ô cho cả 2A và 2B bằng
   `holdout_predict.py` + niêm phong** `PREREGISTRATION.md` + `predictions.csv` + SHA-256 + giờ UTC → 2A
   `dl-30/60/120` (120) → 2B còn lại (64, hoặc 80 nếu thêm `dl-60`).
10. **Phân loại (T2.7)** theo hằng thông điệp trong mã; nhãn `selection-noop-invariant` xuất hiện ⟹ lỗi
    cài đặt, dừng. Không bao giờ đếm lỗi thay cho phân loại lỗi.
11. **Phân tích (T2.9):** bằng chứng chính = bảng **dự đoán – kết cục theo ô**; phụ = trần khả thi nhỏ
    nhất theo ô; McNemar chỉ mô tả; hình trung tâm sáng/tối × 4 họ.
12. **Ngưỡng (đã chốt, không đổi sau khi xem kết quả):** 2B "xác nhận trên tập giữ lại" khi dự đoán theo
    ô đúng ≥ 90% cặp ở khung tối **và** hàng `w17` của bảng hướng đúng; phủ định khi < 75%, hoặc `dl-30`
    tối vô nghiệm do `deadline-late` ≥ 3/8, hoặc `dl2-30` và `visible-30` tối cùng ≤ 2/8. Luật diễn giải
    khi dự đoán theo ô đúng mà bảng hướng sai: *"Định lý 4 đúng theo ô, nhưng khung tối thật không đủ
    thuận lợi để hạn chót một chiều an toàn"*.
13. **Sau khi xong:** cập nhật `docs/18`, `docs/19` và một decision entry **trong worktree/nhánh
    `research/deadline-gate`** (theo `AGENTS.md`), gắn nhãn **thăm dò**; viết kết quả vào Chương 4 theo
    mẫu câu T2.10; hạ claim nếu không đạt ngưỡng. **Không commit/push** khi chưa hỏi người dùng.

Ước lượng: mã 1,5–2 ngày, test 1–1,5 ngày, runner + đối chứng 0,5–1 ngày, chạy 5–8 giờ tính toán (6 luồng,
~11 phút/ô), phân tích 1–1,5 ngày. Dung lượng ~5–15 GB. Nếu chỉ đủ một nửa: làm đối chứng + 2B trước
(120 lần, ~2–8 GB).

### 8.4 Tầng 1 — việc còn lại

**T1.12 — Phủ định C1 của WP15** (bắt buộc theo `docs/tasks/47` §2 trước khi cài trục C): đọc
`payload.solver.executionEvidence.prunedCandidates[].commitmentWitnesses[]` có `code ==
"COMMITMENT_PHASE_LOCK"`; lấy `simTimeMs` của khung và `promise.pickupEtaMs` của khách bị witness; vẽ phân
bố `pickupEta − simTime`; chạy trên bundle panel phát triển (không trên panel H6); nếu prune do khóa không
tập trung gần giờ đón ⟹ trục C vô hiệu, ghi kết quả âm. ⚠️ Đọc transcript: mỗi dòng
`{"frameBase64": "..."}` → base64 → JSON; lọc `messageType == "decision"`; thời điểm ở `frame["simTimeMs"]`;
id trong `run-00.json` là `req-<32hex>`, trong transcript là `rq-<64hex>` — không so trực tiếp (bẫy 12.3).

---

## 9. Giao thức chống ảo giác và bảo đảm chất lượng — BẮT BUỘC cho mọi bước

### 9.1 Trước khi viết mã hoặc văn bản

1. Đọc tệp đích (đúng vùng liên quan) **trong phiên hiện tại**. Grep lại mọi số dòng lấy từ kế hoạch.
2. Kiểm mọi giả định của đặc tả trong mã thật: tên kiểu, chữ ký hàm, thành viên có tồn tại không (ví dụ
   `InsertionCandidate.IsNoOp`, `CandidatePruneWitness.Code/Message/CandidateId`, chữ ký
   `CommitmentValidationWitness`, biến `witnesses` trong `CommitmentLockEvaluator.Evaluate`). Mã mẫu trong
   kế hoạch là **phác thảo đã đối chiếu với mã lúc lập kế hoạch**, không phải mã đã biên dịch — nếu lệch,
   theo mã thật và ghi lại chỗ lệch.
3. Viết ra (trong ghi chú làm việc) các bất biến phải giữ: mặc định tắt; B1–B4 không đổi hành vi; ranh
   giới `>` chứ không `≥`; một chiều không bắt `candidate < anchor`; no-op của cổng hành vi không bao giờ
   bị loại; thay đổi 6 không đổi lần chạy thành công nào.

### 9.2 Khi viết mã

- Theo thành ngữ của tệp xung quanh: mật độ chú thích, cách đặt tên, cách ném lỗi (`ArgumentException`
  ở Domain; `InvalidDataException` ở cấu hình Runner), tiếng Anh trong mã.
- Viết test **cùng lúc hoặc trước** mã. Mỗi ca biên (bằng ngưỡng, ngưỡng + 1, âm, null) có test riêng.
- Chạy test mục tiêu trước (`dotnet test <project> --filter <tên lớp>`), rồi **toàn bộ**
  `dotnet test RideBound.slnx`. Ghi số pass/fail/skip và so với baseline bước 2 của §8.3.
- Không đổi test hiện có để nó xanh. Không dùng `--no-verify`, không tắt analyzer.

### 9.3 Review sau mỗi thay đổi có ý nghĩa

1. `git diff` trong worktree — đọc lại **từng dòng**, đối chiếu đặc tả T2.1.
2. **Review độc lập:** giao diff + đặc tả cho một subagent **ngữ cảnh mới** (không đưa kết luận của mình)
   với yêu cầu tìm lỗi logic, ca biên thiếu, vi phạm bất biến, sai dấu, sai ranh giới, đường mã chưa test,
   rò rỉ thay đổi sang B1–B4. Xử lý từng phát hiện; phát hiện nào bác bỏ thì ghi lý do.
3. Kiểm logic bằng tay trên các ca số của kế hoạch (CE-1…CE-6, ca (a)–(k) của T2.2).
4. Chỉ đi tiếp khi: test xanh (trừ ngoại lệ đã xác nhận), review không còn phát hiện mở.

### 9.4 Khi chạy mô phỏng và phân tích

- Đối chứng runner **trước** mọi nhánh mới; lệch là dừng.
- Kiểm tái lập script trước khi dùng (chạy lại một kết quả đã biết, ví dụ `harmledger.py`, `cellpred.py`
  phải ra 54…102).
- Mọi lần chạy hỏng: mở `failure-00.json`, phân loại theo hằng thông điệp, không đoán.
- Niêm phong tiền đăng ký **trước** khi chạy nhánh được dự đoán. Không đổi ngưỡng, khung, ô, sau khi xem.
- Báo tiến độ mỗi giờ khi job dài đang chạy; lưu kết quả trung gian ra tệp, script có chế độ `"reused"`
  để chạy tiếp khi bị cắt ngang.

### 9.5 Khi viết khóa luận

- Mỗi câu có số phải truy được về §6 của tài liệu này, kế hoạch, hoặc kết quả mới có script.
- Build LaTeX sau mỗi lần sửa; kiểm `main.log` không còn "undefined references"/"Reference … undefined"
  (không có pdftotext trong máy); kiểm không câu nào trong danh sách ❌ (§7.5) xuất hiện.
- Dùng công cụ Write/Edit cho văn bản tiếng Việt, **không** dùng heredoc bash.

---

## 10. Quyết định còn mở — mặc định đã chọn cho phiên sau

| Quyết định | Mặc định | Lý do |
|---|---|---|
| Sửa mã RideBound | **Được**, chỉ trong worktree `E:\Code\RideBound-deadline`, nhánh `research/deadline-gate` từ `41a4e11` | Người dùng giao AI quyết (23/09); worktree bảo vệ thay đổi chưa commit ở cây chính |
| Thăm dò hay chính thức | **Thăm dò có đối chứng và tiền đăng ký** | WP14R `009..012` còn `UNAUTHORIZED`; chế độ chính thức cần ADR + builder freeze (kế hoạch §7.2) |
| Dung lượng | Được vượt 30 GB; giữ E: ≥ 40 GB và C: ≥ 50 GB trống; **không xóa gì** | Chính sách mới §2.1 |
| Có chạy `dl-60` ở 2B | Có, nếu dung lượng còn thoải mái (+16 lần) | Cho trần khả thi nhỏ nhất mịn hơn |
| Có chạy `dl2-30` ở 2A | Không | Buổi sáng Hệ quả 4.3 đoán `dl2` ≈ `dl` |
| Commit / push | **Hỏi người dùng** | Thao tác ngoài phạm vi đã giao |
| Tên CBHD | **Hỏi người dùng** | Chỉ người dùng biết |
| Tầng 3 | **Hỏi người dùng** sau khi có kết quả Tầng 2 | 4–10 tuần công |
| Thứ tự làm | Tầng 0 phần không phụ thuộc Tầng 2 → T1.12 → Tầng 2 (2B có thể trước 2A) → cập nhật Chương 4 bằng kết quả Tầng 2 | Tầng 0–1 rẻ và bịt lỗ phản biện ngay |

---

## 11. Bẫy kỹ thuật — tổng hợp (đọc trước khi chạy bất cứ gì)

**Từ bàn giao 16/09 (§12):** 12.1 chọn sai bộ cấu hình cho runner; 12.2 `op_max_wait_time` kẹp cửa sổ;
12.3 id không khớp giữa run và transcript; 12.4 đếm lỗi thay vì phân loại lỗi; 12.5 đoán tên trường trong
bằng chứng; 12.6 heredoc bash làm hỏng chuỗi tiếng Việt; 12.7 `semanticHash` khác ≠ quyết định khác (so
bằng `decision_identity.py`); 12.8 thư mục đầu ra dở dang chặn lần chạy lại / tiến trình mồ côi; 12.9 đánh
số mục tay trong LaTeX; 12.10 các dự đoán sai đã ghi nhận.

**Từ kế hoạch (§7.4, N1–N14):** N1 tin prose "`decisionDelta` một chiều"; N2 gọi `d` là "do giao thông";
N3 nhánh mới rơi vào nhánh mặc định của `EffectivePolicies` (`SolverBackedRidePoolingPolicy.cs:396-410`) và
âm thầm chạy không ràng buộc; N4 cổng loại no-op làm hỏng run; N5 đổi `policyId` (preflight hard-code
`wp6-synthetic-policy-overlay-v1` ở `actual_fleetpy_medium_preflight.py:189`, `:234`); N6 chạy verifier
medium lên lần chạy có trôi dạt; N7 test `GitDirty` trên worktree sạch; N8 heredoc tiếng Việt; N9 Gini;
N10 CI theo số khách; N11 đọc "First rejection" như lý do của no-op; N12 chạy ô tối bằng
`preflight_drift.py` gốc (mốc 28800 hard-code ở dòng 73 ⟹ áp hệ số sáng lên ô tối, **không báo lỗi**); N13
gọi hậu nghiệm là "xác nhận"; N14 suy dự đoán tối từ tỉ số khung.

**Môi trường (phiên này vấp):**
- `python` không có trong PATH của Git Bash — dùng `E:/RideBoundData/wp7/envs/fleetpy-1.0.2/python.exe`.
- In tiếng Việt từ Python: console cp1252 ⟹ `UnicodeEncodeError`; đặt `PYTHONIOENCODING=utf-8`.
- Công cụ Bash reset thư mục làm việc về `e:\Code\RideBound` sau mỗi lệnh — luôn dùng đường dẫn tuyệt đối.
- `du -sh E:/RideBoundData` chạy quá 5 phút — dùng `Get-PSDrive` trong PowerShell để xem dung lượng trống.
- Công cụ Edit đòi đã Read tệp trong phiên.
- `preflight_drift.py` trỏ cứng `REPO = E:/Code/RideBound` (dòng 65) và `TARGET` (dòng 66) — chạy từ
  worktree phải dùng **bản sao** đã sửa hai hằng này (`preflight_drift_v2.py`).
- Không có poppler/pdftotext — kiểm LaTeX qua `main.log`.
- **Worktree mới bị CRLF** (phát hiện bởi phiên `ridebound-ef`): `core.autocrlf=true` của hệ thống làm các
  tệp `*.ndjson/*.hex/*.py/*.csv/*.txt` thành CRLF ⟹ test so byte vàng đỏ (6/908 lúc đầu). Cách sửa:
  `ridebound-scratchpad\deadline\restore_index_bytes.py` (ghi đúng byte blob trong index, kiểm bằng
  `git hash-object --no-filters`). Sau đó `git status` hiện ~147 dòng `M` chỉ là thẩm mỹ — xem thay đổi thật
  bằng `git -c core.autocrlf=false diff`. Chi tiết ở ghi nhớ `ridebound-env-traps`.
- Sau khi khôi phục byte, baseline worktree còn 1 test đỏ ở `RideBound.Benchmarking.Tests` (148 test) — theo
  ghi nhớ là `StrictBagItBundleTests` đòi `GitDirty == true` (dòng 32) hoặc
  `PublicDerivativeMechanicalDrainConversationTests` vượt thời gian CPU khi build lạnh/song song. Phải xác
  định đúng test nào trước khi coi là baseline.

---

## 12. Những việc KHÔNG làm

- Không authorize `RB-WP14R-009..012`, không authorize WP15, không mở H7.
- Không sửa cây làm việc chính của kho; không sửa `docs/18`, `docs/19` ở cây chính.
- Không đổi margin, panel, mẫu số, factor level hay failure treatment đã tiền đăng ký.
- Không lấy tham số số học từ văn liệu để đặt mức cho nhánh; không dùng số H6 để chọn tham số nhánh mới.
- Không tuyên bố RideBound tốt hơn/nhanh hơn/tương đương công trình nào.
- Không đề xuất lại tám hướng đã chết (bàn giao 16/09 §8) nếu không có bằng chứng mới.
- Không xóa tệp nào; không đụng báo cáo thực tập; không thêm lại mục 4–7 của báo cáo tiếng Việt cũ.
- Không sửa khiếm khuyết `worst-hard-utilization-ppm` trong Tầng 2 (K12).

---

## 13. Đoạn dán vào đầu phiên mới

> Tôi là Trần Quang Thành (23020155, UET/VNU), đang làm khóa luận về RideBound — hệ điều phối xe đi chung
> có "lời hứa có biên được chứng nhận". Trước khi làm bất cứ việc gì, hãy đọc **toàn bộ**
> `E:\Code\Report_INT3508\BAN-GIAO-PHIEN-2026-09-23.md`, rồi đọc đủ **nhóm A** trong §0 của tệp đó
> (`AGENTS.md`, `docs/00`, `docs/01`, `docs/18`, `docs/16`, `docs/03`, `docs/tasks/47`, và toàn bộ kế hoạch
> `E:\Code\Report_INT3508\KE-HOACH-HOP-NHAT-2026-09-23.md`). Sau đó thực hiện kế hoạch **từng bước** theo
> §8 và §10 của tệp bàn giao, tuân thủ tuyệt đối §2 (ràng buộc) và §9 (giao thức chống ảo giác: đọc mã
> trước khi viết, test sau mỗi thay đổi, review độc lập, báo cáo trung thực). Không bịa bất cứ thứ gì;
> chưa kiểm thì ghi "chưa kiểm". Không xóa tệp nào. Báo tiến độ mỗi giờ khi có job dài. Hỏi tôi trước khi
> commit/push, trước khi bắt đầu Tầng 3, và để lấy tên cán bộ hướng dẫn. Trả lời tôi bằng tiếng Việt, giải
> thích đơn giản kèm ví dụ thật từ hệ thống.
