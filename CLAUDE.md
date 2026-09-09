# CLAUDE.md

Đọc [`AGENTS.md`](AGENTS.md) ở thư mục gốc trước. Đó là luật phối hợp chung cho Codex, Claude Code và Antigravity — không có luật riêng cho Claude ở file này.

Nhắc lại bốn điểm dễ bỏ sót:

- **Review theo từng bước, không đợi tới PR.** Mỗi sản phẩm trung gian — gợi ý chuyện, khung sườn, bản tiếng Việt, bản tiếng Anh — đi qua một luồng review nhiều vòng với hai agent còn lại. Bắt đầu bằng `python scripts/thread.py status`. Quy trình một lượt ở `.claude/skills/deliberation/SKILL.md`.
- **Được phản bác.** Yêu cầu sửa không phải mệnh lệnh — nhưng phản bác phải thuộc bốn loại lý do ở AGENTS.md mục 8, và phải trả lời đúng điểm được nêu. Không im lặng, không sửa lấy lệ.
- **Claim trước khi làm.** Xem `coordination/claims/`, chạy `python scripts/claims.py check`. Không đụng vào mã `NET-xxxx` đang có claim `active` của agent khác.
- **Vai mặc định của Claude:** khung sườn / beat sheet, skill và script, review đối chiếu nguồn, và bản tiếng Anh thu âm **sau khi Tú đã duyệt bản tiếng Việt**.

Việc của kênh: đọc tiếp `t-i/outputs/YouTube-Research-System/AGENTS.md`.
