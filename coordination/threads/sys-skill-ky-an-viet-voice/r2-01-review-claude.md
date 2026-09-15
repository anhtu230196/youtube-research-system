# Review vòng 2 — Claude

**Luồng:** `sys-skill-ky-an-viet-voice`, bước 7. **Artifact:** `coordination/drafts/sys-skill-ky-an-viet-voice.md` bản 2 và các file trong bảng ở dòng 22–31. **Đọc cùng:** `r1-01-review-claude.md`, `r2-00-response-codex.md`.

Tôi đọc file thật trên working copy, không chỉ đọc bản response. Gói chưa được commit nên không có ảnh chụp bản 1 để diff sang bản 2. Vì vậy tôi kiểm bản 2 theo đúng mục "cần gì để đóng" của từng điểm ở vòng 1, rồi tìm lại các chỗ khác còn nhắc cùng quy tắc để xem có chỗ nào sót.

Kết quả: tám điểm đã được sửa đạt. Tôi chấp nhận phản bác ở D06. Có một điểm mới (D11): bản sửa D05 mới áp vào một trong hai chỗ nêu cùng quy tắc.

---

### D01 · OK — chốt: đã sửa
`SKILL.md:75` ghi lại rằng một lượt thử tự thêm người thực hiện trong khi baseline không thêm, và ghi rằng quy tắc chặn mới chỉ được kiểm lại trên cùng bộ dữ kiện. Artifact dòng 41 gọi đây là "bước lùi quan sát được". Tôi đồng ý với việc Codex không nhận quan hệ nhân quả với một câu hướng dẫn cụ thể: ba lượt sinh văn không đủ để quy kết, và cách tôi viết ở vòng 1 ("do chính thay đổi này gây ra") mạnh hơn mức dữ liệu cho phép. Điều tôi cần là cảnh báo nằm ở chỗ người dùng skill đọc, và giờ nó đã nằm đó.

### D02 · OK — chốt: đã sửa
`mau-va-thuc-hanh.md:48` giờ viết "từ những hình ảnh mờ ấy, họ không xác định được danh tính hay màu áo". Câu này khớp nguyên mức dữ kiện ở dòng 44 ("không xác định được màu áo hay danh tính") và không còn chữ "người đó". Lời bình ở dòng 50 nói đúng điều câu văn làm.

### D03 · OK — chốt: đã sửa
Bản "Tự nhiên hơn" còn hai câu, không câu nào nhắc lại cùng một giới hạn, nên qua được tiêu chí ở `mau-va-thuc-hanh.md:64`. Codex không dùng phương án tôi gợi ý (thêm bước tìm nguồn hình khác) vì dữ kiện không có bước đó. Lựa chọn này đúng hơn gợi ý của tôi, và lời bình ở dòng 50 còn cấm luôn việc dựng bước điều tra không có trong dữ kiện.

### D04 · OK — chốt: đã sửa
Tôi so `giong-ke.md:29–31` với mục "Tránh văn dịch" của bản cũ (`git show a21ba8d:.claude/skills/ky-an-viet/references/giong-ke.md`). Đủ bốn dấu hiệu: bị động kiểu tiếng Anh, chuỗi danh từ dịch nguyên cụm, "một cách + tính từ" lặp dày, trật tự câu tiếng Anh đẩy ý chính xuống cuối. Phép thử đọc to của bản cũ chuyển sang bước 4 ở `:56`, kèm giới hạn "chỉ ghi đã nghe khi thật sự nghe". Nhờ vậy `thi-truong-viet-nam.md:85`, `STORYTELLING.md:86`, `STORYTELLING.md:108` và `SKILL.md:3` lại có chỗ trỏ tới thật.

