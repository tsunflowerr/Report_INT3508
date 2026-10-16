import json
from pathlib import Path
root = Path(__file__).parent
p = root / 'reading-progress.json'
data = json.loads(p.read_text(encoding='utf-8-sig'))
data['readChunks'] = sorted(set(data['readChunks']) | set(range(69,96)) | {167,168,169,170,171,172})
data['next'] = next(i for i in range(1,179) if i not in data['readChunks'])
data['note'] = 'Full chunks read as explicitly enumerated; remaining chunks are not claimed read. Core production, FleetPy and RidePy production reviewed; tests/research tooling still in progress.'
p.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
plan = root / 'KE-HOACH-END-TO-END-CONDUCT-OUTCOME-STOCHASTIC.md'
s = plan.read_text(encoding='utf-8-sig')
s = s.replace('Chọn pickup ETA là primary coordinate trước boarding và drop ETA là secondary/onboard coordinate; chốt có hai ngân sách độc lập hay một weighted norm.', 'Ưu tiên đánh giá drop-off ETA làm primary coordinate ứng viên vì kết quả cũ cho thấy pickup có thể ít cơ hội thay đổi; kiểm tra cơ hội quyết định trong pilot và khóa endpoint theo câu hỏi nghiên cứu trước test. Pickup ETA là secondary coordinate trước boarding, đóng băng tại actual pickup. Chốt có hai ngân sách độc lập hay một weighted norm.')
plan.write_text(s, encoding='utf-8')
