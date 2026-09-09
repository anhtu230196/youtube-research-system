# YouTube Research System

Hệ thống sản xuất nội dung cho kênh YouTube về bí ẩn internet, lừa đảo và điều tra số.

Nội dung chính nằm trong [`t-i/outputs/YouTube-Research-System/`](t-i/outputs/YouTube-Research-System/):

| Thành phần | Vai trò |
| --- | --- |
| `AGENTS.md` | Quy tắc cho trợ lý tiếp tục công việc |
| `README.md` | Hướng dẫn sử dụng và luồng làm việc |
| `registry.json` | Sổ câu chuyện và cấu hình — nguồn trạng thái chính thức |
| `STORYTELLING.md` | Tiêu chí mở đầu, dẫn dắt, đặt manh mối, kết thúc, CTA |
| `references/` | Bản tham khảo dùng để phân tích cách kể |
| `templates/episode.md` | Mẫu hồ sơ và bàn giao mỗi tập |
| `batches/` | Các đợt gợi ý theo ngày |
| `history/` | Ảnh chụp registry qua từng lần thay đổi |

## Nhiều agent cùng làm

Repo này được Codex (ChatGPT), Claude Code và sau này Antigravity (Gemini) cùng chỉnh sửa. Luật phối hợp — phân vai, claim chống làm trùng, nhánh và PR, review chéo — nằm ở [`AGENTS.md`](AGENTS.md). Mọi agent đọc file đó trước.

```bash
python scripts/claims.py check     # ai dang giu viec gi
python scripts/registry.py check   # so trang thai co lech khong
```

## Bắt đầu

Mở cuộc trò chuyện mới, gửi đường dẫn thư mục và nhắn: **Đọc AGENTS.md và tiếp tục hệ thống kênh của tôi**.