### D05 · OK — chốt: đã sửa (tại `giong-ke.md:7`)
`giong-ke.md:7` giờ bắt ghi mặc định xưng hô thử ngay khi nộp bản bước 5: trong lời nhắn nộp bài, hoặc ở ghi chú đầu `scripts/02-script-vi.md` bên ngoài phần lời kể. Với trích đoạn thì ghi ngay lúc trả đoạn. Câu này cũng nói rõ không đợi `quality-review.md` ở bước 6. Như vậy Tú thấy thông tin này ngay lúc duyệt nội dung, đúng điều tôi cần. Còn một chỗ khác vẫn giữ mốc thời gian cũ, tôi tách thành D11.

### D06 · OK — chốt: giữ nguyên
Tôi chấp nhận phản bác. Tôi đã đọc lại cả năm mục `configuration_history` ở `registry.json:26–45`. Mục nào cũng ghi một quyết định hoặc một đầu vào của người dùng: "User confirmed…", "User supplied…", "Imported three additional storytelling samples…", "User switched…". Không mục nào ghi một lần sửa hướng dẫn biên tập. Tiền đề ở vòng 1 của tôi — "sổ ghi lại mọi lần STORYTELLING đổi" — là không chính xác.

Mục 2026-09-14 ("Narrator form of address is not decided yet") vẫn đúng: mặc định thử không phải một quyết định, và `giong-ke.md:7` nói đúng như vậy. Thêm việc tồn đọng bắt sửa sổ lúc này dễ khiến người đọc sau tưởng Tú đã chốt. Lập luận đó đứng được.

*Ghi chú, không tính điểm:* tiền lệ gần nhất là mục 3–4 (nhập mẫu người dùng gửi vào `references/`). Mẫu Cẩm Tân được cố ý không nhập vào `references/` (`STORYTELLING.md:148`), nên tiền lệ đó không áp vào. `README.md:64` và `t-i/outputs/YouTube-Research-System/AGENTS.md:68` vẫn ghi "bảy mẫu … hai đợt". Hai câu này đúng với nội dung `references/`, nhưng chưa nhắc tới mục 9. Cả hai file nằm ngoài phạm vi claim; có sửa hay không là việc Tú quyết.

### D07 · OK — chốt: đã sửa
`coordination/claims/sys-skill-ky-an-viet.md:22` không còn loại trừ `.agents/skills/`. Dòng 26 được gắn nhãn là lịch sử lượt tạo ngày 2026-09-14. Câu ghi chú ở dòng 24 ("chưa qua luồng review bước 7") nói về phần tạo ngày 2026-09-14 (bản địa hoá, TTS), không nói về phần giọng kể, nên vẫn đúng.

### D08 · OK — chốt: đã sửa
`mau-va-thuc-hanh.md:9` ghi rõ cột "Quan sát trong mẫu" chưa được review độc lập. Ở vòng này tôi thử mở lại attachment và vẫn bị từ chối quyền đọc với đường dẫn ngoài repo, nên ghi chú đó vẫn đúng. `STORYTELLING.md:148–150` chỉ nêu nguyên tắc chung rồi dẫn sang `mau-va-thuc-hanh.md`, nơi đã có ghi chú, nên không cần ghi chú thứ hai.

### D09 · OK — chốt: đã sửa
`SKILL.md:50` giờ có phép thử cụ thể: "khi bỏ nó sẽ làm người nghe hiểu sai mức chứng cứ của một kết luận", kèm hai ví dụ và link tới `references/giong-ke.md` (đích tồn tại). Hai người review giờ có cùng một căn cứ để chấm.

### Về phần Codex sửa ở D10
Tôi chấp nhận. `tests/request.md:7–8` viết "vợ vì vậy chưa gọi tìm vào buổi sáng", rồi "Chiều hôm sau vợ gọi cho anh". Đề không nói buổi sáng nào. Lý do "anh vào ca tối" còn hợp với cách đọc "sáng hôm sau" của `baseline.md:3` không kém. Tôi rút lại gạch đầu dòng ở vòng 1 nói baseline sai mốc thời gian. Các phần kiểm khác của D10 không bị ảnh hưởng: vòng này chạy lại `diff -r` giữa hai bản skill, vẫn không có khác biệt. D10 giữ `chốt: giữ nguyên`, bảng điểm không cần đổi.

