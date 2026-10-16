# Agent regression audit — Ch4B v7 to v10

Scope: wording, caveats, denominators, references, EV mapping and rounding. This audit reads the prescribed rules, writing brief, style guide, corrected glossary, Addendum 1 §0, v7/v10, Addendum 6 plus errata, source rows in the main register and Addendum 3, FORECAST-REPORT, MLT header/rows, latest partA v4, Ch3 r33 v4-v3, and Ch2 v4. Root owns independent numeric probes; no simulation/build/install was run here. Suggested verdict: **ACCEPT WITH CORRECTIONS**.

## Required corrections, ranked within this scope

### 1. A 29,2-second observed maximum is not the designed guarantee — v10:220–222

Newly adding “theo cách xây dựng luật” makes the old shorthand materially stronger. C-30 guarantees the 30-second cap, subject to the conditions of Ch3; 29,239 seconds is the observed maximum on this cohort. The opening already makes clear that padding equals C at the one-minute on-time count and exceeds C at two minutes, so it need not be rejected as unfair to padding. It should distinguish the guarantee from its measured maximum.

Replace v10:220–222 with:

> Nhưng đệm không đổi quyết định điều phối: vẫn có 174 khách bị điều phối dời giờ trả, với tổng độ dời lớn nhất là 590,1 giây (gần 10 phút). Luật C đặt trần 30 giây cho tổng độ dời do điều phối của mỗi khách; trên 34 kịch bản, mức lớn nhất đo được là 29,2 giây, kể cả các kịch bản cuối tuần không có dự báo. Đổi lại, luật C phục vụ ít hơn 96 lượt.

EV remains C20/N-23/N-28/C02/A06/A22/K05. This wording makes no guarantee about arrival relative to the first promise.

### 2. Equal extensions are only approximate; fivefold extension is not a proved necessity — v10:269–271

“Ở cùng độ dài lời hứa” is a regression from v7:266 (“độ dài thêm gần bằng nhau”). The table compares average extensions 37,18 versus 37,37 seconds, on different served cohorts, not equal full promise durations. N-17/N-18 support the observed comparison and ratio 5,05; they do not establish the minimum padding required to reach a given on-time count. “Muốn … phải” strengthens the already overbroad v7 claim.

Replace v10:269–271 with:

> \textbf{Vai trò của từng thành phần.} Thứ nhất, ở mức kéo dài lời hứa gần bằng nhau, luật C hơn cách đệm ở ngưỡng một phút và kém ở ngưỡng hai phút: khi cùng đệm 30 giây, 2.336 so với 2.328 lượt và 2.338 so với 2.366 lượt. Ở hàng đệm 30 giây, điều phối không trần đạt cùng 2.328 lượt không trễ quá một phút như luật C có dự báo không đệm, với lời hứa dài thêm trung bình 37,18 so với 7,37 giây, tức khoảng năm lần.

### 3. Restore missing forecast cohorts — v10:124–127 and 134–136

The new count paragraph prints 66 → 2 without the different denominators of M⁺-30 (1.471) and V-30 (1.470), and drops 437/418 for the 17-hour comparison. Its EV correctly distinguishes all four populations (N4B8-02), so this is a body/EV scope mismatch, not a numeric error. The oracle-fit statement at v10:135 also drops the explicit “34 kịch bản” of v7:135 while the paragraph opens with 2/1.471 on 21 scenarios; the 2.305 oracle cohort belongs all 34 scenarios (FR:77; F10).

Replace v10:124–127 with:

