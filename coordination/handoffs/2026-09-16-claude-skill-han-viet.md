# Bàn giao: sys-skill-han-viet-suy-ngam — Claude → người dùng skill

**Ngày:** 2026-09-16. **Nhánh làm việc:** không dùng, commit thẳng lên `main`. **Claim:** `sys-skill-han-viet-suy-ngam`.

## Đã làm

Bốn thay đổi Tú chốt sau lượt rà skill ngày 2026-09-15, đối chiếu với mẫu Cẩm Tân Đại Lâu / mất tích đêm Trung thu:

1. Cho phép kể suy nghĩ nhân vật khi nguồn có lời khai, kèm Ví dụ 5.
2. Tên người và địa danh gốc Hán dùng âm Hán Việt, chỉ chuyển khi chữ Hán có trong nguồn; kịch bản làm việc giữ chữ Hán.
3. Đoạn kết được thêm một đoạn suy ngẫm ngắn, có ba điều kiện và một cặp ví dụ ranh giới.
4. Mục mới "Mở nhánh giả thuyết" trong kiến trúc câu chuyện, kèm Ví dụ 6.

## File liên quan

| Đường dẫn | Trạng thái |
| --- | --- |
| `.claude/skills/ky-an-viet/references/` — `giong-ke.md`, `mau-va-thuc-hanh.md`, `kien-truc-cau-chuyen.md`, `thi-truong-viet-nam.md`, `ban-thu-am.md` | Hoàn tất, bản 2 sau review |
| `.agents/skills/ky-an-viet/references/` | Bản sao, trùng từng byte |
| `t-i/outputs/YouTube-Research-System/AGENTS.md` dòng 56 | Quy tắc tên theo quyết định 2026-09-16 |
| `coordination/drafts/sys-skill-han-viet-suy-ngam.md` | Bản 2, có mục "Sửa sau vòng 1" |
| `coordination/threads/sys-skill-han-viet-suy-ngam/` | Vòng 1 Codex và Gemini, lượt trả lời của tác giả |

## Chưa kiểm chứng

- **Không chạy kiểm thử hành vi nào.** Cả ba agent đều nêu cùng giới hạn này. Chưa biết Ví dụ 5 có khiến người viết kể suy nghĩ khi nguồn chỉ ghi hành động không, và chưa biết luật "nhánh nào mở ra phải đóng lại" có giữ được khi chỗ mở và chỗ đóng cách nhau xa trong một tập thật không.
- **Bốn bản sửa sau review chưa có mắt thứ hai.** Tú quyết định đóng luồng sau vòng 1, nên D01–D04 được chốt ở lượt tác giả.
- Chưa dùng quy tắc tên Hán Việt trên tập thật; kênh chưa có tập nào là vụ Đài Loan hay Trung Quốc.
- Chưa nghe audio, không có số liệu giữ chân.
- Hai sửa đổi có sẵn trong working copy ở `giong-ke.md` (nhấn chi tiết pháp y khi nó lật mâu thuẫn lời khai; nới một phần lệnh cấm bài học đạo đức) chưa xác định được của ai. Đã giữ sửa đổi thứ nhất, viết chồng lên sửa đổi thứ hai.

## Một lỗi công cụ phát hiện trong lúc làm

`scripts/orchestrate.py` truyền prompt qua dòng lệnh. Trên Windows, các CLI agent đều là shim `.cmd` nên `cmd.exe` cắt dòng lệnh tại ký tự xuống dòng đầu tiên: mọi lượt tự động trước đây chỉ nhận được dòng đầu của prompt. Đã sửa ở `0ee7b95` bằng cách cho agent khai `prompt_via=stdin`; Codex dùng `-`. Đã kiểm lại: lượt review chạy 129 giây, rollout chứa đủ prompt, file vòng trả về bốn điểm.

**Còn tồn:** `claude` và `agy` vẫn truyền prompt qua argv nên vẫn dính lỗi. Cần đo từng CLI trước khi sửa, không suy đoán.

## Bước kế tiếp khi dùng skill

Đọc `SKILL.md`, rồi `giong-ke.md` và `mau-va-thuc-hanh.md` khi viết câu, `kien-truc-cau-chuyen.md` khi dựng khung. Lần đầu dùng mục mở nhánh và đoạn suy ngẫm trên một tập thật thì ghi lại chỗ không khớp thực tế để sửa skill.

## Quyết định của người dùng

Không có câu hỏi nào đang chờ Tú để hoàn tất phần skill. Còn hai việc Tú chưa trả lời, không chặn gói này: hai sửa đổi có sẵn trong `giong-ke.md` có phải của Tú không, và việc hạ model Codex từ `gpt-6-astra` xuống `gpt-5.6-terra` có phải của Tú không.
