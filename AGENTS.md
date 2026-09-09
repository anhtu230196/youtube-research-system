# Quy tắc phối hợp nhiều agent

Repo này được nhiều agent cùng chỉnh sửa:

- **Codex (ChatGPT)** — chạy cloud qua pull request, và có thể chạy CLI ngay trên thư mục local này.
- **Claude Code** — chạy local, push nhánh và mở PR.
- **Antigravity (Gemini)** — dự kiến bổ sung sau, dùng chung luật này.

Mọi agent đọc file này trước khi làm bất cứ việc gì. `CLAUDE.md` và `GEMINI.md` ở thư mục gốc chỉ là con trỏ về đây — không viết luật riêng trong hai file đó.

## 1. Thứ tự đọc

| Việc | Đọc thêm |
| --- | --- |
| Bất kỳ việc gì trong repo | `AGENTS.md` (file này) |
| Việc của kênh YouTube | `t-i/outputs/YouTube-Research-System/AGENTS.md`, `README.md`, `registry.json` |
| Gợi ý góc kể, hook, dàn ý, kịch bản | thêm `t-i/outputs/YouTube-Research-System/STORYTELLING.md` |
| Sửa `registry.json` | thêm `.claude/skills/registry-safe-update/SKILL.md` |

Luật nghiệp vụ của kênh nằm trong `t-i/outputs/YouTube-Research-System/AGENTS.md`. File này chỉ nói **nhiều agent chia việc và tránh giẫm chân nhau thế nào**. Mâu thuẫn thì: luật nghiệp vụ quyết định nội dung, file này quyết định quy trình. Chỉ dẫn mới nhất của người dùng ưu tiên hơn cả hai.

## 2. Phân vai mặc định

| Agent | Việc chính | Không nhận mặc định |
| --- | --- | --- |
| **Codex** | Nghiên cứu, tải nguồn, dựng timeline và claim ledger, viết bản tiếng Việt đầy đủ để duyệt | Tự review chính bản mình vừa viết |
| **Claude Code** | Xây skill, script, CI, cấu trúc repo; review đối chiếu nguồn bản tiếng Việt; viết bản tiếng Anh thu âm sau khi người dùng đã duyệt | Viết bản tiếng Việt gốc của tập Codex đang giữ |
| **Gemini / Antigravity** | Kiểm chứng chéo nguồn, kế hoạch hình ảnh theo cảnh, đối chiếu bản Anh với bản Việt đã duyệt | Sửa `registry.json` cho tới khi được giao rõ |

Nguyên tắc đứng sau bảng này: **người viết không phải là người review.** Một tập đi qua ít nhất hai agent trước khi bàn giao.

Vai là mặc định, không phải hàng rào. Người dùng giao khác thì làm theo người dùng — nhưng vẫn phải claim theo mục 4.

## 3. Nhánh, commit, pull request

- Nhánh đặt tên `codex/<slug>`, `claude/<slug>`, `gemini/<slug>`. Một nhánh một việc.
- Không commit thẳng lên `main`, trừ file claim (mục 4).
- Rebase lên `origin/main` trước khi mở PR. Không rebase, không force-push, không sửa nhánh của agent khác.
- Commit message thêm trailer `Agent: codex` / `Agent: claude` / `Agent: gemini` để tra lại được ai làm gì.
- Thân PR nêu rõ: mã `NET-xxxx` đụng tới, có sửa `registry.json` hay không, đang giữ claim nào.
- PR phải xanh CI `agent-checks` trước khi merge.
- PR nhỏ và merge sớm. Nhánh sống lâu là nguyên nhân chính gây lệch trạng thái ở repo nhiều agent.

## 4. Claim — chống hai agent làm trùng

Trước khi bắt tay vào một việc, tạo một file claim: `coordination/claims/<ID>.md`.

`<ID>` là mã tập (`NET-0006`) hoặc slug việc hệ thống (`sys-skill-library`). Mỗi claim một file riêng — không dùng bảng chung — để hai agent claim cùng lúc không xung đột merge.

**Claim phải nhìn thấy được trên `main` trước khi làm việc nặng:**

- Agent push được lên `main`: commit riêng chỉ chứa file claim, đẩy ngay.
- Agent chỉ mở được PR (Codex cloud): claim là commit **đầu tiên** của nhánh, hoặc mở một PR nhỏ tên `claim: <ID>` để người dùng merge sớm.

Trước khi làm:

```bash
git fetch origin && git log origin/main --oneline -1
python scripts/claims.py check
```