> Lợi ích không riêng của luật C. Trên cùng 21 kịch bản, khi có dự báo, luật hạn chót 30 giây giảm từ 66 xuống 2 khách trễ trong 1.471 khách được phục vụ; luật trần độ dời khách thấy 30 giây cũng giảm từ 66 xuống 2 trong 1.470 khách. Điều phối không trần giảm từ 129 xuống 63 trong 1.512 khách. Riêng khung 17 giờ, 28 khách trễ trong 437 khách của điều phối không trần không đổi, còn luật C có 0 trong 418 khách. Theo sổ, 86,1\% số giây trễ của 68 khách trễ khi không dự báo thuộc phần được hồ sơ lịch sử giải thích (Hình~\ref{hinh:c4-so}); dự báo và trần nhắm vào hai phần khác nhau của sổ.

Replace the oracle sentence at v10:135–136 with:

> Trên cả 34 kịch bản, với luật C, kéo dài lời hứa theo đúng hệ số sẽ xảy ra cho giờ trả khớp trong vòng 2 giây ở cả 2.305 khách không bị điều phối dời.

### 4. Restore the aggregation label for 41,3% — v10:284–287

v7:319 said “trung bình theo kịch bản”; v10 deletes it. v10 EV:288 still correctly identifies that estimand. A reader may interpret “41,3% lượt quyết định” as the pooled decision count, which is instead 7.710/20.103 = 38,35% (Addendum 1 N-21). Do not substitute pooled numbers into the mean as if they were its numerator and denominator.

Replace v10:286–287 with:

> Theo nghĩa vụ đó, tính trung bình theo kịch bản, nó bị ép ở 41,3\% lượt quyết định và có khách bị phá lời hứa ở 28 trong 34 kịch bản, còn luật C không có (Bảng~\ref{bang:c4-nghiavu}).

If strict count-plus-denominator enforcement warrants a second metric, add a separate sentence, not a synthetic count for 41,3%:

> Tính gộp, đó là 7.710 trong 20.103 lượt quyết định.

The 47,6%/62,8% and 39,0%/11,0% passage at v10:184–186 explicitly labels scenario means and the 15 completed paired scenarios. Root owns deciding whether verified pooled counts should be added there.

### 5. English word in Vietnamese prose — v10:191–192

“theo gradient” precedes the permitted English parenthesis and violates the owner’s Vietnamese-only sentence rule. The first-use English parenthesis can stay.

Replace:

> Đó là cây quyết định tăng cường theo gradient (gradient boosting)

with:

> Đó là mô hình cây quyết định tăng cường (gradient boosting)

### 6. Disclose the recovered ML counts — v10:206–211

Accept the integers **if root confirms the rounding checks**. MLT reports percentages over the displayed exact n, not scenario-average rates; the possible-count interval has radius 0,0005 n/100 and width 0,001 n/100, at most 0,00807 here. If exactly one integer lies in that interval, count recovery is an exact arithmetic deduction from the known rounding rule, even though the source printed a rounded percentage. This is acceptable thesis evidence under the existing [A]/derived-number convention. It is not a new direct recount of riders from transcripts.

The reviser’s note that R29 declined the operation is factually a description of the previous review choice; that earlier conservatism is not a prohibition on a later validated derivation. Addendum 6’s shorthand “cận nhỏ hơn 1 nên k là duy nhất” is insufficient as a general theorem (radius < 1 is not enough); its actual radii here are far below 0,5, so the concrete count conclusions can still hold.

After “Không mô hình nào thỏa đủ bốn điều kiện.” at v10:206, add:

> Các số đếm sau được suy từ tỉ lệ gộp theo khách đã làm tròn đến ba chữ số thập phân trong bảng kết quả; với mẫu số tương ứng, mỗi tỉ lệ chỉ ứng với một số nguyên.

Then retain the reported 0/147, 0/197, 2 → 1/145, 1 → 1/200, 104 → 94/807 and 57/807 if verified. Add the saved probe anchor to EV:211 and record the percentage-rounding bound in the final review/notes. No forbidden “duy nhất” is needed in the suggested thesis wording.

## EV/rounding correction, lower severity

