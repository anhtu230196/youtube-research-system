# Cập nhật giọng kể kỳ án tiếng Việt — bản 3

**Ngày:** 2026-09-15. **Tác giả:** Codex, theo yêu cầu trực tiếp của Tú. **Claim:** `sys-skill-ky-an-viet`. **Bước:** 7, cập nhật skill; Claude review độc lập. Vai tác giả đổi theo chỉ định của Tú; không phải luồng sản xuất tập hay duyệt nội dung NET-0006.

## Vấn đề và hướng sửa

Tú muốn kể kỳ án cho khán giả Việt với cách dẫn gần gũi như transcript Cẩm Tân Đại Lâu / mất tích đêm Trung thu đã gửi. Cấu hình kênh và skill đã chuyển sang tiếng Việt từ 2026-09-14; đổi nhãn khán giả thêm lần nữa không tự sửa được lời văn.

Đọc bản hiện có `t-i/outputs/YouTube-Research-System/episodes/NET-0006-sherri-rasmussen/scripts/02b-narration-vi-review.txt` cho thấy các nhóm lỗi có thể sửa bằng hướng dẫn cụ thể:

- Những phát hiện thường bị ngắt bởi lời nhắc “chưa chứng minh”, “chưa phải kết luận”, rồi lại nhắc câu hỏi còn lại. Ví dụ quanh các dòng 45–61, 99 và 139–159. Giới hạn có ý nghĩa vẫn phải giữ; vấn đề là việc thuyết minh về chúng bị lặp hoặc tách khỏi hành động.
- Câu đơn đứng riêng liên tiếp quanh các dòng 75–87 và 101–117, dù cùng giải thích một phát hiện; nhịp nhấn mất tác dụng khi kéo dài.
- Những cụm trừu tượng quanh các dòng 107, 119 và 213 nói về “mối liên hệ” hoặc bước tiến hồ sơ thay vì nói rõ người và chứng cứ.
- Chuyển đoạn quanh các dòng 123, 197 và 251 nói về cách tổ chức bài, làm lộ giọng tổng kết hồ sơ.

Đây là nhận xét trên văn bản, không chứng minh skill mới tạo ngày 2026-09-14 đã gây ra mọi lỗi của bản cũ. Không sửa artifact NET-0006 đang đóng băng.

## Gói nội dung đóng băng để review

Artifact này mô tả gói; review phải đọc các file thật dưới đây, không chỉ bản mô tả. Đối chiếu diff với `a21ba8d` (commit claim, nội dung skill còn bản cũ). Trong lượt reviewer, toàn bộ gói nội dung này được giữ nguyên.

| File | Thay đổi |
| --- | --- |
| `.claude/skills/ky-an-viet/SKILL.md` | Mở rộng trigger cho sửa lời kể cứng; bắt buộc đọc tài liệu giọng và thực hành khi viết câu; phân biệt sửa trích đoạn với sản xuất tập; sửa bất biến để không tự đính chính sau mọi phát hiện. |
| `.claude/skills/ky-an-viet/references/giong-ke.md` | Người dẫn chuyện, đoạn có nhịp nói, hành động cụ thể, quy nguồn theo mạch và giới hạn có ý nghĩa; chặn việc tự thêm người thực hiện khi nối câu; bảo toàn chi tiết theo phạm vi yêu cầu. |
| `.claude/skills/ky-an-viet/references/mau-va-thuc-hanh.md` | Phân tích cơ chế trong mẫu và giới hạn của mẫu; bốn ví dụ từ dữ kiện hư cấu, có cặp trước–sau và đoạn kể liền mạch. |
| `.claude/skills/ky-an-viet/references/kien-truc-cau-chuyen.md` | Ai hiểu manh mối theo cách nào; tách sự việc với thời điểm phát hiện; trở ngại thật thay cho câu úp mở. |
| `.claude/skills/ky-an-viet/references/mo-dau.md` | Cho phép lời chào ngắn nếu hợp yêu cầu; không mặc định sao chép chuyện dẫn dài của mẫu. |
| `.agents/skills/ky-an-viet/` | Bản sao tương ứng, đồng nhất từng byte với cả chín file Markdown ở thư viện chung. |
| `.claude/skills/README.md` | Cập nhật mô tả khả năng sửa lời kể. |
| `t-i/outputs/YouTube-Research-System/STORYTELLING.md` | Bản 4 thêm phần 9 dẫn tới hướng dẫn mới; giữ bảy mẫu và mã REF trong manifest cũ. |

