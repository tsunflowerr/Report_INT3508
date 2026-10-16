# Kết quả chân A, C, D — RideBound

Ngày 2026-09-11. Chân B (đường biên) đang chạy, báo cáo riêng khi xong.
Không ghi gì vào repository.

---

# CHÂN C — Kết quả cấu trúc (lý thuyết + xác nhận thực nghiệm)

## C.0 Bất biến nền, đã xác minh trong code

Tập phương án của mỗi xe **luôn chứa phương án không-làm-gì** (no-op): giữ nguyên kế hoạch
hiện tại. Ba chỗ trong code khẳng định độc lập:

| Vị trí | Nội dung |
|---|---|
| `CandidateFleetSelector.cs:23` | *"Every vehicle requires at least one feasible plan, including no-op."* |
| `CandidatePortfolioRetainer.cs:56` | *"A per-vehicle portfolio requires one no-op candidate."* |
| `HardVectorCandidateAssessor.cs:204` | tách hai chế độ hỏng: *"even the safety no-op was absent"* vs *"rejected every generated candidate"* |

Điều này cũng bắt buộc về mặt mô hình: ILP có ràng buộc `Σ(options của xe v) == 1`, nên mỗi xe
phải chọn đúng một phương án. Không có no-op thì ILP vô nghiệm ngay khi một xe không nhận thêm
được ai.

## C.1 Ký hiệu

Tại một epoch quyết định, với hành khách r đang mở lời hứa trên xe v:

- **previous** = lời hứa đã công bố lần cuối cho r
- **exogenous** = chính kế hoạch đó, **chiếu lại từ vị trí thật hiện tại của xe**
  (cùng lộ trình, cùng phân công, chỉ khác điểm xuất phát)
- **proposed** = lời hứa mà phương án đang xét sẽ tạo ra

Hai cơ sở tính ngân sách:

- **conduct** (`decisionInduced`) = |proposed − exogenous| — phần nhà xe tự gây ra
- **outcome** (`customerVisible`) = |proposed − previous| — toàn bộ những gì khách thấy dịch chuyển

Ngân sách là **bộ đếm tích luỹ** theo (hành khách, chiều), đơn điệu tăng, so với trần β.

## C.2 Mệnh đề ①: cơ sở conduct LUÔN thoả được

Với phương án no-op n: kế hoạch không đổi, nên phép chiếu của n từ vị trí hiện tại **chính là**
phép chiếu exogenous. Tức là

    proposed(n) = exogenous

Do đó

    decisionDelta(n) = |proposed(n) − exogenous| = 0

Bộ đếm sau = bộ đếm trước + 0 = bộ đếm trước. Mà bộ đếm trước ≤ β (vì mọi lần công bố trước đó
đều đã qua kiểm tra). Vậy no-op **không bao giờ** vượt trần.

**⇒ Dưới cơ sở conduct, tập phương án của một xe không bao giờ bị làm rỗng. ∎**

Điểm cốt lõi: conduct khả thi **không phải vì nó dễ dãi**, mà vì nó được đo so với một mốc mà
nhà xe kiểm soát được. "Không làm gì" theo định nghĩa là "không gây ra gì".

## C.3 Mệnh đề ②: cơ sở outcome CÓ THỂ vô nghiệm

Với cùng phương án no-op:

    visibleDelta(n) = |proposed(n) − previous| = |exogenous − previous| = d_r

trong đó d_r là **trôi dạt ngoại sinh** tích luỹ kể từ lần công bố trước — do kẹt xe và tiến
trình của xe, **không phải do nhà xe**.

Nếu Σ d_r > β thì ngay cả no-op cũng bị loại. Nếu mọi phương án khác cũng bị loại thì tập rỗng
→ `VehicleHasNoFeasibleCandidate` → lần chạy hỏng.

**Xác nhận thực nghiệm**: nhánh outcome ở β = 30 s **vô nghiệm trên 4/20 ô**, với đúng thông báo
lỗi *"C1 rejected every generated candidate for this vehicle"*.

## C.4 Mệnh đề ③: nới β KHÔNG chữa được, chỉ dời chỗ đau

Σ d_r là tổng các trị tuyệt đối, **đơn điệu tăng theo thời gian sống của chuyến đi**. Với bất kỳ
β hữu hạn nào, luôn tồn tại chuyến đủ dài hoặc mạng đủ biến động để Σ d_r > β. Không có β hữu hạn
nào bảo đảm khả thi.

**Xác nhận thực nghiệm**: nâng lên β = 120 s **vẫn vô nghiệm 4/20 ô**, nhưng là **một tập ô khác**:

| β | Tập ô vô nghiệm |
|---|---|
| 30 s | 16-r2, **16-r4**, 17-r1, 17-r3 |
| 120 s | 14-r4, 15-r2, **16-r4**, 17-r4 |

Chỉ giao nhau ở đúng một ô. Đó là sự **dời chỗ**, không phải sự chữa lành.

Ở 16 ô chung: conduct@30s = 1246 khách, outcome@120s = 1266 khách.

## C.5 Vì sao đây là kết quả đáng kể

Đây là một mệnh đề **chứng minh được rồi xác nhận bằng đo đạc** — không phải chỉ là con số.
Và nó nói một điều thực dụng:

> Nếu muốn hứa với khách một cách **cưỡng chế được**, phải hứa về **hành vi của mình**
> ("tôi sẽ không tự dời giờ của bạn quá β"), chứ không thể hứa về **kết quả**
> ("giờ của bạn sẽ không đổi quá β"). Lời hứa thứ hai nghe hay hơn nhưng không giữ được,
> vì một phần của nó nằm ngoài tầm kiểm soát của người hứa.

Không bài nào trong 6 bài đã đọc, và không nguồn nào trong 1064 nguồn đã khảo sát, phân biệt hai
cơ sở này.

## C.6 Sự phân biệt này ĐÃ CÓ TÊN — trong luật hợp đồng

Tra thêm ngày 2026-09-11: cái mà ta gọi là conduct/outcome chính là một phân biệt kinh điển của
luật nghĩa vụ, có từ lâu đời:

