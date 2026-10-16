from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ORIGINAL = ROOT.parent.parent / 'ridebound' / 'noi-dung' / '07-chuong3.tex'
TARGET = ROOT / 'source' / 'noi-dung' / '07-chuong3.tex'
s = ORIGINAL.read_text(encoding='utf-8')

def span(start, end, replacement):
    global s
    a = s.index(start)
    b = s.index(end, a)
    s = s[:a] + replacement + '\n\n' + s[b:]

s = s.replace(r'\chapter{Lời hứa có biên được chứng nhận}',
              r'\chapter{Lời hứa có biên và các điều kiện bảo đảm}\label{ch:phuongphap}')
span('Chương này trình bày', r'\section{Mô hình bài toán mở rộng}', r'''Chương này trả lời RQ1 bằng cách xác định đại lượng được ghi sổ, thời điểm kiểm tra và phạm vi
của chứng nhận. Từ đó, chương xây dựng khung bốn họ cổng để trả lời phần lý thuyết của RQ3.
Các bảo đảm đều có giả thiết; chúng không thay thế việc đo chất lượng dịch vụ và các biến động
mà hành khách thực sự nhìn thấy ở Chương~\ref{ch:thucnghiem}.

\section{Tổng quan cơ chế}

RideBound công bố giờ đón và giờ trả dự kiến cho khách đã nhận. Mỗi khi công bố lại, độ dời
được ghi vào sổ cái riêng của khách. Sổ cái chỉ tăng; phương án làm vượt trần cứng bị loại
trước khi bộ chọn đội xe giải bài toán quy hoạch nguyên.

Điểm cần lựa chọn là độ dời nào được tính. Khóa luận so phương án mới với tuyến giữ nguyên
trên cùng trạng thái hiện tại. Phần chênh giữa hai phép chiếu là phần do quyết định. Phần
chênh giữa tuyến giữ nguyên và giờ đã báo là phần thay đổi khi giữ tuyến. Một trần trên phần
thứ nhất không đồng nghĩa trần trên toàn bộ biến động khách nhìn thấy.

Một quyết định có miễn trừ vẫn có thể tiếp tục phục vụ khách nhưng phải ghi vi phạm và không
được gắn nhãn vận hành bình thường. Đây là một phần của phạm vi chứng nhận, không phải một
cách biến lời hứa đã vượt trần thành lời hứa được giữ.''')
s = s.replace('Mở rộng mô hình ở mục 2.1,', 'Mở rộng mô hình bài toán ở Chương 2,')
span('Trên panel thực nghiệm, trường hợp này', r'\subsection{Ví dụ minh họa}', r'''Đây là giới hạn của sổ cái đối xứng. Bộ sinh chèn thuần trong các phép so chính chưa dùng
sửa chữa kéo giờ hẹn về sớm hơn mốc giữ tuyến. Kết quả ấy là đặc điểm của bộ sinh và dữ liệu,
không làm mất phản ví dụ. Một sổ cái chỉ tính phần gây hại cần định nghĩa và đánh giá riêng.''')
span(r'\begin{table}[htbp]'+'\n'+r'\centering'+'\n'+r'\caption{Ba mốc', 'Với phương án đổi kế hoạch', r'''\begin{figure}[htbp]
\centering
\includegraphics[width=0.95\linewidth]{hinh/co-che-ba-moc.pdf}
\caption{Ví dụ dựng để giải thích ba mốc: tuyến giữ nguyên trễ 40 giây, phương án mới thêm
30 giây. Sơ đồ này không phải một quan sát thực nghiệm.}
\label{hinh:bamoc}
\end{figure}
Hình~\ref{hinh:bamoc} dùng giờ đã báo làm gốc để minh họa phép đối chiếu.''')
s = s.replace('nên phương án này luôn hợp lệ.', 'nên riêng cổng hành vi không loại phương án này nếu sổ cái trước đó hợp lệ.')
s = s.replace('Ba đặc điểm của sổ cái này cần được nhấn mạnh vì chúng là chỗ khác biệt so với văn liệu.',
              'Ba đặc điểm sau xác định chính xác cơ chế được kiểm trong khóa luận.')
