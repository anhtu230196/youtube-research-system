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
| Nhận một lượt trong luồng review | thêm `.claude/skills/deliberation/SKILL.md` |
| Sửa `registry.json` | thêm `.claude/skills/registry-safe-update/SKILL.md` |

Luật nghiệp vụ của kênh nằm trong `t-i/outputs/YouTube-Research-System/AGENTS.md`. File này chỉ nói **nhiều agent chia việc và tránh giẫm chân nhau thế nào**. Mâu thuẫn thì: luật nghiệp vụ quyết định nội dung, file này quyết định quy trình. Chỉ dẫn mới nhất của người dùng ưu tiên hơn cả hai.

## 2. Phân vai mặc định

| Agent | Việc chính | Không nhận mặc định |
| --- | --- | --- |
| **Codex** | Nghiên cứu, tải nguồn, dựng timeline và claim ledger, viết bản tiếng Việt đầy đủ để duyệt | Tự review chính bản mình vừa viết |
| **Claude Code** | Khung sườn / beat sheet; skill, script, CI, cấu trúc repo; review đối chiếu nguồn bản tiếng Việt; viết bản tiếng Anh thu âm sau khi người dùng đã duyệt | Viết bản tiếng Việt gốc của tập Codex đang giữ |
| **Gemini / Antigravity** | Kiểm chứng chéo nguồn, kế hoạch hình ảnh theo cảnh, đối chiếu bản Anh với bản Việt đã duyệt | Sửa `registry.json` cho tới khi được giao rõ |

Nguyên tắc đứng sau bảng này: **người viết không phải là người review.** Một tập đi qua ít nhất hai agent trước khi bàn giao.

Bảng này nói ai **cầm** bước nào. Nó không cho ai quyền bỏ qua review: mỗi bước vẫn đi qua một luồng review nhiều vòng với hai agent còn lại (mục 8), và vai tác giả xoay theo bước chứ không cố định theo agent.

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

## 8. Review theo từng bước

Ba agent **không có kênh nói chuyện trực tiếp**. Không agent nào gọi được agent khác, không agent nào chờ được agent khác trả lời trong cùng một phiên. Cái chung duy nhất là repo, và người chuyển lượt là Tú. Đừng thiết kế hay hứa hẹn như thể có kênh thời gian thực.

Nhưng "không nói chuyện thời gian thực" không có nghĩa là chỉ review một lần ở cuối. Review ở mức pull request là quá muộn: một khung sườn sai từ đầu thì cả bản viết dựng trên nền đó cũng sai, và lúc phát hiện thì sửa đã đắt.

**Mỗi sản phẩm trung gian đi qua một luồng review nhiều vòng trước khi bước sau bắt đầu.**

### Nguyên tắc

Ba agent là một nhóm làm việc, không phải ba dây chuyền song song. Với mỗi bước:

- Một agent là **tác giả** — người viết ra sản phẩm bước đó.
- Hai agent còn lại là **người review** — đọc và nêu điểm chưa hợp lý, có dẫn chiếu cụ thể.
- Tác giả **được phản bác**. Yêu cầu sửa không phải mệnh lệnh. Nhưng phản bác phải thuộc loại lý do được chấp nhận ở dưới, không phải "tôi thích viết khác".
- Người review phải trả lời phản bác: chấp nhận, hoặc đưa chứng cứ mới, hoặc đẩy lên Tú. Không lặp lại nguyên văn ý cũ.

Vai tác giả xoay theo bước, không cố định theo agent. Mục 2 chỉ nói mặc định ai **cầm** bước nào; nó không cho ai quyền bỏ qua review.

### Các bước có luồng review

