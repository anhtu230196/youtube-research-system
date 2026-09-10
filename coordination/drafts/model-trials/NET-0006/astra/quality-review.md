# Bản thử Astra — đầu vào và kiểm tra

Ngày: 11/09/2026. Trạng thái: bản thử hoàn tất, chờ Tú đánh giá; không phải bản sản xuất đã duyệt.

## Phạm vi phép thử

Yêu cầu của Tú: thử từng model biên tập kịch bản từ beat sheet đã gửi, bắt đầu với GPT-6 Astra. Astra trong task hiện tại viết toàn bộ lời kể tiếng Việt. Một subagent cùng model kiểm tra nguồn và bản viết theo chế độ chỉ đọc; không viết đoạn thay thế. Đây là bản có vòng kiểm chứng, không phải đầu ra một lượt chưa qua chỉnh sửa. Không dùng Claude, Gemini, Sol, Terra, Luna hoặc GPT-5.5 để viết lại prose.

Đầu vào:

- `t-i/outputs/YouTube-Research-System/episodes/NET-0006-sherri-rasmussen/scripts/01-beat-sheet.md`, v2, luồng khung sườn đã settled.
- SHA-256 beat sheet: `0FACF42DF4FBE47D7683E7ED839A2B1ECFDD3891128FE722137100056FEF1AF4`.
- Hồ sơ cùng tập: `claims.csv`, `sources.csv`, `timeline.md`, `dossier.md`, `gaps.md`; quy tắc trong AGENTS.md và STORYTELLING.md.
- Không đọc hai bản prose cũ của Codex/Gemini để lấy câu văn làm mẫu. Những nhận xét về bản cũ chỉ xuất hiện trong tài liệu khung và sổ review được đọc để hiểu trạng thái.
- Không ghi lại thông số reasoning/speed vì chưa có căn cứ xác minh giá trị đang được dùng. Nếu so sánh model về sau, nên giữ cùng đầu vào, quyền tra cứu và mức kiểm chứng; kết quả một lần viết chưa phải bảng xếp hạng năng lực.

## Sản phẩm

- `02-script-vi-astra.md`: đủ B01–B14, chú thích claim/source trong các comment, danh mục URL cuối file.
- `02b-ban-doc-astra.txt`: chỉ lời kể, tạo trực tiếp từ bản trên bằng cách bỏ tiêu đề nhịp và chú thích; không viết lại lần hai. Có 4.225 đơn vị tách bằng khoảng trắng, không phải phép đếm từ vựng tiếng Việt. Không suy ra thời lượng bản Anh từ con số này.

## Kết quả kiểm chứng và hiệu chỉnh

