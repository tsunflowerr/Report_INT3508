# Việc B: khung 7:00–9:00, chỉ tắc đường đo thật, THĂM DÒ

Trạng thái: viết 2026-09-29 và niêm phong bằng SHA-256 (`W07-PLAN.sha256`) **trước mọi lần chạy trên ô w07**, kể cả lần chạy
thử của wrapper v1.2.

- Nguồn giao việc: `BAN-GIAO-PHIEN-2026-09-29.md` §9 việc B. Chủ nghiên cứu đã đồng ý ("Oke đấy") chạy phép thử chỉ dữ liệu
  thật ở khung 7:00–9:00.
- Mọi ô w07 thuộc panel phát triển (`claimClass: development-exploratory-only`). Kết quả là **mô tả thăm dò**, không phải
  xác nhận, và không chốt ngưỡng nào của H2, H3, T3.8, T3.9.
- Biết trước khi viết: kết quả Việc A (`../vm/analysis/full-2026-09-29-report.txt`, `describe-2026-09-29.txt`) và mọi kết
  quả của phép quét. **Chưa** có lần chạy nào trên ô w07.

## 1. Câu hỏi

Hai khung đã chạy (8:00–10:00 và 17:00–19:00) đều đã qua đoạn tắc đường tăng nhanh. Trong cùng tệp hệ số đo thật, khung
7:00–9:00 của ngày 12/11 và 13/11 có đỉnh tăng +47,8% và +54,4% so với đầu khung, bước 15 phút lớn nhất +10,6% và +13,4%, và
bước nhỏ nhất vẫn dương (+1,0% và +1,2%, tức tắc đường tăng suốt khung). Khung 8:00–10:00 của hai ngày ấy chỉ tăng +17,6% và
+15,4%, bước lớn nhất +7,1% và +3,7% (`../sweep/logs/traffic-windows-2026-09-29.txt`, tính với các mốc từ đầu tới cuối khung).

Luận văn hiện ghi: "trên tắc đường thật, từ mức lời hứa 1 phút không luật nào phá lời hứa" chỉ đúng cho hai khung đã chạy.
Việc B kiểm câu đó trên khung tắc tăng dốc nhất: hạn chót của Schulz và Pfeiffer (`M⁺-x`) có phá lời hứa của chính nó ở mức
1–2 phút trên dữ liệu thật hay không, trong khi số khách phục vụ của hai luật ra sao.

## 2. Ô và dữ liệu

