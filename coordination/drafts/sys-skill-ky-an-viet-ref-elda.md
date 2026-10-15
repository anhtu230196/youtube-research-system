# Bài học từ mẫu REF-09 (vụ Elda) cho skill kỳ án tiếng Việt — bản 1

**Ngày:** 2026-10-15. **Tác giả:** Claude. **Claim:** `sys-skill-ky-an-viet-ref-elda`. **Bước:** 7 (skill). **Người review:** Codex và Gemini. **Nhánh:** `claude/skill-ref-elda`. **Đối chiếu:** `git diff 9c4eafb` (commit claim trên `main`).

Gói được mở rộng một lần trong ngày, trước khi có lượt review nào: sau khi đọc bản đề xuất r1-00, Tú chốt sửa luật nghiệp vụ cho khớp skill (dòng 60 và 68 của `t-i/outputs/YouTube-Research-System/AGENTS.md`). Chưa người review nào đọc bản hẹp hơn, nên đây vẫn là bản 1. Câu hỏi về người dưới 18 tuổi trong r1-00 vẫn chờ Tú, không nằm trong gói.

## Vì sao có thay đổi này

Ngày 2026-10-15, Tú gửi transcript một tập của kênh Truyện Ma Bẻ Lái — cùng kênh với mẫu Cẩm Tân đã phân tích ngày 2026-09-15 — và hỏi dự án học thêm được gì, bỏ qua phần dẫn về vua Carlos II. Lượt phân tích tìm sáu điểm đáng học và một nhóm lỗi skill chưa chặn rõ. Tú duyệt cả gói và yêu cầu lưu transcript vào `references/`.

Phần lớn kỹ thuật của kênh này đã có trong skill sau lần phân tích mẫu Cẩm Tân: người kể hỏi và nhắc, mở nhánh giả thuyết, lời thú nhận mở thêm một lớp, đặt rồi trả chi tiết đời thường. Gói này chỉ thêm phần chưa có.

### 1. Lời kể của người trong cuộc bị lật

Cả vụ trong mẫu dựng trên lời khai của người phụ nữ duy nhất còn sống trong căn hộ; về sau cảnh sát kết luận cô dựng chuyện. Mẫu kể lời khai như cảnh thật và để khoảng 60% phần vụ án (tính theo ký tự) trôi qua trước khi lật. Skill hiện cấm kể niềm tin như sự thật khách quan rồi rút lại (`kien-truc-cau-chuyen.md`, mục Hướng điều tra sai) nhưng chưa chỉ cách giữ cú lật mà vẫn đúng luật. Hình dạng này rất hay gặp ở nhóm "hiện trường dàn dựng" mà `chon-vu.md` đã nhận vào phạm vi.

### 2. Câu hỏi treo gắn với một việc đang chờ kết quả

Mẫu nêu camera "đang thu nhưng cần thời gian" và lá thư nặc danh ở ngày thứ ba, rồi trả cả hai ở đoạn lật. Khác câu úp mở chung chung, người nghe biết mình đang chờ kết quả của việc gì.

### 3. Đoạn giữa khi điều tra bế tắc

Mẫu loại từng hướng bằng một dữ kiện (người yêu cũ đang ở tù, đối thủ có ngoại phạm) và dùng việc dư luận chê cảnh sát làm lực căng. Danh sách nguồn căng thẳng ở `STORYTELLING.md` mục 4 chưa có dư luận.

### 4. So sánh với đời sống Việt Nam

Giờ ăn tối muộn, đồ biker, trò nhét tờ rơi khe cửa, lỗi chính tả do phát âm — mỗi cái giải thích một cơ chế bằng trải nghiệm của người nghe Việt. `thi-truong-viet-nam.md` mới chỉ cấm so sánh sai; tìm nhanh trong ba bản kịch bản NET-0006/NET-0007 không thấy chỗ nào so sánh kiểu này.

### 5. Lỗi skill chưa chặn rõ

Phần cuối mẫu nối khuyết tật bẩm sinh của người phạm tội với động cơ giết người, kèm "theo thống kê" không nguồn; một đoạn khác lấy nhận định chung về trẻ tự kỷ làm chứng cứ. Danh sách không gắn tội phạm với nhóm người trong skill có vùng miền, tôn giáo, dân tộc, giới tính, nhưng chưa có khuyết tật hay chẩn đoán bệnh. Mục "Ngôn từ" chứa danh sách đó lại nằm dưới tiêu đề "Vụ án tại Việt Nam".

Thêm một thuật ngữ: mẫu gọi mức án là "chung thân", trong khi Tây Ban Nha có chế định *prisión permanente revisable* với cơ chế xem xét lại riêng. Bảng thuật ngữ hiện chỉ có ví dụ Mỹ.

## Gói nội dung đóng băng để review

