# Kiểm toán cấu trúc và khả năng đọc

Ngày đọc: 04/10/2026. Nguồn gốc giữ nguyên tại `E:/Code/Report_INT3508/ridebound`.

## Phạm vi đã đọc

Đã đọc trọn `main.tex`, toàn bộ 11 tệp `noi-dung/*.tex`, yêu cầu f8bac của người dùng và báo cáo `tang3/w07x/W07X-REPORT.md`, `tang3/t38/T38-REPORT.md`. Vòng đọc hoàn tất trước khi chỉnh sửa. PDF gốc có **105 trang**, xác nhận bằng pypdf. Dữ liệu ở báo cáo mới chỉ được dùng sau kiểm toán số liệu của nhánh phụ trách bằng chứng.

Đã đọc trực tiếp Nature Skills `nature-reader`, `nature-writing`, `nature-polishing`, `nature-shared`, manifests và các tài nguyên lõi về grounding, reader workflow, taxonomy, ethics, terminology, stance, writing workflow, output format, failure modes, main-text discipline, discussion argument, consistency và LaTeX layout. Đây là hướng dẫn biên tập, không phải nguồn bằng chứng. Cấu hình áp dụng: bản thảo thuật toán/hệ thống, thể loại khóa luận, tiếng Việt theo yêu cầu người dùng; không nhập các giới hạn của tạp chí Nature.

## Chẩn đoán chính

Nội dung gốc đã có bằng chứng mạnh và tự phê bình quan trọng, nhưng tổ chức theo các lớp bổ sung khiến kết quả được chứng minh, nhắc lại và giải thích lại nhiều lần. Chương 4 chiếm 46 trang, còn kết luận 7 trang; Chương 1 có 9 trang và kể gần toàn bộ kết quả trước Methods. Rút gọn nên nhắm vào sự lặp lại, câu diễn giải và nhật ký triển khai; không bỏ giới hạn có tác dụng thay đổi cách đọc kết quả.

Phân bố PDF gốc: trước chương 1 có 16 trang; Chương 1 trang vật lý 17–25 (9 trang); Chương 2 26–31 (6); Chương 3 32–48 (17); Chương 4 49–94 (46); Chương 5 95–101 (7); tài liệu tham khảo 102–105 (4). Trang 102 chỉ có tiêu đề tài liệu tham khảo, tiếp theo lại có tiêu đề tiếng Anh “Bibliography”; bỏ tiêu đề đôi để tránh một trang rỗng.

Có **48 bảng và 2 hình được đánh số**, cộng 2 longtable ký hiệu không đánh số. Chương 4 có 41 bảng và 1 hình, Chương 3 có 6 bảng và 1 hình, Chương 2 có 1 bảng. Tệp `inventory.csv` ghi quyết định cho từng display. Những con số này đếm môi trường thật, không đếm lời nhắc trong mục lục.

## Xương sống và ngân sách trang

Mệnh đề một câu: khóa luận cài đặt một sổ cái giới hạn phần dịch chuyển do quyết định so với phép chiếu tuyến giữ nguyên, đánh giá giá phục vụ phải trả và điều kiện mà các họ cổng khác phải phục hồi dưới thời gian đi thay đổi; bảo đảm hành vi không đồng nghĩa bảo đảm giờ khách thấy.

| Phần | Câu hỏi người đọc | Nội dung cần giữ | Ngân sách |
|---|---|---|---:|
| Đầu luận văn | Đề tài và kết quả là gì? | Bìa theo mẫu, cảm ơn ngắn có thể xác minh, tóm tắt VN 250–400 từ, EN nếu mẫu yêu cầu, mục lục, danh sách hình/bảng gọn, ký hiệu thiết yếu | 9 |
| Chương 1: Đặt vấn đề | Vì sao cần giới hạn lời hứa và nghiên cứu hỏi gì? | Một ví dụ dời ETA; tầm quan trọng được nguồn hỗ trợ; 3 RQ; 2–3 đóng góp có biên; phạm vi | 6 |
| Chương 2: Công trình liên quan và nền tảng | Literature đã bảo vệ lời hứa đến đâu? | Bài toán DARP/RTV ngắn; đo chuỗi và hai đầu; nhóm cơ chế bảo đảm; Fielbaum, Elmi, Schulz; bảng ranh giới đúng mức | 7 |
| Chương 3: Phương pháp | Đo gì, kiểm gì và bảo đảm nào được chứng minh? | v/e/p, sổ cái, bốn cổng, no-op và N, chuỗi bất đẳng thức, định lý với chứng minh, H và phản ví dụ sửa có lợi, cài đặt/chứng cứ/recovery | 14–15 |
| Chương 4: Thực nghiệm | Evidence trả lời ba RQ đến đâu? | Thiết kế và mức bằng chứng; attribution và đuôi; trade-off; bốn cổng dưới drift; recovery; W07X; T38 kiểm tra giữ lại và khoảng dự phòng; giới hạn/negative evidence | 28–29 |
| Chương 5: Kết luận | Ta biết gì, áp dụng thế nào, còn thiếu gì? | Ba câu trả lời tổng hợp; ranh giới; 3 việc tiếp theo gắn với uncertainty | 4 |
| Tham khảo | Bằng chứng bên ngoài ở đâu? | Chỉ các nguồn có trích dẫn và metadata/entailment đã kiểm | 3–4 |
| **Tổng** | | | **71–74** |

