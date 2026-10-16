# Hướng mở rộng sau đối chiếu Claude — 20/09/2026

## Kết luận và mức độ bằng chứng

Còn hướng đáng làm. Hướng được phát triển trong vòng này là **đồng tối ưu tuyến và thời điểm/độ chính xác của lời hứa, với hạn chót cung cấp thông tin chính xác đã cam kết từ đầu**. Tên mô tả tiếng Anh: *precision-deadline constrained dispatch*. Đây là đề xuất nghiên cứu cụ thể, chưa xác nhận là mới toàn cầu, chưa có uplift closed-loop. Không đề nghị đổi tên interval hoặc count budget rồi nhận là thuật toán mới.

Tín hiệu mới: qua core E1 gốc, 3/16 rejected states có một candidate giữ conservative leading block, qua toàn bộ các ràng buộc cũ còn lại khi bỏ riêng drop cumulative budget, và nằm trong khoảng drop ban đầu giả định rộng 300s trước hạn phải thu hẹp. Đây là cơ hội hẹp nhưng tích cực, khác với 0/16 của các phép sửa tuyến giữ nguyên hợp đồng. Không được cộng chúng thành 3 khách hoàn thành thêm.

## 1. Đánh giá các lập luận trong bản Claude

Đã đọc nội dung file người dùng gửi: `C:/Users/quang/.codex/attachments/1e4bc3f2-053b-40cc-9b77-6943803b0eda/Pasted text.txt`.

| Nội dung | Đánh giá độc lập |
|---|---|
| Thiết kế lại nội dung/thời điểm lời hứa | Đáng theo đuổi; chuyển biến quyết định từ chỉ chọn tuyến sang chọn cả hợp đồng thông tin. |
| Khoảng lồng nhau chưa ai làm | Chưa chứng minh; tìm được Woop có slot refinement nằm trong khoảng cũ và tác động tới optimization. Không nhận nesting làm novelty. |
| Chưa ai buộc dispatcher tôn trọng khoảng đã hiển thị | Quá rộng, ngay bảng của Claude đã có choice-driven DARP khóa cửa sổ accepted. Cần so đúng thuật toán và semantics cụ thể. |
| w=0 cho lại RideBound hiện tại | Sai: singleton cố định cấm mọi ETA change, còn budget30 có thể cho phép 10s. Cần một tham số cumulative budget riêng để biểu diễn cơ chế cũ. |
| w=l cho lại Schulz; w=Ω cho lại B1 | Không tự đúng: khác hai phía/một phía, pickup/drop, thời điểm anchor, luật publication, generator và objectives. |
| w lớn hơn sample maximum bảo đảm khả thi mọi epoch | Sai: maximum quan sát không phải bound hỗ trợ tương lai; containment không chứng minh tồn tại cùng một kế hoạch vật lý thỏa tất cả hành khách. |
| Nesting cho visible change bằng0 | Chỉ bảo đảm không rút lại phần đã loại và không mở rộng set. Khách vẫn phải cập nhật kế hoạch khi khoảng thu hẹp; point forecast nếu tiếp tục hiển thị vẫn có thể đổi. Không đồng nhất set consistency với zero inconvenience. |
| Superset feasible suy ra frontier trội online | Sai nếu thiếu policy/compute/trajectory coupling. Lựa chọn trước làm đổi state sau. |
| 96% vehicle epochs no-op chứng minh selection vô dụng | Mẫu số chứa rất nhiều epoch không có pending. Audit E1 thấy 1.045/1.571 active acceptance epochs của C1 có nhiều phương án cùng acceptance. Không gọi là định lý thực nghiệm toàn cục. |
| Repair và origin hold chưa kiểm tra đủ | Nghiên cứu tiếp nối đã bổ sung all-order + waiting audit có phạm vi rõ; không nên chạy lại cùng hướng chỉ vì bản Claude cũ chưa có kết quả ấy. |
| Hứa một phần khách | Đã va trực tiếp shareability shadows2026. Có thể là comparator, không đủ thành hướng chính. |
| +7,1pp ở bài khác có thể bù -7,13pp RideBound | Không suy ra được. Khác instances, fleet, information và constraints; biết tương lai thật còn khác forecasting. |
| Optimal allocation cùng tổng quỹ chứng minh hiệu quả online | Đó là upper-bound kiểu hậu nghiệm nếu dùng toàn bộ realized demands/revisions, không phải thuật toán online khả dụng. |

Các phép đo Đ1–Đ4 của Claude không kèm script/hash/raw mapping trong tệp gửi. Vòng này không nhận các số đó là đã tái lập, không dùng chúng làm kết quả mới của mình.

