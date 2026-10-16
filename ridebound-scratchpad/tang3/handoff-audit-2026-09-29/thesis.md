# thesis

## 1. [thesis-files]
The thesis root E:\Code\Report_INT3508\ridebound has main.tex, README.md, main.pdf, main.log, hinh\{logo-uet.png, tang2-bon-ho.pdf, tang2-bon-ho-v2.pdf} and noi-dung\00-bia, 01-loi-cam-on, 02-tom-tat, 03-muc-luc, 04-viet-tat, 05-chuong1, 06-chuong2, 07-chuong3, 08-chuong4, 09-chuong5, 10-tai-lieu (.tex). main.tex pulls them in that order (\input at lines 101-118).
SOURCE: Glob E:\Code\Report_INT3508\ridebound\*; E:\Code\Report_INT3508\ridebound\main.tex:101-118

## 2. [thesis-files]
Last-modified times: 08-chuong4.tex 2026-09-29 11:54:31; 09-chuong5.tex 2026-09-29 01:14:49; 05-chuong1.tex 2026-09-25 16:30:57; 02-tom-tat.tex 2026-09-24 21:24:24; 07-chuong3.tex 2026-09-24 21:24:30. main.log and main.pdf were both written 2026-09-29 11:54:58, after the last edit to chuong4.
SOURCE: PowerShell Get-ChildItem / Get-Item LastWriteTime on noi-dung\*, main.log, main.pdf

## 3. [thesis-build-state]
main.log reports 'Output written on main.xdv (100 pages, 2154652 bytes)'. A grep for undefined/Overfull/multiply defined/Error finds nothing except the rerunfilecheck package line 678. The log is fresh (11:54:58, after the 11:54:31 edit).
SOURCE: E:\Code\Report_INT3508\ridebound\main.log:1260, :678 (grep)

## 4. [thesis-version-control]
The thesis folder ridebound/ is untracked in git in E:\Code\Report_INT3508, shown as '?? ridebound/'. That repo has a single commit, ac0e13e (2026-09-09, the internship report), and uncommitted changes to its own internship files. The untracked items also include BAN-GIAO-PHIEN-2026-09-23.md, KE-HOACH-HOP-NHAT-2026-09-23.md, KE-HOACH-NGHIEN-CUU-2026-09-22.md, RIDEBOUND-BAN-GIAO-CONTEXT.md and ridebound-scratchpad/.
SOURCE: git -C E:\Code\Report_INT3508 log -3 / status --short (output)

## 5. [thesis-structure]
Chapter/section titles with line numbers. 01-loi-cam-on:1 Lời cảm ơn. 02-tom-tat:1 Tóm tắt, :46 Abstract. 04-viet-tat:1 Danh mục từ viết tắt. 05-chuong1:1 Ch.1 Đặt vấn đề, with sections :3 Bối cảnh, :51 Hạn chế của các phương pháp hiện tại, :84 Chỗ đứng so với công trình gần nhất (muc:chodung), :196 Mục tiêu và đóng góp, :267 Phạm vi và giới hạn, :285 Cấu trúc báo cáo. 06-chuong2:1 Ch.2 Cơ sở lý thuyết, with sections :12, :80, :136, :162, :189 Giá trị của độ tin cậy, :210 Điều khiển trực tuyến có nhiễu. 10-tai-lieu:1 Tài liệu tham khảo.
SOURCE: Grep \\(chapter|section|subsection) in noi-dung (output)

## 6. [thesis-structure]
07-chuong3.tex (Ch.3 Lời hứa có biên được chứng nhận, line 1) has sections at :8 Tổng quan cơ chế, :47 Mô hình mở rộng, :73 Phép phân rã ba mốc, :151 Sổ cái cam kết, :175 Hai cơ sở tính, các định lý và khung bốn họ cổng, :677 Các cơ chế bảo vệ bổ sung and :695 Kiến trúc cài đặt. Subsections include :283 Ba định lý, :415 Khung so sánh bốn họ cổng (label muc:hocong :416), :596 and :636 Các phản ví dụ. Key labels: dl:hanhvi :287, dl:ketqua :305, dl:tapcon :316, md:chuoi :441, bang:hocong :466, dl:hocong :502, hq:tatdinh :545, hq:chieutroi :559, bang:phanvidu :644.
SOURCE: Grep in 07-chuong3.tex (output)

## 7. [thesis-structure]
08-chuong4.tex (Ch.4 Thực nghiệm và đánh giá) sections: :36 Thiết lập thực nghiệm; :115 Quy trách; :304 Đường biên; :441 So sánh hai cơ sở tính; :515 Độ vững với cách đo; :582 Thí nghiệm phụ: bảo đảm một chiều; :660 Thí nghiệm trôi dạt thật (muc:troidat), which contains subsections :875 (muc:haunghiem) and :915 (muc:hoito); :937 Thí nghiệm hạn chót có tiền đăng ký (thăm dò) (label muc:tang2 :938); :1132 Quét mức lời hứa dưới tắc đường: hành vi so với hạn chót (thăm dò) (label muc:quet :1133); :1405 Phép thử trần cửa sổ đón (muc:cuaso); :1552 Đối chiếu với Fielbaum và Alonso-Mora; :1673 Phúc lợi; :1715 Chứng cứ không giả tạo; :1746 Bộ sinh phương án biết đến lời hứa; :2008 Các hướng đã thử (muc:dathu); :2055 Hạn chế của thực nghiệm (label muc:hanche :2056).
SOURCE: Grep in 08-chuong4.tex (output)

