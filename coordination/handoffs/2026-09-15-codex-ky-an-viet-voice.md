# Bàn giao: sys-skill-ky-an-viet — Codex → người dùng skill

**Ngày:** 2026-09-15. **Nhánh làm việc:** `codex/ky-an-viet-voice`. **Claim:** `sys-skill-ky-an-viet`.

## Đã làm

Cập nhật skill hiện có cho giọng kể kỳ án tiếng Việt tự nhiên theo yêu cầu của Tú: người và hành động cụ thể, nhịp đoạn liền mạch, mạch manh mối, người kể xuất hiện khi có ích, giữ giới hạn chứng cứ. Thêm bốn ví dụ thực hành và đồng bộ bản `.agents` với thư viện chung `.claude`. Giữ nguyên gợi ý, chống trùng, nghiên cứu, registry và các tập đang làm.

## File liên quan

| Đường dẫn | Trạng thái |
| --- | --- |
| `.claude/skills/ky-an-viet/SKILL.md` và `references/` | Hoàn tất; gói bản 3 đã qua review, không còn điểm mở |
| `.agents/skills/ky-an-viet/` | Bản sao để Codex đọc |
| `t-i/outputs/YouTube-Research-System/STORYTELLING.md` | Bản 4 bổ sung phần áp dụng giọng kể |
| `coordination/drafts/sys-skill-ky-an-viet-voice.md` | Phạm vi, chẩn đoán và kết quả thử có giới hạn |
| `coordination/threads/sys-skill-ky-an-viet-voice/` | Lượt Claude review độc lập, phản hồi tác giả và dữ kiện/đầu ra thử |

## Chưa kiểm chứng

- Chưa thử trọn một tập tiếng Việt, nghe audio hoặc có dữ liệu giữ chân. Bài thử ngắn không chứng minh giọng mới hấp dẫn hơn bản cũ trên cả tập.
- Một lượt mới đã thêm chủ thể hành động mà baseline không thêm; sau quy tắc bổ sung, lượt kiểm lại cùng bộ dữ kiện không lặp lỗi. Chưa thử quy tắc chặn trên bộ khác.
- Claude chưa đối chiếu transcript attachment. Không coi phần quan sát từ mẫu là đã được review nguồn độc lập. Riêng chẩn đoán trên NET-0006 đã được Claude đọc và kiểm lại ở vòng 2.
- Các đầu ra thử chưa kiểm hiệu quả của xưng hô; đề thử có một mốc “buổi sáng” chưa rõ thuộc ngày nào. Không chấm tiến bộ từ điểm đó.

## Kiểm tra và hoàn tất

Quick_validate cho cả hai bản skill đạt. Kiểm cuối sau khi review chốt: cả chín file skill trùng từng byte; 32 liên kết cục bộ hợp lệ; registry, episodes, scripts, hướng dẫn chọn vụ và nghiên cứu không đổi; ba lệnh registry/claims/thread đều qua; git diff không có lỗi khoảng trắng. Bài thử được giữ nguyên, không sửa đầu ra để làm đẹp kết quả.

Luồng review đã `settled` sau ba vòng Claude, không còn điểm mở. Vòng 3 hoàn tất nội dung nhưng tiến trình bao ngoài bị timeout sau một gián đoạn dài, nên chưa ghi được file vòng. Codex khôi phục **nguyên văn thông điệp cuối của Claude** từ session `2155180a-006b-4363-8044-ca32fba995ec` vào `r3-01-review-claude.md`, xác nhận có quyết định D11, rồi dùng `thread.py apply` cập nhật luồng. Không tự viết nhận xét thay Claude hoặc sửa trực tiếp `THREAD.md`.

## Bước kế tiếp khi dùng skill

Đọc `SKILL.md`, hướng dẫn giọng kể và tài liệu thực hành khi viết/sửa câu. Nộp bản tiếng Việt đầy đủ để Tú duyệt theo quy trình hiện hành. Với yêu cầu không lược chi tiết, đối chiếu giữ đủ thông tin; không sửa artifact đang đóng băng ngoài lượt.

## Quyết định của người dùng

Không có câu hỏi cần Tú trả lời để hoàn tất cập nhật skill. Xưng hô mình–các bạn chỉ là lựa chọn biên tập thử khi sổ còn trống; phải ghi rõ ngay lúc nộp bản bước 5 hoặc trích đoạn. `narrator_voice: null` vẫn đúng. Khi Tú thật sự chốt xưng hô, mới cập nhật sổ theo quy trình; không có việc bắt buộc thêm sự kiện cấu hình chỉ vì hướng dẫn biên tập lên bản 4.
