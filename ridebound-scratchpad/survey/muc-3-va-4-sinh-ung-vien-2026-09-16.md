# Mục 4 và mục 3 (A, B, C): bộ sinh ứng viên biết đến lời hứa

Ngày 16/09/2026. Tài liệu ghi lại toàn bộ phép đo và kết luận cho hai hạng mục
cuối trong bảng câu hỏi mở. Mọi số liệu đều đo từ bằng chứng đã niêm phong;
không có dòng mã nào được ghi vào kho.

---

## 0. Tóm tắt một đoạn

Cả bốn hạng mục đều bị chính dữ liệu của hệ thống bác bỏ, mỗi hạng mục vì một lý
do khác nhau, và ba trong bốn lý do đo được **trước khi viết một dòng mã nào**.

Mức A và mức B chết vì tập lựa chọn quá mỏng: trên 217 736 quyết định cấp xe của
toàn panel, **96,0%** chỉ có đúng một ứng viên khả thi, trần số ứng viên chưa bao
giờ chạm, và không một ứng viên khả thi nào từng bị cắt bỏ. Mức C chạy được thật
nhưng **trùng khớp từng quyết định** với đối chứng: tầng cảnh báo bị đặt bên dưới
một tầng mục tiêu liên tục đo cùng đại lượng ở thang mịn hơn, nên nó không bao
giờ được lên tiếng — ý tưởng đặt trước ngân sách hóa ra đã có sẵn trong hệ thống
ở dạng mạnh hơn. Mục 4 — bộ sinh có khả năng sắp xếp lại — cũng **đã có sẵn
trong kho**, nhưng nó không bị ràng buộc cam kết, không thể ghép với chính sách
cam kết theo cấu hình hiện tại, và khi bật lên thì hỏng 18 trên 20 ô vì va vào
một bất biến thứ hai của mô hình.

---

## 1. Mức A và mức B: bị bác bỏ bằng phép đo

### 1.1 Hai mức này định làm gì

| Mức | Ý tưởng | Điều kiện để có tác dụng |
|---|---|---|
| A | Xếp hạng các vị trí chèn theo chi phí ngân sách, ưu tiên vị trí rẻ | Phải có ≥ 2 vị trí chèn để xếp |
| B | Cắt tỉa sớm nhánh sinh bằng cận dưới của chi phí ngân sách | Phải có nhánh bị cắt, hoặc có vấn đề tốc độ |

### 1.2 Phép đo

Nguồn: `payload/solver/executionEvidence/generation/vehicleLosses[]` trong
transcript, một mục cho mỗi xe ở mỗi vòng quyết định. Đo trên **toàn bộ panel
20 ô đã niêm phong, cả hai nhánh**: 113 064 quyết định cấp xe ở B1 và 104 672 ở
C1, tổng **217 736**.

| Chỉ số | B1 (không hứa) | C1 (trần 30 s) |
|---|---:|---:|
| Số lần chạm trần ứng viên (`candidateCapApplied`) | **0** | **0** |
| Số lần cạn ngân sách tính toán (`workBudgetExhausted`) | **0** | **0** |
| Ứng viên khả thi bị bỏ do trần | **0** | **0** |
| Nhánh chưa khai triển bị bỏ | **0** | **0** |
| Ứng viên khả thi trước trần / xe | 1,044 | 1,047 |
| Ứng viên được giữ lại / xe | **1,044 — y hệt** | **1,047 — y hệt** |
| Bị loại vì vật lý hoặc lịch trình / xe | 1,057 | 0,956 |

Phân bố số ứng viên trên mỗi quyết định cấp xe:

| Số ứng viên | B1 | C1 |
|---:|---:|---:|
| 1 | **96,04%** | **95,87%** |
| 2 | 3,59% | 3,65% |
| 3 | 0,31% | 0,42% |
| 4 | 0,05% | 0,04% |
| ≥ 5 | 0,02% | 0,02% |
| **≥ 2 (có gì để chọn)** | **3,96%** | **4,13%** |