| # | Sản phẩm bước | Tác giả mặc định | Người review |
| --- | --- | --- | --- |
| 1 | Danh sách gợi ý chuyện mới | Codex | Claude (chống trùng `registry.json`), Gemini |
| 2 | Câu hỏi trung tâm và góc kể | Codex | Claude, Gemini |
| 3 | Timeline + claim ledger sau nghiên cứu | Codex | Claude (truy nguồn ngược), Gemini (kiểm chứng chéo) |
| 4 | **Khung sườn / beat sheet** | Claude | Codex, Gemini |
| 5 | Bản tiếng Việt đầy đủ | Codex | Claude (đối chiếu nguồn), Gemini — rồi **Tú duyệt nội dung** |
| 6 | Bản tiếng Anh thu âm | Claude | Codex, Gemini (đối chiếu bản Việt đã duyệt) |
| 7 | Skill, script, CI, cấu trúc repo | Claude | Codex |

Bước 5 có hai lớp: agent review nguồn và tính nhất quán, **Tú duyệt nội dung**. Agent không thay được lớp thứ hai.

### Cấu trúc một luồng

```
coordination/threads/<slug>/
  THREAD.md                    trạng thái: vòng mấy, tới lượt ai, điểm nào còn mở
  r1-00-proposal-claude.md     tác giả nộp bản v1
  r1-01-review-gemini.md
  r1-02-review-codex.md
  r2-00-response-claude.md     nhận điểm nào, phản bác điểm nào, ra v2
  r2-01-review-gemini.md
  ...
```

`THREAD.md` là thứ **duy nhất** cần đọc để biết phải làm gì tiếp. Sản phẩm thật (khung sườn, kịch bản) nằm ở đường dẫn `artifact:` trong `THREAD.md`, không nằm trong luồng.

```bash
python scripts/thread.py status          # tất cả luồng đang mở
python scripts/thread.py next <slug>     # in ra đúng câu cần dán cho agent tới lượt
python scripts/thread.py check           # CI dùng
```

### Luật lượt

Một lượt một agent. `THREAD.md` ghi `turn:`. **Không viết khi không tới lượt** — nếu thấy có vấn đề gấp thì ghi vào `THREAD.md` mục "ngoài lượt" một dòng, không viết file vòng.

Tác giả **không sửa artifact giữa một vòng review**. Bản đang review là bản đóng băng. Sửa chỉ diễn ra ở lượt response của tác giả, kèm bump `artifact_version`.

### Điểm tranh luận

Mỗi điểm có mã `D01`, `D02`… do người nêu đặt, và sống qua các vòng cho tới khi chốt. Bảng điểm nằm trong `THREAD.md`.

| Trạng thái | Nghĩa |
| --- | --- |
| `mở` | Vừa nêu, tác giả chưa trả lời |
| `đã sửa ở v<N>` | Tác giả chấp nhận và đã sửa |
| `tác giả phản bác — chờ <reviewer>` | Chờ người nêu trả lời phản bác |
| `chốt: đã sửa` / `chốt: giữ nguyên` | Hai bên đồng ý, đóng |
| `đẩy lên Tú` | Không hội tụ, chờ người quyết |

### Người review được nêu cái gì

Được:

- Nút thắt không có chứng cứ đỡ; suy diễn trình bày như sự thật; thoại hoặc cảnh không ai chứng kiến được dựng thành sự thật.
- Câu hỏi mở ra mà không bao giờ đóng lại; hoặc lời giải xuất hiện mà manh mối chưa được đặt trước.
- Trình tự tiết lộ hỏng: người nghe biết trước điều lẽ ra phải khám phá sau.
- Chi tiết không phục vụ câu chuyện, hoặc lặp chức năng với một chi tiết khác.
- Trùng chuyện đã có trong `registry.json`.
- Rủi ro quảng cáo, rủi ro pháp lý, vi phạm luật trong `AGENTS.md` hoặc AGENTS.md nghiệp vụ.

Không được:

- "Tôi sẽ viết khác." Khác gu không phải lỗi.
- Đòi viết lại toàn bộ khi chỉ một đoạn có vấn đề.
- Nêu lại một điểm đã chốt ở vòng trước mà không có chứng cứ mới.
- Góp ý về thứ thuộc bước sau — khung sườn không bị chê vì chưa có câu văn hay.

