# R35 — Kiểm độc lập siêu dữ liệu và câu TLC

Ngày kiểm: 13/10/2026. Đây là đầu ra phụ để phiên chính kiểm lại trước khi dùng. Chỉ đọc nguồn; không sửa luận văn, bản nháp hay sổ bằng chứng. Danh tính tài liệu được xác định từ bản gốc/trang nguồn trước khi mở `06-chuong2-BIB.md`; sau đó mới so với BIB và `ridebound/noi-dung/10-tai-lieu.tex`.

## Kết luận

- Cả 15 mục siêu dữ liệu trong BIB của người viết khớp đúng phiên bản họ đã đọc. Không có DOI, năm hay tác giả bịa trong 15 mục đó.
- Mục đang có trong luận văn `alonsogonzalez2020` SAI danh sách/thứ tự tác giả. BIB người viết đã sửa đúng; phải đưa bản sửa vào luận văn.
- Có 9 khóa mới phải thêm khi ghép chương; đây là công việc tích hợp, không phải bằng chứng metadata sai: `engelhardt2026`, `horl2022`, `hu2022`, `laupichler2026`, `leonardi2024`, `lu2024`, `molenbruch2017`, `wardman2026`, `yu2022`.
- `lu2024` và `leonardi2024` là các bản tiền ấn có thật; bản xuất bản sau không làm trích dẫn bản đã đọc thành sai. Không ghép DOI/năm của bản tạp chí với trang/công thức của bản tiền ấn khi chưa đối chiếu nội dung.
- Câu TLC công bố theo tháng, thường trễ hai tháng: AGREE. Câu suy luận về dữ liệu của hãng xe nên nêu rõ là giả định của khóa luận.
- Lỗi truy vết nhỏ trong addendum 5: DRE dài 9 trang, không phải 3 trang.

## Một hàng cho mỗi khóa

Cột kết luận đánh giá siêu dữ liệu BIB đề nghị cho Chương 2. Lỗi trong thư mục luận văn hiện hành ghi riêng; chưa chạy LaTeX.