Kiểm chứng chéo trên cấu hình cửa sổ rộng: C1 tại 900 s cho trung bình 1,066 ứng
viên và 5,62% quyết định có ≥ 2. Trần không chạm lần nào ở bất kỳ cấu hình nào.

### 1.3 Kết luận

**Mức A là phép toán rỗng.** Với một ứng viên thì không có gì để sắp xếp. Việc
xếp hạng chỉ có thể tác động lên **3,96–4,13%** số quyết định, và ngay cả ở đó
thì chín phần mười trường hợp tập chỉ có đúng hai phần tử.

**Mức B là phép toán rỗng.** Không có gì bị cắt (0 bỏ sót, 0 nhánh chưa khai
triển) nên cắt tỉa sớm không tiết kiệm được gì; và không có vấn đề tốc độ (0
lần cạn ngân sách) nên cũng không có gì để tăng tốc.

Ràng buộc siết chặt nằm ở tầng vật lý — cửa sổ đón và lịch trình — chứ không ở
bộ sinh. Đây là hệ quả trực tiếp của phát hiện đã ghi trong mục 4.10 của báo
cáo: khoảng bảy mươi mấy phần trăm ứng viên bị loại là do cửa sổ thời gian.

---

## 2. Mục 4: bộ sinh có khả năng sắp xếp lại

### 2.1 Phát hiện thứ nhất — nó đã có sẵn

Kho đã có sẵn cơ chế này: `WaitingIncumbentRepairSeedBuilder` (149 dòng), bật
qua trường cấu hình `repair.maximumRequestsConsideredPerVehicle`. Cơ chế lấy
một hành khách đang chờ, gỡ **cả cặp** đón–trả của người đó khỏi đuôi khả biến,
rồi chèn lại cặp ấy vào mọi vị trí giữ được thứ tự đón trước trả. Nó không gộp
nhiều nước đi, không đổi xe, không động vào người đã lên xe, không sửa chặng đã
đóng băng.

Một nhánh thực nghiệm đã chạy trước đây với `maximumRequestsConsideredPerVehicle
= 4`, kết quả ở `E:/RideBoundData/wp9/exploratory-b4-repair-v1`. Trước phiên này
nhánh đó chưa được chẩn đoán.

### 2.2 Phát hiện thứ hai — nó thật sự sắp xếp lại

Đây là điểm quan trọng, vì bộ sinh chèn thuần đã được kiểm chứng là **không bao
giờ** đảo thứ tự (0 lần đảo trên 2 980 lần công bố).

| Nhánh | Ô | Cập nhật kế hoạch | Sắp lại | Đổi chặng đầu | Đầu bị đẩy xuống | Đóng băng sớm |
|---|---:|---:|---:|---:|---:|---:|
| B1 (không hứa) | 20 | 5 328 | **0** | 2 950 | 57 | 0 |
| C1 (trần 30 s) | 20 | 4 864 | **0** | 2 618 | 17 | 0 |
| b4 (sắp lại) | 20 | 1 978 | **245** | 954 | 150 | 0 |

Sổ cái cam kết cũng ghi nhận: chiều `incumbentOrderInversionCount` bị tính phí
116 lần, tổng 120 đơn vị. Chiều này tồn tại trong vector ngân sách từ đầu nhưng
trước đây luôn bằng 0 vì bộ sinh chèn thuần về mặt cấu trúc không thể sinh ra
nó.

Nhánh b4 còn dao động: 167 lần một kế hoạch trùng đúng kế hoạch của hai lần
công bố trước đó (A → B → A). Ví dụ cụ thể, xe `6eb906e5` trong ô
`d20181114-s10-r2`, năm lần công bố liên tiếp:

```
#193   pk 43e7  dr 43e7  pk b5ef  dr b5ef
#194   pk 43e7  pk b5ef  dr 43e7  dr b5ef      <- đảo
#196   pk 43e7  dr 43e7  pk b5ef  dr b5ef      <- đảo ngược lại
#198   pk 43e7  pk b5ef  dr 43e7  dr b5ef      <- đảo lần nữa
#199            dr 43e7  pk b5ef  dr b5ef      <- đảo lần thứ ba, và sập
```