Nếu `<ID>` đã có claim `active` của agent khác: **không làm**, báo người dùng và đề xuất việc khác.

Xong việc: đổi `status: done` trong chính PR kết thúc việc. Bỏ giữa chừng: `status: released` kèm lý do và tình trạng còn dở. Claim `active` quá 7 ngày không cập nhật coi như nguội — agent khác được tiếp quản sau khi hỏi người dùng.

## 5. `registry.json` — sổ trạng thái

`t-i/outputs/YouTube-Research-System/registry.json` là nguồn trạng thái duy nhất. Thư mục `episodes/` không phải nguồn trạng thái.

- **Một PR chỉ có một agent sửa `registry.json`.**
- Quy trình sửa: đọc bản mới nhất trên `origin/main` → `python scripts/registry.py snapshot` → sửa → `python scripts/registry.py check`.
- Cấp mã mới: lấy `next_case_number`, tạo case, **bump `next_case_number` trong cùng commit**.
- Không tạo `episodes/<ID>-slug/` khi chưa có case `<ID>` trong sổ. Lỗi này đã xảy ra thật với NET-0006: thư mục tập và kịch bản tồn tại nhưng sổ không biết, và `next_case_number` vẫn định cấp lại mã đó cho chuyện khác.
- Mỗi lần đổi status thêm một mục `history` có `date`, `status`, `reason`.
- Xung đột merge ở `registry.json`: không tự chọn bên nào. Lấy bản trên `main`, áp lại thay đổi của mình bằng tay, chạy `check`.

## 6. Hai agent cùng chạy local

Codex CLI và Claude Code có thể cùng trỏ vào `C:\Users\tu.vu\Documents\Codex\2026-09-08`. Hai tiến trình sửa chung một working copy là cách hỏng việc nhanh nhất.

- Ưu tiên: agent thứ hai làm trong worktree riêng.

  ```bash
  git worktree add ../wt-claude-<slug> -b claude/<slug>
  ```

- Buộc phải dùng thư mục chính: tạo `.agent-lock` ở gốc (đã gitignore) ghi tên agent và giờ bắt đầu, xóa khi xong. Thấy `.agent-lock` của agent khác còn mới thì không sửa file — chuyển sang worktree.
- Khi có lock của agent khác: không chạy `git checkout`, `git switch`, `git stash`, `git reset --hard` trên thư mục chính.

## 7. Thư viện skill dùng chung

`.claude/skills/<ten-skill>/SKILL.md` là **thư viện skill chung cho cả ba agent**, không phải riêng Claude. Đặt ở đó vì Claude Code tự nạp được thư mục này; Codex và Gemini đọc như tài liệu markdown bình thường khi AGENTS.md hoặc người dùng chỉ tới.

- Frontmatter có `name` và `description`. Phần thân là quy trình viết cho một agent bất kỳ.
- Không dùng cú pháp riêng của một nhà cung cấp trong phần thân. File phụ đặt cạnh `SKILL.md`.
- Thêm hoặc sửa skill = một PR riêng, có claim `sys-skill-<ten>`.
- Skill mô tả quy trình đã chạy được thật, không phải ý định. Chưa chạy thử thì ghi rõ phần nào chưa kiểm chứng.

## 8. Nói chuyện và review chéo

Ba agent **không có kênh nói chuyện trực tiếp**. Không agent nào gọi được agent khác, không agent nào chờ được agent khác trả lời trong cùng một phiên. Mọi trao đổi đi qua repo và GitHub, và người điều phối là Tú. Đừng thiết kế hay hứa hẹn như thể có kênh thời gian thực.

Ba mặt phẳng trao đổi, theo thứ tự ưu tiên:

**a) Pull request — kênh chính.** PR là nơi hai agent thật sự tranh luận, vì comment gắn thẳng vào từng dòng diff và lưu lại vĩnh viễn.

```bash
gh pr view <n> --json title,body,files
gh pr diff <n>
gh pr review <n> --comment --body-file coordination/reviews/<n>-<agent>.md
gh pr comment <n> --body "CHAN: ..."
```

Codex cloud đọc được PR khi Tú dán link. Claude Code và Antigravity dùng `gh`.

**b) `coordination/reviews/<PR>-<agent>.md` — báo cáo review dài.** Đối chiếu nguồn từng claim không nhét vừa một comment. Viết thành file theo `coordination/reviews/_TEMPLATE.md`, commit lên chính nhánh của PR, rồi để một comment ngắn trỏ tới file. Agent nào cũng đọc được file trong repo, kể cả khi không lấy được comment qua API.

