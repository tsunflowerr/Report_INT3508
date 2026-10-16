# Kết quả: quy trách và điểm hoà vốn của cam kết

Nguồn: 40 ô đã niêm phong `E:/RideBoundData/wp9/confirmatory-h6-panela-v2` (H6 Panel A, 2160 yêu cầu).
Không chạy mô phỏng mới. Chỉ đọc lại `transcript-00.ndjson`.
Kiểm tra toàn vẹn: cả 40/40 ô có số `promisePublished` khớp chính xác `publicationCount`
trong `run-00.json`, và số accepted/rejected khớp `run-00.json`.

Script: `extract_promise_movement.py` (bóc tách), `aggregate.py` (tổng hợp).

---

## 1. Bảng chính

| Đại lượng | B1 (không cam kết) | C1 (cam kết) | Chênh |
|---|---:|---:|---:|
| Hành khách được phục vụ | 1,735 | 1,581 | −154 |
| Tỉ lệ phục vụ | 80.3241% | 73.1944% | **−7.1296 pp** |
| Số lần công bố lời hứa | 54,311 | 45,542 | −8,769 |
| ETA khách **nhìn thấy** dịch chuyển — đón | 12,059 s | 2,510 s | −9,549 s |
| ETA khách **nhìn thấy** dịch chuyển — trả | 71,529 s | 6,822 s | −64,707 s |
| Phần **do nhà xe quyết định** — đón | 9,580 s | 0 s | −9,580 s |
| Phần **do nhà xe quyết định** — trả | 64,863 s | 128 s | −64,735 s |
| Phần **do trôi dạt vật lý** — đón | 2,483 s | 2,510 s | +26 s |
| Phần **do trôi dạt vật lý** — trả | 6,719 s | 6,695 s | −25 s |

### Trên mỗi hành khách được phục vụ

| | B1 | C1 |
|---|---:|---:|
| Tổng ETA dịch chuyển khách nhìn thấy | **48.18 s** | **5.91 s** |
| — do nhà xe | 42.91 s | 0.08 s |
| — do vật lý | 5.30 s | 5.82 s |

→ **Khách của hệ thống có cam kết chịu ít hơn ~8 lần lượng xáo trộn giờ đã báo.**

---

## 2. Phát hiện then chốt: QUY TRÁCH

Tỉ lệ lượng ETA dịch chuyển mà khách nhìn thấy là **do chính bộ điều phối gây ra**,
không phải do kẹt xe hay xe chạy chậm:

- **B1: 89.06%** (74,443 s trên tổng 83,587 s)
- **C1: 1.37%** (128 s trên tổng 9,332 s)

Đây là con số chưa từng có trong văn liệu. Nó nói rằng trong một hệ ride-pooling tối ưu liên tục
theo lối kinh điển, **gần chín phần mười sự bất định mà hành khách trải nghiệm là do hệ thống tự tạo ra**,
chứ không phải do thế giới vật lý.

Và vì cơ chế sinh phương án là chèn-thêm (insertion-only), đã kiểm chứng trước đó rằng
`decisionMovedEarlier = 0` trên 421,752 lần sửa — nên toàn bộ 74,443 s đó là **dịch chuyển theo hướng xấu đi**,
không có lần nào tốt lên.

### Nhóm chứng (control) tự nhiên

Phần trôi dạt vật lý gần như bằng nhau giữa hai nhánh (2,483 vs 2,510 s đón; 6,719 vs 6,695 s trả).
Thế giới vật lý cư xử như nhau ở cả hai nhánh; khác biệt nằm trọn ở **hành vi của bộ điều phối**.
Đây là bằng chứng thực nghiệm cho tính đúng đắn của phép phân rã ba mốc.

---

## 3. Ngân sách có thực sự bị tiêu không?

Mức tiêu ngân sách cao nhất từng ghi nhận trên một hành khách:

