# Đề xuất vòng 1 — Claude

**Artifact:** `coordination/drafts/sys-skill-ky-an-viet-ref-elda.md` bản 1, cùng gói file liệt kê trong đó. **Claim:** `sys-skill-ky-an-viet-ref-elda`. **Nhánh:** `claude/skill-ref-elda`. **Đối chiếu:** `git diff 9c4eafb`. **Người review:** Codex và Gemini.

## Đã quyết định và vì sao

Tú gửi transcript REF-09 ngày 2026-10-15, bảo bỏ qua phần Carlos II, rồi duyệt cả gói đề xuất rút từ mẫu. Gói có ba phần.

**Thêm cách làm.** Hình dạng "lời kể của người trong cuộc bị lật", câu hỏi treo gắn với việc đang chờ kết quả, đoạn giữa khi điều tra bế tắc, và so sánh với đời sống Việt Nam. Mỗi phần có điều kiện dùng và một chỗ kiểm được: Ví dụ 7, Ví dụ 8, hoặc một dòng trong danh sách kiểm.

**Chặn lỗi mẫu mắc mà skill chưa chặn.** Gắn khuyết tật với động cơ, tự chẩn đoán tâm lý, khái quát về một nhóm người làm chứng cứ, và lấp động cơ chưa rõ bằng phân tích của người kể.

**Lưu mẫu.** Transcript nguyên văn thành REF-09, trích bằng script từ log phiên chat để không gõ lại sai; thêm mục manifest có SHA-256. Mẫu Cẩm Tân trước đây chỉ trỏ tới một file `C:/...` trên máy khác, không truy lại được.

Ba lựa chọn có cân nhắc:

1. **Lời kể bị lật chỉ dùng khi đã có bản án hoặc kết luận chính thức.** Không có rào này thì hình dạng này thành công cụ ngầm buộc tội người sống sót. Lời thừa nhận đơn lẻ không đủ, vì skill đã ghi lời thú nhận không tự xác nhận mọi chi tiết.
2. **Quy nguồn một lần kèm lý do, thay vì "theo lời" ở mọi câu.** Câu kiểu "chỉ một người còn sống để kể lại" vừa đúng sự thật vừa tạo căng thẳng. Cách này dựa trên quy tắc đã có ở `giong-ke.md` mục "Giữ chứng cứ rõ": quy nguồn khi bắt đầu một đoạn lời khai, nhắc lại khi đổi nguồn.
3. **Ví dụ 7 dùng một vụ dựng chuyện cướp tiền, không phải án mạng.** Kỹ thuật vẫn đủ — chi tiết trong lời khai trở thành chỗ vênh, đoạn lật đi theo cặp, camera giữ giới hạn — mà ví dụ không phải mô tả bạo lực.

Mục "Ngôn từ" trong `thi-truong-viet-nam.md` đang nằm dưới tiêu đề "Vụ án tại Việt Nam". Mình thêm câu "Áp dụng cho mọi vụ" thay vì chuyển mục, để diff nhỏ và không đổi cấu trúc file.

## Chỗ yếu nhất đã biết

- **Hình dạng lời kể bị lật có thể bị dùng sai theo hướng ngược lại:** người viết đặt câu quy nguồn đầu tiên rồi kể phần còn lại như sự thật khách quan, coi một câu đó là đủ. Quy tắc có ghi "nhắc lại nguồn khi chuyển sang những gì người điều tra tự kiểm", nhưng chưa thử trên bài thật.
- **Đặt sớm dấu hiệu cảnh báo** có thể làm người nghe nghi người kể quá sớm, hoặc thành ngầm buộc tội nếu viết kèm phán xét. Rào hiện tại: chỉ khi có nguồn, kể đúng cách người trong cuộc hiểu lúc đó.
- **Điều kiện "dữ kiện trong phép so sánh cũng cần nguồn"** chưa rõ có buộc cả vế Việt Nam (trò nhét tờ rơi) phải có nguồn hay chỉ vế vụ án. Mình định nghĩa là cả hai, nhưng câu chữ chưa nói rõ.
- **Hàng *prisión permanente revisable*** viết từ hiểu biết chung, chưa có nguồn trong repo.
- **Tỷ lệ trong mục mẫu thứ hai** đếm theo ký tự với mốc phân đoạn do mình chọn; người khác chọn mốc khác sẽ ra số hơi khác.

## Xin review đúng phạm vi

- Mục "Lời kể của người trong cuộc bị lật" (`kien-truc-cau-chuyen.md:11–24`) có mâu thuẫn với mục "Hướng điều tra sai" ngay trên nó, hoặc với câu "Không giấu sự kiện gỡ tội đã biết…" ở `giong-ke.md` không? Có chỗ nào cho phép kể lời khai như sự thật khách quan không?
- Ví dụ 7 và 8 (`mau-va-thuc-hanh.md:107`, `:121`): lời kể có thêm điều gì không có trong khối dữ kiện hư cấu, hoặc tăng mức chắc chắn không?
- Codex: kiểm mô tả *prisión permanente revisable* (`thi-truong-viet-nam.md:25`) bằng nguồn luật Tây Ban Nha.
- Gemini: đối chiếu mục "Điều học từ mẫu thứ hai" (`mau-va-thuc-hanh.md:22–43`) với transcript REF-09 — mình đã quan sát đúng chưa, có chỗ nào gán cho mẫu điều mẫu không nói không.
- Năm điều kiện so sánh (`thi-truong-viet-nam.md:31–37`) đã đủ chặn việc coi hai chế định pháp lý là tương đương, và việc nối giọng vùng miền với học vấn chưa?

## Câu hỏi để Tú quyết, không thuộc review

- Skill giờ cấm gắn tội phạm với khuyết tật và chẩn đoán bệnh, nhưng luật nghiệp vụ `t-i/outputs/YouTube-Research-System/AGENTS.md:60` vẫn chỉ liệt kê vùng miền, tôn giáo, dân tộc, giới tính. Có sửa luật nghiệp vụ cho khớp không?
- `AGENTS.md:58` cấm nêu thông tin nhận diện người dưới 18 tuổi nhưng không nói có áp dụng cho nạn nhân trẻ em đã mất ở vụ nước ngoài, khi báo chí nước đó đã nêu tên, hay không. Vụ Elda và phần lớn vụ có nạn nhân trẻ em vướng chỗ này.
- `AGENTS.md:68` vẫn ghi `STORYTELLING.md` lưu phân tích "bảy mẫu"; giờ đã có thêm mẫu Cẩm Tân và REF-09.

## Chưa làm

Không sửa `registry.json` (kể cả `configuration_history`), luật nghiệp vụ, `episodes/`, các file skill khác. Không chạy bài thử hành vi. Không mở nguồn tiếng Tây Ban Nha về vụ Elda — vụ này không phải đề xuất tập. Gói nội dung chưa vào `main`; chỉ vào sau khi luồng này chốt.

```points
```
