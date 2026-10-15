# GEMINI.md

Đọc [`AGENTS.md`](AGENTS.md) ở thư mục gốc trước. Đó là luật phối hợp chung cho Claude Code và Antigravity — không có luật riêng cho Gemini ở file này.

Nhắc lại bốn điểm dễ bỏ sót:

- **Review theo từng bước, không đợi tới PR.** Mỗi sản phẩm trung gian — gợi ý vụ, khung sườn, bản tiếng Việt, bản thu âm — đi qua một luồng review nhiều vòng với agent còn lại (Claude viết thì Gemini review, và ngược lại). Codex đã ngừng dùng từ 2026-10-15. Bắt đầu bằng `python scripts/thread.py status`. Quy trình một lượt ở `.claude/skills/deliberation/SKILL.md`.
- **Được phản bác.** Yêu cầu sửa không phải mệnh lệnh — nhưng phản bác phải thuộc bốn loại lý do ở AGENTS.md mục 8, và phải trả lời đúng điểm được nêu. Không im lặng, không sửa lấy lệ.
- **Claim trước khi làm.** Xem `coordination/claims/`, chạy `python scripts/claims.py check`. Không đụng vào mã `NET-xxxx` đang có claim `active` của agent khác.
- **Vai mặc định của Gemini:** người review duy nhất ở mọi bước Claude viết — chống trùng, truy nguồn và kiểm chứng chéo, đối chiếu nguồn bản tiếng Việt, kế hoạch hình ảnh theo cảnh, đối chiếu bản thu âm. Chưa sửa `registry.json` cho tới khi Tú giao rõ.

Việc của kênh: đọc tiếp `t-i/outputs/YouTube-Research-System/AGENTS.md`. Đây là kênh kỳ án tiếng Việt cho khán giả Việt Nam; quy trình làm tập ở `.claude/skills/ky-an-viet/SKILL.md`.
