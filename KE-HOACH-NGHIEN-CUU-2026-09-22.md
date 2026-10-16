# RideBound — Kế hoạch nghiên cứu end-to-end

**Lập ngày:** 2026-09-22
**Người thực hiện:** Trần Quang Thành — 23020155 — K68I-IT2, UET/VNU
**Trạng thái tài liệu:** kế hoạch, chưa authorize execution. Không tài liệu nào trong
kho `E:\Code\RideBound` bị thay đổi bởi tài liệu này.

---

## 0. Cách đọc tài liệu này

Tài liệu này là **kế hoạch thực thi**, không phải báo cáo kết quả. Nó được viết để một
người khác (hoặc một trợ lý lập trình khác) có thể cầm lên và thực hiện mà không cần
hỏi lại.

Quy ước:

| Ký hiệu | Nghĩa |
|---|---|
| ✅ ĐÃ ĐO | Con số đã có từ bằng chứng niêm phong, không cần chạy lại |
| 🔬 CẦN CHẠY | Phải chạy mô phỏng mới |
| ✍️ CHỈ VIẾT | Không tốn lần chạy nào |
| ⚠️ CỔNG | Có rào cản quản trị hoặc kỹ thuật phải vượt trước |
| ❌ KHÔNG LÀM | Đã bị loại, kèm lý do |

**Thứ tự đọc bắt buộc trước khi thực thi bất cứ mục nào:** §1 → §3 → §5 → §7.
§7 là các cổng quản trị; bỏ qua nó thì mọi số đo sau đó đều không dùng được.

---

## 1. Bối cảnh: hệ thống đang ở đâu

### 1.1 Cơ chế

RideBound là hệ điều phối xe đi chung có thêm một cơ chế: **lời hứa có biên được chứng
nhận**. Mỗi lần hệ công bố lại giờ đón/giờ trả cho một khách, độ dời được ghi vào một
sổ cái riêng của khách đó, cộng dồn và đơn điệu không giảm, đối chiếu với một trần `β`.
Phương án nào làm vượt trần bị **xóa khỏi tập lựa chọn ngay tại thời điểm ra quyết
định**, không phải bị phạt điểm.

Điểm phân biệt cốt lõi là **phân rã theo nguyên nhân**. Mỗi lần công bố có ba mốc:

| Ký hiệu | Tên | Định nghĩa |
|---|---|---|
| `v` | previous | lời hứa đã công bố lần trước |
| `e` | exogenous | chính lời hứa đó, **chiếu lại từ vị trí thật hiện tại của xe**, giữ nguyên lộ trình và phân công |
| `p` | proposed | lời hứa mà phương án đang xét sẽ tạo ra |

Ba đại lượng dẫn xuất, tính trên từng lần công bố:

```
A = |p − e|   conduct  — do quyết định của nhà điều hành
d = |e − v|   drift    — do thế giới vật lý
B = |p − v|   visible  — cái khách thực sự nhìn thấy
```

Cộng dồn qua toàn bộ chuỗi công bố của một khách:

```
C = Σ A     X = Σ d     V = Σ B
E  = |q_T − q_0|          (độ lệch hai đầu)
D⁺ = max(0, q_T − q_0)    (chỉ phần muộn, tức "hạn chót")
```

Quan hệ (đã kiểm chứng số, xem §5.1):

```
D⁺  ≤  E  ≤  V  ≤  C + X
```

**`β` chặn `C`.** Không chặn `V`, `E`, hay `D⁺`.

### 1.2 Trạng thái thực nghiệm

| | |
|---|---|
| Số lần chạy mô phỏng | 558, 33,62 GB bằng chứng niêm phong |
| Panel chính A | `wp9-confirmatory-fixed-panel-v2` — 20 ô, 108 yêu cầu, **8 xe** |
| Panel B | `wp9-confirmatory-fixed-panel-v3-veh4` — 20 ô, **4 xe** |
| Panel phát triển | `wp14-development-panel-v1` — **16 ô**, hai khung giờ `w08`/`w17` |
| Dữ liệu | chuyến đi công khai Manhattan (NYC TLC), cửa sổ đón 600 s |
| Hạt giống | master seed 7 ở mọi lần chạy; `solverSeedsAreReplicates: false` — bộ giải **tất định** |
| Kết quả trung tâm | B1 1.735 khách (80,32%) → C1 1.581 (73,19%), **−7,13 pp**; gánh nặng 74.443 s → 128 s (**−99,8%**) |
| Panel B | −4,91 pp |
| Panel phát triển (v6, 160 job) | b1-ref 94,27% → c1 88,77%, **−5,50 pp** |

**Lưu ý về "nhiều seed":** hệ tất định, nên lặp lại **không** đến từ seed mà từ **20 ô
= 5 ngày × 4 mẫu nhu cầu**. Yêu cầu "chạy nhiều seed" trong các bản kế hoạch trước là
hiểu sai kiến trúc thí nghiệm; cái thiếu là **nhiều mức nhu cầu và nhiều cỡ đội xe**,
và hai cỡ đội xe thì **đã có** (8 và 4).

### 1.3 Ba định lý hiện có

- **ĐL 3.1** — cơ sở hành vi luôn thỏa được: phương án không-làm-gì có `A = 0`.
- **ĐL 3.2** — cơ sở kết quả có thể vô nghiệm: phương án không-làm-gì có `B = d > 0`.
- **ĐL 3.3** — cơ sở kết quả không mở rộng tập quỹ đạo khả thi. *(Đã sửa 2026-09-21:
  phát biểu lại trên tập quỹ đạo và chính sách tối ưu, thêm điều kiện (H) `A ≤ B` có
  đo đạc — xem §5.2.)*

### 1.4 Tám hướng đã thử và bị bác bỏ

Đệm ETA đồng loạt (tỉ lệ 12:1); hứa theo hạn chót *(lý do loại đã được chứng minh là
sai — xem §2.3)*; cổng mềm; nới cửa sổ đón đồng loạt (−7,13 → −8,56 pp); xếp hạng vị
trí chèn; cắt tỉa sớm; bộ sinh sắp xếp lại (hỏng 18/20 ô); đặt trước ngân sách (mức C,
giống hệt đối chứng trên 20/20 ô).

---

## 2. Vị trí trong văn liệu, tính đến 09/2026

### 2.1 Bảy công trình gần nhất

| Công trình | Đối tượng hứa | Sửa được sau khi hứa? | Sổ cái cộng dồn | Quy trách nguyên nhân | Cưỡng chế lúc quyết định |
|---|---|---|:-:|:-:|:-:|
| Alonso-Mora và cs. 2017 (PNAS) | — (chỉ Ω, Δ nội bộ) | tự do | ✗ | ✗ | ✗ |
| **Fielbaum & Alonso-Mora 2020** (TR-C 121) | điểm (chỉ **đo**) | tự do; §6 đóng băng nhị phân | ✗ | ✓ định tính | chỉ ở kịch bản §6 |
| Sharif Azadeh và cs. 2022 (TR-B 161) | **hộp tĩnh** (cửa sổ + `L^Max`) | bên trong hộp: tự do | ✗ | ✗ | ✓ |
| Haferkamp 2024 | **nhiều lựa chọn giờ đón**, khách chọn | ràng buộc sau khi chọn | ✗ | ✗ | ✓ |
| Ackermann & Rieck 2025 (OR Spectrum) | — | multiple plan, **least-commitment** | ✗ | ✗ | ✓ hard TW |
| **Schulz & Pfeiffer 2026** (OR Spectrum 48:541–586) | **hạn chót `l`**, báo cho khách | trượt tới `l` | ✗ | ✗ | ✓ |
| Schmidt–Golak–Schulz–Fliedner 2026 (TSP-SC) | một giờ đến, công bố **một lần** | không sửa | ✗ | ✗ | ✓ |
| Sivagnanam và cs. 2026 (ICCPS) | **chỉ "sẽ được phục vụ"** | giờ tự do trong cửa sổ | ✗ | ✗ | ✓ |
| Zalesak và cs. 2025 | — | swapping / cyclic exchange | ✗ | ✗ | — |
| **Elmi, Moylan, Alonso-Mora, Fielbaum 2026** (TR-C 192:105897) | điểm, **bảo đảm không đổi** cho nhóm chọn lọc | nhóm còn lại: tự do | ✗ | ✗ | ✓ |
| **RideBound** | điểm + **sổ cái cộng dồn 10 chiều** | có trần `β` | **✓** | **✓ định lượng** | **✓** |

### 2.2 Đối thủ nguy hiểm nhất và ranh giới chính xác

**Elmi, Moylan, Alonso-Mora & Fielbaum (2026)**, *"Improving ridepooling reliability
using shareability shadows"*, **TR-C 192:105897**, nhận 16/01/2026, chấp nhận
24/07/2026, trực tuyến **04/08/2026**. Đồng tác giả là **chính nhóm** viết bài 2020 mà
khóa luận lấy làm mốc.

Cơ chế của họ: dự báo *Shareability Score* cho từng khách **tại thời điểm phân công**,
rồi **quản lý slack** — khách điểm thấp được **0%** slack (bảo đảm tuyệt đối không đổi
giờ), khách điểm cao được **100%** slack.

Kết quả (Bảng 2, trang 19), cùng tỉ lệ từ chối ~29%:

| | Ordinary control | Shadow control |
|---|---:|---:|
| % khách bị tăng tổng trễ | 63,17% | **15,39%** |
| Trễ tăng trung bình **trong nhóm bị ảnh hưởng** | 0,84 ph | **3,74 ph** |
| Số lần bị tăng nhiều nhất | 2 | **5** |
| **Trung bình toàn dân số** (suy ra) | ~0,576 ph | ~0,531 ph |

⟹ **Cơ chế của họ PHÂN PHỐI LẠI gánh nặng, gần như không giảm tổng.**

**Ba câu trong bài họ bảo vệ khóa luận:**

1. Thước đo của họ là **hai đầu**, không phải chuỗi — phương trình (1), §2.1.3:
   *"a passenger can experience several changes throughout a single trip, each of which
   holds a unique value, but Eq. (1) is the result of all changes, i.e., **the final
   values at the moment of drop off**."*
2. Họ cố ý chỉ xử lý **lần đổi đầu tiên** — §2.4.1: *"while in this work we adjust the
   slack immediately after the initial assignment to control the occurrence of **the
   first change**, a similar mechanism could be applied after the first change to
   control the second change, and so on. However, we focus on the first change."*
3. Câu quan trọng nhất — §2.4.1: *"Such a guarantee **would not be possible if even a
   single change were allowed**, as passengers would still face uncertainty."*

**Câu 3 là phản đề của cả khóa luận.** Họ khẳng định bảo đảm chỉ tồn tại khi cấm tuyệt
đối. RideBound đưa ra bảo đảm **có mức** — cho phép thay đổi nhưng chặn tổng — và đo
được giá của nó.

**Và mô hình của họ dùng mạng đi lại TĨNH** ⟹ trong khung của họ **không tồn tại trôi
dạt ngoại sinh**, nên mốc `e`, đẳng thức phân rã, hai cơ sở tính và ĐL 3.1–3.3 **không
thể phát biểu được**.

### 2.3 Hàng xóm gần nhất về cơ chế

**Schulz & Pfeiffer 2026** có gần đủ bộ khung: lời hứa `l_i⁻ = B_i⁻ + l` **báo cho
khách**, trần trượt `l` mặc định 900 s, quét `l ∈ {0,5,…,30}` phút, sửa tuyến, đo độ
trượt thực tế (181,7 s → 279,9 s khi bật repair).

Khác biệt: `l` là **hạn chót một chiều tuyệt đối**, không phải sổ cái — khách bị dời 14
lần trong `l` vẫn tính **0**; `l` là **hằng số toàn cục**; **không quy trách**; **không
hứa giờ đón** và không có cửa sổ đón, nên tập phương án của họ không bao giờ rỗng.

> ⚠️ **Đính chính bắt buộc cho mục 8.2 của tài liệu bàn giao.** Hướng "hứa theo hạn
> chót thay vì theo điểm" bị loại với lý do *"đây chính xác là cửa sổ Ω và Δ đã có
> sẵn"*. **Lý do đó sai.** Hạn chót được *công bố* khác hẳn cửa sổ khả thi *nội bộ*, và
> Schulz & Pfeiffer đã dựng cả một bài OR Spectrum trên đúng cơ chế đó. Mục 8.2 phải
> được viết lại, và hạn chót phải trở thành **một nhánh đối chứng bắt buộc** (§8.5).