v10:177 has the right full-precision weekday sum 81,742 + 5.352,646 + 783,018 = 6.217,406 seconds. But its note says the displayed labels may differ by 0,1 seconds. The actual figure labels are whole seconds: 82 + 5.353 + 783 = 6.218, versus a displayed total of 6.217, a 1-second gap. The 0,1-second gap belongs the old one-decimal numbers 81,7 + 5.352,6 + 783,0 = 6.217,3 versus 6.217,4, not the drawn labels. Replace the final clause of EV:177 with:

> các nhãn làm tròn đến giây độc lập, nên tổng ba nhãn là 6.218 s, lệch 1 s so với nhãn tổng 6.217 s

This is an EV-comment error, not an incorrect figure cohort or a new substantive sum. The snow labels also round independently: 8,6 + 251,5 + 3.185,9 = 3.446,0 versus total 3.445,9; the independently rounded percentages 0,25 + 7,3 + 92,5 = 100,05%. All use the same 3.445,933-second denominator. No need to force those rounded displays to sum exactly 100%.

## Reference and forbidden-language results

- Saved `agent-regressions-ref-audit-v2.ps1` / `agent-regressions-ref-audit.txt`: all 24 visible \ref/\eqref occurrences checked against the requested latest chapter set. Every target resolves except `phuluc:C` at v10:382. All 11 v10 labels are distinct, without duplicates across the checked chapter set.
- `phuluc:C` is an outstanding assembly dependency, not a v10 regression: no definition exists in rewrite-kit .tex files or current thesis noi-dung .tex, and ASSEMBLY-NOTES:61 plus v8-NOTES:56 explicitly acknowledge it. Do not invent an appendix. Before final thesis assembly, create the evidence-backed Appendix C and its label; otherwise replace only “(Phụ lục~\ref{phuluc:C})” with an empty string until that appendix exists.
- Removed `bang:c4-haiphia` has no inbound occurrence in latest partA v4, Ch3 r33 v4-v3 or Ch2 v4. Its removal does not break their cross-references.
- No banned sealed-plan/novelty/cap-optimality wording in visible v10 body. The glossary-specific banned language is also absent on manual review. English “gradient” above is the language exception found. Source identifiers and code/hash names remain in hidden EV comments, as before.
- No new causal claim for the ledger split found. “Theo sổ”, “phần tính cho điều phối”, forecast-dependent residual and the absence of real-world validation remain. C’s 0 forced decisions are now correctly framed as an implementation check under (N) and U’s same zero is disclosed.

## Caveats retained or correctly strengthened; optional polish

The revision retains different served cohorts and 2.207 overlap, forecast replay, weekend absence of forecasts, negative ML result, paired complete-run restriction, information limitations in snow variants, retrospective design, simulation limits, low load, zero-stop sample limitation, missing cost-first simulation, missing per-revision-cap comparison, absence of business/user-value measurement and absence of an optimal cap. It correctly replaces the old unverified snow-runner caveat with the checked identity claim; this is a resolved uncertainty, not suppressed caveat. It also distinguishes capped snow decomposition from the signed ledger and restricts generator-counter coverage instead of claiming all computation limits were inactive.

Optional: the parenthetical quantile explanation at v10:191 could say “mức mà mô hình ước lượng 90\% khách có thông tin tương tự không vượt” to emphasize that this is an estimated conditional quantile, not demonstrated empirical coverage. “Ước lượng” already governs the main sentence, so this is polish, not a rejection issue.

Optional: v10:130 drops explicit “trên 21 kịch bản” from the original 13,7-second scenario-mean extension sentence; the section and immediately preceding table identify that cohort, and the 34-scenario table later labels the different pooled extension. Restoring “Trên 21 kịch bản này,” is useful but lower priority than the 2.305 scope correction.

Saved scripts create files with CreateNew. The initial UTF-8-without-BOM PowerShell script failed to parse before running; `-v2.ps1` adds a BOM and succeeds without overwriting it. No source/draft file was modified.