Tại #199 xe vừa thực hiện xong `pk 43e7` nên đang trên đường tới `pk b5ef` theo
kế hoạch #198. Kế hoạch #199 lại bảo nó đi tới `dr 43e7` trước. Xe không quay
đầu giữa đường được.

### 2.3 Phát hiện thứ ba — nó hỏng 18 trên 20 ô

| Mã lỗi | Số ô |
|---|---:|
| `RBWP7_LOCKED_LEG_MISMATCH at $.vehicles[N].activeLeg` | **18** |
| `RBWP7_RUNNER_PROTOCOL_ERROR` (ngân sách giai đoạn tiền giải) | 1 |
| chạy trọn vẹn | 1 |

Nguyên nhân gốc là **hai mô hình bất đồng về thời điểm một chặng trở thành
không thể rút lại**:

- Phía RideBound, `RoutePlan.AdvanceReachedStop` chuyển một chặng từ đuôi khả
  biến sang tiền tố đóng băng **khi xe tới nơi**. Không có chuyển trạng thái nào
  cho "xe đã xuất phát hướng tới". Giữa lúc xuất phát và lúc tới, chặng đích nằm
  ở `MutableSuffix[0]` và về mặt mô hình vẫn sửa được.
- Phía FleetPy, cầu nối khóa chặng đang chạy ngay khi xe lăn bánh, và
  `assign_vehicle_plan` từ chối mọi kế hoạch thay thế có chặng đầu không trùng
  khít (`_leg_signature`: trạng thái, đích, danh sách lên, danh sách xuống, cờ
  khóa, thời lượng, mốc sớm nhất bắt đầu, mốc sớm nhất kết thúc).

Cột "đóng băng sớm" trong bảng ở mục 2.2 bằng **0 trên cả ba nhánh**, tức là hệ
thống chưa một lần đóng băng một chặng trước khi xe tới, mặc dù kiểu dữ liệu
`RoutePlan` cho phép điều đó (`ExecutedStopCount < FrozenPrefix.Count` là trạng
thái hợp lệ, và `PendingStops` đã xử lý đúng trường hợp ấy).

Tỉ lệ đẩy chặng đầu trên mỗi lần cập nhật kế hoạch: B1 1,07%, C1 0,35%, b4
**7,58%**. Sắp xếp lại làm tỉ lệ này tăng bảy lần, và với khoảng một trăm lần
cập nhật mỗi ô thì việc bắt gặp một xe đang giữa đường gần như chắc chắn xảy ra.

### 2.4 Phát hiện thứ tư — nhánh này không bị ràng buộc cam kết

Đọc `SolverBackedRidePoolingPolicy.cs`: câu lệnh `switch` gán hồ sơ mục tiêu chỉ
xử lý `RollingPenalty`, `FixedFreezeHorizon`, `RideBoundHardVector` và
`CommitSoftHardHybrid`. `NoReassignmentRepair` **rơi xuống mặc định**
`RollingCost`, không qua bộ lọc cam kết nào.

Điều này được xác nhận ở tầng sâu hơn chứ không chỉ suy từ câu `switch`. Hàm
`EffectivePolicies` đưa mọi chính sách không nằm trong ba trường hợp trên qua
`MechanismCommitmentPolicyProvider.RevisionPenalty`, và hàm này dựng lại từng
chính sách với `hardLimit: null` trên **mọi** chiều cùng
`finalConfirmationLocks: PromiseLock.None`. Bộ kiểm tra toàn đội
(`FullFleetValidator`) sau đó kiểm chứng trên chính bộ chính sách đã bị gỡ trần
ấy. Nói cách khác, nhánh b4 chạy với **toàn bộ trần cam kết bị tháo bỏ có chủ
ý** — đúng như nhánh B1. Vậy b4 so sánh được với B1, không so được với C1.

