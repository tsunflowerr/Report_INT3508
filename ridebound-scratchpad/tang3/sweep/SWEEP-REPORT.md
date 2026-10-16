# Quét mức lời hứa: luật hành vi `C` so với hạn chót `M⁺` (kiểu Schulz và Pfeiffer), THĂM DÒ

- **Kế hoạch:** `SWEEP-PLAN.md`, niêm phong 2026-09-25T09:33:58Z, SHA-256 `756b65fd…423f`, trước mọi job.
- **Sửa đổi sau niêm phong:** `SWEEP-AMENDMENTS.md`.
  - A1: luật phục hồi (b).
  - A2: sự cố tôi gây ra; các job hỏng đã chạy lại.
- **Phạm vi:** ô phát triển, mỗi (thế giới, ô) một episode. Mọi kết quả là mô tả thăm dò.
- **Quy đổi:** 108 yêu cầu mỗi ô, 8 xe. Tám ô có tắc đường (W1, W2, W4, W5, mỗi thế giới hai ca) cộng lại là 864 yêu
  cầu; khi đó 1 khách ≈ 0,12%.

## 1. Đã chạy gì

- 13 nhánh × 6 thế giới × 2 ô = **156 job**. Nhánh gồm `U`, và `C-x`, `M⁺-x` với x ∈ {30, 60, 120, 300, 600, 900} s.
- Thế giới v1.1: đổi khung đúng `bin × 900 s`. Runner `runner-tier3-v1`. WP4 `wp4-tier3-v1.json`.
- **Công bằng giữa hai luật:**
  - Mỗi cặp `C-x`/`M⁺-x` chỉ khác đúng hai khóa (`configs/make_configs_sweep.log`).
  - Cả hai luật đều "vượt mới loại": `C` ở `CommitmentBudgetEvaluator.cs:88`, `M⁺` ở `CommitmentLockEvaluator.cs:186-191`.
  - Hạn chót được tính từ lời hứa đầu, đúng định nghĩa `l = B + L` của bài gốc.
- **Khác biệt còn lại so với bài gốc**, áp như nhau cho cả hai luật:
  - không có mô hình khách từ chối lời mời;
  - không có thuật toán chèn và tái tối ưu của họ;
  - dữ liệu là Manhattan;
  - có cửa sổ đón và thời gian đi tối đa;
  - cấm đổi xe.

## 2. Hợp lệ

- **Trạng thái:** 156/156 output dùng để phân tích có `status: pass`; audit v/e/p đúng cả 156 (`sweep-jobs-2026-09-26.tsv`).
- **Sự cố A2:**
  - 12 job hỏng vì tôi sửa code trong worktree mà quét đang dùng.
  - Chúng được chạy lại vào `-rerun1`, và **12/12 trùng từng frame** với bản hỏng. Hệ tất định.
  - 156/156 có cùng inventory kho `0da63eaf…`.
- **Thế giới:** 156 log, 0 vấn đề. Đổi khung đúng từng mốc; hệ số giống nhau giữa các nhánh; mỗi ô một hash kịch bản
  (`logs/sweep-worlds-final-2026-09-26.txt`).

## 3. Dự đoán đã niêm phong (`logs/sweep-predictions-2026-09-26.txt`)

| # | Dự đoán | Kết quả |
|---|---|---|
| D1 | W0: ở mọi x, `C-x` và `M⁺-x` nhận đúng cùng một tập khách | **Đúng** 12/12 |
| D2 | x = 900: `C`, `M⁺` và `U` cùng một tập khách ở mọi ô | **Đúng** 12/12 |
| D3 | `C` không có quyết định phục hồi nào | **Đúng**, 0/72 job |
| D4 | `M⁺` bị ép ở x = 30 trong mọi ô có tắc; không bị ép ở W0, W3; không bị ép ở x ≥ 600 | **Sai**: 7/8. W5 tối không bị ép, vì ngày đo thật buổi tối giao thông giảm. Hai vế còn lại đúng |
| D5 | x = 30: `C` phục vụ ≥ `M⁺` ở ≥ 6/8 ô có tắc | **Đúng**, vừa đủ: 6/8 |
| D6 | W3: `M⁺` ≥ `C` ở mọi x | **Đúng** 12/12, mọi cặp bằng nhau |
| D7 | x ≤ 120: lời hứa `M⁺` bị phá > 0 **và** tỉ lệ đó ≤ tỉ lệ trễ tương ứng của `C` ở ≥ 6/8 ô | **Sai, cả hai vế**: vế "> 0" chỉ 7/8, 6/8, 6/8; vế "≤ `C`" 5/8, 5/8, 7/8 (x = 30, 60, 120), tức chỉ đạt ngưỡng ở 120 s. Sửa 2026-09-29; bản đầu chỉ ghi vế thứ hai |

