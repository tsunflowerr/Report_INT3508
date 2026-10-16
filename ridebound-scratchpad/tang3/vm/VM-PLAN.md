# Việc A: so lại luật theo giờ khách thấy (`V-30`) và hạn chót hai chiều (`M-30`) bằng cả hai luật phục hồi, THĂM DÒ

Trạng thái: viết 2026-09-29 và niêm phong bằng SHA-256 (`VM-PLAN.sha256`) **trước khi chạy job nào** của việc này.

- Nguồn giao việc: `BAN-GIAO-PHIEN-2026-09-29.md` §9 việc A. Phạm vi nằm trong Tầng 3 đã được chủ nghiên cứu duyệt.
- Chạy trên ô phát triển, mỗi (thế giới, ô) một episode. Mọi kết quả là mô tả thăm dò, không phải xác nhận.
- Việc này **không** chốt bất kỳ ngưỡng nào của H2, H3, T3.8 hay T3.9 (δ_s, δ_b, δ_r, α, quy tắc quyết định...). Các
  ngưỡng đó thuộc chủ nghiên cứu (bàn giao §8).

## 1. Câu hỏi

Ở thí điểm T3.7 (thế giới v1, luật phục hồi (a)), `C-30` phục vụ không ít hơn `V-30` ở 12/12 episode, hơn 0–10 khách.
Nhưng `V-30` và `M-30` bị ép ở đa số quyết định trong 5/12 episode, và xe bị ép thì "đóng băng". Với `M⁺`, luật phục
hồi (b) đã xóa gần hết chênh lệch số khách (quét C/M⁺ §7). Câu hỏi:

1. Khi `V-30` và `M-30` được xử lý kẹt bằng luật (b), `C-30` còn phục vụ nhiều hơn rõ rệt không? Nếu không, tín hiệu H2
   ở thí điểm chủ yếu là do luật phục hồi.
2. Đường miễn trừ **theo ngân sách** của (b) (`tổng sau ≤ tổng sau của tuyến giữ`) và đường **cận dưới** của hạn chót hai
   chiều có thật sự được đi qua đầu-cuối không? Cả hai mới chỉ có unit test (ADR-077).

## 2. Ma trận (48 job)

| Mục | Giá trị |
|---|---|
| Nhánh (2) | `V-30` (`../configs/V-30.json`, SHA-256 `2462484a…05d5`), `M-30` (`../configs/M-30.json`, `34e1f263…bfd`). `V-30` khác `C-30` đúng một khóa `budgetBasis: customerVisible`; `M-30` = `Mplus-30` cộng `dropEtaDeadlineTwoSided: true` (`../configs/make_configs_t3.log`) |
| Luật phục hồi (2) | (a): Runner `E:\RideBoundData\research\runner-tier3-v1` (tree `5049f6d3…52c5cb`) + `../configs/wp4-tier3-v1.json` (`d132e9d3…1d5b`, `forced-reference-v1`). (b): Runner `C:\RideBoundData\research\runner-tier3-v2` (tree `ac251ef3…cff3f`) + `../configs/wp4-tier3-v2.json` (`66e9b592…4518`, `no-worse-than-reference-v1`). Hai tệp WP4 chỉ khác khóa `commitmentRecovery` (`../configs/make_wp4_v2.log`) |
| Thế giới (6) | W0–W5, **đúng các tệp** `../pilot/worlds/` của thí điểm và phép quét |
| Ô (2) | `d20181112-s10-r1-w08`, `d20181112-s10-r1-w17` (panel phát triển), 108 yêu cầu, 8 xe |
| Cài đặt thế giới | v1.1 (`../world/preflight_world_v1_1.py`, SHA-256 `7df4a458…7725`) |
| Lệnh | đúng lệnh của phép quét (`../sweep/run_sweep.command`), chỉ đổi `--label`, `--runner-root`, `--wp4-config`, `--output`, và thêm `--expected-repository-inventory-sha256 0da63eaf…4cbe` |
| cwd | `E:\Code\RideBound-deadline` (HEAD `1ce15e9`, inventory `0da63eaf…4cbe`, tính lại 2026-09-29). **Không sửa, không build** ở đây |
| Output | `C:\RideBoundData\research\tier3-vm-v11-a\<job>` và `…-b\<job>`; log `logs/<a|b>-<job>.log` mode `x`; công tắc `STOP` cạnh driver |
| Driver | `run_vm.py`: 6 luồng, chỉ chạy khi cắm sạc, giữ máy thức, không chạy lại output đã có |

