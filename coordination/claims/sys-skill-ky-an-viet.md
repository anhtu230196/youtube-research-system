---
id: sys-skill-ky-an-viet
agent: codex
branch: codex/ky-an-viet-voice
status: active
opened: 2026-09-14
updated: 2026-09-15
scope:
  - .claude/skills/ky-an-viet/
  - .claude/skills/README.md
  - .agents/skills/ky-an-viet/
  - t-i/outputs/YouTube-Research-System/STORYTELLING.md
  - coordination/threads/sys-skill-ky-an-viet-voice/
  - coordination/drafts/sys-skill-ky-an-viet-voice.md
  - coordination/handoffs/2026-09-15-codex-ky-an-viet-voice.md
---

# sys-skill-ky-an-viet — Skill ky-an-viet: quy trinh kich ban ky an tieng Viet cho khan gia Viet Nam

**Làm gì:** Skill ky-an-viet: quy trinh kich ban ky an tieng Viet cho khan gia Viet Nam

**Không đụng tới:** `~/.codex/skills/mystery-case-script` (skill toàn cục của máy, dùng chung dự án khác); plugin `mystery-case-script` của Claude. Bản `.agents/skills/ky-an-viet/` nằm trong phạm vi cập nhật từ lượt tiếp quản ngày 2026-09-15.

**Ghi chú:** Kế thừa `mystery-case-script` bản 2026-09-08. Phần mới (bản địa hoá, vụ án Việt Nam, cạnh tranh tiếng Việt, TTS tiếng Việt) chưa chạy trên tập thật và chưa qua luồng review bước 7 — ghi rõ trong chính skill. 

**Lịch sử lượt tạo 2026-09-14 (đã đóng):** skill đã vào `main`. Khi đóng lượt đó, phần mới chưa chạy trên tập thật và chưa qua luồng review bước 7. Trạng thái hiện tại theo frontmatter và lượt tiếp quản bên dưới.

## Tiếp quản 2026-09-15 — Codex

Tú yêu cầu cập nhật skill theo mẫu Cẩm Tân Đại Lâu / mất tích đêm Trung thu để lời kể tiếng Việt tự nhiên hơn. Lượt tạo của Claude ở trên đã hoàn tất; không có claim active khác cho skill này. Codex cập nhật hướng dẫn giọng kể, ví dụ thực hành, cách nạp hướng dẫn và bản sao `.agents/skills/ky-an-viet/`, kiểm thử trên dữ kiện đóng, tổ chức review trước khi đưa thay đổi nội dung vào main.

Phạm vi không sửa: `registry.json`, trạng thái và lịch sử các case, chức năng gợi ý/chống trùng/nghiên cứu, kịch bản NET-0006 đang trong vòng review, cấu hình model và các skill toàn cục. Mẫu được dùng để học kỹ thuật kể, không được nhập như một case mới hay coi là nguồn xác minh vụ án.
