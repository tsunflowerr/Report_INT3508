# EVIDENCE REGISTER — viết lại khóa luận RideBound (2026-10-10)

**Vai trò.** Sổ đăng ký bằng chứng cho người viết từng chương. Mỗi câu nêu sự kiện, con số, cơ chế hay khẳng định văn
liệu trong luận văn mới phải trỏ được về một dòng của sổ này. Không dán mã vào luận văn; chỉ ghi nơi bằng chứng nằm.

**Cách tôi kiểm (Claude, evidence registrar, 2026-10-10).**
- Mở trực tiếp các tệp output, mã nguồn, cấu hình, bản trích PDF được trỏ tới; đối chiếu số với tệp output gốc.
- Chạy một script chỉ đọc, một tiến trình: `rewrite-2026-10/evidence/checks/verify_register.py` →
  `checks/verify-register-v2-2026-10-10.txt` (khóa **CHK**). Nó kiểm 166 cặp (tệp:dòng, đoạn trích) — **166 OK, 0 FAIL**
  (CHK:168) — và tính lại các phép số học dẫn xuất (CHK:169-212), cùng nhận dạng trang 1 của hai PDF (CHK:213-214).
  Bản v1 `verify-register-2026-10-10.txt` được giữ lại: nó đếm sai dòng vì `splitlines()` coi ký tự form feed của PDF là
  xuống dòng; không dùng v1 làm bằng chứng.
- Không chạy mô phỏng, không build, không cài đặt, không xóa; không ghi ngoài `rewrite-2026-10/evidence/`.

**Nhãn trạng thái.**
- **VERIFIED-by-me** — tôi đã mở dòng được trỏ trong phiên này và thấy đúng con số/đoạn chữ. Khi tệp output là bản dựng lại
  của Codex (A) hay Claude (DIAL17, FJC…), cột ghi chú nói rõ ai dựng.
- **VERIFIED-by-Codex R15 / R18** — chỉ Codex đã kiểm ở mức dữ liệu thô hay web; tôi đọc dòng kết luận của Codex, không
  tự kiểm lại bằng chứng gốc.
- **VERIFIED-by-Codex R14 / R13 (web)** — biến thể của nhãn trên cho nguồn web mà Codex mở ở vòng 13–14; tôi không mở lại.
- **UNVERIFIED** — không ai (hoặc không phải tôi và không có xác nhận đáng tin) mở được nguồn gốc; không dùng làm căn cứ.

**Nhãn mẫu số (bắt buộc ghi kèm số tỉ lệ).** `[gộp theo khách]` = tổng số khách/tổng khách được chở; `[TB theo ô]` =
trung bình không trọng số của tỉ lệ từng ô; `[trên yêu cầu]` = chia cho 3.672 yêu cầu; `[đếm]` = số đếm tuyệt đối.

## Khóa anchor

Đường dẫn tương đối với `E:/Code/Report_INT3508/ridebound-scratchpad/` trừ khi ghi tuyệt đối. `DEB` =
`optimize/codex-debate/`, `CW` = `DEB/claude-work/`, `XW` = `DEB/codex-work/`, `SRC` = `C:/Code/RideBound-noworse/src/`.

| Khóa | Tệp |
|---|---|
| A | `XW/R15-audit-summary.txt` (Codex dựng lại độc lập 227 transcript) |
| NEW | `XW/R18-verification.txt` (Codex R18) |
| R15 / R18 | `XW/R15-CONFIRM-CODEX.md` / `XW/R18-CONFIRM-CODEX.md` |
| R14 | `XW/R14-JUDGE-OF-CLAUDE-BY-CODEX.md` |
| V17 / V13 | `CW/R17-FINAL-VERDICT.md` / `CW/R13-FINAL-VERDICT.md` |
| HO | `E:/Code/Report_INT3508/BAN-GIAO-PHIEN-2026-10-09.md` |
| T38 / T38A / T38I / T38RX | `tang3/t38/T38-REPORT.md` / `analysis-2026-10-02-report.txt` / `independent/RESULT.md` / `rider-experience-2026-10-05-report.txt` |
| SPLIT / RUN38 | `tang3/t38/split-t38-v1.json` / `tang3/t38/run_t38.py` |
| W07 / W07AGG / RUNW07 | `tang3/w07/W07-REPORT.md` / `tang3/w07/analysis/aggregate-2026-09-30.txt` / `tang3/w07/run_w07.py` |
| W07X / W07XM | `tang3/w07x/W07X-REPORT.md` / `tang3/w07x/analysis/mechanism-2026-10-01.txt` |
| SWEEP | `tang3/sweep/SWEEP-REPORT.md` |
| CFG / WP4 | `tang3/configs/<arm>.json` / `tang3/configs/wp4-tier3-v2.json` |
| AUDIT / SPEC | `tang3/evidence/audit_vep.py` / `tang3/evidence/METRICS-SPEC.md` |
| PREF / PREF12 | `tang3/world/preflight_world.py` / `tang3/world/preflight_world_v1_2.py` |
| FIX | `C:/RideBoundData/research/fixtures-panelA-v1/d20181114-s10-r3-w08/normalizer-configuration.json` (1 dòng JSON) |
| FR / FA / SNOW | `optimize/FORECAST-REPORT.md` / `optimize/test-family-a-causal-no15-2026-10-06-report.txt` / `optimize/test-snow-2026-10-06-report.txt` |
| DISP / STRETCH | `optimize/display_layer.py` / `optimize/promise_stretch.py` |
| RX / CON / LATE / EXAMPLE | `optimize/report-extras/` `report-extras-2026-10-06.txt` / `constraints-and-pooling-2026-10-06.txt` / `lateness-distribution-2026-10-06.txt` / `example-rider-2026-10-06.txt` |
| EXP / SHARE / STT / SEL6 / FAC / COM / BURD / SERV | `DEB/` `exposure-check` / `pooling-share` / `shared-time-share` / `selection-length-check` / `factor-anchor-check` / `common-riders-check` / `burden-and-rescale` / `service-duration-check` `-2026-10-06.txt` |
| PAD / LAD / BUD / PROP / BACK / LOAD / BUC / WBU / INV / PROV | `CW/` `cap-vs-pad-frontier-2026-10-07` / `wp14r-ladder-reanalysis-2026-10-08` / `budget-block-diagnosis-2026-10-07` / `proportional-budget-screen-2026-10-07` / `calib-backtest-2026-10-07` / `load-and-occupancy-2026-10-07` / `budget-use-check-2026-10-09` / `wp14r-budget-use-2026-10-10` / `data-inventory-summary-2026-10-08` / `provenance-overlap-check-2026-10-08` `.txt` |
| ML / ML0 / MLS / MLA | `CW/ml-pilot-report-a1-2026-10-08.txt` / `CW/ml-pilot-report-2026-10-08.txt` (trước phụ lục, không hợp lệ) / `CW/ML-PILOT-SEALED.md` / `CW/ML-PILOT-AMENDMENTS.md` |
| DIAL17 / WP17 / DER17 / EL17 / WX17 / DIALPY | `CW/r17-rebuttal/` `r17-verify-dial` / `r17-wp14r-check` / `r17-derived-counts` / `r17-wp14r-elapsed` / `r17-weather-recount` `-2026-10-10.txt` / `r17_verify_dial.py` |
| FJC / FJR / FJO / FJS | `CW/r13-final-judge/` `cumulative-decisive-check` / `per-run-cumulative-only-b` / `objective-levels-check` / `served-overlap-check` `-2026-10-10.txt` |
| CVP / TIER | `CW/r13-proposer/cumulative-vs-perinsertion-2026-10-10.txt` / `tier-budget-screen-2026-10-10.txt` |
| RP1 / NOAA13 / PQ | `CW/r16-forecast/rider-nowcast-replay-2026-10-10.txt` / `noaa-event-days-2009-2013-2026-10-10.txt` / `parquet-footer-probe-2013-2026-10-10.txt` |
| CAP / WX / SCOPE | `XW/R16-cap-outcomes.txt` / `XW/R16-weather-inventory.txt` / `XW/R16-scope-inventory.txt` |
| SF / PV / CASE / META / SIZE | `XW/R17-screen-forecast-verification.txt` / `R17-portfolio-verification.txt` / `R17-C30-sum-case.txt` / `R17-metadata-verification.txt` / `R17-data-size-verification.txt` |
| SUR13X / PAP13 | `XW/R13-SURVEY-CODEX.md` / `CW/R13-PAPERS-CLAUDE.md` |
| TLC / SYED | `CW/r13-ml-data-samples/tlc_data_reports_monthly.csv` / `CW/r13-ml-data-samples/syed2021_ffutr.txt` |
| DELTA | `SRC/RideBound.Application/Promises/PromiseDeltaCalculator.cs` |
| VALID | `SRC/RideBound.Application/Commitments/CommitmentDecisionValidator.cs` |
| PROJ / PPROJ | `SRC/RideBound.Application/Scheduling/RouteScheduleProjector.cs` / `SRC/RideBound.Application/Promises/PromiseProjector.cs` |
| BUDGET / LEDGER / LOCK / POLICY / DIM | `SRC/RideBound.Domain/Commitments/` `CommitmentBudgetEvaluator.cs` / `CommitmentLedger.cs` / `CommitmentLockEvaluator.cs` / `CommitmentPolicy.cs` / `CommitmentDimension.cs` |
| SEL / POL | `SRC/RideBound.Algorithms/Policies/SolverBackedFleetSelection.cs` / `SolverBackedRidePoolingPolicy.cs` |
| HVA / CCA / CSE | `SRC/RideBound.Algorithms/Commitments/HardVectorCandidateAssessor.cs` / `CommitmentCandidateAssessor.cs` / `SRC/RideBound.Algorithms/Candidates/CandidateScheduleEvaluator.cs` |
| NORM | `SRC/RideBound.Benchmarking/Normalization/FleetPyManhattanNormalizer.cs` |
| ADR | `C:/Code/RideBound-noworse/docs/18-status-and-decision-log.md` (ADR-077 ở dòng 5066–5139) |
| D03 | `E:/Code/RideBound/docs/03-related-work-and-claim-boundary.md` (chỉ đọc) |
| HZ / FLEET / LEO / LUK / GM | `CW/pdf/` `hoerl-zwick-2022` / `fleetpy-etrr-2026` / `leonardi-2024` / `lu-kuehnel-2024` / `gardner-1985` `.txt` |
| FAM / SP / WAR / AGZ / MOL | `C:/Users/quang/AppData/Local/Temp/claude/e--Code-RideBound/4f238113-dd3b-4bd1-b13f-53613b57f0e6/scratchpad/papers/` `Unreliability_in_ridesharing_systems_Measuring_cha` / `s00291-026-00847-0` / `1-s2.0-S0965856426000662-main` / `Value_of_time_and_reliability_for_urban_pooled_on-` / `OperationalEffectsofServiceLevelVariations-publication151005` `.txt` (PDF gốc cùng tên ở `C:/PDF/Paper/`) |
| AM17 / COHEN | `E:/RideBoundData/literature-survey-2026-10-06/pdf/alonso-mora-pnas2017.pdf` / `cohen-fiszer-kim-2022-frustration.pdf` |
| CHK | `rewrite-2026-10/evidence/checks/verify-register-v2-2026-10-10.txt` |

Số dòng của các tệp `.txt` trích PDF là số dòng theo ký tự LF (như `cat -n`, `grep -n`).

---

## A. Hệ thống và cơ chế

