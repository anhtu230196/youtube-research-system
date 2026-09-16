---
id: sys-skill-han-viet-suy-ngam
agent: claude
branch: claude/skill-han-viet
status: done
opened: 2026-09-16
updated: 2026-09-16
scope:
  - .claude/skills/ky-an-viet/
  - .agents/skills/ky-an-viet/
  - t-i/outputs/YouTube-Research-System/AGENTS.md
  - coordination/threads/sys-skill-han-viet-suy-ngam/
  - coordination/drafts/sys-skill-han-viet-suy-ngam.md
  - coordination/handoffs/2026-09-16-claude-skill-han-viet.md
---

# sys-skill-han-viet-suy-ngam — Ba thay đổi Tú chốt ngày 2026-09-16 cho skill kỳ án tiếng Việt

**Làm gì:** Ba điểm Tú duyệt sau lượt rà skill so với mẫu Cẩm Tân Đại Lâu / mất tích đêm Trung thu:

1. **T1** — thêm ví dụ kể suy nghĩ nhân vật khi nguồn có lời khai, kèm câu luật tương ứng trong hướng dẫn giọng kể.
2. **S1** — tên người và địa danh gốc Hán dùng âm Hán Việt, kịch bản làm việc giữ chữ Hán để đối chiếu. Sửa cả luật nghiệp vụ `t-i/outputs/YouTube-Research-System/AGENTS.md` vì quy tắc "tên người giữ chữ viết gốc" nằm ở đó.
3. **Phương án B cho đoạn kết** — cho phép một đoạn suy ngẫm ngắn rút từ dữ kiện vụ án, không giảng đạo, không đổ lỗi cho nạn nhân.
4. **Mở nhánh giả thuyết** — Tú bổ sung ngày 2026-09-16: mục mới trong `kien-truc-cau-chuyen.md` cùng một ví dụ, dạy cách nêu nhiều khả năng thay vì kết luận, chạy bằng dữ kiện đã xác lập.

**Không đụng tới:** `registry.json` và trạng thái các case; `episodes/` và kịch bản NET-0006 đang trong luồng review khác; `STORYTELLING.md`; các skill khác trong `.claude/skills/`; skill toàn cục `~/.codex/skills/` và plugin của Claude; cấu hình model.

**Ghi chú:** Bước 7 theo bảng ở `AGENTS.md` mục 8 — tác giả Claude. Người review: Codex và Gemini, Tú chỉ định thêm Gemini so với bảng mặc định. Trong working copy đã có sẵn hai sửa đổi chưa commit ở `giong-ke.md` (nhấn chi tiết pháp y khi nó lật mâu thuẫn trong lời khai; cho phép đúc kết ngắn về tâm lý hành vi). Không rõ ai sửa, sửa lúc 2026-09-15 17:44, hai bản `.claude` và `.agents` vẫn trùng nhau. Giữ nguyên các sửa đổi đó và viết phương án B chồng lên, có ghi trong bản đề xuất để Tú xác nhận.

Các đề xuất còn lại của lượt rà chưa được chốt, không nằm trong claim này. Hướng nới lỏng rộng hơn mà Tú nêu ngày 2026-09-16 — cho phép chi tiết không có trong hồ sơ nếu không gây hậu quả nghiêm trọng — cũng tách riêng, chưa chốt và chưa làm.

## Hoàn tất 2026-09-16

Gói đã vào `main` qua `4a48b3d` (skill và luật nghiệp vụ) và `5b549ea` (bản đề xuất, luồng review, bàn giao). Luồng `sys-skill-han-viet-suy-ngam` chốt sau vòng 1: Codex nêu bốn điểm, Gemini đồng tình cả bốn và không thêm điểm mới, tác giả nhận cả bốn. Tú quyết định không chạy vòng 2, nên bốn bản sửa chưa có reviewer đọc lại — ghi trong luồng và trong bàn giao. Hai bản skill trùng từng byte, 66 link cục bộ hợp lệ, ba lệnh kiểm repo đều qua. Không chạy kiểm thử hành vi; không đụng `registry.json`.

Ngoài phạm vi claim này, trong lúc làm đã sửa một lỗi của `scripts/orchestrate.py` (`0ee7b95`, claim `sys-agent-coordination`): prompt nhiều dòng truyền qua dòng lệnh bị `cmd.exe` cắt tại dòng đầu, nên mọi lượt tự động trước đây chỉ nhận được một dòng. `claude` và `agy` vẫn còn lỗi này.