## 8. [thesis-structure]
09-chuong5.tex (Ch.5 Kết luận, line 1) has sections :3 Tổng kết, :81 Hạn chế, :125 Hướng phát triển and :191 Kết luận cuối.
SOURCE: Grep in 09-chuong5.tex (output)

## 9. [ch3-theorem]
Theorem dl:hocong (Thứ tự khả thi của các họ cổng) assumes (N). (a) For every kappa and on every trajectory, gate C never rejects the do-nothing option, so the conduct gate is never the cause of an empty choice set. (b) On the fallback trajectory with a continuous announcement chain, the minimal safe thresholds are kappa*_C=0 <= kappa*_M+ = M+_noop <= kappa*_M = M_noop <= kappa*_V = X_noop. Corollary hq:chieutroi: under adverse drift M+_noop=M_noop=V_noop; under favourable drift M+_noop=0 while M and V can still reject do-nothing. The four families (bang:hocong) are C (sum A_t <= kappa), M+ (p_t-p0 <= kappa, Schulz-Pfeiffer), M (|p_t-p0| <= kappa) and V (sum B_t <= kappa).
SOURCE: E:\Code\Report_INT3508\ridebound\noi-dung\07-chuong3.tex:466-476, 501-517, 558-572

## 10. [ch3-side-prediction]
Ch.3 states a side prediction: under a one-sided deadline and favourable drift, the operator can spend the favourable drift, so M+ may serve more riders than C. It says this was not observed on the 8 evening cells of muc:tang2 (the 30 s deadline accepted exactly one more rider in one cell and the same number in seven).
SOURCE: 07-chuong3.tex:587-594

## 11. [tang2-design]
The muc:tang2 design compares four families at a 30 s cap: C = config C1; M+ drops the drop-off budget and rejects any plan that makes a drop-off later than the rider's FIRST promise by more than l, with l in {30,60,120}; M also rejects plans earlier than the first promise by more than 30 s; V = C1 with the rider-visible basis. The deadline rule is off by default, and with it off the runner is byte-identical to the old runner (963 tests and 2 independent reviews). The new runner reports the reject reason of the do-nothing option itself.
SOURCE: 08-chuong4.tex:946-959

## 12. [tang2-design]
Panel 2A is the main panel: 20 cells, 8:00-10:00, 14-18/11, k in {0,1}. Panel 2B is a development panel of 16 cells from 12-13/11 that was never used to build the prediction rule: 8 morning cells and 8 evening cells (17:00-19:00). On the 12/11 evening the factor rises to 1.015 at minute 15, then falls to 0.837. A cell counts as commitment-infeasible when the run stops with an error whose reason is a commitment rule. Stops from the pickup-window invariant count as NOT commitment-infeasible.
SOURCE: 08-chuong4.tex:961-971

## 13. [tang2-controls]
The k=0 controls on 20 cells of 2A reproduce the old runs exactly on the 36 completed cells. V is infeasible on exactly 16-r2, 16-r4, 17-r1 and 17-r3, and the other 16 cells accept a total of 1,294 riders (= bang:coso). The reference C runs at k=1 give 2A: 9 completed and 11 stopped by the pickup-window invariant; 2B: 13 completed and 3 morning cells stopped.
SOURCE: 08-chuong4.tex:975-986

## 14. [tang2-seal]
The preregistration, 200 predictions and the code were sealed with SHA-256 at 06:03:52 UTC on 24/9/2026, before any predicted arm ran. A bug found before sealing (infinity <= infinity) was kept, unsealed and unused. Five runs broken by laptop sleep were rerun under a pre-hashed rule. Without that rule 2A accuracy would be 99/102 instead of 98/102.
SOURCE: 08-chuong4.tex:995-1002

## 15. [tang2-results-table]
bang:tang2-dem gives commitment-infeasible cells, with pickup-window stops in parentheses, for C / M+30 / M+60 / M+120 / M30 / V. 2A k=0 (20): 0/0/0/0/---/4. 2A k=1 (20): 0(11) / 19(1) / 13(5) / 3(11) / --- / 19(1). 2B morning k=1 (8): 0(3) / 4(1) / 0(3) / 1(4) / 4(1) / 8. 2B evening k=1 (8): 0/0/0/0/7/8.
SOURCE: 08-chuong4.tex:1006-1023

## 16. [tang2-results]
Behaviour gate: 0 commitment-infeasible in 56 runs; its 14 stops are all from the pickup-window invariant. All 90 commitment-infeasible runs cite the do-nothing option itself: 51 in the deadline families and 39 in V. On the reference trajectory, the 30 s crossing time is 900-942 s in 13/19 cells. At 60 s and 120 s, 13/20 and 3/20 cells are still infeasible. The effect is non-monotone: cell 18-r2 completes at 60 s but is infeasible at 120 s.
SOURCE: 08-chuong4.tex:1033-1047