| ID | Câu có thể dùng trong luận văn | Số chính xác | Anchor | Trạng thái | Lưu ý |
|---|---|---|---|---|---|
| A01 | Với mỗi lần sửa lời hứa, v là lời hứa đã công bố trước đó, e là tuyến cũ của xe tính lại theo bảng giờ đi hiện tại, p là lời hứa mới; x = e − v là phần do giao thông, c = p − e là phần do quyết định điều phối, z = p − v = x + c là phần khách thấy. | — | SPEC:41-50; AUDIT:5-10,106-113; VALID:355-379; CHK:91-93,148-149 | VERIFIED-by-me | v **không** phải "lời hứa đầu chỉ bị dời bởi tắc đường" (HO:398-400). Đây là phép chiếu mô hình tại cùng trạng thái, không nhận diện nhân quả (D03:222-224). |
| A02 | e được tính bằng cách chạy lại tuyến cũ của xe từ vị trí hiện tại với bảng giờ đi hiện tại, ở thời điểm quyết định. | — | VALID:355-379 (359: `ReducedState.TravelTimes`); PROJ:50-148 | VERIFIED-by-me | e là "kế hoạch giữ nguyên" của mô hình, không phải giờ đến thật. |
| A03 | Giờ phục vụ ở điểm đón là max(giờ xe tới, giờ đón sớm nhất), giờ rời = giờ phục vụ + thời gian dừng, và lời hứa trả là giờ phục vụ tại điểm trả. | — | PROJ:117-140,151-166; PPROJ:61-80,120-131 | VERIFIED-by-me | Trong thí nghiệm thời gian dừng = 0 (B05). |
| A04 | Sổ cái lưu trị tuyệt đối của ba độ lệch \|e−v\|, \|p−e\|, \|p−v\| cho từng chiều cam kết; giờ trả là một trong mười chiều. | 10 chiều | DELTA:64-97,101-160 (139), 259-260; DIM:3-32; CHK:84-87 | VERIFIED-by-me | Dấu của x, c chỉ khôi phục được từ v, e, p trong checkpoint (AUDIT:5-9). |
| A05 | Bộ điều phối chỉ nhận ảnh chụp giờ đi hiện tại và giữ nguyên chúng cho tương lai; nó không đọc thế giới mô phỏng. | — | PREF:13-20; PREF12:18-19; CHK:158-159 | VERIFIED-by-me | Vì vậy e không chứa dự báo. |
| A06 | Luật C đặt cho mỗi khách một ngân sách cả chuyến: tổng trị tuyệt đối các lần dời giờ trả do điều phối (c) không vượt B; ngân sách đã tiêu cộng với phần dời mới phải ≤ B, nếu vượt thì phương án bị loại. | C-30: B = 30 000 ms; C-120: 120 000 ms | VALID:494-520; BUDGET:41-105 (51, 88); LEDGER:285-288; CFG C-30.json:6,17-23; CHK:88-89,94-97,133-134 | VERIFIED-by-me | B là ngân sách cả chuyến, phần còn lại = B − phần đã dùng; không cấp lại B mỗi lần (R18 §2). |
| A07 | Trong mọi nhánh, ba chiều đổi xe, đổi điểm đón, đổi điểm trả có trần cứng 0; chỉ chiều giờ trả có trần dương ở nhánh C. | hardLimit 0 ×3 | CFG C-30.json:34-35,50-51,66-67; CFG U.json:33-34,49-50,65-66 | VERIFIED-by-me | Các trần 0 là phần "khóa" chung của U và C. |
| A08 | Nhánh U giống hệt C-30 trừ việc không có trần giờ trả; nó vẫn khóa xe, điểm đón và giờ đón khi xác nhận đặt xe. | khác biệt duy nhất `/policies/0/limits/1/hardLimit` (vắng → 30000); sha256 U 998a0a94…, C-30 d6124f3f…, C-120 ac0f9758… | NEW:11-12; tôi chạy `diff U.json C-30.json` và `sha256sum`; CFG C-30.json:94-98 | VERIFIED-by-me | U **không** phải FREE (FREE không khóa gì, HO:108-109). |
| A09 | Luật hạn chót M⁺-B loại phương án khi giờ trả mới muộn hơn lời hứa trả **đầu tiên** quá B (một phía), và M⁺-30 chỉ khác U ở khóa `dropEtaDeadlineSlackMs = 30000`. | slack 30 000 ms | LOCK:162-197 (186-191); POLICY:242-249; VALID:386-402; CFG Mplus-30.json:98; tôi chạy `diff C-30.json Mplus-30.json`; CHK:99-101,137 | VERIFIED-by-me | Gọi là "thành phần hạn chót kiểu Schulz & Pfeiffer", không phải phương pháp của họ (POLICY:244; HO:369-370). |
| A10 | Các khóa so phương án với phép chiếu ngoại sinh nên trôi do giao thông không bao giờ kích hoạt khóa, còn hạn chót so với lời hứa đầu nên riêng trôi do giao thông có thể kích hoạt nó, kể cả với phương án giữ nguyên. | — | LOCK:156-161; POLICY:243-248; CHK:98 | VERIFIED-by-me | Đây là gốc của việc M⁺ bị "ép" còn C thì không. |
| A11 | Luật V-B giới hạn tổng trị tuyệt đối phần khách thấy z; cấu hình V-30 dùng cơ sở ngân sách "customerVisible". | B = 30 000 ms | CFG V-30.json:6,23; LEDGER:285-287 | VERIFIED-by-me | — |
| A12 | Cộng có dấu phần điều phối và phần giao thông thì ra đại lượng của M⁺ (p − p0), cộng trị tuyệt đối thì ra V; vì vậy "tính cả hai phần" không phải luật mới. | — | HO:113-114; SPEC:50,62-63 (chuỗi liên tục v_t = p_{t−1}) | VERIFIED-by-me | Suy luận theo định nghĩa (tổng z co về p_cuối − p0). |
| A13 | Lời hứa đầu được công bố lúc xác nhận đặt xe. | `initialPromiseTrigger: booking-confirmation` | WP4:5; CHK:139 | VERIFIED-by-me | — |
| A14 | Bộ chọn phương án xếp hạng theo thứ tự từ điển: (1) ít phương án "bị ép" nhất (chỉ khi có), (2) nhận nhiều yêu cầu mới nhất, (3) mức dùng ngân sách lớn nhất nhỏ nhất và các mức sửa lời hứa (khi có trần cứng), (4) chi phí kế hoạch, (5) thứ hạng mã phương án để phá hòa. | — | SEL:271-385 (290, 300, 323, 367, 381); CHK:108-112; R15 row 33 | VERIFIED-by-me | Mức (1) chỉ bật với hồ sơ HardVector/SoftHardHybrid (SEL:276-280). |
| A15 | Vì có trần 0, mức dùng ngân sách lớn nhất luôn bão hòa ở 1 000 000 ppm, nên tầng này không phân biệt phương án trên các quyết định đã ghi. | U 3.503/3.503; C-30 3.506/3.506 quyết định (incumbent = bound = có mức) | HVA:612-626; A:7,9; FJO:3,7; CHK:114-115,174,179 | VERIFIED-by-me (mã + output Codex A và Claude FJO) | Bão hòa quan sát được ≠ mọi tầng ổn định đều hằng; các tầng sửa lời hứa sau nó vẫn xếp hạng (R18 B22). |
| A16 | "Chi phí kế hoạch" mà bộ chọn dùng là thời lượng còn lại của tuyến dự kiến tính bằng mili giây từ thời điểm quyết định, không phải chi phí vận hành thực. | — | PROJ:143-148; CSE:61-83; SEL:365-368; CHK:104,120 | VERIFIED-by-me | Được tính lặp qua các quyết định; không suy ra tiền xăng hay lợi nhuận (R18 §2). |
| A17 | Chính sách mặc định là RollingCost; các nhánh hard-vector gọi bộ đánh giá cứng có phương án giữ nguyên an toàn và hai luật phục hồi. | — | POL:287,322-334; CHK:116-117 | VERIFIED-by-me | Đổi sang RollingCost sẽ bỏ cả bộ đánh giá cứng (R18 B20). |
| A18 | Luật phục hồi (b) "không tệ hơn tuyến giữ" (ADR-077): trên xe đã bị ép, một phương án bị loại được giữ làm phương án bị ép khi tuyến giữ cũng mắc đúng lỗi đó và phương án không tệ hơn ở lỗi đó; khóa pha và khóa xe không bao giờ được miễn, và mỗi miễn trừ được ghi thành vi phạm `ForcedNoWorse`. | — | ADR:5066-5092; HVA:85-99,257-300; CHK:113,127-131 | VERIFIED-by-me | ADR-077 ở trạng thái "Proposed (thăm dò)", nhánh `research/tier3-no-worse`. |
| A19 | Ở T3.8, mọi nhánh đều chạy với luật phục hồi (b). | `commitmentRecovery: no-worse-than-reference-v1` | RUN38:9; WP4:7; CHK:140,146 | VERIFIED-by-me | — |
| A20 | Trên 34 checkpoint cuối của M⁺-30 ở T3.8 có 154 mục `forcedNoWorse`, 8.371 mục `forcedReference` và 2.538 mục `exogenousServiceQuality`. | 154 / 8.371 / 2.538 | NEW:17; META:8 | VERIFIED-by-Codex R18 | Đây là số mục vi phạm, không phải số quyết định. Claude R17 kiểm 3/34 ô (11/17/0, META:9,21,11). |
| A21 | Trên 49 lần chạy C-30 (34 kiểm + 15 hiệu chỉnh) không có quyết định nào phải xử lý kẹt (non-normal). | 0/49 | T38:47; T38A:65,129,135 | VERIFIED-by-me | Kết quả theo cấu tạo: phương án giữ nguyên có c = 0. |
| A22 | Theo cấu tạo, phương án giữ nguyên kế hoạch luôn qua luật C vì phần điều phối của nó bằng 0 (\|e − e\| = 0), dưới giả thiết các kiểm tra khác đều qua. | — | V17 B8 (TEX/07:292-297); R18 B8 | VERIFIED-by-Codex R18 | Tôi không mở TEX. Giữ giả thiết (N). Một hạn chót nới kiểu Hörl–Zwick max(p0 + B, e) cũng có tính chất này [suy luận, V17 R6]. |
| A23 | Bộ kiểm quyết định dừng ở lỗi đầu tiên (rider đầu, tầng đầu) trừ khi bật hồ sơ thu đủ witness; T3.8 không bật hồ sơ này. | — | VALID:222-239; NEW:13 (T3.8 không có `solverExecutionEvidenceProfile`, WP14r có); R15 row 30 | VERIFIED-by-me | Một witness ngân sách ghi lại không phải bằng chứng đủ về tính khả thi của phương án. |
| A24 | Bộ sinh phương án bị chặn: tối đa 100 phương án mỗi xe, 2 yêu cầu mới mỗi xe, giữ lại theo danh mục ổn định tập phục vụ, hạt giống 7, OR-Tools 9.15. | 100 / 2 / seed 7 | WP4:9-23; CHK:141-144 | VERIFIED-by-me | Mỗi nhánh T3.8 có 1 yêu cầu bị bỏ (A:7-9 `omitted_requests` 1). |
| A25 | Ngưỡng sửa lời hứa "đáng kể" là 1 000 ms trên giờ thô và độ rộng 60 000 ms; con số sau là ngưỡng, không phải cách hiển thị cho khách. | 1 000 / 60 000 ms | CFG C-30.json:90-93; HO:378-380 | VERIFIED-by-me | Lý lẽ "khách không thấy 30 s" đã bị rút (HO:378-380). |
| A26 | Kiểm chéo đặc tả: ở cả 382.006 lần sửa giờ trả của 185 lần chạy T3.8, \|x\|, \|c\|, \|z\| tính lại bằng đúng các trường chênh lệch trong sổ cái. | 382.006; 0 lệch | T38:106; T38I:68 | VERIFIED-by-me | Kiểm bằng mã độc lập của agent. |
| A27 | Thời điểm ADR-077, bộ kiểm thử `dotnet test RideBound.slnx` đạt 1025/1025. | 1025/1025 | ADR:5100 | VERIFIED-by-me (văn bản ADR) | Số lịch sử, không chạy lại trong phiên này. |
| A28 | T3.8 dùng runner lưu trữ `runner-tier3-v2` (cây ac251ef3…), được publish từ commit 45f8026; khung initializeRun ghi core 1ce15e92…. | — | RUNW07:40-41; ADR:5117-5118; R14:84; R15 rows 38-40 | VERIFIED-by-me (đường dẫn, mã cây); core commit VERIFIED-by-Codex R15 | Build lại phải qua Gate 0 (R18 B24). |

## B. Thiết lập mô phỏng và dữ liệu

| ID | Câu | Số | Anchor | Trạng thái | Lưu ý |
|---|---|---|---|---|---|
| B01 | Mô phỏng dùng FleetPy 1.0.2 với bộ dữ liệu chuẩn Manhattan, nối với runner RideBound qua một adapter. | FleetPy 1.0.2 | D03:99-107; FLEET:474; RUN38:1-11 | VERIFIED-by-me | Một mô phỏng duy nhất (I01). |
| B02 | Nhu cầu lấy từ bộ dữ liệu chuẩn FleetPy dựng từ chuyến taxi NYC tuần 11–18/11/2018; mỗi ô lấy 108 yêu cầu từ một mẫu 10% trong một khung 2 giờ. | 108 yêu cầu/ô; ví dụ `2018-11-14_sample_10_3.csv`, khung 28 800–36 000 s | FIX; FLEET:360-364; INV:82; CHK:45-46,164 | VERIFIED-by-me | "108 ≈ 0,4% số chuyến thật trong 2 giờ" (HO:203) chưa được tôi tính: UNVERIFIED. |
| B03 | Mỗi ô có 8 xe sức chứa 4 trên một đồ thị 96 nút; khách chờ đón tối đa 10 phút kể từ lúc gọi và ngồi xe tối đa 1,5 lần thời gian đi thẳng. | 8 xe; 4 chỗ; 96 nút; 600 000 ms; 1500‰ | FIX; NORM:420-450 (444-445); PREF:6; CHK:124-125,157,160-165 | VERIFIED-by-me | Đồ thị là bao đóng OD 96 nút, không phải mạng đường phố (PREF:22-26). |
| B04 | Công cụ chuẩn hóa từ chối kịch bản quá 128 yêu cầu, 32 xe hoặc 96 nút. | 128 / 32 / 96 | NORM:322-328; CHK:121-123; R15 row 47 | VERIFIED-by-me | — |
| B05 | Thời gian dừng đón/trả trong các lần chạy bằng 0 s, trong khi bài FleetPy 2026 dùng 30 s mỗi khách. | 0 s (3 lần chạy mẫu); 30 s | SERV:2-4; FLEET:423-424; CHK:48-49,167 | VERIFIED-by-me | Chỉ kiểm 3 lần chạy mẫu. |
| B06 | Tắc đường là một hệ số giờ đi chung cho cả thành phố theo bin 15 phút, đọc từ tệp hệ số của bộ dữ liệu FleetPy Manhattan và lấy tỉ lệ so với đầu khung; thế giới T3.8 không có nhiễu tự tạo. | bin 900 s; sigma = shockRate = 0 | PREF:51-55,67-93; RUN38:8-9; W07:16; FR:168 | VERIFIED-by-me | Hệ số đo từ dữ liệu taxi, không phải tốc độ từng đoạn đường. |
| B07 | Tốc độ nền của mọi ô lấy lúc 00:00, nên ở đầu khung giờ đi mô phỏng bằng giờ đi đo được nhân f(0)/f(đầu khung): 0,60–0,89 ở 8h ngày thường, 0,47–0,77 ở 17h, 1,23–1,46 ở các ô sáng cuối tuần. | xem CHK:207-209 | FAC:1-9; FIX (`travelFactorAtSeconds` 0); BURD:2; CHK:166,207-209 | VERIFIED-by-me | HO:211 ghi "1,23–1,55": 1,55 là 18/11 lúc 7h, không có ô nào trong panel (SPLIT; SCOPE:14). Quy đổi lại (giữ quyết định) gần như không đổi kết luận (BURD:8,14). |
| B08 | Panel A gồm 49 ô (ngày 14–18/11 × mẫu r1–r4 × khung 7h, 8h, 17h, trừ 11 ô không dựng được), chia 15 ô hiệu chỉnh và 34 ô kiểm theo nhóm (ngày, mẫu). | 49 = 15 + 34; 11 ô thiếu | RUN38:3-7; SPLIT:2-60; T38:92 | VERIFIED-by-me | Ô `d20181114-s10-r1` đã bị xem ở smoke (T38:95). |
| B09 | Panel kiểm T3.8 có 34 ô × 108 = 3.672 yêu cầu mỗi nhánh, trải 5 ngày 14–18/11/2018; khung 7h có 9 ô, 8h có 14 ô, 17h có 11 ô. | 3.672; 9/14/11 | A:7-9; SCOPE:3,14; T38:29-33; CHK:169 | VERIFIED-by-me | — |
| B10 | T3.8 có 5 nhánh (U, C-30, M⁺-30, M⁺-60, V-30), 170 job kiểm và 15 job hiệu chỉnh đều đạt; kế hoạch niêm phong (SHA 78954a15…) được push trước job đầu. | 170 + 15; 5 mã cấu hình | T38:3-15; T38A:1-4 | VERIFIED-by-me | Nhãn "THĂM DÒ": ngưỡng, biên, cách chia do Claude chọn sau khi xem trước; chủ nghiên cứu chưa duyệt (T38:8). |
| B11 | Mỗi (ngày, mẫu, khung) chỉ cho một episode tất định; ba khung của cùng (ngày, mẫu) chung nguồn nhu cầu và chồng 3–20/108 dòng. | 3–20/108 | T38:90,93 | VERIFIED-by-me | 34 ô không phải 34 mẫu độc lập (R18 §3). |
| B12 | Tải hệ thống trung bình x = 0,814 và số khách trung bình trên xe kể cả lúc rỗi là 0,535 (U), thấp hơn nhiều so với ≈ 1,33 của bài FleetPy 2026 (180 xe, 21.400 yêu cầu, thuật toán AM). | x 0,814 (0,600–1,038); 0,535 U / 0,505 C-30; 1,33 | LOAD:2-3; FLEET:433-434,447-449,474-478; CHK:50-56; R15 row 20 | VERIFIED-by-me | Hai thiết lập khác nhau; chỉ là giới hạn mô tả. |
| B13 | Các chuyến được chọn ngắn hơn tập đủ điều kiện: trung vị đi thẳng 165 s so với 196 s, ở cả 49/49 ô. | 165 / 196 s; 49/49 | SEL6:2-4 | VERIFIED-by-me | — |
| B14 | Lời hứa đầu đã chứa sẵn thời gian chờ và đi vòng: trung bình 14,15 phút (U) và 14,12 phút (C-30), trong khi trễ trung bình so với lời hứa đầu chỉ +0,317 và +0,155 phút. | `[gộp theo khách]` | BURD:5,7,11,13 | VERIFIED-by-me | — |
| B15 | Việc B (w07) chạy 88 job trên 8 ô phát triển 7–9h ngày 12–13/11 với U, C và M⁺ ở 30/60/120/300 s, V-30, M-30. | 88 job; 864 yêu cầu | W07:1-11; RUNW07:33-34; W07AGG:1 | VERIFIED-by-me | Panel phát triển; mỗi ô trùng 7–15/108 khách với ô w08 đã xem (W07:64). |
| B16 | Việc w07x chạy thêm 104 job trên cùng 8 ô ở các mức 90–240 s, mức được chọn sau khi xem Việc B. | 104 job | W07X:1-10 | VERIFIED-by-me | — |
| B17 | Bậc thang WP14r dùng giao thông cố định trên 16 ô khung 8h/17h ngày 12–13/11, với runner đời cũ không có luật phục hồi, gồm FREE, LOCKS, C-120, C-60, C-30. | 16 ô; 1.728 yêu cầu | LAD:1-6; WBU:1; NEW:13; HO:229-242 | VERIFIED-by-me (cấu hình khác: NEW:13); core 38d517d VERIFIED-by-Codex R15 (row 39) | Không chuyển kết quả sang T3.8 (R18 B55). |
| B18 | Phép quét tier3-sweep-v1 chạy 156 job: 13 nhánh × 6 thế giới × 2 ô, gồm thế giới nhiễu tự tạo (W1, W2, W4) và thế giới đo thật W5. | 156 job | SWEEP:8-14,67-73 | VERIFIED-by-me | Thăm dò; bảng luận văn dùng bản tách thật/tự tạo (SWEEP:73). |
| B19 | Kho dữ liệu đã chạy gồm 1.991 bản ghi lần chạy. | 1.991 | INV:1 | VERIFIED-by-me | Bản kiểm kê của Claude; bản của Codex tôi không mở. |
| B20 | Buổi chiều tuyết là 8 ô ngày 15/11/2018 (khung 14–16h và 15–17h, C-30) với 601 khách được chở. | 8 ô; 601 | SNOW:2-10; RP1:6 | VERIFIED-by-me | — |
| B21 | Ngày 11/11/2018 là Chủ nhật và 12/11 là thứ Hai; báo cáo dự báo ghi 12/11 là ngày nghỉ bù Veterans Day. | — | RX:16; FR:97 | VERIFIED-by-me (thứ trong tuần); trạng thái ngày nghỉ: UNVERIFIED ở nguồn gốc | Không mở lịch chính thức. |
| B22 | Dữ liệu taxi vàng TLC 2016-07…2020-02 nặng khoảng 5,354 GB (44 tệp) và cả năm 2013 khoảng 2,144 GB, theo metadata. | 5.354.364.554 B; 2.143.914.255 B | SIZE:2; SF:31 | VERIFIED-by-me | Kích thước nén theo HEAD, không phải chi phí dựng lại. |
| B23 | Hai tệp chính thức tháng 1 và 11/2013 đã kiểm chỉ có mã vùng đón/trả, không có tọa độ. | 14.776.617 / 14.388.451 dòng | META:2-3; PQ:1-2 | VERIFIED-by-me | Chỉ hai tệp; không suy ra cho mọi tháng (R18). |
| B24 | Số chuyến mỗi ngày của taxi vàng là 479.527 (11/2013) so với 271.501 (11/2018), còn xe công nghệ lớn (FHV-HV) là 691.379 (11/2018). | 479.527 / 271.501 / 691.379 | TLC:1,552,556,860; CHK:70-72 | VERIFIED-by-me | Bảng không có dòng FHV-HV 2013; không suy ra "tăng từ 0". |
| B25 | Năm 2013 có 2 ngày thường tuyết từ 3 inch (8/2 và 8/3); mười ngày thứ Hai–thứ Năm trong cửa sổ Fielbaum–Alonso-Mora đều không có tuyết. | 6 ngày ≥ 1 in; 2 ngày ≥ 3 in | NOAA13:4,6; NEW:10; CHK:73 | VERIFIED-by-me | Ngày lễ chưa bị loại khỏi phép đếm. |
| B26 | Trong giai đoạn kiểm đề xuất 9/2018–12/2019 chỉ có 5 đợt tuyết ≥ 25,4 mm (ghép ngày cách nhau ≤ 2), một đợt chính là 15/11/2018 đã xem. | 5 đợt | NEW:9; WX:6-7; WX17:4-5 | VERIFIED-by-me | Proxy thời tiết, không chứng minh độc lập hay gây tắc. |
| B27 | TLC công bố dữ liệu chuyến theo tháng, thường trễ khoảng hai tháng. | ~2 tháng | R18 B72 (trang TLC, kiểm 2026-10-10) | VERIFIED-by-Codex R18 | Nguồn web, tôi không mở lại. |