| Thuật ngữ pháp lý | Tương ứng trong RideBound |
|---|---|
| **Obligation de moyens** (nghĩa vụ phương tiện / obligation of means) | cơ sở **conduct** — `decisionInduced` |
| **Obligation de résultat** (nghĩa vụ kết quả / obligation of result) | cơ sở **outcome** — `customerVisible` |

Định nghĩa chuẩn: *"In obligations of means, the debtor does not breach if they act carefully
despite not achieving the result, whereas in obligations of result, the debtor is liable for
failing to achieve the result."*

Ví dụ kinh điển: **luật sư** chịu nghĩa vụ phương tiện — cố hết sức nhưng không bảo đảm thắng
kiện. **Thợ lắp thang máy** chịu nghĩa vụ kết quả — thang chạy hoặc không.

Và trong hợp đồng dịch vụ CNTT (SLA), đúng vấn đề của mệnh đề ② được xử lý bằng điều khoản
loại trừ: *"neither party will be liable for SLA failures resulting from events **beyond its
reasonable control**, provided reasonable efforts are made to minimize service disruption."*

### Vì sao điều này làm chân C mạnh hơn nhiều

1. **Kết quả của ta có tên và có nền.** Mệnh đề ② không còn là một quan sát kỹ thuật lẻ loi:
   nó là phiên bản thuật toán của một nguyên lý mà luật đã kết luận từ lâu — **không thể áp đặt
   nghĩa vụ kết quả khi một phần kết quả nằm ngoài tầm kiểm soát của người có nghĩa vụ**, nếu
   không hợp đồng trở nên bất khả thi. Ta chứng minh và đo được đúng điều đó trong điều phối xe.

2. **Và đây mới là chỗ mới thật sự**: luật/SLA xử lý ranh giới "beyond reasonable control" bằng
   **văn xuôi** — điều khoản bất khả kháng, tranh cãi sau sự việc. RideBound **tính được ranh giới
   đó**, theo từng quyết định và từng hành khách, bằng mốc exogenous.

   > Nói cách khác: mốc exogenous là một phép **xác định bất khả kháng tự động**, thay cho
   > điều khoản bất khả kháng viết bằng lời.

3. **Nó cho khoá luận một phát biểu vấn đề dễ hiểu, không cần thuật ngữ:**
   *"Làm thế nào để một hãng gọi xe chung đưa ra được lời hứa về giờ giấc mà hãng thực sự
   giữ được — và cái đó đắt bao nhiêu?"*

Điều này cũng giải thích vì sao mệnh đề ① đúng một cách hiển nhiên khi nhìn lại: nghĩa vụ phương
tiện luôn có thể hoàn thành bằng cách "cư xử đúng mực", và phương án no-op chính là hành vi đúng
mực tối thiểu — không làm gì thì không gây ra gì.

---

# CHÂN A — Quy trách

## A.1 Con số chính

Tỉ lệ lượng ETA mà hành khách nhìn thấy dịch chuyển, **do chính bộ điều phối gây ra**:

- **B1 (không cam kết): 89.06%** — 74,443 s trên tổng 83,587 s
- **C1 (cam kết 30 s): 1.37%** — 128 s trên tổng 9,332 s

Chỉ ~11% là do thế giới vật lý.

## A.2 Nhóm chứng tự nhiên

Trôi dạt ngoại sinh giữa hai nhánh: 9,202.6 s vs 9,204.5 s.

Con số 0.02% này **không nên dùng làm phát biểu chính** — xem B.4: với nhánh thứ ba nó lệch tới
5.4%, nên độ khớp sát của riêng cặp B1/C1 là may mắn. Phát biểu đúng, vẫn rất mạnh:

> Qua các chính sách rất khác nhau, trôi dạt vật lý dao động **vài phần trăm**, còn xáo trộn do
> nhà xe gây ra thay đổi **580 lần**. Hai đại lượng phản ứng hoàn toàn khác nhau với chính sách —
> đó chính là điều phép phân rã ba mốc cần chứng minh.

## A.3 Thiệt hại tập trung, không dàn đều

| | B1 | C1 |
|---|---:|---:|
| Hành khách được phục vụ | 1,735 | 1,581 |
| Khách từng bị dời do nhà xe | **403 (23.2%)** | **11 (0.7%)** |
| Số lần dời | 479 | 11 |
| **Trung bình mỗi lần dời** | **155 s** | 11.6 s |
| Trung bình mỗi khách bị ảnh hưởng | 185 s | 11.6 s |
| **Khách tệ nhất** | **840.9 s ≈ 14 phút** | 27.6 s |
| Phân vị 99 | 536.4 s | 0.0 s |
| Phân vị 95 | 264.6 s | **0.0 s** |

Ba điều đọc ra:

1. **Ba phần tư hành khách không hề bị ảnh hưởng.** Vấn đề nằm ở một cái đuôi mỏng.
2. **Mỗi lần bộ điều phối đổi ý, nó dời giờ đã báo trung bình 155 giây.** Không phải nhích vài
   giây — mỗi lần là hơn hai phút rưỡi.
3. **Khách tệ nhất bị dời tổng cộng 14 phút** mà hệ thống vẫn tính là phục vụ thành công, vì
   vẫn nằm trong cửa sổ Ω/Δ hợp lệ. Đây là minh hoạ cụ thể nhất cho nhược điểm W1: cửa sổ hợp lệ
   không bảo vệ lời đã nói.

Điểm 3 cũng chỉ ra vì sao **hàm mục tiêu cộng gộp không đủ**: Alonso-Mora Eq.(1) tối thiểu hoá
*tổng* thiệt hại gây cho khách cũ. Cộng gộp thì người khổ nhất tàng hình. 14 phút của một người
bị pha loãng trong 1,735 người.

## A.4 Chỗ đứng so với văn liệu

Xác nhận từ chính bài của Fielbaum (bản arXiv đọc được):
- *"The paper does not decompose unreliability into specific causal categories like new request
  arrivals versus traffic effects."*
- Ωw, Ωd là *"hard constraints rather than fairness budgets across passengers"*
- *"no per-passenger reassignment limits are enforced"*