## 17. [tang2-scope]
Scope stated in the thesis: 30/60/120 s are much tighter than Schulz-Pfeiffer's L=900 s (they recommend 10-15 min), and the two rules bound different quantities, so the result must not be read as the thesis mechanism beating theirs. At k=0 on all 20 cells of 2A, C-30 and M+-30 accept exactly the same rider set. The largest per-rider cumulative drift is 150.7 s (bang:troidat), so at 15 min a deadline likely does not empty the set. The sweep in muc:quet is cited as showing exactly that.
SOURCE: 08-chuong4.tex:1049-1064

## 18. [tang2-results]
Evening 2B: M+ is infeasible on 0/8, M on 7/8 and V on 8/8, and all seven M failures are at the LOWER bound. Morning 2B: M+ and M each fail on 4/8, the same four cells, all at the upper bound. Clopper-Pearson 95% intervals: 0/8 [0;0.37], 7/8 [0.47;1], 8/8 [0.63;1], 19/20 [0.75;1].
SOURCE: 08-chuong4.tex:1066-1081

## 19. [tang2-predictions]
bang:tang2-dudoan (sealed per-cell predictions): 2A 98/102 (96.1%) against a threshold of >=90% plus M+30 at k=1 infeasible on >=11/20 (met, 19/20); 2B morning 31/32 (96.9%); 2B evening 40/40 (100%) against >=90% plus the evening row in the right direction (met); weak predictions (window stops) 25/26. The five determinate misses: four dl-120 cases, where the branch's conduct component is 189-394 s against 0-8 s in the reference, and one dl-60 case (cell 15-r3, M+ = 56.4 s).
SOURCE: 08-chuong4.tex:1083-1108

## 20. [tang2-side]
The side prediction is not supported: on the 8 evening cells, M+30 accepts one more rider in one cell and the same in seven. With no drift, M+30 equals C on all 20 cells (1,581 riders), and relaxing to 120 s adds 27 riders.
SOURCE: 08-chuong4.tex:1110-1114

## 21. [tang2-interpretation]
The 'Diễn giải và giới hạn' subsection of tang2 says: only the conduct quantity is never the cause of an empty set, and which other family fails depends on drift direction, as predicted per cell. It explicitly makes NO claim that the thesis mechanism is better than Schulz-Pfeiffer. Stated limits: exploratory (drift runs not verified by the project verifier), scalar network-wide drift, 8 cells per window from 2 days with one seed, the 2B morning M+ result at exactly 4/8 (near the 'majority' threshold), a heuristic prediction rule, and 11/20 window stops under C in 2A as a system limit.
SOURCE: 08-chuong4.tex:1116-1130

## 22. [quet-design]
muc:quet design: C-x and M+-x for x in {30,60,120,300,600,900}, plus the ungated arm U. 13 arms x 6 worlds x 2 dev cells = 156 runs, each cell with 108 requests and 8 vehicles. The worlds are no-noise, one shock with recovery, repeated shock, easing congestion, pairwise noise, and the measured Manhattan day. The factor switches exactly at each 15-min bin. Recovery rule (a): when all options are rejected, the vehicle keeps its route and a typed violation is logged; it only applies to M+. Seven predictions were SHA-256-sealed before the first run.
SOURCE: 08-chuong4.tex:1135-1159

## 23. [quet-results]
All 156 runs completed and passed the ledger audit. Twelve runs were rerun after an operator error that changed the source tree mid-run, and the reruns match the broken runs frame for frame. Real-congestion group: 2 cells of 12/11 (morning and evening), 216 requests, U serves 192. Synthetic group: 6 cells (one shock, repeated shock, pairwise noise), 648 requests, U serves 523.
SOURCE: 08-chuong4.tex:1163-1173

## 24. [quet-table-bang:quet]
bang:quet columns: served C/M+, M+ promise broken, C scored by the M+ rule, M+ forced. Real (2 cells): 30: 189/189, 1.1%, 1.1%, 11.9%; 60: 190/190, 0, 0, 0; 120: 190/191, 0, 0, 0; 300: 192/192, 0s; 600,900: 192/192, 0s. Synthetic (6 cells): 30: 508/503, 18.8%, 17.7%, 33.5%; 60: 509/503, 14.7%, 14.4%, 28.9%; 120: 513/513, 10.1%, 10.8%, 17.2%; 300: 522/524, 1.0%, 1.0%, 5.2%; 600,900: 523/523, 0s. C's promise is never broken. Pooled over 8 cells, M+ breaks 14.4/11.0/7.6/0.7% at 30/60/120/300.
SOURCE: 08-chuong4.tex:1175-1212

