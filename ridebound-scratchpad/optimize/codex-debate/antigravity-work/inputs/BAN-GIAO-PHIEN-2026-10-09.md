# BÀN GIAO PHIÊN 2026-10-09: RideBound (khóa luận) + tranh luận với Codex

> **Phiên mới đọc tệp này TRƯỚC TIÊN.** Tệp thay cho các bàn giao cũ (`BAN-GIAO-PHIEN-2026-09-29.md`,
> `-09-23.md`), nhưng các quy tắc trong đó vẫn còn hiệu lực.
>
> Mọi con số dưới đây đều có script và output lưu lại; đường dẫn ghi kèm. Chỗ nào chưa tự kiểm thì ghi rõ
> "⚠️ chưa tự kiểm".
>
> **Tóm tắt một dòng:** lõi khóa luận (luật C + hứa theo dự báo + sổ cái ba phần) đã có kết quả vững và đã kiểm chéo.
> Phiên trước tranh luận nhiều vòng với Codex để kiểm tra, tìm hướng tối ưu và xác định ranh giới đóng góp. **Chưa
> sửa luận văn**; mọi thay đổi luận văn đều cần chủ nghiên cứu duyệt.

---

## 0. Bắt đầu nhanh cho phiên mới

**Đọc theo thứ tự:**
1. Tệp này.
2. `ridebound-scratchpad/optimize/codex-debate/DEBATE-LEDGER.md`: nhật ký 12 vòng tranh luận, tệp nào ở đâu.
3. `ridebound-scratchpad/optimize/codex-debate/JOINT-CONCLUSIONS-2026-10-07.md` và `AGREED-DIRECTION-2026-10-08.md`.
4. `ridebound-scratchpad/optimize/FORECAST-REPORT.md` và `ridebound-scratchpad/tang3/t38/T38-REPORT.md`: hai báo cáo
   kết quả chính.

**Hỏi chủ nghiên cứu muốn làm gì tiếp** (mục 8). Không tự chạy mô phỏng hay sửa luận văn.

**Trả lời** bằng tiếng Việt, câu tự nhiên, tránh thuật ngữ và chữ tắt, giải thích đơn giản kèm ví dụ thật từ hệ
thống. **Báo kết quả trước**; chỉ sửa luận văn khi được đồng ý.

---

## 1. Chủ nghiên cứu và các quy tắc bắt buộc

**Người dùng:**
- Trần Quang Thành, MSSV 23020155, K68I-IT2, UET/VNU. Khóa luận tốt nghiệp về RideBound.
- **Tên cán bộ hướng dẫn: CHƯA BIẾT.** Luôn hỏi, không bao giờ tự điền.

**Quy tắc chủ nghiên cứu đặt (giữ nguyên văn):**
- "Không bịa; chưa kiểm thì ghi 'chưa kiểm'. Không xóa tệp nào."
- "Không đụng cây chính E:\Code\RideBound và không đụng báo cáo thực tập."
  - Báo cáo thực tập gồm `main.tex`, `noi-dung/`, `Baocaothuctap_*` ở gốc `E:\Code\Report_INT3508`.
- "Không sửa, build hay ghi fixture trong worktree mà job đang dùng (E:\Code\RideBound-deadline)."
- "Output mới để ở ổ C:."
- "Chỉ chạy job dài khi cắm sạc; báo tiến độ mỗi giờ."
- "Niêm phong dự đoán trước khi chạy."
- "Mỗi con số đưa vào luận văn phải có script và output lưu lại."
- "Không commit kho luận văn."
- "Trả lời tôi bằng tiếng Việt, câu tự nhiên, tránh thuật ngữ và chữ tắt, giải thích đơn giản kèm ví dụ thật từ hệ
  thống."
- "Báo kết quả cho tôi TRƯỚC. Chỉ sửa luận văn khi tôi đồng ý."
- Hỏi trước khi commit/push.
- Không thêm lại mục 4–7 của báo cáo tiếng Việt cũ. Quy tắc này không áp dụng cho luận văn LaTeX.
- **Chủ nghiên cứu muốn MỘT hướng duy nhất.** Họ đã phàn nàn khi phiên trước mở quá nhiều nhánh. Mọi câu hỏi mới phải
  gắn vào câu chuyện chính (mục 3); đề xuất tối đa một bước tiếp theo.
- **Trước khi đề xuất chạy mô phỏng, phải xem kho dữ liệu đã chạy** (mục 7). Phiên trước đã đề xuất chạy lại thứ đã có
  (bậc thang WP14r) và bị nhắc.

**Ổ đĩa:**
- Giữ E: ≥ 40 GB trống và C: ≥ 50 GB trống. Ngày 2026-10-07, E: còn khoảng 41 GB, **sát ngưỡng**, nên output mới để
  trên C:.
- Không bao giờ xóa để lấy chỗ.