## 2. Nguồn kiểm tra bổ sung

1. **Woop, Slot Refinement**, nguồn sản phẩm trực tiếp: https://help.woopit.fr/hc/en-gb/articles/39780510706449-Slot-Refinement . Trang mô tả thu hẹp một lần theo giờ đặt trước, refined slot phải nằm trong initial slot. Reoptimization sau đó có thể làm mission unplanned; các mission đã refine được ưu tiên giữ. Đây không phải một chứng minh hard guarantee online, nhưng đủ bác việc tự nhận toàn bộ ý tưởng nested refinement là chưa từng có. Phần thông báo khách trên trang còn ghi đang phát triển.
2. **Hosseini–Rostami–Araghi, Service Time Window Design in Last-Mile Delivery**: https://arxiv.org/html/2508.01032v1 . Đối chiếu trang8–9 của PDF local và HTML phần mô hình: thiết kế width/reliability cho route và integrated routing. Không nhận joint route-window optimization nói chung là mới. Chưa đọc hết47trang trong vòng này; không backfill coverage.
3. **Oracle Communicated Windows**: https://docs.oracle.com/en/cloud/saas/field-service/fawmt/overview-communicated-windows.html . Đây là lưu/pin thông tin đã nói với khách, không có đủ bằng chứng trên trang rằng một hard dispatch gate được áp dụng. Không nhầm việc giữ nguyên hiển thị với bảo đảm thực hiện.
4. **Schmidt et al., TSP-SC**: https://arxiv.org/abs/2609.11950 . Abstract chính chủ xác nhận cơ chế cam kết arrival trước demand acceptance rồi chọn subset được phục vụ; vòng này mới kiểm metadata/abstract, chưa audit toàn văn. Khác yêu cầu giữ phục vụ tất cả khách đã accepted của đề xuất.
5. Các đối chứng đã đọc trước: Schulz–Pfeiffer2026, Ackermann–Rieck2025, choice-driven DARP2022, shareability shadows2026. Không có một “đối thủ duy nhất”: mỗi bài chặn một phần novelty khác nhau.

## 3. Hợp đồng đề xuất: chính xác đến mức nào, và biết trước lúc nào

Bản đầu chỉ đổi **drop-time promise**. Giữ pickup ETA lock, xe, điểm đón/trả, physical constraints và execution prefix. Điều này tách riêng giá trị của thiết kế lời hứa drop, tránh đồng thời nới nhiều cơ chế.

Khi accepted ở thời điểm t0, công bố:

- Khoảng ban đầu I0=[L0,U0], độ rộng không vượt W0.
- Hạn chót tau=L0-h, với h là thời gian báo trước tối thiểu.
- Chậm nhất tau, khoảng phải được thu hẹp xuống không quá Wf, luôn nằm trong I0 và mọi khoảng đã công bố trước đó.
- Không hủy khách đã accepted để cứu precision target; muốn nhận thêm khách phải có một route hoàn tất mọi khách cũ vẫn hợp lệ.

Ví dụ minh họa sản phẩm: “Đến trong 10:20–10:25; trước10:17 sẽ báo một khoảng rộng tối đa1phút, nằm trong khoảng này.” Đây không phải thông số đã hiệu chuẩn cho người dùng thật.

Hạn tau neo vào **L0 lúc accepted**, không tính lại từ ETA hiện tại. Nếu tính lại từ ETA, dispatcher có thể đẩy khách trễ để trì hoãn nghĩa vụ báo rõ. Nếu tau đã tới ngay lúc booking, phải phát khoảng hẹp ngay hoặc không chào loại hợp đồng đó.

Phần đánh đổi: thông tin ban đầu kém chính xác hơn, có thể ETA thực muộn hơn dù vẫn trong khoảng, cần thêm timer/validation/state. Lợi ích nhắm tới: giữ cơ hội ghép chuyến sớm, nhưng vẫn có độ chính xác và thời gian báo trước hữu hạn cho mọi khách được nhận. Không lấy zero revisions của UI làm chỉ tiêu thắng.

## 4. Thuật toán cụ thể

State bổ sung per rider: I_current, I_initial, tau bất biến, precision stage, complete publication history. Lưu ETA nội bộ tách khỏi contract hiển thị. Giữ lịch sử delta cũ để đo; không reset để xóa burden quá khứ.

Tại event thông thường:

