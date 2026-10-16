# R33 — Triage of Antigravity R27 against the current chapters (Claude, 2026-10-14)

**Input reviewed (read only):** `optimize/codex-debate/antigravity-work/R27-ANTIGRAVITY.md` (148 lines; cited below as
`R27:n`), written against the old inputs in `antigravity-work/inputs-r27/` (Ch2 v4, Ch3 v3, Ch4A v1, Ch4B v7).

**Current versions checked (read only):**

| Chapter | Current file (cited as) |
|---|---|
| Ch2 | `rewrite-2026-10/drafts/06-chuong2-v6.tex` (**C2**) |
| Ch3 | `optimize/codex-debate/codex-work/r33-ch3v4/07-chuong3-v4-v3.tex` (**C3**) |
| Ch4A | `optimize/codex-debate/codex-work/r36-ch4a-v5/08-chuong4-phanA-v5-v3.tex` (**C4A**) |
| Ch4B | `optimize/codex-debate/codex-work/r39-ch4b-v11/09-chuong4-phanB-v11-v2.tex` (**C4B**) |

Old files are cited as **O2**, **O3**, **O4A**, **O4B**. Also read: the four revision logs, the three Codex CHANGES files,
`WRITING-BRIEF.md`, `STYLE-GUIDE-VI.md` (rules 5, 6, 11, 14, 16, 20, 24, 32–34), `GLOSSARY-VI-v2.md`, the register rows
named below, and `codex-work/r37-ch4b-verify/R37-CH4B-V10-VERIFY-CODEX.md` §5 with `verify-supplement.json`.
No draft was edited. No simulation was run.

**Classes.** **AF** = ALREADY FIXED (current text resolves it). **SAC** = STILL APPLIES & CORRECT (exact replacement
given). **SABW** = STILL APPLIES BUT WRONG (misreading, wrong number or meaning, or a request the rules forbid; includes
comments whose "problem" was already handled in the very version Antigravity read). **CC** = CANNOT CHECK.
Pure praise or verified-true statements that ask for nothing are listed as **no action** and not counted.

**Sentence-length yardstick.** STYLE-GUIDE rule 5: "câu dài hơn 40 tiếng thì tách đôi"; "tiếng" = whitespace token,
sentences split at `. ! ? :` (STYLE-GUIDE line 28). Token deltas below were measured with `wc -w` on scratch copies.

## 0. Counts

| Class | Ch2 | Ch3 | Ch4 | Total |
|---|---:|---:|---:|---:|
| AF | 3 | 3 | 18 | **24** |
| SAC | 2 | 5 (one is a duplicate) | 1 | **8** (7 distinct edits) |
| SABW | 1 | 7 | 4 | **12** |
| CC | 0 | 0 | 2 | **2** |
| Total classified | 6 | 15 | 25 | **46** |
| No action (praise / verified true) | 1 | 1 | 2 | 4 |

---

## 1. Chương 2 (O2 = Ch2 v4 → C2 = Ch2 v6)

| ID | R27 | Old | Current | Class | Finding |
|---|---|---|---|---|---|
| AG2-1 | 26–29 | O2:26–28 "trong khi giữ các yêu cầu về mức dịch vụ" | C2:28–30 | **AF** | Now "tìm các tuyến xe có tổng chi phí nhỏ nhất để chở chung khách theo đặt chỗ, đồng thời giữ các ràng buộc về mức dịch vụ". Antigravity's version ("bảo đảm các tiêu chuẩn về chất lượng dịch vụ") drifts from "ràng buộc dịch vụ", the glossary term used in Bảng 2.1. |
| AG2-2 | 30–33 | O2:32–37 (RTV graph; subgroup check) | C2:34–38 | **AF** | Rewritten as two steps; subgroup sentence replaced by "các nhóm được dựng dần từ nhỏ đến lớn". Antigravity's proposal also puts a long gloss in parentheses (rule 6). |
| AG2-3 | 34–37 | O2:56–59 "số hạng mềm … miễn là mỗi lần tổng chi phí nhỏ hơn" | C2:59–62 | **AF** | "Số hạng mềm" is gone ("chỉ như một khoản chi phí cộng chung cho mọi khách"); the "miễn là…" clause was deleted as unsupported (CH2 log, R35 C5). **Antigravity's proposal is wrong twice:** it re-adds that deleted clause ("miễn là mỗi lần điều chỉnh đều làm tổng chi phí … giảm xuống"), and its gloss "(cho phép vi phạm nhưng tính thêm chi phí)" misdescribes Alonso-Mora: delay is a cost term, not a violated constraint; a hard maximum delay still applies (C2:63 EV, C2-10 tr. 4). |
| AG2-4 | 38–41 | O2:131–136 (two sentences > 45 words) | C2:138–142 | **SAC** | Still two over-long sentences: 55 and 49 tiếng. Replacement in §1.1. Antigravity's own version has errors: "giờ báo ban đầu" (the FAM baseline is a *value* of wait, detour or total delay, not a clock time; C2 keeps "giá trị báo ban đầu"); "do hãng xe" (C2 uses "do cách gán xe"); "lộ trình" for the glossary's "kế hoạch". |
| AG2-5 | 42–45 | O2:206–211 (positioning sentence, five features) | C2:211–214 | **SAC** | Partly fixed (CH2 log B2: "Bảng 2.2 cho thấy…", "không nới" moved to the next sentence). The part after the colon is still 47 tiếng and stacks three features. Replacement in §1.1. Antigravity's version adds "chi tiết" and "sổ theo dõi" (glossary term is "sổ"). |
| AG2-6 | 11–12 | Answer to "how does luật C differ from the closest work?" | C2:17–19, 211–219 | **SABW** | Two errors. (a) It says Schulz & Pfeiffer's one-sided deadline "khiến tắc đường dễ làm vỡ hạn". Their model uses given travel times (C2:191–192, "Ngoài phạm vi: thời gian đi cho trước"), and CH2 log D3/T211 rejected exactly this attribution. The 14,5% breakage is the thesis's *borrowed* 30 s deadline under measured congestion, not their method. (b) "Hörl & Zwick … chỉ phạt phần trễ trong hàm mục tiêu" omits the hard constraint on the enforced drop-off time (C2:161–163); K26 forbids using hard/soft as the difference. C2 already states the difference in one sentence at 17–19. |
| — | 88–90 | Ch2 lecturer evaluation (praise) | — | no action | Its claim that Ch2 does not over-claim DARP, RTV, dynamic insertion or ETA is consistent with C2:218–219. |

