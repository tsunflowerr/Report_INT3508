# Khảo sát văn liệu cho RideBound — ưu/nhược điểm của dòng bài Alonso-Mora và chỗ đứng của ta

Ngày: 2026-09-10. Kho nguồn: 1064 URL duy nhất (đợt salvage) + 14 trục tra cứu mới trong phiên này.
Tài liệu này KHÔNG ghi vào repo; chỉ nằm ở scratchpad.

---

## 0. Cách đọc tài liệu này

Câu hỏi của người dùng: *có thể "hơn" dòng bài Alonso-Mora ở một chiều nào đó không, kể cả khi
thua một chút về con số chính?* Muốn trả lời thì phải biết dòng bài đó **yếu ở đâu một cách có hệ thống**,
chứ không phải yếu ngẫu nhiên. Phần 2 làm việc đó.

---

## 1. Bản đồ 14 trục đã khảo sát

| # | Trục | Trạng thái | Kết luận ngắn |
|---|------|-----------|----------------|
| 1 | Ghép chuyến dung lượng lớn (RTV, ILP) | đã kỹ | Alonso-Mora 2017 là chuẩn; ta trùng cấu trúc ILP |
| 2 | Reassignment / unreliability phía nhà xe | đã kỹ | Fielbaum & Alonso-Mora 2020 — hàng xóm gần nhất |
| 3 | Giá trị độ tin cậy (VOR/VOT) | đã kỹ | **Có mỏ vàng**: thời gian bất ngờ ~ 2–3x VOT |
| 4 | Sở thích công bố ETA (Bansal) | đã kỹ | **Giả định phía cung là miễn phí** |
| 5 | Đệm ETA trong công nghiệp | đã kỹ | Phổ biến trong thực tế, mỏng trong học thuật |
| 6 | Cảm nhận chờ đợi (Geržinič) | đã kỹ | Chờ bất ngờ ~ 20–25 EUR/h |
| 7 | Đánh giá phúc lợi ride-pooling | đã kỹ | **Hàm phúc lợi không có số hạng nào cho thời gian bất ngờ** |
| 8 | Công bằng trong ride-pooling | đã kỹ | Sôi động nhưng theo trục thu nhập/nhân khẩu, không theo trục lời hứa |
| 9 | Consistency trong VRP (ConVRP) | đã kỹ | **Có "arrival time consistency" — nhưng cho giao hàng tĩnh nhiều ngày** |
| 10 | Nervousness / ổn định lịch (MRP, OM) | đã kỹ | **Khung khái niệm khớp 1:1, chưa ai bê sang ride-pooling** |
| 11 | Quy trách trễ (đường sắt, hàng không) | đã kỹ | Tiền lệ pháp lý cho việc quy trách nguyên nhân |
| 12 | Price-of-X trong giao thông | đã kỹ | Thể loại hợp lệ; chưa có "price of commitment" |
| 13 | DARP bền vững / ngẫu nhiên | đã kỹ | Bảo vệ cửa sổ thời gian, không bảo vệ lời đã nói |
| 14 | Khả năng tái lập trong AMoD | đã kỹ | **arXiv:2506.07345 kêu gọi đúng thứ ta đã có** |

---

## 2. Ưu và nhược điểm CÓ HỆ THỐNG của dòng bài này

### 2.1 Ưu điểm (vì sao nó thống trị)

- **U1. Quy mô thật.** Manhattan, hàng trăm nghìn chuyến/ngày, đội xe hàng nghìn. Kết quả có sức nặng.
- **U2. Cấu trúc tối ưu sạch.** Đồ thị RTV + ILP tách rời việc *sinh* khả năng khỏi việc *chọn*.
  Đây là đóng góp thuật toán thật và nó bền.
- **U3. Một con số tiêu đề dễ nhớ.** "98% nhu cầu Manhattan với 3000 xe 4 chỗ."
- **U4. Có mã nguồn và mô phỏng mở** (FleetPy, AMoD-sim), nên dễ nối tiếp.