## 25. [quet-table-bang:quet-kieu]
bang:quet-kieu (2 cells and 216 requests per world) gives U; M+ broken at 30/60/120/300 s; and served at 30 s as C/(a)/(b). No change: 201; 0/0/0/0; 192/192/192. One shock*: 167; 12.3/12.3/7.8/3.0; 161/162/161. Repeated shock*: 166; 28.8/25.2/21.4/0; 164/160/164. Easing*: 215; all 0; 215/215/215. Pairwise noise*: 190; 15.3/6.6/1.1/0; 183/181/183. Real day 12/11: 192; 1.1/0/0/0; 189/189/189. Shock definitions: one shock goes to 1.6 at minute 30 and back to 1.0 at minute 75; repeated alternates 1.5/1.1 every 15 min; easing goes down to 0.7; noise is about 8% per OD pair plus random shocks. With (b), M+ equals C at 30 s in all six worlds.
SOURCE: 08-chuong4.tex:1214-1262

## 26. [quet-predictions]
Five of seven sweep predictions were correct. Three are listed: identical rider set with no noise (12/12 pairs); at 900 s both rules equal U (12/12); C never forced (0/72). Two failed: M+ was not forced on the real evening cell (traffic eased); and on its own metric M+ was not consistently better than C (5/8, 5/8, 7/8 cells at the three tight levels, 'below the 6/8 threshold').
SOURCE: 08-chuong4.tex:1264-1276

## 27. [quet-recovery-b]
Recovery rule (b), 'no worse than reference': a forced vehicle may re-route if every gate the new route violates was already violated by the old route, and the new route is no worse on each. It was added AFTER sealing, behind a new config key, and (a) results are kept. Rerun: 22 forced M+ runs plus 6 unforced controls, all 28 completed and audited. The 6 controls are decision-identical, and (b) was used at 49 decisions.
SOURCE: 08-chuong4.tex:1278-1291

## 28. [quet-table-bang:quetb]
bang:quetb columns: served C/M+(a)/M+(b), M+(b) same decisions as C, M+(b) broken, M+(b) forced. Real: 30: 189/189/189, 2/2, 1.1%, 11.6%; 60: 190/190/190, 2/2, 0, 0; 120: 190/191/191, 1/2, 0, 0; 300: 192/192/192, 2/2, 0, 0. Synthetic: 30: 508/503/508, 5/6, 18.4%, 35.5%; 60: 509/503/509, 6/6, 14.4%, 25.6%; 120: 513/513/514, 4/6, 10.4%, 18.1%; 300: 522/524/522, 6/6, 1.0%, 5.3%. On the 22 forced runs, served totals are (b) 1874, (a) 1864, C 1873; (b) equals C in 21/22 runs and has the same decision chain in 19/22. Example: one evening cell at 120 s, (a) 82 and (b) 79 = C. Consistency check: at 60 and 300 s, M+(b) makes the same decisions as C in all 8 cells, and its broken rate equals the 'C by M+ rule' column (14.4% and 1.0% synthetic, 0% real).
SOURCE: 08-chuong4.tex:1293-1336

## 29. [quet-interpretation]
The sweep's 'Diễn giải và giới hạn' makes three claims. (1) At 600 s and above, including the original paper's level, the two rules do not differ on this data. (2) At tight levels the served counts are nearly equal: the gap is at most 6 of 864 (at most 1 of 216 on real congestion) and changes sign; under (b) the gap is 0-2 riders, so the small gap came from recovery, not the deadline. (3) The difference is whether promises hold: C always keeps its promise; M+ breaks it for 10-19% of riders at 30-120 s under synthetic congestion and for 1.1% at 30 s (0% from 60 s) under real congestion; M+ is forced at 17-34% of decisions (synthetic) and 12% (real, 30 s). Example: at 60 s with (b), same decisions as C in all 8 cells, yet M+ records 14.4% broken and 25.6% forced. The conclusion does NOT support 'the conduct cap serves more'; it supports the narrower claim that under tight promises in congestion only the conduct promise is keepable without recovery.
SOURCE: 08-chuong4.tex:1338-1366

## 30. [quet-limits]
Stated sweep limits: one run per cell with no CIs, and four synthetic worlds. Big breaks occur only under synthetic shocks: +60% in one 15-min bin, which is about 3.7 times the largest real step (16.2%, 14/11); on 12/11 the real factor rises only to 17.6% over 75 min in the morning and falls 16% in the evening. On the real day M+ breaks only at 30 s in the morning, for 2.2% of that cell's riders (= C scored by M+). Real data does have cumulative +29-50% per hour on 12-16/11. The 7:00-9:00 window was not run: its peak rise is 47-66% against 15-23% for 8:00-10:00, its largest step 8.3-16.2% against 3.7-7.1%, and its demand is similar (2,400-2,700 against 2,500-2,800 in a 10% sample). So the conclusion 'on real congestion the two rules are equal from a 1-minute promise' holds only for the two windows run. Other limits: only Manhattan (the Hamburg dataset is public but not run); only the promise rule is compared, not the full Schulz-Pfeiffer system (no rejection model and no insertion/re-opt of theirs); (b) is descriptive (post-seal), and other recoveries (vehicle swap, fleet re-optimisation) were not tried.
SOURCE: 08-chuong4.tex:1368-1403

