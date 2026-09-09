# Thư viện skill dùng chung

Các file `SKILL.md` trong thư mục này là **quy trình dùng chung cho cả ba agent** — Codex, Claude Code và Antigravity — chứ không phải riêng Claude.

Đặt ở `.claude/skills/` vì Claude Code tự nạp được thư mục này. Codex và Gemini đọc như tài liệu markdown bình thường, khi `AGENTS.md` hoặc người dùng chỉ tới.

| Skill | Dùng khi |
| --- | --- |
| `registry-safe-update/` | Sửa `registry.json`: cấp mã mới, đổi trạng thái, tạo thư mục tập |
| `deliberation/` | Nhận một lượt trong luồng review nhiều vòng: viết đề xuất, review, phản bác, đóng luồng. Kèm hợp đồng khối `points` và luật khi chạy dưới orchestrator |
| `cross-review/` | Review chéo một PR của agent khác, hoặc trả lời review về bài mình |

## Viết skill mới

- Frontmatter có `name` và `description`. `description` quyết định skill có được gọi đúng lúc hay không: viết rõ **làm gì** và **dùng khi nào**, kèm vài từ khóa người dùng hay gõ.
- Phần thân là quy trình cho một agent bất kỳ. Không dùng cú pháp riêng của một nhà cung cấp.
- Mô tả quy trình đã chạy được thật, không phải ý định. Phần chưa kiểm chứng thì ghi rõ là chưa.
- Có mục nói skill **không** làm được gì. Đây là phần hay bị bỏ và là phần cứu agent sau khỏi tin nhầm.
- File phụ đặt cạnh `SKILL.md` trong cùng thư mục.

Thêm hoặc sửa skill = một PR riêng, có claim `sys-skill-<ten>` (xem [`../../AGENTS.md`](../../AGENTS.md) mục 4 và 7).