### 2.2 Nhược điểm có hệ thống (đây là nơi có ngách)

**W1 — Hành khách được mô hình hoá như một RÀNG BUỘC, không phải một ĐỐI TÁC.**
Toàn bộ dòng bài đặt hai tham số: Omega (chờ tối đa) và Delta (trễ tối đa). Miễn là còn trong cửa sổ đó,
kế hoạch được phép nhảy tuỳ ý, bao nhiêu lần cũng được. **Không có khái niệm "điều đã nói với khách".**
Một hành khách bị đổi ETA 12 lần và một hành khách được báo đúng một lần là *giống hệt nhau*
trong mọi hàm mục tiêu của dòng bài này.

**W2 — Không có quy trách nguyên nhân.**
Khi ETA của khách xấu đi, không ai tách phần *do nhà xe quyết định lại* khỏi phần *do xe chạy chậm/kẹt xe*.
Fielbaum & Alonso-Mora (2020) là ngoại lệ duy nhất — họ tách được phần "controlled by the system provider" —
nhưng họ **đo** nó chứ không **ràng buộc** nó, và không tách tiếp phần trôi dạt vật lý của xe.

**W3 — Chỉ đánh giá theo KẾT QUẢ, không đánh giá theo HÀNH VI.**
Chỉ số chuẩn: tỉ lệ phục vụ, thời gian chờ, VKT, tỉ lệ ghép. Không có chỉ số nào nói
"hệ thống này cư xử có giữ lời hay không". Trong ngôn ngữ của ta: có outcome metric, không có conduct metric.

**W4 — Phía cầu chứng minh độ tin cậy có giá trị; phía cung giả định nó miễn phí.**
Đây là khe nứt lớn nhất và nó nằm giữa hai dòng văn liệu không nói chuyện với nhau:

- Meta-analysis 2872 hệ số / 606 nghiên cứu / 52 nước / 1963–2023 (TR-A) — độ tin cậy có giá rõ ràng.
- Alonso-González et al. 2020 (TR-C 115:102621): VOR/VOT ~ 0.5; VOT trên xe 7.88–10.80 EUR/h.
- Geržinič, Cats & van Oort 2023: **chờ bất ngờ được định giá 20–25 EUR/h**, tức ~ 2–3x VOT thường.
- Bansal, Liu, Daziano & Samaranayake (arXiv:1904.07987): công bố ETA trung thực làm
  tỉ lệ chấp nhận chuyến tăng 9.9–11.7%. Nhưng chính họ viết: **"No supply-side costs are modeled...
  The framework assumes the dispatcher can always deliver passengers to the displayed percentile."**

→ Cả một nhánh văn liệu nói "giữ lời rất đáng tiền" mà **chưa ai trả lời "giữ lời tốn bao nhiêu"**.

**W5 — Khả năng tái lập kém, và điều này đã được thừa nhận chính thức.**
arXiv:2506.07345, "Reproducibility in the Control of Autonomous Mobility-on-Demand Systems"
(Li, Alharbi, Gammelli, Harrison, Rodrigues, Schiffer, Pavone, Frazzoli, Zhao, Zardini —
MIT/Stanford/DeepMind/DTU/TUM/ETH, IEEE 2025). Họ chỉ đích danh:
phân hoạch mạng "often underreported or completely omitted"; chi tiết mô phỏng "poorly documented
or not made publicly available"; tiền xử lý dữ liệu "another critical but often underreported step";
chọn cỡ đội xe thiếu minh bạch. Họ đề xuất một "reproducibility checklist".

**W6 — Các khái niệm ổn định đã tồn tại ở ngành khác nhưng CHƯA AI bê sang ride-pooling.**