## C. Kết quả chính (T3.8, 34 ô kiểm, 3.672 yêu cầu)

| ID | Câu | Số | Anchor | Trạng thái | Lưu ý |
|---|---|---|---|---|---|
| C01 | Trên 34 ô kiểm, U chở 2.434 khách, C-30 và M⁺-30 cùng chở 2.338, M⁺-60 chở 2.347 và V-30 chở 2.336. | `[đếm]` | T38:46; T38A:69; A:7-9; T38I:84 | VERIFIED-by-me | Nguồn chính lấy từ checkpoint cuối (T38:113). |
| C02 | So với U, C-30 chở ít hơn 96 khách, tức 2,61 điểm phần trăm số yêu cầu hay 3,94% số khách U chở; trung bình 2,82 khách mỗi ô, khoảng 95% [1,79; 3,82]. | −96; 2,61 pp `[trên yêu cầu]`; 3,94%; F +2,82 | T38:49; T38A:61; CHK:185 | VERIFIED-by-me | Chi phí không đều: U − C-30 > 2 khách ở 21/34 ô, khoảng −4..+9 (T38:109). Sàn 5 do Claude chọn, chưa được duyệt (T38:85). |
| C03 | Chi phí phục vụ tập trung ở khung 8–10h (−39 khách) và 17–19h (−52), còn khung 7–9h chỉ −5. | 1.014→975; 904→852; 516→511 | T38:50-52; T38A:81-94; CHK:199 | VERIFIED-by-me | — |
| C04 | Hai tập khách được chở khác nhau: U và C-30 chung 2.207 khách, 227 chỉ U, 131 chỉ C-30; C-30 và M⁺-30 chung 2.332, mỗi bên 6 riêng. | 2.207/227/131; 2.332/6/6 | A:18-19; FJS:3-4 | VERIFIED-by-me (Codex A và Claude FJS độc lập) | "Cùng số khách" ≠ "cùng khách". |
| C05 | Với khách được cả U và C-30 chở, C-30 có thời gian ngồi xe ngắn hơn 10,5 s và chờ lâu hơn 0,5 s. | chờ +0,522 s; ngồi −10,507 s; tổng −9,985 s | COM:2-3 | VERIFIED-by-me | Tập khách chung là tập sau điều trị, không phải phép so ngẫu nhiên. |
| C06 | Theo lời hứa ngây thơ, số khách đến trễ hơn lời hứa đầu quá 60 s là 203 (U), 76 (C-30) và 74 (M⁺-30). | 8,34% / 3,25% / 3,17% `[gộp theo khách]` | A:7-9; LATE:5,12,19; CHK:170,175,180 | VERIFIED-by-me | Trễ tính so với lời hứa trả đầu (DIALPY:8). |
| C07 | Trễ quá 120 s là 102 (U) so với 11 (C-30, M⁺-30); trễ quá 300 s là 18 so với 0; trễ quá 600 s là 2 so với 0. | `[đếm]` | A:7-9 | VERIFIED-by-me | — |
| C08 | Tính trên mỗi yêu cầu, số lượt đến không trễ quá 60 s là 2.231 (U), 2.262 (C-30), 2.264 (M⁺-30); không trễ quá 120 s là 2.332, 2.327, 2.327. | timely60 60,76% / 61,60% / 61,66% `[trên yêu cầu]` | A:7-9; DIAL17:12-13; CHK:170,175,180 | VERIFIED-by-me | timely = phục vụ − trễ; yêu cầu bị từ chối không tính là kịp (DIALPY:9). Ở 120 s, U hơn C-30 5 lượt. |
| C09 | Khi phát lại lời hứa có dự báo (causal-no15) trên cả 34 ô, trễ quá 60 s còn 137 (U), 10 (C-30), 10 (M⁺-30); kịp 60 s là 2.297 / 2.328 / 2.328; kịp 120 s là 2.347 / 2.338 / 2.338. | C-30 0,43% `[gộp theo khách]` | A:7-9; DIAL17:12-13; PAD:12,33,54; CHK:171,176,181 | VERIFIED-by-me | Chỉ phát lại lớp lời hứa trên quỹ đạo đã có; dự báo hoạt động ở 21/34 ô (DIAL17:12-13 "active 21"). |
| C10 | Không trần nhưng có dự báo và đệm thêm 30 s, U cũng đạt 2.328 lượt kịp 60 s như C-30 có dự báo, đạt 2.366 lượt kịp 120 s (C-30: 2.338), nhưng lời hứa dài thêm 37,18 s thay vì 7,37 s và 1,81% khách tới sớm quá 60 s thay vì 0,17%. | U+fc+30: trễ60 106, kịp60 2.328, kịp120 2.366, ext 37,18 s, early60 44/2.434; C-30+fc: ext 7,37 s, early60 4/2.338 | A:7,9; NEW:2; PAD:14,33; R15:165-177; CHK:172,176 | VERIFIED-by-me | Đây là điểm đánh đổi đã đo, không phải ưu thế chung của C. Đệm U là phát lại, không phải đối chứng ghép cặp. |
| C11 | Đệm 60 s trên U có dự báo cho 2.347 lượt kịp 60 s và 2.386 lượt kịp 120 s, nhưng 42,44% khách tới sớm quá 60 s và lời hứa dài thêm 67,18 s. | trễ60 87; early60 1.033 | A:9; PAD:15; CHK:173 | VERIFIED-by-me | Phải trình bày cùng hàng đệm 30 s (R15 §2). |
| C12 | Đệm đều lời hứa ngây thơ của C-30 xóa được trễ nhưng làm lời hứa vô nghĩa: đệm 60 s còn 0,47% trễ nhưng 29,21% tới sớm, đệm 180 s còn 0% trễ nhưng 99,53% tới sớm. | `[gộp theo khách]`; đệm 120 s: 0,17% / 96,75% | PAD:28-31 | VERIFIED-by-me | — |
| C13 | Theo nghĩa vụ của chính từng luật, C-30 bị ép ở 0% quyết định và không phá lời hứa của nó với khách nào, trong khi M⁺-30 bị ép ở 41,3% quyết định và phá lời hứa của chính nó với 14,5% khách. | `[TB theo ô]`: ép 0 / 41,3 / 22,5 / 53,8% (C-30, M⁺-30, M⁺-60, V-30); phá hứa 0 / 14,5 / 4,2 / 21,6%; `[gộp theo khách]` M⁺-30 12,4%, M⁺-60 3,4%; ô có ≥ 1 phá hứa 0/28/22/34 | T38:58-60,111; T38A:76-79 | VERIFIED-by-me | Hai luật kiểm hai nghĩa vụ khác nhau; không phải so cùng một chuẩn đúng giờ (R15 row 2). |
| C14 | Ở khung 7–9h, M⁺-30 phá lời hứa của chính nó với 36,5% khách (9/9 ô) và bị ép ở 75,6% quyết định, còn ở 17–19h chỉ 1,0% (5/11 ô) và 5,0%. | `[TB theo ô]` | T38:62-63; T38A:83,95 | VERIFIED-by-me | Phụ thuộc cách hứa: dự báo trong bộ điều phối giảm phá hứa 69% (FR:125-133). |
| C15 | C-30 và M⁺-30 có cùng chuỗi hành động đội xe ở 30/34 ô; C-30 và V-30 ở 27/34 ô. | 30/34; 27/34 | T38:64; T38A:71 | VERIFIED-by-me | Không phải ở mọi ô. |
| C16 | Chênh số khách trung bình mỗi ô giữa C-30 và M⁺-30 là 0,00 [−0,15; +0,12], giữa C-30 và V-30 là +0,06 [−0,12; +0,21], và không ô nào lệch quá 2 khách. | D_M 0,0000; D_V +0,0588 | T38:43-45,110; T38A:59-60,70 | VERIFIED-by-me | Khoảng bootstrap theo ô, 34 ô phụ thuộc theo ngày. |
| C17 | Khoảng dự phòng γ hiệu chỉnh trên 15 ô là 222,259 s (β + γ = 252,259 s); 2/34 ô kiểm vượt γ (5,9%), cả hai ở khung 7h, cận trên Clopper–Pearson 95% là 17,4%. | γ 222,259 s; 2/34; CP 17,4%; khung 7h phủ 7/9 | T38:19-37; T38A:6-15 | VERIFIED-by-me | γ do một ô quyết định; không cấp bảo đảm cho ngày mới (D03:224-225). |
| C18 | Bảy trên tám dự đoán niêm phong của T3.8 đúng; P7 sai (M⁺-30 phá hứa ở 5/11 ô 17h, dự đoán ≤ 3/11). | 7/8 | T38:67-79; T38A:131-139 | VERIFIED-by-me | Dự đoán viết sau khi đã xem trước panel phát triển. |
| C19 | Một agent kiểm độc lập tính lại 13 hạng mục của T3.8 từ bản ghi thô và không thấy hạng mục nào lệch. | 13/13 | T38I:79-97 | VERIFIED-by-me | — |
| C20 | Số khách bị điều phối dời giờ trả ít nhất một lần là 174 (U) so với 33 (C-30); 12 khách U bị dời từ hai lần trở lên, còn C-30 không có ai; tổng dời lớn nhất của một khách là 590,1 s (U) và 29,2 s (C-30). | 7,15% / 1,41% `[gộp theo khách]`; M⁺-30: 29 | A:7-9; BUC:34,37; CVP:14; CHK:174,179,184 | VERIFIED-by-me | — |
| C21 | Trong 203 khách U trễ quá 60 s, 134 người từng bị điều phối dời giờ trả (77,01% khách U bị dời là trễ), còn ở C-30 chỉ 4/76 và M⁺-30 1/74. | 134/203; 134/174 = 77,01%; 4/76; 1/74 | EXP:2-4; A:7-9 (`late60_and_exposed`); CHK:204 | VERIFIED-by-me | Đây là giao của hai tập, không phải tỉ lệ nhân quả. 72 khách trễ của C-30 không có thay đổi giờ trả do điều phối được ghi, chưa chứng minh trễ thuần vì kẹt xe (R15 corr. 2). |
| C22 | Mỗi lần điều phối dời giờ trả, trung vị là 108,6 s ở U (187 lần) và 8,3 s ở C-30 (33 lần, lớn nhất 29,2 s). | trung vị theo lần sửa | CON:6,13 | VERIFIED-by-me | Quần thể là các lần sửa khác 0, khác thống kê theo khách của BUC (R15 row 13). |
| C23 | Ở C-30, 29 khách (1,24%) bị điều phối dời giờ trả muộn đi và 4 khách được trả sớm hơn. | 29/2.338; 4 | BUC:37; CHK:205 | VERIFIED-by-me | — |
| C24 | Theo sổ cái, phần dời do điều phối chiếm 73,4% số giây trễ của các khách U trễ quá 60 s, nhưng chỉ 1,2% ở C-30. | 73,4% / 1,2% | CON:5,12 | VERIFIED-by-me | Kết quả của sổ cái mô hình, không phải quan hệ nhân quả (HO:385). |
| C25 | Tỉ lệ khách đi chung là 22,8% (U), 13,4% (C-30) và 13,1% (M⁺-30); tỉ lệ phút-hành-khách đi chung là 15,2%, 7,6% và 7,4%. | `[gộp theo khách]`; 2.962 / 1.388 / 1.341 phút đi chung | SHARE:2-4; STT:2-4; EXP:2-4 | VERIFIED-by-me | Số tuyệt đối ≈ 555 / 313 khách chỉ là xấp xỉ từ % làm tròn (R18 B32; CHK:202). |
| C26 | Phân bố trễ so với lời hứa đầu: U có 8,34% trễ quá 1 phút, 4,19% quá 2 phút, 0,74% quá 5 phút và lâu nhất 11 phút; C-30 có 3,25%, 0,47%, 0% và lâu nhất 3,87 phút; C-30 có dự báo có 0,43%, 0%, 0% và lâu nhất 1,90 phút. | `[gộp theo khách]`; U >10 phút 0,08% | LATE:3-5,10-12,24-26 | VERIFIED-by-me | — |
| C27 | Tính trung bình theo ô, tỉ lệ khách trễ quá 1 phút là 9,10% (U) và 4,12% (C-30), trễ quá 5 phút là 0,77% và 0%. | `[TB theo ô]` | T38RX:10-18 | VERIFIED-by-me | Khác số gộp ở C26; luôn ghi mẫu số. |
| C28 | Nếu một hợp đồng giả định bồi thường mọi lượt trả muộn quá T so với lời hứa đầu, số lượt phải bồi thường trên 100 yêu cầu là 5,53 / 2,78 / 0,49 / 0,05 (U) và 2,07 / 0,30 / 0 / 0 (C-30) ở T = 1 / 2 / 5 / 10 phút. | C-30 có dự báo: 0,27 / 0 / 0 / 0 | A:7,9 (đếm ngây thơ / 3.672); V13:111-121; CHK:203 | VERIFIED-by-me (số học) | Giữ mọi tham số tiền dạng ký hiệu; không phải ROI (R15 corr. 3). |
| C29 | Phép tính độ nhạy giản lược: với −96 lượt phục vụ và −127 lượt trễ quá 60 s, C chỉ có lợi hơn U nếu chi phí một lượt trễ vượt 0,756 lần biên lợi nhuận một chuyến, khi mọi yếu tố khác bằng 0. | 96/127 = 0,756 | R15:231-235; CHK:206 | VERIFIED-by-me (số học) | Hai nhóm khách khác nhau; không có chuyển đổi một-một. |
| C30 | Ở cả 25 ô khung 8h và 17h, U có nhiều khách trễ quá 60 s (ngây thơ) hơn C-30; ở 9 ô khung 7h, U nhiều hơn ở 3 ô và bằng ở 6 ô. | 14 + 11 ô; 3 dương, 6 bằng | DER17:2-13; NEW:4 | VERIFIED-by-me | 25 ô không phải 25 ngày độc lập. |
| C31 | Ví dụ một khách (ô d20181115-s10-r1-w07): đặt xe 7:11:56, được hứa trả 7:34:51, đón 7:22:30, tới nơi 7:38:02, tức trễ 190,5 s; lời hứa có dự báo là 7:37:44, chỉ lệch 17,6 s. | +190,5 s; +17,6 s; hứa dài thêm 172,9 s | EXAMPLE:1-4,60-61; R15 row 56 | VERIFIED-by-me | Một ví dụ minh họa, không phải bằng chứng thống kê. |
| C32 | Không có bằng chứng "C phục vụ nhiều hơn": kết quả là tương đương về số khách với luật hạn chót. | — | T38:82-85; W07X:66-70 | VERIFIED-by-me | — |