| Khóa | Siêu dữ liệu độc lập | Phiên bản và nguồn kiểm | Kết luận / điều chỉnh khi ghép |
|---|---|---|---|
| `alonsomora2017` | Javier Alonso-Mora; Samitha Samaranayake; Alex Wallar; Emilio Frazzoli; Daniela Rus. **On-demand high-capacity ride-sharing via dynamic trip-vehicle assignment**. *Proceedings of the National Academy of Sciences* **114(3), 462–467 (2017)**. DOI **10.1073/pnas.1611675114**. | [PNAS](https://www.pnas.org/doi/10.1073/pnas.1611675114), tên/tác giả/năm/tập/số/trang ở phần đầu; xuất bản trực tuyến 03/01/2017. Bản Early Edition 6 trang có số trang 1–6; số in là 462–467. | **ACCEPT / AGREE**. BIB và mục đang có đều đúng. PNAS ghi có correction năm 2018; correction sửa cách viết họ Samaranayake, BIB đang dùng đúng. |
| `alonsogonzalez2020` | María J. Alonso-González; Niels van Oort; Oded Cats; Sascha Hoogendoorn-Lanser; Serge Hoogendoorn. **Value of time and reliability for urban pooled on-demand services**. *Transportation Research Part C: Emerging Technologies* **115, article 102621 (2020)**. DOI **10.1016/j.trc.2020.102621**. | Trang 1 PDF `C:/PDF/Paper/Value_of_time_and_reliability_for_urban_pooled_on-.pdf`; [trang nhà xuất bản](https://www.sciencedirect.com/science/article/pii/S0968090X1931589X) cũng cho đủ 5 tác giả, tập 115, tháng 6/2020, mã bài. | **ACCEPT WITH CORRECTIONS / WRONG ở bib luận văn, AGREE ở BIB người viết**. Luận văn thêm nhầm S. van Cranenburgh, thiếu S. Hoogendoorn-Lanser, đảo thứ tự van Oort/Cats. Dùng chính xác bản thay thế dưới đây. |
| `elmi2026` | Amir Elmi; Emily Moylan; Javier Alonso-Mora; Andres Fielbaum. **Improving ridepooling reliability using shareability shadows**. *Transportation Research Part C: Emerging Technologies* **192, article 105897 (2026)**. DOI **10.1016/j.trc.2026.105897**. | PDF ELMI trong SP5: bìa kho TU Delft ghi Final published version, bài trang 1/PDF trang 2 cho đủ metadata; available online **04/08/2026**. [TU Delft](https://research.tudelft.nl/en/publications/improving-ridepooling-reliability-using-shareability-shadows/), [nhà xuất bản](https://www.sciencedirect.com/science/article/pii/S0968090X26003839) ghi issue **11/2026**. | **ACCEPT / AGREE**. Bản cuối đã công bố online trước ngày kiểm; số tháng của issue trong tương lai không phải lỗi. `105897` là mã bài, không phải trang. |
| `engelhardt2026` | Roman Engelhardt; Florian Dandl; Arslan Ali Syed; Chenhao Ding; Santiago Alvarez-Ossorio Martinez; Yunfei Zhang; Hoda Hamdy; Joel Brodersen; Zhipu Chen; Klaus Bogenberger. **FleetPy: an open source simulator for reproducible research on mobility-on-demand services**. *European Transport Research Review* **18, article 52 (2026)**, 16 trang. DOI **10.1186/s12544-026-00823-3**. | PDF `claude-work/pdf/fleetpy-etrr-2026.pdf`, trang 1; [Springer](https://link.springer.com/article/10.1186/s12544-026-00823-3), Published/Version of record **15/07/2026**. | **ACCEPT / AGREE**. Thêm khóa mới. Không dùng metadata của FleetPy tiền ấn 2022 cho nội dung phiên bản 2026. `18:52` nghĩa là tập/mã bài. |
| `fielbaum2020` | Andrés Fielbaum; Javier Alonso-Mora. **Unreliability in ridesharing systems: Measuring changes in users' times due to new requests**. *Transportation Research Part C: Emerging Technologies* **121, article 102831 (2020)**. DOI **10.1016/j.trc.2020.102831**. | Trang 1 PDF `C:/PDF/Paper/Unreliability_in_ridesharing_systems_Measuring_cha.pdf`; available online **22/10/2020**. [Nhà xuất bản](https://www.sciencedirect.com/science/article/pii/S0968090X2030735X) ghi issue 12/2020. | **ACCEPT / AGREE**. BIB và mục hiện hành đúng. |
| `horl2022` | Sebastian Hörl; Felix Zwick. **Traffic uncertainty in on-demand high-capacity ride-pooling**. Conference paper, **ETH Zurich Research Collection (2022)**. DOI **10.3929/ethz-b-000561639**. | Bìa PDF `claude-work/pdf/hoerl-zwick-2022.pdf` ghi tác giả, Conference Paper, 2022 và DOI; trang đầu bản thảo ghi Submission Date **27/10/2021**. [ETH IVT](https://www.ivt.ethz.ch/en/research/matsim.html) và [CV tác giả trên HAL](https://cv.hal.science/sebhoerl), nội dung được chỉ mục tìm kiếm, liên hệ bài với **101st Annual Meeting of the Transportation Research Board, Washington, DC, 9–13/01/2022**, paper **TRBAM-22-01001**. | **ACCEPT / AGREE**. BIB tối thiểu hiện tại đúng. Có thể bổ sung hội nghị nếu muốn, nhưng không bắt buộc; không phải bài TR-B 161 của Sharif Azadeh. DOI kho lưu không phải DOI tạp chí. Không bịa tập/trang proceedings; TRBAM-22-01001 là mã bài. |
| `hu2022` | Xinyu Hu; Tanmay Binaykiya; Eric Frank; Olcay Cirit. **DeeprETA: An ETA Post-processing System at Scale**. **arXiv:2206.02127v1 (2022)**, 9 trang. DOI **10.48550/arXiv.2206.02127**. | [arXiv abs](https://arxiv.org/abs/2206.02127), v1 **05/06/2022**, cs.LG, không có journal-ref; [PDF](https://arxiv.org/pdf/2206.02127) có 9 trang. Bản DRE cục bộ cũng có 9 dấu phân trang pdftotext. | **ACCEPT / AGREE** đối với BIB. Thêm khóa mới. **WRONG** đối với addendum 5, dòng anchor DRE ghi “3 trang”; sửa thành “9 trang”. Không suy tên hội nghị từ định dạng ACM của bản thảo. |
| `laupichler2026` | Moritz Laupichler; Robin Andre; Kim Kandler; Peter Sanders; Peter Vortisch. **Advancing Dynamic Ride-Pooling Simulation -- A Highly Scalable Dispatcher**. **arXiv:2605.11798v1 (2026)**. DOI **10.48550/arXiv.2605.11798**. | [arXiv](https://arxiv.org/abs/2605.11798), v1 **12/05/2026**, cs.CE, không có journal-ref. | **ACCEPT / AGREE**. Thêm khóa mới; không gán venue/tập/trang tạp chí khi nguồn chưa có. |
| `leonardi2024` | Pierfrancesco Leonardi; Vincenza Torrisi; Andrea Araldo; Matteo Ignaccolo. **Data-driven assessment for the predictability of On-Demand Responsive Transit**. **arXiv:2411.11899v1 (2024)**. DOI **10.48550/arXiv.2411.11899**. Comments: EWGT, **09/2024, Lund, Sweden**. | [arXiv](https://arxiv.org/abs/2411.11899), v1 **14/11/2024**, physics.soc-ph/stat.AP; PDF `claude-work/pdf/leonardi-2024.pdf` là bản thảo này. Bản tạp chí về sau được xác minh riêng bên dưới. | **ACCEPT / AGREE** cho bản đã đọc. Thêm khóa mới. BIB đã nói đúng rằng trích bản arXiv; không buộc đổi sang 2026. |
| `lu2024` | Chengqi Lu; Nico Kühnel. **To Wait or to Cruise: The Trade-Off Between Waiting Time and Detours for Service Efficiency in Ride-pooling Systems**. **Preprint, Technische Universität Berlin, DepositOnce (2024)**. DOI **10.14279/depositonce-21472**. | [DepositOnce](https://depositonce.tu-berlin.de/items/fa1164ba-ed61-4775-a1ac-253d80e1758a), issued **01/10/2024**, deposit **14/10/2024**, Preprint/Submitted Version; PDF `claude-work/pdf/lu-kuehnel-2024.pdf` ghi Compiled October 1, 2024. | **ACCEPT / AGREE** cho bản đã đọc. Thêm khóa mới. Bản 2025 có thật nhưng việc giữ bản tiền ấn 2024 không sai. |
| `molenbruch2017` | Yves Molenbruch; Kris Braekers; An Caris. **Operational effects of service level variations for the dial-a-ride problem**. *Central European Journal of Operations Research* **25(1), 71–90 (2017)**. DOI **10.1007/s10100-015-0422-7**. | PDF `C:/PDF/Paper/OperationalEffectsofServiceLevelVariations-publication151005.pdf`, bìa; [Springer](https://link.springer.com/article/10.1007/s10100-015-0422-7), online **05/10/2015**, issue **03/2017**; [kho tác giả](https://documentserver.uhasselt.be/handle/1942/19719) ghi số 1. | **ACCEPT / AGREE**. Năm 2017 đúng khi trích bản có tập/trang. Phân biệt bài *Typology and literature review for dial-a-ride problems* của cùng nhóm, DOI 10.1007/s10479-017-2525-0; đó không phải PDF được dùng ở chương này. |
| `schulz2026` | Arne Schulz; Christian Pfeiffer. **Efficient insertion and reoptimization algorithms for a customer-oriented dynamic dial-a-ride problem**. *OR Spectrum* **48(2), 541–586 (2026)**. DOI **10.1007/s00291-026-00847-0**. | PDF `C:/PDF/Paper/s00291-026-00847-0.pdf`, trang 1 (in 541); [Springer](https://link.springer.com/article/10.1007/s00291-026-00847-0), online **02/02/2026**, issue **06/2026**. | **ACCEPT / AGREE**. Mục hiện hành 48:541–586 đúng nhưng có thể thêm (2) như BIB. |
| `tlc` | **New York City Taxi & Limousine Commission. TLC Trip Record Data**. Trang web chính thức, không thấy năm công bố cố định. URL **https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page**. | [TLC](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page), mở độc lập **13/10/2026**; người viết đã mở **12/10/2026**. | **ACCEPT / AGREE**. Giữ ngày truy cập người viết nếu ghi lịch sử của họ; nếu ghi lần kiểm này thì dùng 13/10/2026. Không đặt 2026 thành năm xuất bản của trang. |
| `wardman2026` | Mark Wardman; Paul Murphy; Manuel Ojeda-Cabral; Alex Mitrani; Kazuyuki Neki; Richard Martin Humphreys. **Value of time multipliers for walk time, wait time, service headway, displacement time, reliability and congested travel time: review and meta-analysis of worldwide evidence**. *Transportation Research Part A: Policy and Practice* **207, article 104925 (2026)**. DOI **10.1016/j.tra.2026.104925**. | Trang 1 PDF `C:/PDF/Paper/1-s2.0-S0965856426000662-main.pdf`, online **08/03/2026**; [kho tác giả White Rose](https://eprints.whiterose.ac.uk/id/eprint/239301/) ghi issue **05/2026**. | **ACCEPT / AGREE**. Thêm khóa mới. Mã bài 104925, không ghi làm trang. |
| `yu2022` | Qiuping Yu; Yiming Zhang; Yong-Pin Zhou. **Delay Information in Virtual Queues: A Large-Scale Field Experiment on a Major Ride-Sharing Platform**. *Management Science* **68(8), 5745–5757 (2022)**. DOI **10.1287/mnsc.2022.4448**. | [INFORMS](https://pubsonline.informs.org/doi/10.1287/mnsc.2022.4448), Cite as cho đủ metadata; online **08/06/2022**, issue **08/2022**. Đây là trang tóm tắt, không đọc toàn văn. | **ACCEPT / AGREE**. Thêm khóa mới. Không dùng số trang cả issue 5557–6354 làm trang bài. |

Tổng bảng: **14 ACCEPT, 1 ACCEPT WITH CORRECTIONS, 0 REJECT**, khi coi mục AGZ phải sửa trong bib luận văn là lỗi tích hợp. Nếu chỉ chấm file BIB đề nghị của người viết: **15 ACCEPT, 0 ACCEPT WITH CORRECTIONS, 0 REJECT**. Không cộng các hàng này vào tổng fact-check chính một cách máy móc nếu phiên chính đã tạo hàng tương ứng.

## Các phiên bản xuất bản sau: tùy chọn cập nhật, không phải lỗi bắt buộc

1. **Lu và Kühnel (2025).** [Trang Elsevier](https://www.sciencedirect.com/science/article/pii/S2213624X25001361) cho *Case Studies on Transport Policy* **21, article 101499**, issue **09/2025**, DOI **10.1016/j.cstp.2025.101499**. Tên bài như bản tiền ấn. Trang mở trực tiếp trả 403, nhưng nội dung chỉ mục tìm kiếm của chính nhà xuất bản hiển thị đủ venue/tập/năm/DOI. Đã đọc PDF tiền ấn; chưa kiểm công thức 3/trang của bản cuối. Không thay metadata mà bỏ qua đối chiếu nội dung.
2. **Leonardi và cộng sự (2026).** [Trang Taylor & Francis](https://www.tandfonline.com/doi/abs/10.1080/23249935.2026.2650136) có tên **Data-driven assessment for the predictability of demand responsive transit**, *Transportmetrica A: Transport Science*, DOI **10.1080/23249935.2026.2650136**, accepted **18/03/2026**, online **01/04/2026**. Nội dung chỉ mục của trang nhà xuất bản cho các ngày trên; [IP Paris](https://researchportal.ip-paris.fr/en/publications/data-driven-assessment-for-the-predictability-of-demand-responsiv/) xác nhận tác giả/DOI nhưng trường trạng thái còn ghi Accepted/In press 01/01/2026, nên ưu tiên ngày nhà xuất bản. Chưa xác minh volume/issue/page cuối, không điền. Bản 2024 đã đọc vẫn là nguồn hợp lệ cho câu của chương.
3. **Hörl và Zwick (2022).** Có thể viết thêm tên hội nghị TRB vào bib thay cho chỉ “Conference paper, ETH Zurich Research Collection”. BIB hiện tại không gán venue sai; tên hội nghị là bổ sung tùy chọn từ trang của tác giả/cơ quan tác giả. Không đổi năm thành 2021 chỉ vì ngày nộp bản thảo.

## Sửa chính xác

### Mục AGZ trong `10-tai-lieu.tex`

```tex
\bibitem{alonsogonzalez2020}
M.~J. Alonso-González, N.~van Oort, O.~Cats, S.~Hoogendoorn-Lanser, and S.~Hoogendoorn.
\newblock Value of time and reliability for urban pooled on-demand services.
\newblock \emph{Transportation Research Part C: Emerging Technologies}, 115:102621, 2020.
\newblock \url{https://doi.org/10.1016/j.trc.2020.102621}
```

### DRE trong addendum 5

Thay đúng chuỗi:

> `(arXiv 2206.02127v1, 3 trang)`

bằng:

> `(arXiv 2206.02127v1, 9 trang)`

Chỉ nhãn chiều dài PDF sai; trang 1 và 3 được trích ở C2-15 vẫn tồn tại và không bị lỗi này làm sai.

### TLC: hai câu riêng

| Item | Phán định | Chứng cứ / câu thay thế |
|---|---|---|
| “Dữ liệu chuyến công khai … được công bố theo tháng, thường trễ khoảng hai tháng” | **ACCEPT / AGREE** | [Trang TLC](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page), phần Trip Record Data Download Links, dòng 41 trong bản công cụ mở; nguồn nêu rõ cả monthly và two-month delay cùng lý do chờ dữ liệu từ đơn vị cung cấp. Có thể giữ nguyên câu. |
| “Hồ sơ lập từ các ngày ngay trước … vì vậy giả định hãng xe có sẵn dữ liệu chuyến của chính mình” | **ACCEPT WITH CORRECTIONS / OVERSTATED nếu hiểu là suy ra duy nhất từ TLC** | Đây là giả định triển khai hợp lý, không phải kết quả của TLC: có thể dùng nguồn dữ liệu kịp thời khác, và thí nghiệm cục bộ là hồi cứu. Câu thay thế bên dưới giữ đúng giới hạn bằng chứng. |

Câu thay thế tiếng Việt đề nghị cho câu cuối (giữ câu TLC trước nó):

> Trong cách dùng gần thời điểm vận hành, hồ sơ từ vài ngày ngay trước chỉ có thể lập khi đơn vị vận hành có dữ liệu kịp thời; khóa luận giả định hãng xe có dữ liệu chuyến của chính mình.

Hoặc bản ngắn hơn, ít thêm suy luận hơn:

> Với hồ sơ lập từ các ngày ngay trước ở mục~\ref{muc:dubao}, khóa luận giả định hãng xe có sẵn dữ liệu chuyến của chính mình.

Câu ngắn bỏ liên từ “vì vậy”, đánh dấu rõ giả định, không biến lịch phát hành TLC thành bằng chứng về khả năng truy cập dữ liệu của một hãng xe cụ thể.