### 1.1 Replacements for C2 (SAC)

**AG2-4, C2:138–142.** Replace the whole paragraph text (keep the `% EV` line):

> Thước đo của Fielbaum và Alonso-Mora so giá trị cuối với giá trị báo ban đầu. Vì vậy, trong một ví dụ dựng tay, khách
> bị dời muộn 5 phút rồi được kéo về giờ cũ có hiệu bằng 0. Chỉ số đếm số lần tăng có ghi lần dời đó nhưng không cho biết
> độ lớn. Khóa luận kế thừa ý tách phần thay đổi do cách gán xe và kiểm soát nó trước khi quyết định. Điểm khác là ở từng
> lượt, khóa luận so giờ trả của phương án với giờ trả khi xe giữ nguyên kế hoạch, rồi cộng độ lớn phần chênh qua cả
> chuyến (mục~\ref{muc:bamoc}).

Same facts and the same 5-minute example; longest sentence now 33 tiếng.

**AG2-5, C2:211–214.** Replace only the first sentence (from "Bảng~\ref{bang:c2-dangrangbuoc} cho thấy" to
"(mục~\ref{muc:luatc})."). Keep "Phần thay đổi khi giữ nguyên kế hoạch không bị tính, và trần không được nới khi đường
đông lên." and the rest of the paragraph unchanged.

> Bảng~\ref{bang:c2-dangrangbuoc} cho thấy luật C dùng lại mốc giờ trả cập nhật của Hörl và Zwick nhưng giới hạn một
> đại lượng khác. Luật C không đặt hạn cho giờ trả mà cộng độ lớn các lần bộ điều phối dời giờ trả so với mốc đó qua cả
> chuyến. Mọi khách đã xác nhận đặt xe có cùng một trần, và phần trần đã dùng được ghi vào sổ của từng khách
> (mục~\ref{muc:luatc}).

**Budget.** Both Ch2 edits together add **+9 tiếng**. v6 is 3.358 tiếng against a cap of 3.369 (+5% over v4's 3.209;
CH2 log lines 6, 23). With the edits v6 becomes 3.367, still under the cap but with 2 tiếng to spare. Re-count at
assembly.

---

## 2. Chương 3 (O3 = Ch3 v3 → C3 = Ch3 v4-v3)