## D. Núm vặn mức trần (w07/w07x, WP14r) và phép sàng lọc

| ID | Câu | Số | Anchor | Trạng thái | Lưu ý |
|---|---|---|---|---|---|
| D01 | Trên 8 ô sáng 7–9h (864 yêu cầu), số khách được chở là 665 (U), 660 (C-30), 661 (C-60), 664 (C-90), 666 (C-120, C-150, C-180) và 665 (C-240, C-300). | `[đếm]` | CAP:3-11; DIAL17:3-11; W07X:20-29; W07AGG:2-6 | VERIFIED-by-me (Codex CAP và Claude DIAL17 độc lập) | 8 ô phát triển, mỗi ô 1 episode. |
| D02 | Trên các ô này, số khách trễ quá 60 s / kịp 60 s / kịp 120 s là 50 / 615 / 656 (U), 47 / 613 / 658 (C-30), 50 / 614 / 660 (C-90) và 51 / 615 / 659 (C-120). | `[đếm]`, lời hứa ngây thơ | CAP:3-11; DIAL17:3-11 | VERIFIED-by-me | Dự báo causal-no15 không hoạt động ở 12–13/11 nên cột dự báo bằng ngây thơ (CAP:2). |
| D03 | Nới C-30 lên C-120 trên 8 ô sáng cho thêm 6 khách được chở, 4 khách trễ quá 60 s, 5 khách trễ quá 120 s, 2 lượt kịp 60 s và 1 lượt kịp 120 s. | +6 / +4 / +5 / +2 / +1 | CAP:4,7; CHK:198 | VERIFIED-by-me | Không có quy luật đơn điệu: C-120 (666) > U (665). |
| D04 | Ở w07, M⁺ bị ép ở 58,6% / 35,5% / 13,0% / 6,6% / 6,8% / 2,8% / 1,7% / 1,7% quyết định tại các mức 30 / 60 / 90 / 120 / 150 / 180 / 240 / 300 s, còn C luôn 0%, và hai luật chở bằng nhau trong phạm vi 2 khách. | `[TB theo ô]` | W07X:20-29; W07:34-39 | VERIFIED-by-me | — |
| D05 | Ba chỗ hai luật C và M⁺ tách nhau ở 90–120 s đều có cùng cơ chế: một khách đang trên xe đã trễ 61–79 s do tắc đường và phép ghép thêm 61–68 s do điều phối vượt hạn chót của M⁺ nhưng không vượt ngân sách của C; mỗi lần như vậy C nhận thêm đúng 1 khách. | 79,0 + 68,3 s; 60,9 + 61,2 s | W07XM:2-16; W07X:48-62 | VERIFIED-by-me | Phân bổ theo phép chiếu mô hình (R15 row 17). |
| D06 | Ở ô d20181113-s10-r1-w07 dưới C-300 và M⁺-300, khách trễ nhất trễ 307,3 s gồm 99,1 s do tắc đường và 208,2 s do điều phối. | 307,3 = 99,1 + 208,2 s | W07:48-54 | VERIFIED-by-me | Mô tả sau khi xem, không phải dự đoán. |
| D07 | Ở C-120 trên 8 ô sáng chỉ 9 khách (1,35%) bị dời giờ trả do điều phối, tổng dời lớn nhất 96,7 s, không ai dùng tới 90% ngân sách; ở C-30 chỉ 2 khách, lớn nhất 10,0 s. | 9 / 1,35%; 2 / 0,30% | BUC:8,17; A:10,14 | VERIFIED-by-me | — |
| D08 | Trên bậc thang WP14r (giao thông cố định, 1.728 yêu cầu), tỉ lệ phục vụ / đi chung / bị dời giờ trả / trễ quá 60 s lần lượt là 94,3 / 53,1 / 23,8 / 16,82% (FREE), 91,7 / 21,8 / 3,9 / 2,97% (LOCKS), 90,5 / 19,4 / 2,6 / 1,47% (C-120), 89,1 / 17,3 / 1,3 / 0% (C-60), 88,8 / 15,7 / 0,4 / 0% (C-30). | `[gộp theo khách]` | LAD:2-6; R15 row 14 | VERIFIED-by-me | Runner đời cũ, không có luật phục hồi (B17). |
| D09 | Trên WP14r, số khách được chở / trễ quá 60 s / kịp 60 s / kịp 120 s là 1.629 / 274 / 1.355 / 1.465 (FREE), 1.584 / 47 / 1.537 / 1.557 (LOCKS), 1.563 / 23 / 1.540 / 1.563 (C-120), 1.540 / 0 / 1.540 / 1.540 (C-60), 1.534 / 0 / 1.534 / 1.534 (C-30). | `[đếm]` | WP17:2,5,9,14,19; CHK:197 | VERIFIED-by-me | — |
| D10 | Trên WP14r, nới C-30 lên C-120 cho thêm 29 khách được chở, 23 khách trễ quá 60 s và 6 lượt kịp 60 s. | +29 / +23 / +6 | WP17:9,19; CHK:197 | VERIFIED-by-me | Mâu thuẫn với câu "nới trần chỉ có lợi ở ngưỡng 2 phút" của V17 (xem K13). |
| D11 | Trên WP14r, điểm gãy nằm giữa 60 và 120 s: khách trễ quá 60 s tăng từ 0 lên 23 khi đi từ C-60 lên C-120. | 0 → 23 | WP17:9,14; LAD:4-5; HO:241 | VERIFIED-by-me | Một điểm đánh đổi; không có mức tối ưu. |
| D12 | Mức C-120 chưa được chạy trên 34 ô chính của T3.8. | — | T38A:69 (chỉ 5 nhánh); V17:365-369; NEW:18 | VERIFIED-by-me | Là Stage 1a của nghiên cứu tùy chọn (mục L). |
| D13 | Trên 34 ô T3.8 dưới C-30, 148 yêu cầu cuối cùng bị từ chối và có ít nhất một phương án mang dấu vết bị chặn do ngân sách của khách khác (U chở 116 trong số đó); 1.186 lượt từ chối còn lại chỉ có lý do cấu trúc. | 148 (116 U chở, 32 U cũng từ chối); 1.075 + 111 = 1.186; tổng từ chối 1.334 | BUD:2-5; CON:10; CHK:191 | VERIFIED-by-me | Phân loại theo bản ghi, không chứng minh 148 khách bị từ chối **chỉ** vì trần (R15 row 59; R18 §4 Câu 2). |
| D14 | Với 148 yêu cầu đó, mức vượt nhỏ nhất có trung vị 109,6 s (p25 63,7; p75 183,6; lớn nhất 524,8 s), nên các ngưỡng được ghi qua sàng lọc ở B = 60 / 120 / 300 s cho 11 / 59 / 135 yêu cầu. | B ≈ 139,6 s (trung vị), ≈ 554,8 s (tất cả) | BUD:6-9; CHK:194 | VERIFIED-by-me | Sàng lọc bậc một, dừng ở lỗi đầu; không bảo đảm cả 148 trở nên hợp lệ. Tổng dời lớn nhất của U là 590,1 s > 554,8 s. |
| D15 | Ở sàng lọc này, tại B = 60 / 120 / 300 s có 5 / 51 / 123 lần một khách đang đi cùng bị đẩy trễ quá 60 s và 0 / 6 / 79 lần quá 120 s; 59 lượt qua ở 120 s liên quan 58 cặp (khách chặn, lần chạy) khác nhau. | `[đếm lần xuất hiện]` | SF:12,14,18 | VERIFIED-by-me | Số lần, không phải số người; không cộng thành một quỹ đạo. |
| D16 | 1.256 bản ghi chặn do ngân sách giờ trả không phải 1.256 khách: chúng nằm trong 971 quyết định và 973 cặp (yêu cầu, lần chạy), trong đó 807 cặp (82,9%) cuối cùng vẫn được phục vụ; riêng T3.8 C-30 có 643 cặp, 495 được phục vụ, 148 bị từ chối. | 1.256 / 971 / 973 / 807 / 166 | SF:2-11; CHK:194 | VERIFIED-by-me | — |
| D17 | Trên w07 ở B = 120 s, sàng lọc dự báo 6 lượt qua, còn lần chạy thật được thêm 17 và mất 11 khách (ròng +6): số ròng gần đúng nhưng danh tính sai. | 6; +17 / −11 | SF:21,26; R18 B49 | VERIFIED-by-me | Hiệu chỉnh yếu. |
| D18 | Sàng lọc ngân sách theo độ dài chuyến cho 30 yêu cầu qua (chia đều: 11) ở mức trung bình 60 s và 89 (chia đều: 59) ở 120 s. | 30/11; 89/59; 148/135 ở 300 s | PROP:1-7 | VERIFIED-by-me | Không phải số khách được cứu hay trần lợi ích; phân bổ là việc tương lai (R15 corr. 4). |
| D19 | Chỉ 2/148 khách chặn đã tiêu ngân sách trước đó; cả 148 bản ghi đều có một bước dời đơn lẻ vượt B. | 2/148 | BUD:10; FJC:4-6 | VERIFIED-by-me | — |
| D20 | Không có chuẩn ngành cho loại trần này; 30 s chỉ là mức thận trọng và chưa có căn cứ WTP/ROI bên ngoài. | — | D03:260; HO:255-258; CHK:81 | VERIFIED-by-me | So sánh gần nhất: biên giờ đón "2 hoặc 3 phút" của Lu & Kühnel (J22). |

## E. Kiểm toán vế cộng dồn của luật C

| ID | Câu | Số | Anchor | Trạng thái | Lưu ý |
|---|---|---|---|---|---|
| E01 | Trong 98 lần chạy cưỡng chế C dùng hệ số giao thông đo (64.371 quyết định được xác nhận), cả 1.256 bản ghi chặn do ngân sách giờ trả đều có một bước dời do điều phối đã vượt B của nhánh tương ứng, và 0 bản ghi chỉ do cộng dồn. | 98 = 34 + 64; 64.371; 1.256 = 845 + 411; 0 | A:7,10-17; NEW:1; FJC:4-30; CHK:186,192-193 | VERIFIED-by-me (Codex A và Claude FJC là hai bộ đọc độc lập) | B thay đổi từ 30 đến 300 s giữa các nhánh w07 (NEW:1 `by_arm`); không phải tất cả vượt 30 s. |
| E02 | Dưới C trên giao thông đo, không khách được chở nào có quá một lần dời giờ trả khác 0 do điều phối. | `repeated` = 0 | A:7,10-17; NEW:1; BUC:8-38 (max 1) | VERIFIED-by-me | Chỉ nói về thay đổi giờ trả do điều phối, không về mọi chiều (R18 B41). |
| E03 | Trên giao thông cố định, C-60 có 2 bản ghi có thể chỉ do cộng dồn trong 1 quyết định và C-120 có 4 bản ghi trong 3 quyết định; mọi yêu cầu mới liên quan cuối cùng vẫn được phục vụ. | 2/1; 4/3; 0 bị từ chối | A:3-5; FJC:31-45; FJR:2-4 | VERIFIED-by-me | Dấu vết được ghi, không phải tác dụng đo được. |
| E04 | Ở một thế giới giả lập (C-120, W4), có 6 bản ghi trong 5 quyết định nếu tính cả lần chạy lặp, và 4 bản ghi trong 3 quyết định sau khi bỏ bản lặp, với một yêu cầu liên quan cuối cùng bị từ chối. | 6/5 → 4/3; 1 từ chối | A:6,20; FJR:5-7; R15 row 28 | VERIFIED-by-me (đếm); khử trùng lặp VERIFIED-by-Codex R15 | Không phải một khách bị mất do cộng dồn đã chứng minh. |
| E05 | Ví dụ một bản ghi chỉ do cộng dồn: khách đã dùng 51,755 s, phép ghép thêm 80,304 s, tổng 132,059 s > 120 s dù mỗi bước đều dưới B. | 51,755 + 80,304 = 132,059 s | FJC:42; R15 row 27 | VERIFIED-by-me | — |
| E06 | Trên các quỹ đạo không trần đã ghi, số khách mà luật cộng dồn và luật mỗi bước cho kết quả khác nhau là rất ít: ở B = 30 / 60 / 120 / 300 s có 2 / 0 / 13 / 6 trên 1.629 khách FREE, 0 / 0 / 4 / 0 trên 2.434 khách U của T3.8, và 0 ở LOCKS. | WP9 A: 0/1/12/18 trên 1.735; WP9 B: 0/0/10/10 trên 966 | CVP:4-38 | VERIFIED-by-me | Sàng lọc trên đường đã đi, không dự đoán quỹ đạo của chính sách khác; WP9 dùng runner cũ. |
| E07 | Một khách U trên T3.8 bị dời 25,844 s rồi 99,027 s (tổng 124,871 s): mỗi bước ≤ 120 s nhưng tổng > 120 s. | 124,871 s | R14:59; R15 row 24 | VERIFIED-by-Codex R15 | — |
| E08 | Vế cộng dồn vẫn định nghĩa một nghĩa vụ khác: luật "mỗi lần ≤ 30 s" cho phép ba lần tổng 90 s, còn luật tổng ≤ 30 s thì không. | 3 × 30 = 90 s | BUDGET:51,88 (tổng trước + bước mới); R18 §4 Câu 3 | VERIFIED-by-me (theo định nghĩa) | — |
| E09 | Nhánh "mỗi bước một trần" chưa được cài đặt và chưa chạy, nên không biết bỏ cộng dồn có giữ nguyên quỹ đạo hay kết quả không. | — | R15 row 32; R18 B97; V17 R3 | VERIFIED-by-Codex R15/R18 | Không viết "giống hệt" và không viết "vô dụng". |
| E10 | Ở các quần thể C khác vẫn có khách bị dời hai lần: WP14r C-120 có 1 khách (25,661 + 5,924 = 31,585 s), thế giới giả lập C-120 có 1 khách khác nhau (bị nhân đôi bởi lần chạy lặp). | WBU:10 max 2; A:3 repeated 1; A:6 repeated 2 (gồm bản lặp) | WBU:10; A:3,6; R15 row 25, W2 | VERIFIED-by-me (WBU, A); khử trùng lặp VERIFIED-by-Codex R15 | "Không ai bị dời hai lần" chỉ đúng cho C trên giao thông đo. |

## F. Lời hứa có dự báo