## 4. Kết quả, trên 8 ô có tắc đường (`logs/sweep-aggregate-2026-09-26.txt`)

`U` (không cổng) phục vụ 715/864 khách.

| x | Khách phục vụ `C` / `M⁺` | Lời hứa `C` bị phá (`C_r > x`) | Lời hứa `M⁺` bị phá (`A > x`) | `C` chấm theo luật `M⁺` (`A > x`) | `M⁺` bị ép (tỉ lệ quyết định) | Đội xe `M⁺` đóng băng | E2 `C` / `M⁺` |
|---|---|---|---|---|---|---|---|
| 30 | 697 / 692 | 0% | 14,4% | 13,5% | 28,1% | 9,4% | 19,8% / 18,7% |
| 60 | 699 / 693 | 0% | 11,0% | 10,8% | 21,7% | 7,0% | 20,5% / 19,9% |
| 120 | 703 / 704 | 0% | 7,6% | 8,1% | 12,9% | 5,6% | 21,6% / 21,2% |
| 300 | 714 / 716 | 0% | 0,7% | 0,8% | 3,9% | 0,9% | 22,7% / 22,2% |
| 600 | 715 / 715 | 0% | 0% | 0% | 0% | 0% | 22,7% / 22,7% |
| 900 | 715 / 715 | 0% | 0% | 0% | 0% | 0% | 22,7% / 22,7% |

Chú thích cột:
- `A` là giờ trả thật trừ giờ trả hứa lần đầu, nên "`A > x`" là lời hứa của `M⁺` bị phá. `C_r` là tổng phần do điều
  phối gây ra cho mỗi khách.
- Tỉ lệ "bị phá" và E2 là trung bình trên 8 ô.
- Tập khách của `C` và `M⁺` trùng nhau ở 6/12, 7/12, 6/12, 11/12, 12/12 và 12/12 ô cho các mức 30…900 s.

### 4a. Tách theo nguồn tắc đường (thêm 2026-09-29, mô tả)

Bảng gộp ở §4 dễ gây hiểu lầm, nên bảng dưới tách tám ô thành hai nhóm (`sweep-jobs-2026-09-26.tsv`):
- **thật:** W5, 2 ô, 216 yêu cầu; `U` phục vụ 192;
- **tự tạo:** W1, W2, W4, 6 ô, 648 yêu cầu; `U` phục vụ 523.

Luận văn (bảng `bang:quet` và `bang:quetb`) dùng bảng tách này.

| x | Thật: phục vụ `C` / `M⁺` | Thật: `M⁺` phá hứa | Thật: `M⁺` bị ép | Tự tạo: phục vụ `C` / `M⁺` | Tự tạo: `M⁺` phá hứa | Tự tạo: `C` theo luật `M⁺` | Tự tạo: `M⁺` bị ép |
|---|---|---|---|---|---|---|---|
| 30 | 189 / 189 | 1,1% | 11,9% | 508 / 503 | 18,8% | 17,7% | 33,5% |
| 60 | 190 / 190 | 0% | 0% | 509 / 503 | 14,7% | 14,4% | 28,9% |
| 120 | 190 / 191 | 0% | 0% | 513 / 513 | 10,1% | 10,8% | 17,2% |
| 300 | 192 / 192 | 0% | 0% | 522 / 524 | 1,0% | 1,0% | 5,2% |
| 600, 900 | 192 / 192 | 0% | 0% | 523 / 523 | 0% | 0% | 0% |