## 31. [hanche]
muc:hanche lists these limits: small scale (108 requests / 8 vehicles); the network is a metric closure of 96 nodes (9,120 arcs) with synthetic coordinates; drift on the main panel is a lower bound; injected drift is scalar and not verified, and the morning factor is 17-26% higher at the end of the window than at the start with monotonicity 'chưa kiểm'; the deadline experiment is small and heuristic, 4/8 in the 2B morning, and the sleep-rerun rule lowered accuracy from 99/102 to 98/102; C still stops on 11/20 cells under real drift from the pickup-window invariant; 'Không có kết quả về tỉ lệ phục vụ dưới trôi dạt thật' (blocked by the invariant); fences longer than the 600 s booking horizon cannot be tested; welfare is less certain; no reassignment, so the 89.06% holds only without reassignment. muc:hanche does not mention the muc:quet sweep.
SOURCE: 08-chuong4.tex:2055-2106

## 32. [dathu]
muc:dathu says the Schulz-Pfeiffer deadline is the M+ family, run in muc:tang2 (19/20 infeasible at 30 s in the morning), and that because 30 s is much tighter than 15 min and the rules coincide with no drift, this is a result about tight promises, not about their mechanism at their level.
SOURCE: 08-chuong4.tex:2019-2027

## 33. [ch5-summary]
Ch.5 Tổng kết, verbatim excerpt: 'Một thí nghiệm thăm dò có tiền đăng ký sau đó đặt hai họ hạn chót vào cùng phép thử: dự đoán theo từng ô ... đúng ở 98/102 cặp trên panel chính và ở 31/32, 40/40 cặp ... Buổi sáng, hạn chót 30 giây ... vô nghiệm do cam kết ở 19/20 ô; buổi tối ... hạn chót một chiều vô nghiệm ở 0/8 ô trong khi hạn chót hai chiều và cổng kết quả vô nghiệm ở 7/8 và 8/8 ô; cổng hành vi không vô nghiệm do cam kết ở lần chạy nào trong 56 lần. Mức 30 giây chặt hơn nhiều so với 15 phút của Schulz và Pfeiffer. Khi không có trôi dạt, hai luật cùng 30 giây nhận đúng cùng một tập khách ở 20/20 ô. Vì vậy đây là kết quả về vùng lời hứa chặt dưới tắc đường. Một phép quét thăm dò từ 30 giây tới 15 phút (mục \ref{muc:quet}) cho thấy hai luật phục vụ gần như cùng số khách ở mọi mức. Khác biệt là lời hứa có giữ được hay không. Dưới tắc đường tự tạo có cú sốc, ở mức chặt, lời hứa của hạn chót bị phá với 10--19% khách, còn trần hành vi giữ mọi lời hứa. Trên ngày tắc đường đo thật, hạn chót chỉ phá lời hứa ở mức 30 giây buổi sáng, với 2,2% khách.'
SOURCE: 09-chuong5.tex:42-54

## 34. [ch5-summary]
Ch.5 opens with '558 lần chạy trên một panel 20 ô đã niêm phong cho bốn nhóm kết quả' (line 34). Lines 18-22 state the four-family framework and dl:hocong with the families listed as 'hạn chót một chiều kiểu Schulz và Pfeiffer, hạn chót hai chiều, ràng buộc theo kết quả'. Line 41 says the outcome basis is infeasible on 19/20 cells and the conduct basis on none, 'dù 11 ô vẫn dừng'.
SOURCE: 09-chuong5.tex:18-22, 34, 40-42

## 35. [ch5-limits]
Ch.5 Hạn chế, limit 2: 'Schulz và Pfeiffer đã có một hạn chót cưỡng chế được tính từ lời hứa đầu' (lines 95-97). Limit 3: drift is a lower bound, and the drift experiment gives feasibility but NOT service rate because of the domain invariant (lines 99-105). Limit 4: the four-family evidence is exploratory (not verified, scalar drift, 8 cells per window from 2 days, one seed, heuristic rule with 5 misses when branches diverge); favourable drift was seen only on one window type (the evening of two days); and C still stops on 11/20 cells (lines 107-114).
SOURCE: 09-chuong5.tex:91-114

## 36. [ch5-future-work]
Ch.5 Hướng phát triển lists seven items in order. (1) Make the four-family experiment official (the project verifier must accept drift runs), then per-edge drift including two-directional drift and recovery after shocks, over more days and seeds; measure the unobserved side prediction ('trong phép quét ở mục \ref{muc:quet}, hai luật phục vụ bằng nhau ở thế giới tắc đường giảm, nhưng ở đó gần như mọi khách đều được phục vụ nên phép thử chưa đủ nhạy'); and test the per-cell rule when branches diverge (lines 130-137). (2) Harm-only ledger h_t = max(0, |p_t-p0| - |e_t-p0|): on B1, sum h = 64,821.2 s against sum A = 64,863.1 s (a 41.9 s gap, 0.06%), with h != A at 158/479 announcements (lines 139-154). (3) A service-rate comparison of the two bases on a panel with fewer riders per cell (lines 156-162). (4) Extend the surface to a third freedom dimension, fleet size and demand density (lines 164-168). (5) Selectively negotiated pickup window, 172 riders at a median wait of about 407 s (lines 170-173). (6) Relax the pickup-window domain invariant (lines 175-178). (7) Freeze the in-flight leg, then unlock the reorder-aware generator, which fails on 18/20 cells (lines 180-189).
SOURCE: 09-chuong5.tex:125-189