| ID | Câu | Số | Anchor | Trạng thái | Lưu ý |
|---|---|---|---|---|---|
| F01 | Lời hứa trả hiển thị là D = max(p, S), trong đó S kéo dài phần thời gian còn lại p − t theo mức tăng dự báo của hệ số giờ đi toàn thành phố (trung bình các ngày nguồn) sau bin hiện tại; lời hứa không bao giờ bị rút ngắn. | bin 15 phút; trọng số bin hiện tại = 1 | DISP:1-8,60-64; STRETCH:1-12,25-52; CHK:151,153-154 | VERIFIED-by-me | Neo vào mức đo hiện tại; chỉ hình dạng tăng lấy từ ngày khác (STRETCH:10-11). |
| F02 | Quy tắc chính causal-no15 chỉ dùng các ngày cùng loại trước đó, không bao giờ dùng 15/11 (ngày tuyết), và cần ít nhất 2 ngày nguồn; vì vậy chỉ 14, 15, 16/11 có dự báo, còn 12, 13, 17, 18/11 thì không. | — | DISP:10-16,34-52; CHK:152 | VERIFIED-by-me | Cuối tuần không có ngày nguồn (HO:288). |
| F03 | Họ A (kế hoạch niêm phong a5524912…) chỉ phát lại lớp lời hứa trên 170 lần chạy kiểm T3.8, không chạy mô phỏng mới. | 170 lần chạy | FR:3-11 | VERIFIED-by-me | Nhãn "đo lường có đăng ký trước trên các ngày-khung đã được xem trước" (FR:38). |
| F04 | Với C-30 trên 21 ô ngày thường có dự báo, tỉ lệ khách trễ quá 60 s so với lời hứa đầu giảm từ 6,01% xuống 0,17% (khung 7h: 14,44% → 0,27%), trong khi một đệm đều cùng giá chỉ xuống 1,94%. | `[TB theo ô]`; khung 8h 1,35% → 0,18%; 17h 0 → 0 | FR:40-49; FA:8-11 | VERIFIED-by-me | `[gộp theo khách]` trên 21 ô là 2/1.471 = 0,136% (RP1:40; CHK:196); trên 34 ô là 0,51% `[TB theo ô]` (FA:12; D03:267-268) và 10/2.338 = 0,43% `[gộp theo khách]` (A:7). |
| F05 | Mức giảm ΔY = −5,84 điểm %, khoảng bootstrap 95% [−8,78; −3,23], cluster-t (df = 5) [−10,54; −1,15]; so với đệm cùng giá, chênh −1,77 điểm % nhưng cluster-t [−3,62; +0,07] chạm 0. | — | FA:32-42; FR:51-65 | VERIFIED-by-me | A3 mang nhãn "mong manh với suy luận ít cụm" (8 ngày-khung, 3 buổi sáng). |
| F06 | Giá của dự báo là lời hứa trả dài thêm trung bình 13,7 s trên 21 ô (khung 7h 27,8 s) và lời hứa đón dài thêm 3,2 s; trên cả 34 ô, C-30 dài thêm trung bình 7,37 s mỗi khách. | 13,7 s `[TB theo ô]`; 7,37 s `[gộp theo khách]` | FR:67-69; FA:8-9; A:7; CHK:176 | VERIFIED-by-me | — |
| F07 | Có 34/1.471 khách (2,3%; 26 ở khung 7h) có lời hứa đón hiển thị muộn hơn hạn đón muộn nhất, vì phép kiểm khả thi vẫn dùng giờ không dự báo. | 34/1.471 | FR:70; RX:2; FA:29 | VERIFIED-by-me | Phải xử lý trước khi triển khai. |
| F08 | Lợi ích của dự báo không riêng của luật C: M⁺-30 và V-30 cũng đạt 0,17% trên 21 ô, U giảm từ 9,72% xuống 3,90%, và khung 17h của U vẫn 6,76%. | `[TB theo ô]` | FR:65,79-86; FA:3,6,13,23; R15 row 50 | VERIFIED-by-me | — |
| F09 | Sổ chia trễ ba phần trên 21 ô ngày thường (C-30, khách trễ quá 60 s so với lời hứa ngây thơ, tổng 6.217 s): do điều phối 82 s (1,3%), lường trước được 5.353 s (86,1%), không lường trước được 783 s (12,6%). | 6.217,4 = 81,7 + 5.352,6 + 783,0 s | FR:72-75; FA:30; RX:3 | VERIFIED-by-me | Phần "lường trước được" phụ thuộc dự báo đang dùng; phần dư không tự động là "được miễn" (HO:388-389). |
| F10 | Khi kéo dãn lời hứa theo hệ số giao thông thật, giờ trả khớp trong 2 s với mọi khách có phần điều phối bằng 0: 1.452/1.452 trên 21 ô và 2.305/2.305 trên 34 ô. | 1.452; 2.305 | FR:77; RX:8; FA:28 | VERIFIED-by-me | Cho thấy thế giới gần như tất định vì hệ số chung toàn thành phố (FR:167-169). |
| F11 | Khi bỏ 12/11 khỏi ngày nguồn, tiêu chí A1 trượt vì chỉ còn 2 buổi sáng có dự báo; hiển thị hai phía làm tăng dao động buổi chiều. | cluster-t df = 2 [−18,9; +6,4] | FR:88-100 | VERIFIED-by-me | — |
| F12 | Đưa dự báo vào bộ điều phối (Họ B, lớp bọc v1.3, 16 ô) làm 3/32 lần chạy dừng vì PLAN_INFEASIBLE và M⁺-30F vẫn bị ép ở 47,6% quyết định, nên quy tắc triển khai chọn lớp lời hứa. | 3/32; 47,6% `[TB theo ô]` | FR:117-146; RX:9-15 | VERIFIED-by-me | Chỉ đúng cho lớp bọc v1.3 (HO:390). |
| F13 | Trên buổi chiều tuyết (8 ô, 601 khách), dự báo lịch sử chỉ giảm số khách trễ quá 60 s từ 41 xuống 34, và trong 3.445,9 s trễ của 41 khách đó phần do điều phối chỉ là 8,6 s. | 7,19% → 5,94% `[TB theo ô]`; 41/601 = 6,82% → 34/601 = 5,66% `[gộp theo khách]`; trễ > 120 s 0,69% `[TB theo ô]` | SNOW:10; RP1:6-8,24; NEW:5; CHK:195 | VERIFIED-by-me | Một sự kiện, đã xem trước. 92,5% "không lường trước được" là theo dự báo đang dùng (SNOW:10). |
| F14 | Phát lại hồi cứu trên buổi chiều tuyết: BLEND chỉ dùng snapshot trong khung cho 21 khách trễ, BLEND có prefix sáng (trùng cổng 1,3) cho 19, BLEND trễ một bin cho 29, đệm cùng giá cho 27, so với 34 của dự báo lịch sử. | 34 / 21 / 19 / 29 / 27; ORACLE 0 | RP1:1-23; NEW:5; R18 B58,62,89 | VERIFIED-by-me (số đếm); thống kê cổng 1,244/1,323 VERIFIED-by-Codex R18 (tôi không mở FS2) | 19 dùng prefix 06h mà khung 14/15h không được giao và ngưỡng chọn sau khi xem; 29 vẫn neo snapshot hiện tại chính xác. Chưa niêm phong. |
| F15 | Mô hình prefix giải thích thêm 886,9 s ngoài dự báo lịch sử (25,74% tổng giây trễ), còn 2.299,0 s (66,72%) chưa giải thích được bằng các cách đã thử. | 886,858 / 3.445,933; 2.299,012 / 3.445,933 | NEW:5; RP1:24-35; CHK:195 | VERIFIED-by-me | Phần dư phụ thuộc phương pháp; không phải giới hạn "biết trước được". |
| F16 | Giao thức xu hướng tắt dần vòng 12, khi khớp trên dữ liệu, cho α = 1, β = 0, φ = 0,8 và trùng với dự báo lịch sử hiện tại. | (1,0; 0,0; 0,8); 80 mục tiêu | RP1:2; SF:27; NEW:5 | VERIFIED-by-me | Rút khỏi danh sách phép thử hứa hẹn; không suy ra mọi mô hình xu hướng đều vô ích. |
| F17 | Trên 21 ô ngày thường chỉ còn 2/1.471 khách trễ quá 60 s sau dự báo (so với 68 không dự báo), nên dư địa cải thiện của chỉ tiêu này trên mẫu này rất nhỏ. | 2 vs 68 | RP1:38-40; R14:62 | VERIFIED-by-me | Không giới hạn mọi chỉ tiêu, ngưỡng hay ngày mới (R15 corr. 7). |
| F18 | Kiểm ngoài mẫu theo thời gian (kế hoạch niêm phong 6175d2c1…) trên 15–16/11: C-30 có dự báo có 1.031/1.032 khách kịp 60 s, còn U có dự báo và đệm theo khoảng trống E = 60 s có 1.031/1.061 khách kịp, với lời hứa dài thêm khoảng 60 s và 67–84% tới sát giờ báo (±60 s). | C-30: 376/376 + 655/656; U room E60: 377/382 + 654/679 | BACK:1,18,43; HO:312-320 | VERIFIED-by-me | Đệm "room" bị loại vì dự đoán P1 sai (HO:314); quy tắc horizon E60 (BACK:16) cũng cho 1.031/1.061. |
| F19 | Dự báo cho ngày có sự kiện là hướng tương lai, ước tính 80–140 giờ công, cần thiết kế chống rò rỉ thông tin và nhiều sự kiện độc lập. | 80–140 h | V17:450-452; R18 §3 lines 255-261 | UNVERIFIED (ước tính ý kiến) | Mọi thành phần đã có tiền lệ (V17 A3). |

## G. Phép thử học máy (kết quả âm)

| ID | Câu | Số | Anchor | Trạng thái | Lưu ý |
|---|---|---|---|---|---|
| G01 | Phép thử học máy được niêm phong trước (SHA 93f6b968…, 2026-10-08 22:46:17) với ba mô hình cố định: HGB phân vị 0,9, HGB bỏ biến trạng thái xe, và hồi quy tuyến tính phân vị, so ở cùng độ dài lời hứa E = 15/30/60 s (E = 30 là chính). | — | MLS:1-116; `CW/ML-PILOT-SEALED.sha256` | VERIFIED-by-me | Phát lại không chạy mô phỏng; các ngày đã xem trước (MLS:9-10). |
| G02 | Một mô hình chỉ thắng đối chứng khi có tỉ lệ trễ thấp hơn mà lời hứa trung bình không dài hơn quá 1 s, p90 không dài hơn quá 15 s, và tỉ lệ tới sớm không tăng quá 1 điểm %. | 4 điều kiện | MLS:91-95 | VERIFIED-by-me | — |
| G03 | Chia dữ liệu: giao thông đo (U, C-30, khung 7h) học trên 12–13/11, hiệu chỉnh 14/11, kiểm 15/11 và 16/11; giao thông cố định WP14r học 12/11 r1–r3, hiệu chỉnh 12/11 r4, kiểm 13/11. | — | MLS:41-61 | VERIFIED-by-me | — |
| G04 | Lần chạy đầu bỏ sót bước loại 11 chuyến gốc trùng giữa phần học và phần hiệu chỉnh ở 5 nhánh tĩnh; phụ lục A1 loại 55 dòng hiệu chỉnh và chạy lại đúng script, mọi kết luận giữ nguyên. | 11 chuyến × 5 nhánh = 55 | MLA:3-23; PROV:2-8; CHK:210 | VERIFIED-by-me | A1 viết sau khi có kết quả; lần chạy đầu không phải kết quả niêm phong hợp lệ. Phần kiểm không trùng. |
| G05 | ML1 đúng: với C-30 có dự báo, HGB không giảm thêm tỉ lệ trễ (+0,00 điểm % ở cả 15/11 và 16/11). | +0,00 / +0,00 pp | ML:45-47 | VERIFIED-by-me | — |
| G06 | ML2 sai: với U, HGB chỉ hơn dự báo cộng đệm đều +0,69 điểm % (15/11) và +0,00 (16/11), và không qua điều kiện chặn. | +0,69 / +0,00 pp | ML:48-52 | VERIFIED-by-me | — |
| G07 | ML3 sai: với FREE tĩnh, HGB giảm trễ từ 12,89% xuống 11,65% nhưng làm 7,1% khách tới sớm quá 60 s. | 12,89 → 11,65%; early 7,1% | ML:21,53; CHK:212 | VERIFIED-by-me | HO:336 ghi 6,9% là số của lần chạy trước phụ lục (ML0:21; CHK:211). |
| G08 | ML4 đúng: không mô hình nào, ở FREE, LOCKS hay U, đồng thời đạt tỉ lệ trễ và độ chính xác hai phía của C-30 có dự báo trong cùng thế giới. | 0 trường hợp | ML:54-66 | VERIFIED-by-me | — |
| G09 | ML5 sai: thêm biến trạng thái xe không cải thiện gì (G_full = G_nostate). | — | ML:67-70 | VERIFIED-by-me | — |
| G10 | Vì ML2 và ML3 cùng sai, tiêu chí dừng đã kích hoạt: không có cải thiện đã chứng minh trong phép thử này. | KILL: YES | ML:71; MLS:107-111 | VERIFIED-by-me | Câu được phép: "mô hình học máy cố định, đặc trưng đơn giản, không cải thiện đáng kể; không mô hình nào đạt độ tin cậy của luật C" (HO:346-347). |
| G11 | Codex tái lập khớp 95 dòng của phép thử. | 95 | HO:341 | UNVERIFIED (tệp vòng 11 của Codex tôi không mở) | — |
| G12 | Các schema dữ liệu công khai đã kiểm không có giờ hứa với khách; có thể học thời gian chuyến đi nhưng chưa có phép chuyển đã kiểm sang mô phỏng này. | — | R15 corr. 7 (lines 299-313) | VERIFIED-by-Codex R15 | Hoãn chương học máy vì công sức và hạn nộp, không vì "không thể". |

## H. Mục tiêu của bộ chọn (sàng lọc trạng thái cố định; diễn đạt thận trọng)

| ID | Câu | Số | Anchor | Trạng thái | Lưu ý |
|---|---|---|---|---|---|
| H01 | U và C dùng cùng chính sách hard-vector, cùng tệp WP4 và cùng bộ chọn ưu tiên ổn định; chúng chỉ khác trần giờ trả. | — | WP4:3; NEW:12; R14:76 | VERIFIED-by-me | — |
| H02 | Vì bộ chọn xếp các tầng ổn định trước chi phí, câu hỏi phản biện mạnh nhất là độ tin cậy của C đến từ trần hay từ bộ chọn vốn đã thận trọng; câu hỏi này chưa có trả lời bằng quỹ đạo. | — | SEL:271-385; A:7,9; V17:197-199 | VERIFIED-by-me (cơ chế); câu hỏi là suy luận | — |
| H03 | Chạy lại bộ chọn trên các trạng thái đã ghi của WP14r tái lập đúng 62.837/62.837 lựa chọn đã ghi. | 12.663 + 12.525 + 12.364 + 12.325 + 12.960 | PV:2-6; NEW:7; WP17:3-22 | VERIFIED-by-me | Dùng lại mã đã kiểm, không phải hai bản hiện thực độc lập (R18 B50). |
| H04 | Khi bỏ các tầng ưu tiên ổn định ở trạng thái đứng yên, lựa chọn đổi ở 445/1.714 quyết định có yêu cầu mới (25,96%) dưới các cổng của LOCKS, 325/1.715 (18,95%) dưới C-120, 173/1.716 (10,08%) dưới C-60 và 104/1.715 (6,06%) dưới C-30; số yêu cầu được nhận không đổi ở mọi quyết định. | 25,96 / 18,95 / 10,08 / 6,06% | NEW:6; WP17:7,11,16,21; CHK:201 | VERIFIED-by-me | Hai tập trạng thái khác nhau; không phải hiệu ứng nhân quả "4×" của việc thêm trần (R18 §2). |
| H05 | Ở các quyết định đổi lựa chọn, chi phí kế hoạch giảm trung bình 7,79% (LOCKS) và 8,00% (C-30); tính trung bình trên mọi quyết định có yêu cầu mới thì 2,02% và 0,49%; lấy tổng giảm chia tổng chi phí kế hoạch đã chọn trên mọi quyết định được xác nhận thì 0,3069% và 0,0794%. | ba ước lượng khác nhau | NEW:6; PV:2,5 | VERIFIED-by-me | Chi phí kế hoạch = thời lượng tuyến dự kiến còn lại, tính lặp (A16); không phải tiền xăng hay lợi nhuận. |
| H06 | Ở các quyết định đổi lựa chọn, tổng dời giờ trả cộng trên đội xe có trung vị 90,8 s dưới LOCKS và 12,5 s dưới C-30; dưới C-30, trường hợp lớn nhất là 35,5 s chia cho hai khách, mỗi khách 17,77 s, nên không khách nào vượt 30 s. | 90,819 / 12,494 s; max 390,8 (LOCKS) / 35,54 s | WP17:8,22; PV:2,5,7; CASE:1-18; NEW:8 | VERIFIED-by-me | "≤ 35,5 s" là tổng trên 2 khách, không phải mỗi khách. |
| H07 | Trong các quyết định "đổi", 12/445 (LOCKS) và 9/104 (C-30) không rẻ hơn hẳn, tức chỉ là phá hòa. | 445 − 433; 104 − 95 | WP17:7,21; CHK:201 | VERIFIED-by-me | — |
| H08 | Với FREE, 325 trong 401 quyết định đổi lời hứa (81,0%) chỉ đổi giờ trả theo cách mà cổng của LOCKS vẫn cho phép, mang 33.555 s trên 48.509 s dời giờ trả (69,17%); 76 quyết định còn lại đổi giờ đón trước khi lên xe (cận trên). | 325/401; 33.555,4 / 48.508,9 s | PV:8; CHK:200 | VERIFIED-by-me | Phân rã cục bộ, không phải phân rã khoảng cách kết quả FREE–LOCKS (CX17:67 qua V17 R4). |
| H09 | Phương án ưu tiên chi phí dời ít nhất một khách đang có ở 426/445 quyết định đổi (LOCKS) và 81/104 (C-30). | 426/445; 81/104 | DER17:15,18 | VERIFIED-by-me | — |
| H10 | Sàng lọc này không cho biết kết quả quỹ đạo (phục vụ, trễ, đi chung), chi phí thực, hay mức chuyển sang T3.8, vì WP14r dùng giao thông cố định, runner cũ, không có luật phục hồi và policyVersion khác. | — | NEW:13; V17 R4 "Does not show"; R18 B55 | VERIFIED-by-me | — |
| H11 | Nhà cung cấp chính sách "fixed-freeze" bỏ mọi trần cứng và khóa xác nhận, nên không phải lối tắt cho "trần + ưu tiên chi phí". | `hardLimit: null`; `PromiseLock.None` | CCA:97-108; CHK:118-119; R15 rows 41-42 | VERIFIED-by-me | — |
| H12 | Thí nghiệm 2×2 {ưu tiên ổn định, ưu tiên chi phí} × {U, C-30} mới là đề xuất: chưa cài đặt, chưa được duyệt chạy; Giai đoạn 1 gồm 108 job và Giai đoạn 2 có điều kiện 72 job. | 34 + 4 + 2 + 68 = 108; 68 + 2 + 2 = 72 | V17 A2; R18 §3; NEW:18 | VERIFIED-by-me (đây là kế hoạch, không phải kết quả) | Ngưỡng dự đoán là lựa chọn thiết kế trên panel đã xem; xem mục L. |
| H13 | Thời gian chạy lịch sử trên WP14r có trung vị 730 s (FREE), 667 s (LOCKS) và 641 s (C-30) mỗi job. | n = 16 mỗi nhánh | EL17:2-6 | VERIFIED-by-me | Thời gian của nhánh ưu tiên chi phí trên T3.8 chưa đo. |