- Lời hứa `C` bị phá: 0% ở mọi ô.
- Nhóm thật, `C` theo luật `M⁺`: 1,1% ở 30 s, 0% ở các mức còn lại.
- **Luật (b)** (tính lại bằng `split_noworse.py`):
  - Nhóm thật: không đổi số khách. Chỉ `Mplus-30-W5-w08` có forced, và ở đó số khách bằng `C` (90), tỉ lệ
    `A > x` vẫn 2,2%. Tỉ lệ quyết định non-normal đổi từ 0,238 xuống 0,232 (`noworse-jobs-2026-09-26.tsv`). Sửa
    2026-09-29; bản đầu ghi "không đổi gì".
  - Nhóm tự tạo, số khách `C` / (a) / (b): 508/503/508, 509/503/509, 513/513/514, 522/524/522.
  - Kiểm trên từng ô: ở mọi ô mà (b) ra cùng quyết định với `C`, tỉ lệ `A > x` bằng đúng của `C`, không ô nào lệch.

### 4b. Theo từng kiểu tắc đường (`per_world.py`, 2026-09-29)

Mỗi kiểu gồm 2 ô, 216 yêu cầu. `M⁺` phá hứa là số liệu với luật (a); cột cuối là số khách phục vụ ở 30 s.

| Kiểu | `U` | `M⁺` phá hứa 30 / 60 / 120 / 300 s | Phục vụ ở 30 s `C` / (a) / (b) |
|---|---|---|---|
| W0 không đổi | 201 | 0 / 0 / 0 / 0 | 192 / 192 / 192 |
| W1 một cú sốc | 167 | 12,3 / 12,3 / 7,8 / 3,0% | 161 / 162 / 161 |
| W2 sốc lặp | 166 | 28,8 / 25,2 / 21,4 / 0% | 164 / 160 / 164 |
| W3 tắc giảm dần | 215 | 0 / 0 / 0 / 0 | 215 / 215 / 215 |
| W4 nhiễu theo cặp | 190 | 15,3 / 6,6 / 1,1 / 0% | 183 / 181 / 183 |
| W5 ngày thật | 192 | 1,1 / 0 / 0 / 0% | 189 / 189 / 189 |

- `C` phá hứa 0% ở mọi kiểu và mọi mức. Ở x ≥ 600 s, mọi kiểu đều 0% và cả ba nhánh bằng nhau.
- **Gánh bị ép đến từ ít khách** (`noworse-jobs-2026-09-26.tsv`, 22 job điều trị):
  - 15.528 quyết định, trong đó khoảng 3.789 non-normal (24%);
  - toàn bộ do 224 khách có breach forced gây ra, trên 1.874 khách phục vụ.
  - Vậy một khách trễ kéo theo trung bình khoảng 17 quyết định bị ép, cho tới khi xuống xe.

## 5. Cơ chế của các chênh lệch nhỏ (`sweep-mechanism-2026-09-26.tsv`)

- Ở các ô mà hai tập khách khác nhau, phần lớn khách "chỉ luật này phục vụ" **không** bị luật kia chặn trực tiếp.
- Ví dụ W1 tối, x = 30: trong 7 khách chỉ `M⁺` phục vụ, chỉ 2 khách có phương án bị trần `C` loại. Năm khách còn lại
  không có phương án nào bị trần `C` loại. TSV **không** tách được họ bị loại vì mã khác (cửa sổ đón, thời gian đi) hay
  không bị loại lần nào: cột `onlyM_otherCodesOnly` = `onlyM − onlyM_blockedByCBudget` (`sweep_mechanism.py:88`).
  Sửa 2026-09-29; bản đầu ghi "chỉ bị loại vì cửa sổ đón hoặc thời gian đi tối đa", chưa có bằng chứng.