| ID | R27 | Old | Current | Class | Finding |
|---|---|---|---|---|---|
| AG3-1 | 48–51 | O3:135–136, Bảng 3.2 tiêu chí 3 "Mức dùng trần lớn nhất nhỏ nhất" | C3:145–146 (unchanged) | **SAC** | The stacked "lớn nhất nhỏ nhất" (minimise the maximum) is hard to parse. The logs fixed the *content* of this cell (CH3 log RD34 "so lần lượt từng chiều cam kết", CX22 "(khi có chiều mang trần)") but not its readability. Replacement in §2.1. **Antigravity's version is wrong in meaning:** "(nếu chiều đó có đặt trần)" limits the per-dimension comparison to capped dimensions, but X3-07 ranks all ten dimensions; the condition only switches the tier on. It also says "Ưu tiên phương án" although the criteria rank the fleet-wide selection, and it drifts terms ("mức sử dụng trần", "độ dời do điều phối"). |
| AG3-2 | 52–55 | O3:227–230 "Phần nới ở dòng 6 … không phải bảo đảm đúng hạn" | C3:237–239 (unchanged) | **SAC** | One sentence of 54 tiếng (rule 5). Replacement in §2.1. Antigravity's version replaces the defined term "kẹt" with "bế tắc" (rule 11), "giờ đón muộn nhất" with "giờ hẹn tối đa", and adds "ngoài thực tế" to a simulation statement. |
| AG3-3 | 56–59 | O3:287–291 "Bộ sinh chỉ chèn thêm không bảo đảm c ≥ 0, nhưng …" | C3:298–300 (unchanged) | **SAC** | About 60 tiếng with a long parenthesis (rules 5, 6). Replacement in §2.1. **Antigravity's version changes meaning:** "việc can thiệp ở chiều đón/trả sớm" turns "chiều sớm" (the early direction of the dispatch shift *c*) into "early pick-up/drop-off". It also keeps the long parenthesis. Its "chỉ đúng 1 mili giây" matches N-05 ("mỗi lần dời sớm hơn này đúng 1 mili giây"). |
| AG3-4 | 60–63 | O3:507–509 "mỗi giây đồng hồ chỉ đi được 1/g giây quãng đường đó" | C3:517–518 (unchanged) | **SAC** | "1/g giây quãng đường" mixes units and puzzles an outside reader. Replacement in §2.1. **Antigravity's version is wrong:** "khung giờ đường đông hơn gấp g lần" turns a ratio of travel-time factors ("chậm hơn g lần", which can be below 1) into traffic density. It also uses first-person "ta đặt" (rule 16). |
| AG3-5 | 94 | O3:467–471 (Antigravity cites 346–350) | C3:477–481; C4B:384–385 | **SABW** | The fact is right: the first part of criterion 3 saturates at 100% (A15, N-25). But the text already says so, both in the version Antigravity read and now ("tiêu chí 3 vì vậy chỉ tác dụng qua tổng phần dời theo từng chiều"). The cited lines are wrong: 346–350 is the ten-dimensions paragraph. "Ở mọi lượt" over-generalises the text's "ở các lượt đã ghi của tập kiểm tra chính". It is not a modelling defect needing a fix. Placement was settled in CH4B log D4 and L-27. |
| AG3-6 | 95 | O3:595–597 | C3:612–614 | **SABW** | "Xử lý dấu không đồng nhất" is not a flaw. The ledger identity needs signed *c* so that the three parts add up to *a − p₀*, while the rule bounds magnitudes. The text says this explicitly: "q cộng các c giữ nguyên dấu …, khác với Σ\|c\| của luật C, và dưới luật C, \|q\| ≤ Σ\|c\| ≤ B". Antigravity also numbers the ledger formula "(3.5)"; it is **(3.6)**, the sixth equation of Ch3, while (3.5) is the forecast-stretch equation `eq:keodan`. |
| AG3-7 | 96 | O3:554–556 | C3:564–566; C4B:450–451 | **SABW** | The count is right (34 of 1.471 served riders, C-30, 21 forecast scenarios). The issue is already disclosed in both places as an integration limit to fix before deployment. The framing "34 khách *nhận* giờ đón hiển thị …" is wrong: D is computed afterwards by replay (C3:562–563), so no rider in the runs received it. |
| AG3-8 | 97 | O3:356–389 | C3:366–399 | **SABW** | **Wrong reasoning.** Remark 3.1 does *not* depend on zero dwell time or on the absence of execution delay. Assumption (N) is (i) the running plan has no structural violation and (ii) the keep-route drop-off uses the same projection as *e* (C3:366–369). Under (ii), p = e by construction, so c = 0. Dwell time and execution delay change *e* and therefore *x = e − v*, which luật C does not count (C3:263–264: "x gồm … tiến độ thực của xe"; limitation 2 at C3:394–395). |
| AG3-9 | 17 | Reader point 1: risk of reading *e*, *c* as real-world quantities | C3:249–266, 601–603 | **AF** | Already explicit in the version read: "Mốc e là giờ do mô hình tính, không phải giờ đến thật" and "chỉ là phép trừ giữa các giờ của mô hình". C3 now adds a real simulated rider at 601–603. Antigravity's own gloss is consistent with this. |
| AG3-10 | 19 | Reader point 3: explain replay | C3:562–563; C4A:174–176 | **AF** | "xe nào chở ai giữ nguyên, chỉ giờ báo cho khách đổi" (C3) and "xe nào chở ai giữ nguyên, chỉ các giờ báo cho khách được tính lại" (C4A). |
| AG3-11 | 114–115 | Q1: sim-to-real gap; is Remark 3.1 still true with dwell and execution delay? | C3:366–399; C4B:423–429 | **SABW** | The sim-to-real limits (0 s dwell checked on 3 sample runs; one citywide factor) are true and disclosed at C4B:423–427. The status "CHƯA TRẢ LỜI ĐƯỢC / CÒN SƠ HỞ" is wrong for the same reason as AG3-8: the remark holds by construction regardless of dwell and delay. Those affect *x* and lateness, which the thesis does not claim luật C bounds. |
| AG3-12 | 126–127 | Q7: why keep a criterion that is "always 100%"; does it affect CP-SAT? | C3:477–481 | **SABW** | It contradicts Antigravity's own R27:94 ("vô hiệu hóa *một nửa*"). Only the first part saturates; the per-dimension dispatch-shift sums still rank the selections (A15 note; C3:479). Calling it "LỖ HỔNG THIẾT KẾ / CHƯA TRẢ LỜI" ignores the existing text. |
| AG3-13 | 128–129 | Q8: "34 khách bị đón muộn" | C3:564–566; C4B:450–451 | **SABW** | **Wrong meaning.** No rider was picked up late because of this. The *replayed displayed* pickup time of the forecast promise exceeds the latest pickup time for 34 of 1.471 riders; the runs used the non-forecast promise. The status "đã thừa nhận, chưa sửa" is correct. |
| AG3-14 | 143 | Part 3 row 3: add an intuitive v/e/p explanation "ở Chương 3.3 và 4.3" | C3:249–266, 601–603 | **AF** | Already present (see AG3-9). The section number is wrong: v/e/p are in §3.2 (`muc:bamoc`); §3.3 is luật C. |
| AG3-15 | 145 | Part 3 row 5: rewrite the criterion-3 definition and "thừa nhận hạn chế ở Chương 3.2" | C3:145–146; 477–481 | **SAC (duplicate of AG3-1)** | The rewrite part is AG3-1. The admission already exists, in §3.4 (C3:477–481), not in "Chương 3.2". Not counted as a separate edit. |
| — | 91–92 | Ch3 lecturer: method clear and reproducible at a high level | — | no action | — |

