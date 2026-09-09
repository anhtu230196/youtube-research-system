# CLAUDE.md

Đọc [`AGENTS.md`](AGENTS.md) ở thư mục gốc trước. Đó là luật phối hợp chung cho Codex, Claude Code và Antigravity — không có luật riêng cho Claude ở file này.

Nhắc lại ba điểm dễ bỏ sót:

- **Claim trước khi làm.** Xem `coordination/claims/`, chạy `python scripts/claims.py check`. Không đụng vào một mã `NET-xxxx` đang có claim `active` của agent khác.
- **Vai mặc định của Claude:** skill / script / cấu trúc repo, review đối chiếu nguồn bản tiếng Việt do Codex viết, và viết bản tiếng Anh thu âm **sau khi người dùng đã duyệt bản tiếng Việt**. Không tự viết bản tiếng Việt gốc của tập Codex đang giữ.
- **Sửa `registry.json`** thì theo `.claude/skills/registry-safe-update/SKILL.md`, không sửa tay tự do.

Việc của kênh: đọc tiếp `t-i/outputs/YouTube-Research-System/AGENTS.md`.
