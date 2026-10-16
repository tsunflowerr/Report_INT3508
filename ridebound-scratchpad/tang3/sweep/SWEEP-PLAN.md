# Quét mức lời hứa: luật hành vi `C` so với hạn chót `M⁺` (kiểu Schulz và Pfeiffer), THĂM DÒ

Trạng thái: viết và niêm phong 2026-09-25 **trước khi chạy job nào** của quét này (xem `SWEEP-PLAN.sha256`).

- Chạy trên ô phát triển; mỗi (thế giới, ô) một episode.
- Mọi kết quả là mô tả thăm dò, không phải xác nhận.
- Người dùng yêu cầu: "đảm bảo có đủ thông số để so sánh… kiểm tra kĩ, đảm bảo công bằng cho cả hai".

## 1. Câu hỏi

Ở cùng một mức `x` (giây), khi quét `x` qua một dải rộng gồm cả mức 15 phút mà bài gốc dùng, hai luật khác nhau
ở đâu:
- `C-x`: tổng phần thay đổi giờ trả do điều phối gây ra của mỗi khách ≤ x;
- `M⁺-x`: giờ trả không muộn hơn lời hứa đầu + x, tức luật `l = B + L` của Schulz và Pfeiffer (2026) với L = x.

Hai luật được so trên bốn mặt: phục vụ, cái khách nhìn thấy, lời hứa của mỗi luật có giữ được không, và phục hồi.

## 2. Ma trận (156 job)

| Mục | Giá trị |
|---|---|
| Nhánh (13) | `U`; `C-x` và `Mplus-x` với x ∈ {30, 60, 120, 300, 600, 900} s. Cấu hình ở `../configs/`, sinh bằng `make_configs_sweep.py`; log `make_configs_sweep.log` chứng minh mỗi cặp `C-x`/`Mplus-x` chỉ khác đúng hai khóa: `dropEtaDeadlineSlackMs` và `limits[drop_eta_total_ms].hardLimit` |
| Thế giới (6) | W0–W5, **đúng các tệp** `../pilot/worlds/` của T3.7. Gồm cả W3 (giao thông giảm), nơi Chương 3 nói hạn chót một chiều có thể phục vụ nhiều hơn; W3 được giữ để công bằng cho `M⁺` |
| Ô (2) | `d20181112-s10-r1-w08`, `d20181112-s10-r1-w17` (panel phát triển `wp14-development-panel-v1`), 108 yêu cầu, 8 xe |
| Thế giới cài đặt | **v1.1** (`../world/preflight_world_v1_1.py`): đổi khung đúng `bin × 900 s` ở mọi nhánh; smoke đầu-cuối PASS |
| Runner | `E:\RideBoundData\research\runner-tier3-v1` (từ `69512d3`), cùng cho mọi nhánh |
| WP4 | `../configs/wp4-tier3-v1.json`, cho mọi nhánh: `commitmentRecovery: forced-reference-v1` (luật phục hồi (a)) và `lateBoarding: record-v1` |
| Output | `E:\RideBoundData\research\tier3-sweep-v1\<job>`; không ghi đè; log mode `x`; chỉ chạy khi cắm sạc |

## 3. Công bằng: cái gì giống, cái gì khác

**Giống nhau cho cả hai luật:**
- bộ sinh phương án và hàm mục tiêu (accepted → cost → id);
- cấu trúc giới hạn (không đổi xe, không đổi điểm dừng), khóa pha và cửa sổ đón;
- thời gian đi tối đa, luật phục hồi, luật lên xe muộn;
- dữ liệu, hạt giống và thế giới.

**Cả hai so theo kiểu "vượt mới loại":**
- trần `C`: `afterValue > hardLimit` (`CommitmentBudgetEvaluator.cs:88`);
- hạn chót `M⁺`: `shift > slack` so với lời hứa đầu (`CommitmentLockEvaluator.cs:186-191`).

**Khác biệt còn lại so với bài gốc** (áp như nhau cho cả hai luật; phải ghi khi viết):
- không có mô hình khách từ chối lời mời `e^(−µ·RD)`;
- không có thuật toán chèn/tái tối ưu của họ, kể cả việc chuyển khách giữa các xe (ở đây cấm đổi xe cho cả hai);
- dữ liệu Manhattan thay vì Hamburg;
- có cửa sổ đón và thời gian đi tối đa.

Luật phục hồi (a) làm xe "đóng băng" chỉ khi `M⁺` bị ép. Gánh này được báo riêng (M5), và mọi so sánh ở mức có
phục hồi phải đọc kèm nó.

