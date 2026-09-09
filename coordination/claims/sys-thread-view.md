---
id: sys-thread-view
agent: claude
branch: claude/thread-view
status: active
opened: 2026-09-09
updated: 2026-09-09
scope:
  - scripts/thread_view.py
  - scripts/orchestrate.py
  - .gitignore
  - coordination/README.md (muc dong bo hai repo)
---

# sys-thread-view — Trang doc luong review dang nhom chat, sinh lai moi luot

**Làm gì:** Trang doc luong review dang nhom chat, sinh lai moi luot

**Không đụng tới:** `thread.py`, `claims.py`, `registry.py`, `AGENTS.md`, và mọi file trong `coordination/threads/`. Trong `orchestrate.py` chỉ thêm móc sinh trang, không đổi luật chuyển lượt.

**Ghi chú:** Trang sinh ra ở `coordination/threads/<slug>/view.html`, đã cho vào `.gitignore` — nó là sản phẩm dẫn xuất, đọc lại được từ các file vòng bất cứ lúc nào. Lỗi khi sinh trang bị nuốt và chỉ in một dòng: luồng review không được hỏng vì một tiện nghi hiển thị. 