1. Core gốc sinh candidate với active leg/prefix đúng.
2. Validate vật lý và các hard commitments còn giữ nguyên.
3. Kiểm các drop schedules nằm trong I_current; không cho nới I để làm candidate đang trượt trở thành hợp lệ.
4. Chọn fleet assignment không nhận trùng request. Khi cùng acceptance, có thể dùng khả năng còn nhận các demand types lịch sử; phải đếm một type một lần, không đếm nhiều candidate trùng như nhiều cơ hội.
5. Giữ lại kế hoạch hoàn tất đã được validate làm fallback. New request chỉ được nhận nếu plan mới cũng hoàn tất mọi incumbent.

Tại timer tau, xử lý **trước** admission cùng timestamp:

1. Chọn route/fleet plan qua validator, gắn với cùng trạng thái execution hiện tại.
2. Cho một rider đang cần refine và fallback arrival band [a,b], chọn I'=[x,x+w] nằm trong I_current, chứa [a,b], w≤Wf.
3. Trong các vị trí x hợp lệ, có thể chọn vị trí giữ nhiều demand scenarios khả thi nhất, từ các option đã core sinh hợp lệ và thông tin có trước timer. Nếu không có mô hình nhu cầu đáng tin, dùng deterministic placement baseline; không bịa probabilities.
4. Với nhiều rider, phải đánh giá **cùng một kế hoạch chung**. Không ghép các cửa sổ từ những plan khác nhau rồi kết luận toàn fleet feasible. Bản rẻ có thể refine lần lượt, mỗi bước giữ một fallback chung và lọc/revalidate pool. Bản đắt giải joint candidate/window selection.
5. Validate xong mới publish và thu hẹp gate. Nếu forecast thay đổi ngoài mô hình, phát incident/breach thật; không mở rộng âm thầm.

Timer bắt buộc là phần của event stream, cần checkpoint/retry/idempotency và atomic publication với plan. Vì vậy triển khai đầy đủ không phải thêm1 config/115dòng evaluator như bản Claude dự đoán.

### Bài toán con chính xác, đã có prototype

Với I=[L,U], fallback [a,b] và width w, tập left endpoints hợp lệ là:

`x in [max(L,b-w), min(a,U-w)]`.

Nếu [a,b] nằm trong I và b-a≤w≤U-L, tập này khác rỗng. Trong mô hình deterministic, fallback là điểm p nên luôn có thể thu hẹp quanh p, với điều kiện route đó thật sự khả thi. Với uncertainty band rộng hơn Wf, không được nhận rằng bước refine được bảo đảm.

Mỗi scenario có nhiều candidate ETA t. Một ETA được giữ khi `x in [t-w,t]`. Quét các endpoint của những đoạn này, giữ số lượng active theo scenario/color và cộng weight mỗi scenario đúng một lần. Tìm interval tối đa hóa retained scenario coverage trong O(M log M), bộ nhớ O(M), với M ETA options được cung cấp. Closed endpoints phải cộng entry trước khi tính score rồi mới remove exit.

Đây là thuật toán sweep-line chuẩn áp dụng cho bài toán con, **không nhận riêng primitive này là novelty**. Nó tối ưu score trên supplied options cho một tọa độ/fallback cố định, không tối ưu tương lai toàn hệ thống. Joint multi-rider placement cần bài toán khác.

`interval_refinement_math.py` đã đối chiếu1.000 trường hợp nguyên nhỏ với brute-force mọi endpoint hợp lệ; pass. Có case nhiều candidate cùng scenario không bị đếm thừa và case fallback quá rộng bị từ chối đúng. Các case này chỉ kiểm toán học của refinement, không thay cho test Runner.

### Bảo đảm có thể chứng minh trong mô hình xác định

Giả sử static travel đúng, thực thi theo kế hoạch, timer đúng hạn, trạng thái vật lý được cập nhật nhất quán, và từ đầu có complete feasible fallback. Nếu mỗi admission giữ một complete plan trong các interval và mỗi refinement giữ arrival của chính plan đó, thì bằng quy nạp hệ thống còn fallback cho khách đã nhận. Khách mới có thể bị từ chối; không có bảo đảm acceptance lớn hơn baseline.

Nesting + tau=L0-h cho refinement trước mọi realized arrival thuộc I0 ít nhất h, **nếu** timer thực sự chạy đúng hạn và containment được thực hiện. Đây là kết luận có điều kiện, không phải bảo đảm chịu được mọi traffic shock.

Không chứng minh được các bảo đảm nói trên chỉ từ việc current point ETA nằm trong interval hoặc sample maximum nhỏ hơn half-width.

## 5. Phép thử mới qua đúng core E1