| Mục | Giá trị |
|---|---|
| Lưới | `grid-w07-v1.json` (SHA-256 `df6727db…341e`), `gridId tier3-development-w07-v1`. Chép từ các ô w08 của `wp14-development\grid-v1.json`, chỉ đổi `cellId`, `scenarioId`, `sourceWindowStartSeconds` 25200, `sourceWindowEndSeconds` 32400, và hai nhãn |
| Nhãn chọn khách | **Nhãn mới** `ridebound-tier3-w07-v1-selection` và `…-pseudonymization`. Lý do: thứ hạng chọn khách chỉ phụ thuộc nhãn, tệp nguồn và số thứ tự dòng (`FleetPyManhattanNormalizer.cs:627-663`), không phụ thuộc khung; dùng lại nhãn WP14 sẽ chọn trùng nhiều khách giờ 8–9 với các ô w08 đã xem |
| 8 ô | `d2018111{2,3}-s10-r{1..4}-w07`, mỗi ô 108 yêu cầu, 8 xe sức chứa 4, 96 nút, 9.120 cung, cửa sổ đón 600 s, thời gian trên xe ≤ 1,5× đi thẳng. Số dòng đủ điều kiện 1.981–2.886 mỗi ô (`prepare-2026-09-29.log`) |
| Fixture | sinh bằng `tools/RideBound.Wp6Normalize` trong `C:\Code\RideBound-noworse` (normalizer source `34517a83…4d90`, khớp mọi fixture cũ; log `normalize-2026-09-29.log`), rồi chép ra `C:\RideBoundData\research\fixtures-w07-v1\` (`prepare_w07.py`) |
| Driver | `drivers/<ô>.driver.json`: driver w08 cùng (ngày, mẫu), chỉ đổi `scenarioId`, `sourceScenarioContentSha256`, `sourceScenarioHash` |
| Rò rỉ | `leakage-audit-2026-09-29.json`: 0 trùng với 40 ô đóng băng của `wp9-confirmatory\grid-v2.json` và `grid-v3-veh4.json` trên cả 7 trục |
| Trùng với w08 | **7–15 trên 108 khách** của mỗi ô w07 cũng được chọn ở ô w08 cùng (ngày, mẫu) (`prepare-2026-09-29.log`). Các ô w07 vì vậy **không độc lập** với các ô w08 đã xem |

## 3. Ma trận (88 job) và cài đặt

| Mục | Giá trị |
|---|---|
| Nhánh (11) | `U`; `C-30/60/120/300`; `Mplus-30/60/120/300`; `V-30`; `M-30` (`../configs/`, như phép quét và Việc A) |
| Thế giới | chỉ ngày đo thật của ô: `worlds/W5-d20181112-w07.json` (`5382a125…1633`) và `W5-d20181113-w07.json` (`fc2b4995…f924`); sigma = shockRate = 0; base {ngày của ô, exponent 1, windowStart 25200}. Như v1/v1.1, hệ số chỉ đọc trong [07:00, 09:00] và giữ nguyên giá trị 09:00 trong lúc xe chạy nốt khách |
| Wrapper | `../world/preflight_world_v1_2.py`: v1.1 cộng mốc 07:00 và phép chặn "ngày/khung của thế giới phải khớp ô". Test 24 kiểm, 0 lỗi; 9/9 đột biến bị bắt; v1 và v1.1 không đổi byte |
| Luật phục hồi | (b) cho mọi nhánh: Runner `C:\RideBoundData\research\runner-tier3-v2` (tree `ac251ef3…cff3f`) + `../configs/wp4-tier3-v2.json` (`66e9b592…4518`). `C` và `U` không bao giờ bị ép nên (b) không đổi gì với chúng |
| Chạy | `run_w07.py`: cwd `E:\Code\RideBound-deadline` (inventory `0da63eaf…4cbe`, truyền `--expected-repository-inventory-sha256`), 6 luồng, chỉ khi cắm sạc, output `C:\RideBoundData\research\tier3-w07-v1\`, log `logs/` mode `x`, công tắc `STOP` |
| Chạy thử trước | `../world/run_world_v12_smoke.py`: 4 job trên `d20181112-s10-r1-w07` (C-30 với ngày thật; hai thế giới kiểm rò rỉ; một job cố tình sai ngày phải bị từ chối). Nếu chạy thử không PASS thì **không** chạy ma trận |

## 4. Thước đo (như phép quét, cho mọi nhánh)

- `../sweep/sweep_analyze.job_row` (M1–M8), trỏ sang output này: số khách hoàn tất; E2; `A` = giờ trả thật − giờ trả hứa lần
  đầu; tỉ lệ `A > x` (lời hứa `M⁺-x` bị phá); tỉ lệ `C_r > x` (lời hứa `C-x` bị phá); quyết định non-normal; xe bị ép; lên xe
  muộn. Mỗi luật được chấm bằng cả thước của luật kia.
- So quyết định bằng chuỗi hành động đội xe đã xác nhận (`pilot_analyze.fleet_decisions`).
- Kiểm hợp lệ trước khi đọc: 88/88 `status: pass` hoặc phân loại lỗi; audit v/e/p `ok`; mọi log thế giới có dòng
  `version=v1.2`, dòng kiểm ngày khớp ô, đổi mốc đúng `bin × 900 s`; cùng hash kịch bản trong một ô; cùng inventory.

## 5. Dự đoán (viết trước khi chạy; sai thì báo sai)

| # | Dự đoán | Cơ sở |
|---|---|---|
| Q1 | **Bất biến.** Cả 32 job `C-x` có 0 quyết định non-normal | Định lý 4; 0/72 ở phép quét, 0/12 ở thí điểm. Sai ⇒ lỗi cài đặt, dừng |
| Q2 | `Mplus-30` bị ép (≥ 1 quyết định non-normal) ở ≥ 7/8 ô | tắc tăng suốt khung ở cả hai ngày; ngay ở 8:00–10:00 ngày 12/11 (dốc thấp hơn nhiều), `Mplus-30` đã bị ép ở 23,8% quyết định (`../sweep/sweep-jobs-2026-09-26.tsv`, `M5_nonNormalShare`) |
| Q3 | **Chính.** Ở x = 60 s, lời hứa của `Mplus-60` bị phá (tỉ lệ `A > 60 s` > 0) ở **≥ 4/8 ô** | 8:00–10:00 ngày 12/11: trễ lớn nhất so với lời hứa đầu 35,2 s với đỉnh tăng 17,6%; 7:00–9:00 có đỉnh tăng gấp khoảng 2,7–3,5 lần và bước lớn nhất gấp 1,5–3,6 lần. Đây cũng là dự đoán của phiên cũ ("M⁺ sẽ thất hứa ở 60–120 s"), ở dạng yếu hơn |
| Q4 | Ở x = 300 s: `Mplus-300` có 0 quyết định non-normal và tỉ lệ `A > 300 s` bằng 0 ở cả 8/8 ô | trôi của mỗi khách trên dữ liệu thật nhỏ hơn nhiều so với 5 phút (ước lượng thô ở Q3: tới cỡ 100 s) |
| Q5 | Số khách: với mỗi x ∈ {30, 60, 120, 300}, \|phục vụ(`C-x`) − phục vụ(`Mplus-x`)\| ≤ 2 ở ≥ 7/8 ô | với (b): `M⁺(b)` = `C` về số khách ở 21/22 job của quét no-worse; Việc A: `V-30(b)` = `C-30` ở 8/8 ô có tắc |
| Q6 | `V-30` bị ép ở 8/8 ô, và \|phục vụ(`V-30`) − phục vụ(`C-30`)\| ≤ 2 ở ≥ 7/8 ô | `V` tính \|x\| cả hai chiều; Việc A: `V-30(b)` bị ép ở 10/10 ô có trôi nhưng phục vụ đúng như `C-30` |
| Q7 | `C-30` phục vụ không nhiều hơn `U` ở ≥ 7/8 ô | cổng có giá: ở W0 mọi nhánh có cổng phục vụ ít hơn `U` 4–5 khách; chỉ 1/12 ô của thí điểm có `C-30` > `U` |

Không dự đoán: tỉ lệ `A > 120 s`; `M-30` so với `Mplus-30` (Việc A cho thấy dưới `C-30`, ngày thật 12/11 sáng vẫn có khách
đến sớm hơn lời hứa đầu quá 30 s, nên cận dưới của `M` có thể cắn cả khi tắc tăng); E2.

## 6. Không làm

- Không đổi thước đo hay dự đoán sau khi chạy; phân tích thêm thì ghi là mô tả, kèm ngày.
- Không gọi chênh 1–2 khách là hiệu ứng; mỗi ô một episode; không khoảng tin cậy.
- Không gọi kết quả là "xác nhận" hay "trên mạng đường Manhattan".
- Không dùng panel A. Không build `dotnet` khi job đang chạy. Không sửa `E:\Code\RideBound-deadline`.
