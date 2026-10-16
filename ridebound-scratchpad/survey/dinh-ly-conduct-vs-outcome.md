# Nghĩa vụ phương tiện vs nghĩa vụ kết quả — định lý và đo đạc

Ghi ngày 2026-09-14. Tài liệu độc lập, viết để lắp thẳng vào khoá luận.
Không ghi gì vào repository.

---

## 0. Vì sao câu hỏi này tồn tại

Một hệ điều phối **công bố lời hứa** cho hành khách ("xe đón bạn lúc 9:10"), rồi sau đó
liên tục tối ưu lại. Khi lời hứa bị dời, phải tính vào tài khoản của nhà xe **bao nhiêu**?

Có đúng hai cách tính, và chúng không tương đương.

**Phân biệt này chỉ nảy sinh khi hệ thống đồng thời có hai tính chất:**

1. **Công bố lời hứa** cho khách (có "điều đã nói" để so)
2. **Mô hình hoá trôi dạt giao thông** (thời gian di chuyển thay đổi theo thời gian)

Thiếu (1) thì không có mốc để so. Thiếu (2) thì hai cách trùng nhau hoàn toàn.

**ĐÍNH CHÍNH (2026-09-14, sau khi kiểm tra fixture).** Bản đầu của mục này khẳng định panel
có `travelTimesUpdated`. **Sai.** Kiểm tra trực tiếp:

- `scenario-content.json` có `travelSnapshots` **dài đúng 1**
- 108 sự kiện, **toàn bộ** là `requestArrived`; không có sự kiện cập nhật giao thông
- quét toàn bộ transcript một run: **đúng 1 định danh snapshot** (`781840ce…`) từ đầu đến cuối

Nghĩa là đồ thị thời gian di chuyển **tĩnh** trong suốt 2 giờ mô phỏng. Vậy 9,204 giây trôi
dạt đo được **không đến từ giao thông**, mà đến từ **độ trễ thực thi**: xe di chuyển theo bước
rời rạc và có thời gian dừng đón/trả, nên khi chiếu lại cùng một lộ trình từ vị trí thật hiện
tại (`CommitmentDecisionValidator.cs:316-340`, dùng `oldVehicle.Route` + `TravelTimes` hiện
hành + `SimulationTime` hiện hành) thì giờ đến lệch đi một chút.

Đó là lý do `d` nhỏ: p50 = 4.9 s, max = 39.9 s. Đây là **cận dưới** của trôi dạt, không phải
giá trị điển hình của một hệ thật.

**Hệ quả cho luận điểm.** Đẳng thức B = A + d vẫn đúng chính xác. Nhưng khẳng định "A và B
gần như không khác nhau" là **tính chất của panel này**, không phải tính chất của bài toán.
Xem mục 7 và mục 12.

---

## 1. Ký hiệu

Tại một thời điểm quyết định, với hành khách r đang có lời hứa mở:

| Ký hiệu | Nghĩa |
|---|---|
| `v` | **previous** — lời hứa đã công bố lần cuối cho khách |
| `e` | **exogenous** — chính kế hoạch đó, **chiếu lại từ vị trí thật hiện tại của xe** (cùng lộ trình, cùng phân công, chỉ khác điểm xuất phát) |
| `p` | **proposed** — lời hứa mà phương án đang xét sẽ tạo ra |
| `d` | **trôi dạt** = `\|e − v\|` — phần do giao thông, **không phải do nhà xe** |

Hai cơ sở tính ngân sách:

| | Công thức | Ý nghĩa | Tên pháp lý |
|---|---|---|---|
| **A — conduct** | `\|p − e\|` | *"tôi làm bạn trễ thêm bao nhiêu so với lẽ ra bạn đã bị"* | nghĩa vụ **phương tiện** (obligation de moyens) |
| **B — outcome** | `\|p − v\|` | *"bạn trễ bao nhiêu so với điều tôi đã nói"* | nghĩa vụ **kết quả** (obligation de résultat) |

Ngân sách là **bộ đếm tích luỹ** theo (hành khách, chiều), đơn điệu tăng, so với trần β.

