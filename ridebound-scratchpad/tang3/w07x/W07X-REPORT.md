# Việc w07x: mức hứa 90–240 s trên 8 ô 7:00–9:00, chỉ tắc đường thật — báo cáo (THĂM DÒ)

- **Kế hoạch:** `W07X-PLAN.md`, niêm phong 2026-09-30T17:07:53Z (`W07X-PLAN.sha256`), commit `aa98fa5` và push lên
  `research/tier3-no-worse` lúc 00:08:29 (giờ máy) ngày 1/10, **trước job đầu tiên** (00:09:09). Bản trong git trùng mã băm niêm phong.
- **Vùng mức hứa được chọn sau khi đã xem Việc B** (xem kế hoạch §0). Mọi mức đều được báo.
- **Chạy:** 104 job, 00:09–05:53 ngày 1/10, cắm sạc, 0 job bị hoãn. Output `C:\RideBoundData\research\tier3-w07x-v1\`.
- **Phân tích:** `w07x_analyze.py` → `analysis/full-2026-10-01-report.txt`, `-jobs.tsv`; cơ chế `w07x_mechanism.py` →
  `analysis/mechanism-2026-10-01.txt`. (Tệp `analysis/mechanism-trial-120-only-2026-10-01.txt` là lần chạy thử script lúc job
  còn dở; hai dòng 150/180 trong đó là do bản ghi chưa xong, không dùng.)
- 8 ô phát triển, mỗi ô một episode; 1 khách ≈ 0,9–1,5% một ô. Không có khoảng tin cậy.

## 1. Hợp lệ

- 104/104 `status: pass`; audit v/e/p `ok`; log thế giới đúng như Việc B (dòng v1.2, kiểm ngày, mốc đúng `bin × 900 s`, hệ số
  khớp tệp hệ số); cùng inventory `0da63eaf…4cbe`; 0 vấn đề.
- `policyConfigurationHash`: 23 mã khác nhau cho 23 nhánh (13 mới, 10 dùng lại), mỗi nhánh một mã trên cả 8 ô.

## 2. Kết quả theo từng mức (8 ô, 864 yêu cầu; `U` phục vụ 665)

| x (s) | Phục vụ C / M⁺ / V | C, M⁺ cùng quyết định | Cách ghép bị chặn C / M⁺ / V | Phần do hệ thống lớn nhất (C) | Phá hứa theo thước của chính mình: C / M⁺ / V | Theo thước hạn chót (A > x): C / M⁺ / V | Bị ép: C / M⁺ / V | E2 |
|---|---|---|---|---|---|---|---|---|
| 30 | 660 / 660 / 660 | 8/8 | 221 / 227 / 227 | 10,0 s | 0 / 24,0 / 29,2% | 24,0 / 24,0 / 24,0% | 0 / 58,6 / 63,2% | 8,8% |
| 60 | 661 / 661 / – | 8/8 | 186 / 192 / – | 41,9 s | 0 / 7,3 / –% | 7,3 / 7,3 / –% | 0 / 35,5 / –% | 8,8% |
| **90** | 664 / 663 / 663 | **7/8** | 153 / 159 / 160 | 86,9 s | 0 / 2,1 / 2,9% | 2,1 / 2,1 / 2,1% | 0 / 13,0 / 17,4% | 9,2% |
| **120** | 666 / 664 / 664 | **6/8** | 119 / 129 / 129 | 96,7 s | 0 / 0,9 / 1,0% | 1,2 / 0,9 / 0,9% | 0 / 6,6 / 7,4% | 9,2% |
| 150 | 666 / 666 / 666 | 8/8 | 108 / 115 / 115 | 96,7 s | 0 / 0,5 / 0,8% | 0,5 / 0,5 / 0,5% | 0 / 6,8 / 8,6% | 9,2% |
| 180 | 666 / 666 / 666 | 8/8 | 100 / 105 / 105 | 96,7 s | 0 / 0,5 / 0,5% | 0,5 / 0,5 / 0,5% | 0 / 2,8 / 2,8% | 9,2% |
| 240 | 665 / 665 / 665 | 8/8 | 87 / 91 / 91 | 208,2 s | 0 / 0,2 / 0,4% | 0,2 / 0,2 / 0,2% | 0 / 1,7 / 1,7% | 9,0% |
| 300 | 665 / 665 / – | 8/8 | 85 / 85 / – | 208,2 s | 0 / 0,2 / –% | 0,2 / 0,2 / –% | 0 / 1,7 / –% | 9,0% |

- Mức 30, 60, 120 (C, M⁺), 300 và `U`, `V-30` là lần chạy của Việc B (cấu hình trùng byte). E2 giống hệt nhau giữa ba luật ở mọi mức.
- Theo từng ô: ở 90 s chỉ ô 12/11 mẫu 1 lệch (C 90, M⁺ 89, V 89); ở 120 s ô 12/11 mẫu 1 (90/89/89) và 13/11 mẫu 1 (71/70/70).
  Mọi ô khác, ở mọi mức, ba luật phục vụ đúng như nhau.

## 3. Dự đoán đã niêm phong: 6/8 đúng, 2 sai

| # | Kết quả |
|---|---|
| R1 | **Đúng.** 0/32 job `C-x` mới có quyết định non-normal |
| R2 | **Sai.** Dự đoán mỗi mức mới lệch ở ≥ 1/8 ô; thực tế 90 s lệch 1/8, còn 150, 180, 240 s lệch **0/8** |
| R3 | **Đúng (dự đoán rỗng).** Tổng C − M⁺: +1 (90 s, 1 ô), 0, 0, 0; không mức nào đạt tiêu chí "C phục vụ nhiều hơn" (≥ 3 khách và ≥ 3 ô) |
| R4 | **Sai.** Dự đoán `V` bị ép nhiều hơn M⁺ ở **mọi** mức; đúng ở 90, 120, 150 s (17,4/13,0; 7,4/6,6; 8,6/6,8%) nhưng **bằng nhau** ở 180 và 240 s (2,8 và 1,7%) |
| R5 | **Đúng.** \|tổng V − tổng C\| ≤ 2 ở mọi mức (663/664, 664/666, 666/666, 666/666, 665/665) |
| R6 | **Đúng.** Tỉ lệ phá hứa của M⁺ không tăng: 7,25 / 2,12 / 0,87 / 0,51 / 0,51 / 0,18 / 0,18% (60…300 s); 90 s trong [1,5; 5,0]%; 150–240 s ≤ 1% |
| R7 | **Đúng.** Chấm theo thước hạn chót, C và M⁺ lệch nhau ≤ 0,01 điểm % ở các mức mới |
| R8 | **Đúng.** Phá hứa theo thước của `V` không tăng theo x (29,2 / 2,9 / 1,0 / 0,8 / 0,5 / 0,4%) và ở mỗi mức ≥ tỉ lệ A > x của chính `V` |

## 4. Cơ chế ở các ô lệch (`analysis/mechanism-2026-10-01.txt`; mô tả)

Cả 3 chỗ lệch có cùng một cơ chế:

| Mức, ô | Quyết định lệch đầu tiên | Chuyện gì xảy ra |
|---|---|---|
| 90 s, 12/11 mẫu 1 | thứ 294, t = 3.073 s (≈ 07:51) | C nhận khách mới `rq-150ba8d…` lên xe `veh-176f91…`; M⁺ chặn đúng cách ghép đó (`COMMITMENT_DEADLINE_EXCEEDED`, `deadline_cap`) vì khách đang có `rq-c768366…` đã trễ **79,0 s do tắc đường** (phần do hệ thống 0 s), và cách ghép thêm **68,3 s do hệ thống** → 147 s > 90 s. C chỉ tính 68,3 s ≤ 90 s |
| 120 s, 12/11 mẫu 1 | thứ 294, t = 3.073 s | giống hệt dòng trên (79,0 + 68,3 = 147 s > 120 s) |
| 120 s, 13/11 mẫu 1 | thứ 285, t = 2.903 s (≈ 07:48) | C nhận khách mới `rq-a341968…`; M⁺ chặn vì khách đang có `rq-f6c8ce7…` đã trễ **60,9 s do tắc đường**, cách ghép thêm **61,2 s do hệ thống** → 122 s > 120 s |

- Tức hai luật chỉ khác nhau khi tắc đường **cộng** một lần dời do hệ thống vượt mức hứa, trong khi riêng phần do hệ thống chưa
  vượt. Ở ba chỗ lệch, phần tắc đường trước quyết định là 61–79 s và lần dời do hệ thống là 61–68 s. Ở 150 s trở lên không có chỗ
  lệch nào, tức trên 8 ô này không có quyết định nào mà tổng ấy vượt mức trong khi riêng phần do hệ thống chưa vượt. Chưa kiểm
  phân bố đầy đủ của hai phần này trên mọi quyết định.
- Mỗi lần lệch làm C nhận thêm **đúng 1 khách** ở ô đó.

## 5. Đọc đúng tầm

- **Giả thuyết "hai luật khác nhau ở vùng 90–240 s" chỉ đúng một phần:** khác biệt có thật và có đúng cơ chế dự kiến, nhưng chỉ ở
  90–120 s, chỉ ở 1–2/8 ô, và chỉ **1 khách mỗi ô**. Từ 150 s trở lên hai luật như nhau hoàn toàn.
- **Không được nói "C phục vụ nhiều hơn":** tổng chênh tối đa 2 khách (120 s) và chỉ ở 2 ô — dưới tiêu chí đã chốt.
- **Điều đứng được:** cùng số khách (chênh ≤ 2/864), nhưng M⁺ và `V` phá lời hứa của chính mình (2–3% ở 90 s, 24–29% ở 30 s) và
  phải phục hồi (13–17% quyết định ở 90 s, 59–63% ở 30 s), còn C không bao giờ phải phục hồi và giữ lời hứa của nó theo cấu tạo.
- **Chỗ yếu:** 8 ô của 2 ngày, thuộc panel phát triển, trùng một phần khách với các ô 8–10h đã xem; mỗi ô một episode; vùng mức
  hứa chọn sau khi xem Việc B; hai dự đoán sai (R2, R4).

## 6. Kiểm độc lập (2026-10-01, `independent/RESULT.md`)

Một agent viết mã riêng, không đọc script phân tích của scratchpad, tính lại 7 khẳng định từ 184 bản ghi thô (104 mới, 80 dùng
lại); 383.059 khung dữ liệu khớp mã kiểm; sổ cái trong checkpoint khớp các hành động công bố lời hứa ở cả 184 lần chạy. **7/7 khớp**:
trạng thái và inventory; mã cấu hình mỗi nhánh; bảng số khách từng ô; ba chỗ lệch (90 s ô 12/11 mẫu 1 quyết định 294; 120 s cùng ô
quyết định 294; 120 s ô 13/11 mẫu 1 quyết định 285), và `V` lệch `C` ở đúng ba chỗ đó; 0 quyết định non-normal ở 32 job C mới; tỉ lệ
phá hứa và bị ép (M⁺ 0,0212 / 0,0051 / 0,0051 / 0,0018; bị ép M⁺/V 0,130/0,174, 0,068/0,086, 0,028/0,028, 0,017/0,017; V-120 0,074);
phá hứa của `V` (0,0289 / 0,0101 / 0,0083 / 0,0051 / 0,0036); và cơ chế ở 90 s (78,993 s tắc đường + 68,262 s do hệ thống).

Ghi chú thêm của agent (không đổi kết luận): M⁺ và `V` hành động giống hệt nhau ở cả 48 cặp (mức, ô) có `V`; tỉ lệ bị ép tăng nhẹ từ
120 lên 150 s (M⁺ 0,066 → 0,068; `V` 0,074 → 0,086), chưa tìm hiểu vì sao; dưới `V-x` phần do hệ thống một mình không bao giờ đẩy
khách vượt x (lớn nhất 86,9 s ở V-90), mọi trường hợp vượt đều có phần tắc đường.