## 37. [ch5-final]
The Ch.5 final conclusion says a preregistered experiment on real congestion data confirms dl:hocong 'ở mức thăm dò, theo từng ô và ở cả hai chiều trôi': V jams in both directions; the one-sided deadline jams when congestion rises and is safe when it falls; the two-sided deadline jams in both (upper bound in the morning, lower bound in the evening); only the conduct cap is never the cause. The sweep is not mentioned in Kết luận cuối.
SOURCE: 09-chuong5.tex:202-209

## 38. [ch1]
Ch.1 on Schulz-Pfeiffer: at acceptance they compute a deadline equal to the announced drop-off time plus a common constant (default 15 min); later insertions must keep drop-off no later than it; it is a hard cap on current lateness vs the FIRST promise, with no accumulation and no early-side bound; travel times are fixed in their model; they state accepted riders are never rejected later.
SOURCE: 05-chuong1.tex:142-148

## 39. [ch1]
Ch.1 design-space bullet: 'hạn chót tính từ lời hứa đầu (Schulz và Pfeiffer 2026): theo Định lý \ref{dl:hocong}, có thể tự nó làm rỗng tập phương án khi thời gian đi trôi dạt theo chiều bất lợi --- một hệ quả của định lý, chưa được quan sát trên hệ của họ vì mô hình của họ không có trôi dạt'.
SOURCE: 05-chuong1.tex:166-168

## 40. [ch1]
Ch.1 states the exploratory preregistered comparison is right on 98/102 main-panel pairs and on 31/32 and 40/40 held-out pairs, and that drift runs are not verified by the project verifier.
SOURCE: 05-chuong1.tex:184-188

## 41. [ch1]
Ch.1 contributions bullet on Tier 2, verbatim excerpt: 'Một thí nghiệm thăm dò có tiền đăng ký kiểm thêm hai họ hạn chót: dưới tắc đường buổi sáng, hạn chót 30 giây tính từ lời hứa đầu vô nghiệm do cam kết ở 19/20 ô; buổi tối, khi tắc đường giảm, hạn chót một chiều vô nghiệm ở 0/8 ô còn hạn chót hai chiều ở 7/8 ô, đúng chiều định lý dự đoán. Mức 30 giây chặt hơn nhiều so với 15 phút mà Schulz và Pfeiffer dùng. Khi không có trôi dạt, hạn chót và trần hành vi cùng 30 giây nhận đúng cùng một tập khách ở 20/20 ô, nên kết quả này nói về vùng lời hứa chặt dưới tắc đường. Chứng minh là sơ cấp; bằng chứng thực nghiệm là thăm dò.' Ch.1 does not mention or cite the muc:quet sweep anywhere.
SOURCE: 05-chuong1.tex:219-236; Grep 'muc:quet' in noi-dung (hits only in 08-chuong4 and 09-chuong5)

## 42. [abstract]
Vietnamese Tóm tắt, Tier 2 sentence: 'Một thí nghiệm thăm dò có tiền đăng ký kiểm thêm hai họ hạn chót, với dự đoán theo từng ô niêm phong trước khi chạy các nhánh được dự đoán: dự đoán đúng ở 98/102 cặp trên panel chính và ở 31/32, 40/40 cặp trên khung sáng và khung tối của một tập giữ lại; khi tắc đường giảm, hạn chót một chiều vô nghiệm ở 0/8 ô còn hạn chót hai chiều ở 7/8 ô, đúng chiều định lý dự đoán.' Also: '558 lần chạy mô phỏng' (line 27); 89.06%; 30 s cap -> 1.37% at 7.13 pp (lines 28-30); V 19/20 against C 0 with 11 stops (lines 30-33). There is no sentence about the deadline sweep.
SOURCE: 02-tom-tat.tex:22-38

## 43. [abstract]
English Abstract mirrors the Vietnamese: four families; 558 simulation runs; 89.06%; 1.37% at 7.13 pp; 'outcome basis is commitment-infeasible on 19 of 20 cells while the conduct basis is commitment-infeasible on none --- although 11 cells still stop on a pickup-window invariant'; preregistered predictions 'hold on 98/102 pairs on the main panel and on 31/32 and 40/40 pairs'; 'one-sided deadline is commitment-infeasible on 0 of 8 cells and the two-sided one on 7 of 8'. There is no deadline-sweep sentence.
SOURCE: 02-tom-tat.tex:66-83

## 44. [placeholder]
The supervisor name is still a placeholder: '\textbf{Cán bộ hướng dẫn} & : & \textbf{[chờ bổ sung]}' in Vietnamese and '\textbf{Supervisor} & : & \textbf{[to be filled]}' in English. README.md:65 says to search '[chờ bổ sung]'. 01-loi-cam-on.tex:4 says 'thầy cô hướng dẫn' generically.
SOURCE: 00-bia.tex:28, 00-bia.tex:64, README.md:65, 01-loi-cam-on.tex:4