Trong code: `CommitmentBudgetBasis.DecisionInduced` (A) và `.CustomerVisible` (B).

---

## 2. Ví dụ cụ thể (dùng được trong báo cáo)

Khách đặt xe 9:00, được báo **đón lúc 9:10**. Đến 9:05 hệ thống cân nhắc đổi kế hoạch.

| Mốc | Giá trị |
|---|---|
| `v` đã hứa | 9:10:00 |
| `e` nếu không làm gì (xe đang kẹt, trễ 40 s) | 9:10:40 |
| `p` nếu đổi kế hoạch | 9:11:10 |

- **A tính:** 9:11:10 − 9:10:40 = **30 giây**
- **B tính:** 9:11:10 − 9:10:00 = **70 giây**

Bây giờ xét phương án **không làm gì** (`p = e = 9:10:40`):

| | Bị tính bao nhiêu |
|---|---|
| **A** | 9:10:40 − 9:10:40 = **0 giây** → luôn hợp lệ |
| **B** | 9:10:40 − 9:10:00 = **40 giây** → **đã vượt trần 30 giây** |

**Theo cách B, ngay cả việc không làm gì cũng là vi phạm.** Nếu mọi phương án khác cũng vượt,
chiếc xe không còn kế hoạch hợp lệ nào và hệ thống dừng.

---

## 3. Bất biến nền (đã xác minh trong code)

Tập phương án của mỗi xe **luôn chứa phương án không-làm-gì** (no-op). Ba chỗ khẳng định độc lập:

| Vị trí | Nội dung |
|---|---|
| `CandidateFleetSelector.cs:23` | *"Every vehicle requires at least one feasible plan, including no-op."* |
| `CandidatePortfolioRetainer.cs:56` | *"A per-vehicle portfolio requires one no-op candidate."* |
| `HardVectorCandidateAssessor.cs:204` | tách hai chế độ hỏng: *"even the safety no-op was absent"* vs *"rejected every generated candidate"* |

Cũng bắt buộc về mô hình: ILP có ràng buộc `Σ(options của xe v) = 1`.

Với no-op: kế hoạch không đổi ⟹ phép chiếu của nó **chính là** `e`. Tức `p(no-op) = e`.

---

## 4. Đẳng thức trung tâm: **B = A + d**

Bất đẳng thức tam giác cho ngay:

```
|p − v|  ≤  |p − e| + |e − v|        tức     B ≤ A + d
```

Dấu bằng xảy ra khi `p`, `e`, `v` xếp cùng một chiều. **Điều kiện đó đúng trong hệ này**, dựa
trên hai sự kiện đã đo:

| Điều kiện | Bằng chứng đo được |
|---|---|
| Quyết định không bao giờ làm tốt lên, tức `p ≥ e` | `decisionMovedEarlier = 0` trên **421,752** lần sửa. Nguyên nhân cơ học: bộ sinh phương án **chỉ chèn thêm, không bỏ bớt** — chèn một điểm dừng chỉ đẩy lùi được khách cũ |
| Phép phân rã cộng khít | độ hụt **0.00 – 0.07%** trên 6 nhánh (xem bảng §7) |

> **Sổ cái của B = sổ cái của A + trôi dạt tích luỹ.**

---

## 5. Ba định lý

### Định lý 1 — Cơ sở A luôn thoả được

`A(no-op) = |p − e| = |e − e| = 0`.
Bộ đếm sau = bộ đếm trước + 0 = bộ đếm trước ≤ β (vì mọi lần công bố trước đều đã qua kiểm tra).

**⟹ Dưới cơ sở A, tập phương án của một xe không bao giờ bị làm rỗng. ∎**

*Ý nghĩa:* A khả thi **không phải vì nó dễ dãi**, mà vì nó đo so với một mốc mà nhà xe kiểm
soát được. "Không làm gì" theo định nghĩa là "không gây ra gì".

### Định lý 2 — Cơ sở B có thể vô nghiệm

`B(no-op) = |e − v| = d`. Nếu `Σd > β` thì ngay cả no-op cũng bị loại → tập rỗng →
`VehicleHasNoFeasibleCandidate` → lần chạy hỏng. ∎