- Tức phần lớn chênh lệch 1–3 khách mỗi ô là **đường đi rẽ nhánh**, không phải lợi thế có hệ thống của luật nào. Phân
  tích cơ chế được thêm sau niêm phong, là mô tả.

## 6. Diễn giải, đúng tầm

1. **Không tắc đường** thì hai luật là một ở mọi mức (D1). Đó là tất yếu khi bộ điều phối chỉ chèn thêm khách.
2. **Ở mức lời hứa của bài gốc (15 phút) và từ 600 s trở lên**, trên dữ liệu này, hai luật trùng nhau và trùng cả `U`
   (D2). Không bên nào hơn.
3. **Ở mức lời hứa chặt (30–120 s)**, dưới tắc đường:
   - **Số khách phục vụ gần như bằng nhau:** chênh ≤ 6/864, dưới 1%, và đổi chiều theo mức.
   - **Lời hứa của `C` luôn giữ được**, theo cấu tạo và Định lý 4.
   - **Lời hứa của `M⁺` bị phá** với 7,6–14,4% khách.
   - **Trên chính thước đo của `M⁺`**, tức trễ quá lời hứa đầu + x, `M⁺` không tốt hơn `C` một cách nhất quán (D7 sai):
     13,5% với `C` so với 14,4% với `M⁺` ở 30 s. Ở mức chặt, hạn chót hứa một điều mà tắc đường làm cho không luật
     nào giữ được.
   - `M⁺` phải trả thêm gánh phục hồi: bị ép ở 13–28% quyết định, và 5,6–9,4% đội xe đóng băng.
   - Chênh lệch nhỏ về số khách ở mức chặt biến mất khi dùng luật phục hồi (b) ở x = 30 và 60 s (và 300 s); ở
     120 s còn 705 so với 703 của `C`. Xem §7. (Sửa 2026-09-29: bản đầu ghi "biến mất" không kèm mức.)
4. **Phát biểu được bảo vệ:** hai luật không khác nhau về số khách phục vụ. Chúng khác nhau về **lời hứa có giữ được
   không** và **gánh phục hồi**:
   - `C` hứa ít hơn, chỉ phần do điều phối, nhưng luôn giữ được.
   - `M⁺` hứa nhiều hơn, cả tắc đường, nhưng ở mức chặt thì không giữ được và phải phục hồi.

## 7. Luật phục hồi (b) "không tệ hơn tham chiếu" (sửa đổi A1, sau niêm phong, mô tả)

- **Luật (b) là gì.** Khi một xe bị ép, luật (a) chỉ cho giữ nguyên tuyến cũ, nên xe "đóng băng". Luật (b) cho phép
  thêm một tuyến đã đổi của chính xe đó, với điều kiện: mọi cổng mà tuyến mới vi phạm thì tuyến cũ cũng đã vi phạm, và
  trên từng cổng đó tuyến mới không tệ hơn. ADR-077, commit `45f8026`, Runner v2.
- **Đã chạy:** 28 job (`run_noworse.py`, `logs/noworse-analyze-2026-09-26.txt`, `noworse-jobs-2026-09-26.tsv`).
  - **22 nhánh điều trị:** mọi `M⁺-x` có forced > 0 trong quét.
  - **6 đối chứng:** 4 nhánh `C-30` và 2 nhánh `M⁺-900`, đều không có forced.
  - **Hợp lệ:** 28/28 `status: pass`, audit v/e/p đúng cả 28.
- **Đối chứng: 6/6 giống hệt bản (a),** so trên chuỗi hành động đội xe của mọi quyết định đã được xác nhận. Đúng như
  dự kiến: (b) chỉ đổi hành vi khi có xe bị ép, và `C` không bao giờ bị ép.
- **Runner nhận quyết định `forcedNoWorse` từ đầu đến cuối.**
  - 49 quyết định có witness `forcedNoWorse`, với 50 breach `forcedNoWorse`, từ 0 đến 10 quyết định mỗi job.
  - Mọi job vẫn pass kiểm tra cuối.
  - Đây là bằng chứng chạy thật cho đường Runner mà ADR-077 còn ghi "chưa kiểm".
