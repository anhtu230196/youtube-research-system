---
name: cross-review
description: Quy trình review chéo giữa Codex, Claude và Gemini trên một pull request của repo này — đọc PR, đối chiếu nguồn, viết nhận xét theo nhãn CHAN/SUA/HOI/OK, trả lời review. Dùng khi được giao review bài của agent khác, khi nhận review về bài mình, hoặc khi hai agent bất đồng. Cross review, PR review, doi chieu nguon.
---

# Review chéo giữa các agent

Ba agent không nói chuyện trực tiếp được. Pull request là kênh duy nhất họ thật sự trao đổi với nhau. Skill này là cách dùng kênh đó cho đúng.

Luật nền: [`AGENTS.md`](../../../AGENTS.md) mục 8.

## Nguyên tắc

- Agent viết ra một thứ không review thứ đó.
- Không agent nào merge PR của chính mình.
- Review chéo kiểm **nguồn, tính nhất quán và luật**. Duyệt nội dung câu chuyện vẫn là việc của Tú.
- Không sửa thẳng vào nhánh của agent khác. Viết nhận xét.

## Khi được giao review

### 1. Lấy toàn cảnh

```bash
gh pr view <n> --json title,body,headRefName,files
gh pr diff <n>
gh pr checks <n>
```

Đọc claim đang giữ mã đó (`coordination/claims/`) và handoff gần nhất nếu có. Diff cho biết cái gì đã đổi, không cho biết cái gì đã được kiểm tra.

### 2. Chạy kiểm tra máy trước khi đọc bằng mắt

```bash
git fetch origin && git checkout <headRefName>
python scripts/registry.py check --diff-base origin/main
python scripts/claims.py check
```

Lỗi máy bắt được thì đừng tốn công đọc tay.

### 3. Đối chiếu nguồn — phần quan trọng nhất

Với kịch bản và hồ sơ nghiên cứu, đây là việc thật sự có giá trị:

- Mở lại từng URL trong `sources` và trong các dòng `Đối chiếu`. Ghi rõ link nào mở được, link nào chết.
- Với mỗi nút thắt của câu chuyện, hỏi: nguồn có **nói đúng điều này** không, hay chỉ nói một phần rồi kịch bản suy ra phần còn lại?
- Phân biệt cáo buộc với kết luận. Hồ sơ điều tra và bài báo thời điểm xảy ra thường là cáo buộc.
- Bắt suy diễn tâm lý, thoại không có nguồn, cảnh không ai chứng kiến được dựng thành sự thật.
- Bài sao chép lẫn nhau không phải xác nhận độc lập. Truy ngược về nguồn gốc.
- Kiểm diễn biến mới nhất: án đã có kháng cáo chưa, lịch xét duyệt có đổi không.

### 4. Viết nhận xét

Nhận xét ngắn: comment thẳng trên PR. Báo cáo dài, đối chiếu từng claim: viết `coordination/reviews/<n>-<agent>.md` theo template, commit lên nhánh của PR, rồi comment ngắn trỏ tới file.

Mỗi ý một nhãn:

| Nhãn | Nghĩa |
| --- | --- |
| `CHAN:` | Không merge được cho tới khi sửa |
| `SUA:` | Nên sửa, không chặn merge |
| `HOI:` | Chưa rõ, cần người viết trả lời |
| `OK:` | Đã kiểm và đạt — ghi rõ kiểm bằng cách nào |

Mỗi ý kèm `file:dòng`, và kèm `claim_id` hoặc `source_id` khi nói về nội dung.

```bash
gh pr review <n> --comment --body-file coordination/reviews/<n>-claude.md
gh pr comment <n> --body "CHAN: scripts/02-script-vi.md:88 — C14 noi ... nhung S03 chi noi ..."
```

Không dùng `--approve` hay `--request-changes` trừ khi Tú yêu cầu; `--comment` giữ quyền quyết định ở người.

### 5. Nói rõ đã không kiểm cái gì

Bắt buộc. Review nửa vời mà báo cáo như đã đọc hết làm hỏng cả cơ chế: agent sau sẽ tin là phần đó đã được kiểm.

## Khi nhận review về bài mình

- Trả lời **từng** mục `CHAN:` và `HOI:` — đã sửa ở commit nào, hoặc không sửa vì lý do gì. Không im lặng bỏ qua.
- Không sửa lấy lệ cho comment biến mất. Nếu người review hiểu sai, nói rõ tại sao thay vì đổi bừa.
- `CHAN` chưa được giải quyết thì PR không merge.

## Khi hai agent bất đồng

Dừng. Viết một comment nêu cả hai lập luận và điều gì sẽ giải quyết được bất đồng đó — một nguồn cụ thể, một quyết định của Tú. Để Tú quyết. Không agent nào tự phá thế bế tắc bằng cách merge.

## Điều không nhận xét

Không viết lại theo giọng của mình. Nhận xét cái sai và cái thiếu chứng cứ, không nhận xét cái khác gu. Kịch bản là của người viết chừng nào nó không sai.
