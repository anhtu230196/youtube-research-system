---
name: registry-safe-update
description: Quy trình sửa an toàn registry.json của YouTube Research System — cấp mã NET mới, đổi status, tạo thư mục tập, snapshot và kiểm tra. Dùng khi cần thêm case, chọn chuyện, chuyển trạng thái sang researching/awaiting_review/scripted/published, hoặc khi CI báo lệch giữa episodes/ và sổ. Registry edit, case ID allocation, status change.
---

# Sửa registry.json an toàn

`t-i/outputs/YouTube-Research-System/registry.json` là nguồn trạng thái duy nhất của kênh. Nhiều agent cùng sửa nó là nguyên nhân lệch dữ liệu số một trong repo này. Skill này là quy trình bắt buộc, dùng chung cho Codex, Claude và Gemini.

Luật nền: [`AGENTS.md`](../../../AGENTS.md) mục 5. Luật nghiệp vụ: `t-i/outputs/YouTube-Research-System/AGENTS.md`.

## Trước khi sửa

```bash
git fetch origin
git log origin/main --oneline -3
python scripts/claims.py check
python scripts/registry.py check
```

Dừng lại nếu:

- Một agent khác đang giữ claim `active` trên mã bạn định đụng tới.
- `registry.py check` đang báo lỗi có sẵn mà không phải lỗi bạn định sửa. Báo người dùng trước; đừng sửa chồng lên một sổ đang lệch.
- Nhánh của bạn chưa rebase lên `origin/main`. Sửa registry trên nền cũ gần như chắc chắn tạo xung đột.

## Quy trình sửa

1. **Snapshot trước.** `python scripts/registry.py snapshot` — ghi bản sao có dấu thời gian vào `history/`. CI bắt buộc mỗi PR đụng `registry.json` phải kèm một snapshot mới.
2. **Đọc bản mới nhất trên đĩa**, không dùng lại nội dung đã đọc từ đầu phiên. File có thể đã đổi.
3. **Sửa.** Ghi ra file tạm rồi thay thế, đừng ghi đè trực tiếp một file JSON đang mở.
4. **Kiểm tra.** `python scripts/registry.py check`
5. **Commit registry riêng một commit**, không trộn với nội dung kịch bản, để review và revert được độc lập.

## Cấp mã mới

Một case mới cần đủ:

```
id                 NET-xxxx lấy từ next_case_number, không tự chọn số
canonical_title    tên chuẩn, dùng để chống trùng
aliases            tên khác của cùng câu chuyện
entities           người và tổ chức chính
event_dates        các mốc năm
fingerprint        <nhan-vat>|<su-kien-goc>|<moc-quan-trong>
title_vi           tiêu đề làm việc tiếng Việt
scores             sáu điểm 1–5, theo thứ tự trong AGENTS.md nghiệp vụ
sources            link đã tự mở kiểm tra, không phải link nghe nói có
status             thường là proposed
first_proposed_on  YYYY-MM-DD
batch_id           đợt gợi ý
episode_path       null cho tới khi thật sự tạo thư mục
published_url      null
included_case_ids  [] trừ tập tổng hợp
history            ít nhất một mục có date + status + reason
```

**Bump `next_case_number` trong cùng commit.** Bỏ bước này là lỗi đã xảy ra thật với NET-0006: thư mục tập tồn tại, sổ không biết, và mã sẵn sàng bị cấp lại cho chuyện khác.

## Đổi trạng thái

Thêm một mục vào `history` **và** đổi `status` — hai chỗ, cùng lúc. `check` bắt trường hợp lệch nhau.

```json
{ "date": "2026-09-09", "status": "awaiting_review", "reason": "Ban tieng Viet day du da nop, cho Tu duyet noi dung." }
```

Ranh giới dễ sai:

- `scripted` chỉ khi bản cuối theo ngôn ngữ đã chọn đã bàn giao. Bản tiếng Việt đang chờ duyệt là `awaiting_review`.
- `published` chỉ khi người dùng xác nhận và có `published_url`. Không agent nào tự đăng.
- `selected` phải ghi trước khi bắt đầu nghiên cứu, không ghi sau.

## Tạo thư mục tập

Thư mục tập chỉ được tạo khi case đã có trong sổ, và `episode_path` phải trỏ đúng vào nó.

```bash
mkdir -p t-i/outputs/YouTube-Research-System/episodes/NET-xxxx-slug/{sources,assets,scripts}
```

Slug viết thường, nối bằng dấu gạch ngang, đủ nhận ra câu chuyện.

## Xung đột merge

Không tự chọn một bên. Lấy bản trên `main`, áp lại thay đổi của mình bằng tay, chạy `check`, rồi commit. Nếu không chắc thay đổi của agent kia là gì, đọc snapshot trong `history/` để so.

## Cái skill này không làm được

`check` chỉ bắt lệch máy móc — mã trùng, thư mục không có trong sổ, `next_case_number` sai, status lạ, thiếu snapshot. Nó không biết một case ghi sai sự thật, một `fingerprint` đặt cẩu thả khiến hai chuyện khác nhau trông như một, hay một `source` dẫn tới trang không nói điều bạn ghi. Phần đó vẫn phải người hoặc agent review đọc.