Không đổi registry, mã và trạng thái tập, gợi ý/chống trùng, công cụ nghiên cứu, cấu hình model hoặc skill toàn cục. Không dùng mẫu như nguồn sự thật của một vụ án. Xưng hô `mình — các bạn` là mặc định biên tập thử khi sổ còn trống, phải ghi rõ ngay khi nộp bản bước 5 hoặc khi trả trích đoạn, bên ngoài phần lời kể; chưa phải lựa chọn kênh đã được Tú duyệt.

## Kiểm thử hành vi đã chạy

Đầu vào và đầu ra lưu tại `coordination/threads/sys-skill-ky-an-viet-voice/tests/`. Chỉ dùng hai cảnh hư cấu giới hạn dữ kiện, không tạo episode. Các lượt dùng Codex subagent độc lập, context mới, cùng đầu vào. Chúng là bài thử áp dụng skill, không đại diện ghế Claude hoặc Gemini trong review. Không cung cấp đáp án đích hay kết quả lượt trước cho người viết bài thử.

- `request.md`: nguyên đầu vào A (mất liên lạc → thông tin công việc → xe/thư → nhà nghỉ) và B (giấc mơ → căn hộ → xét nghiệm sơ bộ → dữ liệu camera thiếu).
- `baseline.md`: dùng snapshot skill trước sửa, tương ứng nội dung tại `a21ba8d`. Bản cũ đã giữ khá đủ dữ kiện và có câu nối; không thể khẳng định mặc định cũ chỉ sinh văn cứng.
- `trial-1.md`: dùng hướng dẫn mới trước khi thêm quy tắc đường đi của thông tin. A tự thêm người vợ kiểm tra với phòng nhân sự, trong khi đầu vào không xác định ai liên hệ và baseline không thêm. Đây là bước lùi quan sát được ở lượt dùng hướng dẫn mới; chưa đủ dữ liệu quy kết một câu hướng dẫn cụ thể đã gây ra lỗi. B còn câu bình trừu tượng về việc sơn phòng. Không nhận lượt này là đạt trọn.
- `final-trial.md`: lượt mới sau khi bổ sung quy tắc không tự thêm người thực hiện. Đã giữ phòng nhân sự là bên xác nhận, không gán người vợ đi hỏi; giữ dấu vết nghi là máu, chưa có ADN, camera mất dữ liệu chưa rõ nguyên nhân, giấc mơ là lời kể. Lượt từng bị ngắt bởi hạn mức được tiếp tục sau khi Tú yêu cầu. Lưu nguyên lời kể, chỉ bỏ khung hiển thị và đổi nhãn A/B thành tiêu đề file.

**Đánh giá có giới hạn:** bài thử cuối sửa được lỗi gán người thực hiện của lượt trước, chia đoạn theo nhóm diễn biến và không tự thêm lời giải. Tuy nhiên, đoạn B vẫn có câu liệt kê những điều chưa xác định; chưa chứng minh bản mới hấp dẫn hơn bản cũ trên cả tập. Chưa thử âm thanh hoặc đo giữ chân. Dữ kiện bài thử cũng chưa đủ để đo cảnh cao trào, chất hài hoặc hồi đáp manh mối dài hạn. Bốn ví dụ trong skill minh hoạ lựa chọn biên tập cụ thể, không thay thế kết quả thử.

