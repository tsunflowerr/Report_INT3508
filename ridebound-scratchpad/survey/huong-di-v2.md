# Hướng đi RideBound — sau khi đọc 6 bài người dùng cung cấp + rà lại code

Ngày 2026-09-10. Thay thế phần "ngách" trong `khao-sat-van-lieu.md` ở chỗ nào mâu thuẫn.

---

## 0. Một đính chính bắt buộc

Ở báo cáo trước tôi nói: *"chờ bất ngờ được định giá 20–25 EUR/h, tức ~2–3× VOT"*, và suy ra
điểm hoà vốn 2.68–3.35 EUR. **Bài Alonso-González et al. 2020 — đúng bài cho đúng bối cảnh
ride-pooling — nói ngược lại.**

Họ mô hình hoá riêng cái gọi là **displacement** = chênh lệch giữa thời gian *đã báo* và trung bình
thời gian *thực tế*. Đây chính xác là đại lượng của ta. Kết quả (Bảng 4, 5):

| Đại lượng | Giá trị |
|---|---|
| VOT trên xe | 7.88–10.80 EUR/h |
| VOT chờ | 9.27–16.50 EUR/h |
| **VOR displacement trên xe** | **2.06–4.41 EUR/h** |
| **VOR displacement chờ** | **3.39–6.69 EUR/h** |

Và họ viết thẳng: *"the VOR value associated with this systematic delay ... is **always lower than
the corresponding VOT**. ... Even though this seems counterintuitive and contrary to findings from
previous research (unexpected times are more heavily penalised ...), this suggests that a small
additional unannounced increase in time may not be fully accounted for by individuals."*

Trong khi đó Wardman et al. 2026 (606 nghiên cứu) cho **MeanLate 2.53–3.12 × IVT**, SDL 2.23, RR 0.93;
hướng dẫn chính thức LT 2.5–3.5.

→ Văn liệu **chênh nhau 5–10 lần** về giá của một lời hứa bị phá. Tính lại điểm hoà vốn
(482.2 s = 0.13394 h cho mỗi chuyến hy sinh):

| Nguồn định giá | EUR/h | Hoà vốn / chuyến |
|---|---:|---:|
| Alonso-González, displacement trên xe | 4.41 | **0.59** |
| Alonso-González, displacement chờ | 6.69 | 0.90 |
| Wardman RR 0.93 × VOT 10.80 | 10.04 | 1.34 |
| Wardman MeanLate 2.53 × 10.80 | 27.3 | 3.66 |
| Wardman MeanLate 3.12 × 10.80 | 33.7 | **4.51** |

**Kết luận: lập luận phúc lợi tại điểm β = 30 s KHÔNG vững.** Khoảng 0.59–4.51 EUR quá rộng;
cận dưới thấp hơn thặng dư hợp lý của một chuyến. Không được dùng nó làm luận điểm chính.

Đây là lý do phải đổi khung: **đừng biện hộ cho một điểm vận hành đắt — hãy đi tìm một điểm rẻ.**

---

## 1. Trả lời "chẳng lẽ mọi thứ mình làm người khác đều đã có?"

Không. Bằng chứng nằm trong chính bài Fielbaum–Tirachini–Alonso-Mora mà anh vừa gửi, mục 4.1:

> *"Fielbaum & Alonso-Mora (2020) identify two types of **unreliability** ... Both types of
> unreliability worsen when vehicles are more loaded, i.e., the Flex-route Effect increases
> unreliability. It is worth mentioning that **this is not a minor issue**: for instance,
> Alonso-González et al. (2020) have estimated the value of reliability ... to be approximately a 
> half of the value of time."*

Và ngay trước đó: *"there are other negative externalities that **the model does not directly
capture**"*.

Tức là: chính nhóm Alonso-Mora, trong bài này, (a) đặt tên cho ngoại ứng — Flex-route Effect,
khách cũ bị xấu đi vì khách mới; (b) nói nó **không nhỏ**; (c) trích đúng bài định giá;
và (d) **tuyên bố mô hình của họ không nắm bắt nó.**

RideBound đo đúng ngoại ứng đó, ở mức từng hành khách, từng quyết định, có quy trách nguyên nhân.
Đó không phải "làm lại của người ta" — đó là lấp đúng chỗ họ để trống.