s = s.replace('Tương ứng với nghĩa vụ\nphương tiện trong mục 2.4.', '')
s = s.replace('Tương ứng với nghĩa vụ kết quả.', '')
s = s.replace('``tôi làm bạn trễ thêm bao nhiêu so với lẽ ra bạn đã bị''.',
              'độ lớn phần khác biệt giữa phương án mới và tuyến giữ nguyên, gồm cả chiều sớm lẫn muộn.')
s = s.replace('``bạn trễ bao nhiêu so với điều tôi đã nói''.',
              'độ lớn thay đổi giữa giờ mới và giờ đã công bố, gồm cả chiều sớm lẫn muộn.')
span(r'\paragraph{Độ khít đo được ở mức từng lần công bố.}', r'\subsection{Ba định lý}', r'''\paragraph{Phạm vi của phép đối chiếu.}
Mốc $e$ được dựng trên trạng thái sau khi lô sự kiện đã được áp dụng. Vì vậy $d$ có thể gồm
cập nhật thời gian đi, tiến độ thực, thời gian dừng và độ trễ thực thi. Không được gọi nó là
tác động thuần của giao thông. Tuyến đã chọn trước đó cũng ảnh hưởng vị trí xe hiện tại,
nên $d$ không được giả định độc lập với chính sách.

Phép đối chiếu là một cách hạch toán trong mô hình, tại cùng trạng thái, không phải một ước
lượng tác động nhân quả tổng thể của việc đổi chính sách. Dấu bằng trong~\eqref{eq:phanra}
phải được kiểm, không được giả định. Các tỉ số giữa tổng phần do quyết định và tổng biến
động nhìn thấy ở mục~\ref{muc:quytrach} có tử số, mẫu số rõ ràng; chúng không phải các tỉ
trọng của một phân rã cộng tính luôn đúng.

\paragraph{Điều kiện ngân sách trước quyết định (B).}
Sổ cái được khởi tạo bằng không, cấu hình trần không bị hạ xuống giữa chuỗi, và các lần công
bố trước đều qua cổng trong vận hành bình thường. Khi đó ngân sách trước quyết định không
vượt trần. Các định lý giữ tuyến dưới đây cần điều kiện (B); không áp dụng nguyên trạng cho
một sổ cái đã vượt trần sau miễn trừ.''')
s = s.replace(r'\begin{dinhly}[Cơ sở hành vi không bao giờ loại phương án không làm gì]',
              r'\begin{dinhly}[Cổng hành vi giữ tuyến dưới điều kiện ngân sách]')
s = s.replace('Dưới cơ sở hành vi, ràng buộc cam kết không bao giờ loại phương án không làm gì, nên nó không bao\ngiờ tự làm rỗng tập phương án của một xe.',
              'Dưới điều kiện (B), cổng ngân sách hành vi không loại phương án giữ tuyến. Nếu phương án đó\ncũng qua mọi kiểm tra khác, tập phương án sau cổng không rỗng.')
s = s.replace('Giả sử điều kiện \\emph{(H)}:',
              'Giả sử hai cơ sở dùng cùng phép chiếu, thông tin và các ràng buộc khác. Giả sử điều kiện \\emph{(H)}:')