## I. Giới hạn

| ID | Câu | Số | Anchor | Trạng thái | Lưu ý |
|---|---|---|---|---|---|
| I01 | Mọi kết quả đến từ một mô phỏng (FleetPy) với runner RideBound; theo thang claim của dự án, không được nhảy từ tầng kiểm cơ học lên tầng hiệu lực ngoài đời. | 6 tầng | D03:140-151 | VERIFIED-by-me | — |
| I02 | Tắc đường là một hệ số chung toàn thành phố nên thế giới gần như tất định; kết quả dự báo là mức trần cho loại dự báo theo giờ trong ngày, không phải hiệu quả ngoài đời. | — | FR:165-169; F10; RUN38:8-9 | VERIFIED-by-me | — |
| I03 | Tốc độ nền lấy lúc 00:00 cho mọi ô (B07), thời gian dừng bằng 0 (B05), và các chuyến được chọn ngắn hơn tập đủ điều kiện (B13). | xem B05, B07, B13 | FAC; SERV; SEL6; HO:371-377 | VERIFIED-by-me | — |
| I04 | Mỗi ô chỉ có 108 yêu cầu, 8 xe, 96 nút, với giới hạn công cụ 128 yêu cầu / 32 xe / 96 nút, và tải thấp hơn nhiều so với bài FleetPy (B03, B04, B12). | — | FIX; NORM:322-328; LOAD:2 | VERIFIED-by-me | — |
| I05 | Chỉ có 5 ngày và các ô phụ thuộc nhau, mỗi ô một episode, nên 34 ô không phải 34 mẫu độc lập và không cấp bảo đảm quần thể. | 5 ngày | T38:88-95; D03:222-226; R18 §3 (line 251) | VERIFIED-by-me | — |
| I06 | Các kết quả T3.8, w07, w07x và dự báo đều là thăm dò: ngưỡng, biên, cách chia được chọn sau khi đã xem dữ liệu phát triển. | — | T38:8,88-89; W07X:5; FR:38,163 | VERIFIED-by-me | — |
| I07 | Mô phỏng không có mô hình phản ứng của khách (không hủy chuyến, không từ chối lời mời). | — | FR:115,174; SWEEP:20 | VERIFIED-by-me | — |
| I08 | Witness ngân sách được ghi theo kiểu dừng ở lỗi đầu, nên một witness có thể che một lỗi khác. | — | VALID:222-239; R15 row 30 | VERIFIED-by-me | — |
| I09 | Chi phí kế hoạch của bộ chọn không phải chi phí vận hành thực. | — | A16 | VERIFIED-by-me | — |
| I10 | Giá trị thực tiễn tăng thêm của luật C chưa được xác nhận; muốn nâng claim cần một nhà vận hành thật có vấn đề, chi phí và ngưỡng chấp nhận cụ thể. | — | D03:236-245; CHK:79-80 | VERIFIED-by-me | — |
| I11 | Bằng chứng sự kiện chỉ có một buổi chiều tuyết đã xem, và giai đoạn kiểm tương lai chỉ có 5 đợt tuyết (B26). | 1 sự kiện | SNOW; NEW:9 | VERIFIED-by-me | — |
| I12 | Kết quả WP14r là giao thông cố định với runner đời cũ, không chuyển sang T3.8 (B17). | — | NEW:13 | VERIFIED-by-me | — |
| I13 | Một binary build lại có thể khác binary lưu trữ, nên mọi lần chạy mới phải qua Gate 0. | core 1ce15e9 vs 45f8026 | R15 rows 38-40; R18 B24 | VERIFIED-by-Codex R15 | — |
| I14 | Phép quy đổi trễ (giữ nguyên quyết định) cho U 8,75 / 4,64 / 1,15 / 0,16% trễ quá 1 / 2 / 5 / 10 phút và C-30 3,46 / 0,64 / 0 / 0%. | `[gộp theo khách]` | BURD:8,14 | VERIFIED-by-me | Chỉ là quy đổi mô tả. |
| I15 | Bản LaTeX hiện tại (tệp đã kiểm có mtime 30/9) chưa có số nào của T3.8 và chưa trích Hörl & Zwick 2022 (27 mục tài liệu). | 27 bibitem; 11 tệp TEX | NEW:14-15; META:4-6; R18 B1-B3 | VERIFIED-by-Codex R18 | Tôi không mở TEX. mtime không chứng minh lần build cuối. |
| I16 | Hạn nộp giữa tháng 11/2026 chưa được xác nhận. | — | HO:494 | UNVERIFIED | — |
| I17 | Vế cộng dồn chưa từng là lý do từ chối được ghi trên giao thông đo, nên luận văn không có bằng chứng thực nghiệm về giá trị tăng thêm của nó (E01, E09). | — | A:7,10-17 | VERIFIED-by-me | — |

## J. Văn liệu và công trình trước

| ID | Câu | Số | Anchor | Trạng thái | Lưu ý |
|---|---|---|---|---|---|
| J01 | Hörl và Zwick (2022, chiến lược B) tính lại giờ trả kỳ vọng bằng cách duyệt tuyến đang gán theo giờ đi hiện tại, dùng nó thay cho giờ trả muộn nhất với khách đang trên xe sắp vi phạm, và cho phép thêm điểm đón miễn là khách trên xe không bị trả muộn hơn "the absolute minimum, given current traffic conditions". | — | HZ:529-543 (PDF p7-8); CHK:3-8 | VERIFIED-by-me | Đây là tiền lệ quyết định cho mốc cập nhật theo giao thông (V17 R6). |
| J02 | Động cơ của Hörl và Zwick là tránh "undefined system states" khi không còn chuỗi trả khả thi cho khách trên xe. | — | HZ:481-497,507; CHK:2 | VERIFIED-by-me | — |
| J03 | Phương trình 7 của Hörl và Zwick đặt giờ trả bắt buộc = max(giờ cập nhật, giờ muộn nhất) cho các yêu cầu trên xe đang xét; tuyến phải thỏa ràng buộc cứng trên giờ bắt buộc (9–10) và chịu phạt khi vi phạm giờ gốc (11). | eq. 5–11 | HZ:562-606; CHK:9-12 | VERIFIED-by-me | "Cổng cứng thay vì phạt" không phải điểm khác biệt (R18 B75). |
| J04 | Hörl và Zwick mô phỏng dịch vụ đi chung với nhu cầu thật của MOIA ở Hamburg trong MATSim, dùng thuật toán Alonso-Mora, và chỉ ra đánh đổi giữa vi phạm ràng buộc khách và từ chối muộn. | — | HZ:21,23,69-71,630-632 | VERIFIED-by-me | — |
| J05 | Khác biệt trung thực với Hörl–Zwick B: phần nới của họ phụ thuộc giao thông và chỉ cho khách sắp vi phạm, không cộng dồn và không có sổ; luật C cho mọi khách cùng một ngân sách điều phối B cả chuyến, độc lập với giao thông, tính trị tuyệt đối hai chiều và có sổ theo từng khách. | — | HZ:535-543,567-569; HO:145-147; V17 A1.3, R6; R18 B74 | VERIFIED-by-Codex R18 (suy luận từ hai định nghĩa); văn bản HZ VERIFIED-by-me | Thay p0 + B vào HZ là biến thể suy luận, không phải định nghĩa của bài. Vế cộng dồn chưa từng là lý do từ chối trên giao thông đo (E01). |
| J06 | Fielbaum và Alonso-Mora (2020) đo cách thời gian dự báo của từng yêu cầu thay đổi từ lần gán đầu đến lúc trả, tập trung vào bất ổn do nhà điều hành gây ra và chỉ tính phần thay đổi bất lợi. | — | FAM:93-94,191-195,218,295-296; CHK:13-16 | VERIFIED-by-me | TR Part C 121 (2020) 102831. |
| J07 | Họ dùng mạng Manhattan 4.091 nút / 9.453 cạnh, khung 13–15h ngày 15/01/2013 và mười ngày thứ Hai–thứ Năm từ 14/01/2013, chọn giờ thấp điểm vì "traveling times are somewhat stable, which allows us to disregard unreliability due to traffic conditions", với 2.000 xe 4 chỗ và 19.610 yêu cầu. | 4.091 / 9.453; 2.000; 19.610 | FAM:571-584; CHK:17-24 | VERIFIED-by-me | Bộ này cố ý loại giao thông nên không dùng được cho dự báo sự kiện. |
| J08 | Mục 6 của họ đã kiểm soát bất ổn trước quyết định: kịch bản kiểm soát hoàn toàn đánh dấu khách đã gán là không bị từ chối và cập nhật thời gian chờ tối đa về giá trị dự báo; tỉ lệ từ chối tăng từ 34,5% lên 45,6% và chi phí khách tăng từ 9,56 lên 11,6. | Base 1,01 / 0,65 / 1,66 / 34,5% / 9,56; trung gian 31,2% / 10,3; hoàn toàn 45,6% / 11,6 | FAM:950-986; FAM:942 (dòng Base); CHK:25-28,31; R14 E1 (PDF p17) | VERIFIED-by-Codex R14 (E1: hàng trung gian và hoàn toàn đọc trên PDF p17, vì bản txt dán nhãn sai); văn bản §6 và dòng Base: VERIFIED-by-me | Kiểm soát giờ đón, không phải sổ cộng dồn giờ trả (R14 E1). |
| J09 | Họ nêu bài toán mở là "how to control it, i.e., ... provide more accurate times without increasing the rejection rate". | — | FAM:1038-1040; CHK:29-30 | VERIFIED-by-me | Không dùng để nói "kiểm soát là mới" (D03:54-56). |
| J10 | Schulz và Pfeiffer (2026) đặt hạn chót trả l_i = B_i + l ngay sau khi khách nhận lời mời, công bố cả giờ trả dự kiến lẫn giờ trả muộn nhất, dùng thời gian đi cố định, mặc định l = 900 s, quét l từ 0 đến 30 phút và kết luận 10–15 phút là đánh đổi hợp lý. | l = 900 s; hệ số chấp nhận 0,5 | SP:466-490,568-577,638-642,1196-1206,1468-1471,1493-1496; CHK:32-42 | VERIFIED-by-me | OR Spectrum 48:541–586. |
| J11 | M⁺ trong khóa luận chỉ mượn thành phần hạn chót của Schulz và Pfeiffer ở mức 30–60 s, chặt hơn nhiều so với 900 s, và không tái lập toàn bộ thuật toán của họ. | 30/60 s vs 900 s | D03:214-217; POLICY:243-248; SWEEP:19-24 | VERIFIED-by-me | — |
| J12 | Elmi và cộng sự (2026) đã có độ chùng thông thường và cơ chế bảo đảm cho khách được chọn, nên bảo vệ từng khách hay bảo đảm ETA riêng lẻ không phải điểm mới. | — | D03:211-213 | UNVERIFIED (chỉ theo văn bản ranh giới của chủ nghiên cứu; bài gốc chưa mở) | — |
| J13 | Haferkamp (2024) biến giờ đón đã chọn thành ràng buộc có độ lệch nhỏ cho phép. | — | D03:218-220 | UNVERIFIED (bài gốc chưa mở) | — |
| J14 | Ackermann và Rieck (2025) đã có chèn động, nhiều kế hoạch, cam kết tối thiểu và đồng thuận theo thời gian, nhưng không có sổ ngân sách nhiều chiều theo từng khách. | — | D03:13-35 | UNVERIFIED (bài gốc chưa mở) | — |
| J15 | Tellez và cộng sự (2022) tối ưu tính nhất quán giờ phục vụ qua nhiều ngày, không phải lịch sử sửa lời hứa trong một chuyến. | — | D03:37-48 | UNVERIFIED (bài gốc chưa mở) | — |
| J16 | Bài "anticipatory walking" (2026) đã dùng lịch tham chiếu và cơ chế no-worse cho một lần cập nhật, nên luật phục hồi "không tệ hơn" không phải điểm mới. | — | D03:58-67 | UNVERIFIED (bài gốc chưa mở) | — |
| J17 | Alonso-Mora và cộng sự (2017, PNAS) đề xuất gán xe–chuyến động cho đi chung sức chứa lớn; FleetPy hiện thực thuật toán này (AM). | — | AM17 trang 1 (CHK:213); FLEET:430-433; D03:89 | VERIFIED-by-me (nhận dạng bài và việc FleetPy dùng AM) | Nội dung thuật toán chưa được tôi đọc chi tiết. |
| J18 | FleetPy (Engelhardt và cộng sự, ETRR 2026) cung cấp dữ liệu chuẩn Manhattan: mạng OSM 4.410 nút / 9.574 cạnh, dữ liệu taxi tuần 11–18/11/2018 còn 1.807.255 chuyến, hệ số giờ đi hiệu chỉnh theo từng giờ; nghiên cứu điển hình dùng mẫu 10% (21.400 yêu cầu) ngày 12/11/2018, dừng 30 s mỗi khách, 180 xe 4 chỗ và số khách trung bình trên xe ≈ 1,33. | xem câu | FLEET:1-12,340-372,421-449,474-478; CHK:43-56 | VERIFIED-by-me | Bản trích hai cột; tham số nằm ở PDF trang 11. |
| J19 | Syed và cộng sự (2021, Front. Future Transp., doi 10.3389/ffutr.2021.681451) thuộc nhóm FleetPy; V17/R18 gọi mục tiêu hệ số tương lai là "kiểu Syed". | — | SYED (đầu tệp); V17:443 | VERIFIED-by-me (nhận dạng bài và cách V17 gọi tên) | Việc bài này định nghĩa công thức hệ số giờ đi là UNVERIFIED; kiểm kỹ trước khi trích công thức. |
| J20 | Gardner và McKenzie (1985) đề xuất làm trơn hàm mũ với xu hướng tắt dần. | Management Science 31(10):1237–1246 | GM:1-11,70; CHK:60-61 | VERIFIED-by-me | — |
| J21 | Leonardi và cộng sự (2024) cho rằng mức dự đoán được của dịch vụ đáp ứng theo nhu cầu có thể là một tham số thiết kế. | — | LEO:1-8,1101; CHK:57 | VERIFIED-by-me | — |
| J22 | Lu và Kühnel (2024, MOIA) mô tả biên giờ đón so với giờ đón đã hẹn, với biên nhỏ "2 or 3 minutes" trong thực tế. | 2–3 phút | LUK:1-8,47; CHK:58-59 | VERIFIED-by-me | Là biên giờ đón, có tính tắc đường. |
| J23 | Phân tích tổng hợp của Wardman và cộng sự (2026) cho hệ số thời gian trễ trung bình 2,53 (15 quan sát, 2 nghiên cứu) và 3,12 (66 quan sát, 27 nghiên cứu). | 2,53; 3,12 | WAR:614-617; CHK:62-63 | VERIFIED-by-me | Hai cấu trúc khác nhau; không phải giá của ngân sách C (R15 row 64). |
| J24 | Alonso-González và cộng sự (2020, N = 1.006, khảo sát lựa chọn ở Hà Lan) thấy tỉ số độ tin cậy khoảng 0,5 cho dịch vụ đi chung, và trễ nhỏ không báo trước được định giá thấp hơn thời gian đã báo; họ không đặt người trả lời vào tình huống đến muộn. | N = 1.006; RR ≈ 0,5 | AGZ:25,30,642,872; CHK:64-67 | VERIFIED-by-me | Khác cấu trúc với J23; không đổi thành "trễ chỉ đáng một nửa" (R15 corr. 6). |
| J25 | Molenbruch và cộng sự (2015) khảo sát 78 tổ hợp mức dịch vụ, với giới hạn thời gian ngồi xe biểu diễn bằng tỉ lệ của thời gian đi thẳng. | 78 | MOL:52,148-150; CHK:68-69 | VERIFIED-by-me | Tiền lệ cho giới hạn theo tỉ lệ (D18). |
| J26 | Các nghiên cứu về tính nhất quán trong định tuyến (Kovacs và cộng sự 2014) và đóng băng lịch sản xuất (Sridharan và cộng sự 1987) cho thấy đánh đổi ổn định–hiệu quả đã được nghiên cứu từ lâu. | — | SUR13X:18-19; PAP13 §10-11 | VERIFIED-by-Codex R13 (nội dung); nhận dạng tệp VERIFIED-by-me | — |
| J27 | Cohen, Fiszer và Kim (2022) chạy thí nghiệm thực địa với Via về khuyến mãi khi khách bực bội, và thấy cách này hiệu quả với chờ lâu nhưng không với đi lâu. | — | COHEN trang 1 (CHK:214); SUR13X:35; D03:262-265 | VERIFIED-by-Codex R13 (trích dẫn; tôi không mở lại phần thân bài); nhận dạng PDF: VERIFIED-by-me | Sai số ETA của Via là giờ đón, không phải giờ trả (D03:263). |
| J28 | Trang UberX Share ghi "we cannot guarantee arrival times" và thời gian đi thêm trung bình 8 phút. | 8 phút | R15 row 68; R14 E10 | VERIFIED-by-Codex R15 | Nguồn web. |
| J29 | "Delayed Ride Guarantee" của Uber là khoản điều chỉnh trả cho tài xế và loại trừ chuyến đi chung. | ≥ 5 phút | R14 E10; HO:394 | VERIFIED-by-Codex R14 (web; không mở lại) | Không phải bồi thường cho khách. |
| J30 | Lyft cho tín dụng 15 USD khi tài xế trễ quá 10 phút với một số chuyến đặt trước đi sân bay, và 50 USD khi không ghép được tài xế. | 15 / 50 USD; 10 phút | R15 row 70; R14 E7 | VERIFIED-by-Codex R15 | Là bảo đảm giờ đón, không phải giờ trả. |
| J31 | MOIA Express quảng cáo "shorter arrival window" như một nâng cấp tùy chọn. | — | R15 row 69; R14 E11 | VERIFIED-by-Codex R15 | — |
| J32 | Mt-KaRRi giới hạn thời gian chuyến α·T_đã-nhận + β (α = 1,4, β = 10 phút), neo vào thời gian khách đã chấp nhận, không cấp lại ngân sách mỗi lần sửa. | α 1,4; β 10 phút | R15 rows 72,75; R14 E13 | VERIFIED-by-Codex R15 | — |
| J33 | Yu, Zhang và Zhou (2022) thấy thay đổi 1 phút của thông tin chờ ban đầu không đổi tỉ lệ bỏ đi vì hai hiệu ứng triệt tiêu nhau, trên 1.425.745 chuyến. | 1.425.745 | R15 row 73; R14 E6 | VERIFIED-by-Codex R15 | Chờ trước khi ghép, không phải giờ trả. |
| J34 | Bằng sáng chế Lyft US12182741B2 mô tả chế độ "dự đoán được" với ràng buộc so với ETA báo ban đầu. | 5 / 7 phút; 0,25 | R15 row 71; R14 E12 | VERIFIED-by-Codex R15 | Không phải phân tích pháp lý. |
| J35 | Hứa theo dự báo và dự báo phân vị giờ đến đã là thực hành phổ biến (Uber DeepETA, DoorDash). | — | SUR13X:39-41,70; HO:141-142; FR:177 | VERIFIED-by-Codex R13 (web; không mở lại) | Không nhận dự báo lời hứa là mới. |
| J36 | Quy định 49 CFR 37.131 tách trễ "lường trước được lúc xếp lịch" khỏi "không lường trước được" (dùng làm tương tự). | — | FR:105; HO:395 | UNVERIFIED (tôi không mở eCFR) | Chỉ là tương tự, không phải căn cứ pháp lý. |
| J37 | Nghiên cứu OneBusAway (Watkins và cộng sự) thấy thông tin thời gian thực giảm thời gian chờ cảm nhận 0,7 phút. | 0,7 phút | SUR13X:45 | VERIFIED-by-Codex R13 (web; không mở lại) | Câu "trung vị chịu sai 4–6 phút" (HO:256): UNVERIFIED. |
| J38 | Chèn động, gán lại, cập nhật ETA, ngưỡng trễ, tương đồng tuyến, cam kết tối thiểu, nhất quán thời gian, hài lòng khách, phát hiện bất ổn, kiểm soát trước quyết định và đánh đổi dịch vụ–ổn định đều đã có tiền lệ. | — | D03:5-9,54-56,83,153-164; `E:/Code/RideBound/AGENTS.md` | VERIFIED-by-me | — |
| J39 | Phạm vi đóng góp được bảo vệ chỉ là tổ hợp đã hiện thực và kiểm: theo từng khách + phụ thuộc đường đi + nhiều chiều + ngân sách cộng dồn/đổi + chèn cuốn chiếu nhiều epoch + chứng nhận kiểm bằng máy; tổ hợp này không tự chứng minh quyền ưu tiên trên toàn văn liệu. | — | D03:5-9; CHK:74 | VERIFIED-by-me | — |
| J40 | Gschwind và Drexl (2019) có phép kiểm khả thi chèn thời gian hằng, nhưng không được nhập vào RideBound. | 3,8× (không dùng làm claim) | D03:95 | VERIFIED-by-me (văn bản D03) | — |
| J41 | Ding, Dandl và Bogenberger học kết quả đi chung từ mô phỏng FleetPy. | — | HO:144 | UNVERIFIED (chỉ Codex đọc, trang chặn bot) | Không trích trước khi mở được bài. |
| J42 | Schmidt và cộng sự (2026, arXiv 2609.11950) mô hình hóa rằng một cam kết tham vọng thu hút nhiều cầu hơn một cam kết thận trọng. | — | SUR13X:59; R14 E14 | VERIFIED-by-Codex R14 (web; không mở lại) | Kết quả từ mô hình, không phải phản ứng thật của khách. |