Kovacs et al. 2014 (mục 7) cũng để mở đúng bài toán này cho phía vận trù:
> *"future work could incorporate **stochastic travel times** into the models. The challenge here is
> to design robust a priori routes that **guarantee stable arrival times** at the customer locations
> despite unforeseeable events such as traffic jams."*

Phân rã ba mốc chính là dụng cụ cho câu đó: nó tách "giờ đến xê dịch vì kẹt xe" khỏi
"giờ đến xê dịch vì tôi đổi ý".

---

## 2. Ba bài kia hợp thức hoá PHƯƠNG PHÁP (không tranh chỗ)

### Sridharan, Berry & Udayabhanu 1987, *Management Science* 33(9)
Cấu trúc bài này là khuôn mẫu chính xác cho cái ta nên viết:

- Một **núm ổn định**: tỉ lệ đóng băng F = P/N.
- Một **đường cong giá**: cost error theo F.
- **Kết quả trung tâm**: *"freezing up to 50% of the planning horizon has a **marginal effect** on
  cost"*; cost error đi từ **0.026% ở F=0.5 lên 143.43% ở F=1.0**. Rẻ đến một ngưỡng rồi vọt.
- **So hai PHƯƠNG THỨC đóng băng** (theo kỳ vs theo đơn) và tìm ra một cái trội hơn khi F > 0.5.
- Một **mô hình hồi quy** dự báo cost error từ đặc trưng bài toán.
- Họ tự liệt kê việc còn thiếu: *"the measurement of nervousness and **the establishment of
  trade-offs with freezing costs**"*.

→ Ta đang có **đúng một điểm** (β=30 s → −7.13 pp). Sridharan sẽ gọi đó là "chỉ báo cáo F=1.0".
**Thiếu cả đường cong.**

### Bregni, D'Avino & Schiraldi 2011 (DAAAM)
Hai câu đáng giá:

- *"an issue apparently never discussed in the known literature is that **nervousness is present even
  with stable demand**, in the form of irregular order releases"* → chính là decisionInduced: hệ tự
  gây bất ổn dù thế giới bên ngoài đứng yên. Ta **đo được** con số đó: 89.06%.
- *"All the identified solutions ... are not so effective, actually appearing as **'sandbagging'**
  (i.e., introducing safety stocks, time or capacity), **introducing inflexibility** to the system
  (i.e. fixed planned orders, freezing, etc.)"*

→ Bản đồ sang ride-pooling: "sandbagging" = **đệm ETA** (Bansal: công bố phân vị 25.8–39.1);
"inflexibility" = **khoá/cấm reassignment** (Fielbaum 2020). Cả hai đều đã có người làm và đều bị
chê. Con đường thứ ba: **sửa cách bộ điều phối chọn phương án để bất ổn không phát sinh ngay từ đầu.**

### Kovacs, Golden, Hartl & Parragh 2014, *Networks* 64(3)
- Ba chiều consistency; **arrival time consistency** là chiều gần ta nhất — nhưng **tĩnh, nhiều ngày,
  giao hàng**, không phải lời hứa động cho hành khách. Không tranh chỗ.
- **Giá của consistency đã được đo trong ngành đó**: Groër 6.6–15%; Feillet 1–5.9%;
  Kovacs: siết 60% → chi phí **+186.16%** khi giờ xuất phát cố định.
- **Ba kết quả về hình dạng đánh đổi mà ta nên đi tìm bản sao:**
  1. *"Allowing flexible departure times reduces the impact of tight arrival time consistency
     constraints on cost **significantly** ... arrival time consistency can be improved **without
     increasing working time**."* → chỗ đặt slack quyết định giá của cam kết.
  2. Spliet: ép driver consistency cho **75%** khách thay vì 100% → chi phí từ **12.7% xuống 2.9%**.
     Kovacs: cho phép 2 tài xế thay vì 1 → giảm 6.5%; cho phép hơn 2 → **không thêm gì**.
     → **Cam kết một phần rẻ hơn cam kết toàn phần rất nhiều, và lợi ích bão hoà nhanh.**
  3. Smilowitz: *"solution approaches devised for improving consistency perform better with regard
     to cost than cost-driven approaches with regard to consistency"* → bất đối xứng.