- **(b) ít khi dùng tới:** 5155 breach vẫn là `forcedReference` (giữ tuyến), chỉ 50 là `forcedNoWorse`.

### 7.1. Kết quả trên 8 ô có tắc đường (`logs/noworse-aggregate-2026-09-26.txt`)

- `M⁺(b)` dùng job no-worse khi ô đó có forced, và job quét ở các ô còn lại; đối chứng cho thấy hai cách cho cùng kết
  quả khi không có forced.
- Cột "cùng quyết định với `C`" so toàn bộ chuỗi hành động đội xe.

| x | Khách phục vụ `C` / `M⁺(a)` / `M⁺(b)` | `M⁺(b)` cùng quyết định với `C` | Lời hứa `M⁺(b)` bị phá (`A > x`) | `C` chấm theo luật `M⁺` | `M⁺(b)` bị ép (tỉ lệ quyết định) | Đội xe `M⁺(b)` đóng băng |
|---|---|---|---|---|---|---|
| 30 | 697 / 692 / **697** | 7/8 | 14,1% | 13,5% | 29,5% | 9,4% |
| 60 | 699 / 693 / **699** | 8/8 | 10,8% | 10,8% | 19,2% | 7,0% |
| 120 | 703 / 704 / **705** | 5/8 | 7,8% | 8,1% | 13,6% | 5,8% |
| 300 | 714 / 716 / **714** | 8/8 | 0,8% | 0,8% | 4,0% | 0,9% |
| 600 | 715 / 715 / 715 | 8/8 | 0% | 0% | 0% | 0% |
| 900 | 715 / 715 / 715 | 8/8 | 0% | 0% | 0% | 0% |

- **Trên 22 job điều trị,** tổng khách phục vụ là (b) 1874, (a) 1864, `C` 1873.
  - (b) bằng `C` ở 21/22 job, và có cùng chuỗi hành động với `C` ở 19/22.
  - Ba job khác `C`, ghi theo thứ tự (b)/(a)/`C`:
    - `Mplus-120-W4-w08`: 94/94/93;
    - `Mplus-120-W4-w17`: 92/92/92, cùng số khách nhưng khác hành động;
    - `Mplus-30-W4-w17`: 89/86/89.
- **(b) không phải lúc nào cũng tăng số khách so với (a).** Ví dụ `Mplus-120-W1-w17`: (a) 82, (b) 79, bằng `C`. Ở đó xe
  đóng băng của (a) tình cờ dẫn tới nhánh đường đi phục vụ nhiều hơn. (b) đưa `M⁺` về gần `C`, theo cả hai chiều.
- **Kiểm tra nhất quán:** ở x = 60 và x = 300, `M⁺(b)` ra cùng quyết định với `C` ở 8/8 ô. Khi đó chuyến đi thật trùng
  nhau, nên tỉ lệ `A > x` của `M⁺(b)` phải bằng tỉ lệ của `C` chấm theo luật `M⁺`. Số đo đúng như vậy: 10,8% = 10,8% và
  0,8% = 0,8%.
- **Tỉ lệ khách mà `M⁺(b)` làm vượt trần `C`** (`C_r > x`): trung bình 0,15% trên 22 job. Tức (b) gần như không đổi
  trễ do điều phối.

### 7.2. Đọc đúng tầm

1. **Chênh lệch số khách của (a) gợi ý là hệ quả của luật phục hồi, không phải của luật hạn chót.** Với luật phục
   hồi công bằng hơn, `M⁺` phục vụ đúng như `C` ở x = 30, 60, 300 s và ≥ 600 s. Ví dụ x = 30: 697 = 697, trong khi (a)
   là 692. Ở 120 s thì không bằng hẳn: 705 so với 703. Chỉ là gợi ý, vì (b) thêm sau niêm phong và mỗi ô một lần
   chạy. (Sửa 2026-09-29: bản đầu ghi "đúng như `C`" không kèm mức, và không ghi "gợi ý".)