## K. Quy tắc diễn đạt (câu cấm → câu đã sửa)

| ID | Câu bị cấm / nói quá | Câu được dùng | Nguồn quy tắc | Trạng thái | Bằng chứng số |
|---|---|---|---|---|---|
| K01 | "Khác biệt cốt lõi so với văn liệu là độ dời được phân rã theo nguyên nhân." | "Tiếp nối mốc giờ trả cập nhật theo tắc đường của Hörl và Zwick (2022, chiến lược B), khóa luận chỉ tính vào sổ phần dời do quyết định điều phối, cho mọi khách cùng một mức cho phép B không phụ thuộc phần tắc đường, cộng dồn trị tuyệt đối qua cả chuyến và kiểm được theo từng khách." | V17 D2; R18 §2 | VERIFIED-by-me (văn bản quy tắc) | J01-J05 |
| K02 | "Chỉ ràng buộc theo hành vi không bao giờ là nguyên nhân làm rỗng tập phương án" (không phạm vi); "chỗ khác biệt chứng minh được". | "Trong bốn họ được so, chỉ luật C không bao giờ tự loại phương án giữ nguyên kế hoạch; điều này đúng theo cấu tạo. Một hạn chót nới kiểu Hörl và Zwick cũng có tính chất này; trên 34 ô, luật hạn chót có phục hồi 'không tệ hơn' chở đúng bằng luật C." | V17 D3 | VERIFIED-by-me | A22, C01 |
| K03 | "Không ai tách phần do nhà điều hành khỏi phần do đường tắc." | "Ngoài phân loại định tính của Fielbaum và Alonso-Mora, Hörl và Zwick (2022) đã tách phần do tắc đường bằng cách tính lại tuyến cũ theo tốc độ hiện tại; khóa luận dùng một phép chiếu tương tự để tính sổ." | V17 D5 | VERIFIED-by-me | J01, J06 |
| K04 | "Quy trách nguyên nhân" / "causal attribution". | "Quy trách theo mô hình" / "model-based attribution"; "phép chiếu mô hình tại cùng trạng thái". | V17 D10; D03:222-224 | VERIFIED-by-me | A01 |
| K05 | "Trần hành vi, theo cấu tạo, giữ mọi lời hứa của nó"; "về giờ đến thực tế, C và luật hạn chót như nhau". | "C giữ nghĩa vụ của chính nó theo cấu tạo, vì nghĩa vụ ấy không bao gồm phần do tắc đường. Trên 34 ô, C-30 và M⁺-30 cùng chở 2.338 lượt và cùng có 2.328 lượt kịp ngưỡng 60 s khi phát lại dự báo; không phải cùng mọi giờ đến (trễ quá 60 s theo lời hứa ngây thơ: 76 so với 74)." | V17 D11 + R18 §2 | VERIFIED-by-me | C01, C06, C09 |
| K06 | "C phục vụ nhiều hơn" / "C cho nhiều lượt đúng giờ hơn". | "C và luật hạn chót phục vụ cùng số lượt; so với U có dự báo và đệm 30 s, C hòa ở ngưỡng 60 s (2.328 = 2.328) và kém ở ngưỡng 120 s (2.338 so với 2.366), đổi lại lời hứa sát hơn (7,4 s so với 37,2 s) và ít khách tới sớm hơn (0,17% so với 1,81%)." | T38:84; R15 §2; V17 C Câu 1 | VERIFIED-by-me | C10 |
| K07 | "C-30 và M⁺-30 phục vụ cùng những khách." | "Cùng số khách: 2.332 chung, mỗi nhánh 6 khách riêng." | V17 debate table; R18 §2 | VERIFIED-by-me | C04 |
| K08 | "Phần cộng dồn không có tác dụng"; "behaviourally inert"; "never changed a decision"; "tác dụng nhiều nhất 7 quyết định / 1 lượt từ chối"; "luật mỗi bước sẽ nhận đúng các phương án đó". | "Trong 98 lần chạy cưỡng chế C dùng hệ số giao thông toàn thành phố lấy từ dữ liệu đo (64.371 quyết định được xác nhận), cả 1.256 bản ghi chặn do ngân sách giờ trả đều ghi nhận một độ dời tuyệt đối do điều phối vượt B của nhánh tương ứng. Không bản ghi nào cần phần ngân sách đã dùng trước đó để giải thích lỗi được ghi, và không khách đã phục vụ nào dưới C có hơn một lần dời giờ trả khác 0 do điều phối. Chưa cài đặt và chạy nhánh mỗi bước một trần, nên chưa biết bỏ cộng dồn có giữ nguyên quỹ đạo hoặc kết quả không. Bốn quyết định ở giao thông cố định và ba quyết định ở thế giới giả lập là dấu vết được ghi, không phải cận trên cho tác dụng." | R18 §4 Câu 3; R15 corr. 1; V17 R3 | VERIFIED-by-me | E01-E05, E09 |
| K09 | "Cả 1.256 lần chặn đều do một lần dời đã vượt trần 30 giây." (V17:640) | "… vượt B của nhánh tương ứng; bộ này gồm C-30 đến C-300." | R18 §4 Câu 3 | VERIFIED-by-me | E01 (NEW:1 `by_arm`) |
| K10 | "148 khách bị từ chối vì trần" / "bị chặn chỉ vì ngân sách" (V17:620; HO:223). | "148 yêu cầu cuối cùng bị từ chối và có ít nhất một phương án mang dấu vết bị chặn do ngân sách của khách khác." | R18 §4 Câu 2; R15 row 59 | VERIFIED-by-me | D13 |
| K11 | "Muốn cho cả 148 khách qua, trần phải khoảng 555 s; lúc đó gần như không còn trần" như một bảo đảm. | "Khoảng 555 s làm các ngưỡng ngân sách được ghi của mỗi yêu cầu này qua sàng lọc; vì bộ kiểm dừng ở lỗi đầu và quỹ đạo sẽ đổi, điều đó không bảo đảm cả 148 yêu cầu được phục vụ." | R18 §2, §4 Câu 2 | VERIFIED-by-me | D14 |
| K12 | "U là cận trên"; "nới trần lấy lại tối đa 96 khách". | "U là một điểm đối chứng đã đo; trần hữu hạn không nhất thiết nằm giữa (trên w07, C-120 chở 666 > U 665)." | R18 B94; V17 debate table | VERIFIED-by-me | D01 |
| K13 | "Nới trần chỉ tốt hơn khi chấp nhận trễ 2 phút; ở 1 phút cứ thêm một khách thì thêm một khách trễ." (V17:631-632) | "Trên 8 ô sáng, C-30 → C-120 thêm 2 lượt kịp ngưỡng 60 s; trên 16 ô giao thông cố định thêm 6. Có lợi hay không phụ thuộc tiêu chí, giá của lời hứa và điểm đánh đổi." | R18 §4 Câu 2, §5 | VERIFIED-by-me | D03, D10 |
| K14 | "Khoảng 2.380 lượt kịp 120 s ở B = 120 s." | Bỏ hẳn: đây là số học trên các phép sàng lọc không cộng được, không phải ước lượng. | R18 B96 | VERIFIED-by-me | D15 |
| K15 | "Ưu tiên chi phí tiết kiệm 7,8% chi phí kế hoạch" (không điều kiện). | Báo ba ước lượng: 7,79% / 8,00% ở các quyết định đổi; 2,02% / 0,49% trung bình trên quyết định có yêu cầu mới; 0,3069% / 0,0794% tổng giảm chia tổng chi phí; không phải chi phí vận hành thực. | R18 §2, B52 | VERIFIED-by-me | H05 |
| K16 | "Trần hạn chế bộ chọn 4×"; "trần đã tự chặn phần lớn những gì bộ chọn ưu tiên chi phí muốn đổi". | "26,0% so với 6,1% trên hai tập trạng thái khác nhau; kết quả gợi ý rằng dưới các cổng C-30 bộ chọn có ít cơ hội đổi hơn trên những trạng thái đã kiểm." | R18 §2, §4 Câu 4 | VERIFIED-by-me | H04 |
| K17 | "Đẩy giờ trả ≤ 35,5 s mỗi khách." | "≤ 35,5 s cộng trên hai khách, mỗi khách 17,77 s." | R18 B86 | VERIFIED-by-me | H06 |
| K18 | "Chính trần, không phải bộ chọn thận trọng, giữ lời hứa." | Chưa được nói (chưa chạy). Sau thí nghiệm, nếu đạt: "bằng chứng cơ chế trong cấu hình mô hình này"; không nói C tự bảo đảm giờ đến thực. | R18 §4 Câu 4; R15 corr. 2 | VERIFIED-by-me | H12 |
| K19 | "Khoảng 67% số giây trễ không thể biết trước." | "Mô hình prefix đã thử giải thích thêm khoảng 26% số giây trễ; khoảng hai phần ba còn lại chưa giải thích được bằng các cách đã thử." | V17 R5; R18 B60, B88 | VERIFIED-by-me | F15 |
| K20 | "Dự báo nhận ra bất thường giảm 34 → 19 mà không tốn gì ngày thường"; "26% biết trước được từ snapshot đã giao". | "BLEND chỉ dùng snapshot trong khung giảm 34 → 21; con số 19 dùng prefix buổi sáng chưa được giao và một ngưỡng chọn sau khi xem." | V17 debate table; R18 B89 | VERIFIED-by-me | F14 |
| K21 | "Độ trễ một bin: 34 → 29" như kiểm độ trễ thực tế. | "Một phân tích độ nhạy xu hướng trễ một bin, trong đó mốc neo vẫn là snapshot hiện tại chính xác." | V17 debate table; R18 B89 | VERIFIED-by-me | F14 |
| K22 | "Toàn bộ dư địa nằm ở dải 60–120 s." | "Trên một lần phát lại này, trễ quá 120 s theo lời hứa ngây thơ là 0,69% (trung bình theo ô)." | R18 B90 | VERIFIED-by-me | F13 |
| K23 | "Xe công nghệ tăng từ 0 (2013 → 2018)." | "FHV-HV có 691.379 chuyến/ngày ở 11/2018; bảng không có dòng FHV-HV năm 2013." | V17 B91; R18 B69, B91 | VERIFIED-by-me | B24 |
| K24 | "0,17%" không kèm mẫu số. | Luôn ghi: "0,17% là trung bình theo ô của 21 ô có dự báo (gộp theo khách 2/1.471); trên cả 34 ô là 0,51% trung bình theo ô, 0,43% gộp theo khách"; và tách khỏi "4/2.338 = 0,17% khách tới sớm quá 60 s". | D03:267-268; R18 B30; HO:386-387 | VERIFIED-by-me | F04, C10 |
| K25 | "Tuyết: 7,19% → 5,94%" như số gộp. | "Trung bình theo ô 7,19% → 5,94%; gộp theo khách 41/601 = 6,82% → 34/601 = 5,66%." | R18 B59 | VERIFIED-by-me | F13 |
| K26 | "Luật C là cổng cứng còn Hörl–Zwick là phạt" như điểm khác biệt. | Bỏ; dùng khác biệt ở J05 (ngân sách B không phụ thuộc giao thông, cả chuyến, trị tuyệt đối, có sổ). | R18 B75, B92; V17 R6 | VERIFIED-by-me | J03 |
| K27 | "T3.8 thiếu M⁺ có phục hồi (b)." | "M⁺ trên T3.8 đã dùng phục hồi (b); một hạn chót nới kiểu HZ max(p0 + B, e) là cổng khác, để việc tương lai." | R18 B93; V17 R6 | VERIFIED-by-me | A19-A20 |
| K28 | "Một thí nghiệm có tiền đăng ký trên dữ liệu tắc đường thật xác nhận định lý." | "… nhất quán với nó, trong mô phỏng dùng hệ số tắc đường toàn thành phố lấy từ dữ liệu đo (thăm dò)." | V17 D15; R18 B15 | VERIFIED-by-me | B06, B10 |
| K29 | "89,06% độ dời do chính bộ điều phối gây ra." | "Trong phép chiếu mô hình trên panel thời gian đi tĩnh (độ trôi chỉ do trễ thực thi), phần dời gắn với quyết định điều phối chiếm 89,06%." | V17 D9 | VERIFIED-by-Codex R18 (B-rows; tôi không mở TEX nguồn của 89,06%) | — |
| K30 | "Mọi thước đo chuẩn … đều không ghi nhận" việc sửa lời hứa. | "Các hàm mục tiêu điều phối theo thông lượng không định giá việc sửa lời hứa; Fielbaum và Alonso-Mora (2020) đã đo và kiểm soát hiện tượng này." | V17 D1 | VERIFIED-by-me | J06-J08 |
| K31 | "Biến một đại lượng trước nay chỉ đo được sau sự việc thành ràng buộc cưỡng chế được." | "Khóa luận cài đặt và kiểm một dạng kiểm soát trước quyết định, và đo cái giá của nó." | V17 D8; D03:56 | VERIFIED-by-me | J38 |
| K32 | "Về mặt toán học, thước đo hai đầu không thể trở thành ràng buộc." | "Thước đo hai đầu của họ là hậu nghiệm; mục 6 của họ đã ràng buộc trực tiếp lời hứa đón." | V17 D7 | VERIFIED-by-me | J08 |
| K33 | "Trần 30 giây cắt xáo trộn xuống còn 0,17%, giá 7,13 điểm." | Nói rõ đây là gói C1 (khóa + ngân sách + cố định giờ đón) so với B1; đổi tên chỉ số để không trùng 0,17% của dự báo; giữ −7,13 điểm là giá của cả gói. | V17 D12; D03:238 | VERIFIED-by-me | — |
| K34 | "Chênh lệch phản ánh đúng tác động của cam kết." | "… phản ánh tác động của cả gói cam kết, không phải của giới hạn tính toán." | V17 D17; R18 B11 | VERIFIED-by-me | — |
| K35 | Ngưỡng phúc lợi dùng giá 20–25 EUR/h chưa đối chiếu. | Bỏ hai hàng đó, hoặc chuyển sang phụ lục minh họa với tham số ký hiệu q, m. | V17 D16; R18 B10 | VERIFIED-by-me | C29 |
| K36 | "Mức trần tối ưu", "C-120 là tối ưu". | "Một điểm thêm trên đường đánh đổi." | V17 A2 (lines 303-308); R18 §2 a3 | VERIFIED-by-me | D11 |
| K37 | "Lợi ích của dự báo là nhờ luật C." | "Lợi ích không riêng C: M⁺ và V cũng đạt 0,17% trên 21 ô." | FR:65; R15 row 50 | VERIFIED-by-me | F08 |
| K38 | "Giảm C làm khách hài lòng hơn / tăng doanh thu / giảm khiếu nại." | "Giá trị thực tiễn tăng thêm chưa xác nhận; luận văn bảo vệ đặc tả, hiện thực, kiểm nghĩa vụ và đánh đổi có giới hạn." | D03:236-245; FR:115 | VERIFIED-by-me | I10 |
| K39 | "72 khách C-30 trễ thuần vì kẹt xe." | "72 người không có thay đổi giờ trả do điều phối được ghi nhận." | R15 corr. 2 | VERIFIED-by-me | C21 |
| K40 | "Không dữ liệu nào giúp được; học máy là vô ích." | "Có thể học thời gian chuyến đi từ dữ liệu công khai, nhưng các schema đã kiểm không có giờ hứa và chưa có phép chuyển đã kiểm sang mô phỏng này; chưa nên làm chương học máy trước hạn nộp." | R15 corr. 7 | VERIFIED-by-me | G10, G12 |
| K41 | "Hai bên tính lại độc lập và khớp đến từng khách"; "lõi đã vững". | "Các kết quả lưu trữ được dựng lại độc lập và khớp trong phạm vi đã kiểm; phép chạy lại bộ chọn dùng lại mã đã kiểm." | R18 §2 (V:603-604) | VERIFIED-by-me | H03 |
| K42 | "Không thể kiểm cộng dồn ở B = 30 s." | "Dấu vết ghi được thưa ở 30 s và nhiều hơn ở 120 s trên vài đường không trần; 120 s là mức thử được chọn." | R18 §2 (V:205) | VERIFIED-by-me | E06 |
| K43 | "Mỗi thời điểm khách được cấp lại B." | "B là tổng ngân sách cả chuyến; phần còn lại bằng B trừ phần đã dùng." | R18 §2, §4 Câu 3 | VERIFIED-by-me | A06 |
| K44 | "Dữ liệu 2013 chỉ có mã vùng" (cả năm). | "Hai tệp chính thức tháng 1 và 11/2013 đã kiểm có mã vùng, không có tọa độ; các tháng khác chưa kiểm." | R18 §2 (B67) | VERIFIED-by-me | B23 |
| K45 | "LaTeX được build lần cuối ngày 30/9." | "Các tệp đã kiểm có thời điểm sửa 30/9." | R18 B1 | VERIFIED-by-Codex R18 | I15 |
| K46 | "duy nhất", "chỉ … không bao giờ", "khác biệt cốt lõi so với văn liệu", "không ai tách" không có phạm vi. | Chỉ dùng kèm phạm vi rõ ("trong bốn họ đã so", "phép chiếu mô hình"). | V17 A1 K2 | VERIFIED-by-me | — |
| K47 | "first", "novel", "unprecedented", "lần đầu" cho chèn động, giới hạn ETA, gán lại, tương đồng tuyến, cam kết tối thiểu, nhất quán thời gian, hài lòng khách. | Không dùng; xem J38-J39. | `E:/Code/RideBound/AGENTS.md`; D03:153-164 | VERIFIED-by-me | J38 |
| K48 | "Trên mạng đường Manhattan"; "xác nhận". | "Trên bao đóng OD 96 nút lấy từ dữ liệu Manhattan của FleetPy"; "thăm dò". | W07:63; PREF:22-26 | VERIFIED-by-me | B03 |
| K49 | "Trên tắc đường thật" (không giải thích). | "Mô phỏng dùng hệ số giao thông toàn thành phố lấy từ dữ liệu đo", không phải chuyến chạy thật. | R15 corr. 8 (line 325) | VERIFIED-by-me | B06 |
| K50 | "U là ghép tự do / không khóa." | "U không có trần giờ trả nhưng vẫn khóa xe, điểm đón và giờ đón khi xác nhận; FREE không khóa gì." | HO:107-109; R18 B19 | VERIFIED-by-me | A08 |
| K51 | "Hứa dài ra là đủ / đệm luôn kém." | Trình bày cả hai hàng đệm 30 s và 60 s; đệm 30 s hòa C ở ngưỡng 60 s. | R15 §2 | VERIFIED-by-me | C10-C11 |
| K52 | "Ở mức 30 s khách không thấy thay đổi." | "Mức 30 s không phải ngưỡng cảm nhận; trình bày trần như một điểm trên đường đánh đổi." | HO:378-380 | VERIFIED-by-me | A25, D20 |

