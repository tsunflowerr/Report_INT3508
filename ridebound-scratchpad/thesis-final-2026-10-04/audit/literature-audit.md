# Kiểm toán văn liệu và trích dẫn

Ngày đối chiếu: 04/10/2026. Bản gốc có 27 mục tài liệu tham khảo, trong đó 19 khóa được trích trong nội dung. Đã kiểm metadata của mọi mục gốc bằng Crossref, arXiv, trang nhà xuất bản hoặc trang tài nguyên chính thức. Bản sửa metadata đầy đủ nằm ở `corrected-bibliography.tex` (32 mục gồm 5 nguồn bổ sung cần cho ranh giới claim). Root sẽ chỉ giữ các mục thực sự được trích trong bản cuối.

Đây là kiểm toán metadata và khả năng nguồn hỗ trợ phát biểu, không phải tổng quan hệ thống toàn bộ văn liệu. Toàn văn cục bộ được dùng khi kiểm các cơ chế gần nhất và những con số dễ sai; với nguồn chỉ đọc abstract/trang xuất bản, không suy diễn sự vắng mặt của cơ chế trong toàn bài.

## Quy trình và Nature Skills

Đã đọc router `nature-academic-search`, `nature-ref-verifier`, `nature-citation`, `nature-paper-card`. Academic search dùng luồng citation-verification và các nguồn T1; MCP academic-search không có trong phiên nên dùng Crossref REST và web/publisher. Chạy bundled preflight, 3/3 endpoint PubMed, Crossref, arXiv truy cập được. Hai lần Crossref ban đầu bị 429 được đọc lại thành công; dữ liệu raw ở `literature-crossref-metadata.json`.

Nature Citation có phạm vi Nature/CNS, không phù hợp với văn liệu transportation/OR không giới hạn của khóa luận. Đã dùng nguyên tắc kiểm entailment nhưng không ép danh sách vào CNS hoặc bổ sung nguồn ngoài chủ đề. Nature Paper Card có đầu ra thẻ 16 mục cho một bài, không phải đầu ra được yêu cầu ở đây, nên chỉ đọc để xác định phạm vi và không tạo thẻ giả. Nature Writing áp dụng bản thảo thuật toán, phần mở đầu/văn liệu, đích khóa luận thông thường; tiếng Việt theo yêu cầu người dùng.

## Các lỗi metadata phải sửa

