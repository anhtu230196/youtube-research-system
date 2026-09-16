# Bốn thay đổi Tú chốt cho skill kỳ án tiếng Việt — bản 2

**Ngày:** 2026-09-16. **Tác giả:** Claude. **Claim:** `sys-skill-han-viet-suy-ngam`. **Bước:** 7 (skill). **Người review:** Codex và Gemini — Tú chỉ định thêm Gemini, bảng ở `AGENTS.md` mục 8 mặc định chỉ có Codex.

Gói mở rộng trong ngày: ba điểm đầu viết xong buổi sáng, điểm thứ tư được Tú bổ sung ngay sau đó và gộp vào cùng bản. Chưa có vòng review nào chạy trên bản hẹp hơn, nên đây vẫn là bản 1.

## Vì sao có thay đổi này

Ngày 2026-09-15, Tú yêu cầu rà `.claude/skills/ky-an-viet/` xem có đúng với mẫu Cẩm Tân Đại Lâu / Chu Quốc Khâm mất tích đêm Trung thu không. Lượt rà nêu 11 đề xuất, Tú chốt ba, rồi bổ sung điểm thứ tư sau khi đưa một ví dụ cụ thể về cách giữ tò mò bằng nhánh giả thuyết.

### T1 — kể suy nghĩ nhân vật khi nguồn có lời khai

`giong-ke.md:45` cấm bịa ý nghĩ nhưng không nói khi nguồn *có* lời khai về suy nghĩ thì viết thế nào. `STORYTELLING.md:80` đã cho phép ("tâm lý được kể khi có lời nói/ghi chép hỗ trợ") mà skill không có ví dụ nào. Quan sát trên mẫu: phần lớn cảm giác gần gũi đến từ việc kể theo suy nghĩ của người vợ; bản NET-0006 thì né hẳn lớp này.

### S1 — tên người và địa danh gốc Hán

`thi-truong-viet-nam.md:15` và `AGENTS.md:56` đều ghi "tên người giữ chữ viết gốc", viết cho vụ án Mỹ. Với vụ Đài Loan hay Trung Quốc, chữ viết gốc là chữ Hán (周國欽) — người nghe không đọc được, và báo Việt lẫn mẫu đều dùng Hán Việt. Rủi ro thật kèm theo: tra âm theo tai thay vì theo chữ Hán sinh ra lỗi như "Lâm Sâm Quang Quang" trong transcript, chữ gốc 林森觀光大樓, đọc đúng là Lâm Sâm Quan Quang.

### Đoạn kết — phương án B

`giong-ke.md:60` cấm hẳn "bài học đạo đức". Mẫu kết bằng một đoạn dài về ngoại tình. Tú chọn phương án B: cho phép một đoạn suy ngẫm ngắn, có rào chắn. Trong vụ mẫu, nạn nhân chính là người ngoại tình, nên rào chắn quan trọng nhất là không đổ lỗi cho nạn nhân.

### Mở nhánh giả thuyết

Tú nêu nhu cầu: nhiều chỗ cần suy luận để người nghe tò mò, nhưng không phải kết luận — mà là đặt câu hỏi hoặc nêu vài khả năng để thấy hướng điều tra khó tới đâu. Ví dụ Tú đưa: hiện trường chỉ có vân tay của những người hiếu kỳ, không có vân tay của nạn nhân, vậy hoặc hung thủ đã lau hiện trường, hoặc hung thủ đang đứng trong đám đông.

Skill mới có đúng một câu cho phép (`kien-truc-cau-chuyen.md:15`: cách hiểu ban đầu có thể là "một khả năng người nghe có thể nghĩ tới") và không có cách làm nào. Mẫu thì dùng kỹ thuật này hai lần: vụ tầng 11 đi qua ba hướng, vụ chính đi qua tình, tiền, thù hận.

Điểm này chạy hoàn toàn bằng dữ kiện đã xác lập nên không đụng tới ranh giới bịa tình tiết. Việc nới lỏng quy tắc "phải có nguồn" mà Tú nhắc tới hôm nay được tách riêng, chưa nằm trong gói này.

## Gói nội dung đóng băng để review

Đọc file thật, không chỉ đọc bảng này. Đối chiếu bằng `git diff` so với `945c6f2`.

| File | Thay đổi |
| --- | --- |
| `references/giong-ke.md` | Dòng 45: cho phép kể suy nghĩ khi nguồn ghi lại, kèm cách quy nguồn và link tới Ví dụ 5. Mục "Người kể có mặt": trỏ sang mục mở nhánh. Mục "Kết thúc": viết lại theo phương án B, ba điều kiện và một cặp ví dụ ranh giới |
| `references/mau-va-thuc-hanh.md` | Ví dụ 5 (suy nghĩ có lời khai) và Ví dụ 6 (mở nhánh thay cho kết luận), đều dùng dữ kiện hư cấu |
| `references/kien-truc-cau-chuyen.md` | Mục mới "Mở nhánh giả thuyết": bảy quy tắc và luật cho câu hỏi treo |
| `references/thi-truong-viet-nam.md` | Mục Tên viết lại theo S1; thêm hai dòng vào danh sách kiểm trước khi nộp bản tiếng Việt |
| `references/ban-thu-am.md` | Tên Hán Việt là âm tiếng Việt nên engine đọc như chữ thường; `pronunciation.md` ghi cặp chữ Hán → Hán Việt |
| `.agents/skills/ky-an-viet/references/` | Bản sao năm file trên, trùng từng byte |
| `t-i/outputs/YouTube-Research-System/AGENTS.md` | Dòng 56: quy tắc tên theo S1, ghi rõ Tú chốt ngày 2026-09-16 |