2. **Phần khác biệt còn lại nằm ở cách hai luật ghi nhận cùng những quyết định đó,** không nằm ở số khách phục vụ. Ví dụ
   x = 60: `M⁺(b)` và `C` ra **cùng** quyết định ở 8/8 ô, vậy mà:
   - `C` giữ 100% lời hứa, vì nó chỉ hứa phần do điều phối;
   - `M⁺` phải ghi phá hứa với 10,8% khách, và 19,2% quyết định là quyết định bị ép (không bình thường).
3. **Mỗi ô một episode, trên ô phát triển;** một khách ≈ 0,12%. Các chênh lệch 1–2 khách không có ý nghĩa thống kê.

## 8. Giới hạn

- Mỗi ô một episode, chỉ trên ô phát triển; không có khoảng tin cậy.
- W1–W4 là thế giới tự tạo; W5 là ngày đo thật.
- **Các lần phá hứa lớn đến từ thế giới tự tạo** (`sweep-jobs-2026-09-26.tsv`, cột `M3_shareA_gt_x`).
  - Trên W5, ngày 12/11 đo thật:
    - hệ số tăng tới 17,6% trong khung sáng (2,797 lúc 08:00 lên 3,289 lúc 09:15) và giảm 16% trong khung tối
      (3,194 lúc 17:00 xuống 2,673 lúc 19:00), theo `2018-11-12_tt_factors.csv`;
    - `M⁺` chỉ phá lời hứa ở x = 30 s buổi sáng, 2,2% khách, bằng đúng tỉ lệ của `C` chấm theo luật `M⁺`;
    - từ x ≥ 60 s thì 0% ở cả hai khung.
  - Ở x = 60 s theo từng thế giới: W1 12,2% / 12,3%, W2 20,5% / 29,9%, W4 7,5% / 5,7%, W5 0% / 0%.
- Chỉ dữ liệu Manhattan. Dữ liệu Hamburg của bài gốc (tải về, CC BY 4.0) **chưa chạy**, vì cần sửa preflight trong kho:
  `op_max_wait_time` đang cố định ở 600 s. Cũng cần một bộ chuyển đổi và mô hình khách chọn.
- **Khung giờ đã chạy là khung đã qua đoạn tắc đường tăng nhanh.** Nguồn: các số của khung 7–9h, bước 15 phút và số
  yêu cầu ban đầu được tính bằng lệnh PowerShell, **không** bằng `why_similar.py`. Từ 2026-09-29 chúng có script
  `traffic_windows.py`, log `logs/traffic-windows-2026-09-29.txt`, và mọi số dưới đây khớp log đó (đỉnh 7–9h 12–16/11:
  46,9–65,6%, ghi tròn 47–66%). Trôi dạt theo khách lấy từ `why_similar.py` phần B:
  - trong cùng tệp `*_tt_factors.csv`, khung 7:00–9:00 ngày 12–16/11 có đỉnh tăng 47–66% so với đầu khung;
    khung 8:00–10:00 của các ngày đó chỉ 15–23%;
  - bước tăng lớn nhất giữa hai mốc 15 phút: 8,3–16,2% (7–9h) so với 3,7–7,1% (8–10h);
  - nhu cầu 7–9h ngày 14–16/11 gần bằng 8–10h (2.396–2.724 so với 2.458–2.757 yêu cầu trong một tệp `sample_10_1`);
    độ phủ của 96 nút chưa kiểm;
  - trôi dạt của từng khách trên ngày thật 12/11 nhỏ: sáng 2,2% khách trôi quá 30 s, 0% quá 60 s, lớn nhất 35,2 s; tối 0%, lớn nhất 7,7 s.
    Ở thế giới tự tạo: 12–32% khách trôi quá 30 s ở W1, W2, và tới 6–7 phút ở W1;
  - vậy "hai luật như nhau trên tắc đường thật" chỉ đúng cho hai khung đã chạy. Khung 7–9h chưa chạy.
- Một ô Panel A (`d20181114-s10-r1`) đã bị nhìn thấy trong smoke T3.5/T3.6; ô này không có trong quét.
