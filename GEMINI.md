# GEMINI.md

Đọc [`AGENTS.md`](AGENTS.md) ở thư mục gốc trước. Đó là luật phối hợp chung cho Codex, Claude Code và Antigravity — không có luật riêng cho Gemini ở file này.

Nhắc lại ba điểm dễ bỏ sót:

- **Claim trước khi làm.** Xem `coordination/claims/`, chạy `python scripts/claims.py check`. Không đụng vào một mã `NET-xxxx` đang có claim `active` của agent khác.
- **Vai mặc định của Gemini:** kiểm chứng chéo nguồn, kế hoạch hình ảnh theo cảnh, đối chiếu bản tiếng Anh với bản tiếng Việt đã duyệt. Chưa sửa `registry.json` cho tới khi người dùng giao rõ.
- **Thư viện skill dùng chung** nằm ở `.claude/skills/*/SKILL.md`. Đó là tài liệu markdown cho mọi agent, không phải riêng Claude.

Việc của kênh: đọc tiếp `t-i/outputs/YouTube-Research-System/AGENTS.md`.