**Đối chứng so sánh, không chạy lại:** `C-30`, `U`, `Mplus-30` của phép quét (`E:\RideBoundData\research\tier3-sweep-v1`,
Runner v1, WP4 v1, cùng wrapper, cùng inventory), đọc qua `run_sweep.effective` vì `C-30-W4-…-w17` chỉ có bản `-rerun1`.
`C-30` dùng được cho cả (a) và (b): trong quét no-worse, 4/4 đối chứng `C-30` chạy bằng Runner v2 + WP4 v2 có chuỗi hành
động đội xe giống hệt bản quét, vì `C` không bao giờ bị ép. `Mplus-30(b)` lấy từ `C:\RideBoundData\research\tier3-sweep-noworse-v1`
khi ô đó có trong quét no-worse, ngược lại lấy bản quét.

## 3. Công bằng

- Mỗi cặp so chỉ khác đúng khóa đã nêu ở mục 2: cùng bộ sinh phương án, hàm mục tiêu, ràng buộc cấu trúc, khóa pha,
  cửa sổ đón, thời gian đi tối đa, luật lên xe muộn, dữ liệu, hạt giống, thế giới.
- Cả ba luật đều "vượt mới loại" (`C`, `V`: `afterValue > hardLimit`; `M`: `|p − p0| > slack`).
- (b) lệch khỏi đề xuất phục hồi chung của kế hoạch Codex §12.3 ở hai điểm, và phải báo kèm kết quả:
  (i) Codex đòi không nhận thêm khách trong lượt phục hồi đầu (dòng 506), còn (b) cho xe bị ép nhận khách mới;
  (ii) Codex đòi mọi nhánh cùng ngân sách công việc sửa chữa (dòng 508), còn công validate thêm của (b) chưa được cộng
  vào `validationWorkUnits` (ADR-077).

## 4. Thước đo (tính cho mọi job, như phép quét)

- Dùng lại `../sweep/sweep_analyze.job_row` (M1–M8), trỏ `OUT_ROOT`, `effective`, `state_of` sang output của việc này như
  `noworse_analyze.py` đã làm.
- Thêm: đếm quyết định có witness theo (giai đoạn, mã) trong chứng nhận (`forcedReference`/`forcedNoWorse` ×
  `COMMITMENT_BUDGET_EXCEEDED`/`COMMITMENT_DEADLINE_EXCEEDED`); breach theo loại trong final checkpoint.
- So quyết định bằng chuỗi hành động đội xe đã được xác nhận (`../pilot/pilot_analyze.fleet_decisions`), không bằng
  semanticHash.
- Ghép cặp `C-30` với `V-30(b)` theo khách chung (như `../pilot/pilot_paired.py`), chỉ để chẩn đoán. E2 chính dùng mẫu số
  là khách của chính nhánh đó.
- Định nghĩa dùng trong dự đoán:
  - "phục vụ" = `M1_completed` (khách hoàn tất);
  - "bị ép" = có ≥ 1 quyết định có chứng nhận non-normal;
  - **8 ô có tắc** = W1, W2, W4, W5 × {w08, w17} (như phép quét); **10 ô có trôi** = W1–W5 × {w08, w17}.

## 5. Kiểm hợp lệ trước khi đọc kết quả

1. 48/48 `status: pass`, hoặc mỗi job hỏng được phân loại theo hằng thông điệp trong `failure-00.json`.
2. `audit_vep.py` qua mọi đối chiếu (cột `audit = ok`).
3. Mọi log thế giới: đổi mốc đúng `bin × 900 s`, mốc 0 bằng 1, hệ số giống nhau giữa các nhánh trên mốc chung (cách của
   `../sweep/sweep_worlds.py`), cùng `sourceScenarioContentSha256` trong một ô, cùng `repositoryInventorySha256 0da63eaf…`.

## 6. Dự đoán (viết trước khi chạy; sai thì báo sai)

