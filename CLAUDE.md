# CLAUDE.md

Đọc [`AGENTS.md`](AGENTS.md) ở thư mục gốc trước. Đó là luật phối hợp chung cho Codex, Claude Code và Antigravity — không có luật riêng cho Claude ở file này.

Nhắc lại bốn điểm dễ bỏ sót:

- **Review theo từng bước, không đợi tới PR.** Mỗi sản phẩm trung gian — gợi ý vụ, khung sườn, bản tiếng Việt, bản thu âm — đi qua một luồng review nhiều vòng với hai agent còn lại. Bắt đầu bằng `python scripts/thread.py status`. Quy trình một lượt ở `.claude/skills/deliberation/SKILL.md`.
- **Được phản bác.** Yêu cầu sửa không phải mệnh lệnh — nhưng phản bác phải thuộc bốn loại lý do ở AGENTS.md mục 8, và phải trả lời đúng điểm được nêu. Không im lặng, không sửa lấy lệ.
- **Claim trước khi làm.** Xem `coordination/claims/`, chạy `python scripts/claims.py check`. Không đụng vào mã `NET-xxxx` đang có claim `active` của agent khác.
- **Vai mặc định của Claude:** khung sườn / beat sheet, skill và script, review đối chiếu nguồn, và bản thu âm tiếng Việt + đóng gói **sau khi Tú đã duyệt bản tiếng Việt**.

Việc của kênh: đọc tiếp `t-i/outputs/YouTube-Research-System/AGENTS.md`. Đây là kênh kỳ án tiếng Việt cho khán giả Việt Nam; quy trình làm tập ở `.claude/skills/ky-an-viet/SKILL.md`. **Không dùng skill `mystery-case-script`** — nó viết lời kể tiếng Anh cho khán giả Mỹ, hướng kênh đã bỏ từ 2026-09-14.