### Tác giả được phản bác bằng lý do gì

- **Nguồn nói khác điều người review tưởng** — dẫn ra nguồn và vị trí.
- **Ngoài phạm vi bước này** — để bước sau xử lý, nói rõ bước nào.
- **Đã có chỗ khác xử lý** — chỉ ra chỗ đó.
- **Đây là lựa chọn kể chuyện trong vùng cho phép**, không phải lỗi sự thật hay lỗi cấu trúc.

Phản bác phải trả lời đúng điểm được nêu. Không im lặng bỏ qua, và cũng không sửa lấy lệ cho điểm biến mất.

### Hội tụ

- **Tối đa 3 vòng một luồng.**
- **Một điểm tối đa 2 lần phản bác qua lại.** Lần thứ ba tự động chuyển `đẩy lên Tú`.
- Hết vòng mà còn điểm mở: `THREAD.md` chuyển `status: blocked`, liệt kê điểm mở, Tú quyết.
- Không mở luồng mới cho một điểm đã chốt.

Mục tiêu là **đủ tốt và có căn cứ**, không phải hoàn hảo. Ba agent để tự do sẽ sinh vòng review vô hạn vì vòng nào cũng tìm được thứ để nói. Trần này là cố ý, đừng nới nó vì thấy còn góp ý được.

### Khối `points` — hợp đồng giữa agent và sổ luồng

Mọi file vòng phải kết thúc bằng một khối máy đọc được. Không có khối này thì bảng điểm trong `THREAD.md` không cập nhật được, và `thread.py check` sẽ báo lỗi.

````
```points
D01 | mở | scripts/01-beat-sheet.md:44 | Gán trạng thái tâm lý không có nguồn
D02 | đã sửa ở v2 | scripts/01-beat-sheet.md:70 | Đã đổi thành mô tả hành động
```
````

Trạng thái phải chép đúng nguyên văn một trong: `mở` · `đã sửa ở v<N>` · `tác giả phản bác — chờ <agent>` · `chốt: đã sửa` · `chốt: giữ nguyên` · `đẩy lên Tú`.

Agent **không tự sửa `THREAD.md`**. Ghi file vòng xong thì chạy:

```bash
python scripts/thread.py apply <slug> <ten-file-vong>
```

Lệnh này cập nhật bảng điểm, đổi lượt, bump `artifact_version`, và tự chuyển luồng sang `settled` hoặc `blocked` theo trần hội tụ. Máy giữ trạng thái, agent chỉ viết nội dung — agent quên đổi lượt là lỗi hay gặp nhất khi để chúng tự quản.

### Ai chuyển lượt

Không agent nào tự đánh thức agent khác.

**Thủ công:** `python scripts/thread.py next <slug>` in ra đúng câu cần dán cho agent kế tiếp. Tú dán, agent làm, rồi `thread.py apply`.

**Tự động bằng CLI:** `scripts/orchestrate.py` gọi thẳng CLI của từng agent ở chế độ headless — `claude -p`, `gemini -p`, `codex exec` — nên chạy bằng subscription đã trả, không tính theo token như gọi API. Cấu hình lệnh ở `coordination/agents.json`.

```bash
python scripts/orchestrate.py doctor --probe   # CLI nao dung duoc, con dang nhap khong
python scripts/orchestrate.py turn <slug>      # chay dung mot luot roi dung
python scripts/orchestrate.py run <slug>       # chay den khi hoi tu hoac het tran
```

Luật an toàn của chế độ tự động:

- **Lượt review chạy chế độ chỉ đọc** (`--approval-mode plan`, `--permission-mode plan`, `--sandbox read-only`). Người review không cần quyền ghi, và không nên có.
- **Chỉ lượt tác giả được sửa artifact.** Không lượt nào được sửa `THREAD.md`; orchestrator lấy stdout làm file vòng rồi tự cập nhật sổ.
- Agent không xuất được khối `points` thì orchestrator **giữ lại file vòng và dừng**, không đoán thay. Sửa tay rồi `thread.py apply`.
- `run` dừng ngay khi luồng chuyển `settled` hoặc `blocked`, và có trần số lượt riêng.