---

# CHÂN D — Kết luận có phụ thuộc cách đo không?

## D.1 Vì sao phải hỏi

Sridharan, Berry & Udayabhanu (1987) kết bài bằng việc trỏ sang bài bạn đồng hành
(*Decision Sciences* 19(1), 1988) về **cách đo** bất ổn, và ghi rõ rằng các thước đo đó
*"permit different weights to be placed on MPS changes that occur at different points in the
planning horizon, as well as the use of linear and quadratic expressions"*.

RideBound hiện chỉ dùng **một** thành viên của họ đó: tổng tuyến tính không trọng số.
Nếu thứ hạng đổi theo thước đo thì chính điều đó là phát hiện.

## D.2 Kết quả (40 lần chạy đã niêm phong, 35 giây tính toán, không chạy mô phỏng)

| Thước đo | B1 | C1 | C1/B1 |
|---|---:|---:|---:|
| Tuyến tính Σ\|Δ\| | 74,443 s | 128 s | 0.0017 |
| Bình phương √Σ Δ² | 4,501.6 s | 51.6 s | **0.0001** |
| Trọng số bậc thang (3× trong 5 phút cuối, 2× trong 10 phút) | 180,824 s | 300 s | 0.0017 |
| Trọng số cận kề liên tục 300s/(300s+r) | 41,571 s | 77 s | 0.0018 |
| Đếm số lần dời | 479 | 11 | **0.0230** |
| Khách tệ nhất | 840.9 s | 27.6 s | **0.0328** |
| Khách phân vị 95 | 264.6 s | 0.0 s | 0.0000 |

## D.3 Hai kết luận

**① Hướng vững tuyệt đối.** C1 ổn định hơn B1 dưới **cả bảy** thước đo. Không thước nào lật
ngược. Kết luận chính của khoá luận không phụ thuộc lựa chọn cách đo.

**② Độ lớn lệch tới ~300 lần.** Tuyến tính nói "tốt hơn 585×"; đếm số lần nói "43×";
khách-tệ-nhất nói "30×". Cùng dữ liệu, cùng hướng, hai bậc độ lớn khác nhau.

Hệ quả thực hành: **không được quảng cáo con số 585×.** Phải báo cáo cả họ thước đo, và nói rõ
con số nào ứng với câu hỏi nào:
- "hệ thống dời tổng cộng bao nhiêu?" → tuyến tính
- "bao nhiêu lần khách bị làm phiền?" → đếm
- "người khổ nhất khổ đến đâu?" → worst-rider

Ba câu hỏi khác nhau, ba con số khác nhau, đều đúng.

## D.4 Vì sao mục này đáng có trong khoá luận

Nó biến một điểm yếu tiềm tàng ("sao anh chọn cách đo này?") thành một mục robustness.
Và nó tái hiện trong ride-pooling đúng cảnh báo mà OM đã đưa ra từ 1988 — có nền, có trích dẫn,
và chưa ai làm ở ngành này.

---

# Trạng thái chân B

8 nhánh × 20 ô = 160 lần chạy, đang chạy nền, song song 4.
Đo được: 10 phút/ô, 62 MB/ô → ~7 giờ, ~10 GB.

Bộ chạy đã xác thực: nhánh `reference` tái lập đúng C1 niêm phong (92 = 92) trên ô kiểm.

Thứ tự: nobudget → budget300 → budget120 → budget60 → freeze300 → freeze600 → ratchet →
freeze300+ratchet.

---

# CHÂN B — Đường biên (đang chạy, kết quả từng phần)

## B.1 Bậc thang ngân sách — 4/5 điểm đã có

| Nhánh | Cam kết | Phục vụ | Tỉ lệ % | vs B1 pp | Xáo trộn do nhà xe (s) | Khách tệ nhất (s) | Khách bị ảnh hưởng |
|---|---|---:|---:|---:|---:|---:|---:|
| B1 | không hứa gì | 1735 | 80.3241 | 0 | 74,443 | 841 | 403 |
| nobudget | cùng xe + cùng điểm | 1655 | 76.6204 | −3.70 | 22,485 | 595 | 142 |
| budget300 | + trần 300 s | *đang chạy* | | | | | |
| budget120 | + trần 120 s | 1608 | 74.4444 | −5.88 | 5,063 | 119 | 76 |
| budget60 | + trần 60 s | *đang chạy* | | | | | |
| C1 | + trần 30 s | 1581 | 73.1944 | −7.13 | 128 | 28 | 11 |

## B.2 Phân rã cái giá 7.13 pp

| Bước | Cam kết thêm | Giá | Ổn định mua thêm |
|---|---|---:|---:|
| B1 → nobudget | khoá danh tính xe + điểm đón/trả | **−3.70 pp** (52%) | 51,958 s (70%) |
| nobudget → budget120 | trần ETA 120 s | −2.18 pp | 17,422 s |
| budget120 → C1 | siết xuống 30 s | −1.25 pp | 4,935 s |

**Chi phí biên của việc siết chặt đang GIẢM DẦN.** Phần đắt nhất là quyết định cam kết chút nào đó
(khoá danh tính), không phải độ chặt của lời hứa về thời gian.

Điều này **ngược với Sridharan 1987** trong sản xuất, nơi cost error bùng nổ khi đóng băng quá 80%
tầm nhìn. Nếu giữ vững khi có β=300 và β=60, đây là một tương phản liên ngành đáng viết thành mục
riêng: *vì sao ổn định lịch trong điều phối xe lại có cấu trúc chi phí ngược với ổn định lịch
trong sản xuất?*

Giả thuyết giải thích: trong MRP, đóng băng lấy đi **quyền chọn lại lô hàng** — thứ mà thuật toán
lot-sizing dựa vào để tiết kiệm. Trong ride-pooling, khi đã khoá xe và điểm dừng thì không gian
quyết định còn lại vốn đã hẹp; siết thêm trần thời gian chỉ cắt nốt một cái đuôi mỏng
(76 → 11 hành khách). Cái đuôi mỏng thì rẻ.

## B.3 Lời hứa được cưỡng chế đúng thiết kế