- **Và họ cảnh báo đúng cái ta gặp**: *"Using hard constraints ... may lead to **infeasible or
  unreasonable solutions** when demand fluctuations cannot be anticipated."* Kovacs et al. chuyển
  sang **phạt mềm trong hàm mục tiêu** vì *"it is difficult to predict reasonable bounds if demand is
  fluctuating: loose constraints decrease service quality while excessively tight constraints lead to
  a **disproportional** increase in travel cost."*

→ Cả MRP (Kropp/Carlson/Jucker 1983 "Less Nervous MRP Systems") lẫn ConVRP đều **độc lập đi tới cùng
một kết luận: phạt kinh tế mềm tốt hơn ràng buộc cứng.** RideBound đang dùng ràng buộc cứng.

---

## 3. Rà lại code: cái gì đã có mà CHƯA DÙNG

| Cơ chế | Trạng thái code | Config có sẵn | Đã chạy trên panel niêm phong? |
|---|---|---|---|
| Ngân sách cứng β (drop ETA) | ✔ `CommitmentBudgetEvaluator` | `budget60`, `budget120`, `nobudget` | **Chỉ β=30 s** |
| Cơ sở tính (conduct/outcome) | ✔ `CommitmentBudgetBasis` | `commit-visible-*` (scratchpad) | conduct đủ; outcome mới thăm dò |
| **Time fence** `freezeHorizon` + `freezeHorizonLocks` | ✔ `CommitmentLockEvaluator:54` | `f1-freeze300`, `f1-freeze600` | **Chưa bao giờ** |
| **Bảo đảm một chiều** `ratchetLocks` | ✔ `CommitmentPolicy:229` | `f2-ratchet`, `f1f2-freeze300-ratchet` | **Chưa bao giờ** |
| **Phạt mềm** `SoftHardHybrid` + `warningLimit` | ✔ `SolverBackedFleetSelection:313` | `wp9-fleetpy-soft-hard-hybrid-audited-v1` | **Chưa bao giờ** (panel dùng `HardVector`) |
| Mục tiêu từ điển `revision` | ✔ `AddRevisionObjectives` | mặc định | có, nhưng **99.85% degenerate** |

**Giới hạn đã xác nhận:** `CommitmentPolicy` bắt buộc *mỗi dimension đúng một limit*
(`CommitmentPolicy.cs:155-164`, `_limits` là `FrozenDictionary` khoá theo dimension).
Nên **không thể** đặt hạn mức khác nhau theo phase. Ý tưởng "time fence bằng cách cho hardLimit khác
nhau ở accepted/waitingPickup/onboard" là **không khả thi** nếu không sửa lõi.
Nhưng không cần: `freezeHorizon` đã là time fence thật.

Ngân sách là **bộ đếm tích luỹ** theo (request, dimension); `applicablePhases` chỉ bật/tắt việc
kiểm tra, không reset. Đây là ngữ nghĩa đúng cho một hàng rào thời gian.

---

## 4. Con số quyết định — đã nằm sẵn trong chứng cứ niêm phong

`docs/benchmarking/evidence/wp14-001-mechanism-probe-v1-summary.json`, nhánh **B1 (không ràng buộc)**,
`cumulativeDropEtaConsumption`:

```
requests            : 1735
zeroConsumption     : 1332   (76.8%)
percentiles (ms)    : p50=0  p75=0  p90=154,821  p95=234,222  p99=420,455  p100=573,491
requestsAboveThreshold:  >0s: 403 | >30s: 369 | >60s: 341 | >120s: 230 | >300s: 48
```

Đọc bảng này: **nếu áp ngân sách β, số hành khách mà nhánh không ràng buộc đã vi phạm là**

| β | Số khách bị ràng buộc | % đội hình |
|---:|---:|---:|
| 30 s | 369 | 21.3% |
| 60 s | 341 | 19.7% |
| 120 s | 230 | 13.3% |
| 300 s | **48** | **2.8%** |