### 2.1 Replacements for C3 (SAC)

**AG3-1, C3:145–146 (Bảng 3.2, row "Tiêu chí 3").** Replace the row:

> `Tiêu chí 3 & Mức dùng trần lớn nhất trên đội xe càng nhỏ càng tốt; nếu hòa, tổng phần dời do điều phối nhỏ nhất,`
> `so lần lượt từng chiều cam kết (khi có chiều mang trần) & Ưu tiên ổn định\\`

"Trên đội xe" makes the maximum's scope explicit, as in X3-07 ("mức dùng trần lớn nhất trên đội xe (cực tiểu của cực
đại)") and CH3 log RD53. The logged wording "so lần lượt từng chiều cam kết" and "(khi có chiều mang trần)" is kept as
is. Change: +5 tiếng.

**AG3-2, C3:237–239.** Replace the sentence "Phần nới ở dòng 6 … không phải bảo đảm đúng hạn." with:

> Phần nới ở dòng 6 giúp xe không kẹt vì tắc đường. Mỗi lần vượt như vậy, và mỗi lần khách thực tế lên xe muộn hơn giờ
> đón muộn nhất, được ghi lại thay vì làm dừng lần chạy. Vì vậy cửa sổ đón là điều kiện để kiểm phương án, không phải
> bảo đảm đón đúng hạn.

Change: +5 tiếng; longest sentence 28 tiếng.

**AG3-3, C3:298–300.** Replace from "Bộ sinh chỉ chèn thêm không bảo đảm $c \ge 0$, nhưng" (line 298) to the end of line
300. Keep line 297 and the start of 298 up to "chỉ tính phần bất lợi." unchanged.

> Bộ sinh chỉ chèn thêm không bảo đảm $c \ge 0$. Trên tập kiểm tra chính, khóa luận đã kiểm 136 lần chạy của bốn cấu
> hình: điều phối không trần, luật C trần 30 và 120 giây, luật hạn chót 30 giây. Ở các lần chạy này, mỗi lần kéo giờ trả
> sớm hơn $e$ chỉ sớm 1 mili giây, nên chiều sớm chưa cho thấy tác dụng đáng kể.

Source: N-05 (U 2/174, C-30 4/33, C-120 3/103, M⁺-30 4/29 on 34 scenarios, each early step exactly 1 ms; 4 × 34 = 136
runs). Change: +7 tiếng.

**AG3-4, C3:517–518.** Replace the first sentence ("Theo tốc độ lúc công bố, … quãng đường đó.") with:

> Theo tốc độ lúc công bố, xe cần thêm $p - t$ giây. Trong khung chậm hơn khung hiện tại $g$ lần, mỗi giây đồng hồ chỉ
> đi được phần đường mà ở tốc độ lúc công bố mất $1/g$ giây.

Same meaning as `eq:keodan` (∫dτ/g = p − t). The worked example at C3:520–524 (g = 1,2; 600 s → 720 s) still reads
correctly after it. Change: +5 tiếng.

---

## 3. Chương 4 (O4A = Ch4A v1 → C4A = v5-v3; O4B = Ch4B v7 → C4B = v11-v2)

Table numbering. Old: 4.5 `c4-chinh`, 4.7 `c4-phanbotre`, 4.13 `c4-congdon`, 4.14 `c4-sangloc`, 4.15 `c4-dubao`.
Current (the old 4.8 `c4-ngaykhung` was removed): 4.5 `c4-chinh`, 4.7 `c4-phanbotre`, 4.12 `c4-congdon`, 4.13
`c4-sangloc`, 4.14 `c4-dubao`, 4.15 `c4-dem`. Antigravity's table numbers were correct for the old files.