### Định lý 3 — **B không bao giờ phục vụ được nhiều hơn A, với MỌI β**

Từ §4: `B ≥ A` tại mọi lần công bố ⟹ bộ đếm của B ≥ bộ đếm của A tại mọi thời điểm
⟹ mọi phương án B chấp nhận thì A cũng chấp nhận
⟹ **tập khả thi của B ⊆ tập khả thi của A**
⟹ số khách B phục vụ **≤** số khách A phục vụ, **với mọi trần β**. ∎

*Đây là điểm quan trọng nhất:* kết quả "B không hơn gì" **không phải là quan sát may mắn ở
β = 30 s**. Nó là định lý, đúng ở mọi β.

### Hệ quả — hai cách chỉ khác nhau trong một dải hẹp bề rộng `d`

Một phương án bị B loại mà A không loại **khi và chỉ khi**

```
A_sổcái  ≤  β  <  A_sổcái + d
```

tức nó phải rơi đúng vào một dải rộng **`d`** ngay dưới trần.

**`d` không phụ thuộc β.** Nó do giao thông quyết định. Nên nới trần **không** làm dải rộng ra.

---

## 6. Đo đạc — hai đại lượng quyết định

### 6.1 Trôi dạt tích luỹ mỗi hành khách (bề rộng dải `d`)

Đo trên 1,581 hành khách, panel A, nhánh C1:

| | Giá trị |
|---|---|
| p50 | **4.9 s** |
| p90 | 10.8 s |
| p95 | 13.3 s |
| p99 | 22.2 s |
| **max** | **39.9 s** |

Số hành khách mà **riêng trôi dạt** đã vượt trần:

| Trần β | Số khách vượt | Hệ quả |
|---:|---:|---|
| 30 s | **3** (0.19%) | B vô nghiệm với 3 người này |
| 60 s | **0** | B hết vô nghiệm |
| ≥ 120 s | **0** | B hết vô nghiệm |

### 6.2 Cú nhảy do một lần chèn

Mức vượt trần của các phương án bị cắt vì ngân sách (trần 30 s):

| | Vượt thêm |
|---|---|
| p10 | 31 s |
| **p50** | **101 s** |
| p90 | 232 s |
| max | 483 s |

Tức **cú nhảy điển hình ≈ 130 giây** (30 + 101).

### 6.3 So sánh trực tiếp A vs B ở cùng trần

| Trần | A khả thi | B khả thi | Phục vụ trên các ô chung |
|---|---:|---:|---|
| 30 s | **20/20** | 16/20 | A = 1294, B = 1294, **chênh 0** |
| 120 s | **20/20** | 16/20 | A = 1267, B = 1266, **chênh −1** |

Tập ô vô nghiệm của B:

| β | Ô vô nghiệm |
|---|---|
| 30 s | 16-r2, **16-r4**, 17-r1, 17-r3 |
| 120 s | 14-r4, 15-r2, **16-r4**, 17-r4 |

Giao nhau đúng **1/4 ô** — nới trần gấp 4 lần **dời chỗ đau** chứ không chữa.

---

## 7. Vì sao chênh lệch bằng 0 — khớp giữa lý thuyết và số liệu

| | |
|---|---|
| Bề rộng dải khác biệt `d` | **~5 giây** (trung vị) |
| Cú nhảy cần lọt vào dải đó | **~130 giây** |

Xác suất một cú nhảy 130 giây rơi trúng một dải rộng 5 giây ngay dưới trần là **rất nhỏ**.
Đó chính xác là lý do đo ra **0** khách ở β=30 s và **1** khách ở β=120 s.

**Không phải trùng hợp — là hệ quả số học của `d ≪ cú nhảy`.**

### Và khi nới trần lên 5–10 phút thì sao?

- Dải khác biệt vẫn rộng ~5 s (`d` không đổi theo β)
- Cú nhảy vẫn ~130 s
- ⟹ khác biệt **vẫn ~0**
- Còn tính vô nghiệm thì **biến mất** từ β ≥ 60 s

