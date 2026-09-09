# coordination/

Nơi các agent nói cho nhau biết ai đang làm gì. Luật đầy đủ ở [`../AGENTS.md`](../AGENTS.md).

| Thư mục | Dùng để |
| --- | --- |
| `claims/` | Một file cho một việc đang giữ. Chống hai agent làm trùng. |
| `reviews/` | Báo cáo review chéo dài cho một PR, khi comment không đủ chỗ. |
| `handoffs/` | Ghi chú bàn giao khi việc chuyển từ agent này sang agent khác. |

## claims/

Một file một claim, tên theo mã việc: `NET-0006.md`, `sys-skill-library.md`. Một file riêng cho mỗi claim là cố ý — hai agent claim cùng lúc sẽ không xung đột merge.

Tạo nhanh:

```bash
python scripts/claims.py new NET-0007 --agent codex --branch codex/net-0007-research --task "Nghien cuu va tai nguon"
```

Kiểm tra trước khi bắt đầu bất cứ việc gì:

```bash
git fetch origin
python scripts/claims.py check
```

Vòng đời: `active` → `done` (xong việc) hoặc `released` (bỏ giữa chừng, ghi rõ còn dở gì). Claim `active` quá 7 ngày không cập nhật coi như nguội.

Claim phải có mặt trên `main` trước khi làm việc nặng, nếu không nó không khóa được gì.

## handoffs/

Đặt tên `YYYY-MM-DD-<agent>-<slug>.md`, theo `handoffs/_TEMPLATE.md`. Agent nhận việc đọc handoff trước khi đọc diff.

## reviews/

Đặt tên `<so-PR>-<agent-review>.md`, theo `reviews/_TEMPLATE.md`. Commit lên chính nhánh của PR đang review, rồi để một comment ngắn trên PR trỏ tới file.

Dùng khi review dài — đối chiếu nguồn từng claim, kiểm tra danh mục tải. Nhận xét ngắn thì viết thẳng comment trên PR, đừng tạo file.

Nhãn dùng trong cả comment lẫn file: `CHAN:` (chặn merge), `SUA:`, `HOI:`, `OK:`. Luật đầy đủ ở [`../AGENTS.md`](../AGENTS.md) mục 8.