Cho phép 2–3 trang dao động vì floats/công thức nhưng giữ hard limit 80. Không làm nhỏ chữ hoặc khoảng cách dòng. Mức mục tiêu 72–78 tương thích với ngân sách trên sau render. Front matter 9 trang giả định mục lục 2 trang, danh sách hình/bảng cùng một trang, tóm tắt mỗi ngôn ngữ 1 trang và ký hiệu 1 trang; không ép bằng font nhỏ.

### Outline đề xuất

1. Chương 1: vấn đề lời hứa động; giới hạn của metric dịch vụ; câu hỏi RQ1 accounting/cưỡng chế, RQ2 trade-off, RQ3 drift/khả thi/phục hồi; đóng góp và phạm vi; lộ trình 1 đoạn. Không kể các số 98/102, 31/32, 40/40, 24%, 7,3% ở đây.
2. Chương 2: bài toán và kiến trúc lựa chọn; metric endpoint/chuỗi và objective mềm; các nhóm bảo đảm (ratchet, hạn chót, lựa chọn người được bảo đảm); ranh giới với nguồn 2026; gap hẹp. Xóa mục pháp lý và phần giá tiền chưa kiểm chứng. MRP/online control chỉ giữ đoạn nếu giải thích công thức hiện tại, không cần bảng riêng.
3. Chương 3: pipeline; lời hứa/lifecycle và ba mốc; signed identity và absolute inequality; sổ cái và certificate; 4 gates; N/no-op và theorem; monotone insertion và beneficial-repair counterexample; recovery(a)/(b) và non-normal certificate; triển khai/versioned runner/provenance. Chỉ định nghĩa một lần, không chứa bảng kết quả thực nghiệm dài.
4. Chương 4: (4.1) thiết kế/phân loại bằng chứng và tái lập; (4.2) RQ1 accounting, ratio 89,06/1,37 và đuôi burden; (4.3) RQ2 trade-off, service gate âm, window robustness và sensitivity; (4.4) RQ3 cơ chế no-op và bốn họ dưới drift, phân loại commitment/physical, prediction accuracy; (4.5) phục hồi và giới hạn lời hứa, W07/W07X; (4.6) T38 trên 34 episode kiểm tra, chi phí so U, khoảng dự phòng và giới hạn coverage; (4.7) validity/negative evidence gọn. Không trình bày như lịch sử thử các nhánh.
5. Chương 5: trả lời ba RQ bằng tổng hợp; ý nghĩa thiết kế và ranh giới; giới hạn còn lại; ba bước tiếp theo có phép thử rõ. Không sao chép từng bảng hay giới thiệu số mới.

## Redundancy map

