---
id: sys-gemini-agy
agent: claude
branch: claude/gemini-agy
status: done
opened: 2026-09-09
updated: 2026-09-09
scope:
  - coordination/agents.json
  - AGENTS.md (muc 8, hai dong noi ten lenh CLI)
---

# sys-gemini-agy — Chuyen ghe Gemini tu gemini CLI sang Antigravity CLI (agy)

**Làm gì:** Google đã ngắt đăng nhập OAuth của `gemini` CLI cho tài khoản cá nhân từ 18/06/2026 (Gemini Code Assist for individuals / AI Pro / Ultra). Đổi mục `gemini` trong `coordination/agents.json` sang Antigravity CLI (`agy -p`), và đặt luật chỉ-đọc cho lượt review bằng `permissions.deny` trong `~/.gemini/antigravity-cli/settings.json`.

**Không đụng tới:** `scripts/`, `coordination/threads/`, `registry.json`. Trong `AGENTS.md` chỉ sửa hai dòng ở mục 8 gọi tên lệnh CLI — không đổi luật nào.

**Ghi chú:** Luật chỉ-đọc của `agy` đặt ở file settings toàn cục chứ không phải cờ theo lần gọi, nên `write_cmd` của gemini không dùng được nữa. Chấp nhận được vì `AGENTS.md` mục 2 và mục 8 không giao cho Gemini vai tác giả ở bước nào — Gemini chỉ kiểm chứng chéo, dựng kế hoạch hình ảnh và đối chiếu bản Anh với bản Việt.

**Đóng:** Xong 2026-09-09: agy -p thay gemini CLI, model chot cho ca ba ghe, doctor --probe xanh. Da vao main.