Trên ô duy nhất chạy trọn vẹn (`d20181114-s10-r1`):

| Nhánh | Phục vụ |
|---|---:|
| B1 (chèn thuần, không hứa) | 99 |
| b4 (sắp lại, không hứa) | **99** |
| C1 (chèn thuần, trần 30 s) | 92 |

Thêm khả năng sắp xếp lại vào một bộ điều phối vốn đã tự do hoàn toàn thu được
**đúng không hành khách nào**. Cỡ mẫu một ô nên đây là chỉ dấu chứ chưa phải kết
luận, nhưng nó phù hợp với phát hiện gốc: ràng buộc siết chặt là cửa sổ đón, chứ
không phải thứ tự các điểm dừng.

### 2.5 Phát hiện thứ năm — không thể ghép sắp-lại với cam kết

`Wp4RunnerConfiguration.RequireVariantFields` kiểm tra `hasRepair != isB4` và
ném `InvalidDataException`. Trường `repair` **chỉ** dùng được với chính sách
`no-reassignment-repair`. Nói cách khác, cấu hình hiện tại không diễn đạt được
tổ hợp "sắp xếp lại + lời hứa có biên" — đúng tổ hợp mà mục 4 cần.

### 2.6 Đóng băng chặng đang chạy có giết luôn cơ chế không?

Không. Phân loại 245 lần sắp xếp lại quan sát được:

| Loại | Số lần | Tỉ lệ |
|---|---:|---:|
| Diễn ra hoàn toàn **phía sau** chặng đang chạy — vẫn hợp lệ | 102 | **41,6%** |
| Đẩy chặng đang chạy xuống — bị chặn, và là thứ đang làm sập | 134 | 54,7% |
| Chặng đầu vừa được phục vụ xong | 9 | 3,7% |

Bước sửa lấy đi khoảng một nửa láng giềng nhưng giữ lại một nửa. Đủ để câu hỏi
còn đáng hỏi.

### 2.7 Phạm vi thật của mục 4

Muốn trả lời câu hỏi của mục 4 phải sửa mã nguồn ở ba chỗ, theo đúng thứ tự
này:

1. **Miền.** Thêm chuyển trạng thái đóng băng chặng đang bay — chuyển
   `MutableSuffix[0]` vào `FrozenPrefix` mà không tăng `ExecutedStopCount`. Kiểu
   dữ liệu đã hỗ trợ; chỉ thiếu điểm gọi. Không có bước này thì mọi thứ phía sau
   đều hỏng 18/20 ô.
2. **Chính sách.** Cho `RideBoundHardVector` nhận `MaximumRepairRequestsConsideredPerVehicle`
   (hiện chỉ nhánh `NoReassignmentRepair` truyền tham số này vào
   `generationOptions.WithRepairRequestCap`).
3. **Cấu hình.** Nới điều kiện `hasRepair != isB4` để cho phép `repair` đi kèm
   chính sách cam kết.

Cộng thêm một bản dựng runner mới và hai nhánh đối chứng theo đúng kỷ luật đã
dùng cho thí nghiệm ratchet. Đây là công việc có phạm vi rõ ràng chứ không mơ
hồ, nhưng nó **không phải** là bật một cờ cấu hình, và bằng chứng ở mục 2.4 gợi
ý rằng phần thưởng nhiều khả năng bằng không.

---

## 3. Mức C: đặt trước ngân sách — nhánh duy nhất chạy được

### 3.1 Cơ chế

Mức C không động vào bộ sinh. Nó chèn một tầng vào hàm mục tiêu từ điển của bài
toán đóng gói tập hợp trên toàn đội xe:

```
worst-hard-utilization  >  warning-excess  >  revision  >  cost
```

Một ứng viên còn nằm trong trần cứng nhưng đã vượt một ngưỡng cảnh báo thấp hơn
sẽ bị hạ bậc. Ý đồ là làm cho bộ điều phối tiêu ngân sách của một hành khách một
cách dè dặt, để dành chỗ cho một yêu cầu sau có thể cần tới — đặt trước có chủ
ý, thay vì ai đến trước tiêu trước.

