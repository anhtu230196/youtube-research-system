# Review vòng 1 — Codex

**Artifact:** `coordination/drafts/sys-skill-han-viet-suy-ngam.md` v1  
**Claim:** `sys-skill-han-viet-suy-ngam`

## Nhận xét

### D01 — CHAN

- **Chỗ nào:** `.claude/skills/ky-an-viet/references/mau-va-thuc-hanh.md:70`
- **Vấn đề gì:** Ví dụ 6 gọi người giả định là “hung thủ” và dùng đại từ “hắn”, dù dữ kiện chỉ cho thấy hiện trường đã bị đám đông làm xáo trộn. Cách viết này vừa tự gán giới tính, vừa mâu thuẫn với chính `giong-ke.md` về việc không gọi người chưa bị kết án là “hắn”, “ả”, “tên”. Đây là mẫu để người viết bắt chước nên có thể biến một nhánh giả thuyết thành quy tội ngầm.
- **Cần gì để đóng:** Đổi thành cách diễn đạt không gán giới tính hay tư cách phạm tội, chẳng hạn một người trong đám đông *có thể đã liên quan đến việc xáo trộn hiện trường*; chỉ dùng “hung thủ” nếu giới tính và việc có người gây án đã được nguồn xác lập.

### D02 — CHAN

- **Chỗ nào:** `.claude/skills/ky-an-viet/references/mau-va-thuc-hanh.md:70`
- **Vấn đề gì:** Câu “Chuyện đó chỉ giải thích được theo mấy hướng” trình bày ba khả năng như toàn bộ lời giải có thể có, trong khi dữ kiện hư cấu chỉ nói không thu được vân tay nạn nhân hay người khác. Chính dữ kiện đó chưa loại trừ giới hạn thu thập dấu vết, bề mặt không lưu vân tay, hoặc các giải thích bình thường khác. Điều này trái với quy tắc không biến suy luận thành sự thật.
- **Cần gì để đóng:** Đổi thành “có thể có vài cách giải thích”, và sửa nhánh bình thường để bao gồm cả giới hạn/độ tin cậy của dấu vết. Giữ rõ đây là khả năng của người kể, không phải kết luận pháp y.

### D03 — SUA

- **Chỗ nào:** `.claude/skills/ky-an-viet/references/thi-truong-viet-nam.md:15`; `t-i/outputs/YouTube-Research-System/AGENTS.md:56`
- **Vấn đề gì:** Quy tắc yêu cầu ghi chữ Hán và tra âm từ chữ Hán, nhưng chưa buộc chữ Hán đó phải lấy từ nguồn gốc hoặc nguồn có thẩm quyền. Khi hồ sơ chỉ có Romanization hay tên Latin chính thức, người viết vẫn có thể tự suy ngược chữ Hán rồi tạo ra một tên khác, làm sai danh tính.
- **Cần gì để đóng:** Bổ sung rằng chỉ chuyển Hán Việt khi chữ Hán được nguồn gốc/nguồn đáng tin xác nhận; nếu không xác minh được thì giữ nguyên cách viết Latin có trong hồ sơ và ghi rõ giới hạn trong kịch bản làm việc. Thêm cùng điều kiện này vào checklist.

### D04 — SUA

- **Chỗ nào:** `.claude/skills/ky-an-viet/references/giong-ke.md:63`
- **Vấn đề gì:** Đoạn suy ngẫm cho phép nêu “lòng tham”, “tin người chỉ vì quen mặt”, hoặc “tự hợp lý hoá” như cơ chế vụ án cho thấy. Ba điều kiện hiện có vẫn không buộc cơ chế đó phải gắn với claim đã xác lập; vì vậy động cơ hoặc tâm lý chỉ là suy luận vẫn có thể bị đóng khung thành bài học từ vụ án.
- **Cần gì để đóng:** Yêu cầu mỗi cơ chế hành vi phải truy được về chi tiết/claim established đã có trong tập và được diễn đạt theo mức chắc chắn của nguồn. Nếu chỉ có suy đoán về động cơ, chỉ giữ phần hệ quả con người, không gọi đó là cơ chế vụ án đã chứng minh.

## Phần đã kiểm

Ngoại lệ T1 ở `.claude/skills/ky-an-viet/references/giong-ke.md:45` được giới hạn đúng vào suy nghĩ do chính nhân vật kể lại; Ví dụ 5 cũng cấm suy ý nghĩ từ hành động. Phần này giữ được ranh giới chứng cứ nếu các điểm trên được sửa.

## Tôi đã không kiểm cái gì

Tôi chưa chạy kiểm thử hành vi với người viết hay TTS, chưa đối chiếu cách đọc từng tên Hán Việt với nguồn ngôn ngữ gốc, và chưa kiểm chứng các ví dụ hư cấu bằng một tập thật. Vì vậy tôi không kết luận được các hàng rào mới có được áp dụng nhất quán khi sản xuất hay không.

```points
D01 | mở | .claude/skills/ky-an-viet/references/mau-va-thuc-hanh.md:70 | Nhánh giả thuyết dùng “hung thủ/hắn”, tự gán giới tính và quy tội ngầm
D02 | mở | .claude/skills/ky-an-viet/references/mau-va-thuc-hanh.md:70 | “Chỉ giải thích được” biến ba khả năng thành lời giải bao quát không có chứng cứ
D03 | mở | .claude/skills/ky-an-viet/references/thi-truong-viet-nam.md:15 | Chưa buộc chữ Hán dùng để chuyển Hán Việt phải được nguồn xác nhận
D04 | mở | .claude/skills/ky-an-viet/references/giong-ke.md:63 | Đoạn suy ngẫm chưa buộc cơ chế tâm lý phải bám claim established
```