- *Vận trù giao hàng*: Consistent VRP (Groër, Golden, Wasil 2009) có **arrival time consistency** —
  ràng buộc chênh lệch giờ đến giữa các ngày. Khảo sát: Kovacs, Golden, Hartl, Parragh,
  *Networks* 64(3), 2014. Nhưng đây là bài toán **tĩnh, nhiều ngày, giao hàng** — không phải
  lời hứa động trong ngày cho hành khách.
- *Sản xuất*: "MRP system nervousness" (Blackburn, Kropp, Millen, IJPE 1985/86 — "Causes and cures";
  Sridharan, Berry, Udayabhanu, *Management Science* 33(9):1137, 1987 — đo ổn định MPS dưới rolling horizon;
  Zhao 1993/2001; Xie 2003). Dòng này **đã phân biệt sẵn** nervousness do
  cập nhật nhu cầu (ngoại sinh) với nervousness do chính quy tắc lập kế hoạch (nội sinh), và
  "cure" kinh điển của họ là **đóng băng master production schedule** — chính là `PromiseLock`.
- *Đường sắt / hàng không*: quy trách trễ sơ cấp vs trễ phản ứng (reactionary delay) là một
  chế định pháp lý — UK ORR Delay Attribution Guide; Eurocontrol lexicon. Tức là **việc quy trách
  nguyên nhân của một lời hứa bị phá đã là chuẩn mực hợp đồng ở các ngành vận tải khác.**

→ Kiểm chứng: tra thẳng "nervousness/instability + ride-pooling" chỉ trả về văn liệu
wait-time/detour thông thường. **Cầu nối này chưa được bắc.**

---

## 3. Hàng xóm gần nhất — ranh giới chính xác

| Bài | Họ làm gì | Họ KHÔNG làm gì |
|-----|-----------|------------------|
| Alonso-Mora et al. 2017 (PNAS) | RTV + ILP, quy mô lớn | Không có lời hứa; cửa sổ Omega/Delta là tất cả |
| **Fielbaum & Alonso-Mora 2020** (TR-C 121:102831) | **Đo** bất định do nhà xe gây ra; thử hạn chế reassignment | Không **ràng buộc theo ngân sách từng khách**; không tách trôi dạt vật lý; không so hai CƠ SỞ tính |
| **Sivagnanam, Mukhopadhyay, Samaranayake, Dubey, Laszka 2026** (ICCPS, arXiv:2603.07422) | Xác nhận sớm + tối ưu liên tục, **đảm bảo phục vụ** mọi yêu cầu đã nhận | Đảm bảo **được phục vụ**, KHÔNG đảm bảo **giờ đã báo**; tối ưu liên tục được tự do dời ETA; không quy trách |
| Groër/Golden/Wasil 2009; Kovacs et al. 2014 | Arrival time consistency | Tĩnh, nhiều ngày, giao hàng — không phải hành khách, không động |
| Bansal et al. (arXiv:1904.07987) | Định giá ETA trung thực phía cầu | **Không mô hình hoá chi phí phía cung** (họ tự nói) |
| arXiv:2609.04618 | Định giá **cam kết GIÁ TIỀN** như hợp đồng quyền chọn | Cam kết tiền, không phải cam kết THỜI GIAN |
| Schulz (CD-DARP) | Menu/tiered promise | Không có ngân sách sửa đổi theo hành vi |

---

## 4. Kết luận khảo sát: ba chân của ngách

1. **Kết quả cấu trúc (đóng góp lý thuyết).** Conduct basis (`decisionInduced`) *luôn* khả thi vì
   phương án không-làm-gì có `proposed = exogenous` nên bị tính 0. Outcome basis (`customerVisible`)
   *có thể* vô nghiệm ở mọi mức ngân sách vì trôi dạt ngoại sinh một mình đã ăn hết ngân sách.
   Đã chứng minh bằng lập luận + đo được: beta=30s vô nghiệm ở 4/20 ô; nâng lên beta=120s vẫn vô nghiệm
   ở 4/20 ô nhưng là **một tập ô KHÁC** — tăng ngân sách không chữa được, chỉ dời chỗ đau.
   **Không bài nào trong 1064 nguồn có kết quả này.**