> **Không tồn tại β nào mà B tốt hơn A. Ở β nhỏ B vô nghiệm; ở β lớn B ≡ A.**

### Kiểm tra độ khít của phép phân rã (cơ sở cho đẳng thức B = A + d)

| Nhánh | A (decision) | d (exogenous) | A + d | B (visible) | hụt | hụt % |
|---|---:|---:|---:|---:|---:|---:|
| B1 | 74,443 | 9,203 | 83,646 | 83,587 | 58 | **0.07%** |
| nobudget | 22,485 | 9,703 | 32,188 | 32,176 | 12 | 0.04% |
| budget300 | 15,809 | 9,641 | 25,450 | 25,441 | 9 | 0.03% |
| budget120 | 5,063 | 9,260 | 14,324 | 14,318 | 5 | 0.04% |
| budget60 | 1,109 | 9,184 | 10,293 | 10,291 | 1 | 0.01% |
| C1 | 128 | 9,204 | 9,332 | 9,332 | 0 | **0.00%** |

Đẳng thức `B = A + d` đúng tới **0.07%** ở trường hợp tệ nhất, và **chính xác tuyệt đối** ở C1.

---

## 8. Alonso-Mora đo cách nào? (viết lại 2026-09-14 — đã có toàn văn)

Bản đầu của mục này ghi *"chưa đọc được toàn văn Fielbaum & Alonso-Mora 2020"* và suy luận
gián tiếp. **Đã lấy được toàn văn** (`Unreliability_in_ridesharing_systems_Measuring_cha.pdf`,
TR-C 121:102831, 20 trang, CC-BY). Mục này thay thế hoàn toàn bản cũ. Hai câu trích từ "bản
arXiv" trong bản cũ **không có trong bài** — đã xoá.

### 8.1 Phải tách hai bài khác nhau

| | Scale analysis (Fielbaum–Tirachini–Alonso-Mora) | **Unreliability 2020** (Fielbaum–Alonso-Mora) |
|---|---|---|
| Bài toán | kinh tế học quy mô ODRP, đội xe nội sinh | **lời hứa công bố bị xê dịch** |
| Trùng với mình? | **không** — chỉ chung cỗ máy RTV/ILP | **có, và trùng nhiều** |
| Cơ sở A hay B | **không cái nào** — không có lời hứa công bố | **B, dạng yếu** |

Bài scale-analysis tự khai chỗ trống (§4.1): *"there are other negative externalities that the
model does not directly capture… Fielbaum & Alonso-Mora (2020) identify two types of
unreliability… **this is not a minor issue**"*. Nó **chỉ sang** bài 2020.

### 8.2 Bài 2020 đo gì — nguyên văn

```
Δt_w(r) = t_w(r) − t¹_w(r)        (thực tế − lần công bố ĐẦU TIÊN)
Δt_d(r) = t_d(r) − t¹_d(r)
ΔD(r)   = Δt_w(r) + Δt_d(r)
```

> *"First-announced waiting time t¹_w(r)… the waiting time that would be achieved if the
> vehicle's itinerary remains unchanged until picking the passenger up."*

> *"In the remainder of the paper we consider the positive values for these indices, and
> **truncate to zero** those that are negative."*

Và Định nghĩa 9:
> *"(Number of changes faced per request) …we compute the expected waiting time at each
> assignment, since the first one until it is picked-up, and **count how many times this
> prediction increases**."*

### 8.3 Cơ sở nào? — **B, nhưng ba điểm yếu hơn**

| | Bài 2020 | RideBound |
|---|---|---|
| Mốc so | **một** lần công bố đầu (`t¹`) | lời hứa **gần nhất**, tái công bố mỗi quyết định |
| Dạng | **hiệu hai đầu** \|cuối − đầu\| | **độ dài đường đi** Σ\|p − v\| trên chuỗi |
| Dấu | cắt âm về 0 | trị tuyệt đối, cả hai chiều |
| Độ lớn × chuỗi | **không có** (có Δ=độ lớn×hai-đầu; có NC=đếm×chuỗi) | **có** — chính là đại lượng đặt trần được |
| Vai trò | **thước đo hậu nghiệm** | **ràng buộc tiền nghiệm** có trần β |
| Tách nhân quả | Def 1/Def 2 — **định tính, bằng lời** | **ba mốc số v/e/p mỗi lần công bố** |
| Trôi dạt giao thông | **loại khỏi phạm vi** (§2: *"we do not discuss unreliability sources… such as congestion"*) | có `d`, dù nhỏ (xem mục 0) |