| Nội dung lặp | Vị trí gốc | Nơi có thẩm quyền trong bản mới | Biên tập |
|---|---|---|---|
| Fielbaum metric “không thể thành ràng buộc” | Ch1 1.3/1.4, Ch2 2.2.2, Ch5 5.1/5.4 | Ch2 | Chỉ nói metric thực tế là hồi cứu; chính họ có kiểm soát ex ante. Không dựng novelty trên cáo buộc bất khả thi của prior work. |
| 89,06%, 1,37%, -7,13pp | Abstract, Ch1, Ch3, Ch4, Ch5 | Ch4 exact report; Abstract 1 câu | Introduction giới thiệu câu hỏi; Conclusion dùng evidence tổng hợp, không diễn giải đầy đủ lại. |
| Bốn họ, an toàn no-op, N | Ch1 1.3 và dài ở1.4; Ch3 nhiều đoạn sau proof; Ch4 nhiều interpretation boxes; Ch5 | Ch3 theorem và Ch4 đối chiếu | Một proof chung, một giới hạn N rõ; giữ distinction “no-op không bị commitment loại” và “hệ thống không dừng”. |
| H và độ khít | Ch3 3.5.3/3.5.4; Ch4 4.2.5; Ch1/Ch5 kể các count | Ch3 hypothesis, Ch4 diagnostic gọn | Gộp bảng khít và H; không gọi tỷ lệ 99,58% proof mạnh vì đa số thành phần bằng0. |
| Static C/V cùng khách trên common cells | Ch4 4.4; drift retrospective4.7; Ch5 | Ch4 so sánh tổng hợp | Giữ caveat missing outcomes và diagnostic120 chưa rerun; không kết luận “không khoảng giữa”, không phát biểu dominance thực nghiệm từ H thất bại. |
| “Không khoảng giữa”, (1-p)^n | Ch4 4.7.7 và Ch5 | Không là evidence cuối | Giả thiết independent rider chưa chứng minh và later recovery/T38 đã cho common complete cells. Xóa bảng và universal conclusion. |
| 98/102, 31/32, 40/40 | Abstract, Ch1, Ch3, Ch4, Ch5 | Ch4 bảng prediction | Các nơi khác dẫn chiếu; ghi weak predictions25/26 tách mẫu số và heuristic. |
| Quét phát triển(a)/(b), lời hứa thực/synthetic | Ch4 4.9 nhiều bảng, phần giải thích và phần giới hạn lặp | Ch4 recovery table + real-data figure | Một compact table để thấy recovery đổi service và breaches; một trend figure với caption denominator. |
| W07 24%/7,3% | Abstract, Ch1, Ch4 4.9.6/7, Ch5 | Ch4 bảng/figure cùng W07X | Không giới thiệu là independent confirmation; ngày12/13 phát triển, window overlap. |
| Novelty boundary | Ch1 1.3, Ch2, Ch4 4.11.4, Ch5 5.2 | Ch2 | Một synthesis table, claim wording nhất quán; không cần bảng “có/không” lặp ở Results. |
| Ratchet/horizon equivalence | Ch4 4.3.4 và4.6; Ch3/Ch5 nhắc | Ch4 negative evidence/implementation boundary | Gộp4bảng xuống1table nhỏ hoặc1đoạn có chính xác bộ sinh chèn thuần. |
| Search not capped/thin set | Ch4 4.13 và4.14.2 | Ch4 audit/limitations | Báo các caps0 trong1đoạn; completeness chỉ trong generator đã định nghĩa, không toàn không gian DARP. |
| Generator A/B/C và reordering | Ch4 4.14,4.15,Ch5 10futureitems | Ch4 bảng âm +Ch5 relevant uncertainty | Giữ no gain/18of20 failure và reason; bỏ chi tiết layers/warnings table cũng như speculation reward zero. |
| Welfare | Ch2 2.5,Ch4 4.12,Ch5 hạn chế | Xóa | Hệ số20–25UNVERIFIED; conversion accumulated revision→welfare không chứng minh dùmetadatađúng. |
| Limitations | Ch4 cuối từngmục +4.16 +Ch5 | Ch4 kết nốiclaim; Ch5 synthesis gọn | Giữ mỗi caveat tại nơi nó thay đổi interpretation, Conclusion không lặp toàn bộ inventory. |

## Điều không được rút