| Khóa | Bản gốc | Sửa đã xác minh | Nguồn chính |
|---|---|---|---|
| alonsogonzalez2020 | Sai danh sách và thứ tự tác giả, có van Cranenburgh, thiếu Hoogendoorn-Lanser | María J. Alonso-González; Niels van Oort; Oded Cats; Sascha Hoogendoorn-Lanser; Serge Hoogendoorn | [Publisher](https://www.sciencedirect.com/science/article/pii/S0968090X1931589X), Crossref doi10.1016/j.trc.2020.102621 |
| li2025 | D. Li, A. Alharbi | X. Li (Xinling), M. Alharbi (Meshal); 8 tác giả còn lại giữ đúng thứ tự | [arXiv](https://arxiv.org/abs/2506.07345) |
| fielbaum2022scale | Trộn tên preprint có “and comparison with public transport” với tên tạp chí 2023; thiếu tập/article/DOI | Tên bản xuất bản: Economies and diseconomies of scale in on-demand ridepooling systems. Economics of Transportation34:100313,2023 | [Bản gốc tác giả](https://autonomousrobots.nl/assets/files/publications/23-fielbaum-eco.pdf), doi10.1016/j.ecotra.2023.100313 |
| sridharan1987 | Dùng làm nguồn cho cả thước đo1988 | Giữ bài freezing1987; thêm bài measuring1988 riêng | [Wiley](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1540-5915.1988.tb00259.x) |
| schulz2026 | Thiếu kỳ | OR Spectrum48(2):541–586,2026 | [Publisher](https://link.springer.com/article/10.1007/s00291-026-00847-0) |
| sivagnanam2026 | Thiếu trang/DOI | ICCPS2026,pp48–57,doi10.1109/ICCPS68698.2026.00012 | Crossref; [bản tác giả](https://scopelab.ai/files/iccps2026_prompt_confirmation.pdf), [arXiv](https://arxiv.org/abs/2603.07422) |
| haferkamp2024 | Thiếu DOI | Thêm10.1016/j.ejtl.2024.100134 | [Bản gốc do EURO cung cấp](https://www.econstor.eu/bitstream/10419/325197/1/1903375193.pdf), Crossref |
| fleetpy2022 | Preprint lịch sử còn hợp lệ nhưng chưa nêu bài cuối2026 | Giữ bản2022 nếu cần; thêm bài xuất bản2026 với danh sách tác giả khác | [Publisher](https://link.springer.com/article/10.1186/s12544-026-00823-3) |
| ortools | Gán năm2024 cho trang docs không có phiên bản trong citation | Dùng corporate author Google, tài liệu/phần mềm, access04/10/2026; phiên bản thực nghiệm ghi ở Methods | [Google docs](https://developers.google.com/optimization) |

Ngày online và ngày tập tạp chí không đồng nhất không phải DOI sai. Elmi2026 thuộc TRC192:105897; tập tháng11/2026 nhưng bài final đã online trước ngày audit. Tellez thuộc Networks79(4):452–478,2022, dù online11/06/2021. Không đổi năm theo chuỗi ký tự năm trong DOI.

## Metadata các mục gốc còn lại

| Khóa | Kết luận | Nguồn định danh chính và phạm vi |
|---|---|---|
| alonsomora2017 | Đúng tên, tác giả,114(3):462–467,2017 | [DOI](https://doi.org/10.1073/pnas.1611675114); bản PDF gốc tại corpus nghiên cứu |
| fielbaum2020 | Đúng121:102831,2020 | [Toàn văn tác giả](https://autonomousrobots.nl/assets/files/publications/20-Fielbaum-TRC.pdf), [DOI](https://doi.org/10.1016/j.trc.2020.102831) |
| gerzinic2023 | Đúng tác giả33:100616,2023 | [PDF TU Delft](https://repository.tudelft.nl/file/File_9e0d2458-33d1-4048-af81-2163aa53ba0d?preview=1), [DOI](https://doi.org/10.1016/j.tbs.2023.100616) |
| bansal2019 | Đúng arXiv2019 | [arXiv](https://arxiv.org/abs/1904.07987), toàn văn6trang đã tải vào audit/papers |
| kovacs2014 | Đúng64(3):192–213 | [Wiley](https://onlinelibrary.wiley.com/doi/abs/10.1002/net.21565), Crossref |
| cordeau2007 | Đúng153(1):29–46 | [Publisher](https://link.springer.com/article/10.1007/s10479-007-0170-8), Crossref; gốc chưa trích, bản mới dùng làm nềnDARP |
| toth2014 | Đúng sách2nded và hai editors | [SIAM](https://epubs.siam.org/doi/book/10.1137/1.9781611973594); gốc không trích |
| groer2009 | Đúng11(4):630–643 | [DOI](https://doi.org/10.1287/msom.1080.0243), Crossref; gốc không trích |
| blackburn1986 | Đúng32(4):413–429 | [DOI](https://doi.org/10.1287/mnsc.32.4.413), Crossref; gốc không trích |
| agatz2012 | Đúng223(2):295–303 | [DOI](https://doi.org/10.1016/j.ejor.2012.05.028), Crossref; gốc không trích |
| tlc | Tên nguồn/URL tồn tại | [Official](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page); nguồn dữ liệu, không xác nhận giấy phépCCBY cho mọi bản dẫn xuất |
| elmi2026 | Đúng4tác giả,192:105897 | [TU Delft final](https://repository.tudelft.nl/record/uuid%3A8d4faffb-7e75-425b-9e53-1ac78e70e2a5), Crossref; localPDF33trang gồm cover |
| sharifazadeh2022 | Đúng161:128–149 | [PDF TU Delft](https://research.tudelft.nl/files/125571588/1_s2.0_S0191261522000716_main.pdf), Crossref |
| schmidt2026 | Tồn tại, đúng4tác giả, preprint2026 | [arXiv](https://arxiv.org/abs/2609.11950); entailment phạm vi abstract, không kết luận không có ledger từ abstract |
| zalesak2025 | Đúng3tác giả/arXiv | [arXiv](https://arxiv.org/abs/2504.10649); không dùng chữ stability của thuật toán làm lời hứa người dùng |
| agarwal2019 | ĐúngPMLR97:111–119 | [PMLR](https://proceedings.mlr.press/v97/agarwal19c.html); không chuyển guarantees onlinecontrol sangRideBound |
| chen2018 | ĐúngPMLR75:1574–1594 | [PMLR](https://proceedings.mlr.press/v75/chen18b.html); đuôi URL18b,18a là bài khác |
| borodin1992 | Đúng39(4):745–763 | [DOI](https://doi.org/10.1145/146585.146588), Crossref; chỉ analogymetric không competitivebound RideBound |

Các nguồn bổ sung đã đối chiếu: [Sridharan1988](https://doi.org/10.1111/j.1540-5915.1988.tb00259.x), [FleetPy2026](https://doi.org/10.1186/s12544-026-00823-3), [Ackermann/Rieck2025](https://link.springer.com/article/10.1007/s00291-025-00809-y), [Tellez2022](https://onlinelibrary.wiley.com/doi/10.1002/net.22063), [Wang/Fielbaum2026](https://www.sciencedirect.com/science/article/pii/S0968090X26001336). Metadata raw gồm đầy đủ thứ tự tác giả. Wang entailment dựa publisher highlights, không đọc toàn văn để khẳng định mọi chi tiết.

## Audit entailment và ranh giới phát biểu

| Phát biểu gốc | Đánh giá | Xử lý trong Ch1/2 mới |
|---|---|---|
| Fielbaum chỉ đo sau sự việc, “về mặt toán học không thể trở thành ràng buộc” | Gây hiểu nhầm: metricactual retrospective, nhưng mục6 đã có predicted waiting ratchet | Tách metricactual với cổng predicted, công nhận cơ chế kiểm soát trước quyết định đã có |
| Fielbaum đầy đủ kiểm soát từ chối34.5→45.6% | VERIFIED bảng5, PDFpage17, fleet2000capacity4 | Giữ11.1pp có scope, không so trực tiếp với7.13pp của RideBound |
| Alonso-Mora3000xe4chỗ98% | VERIFIED, chờTB2.8min/delay3.5min, nghiên cứu mô phỏng | Bỏ “ở quy mô thật” theo nghĩa deployment; ghi điều kiện mô phỏng |
| Bansal công bốETAtrungthực→nhậnchuyến+10% | Không phải quan hệ nhân quả empirical đó; bài strategicdisplaypercentile+simulation | Bỏ con số ở mở đầu, mô tả đúng chiến lược hiển thị; không suy luận nhu cầuRideBound |
| Bansal không có mô hình phía cung | Bài có riêng Section3 Supply-sideOptimization | Bỏ phát biểu khái quát |
| Geržinič20–25EUR/h chưa đọc gốc | Nay VERIFIED summarySection4.1, PDFpage9; Table4page8 là early26.59/late18.14EUR/h | Giữ qualitativepreference; không đưa các đơn giá vào phúc lợiTVdropoff |
| Alonso-GonzálezVORthấphơnVOT | VERIFIED abstract; reliabilityratio≈.5, SPNetherlandsN1006 | Không suy rộng sang ledgerTV, không dùng như tiền cho mỗi giâyETA |
| MRP chưa chuyển sang điều phốixe | Không được chứng minh bởi khảo sát này | Bỏ noveltybridgeclaim; chỉ nhận intellectualdebt về ổn định lịch |
| Freezingcosttăngvọt80% | Chưa đối chiếu toàn văn đủ hỗ trợ ngưỡng đó | Bỏ ngưỡng80% và “tương ứng chính xác” |
| Luậtnghĩavụ/SLA tươngứngchínhxác vànoveltycomputeboundary | Thiếu legalprimarysources; mang thêm claim ngoài phạmvi | Bỏ phần luật trongCh2; phương pháp đứng bằng định nghĩa và giả thiết riêng |
| Elmi chỉ bảo vệ một nhóm, không có trần cho mọi khách | Sai nếu bỏ ordinarycontrol và residualslack constraints | Công nhận cả targetedcontrol và uniformslackbenchmark theo khách |
| Schulz có deadline từ firstpromise | VERIFIED Section3.1, localPDFpage9; slackdefault15min ở6.3.5,page28 | Ghi đối chứng cùng hình thức, không tái lập solver/data/acceptancepaper |
| SharifAzadeh hai chiều bằng cổngM của khóa luận | Window/maxride trong choice/pricingmodel không tự bằng symmetricfirstpromise cap | Ch2 không đồng nhất; Ch3 nên xem M là đối chứng khái niệm, không replicationtoànpaper |
| TotalTV chứng minh hài lòng/phúc lợi | Chưa có dữ liệu phù hợpconstruct/population/monetization | Bỏ conversion, để hai outcome service/instability riêng |
| Đối chiếu giữ tuyến là causal attribution | Chỉ accountingcounterfactual tại samecurrentstate; routehistory vẫn policydependent | Nêu rõ phép phân rã trong mô hình; không estimationtotalcausaleffect |

## Phạm vi contribution

1. Operationalmodel/system: sổ cái theo khách và chiều, phần thay đổi giữa phương án giữ tuyến với đề xuất, witness/certificate và runner cùng ngữ nghĩa. Không nhận riêng dynamicinsertion/ETA/reassignment/consistency/leastcommitment/no-worse là novel.
2. Conditionalanalysis: bốn dạng cổng và giả thiết giữ phương án no-op; không bảo đảm toànbộphysicalfeasibility hay actualserviceSLA. Các phép chứng minh sơ cấp được mô tả đúng mức.
3. Evidence: pairedservice/instabilitycost và trường hợp drift/recovery; replication và negativefindings giữ vai trò bằng chứng thay vì tăng số“đónggóp”. Không claimsuperiorityagainstcompleteprioralgorithms, useracceptance hoặc deployment.

Bản Ch1/2 mới đã đọc lại sau viết. Giữ baRQ, ba nhóm contribution, không lặp danh sách số liệu kết quả. `muc:chodung` chuyển sang Ch2 nơi đối chiếu nguồn gần nhất. Bản gốc không bị sửa. Ch3/4/5 và các audit bằng chứng do thành viên khác kiểm tra; không tuyên bố agent này độc lập đọc lại mọi dòng của toàn bộ năm chương.

## Bổ sung nguồn hiệu chỉnh phân vị T38

- Angelopoulos, A. N. và Bates, S. (2023). *Conformal Prediction: A Gentle Introduction*. *Foundations and Trends in Machine Learning*, 16(4), 494–591. DOI: https://doi.org/10.1561/2200000101. Metadata xác minh tại trang tóm tắt nhà xuất bản: https://www.nowpublishers.com/article/DownloadSummary/MAL-101.
- Đã đọc phần liên quan trong bản tác giả v6: https://arxiv.org/pdf/2107.07511v6, mục 1.1 và Appendix D, Theorem D.1 (trang PDF 50–51). Không tuyên bố đã đọc toàn bộ 51 trang cho nguồn bổ sung này.
- Công thức lấy điểm thứ k trong các score đã sắp: `k = ceil((n+1)(1-alpha))`. Với n=15, alpha=0.1, k=15 nên ngưỡng là score lớn nhất của phần hiệu chỉnh. Định lý yêu cầu các score hiệu chỉnh và score mới trao đổi được, và chỉ bảo đảm độ phủ biên; nó không bảo đảm cho từng hành khách, mọi episode, hay một tập calibration đã cố định.
- Trong T38, tách `(day,sample)` chỉ làm rời ID nhóm; kiểm tra nguồn đã xác nhận 75 chuyến nguồn xuất hiện ở cả calibration và test theo `(day, original CSV request_id)`, khớp timestamp và OD. Vì chưa chứng minh tính trao đổi được của các score episode và các nhóm có phụ thuộc, phải gọi đây là quy tắc phân vị lấy cảm hứng từ split conformal. `32/34` score không vượt ngưỡng và `33/34` actual-V trong biên là tần suất mô tả trên các trường hợp đã chạy, không phải bảo đảm 90% cho quần thể. Chẩn đoán cũ 43 cặp `(day, ordinal)` không được dùng như số chuyến giao nhau.

## Nguồn bộ dữ liệu bổ sung trong bảng cấu hình — 05/10/2026

Đã mở trang chính thức [Zenodo record 15187906](https://zenodo.org/records/15187906):
R. Engelhardt và F. Dandl, *FleetPy: Input Data for Manhattan Case Study*, phiên bản
1.0, xuất bản 10/04/2025, DOI `10.5281/zenodo.15187906`. Trang mô tả nhu cầu TLC
Manhattan ngày 11–18/11/2018 và mạng OSM, liệt kê `FleetPy_Manhattan.zip` 408,9 MB.
Khóa `fleetpydata2025` được trích ở phần tái tạo đầu vào. Bản PDF cuối có 24 tài
liệu, tất cả được trích; không giữ 32 mục của bản sửa metadata trung gian như một
danh mục cuối. Kiểm kích thước byte và SHA-256 của ZIP cục bộ ghi riêng trong
`reproducibility-config.json`; không suy ra quyền giấy phép của mọi bản dẫn xuất
từ một trang metadata.
