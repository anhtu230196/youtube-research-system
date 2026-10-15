---
id: sys-remove-codex
agent: claude
branch: main
status: done
opened: 2026-10-15
updated: 2026-10-15
scope:
  - AGENTS.md
  - CLAUDE.md
  - GEMINI.md
  - README.md
  - coordination/README.md
  - coordination/agents.json
  - coordination/claims/_TEMPLATE.md
  - coordination/threads/net-0006-ban-tieng-viet/THREAD.md
  - coordination/threads/net-0006-khung-suon-moi/THREAD.md
  - coordination/threads/net-0006-khung-suon-v3/THREAD.md
  - coordination/threads/sys-skill-ky-an-viet-ref-elda/THREAD.md
  - scripts/
  - .github/workflows/agent-checks.yml
  - .claude/skills/
  - .agents/skills/
---

# sys-remove-codex — Bỏ Codex khỏi hệ thống nhiều agent

**Làm gì:** Tú quyết ngày 2026-10-15 ngừng dùng Codex vì không còn gói ChatGPT Plus. Bỏ Codex khỏi luật phối hợp, phân vai, bảng bước review, cấu hình orchestrator, mặc định của script và các skill dùng chung. Claude nhận các bước tác giả Codex từng cầm; Gemini là người review duy nhất. Các luồng đang mở có lượt Codex được bỏ Codex khỏi danh sách người review, hoặc ghi chú khi Codex là tác giả.

**Không đụng tới:** lịch sử — file vòng, handoff, claim đã đóng, `history/`, `registry.json`, bản tập và thử model đã làm bằng Codex. Script vẫn đọc được `codex` trong hồ sơ cũ để `check` không báo lỗi trên lịch sử.

**Ghi chú:** Tú yêu cầu commit và đẩy thẳng; không mở luồng review cho thay đổi này. Gemini đọc lại sau khi vào `main`.

## Hoàn tất 2026-10-15

Đã vào `main` cùng commit này và commit trước. Ba lệnh kiểm repo đều qua; `thread.py new`, `claims.py new` và `orchestrate.py start` từ chối `codex`. Không có lượt review: Tú yêu cầu commit và đẩy thẳng. Luồng `net-0006-ban-tieng-viet` có Codex là tác giả, chờ Tú giao lại.

Bổ sung cùng ngày: Tú đóng luồng `net-0006-ban-tieng-viet`. `thread.py` có thêm trạng thái `closed` (Tú dừng luồng mà không chốt, điểm mở giữ làm hồ sơ, `apply` từ chối file vòng mới); `AGENTS.md` mục 8 và skill `deliberation` ghi thêm trạng thái này. Làm tiếp bản tiếng Việt NET-0006 thì mở luồng mới.