## 45. [unverified-citation]
Geržinič et al. (gerzinic2023, Travel Behaviour and Society 33:100616, 2023) is cited at 05-chuong1.tex:34, 06-chuong2.tex:203-208 and 08-chuong4.tex:1702-1704. The 20-25 EUR/h surprise-wait valuation attributed to it is explicitly marked 'chưa đối chiếu được với bản gốc' in Ch.2:206-207 and Ch.4:1703; the Alonso-González figures are marked as checked. The last two rows of bang:hoavon (2.68 and 3.35 EUR) depend on the unchecked figure.
SOURCE: 10-tai-lieu.tex:32-37; 06-chuong2.tex:203-208; 08-chuong4.tex:1693-1704

## 46. [unverified-citation]
No text matching 'anticipat' or 'walking' exists anywhere in the thesis .tex/.md files.
SOURCE: Grep '[Gg]er[zž]ini|anticipat|walking|...' in E:\Code\Report_INT3508\ridebound (output)

## 47. [build-command]
The documented build command is E:\Code\Report_INT3508\tools\tectonic.exe, run from ridebound\ as '..\tools\tectonic.exe -X compile main.tex --outdir . --keep-logs'. There is no poppler/pdftotext; check main.log for undefined refs and Overfull boxes. Without --keep-logs tectonic does not rewrite main.log, so always check main.log's timestamp. README.md:12-15 documents the same command WITHOUT --keep-logs.
SOURCE: C:\Users\quang\.claude\projects\e--Code-RideBound\memory\ridebound-env-traps.md:15; E:\Code\Report_INT3508\ridebound\README.md:12-15

## 48. [schulz-bib]
The bib entry schulz2026 is A. Schulz and C. Pfeiffer, 'Efficient insertion and reoptimization algorithms for a customer-oriented dynamic dial-a-ride problem', OR Spectrum 48:541-586, 2026, doi 10.1007/s00291-026-00847-0. The thesis says the original paper sets L=900 s and recommends 10-15 min.
SOURCE: 10-tai-lieu.tex:116-121; 08-chuong4.tex:1050-1051

## 49. [consistency-checks-passed]
Cross-checks that hold: bang:quet-kieu synthetic worlds sum to bang:quet (U 167+166+190=523; C@30 161+164+183=508; M+(a)@30 162+160+181=503). The broken-rate means per group match (e.g. (12.3+28.8+15.3)/3=18.8). The pooled 8-cell figures (14.4/11.0/7.6/0.7) match. The 22-run totals are consistent (1873-9=1864 for (a); +1 for (b)=1874). The tang2 counts add up (56 = 20+20+8+8, 14 = 11+3, 51 = 23+13+4+11, 39 = 4+19+8+8, 5 misses = 4+1+0). 200 predictions = 102+32+40+26. The Clopper-Pearson bounds recomputed agree after rounding. The 3.7 ratio = 60/16.2. 1,581 = C1 served (bang:thang1:329).
SOURCE: 08-chuong4.tex:1017-1020, 1033-1043, 1092-1096, 1188-1199, 1210, 1234-1239, 1306-1315, 1326-1327, 1379-1380; bang:thang1 08-chuong4.tex:329 (arithmetic done by reader)

## 50. [calendar]
In the calendar, 2018-11-12 is a Monday, 13 Tuesday, 14 Wednesday, 15 Thursday, 16 Friday, 17 Saturday and 18 Sunday.
SOURCE: PowerShell Get-Date -Year 2018 -Month 11 -Day 12..18 DayOfWeek (output)