Code: `interval-deadline-probe/Program.cs`; protocol: `interval-deadline-probe/PROTOCOL.md`.
Inputs: 16 rejected states đã capture; DLL E1 gốc. Toàn bộ16 control/count/state hashes khớp all-order audit trước. 4.153 route,9 physical-pass,0 old-contract acceptance như cũ.

Hypothetical initial drop interval: firstPublishedDrop ±150s, total width300s; deadline=lower-180s. Gỡ riêng hardLimit drop_eta_total_ms trong một policy catalog ngoài repo để core kiểm **toàn bộ ràng buộc còn lại**. Không sửa ledger input. Sau đó kiểm initial interval containment, thời điểm trước deadline và historical publications trên xe đang sửa. Conservative head screen vẫn bắt buộc.

| Epoch | Decision-induced drop delay | Còn trước precision deadline | Cơ hội qua các điều kiện trên |
|---|---:|---:|---|
|304|86,142s|717,070s|Có|
|374|123,060s|535,306s|Có|
|394|71,785s|73,384s|Có|

Cả ba rider bị tác động đều waitingPickup, pickup lock vẫn giữ. Các candidate khác còn vướng pickup lock, execution-head screen hoặc interval width. Không cộng các witness trùng thành nhiều khách.

**Giới hạn bắt buộc:** đây là ba single-state opportunities trên factual C1 trajectories. Chưa thực thi new contract từ booking, chưa chạy timer/refinement60s, chưa kiểm historical compliance toàn fleet theo new contract, chưa đo completion/service uplift, chưa có uncertainty model. Nới budget đơn thuần cũng mở được các early candidates; chưa chứng minh thuật toán tốt hơn budget relaxation. W0/h là lựa chọn exploratory cho cơ chế, không phải optimal/calibrated parameters; không dùng chúng làm preregistered H7 levels.

Receipt: `interval-deadline-probe-receipt.json`; raw output: `interval-deadline-opportunities.json`. Receipt có SHA-256 code/output và các DLL.

## 6. Thiết kế thí nghiệm tiếp theo để phân biệt có ích với đổi tên

So paired development cells mới, cùng generator, travel, fleet, physical constraints và compute budget:

- C1 hiện tại.
- Nới cumulative drop budget, giữ contracts point như cũ.
- Fixed initial drop window không refine: mua service bằng bất định kéo dài.
- Staged windows + fixed placement, cùng W0/Wf/h.
- Staged windows + option-preserving refinement, cùng W0/Wf/h và compute.
- Delayed precise promise theo phase làm comparator; giữ full history, không xóa số liệu trước commit.

Đo served/accepted, physical wait/detour, distribution per rider, deadline misses, interval violations, actual refinement lead time, width theo thời gian và uncertainty area `integral width(t) dt`, runtime p95/p99. Report internal ETA revisions kể cả khi UI không publish. Thêm uncertainty-aware tests trước khi nói về actual-arrival guarantee.

Điều kiện để ưu tiên triển khai lớn: staged policy tạo service–information tradeoff tốt hơn các baseline trên dữ liệu phát triển mới, với0 avoidable contract breaches. Nếu option-preserving refinement không thắng fixed placement thì bỏ phần phức tạp ấy, không nhận nó là đóng góp. Nếu kết quả chỉ bằng nới budget và chỉ giảm số lần hiển thị, không đủ đáp ứng mục tiêu nghiên cứu.

## 7. Hướng phụ và quyết định hiện tại

- H2 cam kết muộn: giữ làm comparator và thành phần của main mechanism, không nhận lần đầu đặt câu hỏi thời điểm commitment.
- H3 immediate repair giữ nguyên contracts: bằng chứng âm bounded vẫn còn; không ưu tiên chạy lại cùng route family.
- H4 origin hold: có thể hữu ích trong advance-booking windows mới, nhưng không cứu16 state đã audit; không “miễn phí” vì tăng wait/mất cơ hội xe.
- H5 partial guarantee: phải so trực tiếp shareability shadows; chưa ưu tiên làm contribution chính.

Ưu tiên hiện tại là **một hợp đồng thông tin có hạn chót, kèm thuật toán giữ feasible fallback và chọn vị trí thu hẹp**. Có tính khả thi cục bộ được core hỗ trợ và bài toán con đã kiểm, nhưng tính mới học thuật và giá trị closed-loop còn mở. Mọi artifact ở scratchpad ngoài repo; không thay baseline/claims/status của RideBound. Đây là nghiên cứu exploratory theo yêu cầu mới của người dùng, không tự mở WP15/H7 chính thức.
