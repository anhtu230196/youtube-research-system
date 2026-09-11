---
id: sys-model-trial-claude-net0006
agent: claude
branch: claude/model-trial-claude-net0006
status: active
opened: 2026-09-11
updated: 2026-09-11
scope:
  - coordination/drafts/model-trials/NET-0006/opus/
  - coordination/drafts/model-trials/NET-0006/sonnet/
  - coordination/drafts/model-trials/NET-0006/haiku/
  - coordination/drafts/model-trials/NET-0006/_claude-trial/
---

# Thử viết kịch bản bằng ba model Claude từ beat sheet NET-0006

Tú yêu cầu ngày 2026-09-11: so sánh khả năng viết kịch bản giữa các model Claude — Opus 5, Sonnet 5, Haiku 4.5 — xem bản nào hay nhất. Nối tiếp hai bản thử đã có ở cùng thư mục (`astra/` = GPT-6 Astra, `sol/` = GPT-5.6 Sol) và dùng **đúng cùng một đầu vào** để so được.

Thiết kế phép thử:

- Cùng beat sheet v2 (`episodes/NET-0006-sherri-rasmussen/scripts/01-beat-sheet.md`), cùng hồ sơ nghiên cứu, cùng quy tắc kênh. Cùng một prompt nguyên văn cho cả ba, lưu tại `_claude-trial/PROMPT.md`.
- Ba ghế viết là ba subagent, mỗi ghế một model, chạy song song, **không đọc bản của nhau** và không đọc prose cũ (Codex, Gemini, Astra, Sol) làm mẫu.
- Một lượt viết, **không** có subagent kiểm nguồn riêng — khác với bản thử Astra ở điểm này. Chỗ lệch đó được ghi trong bản so sánh; nó làm bản Claude không so trực tiếp 1-1 với Astra về mức kiểm chứng, nhưng ba bản Claude so với nhau thì vẫn cùng điều kiện.
- Chấm điểm: phần đếm được (đủ 14 nhịp, thứ tự, ranh giới thang tiết lộ §3, CTA một câu, ngày điều trần viết bằng chữ) chạy bằng script. Phần văn chương do Tú đọc, có bản ẩn nhãn A/B/C ở `_claude-trial/blind/`.

**Không đụng tới:** `registry.json`, thư mục `episodes/`, claim `NET-0006`, claim `sys-model-trial-sol-net0006` của Codex (thư mục `sol/` đang có bản thử chưa commit), hai luồng review đang mở.

**Ghi chú:** Người viết bản Opus và người viết bản so sánh là cùng một model. Xung đột đó được nêu rõ trong bản so sánh: kết luận "hay nhất" thuộc Tú, không thuộc agent chấm.