Đọc file thật trên nhánh, không chỉ đọc bảng này.

| File | Thay đổi |
| --- | --- |
| `references/kien-truc-cau-chuyen.md` | Dòng 3: thêm hình dạng vào danh sách. Mục mới "Lời kể của người trong cuộc bị lật" (dòng 11–24): điều kiện dùng, sáu quy tắc. Mục mới "Khi điều tra đi vào bế tắc" (dòng 26–32). Đoạn mới về câu hỏi treo có hẹn (dòng 48) |
| `references/thi-truong-viet-nam.md` | Hàng *prisión permanente revisable* trong bảng thuật ngữ và một đoạn về tên tội danh nước ngoài (dòng 25–27). Đoạn "So sánh với đời sống Việt Nam" với năm điều kiện (dòng 31–37). Mục Ngôn từ: ghi rõ áp dụng cho mọi vụ, thêm khuyết tật, tình trạng sức khoẻ, cấm tự chẩn đoán (dòng 74–76). Hai dòng mới trong danh sách kiểm |
| `references/giong-ke.md` | Dòng 45: thêm khuyết tật và chẩn đoán bệnh vào câu không gắn tội phạm với nhóm người. Đoạn mới dòng 47: không tự suy trạng thái tâm lý, nhận định chuyên gia chỉ áp cho người được đánh giá, thống kê cần nguồn. Đoạn mới dòng 66: động cơ chưa rõ thì nói chưa rõ |
| `references/mau-va-thuc-hanh.md` | Mục mới "Điều học từ mẫu thứ hai: vụ Elda" (dòng 22–43): bảng sáu quan sát, danh sách không bê nguyên. Ví dụ 7 — kể lời khai sẽ bị lật (dòng 107). Ví dụ 8 — so sánh với đời sống Việt Nam (dòng 121). Cả hai dùng dữ kiện hư cấu |
| `SKILL.md` | Dòng 22: nhắc mẫu REF-09 trong "Đích giọng kể". Dòng 77: phần chưa kiểm chứng cho các bổ sung mới |
| `.agents/skills/ky-an-viet/` | Bản sao năm file trên, trùng từng byte |
| `t-i/outputs/YouTube-Research-System/STORYTELLING.md` | Dòng 3 và một đoạn trỏ ở cuối mục 9 |
| `t-i/outputs/YouTube-Research-System/AGENTS.md` | Dòng 60: thêm khuyết tật, tình trạng sức khoẻ, chẩn đoán bệnh, cấm tự chẩn đoán rối loạn khi hồ sơ không có giám định, ghi rõ áp dụng cho mọi vụ — khớp mục Ngôn từ của `thi-truong-viet-nam.md`. Dòng 68: ghi thêm mẫu Cẩm Tân và REF-09 sau bảy mẫu ban đầu. Tú chốt 2026-10-15 |
| `t-i/outputs/YouTube-Research-System/references/ref-09-elda-survivor-account.txt` | Transcript nguyên văn, trích bằng script từ log phiên chat, không gõ lại |
| `t-i/outputs/YouTube-Research-System/references/manifest.json` | Mục REF-09 kèm SHA-256 |

Không đổi `registry.json`, trạng thái case, `episodes/`, phần còn lại của luật nghiệp vụ (kể cả quy tắc người dưới 18 tuổi ở dòng 58), `chon-vu.md`, `mo-dau.md`, `nghien-cuu-va-kiem-chung.md`, `ban-thu-am.md`, cấu hình model hay skill toàn cục.

## Đã kiểm

- `diff -r .claude/skills/ky-an-viet .agents/skills/ky-an-viet`: không khác biệt.
- 45 link markdown cục bộ trong skill và `STORYTELLING.md`: mọi đích tồn tại.
- SHA-256 của REF-09 trong manifest khớp file: `10CE1378AB2C943748B25356983F140A0CB4722D9EE7F037C6856B8683E0394C`.
- Tỷ lệ trong mục mẫu thứ hai đếm bằng script theo ký tự, với mốc phân đoạn do tác giả chọn: phần dẫn trước vụ chính 15,3% transcript; trước đoạn lật 59,6% phần vụ án; phân tích tâm lý 6,3% so với đoạn bác lời giải thích thứ hai 3,8%.
- Ba lệnh `registry.py check`, `claims.py check`, `thread.py check` chạy trước khi đẩy nhánh.

## Chưa kiểm

- Không chạy bài thử hành vi nào với hướng dẫn mới.
- Không mở nguồn tiếng Tây Ban Nha nào về vụ Elda. Mọi tên, ngày, tình tiết vụ án trong skill được ghi là định vị trong transcript.
- Mô tả *prisión permanente revisable* viết từ hiểu biết chung về luật hình sự Tây Ban Nha, chưa dẫn nguồn trong repo. Không khẳng định vụ Elda áp dụng chế định này.