| Nhánh | Trần | Khách tệ nhất thực tế |
|---|---:|---:|
| budget120 | 120 s | **119 s** ✓ |
| C1 | 30 s | **27.6 s** ✓ |

Không ô nào vượt trần. Đây là bằng chứng lời hứa cưỡng chế được, không phải chỉ là chỉ tiêu.

## B.4 Nhóm chứng, phát biểu đúng

| | Số lần công bố | Trôi dạt ngoại sinh | Trôi dạt / lần công bố |
|---|---:|---:|---:|
| B1 | 54,311 | 9,202.6 s | 0.169 s |
| nobudget | 50,201 | 9,703.1 s | 0.193 s |
| budget120 | — | 9,259.6 s | — |
| C1 | 45,542 | 9,204.5 s | 0.202 s |

Tổng trôi dạt vật lý dao động **vài phần trăm** qua các chính sách rất khác nhau, trong khi xáo
trộn do nhà xe gây ra thay đổi **580 lần**. Không nên nói "lệch 0.02%" — đó là may mắn riêng của
cặp B1/C1. Phát biểu đúng: hai đại lượng phản ứng hoàn toàn khác nhau với chính sách.

## B.5 Chân D mở rộng sang 3 nhánh

Thứ hạng ổn định B1 > nobudget > C1 giữ nguyên trên **cả bảy** thước đo. Kết luận robustness
không còn dựa trên 2 nhánh mà 3.

## B.6 Sự cố đã xử lý

1. **Config β=300 s hỏng cả 20 ô** — tôi đổi `policyId` cho dễ đọc, nhưng kịch bản ràng buộc nhà
   xe với đúng id cũ (`RBWP7_COMMITMENT_POLICY_UNDECLARED`). Đã trả lại id gốc, xác minh config
   giống hệt `budget120` trừ đúng trần. Hỏng ở bước khởi tạo nên chỉ tốn ~25 giây.
2. **Phiên làm việc kết thúc làm chết sweep ở ô thứ 43.** Đã dọn 6 ô dở và phóng lại
   **tách rời khỏi shell** (`Start-Process`) để lần sau sống sót.
3. **Màn theo dõi báo động giả** rồi tự thoát: phép kiểm tra sự sống bằng `tasklist` không khớp.
   Đã thay bằng kiểm tra theo tiến độ (không có ô nào xong trong ~20 phút thì mới báo).

---

# CHÂN C — Bổ sung: TRỘI NGHIÊM NGẶT, đo ở cùng mức ngân sách

Xác minh trực tiếp từ các thư mục kết quả (không qua tóm tắt phiên cũ).

## C.7 Tập ô vô nghiệm, xác nhận từ dữ liệu gốc

| β (cơ sở outcome) | Ô vô nghiệm |
|---|---|
| 30 s | 16-r2, **16-r4**, 17-r1, 17-r3 |
| 120 s | 14-r4, 15-r2, **16-r4**, 17-r4 |

Giao nhau đúng 1/4 ô. Nới ngân sách gấp 4 lần **không chữa được** — chỉ dời chỗ đau. Mệnh đề ③ ✓

## C.8 So ở CÙNG mức ngân sách — cơ sở conduct trội nghiêm ngặt

| Trần | Conduct khả thi | Outcome khả thi | Phục vụ trên 16 ô chung |
|---|---:|---:|---|
| 30 s | **20/20** | 16/20 | conduct 1294 — outcome 1294 — **chênh 0** |
| 120 s | **20/20** | 16/20 | conduct 1267 — outcome 1266 — **chênh −1** |

Ở trần 30 s: **không một ô nào khác nhau**, đúng 0 hành khách chênh lệch.
Ở trần 120 s: khác nhau ở đúng 1 ô, đúng 1 hành khách.

### Phát biểu

> Ở cùng một mức ngân sách, cơ sở **outcome** cho **gần như đúng cùng số hành khách** ở những ô
> nó chạy được — nhưng **sụp hoàn toàn ở 4/20 ô** ở cả hai mức ngân sách. Cơ sở **conduct**
> không bao giờ sụp.

Tức là **nghĩa vụ kết quả là thuần rủi ro**: nó không mua thêm gì cả, và nó phá vỡ hệ thống
trên 20% số ô. Đây là **trội nghiêm ngặt** — conduct không bao giờ tệ hơn, và đôi khi tốt hơn
theo kiểu thảm hoạ-vs-không-thảm-hoạ.

### Vì sao đây là bằng chứng đẹp

Lý thuyết (C.2–C.4) nói: conduct **luôn** khả thi, outcome **có thể** vô nghiệm, nới β không cứu.
Thực nghiệm nói thêm một điều lý thuyết không nói: **khi outcome khả thi thì nó cũng chẳng cho
thêm gì.**

Hai vế khớp nhau hoàn hảo, và vế thực nghiệm làm kết luận thành lời khuyên thiết kế dứt khoát:
*đừng hứa về kết quả — không phải vì hứa kết quả thì tốn kém, mà vì nó vô ích và nguy hiểm.*

---

# CHÂN B — Bậc thang ngân sách HOÀN TẤT (6 điểm)

| Nhánh | Cam kết | Phục vụ | vs B1 pp | Xáo trộn (s) | Khách tệ nhất | Bị ảnh hưởng |
|---|---|---:|---:|---:|---:|---:|
| B1 | không hứa gì | 1735 | 0 | 74,443 | 841 s | 403 |
| nobudget | khoá xe + điểm | 1655 | −3.70 | 22,485 | 595 s | 142 |
| budget300 | + trần 300 s | 1641 | −4.35 | 15,809 | 291 s | 128 |
| budget120 | + trần 120 s | 1608 | −5.88 | 5,063 | 119 s | 76 |
| budget60 | + trần 60 s | 1579 | −7.22 | 1,109 | 59 s | 34 |
| C1 | + trần 30 s | 1581 | −7.13 | 128 | 28 s | 11 |

Trần luôn được tôn trọng: 291<300, 119<120, 59<60, 27.6<30. Cơ chế cưỡng chế đúng.