2. **Phân rã cái giá của cam kết (đóng góp đo lường, đã hiệu chuẩn ngoài).**
   Khoá danh tính xe <= 0.69 pp. Khoá ETA 7.13 pp. Gấp ~10 lần. Tức là:
   *phần đắt của một lời hứa không phải là "cùng một chiếc xe", mà là "đúng giờ đã báo".*
   Đã hiệu chuẩn với FleetPy AlonsoMora + InsertionHeuristic trên cùng mạng/nhu cầu/đội xe.

3. **Chứng cứ niêm phong (đóng góp phương pháp).** Trả lời trực tiếp arXiv:2506.07345.

---

## 5. Thí nghiệm còn thiếu — và nó rẻ

Khe nứt W4 nói: phía cầu định giá độ tin cậy, phía cung chưa định giá chi phí. **Ta có cả hai vế.**

Dữ liệu đã niêm phong chứa, trong `transcript-00.ndjson` của từng ô, mọi bản ghi `promisePublished` với:
`requestId`, `promise.pickupEtaMs`, `promise.dropEtaMs`, `decisionDelta`, `exogenousDelta`,
`visibleDelta` (đủ 10 chiều), `promiseVersion`, `reasonCode`.

Vậy tính được, cho từng nhánh B1 và C1:

- tổng thời gian ETA bị dịch chuyển mà khách nhìn thấy, theo từng hành khách;
- phần do quyết định của nhà xe, tách khỏi phần do trôi dạt vật lý.

Rồi quy ra tiền bằng hệ số đã công bố (chờ bất ngờ 20–25 EUR/h so với VOT trên xe 7.88–10.80 EUR/h),
và đặt lên bàn cân với số chuyến bị mất (7.13 pp).

→ Cho ra **điểm hoà vốn**: mức giá trị độ tin cậy mà tại đó hệ thống có cam kết
thắng hệ thống không cam kết **về phúc lợi**, dù thua về tỉ lệ phục vụ.
Đây đúng là "thua một chút nhưng đánh đổi tốt hơn" — và nó là một con số, không phải một lời tuyên bố.

Không cần chạy mô phỏng mới. Chỉ đọc lại transcript đã niêm phong.

---

## 6. Bài cần tải (bị chặn, không truy cập được)

| Bài | Vì sao cần | Nguồn |
|-----|-----------|-------|
| Fielbaum & Alonso-Mora 2020, TR-C 121:102831, "Unreliability in ridesharing systems" | Hàng xóm gần nhất — cần định nghĩa chính xác các chỉ số bất định của họ | ScienceDirect S0968090X2030735X (403) |
| Alonso-González et al. 2020, TR-C 115:102621 | Tham số VOR/VOT gốc cho ride-pooling | ScienceDirect (paywall) |
| Meta-analysis VOT multipliers, TR-A 2026 (2872 hệ số / 606 nghiên cứu) | Hệ số quy đổi có thẩm quyền nhất | ScienceDirect S0965856426000662 |
| Geržinič, Cats & van Oort 2023, TR Interdisciplinary | Con số 20–25 EUR/h cho chờ bất ngờ | Bản arXiv 2301.04982 đọc được; bản tạp chí thì không |
| Kovacs, Golden, Hartl, Parragh 2014, *Networks* 64(3) | Khảo sát chuẩn về consistency trong VRP | Wiley (paywall) |
| Sridharan, Berry, Udayabhanu 1987, *Management Science* 33(9):1137 | Định nghĩa gốc của thước đo ổn định MPS | INFORMS (paywall) |
| Blackburn, Kropp, Millen 1985/86, IJPE, "MRP system nervousness: Causes and cures" | Nguồn gốc phân biệt nội sinh/ngoại sinh | ScienceDirect 0167188X85900217 |
