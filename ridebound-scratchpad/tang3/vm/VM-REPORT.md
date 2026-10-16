# Việc A: `V-30` và `M-30` với hai luật phục hồi trên world v1.1 — báo cáo (THĂM DÒ)

- **Kế hoạch:** `VM-PLAN.md`, niêm phong 2026-09-29T09:29:51Z (`VM-PLAN.sha256`), trước job đầu tiên. Driver `run_vm.py` niêm
  phong cùng lúc.
- **Chạy:** 48 job, 16:30–19:26 giờ máy ngày 29/09, 6 luồng, cắm sạc. Output `C:\RideBoundData\research\tier3-vm-v11-a|b\`.
- **Phân tích:** `vm_analyze.py` → `analysis/full-2026-09-29-report.txt`, `-jobs.tsv`, `-paired.tsv`. Phần mô tả thêm sau khi xem
  kết quả: `vm_describe.py` → `analysis/describe-2026-09-29.txt`.
- Mỗi (thế giới, ô) một episode, trên ô phát triển. Một khách ≈ 0,9% của một ô. Không có khoảng tin cậy.

## 1. Hợp lệ

- 48/48 `status: pass`; audit v/e/p `ok` ở cả 48; 0 vấn đề về thế giới (đổi mốc đúng `bin × 900 s`, mốc 0 bằng 1, hệ số giống
  nhau giữa các nhánh trên mốc chung); cùng hash kịch bản trong mỗi ô; cả 48 job và 12 job so sánh `C-30` có cùng inventory
  `0da63eaf…4cbe`.

## 2. Dự đoán đã niêm phong: 8/8 đúng

| # | Kết quả |
|---|---|
| P1 đối chứng | **Đúng.** 4/4 cặp mà (a) không bị ép cho chuỗi hành động (b) giống hệt (a) (đó là 4 job W0) |
| P2 W0 | **Đúng.** 8/8 biến thể không bị ép và nhận đúng tập khách của `C-30`; thật ra ra **cùng từng quyết định** với `C-30` (788 và 765 quyết định) |
| P3 bị ép | **Đúng.** `V-30(a)` và `M-30(a)` bị ép ở 10/10 ô có trôi, kể cả W3 và W5 tối |
| P4 (b) ≥ (a) | **Đúng.** `V-30`: 912 so với 877 khách trên 10 ô, (b) ≥ (a) ở 9/10. `M-30`: 914 so với 869, (b) ≥ (a) ở 9/10 |
| P5 đường mới | **Đúng.** `V-30(b)`: 118 quyết định có witness `forcedNoWorse` mã `COMMITMENT_BUDGET_EXCEEDED` (đường miễn trừ theo ngân sách, lần đầu chạy đầu-cuối). `M-30(b)`: 12 quyết định `forcedNoWorse` ở W3 (cận dưới) |
| P6 tín hiệu H2 | **Đúng như dự đoán: tiêu chí KHÔNG đạt.** `C-30 − V-30(b)` = 0 ở **cả 8/8** ô có tắc; tổng 697 = 697 |
| P7 E2 | **Đúng.** E2 của `V-30(b)` ≤ `C-30` ở 8/8 ô; bằng nhau ở 7/8, thấp hơn ở W4 sáng (0,117 so với 0,128) |
| P8 tất định | **Đúng.** `V-30(a)` W4 sáng trùng 754/754 quyết định với bản smoke v1.1, 92 khách |

## 3. Số khách phục vụ (trên 108 mỗi ô)

| Thế giới | Ô | `U` | `C-30` | `V-30` (a) / (b) | `M-30` (a) / (b) | `M⁺-30` (a) / (b) |
|---|---|---|---|---|---|---|
| W0 không đổi | sáng / tối | 102 / 99 | 97 / 95 | 97/97 · 95/95 | 97/97 · 95/95 | 97/97 · 95/95 |
| W1 một cú sốc* | sáng | 87 | 82 | 80 / 82 | 79 / 85 | 82 / 82 |
| | tối | 80 | 79 | 78 / 79 | 78 / 79 | 80 / 79 |
| W2 sốc lặp* | sáng | 87 | 85 | 77 / 85 | 77 / 85 | 83 / 85 |
| | tối | 79 | 79 | 66 / 79 | 66 / 79 | 77 / 79 |
| W3 tắc giảm dần* | sáng | 108 | 108 | 108 / 108 | 108 / **105** | 108 / 108 |
| | tối | 107 | 107 | 103 / 107 | 102 / 107 | 107 / 107 |
| W4 nhiễu theo cặp* | sáng | 96 | 94 | 92 / 94 | 89 / 94 | 95 / 94 |
| | tối | 94 | 89 | 85 / 89 | 86 / 89 | 86 / 89 |
| W5 ngày thật 12/11 | sáng | 92 | 90 | **92** / 90 | 87 / **92** | 90 / 90 |
| | tối | 100 | 99 | 96 / 99 | 97 / 99 | 99 / 99 |

\* thế giới tự tạo. Cột `U` và `M⁺-30` lấy từ phép quét và quét no-worse, để đối chiếu.

**Tổng trên 8 ô có tắc** (W1, W2, W4, W5): `C-30` 697; `V-30` (a) 666 / (b) **697**; `M-30` (a) 659 / (b) 702.

## 4. Mô tả thêm sau khi xem (không phải dự đoán)

1. **`V-30(b)` ra cùng từng quyết định với `C-30` ở 11/12 ô** (mọi ô trừ W4 sáng). Tức với cách xử lý kẹt công bằng, luật theo
   giờ khách thấy và luật của khóa luận chở đúng cùng những chuyến đi trên workload này.
2. **Lời hứa của chính mỗi luật** (`describe-2026-09-29.txt`; khách của `V-30(b)`):
   - lời hứa của `V-30` (tổng độ dời giờ trả khách thấy ≤ 30 s) bị phá với 26–54% khách ở W1, W2, W4, và với **12,2%** (sáng)
     và **7,1%** (tối) khách trên ngày thật 12/11;
   - lời hứa của `C-30` (tổng phần do điều phối ≤ 30 s): 0% ở mọi ô, theo cấu tạo;
   - vì `V-30(b)` và `C-30` cùng quyết định ở 11/12 ô, `C-30` chấm theo luật của `V` cho đúng các tỉ lệ trên. Chuyến đi giống
     nhau; khác nhau chỉ ở lời hứa được đưa ra và việc có phải phục hồi hay không.
3. **Gánh phục hồi của `V-30(b)`:** 37–80% quyết định là non-normal ở 8 ô có tắc; riêng ngày thật 44,7% (sáng) và 55,0% (tối).
   Tức trên chính dữ liệu thật, `V-30` ở chế độ phục hồi ở khoảng một nửa số quyết định.
4. **`M-30(b)`** phục vụ 702 so với 697 của `C-30` trên 8 ô có tắc (+3 ở W1 sáng, +2 ở W5 sáng), nhưng **ít hơn 3 khách** ở W3 sáng
   (105 so với 108; `M-30(a)` là 108). Như với `M⁺`, (b) có thể làm giảm số khách.
5. **Khách đến sớm hơn lời hứa đầu:** dưới `C-30` trên ngày thật 12/11 sáng, 2,2% khách đến muộn quá 30 s so với lời hứa đầu,
   nhưng 7,8% khách lệch quá 30 s theo **cả hai chiều**, tức có khoảng 5,6% đến **sớm** quá 30 s. Vì vậy cận dưới của hạn chót
   hai chiều cũng cắn cả khi tắc đường tăng.

## 5. Đọc đúng tầm

- **Tín hiệu H2 ở thí điểm (C phục vụ nhiều hơn V tới 10 khách) biến mất khi xử lý kẹt công bằng.** Với luật (a), khoảng cách
  vẫn còn (697 so với 666 trên 8 ô). Với luật (b), khoảng cách bằng 0 ở cả 8 ô. Vậy khoảng cách ở thí điểm là do luật phục
  hồi (xe "đóng băng"), không do cơ sở ngân sách. Đây là **kết quả âm** cho dạng H2 "C phục vụ nhiều hơn V", và được báo
  đúng như vậy. Nó chỉ là mô tả thăm dò trên 2 ô phát triển.
- **Khác biệt còn lại nằm ở lời hứa, không ở chuyến đi:** cùng những chuyến đi, luật `V` hứa điều mà tắc đường làm cho không
  giữ được (7–12% khách trên ngày thật, 26–54% dưới tắc tự tạo) và phải phục hồi ở khoảng một nửa số quyết định; luật `C` hứa
  ít hơn nhưng giữ được theo cấu tạo. Kết luận này giống kết luận với `M⁺` ở phép quét.
- **Không được nói:** "`C` phục vụ nhiều hơn `V`"; "0% phá hứa của `C`" như một phát hiện (đó là cấu tạo); "đã xác nhận".
- **Chỗ yếu:** mỗi ô một episode; chỉ 2 ô phát triển; 3/4 thế giới có trôi là tự tạo; (b) lệch khỏi đề xuất phục hồi của kế
  hoạch Codex §12.3 ở hai điểm: (i) xe bị ép vẫn nhận khách mới trong lượt phục hồi (Codex dòng 506 đòi không); (ii) công
  validate thêm của (b) chưa được cộng vào `validationWorkUnits` (Codex dòng 508 đòi cùng ngân sách công việc).

## 6. Hệ quả cho các quyết định của chủ nghiên cứu (chưa chốt gì)

- Bàn giao §8 dòng 5 (luật phục hồi cho phép so xác nhận): với (b), phép so `C-30`/`V-30` trên workload này gần như chắc
  chắn không có khác biệt số khách. Nếu vẫn giữ H2 ở dạng "C phục vụ nhiều hơn V ít nhất δ_b", nó khó có cơ hội đạt; có thể
  cần đổi câu hỏi sang "giữ lời hứa và gánh phục hồi ở cùng số khách". Đây là việc của chủ nghiên cứu, không tự quyết.
- Kiểm độc lập: xem mục 7.

## 7. Kiểm độc lập (2026-09-29, `independent/RESULT.md`)

Một agent kiểm độc lập viết mã riêng, không dùng module nào của scratchpad, và tính lại 7 khẳng định từ 60 bản ghi thô
(48 job Việc A và 12 job `C-30`). **7/7 khớp:**
1. 48/48 `pass`, cùng inventory `0da63eaf…4cbe`; 12 job `C-30` cũng `pass`.
2. Số khách phục vụ của cả 12 ô × 5 nhánh, ở bảng mục 3. Kiểm chéo: số khách có sự kiện xuống xe bằng số khách hoàn tất.
3. W0: 0 quyết định non-normal ở cả 4 biến thể. W1–W5: `V-30(a)` và `M-30(a)` ít nhất 153 và 152 quyết định non-normal mỗi ô,
   thấp nhất ở W3 sáng.
4. `V-30(b)` cùng chuỗi hành động đội xe với `C-30` ở 11/12 ô, trừ W4 sáng. Kết quả giữ nguyên qua 6 cách so. Ở W4 sáng, chỗ
   khác đầu tiên là quyết định thứ 634 (6.394.000 ms): `C-30` nhận một khách mà `V-30(b)` từ chối, và quyết định đó mang
   witness `forcedReference`, không phải `forcedNoWorse`.
5. 118 quyết định `forcedNoWorse` mã `COMMITMENT_BUDGET_EXCEEDED` của `V-30(b)` (sáng/tối: W1 8/11, W2 23/11, W3 2/14, W4 21/16,
   W5 9/3), và 12 quyết định `forcedNoWorse` của `M-30(b)` ở W3 (2 + 10).
6. `C-30` và `V-30(b)` W5 sáng: 11/90 = 0,122 khách có tổng độ dời giờ trả > 30 s.
7. `C-30` W5 sáng: 2/90 trễ quá lời hứa đầu 30 s; 7/90 lệch quá 30 s theo cả hai chiều (2 muộn, 5 sớm).

Hai điểm agent ghi nhận, phải nói rõ khi dùng số:
- **Lời hứa giờ trả cuối cùng của mỗi khách được công bố lúc hoặc sau khi khách xuống xe, và bằng đúng giờ trả thật (90/90).**
  Vì vậy "tổng độ dời khách thấy" gồm cả lần chỉnh cuối về giờ thật. Bỏ lần chỉnh đó đi thì tỉ lệ vẫn là 11/90. Cũng vì vậy,
  "lệch quá 30 s theo cả hai chiều" ở điểm 7 đúng bằng thay đổi ròng từ lời hứa đầu tới lời hứa cuối.
- Mọi witness `forcedNoWorse` của `M-30` mang mã `COMMITMENT_DEADLINE_EXCEEDED`, là mã chung cho cả cận trên lẫn cận dưới. Câu
  "ở W3 mọi vi phạm là ở cận dưới" (P5) là **suy luận** từ việc tắc đường giảm suốt khung, **chưa kiểm** được bằng mã.