| ID | R27 | Old | Current | Class | Finding |
|---|---|---|---|---|---|
| AG4-1 | 66–69 | O4A:269–271 (2.207 riders: waited 0,5 s longer, rode 10,5 s less) | C4A:297–300 | **AF** | The sentence was cut (C4A:300 EV: "câu về chờ, ngồi xe của khách chung, C05, cắt vì ngân sách trang"). Antigravity's numbers match C05 (+0,522 s; −10,507 s). |
| AG4-2 | 70–73 | O4A:477–483 ("dừng ở lỗi gặp trước"; 59 requests) | C4A:470–474; C3:356–360 and Bảng 3.4 line 5 | **AF** | Now two short sentences: "Không thể kết luận 59 yêu cầu đó sẽ được phục vụ: bộ kiểm dừng ở khách vi phạm gặp trước, và khi trần đổi thì các quyết định trước cũng đổi." The consequence (each blocking record names only the first violating rider) is defined at C3:358–360. Antigravity's version uses "chạm trần thời gian" (wrong term: the cap is on the dispatch shift) and a long parenthesis. |
| AG4-3 | 74–77 | O4B:69–73 ("trên quỹ đạo") | C4B:19–21, 72–73; limitation C4B:459 | **AF** | Now "khi cả lần chạy đi theo lựa chọn mới" (CH4B log B15) and "chưa được chạy thành lần mô phỏng đầy đủ". **Antigravity's version breaks two rules:** "bằng chứng *duy nhất*" (forbidden word: WRITING-BRIEF, STYLE rule 34), and "khi xe chạy động theo thời gian thực" (the runs are simulations, not real time). |
| AG4-4 | 78–81 | O4B:218–221 (padding opening sentence) | C4B:226–227 | **SAC** | Still one sentence of 48 tiếng with six numbers. Replacement in §3.1. **Antigravity's version is wrong:** first-person "ta" (rule 16); evaluative "Thậm chí … vượt qua" (rules 14, 34); undefined "kịp giờ" instead of "không trễ quá hai phút"; a parenthesis "(trên 3.672 yêu cầu)" (rule 6); and it drops "có dự báo" after "luật C trần 30 giây", which v11 added deliberately. Without forecast, luật C has 2.262, not 2.328. |
| AG4-5 | 13–14 | Answer: why luật C if a 30 s pad gives as many on-time riders | C4B:226–232 | **AF** | v11 opens 4.8 with this answer, worded correctly ("dưới giả thiết (N)"; 29,2 s maximum including weekends; −96 served). Antigravity's numbers are right (44; 174; 590,1 s; 37,18/7,37 = 5,05, N-18). But "làm lời hứa dài thêm gấp 5 lần" reads as "the promise becomes five times longer", while it is the *extension* (37,18 vs 7,37 s) that is five times larger on promises of about 14 minutes (C4A:162–164). |
| AG4-6 | 18 | Reader point 2: deadline rule "phá hứa 14,5%, bị ép 41,3%" while lateness is equal (74 vs 76) | C4A:355–359 | **AF** | C4A now measures luật C with the deadline rule's own yardstick: 292 vs 289 of 2.338 riders late by more than 30 s, in 28 of 34 scenarios each, and states the reason. Numbers: 14,5% and 41,3% are the old *scenario averages* (O4A Table 4.6). C4A Table 4.6 now gives pooled counts, 289/2.338 (12,4%) and 7.710/20.103 (38,4%); 41,3% survives only at C4B:297, labelled "trung bình theo kịch bản". **Error:** "số khách trễ thực tế ngoài đời". These are simulated riders. |
| AG4-7 | 20 | Reader point 4: cumulative clause almost never decisive | C4A:708–711, 772–776; C4B:459–461 | **AF** (paraphrase wrong) | The point is already stated. **Two paraphrase errors:** (a) "mọi phương án bị chặn đều vượt 30 giây ngay trong một lần dời" for all 98 runs. The 98 runs cover caps of 30–300 s, and each record exceeds *its own configuration's* cap (C4A:709–710). (b) "chỉ khi nới trần lên 120 giây mới xuất hiện 3 bản ghi" is false as a general statement. The morning set at 120 s has 0 such records (Table 4.12, row 64 runs). The fixed-traffic set has 2 at 60 s and 4 at 120 s, and the synthetic sweep has 4 at 120 s (C4A:766–769). It also writes "98 lần chạy *cũ*", copying an old label that C4A:709 removed. |
| AG4-8 | 21 | Reader point 5: sets and aggregation switch | C4A:112–140 (Bảng 4.3), 168–172 | **AF** | The four sets are tabulated, and C4A:168–172 now explains "gộp theo khách" against "trung bình theo kịch bản" with a worked example. Antigravity's "Chiều tuyết … 601 khách" copied the old table's unit mix (O4A:130 "601 lượt phục vụ"). C4A:135 now reads "8 kịch bản, 864 yêu cầu". |
| AG4-9 | 102 | Error 1: "Điều này đúng theo cấu tạo … luôn qua luật C" is an over-claim | C4A:339–344; Table 4.6 caption C4A:312–313; C4B:373–375 | **AF** (reason wrong) | Now conditional: "nếu giả thiết (N) đúng ở lượt đang xét và … 0 ≤ L_r ≤ B …; nhận xét không bảo đảm giờ trả thực tế". The justification Antigravity gave (dwell time, execution delay) is wrong; see AG3-8. |
| AG4-10 | 103 | Error 2: "+31 = −96 − (−127)" suggests causal offsetting | C4A:297–299 | **AF** (old text already guarded it) | Now "127 − 96 = 31", followed by "Vì vậy 31 là chênh lệch hai tổng, không phải 31 khách cụ thể được đưa tới đúng giờ". The same caveat already followed the equation in O4A:267–269; Antigravity overlooked it. |
| AG4-11 | 105 | Error 3a: Table 4.5 shared riders, U 555 vs C-30 313, "không tách bạch phần giảm do luật C từ chối bớt khách" | C4A:275–277, 290–294 | **SABW** | The thesis also gives the drop as a *rate* per served rider (22,8% → 13,4%, gộp theo khách), which already corrects for the smaller served set. Even if all 96 lost rides had been shared riders, 146 of the 242 fewer shared riders would remain. No causal mechanism is claimed ("không có bằng chứng về giá trị…"). The "network density" mechanism is Antigravity's untested hypothesis. |
| AG4-12 | 106 | Error 3b: Table 4.7 maximum lateness (11 vs 3,87 min) may reflect selection; analyse the 2.207 shared riders | C4A:365–393; C4B:408–410 | **CC** | No saved output gives maximum (or binned) lateness *without forecast* on the 2.207 intersection. The closest evidence is R37 §5 (`verify-supplement.json:common_served_cohort`): with forecast, on the same 2.207 riders, U + 30 s pad has 94/59 late by more than 60/120 s and C-30 has 9/0. So in that comparison the gap does not vanish on shared riders. R39 CHANGES-v2:100 decided not to add that probe to the body. The text already labels Table 4.7 "trên hai nhóm khách khác nhau" (C4B:409–410). Current values: 660,1 s and 232,3 s (C4A-14). |
| AG4-13 | 107 | Error 3c: Table 4.14 compares cost reduction on two diverged state sets | C4B:32–35 (caption), 67–69 | **SABW** | Already stated in the version Antigravity read (O4B:31–32 caption; O4B:64–65) and now: "hai cột là hai tập tình huống khác nhau … chỉ gợi ý". |
| AG4-14 | 109 | No forbidden words | all four current files | no action (verified) | Confirmed by grep on body text (comments excluded) of all eight old and current files: no "niêm phong", "tiền đăng ký", "dự đoán trước", "duy nhất", "đầu tiên", "vượt trội", "đột phá", "tối ưu", "chúng tôi", "hóa ra", "đáng chú ý". Antigravity's own AG4-3 proposal introduces "duy nhất". |
| AG4-15 | 110 | Error 4: delete or fill "chưa đưa vào bảng" (Table 4.5) and "chưa đo" (Table 4.15) | C4A:279–280; C4B:105–106 | **AF** | Table 4.5 rows M⁺-60 and V-30 are now filled (79/2.268/2.336 and 74/2.262/2.325; C4A-02). Only the shared-rider cell says "chưa đếm" (CH4A log #3, D30). The old "chưa đo" cell was measured and is 0 (CH4B log D1; N4B8-08). The "loại bỏ các dòng" option would break STYLE rule 20: "Ô chưa đo ghi 'chưa đo' hoặc 'không áp dụng', không ghi 0". |
| AG4-16 | 116–117 | Q2: economics; "giảm 43,6% khách đi chung … chỉ để giảm trễ cho 127 khách" | C4A:290–299; C4B:413–416 | **SABW** | The arithmetic is right: 242/555 = 43,6% (Antigravity's own figure; the thesis uses 22,8% → 13,4% gộp theo khách). **Wrong meaning:** "giảm trễ cho 127 khách". 127 = 203 − 76 is a difference of two pooled totals over different served sets (C04: 2.207 shared, 227 U-only, 131 C-only). The thesis forbids reading it as specific riders (C4A:297–299). "Phá sản mô hình kinh doanh" is rhetoric. The status "trả lời một phần, chưa có k và m" is correct (C4B:413–416). |
| AG4-17 | 118–119 | Q3: padding vs luật C | C4B:226–232, 279–293 | **AF** | Numbers right (2.328; 96; 590,1 s; 44; 1 rider later than 600 s with U + pad 30, N-01). Its status "đã trả lời rất tốt" agrees. "Tới sớm vô ích" is evaluative wording that must not be reused. |
| AG4-18 | 120–121 | Q4: ledger split is accounting, not causation | C3:263–265, 621–625; C4A:442–444 | **AF** | Status correct. Its wording "điều phối chỉ *đóng góp* 1,2%" is the causal phrasing STYLE rule 33 forbids. The thesis writes "phần tính cho điều phối bằng". |
| AG4-19 | 122–123 | Q5: is the cumulative clause useless; per-step rule not run | C4A:708–711, 772–776; C4B:459–461 | **AF** | Numbers right (140 runs; 3 records at C-120; 0 at C-30). Status correct: the per-step rule "chưa được cài đặt và chưa chạy". |
| AG4-20 | 124–125 | Q6: selection bias in maximum lateness; "chưa phân tích trên 2.207 khách chung" | as AG4-12 | **CC** | As AG4-12. Its claim that nothing was analysed on the 2.207 riders is partly outdated: R37 §5 did analyse them, but for the forecast + pad comparison only. |
| AG4-21 | 130–131 | Q9: fairness to Schulz & Pfeiffer (900 s vs 30 s) | C4A:252–254; C3:442–445; C4B:462–464 | **AF** | Status correct; 900 s right. |
| AG4-22 | 132–133 | Q10: cap or selector? cost-first not run | C4B:18–21, 72–73, 459–461 | **AF** | Status correct. |
| AG4-23 | 141 | Part 3 row 1: put the padding answer at the top of 4.8 | C4B:226–232 | **AF** | Done in v11. Do not import "gấp 5 lần" (ambiguous) or "vô ích". |
| AG4-24 | 142 | Part 3 row 2: state in 4.5 and 4.11 that "trên thực nghiệm trần từng bước đã đủ chặn phần lớn" | C4A:708–711, 772–776; C4B:459–461 | **SABW** | The substance (cumulative-only records are rare) is already stated. The proposed wording claims a per-step rule *would* suffice, but that rule was never implemented or run (E09, K08; C4A:775–776 "Phép tính thử không cho biết kết quả nếu chạy thật với luật kia"). It is an over-claim. |
| AG4-25 | 144 | Part 3 row 4: cautionary notes under Tables 4.5 and 4.7 | C4A:297–299; C4B:235–236, 409–410 | **AF** | Both notes exist: the different served sets for Table 4.5's comparison, and "trên hai nhóm khách khác nhau (Bảng 4.7)". |
| AG4-26 | 146 | Part 3 row 6: draft table cells | as AG4-15 | **AF** | Duplicate of AG4-15. |
| — | 98–99 | Ch4 lecturer praise | — | no action | — |

### 3.1 Replacement for C4B (SAC)

**AG4-4, C4B:226–227.** Replace the first sentence, from "Khi có dự báo, cộng thêm 30 giây" to "là 2.366 so với
2.338.". Keep "Hai cách này cho hai thứ khác nhau." and everything after it unchanged.

> Khi có dự báo, cộng thêm 30 giây vào mọi lời hứa của điều phối không trần cũng cho 2.328 lượt không trễ quá một phút
> trên 3.672 yêu cầu, bằng luật C trần 30 giây có dự báo. Ở ngưỡng hai phút, cách đệm này cho 2.366 lượt, so với 2.338
> của luật C.

Sources: C10, N-16. The first sentence is now 39 tiếng and compares two rules on one metric (rule 5 exception). Change:
+7 tiếng.

---

## 4. Every number Antigravity wrote, checked against the source

| R27 line(s) | Number(s) as written | Source | Verdict |
|---|---|---|---|
| 14, 119, 141 | 30 s pad; 44 riders early by more than 1 min; 174 riders shifted; 590,1 s; "gấp 5 lần" | C10, N-02, C20, N-23, N-18 (37,1833/7,3671 = 5,05) | Correct. "Gấp 5 lần" is attached to the wrong noun (AG4-5). |
| 18 | 14,5%; 41,3%; 0%; 74 vs 76 | O4A Table 4.6 (scenario averages); C06; C4A:277 | Correct for the old file. Now pooled: 289/2.338 (12,4%) and 7.710/20.103 (38,4%). |
| 20 | 98 runs; "vượt 30 giây"; "chỉ khi … 120 giây"; 3 records | E01, N-08, E03, E04 | 98 and 3 are correct; the other two phrases are wrong (AG4-7). |
| 21 | 34/3.672; 8/864; 16/1.728; 8/601 | B09, B15, B17, N-26 | Correct. 601 is *served riders*; the snow set has 864 requests. |
| 32, 36, 40, 44, 58 | "43 từ", "> 45 từ", "52 từ", "56 từ" | — | Undefined unit. Claude R30 counted 58 tiếng for the sentence Antigravity put at 52 (CH2 log B2). Not material. |
| 57, 59 | 4 configurations, 30/120/30 s, 136 runs, 1 ms | N-05; C3:298–300 | Correct. |
| 67, 69 | 2.207; 0,5 s; 10,5 s | C04, C05 | Correct. |
| 71, 73 | 59 requests | D14 | Correct. |
| 79, 81 | 2.328; 3.672; 2.366; 2.338; 37,2 s; 7,4 s | C10, N-16, N-18 | Correct. The proposal drops "có dự báo" (AG4-4). |
| 94 | 100%; cited O3:346–350 | A15, N-25; O3:467–471 | Value right; **line cite wrong**; "ở mọi lượt" over-generalised. |
| 95 | "công thức Sổ cái (3.5)" | O3 equations, in order: eq:chon, bamoc, luatc, dongnhat, keodan, so | **Wrong.** The ledger is (3.6); (3.5) is the forecast stretch. |
| 96, 128 | 34 riders; O3:554–556 | F07 | Count and cite right. "Bị đón muộn" is wrong (AG3-13). |
| 102, 103 | O4A:308–310; O4A:265–266; +31 = −96 − (−127) | — | Quotes and cites right. |
| 105 | Table 4.5: U 555, C-30 313 | N-09 | Correct. |
| 106, 124 | Table 4.7: 11 min vs 3,87 min; 2.207 | C26, C4A-14 (660,1 s / 232,3 s), C04 | Correct for the old file; current values are in seconds. |
| 110 | Two "chưa đưa vào bảng" cells (Table 4.5); one "chưa đo" cell (Table 4.15) | O4A:247–248; O4B:107 | Correct for the old files; both fixed now. |
| 114 | Dwell 0 s; 15-minute factor; Nhận xét 3.1 | B05, B06; C4A:90–92 | Correct. The inference drawn from it is wrong (AG3-8). |
| 116 | 96; 43,6%; 555 → 313; 127; k > 0,756m | C02, N-09, C06, C29 | All correct as numbers (242/555 = 0,4360; 96/127 = 0,756). "Giảm trễ cho 127 khách" is wrong (AG4-16). |
| 118 | 2.328; 96 | C10, C02 | Correct ("lượt", not "khách"). |
| 119 | 590 s; "trễ trên 10 phút" | C20, N-01 (1 rider later than 600 s, U + pad 30) | Correct. |
| 120 | 1,2% vs 73,4% | C24 | Correct. "Đóng góp" is a causal word (AG4-18). |
| 122, 142 | Table 4.13; 140 runs; 3 at C-120; 0 at C-30 | N-15, N-08, E01 | Correct (old numbering; now Table 4.12). |
| 130 | 900 s; 30 s | J10, J11 | Correct. |
| 133 | 34 main scenarios | B09 | Correct. |
| 143, 145 | "Chương 3.3", "Chương 4.3", "Chương 3.2"; "Mục 4.5, 4.11, 4.8" | C3/C4 section order | v/e/p are in §3.2, not 3.3. Criterion 3 is in Bảng 3.2 (in §3.1), and its admission is in §3.4. The 4.x section numbers are right. |

**Conclusion on numbers.** Every number Antigravity *copied* matches the source. Its errors are in what it attached
the numbers to: "127 khách", "34 khách bị đón muộn", "gấp 5 lần" lời hứa, "vượt 30 giây" over 30–300 s caps. They are
also in its own labels and references: "(3.5)", "346–350", "Chương 3.3".

---

## 5. Antigravity's worst errors

1. **Remark 3.1 (keep-route always passes luật C) "depends on dwell = 0 and no execution delay"** (R27:97, 102, 114).
   False. Under (N)(ii), p = e by construction, so c = 0. Dwell time and execution delay move *e*, and therefore *x*,
   which luật C does not count (C3:263–264, 366–399). On that basis it labels an answered point "CHƯA TRẢ LỜI / CÒN SƠ
   HỞ".
2. **"34 khách bị đón muộn"** (R27:128). Nobody was picked up late because of this. It is the *replayed displayed*
   pickup time of the forecast promise that exceeds the latest pickup time for 34 of 1.471 riders (C3:562–566).
3. **"Giảm trễ cho 127 khách"** (R27:116). 127 is a difference of two pooled totals on different rider sets, exactly
   the reading the thesis rules out at C4A:297–299.
4. **Cumulative-clause paraphrase** (R27:20, 142). It says every block in the 98 runs "vượt 30 giây" (the caps are
   30–300 s, each record against its own cap). It says the 3 cumulative-only records appear "chỉ khi nới trần lên 120
   giây" (false: 0 on the morning set at 120 s; 2 at 60 s on the fixed-traffic set). It then recommends writing that a
   per-step cap "đã đủ", a rule never implemented or run.
5. **Proposed rewrites that break owner rules or change meaning:**
   - the forbidden word "bằng chứng *duy nhất*" (AG4-3);
   - first-person "ta" (AG3-4, AG4-4);
   - simulation called "thời gian thực", "ngoài thực tế", "ngoài đời" (AG4-3, AG3-2, AG4-6);
   - a defined term replaced ("bế tắc" for "kẹt");
   - meaning changed: "chiều đón/trả sớm" for "chiều sớm", "đường đông hơn gấp g lần" for "chậm hơn g lần", "(nếu
     chiều đó có đặt trần)" restricting the selector comparison;
   - in Ch2, re-adding the unsupported clause "miễn là mỗi lần … tổng chi phí giảm", which R35 removed (AG2-3).
6. **Mis-attribution to related work** (R27:12). It says congestion breaks Schulz & Pfeiffer's deadlines, although
   their model uses given travel times; CH2 log D3/T211 had already rejected this. It reduces Hörl & Zwick to "chỉ
   phạt", omitting the hard enforced-time constraint (K26).
7. **Asking to delete "chưa đo" cells** (R27:110, 146). This is contrary to STYLE rule 20. The cells are now filled or
   deliberately kept as "chưa đếm".
8. **Wrong references:** ledger "(3.5)" (it is 3.6); O3:346–350 for the 100% statement (it is 467–471); "Chương 3.3"
   for v/e/p (it is §3.2); and "ở mọi lượt" for a scope that the text limits to "các lượt đã ghi".

---

## 6. Ready to apply at assembly: STILL APPLIES & CORRECT, per current file

Apply each change as a text substitution on the current file. Line numbers refer to the files as they stand on
2026-10-14. Replacement texts are in §1.1, §2.1 and §3.1.

**`rewrite-2026-10/drafts/06-chuong2-v6.tex`** (Ch2 budget: +9 tiếng → 3.367 of the 3.369 cap; re-count)
1. **AG2-4, lines 138–142.** Split the Fielbaum–Alonso-Mora paragraph (55 + 49 tiếng) into five sentences; same
   example and facts.
2. **AG2-5, lines 211–214.** Split "Bảng 2.2 cho thấy luật C … (mục~\ref{muc:luatc})." into three sentences; keep the
   next sentence as is.

**`optimize/codex-debate/codex-work/r33-ch3v4/07-chuong3-v4-v3.tex`**
3. **AG3-1, lines 145–146.** Bảng 3.2, tiêu chí 3: "Mức dùng trần lớn nhất trên đội xe càng nhỏ càng tốt; …"
   (+5 tiếng).
4. **AG3-2, lines 237–239.** Split the "Phần nới ở dòng 6 …" sentence (54 tiếng) into three (+5 tiếng).
5. **AG3-3, lines 298–300.** Split "Bộ sinh chỉ chèn thêm không bảo đảm c ≥ 0, nhưng …" and remove the long
   parenthesis (+7 tiếng).
6. **AG3-4, lines 517–518.** Replace "mỗi giây đồng hồ chỉ đi được 1/g giây quãng đường đó" with the two-sentence
   version (+5 tiếng).

**`optimize/codex-debate/codex-work/r36-ch4a-v5/08-chuong4-phanA-v5-v3.tex`**: no edit.

**`optimize/codex-debate/codex-work/r39-ch4b-v11/09-chuong4-phanB-v11-v2.tex`**
7. **AG4-4, lines 226–227.** Split the 4.8 opening sentence (48 tiếng, six numbers) at "; ở ngưỡng hai phút" (+7 tiếng).

The AG3-15 duplicate is covered by item 3. No CC item should be acted on without new saved output; the related R37 §5
probe is optional and was declined at R39 (CHANGES-v2:100).

*End of R33 triage. Written by Claude, 2026-10-14. Only this file was created.*