Nguồn chính là nguyên văn phán quyết công khai [People v. Lazarus](https://law.justia.com/cases/california/court-of-appeal/2015/b241172.html), không phải phần Justia Opinion Summary. Một số locator trong ledger/beat sheet chưa chính xác; bản thử dùng vị trí đã đối chiếu lại, không sửa đầu vào của agent khác.

| Nội dung | Quyết định trong bản thử |
|---|---|
| B01 / C03 | Chồng thiết bị ở cửa dẫn vào gara; không thêm tầng cao/thấp, thời tiết, âm thanh hoặc camera tưởng tượng. |
| B02 / C01–C02 | Nghề, địa danh, báo nghỉ bệnh và các cuộc gọi đối chiếu S01 tr.3–4,11; tuổi đối chiếu AP. 7:20 đến 18:00 là khoảng 10 giờ 40 phút, không phải giờ tử vong. |
| B04 / C06 | S01 tr.71–74 xác nhận vụ trộm sáu tuần sau và việc bào chữa xin đưa vào tòa, không xác nhận nó gây ra quyết định điều tra ban đầu. B04 chỉ nêu sự kiện; B10 đóng tuyến này bằng quyết định loại chứng cứ vì thiếu liên hệ. |
| B05 / C08–C09 | Giữ 2003 yêu cầu, cuối 2004 tìm mẫu, 2005 xét nghiệm. Hồ sơ phụ chỉ “phù hợp” Sherri. Hồ sơ chính là nữ không tự loại mọi khả năng có đồng phạm nam. |
| B06 / C10 | Stearns/Jaramillo chỉ được nêu ở cuộc hỏi cung; không gán họ là người nhận hồ sơ tháng Hai. Bỏ cấp bậc Detective III chưa được nguồn đã mở xác nhận. |
| B07 / C11 | Không thêm Costco; nguồn S01 chỉ xác nhận cốc/ống hút bỏ đi. Đúng 11 vị trí đọc được; không dựng ngưỡng pháp lý “11 chưa dùng được ở tòa”, không khẳng định lệnh bắt cụ thể. |
| B08 / C12 | Theo lời khai John: gọi khóc và mời đến trước, nói yêu khi anh đã đến. Không dựng nguyên văn cuộc đối đầu ở bệnh viện. |
| B09 / C16–C17 | S01 tr.42–43 ghi trả lời chưa dứt khoát và cần hỏi luật sư, không phải từ chối dứt khoát ngay. Chỉ nói mẫu miệng được lấy sau bắt; chưa tìm thấy căn cứ cho “lệnh cưỡng chế lấy mẫu miệng” trong nguồn đã kiểm. |
| B10 / C13–C19 | Tách mẫu cốc 11 vị trí, đối chiếu mẫu trực tiếp 13 vị trí, SERI 15 vị trí; có đại diện bào chữa hiện diện. Giữ phong bì rách, ống có vẻ nguyên và dấu vân tay/DNA lạ, đồng thời nêu nhận xét của tòa rằng không có chứng cứ thuyết phục mẫu bị can thiệp (S01 tr.70). Súng không thu hồi; đạn đạo bị phản biện; tài liệu nhật ký thu sau bắt. |
| B11 / C20 | Giải thích chồng đồ quy rõ cho chuyên gia công tố Safarik. Dùng “sau cuộc vật lộn” có giới hạn, không dựng phút gây án. Locator chính: tr.6–7, chú thích 10; không dùng locator tr.67–69 trong ledger. |
| B12 / C21–C22 | Đối chiếu S01 và [Ninth Circuit 2023](https://cdn.ca9.uscourts.gov/datastore/memoranda/2023/09/05/21-55483.pdf), tr.1–5. Giả định cover-up để phân tích không phải kết luận có cover-up. |
| B13 / C23–C25 | Đọc bài AP qua kết quả tìm kiếm đầy đủ; mở trực tiếp AP gặp lỗi. Mở CBS và [lịch chính thức](https://www.cdcr.ca.gov/bph/2026/04/08/october-2026-hearing-calendar/) thành công. Lịch WE4479 vẫn là 9/10/2026, 08:30, trong lịch tháng Mười; bản kể ghi tháng bằng chữ và nói rõ đây không phải quyết định thả. |

## Nhịp kể và định dạng

Tác giả đã đọc lại để nối các bước điều tra bằng câu hỏi, hành động và kết quả. B01 đặt câu hỏi về chồng đồ; B11 trả lời bằng diễn giải có nguồn. Tên Lazarus và nghề cảnh sát xuất hiện ở B06, hồ sơ nữ ở B05, các kết quả 13/15 vị trí ở B10. B08 dành riêng cho quan hệ và lập luận động cơ. B14 trở lại nạn nhân; CTA một câu sau kết thúc.

Nhận xét về nhịp là biên tập của tác giả, không phải chứng minh giữ chân khán giả hay tự phê duyệt bản sản xuất. Subagent kiểm nguồn riêng một lượt trước prose và một lượt trên bản mới; tác giả đối chiếu nguồn các điểm bị nêu rồi sửa. Không có phản biện nào từ Claude/Gemini trong phép thử này.

Kiểm tra văn bản tự động: đúng 14 nhịp theo thứ tự; bản sạch khớp lời kể trong bản chú thích; không còn tiêu đề B**, mã claim hay ghi chú kỹ thuật trong bản sạch. Đọc lại các đoạn đã hiệu chỉnh để bảo đảm không lộ lời giải trước nhịp tương ứng.

Đã mở [chính sách bạo lực](https://support.google.com/youtube/answer/2802008?hl=en) và [hướng dẫn phù hợp quảng cáo](https://support.google.com/youtube/answer/6162278?hl=en) của YouTube ngày 11/09/2026. Lời kể tập trung điều tra, không mô tả tổn thương đồ họa hay hướng dẫn gây án; bối cảnh nằm trong lời kể. Chưa có hình, thumbnail hay video để đánh giá toàn bộ sản phẩm; chưa thể bảo đảm quảng cáo.

## Chưa kiểm và bàn giao

Chưa xem trọn video hỏi cung, chưa đọc toàn bộ biên bản xét xử/parole, chưa tải PDF gốc S01, chưa kiểm quyền media, chưa nghe audio và chưa kiểm cách phát âm tên riêng. Bản `.txt` phục vụ đọc duyệt, không phải tuyên bố đã sẵn sàng thu âm. Không phát biểu Lazarus chưa bao giờ nhận tội; đoạn B09 chỉ nói riêng cuộc phỏng vấn năm 2009.

Tú đánh giá bản thử này rồi có thể dùng cùng beat sheet để thử model tiếp theo. Nếu chọn dùng làm kịch bản sản xuất, cần đưa bản được chọn qua quy trình review nội dung của tập; bản thử này chưa hoàn tất bước đó. Registry hiện đã là awaiting_review và không thay đổi.

Claim NET-0006 và hai luồng review cũ giữ nguyên. Đầu ra đặt ngoài scope Claude đang giữ. Luồng review sản xuất riêng chưa được mở vì yêu cầu hiện tại là so sánh bản viết của từng model; không ghi nhận phép kiểm tra phụ này là review Claude/Gemini hoặc tự thay thế bước duyệt của Tú.