Điểm mấu chốt khiến mức C **không** chết như mức A và B: tầng này tác động lên
bài toán ILP trên toàn đội xe, chứ không phải lên danh sách ứng viên trong một
xe. Ngay cả khi mỗi xe chỉ có một ứng viên, ILP vẫn phải chọn xe nào phục vụ yêu
cầu nào. Phát hiện "tập lựa chọn mỏng" vì thế không vô hiệu hóa nó.

### 3.2 Ghép cấu hình

Ngưỡng cảnh báo bắt buộc phải thấp hơn trần cứng; runner từ chối
`warningLimit > hardLimit` bằng `INVALID_COMMITMENT_WARNING_LIMIT`. Cấu hình
soft-hybrid đã kiểm toán mang `warningLimit = 60 s` trên `drop_eta_total_ms`,
nên nó không ghép được với trần 30 s đã niêm phong. Nó ghép với trần 120 s:

| Nhánh | Chính sách chọn | Cấu hình cam kết |
|---|---|---|
| điều trị | `wp9-fleetpy-soft-hard-hybrid-audited-v1` (cảnh báo 60 s) | `wp14-c1-budget120-v1` (trần 120 s) |
| đối chứng | `wp9-fleetpy-ridebound-hard-vector-audited-v1` | `wp14-c1-budget120-v1` (trần 120 s) |

Đối chứng đã niêm phong sẵn: `frontier-v1/fr-budget120-*` phục vụ 1 608 trên
2 160. Nên chỉ cần chạy mới 20 ô nhánh điều trị, cùng runner, cùng fixture,
cùng driver, cùng hạt giống 7.

### 3.3 Kết quả: trùng khớp từng quyết định, đủ 20 ô

Cả hai nhánh phục vụ **1 608 / 2 160**, giá lời hứa **−5,88 pp**, chênh **0 trên
mọi ô** — không một ô nào lệch dù một hành khách.

| Đại lượng so sánh | Đối chứng | Mức C |
|---|---:|---:|
| Khách được phục vụ | 1 608 | **1 608** |
| Lần công bố lời hứa | 47 118 | **47 118** |
| Lần công bố có dịch chuyển | 79 | **79** |
| Xáo trộn tuyến tính (s) | 5 063,3 | **5 063,3** |
| Căn bậc hai của bình phương (s) | 648,6 | **648,6** |
| Có trọng số bước (s) | 13 129,2 | **13 129,2** |
| Có trọng số kề cận (s) | 3 214,0 | **3 214,0** |
| Khách nhìn thấy (s) | 14 318,1 | **14 318,1** |
| Ngoại sinh (s) | 9 260,2 | **9 260,2** |
| Khách bị dịch nặng nhất (s) | 119,0 | **119,0** |
| Số khách bị dịch ít nhất 1 lần | 76 | **76** |

Phép so từng quyết định (`decision_identity.py`) trên đủ 20 ô:

| Đại lượng so sánh | Kết quả |
|---|---|
| Chuỗi (xe, ứng viên) được gán | **giống hệt 20/20** |
| Tập lời hứa công bố trong từng khung quyết định | **giống hệt 20/20** |
| Chuỗi mã lý do | **giống hệt 20/20** |

Bám ngữ nghĩa niêm phong của hai nhánh *có* khác nhau trên cả 20 ô, nhưng đó
**không** phải bằng chứng quyết định khác nhau: nhánh soft-hybrid ghi thêm chứng
cứ cảnh báo vào bằng chứng niêm phong và phát các lần công bố theo thứ tự khác
bên trong cùng một khung. Không có một quyết định nào đổi.

### 3.4 Tại sao: tầng cảnh báo bị đặt dưới một tầng mạnh hơn

Có hai kiểu "rỗng" rất khác nhau cho một tầng trong hàm mục tiêu từ điển:

- **(a)** giá trị của nó luôn bằng 0, tức ngưỡng chưa bao giờ bị chạm;
- **(b)** giá trị có biến thiên, nhưng một tầng cao hơn đã phân định xong mọi so
  sánh nên tầng dưới không bao giờ được lên tiếng.

Đọc `objectiveBounds` trong chứng cứ solver cho câu trả lời là **(b)**:

| Tầng mục tiêu | Số lần | Khác 0 | Tỉ lệ |
|---|---:|---:|---:|
| `accepted-request-count` | 4 264 | 519 | 12,2% |
| `operational-cost` | 4 264 | 4 240 | 99,4% |
| **`worst-hard-utilization-ppm`** | 4 240 | **4 240** | **100,00%** |
| `warning-excess:drop_eta_total_ms` | 4 240 | **810** | **19,1%** |
| 9 chiều cảnh báo còn lại | 4 240 | 0 | 0% |
| `revision:drop_eta_total_ms` | 4 240 | 21 | 0,5% |

Ngưỡng cảnh báo 60 giây **có** bị chạm, trong 19,1% quyết định. Nhưng tầng ngay
phía trên nó khác 0 trong **100%** quyết định. Tầng đó đo mức tiêu ngân sách tệ
nhất theo phần triệu — tức một thang **liên tục** của đúng cái mà ngưỡng cảnh
báo chia thành hai bậc. Đặt một tầng ngưỡng bên dưới một tầng liên tục cùng ý
nghĩa thì tầng ngưỡng thành dư.

Kết luận đáng ghi vào báo cáo: ý tưởng "đặt trước ngân sách" **không sai, mà đã
có sẵn trong hệ thống ở dạng mạnh hơn**. Cực tiểu hóa mức tiêu tệ nhất chính là
"tiêu dè dặt", và nó làm việc đó trên thang mịn hơn hẳn một ngưỡng 60 giây. Đối
chứng (đủ 20 ô) cũng cho `worst-hard-utilization-ppm` khác 0 trên 13 188/13 188
quyết định — cùng cấu trúc, chỉ thiếu mười tầng cảnh báo.

Hai cách để mức C có tác dụng thật, cả hai đều là thay đổi thiết kế chứ không
phải thay đổi cấu hình: đặt tầng cảnh báo **lên trên** `worst-hard-utilization`,
hoặc bỏ tầng liên tục ấy đi trong nhánh soft-hybrid. Cả hai đều làm hệ thống tệ
hơn theo thước đo hiện có, nên không đáng.

---

## 4. Trả lời gọn cho bảng câu hỏi mở

| Hạng mục | Kết luận | Căn cứ |
|---|---|---|
| Mức A — xếp hạng vị trí chèn | **Rỗng** | 96,0% quyết định có đúng 1 ứng viên |
| Mức B — cắt tỉa sớm | **Rỗng** | 0 bỏ sót, 0 nhánh chưa khai triển, 0 lần cạn ngân sách |
| Mức C — đặt trước ngân sách | **Rỗng theo nghĩa (b)** — ngưỡng có chạm (19,1%) nhưng tầng trên đã quyết xong 100% | trùng khớp từng quyết định với đối chứng |
| Mục 4 — bộ sinh sắp xếp lại | Đã có sẵn; hỏng 18/20 vì bất biến chặng đang chạy; cần sửa 3 chỗ trong mã nguồn | 245 lần sắp lại, 150 lần đẩy chặng đầu, 0 lần đóng băng sớm |

Một nhận xét đáng ghi vào báo cáo: cả bốn hạng mục đều bị loại hoặc bị giới hạn
**bởi chính các phép đo mà cơ chế lời hứa sinh ra**. Sổ cái cam kết ghi lại đủ
chi tiết để biết trước rằng việc sắp xếp lại không có chỗ để tác động, trước khi
bỏ ra ngày nào chạy benchmark. Đó cũng là một kiểu giá trị của cơ chế, dù không
phải kiểu được nêu trong phát biểu vấn đề.