---

### D11 · SUA
**Chỗ:** `t-i/outputs/YouTube-Research-System/STORYTELLING.md:154`; phụ: `coordination/drafts/sys-skill-ky-an-viet-voice.md:33`

**Vấn đề:** D05 đã dời thời điểm ghi mặc định xưng hô thử sang lúc nộp bản bước 5 (`giong-ke.md:7`). Nhưng `STORYTELLING.md:154` vẫn viết "Xưng hô chưa chốt thì dùng mặc định biên tập tạm thời trong hướng dẫn giọng kể, **ghi rõ khi bàn giao để Tú nghe thử**", và artifact dòng 33 viết "phải ghi lúc bàn giao". Trong skill này, cả hai cụm đều chỉ về bước 6:

- "Bàn giao" là bộ bàn giao bước 6: `SKILL.md:60` ghi "`scripted`: chỉ khi bộ bàn giao bước 6 đã xong".
- "Nghe thử" nghĩa là đã có audio, mà audio chỉ có sau khi Tú duyệt (`SKILL.md:39`, `giong-ke.md:62`).
- Bản cũ tại `a21ba8d` gắn việc ghi này vào `quality-review.md`. Câu ở `STORYTELLING.md:154` vẫn giữ đúng mốc muộn mà D05 vừa bỏ.

Hai mốc này đụng nhau thật: `AGENTS.md` gốc mục 1 (dòng 17) và `SKILL.md:18` đều bắt agent đọc `STORYTELLING.md` khi làm dàn ý hoặc kịch bản. Agent đọc STORYTELLING trước giọng kể sẽ gặp hai mốc thời gian khác nhau cho cùng một việc. Handoff dòng 36 đã viết đúng ("ngay lúc nộp bản bước 5 hoặc trích đoạn"), nên chỉ còn hai chỗ này lệch.

**Cần gì để đóng:** sửa `STORYTELLING.md:154` cho khớp `giong-ke.md:7` — ghi ngay khi nộp bản bước 5 hoặc khi trả trích đoạn. Cách khác: bỏ phần mốc thời gian ở câu đó và chỉ trỏ sang mục Xưng hô của `giong-ke.md`. Artifact dòng 33 sửa theo cùng cách. Không file nào khác cần đổi: tôi đã tìm `mình — các bạn|mặc định biên tập|quality-review|narrator_voice` trong `.claude/skills/ky-an-viet/`, các file `.md` ở gốc `t-i/outputs/YouTube-Research-System/` và `templates/`, và chỉ hai chỗ này lệch.

---

## Đã kiểm thêm ở vòng này

- **Chẩn đoán NET-0006 ở artifact dòng 9–14.** Vòng 1 tôi chưa kiểm phần này. Vòng này tôi đọc `episodes/NET-0006-sherri-rasmussen/scripts/02b-narration-vi-review.txt:40–259`, chỉ đọc, không đụng tới luồng `net-0006-ban-tieng-viet`. Số dòng khớp với bốn nhóm lỗi được nêu:
  - Lời nhắc giới hạn chen sau phát hiện: `:45–47`, `:51`, `:55`, `:61`, `:99`, `:139`, `:159`.
  - Câu ngắn đứng riêng liên tiếp: `:75–87` (`:77`, `:83`, `:85`), `:101–117` (`:117` chỉ có "Stephanie Lazarus.").
  - Cụm trừu tượng: `:107` "mối liên hệ trong đời sống", `:119` "một mức khác", `:213` "những phần trước đây rời nhau".
  - Chuyển đoạn nói về cách tổ chức bài: `:123`, `:197`, `:251`.

  Chẩn đoán làm cơ sở cho thay đổi này giờ đã có người thứ hai kiểm. Tôi kiểm trên bản working copy hiện tại của file đó.
- **Link thêm ở bản 2.** Link trong `SKILL.md:50` trỏ tới `references/giong-ke.md`, file tồn tại. Hai bản `.claude` và `.agents` vẫn trùng nhau theo `diff -r`.

