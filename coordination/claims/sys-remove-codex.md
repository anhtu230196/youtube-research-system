---
id: sys-remove-codex
agent: claude
branch: main
status: active
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