**Ba phần tư hành khách tiêu thụ ĐÚNG BẰNG KHÔNG.** Ràng buộc chỉ chạm vào một cái đuôi mỏng, và
cái đuôi đó teo đi 87% khi nới β từ 30 s lên 300 s.

→ **Giả thuyết trung tâm**: giá của cam kết sụp rất nhanh theo β. Ở β = 300 s ta vẫn cho mỗi hành
khách một lời hứa **có trần 5 phút, cưỡng chế được**, mà cái giá có thể chỉ còn một phần nhỏ của
7.13 pp. Đó chính là hình dạng Sridharan tìm ra ("rẻ tới ngưỡng rồi vọt"), và nếu đúng thì
**không cần lập luận phúc lợi mong manh nữa** — điểm vận hành tự nó hấp dẫn ở mọi mức định giá.

**Cảnh báo phải tôn trọng**: file chứng cứ tự ghi `claimBoundary`:
`notACounterfactualCompletionEstimate`, `mustNotSelectAnyFutureConfiguration`.
Phân bố này **chỉ dùng để đặt giả thuyết, không thay thế phép đo**. Ràng buộc 369 khách sẽ làm dây
chuyền đổi cả loạt quyết định khác. **Bắt buộc phải chạy thật.**

## 4b. Cơ chế nào đang gây mất khách (nhánh C1)

```
commitmentPrunedByCode : COMMITMENT_BUDGET_EXCEEDED 780 | COMMITMENT_PHASE_LOCK 160
immediateAcceptanceBlocks: 143   (drop_eta 118, cả hai 18, pickup_eta 7)
vehicleChoiceSetsEmptiedByGate: 534   (B1: 0)
degenerateFraction: 0.974
objectiveFamilies: worst-hard-utilization-ppm  built 13,004 / degenerate 13,004  → 100% VÔ DỤNG
                   revision                    built 130,040 / degenerate 129,851 → 99.85% vô dụng
```

Ba điều rút ra:
1. **Ngân sách ETA là cơ chế ràng buộc chi phối** (780 vs 160), không phải các khoá switch.
2. **534 tập lựa chọn xe bị làm rỗng** — đó là cơ chế vật lý của việc mất khách.
3. **Các tầng mục tiêu nhận biết cam kết gần như trơ.** Ràng buộc cứng làm hết việc; hàm mục tiêu
   không phân biệt được gì. Đây là bằng chứng nội bộ cho đúng điều Kovacs et al. phê phán.

---

## 5. Hướng đi đề xuất — ba chân, tăng dần tham vọng

### Chân A — QUY TRÁCH (đã xong, chỉ cần viết)
Phân rã ba mốc = phép quy trách nhân quả đầu tiên cho bất ổn lời hứa trong ride-pooling.
- 89.06% lượng ETA khách thấy xê dịch là **do bộ điều phối**, không phải kẹt xe.
- **Tập trung**: 426/1735 khách (24.6%) gánh toàn bộ; 76.8% tiêu thụ bằng 0 → ~175 s/khách bị ảnh hưởng.
- **Nhóm chứng tự nhiên**: trôi dạt ngoại sinh gần như y hệt hai nhánh (6,709,435 vs 6,688,485 ms).
- Trả lời trực tiếp ngoại ứng mà Fielbaum–Tirachini–Alonso-Mora tuyên bố không mô hình hoá.
- Đã tái lập độc lập: script của tôi ra 74,443,002 ms và 128,020 ms, **khớp tuyệt đối** file niêm phong.

### Chân B — ĐƯỜNG BIÊN (rẻ, config có sẵn, BẮT BUỘC LÀM)
Quét và vẽ đường đánh đổi, thay vì một điểm.
- β ∈ {0(nobudget), 30, 60, 120, 300} trên cơ sở conduct.
- Cơ chế ∈ {ngân sách, time fence 300/600, ratchet, fence+ratchet}.
- Cơ sở ∈ {conduct, outcome} — kết quả trội đã có dấu hiệu (outcome vô nghiệm 4/20 ô).
- **Sản phẩm**: hình trung tâm của khoá luận — tỉ lệ phục vụ theo độ chặt cam kết, có đầu gối.
- **Đối chiếu văn liệu**: Sridharan (0.026% → 143%), Kovacs (+186% khi siết 60%),
  Spliet (12.7% → 2.9% khi phủ 75%). Nếu RideBound cũng lồi mạnh, đó là bản sao ride-pooling của
  một quy luật đã biết ở hai ngành khác — vừa mới vừa có nền.