### 2.4 Trích dẫn phải sửa

| Chỗ | Lỗi | Sửa thành |
|---|---|---|
| Mục 11 & 10.5 tài liệu bàn giao | `arXiv:2504.10649` mô tả là *"LRP prefix-freezing + Definition 6.1 stability"* | Bài thật là Zalesak, Hu, Samaranayake 2025, *"Ride-pool Assignment Algorithms"*. **LRP = "Limit and Recall Prefix"**, một heuristic cho **CTSP oracle**. `freez`/`frozen` xuất hiện **0 lần**. Định nghĩa 6.1 là **ổn định của bộ giải**, không phải ổn định lời hứa |
| `10-tai-lieu.tex` | DOI bị hoán giữa time-consistent DARP và multiple-plan DARP (Codex phát hiện) | Đối chiếu lại `10.1002/net.22063` và `10.1007/s00291-025-00809-y` |

Ba bài phải **thêm** vào Chương 1: Schulz & Pfeiffer 2026, Elmi và cs. 2026,
Sivagnanam và cs. 2026. Nên thêm: Haferkamp 2024, TSP-SC 2026, Zalesak và cs. 2025.

### 2.5 Món quà từ Zalesak và cs. 2025

Định nghĩa 6.1 của họ (*"the original route `S_v` and the updated route
`H(T(S_v,Δt),R)` have the same ordering for their common nodes"*) gần như trùng khít về
hình thức với chiều `incumbent_order_inversion_count = 0` của RideBound. Và họ đưa ra
một **lập luận hiệu quả** cho việc bảo toàn thứ tự: Hình 7 cho thấy heuristic chèn đảo
hai điểm trả khi tính lại, và cú đảo đó làm một lần chèn về sau **bất khả thi**. Kết
luận nguyên văn: *"an unstable heuristic, compared to a stable one, is **less likely to
find a solution when new requests are added in future epochs**."*

⟹ Một nhóm độc lập (Samaranayake, 2025) tìm ra rằng **giữ nguyên thứ tự khách cũ giúp
tỉ lệ phục vụ**, vì lý do tính toán. Ràng buộc của RideBound không thuần túy là gánh
nặng.

Họ cũng cho một con số hiệu chuẩn: **8 phút nhìn trước tương lai nâng tỉ lệ phục vụ từ
63,5% lên 70,6%** (full RTV) và 62,3% → 69,5% (LA). ⚠️ **Không được** trừ con số này
vào −7,13 pp của RideBound: khác instance, khác đội xe, và *biết trước thật* ≠ *dự báo*.

---

## 3. Chẩn đoán: cái gì thật sự phân biệt

Đây là phần quan trọng nhất của tài liệu. Nó dựa trên **chín phép đo mới** chạy trên
chính bằng chứng niêm phong trong hai ngày 2026-09-16 → 2026-09-22. Toàn bộ script nằm
ở `ridebound-scratchpad/claude-measurements-2026-09/`.

### 3.1 ✅ ĐÃ ĐO — Phân rã là **bất đẳng thức**, không phải đẳng thức

Kiểm `A + d = B` ở mức **từng lần công bố** (chiều `drop_eta_total_ms`):

| | B1 | C1 |
|---|---:|---:|
| Số lần công bố | 54.311 | 45.542 |
| `A + d = B` đúng chính xác | 54.083 (**99,58%**) | 45.539 (99,99%) |
| Số lần **cả hai** `A>0` và `d>0` | **476 (0,88%)** | 11 |
| — trong đó đẳng thức **hỏng** | **228 → 47,9%** | 3 → 27,3% |
| Độ hụt khi hỏng: trung vị / cực đại | 168 ms / 1.380 ms | — / 208 ms |
| **Độ hụt trên tổng** | **0,0748%** | **0,0059%** |

**Đọc đúng:** con số 99,58% là ảo. Trong **99,12%** số lần, một trong hai đại lượng bằng
0, nên phép cộng đúng một cách tầm thường. Phép kiểm thật chỉ có ở 476 lần, và ở đó nó
**hỏng gần một nửa**.

**Cơ chế hỏng:** khi trôi dạt kéo `e` **sớm** hơn `v` còn quyết định đẩy `p` **muộn** hơn
`e`, hai hiệu ngược dấu triệt tiêu một phần và `B = A − d`. Khi đó phần hụt **đúng bằng
`2d`**. Ca thật, ô `d20181114-s10-r1`, khách `rq-acbbcd86c…`, lần công bố thứ 13:

```
       e            v                                              p
  00:15:09.253  00:15:09.943                                 00:16:39.497
       |<-0,690s--->|                                              |
       |<---------------------- A = 90,244 s --------------------->|
                    |<-------------- B = 89,554 s ---------------->|
                                        hụt = 2 × 0,690 = 1,380 s
```

Trôi dạt trên panel chính đến từ **độ trễ thực thi** (đồ thị thời gian di chuyển tĩnh),
cỡ phần nghìn tới phần mười giây, nên phần hụt cỡ **2 × vài trăm ms**. Đó là toàn bộ lý
do con số 0,0748% nhỏ — **không phải vì công thức đúng**.

### 3.2 ✅ ĐÃ ĐO — Điều kiện `A ≤ B` của ĐL 3.3 hỏng 0,42%

| | B1 | C1 |
|---|---:|---:|
| `A < B` | 52.345 (96,38%) | 43.958 (96,52%) |
| `A = B` | 1.738 (3,20%) | 1.581 (3,47%) |
| **`A > B` — vi phạm (H)** | **228 (0,42%)** | 3 (0,007%) |
| vượt nhiều nhất | 690 ms | 104 ms |

Tập vi phạm (H) **trùng khít** tập làm hỏng đẳng thức — tất yếu, vì cùng một hình học.

### 3.3 ✅ ĐÃ ĐO — Bằng chứng mạnh nhất là phép thử giả dược

Chính sách điều phối **không thể** tác động lên giao thông. Nếu phép tách sai, `d` sẽ
trôi theo chính sách.

| | B1 | C1 | Thay đổi |
|---|---:|---:|---:|
| `C` (conduct, cả chuỗi) | 64.863.133 ms | 128.020 ms | **507 lần** |
| `X` (exogenous, cả chuỗi) | 6.719.286 ms | 6.694.740 ms | **0,37%** |

Cái lẽ ra phải đứng yên thì đứng yên; cái lẽ ra phải phản ứng thì phản ứng. **Đây phải
là luận cứ chính, thay cho đẳng thức.**

### 3.4 ✅ ĐÃ ĐO — Bảo đảm hai lớp **đã quan sát được**

Trần chỉ cam kết `C ≤ 30 s`. Nhưng phân bố `V` (cái khách thực sự nhìn thấy, cộng dồn
cả chuyến):

| `V` mỗi khách | B1 | **C1** |
|---|---:|---:|
| trung vị | 3,6 s | 3,4 s |
| p90 | 160,0 s | **8,1 s** |
| p99 | 441,3 s | **21,0 s** |
| **cực đại** | 585,1 s | **38,7 s** |
| số khách vượt 30 s | 375/1735 = **21,6%** | **4/1581 = 0,3%** |

⟹ `C ≤ 30 s` ∧ `X_max ≈ 8,7 s` ⟹ `V_max = 38,7 s`. **99,7% khách có tổng biến động
nhìn thấy dưới 30 giây.**

Đây là câu trả lời cho phản biện *"khách đâu quan tâm lỗi do ai"*, và nó **đã có sẵn**.

> ⚠️ `X` trên panel này là **độ trễ thực thi**, không phải tắc đường. Con số `γ ≈ 8,7 s`
> **không** dùng được cho hệ thật. Xem §3.7 và §8.6.

### 3.5 ✅ ĐÃ ĐO — Nhu cầu dịch chuyển **không chia được**

| Độ lớn từng lần dời (n = 479, B1) | p10 | p25 | **p50** | p75 | p90 | max |
|---|---:|---:|---:|---:|---:|---:|
| giây | 28,1 | 68,3 | **115,6** | 188,7 | 267,8 | 511,6 |

- **89,1%** số lần dời **lớn hơn toàn bộ trần** β = 30 s.
- **358/403** khách bị ảnh hưởng có **lần dời đầu tiên** đã một mình làm vỡ trần.
- Trung bình **1,19** lần dời trên mỗi khách bị ảnh hưởng (332/403 đúng một lần).
- **373/425** quyết định gây dời chỉ đụng **đúng một** khách; trung vị 125,1 s.

Phương án bị cổng loại (n = 780) vượt trần **trung vị 113,1 s**; nới trần thêm 30 s chỉ
cứu **8,1%**.

⟹ **Không có đuôi "suýt lọt".** Mọi cơ chế định giá / tiết kiệm ngân sách / online
knapsack đều vô nghĩa ở đây: đây không phải knapsack nhiều món nhỏ, mà là **một cục
không chia được lớn gấp bốn lần cái hộp**.

### 3.6 ✅ ĐÃ ĐO — Hai lỗi phân tích phải sửa

**(a) Con số "96% chỉ có một ứng viên" bị pha loãng.**

| | B1 | C1 |
|---|---:|---:|
| Tổng số epoch | 14.133 | 13.084 |
| Epoch **có** nhận/từ chối khách | 2.142 (**15,2%**) | 2.143 (16,4%) |
| Tập lựa chọn xe chỉ 1 ứng viên — **mọi epoch** | 96,04% | 95,87% |
| Tập lựa chọn xe chỉ 1 ứng viên — **epoch hoạt động** | **73,84%** | **74,76%** |
| Epoch hoạt động có ≥1 xe với ≥2 ứng viên | **80,4%** | 79,9% |

85% số epoch không có yêu cầu nào đến. Kết luận *"hệ không có gì để chọn, nên mọi cơ chế
tác động lên khâu chọn đều bất lực"* **không đứng vững**. Kết luận đúng vẫn là "khâu
chọn không phải chỗ nghẽn", nhưng lý do là §3.5, không phải độ mỏng.

**(b) `worst-hard-utilization-ppm` là một HẰNG SỐ.**

`HardVectorCandidateAssessor.cs:316–331`:

```csharp
if (hardLimit == 0) { ...; worst = PartsPerMillion; continue; }   // = 1_000_000
```

Và mọi cấu hình cam kết đều có `vehicle_switch_count`, `pickup_stop_switch_count`,
`drop_stop_switch_count` với `hardLimit = 0` (xác minh trên
`wp14-c1-h6-reference-v1.json`).

⟹ Chỉ số bị ép bằng **1.000.000 cho mọi phương án, mọi quyết định**. Khớp với probe:
*nonzero 13.004/13.004* **và** *degenerate 13.004/13.004*.

**Hệ quả:** lời giải thích ở mục 8.8 (*"tầng trên khác 0 trong 100% quyết định nên tầng
dưới không lên tiếng"*) **sai** — tầng đó không bao giờ lên tiếng vì nó hòa vĩnh viễn.
Và trong số các phương án đã qua cổng, C1 thực tế chọn theo `operational-cost`, **không**
theo chi phí lời hứa. Toàn bộ tầng mục tiêu nhận biết cam kết đang bị vô hiệu hóa.

### 3.7 ✅ ĐÃ ĐO — **Kết quả quyết định**: dưới trôi dạt thật, hai cơ chế tách hẳn nhau

Đây là phép đo quan trọng nhất trong toàn bộ tài liệu.

**Trên panel tĩnh (không trôi dạt)**, chặn theo hai đầu `D⁺` và chặn theo chuỗi conduct
`A` gate **gần như cùng một tập khách**:

| Ngưỡng (B1) | vượt `D⁺` | vượt `A` | vượt `V` |
|---:|---:|---:|---:|
| 30 s | 369 (21,3%) | **369** (21,3%) | 375 (21,6%) |
| 60 s | 340 | 341 | 349 |
| 120 s | 229 | 230 | 236 |
| 300 s | 48 | 48 | 49 |

Lý do: bộ sinh chèn **chỉ đẩy muộn, không bao giờ kéo sớm** (`decisionMovedEarlier = 0`
trên 421.752 lần sửa), nên chuỗi conduct ≈ hiệu hai đầu.

**Nhưng dưới trôi dạt Manhattan thật (k = 1, `wp14/drift-v1`, 9 ô hoàn tất, 583 khách):**

| | `dr-conduct-k0` (20 ô, 1581 khách) | **`dr-conduct-k1` (9 ô, 583 khách)** |
|---|---:|---:|
| `D⁺` (hai đầu) | 126 s | **6.964 s** |
| `E` | 326 s | 7.072 s |
| `V` (chuỗi) | 6.822 s | 10.101 s |
| **`C` (conduct)** | 128 s | **27 s** |
| `X` (exogenous) | 6.695 s | 10.074 s |
| Khách vượt 30 s theo **`D⁺`** | 0 | **60** |
| Khách vượt 30 s theo **`A` (conduct)** | 0 | **0** |
| `|gate_D \ gate_A|` | 0 | **60** |

> **Dưới trôi dạt thật, một trần theo hạn chót kiểu Schulz sẽ chặn 60 khách (10,3%)
> hoàn toàn vì tắc đường, trong khi trần conduct chặn 0 — vì nhà điều hành thực sự chỉ
> gây ra 27 giây trên 583 khách.** Tỉ lệ `X/C = 373:1`.

⟹ **Đây, chứ không phải total variation, mới là điểm phân biệt có bằng chứng.** Sự khác
biệt giữa RideBound và mọi cơ chế outcome-flavoured (`D⁺`, `E`, `V`) **bằng không trên
mạng tĩnh và bùng nổ dưới trôi dạt thật.**

⚠️ **Ranh giới:** đây là phép đo **hậu nghiệm** trên quỹ đạo đã chạy dưới cổng conduct;
nó là **giả thuyết mạnh**, không phải kết quả đối chứng. Thí nghiệm đối chứng là §8.7.
Và chỉ **9/20 ô** hoàn tất ở k=1 — 11 ô còn lại chết vì bất biến miền (§4.3).

### 3.8 ✅ ĐÃ ĐO — Đuôi và tập trung gánh nặng

| | B1 | C1 |
|---|---:|---:|
| Tổng `A_r` | 64.863 s | 128 s |
| Số khách `A_r = 0` | 1.332 (**76,8%**) | 1.570 (**99,3%**) |
| p90 / p95 / p99 | 155,5 / 235,3 / 421,9 s | 0 / 0 / 0 |
| **cực đại** | **573,5 s** | **27,6 s** |
| **CVaR₉₅** | **336,5 s** | **1,6 s** |
| CVaR₉₉ | 473,4 s | 8,0 s |
| top 5% khách gánh | 44,8% tổng | — |
| top 10% khách gánh | 70,6% tổng | — |
| top 20% khách gánh | 97,7% tổng | — |

> ⚠️ **Bẫy Gini.** Gini **tăng** từ 0,8569 lên **0,9963** khi đi từ B1 sang C1 — tức
> chỉ số bất bình đẳng tương đối nói C1 *tệ hơn*, trong khi C1 tốt hơn cho **mọi** khách.
> Nguyên nhân: 99,3% giá trị bằng 0. **Không dùng Gini/Lorenz cho đại lượng gánh nặng
> có nhiều số 0.** Dùng **đo tuyệt đối ở đuôi**: max, p95, p99, CVaR.

So sánh hình dạng với Elmi và cs. (không so số tuyệt đối — khác mẫu số, khác mạng):

| | Elmi 2026 | RideBound |
|---|---|---|
| Số người bị đụng | 63,17% → 15,39% (÷4,1) | 23,2% → 0,7% (÷33) |
| Gánh nặng của người **bị đụng** | 0,84 → **3,74 ph** (×4,5, **tệ đi**) | CVaR₉₅ 336,5 → **1,6 s** (÷210, **tốt lên**) |
| Số lần bị đổi nhiều nhất | 2 → **5** (tệ đi) | — |
| Tổng gánh nặng | ~không đổi | **−99,8%** |
| Giá phải trả | ~0 pp tỉ lệ từ chối | **−7,13 pp** |

⟹ Hai triết lý khác nhau: họ **phân phối lại**, ta **xóa**. Đây là hình so sánh mạnh
nhất và **không tốn lần chạy nào**.

### 3.9 Chẩn đoán hợp nhất

1. Cái phân biệt RideBound **không** phải total variation (bằng chứng: §3.7 phần tĩnh).
2. Cái phân biệt là **quy trách** — và nó chỉ hiện ra dưới trôi dạt (bằng chứng: §3.7
   phần k=1, 60 vs 0).
3. Cơ chế hiện tại **không** chặn cái khách nhìn thấy, nhưng **thực tế đạt được** một
   biên outcome rất gần (§3.4: `V_max = 38,7 s` với `β = 30 s`).
4. Các tầng mục tiêu nhận biết cam kết đang **bị vô hiệu hóa bởi một khiếm khuyết cài
   đặt** (§3.6b) — phải sửa trước khi đo bất cứ cơ chế mới nào.
5. Panel trôi dạt — thứ duy nhất làm đóng góp chính hiện ra — **chưa chạy trọn** (9/20).

---

## 4. Trạng thái mã nguồn liên quan

*(Mục này sẽ được bổ sung chi tiết từ báo cáo khảo sát mã nguồn đang chạy. Phần dưới là
những gì đã xác minh trực tiếp.)*

### 4.1 Bản đồ tệp liên quan

```
src/RideBound.Domain/Commitments/
  CommitmentPolicy.cs          230 dòng  — _limits: FrozenDictionary theo dimension
  CommitmentDimension.cs        59       — vocabulary 10 chiều
  CommitmentVector.cs          153       — Add(), kiểm tràn
  CommitmentLedger.cs          343       — entry, history, append
  CommitmentBudgetEvaluator.cs 115       — after = before + delta; so hardLimit
  CommitmentLockEvaluator.cs   148       — finalConfirmationLocks, freezeHorizon, ratchet
  RiderPromise.cs              180       — PromiseProjection, ThreeWayPromiseDelta
src/RideBound.Domain/Validation/
  ServiceQualityAllowance.cs            — ADR-045/047, nới ngoại sinh (xem 4.3)
  PhysicalPlanValidator.cs
src/RideBound.Domain/Requests/
  RideRequest.cs               Board() dòng 250–281 — bất biến cửa sổ đón (xem 4.3)
src/RideBound.Algorithms/Commitments/
  HardVectorCandidateAssessor.cs 548     — AssessAndFilter, khiếm khuyết ppm 316–331
  CommitmentCandidateAssessor.cs 284
  CommitmentCandidateFilter.cs   158
  CommitmentWarningProfile.cs    102
src/RideBound.Algorithms/Policies/
  SolverBackedRidePoolingPolicy.cs 546   — bộ định tuyến chính sách
  SolverBackedFleetSelection.cs    561   — hàm mục tiêu từ điển
  MultiplePlanPolicy.cs            775   — ĐÃ CÀI, chưa ghép được với cam kết
  HardVectorPolicy.cs              273
  SoftHardHybridPolicy.cs          319
src/RideBound.Runner/Configuration/
  Wp4RunnerConfiguration.cs              — RequireVariantFields dòng 571–592
```

### 4.2 ✅ XÁC MINH — Thứ tự hàm mục tiêu từ điển thật

Đọc `levelIndex` từ `objectiveBounds` của một ô C1 niêm phong (747 quyết định):

| Họ mục tiêu | levelIndex | Số lần | Khác 0 |
|---|---|---:|---:|
| `accepted-request-count` | **0** | 747 | 92 |
| `worst-hard-utilization-ppm` | **1** | 743 | 743 *(hằng số, xem §3.6b)* |
| `revision:<10 chiều>` | 2–11 | 7.430 | **0** |
| `operational-cost` | 1–12 | 747 | 743 |
| `candidate-id-rank` | 2–20 | 5.976 | 118 |

> ⚠️ Mục 4.2 của tài liệu bàn giao ghi thứ tự **sai** (`accepted > operational-cost >
> candidate-id-rank > worst-hard-utilization-ppm > …`). Thứ tự thật đặt tầng cam kết
> **trên** chi phí vận hành.

### 4.3 ⚠️ CỔNG — Bất biến chặn panel trôi dạt

`src/RideBound.Domain/Requests/RideRequest.cs:266–273`, trong `Board()`:

```csharp
if (pickupTime.Milliseconds < EarliestPickup.Milliseconds
    || pickupTime.Milliseconds > LatestPickup.Milliseconds)
{
    return DomainResult<RideRequest>.Fail(
        RequestFailureCodes.PickupTimeOutsideWindow, ...);
}
```

Dưới trôi dạt, xe tới muộn ⟹ giờ lên xe thật rơi ngoài cửa sổ đã nhận ⟹ **hỏng cứng cả
ô**. Đây là nguyên nhân 11/20 ô chết ở k=1.

**Cơ chế sửa đã tồn tại và đã được thiết kế đúng: ADR-045 `ServiceQualityAllowance`.**
Trích nguyên văn tài liệu trong mã:

> *"ADR-045 splits the physical constraints into two classes. Structural constraints
> … stay strict everywhere. Service-quality constraints are promises about time;
> worsening travel can breach them without anyone deciding anything. **Enforcing those
> continuously deletes the safety no-op and kills the run, which is what blocked WP9.**"*
>
> *"The relaxed bound is `max(contractual, exogenous)`. Because the exogenous value is
> what the unchanged active route already realizes, the relaxation can never admit a
> candidate that is worse on that dimension than doing nothing — **a decision cannot
> launder its own damage through a breach it did not cause.**"*

ADR-047 thu hẹp phạm vi: chỉ áp cho **safety no-op** trong bộ sinh phương án, vì
*"the simulator keeps its own hard feasibility check … but never re-checks a route it is
already executing"*.

⟹ Việc cần làm là **mở rộng ADR-045 sang tầng chuyển trạng thái `Board()`**, giữ nguyên
tính chất chống rửa. ⚠️ Rủi ro tích hợp: FleetPy có bộ kiểm tra riêng — xem §9.3.

### 4.4 Cơ chế đã có nhưng chưa dùng được

| Cơ chế | Trạng thái mã | Rào cản |
|---|---|---|
| `MultiplePlanPolicy` (775 dòng) | ✅ đã cài, có `MaximumPlanCount` | Guard `hasMultiple != isB5` — chỉ dùng được với `least-commitment-consensus`, **không ghép được** với `ridebound-hard-vector` |
| `WaitingIncumbentRepairSeedBuilder` | ✅ đã cài | Guard `hasRepair != isB4`; và bất biến chặng đang bay |
| `SoftHardHybrid` + `warningLimit` | ✅ đã cài | Đã chạy (mức C) — **giống hệt đối chứng 20/20 ô** |
| `ratchetLocks`, `freezeHorizon` | ✅ đã cài | Đã chạy — **trơ**, 3/4 factor không dịch chuyển gì |
| `budgetBasis: customerVisible` | ✅ đã cài | Đã chạy — vô nghiệm 4/20 ô (k=0), 19/20 (k=1) |
| `ServiceQualityAllowance` | ✅ đã cài cho bộ sinh | Chưa áp cho `Board()` |

**`RidePoolingPolicyKind.LeastCommitmentConsensus` đã có trong enum** ⟹ nhánh đối chứng
Ackermann & Rieck **đã được dựng sẵn**.

---

## 5. Sửa lý thuyết — đã thực hiện một phần

### 5.1 ✍️ ĐÃ LÀM (2026-09-21) — Chương 3

| Thay đổi | Tệp |
|---|---|
| "Đẳng thức trung tâm" → "Phân rã cộng tính và độ khít"; `B = A + d` → `B ≤ A + d` | `noi-dung/07-chuong3.tex` |
| Thêm bảng độ khít từng lần công bố (99,58% / 52,1% / 0,0748%) | nt |
| Thêm lập luận **giả dược** làm bằng chứng chính | nt |
| Khai báo **quy ước một chiều** `A = max(0, p−e)` và giới hạn của nó | nt |
| Viết lại **ĐL 3.3** trên tập quỹ đạo + chính sách tối ưu; thêm **điều kiện (H)** có đo; thêm đoạn nói rõ định lý **không** áp cho bộ giải tham lam | nt |
| Hệ quả: "bề rộng đúng bằng `d`" → "**tối đa** bằng `d`" | nt |
| Sửa tiêu đề bảng 4.x; nối sang kết quả mịn ở Chương 3 | `noi-dung/08-chuong4.tex` |

Biên dịch `tectonic` sạch, **0 tham chiếu treo**.

### 5.2 ✍️ CÒN LẠI — Chương 1 và Chương 4

| # | Việc | Tệp |
|---|---|---|
| 1 | Viết lại định vị quanh Elmi 2026; bỏ khung *"Fielbaum kêu gọi — tôi trả lời"*; dựng **không gian ba góc** | `05-chuong1.tex` |
| 2 | Thêm 3–6 bài mới vào bảng công trình liên quan và thư mục tham khảo | `05`, `10` |
| 3 | Mệnh đề **`D⁺ ≤ E ≤ V ≤ C + X`** + phản ví dụ dao động + nói rõ **ta chặn `C`** | `07-chuong3.tex` |
| 4 | **Mệnh đề đơn điệu:** nếu bộ sinh không bao giờ kéo sớm thì `C = D⁺_conduct`, và trần hai đầu ≡ trần chuỗi. Đo: 369 vs 369. **Đây là một kết quả, không phải một điểm yếu** | `07`, `08` |
| 5 | Mục §3.4 (bảo đảm hai lớp đã quan sát) vào Chương 4 | `08-chuong4.tex` |
| 6 | Mục §3.8 (đuôi + CVaR + bẫy Gini) vào Chương 4 | `08-chuong4.tex` |
| 7 | Sửa bảng thứ tự hàm mục tiêu + giải thích §8.8 | `08-chuong4.tex` |
| 8 | Bỏ chữ **"cận dưới"** khi so với baseline cho đổi xe | `08-chuong4.tex` |
| 9 | Đổi khung §8.5/8.6 thành **phép đo đầu tiên về độ mỏng tập lựa chọn**, dùng mẫu số đúng (73,84%) | `08-chuong4.tex` |
| 10 | Sửa hai trích dẫn §2.4 | `09`, `10` |
| 11 | Điền tên cán bộ hướng dẫn | `00-bia.tex` |

### 5.3 Mệnh đề mới — phát biểu chính xác

**Mệnh đề 1 (chuỗi bốn đại lượng).** Với mọi chuỗi lời hứa `q_0,…,q_T`:

```
D⁺ ≤ E ≤ V ≤ C + X
```

*Chứng minh:* `D⁺ ≤ E` do `max(0,x) ≤ |x|`. `E ≤ V` do bất đẳng thức tam giác cộng dồn.
`V ≤ C + X` do cộng dồn `|p_t − v_t| ≤ |p_t − e_t| + |e_t − v_t|`. ∎

Đã kiểm số trên cả bốn nhánh (B1, C1, k0, k1) — §3.7.

**Mệnh đề 2 (đơn điệu ⟹ chuỗi ≡ hai đầu).** Nếu bộ sinh phương án không bao giờ làm
lời hứa sớm lên, tức `p_t ≥ e_t` và `q_t ≥ q_{t−1}` với mọi `t` trên thành phần conduct,
thì `C = D⁺_conduct` và một trần theo hai đầu tương đương một trần theo chuỗi.

*Đo được:* `decisionMovedEarlier = 0` trên 421.752 lần sửa; hai tập bị gate khác nhau
**≤ 1 khách trên 1.735** ở mọi ngưỡng (§3.7).

**Ý nghĩa:** phát biểu *"chặn chuỗi mạnh hơn chặn hai đầu"* đúng về toán nhưng **rỗng
trên hệ này**. Nó chỉ có hiệu lực khi bộ sinh có thể kéo sớm — tức khi có sắp xếp lại.
Đây là một **liên kết tới hướng phát triển**, không phải một luận điểm bảo vệ.

**Mệnh đề 3 (bảo đảm hai lớp).** Nếu cơ chế bảo đảm tất định `C ≤ β`, và nếu từ dữ liệu
ước lượng được `P(X ≤ γ) ≥ 1 − α`, thì

```
P(V ≤ β + γ) ≥ 1 − α
```

*Chứng minh:* trực tiếp từ Mệnh đề 1. ∎

⚠️ **Tương thích với ràng buộc WP15 #4** (*"không soft/probabilistic constraint"*):
ràng buộc vẫn **tất định**; chỉ **báo cáo** là xác suất. Phải viết rõ điều này, nếu
không nó vi phạm ràng buộc đã khóa.

---

## 6. Phát biểu lại đóng góp

### 6.1 Cái KHÔNG được tuyên bố

- ❌ "Lần đầu tiên có bảo đảm ETA cho từng hành khách" — Elmi 2026 đã có.
- ❌ "Lần đầu kiểm soát bất ổn trong ride-pooling" — Elmi 2026 đã có.
- ❌ "Trì hoãn cam kết" / "least-commitment" là mới — Ackermann & Rieck 2025; `docs/03`
  đã ghi.
- ❌ "Time consistency" là mới — Tellez và cs. 2022.
- ❌ "Bảo vệ no-worse cho một lần cập nhật" là mới — anticipatory walking 2026.
- ❌ "Chặn total variation" là điểm phân biệt — §3.7 phần tĩnh bác bỏ.
- ❌ Vượt trội về tỉ lệ phục vụ — **mọi** cấu hình có cam kết đều phục vụ ít hơn.
- ❌ Dùng "+7,1 pp của Zalesak" để bù "−7,13 pp".
- ❌ Gini làm chỉ số công bằng cho `A_r`.

### 6.2 Cái ĐƯỢC tuyên bố

Theo đúng `docs/03-related-work-and-claim-boundary.md`, novelty chỉ nằm ở **tổ hợp**:

> per-passenger + **path-dependent** + multi-dimensional + cumulative/switch budget +
> multi-epoch rolling insertion + **machine-checkable certificate**

Cộng thêm hai thứ tài liệu đó chưa nêu và §3 vừa chứng minh là có giá trị:

1. **Phân rã nhân quả `v/e/p` bằng một phản thực KHẢ THI.** `e` không phải mô hình —
   nó là phương án không-làm-gì, có thật trong tập lựa chọn, qua bộ kiểm tra vật lý, có
   mã định danh trong biên bản. Bằng chứng đúng đắn: phép thử giả dược §3.3.
2. **Bảo đảm CÓ MỨC, cho MỌI khách** — trái với khẳng định của Elmi và cs. rằng bảo đảm
   *"would not be possible if even a single change were allowed"*.

### 6.3 Câu chuyện một đoạn

> Văn liệu đã khám phá hai góc. Fielbaum & Alonso-Mora (2020) cấm tuyệt đối mọi thay
> đổi cho **mọi** khách: bất ổn về 0, từ chối tăng **+11,1 pp**. Elmi và cs. (2026) cấm
> tuyệt đối cho **một nhóm được chọn**: cùng tỉ lệ từ chối, số người bị đụng giảm 4,1
> lần, nhưng gánh nặng được **phân phối lại** — người bị đụng chịu nặng gấp 4,5 lần,
> trung bình toàn dân số gần như không đổi. Và họ phát biểu rõ rằng bảo đảm *"would not
> be possible if even a single change were allowed"*.
>
> Khóa luận này khám phá **góc thứ ba**: một bảo đảm **có mức, cho mọi khách** — giờ
> được phép dời, nhưng tổng lượng dời **do nhà điều hành gây ra** bị chặn bởi một trần
> cộng dồn, cưỡng chế **trước** khi ra quyết định, kèm chứng chỉ kiểm được bằng máy.
> Phần *"do nhà điều hành gây ra"* đòi hỏi một phép phân rã nhân quả không tồn tại
> trong bất kỳ công trình nào kể trên — và dưới trôi dạt giao thông thật, phép phân rã
> đó là khác biệt giữa **chặn 60 hành khách vì tắc đường** và **chặn 0**.

---

## 7. ⚠️ CỔNG QUẢN TRỊ — đọc trước khi chạy bất cứ thứ gì

Kho có quy trình chính thức. Bỏ qua nó thì kết quả không được công nhận trong chính hệ
thống bằng chứng của dự án.

### 7.1 Trạng thái theo `docs/18` và `docs/16`

```
Research direction : LOCKED_FOR_IMPLEMENTATION_PLANNING
Current WP         : WP14R active (ADR-071/072)
                     RB-WP14R-001..008R xong/đang chạy
                     009..012 UNAUTHORIZED
WP15               : Roadmap-level only, chưa authorize execution
H7 (WP17)          : chỉ mở khi WP15–WP16 đạt gate
```

Chuỗi phụ thuộc bắt buộc (`docs/tasks/47`, §5):

```
RB-WP14R-008 paired gate → 009 matrix → 010 independent verifier
  → 011 two-axis frontier → 012 audit + closure decision
  → [ADR mở WP15] → WP15 ticket hóa
```

### 7.2 Mâu thuẫn phải xử lý trước

`docs/18` (cập nhật 2026-08-28) ghi `009_MATRIX_HALTED_40_OF_160`. Nhưng
`docs/benchmarking/wp14r-013-v6-matrix-and-h6-rerun-2026-09-05.md` ghi **160/160 job
terminalSuccess**, verifier độc lập 160/160 valid, 28,55 h.

⟹ **`docs/18` và `docs/19` đang lạc hậu so với bằng chứng.** `AGENTS.md` yêu cầu cập
nhật chúng ở cuối mọi task. **Việc đầu tiên trong mọi kế hoạch là cập nhật hai tệp này**,
nếu không toàn bộ chuỗi authorize bị kẹt trên một trạng thái sai.

### 7.3 Ràng buộc bất di bất dịch của WP15 (`docs/tasks/47`, §4)

| # | Ràng buộc | Ảnh hưởng tới kế hoạch này |
|---|---|---|
| 1 | Không mở WP15 trước khi WP14R có frontier verified và ADR authorize | §8.9 trở đi phải chờ |
| 2 | **Không dùng số đo H6/E1/WP14-v1 để chọn mức của bất kỳ trục nào** | Mọi số ở §3 chỉ dùng **mô tả/đặt giả thuyết**, **không** dùng để chọn `β`, `w`, `γ` |
| 3 | Mọi promise field/lock/profile mới đều mặc định **tắt**; không nới nghĩa cái cũ | Cửa sổ phải là **field mới** |
| 4 | Mọi quyết định vẫn phải phát certificate máy kiểm; **không soft/probabilistic constraint** | Mệnh đề 3 phải là **báo cáo**, không phải ràng buộc |
| 5 | Không lấy tham số số học từ paper | Không nhập `γ` từ văn liệu |
| 6 | Trục nào bị điều kiện phủ định bắt được thì báo **vô hiệu** | Đã khai báo sẵn cho từng bước ở §8 |
| 7 | Kết quả âm của WP15 là kết quả hợp lệ | Không ép cho đẹp |

### 7.4 Thiết kế WP15 đã khóa sẵn — **không được đề xuất lại như ý tưởng mới**

`docs/tasks/47-wp15-lifecycle-commitment-refinement.md` đã khóa ba trục:

- **Trục B — lời hứa là cửa sổ có mức bảo đảm dẫn xuất.** Theo Hosseini, Rostami &
  Araghi (2025, arXiv:2508.01032), cửa sổ tối ưu là **quantile của phân phối thời điểm
  tới** ở mức đúng bằng tỷ số penalty: `Pr(τ ≤ ℓ) = a_w/a_ℓ`, `Pr(τ ≤ u) = 1 − a_w/a_u`.
  - **Phủ định B1:** nếu độ rộng cần thiết vượt `pickupWindowMs` (600.000 ms) hoặc vượt
    p90 biến động đã đo (154.821 ms) tới mức lời hứa mất nghĩa ⟹ trục B **vô hiệu**.
  - **Phủ định B2:** nếu phân phối thời điểm tới **không** ước lượng tất định được từ
    state hiện có ⟹ không certify được ⟹ **dừng**.
- **Trục C — freeze horizon phụ thuộc lifecycle.**
  - **Phủ định C1:** nếu phân bố thời điểm prune do lock **không** tập trung gần giờ
    đón ⟹ trục C **vô hiệu**. Phép đo này phải làm **trước** khi cài.
- **Trục D — giảm phương sai bằng stop pooling.** Ngoài phạm vi sản phẩm; cần ADR riêng.

**Anchor giữ nguyên là lời hứa khách đã chấp nhận** (xác nhận độc lập bởi Laupichler và
cs. 2026, Mt-KaRRi). **Mọi policy v2 phải bảo đảm tập khả thi không rỗng theo cấu tạo.**

### 7.5 Kết luận quản trị quan trọng nhất

`docs/tasks/47` §5, nguyên văn:

> *"Nếu `012` kết luận cái giá của hard commitment là **cấu trúc** chứ không phải lỗi
> tham số, thì trục A đã cạn và WP15 phải bắt đầu từ trục B — nhưng **kết luận đó cũng
> là một đóng góp hoàn chỉnh cho bài báo, và WP15 không bắt buộc phải tồn tại để bài
> báo đứng được.**"*

⟹ **Khóa luận KHÔNG cần WP15 để hoàn chỉnh.** Kế hoạch dưới đây vì thế chia làm hai
nửa rõ rệt: **§8.1–§8.7 đủ để đóng khóa luận**; §8.8 trở đi là mở rộng nghiên cứu.

---

## 8. Kế hoạch thực hiện

Mười giai đoạn. **P0–P2 không tốn một lần chạy nào** và đã đủ để đóng khóa luận ở mức
vững. P3 trở đi cần sửa mã và dựng runner mới.

Mỗi giai đoạn khai báo: **đầu vào**, **việc làm**, **điều kiện hoàn thành**, **điều kiện
phủ định** (cái gì làm giai đoạn đó vô hiệu), và **kết quả dự tính**.

---

### P0 — Quản trị. ✍️ CHỈ VIẾT. Bắt buộc làm trước mọi thứ.

**P0.1 — Đồng bộ `docs/18` và `docs/19` với bằng chứng thật.**

`docs/18` (2026-08-28) ghi `009_MATRIX_HALTED_40_OF_160`. `wp14r-013` (2026-09-05) ghi
**160/160 terminalSuccess**, verifier độc lập 160/160 valid. Hai tệp đang lạc hậu, và
`AGENTS.md` yêu cầu cập nhật ở cuối mọi task.

Cụ thể phải ghi vào `docs/18`:
- `RB-WP14R-009` matrix: 160/160, 28,55 h, retained 17,13 GiB / trần 20 GiB, một
  `repositoryInventorySha256` duy nhất `1a2102eb…` trên cả 160 bundle.
- Defect entered-edge position đã sửa (`mapping.py` clamp `progressPermille ≥ 1`).
- H6 re-run dưới adapter đã sửa: **tái lập tới từng mili-giây**, service gate vẫn FAIL
  ở −7,1296 pp / −4,9074 pp, burden gate PASS 99,8280% / 99,2339%.
- Ba factor F1/F2/pickup-lock **trơ**: 6/10 nhánh không phân biệt được trên mọi counter.
- Đính chính interim claim về `behavioralHash`.

Cập nhật `docs/19-requirement-traceability.md` tương ứng.

**Điều kiện hoàn thành:** `docs/18` phản ánh đúng `wp14r-013`; chuỗi authorize không còn
kẹt trên trạng thái sai.

**P0.2 — Ghi nhận đúng nguồn gốc khiếm khuyết ppm.**

⚠️ Khiếm khuyết `worst = PartsPerMillion` **đã được kho ghi nhận từ 2026-08-25**:
- `docs/handoffs/wp14-continuation-2026-08-25.md:107-109` — *"`worst-hard-utilization-ppm`:
  **0,000%** phân biệt — hằng số `1000000` ở **13.004/13.004** decision."*
- `docs/reviews/wp1-wp13-optimization-and-fairness/README.md:110-130`, `:141`, `:219`
- `docs/19:621`, `docs/18:4394`, `docs/18:4987`

Đây **không phải phát hiện mới**. Mọi tài liệu mô tả nó như phát hiện mới đều phải sửa.
Cái mới duy nhất là: **nó chưa bao giờ được sửa, và chưa có test nào phủ nó.**

**P0.3 — Chốt phạm vi.**

Hai lựa chọn, phải chọn trước khi làm P3:

| | Phạm vi | Cần |
|---|---|---|
| **A — Đóng khóa luận** | P0 → P2, tùy chọn P3 | Không cần ADR mới, không đụng WP15 |
| **B — Mở rộng nghiên cứu** | P0 → P8 | Cần đóng WP14R-012 + **ADR authorize WP15** (§7.1) |

`docs/tasks/47` §5 đã nói rõ: *"WP15 không bắt buộc phải tồn tại để bài báo đứng được."*

---

### P1 — Sửa báo cáo LaTeX. ✍️ CHỈ VIẾT.

Đã làm một phần ngày 2026-09-21 (§5.1). Còn 11 mục ở §5.2.

**Ưu tiên theo giá trị / công sức:**

1. **Mục 1 (định vị Elmi)** — rủi ro mất điểm lớn nhất. Dùng nguyên văn §6.3.
2. **Mục 3 + 4 (Mệnh đề 1 và 2)** — biến khác biệt thành quan hệ chứng minh được, **và
   trung thực về việc Mệnh đề 2 làm mệnh đề "chuỗi mạnh hơn hai đầu" trở nên rỗng trên
   hệ này**.
3. **Mục 5 (bảo đảm hai lớp)** — số đã có, chỉ viết.
4. **Mục 6 (đuôi + CVaR + bẫy Gini)** — số đã có, chỉ viết.
5. Các mục còn lại.

**Điều kiện hoàn thành:** `tectonic` biên dịch sạch, 0 tham chiếu treo, và **không câu
nào trong §6.1 xuất hiện trong bản in**.

---

### P2 — Phân tích trên dữ liệu đã niêm phong. ✍️ 0 LẦN CHẠY.

Toàn bộ script đã có ở `ridebound-scratchpad/claude-measurements-2026-09/` (14 tệp).

| # | Phân tích | Script | Trạng thái |
|---|---|---|---|
| P2.1 | Độ khít phân rã từng lần công bố | `identity.py` | ✅ xong (§3.1) |
| P2.2 | Điều kiện (H) `A ≤ B` | `aleb.py` | ✅ xong (§3.2) |
| P2.3 | Phép thử giả dược `d` bất biến | `analyze1.py`, `tvcheck.py` | ✅ xong (§3.3) |
| P2.4 | Bảo đảm hai lớp — phân bố `V` | `tvcheck.py` | ✅ xong (§3.4) |
| P2.5 | Độ lớn từng lần dời, phần vượt trần | `analyze3.py`, `excess.py` | ✅ xong (§3.5) |
| P2.6 | Mẫu số đúng cho độ mỏng tập lựa chọn | `choiceset.py` | ✅ xong (§3.6a) |
| P2.7 | Thứ tự hàm mục tiêu thật | `objorder.py` | ✅ xong (§4.2) |
| P2.8 | So chuỗi / hai đầu / conduct, tĩnh và trôi dạt | `endpoint.py`, `drifttv.py` | ✅ xong (§3.7) |
| P2.9 | Đuôi, CVaR, tập trung, bẫy Gini | `equity.py` | ✅ xong (§3.8) |
| **P2.10** | **Điều kiện phủ định C1 của WP15** | **chưa viết** | 🔬 phải làm |

**P2.10 là việc duy nhất còn lại của P2 và nó là bắt buộc theo `docs/tasks/47`:**

> *"Phủ định C1: nếu phân bố thời điểm prune do lock **không** tập trung gần giờ đón ⟹
> trục C vô hiệu. Phép đo này phải làm **trước** khi cài, trên frontier của WP14R,
> không phải trên H6/E1."*

Việc cần làm: đọc `prunedCandidates[].commitmentWitnesses` có `code =
COMMITMENT_PHASE_LOCK`, lấy `simTimeMs` của khung và `promise.pickupEtaMs` của khách bị
witness, vẽ phân bố `pickupEta − now`. **Chạy trên bundle WP14R development panel, không
phải panel H6.**

**Bàn giao:** chép toàn bộ script sang thư mục làm việc của Codex để tái lập độc lập.
Codex đã từ chối nhận số khi không có script — đúng quy trình.

---

### P3 — Sửa khiếm khuyết bão hòa ppm. 🔬 CHẠY NHỎ. ⚠️ Chạm mã.

**Vì sao trước mọi cơ chế mới:** nếu không sửa, lợi ích của bất kỳ nhánh mới nào sẽ bị
lẫn với việc vô tình sửa lỗi này. Và với nhánh chọn-lọc (P9) thì kết quả **không diễn
giải được**: một khách bị khóa làm bão hòa điểm của cả xe.

**Thay đổi: đúng một dòng.** `HardVectorCandidateAssessor.cs:329`

```diff
             if (hardLimit == 0)
             {
                 if (value != 0)
                 {
                     return UtilizationResult.Failure(...);   // giữ nguyên, fail-closed
                 }
-                worst = PartsPerMillion;
                 continue;
             }
```

**Giữ nguyên `hasLimit = true;` ở dòng 313.** Nếu chuyển nó xuống dưới nhánh zero thì
`HasApplicableHardLimit` thành false với một policy chỉ có trần 0, và theo
`SolverBackedFleetSelection.cs:271-272, 300-312` toàn bộ tầng
`worst-hard-utilization-ppm` **và** mười tầng `revision:*` biến mất, làm hình dạng mục
tiêu của C1 sụp về RollingCost — một thay đổi ngữ nghĩa lớn hơn nhiều so với việc sửa
khiếm khuyết.

**Không chạm** nhánh `hardLimit == 0 → return PartsPerMillion` trong
`CeilingPartsPerMillion` (`:353-356`): nó thành chết từ call-site này nhưng **có test
khẳng định trực tiếp** (`ExactSmallCommitmentDifferentialTests.cs:381-383`).

**Test mới bắt buộc** (hiện **không test nào** phủ khiếm khuyết này): một policy có trần
0 trên một chiều switch **và** trần dương trên `drop_eta_total_ms`, khẳng định hai ứng
viên nhận **hai giá trị ppm khác nhau**.

**Ảnh hưởng đã xác minh:** 5 nơi tiêu thụ giá trị (`HardVectorPolicy.cs:151-153,170-188`;
`SoftHardHybridPolicy.cs:161-163,180-185`; `SolverBackedFleetSelection.cs:304-306,
317-319,335-337,435-437`; `RollingCostPolicy.cs:237`) — **không nơi nào cần sửa**, tất
cả đổi hành vi. **Không test nào hỏng.**

**Artefact phải cập nhật theo `AGENTS.md`:**
`docs/benchmarking/evidence/wp14-001-mechanism-probe-v1-summary.json`; mọi decision hash
phủ `objectiveBounds[].incumbentValue`; và năm phát biểu prose đã liệt kê ở P0.2.

**Chạy:** C1 trên **panel phát triển 16 ô** (`wp14-development-panel-v1`), **không** trên
panel H6 niêm phong.

**Kết quả dự tính.** Hai khả năng, cả hai đều có giá trị:

| Kết quả | Diễn giải | Xác suất chủ quan |
|---|---|---|
| Tỉ lệ phục vụ **không đổi** | Xác nhận rất mạnh rằng khâu chọn không phải chỗ nghẽn — mạnh hơn mọi lập luận, vì đã bật tầng mục tiêu lên mà vẫn không dịch | cao |
| Tỉ lệ phục vụ **tăng vài phần mười pp** | Một phần của −5,50 pp là lỗi cài đặt, không phải giá của cam kết | thấp |

**Điều kiện phủ định P3:** nếu sau khi sửa, `worst-hard-utilization-ppm` **vẫn** degenerate
≥ 99% số quyết định, thì tầng đó không cứu được và không nên đầu tư thêm vào khâu chọn.

---

### P4 — Mở khóa panel trôi dạt. ⚠️ CỔNG. Đường găng của cả nghiên cứu.

**Vấn đề.** `RideRequest.Board()` (`:266-273`) từ chối khi giờ lên xe thật rơi ngoài cửa
sổ đón đã nhận. Dưới trôi dạt, xe tới muộn ⟹ **hỏng cứng cả ô**. Đây là lý do **11/20 ô
chết ở k=1**, và vì thế kết quả quyết định §3.7 chỉ dựa trên 9 ô.

**Cơ chế sửa đã được thiết kế sẵn: ADR-045.** `ServiceQualityAllowance` đã tách ràng buộc
vật lý thành hai lớp và đã có bound `max(contractual, exogenous)` kèm tính chất chống
rửa. Tài liệu trong mã nói thẳng: *"Enforcing those continuously deletes the safety no-op
and kills the run, **which is what blocked WP9**."*

ADR-047 thu hẹp phạm vi xuống **chỉ safety no-op trong bộ sinh**, lý do: *"the simulator
keeps its own hard feasibility check … but never re-checks a route it is already
executing"*.

**Việc cần làm:** một **ADR mới** mở rộng ADR-045 sang tầng chuyển trạng thái `Board()`,
giữ nguyên ba tính chất:
1. bound vẫn là `max(contractual, exogenous)`;
2. `exogenous` vẫn lấy từ **tuyến đang chạy không đổi**;
3. request không có điểm dừng trên tuyến đang chạy **không** được nới.

**⚠️ Rủi ro tích hợp lớn nhất của toàn kế hoạch.** ADR-047 nói rõ nới ở phía RideBound
cho một plan **đã đổi** sẽ làm RideBound đề xuất plan mà simulator từ chối. Ở đây ta nới
ở **tầng trạng thái**, không phải tầng sinh phương án, nên khác — nhưng **phải kiểm
chứng bằng một ô dry-run trước khi chạy cả panel**.

**Điều kiện hoàn thành:** panel trôi dạt k=1 chạy **≥ 18/20 ô**, và các ô còn hỏng hỏng
vì lý do **khác** `PICKUP_WINDOW`.

**Điều kiện phủ định P4:** nếu sau khi nới, FleetPy từ chối plan với lỗi riêng của nó
(`RBWP7_*`) ở ≥ 3 ô, thì hướng nới ở tầng trạng thái **vô hiệu** và phải chuyển sang
phương án dự phòng: dùng **fixture cửa sổ rộng 900 s** (`build_wide_fixture.py` +
`preflight_wide.py` đã có), chấp nhận rằng **không so được số với panel 600 s** (kỷ luật
mục 6.3) và chỉ so **nội bộ trong panel 900 s**.

---

### P5 — Nhánh đối chứng "hạn chót" kiểu Schulz. 🔬 ⚠️ Chạm mã.

**Đây là nhánh đối chứng bắt buộc** — không có nó thì không trả lời được câu *"Schulz
2026 cũng có bounded time shift rồi, em khác gì?"*.

**Kết luận khảo sát mã: bộ từ vựng 10 chiều hiện tại KHÔNG diễn đạt được cơ chế này.**
Hai lý do:

1. `drop_eta_total_ms` là **đối xứng và cộng dồn**
   (`PromiseDeltaCalculator.cs:137-139` dùng `AbsoluteDifference`;
   `CommitmentLedger.cs:288` cộng dồn). Đó là **độ dài đường đi** của ETA, không phải
   một **mức**. Nó không chặn hướng, cũng không chặn độ lệch cuối so với mốc.
2. `ratchetLocks` một chiều nhưng **neo sai chỗ và dung sai bằng 0**.
   `CommitmentLockEvaluator.cs:144-147` so `after > before`, nhưng `before` là **mốc
   ngoại sinh** (`CommitmentDecisionValidator.cs:347-353`), không phải lời hứa đầu tiên.
   Nghĩa là *"đừng làm muộn hơn mức nó vốn sẽ muộn, trong kỷ nguyên này"*, slack đúng 0.
   Schulz cần `candidateDropEta ≤ initialDropEta + l`.

**Đường đi đúng: một LUẬT KHÓA MỚI, không phải một chiều thứ 11.**

> Thêm một chiều thứ 11 tốn **~30 điểm sửa**, gồm 15 tệp cấu hình, schema JSON, adapter
> Python, ~10 tệp test, và **làm mất hiệu lực mọi hash đã ghi**. Tuyệt đối tránh.

Mốc neo đã có sẵn, không cần thêm trạng thái:
`history.Entries[0].PublishedPromise.Projection.DropEta` — entry đầu luôn là
`CommitmentLedgerEntryKind.InitialPromise` (`CommitmentLedger.cs:189-195`).

**Các điểm sửa, đầy đủ:**

| # | Tệp | Việc |
|---|---|---|
| 1 | `CommitmentPolicy.cs:129-137, 184-203` | Thêm `Duration? DropEtaDeadlineSlack` (ctor param + validation + property) |
| 2 | `CommitmentLockEvaluator.cs:13-19` | **Đổi chữ ký** — thêm tham số `anchor` (`PromiseProjection`) |
| 3 | `CommitmentLockEvaluator.cs:87-138` | Trong `AddWitnesses`, thêm kiểm `candidate.DropEta > anchor.DropEta + slack` với `Rule = "deadline_cap"` |
| 4 | `CommitmentDecisionValidator.cs:347-353` | Truyền `priorHistory.Entries[0].PublishedPromise.Projection` |
| 5 | `CommitmentPolicyConfiguration.cs:20-28` | Thêm khóa vào `PolicyFields` |
| 6 | `CommitmentPolicyConfiguration.cs:167-184` | Parse khóa mới, cạnh `ReadLocks(element, "ratchetLocks")` |
| 7 | `benchmarks/configurations/` | Một tệp cấu hình cam kết mới cho nhánh |

**Không cần sửa gì ở tầng Algorithms** nếu trần là một cổng thuần:
`RideBoundHardVector` đã truyền `context.Policies` nguyên vẹn
(`SolverBackedRidePoolingPolicy.cs:406-407`), nên **một tệp cấu hình mới là đủ để có
nhánh**. Chỉ cần thêm `RidePoolingPolicyKind` nếu muốn biên bản **gọi tên** nhánh trong
ma trận thí nghiệm — và bảng factor của WP14 (`wp14_freeze_v2.py:104-130`) cho thấy là
có muốn.

> ⚠️ **Bẫy `EffectivePolicies`.** `SolverBackedRidePoolingPolicy.cs:396-410` có nhánh
> mặc định `_ => MechanismCommitmentPolicyProvider.RevisionPenalty`, **xóa sạch mọi hard
> limit**. Một policy kind mới bị quên ở đây sẽ **âm thầm chạy như baseline không ràng
> buộc** và cho kết quả vô nghĩa mà không báo lỗi. Đây là bẫy nguy hiểm nhất trong mã.

**Quét:** `l ∈ {0, 30, 60, 120, 300, 600} s`, đối xứng với quét `β` đã có.

**Điều kiện phủ định P5:** nếu trên panel **tĩnh**, nhánh hạn chót và nhánh conduct cho
tỉ lệ phục vụ chênh nhau **dưới sàn nhiễu ±0,3 pp** ở mọi mức, thì **trên panel tĩnh hai
cơ chế không phân biệt được** — và đó chính là điều §3.7 dự đoán. Khi đó **không được**
kết luận "cơ chế của tôi tốt hơn"; phải chuyển thẳng sang P6.

---

### P6 — Thí nghiệm quyết định: conduct vs hạn chót **dưới trôi dạt**. 🔬

**Đây là thí nghiệm quyết định số phận đóng góp chính.**

Phụ thuộc: **P4 xong** (panel trôi dạt chạy được) **và P5 xong** (có nhánh hạn chót).

**Thiết kế ghép cặp:** cùng ô, cùng nhu cầu, cùng đội xe, cùng đồ thị, cùng hệ số trôi
dạt, cùng ngân sách tính toán. Bốn nhánh × ba mức trôi dạt:

| Nhánh | Chặn gì | Vai trò |
|---|---|---|
| `b1` | không chặn | đối chứng |
| `deadline-l` | `D⁺ ≤ l` so với lời hứa đầu | **đối thủ trực tiếp (Schulz)** |
| `conduct-β` | `C ≤ β` | cơ chế đề xuất |
| `outcome-β` | `V ≤ β` | ablation (đã biết: vô nghiệm) |

Mức trôi dạt `k ∈ {0, 0.5, 1}` — hạ tầng bơm trôi dạt đã có
(`scratchpad/drift/preflight_drift.py`, mô hình `f_k(t) = (f_real(t0+t)/f_real(t0))^k`,
chuẩn hóa `f(0) = 1`).

**Đo, cho từng nhánh × mức:** số khách phục vụ; `D⁺`, `E`, `V`, `C`, `X` cộng dồn và
theo từng khách; số khách bị gate và **lý do** (phân loại theo **mã lỗi thật**, không so
chuỗi — bẫy 12.4); chờ/vòng đường thật; runtime p50/p95/p99.

**Kết quả dự tính (giả thuyết tiền đăng ký, dựa trên §3.7):**

| Mức | Dự đoán |
|---|---|
| `k = 0` | `deadline-l` và `conduct-β` **không phân biệt được** (chênh < 0,3 pp), gate gần cùng một tập khách |
| `k = 1` | `deadline-l` gate **nhiều khách hơn hẳn** `conduct-β`, và phần lớn số khách đó bị gate **do tắc đường**. Ước lượng từ dữ liệu hậu nghiệm: cỡ **60 vs 0** trên 583 khách |
| `k = 1` | `outcome-β` **vô nghiệm ở đa số ô** (đã đo: 19/20) |

**Điều kiện phủ định P6 — quan trọng nhất trong cả kế hoạch:** nếu ở `k = 1`, số khách
bị gate bởi `deadline-l` và bởi `conduct-β` **chênh nhau dưới 3×**, thì phép quy trách
**không tạo ra khác biệt vận hành**, và đóng góp chính phải được hạ xuống thành *"một
phép đo và một khung khái niệm"* thay vì *"một cơ chế tốt hơn"*. Ghi kết quả âm đó,
không ép.

---

### P7 — Bảo đảm hai lớp, có thống kê đúng. ✍️ + 🔬

**Phát biểu (Mệnh đề 3):** `C ≤ β` tất định **∧** `P(X ≤ γ) ≥ 1 − α` ⟹
`P(V ≤ β + γ) ≥ 1 − α`.

⚠️ **Tương thích ràng buộc WP15 #4**: ràng buộc vận hành vẫn **tất định**; chỉ phần
**báo cáo** là xác suất. Phải viết rõ, nếu không nó vi phạm ràng buộc đã khóa.

**Cách ước lượng `γ` cho đúng — không dùng phân vị mẫu trần trụi.**

Dùng **bất đẳng thức Dvoretzky–Kiefer–Wolfowitz** với hằng số chặt của Massart (1990):

```
P( sup_x |F̂_n(x) − F(x)| > ε )  ≤  2 e^{−2nε²}
⟹  ε(n, α) = sqrt( ln(2/α) / (2n) )
```

Với `α = 0,05` và `n = 1.581` khách: `ε = sqrt(ln 40 / 3162) = sqrt(0,0011667)` ≈
**0,0342**, tức **±3,42 điểm phần trăm** trên CDF.

⟹ Để tuyên bố `P(X ≤ γ) ≥ 0,95` một cách phân-phối-tự-do, lấy `γ` = **phân vị mẫu
98,42%** của `X` (0,95 + 0,0342), không phải phân vị 95%.

**Bổ sung:**
- **Khoảng Clopper–Pearson** cho tỉ lệ *"số khách có `V ≤ ngưỡng`"* — chính xác, không
  xấp xỉ chuẩn, quan trọng vì tỉ lệ ở gần 1 (99,7%).
- **CVaR** báo cáo kèm sai số DKW theo cùng khung — xem arXiv:2509.11859, *"Statistical
  Model Checking Beyond Means: Quantiles, CVaR, and the DKW Inequality"*, đúng tổ hợp
  công cụ cần dùng.
- **Không dùng bootstrap cho cực đại.** Bootstrap cho max là không nhất quán. Nếu cần
  phát biểu về đuôi, dùng **lý thuyết giá trị cực trị** (POT/GPD), hoặc chỉ báo cáo cực
  đại quan sát được **như một quan sát**, không như một ước lượng.
- **Thiết kế ghép cặp**: vì cùng ô / cùng nhu cầu, phải dùng kiểm định ghép cặp, và
  **đơn vị thí nghiệm là Ô**, không phải khách. `n = 20` ô, không phải `n = 1735`.

⚠️ **Ràng buộc WP15 #2 và #5**: **không** được dùng `γ` đo trên H6/E1 để **chọn** mức
của bất kỳ nhánh nào, và **không** nhập `γ` từ văn liệu. `γ` chỉ được **báo cáo** trên
panel trôi dạt mới của P4/P6.

**Kết quả dự tính:** trên panel trôi dạt k=1, `γ` sẽ **lớn hơn nhiều** so với 8,7 s của
panel tĩnh (đo được: `d` p90 = 47,4 s, max = 150,7 s). Bảo đảm sẽ có dạng *"tổng biến
động bạn nhìn thấy ≤ 30 s + ~150 s, với xác suất ≥ 95%"*. **Phải báo cáo trung thực rằng
lớp thứ hai rộng gấp năm lần lớp thứ nhất** — đó là bản chất của việc giao thông không
kiểm soát được.

---

### P8 — Vững chắc. 🔬

| Trục | Trạng thái |
|---|---|
| Lặp lại | **Đã có**: 20 ô = 5 ngày × 4 mẫu nhu cầu |
| Cỡ đội xe | **Đã có**: panel A 8 xe, panel B 4 xe |
| Khung giờ | **Đã có**: panel phát triển có `w08` và `w17` |
| **Mức nhu cầu** | ❌ **Thiếu** — cần ít nhất 2 mức |
| **Runtime p50/p95/p99** | ❌ **Thiếu** — hội đồng luôn hỏi |

⚠️ **"Chạy nhiều seed" là hiểu sai kiến trúc.** Bộ giải **tất định**;
`solverSeedsAreReplicates: false` đã được tiền đăng ký và hai seed contrast đo được
**đúng bằng 0**. Lặp lại đến từ mẫu nhu cầu, không từ seed.

Đối chiếu quy mô: Schulz & Pfeiffer dùng 900 instance × 3 seed = 2.700, và 32 cấu hình
= 86.400 quan sát. RideBound ở quy mô nhỏ hơn nhiều — **phải nói rõ trong phần hạn chế**.

---

### P9 — (Tùy chọn) Nhánh đối chứng "không cập nhật, chọn lọc" kiểu Elmi. 🔬

**Tin tốt: bộ từ vựng hiện tại diễn đạt được, KHÔNG cần sửa Domain/Application/Algorithms.**

`commitmentPolicyId` đã là **trường theo từng request** trong giao thức
(`OnlineEventModels.cs:60-70`), được phân giải **theo từng request** tại
`HardVectorCandidateAssessor.cs:284-286` và `CommitmentDecisionValidator.cs:202-208`.
`policies[]` đã là mảng; `hardLimit` bỏ trống ⟹ không giới hạn.

**Nhưng bị chặn ở bốn chỗ:**

| # | Chặn | Sửa |
|---|---|---|
| 1 | `PublicDerivativePairedHarness.cs:142-158` — *"Public derivative requests must bind exactly one commitment policy ID"* | Đổi sang kiểm theo **tập** |
| 2 | `FleetPyManhattanNormalizer.cs:448, :1003` — đóng dấu **một** id lên mọi request | Quy tắc chia theo `SourceRecordOrdinal` (đã có sẵn), để tái lập được và ổn định hash |
| 3 | `session.py:103-126` `_require_declared_commitment_policy` — id hard-code `"wp6-synthetic-policy-overlay-v1"` | Chấp nhận một tập id |
| 4 | `Wp4RunnerConfiguration.cs:556-566` — C2 đòi một warning profile **cho mỗi** policy | Chỉ nếu đi đường C2 |

⚠️ **Phải làm P3 trước.** Với khiếm khuyết bão hòa, cohort "trần 0" ép ppm lên
1.000.000 còn cohort "không trần" cho `hasLimit = false`; vì `worst`/`hasLimit` gộp
**theo xe** trên mọi khách của xe đó, **một** khách bị khóa làm bão hòa cả xe và nhánh
hỗn hợp **không diễn giải được**.

**Điều kiện phủ định P9:** nếu nhánh chọn-lọc cho cùng tỉ lệ phục vụ nhưng gánh nặng
**chỉ dịch chuyển** sang nhóm không được bảo vệ (đo bằng CVaR₉₅ của nhóm đó), thì nó tái
lập đúng kết quả của Elmi và **không phải đóng góp** — chỉ là một comparator.

---

### P10 — (Tùy chọn) Plan pool để tách "giá của cam kết" khỏi "giá của tìm kiếm thiển cận". 🔬

**Câu hỏi:** trong −7,13 pp, bao nhiêu là giá thật của cam kết, bao nhiêu chỉ là hệ quả
của việc commit quá sớm vào một kế hoạch?

**Mã đã có:** `MultiplePlanPolicy.cs` 775 dòng, `RidePoolingPolicyKind.LeastCommitmentConsensus`
đã trong enum ⟹ **baseline Ackermann & Rieck đã dựng sẵn**.

**Nhưng ghép với cổng cứng thì chưa được.** Bảy điểm sửa đã xác định:

1. `MultiplePlanPolicy.cs:706-711` — `Decide` nhận `CommitmentMechanismContext` thay vì
   `OnlineState`, thêm `HardVectorCandidateAssessor`.
2. `:729-731` — thay `commitmentFilter.Filter(...)` bằng `_hardAssessor.AssessAndFilter(...)`;
   việc này cũng mang theo **guard fail-closed** mà B5 hiện thiếu.
3. `MultiplePlanFleetSelector.Select:102-105` — thêm tham số assessments; luồng
   `worstUtilization` và vector revision qua `Enumerate:281-371`.
4. Chèn khóa cam kết vào **ba** hàm xếp hạng: `IsOperationallyBetter:612-629`,
   `Dominates:429-443`, chuỗi `OrderByDescending:228-234`. **Đặt nó trên hay dưới
   `ConsensusScore` là một quyết định nghiên cứu, không phải cơ học.**
5. `RunnerSession.cs:859-892` — bỏ hard-code `MechanismCommitmentPolicyProvider.RevisionPenalty`
   ở `:861-862`. **Hiện tại B5 chỉ áp phase lock, KHÔNG có ràng buộc ngân sách nào.**
6. `Wp4RunnerConfiguration.cs:571-593` — cần cờ `isB6` riêng.
7. `SolverBackedRidePoolingPolicy.cs:87-91` — nới nếu nhánh mới cũng cần đường solver.

⚠️ **Cùng rào cản đã giết H3** (`hasRepair != isB4` ↔ `hasMultiple != isB5`). Đặt kỳ vọng
thấp và để cuối.

---

## 9. Kỷ luật bằng chứng và runner niêm phong

### 9.1 Ba lớp ghim một bản dựng runner

| Lớp | Cơ chế |
|---|---|
| **(a) Biên nhận artifact mỗi lần chạy** | `runner_client.py:481-491` băm SHA-256 mọi artifact khai báo, lấy ở `start()` và lại ở `shutdown()`; khác nhau ⟹ `RBWP7_RUNNER_ARTIFACT_DRIFT`. Tập artifact gồm **mọi tệp trong `runner_root`**, sáu tệp FleetPy, `environment.lock.yml`, mọi `ridebound_fleetpy/*.py`, toàn bộ cây scenario |
| **(b) Định danh manifest trên dây** | `policyConfigurationHash`, `coreCommitSha` (`git rev-parse HEAD`), `binarySha256`. Runner kiểm ở `RunnerSession.cs:300-323` ⟹ `HASH_MISMATCH`, `FailSession` |
| **(c) Niêm phong cây bằng freeze receipt** | §9.3 |

### 9.2 Ba hash có tên

| Tên | Phủ cái gì |
|---|---|
| `repositoryInventorySha256` | **Toàn bộ cây làm việc Git nhìn thấy được** — cả tracked lẫn untracked-không-ignore — qua `git ls-files -z --cached --others --exclude-standard` |
| `semanticHash` | JSON chuẩn tắc của dict `semantic` |
| `publicationDigest` | `control._rb_publications`, lồng **bên trong** `semantic` |

⟹ **Mọi tệp mới bạn tạo trong kho đều đổi `repositoryInventorySha256`.** Đây là lý do
kỷ luật "không ghi gì vào kho" tồn tại, và là lý do tài liệu này nằm ở
`Report_INT3508`, không nằm trong `RideBound`.

### 9.3 Quy trình dựng runner niêm phong mới

Bắt buộc theo đúng tám bước, dẫn xuất từ tiền lệ
`docs/benchmarking/wp8-011c-pre-outcome-runner-artifact-repin.md`:

1. `dotnet test RideBound.slnx` xanh (baseline `AGENTS.md`).
2. Publish **Release** sạch ra một gốc **ngoài kho** (`E:\RideBoundData\...`),
   framework-dependent multi-file, phải có `RideBound.Runner.dll`.
3. Gốc publish phải **ổn định** — mọi tệp trong đó bị băm.
4. Thêm cấu hình nhánh mới vào `benchmarks/configurations/`, driver/grid, và dòng nhánh
   mới trong `ARMS` / `WP4_CONFIG_BY_POLICY`.
5. Viết **module freeze mới** (`wp14_freeze_v3.py`-style), **tự niêm phong**: đường dẫn
   của chính nó **và** đường dẫn test của chính nó phải nằm trong `STATIC_REPOSITORY_FILES`
   — có test bắt buộc điều này (`Wp14FreezeV2SelfSealTests`). **Không bao giờ sửa một
   receipt đã có**: `write_exclusive` từ chối.
6. Chạy builder với `--write --frozen-at-utc <Z>`, rồi chạy lại **không** `--write` để
   `verify_receipt` dựng lại và so **từng byte**.
7. Lấy `repositoryInventorySha256` **sau khi** mọi thứ đã commit, truyền vào mọi lần chạy
   qua `--expected-repository-inventory-sha256`.
8. Chạy ma trận qua `wp14_run_matrix.py` — nó tự kiểm lại `wp4ConfigSha256`,
   `commitmentConfigSha256`, `driverSha256`, `scenarioContentSha256` trước khi spawn.

### 9.4 Đối chứng bắt buộc khi đổi runner

Theo kỷ luật đã dùng ở thí nghiệm ratchet (mục 7.5 tài liệu bàn giao): chạy **hai nhánh
đã biết kết quả** trên runner mới và yêu cầu **tái lập đúng từng ô**. Tiền lệ: reference
1.581/1.581 sai lệch 0/20 ô; nopickuplock 1.583/1.583 sai lệch 0/20 ô.

### 9.5 Mười bẫy đã vấp — đọc lại trước mỗi đợt chạy

Giữ nguyên mục 12 của tài liệu bàn giao. Ba bẫy liên quan nhất tới kế hoạch này:

- **12.4 Đếm lỗi thay vì phân loại lỗi.** Suýt báo "Định lý 1 sai" khi 11/20 ô hỏng ở
  k=1; mở log ra thì cả 11 là bất biến miền, không phải vô nghiệm do cam kết. **P4 và P6
  phải phân loại theo mã lỗi thật.**
- **12.5 Đoán tên trường trong bằng chứng.** Dump cấu trúc trước khi viết bộ phân tích.
- **12.7 `semanticHash` khác nhau ≠ quyết định khác nhau.** Muốn biết quyết định có khác
  không, so **chuỗi (xe, ứng viên) được gán** và **tập lời hứa đã sắp xếp trong từng
  khung**.

---

## 10. Kết quả dự tính, và tiêu chí thành công / thất bại

| Giai đoạn | Kết quả dự tính | Tiêu chí thành công | Tiêu chí vô hiệu |
|---|---|---|---|
| P0 | `docs/18` đồng bộ | Chuỗi authorize không kẹt | — |
| P1 | Báo cáo hết lỗi | `tectonic` sạch; 0 câu trong §6.1 | — |
| P2 | 9/10 xong | P2.10 có phân bố thời điểm prune | Prune do lock rải đều ⟹ **trục C vô hiệu** |
| P3 | Tỉ lệ phục vụ **không đổi** | Có kết luận một trong hai | ppm vẫn degenerate ≥99% |
| P4 | ≥18/20 ô chạy ở k=1 | Ô hỏng còn lại không phải `PICKUP_WINDOW` | FleetPy từ chối ≥3 ô ⟹ dùng fixture 900 s |
| P5 | Nhánh hạn chót chạy được, quét `l` | Đường cong `l` ↔ phục vụ | Trên panel tĩnh chênh <0,3 pp ⟹ **chuyển thẳng P6** |
| **P6** | **`deadline-l` gate ≫ `conduct-β` ở k=1** | **Chênh ≥3×** | **Chênh <3× ⟹ hạ đóng góp xuống "phép đo + khung khái niệm"** |
| P7 | `γ` lớn hơn nhiều panel tĩnh | Báo cáo có DKW + Clopper–Pearson | — |
| P8 | 2 mức nhu cầu + runtime | Có bảng | — |
| P9 | Tái lập hình dạng Elmi | Là comparator hợp lệ | Chỉ dịch chuyển gánh nặng ⟹ không phải đóng góp |
| P10 | Chưa rõ | Một phần −7,13 pp là giá tìm kiếm | Không cải thiện ⟹ kết quả âm hợp lệ |

**Con số neo đã có, dùng để đối chiếu khi chạy:**

| | B1 | C1 |
|---|---:|---:|
| Phục vụ (panel A) | 1.735 (80,32%) | 1.581 (73,19%) |
| `C` gánh nặng conduct | 64.863 s | 128 s |
| `X` trôi dạt | 6.719 s | 6.695 s |
| `V` khách nhìn thấy, cực đại/khách | 585,1 s | **38,7 s** |
| CVaR₉₅ của `A_r` | 336,5 s | 1,6 s |
| Khách `A_r = 0` | 76,8% | 99,3% |

---

## 11. Rủi ro

| # | Rủi ro | Mức | Giảm thiểu |
|---|---|---|---|
| R1 | **Bẫy `EffectivePolicies`** — nhánh mới âm thầm chạy không ràng buộc | **Cao × Cao** | Thêm test khẳng định mỗi `RidePoolingPolicyKind` mới có nhánh tường minh; `EffectivePolicyFairnessTests.cs:33-39` đã tự liệt kê enum và sẽ đỏ |
| R2 | P4: FleetPy từ chối plan sau khi nới `Board()` | Cao × Cao | Dry-run **một ô** trước; phương án dự phòng fixture 900 s |
| R3 | Sửa ppm làm đổi mọi decision hash ⟹ không so được với bằng chứng cũ | Chắc chắn × Trung bình | Chỉ chạy trên panel phát triển; giữ nguyên H6 niêm phong; chạy hai nhánh đối chứng (§9.4) |
| R4 | P6 cho kết quả âm (chênh <3×) | Trung bình × Cao | **Đã khai báo trước** là kết quả hợp lệ (ràng buộc WP15 #7). Khóa luận vẫn đứng trên P0–P2 |
| R5 | Cổng quản trị chặn P4 trở đi | Cao × Trung bình | P0.3 chốt phạm vi từ đầu; nhánh A không cần ADR |
| R6 | Dung lượng: đang **33,62 GB**, mục tiêu <30 GB | Chắc chắn × Thấp | Ứng viên xóa an toàn: `wp14/driftwide-v1` (1,10 GB), `wp14/levelc-v1` (1,20 GB) — kết luận đã trích đủ. ⚠️ `AGENTS.md` cấm xóa artifact kết quả như thao tác dọn dẹp ⟹ cần quyết định tường minh |
| R7 | Thêm chiều thứ 11 vì nghĩ là cách dễ | Trung bình × Rất cao | §P5 đã chứng minh là ~30 điểm sửa + mất mọi hash. **Dùng luật khóa.** |
| R8 | Dùng số H6 để chọn tham số nhánh mới | Trung bình × Cao | Ràng buộc WP15 #2. Mọi mức phải chọn trên panel phát triển |
| R9 | Báo cáo Gini và bị hỏi ngược | Trung bình × Trung bình | §3.8 đã đo: Gini **tăng** khi cơ chế tốt lên. Dùng đo tuyệt đối ở đuôi |
| R10 | Giới hạn phiên API cắt ngang công việc dài | Cao × Thấp | Chia nhỏ; lưu kết quả trung gian ra tệp sau mỗi bước |

---

## 12. Lịch trình và phụ thuộc

```
P0 Quản trị ──┬── P1 Sửa báo cáo ──────────────┐
              │                                 ├──► ĐỦ ĐỂ ĐÓNG KHÓA LUẬN
              └── P2 Phân tích dữ liệu đã có ───┘
                        │
                        └── P2.10 (phủ định C1) ──► quyết định trục C
                        
P3 Sửa ppm ──┬── P9 Nhánh chọn lọc (Elmi)
             └── P5 Nhánh hạn chót ──┐
                                      ├──► P6 THÍ NGHIỆM QUYẾT ĐỊNH ──► P7 Hai lớp
P4 Mở khóa trôi dạt ──────────────────┘
                                      
P8 Vững chắc ── song song, bất cứ lúc nào sau P3
P10 Plan pool ── cuối cùng, kỳ vọng thấp
```

**Đường găng:** `P0 → P3 → P4 → P5 → P6`. P4 là mắt xích rủi ro nhất.

**Nếu thời gian ngắn:** làm P0 → P1 → P2. Ba giai đoạn này **không tốn lần chạy nào** và
đã bịt đúng những lỗ mà một phản biện đọc kỹ sẽ chọc vào.

---

## 13. Phụ lục

### 13.1 Script đo đã có

`E:\Code\Report_INT3508\ridebound-scratchpad\claude-measurements-2026-09\` — 14 tệp:

| Script | Đo gì |
|---|---|
| `promise_paths.py` | Trích quỹ đạo lời hứa từ transcript (13 s cho 20 ô) |
| `identity.py` | Độ khít `A + d = B` từng lần công bố |
| `aleb.py` | Điều kiện (H) `A ≤ B` |
| `tvcheck.py` | `D⁺ ≤ E ≤ V ≤ C + X`, phân bố `V` theo khách |
| `endpoint.py` | So ngưỡng `D⁺` / `A` / `V` |
| `drifttv.py` | **So dưới trôi dạt — phép đo quyết định** |
| `equity.py` | Đuôi, CVaR, Gini, tập trung |
| `analyze1.py` | Thời điểm gánh nặng, chính sách công bố, phơi nhiễm |
| `analyze2.py` | Hiệu quả phân bổ ngân sách |
| `analyze3.py` | Độ lớn từng lần dời, dấu chân ngoại ứng |
| `excess.py` | Phần vượt trần của phương án bị loại |
| `choiceset.py` | Độ mỏng tập lựa chọn, mẫu số đúng |
| `objorder.py` | Thứ tự tầng mục tiêu thật |
| `realcase.py` | Trích ca `v/e/p` thật để minh họa |

Cách chạy: `E:/RideBoundData/wp7/envs/fleetpy-1.0.2/python.exe -B <script>.py`

### 13.2 Lệnh chạy một ô

```bash
E:/RideBoundData/wp7/envs/fleetpy-1.0.2/python.exe -B \
  simulators/fleetpy-ridebound/actual_fleetpy_medium_preflight.py \
  --label "<nhan>" \
  --fleetpy-root E:/RideBoundData/wp7/FleetPy-1.0.2 \
  --runner-root  <goc runner niem phong> \
  --dotnet "C:/Program Files/dotnet/dotnet.exe" \
  --commitment-config benchmarks/configurations/<cam-ket>.json \
  --wp4-config        benchmarks/configurations/<chinh-sach>.json \
  --scenario             <fixture>/scenario-content.json \
  --derivative-manifest  <fixture>/derivative-manifest.json \
  --normalization-report <fixture>/normalization-report.json \
  --selection-frame      <fixture>/selection-frame.json \
  --driver benchmarks/scenarios/<panel>/<cell>.driver.json \
  --output <thu muc moi, KHONG duoc ton tai> \
  --repeats 1 --master-seed 7 \
  --expected-repository-inventory-sha256 <64 hex>
```

`~11 phút/ô` một luồng; 6 luồng song song ⟹ 20 ô ≈ 45 phút. `19–67 MB/ô`.

⚠️ `--output` dùng `mkdir(exist_ok=False)` — **không bao giờ dùng lại thư mục**. Thư mục
dở dang (có `transcript` nhưng không có `summary.json`) sẽ chặn lần chạy lại; phải xóa.

### 13.3 Mười chiều cam kết

| # | Enum | Chuỗi giao thức | Đơn vị |
|---|---|---|---|
| 0 | `PickupEtaTotalMs` | `pickup_eta_total_ms` | ms |
| 1 | `DropEtaTotalMs` | `drop_eta_total_ms` | ms |
| 2 | `MaterialEtaRevisionCount` | `material_eta_revision_count` | đếm |
| 3 | `VehicleSwitchCount` | `vehicle_switch_count` | đếm |
| 4 | `PickupStopRelocationMm` | `pickup_stop_relocation_mm` | mm |
| 5 | `PickupStopSwitchCount` | `pickup_stop_switch_count` | đếm |
| 6 | `DropStopRelocationMm` | `drop_stop_relocation_mm` | mm |
| 7 | `DropStopSwitchCount` | `drop_stop_switch_count` | đếm |
| 8 | `IncumbentOrderInversionCount` | `incumbent_order_inversion_count` | đếm |
| 9 | `PrePickupInsertedStopCount` | `pre_pickup_inserted_stop_count` | đếm |

### 13.4 Ngữ nghĩa khóa — dễ hiểu sai

| Cơ chế | Kích hoạt khi | Chặn |
|---|---|---|
| `accepted_assignment` | **luôn luôn** | chỉ `Vehicle` — hard-wired, không cấu hình được |
| `onboard` | `Lifecycle == Onboard` | `Vehicle \| PickupStop \| PickupEta` — hard-wired |
| `finalConfirmationLocks` | **chỉ** `Lifecycle == WaitingPickup` | theo cấu hình |
| `freezeHorizon` | `0 ≤ previous.PickupEta − now ≤ horizon` | theo cấu hình |
| `ratchetLocks` | chỉ hợp lệ trên `PickupEta \| DropEta` | một chiều |

> **Chi tiết quan trọng nhất:** khóa so ứng viên với **mốc ngoại sinh**, không so với lời
> hứa đã công bố (`CommitmentDecisionValidator.cs:347-353`). Vì vậy **trôi dạt ngoại
> sinh không bao giờ làm vướng khóa** — chỉ dịch chuyển do quyết định mới làm vướng. Đây
> là một tính chất thiết kế rất đẹp và nên được nêu trong báo cáo.

### 13.5 Những gì tài liệu này KHÔNG authorize

- Không authorize `RB-WP14R-009..012`.
- Không authorize execution của WP15.
- Không mở H7/WP17.
- Không đổi margin, panel, denominator, factor level hay failure treatment nào.
- Không lấy một tham số số học nào từ bất kỳ paper nào.
- Không claim RideBound nhanh hơn, tốt hơn hay tương đương bất kỳ paper nào.

### 13.6 Nguồn đã xác minh trong vòng khảo sát này

Elmi, Moylan, Alonso-Mora & Fielbaum (2026) TR-C 192:105897 — bản PDF cục bộ, SHA-256
`5a68817ab7d231c0875686d9b468d924d80695621379902756efd5b4cfe728a5` ·
Schulz & Pfeiffer (2026) OR Spectrum 48:541–586 ·
Schmidt, Golak, Schulz & Fliedner (2026) TSP-SC, arXiv:2609.11950 ·
Sivagnanam, Mukhopadhyay, Samaranayake, Dubey & Laszka (2026) ICCPS ·
Zalesak, Hu & Samaranayake (2025) arXiv:2504.10649 ·
Haferkamp (2024) *"Design of multi-optional pickup time offers in ride-sharing systems"* ·
Fu (2002) TR-B 36(6):485–506 ·
Chen, Eberle, Megow, Schewior & Stein (2018) arXiv:1811.08238 ·
Eberle, Megow & Schewior (2019/21) arXiv:1912.10769 ·
Shah, Lowalekar & Varakantham (AAAI-20) arXiv:1911.08842 ·
Li, Lei, Qian & Ukkusuri (2025) arXiv:2506.20788 ·
Massart (1990) hằng số chặt DKW ·
arXiv:2509.11859 *"Statistical Model Checking Beyond Means: Quantiles, CVaR, and the DKW
Inequality"*

### 13.7 Việc còn dở của chính tài liệu này

Luồng khảo sát web về **lý thuyết switching cost / smoothed online convex optimization /
metrical task systems** bị giới hạn phiên API cắt ngang và **chưa hoàn tất**. Đây là
"ngôi nhà lý thuyết" tự nhiên cho đại lượng `Σ|q_t − q_{t−1}|` mà khóa luận chưa kết
nối tới. Nên quét nốt trước khi viết Chương 2, với các từ khóa: *metrical task systems*,
*smoothed online convex optimization*, *online balanced descent*, *switching cost*,
*bounded recourse*, *bounded migration*.

Phần thống kê (§P7) tôi đã tự tra và xác minh DKW + Massart + Clopper–Pearson, nhưng
**chưa** tra kỹ: tolerance interval theo công thức Wilks, và extreme value theory cho
đuôi. Nên bổ sung nếu P7 được thực hiện.