Khác biệt (b) không vụn vặt: lời hứa 9:00 → 9:10 → 9:00 cho **Δ = 0** theo họ, **20 phút**
theo mình. Khách đã bị làm phiền hai lần.

### 8.4 Họ CÓ frontier — Chân B của mình là lặp lại

§6 + Table 5. Ba chế độ, đội 2000 xe sức chứa 4:

| Scenario | Av. Waiting | Av. Detour | Av. Delay | **Rejected** | Av. users' cost |
|---|---|---|---|---|---|
| Base | 1.01 | 0.65 | 1.66 | **34.5%** | 9.56 |
| Intermediate | 1.51 | 1.01 | 2.52 | **31.2%** | 10.3 |
| Fully controlled | 0.77 | 0.94 | 1.71 | **45.6%** | 11.6 |

- **Fully controlled** = *"it is marked as non-rejectable… and her maximum waiting time is
  **updated to the predicted one**"* → **đúng là `ratchetLocks` của mình**, tức **cơ sở B với β = 0**
  trên chiều đón.
- **Intermediate** = cấm huỷ-sau-khi-nhận, ETA vẫn được trôi.

Kết luận của họ, nguyên văn: *"This reinforces the need of **more sophisticated ideas to
control unreliability**."*

### 8.5 Cái gì mình KHÔNG được nhận là mới nữa

Phải ghi thẳng trong khoá luận:

1. Khái niệm one-time unreliability — **của họ** (Def 3)
2. Phân loại nguyên nhân khách-vs-nhà-điều-hành — **của họ** (Def 1/2), tuy chỉ định tính
3. Đo độ lớn xê dịch mỗi khách, phân bố không gian, ai chịu thiệt — **của họ**
4. Đếm số lần đổi dự báo — **của họ** (Def 9)
5. Đánh đổi ổn định ↔ tỉ lệ phục vụ — **của họ** (§6)
6. Ratchet trên ETA đón như một cơ chế — **của họ** ("fully controlled")
7. Cấm huỷ-sau-khi-nhận — **của họ** ("intermediate")

⟹ **Chân A và Chân B của RideBound là tái lập + tinh chỉnh bài 2020 trên panel khác.**
Với KLTN, tái lập có kiểm chứng vẫn có giá trị — nhưng **phải gọi đúng tên**.

### 8.6 Cái gì còn lại là của mình

1. **Trần số β** trên xê dịch. Họ có 3 chế độ bật/tắt; không có tham số liên tục, không có
   thang β. Họ **gọi tên chỗ trống này** ở câu cuối §6.
2. **Dạng cộng dồn theo chuỗi** — điều kiện cần để đặt trần được (8.3 dòng 3).
3. **Câu hỏi cơ sở A vs B và định lý của nó.** Không diễn đạt được trong mô hình của họ:
   không có chuỗi tái công bố, và trôi dạt bị loại khỏi phạm vi nên `d = 0`.
4. **Bảo đảm khả thi** (Định lý 1). Không có đối ứng trong bài họ.

### 8.7 Định lý giải thích một con số đã công bố của họ

"Fully controlled" = cơ sở **B**, β = 0, chiều đón. Tỉ lệ từ chối **34.5% → 45.6%** (+11.1 pp).

Định lý 2 nói cơ sở B **có thể vô nghiệm**, vì no-op vẫn bị tính phí `d`. Đo được đúng vậy:
ở trần 30 s, cơ sở A khả thi **20/20 ô**, cơ sở B chỉ **16/20**.