## B.7 ĐỘ NHẠY QUỸ ĐẠO — cảnh báo phương pháp luận bắt buộc

`budget60` phục vụ 1579, `C1`@30 s phục vụ **1581**. Trần chặt hơn lại cho kết quả tốt hơn.

Kiểm tra từng ô:
- **11/20 ô khác nhau giữa 60 s và 30 s**, khác theo **cả hai chiều**:
  +4, +2, +1, +1, +1 và −2, −1, −1, −1, −1, −1
- **8/20 ô vi phạm thứ tự đơn điệu** 120 ≥ 60 ≥ 30

Đây **không phải nhiễu thống kê**: mọi lần chạy dùng cùng hạt giống (master-seed 7), hoàn toàn
tất định. Đây là **độ nhạy quỹ đạo** — ràng buộc chặt hơn làm đổi *phương án nào được chọn sớm*,
và khác biệt đó lan truyền qua chuỗi quyết định. Tất định nhưng thực tế không dự đoán được.
Cùng cơ chế khiến tối ưu tham lam không phải tối ưu toàn cục.

### Sàn nhiễu, và phải công bố nó

Độ tán mức ô: ±1 đến ±4 khách trên ~80. Trên bảng 20 ô, **chênh lệch dưới ~±7 khách (±0.3 pp)
không diễn giải được.**

| So sánh | Chênh | Kết luận |
|---|---:|---|
| ∞ → 300 s | 0.65 pp (14 khách) | vừa đủ trên sàn |
| 300 → 120 s | 1.53 pp (33 khách) | **thật** |
| 120 → 60 s | 1.34 pp (29 khách) | **thật** |
| 60 → 30 s | 0.09 pp (2 khách) | **thuần nhiễu quỹ đạo** |

Không có bước kiểm tra từng ô này, ta đã báo cáo "siết từ 60 xuống 30 giây tiết kiệm 2 chuyến" —
một kết luận vô nghĩa.

### Bất đối xứng đáng chú ý

| | Phản ứng với chính sách |
|---|---|
| Tỉ lệ phục vụ | **nhiễu** — vi phạm đơn điệu ở 8/20 ô, sàn ±0.3 pp |
| Độ ổn định lời hứa | **sạch** — đơn điệu tuyệt đối, trải 175×, không ngoại lệ |

Điều này củng cố chân D: các thước đo ổn định là tín hiệu đáng tin hơn nhiều so với đếm hành khách.
Một khoá luận chỉ báo cáo tỉ lệ phục vụ sẽ đọc nhầm nhiễu thành kết quả.

## B.8 Khuyến nghị thiết kế từ bậc thang ngân sách

1. **Điểm gãy ở 300 giây.** 4.35 pp mua lời hứa "giờ trả không xê dịch quá 5 phút"; chỉ +0.65 pp
   so với chỉ-khoá-danh-tính, mà cắt đôi trường hợp tệ nhất (595 → 291 s).
2. **Từ 60 xuống 30 giây là miễn phí.** Chi phí không đổi trong sàn nhiễu, nhưng xáo trộn giảm
   9× và trường hợp tệ nhất giảm một nửa. Đã trả tới 60 s thì đi tiếp tới 30 s.
3. **Phần đắt nhất là quyết định cam kết chút nào đó** — 3.70 pp cho khoá danh tính, hơn nửa
   tổng chi phí, trước khi hứa một chữ về thời gian.

## B.9 Hiệu suất mua sự ổn định (giây ổn định trên mỗi chuyến hy sinh)

649 → 624 → 546 → 470 → 483

Giảm dần cho tới khi chạm sàn nhiễu ở hai điểm cuối (470 và 483 không phân biệt được).
Lợi ích cận biên giảm dần, đo được.

---

# CHÂN B HOÀN TẤT — 141 lần chạy, 7/9 nhánh

## B.10 Bảng đầy đủ

### Bậc thang 1: ngân sách giờ trả (mọi khoá giữ nguyên)

| Nhánh | Cam kết | Phục vụ | vs B1 pp | Xáo trộn (s) | Tệ nhất | Bị ảnh hưởng |
|---|---|---:|---:|---:|---:|---:|
| B1 | không hứa gì | 1735 | 0 | 74,443 | 841 s | 403 |
| nobudget | khoá xe + điểm | 1655 | −3.70 | 22,485 | 595 s | 142 |
| budget300 | + trần 300 s | 1641 | −4.35 | 15,809 | 291 s | 128 |
| budget120 | + trần 120 s | 1608 | −5.88 | 5,063 | 119 s | 76 |
| budget60 | + trần 60 s | 1579 | −7.22 | 1,109 | 59 s | 34 |
| C1 | + trần 30 s | 1581 | −7.13 | 128 | 28 s | 11 |

### Bậc thang 2: bảo vệ giờ đón (trần giờ trả cố định 30 s)

| Nhánh | Bảo vệ giờ đón thế nào | Phục vụ | vs B1 pp | Xáo trộn (s) | Tệ nhất |
|---|---|---:|---:|---:|---:|
| nopickuplock | không bảo vệ | 1583 | −7.04 | 187 | 34 s |
| freeze300 | hàng rào 300 s | 1583 | −7.04 | 187 | 34 s |
| freeze600 | hàng rào 600 s | 1581 | −7.13 | 128 | 28 s |
| C1 | khoá khi xác nhận | 1581 | −7.13 | 128 | 28 s |
| ratchet | một chiều | **không chạy được** | | | |
| freeze300+ratchet | cả hai | **không chạy được** | | | |

**Bậc thang 2 sụp xuống đúng HAI hành vi**, không phải năm:

- **Không bảo vệ trong cửa sổ 300–600 s trước lúc đón** → 187 s xáo trộn, 1583 khách
  (`nopickuplock`, `freeze300`)
- **Có bảo vệ trong cửa sổ đó** → 128 s, 1581 khách (`freeze600`, `C1`)

Giá của việc bảo vệ: **2 hành khách** (trong sàn nhiễu). Lợi ích: bớt 32% xáo trộn.

## B.11 Vì sao bậc thang 2 sụp — đo trực tiếp

