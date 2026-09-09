# Bàn giao: NET-0006 — Claude → Codex / Tú

**Ngày:** 2026-09-09 · **Nhánh:** `claude/agent-coordination`

## Đã làm

Dựng lớp phối hợp nhiều agent, và trong lúc đó phát hiện NET-0006 nằm ngoài sổ trạng thái. Đã đưa vào `registry.json`:

- Thêm case `NET-0006` với `status: awaiting_review`, `episode_path: episodes/NET-0006-sherri-rasmussen`.
- `next_case_number` 6 → 7. Trước khi sửa, mã NET-0006 sắp được cấp lại cho một chuyện khác.
- Hai mục `history` ghi ngày hôm nay, nêu rõ đây là ghi nhận hồi tố cho việc đã làm ở commit `d329477`.
- Snapshot trước khi sửa: `history/registry-20260909-101008-700.json`.

Không đụng vào nội dung kịch bản.

## File liên quan

| Đường dẫn | Trạng thái |
| --- | --- |
| `registry.json` | đã sửa, `python scripts/registry.py check` sạch |
| `episodes/NET-0006-sherri-rasmussen/scripts/02-script-vi.md` | bản nháp đầy đủ, chờ Tú duyệt — **chưa ai đối chiếu nguồn** |
| `episodes/NET-0006-sherri-rasmussen/scripts/02b-narration-vi-review.txt` | bản narration sạch |

## Chưa kiểm chứng

**Tôi chưa đối chiếu nguồn của kịch bản này.** Chưa mở lại một URL nào, chưa kiểm một claim nào. Việc tôi làm chỉ là ghi nhận trạng thái. Đừng đọc bước này như một lần review.

## Còn thiếu trong hồ sơ tập

So với `templates/episode.md`, thư mục tập mới chỉ có `scripts/`:

- Không có `sources/` và `assets/`.
- Không có hồ sơ tập theo template: `sources.csv`, `claims.csv`, timeline, báo cáo khoảng trống, `assets.csv`, bộ bàn giao.
- Kịch bản dẫn chiếu `C01`–`C26` và `S01`–`S05`, `S07`, nhưng **không có claim ledger hay danh mục nguồn nào trong repo** để tra các mã đó. Chúng đang trỏ vào hư không.
- `S06` không xuất hiện ở đâu trong kịch bản — nhiều khả năng danh mục nguồn gốc có 7 mục và chưa được commit.
- `scores` để rỗng: tập này không đi qua luồng gợi ý batch nên chưa được chấm sáu tiêu chí. Không tự bịa điểm.

## Bước kế tiếp

1. **Codex:** commit claim ledger và danh mục nguồn của NET-0006 để `C01`–`C26`, `S01`–`S07` tra được. Đây là điều kiện để bất kỳ ai review nguồn được.
2. **Claude:** sau khi có ledger, review đối chiếu nguồn theo `.claude/skills/cross-review/SKILL.md`, viết `coordination/reviews/<PR>-claude.md`.
3. **Tú:** duyệt nội dung bản tiếng Việt. Chỉ sau đó mới viết bản tiếng Anh.
4. Khi bản tiếng Anh bàn giao xong: đổi `NET-0006` sang `scripted`.

## Đang chờ Tú

- Duyệt nội dung bản tiếng Việt NET-0006.
- `NET-0001` (James Zhong) đang `selected` từ 2026-09-08, thư mục tập rỗng, chưa ai nhận. Có tiếp tục không, hay để `deferred`?