Không đổi `registry.json`, trạng thái case, `episodes/`, `STORYTELLING.md`, `SKILL.md`, `chon-vu.md`, `mo-dau.md`, `nghien-cuu-va-kiem-chung.md`, cấu hình model hay skill toàn cục.

## Hai sửa đổi có sẵn trong working copy

Trước khi mình bắt đầu, `giong-ke.md` đã có hai sửa đổi chưa commit, sửa lúc 2026-09-15 17:44, hai bản `.claude` và `.agents` trùng nhau. Chưa rõ ai sửa:

1. Dòng 45: thêm "đặc biệt ưu tiên nhấn mạnh khi chứng cứ khoa học/pháp y lật tẩy được sự mâu thuẫn trong lời khai của nghi phạm". **Giữ nguyên.**
2. Dòng 60: đã nới một phần lệnh cấm bài học đạo đức. **Được viết chồng lên** bằng bản phương án B đầy đủ hơn, giữ đúng ý cho phép đúc kết về cơ chế hành vi.

Cần Tú xác nhận đây là sửa đổi của Tú. Nếu của một agent khác thì phải truy lại lượt đó trước khi gói này vào `main`.

## Đã kiểm

- Hai bản skill trùng nhau: `diff -r .claude/skills/ky-an-viet .agents/skills/ky-an-viet` không khác biệt.
- Link markdown cục bộ trong skill và luật nghiệp vụ: mọi đích tồn tại, kể cả link mới từ `giong-ke.md` sang `kien-truc-cau-chuyen.md`.
- Ba lệnh `registry.py check`, `claims.py check`, `thread.py check` chạy trước khi đẩy; kết quả ghi ở handoff.
- Các file ngoài phạm vi khai báo không đổi: xem `git status`.

## Chưa kiểm

- **Không chạy kiểm thử hành vi.** Lượt trước Codex dùng subagent; lượt này không chạy. Hai rủi ro chưa được thử: Ví dụ 5 có khiến người viết kể suy nghĩ cả khi nguồn chỉ ghi hành động không; và mục mở nhánh có khiến người viết tự thêm dữ kiện để dựng nhánh cho đủ ba không.
- Đề xuất cho vòng thử sau: dữ kiện thô, trộn một mục có lời khai về suy nghĩ với một mục chỉ có hành động, và một bộ dữ kiện có đúng một bất thường để xem người viết mở mấy nhánh.
- Chưa dùng quy tắc tên Hán Việt trên tập thật. Kênh chưa có tập nào là vụ Đài Loan hay Trung Quốc.
- Chưa nghe audio, không có số liệu giữ chân.
- `registry.json` không đổi: `narrator_voice` vẫn `null`, và bốn quyết định này là quy tắc biên tập, không có trường tương ứng trong sổ.

## Sửa sau vòng 1

Codex nêu bốn điểm, Gemini đồng tình cả bốn và không thêm điểm mới. Tác giả nhận cả bốn, không phản bác điểm nào.

- **D01** — Ví dụ 6 bỏ chữ "hung thủ" và "hắn". Nhánh hai giờ viết là một trong những người đang đứng ngoài đã vào căn nhà từ trước: đúng mức dữ kiện, không gán giới tính, không quy tội. Lỗi này là mâu thuẫn với chính `giong-ke.md:11` trong cùng skill.
- **D02** — Câu dẫn đổi từ "chỉ giải thích được theo mấy hướng" thành "có thể giải thích theo vài hướng". Nhánh bình thường bổ sung giới hạn thu mẫu: không phải bề mặt nào cũng lưu được vân tay. Lời bình dưới ví dụ nêu rõ ba chỗ cần để ý để người đọc sau không lặp lại lỗi.
- **D03** — Quy tắc tên chỉ cho chuyển Hán Việt khi chữ Hán có trong nguồn; nguồn chỉ có tên Latin hoặc phiên âm thì giữ nguyên và ghi là chưa tra được chữ Hán. Cấm suy ngược từ phiên âm ra chữ Hán. Sửa cùng nội dung ở luật nghiệp vụ và ở danh sách kiểm.
- **D04** — Điều kiện thứ nhất của đoạn suy ngẫm siết lại: cơ chế nêu ra phải truy được về dữ kiện đã xác lập trong tập và nói đúng mức chắc chắn của nguồn; động cơ mới chỉ là suy đoán thì chỉ giữ phần hệ quả với con người.

Tú quyết định đóng luồng sau vòng 1, không chạy vòng 2. Vì vậy bốn điểm được chốt ở lượt tác giả, không có lượt reviewer xác nhận các bản sửa. Người đọc sau nên biết giới hạn đó: các bản sửa này chưa qua mắt thứ hai.

## Câu hỏi cần reviewer trả lời

1. Ví dụ 5 có mở đường cho việc suy từ hành động ra ý nghĩ không? Câu rào ở cuối ví dụ đã đủ chưa?
2. Quy tắc tên Hán Việt có chỗ nào mâu thuẫn với phần còn lại của skill hoặc luật nghiệp vụ không, nhất là `ban-thu-am.md` và danh sách kiểm?
3. Đoạn kết phương án B: ba điều kiện có kiểm được không, hay vẫn là chuyện cảm tính? Cặp ví dụ ranh giới có đúng là ranh giới không?
4. Mục mở nhánh giả thuyết có chỗ nào cho phép tự thêm dữ kiện, hoặc quy tội cho người có thể nhận diện, mà mình chưa chặn không? Luật "nhánh nào mở ra phải đóng lại" có kiểm được từ bản thảo không?
