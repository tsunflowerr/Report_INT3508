# governance

## 1. [BAN-GIAO: file size and table of contents]
File has 706 lines. Headings (line: heading): 1 '# RideBound — Bàn giao toàn bộ bối cảnh cho phiên AI mới (phiên kết thúc 2026-09-23)'; 24 '## 0. Đọc cái gì, theo thứ tự nào — BẮT BUỘC trước khi làm bất cứ việc gì'; 28 '### Nhóm A — bắt buộc, đọc hết'; 42 '### Nhóm B — đọc khi làm tới phần liên quan'; 55 '### Nhóm C — bài báo gốc'; 62 '## 1. Người dùng, đề tài, mục tiêu'; 88 '## 2. Ràng buộc bắt buộc — còn hiệu lực (cập nhật 2026-09-23)'; 90 '### 2.1 Ràng buộc của người dùng'; 127 '### 2.2 Ràng buộc của kho (AGENTS.md — ghi đè mọi mặc định)'; 144 '### 2.3 Kỷ luật trung thực — không thương lượng'; 158 '## 3. Bản đồ tệp và môi trường'; 160 '### 3.1 Kho mã'; 173 '### 3.2 Dữ liệu và công cụ'; 187 '### 3.3 Báo cáo khóa luận LaTeX'; 200 '### 3.4 Kế hoạch, bàn giao, script'; 211 '### 3.5 Bài báo'; 251 '## 4. Hệ thống RideBound trong một trang'; 289 '## 5. Diễn biến và kết quả của chuỗi phiên 16/09 → 23/09'; 291 '### 5.1 Việc đã làm, theo thời gian'; 306 '### 5.2 Các lỗi đã mắc và đã sửa'; 324 '### 5.3 Script đo (18 tệp)'; 351 '### 5.4 Báo cáo LaTeX — đã sửa (Tầng 0 phần T0.1)'; 365 '## 6. Số liệu đã kiểm chứng — dùng được trong khóa luận (kèm nguồn)'; 396 '## 7. Đóng góp đã chốt, định lý, ranh giới claim'; 398 '### 7.1 Định lý 4 — bản có điều kiện'; 424 '### 7.2 Tương ứng lý thuyết'; 432 '### 7.3 Định vị văn liệu'; 444 '### 7.4 Được tuyên bố'; 453 '### 7.5 KHÔNG được tuyên bố (❌) — tổng hợp'; 474 '## 8. Kế hoạch — tóm tắt và trạng thái'; 476 '### 8.1 Bốn tầng'; 486 '### 8.2 Tầng 0 — việc còn lại'; 510 '### 8.3 Tầng 2 — quy trình thực thi'; 564 '### 8.4 Tầng 1 — việc còn lại'; 576 '## 9. Giao thức chống ảo giác và bảo đảm chất lượng — BẮT BUỘC cho mọi bước'; 578 '### 9.1 Trước khi viết mã hoặc văn bản'; 590 '### 9.2 Khi viết mã'; 599 '### 9.3 Review sau mỗi thay đổi có ý nghĩa'; 608 '### 9.4 Khi chạy mô phỏng và phân tích'; 618 '### 9.5 Khi viết khóa luận'; 627 '## 10. Quyết định còn mở — mặc định đã chọn cho phiên sau'; 643 '## 11. Bẫy kỹ thuật — tổng hợp'; 681 '## 12. Những việc KHÔNG làm'; 694 '## 13. Đoạn dán vào đầu phiên mới'.
SOURCE: Grep '^#{1,4} ' on E:\Code\Report_INT3508\BAN-GIAO-PHIEN-2026-09-23.md; Read reported 706 lines total

## 2. [BAN-GIAO §13 standing instructions (VERBATIM)]
> Tôi là Trần Quang Thành (23020155, UET/VNU), đang làm khóa luận về RideBound — hệ điều phối xe đi chung
> có "lời hứa có biên được chứng nhận". Trước khi làm bất cứ việc gì, hãy đọc **toàn bộ**
> `E:\Code\Report_INT3508\BAN-GIAO-PHIEN-2026-09-23.md`, rồi đọc đủ **nhóm A** trong §0 của tệp đó
> (`AGENTS.md`, `docs/00`, `docs/01`, `docs/18`, `docs/16`, `docs/03`, `docs/tasks/47`, và toàn bộ kế hoạch
> `E:\Code\Report_INT3508\KE-HOACH-HOP-NHAT-2026-09-23.md`). Sau đó thực hiện kế hoạch **từng bước** theo
> §8 và §10 của tệp bàn giao, tuân thủ tuyệt đối §2 (ràng buộc) và §9 (giao thức chống ảo giác: đọc mã
> trước khi viết, test sau mỗi thay đổi, review độc lập, báo cáo trung thực). Không bịa bất cứ thứ gì;
> chưa kiểm thì ghi "chưa kiểm". Không xóa tệp nào. Báo tiến độ mỗi giờ khi có job dài. Hỏi tôi trước khi
> commit/push, trước khi bắt đầu Tầng 3, và để lấy tên cán bộ hướng dẫn. Trả lời tôi bằng tiếng Việt, giải
> thích đơn giản kèm ví dụ thật từ hệ thống.
SOURCE: E:\Code\Report_INT3508\BAN-GIAO-PHIEN-2026-09-23.md:694-705

## 3. [BAN-GIAO header: concurrent-session check]
Update 2026-09-24 00:15: another session (`ridebound-ef`) started Tier 2, created worktree E:\Code\RideBound-deadline (branch research/deadline-gate from 41a4e11), hit a CRLF trap fixed by ridebound-scratchpad\deadline\restore_index_bytes.py; logs in ridebound-scratchpad\deadline\logs\. Rule: before any Tier 2 work 'kiểm xem có phiên nào khác đang làm trong worktree không (ListAgents, thời điểm sửa của logs\), đọc nhật ký, và không làm trùng/đè lên việc của phiên kia'. E:\RideBoundData is 90 GB (du 24/09), not 33.6 GB.
SOURCE: E:\Code\Report_INT3508\BAN-GIAO-PHIEN-2026-09-23.md:8-15