| # | Dự đoán | Cơ sở |
|---|---|---|
| P1 | **Đối chứng bắt buộc.** Ở mọi (nhánh, thế giới, ô) mà bản (a) có 0 quyết định non-normal, bản (b) có chuỗi hành động đội xe **giống hệt** bản (a). Sai ⇒ coi là lỗi cài đặt, dừng và điều tra trước khi đọc kết quả | (b) chỉ đổi hành vi trên xe bị ép (ADR-077); quét no-worse: 6/6 đối chứng giống hệt |
| P2 | W0: cả 4 biến thể (`V-30`/`M-30` × a/b) có 0 quyết định non-normal và nhận **đúng cùng tập khách** với `C-30`, ở cả hai ô | không trôi thì x ≈ 0 nên z ≈ c; thí điểm W0: 4 nhánh có cổng giống hệt; quét D1: `C` và `M⁺` cùng tập ở W0 |
| P3 | `V-30(a)` và `M-30(a)` bị ép ở **mỗi** ô trong 10 ô có trôi (kể cả W3 và W5 tối, nơi `M⁺` không bị ép) | `V` tính \|x\| cả hai chiều; `M` có cận dưới; Hệ quả chiều trôi; thí điểm v1: 10/10 cho cả hai |
| P4 | Với mỗi nhánh `V-30`, `M-30`: tổng khách phục vụ trên 10 ô có trôi của (b) **lớn hơn** của (a), và (b) ≥ (a) ở ≥ 7/10 ô | (b) bỏ việc đóng băng; với `M⁺` (22 job điều trị): tổng 1874 so với 1864, (b) ≥ (a) ở 17/22 job, 5 job ngược chiều (`../sweep/noworse-jobs-2026-09-26.tsv`) |
| P5 | Đường miễn trừ mới được đi qua đầu-cuối: `V-30(b)` có ≥ 1 quyết định mang witness `forcedNoWorse` với mã `COMMITMENT_BUDGET_EXCEEDED` (cộng trên 10 ô có trôi); `M-30(b)` có ≥ 1 quyết định mang witness `forcedNoWorse` ở W3 (hai ô cộng lại), nơi mọi vi phạm hạn chót là ở cận dưới | với cơ sở nhìn thấy, khi trôi thuận lợi (e < v) một phép chèn có \|p − v\| ≤ \|e − v\| là "không tệ hơn"; với cận dưới, p ≥ giờ trả của tuyến giữ là "không tệ hơn" |
| P6 | **Tín hiệu H2 ở bước thăm dò này.** Tiêu chí: `C-30 − V-30(b)` ≥ 3 khách ở ≥ 6/8 ô có tắc. **Dự đoán: KHÔNG đạt.** Và tổng khách của `C-30` trên 8 ô có tắc ≥ tổng của `V-30(b)` | thí điểm (v1, (a)): chênh ≥ 3 chỉ ở 5/8 ô (W1 tối 3, W2 sáng 7, W2 tối 10, W4 sáng 4, W5 sáng 3); (b) đã thu hẹp khoảng cách của `M⁺`. Nhưng trần `V` còn cắn cả trên xe không bị ép, nên tổng vẫn nghiêng về `C` |
| P7 | E2 của `V-30(b)` ≤ E2 của `C-30` ở ≥ 5/8 ô có tắc | `V` chặn chính cái khách thấy; thí điểm (a): `V-30` thấp hơn hoặc bằng ở 6/8 |
| P8 | Tham khảo tất định: `V-30(a)` W4-w08 có chuỗi hành động đội xe giống hệt `E:\RideBoundData\research\tier3-world-v11-smoke\v11-V-30-W4` và phục vụ 92 khách | cùng Runner, WP4, wrapper, thế giới, ô; chỉ khác nhãn và inventory kho (không vào quyết định) |

Tiêu chí ở P6 ("≥ 3 khách ở ≥ 6/8 ô") chỉ dùng để đọc kết quả **của bước thăm dò này**. Nó không phải δ_b của H2 và không
chốt quy tắc quyết định H2. Nguồn: `../sweep/SWEEP-PLAN.md` §7 đã ghi rằng chênh 1–2 khách không phải hiệu ứng.

## 7. Không làm

- Không đổi thước đo, tiêu chí hay dự đoán sau khi chạy. Phân tích thêm sau khi xem thì ghi là mô tả, kèm ngày.
- Không chọn một thế giới hay một ô để kết luận "hơn".
- Không gọi chênh 1–2 khách là hiệu ứng.
- Không dùng panel A. Không chạy khi đang có job khác, không build `dotnet` khi job đang chạy.
- Báo **cả hai** kết quả (a) và (b), kể cả khi (b) làm số khách giảm.
- Nếu P1 sai: không diễn giải kết quả (b) cho tới khi tìm ra nguyên nhân.
