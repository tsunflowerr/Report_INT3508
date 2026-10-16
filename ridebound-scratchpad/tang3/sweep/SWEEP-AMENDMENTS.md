# Sửa đổi của quét C/M⁺ sau khi niêm phong

`SWEEP-PLAN.md` được niêm phong lúc 2026-09-25T09:33:58Z (SHA-256 `756b65fd…423f`). Mọi mục dưới đây viết **sau**
thời điểm đó, và **không** thay thước đo, dự đoán hay ma trận đã niêm phong.

## A1 — 2026-09-25, khi quét đã chạy xong 108/156 job: kích hoạt luật phục hồi (b) cho các nhánh `M⁺` bị ép

- **Căn cứ trong kế hoạch.** §7 ghi: luật phục hồi (b) chỉ cài nếu "(a) quyết định kết quả".
- **Cách cụ thể hóa**, viết sau niêm phong và chỉ để quyết định có làm (b) hay không, không dùng làm điểm cuối: ở một
  mức x, `M⁺-x` có phục hồi forced **và** tập khách hoàn tất của `M⁺-x` khác của `C-x` trong cùng (thế giới, ô). Khi
  đó luật (a) có thể là nguyên nhân gây chênh lệch.
- **Quan sát đã có** (`sweep_analyze.py` trên W0–W3):
  - W2 sáng: `M⁺` có 366–419 breach forced ở x ≤ 120, và phục vụ 83 khách so với 85 của `C`.
  - W2 tối: `M⁺` có 492–527 breach forced ở x ≤ 120, và phục vụ 77 khách so với 79 của `C`.
  - Tiêu chí được thỏa ở W2.
  - W1 sáng có forced nhưng tập khách trùng; W1 tối có forced và tập khác, nhưng ở đó `M⁺` phục vụ **nhiều hơn**.
- **Việc sẽ làm:**
  1. Cài (b) "không tệ hơn tham chiếu" sau một khóa tùy chọn mới, mặc định giữ (a); kèm ADR, test và review độc lập.
  2. Publish Runner mới.
  3. Chạy lại **mọi** nhánh `Mplus-x` có forced > 0 trong quét, cùng ma trận và cùng thế giới.
  4. Chạy **đối chứng**: một số nhánh `C-x` và `Mplus-x` không có forced, chạy bằng Runner mới. Chúng phải cho quyết
     định giống hệt bản quét, vì (b) chỉ đổi hành vi khi có xe bị ép, và `C` không bao giờ bị ép (Định lý 4).
  5. Báo **cả hai** kết quả, (a) và (b). Không bỏ kết quả (a).
- **Build và test .NET làm sau khi quét xong**, để không tranh CPU với các job đang chạy: runner client có timeout 60 s
  cho mỗi phản hồi.

### A1 (tiếp) — 2026-09-26: (b) đã cài, review và publish

- **Code:** ADR-077, commit `45f8026` trên nhánh `research/tier3-no-worse`, đã push.
  - Worktree riêng `C:\Code\RideBound-noworse`, **không** phải worktree mà quét dùng.
  - .NET 1025/1025. Review độc lập 2 vòng, không blocker.
- **Runner v2:** `C:\RideBoundData\research\runner-tier3-v2`, publish từ `45f8026` với cây sạch. Manifest
  `../runner-tier3-v2.sha256.tsv`: tree `ac251ef3…cff3f`, 429 file.
- **WP4 v2:** `../configs/wp4-tier3-v2.json`. Chỉ khác v1 ở `commitmentRecovery`, theo `make_wp4_v2.log`.
- **Job:** `run_noworse.py`, gồm 22 nhánh điều trị và 6 đối chứng.
  - Điều trị là mọi `Mplus-x` có forced > 0 trong `sweep-jobs-2026-09-26.tsv`.
  - Output để ở ổ C, vì ổ E còn khoảng 42 GB, sát mức tối thiểu 40 GB.
  - Adapter và preflight vẫn chạy từ worktree quét cũ, không bị sửa.