Quét 19,539 lần công bố (8 ô, C1), khoảng cách từ lúc công bố tới lúc đón:

| | Số lần | Tỉ lệ |
|---|---:|---:|
| Khách đã lên xe | 9,057 | **46.4%** |
| Còn 0–300 s | 7,199 | 36.8% |
| Còn 300–600 s | 3,283 | 16.8% |
| **Còn > 600 s** | **0** | **0.0%** |

Thời gian báo trước lúc xác nhận: p50 = 400 s, p90 = 556 s, **max = đúng 600 s**.

Ba hệ quả:

1. **Hàng rào 600 s không bao giờ mở** — kịch bản có tầm đặt chỗ 10 phút. Mọi hàng rào ≥ 600 s
   đều tương đương khoá vĩnh viễn. *Hạn chế phạm vi: không kết luận được gì về hàng rào dài hơn
   tầm đặt chỗ.*
2. **Hàng rào 300 s ≡ không khoá** — trong vòng 300 s cuối, xe đã cam kết và đang trên đường,
   giờ đón vốn không còn chỗ xê dịch. Khoá nó là thừa.
3. **46.4% mọi lần công bố xảy ra sau khi khách đã lên xe** — chúng chỉ nói về giờ trả.
   Đây là lời giải thích cơ học cho bất đối xứng giữa hai bậc thang: ngân sách giờ trả chi phối
   gần một nửa khối lượng công bố nên đắt; khoá giờ đón chỉ chạm phần đầu vốn đã chật nên rẻ.

Ba kết quả độc lập — chi phí bậc thang 1, chi phí bậc thang 2, phân bố thời điểm công bố — khớp
vào cùng một lời giải thích.

## B.12 CHÂN D mở rộng: 9 thước đo × 6 nhánh, KHÔNG một ngoại lệ

| Thước đo | B1 | nobudget | 300 s | 120 s | 60 s | 30 s |
|---|---:|---:|---:|---:|---:|---:|
| tuyến tính Σ\|d\| | 74,443 | 22,485 | 15,809 | 5,063 | 1,109 | 128 |
| bình phương √Σd² | 4,502 | 2,288 | 1,590 | 649 | 227 | 52 |
| trọng số bậc thang | 180,824 | 58,841 | 40,943 | 13,129 | 2,975 | 300 |
| trọng số cận kề | 41,571 | 13,618 | 9,541 | 3,214 | 728 | 77 |
| đếm số lần dời | 479 | 155 | 135 | 79 | 34 | 11 |
| khách tệ nhất | 841 | 595 | 291 | 119 | 59 | 28 |
| p99 khách | 536 | 331 | 218 | 101 | 39 | 0 |
| p95 khách | 265 | 115 | 83 | 0 | 0 | 0 |
| số khách bị dời | 403 | 142 | 128 | 76 | 34 | 11 |

**Cả chín thước đo đơn điệu trên cả sáu nhánh. Không một ngoại lệ.**

Đối chiếu: tỉ lệ phục vụ **vi phạm** đơn điệu ở 8/20 ô. Trôi dạt ngoại sinh: 9,184–9,703 s,
biên độ 5.6%, **không có xu hướng**.

### Ba đại lượng, ba hành vi khác hẳn nhau

| Đại lượng | Phản ứng với chính sách |
|---|---|
| Độ ổn định lời hứa | **đơn điệu tuyệt đối**, 9 thước đo, 0 ngoại lệ |
| Trôi dạt vật lý | **bất biến**, ±5.6%, không xu hướng |
| Tỉ lệ phục vụ | **nhạy quỹ đạo**, vi phạm đơn điệu 8/20 ô, sàn ±0.3 pp |

Đây là kết quả trung tâm về phương pháp: phép phân rã ba mốc tách được một đại lượng
**phản ứng sạch với chính sách** (hành vi) khỏi một đại lượng **không phản ứng** (vật lý),
trong khi thước đo truyền thống (tỉ lệ phục vụ) lại nhiễu nhất trong ba.

## B.13 HẠN CHẾ: hai nhánh không chạy được

`ratchet` và `freeze300ratchet` chết ngay lúc bắt tay: `RBWP7_RUNNER_EOF at $runner: helloAck`.

Nguyên nhân xác định:

| | Ngày |
|---|---|
| Runner đã niêm phong (`h6-confirmatory-v1`) | **2026-08-22** |
| `FreezeHorizonLocks` vào code | 2026-07-31 → trước → chạy được |
| `RatchetLocks` vào code | **2026-09-04** → sau 13 ngày → runner không biết trường |

Runner bị ghim theo `runnerSha256` trong biên bản niêm phong. Muốn chạy nhánh ratchet phải
**build runner mới**, và khi đó kết quả **không còn so sánh được** với B1/C1 đã niêm phong —
khác nhị phân, khác semanticHash, và sai biên bản.

Đây là hạn chế phải công bố, không phải lỗi. Lựa chọn:

- **(a) Bỏ nhánh ratchet**, ghi rõ lý do. Giữ nguyên tính toàn vẹn của bảng so sánh.
- **(b) Thí nghiệm phụ tách riêng**: build runner mới, chạy ratchet + một nhánh tham chiếu trên
  runner đó, so sánh **nội bộ** với nhau, tuyệt đối không trộn với bảng chính.
  Chi phí ~60 lần chạy ≈ 2.5 giờ.

Phương án (b) có giá trị vì ratchet chính là cơ chế Alonso-Mora 2017 dùng
(*"forbids an increase in the achieved waiting time"*), nên so được "cách của ta" với
"cách của văn liệu". Nhưng phải trình bày như một thí nghiệm riêng.

---

# THÍ NGHIỆM PHỤ — bảo đảm một chiều (ratchet)

## P.0 Vì sao phải tách riêng

Runner niêm phong `h6-confirmatory-v1` (build 2026-08-22, sha256 `8445f053…`) ra đời **trước**
`RatchetLocks` (vào code 2026-09-04) nên chết ngay lúc bắt tay khi nhận policy ratchet.