**Ghi nhớ dài hạn:** thư mục `C:\Users\quang\.claude\projects\e--Code-RideBound\memory\`, chỉ mục `MEMORY.md`. Các
tệp: user-profile, standing-constraints, disk-policy, rigor, handoff, focus-one-direction, data-inventory, env-traps.

---

## 2. Bản đồ thư mục, kho mã, dữ liệu, môi trường

| Thứ | Đường dẫn | Ghi chú |
|---|---|---|
| Luận văn LaTeX | `E:\Code\Report_INT3508\ridebound\` | Build: từ `ridebound\` chạy `..\tools\tectonic.exe -X compile main.tex --outdir . --keep-logs`. **Chưa sửa từ 2026-09-30** (lần cuối: bảng `bang:quet07`). |
| Cây chính RideBound | `E:\Code\RideBound` | **KHÔNG ĐỤNG**: có thay đổi chưa commit của chủ nghiên cứu |
| Worktree job | `E:\Code\RideBound-deadline` | Branch `research/tier3-failure-aware`; chỉ ĐỌC |
| Kho nghiên cứu | `C:\Code\RideBound-noworse` | Branch `research/tier3-no-worse`; commit mới nhất **761915c** (đã push). docs/18 và docs/19 cập nhật tới 2026-10-06; **chưa có kết quả 2026-10-07 → 10-09** |
| Scratchpad | `E:\Code\Report_INT3508\ridebound-scratchpad\` | `tang3/` (T3.x), `optimize/` (dự báo + tranh luận), `business-need/` (nguồn) |
| Tranh luận Codex | `ridebound-scratchpad\optimize\codex-debate\` | `claude-work/` (Claude ghi), `codex-work/` (Codex ghi), `ROUND*-CLAUDE.md` (đề), `ROUND*-CODEX*.md` (trả lời), `DEBATE-LEDGER.md` |
| Output chạy mô phỏng | `C:\RideBoundData\research\*` (T3.8: `tier3-t38-v1`; dự báo: `tier3-forecast-v1`; w07: `tier3-w07-v1`, `tier3-w07x-v1`) và `E:\RideBoundData\*` (wp7…wp14r) | |
| Fixture | `C:\RideBoundData\research\fixtures-panelA-v1`, `fixtures-w07-v1`, `fixtures-snow-v1`; WP14: `E:\Code\RideBound\benchmarks\fixtures\wp6\public\fleetpy-manhattan-v1\wp14-development-panel-v1\` (chỉ đọc) | |
| Dữ liệu FleetPy | `E:\RideBoundData\wp6\extracted\sha256\d9\d9e86f33…\FleetPy_Manhattan\` (demand, networks, `*_tt_factors.csv` 11–18/11/2018) | |
| Python mô phỏng | `E:/RideBoundData/wp7/envs/fleetpy-1.0.2/python.exe` | Luôn dùng `-B` và `PYTHONIOENCODING=utf-8`. **KHÔNG cài thêm gì vào env này** |
| Python học máy | `C:/RideBoundData/envs/ml-v1/Scripts/python.exe` | sklearn 1.7.2; danh sách gói: `claude-work/ml-v1-env-freeze-2026-10-08.txt` |
| Dữ liệu học máy | `C:\RideBoundData\research\ml-pilot-v1\` | `riders-2026-10-08.csv`, `riders-causal-2026-10-08.csv` (SHA 7075ad97…), `riders-causal-a1-2026-10-08.csv` |

**Kiểm thử bắt buộc khi đổi mã:** `dotnet test RideBound.slnx` (xem AGENTS.md). Phiên trước **không** đổi mã C#.

---

## 3. Câu chuyện khóa luận (MỘT hướng, đã thống nhất với Codex)

> Lời hứa giờ tới nơi cho khách đi chung bị lệch vì ba nguyên nhân, mỗi nguyên nhân xử lý ở đúng chỗ:
> 1. **Do hệ thống** ghép thêm khách → **luật C**: tổng các lần hệ thống dời giờ trả của mỗi khách ≤ B (đang dùng
>    30 s).
> 2. **Do tắc đường đoán trước được** → **hứa theo dự báo**: cộng sẵn mức tăng tắc đường (trung bình lịch sử theo
>    khung 15 phút) vào giờ hứa đầu.
> 3. **Do tắc đường bất ngờ** → **sổ cái**: ghi lại theo từng khách. Phần này không tự động được coi là "miễn trách".

**Ký hiệu** (đã kiểm ở `tang3/evidence/audit_vep.py:99-125`). Với mỗi lần sửa lời hứa:
- v = lời hứa đã công bố trước đó;
- e = kế hoạch cũ tính lại theo tốc độ mới;
- p = lời hứa mới;
- x = e − v là phần do tắc đường; c = p − e là phần do điều phối; z = p − v = x + c là phần khách thấy.

**Các luật đem so:**

| Luật | Định nghĩa |
|---|---|
| C-B | Σ\|c\| ≤ B (B = 30, 60, 120…) |
| U | Không có trần giờ trả, nhưng **vẫn khóa** xe, điểm đón và giờ đón khi xác nhận |
| FREE (b1-rolling-cost) | Không khóa gì |
| M⁺-B | p − p0 ≤ B: hạn chót tính từ lời hứa đầu, **không** cộng tắc đường. Đây là *thành phần* hạn chót theo kiểu Schulz & Pfeiffer 2026, KHÔNG phải phương pháp của họ |
| V-B | Σ\|z\| ≤ B |

**Gộp phần hệ thống với phần tắc đường thì ra luật cũ:** cộng có dấu Σ(c + x) chính là M⁺; cộng trị tuyệt đối
Σ|c + x| chính là V. Vì vậy "tính cả hai phần" không phải luật mới.

**Lời hứa được tính thế nào** (`C:/Code/RideBound-noworse/src/RideBound.Application/Scheduling/RouteScheduleProjector.cs:103-166`,
`PromiseProjector.cs:63-131`):
- Hệ thống chạy thử kế hoạch của xe từ vị trí hiện tại, qua các điểm dừng theo thứ tự, theo bảng tốc độ hiện tại.
- Giờ bắt đầu phục vụ tại điểm đón = max(giờ xe tới, giờ đón sớm nhất). Thời gian dừng = 0 (thiết lập của thí
  nghiệm).
- Lời hứa công bố lúc xác nhận đặt xe.
- Mô phỏng chạy đúng kế hoạch, nên sai số chỉ đến từ tắc đường đổi và hệ thống chèn thêm khách **sau** lúc hứa.

### Đóng góp được phép nhận (hẹp, đã thống nhất với Codex)

1. **Cơ chế:** ngân sách thay đổi do điều phối **cộng dồn theo từng khách**, kèm sổ cái tách v/e/p, đã cài đặt và kiểm
   chứng.
2. **Bằng chứng đo được:**
   - so với hạn chót: cùng số khách, nhưng không bao giờ phải phá luật;
   - so với ghép tự do: xóa phần trễ do ghép, với cái giá đo được về số khách.
3. **Phát hiện (thăm dò, trong mô phỏng):**
   - dưới luật C, lời hứa của chuyến đi chung trở thành bài toán đoán kẹt xe, nên một dự báo đơn giản là đủ;
   - luật C và dự báo **bổ sung nhau**, vì mỗi bên gỡ một nguyên nhân;
   - ở cùng độ dài lời hứa, "thay đổi ít hơn" cho lời hứa đáng tin hơn "dự đoán tốt hơn" (câu hỏi Fielbaum &
     Alonso-Mora 2020 để ngỏ). Không được nói quá: chi phí kiểm thực tế và số khách khác nhau.

### KHÔNG được nhận là mới

Theo `C:/Code/RideBound-noworse/docs/03-related-work-and-claim-boundary.md` và các bản khảo sát:
- chèn động, giới hạn ETA, gán lại, tương đồng tuyến, cam kết tối thiểu, nhất quán thời gian, hài lòng khách;
- hứa theo dự báo (Google, Uber DeeprETA, Ele.me, DoorDash, Lyft, lịch xe buýt TCRP 113, giờ bay);
- học máy đoán giờ đến;
- "độ dự đoán được là tham số thiết kế": Leonardi và cộng sự 2024, arXiv 2411.11899, PDF :1101, ✓ đã tự kiểm;
- học kết quả chuyến đi chung từ mô phỏng FleetPy: Ding, Dandl & Bogenberger, ⚠️ chỉ Codex đọc, trang chặn bot;
- cơ chế gần luật C: **Hörl & Zwick 2022, chiến lược B** (`claude-work/pdf/hoerl-zwick-2022.txt:527-539`, ✓). Đón
  thêm chỉ khi khách đang trên xe không bị trả muộn hơn "mức tối thiểu tuyệt đối với giao thông hiện tại". Khác luật
  C: chỉ áp cho khách sắp vi phạm, không cộng dồn, không có sổ.
- Schulz & Pfeiffer 2026 (`E:/RideBoundData/literature-survey-2026-10-06/notes/schulz-pfeiffer-2026-customer-oriented-darp.txt:386-416`, ✓):
  - thời gian đi **cố định**, không có tắc đường;
  - khách nhận lời mời với xác suất e^(−μ·RD), RD là độ đi vòng tương đối;
  - hạn chót l = 900 s, chọn 10–15 phút qua quét;
  - mục tiêu: tối đa khách nhận lời mời.

  Ta chỉ mượn thành phần hạn chót. Phát hiện của ta: không tắc đường thì M⁺ và C nhận **đúng cùng tập khách**
  (`tang3/sweep/SWEEP-REPORT.md:40`, 12/12); có tắc đường thì M⁺ bị ép, C thì không (mục 4.1). Vì vậy đóng góp là
  **tách nguyên nhân**, không phải "mang hạn chót sang thế giới có tắc đường".

---

## 4. Kết quả chính (số liệu + nguồn)

### 4.1 T3.8/T3.9: tắc đường thật, 34 ô kiểm, 3.672 yêu cầu

Nguồn: `tang3/t38/T38-REPORT.md`, kế hoạch niêm phong 78954a15…, γ 222,259 s; kiểm độc lập khớp 13/13.

**Số khách được chở:** U 2.434; **C-30 2.338**; M⁺-30 2.338; V-30 2.336; M⁺-60 2.347.

**Bị ép và tự phá lời hứa:**

| Luật | Quyết định bị ép | Khách bị chính luật phá lời hứa |
|---|---|---|
| C-30 | 0% | 0% |
| M⁺-30 | 41,3% | 14,5% (khung 7h: 36,5%) |
| V-30 | 53,8% | 21,6% |

**Hai kết luận theo quy tắc niêm phong:**
- **H3 ĐẠT:** 2/34 ô vượt γ, cả hai ở khung 7h. Độ phủ khung 7h chỉ 7/9; cận trên Clopper–Pearson 17,4%.
- **H2 ĐẠT:** C-30 = M⁺-30 về số khách; 0 quyết định non-normal.

**Giá của luật C so với U:** −96 khách, tức 2,6 điểm % số yêu cầu, hay 3,9% số khách U chở. Hai tập khách được chở
khác nhau 227 + 131 người. Với khách chung, thời gian ngồi xe ngắn hơn 10,5 s.

**Kinh nghiệm khách** (`tang3/t38/rider-experience-2026-10-05-report.txt`): C-30 và M⁺ giống hệt nhau. So với U:

| Chỉ số | U | C-30 |
|---|---|---|
| Trễ > 1 phút | 9,1% | 4,1% |
| Trễ > 5 phút | 0,77% | 0 |

**Phân bố trễ so với lời hứa đầu** (`optimize/report-extras/lateness-distribution-2026-10-06.txt`):

| Luật | > 1 phút | > 2 phút | > 5 phút | > 10 phút | Lớn nhất |
|---|---|---|---|---|---|
| U | 8,34% | 4,19% | 0,74% | 0,08% | 11 phút |
| C-30 | 3,25% | 0,47% | 0 | 0 | 3,9 phút |
| C-30 + dự báo | 0,43% | 0 | 0 | 0 | 1,9 phút |

### 4.2 Vì sao phút trễ nhỏ (không phải do dữ liệu)

Script và output đều ở `optimize/codex-debate/`.

**Thí nghiệm nhỏ và thưa:**
- Mỗi ô: 108 yêu cầu (khoảng 0,4% số chuyến thật trong 2 giờ), 8 xe chở 4 chỗ, 96 nút. Đón chờ tối đa 10 phút; ngồi
  xe tối đa 1,5 lần đi thẳng.
- Dừng đón trả 0 s (`service-duration-check`); bài FleetPy 2026 dùng 30 s (✓ PDF).
- Tải x = 0,81; trung bình mỗi xe chở **0,54 khách**, so với FleetPy 2026 cùng dữ liệu (21.400 yêu cầu, 180 xe) báo
  **≈ 1,33** (`claude-work/load-and-occupancy`).

**Tốc độ và chuyến đi khác thực tế:**
- Tốc độ nền lấy lúc 00:00 (`factor-anchor-check`). Thời gian mô phỏng so với thời gian đo được: 8h là 0,60–0,89;
  17h là 0,47–0,77; sáng cuối tuần là 1,23–1,55. Quy đổi lại thì hầu như không đổi kết luận.
- Chuyến được chọn ngắn hơn: trung vị 165 s so với 196 s; 49/49 ô (`selection-length-check`).

**Lời hứa đầu đã chứa sẵn chờ và đi vòng:** trung bình 14,1 phút; trễ thêm chỉ khoảng 0,3 phút.

**Rất ít khách bị ghép làm dời giờ** (`exposure-check`):
- Khách đi chung: U 22,8%, C-30 13,4%.
- Khách bị dời giờ trả: U 7,1% (77% trong số đó trễ); C-30 1,4%. Ở C-30, chỉ 1,24% bị cộng thêm; 4 người được trả
  sớm hơn.
- Mỗi lần dời: U trung vị 108,6 s; C-30 trung vị 8,3 s, lớn nhất 29,2 s.

**C-30 từ chối khách vì đâu** (`budget-block-diagnosis`):
- 148 yêu cầu bị chặn chỉ vì ngân sách; U chở 116 trong số đó. Mức vượt trung vị 110 s.
- Chỉ 2/148 ca là do ngân sách đã bị tiêu trước đó, nên thuật toán "tiết kiệm ngân sách" gần như không cứu được ai.

**Ngân sách theo độ dài chuyến** (sàng lọc bậc một, `proportional-budget-screen`): cùng mức trung bình 60 s cứu
30/148 khách (chia đều cứu 11); mức 120 s cứu 89 (chia đều 59). Đã chuyển sang mục hướng phát triển.

### 4.3 Bậc thang cam kết WP14r: tắc đường cố định, 16 ô khung 8h/17h, ngày 12–13/11

Nguồn: `claude-work/wp14r-ladder-reanalysis-2026-10-08.txt`; Codex tái lập khớp 30/30.

| Luật | Khách được chở | Đi chung | Bị dời giờ trả | Trễ > 1 phút | Trễ > 2 phút |
|---|---|---|---|---|---|
| FREE | 94,3% | 53,1% | 23,8% | 16,82% | 10,07% |
| LOCKS (= U) | 91,7% | 21,8% | 3,9% | 2,97% | 1,70% |
| C-120 | 90,5% | 19,4% | 2,6% | 1,47% | 0 |
| C-60 | 89,1% | 17,3% | 1,3% | 0 | 0 |
| C-30 | 88,8% | 15,7% | 0,4% | 0 | 0 |

Điểm gãy nằm giữa 60 và 120 s. **Bậc thang này đã có sẵn**, nên **không chạy lại**. Đây là đợt chạy cũ ngày
2026-09-05, bộ điều phối đời cũ.

### 4.4 Các mức trần đã quét

Đã quét ít nhất 6 lần: wp8 frontier, wp9 frontier-v1, wp14r v5/v6, tier3-sweep-v1, w07, w07x.

Ở khung 7h tắc đường thật (`tang3/w07x/W07X-REPORT.md:20-29`), tỉ lệ M⁺ bị ép theo ngân sách:

| Ngân sách | 30 s | 60 s | 90 s | 120 s | 180 s | 240–300 s |
|---|---|---|---|---|---|---|
| M⁺ | 58,6% | 35,5% | 13,0% | 6,6% | 2,8% | 1,7% |
| C | 0 | 0 | 0 | 0 | 0 | 0 |

**Chọn trần:** không có chuẩn ngành cho loại trần này (khảo sát S3).
- Ngưỡng khách quan tâm tính bằng phút: ứng dụng xe buýt OneBusAway, trung vị chịu sai 4–6 phút (✓).
- Biên thực tế "2 hoặc 3 phút" (Lu & Kühnel, ✓; là biên **giờ đón**, có tính tắc đường).
- Cách biện minh mạnh nhất: quét các mức rồi chọn điểm gãy. 30 s chỉ là mức thận trọng.

### 4.5 Hứa theo dự báo

Nguồn: `optimize/FORECAST-REPORT.md`, kế hoạch niêm phong a5524912…, commit 761915c.

**Họ A** (phát lại, C-30, 21 ô ngày thường): trễ > 60 s so với lời hứa đầu giảm **6,01% → 0,17%** (khung 7h:
14,44% → 0,27%). Lời hứa dài thêm 13,7 s. Đệm đều cùng giá chỉ đạt 1,94%; phép so này mang nhãn "mong manh", cluster-t
UB +0,07.

**Tách nguyên nhân bằng sổ cái:**
- sáng ngày thường: do điều phối 1,3%, đoán trước được 86,1%, bất ngờ 12,6%;
- tuyết (15/11 chiều): bất ngờ 92,5%, dự báo chỉ gỡ được 17,4% (7,19% → 5,94%).

**Luật C và dự báo bổ sung nhau:**

| Cách làm | Trễ |
|---|---|
| U | 9,72% |
| U + dự báo | 3,90% |
| C-30 | 6,01% |
| C-30 + dự báo | 0,17% |

Riêng khung 17h, U vẫn trễ 6,76% dù có dự báo. Dự báo cũng cho 0,17% với M⁺ và V, nên **không riêng C**.

**Họ B** (đưa dự báo vào bộ điều phối): bị bác.
- 3/32 lần chạy PLAN_INFEASIBLE.
- M⁺ tự phá lời hứa giảm 69%, nhưng bị ép vẫn 47,6%.

**Vấp khi đưa vào dùng thật:** 34/1.471 khách (2,3%) có lời hứa đón (theo dự báo) muộn hơn hạn đón tối đa, vì phép
kiểm khả thi vẫn dùng giờ không dự báo. Cuối tuần không có ngày nguồn để dự báo.

**Ví dụ một khách thật** (`optimize/report-extras/example-rider-2026-10-06.txt`), ô d20181115-s10-r1-w07:
- 7:11:56 đặt xe, được hứa 7:34:51;
- 7:22:30 xe tới đón;
- 7:38:02 tới nơi, trễ 190,5 s, do tắc đường lúc 7:15 và 7:30;
- hứa theo dự báo sẽ là 7:37:44, chỉ lệch 17,6 s.

### 4.6 Đệm lời hứa hay giới hạn điều phối ("sao không hứa dài ra?")

Nguồn: `claude-work/cap-vs-pad-frontier-2026-10-07.txt`, C-30, 34 ô gộp:

| Cách hứa | Lời hứa dài thêm | Trễ > 1 phút | Tới sớm > 1 phút |
|---|---|---|---|
| Không đệm | 0 s | 3,25% | 0,13% |
| **Theo dự báo** | **7,4 s** | **0,43%** | **0,17%** |
| Đệm đều 60 s | 60 s | 0,47% | 29% |
| Đệm đều 120 s | 120 s | 0,17% | 97% |
| Đệm đều 180 s | 180 s | 0% | 99,5% |

**Câu trả lời:** hứa dài thì hết trễ, nhưng lời hứa vô nghĩa (khách tới sớm hết) và dài hơn. Ngoài đời, giờ hứa dài
làm mất khách: DoorDash nói đoán quá dài "có thể khiến khách không đặt đơn" (theo khảo sát Codex); Schmidt và cộng sự
2026, arXiv 2609.11950, ⚠️ mới đọc phần tóm tắt. Mô phỏng không có mô hình khách bỏ đi.

**Kiểm ngoài mẫu theo thời gian** (kế hoạch niêm phong `claude-work/CALIB-BACKTEST-PLAN.md` 6175d2c1…; Codex khớp
60/60 dòng):
- **Đệm theo khoảng trống (room): BỊ LOẠI.** Dự đoán P1 sai; nó chỉ là đệm theo độ dài chuyến.
- Trên ngày 15–16/11:

  | Cách làm | Khách đúng giờ | Khách được chở | Lời hứa dài thêm | Tới sát giờ báo (±60 s) |
  |---|---|---|---|---|
  | C-30 + dự báo | 1.031 | 1.032 | 11–17 s | ~100% |
  | U + đệm | 1.031 | 1.061 | ~60 s | 67–84% |

### 4.7 Phép thử học máy: "dự đoán tốt hơn hay thay đổi ít hơn?"

**Kế hoạch:** `claude-work/ML-PILOT-SEALED.md` (SHA 93f6b968…), phiên bản chính xác Codex chấp nhận.

**Dữ liệu:** trạng thái xe lấy từ `projection.serviceOrder` của lời hứa đầu, đảm bảo không lộ thông tin tương lai.
- Có tắc đường (U, C-30): học 12–13/11 w07; hiệu chỉnh 14/11; kiểm 15/11 và 16/11.
- WP14r tĩnh: học 12/11 r1–r3; hiệu chỉnh 12/11 r4; kiểm 13/11.

**Mô hình:** HGB quantile 0.9 với tham số cố định, bản bỏ trạng thái xe, và hồi quy tuyến tính phân vị. So ở cùng độ dài
lời hứa E = 30 s, có điều kiện chặn.

**Kết quả** (`claude-work/ml-pilot-report-a1-2026-10-08.txt`):
- **ML1 ĐÚNG:** C-30 + dự báo đã 0%, học máy không thêm gì.
- **ML2 SAI:** với U, chỉ +0,69 / +0,00 điểm %, và điều kiện chặn trượt.
- **ML3 SAI:** với FREE, 12,89% → 11,65%, nhưng thêm 6,9% khách tới sớm.
- **ML4 ĐÚNG:** không mô hình nào đạt độ tin cậy của C-30.
- **ML5 SAI:** trạng thái xe không thêm gì.
- **Tiêu chí dừng đã kích hoạt.**

**Codex vòng 11:** tái lập khớp 95 dòng. Codex phát hiện **lỗi quy trình**: chưa loại 11 chuyến gốc trùng giữa phần học
và phần hiệu chỉnh (WP14r). Claude đã tự xác nhận (`provenance-overlap-check-2026-10-08.txt`): phần kiểm không trùng.
Phụ lục A1 (`ML-PILOT-AMENDMENTS.md`, viết sau khi có kết quả) loại 55 dòng rồi chạy lại đúng script: **mọi kết luận
giữ nguyên**.

**Được phép nói:** "mô hình học máy cố định, đặc trưng đơn giản, không cải thiện đáng kể; không mô hình nào đạt độ tin
cậy của luật C". **Không nói** "giảm thay đổi luôn thắng dự đoán".

### 4.8 Đường cơ sở mạnh từ bài báo (Codex vòng 12, `codex-work/STRONG-BASELINE-CODEX.md`)

**Phía luật điều phối:**
- **Đã có:** thành phần hạn chót kiểu Schulz & Pfeiffer (M⁺).
- **Đổi cấu hình là được:** kiểu UberX Share, "đón thêm không làm tăng giờ đến", gần luật C ngân sách 0 s (34 lần
  chạy).
- **Phải sửa mã lõi:** Hörl & Zwick B; Fielbaum & Alonso-Mora bản đầy đủ.

**Phía dự báo tắc đường:** chỉ có 8 ngày dữ liệu (11–18/11), nên chỉ phương pháp ít tham số là công bằng. Đối thủ được
chọn: **làm trơn hàm mũ có xu hướng tắt dần (Gardner & McKenzie 1985, ✓ PDF)**, chỉnh theo diễn biến trong ngày.
- Chỗ còn có thể cải thiện: ngày thường rất ít (0,17% so với khoảng 0% khi biết trước tắc đường thật); ngày tuyết
  nhiều.
- Giao thức: `codex-work/ROUND12-REPLAY-PROTOCOL-CODEX.md`.
- **CHƯA niêm phong, CHƯA chạy.**

---

## 5. Đính chính phải áp dụng khi viết (CHƯA áp dụng vào báo cáo, docs hay luận văn)

**Phạm vi và giới hạn:**
1. **M⁺** = hạn chót tính từ lời hứa đầu, không cộng tắc đường. Gọi là "kiểu Schulz & Pfeiffer (thành phần hạn chót)",
   không phải phương pháp của họ.
2. **Giới hạn mô phỏng phải nêu:**
   - tốc độ nền lúc 00:00 cho mọi ô;
   - chuyến chọn ngắn hơn;
   - dừng 0 s;
   - một hệ số tắc đường chung cho cả thành phố;
   - 108 yêu cầu/8 xe;
   - công cụ giới hạn 128 yêu cầu / 32 xe / 96 nút.
3. **Mức 30 s** không phải ngưỡng cảm nhận. `displayBucketWidthMs` là ngưỡng "thay đổi đáng kể", **không phải** cách
   hiển thị; lý lẽ "khách không thấy 30 s" đã bị rút. Trình bày trần như một điểm trên đường đánh đổi; điểm gãy khoảng
   60–120 s.

**Cách nói số liệu:**
4. Giá của luật C: "2,6 điểm % số yêu cầu (3,9% số khách của U)"; hai tập khách khác nhau 227 + 131 người.
5. "Đúng giờ" luôn phải đi kèm độ chính xác hai phía và tỉ lệ tới sớm.
6. Phần trễ do điều phối của U (73,4%) là kết quả của sổ cái, không phải quan hệ nhân quả.
7. Hiển thị C-30 trên 34 ô là 0,51% (trung bình theo ô; gộp theo khách là 0,43%). Con số 0,17% là trung bình theo ô
   của 21 ô có dự báo.
8. Lợi ích của dự báo không riêng luật C. Phần "đoán trước được" phụ thuộc vào dự báo đang dùng. Phần dư không tự động
   là "trễ được miễn" (49 CFR chỉ là tương tự).
9. Họ B chỉ đúng cho lớp bọc v1.3. Con số 108,6 s là trung vị của các lần dời khác 0.

**Trích dẫn:**
10. Via: sai số là của giờ **đón**; quan hệ với mức sử dụng là **quan sát**, không phải thí nghiệm.
11. Uber "Delayed Ride Guarantee" là **trả thêm cho tài xế**, tính từ đón tới trả, và **loại trừ chuyến đi chung**.
12. Điều 37.131: lần sửa nội dung 2016-10-17 theo API eCFR (Codex rút lại ý kiến phản đối).
13. Phải trích Hörl & Zwick 2022, Leonardi 2024 và Ding và cộng sự trong phần liên quan.

**Ký hiệu:**
14. v là "lời hứa đã công bố trước", **không phải** "lời hứa đầu chỉ bị dời bởi tắc đường". Bản gửi Codex vòng 1 từng
    viết sai câu này.

---

## 6. Làm việc với Codex

**Lệnh và phiên:**
- **Đường dẫn:** `$USERPROFILE/.vscode/extensions/openai.chatgpt-26.1002.51308-win32-x64/bin/windows-x86_64/codex.exe`
  (v0.162.0-alpha.2). Tiện ích tự cập nhật thì đường dẫn đổi; tìm lại bằng
  `find ~/.vscode/extensions -maxdepth 5 -path "*openai.chatgpt-*" -name codex.exe`.
- **Phiên tranh luận:** `01a11056-6e20-7ef1-b6e4-fe375272c630`. Phiên nhớ ngữ cảnh 12 vòng; nối tiếp bằng `resume`.
- **Model:** gpt-6.1-sol. Chủ nghiên cứu mới chuyển mức suy nghĩ từ **"ultra"** sang **"xhigh"**. Ultra tốn hạn mức,
  đã làm dừng 4 vòng.
- **Cấu hình Codex của người dùng mặc định là `danger-full-access`, approval never. LUÔN ghi đè sandbox.**
- **Sandbox Windows "elevated" ĐANG HỎNG** (`codex doctor`: "elevated Windows sandbox provisioning recorded a
  structured failure"). Mọi lệnh phải thêm `-c windows.sandbox="unelevated"`. Đã thử: đọc được, ghi ra ngoài thư mục
  `-C` bị chặn. **Không sửa** `~/.codex/config.toml` của người dùng.

**Lệnh mẫu** (chạy nền; Codex chỉ ghi trong `codex-work`):

```bash
CX="$USERPROFILE/.vscode/extensions/openai.chatgpt-26.1002.51308-win32-x64/bin/windows-x86_64/codex.exe"
D=/e/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate
W="E:/Code/Report_INT3508/ridebound-scratchpad/optimize/codex-debate/codex-work"
timeout 7200 "$CX" exec -s workspace-write -C "$W" resume -m gpt-6.1-sol \
  -c model_reasoning_effort="xhigh" -c windows.sandbox="unelevated" \
  -c web_search="live" -c sandbox_workspace_write.network_access=true \
  --skip-git-repo-check -o "$D/ROUNDnn-CODEX-final-message.md" \
  01a11056-6e20-7ef1-b6e4-fe375272c630 \
  "Round nn from Claude. Read E:/.../codex-debate/ROUNDnn-CLAUDE.md and do what it asks. Write only inside codex-work." \
  < /dev/null > "$D/roundnn-codex.log" 2>&1