⟹ Luận điểm: *một phần cái giá 11.1 pp của Fielbaum & Alonso-Mora (2020) không phải giá của
việc giữ lời hứa, mà là giá của việc chọn sai cơ sở tính. Cùng độ chặt, cơ sở hành vi luôn
khả thi (Định lý 1) và không bao giờ phục vụ ít hơn (Định lý 3).*

**Giới hạn phải ghi kèm:** kịch bản của họ siết **hai** thứ cùng lúc (ratchet **và** cấm huỷ),
nên không quy toàn bộ 11.1 pp cho cơ sở tính. Đây là **cơ chế có bằng chứng**, không phải
quy kết đã chứng minh.

---

## 9. Tóm tắt: cái gì chứng minh, cái gì đo

| | Loại |
|---|---|
| A luôn thoả được (Định lý 1) | **chứng minh** + xác nhận bằng code |
| B có thể vô nghiệm (Định lý 2) | **chứng minh** + đo (4/20 ô) |
| **B không bao giờ hơn A, với mọi β** (Định lý 3) | **chứng minh** |
| Khác biệt chỉ nằm trong dải rộng `d`, `d` độc lập với β | **chứng minh** |
| `d` thực tế = 4.9 s trung vị, 39.9 s tối đa | **đo** |
| Cú nhảy thực tế ≈ 130 s | **đo** |
| ⟹ khác biệt ≈ 0 | **suy ra**, và đo xác nhận: 0 và 1 khách |
| Nới β dời chỗ vô nghiệm chứ không chữa | **đo** (giao nhau 1/4 ô) |

Đây là dạng kết quả tốt cho khoá luận: **phần định tính chứng minh được, phần định lượng đo
được, hai phần khớp nhau.**

---

## 10. Cách viết vào báo cáo

**Phát biểu vấn đề, không cần thuật ngữ:**
> *Một hãng gọi xe chung nên hứa điều gì với khách — "tôi sẽ không tự làm phiền bạn", hay
> "giờ của bạn sẽ không đổi"? Lời hứa thứ hai là điều khách thực sự muốn. Bài này chứng minh
> nó không dùng được, và đo xem nó hỏng như thế nào.*

**Kết luận thiết kế:**
> Muốn hứa với khách một cách **cưỡng chế được**, phải hứa về **hành vi của mình**, không thể
> hứa về **kết quả** — vì một phần kết quả nằm ngoài tầm kiểm soát của người hứa. Lời hứa về
> kết quả không mua thêm được gì (Định lý 3) mà lại làm hệ thống vô nghiệm (Định lý 2).

**Neo vào luật hợp đồng:**
> Đây là phiên bản thuật toán của phân biệt kinh điển **nghĩa vụ phương tiện / nghĩa vụ kết
> quả**. Luật sư hứa cố hết sức, không hứa thắng kiện. Thợ lắp thang máy hứa thang chạy.
> Luật đã kết luận từ lâu rằng không thể áp nghĩa vụ kết quả khi một phần kết quả nằm ngoài
> tầm kiểm soát — nếu không hợp đồng trở nên bất khả thi. Ta chứng minh và đo được đúng điều
> đó trong điều phối xe.
>
> **Và đây mới là chỗ mới:** luật và hợp đồng SLA xử lý ranh giới "beyond reasonable control"
> bằng **văn xuôi** — điều khoản bất khả kháng, tranh cãi sau sự việc. Mốc `exogenous` **tính
> được** ranh giới đó, theo từng quyết định và từng hành khách. Đó là một phép **xác định bất
> khả kháng tự động**.

**Lưu ý câu chữ:** phép phân rã không phải phân hoạch chính xác (bất đẳng thức tam giác, hụt
≤ 0.07%). Nên nói *"phần do nhà xe gây ra **bằng** 89.06% lượng khách nhìn thấy"* (một tỉ số),
**không** nói *"89.06% được gây ra bởi…"* (ngụ ý phân hoạch).

---

## 11. Nguồn số liệu