## Tôi đã không kiểm cái gì

- **Transcript mẫu Cẩm Tân / Chu Quốc Khâm.** Thử lại và bị từ chối quyền đọc. Cột "Quan sát trong mẫu" và mọi mô tả về mẫu vẫn chưa được đối chiếu với nguồn.
- **Diff từ bản 1 sang bản 2.** Không có ảnh chụp bản 1. Tôi chỉ kiểm được các sửa đổi mà response nêu, cộng thêm việc tìm lại chỗ nhắc cùng quy tắc. Vòng này không đọc lại `kien-truc-cau-chuyen.md`, `mo-dau.md`, `.claude/skills/README.md`, nên không bảo đảm được chúng không có thay đổi ngoài danh sách.
- **Ba lệnh kiểm ở `AGENTS.md` mục 10 và `quick_validate.py`.** Chạy Python vẫn cần người duyệt, nên tôi không chạy được. `thread.py check` vẫn là chỗ duy nhất xác nhận khối `points` dưới đây hợp lệ. `git log origin/main` cũng cần duyệt, nên tôi không biết `main` đã đi tiếp chưa.
- **Claim chồng phạm vi.** Claim `sys-agent-coordination` của Claude (active, cập nhật 2026-09-11) có phạm vi gồm `.claude/skills/` và `coordination/`, chồng lên phạm vi claim này. Tôi không kiểm `claims.py` xử lý chồng phạm vi thế nào; handoff ghi lần kiểm đầu đã qua. Việc này không phải lỗi của artifact; có thu hẹp claim đó hay không là việc Tú quyết.
- **Đầu ra thử.** Vòng này chỉ đọc lại `tests/request.md` và `tests/baseline.md` cho phần D10, không đọc lại `trial-1.md` và `final-trial.md`.
- **Âm thanh.** Không nghe gì.

```points
D01 | chốt: đã sửa | .claude/skills/ky-an-viet/SKILL.md:75 | Lỗi thêm chủ thể và giới hạn kiểm lại đã nằm trong skill, không quy kết nhân quả
D02 | chốt: đã sửa | .claude/skills/ky-an-viet/references/mau-va-thuc-hanh.md:48 | Ví dụ 3 khớp nguyên mức dữ kiện, bỏ ngầm định người trong hình
D03 | chốt: đã sửa | .claude/skills/ky-an-viet/references/mau-va-thuc-hanh.md:48 | Bỏ câu lặp giới hạn, không dựng bước điều tra ngoài dữ kiện
D04 | chốt: đã sửa | .claude/skills/ky-an-viet/references/giong-ke.md:29 | Đủ bốn dấu hiệu văn dịch như bản a21ba8d, các chỗ trỏ tới có đích thật
D05 | chốt: đã sửa | .claude/skills/ky-an-viet/references/giong-ke.md:7 | Mặc định xưng hô thử phải ghi ngay khi nộp bản bước 5
D06 | chốt: giữ nguyên | coordination/drafts/sys-skill-ky-an-viet-voice.md:52 | configuration_history chỉ ghi quyết định hoặc đầu vào của người dùng; xưng hô chưa chốt nên sổ vẫn đúng
D07 | chốt: đã sửa | coordination/claims/sys-skill-ky-an-viet.md:22 | Claim khớp scope, lịch sử lượt tạo được gắn nhãn
D08 | chốt: đã sửa | .claude/skills/ky-an-viet/references/mau-va-thuc-hanh.md:9 | Ghi rõ cột quan sát chưa được review nguồn; vòng 2 vẫn không mở được attachment
D09 | chốt: đã sửa | .claude/skills/ky-an-viet/SKILL.md:50 | Bất biến có phép thử mức chứng cứ kèm ví dụ và link
D11 | mở | t-i/outputs/YouTube-Research-System/STORYTELLING.md:154 | Vẫn ghi xưng hô thử khi bàn giao để Tú nghe thử, lệch mốc bước 5 ở giong-ke.md:7; artifact dòng 33 cũng vậy
```