Đã build runner mới `ratchet-secondary-v1` (sha256 `931114e2…`) vào thư mục riêng
`E:/RideBoundData/wp14/`. **Runner niêm phong không bị đụng** — hash xác nhận không đổi trước và
sau khi build.

Số liệu thí nghiệm phụ **không bao giờ được trộn vào bảng chính.**

## P.1 Thiết kế tự kiểm chứng

| Nhánh | Vai trò | Kỳ vọng |
|---|---|---|
| `ratchet` | điều trị — cơ chế Alonso-Mora 2017 | chưa biết |
| `reference` | **chứng** (đã có trên runner cũ) | phải ra 1581 |
| `nopickuplock` | **chứng** (đã có trên runner cũ) | phải ra 1583 |
| `freeze300ratchet` | điều trị kết hợp | chưa biết |

## P.2 Kết quả ratchet

| | nopickuplock | **ratchet** | C1 (khoá cứng) |
|---|---:|---:|---:|
| Phục vụ | 1583 | **1581** | 1581 |
| Xáo trộn do quyết định | 187 s | **128 s** | 128 s |
| Số lần dời | 13 | **11** | 11 |
| Khách tệ nhất | 34.4 s | **27.6 s** | 27.6 s |
| Trôi dạt ngoại sinh | 9,212 s | 9,204.5 s | 9,204.5 s |

**Bảo đảm một chiều cho kết quả giống hệt khoá cứng hai chiều, không lệch một chữ số.**

Kiểm tra toàn vẹn: `semanticHash` và `publicationDigest` **khác nhau ở mọi ô** (hai runner khác
nhau, hai lần chạy thật), nhưng số khách từng ô khớp tuyệt đối: 92/92, 87/87, 79/79.
Và việc chạy được đã tự chứng minh config ratchet được nạp — runner cũ chết đúng trên file này.

## P.3 Vì sao ratchet ≡ khoá cứng — dữ liệu tự chứng minh

Ratchet cho phép giờ đón **tốt lên**, cấm **xấu đi**. Lập luận chỉ từ ba con số:

- `nopickuplock` (thả tự do) cho **59 giây** xê dịch giờ đón do quyết định (187 − 128)
- `ratchet` cho **0 giây**
- ⟹ **toàn bộ 59 giây đó đều là xấu đi.** Nếu có phần nào là cải thiện, ratchet đã cho qua.

Nguyên nhân cơ học: bộ sinh phương án **chỉ chèn thêm, không bỏ bớt**. Chèn một điểm dừng chỉ có
thể **đẩy lùi** giờ đón của khách cũ, không bao giờ kéo sớm lên. Quyền "được phép cải thiện" mà
ratchet trao là **quyền không bao giờ dùng được**.

Khớp với kết quả đã biết: `decisionMovedEarlier = 0` trên 421,752 lần sửa.

## P.4 Ý nghĩa đối chiếu văn liệu

Ratchet chính là cơ chế Alonso-Mora 2017:
*"forbids an increase in the achieved waiting time (compared to the one of the previous assignment)"*.

> Trong một bộ điều phối dựa trên chèn, **bảo đảm một chiều nghiêm ngặt đúng bằng khoá cứng**.
> Nó *trông* mềm hơn nhưng không mềm hơn chút nào.

Sự khác biệt tưởng như có giữa "ngân sách cứng" và "quy tắc một chiều của văn liệu" là **ảo** ở
chặng đón. Chỉ lộ ra khi đo.

Hệ quả rộng hơn: **hình thức của lời bảo đảm chỉ có ý nghĩa trong chừng mực bộ sinh phương án
có thể thực thi nó.** Một bảo đảm nới lỏng theo hướng mà thuật toán không bao giờ đi được thì
không nới lỏng gì cả. Đây là một quan sát về tương tác giữa *hình thức bảo đảm* và *cấu trúc
thuật toán* — chưa thấy nêu ở đâu.

## P.5 Trạng thái

Nhánh chứng `reference` đang chạy. **Chưa kết luận cuối** cho tới khi nó xác nhận runner mới
tương đương runner cũ (kỳ vọng 1581). Dấu hiệu hiện tại rất mạnh nhưng chưa đủ.

---

# LƯU Ý KỸ THUẬT — phép phân rã có cộng đúng không?

Ba mốc cho ba đại lượng, tất cả đều là **tổng trị tuyệt đối**:

- decision  = Σ |proposed − exogenous|
- exogenous = Σ |exogenous − previous|
- visible   = Σ |proposed − previous|

Theo bất đẳng thức tam giác, **visible ≤ decision + exogenous**, đẳng thức xảy ra khi hai thành
phần cùng chiều. Nên phép phân rã **không** là một phân hoạch chính xác. Kiểm tra độ hụt:

| Nhánh | decision | exogenous | tổng | visible | hụt | hụt % |
|---|---:|---:|---:|---:|---:|---:|
| B1 | 74,443 | 9,203 | 83,646 | 83,587 | 58 | **0.07%** |
| nobudget | 22,485 | 9,703 | 32,188 | 32,176 | 12 | 0.04% |
| budget300 | 15,809 | 9,641 | 25,450 | 25,441 | 9 | 0.03% |
| budget120 | 5,063 | 9,260 | 14,324 | 14,318 | 5 | 0.04% |
| budget60 | 1,109 | 9,184 | 10,293 | 10,291 | 1 | 0.01% |
| C1 | 128 | 9,204 | 9,332 | 9,332 | 0 | **0.00%** |

Độ hụt tối đa 0.07%, và bằng 0 ở C1.

**Diễn giải**: hai thành phần gần như luôn cùng chiều — khi bộ điều phối làm xấu đi một lời hứa
thì trôi dạt vật lý thường cũng đang làm xấu đi, hoặc một trong hai thành phần áp đảo. Chúng
hiếm khi triệt tiêu nhau.

**Cách phát biểu đúng trong báo cáo**: không nói *"89.06% lượng xáo trộn được gây ra bởi..."*
(ngụ ý phân hoạch), mà nói *"phần do bộ điều phối gây ra bằng 89.06% lượng khách nhìn thấy"*
(một tỉ số, đúng theo nghĩa đen). Sai khác chỉ 0.07% nên kết luận không đổi, nhưng cách nói phải
chính xác.