| Đại lượng | Nguồn |
|---|---|
| Trôi dạt mỗi khách, cú nhảy, so sánh A/B | `E:/RideBoundData/wp9/confirmatory-h6-panela-v2` (niêm phong), `exploratory-visible-basis-v1`, `exploratory-visible-sweep-v1` |
| A ở β=120 s | `E:/RideBoundData/wp9/frontier-v1/fr-budget120-*` |
| `decisionMovedEarlier = 0` | `wp14r-012-v6-promise-direction-v1-summary.json` |
| Bất biến no-op | `CandidateFleetSelector.cs:23`, `CandidatePortfolioRetainer.cs:56`, `HardVectorCandidateAssessor.cs:204` |
| Script đo | `scratchpad/measure/measure_instability.py`, `scratchpad/welfare/extract_promise_movement.py` |

| Toàn văn Fielbaum & Alonso-Mora 2020 | `C:/Users/quang/Downloads/Unreliability_in_ridesharing_systems_Measuring_cha.pdf` → trích ra `scratchpad/survey/unreliability.txt` |
| Toàn văn Scale analysis | `C:/Users/quang/Downloads/Scale_analysis_for_on-demand_ridepooling_systems_a.pdf` → `scratchpad/survey/scale.txt` |
| Panel có đồ thị tĩnh | `travelSnapshots` dài 1; 1 định danh snapshot trong toàn transcript |

---

## 12. Thí nghiệm còn thiếu — và vì sao nó đáng chạy

Mục 0 cho thấy `d` trên panel này nhỏ vì đồ thị tĩnh. Mục 7 cho thấy chênh lệch A–B **không
giãn theo β**; nó giãn theo `d`. Ghép lại thành một **dự đoán định lượng, có thể sai**:

> Nếu bơm biến động thời gian di chuyển vào panel với biên độ tăng dần, thì `d` tăng, và số
> ô **vô nghiệm dưới cơ sở B** (hiện 4/20 ở β=30 s) tăng theo, trong khi cơ sở A giữ nguyên
> **20/20** ở mọi biên độ. Khoảng cách phục vụ A − B giãn **đơn điệu theo `d`**, không theo β.

Vì sao đáng chạy:

1. Đây là **dự đoán trước khi đo**, không phải mô tả sau khi đo. Nếu sai thì định lý sai ở
   đâu đó — đó mới là bằng chứng có giá trị.
2. Cơ sở A giữ 20/20 ở **mọi** mức trôi dạt là hệ quả trực tiếp của Định lý 1 (no-op có
   p = e ⟹ delta = 0, độc lập với `d`). Một phản ví dụ sẽ phá Định lý 1.
3. Nó biến khẳng định *"A không bao giờ kém hơn B"* từ **đúng-nhưng-rỗng** trên panel này
   thành **đúng-và-đo-được**.
4. Nó nối thẳng vào con số 45.6% của Fielbaum & Alonso-Mora (2020) ở mục 8.7.

**Chi phí:** cần thêm nhiều snapshot travel-time vào fixture, tức **sửa fixture** — không còn
là panel niêm phong nữa, phải chạy như một thí nghiệm thứ cấp riêng, giống cách đã làm với
ratchet trên runner `931114e2`. Chưa chạy. Chưa xin phép.

---

## 13. Bảng điểm trung thực (2026-09-14)

| Hạng mục | Trạng thái |
|---|---|
| Khái niệm lời hứa bị xê dịch | **Fielbaum & Alonso-Mora 2020 đã có** |
| Phân loại nguyên nhân (định tính) | **họ đã có** (Def 1/2) |
| Đo độ lớn + đếm số lần | **họ đã có** (Δ, NC) |
| Frontier ổn định ↔ phục vụ | **họ đã có** (§6 Table 5) |
| Ratchet như một cơ chế | **họ đã có** ("fully controlled") |
| Trần số β trên xê dịch cộng dồn | **chưa ai làm** — họ gọi tên chỗ trống này |
| Dạng cộng dồn theo chuỗi (độ lớn × chuỗi) | **chưa ai làm** |
| Cơ sở A vs B + ba định lý | **chưa ai làm** — không diễn đạt được trong mô hình họ |
| Bảo đảm khả thi (Định lý 1) | **chưa ai làm** |
| Chứng cứ định lượng cho A ≠ B | **CHƯA CÓ** — cần mục 12 |