### A1 (kết quả) — 2026-09-26: 28/28 job pass

- **Hợp lệ:** 28/28 `status: pass`, audit v/e/p đúng (`logs/noworse-analyze-2026-09-26.txt`).
- **Đối chứng:** 6/6 có chuỗi hành động đội xe giống hệt bản (a).
- **Runner v2 nhận quyết định `forcedNoWorse` từ đầu đến cuối:** 49 quyết định, 50 breach `forcedNoWorse`; 5155 breach
  còn lại vẫn là `forcedReference`.
- **Điều trị:** tổng khách phục vụ (b) 1874, (a) 1864, `C` 1873. (b) bằng `C` về số khách ở 21/22 job và cùng hành
  động ở 19/22.
- **Lời hứa `M⁺` bị phá gần như không đổi,** (b) 12,2% so với (a) 12,3%, trung bình trên 22 job.
- **Chi tiết và diễn giải:** `SWEEP-REPORT.md` §7 (`logs/noworse-aggregate-2026-09-26.txt`, `noworse_aggregate.py`).
- **Cả hai kết quả (a) và (b) đều được giữ và báo cáo.**

## A2 — 2026-09-25 23:17 (giờ máy): sự cố do tôi gây ra, job hỏng vì cây nguồn đổi giữa chừng

- **Chuyện gì xảy ra.**
  - Khoảng 23:03–23:16 tôi viết code cho (b) **ngay trong worktree mà quét đang dùng**
    (`E:\Code\RideBound-deadline`): 8 tệp trong `src/`, 5 tệp trong `tests/`.
  - Preflight medium băm cây nguồn Git-visible lúc đầu và lúc cuối mỗi job.
  - Các job chạy qua lúc tôi sửa kết thúc với `RuntimeError: repository content inventory drifted during the matrix
    run` (`actual_fleetpy_medium_preflight.py:881`). Chúng có thư mục output nhưng không có `summary.json`
    (`exists-no-summary`).
  - 6 job đầu tiên: `Mplus-60`, `C-120`, `Mplus-120`, `C-300`, `Mplus-300`, `C-600`, cùng ở
    W4-`d20181112-s10-r1-w08`. Các job đang chạy lúc đó cũng sẽ hỏng; danh sách đầy đủ ghi khi quét xong.
- **Không ảnh hưởng tới hành vi của các job khác.**
  - Runner là bản đã publish (`runner-tier3-v1`), không build lại từ nguồn.
  - Code adapter và preflight trong `simulators/` không bị sửa.
  - Chỉ phép kiểm cây nguồn phát hiện thay đổi và làm job dừng.
- **Đã làm lúc 23:17:**
  1. Lưu phần sửa thành patch `no-worse-v1-worktree-edits.patch` (67.705 byte).
  2. Ghi lại **đúng byte** của commit `1ce15e9` cho 13 tệp (`git cat-file blob`).
  3. Kiểm lại bằng `git hash-object --no-filters`: 13/13 khớp; so byte không còn tệp nào khác.
- **Sẽ làm:**
  - Không xóa thư mục hỏng nào.
  - Khi driver chạy xong, chạy lại **đúng** các job hỏng vì lý do này vào `<job>-rerun1`, cùng nhãn và cùng lệnh, như
    Tầng 2 AMENDMENTS A2.
  - Phân tích dùng `-rerun1` khi có.
  - Kiểm rằng mọi job pass có cùng `repositoryInventorySha256`.
  - (b) được phát triển ở một worktree **riêng**, và chỉ sau khi quét xong.
- **Bài học ghi vào memory:** không bao giờ sửa worktree mà một job đang chạy dùng.
- **Đã làm sau khi quét xong** (xem `SWEEP-REPORT.md` §2):
  - 12 job hỏng đã chạy lại vào `-rerun1` bằng `rerun_failed.py`, và 12/12 trùng từng frame.
  - Cả 156 job dùng để phân tích có cùng inventory `0da63eaf…`.
  - Không thư mục hỏng nào bị xóa.