span(r'\paragraph{Điều kiện (H) và mức độ nó đúng.}', r'\begin{hequa}[Dải khác biệt', r'''\paragraph{Phạm vi của quan hệ bao hàm.}
Điều kiện (H) không là hệ quả của bất đẳng thức tam giác. Khi phần thay đổi giữ tuyến hấp thụ
một phần cú đẩy do quyết định, $A>B$ có thể xảy ra. Quan sát của panel chính thực sự có vi
phạm, báo ở mục~\ref{muc:quytrach}. Kiểm trên phương án đã chọn cũng không chứng minh điều
kiện trên mọi phương án. Vì vậy định lý không được dùng như kết luận về panel.

Định lý so tập quỹ đạo và chính sách tối ưu toàn quỹ đạo. Bộ chọn đang cài chỉ tối ưu ở từng
kỷ nguyên, không nhìn trước yêu cầu tương lai. Chọn một phương án khác hôm nay có thể làm
trạng thái ngày mai khác đi, nên một cấu hình chặt hơn vẫn có thể tình cờ hoàn tất nhiều
khách hơn ở một ô. Phần thực nghiệm phải kiểm riêng, không suy trực tiếp từ định lý.''')
span('Hệ quả này chỉ nói về', r'\subsection{Khung so sánh bốn họ cổng}', r'''Hệ quả chỉ so một lần công bố khi hai sổ cái bằng nhau. Trên cả chuỗi, sổ cái có thể tách
nhau và các chính sách đi quỹ đạo khác nhau. Nó không cho một công thức dự báo chênh số khách.''')
span(r'\paragraph{Phạm vi của định lý và giả thiết (N).}', r'\paragraph{Quỹ đạo dự phòng.}', r'''\paragraph{Phạm vi và giả thiết (N).}
Gọi (N) là giả thiết phương án giữ tuyến tại kỷ nguyên đang xét đã qua mọi kiểm tra ngoài
cổng thời gian đang so, gồm cấu trúc tuyến, sức chứa, lịch trình và các khóa khác. Cổng
ngân sách không thay thế tính khả thi vật lý. Nếu xe tới đón ngoài cửa sổ đã chấp nhận,
một bất biến vòng đời vẫn có thể làm lần chạy dừng. Đây là giới hạn đã xuất hiện trong
thực nghiệm; mục~\ref{muc:tang2} phân loại các lần dừng theo nguyên nhân.

Việc danh mục phương án yêu cầu tuyến giữ nguyên cũng là một lựa chọn cài đặt. Trong chiều
trôi thuận lợi, một cổng có thể loại tuyến giữ nguyên nhưng vẫn giữ phương án khác; không
được coi mọi lần tuyến giữ nguyên bị loại là một chứng minh tập toán học hoàn toàn rỗng.''')
s = s.replace('Giả sử (N). Xét một hành khách.', 'Giả sử (B) và (N). Xét một hành khách.')
span('Phần (a) chính là Định lý', r'\begin{hequa}[Khi thời gian đi tất định]', r'''Phần (a) dựa vào $p=e$ của tuyến giữ nguyên và ngân sách trước đó hợp lệ. Phần (b) so các
ngưỡng trên cùng quỹ đạo dự phòng, không so số khách của các nhánh đã chọn tuyến khác nhau.
Chứng minh sơ cấp; khung này có ích vì phân biệt các lời hứa cùng đơn vị giây và tạo dự
đoán kiểm được từ chuỗi công bố. Trong bốn họ đang xét, chỉ $C$ không tính phần trôi vào
ngân sách. Điều đó không phải bảo đảm hệ thống luôn chạy trọn hay khách không thấy đổi giờ.''')
span('Trong mô hình của Schulz và Pfeiffer,', r'\begin{hequa}[Phụ thuộc chiều trôi]', r'''Thời gian đi cố định chưa đủ để suy ra $x_t=0$: tiến độ thực thi và phép chiếu cũng phải
nhất quán. Panel mạng tĩnh của khóa luận vẫn có trôi nhỏ do mô phỏng rời rạc. Vì vậy hệ quả
là một trường hợp lý tưởng của mô hình; việc áp dụng cần kiểm biên bản.''')
span('Hệ quả này là chỗ làm cho định lý', r'\subsection{Khi nào chặn theo chuỗi', r'''Trên hệ thật, phần giữ tuyến có thể đổi dấu và không chỉ gồm giao thông. Dự đoán theo ô
phải tính trên chuỗi đo được của từng khách. Khi trôi thuận lợi, hạn chót một chiều có thể
cho phép chèn thêm bằng phần chùng vừa tạo ra, còn cổng hành vi vẫn tính đủ độ dời do quyết
định. Đây là khả năng đánh đổi, không phải ưu thế dịch vụ của một họ đã được chứng minh.''')
span('Giả thiết thứ nhất của mệnh đề,', r'\section{Các cơ chế bảo vệ bổ sung}', r'''Kết quả này giới hạn cách phát biểu đóng góp. Trong bộ sinh chèn thuần với trôi nhỏ, trần
cộng dồn hành vi gần với trần độ muộn hai đầu. Khóa luận không dùng sự khác nhau giữa hai
hình thức như lợi thế đã được chứng minh độc lập với bộ sinh.

Hai ví dụ dựng tách hiệu hai đầu khỏi độ dài chuỗi. Chuỗi $600\to660\to600$ có $E=0$ nhưng
$V=120$ giây; chuỗi $600\to660\to720$ có $E=V=120$ giây. Ghi nhận dao động không đồng nghĩa
đã đo được tổn thất hài lòng; khóa luận không có dữ liệu lựa chọn hay cảm nhận của hành khách.''')
span(r'\section{Các cơ chế bảo vệ bổ sung}', r'\section{Kiến trúc cài đặt}', r'''\section{Các khóa và cơ chế bảo vệ bổ sung}

Khóa cứng cấm đổi một trường lời hứa trong pha được cấu hình. Hàng rào đóng băng cấm đổi khi
giờ đón còn cách hiện tại dưới một ngưỡng. Cơ chế một chiều cho phép giờ dự báo tốt lên nhưng
cấm xấu đi so với mốc tham chiếu được chọn. Đây là những hình thức có tiền lệ trong văn liệu,
không phải các khái niệm mới của khóa luận.

Các cấu hình này phải được đọc cùng bộ sinh phương án. Nếu bộ sinh không thể làm giờ hẹn
tốt lên, quyền cho phép cải thiện không tạo thêm lựa chọn. Ngược lại, một bộ sinh biết sửa
tuyến có thể làm cơ chế một chiều khác với khóa hai chiều. Mục~\ref{muc:kiemtraphu} báo các
quan sát phụ trong phạm vi cài đặt đã thử.

\section{Chứng nhận và phục hồi có miễn trừ}
\label{muc:phuchoi}

\subsection{Phạm vi của chứng nhận}

``Được chứng nhận'' ở đây nghĩa là quyết định có bằng chứng kiểm tra gắn với phiên bản,
cấu hình và lịch sử lời hứa. Chứng cứ ghi giá trị trước, độ dời, giá trị sau và các lý do
loại hoặc miễn trừ. Nó không phải chứng nhận pháp lý, bảo đảm thời gian đến thật, hay chứng
minh hình thức tính đúng của toàn bộ chương trình.

Quyết định có miễn trừ được đánh dấu \texttt{normalOperation=false}. Nó có thể được thực thi
để tiếp tục phục vụ khách đã nhận, nhưng không được tính là giữ lời hứa của cổng bị vượt.
Tỉ lệ quyết định có miễn trừ và tỉ lệ khách vượt lời hứa có mẫu số khác nhau, phải báo riêng.

\subsection{Hai quy tắc phục hồi}

\textbf{Quy tắc (a), giữ tuyến.} Xe có tuyến tham chiếu đã vượt ngân sách hoặc hạn chót vẫn
đi tuyến đó, với vi phạm được ghi nhận có kiểu. Quy tắc có thể làm giảm cơ hội nhận khách
mới vì xe bị hạn chế đổi tuyến. Việc tiếp tục chạy không biến vi phạm thành tuân thủ.

\textbf{Quy tắc (b), không tệ hơn tham chiếu.} Xe bị vướng được đổi tuyến trên cùng xe chỉ
khi từng cổng được xin miễn trừ cũng bị tuyến giữ nguyên vi phạm và phương án mới không
tệ hơn ở đúng cổng ấy. Với cận muộn, giờ trả mới không muộn hơn mốc giữ tuyến; với cận sớm,
nó không sớm hơn. Với chiều ngân sách, giá trị sau không lớn hơn giá trị sau của tham chiếu
đã vượt trần.

Miễn trừ không áp cho khóa pha, đổi xe hoặc ràng buộc vật lý. Khách mới vẫn phải qua các
cổng thông thường. Nếu một chiều khác phát sinh vi phạm mà tham chiếu chưa có, phương án
không qua quy tắc (b). Chỉ các chiều ngân sách thuộc miễn trừ được bỏ khỏi tầng xếp hạng
mức sử dụng; các chiều còn lại vẫn được kiểm và xếp hạng.

Quy tắc (b) được thêm sau niêm phong phép quét đầu, nên đối chiếu (a)/(b) là phân tích bổ
sung. Các kế hoạch W07, W07X và T38 về sau đã cố định (b) trước khi chạy những nhánh được
dự đoán. Quy tắc có thể cho khách mới lên xe đang có miễn trừ, nên không trùng mọi điều kiện
của quy trình cũ. Việc tính lại tham chiếu chưa được phản ánh đầy đủ trong bộ đếm
\texttt{validationWorkUnits}; khóa luận không tuyên bố hai cách phục hồi có chi phí tính
toán bằng nhau.

\subsection{Biên nhìn thấy có điều kiện}
\label{muc:biendukien}

Vì $V_r\le C_r+X_r$, nếu cổng hành vi giữ $C_r\le\beta$ và một ô có
$S_j=\max_r X_r\le\gamma$, thì mọi khách được xét trong ô ấy có
\begin{equation}
V_r\le\beta+\gamma.
\label{eq:biendukien}
\end{equation}
Đây là suy luận tất định có điều kiện trên $S_j$, không phải bảo đảm $S_j$ luôn nhỏ. $X_r$
được đo trên quỹ đạo thực thi; không lấy từ một nhánh khác mà không kiểm tra.

T38 cố định $C$-30 rồi hiệu chỉnh $\gamma$ trên các ô riêng. Điểm ô là tổng biến động khi
giữ tuyến lớn nhất theo khách. Khách đã được hứa mà không hoàn tất làm điểm bằng vô hạn.
Với $n$ điểm hiệu chỉnh và mức danh nghĩa $1-\alpha$, chỉ số thứ tự là
$k=\lceil(n+1)(1-\alpha)\rceil$; giá trị thứ $k$ được đóng băng trước tập kiểm tra. Không
được cắt ngưỡng lớn hoặc thay điểm vô hạn bằng một số hữu hạn thuận tiện.

Cách hiệu chỉnh theo thứ tự thường gắn với lập luận độ phủ dưới tính hoán đổi được của các
điểm. T38 có khung giờ không đồng nhất và ô chung ngày, mẫu, nên khóa luận chỉ báo độ phủ
thực nghiệm trên tập giữ lại. Biên chưa là bảo đảm phân phối tự do cho ngày vận hành mới.
Mục~\ref{muc:t38} phân biệt điểm vượt $\gamma$ với $V$ thật vượt $\beta+\gamma$, vì hai
sự kiện không đồng nhất.''')
span(r'\section{Kiến trúc cài đặt}', '\\subsection{Sinh phương án theo lối chèn}', r'''\section{Cài đặt và dấu vết tái lập}
\label{muc:caidat}

RideBound được cài bằng C\# trên .NET. Bảng~\ref{bang:kientruc} mô tả trách nhiệm các lớp;
số dòng mã không được dùng như thước đo đóng góp. Domain và Application độc lập với
FleetPy, EF Core, ASP.NET và OR-Tools. Các adapter gọi cùng runner có phiên bản, không
cài lại thuật toán điều phối trong Python.

\begin{table}[htbp]
\centering
\caption{Trách nhiệm các thành phần của RideBound}
\label{bang:kientruc}
\begin{tabularx}{\linewidth}{@{}lX@{}}
\toprule
\textbf{Thành phần} & \textbf{Trách nhiệm}\\
\midrule
Domain & Lời hứa, vector, sổ cái, vòng đời và bất biến nghiệp vụ.\\
Application & Áp sự kiện, đối chiếu ba mốc, kiểm quyết định, ghi chứng cứ.\\
Algorithms & Sinh phương án, đánh giá ứng viên, hồ sơ mục tiêu.\\
Solvers.OrTools & Cầu nối tới bộ giải quy hoạch nguyên của OR-Tools.\\
Contracts và Runner & Giao thức có phiên bản, phiên chạy, tuần tự hóa trạng thái.\\
Benchmarking & Chuẩn hóa dữ liệu, dựng đầu vào và kiểm thực nghiệm.\\
Adapter FleetPy & Đổi sự kiện, hành động giữa mô phỏng và runner.\\
\bottomrule
\end{tabularx}
\end{table}

\texttt{PromiseDeltaCalculator} tính ba cặp mốc. \texttt{CommitmentBudgetEvaluator} cộng
vector và kiểm trần theo pha. \texttt{CommitmentDecisionValidator} kiểm cả khóa, hạn chót
và miễn trừ; \texttt{NoWorseReference} đối chiếu đúng cận hoặc chiều đang vượt. Việc tách
trách nhiệm cho phép kiểm toán đại lượng được tính phí mà không đổi bộ mô phỏng.

FleetPy phiên bản 1.0.2 là nền mô phỏng dùng cho các phép so~\cite{fleetpy2022}. Adapter
truyền trạng thái và hành động tới runner; kết quả được ghim vào cả phiên bản adapter lẫn
runner, không chỉ vào tên thuật toán.''')
span(r'\subsection{Chứng cứ niêm phong}', '\n\n\n' if '\n\n\n' in s[s.index(r'\subsection{Chứng cứ niêm phong}'):] else '\x00', '') if False else None
a = s.index(r'\subsection{Chứng cứ niêm phong}')
s = s[:a] + r'''\subsection{Chứng cứ niêm phong}

Biên bản đầy đủ lưu NDJSON, dữ liệu base64 và SHA-256 của từng khung trao đổi. Điểm kiểm tra
cuối giữ lịch sử lời hứa và trạng thái yêu cầu. Băm runner, cấu hình, đầu vào và cây mã nguồn
ghim kết quả vào đúng phiên bản. Băm ngữ nghĩa và tóm lược công bố hỗ trợ so các lần chạy
giống nhau trong phạm vi dữ liệu được băm; không được nói mọi khác biệt hành vi tất yếu đổi
mọi loại băm.

Tái lập cần đủ phiên bản runner, dữ liệu chuẩn hóa, cấu hình và script phân tích. Các đợt
đổi runner hoặc quy tắc mô phỏng được báo riêng. Thử lại sau lỗi hạ tầng phải theo quy tắc
đã ghi, giữ thư mục lỗi và chỉ rõ bản dùng. Các kiểm tra này hỗ trợ tin cậy của phép so;
chúng không xóa giới hạn về quy mô, nguồn dữ liệu hay giả thiết thống kê.
'''
s = s.replace('Hệ thống cũng cài đặt một cơ chế \\emph{chứng chỉ độ trễ}', 'Hệ thống cũng cài đặt một cơ chế \\emph{chứng chỉ độ trễ}')
TARGET.write_text(s, encoding='utf-8')
print('method characters', len(s), 'original', len(ORIGINAL.read_text(encoding='utf-8')))
