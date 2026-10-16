# Rà soát hoàn tất chương phương pháp

Ngày kiểm: 2026-10-04. Phạm vi biên tập: chỉ `source/noi-dung/07-chuong3.tex`.
Bản gốc tại `E:/Code/Report_INT3508/ridebound/noi-dung/07-chuong3.tex` được giữ nguyên.
Không chạy thí nghiệm, xây lại runner, sửa mã RideBound hoặc thay chứng cứ niêm phong.

## Hướng dẫn áp dụng

Đã đọc `nature-polishing/SKILL.md`, manifest và các lớp lõi được manifest yêu cầu,
cùng các mảnh `algorithmic`, `methods`, `generic`. Đã đọc các tài liệu chia sẻ
`main-text-discipline.md` và `consistency-sweep.md`. Đích là luận văn tiếng Việt;
không áp giới hạn hoặc chính sách xuất bản riêng của tạp chí Nature.

Các tệp hướng dẫn nằm dưới
`E:/Code/Report_INT3508/ridebound-scratchpad/nature-skills-audit-2026-10-04/skills`.

| Thuật ngữ cố định | Nghĩa sử dụng |
|---|---|
| phương án giữ tuyến / no-op | Kế hoạch hiện tại được chiếu lại trên cùng trạng thái. |
| cơ sở hành vi | Cộng độ dời đối xứng `A=abs(p-e)`. |
| cơ sở kết quả | Cộng độ dời đối xứng `B=abs(p-v)`. |
| phần thay đổi khi giữ tuyến | `d=abs(e-v)`, có thể gồm nhiều nguồn và phụ thuộc quỹ đạo. |
| miễn trừ | Vi phạm vẫn được ghi nhận, không tính thành vận hành bình thường. |
| chứng nhận | Chứng cứ kiểm quyết định trong phạm vi phiên bản và cấu hình. |

Đã bỏ việc dùng đồng thời `v` cho xe và cho lời hứa trước trong đoạn định nghĩa ba mốc.

## Nguồn mã và tài liệu thực tế đã đối chiếu

Nguồn C# hiện đọc được là `C:/Code/RideBound-noworse`, nhánh
`research/tier3-no-worse`, HEAD
`24aa747147d49db79675d170829e6f3bf3afc3cc`. Đây là kiểm source đọc được;
không tự suy ra mọi phiên bản runner trong các đợt thực nghiệm giống nhau.

| Đường dẫn dưới nguồn C# | Điều được kiểm |
|---|---|
| `src/RideBound.Application/Promises/PromiseDeltaCalculator.cs` | Ba cặp đối chiếu previous/exogenous, exogenous/proposed, previous/proposed; ETA dùng trị tuyệt đối; đếm cặp token điểm dừng cũ bị đảo thứ tự. |
| `src/RideBound.Domain/Commitments/CommitmentBudgetEvaluator.cs` | `before.Add(delta)`; kiểm từng hard limit đang áp dụng theo pha; vi phạm khi `after > limit`. |
| `src/RideBound.Application/Commitments/CommitmentDecisionValidator.cs` | Dựng lại tuyến giữ nguyên sau sự kiện; `KeptRouteReference`; `NoWorseReference` chỉ miễn trừ cùng cận deadline hoặc cùng chiều ngân sách, với phương án mới không tệ hơn tham chiếu. |
| `src/RideBound.Algorithms/Commitments/HardVectorCandidateAssessor.cs` | Phục hồi safety no-op; phương án đổi tuyến được kiểm lại; trong phục hồi no-worse, chỉ chiều vượt trần của khách được miễn trừ bị bỏ khỏi xếp hạng utilization. |
| `src/RideBound.Algorithms/Candidates/InsertionCandidateGenerator.cs` | No-op bị kiểm và lỗi nếu không giữ được safety candidate; việc có ứng viên no-op không đồng nghĩa khả thi vô điều kiện. |
| `src/RideBound.Algorithms/Candidates/CandidatePortfolioRetainer.cs` | Giữ đúng một no-op trong danh mục và khi áp giới hạn giữ lại. |
| `src/RideBound.Algorithms/Candidates/ForwardSlackProfile.cs` | Cận độ trễ bảo thủ là điều kiện đủ cho tuyến và lịch đón cố định; vượt cận chưa chứng minh bất khả thi. |

Đã đọc thêm bản tương ứng của `PromiseDeltaCalculator`, `CommitmentBudgetEvaluator`,
`CandidatePortfolioRetainer`, `CandidateFleetSelector` và `ForwardSlackProfile` tại
`E:/Code/RideBound`. Các tệp này hỗ trợ đối chiếu cơ chế lõi; bản checkout đó không
chứa phần no-worse, nên không dùng nó để xác nhận phần phục hồi.

Adapter được đối chiếu ở
`E:/Code/RideBound-deadline/simulators/fleetpy-ridebound/ridebound_fleetpy/runner_client.py`:
gọi tiến trình NDJSON, băm artifact, thương lượng capability và dùng ACK theo thứ tự.
Không cài lại sổ cái hay bộ điều phối trong adapter Python.

Tài liệu RideBound đã đối chiếu cho phạm vi này: `docs/00-index.md`,
`docs/01-research-charter.md`, phần trạng thái hiện hành của
`docs/18-status-and-decision-log.md`, work package WP14R trong
`docs/16-roadmap-and-work-packages.md` và
`docs/tasks/46-wp14r-resilient-execution-ticket-plan.md`, cùng các tài liệu
`docs/03-related-work-and-claim-boundary.md`,
`docs/07-commitment-ledger-and-certificates.md`,
`docs/08-algorithms-baselines-and-solver.md`.