Tự động không có nghĩa là tin. Đọc lại các file vòng trước khi dùng kết quả — nhất là mục "tôi đã không kiểm cái gì" của mỗi người review.

### Nhãn dùng trong file review

| Nhãn | Nghĩa |
| --- | --- |
| `CHAN:` | Không đi tiếp bước sau được cho tới khi xử lý |
| `SUA:` | Nên sửa, không chặn |
| `HOI:` | Chưa rõ, cần tác giả trả lời |
| `OK:` | Đã kiểm và đạt — ghi rõ kiểm bằng cách nào |

Mỗi ý kèm `file:dòng`, và kèm `claim_id` hoặc `source_id` khi nói về nội dung. Nhận xét không có dẫn chiếu cụ thể thì tác giả không sửa được.

### Chốt cuối vẫn ở pull request

Luồng review lo chất lượng từng bước. Pull request là cổng cuối trước khi vào `main`:

```bash
gh pr view <n> --json title,body,files
gh pr diff <n>
gh pr review <n> --comment --body-file coordination/reviews/<n>-<agent>.md
gh pr comment <n> --body "CHAN: ..."
```

- PR phải dẫn ra luồng review tương ứng, hoặc nói rõ vì sao bước này không cần luồng.
- Agent viết ra một thứ không duyệt thứ đó. **Không agent nào merge PR của chính mình.**
- Review dài — đối chiếu nguồn từng claim — viết `coordination/reviews/<PR>-<agent>.md`, commit lên nhánh của PR, rồi comment ngắn trỏ tới file.
- Không `--approve` hay `--request-changes` trừ khi Tú yêu cầu; `--comment` giữ quyền quyết định ở người.

### Điều một agent không được làm

Không sửa thẳng vào nhánh hay artifact của agent khác để "sửa giúp" — viết vào file review. Nếu Tú yêu cầu sửa hộ thì mở nhánh mới và nói rõ.

Không viết lại theo giọng của mình. Nhận xét cái sai và cái thiếu chứng cứ, không nhận xét cái khác gu.

## 9. Bàn giao giữa hai agent

Chuyển việc qua tay: viết `coordination/handoffs/YYYY-MM-DD-<agent>-<slug>.md` theo `coordination/handoffs/_TEMPLATE.md`. Ghi rõ đã làm gì, file nào, còn thiếu gì, chi tiết nào **chưa** kiểm chứng, bước kế tiếp.

Agent nhận việc đọc handoff trước, không đoán từ diff. Diff cho biết cái gì đã đổi, không cho biết cái gì đã được kiểm tra.

## 10. Kiểm tra tự động

```bash
python scripts/registry.py check
python scripts/claims.py check
python scripts/thread.py check
```

Ba lệnh này chạy trong CI (`.github/workflows/agent-checks.yml`) trên mọi PR và mọi push lên `main`. Chạy tại máy trước khi mở PR.

CI chỉ bắt lệch máy móc: mã trùng, thư mục tập không có trong sổ, `next_case_number` sai, status lạ, sửa sổ mà không lưu snapshot, claim chồng nhau, luồng review sai lượt hoặc vượt trần vòng. Nó không bắt được nguồn sai, kể sai hay suy diễn không có chứng cứ — phần đó vẫn cần agent review đọc thật.

## 11. Không agent nào tự làm

- Không đăng video, không gửi tin nhắn hay email cho nguồn, không thanh toán, không đưa nội dung ra ngoài repo khi người dùng chưa cho phép.
- Không ghi `published` khi chưa có xác nhận của người dùng.
- Không xóa lịch sử trong `registry.json` hay `history/` để dùng lại mã.
- Không force-push `main`.
- Không sửa file này để nới luật cho riêng mình. Đổi luật thì mở PR và nói rõ lý do.