## 4. Thước đo (tính cho MỌI nhánh, kể cả thước đo có lợi cho luật kia)

| Mã | Thước đo | Ghi chú |
|---|---|---|
| M1 | số khách hoàn tất trên 108 | |
| M2 | E2 = tỉ lệ khách có V giờ trả > 60 s; CVaR₉₅ của V | cái khách thấy qua các lần công bố |
| M3 | **độ trễ thật so với lời hứa đầu** `A = giờ trả thật − giờ trả hứa lần đầu`: trung bình, p95, max; tỉ lệ `A > x` (= **lời hứa của `M⁺-x` bị phá**); tỉ lệ `A > 60/300/900 s` | thước đo luật `M⁺` bảo vệ. Giờ trả thật = `simTimeMs` của lô chứa `passengerAlighted`; đã kiểm với giờ đón: 102/102 khớp `actualPickupTimeMs` |
| M4 | phần do điều phối `C_r`: max; tỉ lệ `C_r > x` (= **lời hứa của `C-x` bị phá**) | thước đo luật `C` bảo vệ |
| M5 | tỉ lệ quyết định non-normal, tỉ lệ khách có breach forced, tỉ lệ đội xe bị ép trung bình | phục hồi |
| M6 | số lần lên xe muộn, trễ lớn nhất | |
| M7 | tỉ lệ quyết định có xe còn ≥ 3 phương án sau cổng | |
| M8 | wall time | |
| P | cặp `C-x`/`M⁺-x` cùng (thế giới, ô): tập khách có trùng không; trên khách chung, so M3 và V | tách phần do chọn khách |

## 5. Kiểm hợp lệ trước khi đọc kết quả

1. 156/156 `status: pass`, hoặc mỗi job hỏng có lý do.
2. `audit_vep.py` qua mọi đối chiếu.
3. Mọi log thế giới: đổi khung đúng `bin × 900 s`; hệ số giống nhau giữa các nhánh.
4. Cùng `sourceScenarioContentSha256` giữa các nhánh trong một ô.

## 6. Dự đoán (viết trước khi chạy; sai thì báo sai)

| # | Dự đoán | Cơ sở |
|---|---|---|
| D1 | W0 (không nhiễu thế giới): ở **mọi** x, `C-x` và `M⁺-x` nhận **đúng cùng một tập** khách, cả hai ô | x = 0 thì c = z; bộ sinh chỉ chèn nên c ≥ 0 (0/479 kéo sớm); Tầng 2 k = 0: 20/20 ô trùng ở 30 s |
| D2 | x = 900: `C-900`, `M⁺-900` và `U` nhận đúng cùng một tập khách ở **mọi** (thế giới, ô) | thí điểm (v1): dưới `U`, trễ so với lời hứa đầu tối đa 498,7 s và phần do điều phối mỗi khách tối đa 331,9 s, đều < 900 s |
| D3 | `C-x` có 0 quyết định non-normal và 0 breach forced ở mọi x, mọi thế giới | Định lý 4 |
| D4 | `M⁺-x` có phục hồi forced ở x = 30 trong W1, W2, W4, W5 (cả hai ô); **không** có ở W0 và W3 với mọi x; không có ở mọi thế giới với x ≥ 600 | trôi thuận/ngược chiều; trễ tối đa dưới `U` < 600 s |
| D5 | Ở x = 30, số khách hoàn tất `C-30` ≥ `M⁺-30` ở ≥ 6/8 (thế giới, ô) thuộc W1, W2, W4, W5 | thí điểm (v1): ≥ ở 12/12 |
| D6 | W3: `M⁺-x` hoàn tất ≥ `C-x` ở mọi x, cả hai ô | Hệ quả chiều trôi (Chương 3) |
| D7 | Ở x ≤ 120 trong W1, W2, W4, W5: tỉ lệ `A > x` của `M⁺-x` **>** 0 (lời hứa của họ bị phá khi bị ép), nhưng ≤ tỉ lệ `A > x` của `C-x` ở ≥ 6/8 (thế giới, ô) cho mỗi x | `M⁺` chặn trễ so với lời hứa đầu; `C` thì không |

## 7. Không làm

- Không đổi thước đo hay dự đoán sau khi chạy.
- Không chọn một mức x để kết luận "hơn".
- Không gọi khác biệt 1–2 khách là hiệu ứng: một episode mỗi ô, nhiễu cỡ ±2 khách đã thấy ở thí điểm.
- Không dùng panel A.
- Luật phục hồi (b) chỉ cài nếu vùng x có phục hồi cho thấy (a) quyết định kết quả; khi đó là một ADR riêng và chạy
  riêng vùng đó.