**c) `coordination/handoffs/` — chuyển việc qua tay** (mục 9).

### Ai review ai

| Sản phẩm | Người viết | Người review |
| --- | --- | --- |
| Danh sách gợi ý chuyện mới | Codex | Claude — chống trùng với `registry.json` |
| Hồ sơ nghiên cứu, claim ledger | Codex | Claude — truy nguồn ngược, bắt suy diễn |
| Bản tiếng Việt để duyệt | Codex | Claude đối chiếu nguồn → **Tú duyệt nội dung** |
| Bản tiếng Anh thu âm | Claude | Codex hoặc Gemini — đối chiếu với bản Việt đã duyệt |
| Skill, script, CI, cấu trúc repo | Claude | Codex |

Hai luật cứng:

- **Agent viết ra một thứ không phải là agent duyệt thứ đó.**
- **Không agent nào tự merge PR của chính mình.** Cần ít nhất một review của agent khác, và Tú bấm merge.

Duyệt nội dung bản tiếng Việt vẫn là việc của Tú. Review chéo giữa agent chỉ kiểm nguồn, kiểm nhất quán, kiểm luật — không thay được bước duyệt đó.

### Cách viết comment review

Mỗi ý mở đầu bằng một nhãn để agent kia phân loại được mà không phải đoán:

- `CHAN:` — không merge được cho tới khi sửa. Sai sự thật, gán sai nguồn, suy diễn không có chứng cứ, lệch trạng thái registry, vi phạm luật trong AGENTS.md.
- `SUA:` — nên sửa, không chặn merge.
- `HOI:` — chưa rõ, cần người viết trả lời trước khi kết luận.
- `OK:` — xác nhận một phần đã kiểm tra và đạt. Ghi rõ đã kiểm cái gì, đừng chỉ nói "ổn".

Kèm `file:dòng`, và với việc kênh thì kèm `claim_id` hoặc `source_id` đang nói tới. Review không có dẫn chiếu cụ thể thì người viết không sửa được.

### Trả lời review

Agent nhận review phải trả lời **từng** mục `CHAN:` và `HOI:` — đã sửa ở commit nào, hoặc không sửa vì lý do gì. Không im lặng bỏ qua.

Hai agent bất đồng và không giải quyết được: dừng lại, nêu cả hai lập luận trong một comment, để Tú quyết. Không agent nào tự phá thế bế tắc bằng cách merge.

### Điều một agent review không được làm

Không sửa thẳng vào nhánh của agent khác để "sửa giúp" — viết comment. Nếu Tú yêu cầu sửa hộ thì mở nhánh mới dựa trên nhánh đó và nói rõ trong PR.

Không dùng review để viết lại theo giọng của mình. Nhận xét cái sai và cái thiếu chứng cứ, không nhận xét cái khác gu.

## 9. Bàn giao giữa hai agent

Chuyển việc qua tay: viết `coordination/handoffs/YYYY-MM-DD-<agent>-<slug>.md` theo `coordination/handoffs/_TEMPLATE.md`. Ghi rõ đã làm gì, file nào, còn thiếu gì, chi tiết nào **chưa** kiểm chứng, bước kế tiếp.

Agent nhận việc đọc handoff trước, không đoán từ diff. Diff cho biết cái gì đã đổi, không cho biết cái gì đã được kiểm tra.

## 10. Kiểm tra tự động

```bash
python scripts/registry.py check
python scripts/claims.py check
```

Hai lệnh này chạy trong CI (`.github/workflows/agent-checks.yml`) trên mọi PR và mọi push lên `main`. Chạy tại máy trước khi mở PR.

CI chỉ bắt lệch máy móc: mã trùng, thư mục tập không có trong sổ, `next_case_number` sai, status lạ, sửa sổ mà không lưu snapshot, claim chồng nhau. Nó không bắt được nguồn sai, kể sai hay suy diễn không có chứng cứ — phần đó vẫn cần agent review đọc thật.

## 11. Không agent nào tự làm

- Không đăng video, không gửi tin nhắn hay email cho nguồn, không thanh toán, không đưa nội dung ra ngoài repo khi người dùng chưa cho phép.
- Không ghi `published` khi chưa có xác nhận của người dùng.
- Không xóa lịch sử trong `registry.json` hay `history/` để dùng lại mã.
- Không force-push `main`.
- Không sửa file này để nới luật cho riêng mình. Đổi luật thì mở PR và nói rõ lý do.