| Chiều | B1 | C1 | Trần C1 |
|---|---:|---:|---:|
| `dropEtaTotalMs` | 573,491 ms | 27,588 ms | 30,000 ms |
| `pickupEtaTotalMs` | 407,767 ms | 0 | không đặt trần |
| `materialEtaRevisionCount` | 3 | 1 | không đặt trần |
| `prePickupInsertedStopCount` | 3 | 1 | không đặt trần |

Hai điều quan trọng:

1. **Ngân sách 30 s là ràng buộc thật, không thừa.** C1 chạm tới 27,588 ms = 92% trần.
2. **Không cam kết thì mức xáo trộn có thể rất lớn.** Một hành khách trong B1 bị dời giờ trả
   tích luỹ tới **573 giây (~9.5 phút)** và giờ đón tới **408 giây (~6.8 phút)** — trong khi
   vẫn nằm trong cửa sổ Omega/Delta hợp lệ. Đây chính là minh hoạ cho W1: cửa sổ hợp lệ
   không hề bảo vệ lời đã nói.

---

## 4. Điểm hoà vốn

- Lượng thời gian bất ngờ mà cam kết **tránh được**: 74,255 s = **20.63 giờ**
- Số chuyến **phải hy sinh** để tránh được nó: **154**
- Tức là: **482 giây (~8 phút) thời gian bất ngờ tránh được cho mỗi chuyến bị hy sinh**

Một chuyến ghép phải đáng giá **hơn** ngần này thì nhánh không cam kết mới thắng về phúc lợi:

| Định giá thời gian bất ngờ | Giá trị hoà vốn của một chuyến |
|---|---:|
| 7.88 EUR/h (VOT trên xe, cận dưới) | 1.06 EUR |
| 10.80 EUR/h (VOT trên xe, cận trên) | 1.45 EUR |
| 15.00 EUR/h | 2.01 EUR |
| 20.00 EUR/h (chờ bất ngờ, cận dưới) | 2.68 EUR |
| 25.00 EUR/h (chờ bất ngờ, cận trên) | 3.35 EUR |

Nguồn hệ số: Alonso-González et al. 2020 (TR-C 115:102621) cho VOT trên xe của ride-pooling;
Geržinič, Cats & van Oort 2023 cho định giá thời gian chờ **bất ngờ**.

### Cách phát biểu trung thực

Đây là một **ngưỡng**, không phải một tuyên bố chiến thắng. Phát biểu đúng là:

> Với mức định giá thời gian bất ngờ đã công bố trong văn liệu (20–25 EUR/h), hệ thống có cam kết
> vượt hệ thống không cam kết về phúc lợi khi thặng dư của một chuyến ghép biên thấp hơn
> khoảng 2.7–3.4 EUR. Vì những chuyến bị từ chối là những chuyến khó phục vụ nhất, tức là
> gần điểm bàng quan nhất, thặng dư biên của chúng theo định nghĩa là nhỏ.

Đây chính là "thua một chút nhưng đánh đổi tốt hơn" — và nó là một con số kiểm chứng được.

---

## 5. Cảnh báo diễn giải (phải ghi vào báo cáo)

1. Đại lượng đo là **tổng dịch chuyển tích luỹ** của giờ đã báo, không phải sai số cuối cùng.
   Một khách bị dời +10 s rồi −10 s được tính 20 s. Đây đúng là cái mà văn liệu nervousness đo
   (bất ổn của kế hoạch), nhưng phải gọi đúng tên: **độ xáo trộn của lời hứa**, không phải **độ trễ**.
2. Trôi dạt vật lý **trên mỗi khách** ở C1 nhỉnh hơn B1 (5.82 vs 5.30 s), vì C1 phục vụ ít khách hơn
   trong khi tổng trôi dạt gần như không đổi. Không ảnh hưởng kết luận nhưng phải nói ra.
3. Phép tính hoà vốn giả định mỗi chuyến bị mất có cùng một giá trị thặng dư. Đó là đơn giản hoá.
4. B1 đã khoá danh tính xe. Nên 89.06% là phần do **đổi lịch**, chưa tính phần do **đổi xe**
   mà một hệ thống cho phép reassignment sẽ còn cộng thêm.