# UNVERIFIED
- Whether the sweep's 2 development cells (12/11 morning and evening) are the same cells as panel 2B's, and why all 156 sweep runs finished when 3/8 2B-morning C runs stopped on the pickup-window invariant. The thesis only says the sweep switches factors exactly at bin starts (08-chuong4.tex:1150); the results data was not read.
- The per-day rise of the morning factor: 08-chuong4.tex:687 and 2077-2078 say 17-26% for 14-18/11 (8:00-10:00), while 08-chuong4.tex:1387 says 15-23% for 8:00-10:00 on 12-16/11. These fit together only if 17/11 or 18/11 supplies the 26%; this cannot be checked without the factor CSV.
- 08-chuong4.tex:1044 (crossing times 900-942 s on 13/19 cells), :1047 (18-r2 non-monotone), :1105-1107 (conduct 189-394 s against 0-8 s; 56.4 s), :1281 (7-12% of the fleet frozen synthetic, max 2% real), :1290 (49 decisions used rule (b)), :1329 (82/79 example), :1390-1391 (demand counts): all are stated without a source path in the thesis and were not checked against the result artifacts.
- Whether the 7 sweep predictions and the 200 Tier-2 predictions match their sealed files. The thesis gives only the timestamp 06:03:52 UTC 24/9/2026 (08-chuong4.tex:995-996); the sealed files were not located or read in this slice.
- Whether Schulz-Pfeiffer really use L=900 s as the default and recommend 10-15 min (08-chuong4.tex:1050-1051, 05-chuong1.tex:144). The paper was not read here.
- Whether the FleetPy Manhattan demand files for '14-18/11/2018' are really those calendar dates. If they are, 17 and 18 are Saturday and Sunday, contradicting 'ngày làm việc'.
- The actual total number of Tier-2 and sweep runs (the thesis does not state a total for muc:tang2; the sweep is 156 + 12 reruns + 28 rule-(b) runs).
# WARNINGS
- STALE RUN TOTAL: bang:quymo (08-chuong4.tex:75-99) totals 558 runs / 33.62 GB and lists no Tier-2 (muc:tang2) or sweep (muc:quet) batches. Yet the abstract (02-tom-tat.tex:27, :72) and Ch.5 (09-chuong5.tex:34) say '558 lần chạy' while also reporting Tier-2 and sweep results. README.md:39-54 has the same 558 list and says the thesis is 66 pages, but main.log:1260 says 100 pages.
- The chapter roadmap bang:lotrinh (08-chuong4.tex:7-34) has a row for muc:tang2 but none for muc:quet. Ch.1 and the abstract never mention the sweep. The sweep appears only in Ch.4 and in Ch.5 lines 50-54 and 135-136.
- INCONSISTENT WORDING, Tier 3: 08-chuong4.tex:1274-1275 says M+ beat C in only '5/8, 5/8 và 7/8 ô ... dưới ngưỡng 6/8 đã ghi', but 7/8 is above 6/8, so only two of the three levels fall below the threshold.
- INCONSISTENT COUNT, Tier 3: 08-chuong4.tex:1264 says 'Năm trên bảy dự đoán đúng', but only three correct predictions are listed (1266-1268) with two wrong (1271-1276), so two correct predictions are never named.
- POSSIBLE INCONSISTENCY, Tier 3: 08-chuong4.tex:1392-1393 limits the claim 'trên tắc đường thật, hai luật như nhau từ mức lời hứa 1 phút', but bang:quet at 120 s real shows C 190 against M+ 191 (08-chuong4.tex:1190), and bang:quetb shows the same decisions on only 1/2 cells at 120 s (08-chuong4.tex:1308). The claim holds for promises broken (0%) but not strictly for served counts or decisions.
- RANGE MISMATCH, Tier 3: 08-chuong4.tex:1356 says M+ is forced at '17--34% quyết định dưới tắc đường tự tạo'. That fits rule (a) (bang:quet 17.2-33.5%, lines 1195-1197) but not rule (b) (bang:quetb 18.1-35.5%, lines 1312-1314), and the same bullet then quotes a (b) figure (25.6%, line 1360).
- PRESENTATION: the real-day M+ break rate is 1.1% in the tables (08-chuong4.tex:1188, 1239, 1306, 1353; mean over 2 cells) but 2.2% in 08-chuong4.tex:1377 and 09-chuong5.tex:53-54 (the morning cell only). Both are internally explained (1209, 1377), but readers may see a conflict. Likewise, 'M+ forced 11.9%/12%' real at 30 s (1188, 1357) is a 2-cell mean while only one cell was forced (1330-1331).
- SCOPE CONFLICT: muc:hanche 08-chuong4.tex:2095-2096 says 'Không có kết quả về tỉ lệ phục vụ dưới trôi dạt thật', but muc:quet reports served counts under measured 12/11 congestion (08-chuong4.tex:1169, 1188-1192, 1239). The hanche sentence should be scoped to the two-basis comparison of muc:troidat. muc:hanche also has no entry for the sweep's limits (one run per cell, synthetic shocks, 7:00-9:00 not run, Hamburg not run, (b) post-seal).
- CONTRADICTION outside Tier 3: 08-chuong4.tex:687-688 says the morning factor rises 17-26% 'và tăng đơn điệu', but muc:hanche 08-chuong4.tex:2078-2079 says 'tính đơn điệu giữa các mốc thì chưa kiểm'.
- CALENDAR: 05-chuong1.tex:271 and 08-chuong4.tex:43-44 call 14-18/11/2018 'ngày làm việc' / 'năm ngày làm việc', but 17/11/2018 is a Saturday and 18/11/2018 a Sunday (PowerShell Get-Date). This needs checking against the dataset.
- Ch.5 Hướng phát triển (09-chuong5.tex:125-189) has no item for the sweep's own open items listed in Ch.4 limits: run the 7:00-9:00 window (08-chuong4.tex:1392-1395), run the public Hamburg dataset (1396), and try other recovery rules such as vehicle swap or fleet re-optimisation (1400-1402).
- 150.7 s, used at 08-chuong4.tex:1060-1061 to argue that a 15-min deadline is unlikely to bind, is a max over SURVIVING cells only (survivor bias is stated at 08-chuong4.tex:728-729).
- The thesis folder E:\Code\Report_INT3508\ridebound is untracked by git (git status shows '?? ridebound/'), so edits have no version history or backup through git.
- README.md:14 gives the tectonic command without --keep-logs. Per ridebound-env-traps.md:15, that leaves a stale main.log. The current main.log is fresh (2026-09-29 11:54:58) and clean (no undefined refs or Overfull boxes).