### Chân C — CAM KẾT ĐỊNH GIÁ MỀM (đóng góp thuật toán; tuỳ chọn nhưng khả thi)
Thay/bổ sung cổng cứng bằng **phạt kinh tế lên decisionDelta trong hàm mục tiêu**.
- **Tiền lệ hai ngành**: Kropp/Carlson/Jucker 1983 (MRP, đưa chi phí đổi MPS vào lot-sizing);
  Kovacs et al. 2013 (GenConVRP, phạt biến thiên giờ đến trong hàm mục tiêu).
- **Chưa ai làm trong ride-pooling.**
- **Bằng chứng cần làm**: 100% degenerate ở `worst-hard-utilization-ppm`, 99.85% ở `revision`,
  534 tập rỗng, 143 chặn tức thì, outcome-basis vô nghiệm.
- **Chi phí thực hiện thấp**: `SoftHardHybrid` + `warningLimit` **đã được cài đặt**;
  `wp9-fleetpy-soft-hard-hybrid-audited-v1.json` đã tồn tại. Chỉ cần đổi profile + chạy.
- **Giá dùng để phạt** lấy từ chính khoảng văn liệu ở mục 0 — và vì khoảng đó rộng,
  ta chạy **độ nhạy** trên cả khoảng thay vì chọn một con số. Sự bất định của văn liệu
  trở thành một biến thí nghiệm, không còn là điểm yếu.

---

## 6. Vì sao ba chân này đứng được trước từng bài

| Bài | Có gì | RideBound thêm gì |
|---|---|---|
| Fielbaum–Tirachini–Alonso-Mora | Đặt tên Flex-route Effect, nói "không nhỏ", **không mô hình hoá** | Đo, quy trách, định giá nó |
| Alonso-Mora 2017 | RTV + ILP | Không có lời hứa; ta thêm ràng buộc theo lời đã nói |
| Alonso-González 2020 | Định giá displacement phía **cầu** | Không có bộ điều phối; ta cho phía **cung** |
| Wardman 2026 | 2872 hệ số, MeanLate 2.5–3.1× | Thuần định giá; ta cung cấp lượng để nhân |
| Sridharan 1987 | Đường cong đóng băng, hai phương thức, hồi quy | Sản xuất, không phải hành khách; ta chuyển khung |
| Kovacs 2014 | Arrival time consistency, giá của nó, cảnh báo hard-constraint | Tĩnh, nhiều ngày, giao hàng; **không quy trách nguyên nhân** |
| Bregni 2011 | Nêu "nervousness kể cả khi cầu ổn định" | Không đo; ta đo được 89.06% |

---

## 7. Thứ tự thực hiện

1. **Chân B, đợt 1** — chạy `nobudget`, `budget60`, `budget120` trên panel A (20 ô × 3 = 60 lần chạy).
   Cho ngay ba điểm mới trên đường cong + tách phần khoá switch khỏi phần ngân sách.
2. **Thêm β = 300 s** (tạo config mới theo mẫu `budget120`) — điểm được dự báo là rẻ nhất.
3. **Chân B, đợt 2** — `f1-freeze300`, `f1-freeze600`, `f2-ratchet`, `f1f2-freeze300-ratchet`.
4. **Chân C** — đổi `wp4-config` sang `wp9-fleetpy-soft-hard-hybrid-audited-v1.json`, chạy lại
   điểm β tốt nhất; so cứng vs mềm trên cùng đường biên.
5. **Chân A** — viết phần quy trách với số đã có; không cần chạy thêm.
6. Độ nhạy định giá trên toàn khoảng 4.41–33.7 EUR/h; báo cáo kết luận nào sống sót cả khoảng.

**Không sửa lõi ở bước 1–3.** Bước 4 chỉ đổi config. Chỉ khi muốn hàng rào thời gian mịn hơn
(hạn mức thay đổi liên tục theo thời gian-đến-đón) mới phải sửa `CommitmentPolicy`.
