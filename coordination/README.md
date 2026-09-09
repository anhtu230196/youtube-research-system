# coordination/

Nơi các agent nói cho nhau biết ai đang làm gì. Luật đầy đủ ở [`../AGENTS.md`](../AGENTS.md).

**Lớp này chạy ở hai repo.** `veo3-auto-generation` dùng bản chép y hệt: `scripts/thread.py`, `scripts/orchestrate.py`, `scripts/claims.py`, `scripts/thread_view.py` và `coordination/agents.json` giữ nguyên từng byte. Chỉ `coordination/RULES.md` bên đó khác (bảng bước của repo đó, và chốt cuối ở nhánh chứ chưa ở PR).

Đường dẫn repo kia khác nhau theo máy — máy `tu.vu` là `Desktop/veo3-auto-generation`, máy `AnhTu` là `Desktop/claude` — nên đặt biến rồi chép:

```bash
VEO3=/c/Users/AnhTu/Desktop/claude
cp scripts/thread.py scripts/orchestrate.py scripts/claims.py scripts/thread_view.py "$VEO3/scripts/"
cp coordination/agents.json "$VEO3/coordination/agents.json"
```

Chép xong thì chạy `python scripts/orchestrate.py doctor` bên đó để chắc lớp mới nhận đúng CLI.

Sửa luật review ở `AGENTS.md` mục 8 thì phải áp lại tay vào `coordination/RULES.md` bên kia — hai file đó cố ý khác nhau.

| Thư mục | Dùng để |
| --- | --- |
| `claims/` | Một file cho một việc đang giữ. Chống hai agent làm trùng. |
| `threads/` | Luồng review nhiều vòng trên một sản phẩm trung gian. Nơi ba agent thật sự tranh luận. |
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

## threads/

Mỗi bước sản phẩm — gợi ý chuyện, khung sườn, bản tiếng Việt, bản tiếng Anh — đi qua một luồng review nhiều vòng trước khi bước sau bắt đầu. Một agent là tác giả, hai agent còn lại review, tác giả được phản bác.

```bash
python scripts/thread.py status                 # luong nao dang mo, toi luot ai
python scripts/thread.py next <slug>            # in cau can dan cho agent ke tiep
python scripts/thread.py new <slug> --artifact <path>     --author claude --reviewers gemini,codex --question "..."
```

`THREAD.md` trong mỗi luồng là thứ duy nhất cần đọc để biết làm gì tiếp: đang vòng mấy, tới lượt ai, điểm `D**` nào còn mở.

Chạy tự động bằng CLI của từng agent (subscription, không phải API):

```bash
python scripts/orchestrate.py doctor --probe
python scripts/orchestrate.py run <slug>
```

Cấu hình lệnh CLI ở `agents.json`. Lượt review chạy chế độ chỉ đọc; chỉ lượt tác giả mới được sửa artifact.

Trần hội tụ: tối đa 3 vòng một luồng, một điểm tối đa 2 lần phản bác qua lại. Quá thì đẩy lên Tú. Luật đầy đủ ở [`../AGENTS.md`](../AGENTS.md) mục 8, quy trình một lượt ở [`../.claude/skills/deliberation/SKILL.md`](../.claude/skills/deliberation/SKILL.md).