## L. Kết quả Giai đoạn 1a/1b (chưa có — để trống)

Chưa có job nào được duyệt hay chạy (HO:480; R18 §3). Khi có kết quả, mỗi dòng phải có anchor tới output mới, mã băm
kế hoạch niêm phong, manifest binary/cấu hình, và áp các cách diễn giải đã sửa của R18 §2 (a1, a3, H2–H9).

| ID | Câu | Số | Anchor | Trạng thái | Lưu ý |
|---|---|---|---|---|---|
| L01 | Stage 1a: SF-C120 trên 34 ô T3.8 — số phục vụ, trễ/kịp 60/120 s, so với C-30 và U | — | — | (chưa chạy) | Dự đoán a1–a3 (V17:256-258) là lựa chọn thiết kế; không gọi một điểm là tối ưu. |
| L02 | Stage 1b Gate 0: binary mới (tắt tùy chọn) tái lập SF-U, SF-C30 trên 2 ô | — | — | (chưa chạy) | Bất kỳ lệch nào: dừng. |
| L03 | Stage 1b: CF-U, CF-C30 (ưu tiên chi phí, giữ cổng/khóa/phục hồi) — tương tác DiD trễ 60 s kèm phục vụ, từ chối, kịp 60/120 s | — | — | (chưa chạy) | I_L = I_served − I_timely60 (NEW:19); báo cả ba kết cục và theo ô/ngày. |
| L04 | Stage 1b: đi chung tuyệt đối của CF-C30 so với SF-C30 (cắt theo số đếm chính xác) | — | — | (chưa chạy) | Ngưỡng 345 chỉ minh họa đến khi có số đếm chính xác (R18 §2 H6). |
| L05 | Cổng Stage 2: số khách chỉ-cộng-dồn trên quỹ đạo CF-U ở B = 120 s | — | — | (chưa chạy) | Là quy tắc phân bổ công sức, không chứng minh không có tác dụng (R18 §2 H7). |

---

## Tổng hợp số mục (đếm theo từng ID)

Mỗi mục được tính theo trạng thái của **khẳng định chính**; chi tiết phụ có trạng thái yếu hơn được ghi ở cột trạng thái
hoặc lưu ý của chính mục đó (ví dụ B02 phần "0,4%", B21 phần ngày nghỉ, A28 phần core commit).

| Mục | Số mục | VERIFIED-by-me | VERIFIED-by-Codex (R13/R14/R15/R18) | UNVERIFIED |
|---|---|---|---|---|
| A | 28 | 26 | 2 (A20, A22) | 0 |
| B | 27 | 26 | 1 (B27) | 0 |
| C | 32 | 32 | 0 | 0 |
| D | 20 | 20 | 0 | 0 |
| E | 10 | 8 | 2 (E07, E09) | 0 |
| F | 19 | 18 | 0 | 1 (F19) |
| G | 12 | 10 | 1 (G12) | 1 (G11) |
| H | 13 | 13 | 0 | 0 |
| I | 17 | 14 | 2 (I13, I15) | 1 (I16) |
| J | 42 | 21 | 14 (J05, J08, J26-J35, J37, J42) | 7 (J12-J16, J36, J41) |
| K | 52 | 50 | 2 (K29, K45) | 0 |
| **A–K** | **272** | **238** | **24** | **10** |

Bảng này khớp với phép đếm máy theo chữ mở đầu cột trạng thái của từng dòng có ID.
| L | 5 chỗ trống (chưa có kết quả) | — | — | — |

## Các con số / câu sai trong tài liệu nguồn (tôi tìm được hoặc xác nhận lại)

1. **HO:116-117** — đường dẫn `RideBound.Application/Scheduling/PromiseProjector.cs` không tồn tại; tệp thật là
   `SRC/RideBound.Application/Promises/PromiseProjector.cs` (nội dung dòng 63-131 đúng như mô tả).
2. **HO:336** — ML3 "thêm 6,9% khách tới sớm" là số của lần chạy **trước** phụ lục A1 (ML0:21); báo cáo A1 hợp lệ ghi
   **7,1%** (ML:21; CHK:211-212). Kết luận ML3 SAI không đổi.
3. **HO:211** — "sáng cuối tuần 1,23–1,55": trên các ô kiểm T3.8 cận trên là **1,462** (18/11 khung 8h); 1,550 là
   f(0)/f(7h) ngày 18/11, không có ô nào của panel A (SPLIT; SCOPE:14; CHK:207-208). Hai dải 8h và 17h đúng.
4. **V17:640** — "Cả 1.256 lần chặn đều do một lần dời đã vượt trần **30 giây**": B thay đổi 30–300 s giữa các nhánh
   (NEW:1); R18 §4 Câu 3 đã sửa.
5. **V17:620-621, 631-632** — "148 khách bị từ chối vì trần"; "nới trần chỉ tốt hơn ở 2 phút; ở 1 phút cứ thêm một khách
   thêm một khách trễ": số liệu mâu thuẫn — w07 C-30→C-120 **+2** lượt kịp 60 s (CAP:4,7), WP14r **+6** (WP17:9,19). R18 đã sửa.
6. **V17 B52** — "0,307% / 0,079% over all frames" mô tả sai ước lượng: đó là **tỉ số tổng giảm chi phí / tổng chi phí**
   (0,3069% / 0,0794%), không phải trung bình theo frame (NEW:6). R18 đánh WRONG.
7. **V17 D11** — "về giờ đến thực tế, luật C và luật hạn chót cho kết quả như nhau": trễ quá 60 s theo lời hứa ngây thơ là
   **76 (C-30) so với 74 (M⁺-30)** (A:7-8). Chỉ tổng phục vụ và kịp 60 s khi có dự báo là bằng nhau.
8. **V17:205** — "Accumulation cannot be tested at B = 30 s": FREE có 2 khách chỉ-cộng-dồn ở 30 s (CVP:5). R18 đã sửa.
9. **V17:603-604** — "khớp đến từng khách": nói quá (R18 §2).
10. **V17 B17** — "VERIFIED (3/34 spot-checked)": đã được Codex giải mã cả 34 checkpoint (NEW:17); không sai số, chỉ cũ.
11. **V13:56-58** — "luật mỗi bước sẽ nhận đúng các phương án đó"; "nhiều nhất 7 quyết định / 1 lượt từ chối" — sai khi
    dùng làm cận (R15 corr. 1; V17 B97, B95).
12. **HO:155-156** — "đóng góp là tách nguyên nhân": bị Hörl & Zwick 2022 chiến lược B bác (HZ:529-543; V17 D2).
13. **HO:223** — "148 yêu cầu bị chặn chỉ vì ngân sách": phân loại theo bản ghi, không chứng minh lý do duy nhất (R15 row 59).
14. Nhãn mẫu số (không sai số nhưng dễ đọc sai): HO:185-188 dùng **trung bình theo ô** (9,1% / 4,1%; 0,77%) ngay cạnh
    bảng **gộp theo khách** (8,34% / 3,25%) ở HO:190-196; FR:42 0,17% là trung bình 21 ô (gộp 0,136%).
15. HO:317-320 hàng "U + đệm 1.031 / 1.061, ~60 s, 67–84%" khớp quy tắc **room** E = 60 (BACK:18), quy tắc đã bị loại;
    quy tắc horizon E = 60 (BACK:16) cũng cho 1.031/1.061 nhưng 72,8–81,4% tới sát giờ báo. Cần ghi rõ quy tắc nào.