## 4. [BAN-GIAO: document authority / conflict rule]
Highest authority on the plan: E:\Code\Report_INT3508\KE-HOACH-HOP-NHAT-2026-09-23.md (1.751 lines, 'Sửa đổi 1'). Handoff = 'bản đồ và luật chơi'; plan = 'đặc tả chi tiết'. On technical-detail conflicts the plan wins; on user-constraint conflicts the handoff wins (newer).
SOURCE: E:\Code\Report_INT3508\BAN-GIAO-PHIEN-2026-09-23.md:17-20

## 5. [BAN-GIAO §0: mandatory reading gate]
Verbatim: 'Không được viết một dòng mã, sửa một dòng LaTeX, hay chạy một mô phỏng nào trước khi đọc xong nhóm A.' Group A: A1 the handoff itself; A2 E:\Code\RideBound\AGENTS.md; A3 docs\00-index.md; A4 docs\01-research-charter.md; A5 docs\18-status-and-decision-log.md (flagged stale vs 41a4e11: says 009_MATRIX_HALTED_40_OF_160 while committed evidence is 160/160); A6 docs\16-roadmap-and-work-packages.md active WP; A7 docs\03-related-work-and-claim-boundary.md; A8 KE-HOACH-HOP-NHAT-2026-09-23.md whole, at minimum §1, §2 (K1–K22), §2.1, §5.2, §5.6, §6 Tầng 0–2, §7, §8, §9, §10; A9 docs\tasks\47-wp15-lifecycle-commitment-refinement.md (locked WP15 constraints #2,#3,#4,#7).
SOURCE: E:\Code\Report_INT3508\BAN-GIAO-PHIEN-2026-09-23.md:26-40

## 6. [BAN-GIAO §0: group B pointers]
Before proposing any new direction read E:\Code\Report_INT3508\RIDEBOUND-BAN-GIAO-CONTEXT.md (2026-09-16, 1.168 lines): §8 (eight dead directions + evidence), §12 (traps 12.1–12.10), §5 (run infra, transcript reading), §7 (558 runs), §13 (old constraints), §17 (what must not be claimed). Codex plan ...\conduct-outcome-plan-2026-09-22\KE-HOACH-END-TO-END-CONDUCT-OUTCOME-STOCHASTIC.md is superseded but its backlog §14–15 (tickets C01–C08, A01–A07, P01–P08, S01–S07, E01–E06; test matrix M/G/W/Q) is the detail source for Tầng 3. KE-HOACH-NGHIEN-CUU-2026-09-22.md superseded (history only). LaTeX thesis at E:\Code\Report_INT3508\ridebound\noi-dung\*.tex.
SOURCE: E:\Code\Report_INT3508\BAN-GIAO-PHIEN-2026-09-23.md:44-53

## 7. [User identity]
Trần Quang Thành — MSSV 23020155 — lớp K68I-IT2 — Trường ĐH Công nghệ (UET), ĐHQGHN. Writes Vietnamese; wants explanations 'đơn giản, dễ hiểu, có ví dụ thực tế từ chính hệ thống', enough to present to others. Use gender-neutral pronouns when referring to the user.
SOURCE: E:\Code\Report_INT3508\BAN-GIAO-PHIEN-2026-09-23.md:64-66

## 8. [Supervisor name rule]
Verbatim: '**Tên cán bộ hướng dẫn:** **chưa biết** — `noi-dung/00-bia.tex` còn `[chờ bổ sung]`. **Phải hỏi người dùng**, không được tự điền.' Also §8.2 T0.2.10 'Tên CBHD — hỏi người dùng' and §10 row 'Tên CBHD | Hỏi người dùng | Chỉ người dùng biết'. Memory: 'Supervisor name is unknown — always ask, never fill it in.' and still listed as open ask on 2026-09-29.
SOURCE: E:\Code\Report_INT3508\BAN-GIAO-PHIEN-2026-09-23.md:70-71, :504, :637; C:\Users\quang\.claude\projects\e--Code-RideBound\memory\user-profile.md:11; memory\ridebound-handoff-2026-09-23.md:36

## 9. [User grading criteria (verbatim)]
*"Bài toán thực tế không? Quan trọng không? Đáng làm không?"* / *"Giải pháp có hợp lý không? Phương pháp/Lý luận → Mới hơn so với đối thủ hoặc có các giới hạn tốt hơn (chi phí rẻ hơn/thời gian nhanh hơn…)"* / *"Minh chứng thông qua kết quả: Định lượng (Nghiên cứu) / Định tính (Demo)"*. User originally wanted real 'khác biệt' (approach/algorithm/trade-off), not just different metrics.
SOURCE: E:\Code\Report_INT3508\BAN-GIAO-PHIEN-2026-09-23.md:72-79

## 10. [User constraint 2.1.1 — no deletion (verbatim)]
'**Không xóa bất kỳ tệp nào của người dùng** — kể cả tệp trông "linh tinh", tệp tạm, kết quả cũ, corpus, dữ liệu tải về, vendor checkout, artifact kết quả. *"Không tùy tiện xóa file quan trọng gây hư hại máy."* Nếu thấy cần xóa, **hỏi trước**.'
SOURCE: E:\Code\Report_INT3508\BAN-GIAO-PHIEN-2026-09-23.md:92-94

## 11. [User constraint 2.1.2 — disk policy (verbatim user quote + thresholds)]
User said 2026-09-23: *"việc quá dung lượng thì không sợ miễn không xóa các file linh tinh trong máy của tôi, đảm bảo máy vẫn đủ dung lượng thoải mái không gây ảnh hưởng nghiêm trọng đến máy tính, còn đâu toàn bộ do AI lúc đó có thể quyết định."* Old '< 30 GB' cap no longer a barrier; keep E: ≥ 40 GB free and C: ≥ 50 GB free (AI-proposed). Check before/after big runs with PowerShell Get-PSDrive; do NOT use `du -sh E:/RideBoundData` (>5 min).
SOURCE: E:\Code\Report_INT3508\BAN-GIAO-PHIEN-2026-09-23.md:95-103

## 12. [User constraint 2.1.3 — decision authority and what still requires asking]
AI may execute Tầng 0–2 including code changes in a separate git worktree with §10 defaults. Must still ASK the user when: deleting files; push/commit to remote or any off-machine action; filling the supervisor name; reversing a decision locked in the plan; starting Tầng 3.
SOURCE: E:\Code\Report_INT3508\BAN-GIAO-PHIEN-2026-09-23.md:104-109

## 13. [User constraint 2.1.4 — main repo tree untouchable (verbatim core)]
'**Không đụng cây làm việc chính của kho `E:\Code\RideBound`.**' It holds uncommitted user changes: docs/benchmarking/wp14r-013-v6-matrix-and-h6-rerun-2026-09-05.md (38 lines modified) and untracked docs/benchmarking/Kết quả benchmark.md — '**Giữ nguyên tuyệt đối.**' Code changes only in a worktree; scripts, experimental configs, intermediate results go outside the repo: E:\Code\Report_INT3508\ridebound-scratchpad\... and E:\RideBoundData\....
SOURCE: E:\Code\Report_INT3508\BAN-GIAO-PHIEN-2026-09-23.md:110-114; memory\ridebound-standing-constraints.md:12

## 14. [User constraint 2.1.5 — hourly progress]
'**Báo tiến độ mỗi 1 giờ** khi có job dài đang chạy.'
SOURCE: E:\Code\Report_INT3508\BAN-GIAO-PHIEN-2026-09-23.md:115; memory\ridebound-standing-constraints.md:13

## 15. [User constraint 2.1.6 — old report sections 4–7]
'Người dùng đã tự xóa các mục 4–7 trong bản báo cáo tiếng Việt cũ của họ — TUYỆT ĐỐI KHÔNG thêm lại.' Applies to the old document, NOT to the LaTeX thesis ridebound/.
SOURCE: E:\Code\Report_INT3508\BAN-GIAO-PHIEN-2026-09-23.md:116-117; memory\ridebound-standing-constraints.md:14

## 16. [User constraint 2.1.7 — internship report untouchable]
Do not touch the internship report at root E:\Code\Report_INT3508\ (main.tex, noi-dung/00-bia.tex … 09-trang-danh-gia.tex, Baocaothuctap_23020155_TranQuangThanh.pdf, and C:\Users\quang\Downloads\Baocaothuctap_23020155_TranQuangThanh.docx) — KiotViet internship report, different from the thesis, has uncommitted user changes.
SOURCE: E:\Code\Report_INT3508\BAN-GIAO-PHIEN-2026-09-23.md:118-121; memory\ridebound-standing-constraints.md:15

## 17. [User constraint 2.1.8 — email]
Never send the user's email (thanh.tq2@kiotviet.com) to any external service.
SOURCE: E:\Code\Report_INT3508\BAN-GIAO-PHIEN-2026-09-23.md:122

## 18. [User constraint 2.1.9 — system safety]
No system software install, no machine config change, no killing user processes (old allowance to stop unused background programs if RAM short — only when truly needed and state what was stopped).
SOURCE: E:\Code\Report_INT3508\BAN-GIAO-PHIEN-2026-09-23.md:123-125

## 19. [Repo constraint (handoff §2.2) — docs updates location]
When a task changes implementation status, contracts, claims, baselines, metrics, repo boundaries or next actions: update docs/18-status-and-decision-log.md, the decision entry, and docs/19-requirement-traceability.md — done IN the worktree/research branch, not the main tree.
SOURCE: E:\Code\Report_INT3508\BAN-GIAO-PHIEN-2026-09-23.md:132-135

## 20. [Honesty discipline §2.3 (verbatim core)]
'**Không bịa.** Không bịa số, không bịa kết quả chạy, không bịa dòng mã, không bịa trích dẫn, không bịa nội dung bài báo. Không biết thì đọc; không đọc được thì ghi ⚠️ "chưa kiểm".' Every code claim needs file:line read in the current session; plan line numbers may drift — grep again before editing. Every thesis number must trace to a script + data file, or a section/table of a read paper. Red test → report red with output; skipped step → say skipped; negative results are valid and recorded like positive ones (WP15 constraint #7). No overstatement (see ❌ list).
SOURCE: E:\Code\Report_INT3508\BAN-GIAO-PHIEN-2026-09-23.md:146-154

## 21. [Environment: Python interpreter]
E:\RideBoundData\wp7\envs\fleetpy-1.0.2\python.exe is the only usable Python (`python` not in Git Bash PATH). Measurement scripts run as `PYTHONIOENCODING=utf-8 E:/RideBoundData/wp7/envs/fleetpy-1.0.2/python.exe -B <script>.py` after cd into script dir (analyze1/2 read b1_paths.pkl relatively).
SOURCE: E:\Code\Report_INT3508\BAN-GIAO-PHIEN-2026-09-23.md:181, :326-329; memory\ridebound-env-traps.md:11

## 22. [Environment: data root never delete]
E:\RideBoundData\ holds all data, envs and experiment results (90 GB, du 24/09). '**Không xóa gì**'.
SOURCE: E:\Code\Report_INT3508\BAN-GIAO-PHIEN-2026-09-23.md:177

## 23. [Environment: traffic-factor CSV column]
...\FleetPy_Manhattan\networks\Manhattan_2019_corrected\2018-11-{11..18}_tt_factors.csv, 15-min step; use column `travel_time_factor` (a past misread used `time_interval`); always print header first.
SOURCE: E:\Code\Report_INT3508\BAN-GIAO-PHIEN-2026-09-23.md:184, :321; memory\ridebound-env-traps.md:16

## 24. [LaTeX thesis build and conventions]
Thesis at E:\Code\Report_INT3508\ridebound\ (subfolder of the user's own git repo E:\Code\Report_INT3508, not the RideBound repo). Build: cd ridebound then `..\tools\tectonic.exe -X compile main.tex --outdir .` (memory adds `--keep-logs`, otherwise main.log is NOT rewritten — check main.log timestamp). No poppler/pdftotext — check dangling refs/Overfull via main.log. Theorem envs: `dinhly` (per chapter), `hequa` shares counter with `dinhly`, `dinhnghia` has its own counter; always \label/\ref, never hand-number (trap 12.9). Chapter files: 00-bia (missing supervisor), 01-loi-cam-on, 02-tom-tat, 03-muc-luc, 04-viet-tat, 05-chuong1, 06-chuong2, 07-chuong3 (method + theorems), 08-chuong4 (experiments), 09-chuong5, 10-tai-lieu.
SOURCE: E:\Code\Report_INT3508\BAN-GIAO-PHIEN-2026-09-23.md:185, :189-198; memory\ridebound-env-traps.md:15

## 25. [Allowed wording for Theorem 4]
Write: *"Cổng hành vi không bao giờ là nguyên nhân khiến tập phương án rỗng."* Do NOT write *"hệ thống dùng cổng hành vi không bao giờ kẹt"*. Say plainly the proof is elementary ('Chứng minh sơ cấp'); value lies in the comparison frame and empirical checks.
SOURCE: E:\Code\Report_INT3508\BAN-GIAO-PHIEN-2026-09-23.md:414-416

## 26. [Claim-level ladder]
Claim level by progress: before Tầng 2 'chứng minh + giải thích hậu nghiệm'; after 2A 'xác nhận cơ chế có đối chứng'; after 2B 'xác nhận trên tập giữ lại, cả hai chiều trôi'.
SOURCE: E:\Code\Report_INT3508\BAN-GIAO-PHIEN-2026-09-23.md:448-450

## 27. [NOT to be claimed (❌ list §7.5)]
Must not claim: first per-rider ETA guarantee / first instability control (Elmi 2026); total-variation bounding as differentiator (Mệnh đề 2); B = A + d as equality; d as pure traffic effect; delayed commitment, least-commitment, time consistency, dynamic insertion, ETA limit, reassignment, route similarity, user satisfaction as novel; superior service rate (every committed config serves less); stronger than Fielbaum 2020, '585× better', absolute-number comparisons with literature; Gini for zero-heavy burden; CIs computed over riders; results on 'Manhattan road network'; drift results 'verified' (not through verifier); using Zalesak '+7,1 pp' to offset '−7,13 pp'; 'system with conduct gate never gets stuck/infeasible'; calling the 9 k=1 cells or 4/4 retrodiction 'confirmation'; McNemar p-value as main Tier 2 evidence; harm-only ledger as novel; Theorem 4 proof as hard/deep; 'lower bound' vs reassigning baseline (drift on main panel as 'lower bound' only with explanation).
SOURCE: E:\Code\Report_INT3508\BAN-GIAO-PHIEN-2026-09-23.md:453-470

## 28. [Tier structure and 'ask before Tier 3']
Four tiers, a complete thesis at any stopping tier: 0 LaTeX fixes; 1 extra analysis on sealed data; 2 Theorem-4 confirmation (2A panel A 20 cells dl-30/60/120 × k∈{0,1}; 2B dev panel 16 cells k=1 conduct-30, visible-30, dl-30, dl-120, dl2-30; ~240 runs); 3 failure-aware core + stochastic world + episode conformal — 'chỉ khi Tầng 2 có tín hiệu; hỏi người dùng trước khi bắt đầu'; 4 WP15 redesign (separate paper, awaiting ADR).
SOURCE: E:\Code\Report_INT3508\BAN-GIAO-PHIEN-2026-09-23.md:476-484

## 29. [Tier 0 ordering rule]
Tier-0 passages about Tier-2 results (e.g. sentence T2.10) are written only AFTER Tier 2 has results; before that ch4 only has post-hoc tables with correct labels.
SOURCE: E:\Code\Report_INT3508\BAN-GIAO-PHIEN-2026-09-23.md:507-508

## 30. [Tier 2 procedure rules (baseline, no test edits, controls)]
Worktree command `git worktree add ..\RideBound-deadline -b research/deadline-gate 41a4e11`; baseline `dotnet test RideBound.slnx` recording pass/fail before edits; if red is StrictBagItBundleTests expecting GitDirty = true, confirm pre-existing on main tree, record, do NOT fix the test. Runner publish root must not change during runs. Two controls (ctl-conduct-k0, ctl-visible-k0) compare DECISIONS via levelc/decision_identity.py, labels and cell sets — not message text; a decision mismatch in even one cell ⟹ stop and investigate. Do not modify original drift/preflight_drift.py. Preregistration (PREREGISTRATION.md + predictions.csv + SHA-256 + UTC time) sealed before predicted arms. Label `selection-noop-invariant` ⟹ implementation bug, stop. 'Không bao giờ đếm lỗi thay cho phân loại lỗi.'
SOURCE: E:\Code\Report_INT3508\BAN-GIAO-PHIEN-2026-09-23.md:512-548

## 31. [Tier 2 thresholds locked]
Locked, not to change after seeing results: 2B 'xác nhận trên tập giữ lại' when per-cell prediction correct ≥ 90% of evening pairs AND w17 row direction correct; negation when < 75%, or dl-30 evening infeasible by deadline-late ≥ 3/8, or dl2-30 and visible-30 evening both ≤ 2/8.
SOURCE: E:\Code\Report_INT3508\BAN-GIAO-PHIEN-2026-09-23.md:552-555

## 32. [Commit policy (handoff)]
§8.3 step 13 verbatim: '**Không commit/push** khi chưa hỏi người dùng.' §10 row: 'Commit / push | **Hỏi người dùng** | Thao tác ngoài phạm vi đã giao'. Results labelled **thăm dò** (exploratory); docs/18, docs/19 + decision entry updated in worktree/branch only.
SOURCE: E:\Code\Report_INT3508\BAN-GIAO-PHIEN-2026-09-23.md:556-558, :636

## 33. [Anti-hallucination protocol §9.1]
Read the target file region in the current session; grep again every line number from the plan; check every spec assumption in real code (type names, signatures, members e.g. InsertionCandidate.IsNoOp, CandidatePruneWitness.Code/Message/CandidateId); plan sample code is a sketch — if it deviates follow real code and record the deviation; write down invariants (default off; B1–B4 unchanged; boundary `>` not `≥`; one-sided does not catch candidate < anchor; conduct-gate no-op never rejected; change 6 alters no successful run).
SOURCE: E:\Code\Report_INT3508\BAN-GIAO-PHIEN-2026-09-23.md:580-588

## 34. [Anti-hallucination protocol §9.2 coding]
Follow surrounding idioms (ArgumentException in Domain; InvalidDataException in Runner config; English in code). Tests written with or before code, each boundary (equal, +1, negative, null) its own test. Run targeted `dotnet test <project> --filter <class>` then full `dotnet test RideBound.slnx`, record pass/fail/skip vs baseline. 'Không đổi test hiện có để nó xanh. Không dùng `--no-verify`, không tắt analyzer.'
SOURCE: E:\Code\Report_INT3508\BAN-GIAO-PHIEN-2026-09-23.md:592-597

## 35. [Anti-hallucination protocol §9.3 review]
`git diff` in worktree, read every line vs spec; independent review by a FRESH-CONTEXT subagent given diff + spec (not own conclusions) to find logic errors, missing edge cases, invariant violations, sign/boundary errors, untested paths, leakage into B1–B4; handle every finding, record rationale for rejected ones; hand-check numeric cases CE-1…CE-6 and (a)–(k); proceed only when tests green (except confirmed exceptions) and no open findings.
SOURCE: E:\Code\Report_INT3508\BAN-GIAO-PHIEN-2026-09-23.md:601-606

## 36. [Anti-hallucination protocol §9.4 simulation]
Runner controls before any new arm; mismatch = stop. Reproduce scripts before use (e.g. harmledger.py; cellpred.py must give 54…102). Every failed run: open failure-00.json, classify by message constant, don't guess. Seal preregistration BEFORE running predicted arms; never change thresholds, windows, cells after viewing. Hourly progress; save intermediate results; scripts have a 'reused' mode to resume.
SOURCE: E:\Code\Report_INT3508\BAN-GIAO-PHIEN-2026-09-23.md:610-616

## 37. [Anti-hallucination protocol §9.5 thesis writing]
Each numeric sentence traceable to handoff §6, the plan, or a new scripted result. Build LaTeX after every edit; check main.log has no 'undefined references'/'Reference … undefined'; check no ❌ sentence appears. Use Write/Edit tools for Vietnamese text, NOT bash heredoc.
SOURCE: E:\Code\Report_INT3508\BAN-GIAO-PHIEN-2026-09-23.md:620-623

## 38. [§10 defaults table]
Code edits allowed only in worktree E:\Code\RideBound-deadline (branch research/deadline-gate from 41a4e11); mode = exploratory with controls and preregistration (WP14R 009..012 still UNAUTHORIZED; official mode needs ADR + builder freeze); disk may exceed 30 GB keeping E: ≥ 40 GB, C: ≥ 50 GB, delete nothing; dl-60 in 2B yes if space allows; dl2-30 in 2A no; commit/push ask user; supervisor name ask user; Tầng 3 ask user after Tier 2 results (4–10 weeks); order: Tier 0 parts independent of Tier 2 → T1.12 → Tier 2 (2B may precede 2A) → update ch4 with Tier 2 results.
SOURCE: E:\Code\Report_INT3508\BAN-GIAO-PHIEN-2026-09-23.md:629-639

## 39. [Traps list §11 (from 16/09 handoff and plan)]
16/09 traps: 12.1 wrong config set for runner; 12.2 op_max_wait_time clamps window; 12.3 run vs transcript id mismatch (run-00.json req-<32hex> vs transcript rq-<64hex>); 12.4 counting errors instead of classifying; 12.5 guessing evidence field names; 12.6 bash heredoc corrupts Vietnamese; 12.7 different semanticHash ≠ different decision (use decision_identity.py); 12.8 half-finished output dir blocks reruns / orphan processes; 12.9 hand-numbered LaTeX; 12.10 recorded wrong predictions. Plan N1–N14: N1 believing 'decisionDelta one-sided'; N2 calling d 'traffic'; N3 new arm falls into EffectivePolicies default branch (SolverBackedRidePoolingPolicy.cs:396-410) running unconstrained; N4 gate rejecting no-op breaks run; N5 changing policyId (preflight hard-codes wp6-synthetic-policy-overlay-v1 at actual_fleetpy_medium_preflight.py:189, :234); N6 running medium verifier on drift runs; N7 GitDirty test on clean worktree; N8 Vietnamese heredoc; N9 Gini; N10 CI over riders; N11 reading 'First rejection' as the no-op reason; N12 running evening cells with original preflight_drift.py (28800 hard-coded line 73 ⟹ morning factors on evening cells, silently); N13 calling post-hoc 'confirmation'; N14 inferring evening prediction from window ratio.
SOURCE: E:\Code\Report_INT3508\BAN-GIAO-PHIEN-2026-09-23.md:645-658, :572

## 40. [Traps §11 environment]
python not on Git Bash PATH; cp1252 UnicodeEncodeError → PYTHONIOENCODING=utf-8; Bash tool resets cwd to e:\Code\RideBound → absolute paths; du on E:/RideBoundData >5 min → Get-PSDrive; Edit requires prior Read; preflight_drift.py hard-codes REPO = E:/Code/RideBound (line 65) and TARGET (line 66) → use edited copy preflight_drift_v2.py from worktree; no pdftotext; fresh worktree gets CRLF (core.autocrlf=true) → golden-byte tests red (6/908), fix via restore_index_bytes.py (verify with git hash-object --no-filters), ~147 cosmetic M lines, view real diff with `git -c core.autocrlf=false diff`; after byte restore 1 red test in RideBound.Benchmarking.Tests (StrictBagItBundleTests GitDirty==true line 32, or PublicDerivativeMechanicalDrainConversationTests CPU-time on cold/parallel build) — identify exactly before accepting as baseline.
SOURCE: E:\Code\Report_INT3508\BAN-GIAO-PHIEN-2026-09-23.md:661-677

## 41. [§12 Do-not list (verbatim items)]
'- Không authorize `RB-WP14R-009..012`, không authorize WP15, không mở H7.' '- Không sửa cây làm việc chính của kho; không sửa `docs/18`, `docs/19` ở cây chính.' '- Không đổi margin, panel, mẫu số, factor level hay failure treatment đã tiền đăng ký.' '- Không lấy tham số số học từ văn liệu để đặt mức cho nhánh; không dùng số H6 để chọn tham số nhánh mới.' '- Không tuyên bố RideBound tốt hơn/nhanh hơn/tương đương công trình nào.' '- Không đề xuất lại tám hướng đã chết (bàn giao 16/09 §8) nếu không có bằng chứng mới.' '- Không xóa tệp nào; không đụng báo cáo thực tập; không thêm lại mục 4–7 của báo cáo tiếng Việt cũ.' '- Không sửa khiếm khuyết `worst-hard-utilization-ppm` trong Tầng 2 (K12).'
SOURCE: E:\Code\Report_INT3508\BAN-GIAO-PHIEN-2026-09-23.md:683-690

## 42. [Reporting language]
Reply in Vietnamese, simple explanations with real examples from the system ('Trả lời tôi bằng tiếng Việt, giải thích đơn giản kèm ví dụ thật từ hệ thống'); code comments/identifiers in English.
SOURCE: E:\Code\Report_INT3508\BAN-GIAO-PHIEN-2026-09-23.md:704-705, :65, :593; memory\user-profile.md:11

## 43. [Memory index (MEMORY.md)]
Six memory entries: user-profile.md; ridebound-standing-constraints.md (no deleting files, main repo tree untouched (worktree only), hourly progress, never re-add old report §4–7); ridebound-disk-policy.md (since 2026-09-23 >30 GB OK; keep E: ≥40 GB, C: ≥50 GB free; never delete to free space); ridebound-rigor.md (zero hallucination: cite file:line, test every change, independent review, faithful reporting); ridebound-handoff-2026-09-23.md (read BAN-GIAO + KE-HOACH first; Tier 2 complete + in thesis; Tier 3 pilot, C/M⁺ sweep and ADR-077 no-worse recovery done 2026-09-26 (M⁺(b) ≈ C service); Hamburg not run); ridebound-env-traps.md (which Python, UTF-8, no heredoc/sed for Vietnamese, tectonic --keep-logs, CSV column, check battery before long runs).
SOURCE: C:\Users\quang\.claude\projects\e--Code-RideBound\memory\MEMORY.md:1-6

## 44. [Memory: user grading target]
Grading criteria targeted: real/important problem; reasonable method newer than competitors or with better limits; quantitative evidence.
SOURCE: memory\user-profile.md:13

## 45. [Memory: standing constraint 6 (ask list)]
'Ask before commit/push, before starting Tier 3, and for the supervisor name.' How to apply: check every file-modifying action against this list.
SOURCE: memory\ridebound-standing-constraints.md:16, :19

## 46. [Memory: rigor rule]
User insists AI 'không được ảo': never invent numbers, code lines, results or paper content; read code before writing and cite file:line read in the current session; run `dotnet test RideBound.slnx` after every code change and compare to recorded baseline; review each diff line by line plus an independent fresh-context subagent review; seal preregistered predictions before running predicted arms; report failures and negative results as faithfully as positive ones. Why: past wrong claims (one-sided A, DKW on riders, 'gate 60 riders', 96% denominator, over-strong Theorem 4, misidentified paper). Apply §9 of BAN-GIAO; mark unverified with ⚠️.
SOURCE: memory\ridebound-rigor.md:11-14

## 47. [Memory: disk policy]
Keep E: ≥ 40 GB free and C: ≥ 50 GB free (2026-09-23: E: 77.4 GB, C: 114.2 GB free; E:\RideBoundData 90 GB by du 2026-09-24). Check with Get-PSDrive before/after big runs. Never free space by deleting.
SOURCE: memory\ridebound-disk-policy.md:11, :14

## 48. [Memory env trap: tectonic stale log]
Without `--keep-logs` tectonic does NOT rewrite main.log — a stale log (dated 09-24, seen 2026-09-26) hid 2 overfull tables. Always check main.log timestamp. Build cmd: ..\tools\tectonic.exe -X compile main.tex --outdir . --keep-logs from ridebound\.
SOURCE: memory\ridebound-env-traps.md:15

## 49. [Memory env trap: CR counting]
`grep -c $'\r'` in Git Bash miscounts CR bytes — count with Python open(f,'rb').read().count(b'\r').
SOURCE: memory\ridebound-env-traps.md:18

## 50. [Memory env trap: known red tests]
StrictBagItBundleTests asserts GitDirty == true (line 32) — red on clean worktree, not a code defect. PublicDerivativeMechanicalDrainConversationTests can fail resource.cpu-time-exceeded on cold/parallel build.
SOURCE: memory\ridebound-env-traps.md:19

## 51. [Memory env trap: battery]
Check power before long simulation runs (`Get-CimInstance Win32_Battery` BatteryStatus 1 = discharging, 2 = AC). On battery the drain test failed; a dying run leaves failed-recorded/incomplete output dirs that must not be deleted and block/contaminate the stage — do not start Tier-2 jobs on battery; ask user to plug in.
SOURCE: memory\ridebound-env-traps.md:20

## 52. [Memory env trap: sed with Vietnamese]
`sed -i` with Vietnamese in the pattern silently fails in Git Bash — use Edit tool.
SOURCE: memory\ridebound-env-traps.md:21

## 53. [Memory env trap: matplotlib DLL]
`import matplotlib.pyplot` in the fleetpy conda env crashes silently (exit -1066598273) unless PATH is prepended with <env>;<env>\Library\mingw-w64\bin;<env>\Library\usr\bin;<env>\Library\bin;<env>\Scripts for that process.
SOURCE: memory\ridebound-env-traps.md:22

## 54. [Memory env trap: host sleep kills jobs]
Modern Standby sleep kills simulation jobs: runner_client 60 s response timeout counts sleep → RBWP7_RUNNER_RESPONSE_TIMEOUT after wake (2026-09-24: 5 jobs; ridebound-scratchpad/deadline/AMENDMENTS.md A2, rerun into <job>-rerun1). Check Get-WinEvent Kernel-Power 506/507. Driver calls SetThreadExecutionState (idle sleep only). To pause: suspend ONLY driver PID (NtSuspendProcess), never kill it, never suspend running jobs.
SOURCE: memory\ridebound-env-traps.md:23

## 55. [Memory env trap: adapter Python test suite]
Run from simulators/fleetpy-ridebound/tests with `-B -m unittest discover -s . -t . -p 'test_*.py'` and RIDEBOUND_FLEETPY_ROOT set. 6 freeze tests fail identically on clean LF checkout E:\Code\RideBound-py-baseline @8d1ea4d (test_wp13_full_audit x2, test_wp13_e1_source_divergence, test_wp14r_freeze_v6, test_wp9_freeze_v6 x2) — pre-existing; compare messages not counts.
SOURCE: memory\ridebound-env-traps.md:25

## 56. [Memory env trap: FleetPy rounding]
FleetPy rounds latest pickup UP to whole seconds (np.ceil, VehiclePlan.py:362).
SOURCE: memory\ridebound-env-traps.md:26

## 57. [Memory env trap: scratchpad test modules]
Scratchpad test scripts end with module-level `raise SystemExit(...)`; importing one exits the importer while printing '0 failure(s)'. Never import a test module; count checks and fail if fewer than expected.
SOURCE: memory\ridebound-env-traps.md:27

## 58. [Memory env trap: never edit worktree during jobs]
NEVER edit files in a worktree while simulation jobs use it: medium preflight hashes the Git-visible source tree at start and end and fails every spanning job ('repository content inventory drifted during the matrix run', actual_fleetpy_medium_preflight.py:881); 2026-09-25 killed ~12 sweep jobs. Develop in a separate worktree; restore bytes with `git cat-file blob HEAD:path` + verify `git hash-object --no-filters`.
SOURCE: memory\ridebound-env-traps.md:28

## 59. [Memory env trap: world bin switch lag]
preflight_world.py / preflight_drift_v2.py apply a new bin only at next _trigger_and_resolve → arm-dependent switch time. Use world/preflight_world_v1_1.py (inserts bin starts) for new runs.
SOURCE: memory\ridebound-env-traps.md:29

## 60. [Memory env trap: always -B]
First un-`-B` test run rewrote 12 tracked .pyc files (restored); always use -B + PYTHONDONTWRITEBYTECODE.
SOURCE: memory\ridebound-handoff-2026-09-23.md:25

## 61. [Memory handoff: user approval superseding ask-rules]
2026-09-24 ~15:30Z: user approved 'thực hiện toàn bộ' (supervisor name later). Worktree branch committed 65d867c and pushed to origin/research/deadline-gate. Thesis repo NOT committed (git inspection of ridebound/ blocked by auto-mode classifier — leave to user). Line 36: 'Still to ask the user: supervisor name (T0.2.10), anticipatory-walking PDF, Geržinič source. (Commit/push + Tier 3 approved by "thực hiện toàn bộ".)'
SOURCE: memory\ridebound-handoff-2026-09-23.md:19, :36

## 62. [Memory handoff: Tier 2 outcome pointer]
2026-09-24 ~14:00Z TIER 2 COMPLETE (296 jobs + 5 host-sleep reruns = 301 dirs); sealed-rule analysis analysis-2026-09-24-final.txt: panel A 98/102, held-out morning 31/32, evening 40/40; both preregistered thresholds met, no negation; 0/56 conduct runs commitment-infeasible; evening one-sided 0/8 vs two-sided 7/8 vs visible 8/8; secondary prediction (deadline serves more when traffic eases) NOT observed. Written into ch4 muc:tang2 (+ch1/ch3/ch5/abstract), figure hinh/tang2-bon-ho-v2.pdf. Preregistration sealed 06:03:52Z (PREREGISTRATION.sha256). Runner E:\RideBoundData\research\runner-deadline-v1.
SOURCE: memory\ridebound-handoff-2026-09-23.md:16-18

## 63. [Memory handoff: Tier 3 decisions and file pointers]
Tier 3 user decisions: recovery = keep route as forced action + typed commitment breach, ledger never reset, theorems cover only non-recovery part; mode exploratory preregistered; world v1 = OD-pair noise (shared RNG keyed worldSeed/odPair/timeBin/component), two-sided + shock recovery on 96-node closure. Files: ridebound-scratchpad/tang3/T3.1-KHOA-CAU-HOI.md, tang3/oracle/, tang3/T3.4-GHI-CHU-THIET-KE.md, tang3/world/, tang3/configs/wp4-tier3-v1.json, tang3/evidence/audit_vep.py + METRICS-SPEC.md, tang3/T3.7-KE-HOACH-THI-DIEM.md, tang3/T3.7-BAO-CAO-THI-DIEM.md, tang3/sweep/ (SWEEP-PLAN.md sealed 756b65fd…, SWEEP-AMENDMENTS.md, SWEEP-REPORT §7–§8, run_noworse.py, noworse_analyze.py, why_similar.py). Commits: 8d1ea4d (T3.3), 69512d3 (T3.4), 1ce15e9 (docs §30), 45f8026 (ADR-077), a90b4b7 (ADR-077 evidence). Runners: E:\RideBoundData\research\runner-tier3-v1, C:\RideBoundData\research\runner-tier3-v2; no-worse outputs C:\RideBoundData\research\tier3-sweep-noworse-v1.
SOURCE: memory\ridebound-handoff-2026-09-23.md:20-32

## 64. [Memory handoff: open items requiring user]
Hamburg (Schulz instances at C:\Users\quang\Downloads\data, CC BY 4.0, static matrix) NOT run — needs converter + op_max_wait_time 600 hard-coded change + customer model, ~1–2 days; ask user. ADR-075 recovery rule ('no worse than reference') needed user decision before confirmatory (later coded as ADR-077). Untested option: real-only 07–09h cells on dev days 12–13/11 (needs new scenarios; effort unestimated); prediction NOT result: M⁺ would break at 60–120 s there.
SOURCE: memory\ridebound-handoff-2026-09-23.md:22, :29, :31-32, :34

## 65. [Memory handoff: central claim and difference vs Elmi]
Central claim: conditional Theorem 4 ('conduct gate is never the cause of an empty candidate set') + corollary on drift direction. Elmi 2026 also bounds increases within slack for all riders (§2.1.4/2.4.1) — difference is the bounded OBJECT (operator-caused part), not 'a level for everyone'.
SOURCE: memory\ridebound-handoff-2026-09-23.md:38

## 66. [Memory handoff: correction about 73.84%]
Thesis table bang:mong (flat-travel 20-cell panel): 73.84% of a vehicle's sets on active epochs have ZERO insertion positions, 23.68% exactly one, 2.48% ≥2 — NOT '73.8% have only one way'. Also verified ~107 request-decisions per job, 83–95% offer ≥2 options, 80–90% riders accepted → 'both just keep route' is FALSE.
SOURCE: memory\ridebound-handoff-2026-09-23.md:33-34

## 67. [Memory handoff: how to resume]
Next session must resume from files, not chat memory: read handoff §0 group A; check ridebound-scratchpad\deadline\logs\ and BASELINE-2026-09-24.md for latest runs.
SOURCE: memory\ridebound-handoff-2026-09-23.md:40-41

## 68. [AGENTS.md: required reading before change]
Before changing anything read: 1 docs/00-index.md; 2 docs/01-research-charter.md; 3 docs/18-status-and-decision-log.md; 4 active WP in docs/16-roadmap-and-work-packages.md; 5 topic-specific doc linked by index.
SOURCE: E:\Code\RideBound-deadline\AGENTS.md:5-11

## 69. [AGENTS.md: source of truth and doc updates]
docs/18-status-and-decision-log.md is the live source of truth; update it, the relevant decision entry, and docs/19-requirement-traceability.md whenever a task changes implementation status, contracts, claims, baselines, metrics, repository boundaries, or next actions.
SOURCE: E:\Code\RideBound-deadline\AGENTS.md:13-16

## 70. [AGENTS.md: BeGo/OptiGo boundary]
RideBound is independent; do not copy BeGo/OptiGo source tree; reuse only audited generic code with provenance and tests; keep BeGo-specific mapping in an adapter.
SOURCE: E:\Code\RideBound-deadline\AGENTS.md:18-20

## 71. [AGENTS.md: layering]
Domain and Application must remain independent of OptiGo entities, EF Core, ASP.NET, map providers, OR-Tools, and simulator libraries. Simulator adapters must call the same versioned runner; never reimplement RideBound in Python, C++, or adapter code.
SOURCE: E:\Code\RideBound-deadline\AGENTS.md:22-25

## 72. [AGENTS.md: claim boundary]
Do not claim as novel: dynamic insertion, ETA limits, reassignment, route similarity, least-commitment, time consistency, user satisfaction. Permitted boundary in docs/03-related-work-and-claim-boundary.md.
SOURCE: E:\Code\RideBound-deadline\AGENTS.md:27-29

## 73. [AGENTS.md: preservation]
Preserve user-owned and unrelated changes. Never delete research corpora, downloaded data, vendor checkouts, result artifacts, or local configuration as cleanup.
SOURCE: E:\Code\RideBound-deadline\AGENTS.md:31-33

## 74. [AGENTS.md: verification command]
Run for every code change: `dotnet test RideBound.slnx`. BeGo integration work must also keep its separately recorded baseline passing (commands/counts in docs/18).
SOURCE: E:\Code\RideBound-deadline\AGENTS.md:37-45

## 75. [Live state: worktrees]
Worktrees: E:/Code/RideBound 41a4e11 [main]; C:/Code/RideBound-noworse a90b4b7 [research/tier3-no-worse]; E:/Code/RideBound-deadline 1ce15e9 [research/tier3-failure-aware]; E:/Code/RideBound-py-baseline 8d1ea4d (detached HEAD). main HEAD 41a4e11eb2897e7af45543078371d51591231b41 2026-09-04 'Add comprehensive tests for commitment and optimization features'. E:/Code/RideBound-deadline HEAD 1ce15e92d2c1459d4254bbbcd581529197257fb2 2026-09-25 'Record the Tier 3 pilot (T3.5-T3.7) status and next decisions (exploratory)'.
SOURCE: command: git -C E:/Code/RideBound worktree list; git -C E:/Code/RideBound log -1; git -C E:/Code/RideBound-deadline rev-parse --abbrev-ref HEAD; git -C E:/Code/RideBound-deadline log -1 (run 2026-09-29)

## 76. [Live state: disk and power]
Free space: C: 103.8 GB free (170.5 used); E: 41.8 GB free (158.9 used). Battery: BatteryStatus 2 (AC), 100%.
SOURCE: command: PowerShell Get-PSDrive C,E + Get-CimInstance Win32_Battery (run 2026-09-29)

## 77. [Live state: other sessions/processes]
ListAgents: no other Claude session reachable on this machine; this process's main session is ridebound-84 [9811d5]. Running processes: no python; one dotnet PID 16164 started 9/29/2026 11:12:21 AM (4 s CPU).
SOURCE: tool ListAgents; command: Get-Process -Name python,dotnet,RideBound* (run 2026-09-29)

# UNVERIFIED
- Whether the user's 'thực hiện toàn bộ' approval (memory ridebound-handoff-2026-09-23.md:19,:36) extends to commits/pushes and new runs beyond the Tier 2/3 scope already done (e.g. Hamburg, new 07–09h cells) — memory line 32 still says 'ask user' for Hamburg.
- Whether any uncommitted real changes exist in E:\Code\RideBound-deadline or C:\Code\RideBound-noworse (git status not run to avoid touching index).
- Identity of the running dotnet PID 16164 (likely build server; not confirmed whether a simulation/runner).
- The KE-HOACH-HOP-NHAT-2026-09-23.md, docs/00, docs/01, docs/03, docs/16, docs/18, docs/19, docs/tasks/47 were NOT read in this slice.
- Contents of ridebound-scratchpad\deadline\logs\ and BASELINE-2026-09-24.md (pointed to by memory:41) not read.
- Memory file:line citations to code (e.g. actual_fleetpy_medium_preflight.py:881, VehiclePlan.py:362, world_v1.py:72) not re-verified against current code; memory files are 3–5 days old per system reminder.
- Whether AGENTS.md in main tree E:\Code\RideBound is byte-identical to E:\Code\RideBound-deadline\AGENTS.md (main tree not read per rule; the injected session context copy shows the same text).
# WARNINGS
- E: has only 41.8 GB free — barely above the ≥40 GB threshold (memory ridebound-disk-policy.md:11). Any new large run should target C: (103.8 GB free; precedent memory handoff:31 moved no-worse work to C: because E: was near 40 GB) and check Get-PSDrive before/after.
- BAN-GIAO-PHIEN-2026-09-23.md is stale on status: it says Tier 2 only 'đã bắt đầu' and worktree E:\Code\RideBound-deadline on branch research/deadline-gate (lines 164, 482, 512, 631), but live git shows that worktree now on research/tier3-failure-aware @1ce15e9, and memory says Tier 2 complete and Tier 3 largely done (memory handoff:18-32). Use memory handoff + git as current state; handoff for rules.
- Rule conflict: BAN-GIAO §2.1.3 (:104-109), §8.3.13 (:558), §10 (:636, :638) and §13 (:703-704) require asking before commit/push and before Tier 3; memory handoff:19 and :36 record user approval 'thực hiện toàn bộ' covering commit/push + Tier 3. The supervisor name remains an ask-the-user item in all sources.
- Thesis repo E:\Code\Report_INT3508 (ridebound/) has not been committed by AI; memory handoff:19 says leave to user. Internship report at repo root must not be touched (BAN-GIAO:118-121).
- Never edit files in a worktree while simulation jobs use it (memory env-traps:28) — inventory hash drift kills jobs.
- docs/18 in main tree is flagged stale vs 41a4e11 (BAN-GIAO:36); docs/18/19 updates live only on research branches (BAN-GIAO:684).