Trong bản luận văn đã đối chiếu toàn bộ chương 3 hiện tại, phần định lý và bảng (H) của
chương 3 gốc, ba câu hỏi ở chương 1 mới, các label chương 4 mới và các tóm lược
`audit/h6-frontier-recheck.json`, `audit/tier2-recomputed-report.txt`.
Việc kiểm đếm và tái dựng raw evidence thuộc audit thực nghiệm của nhóm;
không nhận lại các kết quả đó như phép chạy do rà soát phương pháp tạo ra.

## Phát hiện và chỉnh sửa

1. **Không rỗng có điều kiện.** Đưa (B) và (N) lên trước định lý đầu. (B) là ngân sách
   trước quyết định còn hợp lệ; trần cố định và lịch sử không miễn trừ duy trì điều kiện
   này. Một trần vừa áp dụng do đổi pha hoặc sổ cái đã vượt sau miễn trừ cần kiểm lại.
   (N) là phương án giữ tuyến qua các kiểm tra khác. Kết luận không bảo đảm hệ thống
   luôn chạy trọn, không bảo đảm ETA thực tế và không bao phủ cổng khác nếu điều kiện
   của cổng đó chưa được kiểm.
2. **Chứng minh tồn tại.** Đổi chứng minh cơ sở kết quả có thể vô nghiệm từ mệnh đề
   “nếu tất cả bị loại thì tập rỗng” thành một trạng thái dựng: chỉ một no-op, ngân sách
   trước bằng 0, trần 30 giây và độ dời giữ tuyến 40 giây, với cửa sổ vật lý đủ rộng.
3. **Bao hàm quỹ đạo.** (H) phải đúng tại mọi lần công bố của mọi quỹ đạo khả thi dưới
   cơ sở kết quả. Hai sổ cái được ghi trên chính một quỹ đạo, cùng quy tắc chuyển trạng
   thái. Cực đại phục vụ trên cả chân trời không phải kết quả của bộ chọn từng kỷ nguyên.
   Giữ phản ví dụ `v=600,e=720,p=600`; không tuyên bố ưu thế tối ưu phổ quát.
4. **Hai kiểm tra khác nhau.** `B < A+d` không kéo theo `A>B`. Việc tập strict triangle
   và tập vi phạm (H) trùng nhau trong một bảng gốc, nếu được kiểm từ raw data, vẫn chỉ
   là sự trùng nhau thực nghiệm. Đã bỏ cách diễn giải tương đương tất yếu. Không gán lại
   các số 228 và 3 thành kiểm (H) khi audit hiện chỉ xác nhận strict triangle.
5. **Phân rã và nhân quả.** Đồng nhất có dấu `z=x+c` luôn đúng; chỉ có `V<=C+X` sau trị
   tuyệt đối. Phần giữ tuyến gồm nhiều nguồn, có thể phụ thuộc lịch sử chính sách.
   Tử số `C` không phải tác động nhân quả tổng thể hoặc một phần của phân rã cộng tính
   chính xác trên mọi bản ghi.
6. **Cổng và bộ sinh.** Thứ tự ngưỡng được nói trên cùng quỹ đạo giữ tuyến, từ sổ cái
   khởi tạo bằng 0 và chuỗi liên tục. Thời gian đi tất định chưa đủ cho `x=0` nếu phép
   chiếu và tiến độ không nhất quán. Loại no-op chưa đủ chứng minh toàn bộ tập toán học
   rỗng. Không suy `c>=0` phổ quát chỉ từ thao tác chèn hoặc số lần sớm hơn bằng 0.
7. **Phục hồi và biên.** Không nhận tính mới cho nguyên tắc no-worse. Miễn trừ vẫn là
   vi phạm. Giữ giới hạn của `validationWorkUnits`. Biên `beta+gamma` điều kiện trên
   `max_r X_r<=gamma`; hiệu chỉnh thứ tự xử lý cả điểm vô hạn và `k>n`. Không nhận độ
   phủ phân phối tự do hay độc lập giữa các ô T38.
8. **Văn phong và trình bày.** Sửa nghĩa đối xứng trong hai định nghĩa; đổi “trừ ngân
   sách” thành ghi thêm vào sổ; bỏ cách nói phỏng đoán sở thích hành khách; giảm lặp số
   thống kê trong chương phương pháp. Bảng bốn họ dùng `tabularx` theo bề rộng dòng.

## Kiểm tra tĩnh sau chỉnh sửa

- Đã đọc lại toàn bộ chương 3 sau các chỉnh sửa nội dung.
- Không thiếu label tham chiếu từ chương 3 trên toàn cây `source`.
- Không thiếu khóa tài liệu tham khảo của chương 3.
- Môi trường LaTeX đóng mở đúng, dấu ngoặc nhọn cân bằng.
- Hình `source/hinh/co-che-ba-moc.pdf` tồn tại; caption nói rõ ví dụ dựng.
- Đã đổi tham chiếu cũ tới `muc:trongdiem` và `muc:biendukien-t38` theo chương 4 mới.
- Tệp chương 3 chuẩn hóa UTF-8 không BOM, kết thúc dòng LF.
- Bản gốc có 41.984 ký tự và 8.280 đơn vị tách bởi khoảng trắng; bản cuối chương 3
  có 32.393 ký tự và 6.407 đơn vị. Đây là thống kê văn bản nguồn, không phải đếm từ
  ngôn ngữ học hoặc số trang PDF.

Không thay mã RideBound nên không phát sinh baseline `dotnet test RideBound.slnx` cho
phần việc này. Kiểm biên dịch, phân trang và nhìn toàn bộ PDF thuộc bước đóng gói chung
sau khi mọi chương hoàn tất; các kiểm tra tĩnh trên không thay thế bước đó.