```

- Chế độ chỉ đọc: thay bằng `-s read-only`. Với `exec resume`, đặt `-s` và `-C` **trước** `resume`.

**Quy trình đã dùng:**
1. Claude viết đề `ROUNDnn-CLAUDE.md` bằng tiếng Anh, có quy tắc: zero hallucination, trích `file:line`, output mode
   "x", không chạy mô phỏng.
2. Codex trả lời vào `codex-work/`.
3. Claude **tự kiểm** mọi con số và trích dẫn Codex dùng (script riêng, PDF lưu ở `claude-work/pdf/`).
4. Ghi vào `DEBATE-LEDGER.md`.
5. Sau mỗi vòng, rà soát mtime xem có tệp mới ngoài `codex-work` hay trong `E:\Code\RideBound`,
   `E:\Code\RideBound-deadline` không. Trước giờ đều sạch.

- Khảo sát độc lập: Claude dùng agent con, ghi vào `claude-work/SURVEY-S1…S4`; Codex ghi vào `codex-work/SURVEY-*`.
  Hai bên không đọc bài nhau cho tới vòng đối chiếu.
- **Hạn mức Codex** hết thì báo "try again at HH:MM". Người dùng có thể reset; nếu không thì hẹn giờ chạy lại.

**Tóm tắt các vòng:**

| Vòng | Nội dung |
|---|---|
| 1–3 | Phút trễ có ý nghĩa không, có phải do dữ liệu (`JOINT-CONCLUSIONS-2026-10-06.md`) |
| 4–6 | Khảo sát, ý tưởng, phản biện, kiểm ngoài mẫu (`JOINT-CONCLUSIONS-2026-10-07.md`) |
| 7–8 | Chọn trần, chế độ đi chung nhiều, chốt một hướng (`AGREED-DIRECTION-2026-10-08.md`) |
| 9 | Xác nhận bậc thang WP14r có sẵn; bỏ 102 lần chạy |
| 10–11 | Kiểm kê dữ liệu, khảo sát học máy, phép thử học máy + phụ lục A1 |
| 12 | Đường cơ sở mạnh từ bài báo (`STRONG-BASELINE-CODEX.md`) |

---

## 7. Kho dữ liệu đã chạy (BẮT BUỘC xem trước khi đề xuất chạy)

- **Kiểm kê:** `claude-work/data-inventory-by-experiment-2026-10-08.txt`, gồm 1.991 lần chạy, 51 thí nghiệm. Từng lần
  chạy: `data-inventory-runs-2026-10-08.tsv`; script `data_inventory.py` + `data_inventory_group.py`.
- Codex kiểm kê độc lập: `codex-work/DATA-AUDIT-CODEX.md` (1.991 + 17 lần chạy sau, + 40 lần hiệu chỉnh FleetPy).
- **Các đợt đáng nhớ:**
  - wp8 frontier: 128 yêu cầu, 4/8/16 xe;
  - wp9 confirmatory: panel A 8 xe, panel B **4 xe**, b1 tự do và c1 30 s;
  - wp9 frontier-v1: 141 lần;
  - wp14 drift, wide-window, surface;
  - wp14r v6: bậc thang;
  - tier3-sweep-v1: thế giới giả lập W0–W5, C/M⁺ 30–900;
  - w07, w07x, t38, forecast.
- Công cụ hiện tại đọc được bản ghi WP9 và WP14r.

---

## 8. Việc đang chờ: chủ nghiên cứu quyết định

Chưa có việc nào được duyệt chạy.

1. **(Đề xuất chính)** Phép so dự báo: **Gardner & McKenzie với trung bình lịch sử**.
   - Phát lại các chuyến C-30 có sẵn. Hiệu chỉnh 14/11; kiểm 15/11 và 16/11 khung w07/w08; ô tuyết w14/w15 là phép thử
     chuyển giao.
   - Cùng độ dài lời hứa 30 s; niêm phong trước.
   - Dự đoán: ngày thường hơn không quá 0,2 điểm %; ngày tuyết giảm ít nhất 1 điểm %, có điều kiện chặn.
   - Giao thức: `codex-work/ROUND12-REPLAY-PROTOCOL-CODEX.md` và phụ lục sửa `ROUND12-ERRATA-CODEX.md`.
2. **(Tùy chọn)** 34 lần chạy kiểu UberX Share (luật C ngân sách 0) làm đường cơ sở luật từ thực tế ngành.
3. **(Tùy chọn)** 34 lần chạy C-120 trên các ô T3.8 để xác nhận điểm gãy với tắc đường thật. 18 lần kiểm "tốc độ nền
   đúng giờ" đang để sau.
4. Viết **đoạn tuyên bố đóng góp** (mục 3) rồi nhờ Codex tấn công một vòng tìm chỗ nói quá.
5. **Áp dụng các đính chính** (mục 5) vào `FORECAST-REPORT.md`, `T38-REPORT.md` và docs/18–19 trên kho nghiên cứu.
   Cần hỏi trước khi commit/push.
6. **Viết luận văn** theo câu chuyện mục 3, từng chương đưa duyệt. Hạn "giữa tháng 11/2026" lấy theo các tài liệu
   tranh luận trước, ⚠️ cần xác nhận lại với chủ nghiên cứu.

**Hướng phát triển (không làm trong khóa luận):**
- ngân sách theo độ dài chuyến (cần sửa mã lõi);
- mô phỏng đông hơn giới hạn công cụ: ước tính k² đến 10·k² lần thời gian, gấp 2,5 lần đông thì mỗi job 1,5–15 giờ
  (`claude-work/RUNTIME-ESTIMATE-2026-10-07.md`);
- tắc đường theo từng đoạn đường;
- mô hình khách từ chối;
- học máy với dữ liệu nhiều tháng (dữ liệu taxi New York công khai).

---

## 9. Bẫy môi trường (chi tiết ở memory `ridebound-env-traps`)

- **Python:**
  - `python` không có trên PATH; luôn dùng đường dẫn đầy đủ ở mục 2, với `-B` và `PYTHONIOENCODING=utf-8`.
  - Script dài viết qua heredoc của bash có thể vỡ; dùng công cụ Write rồi chạy.
  - Không dùng heredoc hay `sed` với tiếng Việt.
- **Lệnh và đường dẫn:**
  - Bash tool reset thư mục làm việc sau mỗi lệnh; dùng đường dẫn tuyệt đối.
  - Python trên Windows không hiểu `/e/...`; dùng `E:/...`.
- **Output:** mở ở mode "x" (không ghi đè). Nếu lỡ tạo tệp lỗi, **giữ lại**, ghi tệp mới với hậu tố `b` hoặc `-a1`.
- **Nguồn điện:** kiểm trước job dài bằng `Get-CimInstance Win32_Battery` (BatteryStatus 2 = cắm sạc). Máy ngủ sẽ giết
  job.
- **Không sửa hay build trong worktree đang có job chạy:** inventory drift sẽ làm hỏng mọi job.
- **`pdftotext`** có ở `/mingw64/bin`. Một số trang (Springer, mediatum TUM, nd.edu) trả về trang web hoặc chặn bot,
  nên không tải được PDF.

---

## 10. Đoạn dán nhanh cho phiên mới

> Đọc `E:\Code\Report_INT3508\BAN-GIAO-PHIEN-2026-10-09.md` trước tiên, rồi
> `ridebound-scratchpad\optimize\codex-debate\DEBATE-LEDGER.md`. Lõi khóa luận: luật C (giới hạn thay đổi do điều phối,
> cộng dồn từng khách) + hứa theo dự báo + sổ cái ba phần. Kết quả đã kiểm chéo với Codex. Chưa sửa luận văn. Hỏi tôi
> muốn làm việc nào ở mục 8. Tuân thủ mọi quy tắc ở mục 1 (không bịa, không xóa, không đụng cây chính và báo cáo thực
> tập, niêm phong trước khi chạy, báo kết quả trước, chỉ sửa luận văn khi tôi đồng ý, trả lời tiếng Việt dễ hiểu).
> Codex: phiên `01a11056-6e20-7ef1-b6e4-fe375272c630`, mức xhigh, luôn thêm `-c windows.sandbox="unelevated"`.
