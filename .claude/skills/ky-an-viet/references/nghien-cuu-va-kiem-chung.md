# Nghiên cứu và kiểm chứng

Timeline và claim ledger đi trước văn xuôi.

## Thứ bậc nguồn

Ưu tiên bản ghi gốc đầy đủ nhất tiếp cận được và tin tức độc lập đưa lúc sự việc xảy ra. Mỗi loại tài liệu chứng minh một thứ khác nhau:

- **Bản án phúc thẩm** hữu ích khi có, nhưng chọn lọc: nó thuật lại sự việc dưới một chuẩn xét lại cụ thể.
- **Cáo trạng** xác lập điều bị cáo buộc, không phải điều đã xảy ra.
- **Lời khai** xác lập điều nhân chứng đã nói.
- **Bản án** xác lập phán quyết của toà.

Trước khi kể kết cục, kiểm bản án có bị huỷ, sửa, có phát hiện mới hay trạng thái hiện tại đã đổi không. Thứ bậc nguồn tuỳ ngữ cảnh — không phải lệnh tự động bỏ những gì mâu thuẫn.

Bài đăng gốc đã xác thực hoặc phỏng vấn được ghi lại xác lập *người đó đã nói gì*, không xác nhận mọi điều họ nói là đúng. Phỏng vấn trong phim tài liệu có thể là lời kể trực tiếp quý giá; phân biệt nó với phần dựng lại của nhà làm phim. Bản sao, bài đăng lại, bài tổng hợp không phải xác nhận độc lập.

## Vụ nước ngoài

Đọc nguồn ở ngôn ngữ gốc. Bài tiếng Việt về vụ nước ngoài thường dịch lại từ vài bài gốc: truy ngược về bài gốc, và không đếm nhiều bài dịch là nhiều nguồn độc lập. Bài dịch hay sai con số, tên người, tội danh và mốc thời gian — mọi chi tiết đưa vào kịch bản phải đối chiếu với nguồn gốc.

## Vụ Việt Nam

Nguồn ưu tiên:

- Bản án đã có hiệu lực pháp luật được công bố trên [congbobanan.toaan.gov.vn](https://congbobanan.toaan.gov.vn), cổng công bố bản án, quyết định của Toà án nhân dân tối cao. Ghi số bản án, toà xét xử, ngày tuyên.
- Thông tin chính thức của cơ quan tiến hành tố tụng.
- Báo chí chính thống đưa tin lúc sự việc xảy ra và lúc xét xử.

Bài mạng xã hội chỉ là manh mối. Nhiều báo đăng lại cùng một thông cáo là **một** nguồn.

Không phải bản án nào cũng được công bố, và thông tin nhân thân trong bản án có thể đã được ẩn. **Không tìm cách xác định lại danh tính đã bị ẩn** bằng cách ghép nguồn khác. Ghi rõ tư cách tố tụng của từng người tại ngày kiểm tra — xem [thị trường Việt Nam](thi-truong-viet-nam.md).

## Claim ledger

`claim_id, claim, source_ids, locators, confidence, claim_status, conflicts, script_segment`

`claim_status` là một trong `established / alleged / inference / unknown`. Chi tiết cần thiết mà không có nguồn thì cắt, quy nguồn, hoặc ghi là khoảng trống. Nút thắt quan trọng cần nguồn trực tiếp hoặc đối chiếu độc lập đủ mạnh.

Ghi bản án kèm ngày, và các thay đổi về sau. Quy nguồn cho cáo buộc và các phần dựng lại còn tranh cãi. Không biến nét mặt, sự im lặng hay một chẩn đoán thành bằng chứng phạm tội.

## Danh mục nguồn

Mỗi nguồn: tiêu đề, tác giả hoặc cơ quan, URL gốc, ngày đăng/cập nhật/truy cập, loại nguồn, vị trí liên quan, đường dẫn local, trạng thái tải, quyền dùng lại; kích thước và SHA-256 khi đã thật sự tải file.

Trạng thái tải ghi trung thực: `downloaded_original`, `saved_excerpt`, `link_only`, `blocked`, `missing`. Ghi chú tự viết không phải bản gốc. Tải tài liệu công khai phù hợp khi hữu ích; không vượt kiểm soát truy cập, không thu thập dữ liệu cá nhân rò rỉ hay nội dung độc hại để tạo không khí.

## Chính sách YouTube

Kiểm bản hiện hành trước khi kết luận: [support.google.com/youtube/answer/6162278](https://support.google.com/youtube/answer/6162278) và [support.google.com/youtube/answer/2802008](https://support.google.com/youtube/answer/2802008). Phân biệt ba mức: bị gỡ hoặc cảnh cáo, giới hạn độ tuổi, giới hạn quảng cáo. Bối cảnh phải nằm trong chính video.

## Quyền dùng tư liệu

Theo dõi quyền của từng tài sản. Ảnh và clip báo chí — kể cả báo Việt Nam — không mặc định bị cấm, cũng không mặc định dùng được. Tìm tư liệu có giấy phép, thuộc phạm vi công cộng hoặc có căn cứ khác, và ghi rõ chỗ chưa chắc. Quyền chưa rõ thì dùng minh hoạ tự dựng có ghi rõ là minh hoạ. Không trình bày hình do máy tạo như bằng chứng thật.
