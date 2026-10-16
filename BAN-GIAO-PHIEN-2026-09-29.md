# RideBound — Bàn giao phiên 2026-09-29 (Tầng 3), cho phiên AI làm việc tiếp

> Viết 2026-09-29. Tài liệu này **nối tiếp** `BAN-GIAO-PHIEN-2026-09-23.md`, không thay nó.
> - Luật chơi, ràng buộc và giao thức chống ảo giác vẫn lấy từ bản 23/09 (§2, §9, §11, §12).
> - Trạng thái, kết quả và việc tiếp theo lấy từ tài liệu này.
> - Nếu hai bản mâu thuẫn về **trạng thái**, tin bản này và `git`. Về **ràng buộc của người dùng**, tin bản mới hơn.
> Mọi con số dưới đây có nguồn `tệp:dòng` hoặc lệnh đã chạy. Chỗ nào chưa kiểm thì ghi ⚠️ **chưa kiểm**.
>
> **Hai phiên song song.** Phiên cũ (`ridebound-84`) từ nay **chỉ trả lời câu hỏi** của người dùng và **không
> sửa tệp nào**. Phiên mới là phiên **duy nhất** được sửa tệp và chạy mô phỏng. Trước khi chạy job, vẫn kiểm
> `ListAgents` và thời điểm sửa của các thư mục log:
> - `tang3\sweep\logs\`, `tang3\sweep\logs-noworse\` và `tang3\pilot\logs\`;
> - thư mục log của driver mới.
> Kiểm cả các công tắc `tang3\sweep\STOP` và `tang3\pilot\STOP`.
>
> Tài liệu này đã được soát độc lập 2 vòng ngày 29/09 (4 agent đọc, đối chiếu nguồn). Các lỗi tìm ra đã sửa. Các
> chỗ còn chưa kiểm được đánh dấu ⚠️.

---

## 0. Đọc gì, theo thứ tự nào — BẮT BUỘC trước khi sửa tệp hay chạy job

1. **Toàn bộ tài liệu này.**
2. `E:\Code\Report_INT3508\BAN-GIAO-PHIEN-2026-09-23.md`: §2 (ràng buộc), §9 (giao thức chống ảo giác), §11 (bẫy),
   §12 (việc không làm), §7.5 (❌ không được tuyên bố). Các phần trạng thái của bản đó đã cũ.
3. `E:\Code\Report_INT3508\KE-HOACH-HOP-NHAT-2026-09-23.md`:
   - §1, §5.2, §5.6;
   - §6 Tầng 3 (dòng ~1336–1375);
   - §7.1–7.4;
   - §8 (thiết kế thống kê, **đặc biệt §8.3 hiệu chỉnh γ**, dòng ~1488–1519);
   - §9, §10.
4. Tầng 3 trong `E:\Code\Report_INT3508\ridebound-scratchpad\tang3\`:
   - `T3.1-KHOA-CAU-HOI.md`, khóa câu hỏi, gồm H1, H2 và H3;
   - `T3.7-KE-HOACH-THI-DIEM.md` và `T3.7-BAO-CAO-THI-DIEM.md`;
   - `sweep\SWEEP-PLAN.md`, `sweep\SWEEP-AMENDMENTS.md`, `sweep\SWEEP-REPORT.md`;
   - `world\README.md`. Lưu ý dòng 3 và 75 của README đã cũ: v1.1 **đã** được dùng cho toàn bộ phép quét.
5. Backlog Codex, nguồn chi tiết cho T3.8 và T3.9:
   `E:\Code\Report_INT3508\ridebound-scratchpad\conduct-outcome-plan-2026-09-22\KE-HOACH-END-TO-END-CONDUCT-OUTCOME-STOCHASTIC.md`.
   Đọc §4.5, §9, §12.3, §16, §17 và các ticket P6, P7, P8, E03–E06, Q01–Q12.
6. Kho mã, bản mới nhất nằm ở worktree `C:\Code\RideBound-noworse`:
   - `AGENTS.md`;
   - `docs/18-status-and-decision-log.md`: ADR-074…077, dòng 4726–5137, và change history 2026-09-24→26;
   - `docs/19-requirement-traceability.md` §27–§31.
7. Memory: `C:\Users\quang\.claude\projects\e--Code-RideBound\memory\` (MEMORY.md và các tệp). Đọc kỹ
   `ridebound-env-traps.md`.

---

## 1. Người dùng và luật làm việc

- **Người dùng:** Trần Quang Thành, 23020155, K68I-IT2, UET/VNU. Dùng đại từ trung tính khi nhắc tới người dùng.
- **Yêu cầu thường trực, nguyên văn** (`BAN-GIAO-PHIEN-2026-09-23.md:694-705`): *"Không bịa bất cứ thứ gì;
  chưa kiểm thì ghi 'chưa kiểm'. Không xóa tệp nào. Báo tiến độ mỗi giờ khi có job dài. Hỏi tôi trước khi
  commit/push, trước khi bắt đầu Tầng 3, và để lấy tên cán bộ hướng dẫn. Trả lời tôi bằng tiếng Việt, giải
  thích đơn giản kèm ví dụ thật từ hệ thống."*
- **Phê duyệt đã có:**
  - 2026-09-24: người dùng duyệt "thực hiện toàn bộ", tên cán bộ hướng dẫn để sau. Đây là diễn đạt lại; memory
    `ridebound-handoff-2026-09-23.md:21,38` chỉ ghi "thực hiện toàn bộ". Phê duyệt này gồm commit/push lên các
    **nhánh nghiên cứu** và việc bắt đầu Tầng 3.
  - Tầng 3 đang chạy dưới phê duyệt này.
  - 2026-09-25/26: *"Thực hiện toàn bộ đảm bảo có đủ thông số để so sánh… kiểm tra kĩ đảm bảo công bằng cho cả
    hai"*. Từ đó có phép quét C/M⁺ và luật phục hồi (b).
  - 2026-09-29: người dùng trả lời **"Oke đấy"** cho đề xuất chạy phép thử **chỉ dữ liệu thật ở khung
    7:00–9:00** (§9 việc B). Trong cùng tin, người dùng yêu cầu chuyển sang phiên mới.
  - Đề xuất **"so lại C với V bằng luật phục hồi công bằng"** (§9 việc A) **chưa** được trả lời riêng. Nó vẫn
    nằm trong phạm vi Tầng 3 đã duyệt. Nên báo người dùng một câu trước khi chạy.
  - Nguồn của hai câu người dùng ngày 25–26/09 và 29/09 là hội thoại của phiên cũ; không tệp nào ghi lại. Nếu cần,
    hỏi lại người dùng.
- **Vẫn phải hỏi người dùng:**
  - tên cán bộ hướng dẫn;
  - mọi việc xóa tệp;
  - commit **kho luận văn** `E:\Code\Report_INT3508`: để người dùng tự làm, AI không commit;
  - các **quyết định của chủ nghiên cứu** ở §8 (δ_s, δ_b, δ_r, α, quy tắc quyết định H2 và H3, nguồn episode…),
    trước T3.8;
  - chạy Hamburg hoặc thêm mô hình khách từ chối (chưa quyết).
- **Ràng buộc** (chi tiết ở bản 23/09 §2):
  - Không xóa tệp. Nếu cần bỏ, đổi tên hoặc cách ly.
  - Không đụng cây chính `E:\Code\RideBound`: nó có thay đổi chưa commit của người dùng.
  - Không đụng báo cáo thực tập ở gốc `E:\Code\Report_INT3508` (main.tex, noi-dung/ gốc, Baocaothuctap_*).
    Luận văn là `E:\Code\Report_INT3508\ridebound\`.
  - Không thêm lại mục 4–7 của báo cáo tiếng Việt cũ.
  - Ổ E: phải còn ≥ 40 GB trống và ổ C: ≥ 50 GB. Không xóa để lấy chỗ.
  - Không gửi email người dùng ra ngoài. Không cài đặt, không đổi cấu hình máy, không kill process của người dùng.
  - Chạy `dotnet test RideBound.slnx` sau mỗi thay đổi mã.
  - docs/18, docs/19 và ADR chỉ sửa ở worktree nghiên cứu, gắn nhãn **thăm dò**.
  - Không claim tính mới cho: dynamic insertion, ETA limits, reassignment, route similarity, least-commitment,
    time consistency, user satisfaction.
  - Không authorize RB-WP14R-009..012, WP15, H7.
  - Báo cáo của subagent không phải phê duyệt của người dùng.
  - Job dài chỉ chạy khi cắm sạc. **Không bao giờ sửa worktree mà job đang dùng.**
- **Cách trả lời người dùng**, người dùng đã nhấn mạnh nhiều lần trong phiên 29/09:
  - tiếng Việt, câu tự nhiên, **tránh thuật ngữ và chữ tắt**. Người dùng không nhớ "C/V/W1–W5": gọi bằng tên thường;
  - luôn có ví dụ thật từ dữ liệu;
  - đọc lại nguồn chứ không trả lời theo trí nhớ;
  - nói rõ chỗ yếu.

---

## 2. Trạng thái một trang

| Tầng | Nội dung | Trạng thái |
|---|---|---|
| 0 + 1 | Sửa báo cáo và phân tích thêm 558 lần chạy cũ | ✅ Xong. Còn: tên cán bộ hướng dẫn, nguồn Geržinič (số 20–25 EUR/h ghi "chưa đối chiếu"), bài *anticipatory walking* (luận văn **không** nhắc tới) |
| 2 | Kiểm Định lý 4 trên tắc đường thật, có dự đoán niêm phong | ✅ Xong, đạt ở mức thăm dò. Đã vào Ch.1, 3, 4, 5 và tóm tắt |
| 3 | T3.1–T3.7, phép quét C/M⁺ và ADR-077 | ✅ Xong ở mức thăm dò. **Cổng dừng của thí điểm bị kích hoạt**; (b) được làm để sửa nhưng mới chạy cho M⁺ |
| 3 | T3.8 (chọn chính sách + hiệu chỉnh conformal, H3) | ❌ Chưa làm. Không có mã conformal nào; chưa có ngưỡng nào được chốt |
| 3 | T3.9 (xác nhận trên ma trận khóa, H2) | ❌ Chưa làm |
| 4 | WP15 | Ngoài phạm vi |

- **Giả thuyết Tầng 3** (`T3.1-KHOA-CAU-HOI.md:51-59`):
  - **H1:** C không bao giờ phục hồi vì cam kết. **Đứng** trong mọi lần chạy (0/72 ở phép quét, 12/12 ở thí điểm).
  - **H2:** tồn tại vùng (mức nhiễu, β) nơi C phục vụ nhiều hơn **V** ít nhất một biên (T3.1 viết là δ_s, tài
    liệu này gọi là **δ_b**, xem §8 dòng 1), trong khi E2 của C không lớn hơn E2 của V quá **δ_r**. **Chưa kết luận:**
    δ_b và δ_r chưa chốt, luật phục hồi gây nhiễu kết quả, mỗi ô chỉ một episode.
  - **H3:** γ hiệu chỉnh cho coverage ≥ 1−α, và β+γ đủ nhỏ để hữu ích. **Chưa làm.**
- **"Chứng minh > X%"** mà người dùng nhắc chính là **H2** với X = δ_b, và **H3** với α. H2 **so với V** (luật theo
  giờ khách thấy), **không** so với M⁺: với M⁺ đã thấy số khách bằng nhau (§5.4).
- **Ký hiệu:** trong tài liệu này, δ_s **chỉ** dùng cho sàn phục vụ so với U, còn δ_b là biên của H2. T3.1 dùng δ_s
  cho cả hai nghĩa (`T3.1:44` và `:54`). Phải tách trước khi niêm phong.

---

## 3. Bản đồ tệp và môi trường (đã kiểm 2026-09-29)

### 3.1 Kho mã, worktree, nhánh

`git -C E:\Code\RideBound worktree list`:

| Worktree | Nhánh | HEAD | Ghi chú |
|---|---|---|---|
| `E:\Code\RideBound` | main | 41a4e11 | **Không đụng.** Có thay đổi chưa commit của người dùng |
| `C:\Code\RideBound-noworse` | research/tier3-no-worse | a90b4b7 | **Bản mới nhất, dùng để sửa mã.** Sạch, đã push. Chuỗi 65d867c → 8d1ea4d → 69512d3 → 1ce15e9 → 45f8026 → a90b4b7 |
| `E:\Code\RideBound-deadline` | research/tier3-failure-aware | 1ce15e9 | **Mọi job pilot, quét và no-worse chạy với cwd ở đây.** `git status` hiện 144 ' M' nhưng diff rỗng: chỉ khác CRLF, mtime 2026-09-24. **Không sửa, không "dọn", không build ở đây** vì inventory `0da63eaf…` đang là mốc |
| `E:\Code\RideBound-py-baseline` | detached | 8d1ea4d | Mốc so test Python (6 test freeze đỏ sẵn) |

- Nhánh `research/deadline-gate` = 65d867c (ADR-074), đã push.
- Nhãn "chưa commit" đã **cũ**. Nó còn ở:
  - docs/18 dòng 4726, 4760, 4803, 4861, 4945, 4997, 5197, 5204, 5212;
  - docs/19 dòng 689, 709, 731.
  Commit tương ứng là 65d867c, 8d1ea4d, 69512d3.

### 3.2 Runner đã publish, không đổi

| Runner | Dựng lúc | Tree SHA-256 (manifest) | Dùng cho |
|---|---|---|---|
| `E:\RideBoundData\research\runner-deadline-v1` | 2026-09-24 | 8fa5dd28…61cda8 (`ridebound-scratchpad\deadline\runner-deadline-v1.sha256.tsv:1`) | Tầng 2 |
| `E:\RideBoundData\research\runner-tier3-v1` | 2026-09-25, từ 69512d3 | 5049f6d3…52c5cb (`tang3\runner-tier3-v1.sha256.tsv:1`) | Thí điểm, quét |
| `C:\RideBoundData\research\runner-tier3-v2` | 2026-09-26, từ 45f8026 | ac251ef3…cff3f (`tang3\runner-tier3-v2.sha256.tsv:1`) | No-worse (b) |

- `tang3\runner_manifest.py verify` cho v1 và v2: OK.
- Với runner-deadline-v1: đúng 429/429 tệp, nhưng header dùng định nghĩa tree khác. Không phải lỗi runner.

### 3.3 Output (không xóa gì)

| Thư mục | Nội dung |
|---|---|
| `E:\RideBoundData\research\deadline-v1` | Tầng 2. 301 thư mục: 165 có summary; 136 có `failure-00.json` (lần chạy dừng vì vô nghiệm hoặc bất biến, đúng thiết kế Tầng 2) |
| `E:\RideBoundData\research\tier3-pilot-v1` | Thí điểm. 60 thư mục, inventory 9a003f43…, world v1 |
| `E:\RideBoundData\research\tier3-sweep-v1` | Quét. 168 thư mục = 156 + 12 `-rerun1`. 12 thư mục gốc W4 không có summary (sự cố A2): **phải bỏ qua khi quét thư mục**. Inventory 0da63eaf… |
| `C:\RideBoundData\research\tier3-sweep-noworse-v1` | 28 job (b). Tên thư mục **trùng** tên job quét; `-nw` chỉ là `--label`. Log từng job ở `tang3\sweep\logs-noworse\` |
| `E:\RideBoundData\research\tier3-world-smoke-v1`, `tier3-world-v11-smoke` | Smoke của world |

- Mỗi job 72–93 MB. Thời gian chạy (wall, theo `summary.json`): thí điểm 920–1.732 s, quét 939–2.013 s,
  no-worse 829–1.208 s.
- **Dung lượng 2026-09-29:** C: 103,8 GB trống, E: 41,8 GB trống. **Output mới để ở ổ C:.**

### 3.4 Scratchpad Tầng 3 (`E:\Code\Report_INT3508\ridebound-scratchpad\tang3\`)

- `configs\`:
  - C-30…C-900, Mplus-30…Mplus-900, **M-30/60/120, V-30/60/120** (đã có sẵn, sinh bởi `make_configs_t3.py`), U;
  - `wp4-tier3-v1.json` (`commitmentRecovery: forced-reference-v1`, `lateBoarding: record-v1`);
  - `wp4-tier3-v2.json` (chỉ khác ở `no-worse-than-reference-v1`).
- **V-30 khác C-30 đúng một khóa**, `budgetBasis: customerVisible` (`make_configs_t3.log:4-6`).
  M-30 = Mplus-30 cộng `dropEtaDeadlineTwoSided: true`.
- `world\`:
  - `world_v1.py`: f(od,b) = base(b)·exp(L)·(1+S). Nhiễu AR(1) hai chiều; sốc S luôn ≥ 0 (dòng 72); số ngẫu nhiên
    băm theo khóa;
  - `preflight_world.py` (v1) và `preflight_world_v1_1.py` (v1.1: đổi mốc đúng bin×900 s);
  - test: v1.1 có 14 kiểm, 5/5 đột biến bị bắt; v1 có `mutate_world` 6/6 và `mutate_preflight_world` 7/7
    (`world\README.md:19-28,50,98-100`);
  - `world\README.md` dòng 3 và 75 đã cũ. Sửa được bất cứ lúc nào, vì tệp này nằm ở scratchpad, không phải kho.
- `pilot\`:
  - `run_pilot.py` (WORKERS=6; công tắc STOP; chỉ chạy khi cắm sạc; giữ máy thức);
  - `worlds\W0…W5-*.json`;
  - công cụ phân tích và các TSV thí điểm.
- `sweep\`: `run_sweep.py`, `run_noworse.py`, `rerun_failed.py`, `sweep_analyze.py` (M1–M8), `noworse_analyze.py`,
  `noworse_aggregate.py`, `split_noworse.py`, `per_world.py`, `why_similar.py`, các TSV `*-2026-09-26.tsv`, `logs\`.
- `evidence\`:
  - `audit_vep.py` dựng lại v/e/p có dấu từ checkpoint cuối;
  - `METRICS-SPEC.md`;
  - `choice_metrics.py`;
  - `independent\` (bộ kiểm độc lập).
- `oracle\`: oracle kế toán.
- **Mới 29/09:** `TANG3-BAO-CAO-DE-HIEU-2026-09-29.md`, bản báo cáo Tầng 3 bằng lời thường mà người dùng muốn
  đưa vào báo cáo (§5.8).

### 3.5 Luận văn `E:\Code\Report_INT3508\ridebound\`

- Thư mục này **không nằm trong git**: `git status` của `E:\Code\Report_INT3508` hiện `?? ridebound/`. Không có lịch sử.
- **Build:** `cd E:\Code\Report_INT3508\ridebound; ..\tools\tectonic.exe -X compile main.tex --outdir . --keep-logs`.
  Phải có `--keep-logs`. Kiểm thời điểm của `main.log`, và kiểm 0 Overfull, 0 undefined.
- Build cuối lúc 2026-09-29 11:54:58: sạch, 100 trang.
- Tầng 2 nằm ở `08-chuong4.tex` mục `muc:tang2` (dòng ~937).
- Tầng 3 nằm ở mục `muc:quet` (dòng ~1132–1404), gồm các bảng `bang:quet` (tách thật/tự tạo), `bang:quet-kieu`
  (6 kiểu tắc đường) và `bang:quetb` (luật phục hồi (b), tách thật/tự tạo).
- Định lý 4 là `dl:hocong` ở `07-chuong3.tex:501-517`; hệ quả `hq:chieutroi` ở :558.

### 3.6 Dữ liệu

- **FleetPy Manhattan:** `E:\RideBoundData\wp6\extracted\sha256\d9\d9e86f33645e5eec287d387f8d63ad41ddf41d4ef648138b65d636482e2c599e\FleetPy_Manhattan\`.
  - Zenodo DOI 10.5281/zenodo.15187906, CC BY 4.0.
  - `networks\Manhattan_2019_corrected\`:
    - bản đồ OSM 4.411 nút, 9.573 cạnh, mỗi cạnh một thời gian cố định;
    - bảng đường ngắn nhất;
    - `2018-11-DD_tt_factors.csv`: **một hệ số chung cho cả mạng mỗi 15 phút**, cột `travel_time_factor`.
      Dữ liệu **không có** tắc đường theo từng con đường.
  - `demand\...\2018-11-DD_sample_10_r.csv`.
- **Kịch bản dùng trong mô phỏng:** bảng thời gian giữa **96 điểm** chọn cho từng ô (9.120 cung), tọa độ tổng hợp.
  **Không** nói "trên mạng đường Manhattan".
- **Hamburg** (Schulz và Pfeiffer): `C:\Users\quang\Downloads\data` (900 instance, `readme.txt`, `_distances.txt`).
  **Chưa chạy.**
- **Python:** `E:\RideBoundData\wp7\envs\fleetpy-1.0.2\python.exe -B`, với `PYTHONDONTWRITEBYTECODE=1` và
  `PYTHONIOENCODING=utf-8`. FleetPy ở `E:\RideBoundData\wp7\FleetPy-1.0.2`.

---

## 4. Hệ thống và các luật, định nghĩa ngắn

**Ba mốc cho mỗi lần công bố giờ trả của một khách:**
- v = giờ đã hứa trước đó;
- e = giờ đến nếu **giữ nguyên tuyến cũ** tính theo tình hình hiện tại;
- p = giờ trả mới.
- Từ đó: phần do hệ thống c = p − e; phần ngoại sinh x = e − v; phần khách thấy z = p − v.
- Đây là bất đẳng thức |z| ≤ |c| + |x|, **không** phải đẳng thức.

**Năm luật được so.** Trong câu trả lời cho người dùng, dùng tên thường ở cột 3:

| Chữ tắt | Kiểm gì | Tên thường |
|---|---|---|
| U | Không cổng nghiên cứu, cùng ràng buộc vật lý và khóa | "không luật" |
| C (C1) | Σ\|c\| ≤ x cho mỗi khách | "luật của khóa luận", "hứa theo việc hệ thống làm" |
| M⁺ | p − p₀ ≤ x, với p₀ là lời hứa **đầu** (Schulz và Pfeiffer, l = B + L) | "hạn chót của bài báo" |
| M | \|p − p₀\| ≤ x | "hạn chót hai chiều" |
| V | Σ\|z\| ≤ x | "luật theo giờ khách thấy trên app" |

- **Định lý 4 (`dl:hocong`).** "Giữ nguyên tuyến" có c = 0, nên C không bao giờ loại nó. Vì vậy C **không bao giờ là
  nguyên nhân** làm rỗng tập phương án. M⁺, M và V có thể loại nó khi tắc đường thay đổi; ngưỡng an toàn tăng dần
  theo thứ tự M⁺ ≤ M ≤ V.
- **Hệ quả chiều trôi:**
  - trôi bất lợi (tắc tăng): M⁺ = M = V;
  - trôi thuận lợi: M⁺ an toàn, còn M và V vẫn kẹt.
- **Không được viết** "hệ thống dùng C không bao giờ kẹt": 11/20 ô vẫn dừng vì bất biến cửa sổ đón.
- **Luật phục hồi:**
  - **(a)** `forced-reference-v1` (ADR-075): xe bị ép giữ tuyến và "đóng băng".
  - **(b)** `no-worse-than-reference-v1` (ADR-077): xe bị ép được đổi tuyến nếu mọi cổng vi phạm cũng là vi phạm
    của tuyến giữ, và không tệ hơn trên từng cổng. Đã có unit test cho **cơ sở nhìn thấy (V)** và **cận dưới hai
    chiều (M)**, nhưng **chưa chạy đầu-cuối cho V hay M**.
- **Đón muộn:** `lateBoarding: record-v1` (ADR-076). Mọi nhánh trong một phép so phải cùng giá trị và **cùng byte** cấu hình WP4.
- **Sáu kiểu tắc đường** (`tang3\pilot\worlds\`; mỗi mốc 15 phút; số là hệ số so với đầu khung):

| Mã | Tên thường | Tham số |
|---|---|---|
| W0 | Đường không đổi | base [1] |
| W1 | Một cú sốc *(tự tạo)* | base [1.0, 1.0, 1.6, 1.3, 1.1, 1.0] |
| W2 | Sốc lặp *(tự tạo)* | [1.0, 1.5, 1.1, 1.5, 1.1, 1.5, 1.1, 1.0] |
| W3 | Tắc giảm dần *(tự tạo)* | [1.0, 0.85, 0.75, 0.7] |
| W4 | Nhiễu theo cặp điểm *(tự tạo)* | sigma 0.08, rho 0.7, shockRate 0.02, shockMean 0.4, half-life 2, seed 101 |
| W5 | **Ngày đo thật 12/11** | base {day 2018-11-12, exponent 1, windowStart 28800 hoặc 61200}. `W5-*.json` **gắn cứng ngày 12/11** |

- **Hai ô dùng ở thí điểm và phép quét:** `d20181112-s10-r1-w08` (8:00–10:00) và `-w17` (17:00–19:00), thuộc panel
  phát triển `wp14-development-panel-v1`. Mỗi ô 108 khách, 8 xe sức chứa 4, cửa sổ đón 600 s, thời gian trên xe
  ≤ 1,5× đi thẳng.

---

## 5. Kết quả đã có (thăm dò), kèm nguồn

### 5.1 Trước kế hoạch: 558 lần chạy, panel 20 ô, tắc đường cố định (luận văn Ch.4)

- **Không luật:** 89,06% lượng dời giờ khách thấy là do hệ thống tự gây ra. 23,2% khách gánh toàn bộ; người nặng nhất
  gần 14 phút (Ch.5:34-38).
- **Luật C 30 s:** phần do hệ thống giảm từ 74.443 s xuống 128 s. Đổi lại phục vụ 1.581 thay vì 1.735 khách, tức
  −7,13 điểm %. Riêng việc khóa xe và điểm dừng (cấu hình nobudget) đã tốn 3,70 điểm % (08-chuong4.tex:325).
- **Cơ sở kết quả (V):** vô nghiệm 4/20 ô khi tắc cố định. Khi tắc thật (k=1): 19/20 ô, còn C 0/20.
- **Lựa chọn thưa** (`bang:mong`, 08-chuong4.tex:1805-1807 và :1822, cột B1): trên kỷ nguyên có khách mới,
  **73,84% tập của một xe có 0 vị trí chèn**, 23,68% có 1 vị trí, 2,48% có từ 2 trở lên. Cột C1: 74,76 / 22,30 / 2,95.
  - Lỗi đã sửa trong phiên 29/09: từng nói sai thành "73,8% chỉ có 1 cách ghép".

### 5.2 Tầng 2 (`muc:tang2`; `ridebound-scratchpad\deadline\analysis-2026-09-24-final.txt`)

- **Kết cục là ô "vô nghiệm do cam kết"**, tức lần chạy **dừng**. Chỉ cần một khách một lần là cả ô tính là hỏng.
- **Số ô vô nghiệm** (các dòng C và V của 2A lấy từ luận văn 08-chuong4.tex:1006-1023, không có trong tệp analysis):
  - 2A sáng, tắc thật: C 0/20 (11 ô dừng vì cửa sổ đón); M⁺ 30 s 19/20; M⁺ 60 s 13/20; M⁺ 120 s 3/20; V 19/20.
  - 2B tối: M⁺ 0/8, M 7/8 (đều ở cận dưới), V 8/8.
  - C: 0/56 lần.
- **Dự đoán niêm phong** (06:03:52Z 24/9) đúng 98/102, 31/32, 40/40.
- **Dự đoán phụ không xảy ra:** hạn chót không chở nhiều hơn khi đường thoáng.
- **Giới hạn:** không đo được tỉ lệ phục vụ, vì lần chạy dừng.

### 5.3 Thí điểm T3.7, 60 lần chạy (`T3.7-BAO-CAO-THI-DIEM.md`)

- 5 nhánh U, C-30, V-30, M⁺-30, M-30 × 2 ô × 6 thế giới; **world v1**; runner v1.
- **H1 đứng 12/12:** C lệch do hệ thống tối đa 19,1 s.
- **C-30 ≥ V-30 ở 12/12, hơn ở 9/12,** chênh 0–10 khách trên 108. Ví dụ W2 tối: 79 so với 69.
- **Cổng dừng:** V-30 và M-30 phục hồi ở đa số quyết định trong 5/12 episode (đóng băng tới 30% đội xe), nên chưa
  so xác nhận được.
- **Lỗi công cụ:** mốc tắc đường đổi trễ tới 265 s → làm world v1.1. Riêng lỗi này làm C−V ở W4 sáng đổi từ +4
  xuống +2.
- **Không được** dùng thí điểm làm mốc (a) cho lần chạy mới. Thí điểm khác world (v1 so với v1.1) và inventory
  (9a003f43… so với 0da63eaf…). Runner thì giống nhau: cả hai đều dùng runner-tier3-v1.

### 5.4 Phép quét C/M⁺, 156 lần chạy (`SWEEP-REPORT.md` §2–§6; `logs\sweep-aggregate-2026-09-26.txt`)

- Kế hoạch niêm phong 756b65fd…423f lúc 09:33:58Z 25/9. World v1.1. Runner v1. Luật (a).
- **Công bằng:** mỗi cặp cấu hình chỉ khác 2 khóa; cả hai luật chỉ loại khi vượt hẳn.
- **Bảng tách** (luận văn `bang:quet`; SWEEP-REPORT §4a):

| x | Thật (2 ô, 216 yêu cầu, U 192): C/M⁺, M⁺ phá, M⁺ bị ép | Tự tạo (6 ô, 648 yêu cầu, U 523): C/M⁺, M⁺ phá, C theo luật M⁺, M⁺ bị ép |
|---|---|---|
| 30 | 189/189, 1,1%, 11,9% | 508/503, 18,8%, 17,7%, 33,5% |
| 60 | 190/190, 0, 0 | 509/503, 14,7%, 14,4%, 28,9% |
| 120 | 190/191, 0, 0 | 513/513, 10,1%, 10,8%, 17,2% |
| 300 | 192/192, 0, 0 | 522/524, 1,0%, 1,0%, 5,2% |
| 600, 900 | 192/192, 0, 0 | 523/523, 0, 0, 0 |

- **C phá hứa 0% ở mọi ô,** theo thiết kế. Đây là hệ quả định lý, không phải phát hiện.
- **Theo từng kiểu, M⁺ (a) phá hứa ở 30/60/120/300 s** (luận văn `bang:quet-kieu`, `per_world.py`):

| Kiểu | M⁺ phá hứa 30 / 60 / 120 / 300 s |
|---|---|
| W0 | 0 / 0 / 0 / 0 |
| W1 | 12,3 / 12,3 / 7,8 / 3,0% |
| W2 | 28,8 / 25,2 / 21,4 / 0% |
| W3 | 0 / 0 / 0 / 0 |
| W4 | 15,3 / 6,6 / 1,1 / 0% |
| W5 | 1,1 / 0 / 0 / 0% |

- **Dự đoán D1–D7:** đúng D1, D2, D3, D5 (vừa đủ 6/8), D6; sai D4 (7/8) và D7. D7 sai **cả hai vế**: vế
  "M⁺ A>x > 0" chỉ đạt 7/8, 6/8, 6/8; vế "M⁺ ≤ C" đạt 5/8, 5/8, 7/8.

### 5.5 Luật phục hồi (b), 28 lần chạy (`SWEEP-REPORT.md` §7; `logs\noworse-*`)

- 22 nhánh điều trị (mọi M⁺-x có forced > 0) và 6 đối chứng. Đối chứng giống hệt (a) 6/6.
- **Tổng khách trên 22 job:** (b) 1874, (a) 1864, C 1873. (b) = C ở 21/22 job, cùng chuỗi hành động ở 19/22.
- **Theo nhóm:**
  - Tự tạo, C/(a)/(b): 508/503/508, 509/503/509, 513/513/**514**, 522/524/522.
  - Thật: không đổi số khách.
  - Ở 120 s, (b) **không** bằng hẳn C: 705 so với 703 khi gộp 8 ô.
- **Gánh bị ép:** 15.528 quyết định, khoảng 3.789 non-normal (24%), **do 224 khách trễ gây ra** trên 1.874 khách, tức
  khoảng 17 quyết định bị ép cho mỗi khách trễ.
- **Đọc đúng:** kết quả **gợi ý** rằng chênh lệch số khách của (a) là do luật phục hồi, không do luật hạn chót. Chỉ
  là gợi ý, vì ba lý do:
  - (b) được thêm sau niêm phong, nên chỉ mô tả;
  - mỗi ô chạy một lần;
  - (b) có lúc làm giảm số khách (Mplus-120-W1-w17: (a) 82, (b) 79).
- **(b) lệch khỏi Codex §12.3 ở hai điểm**, cần báo chủ nghiên cứu trước khi chọn (b) cho phép so xác nhận:
  - Codex đòi "không nhận thêm khách trong transaction recovery đầu tiên" (dòng 506), nhưng (b) cho xe bị ép nhận
    khách mới;
  - Codex đòi mọi nhánh có cùng repair operator và work budget (dòng 508), nhưng công validate thêm của (b) chưa
    được cộng vào `validationWorkUnits` (docs/18:5137).

### 5.6 Các kiểm tra sâu trong phiên 29/09, cơ sở cho việc tiếp theo

1. **Tầng 2 hỏng nhiều mà Tầng 3 thất hứa ít** vì đơn vị đo khác nhau (ô so với khách).
   - Cùng ô 12/11 sáng: Tầng 2 dl-30 **dừng**, dl-60 và dl-120 chạy trọn (`analysis-2026-09-24-final.txt:127-131`).
   - Tầng 3 M⁺-30 cùng ô: bị ép ở 23,8% quyết định, khoảng 3/90 khách bị ép, 2/90 (2,2%) thất hứa. M⁺-60: 0 lần ép.
   - Hai tầng khớp nhau.
2. **Luật có cắn thật.** Số phương án bị cổng loại trên các thế giới có tắc: U 139, C-30 474, M⁺-30 587. Ở mức
   ≥ 600 s thì cả ba đều 139. C-30 phục vụ 697 so với U 715.
3. **Không phải "cả hai chỉ giữ tuyến".** Ở C-30, trên W0, W2 và W5 buổi sáng (`why_similar.py` phần C; output
   **chưa lưu log**):
   - mỗi job có 107 quyết định có khách mới;
   - 83–95% trong số đó có ≥ 2 phương án trước cổng; 79–90% vẫn còn ≥ 2 phương án đủ điều kiện sau cổng;
   - 79–90% quyết định có nhận ít nhất một khách (85–96 trên 107). Đây là số **quyết định**, không phải số khách.
4. **Trôi dạt mỗi khách trên ngày thật nhỏ.** Dưới C-30:
   - 12/11 sáng: 2,2% khách trôi quá 30 s, 0% quá 60 s, lớn nhất 35,2 s;
   - tối: lớn nhất 7,7 s;
   - tự tạo: W1 và W2 có 12–32% khách quá 30 s; W4 có 7–18%; W1 tới 6–7 phút.
5. **Khung đã chạy là khung đã qua đoạn tắc dốc.**
   - Cùng tệp hệ số thật, khung 7:00–9:00 các ngày 12–16/11 có đỉnh tăng **47–66%** và bước 15 phút lớn nhất
     8,3–16,2%.
   - Khung 8:00–10:00 chỉ 15–23%, bước lớn nhất 3,7–7,1%.
   - Hai agent soát độc lập đã tính lại từ tệp CSV ngày 29/09 và thấy khớp. Nhưng số này **chưa có script lưu
     riêng**: phiên cũ tính bằng lệnh PowerShell, còn `why_similar.py` phần A không tính khung 7–9h hay bước 15 phút.
     Nên thêm vào script trước khi dùng trong luận văn.
   - Kết luận "trên tắc thật hai luật như nhau" **chỉ đúng cho hai khung đã chạy**.
6. **Cú sốc tự tạo chưa được hiệu chỉnh.** Bước +60% (W1) lớn gấp khoảng 3,7 lần bước thật lớn nhất (+16,2%, 14/11).
   Nhưng tích lũy thật tới 29–50% trong một giờ. Chỗ chưa có bằng chứng là **tính đột ngột**.
   - Các thế giới **công bằng về cách đối xử** (cùng tệp, cùng hạt giống, 0 vấn đề trên 156 log).
   - Nhưng chúng **không trung lập**: 3/4 thế giới tự tạo có cú tăng, và tăng chính là điểm yếu lý thuyết của M⁺.
7. **Thước đo công bằng là chấm cả hai bằng cùng một thước.** Theo thước M⁺ ở 30 s tự tạo: C 17,7%, M⁺(b) 18,4%.
   Theo thước C: C 0%, M⁺(b) 0,2%. Chuyến đi của khách gần như giống hệt nhau.
8. **Ai gây ra việc M⁺ thất hứa.** Trong 22 lần chạy (b) có **222 khách** với A > x:
   - **220 khách** có phần do hệ thống C_r = 0;
   - 2 khách (Mplus-30-W4-d20181112-s10-r1-w08) có C_r = 9,26 s và 6,47 s;
   - trong 222 khách này, không ai có C_r > x.
   - Ngoài 222 khách đó còn 3 khách có C_r > x nhưng A ≤ x (Mplus-120-W4-w08, Mplus-120-W4-w17, Mplus-30-W4-w17).
     Ba khách này ứng với con số 0,15% ở SWEEP-REPORT §7.1.
   Số này do agent soát độc lập đếm ngày 29/09 bằng `audit_vep.py` và `event_times`, và **chưa có script lưu
   riêng**. Muốn dùng trong luận văn thì phải viết script và lưu output.
   - Trước đó phiên cũ từng nói "10/10 khách": thực ra chỉ đã xem 5 khách ở Mplus-60-W4-w08 và 5 khách ở
     Mplus-120-W1-w08.
   - Ví dụ khách của Mplus-120-W1-w08: đặt xe 25:54, cú tắc đến 30:00, **lên xe 32:32**, đến nơi 41:09. Vậy tắc
     đường xảy ra **trước khi khách lên xe**. Phải nói "sau khi đặt xe và được hứa giờ", không nói "sau khi lên xe".
9. **E2** (khách thấy giờ nhảy > 60 s; trung bình 2 ô; script **chưa lưu**):
   - C so với M⁺(b):
     - ở x = 30 s: bằng nhau ở W1, W2, W5; C tốt hơn 0,6 điểm % ở W4;
     - ở x = 60 s: W4 bằng nhau;
     - ở x = 120 s: C tốt hơn 0,5 điểm % ở W5 và 1,0 điểm % ở W4.
   - C so với M⁺(a): với x ≤ 120 s, C **kém hơn** 1,4–2,2 điểm % ở W1 và 1,5–3,3 điểm % ở W2.

### 5.7 Kết luận có thể bảo vệ, và điều không được nói

- ✅ *"C bảo đảm lời hứa về phần do hệ thống, không bao giờ là nguyên nhân làm hết đường chọn (Định lý 4, Tầng 2
  xác nhận thăm dò). So với hạn chót của Schulz và Pfeiffer, C không tốn thêm khách khi xử lý bế tắc công bằng.
  Khác biệt lộ rõ khi tắc đường tăng đột ngột. Trên hai khung thật đã chạy, hạn chót chỉ thất hứa ở mức 30 giây
  (1,1%), và từ mức 1 phút trở lên thì không luật nào thất hứa."*
- ❌ "C chở nhiều khách hơn M⁺".
- ❌ "M⁺ thất hứa 10–29%" như số của thực tế. Chỉ đúng trong thế giới tự tạo.
- ❌ "0% thất hứa của C" như một phát hiện.
- ❌ "Kết quả trên mạng đường Manhattan".
- ❌ "Đã xác nhận" hay "verified" cho các lần chạy có trôi dạt.

### 5.8 Bản dễ hiểu cho báo cáo

`tang3\TANG3-BAO-CAO-DE-HIEU-2026-09-29.md` là bản Tầng 3 bằng lời thường, có bảng tách và bảng 6 kiểu. Người
dùng muốn đưa bản này vào báo cáo. Nếu chèn vào LaTeX, phải kiểm lại từng số với §5.4–5.6.

Một agent soát độc lập đã kiểm bản này ngày 29/09: mọi số trong bảng khớp TSV. Nó tìm ra 20 chỗ nói quá hoặc dùng
chữ chưa chuẩn, và cả 20 đã được sửa trong tệp. Ví dụ:
- "xe chậm đi 60%" → "thời gian đi tăng 60%";
- "một người kiểm độc lập" → thực ra là một agent, kiểm ở giai đoạn thí điểm và có tìm ra một lỗi;
- "hai luật chỉ khác khi tắc đột ngột" → trên ngày thật cũng khác chút ít ở mức 30 giây;
- "cách mới làm mất khoảng chênh" → chỉ là "gợi ý", vì (b) được thêm sau niêm phong.

Khối chú thích nguồn ở đầu tệp phải xóa khi chèn vào luận văn.

**Hồ sơ soát ngày 29/09** lưu ở `tang3\handoff-audit-2026-09-29\`:
- 7 tệp dữ kiện, một tệp cho mỗi phần: `governance`, `inventory`, `tier3plan`, `results`, `thesis`, `docs18`,
  `feasibility`. Mỗi dữ kiện kèm nguồn `tệp:dòng`;
- `critic-plainreport.txt`: 20 lỗi của bản dễ hiểu và 7 chỗ thiếu;
- `critic-2.txt`, từ hai agent (kiểm số liệu, kiểm độ đầy đủ): 28 lỗi và 21 chỗ thiếu của tài liệu này. Tất cả đã
  được sửa hoặc đưa vào §7–§9.

---

## 6. Bài học, sai lầm đã mắc và đã sửa (đừng lặp)

1. **Sự cố A2:** sửa mã trong worktree lúc job đang chạy làm 12 job hỏng ("repository content inventory drifted").
   Đã chạy lại vào `-rerun1`. **Không bao giờ sửa worktree mà job đang dùng.**
2. **tectonic không có `--keep-logs`** thì `main.log` cũ không được viết lại, từng che 2 bảng tràn lề.
3. **Nói quá, đã sửa ở luận văn:**
   - con số gộp 14% (trộn thật và tự tạo), nay đã tách bảng;
   - "73,8% chỉ có một cách";
   - "16 s" thay cho 70 s (Tầng 2);
   - lag 149 s thay cho 265 s.
4. **So sánh vội dễ sai:** với luật (a), C trông như chở nhiều hơn (697 so với 692). Thực ra đó là do cách xử lý bế tắc.
5. **"Bị ép 24%"** là số quyết định; tính theo khách chỉ 12%.
6. **Người dùng hiểu nhanh khi có:** một ví dụ khách thật với giờ cụ thể; tên luật bằng lời; bảng tách thật và tự
   tạo; câu "ô hỏng khác khách thất hứa".
7. **Hệ số 1,6 nghĩa là thời gian đi tăng 60%, không phải "chậm đi 60%".** Tốc độ khi đó còn 62,5%.
8. **Mỗi con số trong báo cáo phải có script và output lưu lại.** Các phép tính tay trong PowerShell ở phiên 29/09
   (đỉnh tăng 7–9h, số yêu cầu 7–9h) chưa nằm trong script nào. Nên thêm vào `why_similar.py` hoặc một script mới.

---

## 7. Errata còn mở — VIỆC 1 (không cần chạy mô phỏng)

**Trước khi sửa luận văn:** thư mục `ridebound\` **không có git**, nên sửa sai thì không lấy lại được.
- Chép toàn bộ `ridebound\noi-dung\` và `main.tex` sang một thư mục sao lưu mới, ví dụ
  `ridebound-scratchpad\tex-backup-2026-09-29-before-errata\`. Có tiền lệ: `tex-backup-2026-09-23-before-T0.2`.
- Không ghi đè, không xóa bản sao cũ.

**Luận văn** `08-chuong4.tex` (số dòng lấy lúc 29/09; grep lại trước khi sửa):
1. :1264–1276: ghi "Năm trên bảy dự đoán đúng" nhưng chỉ liệt kê 3 dự đoán đúng; thiếu "C-30 ≥ M⁺-30 ở ≥ 6/8 ô (đúng,
   vừa đủ)" và "tắc giảm dần: M⁺ ≥ C (đúng 12/12, bằng nhau)".
   - Câu "5/8, 5/8 và 7/8 … dưới ngưỡng 6/8" sai: 7/8 không dưới 6/8.
   - D7 sai **cả vế ">0"** (7/8, 6/8, 6/8). Xem §5.4.
2. :1392–1393: câu "hai luật như nhau từ mức 1 phút" cần nói rõ là về **lời hứa bị phá**. Ở 120 s thật, số khách
   190/191, và cùng quyết định chỉ 1/2 ô.
3. :1356 ghi "17–34%" mà không nói luật nào. Đó là số của luật (a) (33,5 / 28,9 / 17,2). Câu kế tiếp :1359–1361
   lại dùng số của (b) (25,6%). Cách sửa: thêm "(luật (a))", hoặc đổi thành 18–36%, số của (b).
4. :1330 (mục "Nhóm tắc đường thật", dưới bảng `bang:quetb`): "Luật (b) không đổi gì" → "không đổi số khách". Tỉ lệ
   non-normal của ô thật buổi sáng đổi từ 0,238 xuống 0,232.
5. `muc:hanche` :2095–2096: câu "Không có kết quả về tỉ lệ phục vụ dưới trôi dạt thật" phải giới hạn vào phép so hai
   cơ sở. Phép quét đã có số khách trên ngày 12/11. Cũng nên thêm một mục về giới hạn của phép quét.
6. `bang:quymo` (:75–99), tóm tắt (02-tom-tat.tex:27, :72) và Ch.5:34 vẫn ghi "558 lần chạy". Bảng lộ trình
   `bang:lotrinh` (:7–34) chưa có dòng `muc:quet`. Ch.1 và tóm tắt không nhắc phép quét.
   - **Phải chốt quy ước đếm** trước khi sửa, rồi ghi quy ước đó vào luận văn. Đề xuất: đếm **lần chạy được phân
     tích**, và ghi riêng số chạy lại:
     - Tầng 2: `deadline-v1` có 301 thư mục, gồm 5 lần chạy lại vì máy ngủ. 136 thư mục có `failure-00.json`: đó là
       lần chạy dừng đúng thiết kế, vẫn là kết quả;
     - Tầng 3: thí điểm 60; quét 156, cộng 12 lần chạy lại (12 thư mục hỏng vẫn giữ); no-worse 28; smoke 2 + 4.
   - **Dung lượng**, lấy theo tổng từng thư mục, không dùng `du` trên cả gốc (quá 5 phút): deadline-v1 12,84 GB;
     pilot 4,82 GB; sweep 14,09 GB; noworse 2,26 GB; smoke 0,14 + 0,31 GB.
7. :687–688 viết "tăng đơn điệu" cho khung 8–10h của các ngày 14–18/11, trong khi `muc:hanche` :2078 nói "tính
   đơn điệu chưa kiểm". Tính lại từ tệp hệ số, bước 15 phút nhỏ nhất trong khung 8–10h:
   - 14/11: 0,0%; 15/11: +0,4%; 16/11: −1,8%; 17/11: +1,5%; 18/11: −0,8%;
   - 12/11 (panel phát triển): −4,5%.
   Vậy **không** đơn điệu ở 16/11 và 18/11. Phải sửa câu :687–688.
8. 05-chuong1.tex:271 và 08-chuong4.tex:43–44 gọi 14–18/11/2018 là "ngày làm việc". Nhưng 17/11 là thứ Bảy và 18/11
   là Chủ nhật: phải sửa.
9. Ch.5 "Hướng phát triển" chưa có ba mục: khung 7–9h, Hamburg, các cách phục hồi khác.
10. README luận văn: dòng :14 thiếu `--keep-logs`; dòng :5 ghi "66 trang", thực tế 100 trang.
11. Nếu chèn `tang3\TANG3-BAO-CAO-DE-HIEU-2026-09-29.md` vào luận văn: xóa khối ghi chú nguồn ở đầu tệp. Con số
    222/220/2 khách phải có script lưu output trước khi dùng (§5.6 mục 8).

**Báo cáo quét** `tang3\sweep\SWEEP-REPORT.md`:
- §3 D7: bổ sung vế ">0".
- §6.3 và §7.2: "biến mất" và "đúng như C" chỉ đúng ở 30, 60, 300 và ≥ 600 s. Ở 120 s là 705 so với 703.
- §5: "5 khách chỉ bị loại vì cửa sổ hoặc thời gian đi" chưa được TSV chứng minh, vì cột `onlyM_otherCodesOnly` gồm
  cả khách không có mã loại nào.
- §8: các số của khung 7–9h và số yêu cầu được tính bằng lệnh PowerShell, **không** phải bằng `why_similar.py`. Nên
  thêm phần đó vào script, hoặc ghi đúng nguồn.
- §4a "Nhóm thật: không đổi gì": xem errata 4 ở trên.
- `split_noworse.py`, `per_world.py` và `why_similar.py` chưa có log output. Nên chạy lại và lưu vào `sweep\logs\`
  (mở log mode `x`, tên mới).

**Scratchpad khác:** `tang3\world\README.md` dòng 3 ("chưa tích hợp") và 75 ("CHƯA dùng cho run nào") đã cũ.

**Kho** (`C:\Code\RideBound-noworse`, khi có commit tiếp theo): sửa nhãn "chưa commit" ở docs/18 dòng 4726, 4760,
4803, 4861, 4945, 4997, 5197, 5204, 5212 và docs/19 dòng 689, 709, 731. Thay bằng commit id 65d867c, 8d1ea4d,
69512d3.

---

## 8. Quyết định của chủ nghiên cứu cần chốt TRƯỚC T3.8 và T3.9

Chưa có tệp nào ghi các giá trị này. **Phải hỏi người dùng.** Chỉ đưa đề xuất, không tự chốt. Mọi ngưỡng phải chốt
**trước** khi mở tập hiệu chỉnh hay tập kiểm tra, và không suy ra từ kết quả của C.

| # | Quyết định | Tình trạng hoặc đề xuất (chưa duyệt) | Cơ sở |
|---|---|---|---|
| 1 | Tách hai nghĩa của **δ_s**: (i) sàn phục vụ so với U; (ii) biên lợi ích của H2 (C hơn V) | T3.1 dùng cùng một ký hiệu cho cả hai (`T3.1:44` và `:54`). Đề xuất gọi (i) là δ_s và (ii) là δ_b | `T3.7-KE-HOACH:75-77` liệt kê riêng |
| 2 | Giá trị δ_s (sàn) | Người dùng chốt. Số tham khảo: giá của cổng khi đường không đổi là 4–5/108 khách; C-30 so với U từ −5 đến +1 | `T3.7-BAO-CAO:229-233` |
| 3 | Giá trị δ_b (H2) | Phải lớn hơn nhiễu. Riêng việc sửa thời điểm đổi mốc đã dời C−V 2 khách (khoảng 2 điểm %) | `world\README.md:112-117` |
| 4 | δ_r (E2 của C được kém V bao nhiêu) | Thí điểm: E2 chênh tới 7,2 điểm % (W4 sáng) | `T3.7-BAO-CAO:229-233` |
| 5 | Luật phục hồi cho phép so xác nhận | Đề xuất (b), vẫn báo cả (a). Chỉ chốt sau việc A. Phải báo hai chỗ (b) lệch khỏi Codex §12.3, xem §5.5 | Pilot §5 mục 1; Codex :506, :508 |
| 6 | α và điểm số episode S_j | Kế hoạch §8.3: S_j = max_r X_{r,j}, lấy trên giờ trả (hoặc hai điểm số, chia α). Tính tay: α = 0,05 cần n ≥ 19 episode hiệu chỉnh; α = 0,10 cần n ≥ 9 | `KE-HOACH:1488-1519` |
| 7 | Ngưỡng "hữu ích" của β+γ | T3.1 đề xuất: một nửa phân vị 90 của V_r dưới U trên tập phát triển. **Chưa tính** | `T3.1:57-59` |
| 8 | Quy tắc cho quỹ đạo chưa trọn (xả hết / chân trời hữu hạn / điểm số ∞) | Chưa chọn | Codex §9.5 |
| 9 | Nguồn episode và cách chia chọn / hiệu chỉnh / kiểm tra | Xem §9 việc C. Chỉ có 36 ô thật: 20 panel A và 16 panel phát triển. Tầng 2 đã dùng cả hai | Codex §9.2, §17.1 |
| 10 | Tham số thế giới cho ma trận chính (thật so với tự tạo; độ lớn cú sốc) | **Mâu thuẫn cần người dùng quyết.** Phiên cũ đề xuất ưu tiên dữ liệu thật và để thế giới tự tạo làm tập "thử sức chịu đựng" riêng. Nhưng kế hoạch **bắt buộc** Tầng 3 có nhiễu theo cạnh hoặc cặp điểm, có hai chiều và hồi phục sau sốc, vì trôi thật buổi sáng chỉ tăng nên thổi phồng M⁺ | KE-HOACH:1348, :1562 (R4); T3.1:46 |
| 11 | Phép so xác nhận cố định | Đề xuất C-30 so với V-30, cùng episode, chỉ sau việc A | T3.1:43 |
| 12 | Số vòng bootstrap và hạt giống phân tích | Chốt trước khi mở tập kiểm tra | KE-HOACH §8.4 |
| 13 | Ô panel A `d20181114-s10-r1` đã bị nhìn ở smoke T3.5/T3.6 | Loại khỏi tập kiểm tra, hoặc khai báo | T3.7-BAO-CAO:239-246 |
| 14 | Gánh phục hồi chấp nhận được (tỉ lệ quyết định hoặc khách bị ép) | Chưa chốt | T3.7-KE-HOACH:78; Codex §17.2 |
| 15 | Ngân sách thời gian chạy | Chưa chốt. Tham khảo: 6 luồng, 829–2.013 s mỗi job | T3.7-KE-HOACH:79 |
| 16 | Độ chính xác thống kê mong muốn (nửa độ rộng khoảng tin cậy của hiệu ứng ghép cặp chính) | Chưa chốt | T3.7-KE-HOACH:80; Codex §17.2 |
| 17 | T3.8 và T3.9 chạy ở chế độ **thăm dò** hay **chính thức**? | Chính thức cần ADR, builder freeze (KE-HOACH §7.2, 8 bước) và bộ kiểm chứng chấp nhận nhiều mức tắc đường (hiện không). Đề xuất: thăm dò | T3.1:97-98 |
| 18 | **Quy tắc quyết định H2** | Chưa có. Cần chốt: (i) thống kê cho biên δ_b, ví dụ cận dưới khoảng bootstrap ghép cặp theo ô của hiệu E1 phải ≥ δ_b; (ii) điều kiện E2, ví dụ cận trên của hiệu E2 phải ≤ δ_r; (iii) "tồn tại vùng (mức nhiễu, β)" liên hệ thế nào với **một** phép so cố định C-30/V-30; (iv) quy tắc đa phép so | T3.1:43,54-56; KE-HOACH §8.4–8.5 (1521-1534); Codex §17.4 |
| 19 | **Quy tắc đạt của H3 và điểm số** | Chưa có. Cần chốt: điều kiện đạt (cận trên Clopper–Pearson của tỉ lệ episode vi phạm ≤ α, hay coverage thực nghiệm ≥ 1−α); X_r = Σ\|x\| trên các lần sửa giờ trả; nhóm khách (đã hứa hay đã hoàn tất); có tính giờ đón không. `audit_vep.py` chỉ trả tổng theo episode (dòng 155-157), nên phải dựng X theo từng khách (tiền lệ `pilot_analyze` shareDropXAbove60s) | KE-HOACH §8.3 bước 2, 5, 6; Codex §9.1, §9.5 |
| 20 | **Chọn chính sách ở T3.8 là chọn gì** (β ∈ {30, 60, 120}? hàm mục tiêu?) và theo quy tắc nào trên tập chọn | Chưa có | Codex P7 (612-616), §9.2 |
| 21 | Ablation ppm (K12): làm hay bỏ? | Kế hoạch ghi là ablation một yếu tố của Tầng 3, có dự đoán sẵn; chưa làm. Người dùng quyết | KE-HOACH:1350, :1550; T3.1:42 |
| 22 | **Lựa chọn buộc phải hỏi:** episode của T3.8 lấy từ dữ liệu thật hay "thật + nhiễu"? | **(i) Chỉ thật:** thế giới thật không có ngẫu nhiên (sigma = shockRate = 0, nên đổi hạt giống không đổi gì, `world_v1.py:59-74`). Vì vậy mỗi (ngày, mẫu, khung) chỉ cho **một** episode. Panel A có 20 ô, trừ ô đã bị nhìn ở smoke Tầng 3 còn 19; cả 20 ô đều đã dùng ở Tầng 2. Với 0 vi phạm trên 19 episode, cận trên một phía 95% là khoảng 14,6%, **không đạt** 5% hay 10%. **(ii) Thật + nhiễu** (sigma hoặc shock > 0, nhiều hạt giống): đủ episode, nhưng độ lớn nhiễu chưa được hiệu chỉnh (§5.6 mục 6) | Tính tay; KE-HOACH:1507-1513 |
| 23 | **Tập nào được mang claim xác nhận** | Driver của panel phát triển (kể cả ô w07 sao từ w08) có `claimClass: development-exploratory-only`, và cấm "confirmatory-result". Driver panel A có `finite-panel-confirmatory-only`. Vậy chỉ episode dựng từ panel A mới mang được claim xác nhận ở T3.9. Tập hiệu chỉnh và tập kiểm tra phải là **một phép chia ngẫu nhiên của cùng một nguồn** (phân tầng theo ngày, khung) để giữ tính hoán đổi. Nếu không, phải báo là kết quả "thử lệch phân phối" (Codex Q12) | `wp14-development\d20181112-s10-r1-w08.driver.json:19`; KE-HOACH:1509; Codex §17.3 dòng 916 |

**Tính tay cỡ mẫu tập kiểm tra.** Hai agent soát đã kiểm lại các phép tính này. Với 0 episode vi phạm trên m
episode, cận trên một phía 95% là 1 − 0,05^(1/m):
- cần m ≥ 59 để ≤ 5% (KE-HOACH:1507-1513);
- cần m ≥ 29 để ≤ 10%;
- m = 19 cho khoảng 14,6%.

**Cỡ tập hiệu chỉnh.** k = ⌈(n+1)(1−α)⌉; nếu k > n thì γ = ∞:
- α = 0,05: n nhỏ nhất là 19;
- α = 0,10: n nhỏ nhất là 9.

---

## 9. Việc tiếp theo, theo thứ tự đề xuất

### Việc 1 — Sửa errata ở §7 (khoảng nửa ngày, không cần chạy)

Build luận văn sạch sau mỗi lần sửa.

### Việc A — So lại V-30 và M-30 bằng (a) và (b) trên world v1.1

Việc này **quyết định H2 còn tín hiệu hay không**. Khoảng 48 job, ước tính 2,5–4,5 giờ với 6 luồng (829–2.013 s
mỗi job; ⚠️ chưa đo cho V hoặc M trên v1.1), khoảng 4 GB trên ổ C:.

1. **Viết driver mới**, mô phỏng theo `sweep\run_noworse.py`.
   - Danh sách job riêng, vì `run_noworse.jobs` chỉ chọn được M⁺ (`run_noworse.py:30-39`).
   - Nhánh {V-30, M-30} × W0–W5 × {w08, w17}, **hai biến thể**:
     - (a): runner-tier3-v1 + wp4-tier3-v1;
     - (b): runner-tier3-v2 + wp4-tier3-v2.
   - Dùng wrapper `world\preflight_world_v1_1.py`, cwd `E:\Code\RideBound-deadline`.
   - OUT_ROOT mới trên ổ C:, ví dụ `C:\RideBoundData\research\tier3-vm-v11-a` và `…-b`.
   - **LOG_ROOT mới, STOP path mới, nhãn mới.** Log được mở mode `x` (`run_sweep.py:83`), nên dùng lại tên log sẽ
     lỗi sau khi job đã chạy xong.
   - Có thể truyền `--expected-repository-inventory-sha256 0da63eaf2b30ab332fba265a6b2b6e5c36b3ee78950cbac6d6267e60f81e4cbe`
     để hỏng ngay nếu cây nguồn đã đổi. Agent soát đã tính lại: inventory hiện vẫn là giá trị này (1619 tệp).
2. **Viết kế hoạch và dự đoán, rồi niêm phong SHA-256 trước job đầu tiên.** Ví dụ `tang3\vm\VM-PLAN.md` và
   `VM-PLAN.sha256`, theo mẫu `SWEEP-PLAN.sha256`.
   - Viết sẵn thế nào là "C − V(b) dương rõ", ví dụ "≥ 3 khách ở ≥ 6/8 ô có tắc". SWEEP-PLAN §7 đã ghi rằng chênh
     1–2 khách không phải hiệu ứng.
   - Đối chứng bắt buộc: ở W0 (không ép), hành động đội xe của (b) phải bằng (a).
   - Kiểm tham khảo, không bắt buộc bằng hẳn: ở W0 của thí điểm, V-30 = C-30 về số khách (97/97, 95/95) và V không
     bị ép. Các độ trễ thực thi nhỏ vẫn cộng vào V, nên hai bên không nhất thiết trùng hẳn.
   - Kiểm tất định, tùy chọn: so V-30(a) W4-w08 với `tier3-world-v11-smoke\v11-V-30-W4` bằng quyết định. Inventory
     của bản smoke là 9a003f43…, khác bản chạy mới.
   - So với C-30 lấy từ `tier3-sweep-v1`: cùng wrapper và inventory. Phải dùng `run_sweep.effective(...)`, vì
     `C-30-W4-d20181112-s10-r1-w17` chỉ có bản `-rerun1`.
3. **Chạy:** kiểm cắm sạc, `ListAgents`, không có tệp STOP. Báo tiến độ mỗi giờ.
4. **Phân tích:**
   - `sweep_analyze.job_row` dùng lại được, **nhưng** phải ghi đè `OUT_ROOT`, `effective`, `state_of` giống
     `noworse_analyze.py:53-56`. Nếu không, nó sẽ đọc từ `tier3-sweep-v1`.
   - Phần ghép cặp của `sweep_analyze` gắn cứng C với Mplus. `pilot\pilot_paired.py` đã ghép C-30 với V-30 theo nhóm
     khách chung, nhưng chỉ đọc một OUT_ROOT; phải sửa lại cho hai OUT_ROOT.
   - `noworse_analyze.forced_details` và `pilot_analyze.fleet_decisions` dùng lại được.
   - Kiểm audit v/e/p; đếm witness `forcedNoWorse`. Cho một agent độc lập tính lại.
5. **Chỗ rủi ro thật của (b) với V:**
   - Đường **miễn trừ theo chiều ngân sách** ("tổng sau ≤ tổng sau của tuyến giữ") **chưa từng chạy đầu-cuối**.
     Các job M⁺ trước chỉ dùng miễn trừ hạn chót, vì cấu hình Mplus không có hardLimit cho giờ trả.
   - Ba giới hạn cấu trúc bằng 0 thì giống nhau ở C, Mplus và V, nên không phải điểm mới.
   - Phải xác nhận quyết định `forcedNoWorse` của V-30(b) thật sự đi qua đường ngân sách.
   - Nếu job hỏng: mở `failure-00.json`, phân loại theo hằng thông điệp.
6. **Kết quả cần báo:** số khách C / V(a) / V(b) theo từng kiểu tắc; E2; gánh bị ép; tách thật và tự tạo. Kèm hai
   chỗ (b) lệch khỏi Codex §12.3 (§5.5).
   - Nếu C − V(b) đạt mức "dương rõ" đã niêm phong, H2 có tín hiệu.
   - Nếu không đạt, H2 yếu đi, và phải báo trung thực.

### Việc B — Phép thử chỉ dữ liệu thật ở khung 7:00–9:00 (người dùng đã "Oke đấy")

**Chưa ước tính** công sức dựng kịch bản.

1. **Tạo grid mới**, gridId mới (ví dụ `wp14-development-panel-w07-v1`), 8 ô `d2018111{2,3}-s10-r{1..4}-w07`,
   `sourceWindowStartSeconds 25200`, End 32400. Các trường khác chép từ `benchmarks\scenarios\wp14-development\grid-v1.json`.
   - **Không sửa** `grid-v1.json`: hash `1741f8e7…20e5` của nó đã ghim trong `freeze-receipt-v1.json` và `-v2.json`.
   - Đặt tệp grid mới **ngoài** `E:\Code\RideBound-deadline`, ví dụ một thư mục mới trong `C:\Code\RideBound-noworse\benchmarks\scenarios\`.
   - **Quyết định cần ghi lại:** dùng lại selection/pseudonymization label của WP14 hay tạo label mới.
     - Thứ hạng chọn khách băm HMAC theo label, không theo khung (`FleetPyManhattanNormalizer.cs:112-124,627-663`).
     - Nếu dùng lại label, các yêu cầu trong giờ 8–9h có cùng thứ hạng ở w07 và w08, nên dễ chọn trùng khách. Mỗi tệp
       mẫu ngày 12–13/11 có 1.062–1.518 yêu cầu trong giờ 8–9h.
2. **Chạy normalizer** `tools\RideBound.Wp6Normalize`.
   - `--repository` **phải là một cây git có mã normalizer**: công cụ băm 5 tệp
     `<repo>\src\RideBound.Benchmarking\Normalization\*.cs`, và báo lỗi nếu thiếu (`Program.cs:55`,
     `FleetPyNormalizerSourceIdentity.cs:18-37`). Fixture luôn được ghi vào
     `<repo>\benchmarks\fixtures\wp6\public\fleetpy-manhattan-v1\<gridId>\<cellId>` (`Program.cs:91-98`).
   - Dùng `C:\Code\RideBound-noworse`: 5 tệp của nó băm ra `34517a83…aa4d90`, khớp mọi fixture hiện có. Worktree
     này sẽ có thêm tệp fixture chưa theo dõi; không commit chúng nếu chưa quyết.
   - **Tuyệt đối không** dùng `E:\Code\RideBound-deadline`: ghi fixture vào đó làm đổi inventory `0da63eaf…`.
   - Lệnh dạng: `dotnet run --project tools/RideBound.Wp6Normalize -c Release -- normalize --cache E:\RideBoundData\wp6
     --repository C:\Code\RideBound-noworse --accept-license CC-BY-4.0 --grid <grid mới>` (theo
     `docs/benchmarking/wp6-012-public-medium-evidence-2026-08-12.md:62-70`). ⚠️ Chưa chạy thử dạng lệnh này; chưa kiểm
     nó có chạy offline từ cache không.
   - **Không chạy khi đang có job:** build tốn CPU, mà runner có hạn 60 s mỗi phản hồi.
   - Kiểm mỗi ô có 108 yêu cầu, 96 nút, 9.120 cung, và `normalizerSourceSha256 34517a83…`.
   - ⚠️ Chưa kiểm: có ô nào báo `source.node-cap-prevents-target` không. Số yêu cầu thô trong 7–9h là 1.981–2.886
     cho mỗi tệp `sample_10_{1..4}` của ngày 12–13/11.
3. **Fixture và driver:**
   - Chép fixture ra một FIXTURE_ROOT ngoài kho, ví dụ `C:\RideBoundData\research\fixtures-w07-v1\`.
   - Lấy driver w08 làm mẫu, đổi 3 trường `scenarioId`, `sourceScenarioContentSha256`, `sourceScenarioHash`.
   - Preflight nhận đường dẫn ngoài kho (`actual_fleetpy_medium_preflight.py:487-497,801-835`). Tiền lệ:
     `ridebound-scratchpad\window\run_window.py:47`.
   - ⚠️ **Đừng chép `run_window.py` nguyên xi:** dòng 42 của nó gắn cứng `REPO = E:/Code/RideBound`, tức cây chính bị
     cấm. Giữ `REPO = E:/Code/RideBound-deadline` như `run_pilot.py:27`.
4. **Kiểm rò rỉ:**
   - chạy lại `simulators\fleetpy-ridebound\wp14_development_panel_audit.py` với `--repository`, `--development` (grid
     mới), `--frozen` hai lần cho `benchmarks\scenarios\wp9-confirmatory\grid-v2.json` và `grid-v3-veh4.json`, và
     `--output` là tệp mới (`wp14_development_panel_audit.py:166-183`);
   - **thêm** một phép kiểm trùng giữa w07 và w08, vì hai khung dùng chung tệp nhu cầu và trùng giờ 8–9h:
     - so danh sách khách được chọn trong `selection-frame.json` của từng cặp ô cùng (ngày, mẫu); ID khách đã được
       giả danh, nên so bằng thứ tự nguồn;
     - báo số khách trùng. Ô w07 vẫn là tập phát triển, và **không độc lập** với các ô w08 đã xem.
5. **Wrapper world mới (v1.2).** `preflight_world.py:56` chỉ cho phép windowStart 28800 và 61200, và v1.1 thừa kế
   giới hạn này.
   - **Không sửa v1 và v1.1**, vì thí điểm và phép quét đã chạy trên chúng.
   - Viết v1.2, có test, test đột biến và smoke chống rò rỉ, như v1.1.
   - Tệp W5 phải riêng cho từng (ngày, khung). `run_pilot.world_file` hiện chọn W5 **chỉ theo khung**, nên dùng cho
     ô ngày 13/11 sẽ âm thầm áp tắc đường của ngày 12/11.
6. **Chạy**, sau khi niêm phong dự đoán.
   - Đề xuất nhánh: U; C-{30, 60, 120, 300}; Mplus-{30, 60, 120, 300}; V-30; M-30. Tất cả với W5 thật và luật (b).
   - 11 nhánh × 8 ô = 88 job, khoảng 4–8 giờ, khoảng 7–8 GB trên ổ C:.
   - V đáng chạy ở khung này. Trôi thật 7–9h chỉ tăng (bước nhỏ nhất +1,0% ngày 12/11 và +1,2% ngày 13/11), nên
     theo hệ quả chiều trôi thì M⁺ = M = V ở đây.
   - Kết quả là **thăm dò**, vì ô w07 mang claim `development-exploratory-only`.
   - Dự đoán của phiên cũ, **chưa phải kết quả**: M⁺ sẽ thất hứa ở 60–120 s trên khung này.

### Việc C — T3.8: chọn chính sách và hiệu chỉnh conformal (H3)

Làm sau khi người dùng chốt §8.

1. **Viết mã conformal**, đề xuất bằng Python trong scratchpad, ví dụ `tang3\calib\`, có test và test đột biến như
   `tang3\oracle\`.
   - Nếu đặt mã trong kho thì phải có ADR, docs/18, docs/19 và `dotnet test`.
   - Làm đúng KE-HOACH §8.3: thứ hạng nguyên, không nội suy. k = ⌈(n+1)(1−α)⌉; nếu k > n thì γ = ∞, dùng cờ vô hạn,
     **không** mã hóa thành số lớn.
   - Đầu vào (Codex E04): hash chính sách đã đóng băng, manifest chia tập, bảng điểm số.
   - Test bắt buộc:
     - với α = 0,05: n=18 → ∞; n=19 → k=19; n=20 → k=20;
     - với α = 0,10: n=8 → ∞; n=9 → k=9; n=20 → k=19;
     - có hạng bằng nhau; k = n+1; tràn số nguyên.
   - Thêm test theo Codex Q01–Q07: kiểm trùng world, rò nhóm, episode rỗng, khách chưa trọn vòng đời.
2. **Dựng điểm số theo từng khách** theo quyết định ở §8 dòng 19. `audit_vep.py` chỉ trả tổng theo episode.
3. **Chọn rồi đóng băng** chính sách C (cấu hình, runner, wrapper) theo quy tắc ở §8 dòng 20, trước khi hiệu chỉnh.
   Nếu đổi chính sách thì phải hiệu chỉnh lại trên tập mới.
4. **Niêm phong dự đoán H3 có sẵn trong kế hoạch** trước khi hiệu chỉnh (KE-HOACH:1551):
   - γ dưới trôi dạt sẽ lớn hơn nhiều so với 8,7 s của panel tĩnh (d p90 = 47,4 s, max 150,7 s ở k=1);
   - xác nhận nếu có cận hữu hạn với n ≥ 19;
   - bác bỏ nếu γ rộng hơn ngưỡng hữu ích.
5. **Tập episode**, người dùng chốt theo §8 dòng 9, 22, 23:
   - Tập chọn và phát triển: `d20181112-s10-r1` đã dùng nhiều, chỉ còn làm tập phát triển.
   - Chỉ episode dựng từ panel A mới mang được claim xác nhận. Hiệu chỉnh và kiểm tra phải là phép chia ngẫu nhiên
     của cùng một nguồn.
   - Nếu chọn "thật + nhiễu", nhiều hạt giống trên cùng ô làm tính độc lập yếu đi, và phải nói rõ.
6. **Driver cho panel A:**
   - `run_pilot.py:38-39` gắn cứng fixture và driver của `wp14-development`.
   - Panel A: fixture ở `benchmarks\fixtures\wp6\public\fleetpy-manhattan-v1\wp9-confirmatory-fixed-panel-v2\`, driver ở
     `benchmarks\scenarios\wp9-confirmatory\d2018111X-s10-rN.driver.json`. Tiền lệ: `deadline\run_deadline.py:38-39`.
   - Tệp W5 phải riêng cho từng (ngày, khung). Nếu không, sẽ âm thầm áp tắc đường của ngày 12/11 cho mọi ngày.
7. **Ngưỡng hữu ích** (§8 dòng 7) phải tính trên tập phát triển **trước** khi hiệu chỉnh. Hiện U chỉ có trên
   `d20181112-s10-r1`, nên cần chạy U trên tập phát triển đã chọn.
8. **Báo cáo:** coverage theo episode (mẫu số, số vi phạm, khoảng Clopper–Pearson), độ rộng β+γ so với ngưỡng hữu
   ích, tỉ lệ phục vụ. **Không cắt γ.** Kết quả âm cũng báo.

### Việc D — T3.9: xác nhận trên ma trận khóa (H2)

- **Khóa ma trận và ước tính trước:** nhánh, lưới β cho đường biên (E1, E2), world hoặc mức nhiễu, số episode, luật
  phục hồi, runner, phiên bản wrapper.
  - Ví dụ 59 episode × 7 nhánh ≈ 413 job ≈ 20–40 giờ ≈ 35 GB.
  - Ổ C: hiện dư khoảng 53 GB so với mức sàn 50 GB, nên vừa đủ nhưng sát. Phải tính lại trước khi chạy.
- Chạy ma trận ghép cặp đã khóa trên tập kiểm tra, ghi mọi thất bại (Codex E03): mỗi (episode, nhánh) phải có bản
  ghi lần thử.
  - Hiện **chưa có** sổ ghi lần thử, cũng chưa có lệnh kiểm bundle. Phải quyết: dựng cây artifact theo Codex §16.1,
    hay kiểm trực tiếp từ các thư mục output hiện tại.
- Quyết H2 theo quy tắc đã niêm phong ở §8 dòng 18.
  - Khoảng tin cậy bootstrap ghép cặp **theo ô** (không theo khách). Số vòng và hạt giống chốt trước.
- Kiểm sàn phục vụ so với U; phép so C-30 với V-30 cố định; đường biên (E1, E2) theo β.
- Có một lệnh tính lại bảng chính từ bundle (Codex E06).
- Thế giới "thử sức chịu đựng" báo riêng.

### Việc E — Cập nhật sau mỗi việc

- **Luận văn:** Ch.4 `muc:quet`, và các mục mới cho V, 7–9h, T3.8, T3.9. Cập nhật Ch.1, Ch.5, tóm tắt và bảng quy mô.
  Build sạch.
- **Kho `C:\Code\RideBound-noworse`:** docs/18 (dòng đầu, ADR mới nếu có khóa hoặc luật mới, change history) và docs/19
  (§32+).
  - Có sửa mã thì chạy `dotnet test RideBound.slnx` (mốc hiện tại 1025/1025) và cho review độc lập.
  - Commit và push lên nhánh nghiên cứu đã được duyệt. Commit kho luận văn để người dùng làm.
- **Memory:** cập nhật `ridebound-handoff-2026-09-23.md` (hoặc tệp mới) và `MEMORY.md`.

### Việc F — Tùy chọn, hỏi người dùng

- Thêm mô hình khách từ chối theo bài báo, e^(−0,5·RD), cho cả hai luật. Khoảng 1 ngày.
- Chạy dữ liệu Hamburg: cần bộ chuyển đổi và sửa `op_max_wait_time` (cố định 600 s). Khoảng 1–2 ngày. Phiên cũ
  **không** khuyến nghị, vì dữ liệu Hamburg không có tắc đường thay đổi nên hai luật sẽ trùng nhau.

---

## 10. Bẫy kỹ thuật (tóm tắt; đầy đủ ở `ridebound-env-traps.md` và bản 23/09 §11)

- **Không sửa, build hay ghi fixture** trong worktree mà job đang dùng: preflight băm cây nguồn lúc đầu và lúc cuối
  mỗi job (`actual_fleetpy_medium_preflight.py:740-782,872-884`).
- **Mỗi driver có LOG_ROOT và STOP riêng:**
  - `sweep\logs` và `sweep\STOP` (`run_sweep.py:30,32`);
  - `sweep\logs-noworse` (`run_noworse.py:29`);
  - `pilot\logs` và `pilot\STOP` (`run_pilot.py:33,40`).
  Log mở mode `x`: driver mới phải dùng thư mục và nhãn mới.
- **Không chạy `dotnet build` hay `dotnet test` song song với job:** runner client có hạn 60 s mỗi phản hồi.
- **Máy ngủ giết job:** kiểm cắm sạc (`Get-CimInstance Win32_Battery`, BatteryStatus 2 = cắm sạc). Có lúc lệnh này
  không trả dòng nào; driver thì kiểm bằng `GetSystemPowerStatus`. Driver đã gọi `SetThreadExecutionState`. Muốn tạm
  dừng thì chỉ suspend PID driver.
- **Python:** luôn `-B` và `PYTHONDONTWRITEBYTECODE=1`. Không import module test của scratchpad (chúng gọi `SystemExit`).
- **Tiếng Việt:** dùng công cụ Edit/Write, không dùng heredoc hay sed.
- **Đếm vi phạm:** dùng `nonNormalCertificates`, witness hoặc incident ledger, không dùng BreachCount. Cột
  `M5_forcedBreaches` chỉ đếm `forcedReference`: ở (b) thiếu 50 breach `forcedNoWorse`.
- **Không dùng** `wp14_frontier_analyze.py`, `wp14_mechanism_probe.py`, `wp13_recorded_witness_relaxation.py` trên
  output có hạn chót hoặc phục hồi.
- **Khi quét thư mục output**, bỏ 12 thư mục W4 gốc không có summary; dùng bản `-rerun1`.
- **So quyết định** bằng chuỗi hành động đội xe đã xác nhận (`pilot_analyze.fleet_decisions`), không so bằng
  semanticHash.
- **E2** dùng mẫu số là khách của chính nhánh đó. Nhóm khách chung chỉ để chẩn đoán.
- **Khoảng tin cậy** tính theo ô hoặc ngày, không theo khách.

---

## 11. Đoạn dán vào đầu phiên mới

> Tôi là Trần Quang Thành (23020155, UET/VNU), làm khóa luận RideBound. Trước khi làm bất cứ việc gì, hãy đọc
> **toàn bộ** `E:\Code\Report_INT3508\BAN-GIAO-PHIEN-2026-09-29.md`, rồi đọc đủ danh sách ở §0 của tệp đó (luật
> chơi ở `BAN-GIAO-PHIEN-2026-09-23.md` §2, §9, §11, §12; kế hoạch `KE-HOACH-HOP-NHAT-2026-09-23.md` §6 Tầng 3, §7,
> §8; các tệp Tầng 3 trong `ridebound-scratchpad\tang3\`; docs/18 và docs/19 ở `C:\Code\RideBound-noworse`).
> Sau đó làm tiếp Tầng 3 theo §9: việc 1 (sửa errata), rồi việc A (so lại V/M bằng luật phục hồi (b)), việc B (khung
> 7–9h chỉ dữ liệu thật), rồi T3.8 và T3.9. Trước T3.8, hỏi tôi các quyết định ở §8.
> Không bịa; chưa kiểm thì ghi "chưa kiểm". Không xóa tệp nào. Không sửa worktree mà job đang dùng. Báo tiến độ
> mỗi giờ khi có job dài. Hỏi tôi tên cán bộ hướng dẫn; không commit kho luận văn. Phiên cũ chỉ trả lời câu hỏi và
> không sửa tệp. Trả lời tôi bằng tiếng Việt, câu tự nhiên, tránh thuật ngữ và chữ tắt, giải thích đơn giản kèm
> ví dụ thật từ hệ thống.
