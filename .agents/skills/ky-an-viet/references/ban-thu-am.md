# Bản thu âm

Làm sau khi Tú đã duyệt nội dung bản tiếng Việt (bước 5). Bước này **chuẩn bị để đọc**, không viết lại nội dung. Thay đổi đáng kể về nội dung hay cấu trúc phải đưa lại Tú duyệt.

## Ba file

- `scripts/03-script-final-sourced.md` — bản cuối, giữ mã claim theo đoạn.
- `scripts/04-narration-clean.txt` — chỉ phần được đọc lên. Không mã claim, không link, không tiêu đề đoạn, không cue dựng.
- `pronunciation.md` — cách đọc tên riêng, viết tắt, con số; kèm quyết định đã chọn và đã nghe thử hay chưa.

## Tên nước ngoài

TTS tiếng Việt hay đọc sai tên nước ngoài. Cách xử lý tuỳ engine đang dùng: từ điển phát âm nếu engine hỗ trợ, hoặc viết lại theo âm **chỉ trong file thu âm** — kịch bản làm việc vẫn giữ chữ viết gốc. Ghi cặp "chữ gốc → cách viết để đọc" vào `pronunciation.md`.

Không chèn phiên âm trong ngoặc vào lời đọc theo mặc định: engine có thể đọc cả hai. Kiểm cách đọc tên qua nguồn phát âm đáng tin khi có; chưa kiểm được thì ghi là chưa kiểm.

## Số, năm, viết tắt

Viết theo cách giúp engine đang dùng đọc đúng, nhưng **nghe thử một đoạn ngắn trước khi thay hàng loạt**. Không mặc định phải viết số bằng chữ nếu engine đã đọc đúng.

Chốt một cách và giữ nhất quán cả tập:

- Năm: "1986" được giọng đang dùng đọc thành gì?
- Ngày: "24/2" có bị đọc thành phân số không?
- Viết tắt: "DNA" hay "ADN"; "FBI", "LAPD" đánh vần từng chữ, đọc thành từ, hay thay bằng cụm tiếng Việt như "cảnh sát Los Angeles"?

Ghi lựa chọn vào `pronunciation.md`.

## Ngắt nghỉ và công cụ

Dấu câu là gợi ý ngắt, không bảo đảm độ dài khoảng dừng. Kiểm tài liệu hiện hành của nhà cung cấp trước khi dựa vào từ điển, thẻ, SSML hay thông số cụ thể. Không áp một cài đặt giọng cho mọi trường hợp, không đòi cả tập vừa trong một lần tạo.

Ghi lại giọng, model và cài đặt đã dùng. Chia file tại ranh giới cảnh, theo giới hạn độ dài thật của engine. Nghe kiểm độ liền mạch, cách đọc tên và sự tiết chế cảm xúc.

**Không tuyên bố đã sẵn sàng thu âm hay đã nghe kiểm khi mới chỉ đọc chữ.**

## Đóng gói

- `visual-plan.md` — hình theo đoạn, tách tư liệu thật khỏi minh hoạ và tái dựng.
- `packaging.md` — ba tiêu đề tiếng Việt, ý tưởng thumbnail, mô tả kèm liên kết nguồn.
- `quality-review.md` — kiểm sự thật, nhịp kể, quảng cáo, quyền tư liệu, bản địa hoá, định dạng thu âm; nêu hạn chế thật.

Quy tắc tiêu đề và thumbnail: [mở đầu](mo-dau.md) và [thị trường Việt Nam](thi-truong-viet-nam.md).