- v/e/p cùng epoch/state; e là phép chiếu có thể tính chứ không phải tác động giao thông thuần. Route history ảnh hưởng trạng thái, nên không suy ra causal identification hay policy-invariant traffic effect.
- z=x+c là đẳng thức có dấu; V≤C+X là bất đẳng thức tuyệt đối. 89,06% là tỉ số tổng C/tổng V cho hai chiều, không phân hoạch phần trăm. Trần 30s áp giờ trả, khác tổng hai chiều ở bảng headline.
- Sổ cái riêng khách/chiều, cộng dồn và monotone; guarantee chỉnormal certified transitions, phase/identity/physical gates có phạm vi riêng.
- No-op được sinh, p(no-op)=e, ledgertrướctrongtrần, N kiểm vật lý. Loại no-op khác làm rỗngtoàntập; backendcóyêucầubaseline riêng phải giải thích.
- Điều kiệnHphảiđúngmọitrajectoryrelevant cho subset theorem; observed chosen actionskhôngđủvà228/3vi phạm nghĩa giảthiếtkhôngđúng trên panel. Cận thịgreedykhônglà tốiưutoàncục.
- Mplus chỉ chặnmuộn,Mhai chiều,Vtổngbiếnđộng,Ctổngdecision. Cùnggiâykhôngcùnglời hứa. Monotone insertion làmC vàendpointgầntrùngstatic; khôngdùngchain novelty làm headline.
- CE3 sửa có lợi vẫn tiêuC; đồngnhấtcácgiâydời với tổnhại/tinh thần/user satisfactionkhông được.
- Commitmentfailure và physical lateboardingfailure phải tách; recovery tiếp tụcchạy nhưng phát breach/non-normalcertificate, khôngbiếnviolatedpromise thànhfulfilled.
- Recovery(b) phải có violationcùngchiều thamchiếuvàkhôngtệhơn; không bỏphaselock/physicallock; post-sealedamendment và computework hạn chế phải giữ.
- Mainstatic vsprospectivethămdò vsretrospectivephânbiệt rõ. T38 có testholdout nhưng ngưỡngdo chọn sau dev vàepisodecùngnhóm dependent; khônghợp thức hóa thành pureconfirmatory.
- T38 32/34scorecoverage khác1 actualVboundfailure; gammasingleoutlier; 7/9morningcoverage, nominalCPupper17.4 không<=10. Cscorecoveredlogicalbound khácpopulationcalibrationguarantee.
- T38 same service vsMplus/Vkhông nghĩasame promise; -96/3672 là-2.614pp, relative96/2434=3.944%; meanper-episode14.5%khácpooled12.4%.
- Small metricclosure96nodes/9120edges,108requests/8cars,onefixedseed; scalar15-minrealtraffic,notstreetnetwork,notfulllargeManhattan; policycomparisonsnotsystem-vs-literaturecompetitions.

## Tiếng Việt và thông tin cá nhân

Các câu “đập vào”, “cắn đau”, “mất trắng”, “chữa lành”, “cứu khóa luận”, “món hời tồi”, “quyền không bao giờ dùng được” làm giọng văn quá kịch tính hoặc tranh biện. Thay bằng mô tả điều kiện/cơ chế/kết quả. Giảm “chúng tôi”, chọn “khóa luận” hoặc chủ ngữ là “cổng”, “thực nghiệm”. “Quy trách nhân quả”, “nghĩa vụ phương tiện” dễ khiến độc giả hiểu legal/counterfactualcausalclaim rộng hơn dữ liệu; chọn “phân rã vận hành”, “phần thay đổi khi giữ tuyến”, “cơ sở hành vi”.

Lời cảm ơn kể nhiều cuộc trao đổi cụ thể với giảng viên, trong khi tên giảng viên chưa có. Không có chứng cứ cho các giai thoại này: bỏ, dùng lời cảm ơn trung tính với nhà trường và người hỗ trợ do tác giả xác nhận. Không tự tạo họ tên người hướng dẫn. Có thể giữ tên sinh viên/MSV/lớp theo source cho đến khi tác giả sửa.

Ký hiệu v trùng vehiclev ở nền DARP: dùng đội xe K và xe k hoặc giải thích vtiếnghứa là scalartimemarker. Chỉ dùng C,X,Vchoaggregatechuỗi, A,d,Bchoonestep nếugiữ; tránh thêm bảngcodeenum đầy trongmaintext. Thuậtngữ “ô”, “episode”, “lần chạy”, “cặp dự đoán” cần ledger vì đangbịhoánđổi.

## Quality gates cần root kiểm sau biên tập

Mỗi display được nhắc trong prose; khôngcitationunused, khônglabeldangling. Trang cuốiheadingđôithamkhảophảibỏ. Dùng sourcePDFvectorfortwofiguresnew, grayscaleaccessible. Khôngdùngstackedattributionbar impliesexactpartition. Đọccaptionvàthướcđo100%zoom. Kiểm tấtcảpages vàoverflowbằn mắt; 13pt/1.5spacelềgốcgiữ. FinalPDF≤80pages. Ch5mới khôngđược lặp kếhoạchT38 chưa chạy hoặc giảthuyếtC phụcvụnhiềuhơn đãkhôngđạt.