Quy tắc chặn việc thêm chủ thể mới được kiểm lại trên chính bộ dữ kiện sinh ra lỗi; giới hạn này đã đưa vào `SKILL.md` để người sử dụng sau đọc được. Đầu vào A cũng chưa nói rõ “buổi sáng” là ngày nào: không dùng khác biệt giữa “sáng hôm sau” ở baseline và “buổi sáng” ở lượt cuối để kết luận lượt nào tiến bộ về timeline. Các đầu ra được giữ nguyên để kiểm lại, không sửa hồi tố đề hoặc đáp án.

## Các sửa đổi ở bản 2 sau review

Đưa lỗi quan sát được và giới hạn bài thử vào skill; sửa Ví dụ 3 để không ngầm xác nhận người trong lời bảo vệ có mặt trong hình và bỏ câu lặp; trả lại mục nhận diện văn dịch; bắt buộc báo xưng hô thử ngay ở bước 5; ghi rõ mức review nguồn transcript; đưa phép thử mức chứng cứ vào bất biến. Claim phân biệt lịch sử lần tạo và phạm vi hiện tại. Đồng bộ lại bản Codex sau các sửa đổi.

**Về sổ cấu hình:** bản cập nhật biên tập này không chốt cách xưng hô. `registry.json` dòng 44 và 58 vẫn mô tả đúng: cách xưng hô chưa quyết định, `narrator_voice: null`; luật nghiệp vụ `AGENTS.md` dòng 62 yêu cầu cập nhật khi Tú chốt. STORYTELLING bản 4 có lịch sử phiên bản trong chính tài liệu và commit của gói. Không có quy định bắt mọi sửa hướng dẫn biên tập tạo một sự kiện cấu hình kênh; không để lại việc bắt buộc sửa sổ cho một quyết định chưa xảy ra. Khi Tú thật sự chốt xưng hô, cập nhật theo quy trình sửa sổ như luật hiện hành.

**Bản 3:** chỉ đồng bộ mốc ghi xưng hô ở đoạn phạm vi trên và câu cuối STORYTELLING với hướng dẫn giọng kể: ngay lúc nộp bản bước 5 hoặc trả trích đoạn, bên ngoài lời kể. Các file skill giữ nguyên so với bản 2. Ở vòng 2, Claude đã đọc bản NET-0006 chỉ để kiểm chẩn đoán và xác nhận các vị trí nêu ở đầu artifact; giới hạn chưa đối chiếu transcript mẫu vẫn còn.

## Kiểm cấu trúc đã chạy

- `quick_validate.py` của skill-creator: cả bản `.claude` và `.agents` hợp lệ. PyYAML được cài chỉ vào thư mục tạm bị bỏ qua bởi git, không sửa môi trường chung.
- So sánh cả chín file Markdown của hai bản skill: trùng từng byte.
- Kiểm 31 đường dẫn Markdown cục bộ trong skill và STORYTELLING: đích tồn tại.
- So sánh registry, episodes, scripts, hướng dẫn chọn vụ và nghiên cứu với HEAD: không đổi.
- Ba kiểm tra registry/claims/thread sẽ chạy trước khi đẩy theo `AGENTS.md`; kết quả cuối ghi trong handoff. Không coi kiểm máy móc là review chất lượng lời kể.

## Câu hỏi cần reviewer trả lời

1. Có hướng dẫn hoặc ví dụ nào làm tăng mức chắc chắn, bịa người thực hiện, bỏ giới hạn cần thiết hay mâu thuẫn luật kênh không?
2. Có câu nào tiếp tục ép khuôn khiến hướng dẫn mới dễ tạo văn công thức không?
3. Ví dụ có giữ dữ kiện tự công bố và bài thử có được đánh giá đúng mức không? Chỉ ra lỗi có dẫn chiếu, không yêu cầu viết lại theo gu.

Chưa làm một tập thật mới, chưa viết lại tập đang review, chưa chốt xưng hô trong sổ và chưa chuẩn bị audio. Những phần này không thuộc thay đổi skill được giao.