---

# THÍ NGHIỆM PHỤ — HOÀN TẤT (80/80)

## P.6 Runner mới đã được kiểm chứng đầy đủ

| Nhánh chứng | Runner mới | Runner niêm phong | Ô sai lệch |
|---|---:|---:|---:|
| `reference` (khoá cứng) | 1581 | 1581 | **0/20** |
| `nopickuplock` (không khoá) | 1583 | 1583 | **0/20** |

Hai cấu hình độc lập ở hai cực của bậc thang, tái lập **từng ô một**. Runner mới tương đương
hành vi. Số liệu điều trị đọc được trên cùng thang.

## P.7 Bảng cuối — sáu cơ chế, HAI hành vi

| Thước đo | không khoá | freeze300+ratchet | ratchet | khoá cứng |
|---|---:|---:|---:|---:|
| Phục vụ | 1,583 | **1,583** | 1,581 | 1,581 |
| Số lần công bố | 45,644 | 45,644 | 45,542 | 45,542 |
| Tuyến tính Σ\|d\| | 187.0 | **187.0** | 128.0 | 128.0 |
| Bình phương | 66.7 | 66.7 | 51.6 | 51.6 |
| Trọng số bậc thang | 417.9 | 417.9 | 299.9 | 299.9 |
| Trọng số cận kề | 100.6 | 100.6 | 76.9 | 76.9 |
| Số lần dời | 13 | 13 | 11 | 11 |
| Khách tệ nhất | 34.4 s | 34.4 s | 27.6 s | 27.6 s |

Cộng thêm `freeze300` và `freeze600` từ bảng chính, **sáu cơ chế bảo vệ giờ đón rơi vào đúng
HAI hành vi**:

| Hành vi | Cơ chế | Phục vụ | Xáo trộn |
|---|---|---:|---:|
| **A — không bảo vệ cửa sổ 300–600 s** | `nopickuplock`, `freeze300`, `freeze300ratchet` | 1,583 | 187 s |
| **B — có bảo vệ cửa sổ đó** | `freeze600`, `ratchet`, khoá cứng | 1,581 | 128 s |

Khoảng cách giữa hai hành vi: **2 hành khách** (trong sàn nhiễu ±7) và **59 giây** xáo trộn.

## P.8 Ba lời giải thích, tất cả đều đã kiểm chứng bằng đo đạc

1. **`freeze600` ≡ khoá cứng** — vì tầm đặt chỗ đúng 600 s, hàng rào 600 s **không bao giờ mở**
   (0.0% số lần công bố xảy ra sớm hơn 600 s trước lúc đón).
2. **`freeze300` ≡ không khoá** — trong 300 s cuối, xe đã trên đường; giờ đón vốn không còn chỗ
   xê dịch nên khoá là thừa.
3. **`ratchet` ≡ khoá cứng** — bộ sinh phương án chỉ chèn thêm, không bỏ bớt, nên chỉ đẩy lùi
   được giờ đón chứ không kéo sớm lên. Quyền "được phép cải thiện" là quyền không dùng được.
   Dữ liệu tự chứng minh: thả tự do cho 59 s xê dịch, ratchet cho 0 s ⟹ toàn bộ 59 s đều là
   xấu đi.
4. **`freeze300ratchet` ≡ `freeze300` ≡ không khoá** — hệ quả của (2) và (3). *Dự đoán trước
   khi chạy, xác nhận đúng từng chữ số.*

## P.9 Kết luận của thí nghiệm phụ

> **Hình thức của một lời bảo đảm chỉ có ý nghĩa trong chừng mực bộ sinh phương án có thể
> thực thi nó.** Một bảo đảm nới lỏng theo hướng mà thuật toán không bao giờ đi được thì không
> nới lỏng gì cả; một hàng rào rộng hơn tầm đặt chỗ thì không phải hàng rào.

`ratchet` chính là cơ chế Alonso-Mora 2017 dùng
(*"forbids an increase in the achieved waiting time"*). Nên **sự khác biệt tưởng như có giữa
cách của văn liệu và khoá cứng là ảo** ở chặng đón — và chỉ lộ ra khi đo.

Đây là một quan sát về tương tác giữa **hình thức bảo đảm** và **cấu trúc thuật toán sinh
phương án**. Chưa thấy nêu ở đâu trong văn liệu ride-pooling.

### Cảnh báo phương pháp kèm theo

Nếu chỉ nhìn bảng tổng hợp, sáu dòng rơi vào hai giá trị trông như lỗi sao chép config. Chỉ nhờ
`semanticHash` và `publicationDigest` **khác nhau ở 20/20 ô** mới biết đó là các lần chạy thật,
đi qua những chuỗi lời hứa khác nhau, và về đích cùng chỗ. Không có chứng cứ niêm phong ở mức
đó thì kết luận này không kiểm chứng được.

---

> **Chân C đã được viết lại thành tài liệu độc lập, đầy đủ hơn phần C.1–C.8 ở trên:**
> **[`dinh-ly-conduct-vs-outcome.md`](./dinh-ly-conduct-vs-outcome.md)**
>
> Bản đó bổ sung ba thứ mà phần trên chưa có:
> - **Đẳng thức trung tâm `B = A + d`** (sổ cái outcome = sổ cái conduct + trôi dạt), kèm hai
>   điều kiện đã kiểm chứng và bảng độ khít 0.00–0.07%
> - **Định lý 3**: B không bao giờ phục vụ nhiều hơn A **với mọi β** — biến kết quả "chênh 0
>   khách" từ một quan sát ở β=30 s thành một định lý
> - **Trả lời câu "nếu trần rộng 5–10 phút thì sao"**: dải khác biệt rộng đúng `d` (đo được
>   4.9 s trung vị, 39.9 s tối đa) và **không phụ thuộc β**, trong khi cú nhảy ~130 s ⟹
>   khác biệt vẫn ~0; còn tính vô nghiệm biến mất từ β ≥ 60 s
>
> Khi tổng hợp báo cáo, dùng bản độc lập đó cho chương lý thuyết.
