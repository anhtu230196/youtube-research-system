# [NET-0001] — [Tên câu chuyện]

## Hồ sơ tập

- Trạng thái: đọc từ registry.json.
- Tên khác, tài khoản, tổ chức liên quan:
- Sự kiện và khoảng thời gian:
- Fingerprint chống trùng:
- Các chuyện thành phần nếu là tập tổng hợp:
- Ngôn ngữ, khán giả, thời lượng:
- Câu hỏi trung tâm:
- Góc kể và giá trị riêng:
- Kết luận đã biết / chưa biết:
- Kiểm tra diễn biến mới nhất ngày:

## Nguồn — sources.csv

source_id,title,author,published_at,updated_at,accessed_at,url,source_type,local_path,download_status,reuse_rights,locator,file_size,sha256,notes

## Chứng cứ — claims.csv

claim_id,claim,source_ids,locators,confidence,claim_status,conflicts,script_segment

## Timeline

| Ngày/giờ và múi giờ | Sự kiện | Claim ID | Ghi chú |
|---|---|---|---|

## Khoảng trống và mâu thuẫn

| Vấn đề | Đã tìm ở đâu | Kết quả | Cách xử lý trong kịch bản |
|---|---|---|---|

## Dàn nhịp kể

Đọc STORYTELLING.md trước khi lập dàn ý. Viết thử ba hook tiếng Việt và chọn một để đưa vào bản đầy đủ. Ghi câu hỏi người nghe sẽ có sau hook và đoạn nào trả lời nó; không bắt buộc thêm một vòng duyệt hook riêng.

| Đoạn | Câu hỏi của khán giả | Chi tiết/phát hiện | Claim ID | Hình dự kiến | Thời lượng ước tính |
|---|---|---|---|---|---|

Không bắt buộc giả thuyết sai. Chỉ sử dụng cú đảo chiều đã được xác minh. Ghi tổng thời lượng dựa trên bản đọc thực tế hoặc tốc độ đọc giả định được nêu rõ.

## Theo dõi manh mối và câu hỏi

| Chi tiết / câu hỏi | Claim ID | Đoạn xuất hiện | Cách hiểu lúc đầu | Đoạn giải thích | Ý nghĩa hoặc giới hạn thực tế |
|---|---|---|---|---|---|

CTA mặc định: một câu ngắn cuối tập sau phần giải đáp, hoặc bỏ nếu không phù hợp. Không chen trước phát hiện quyết định.

## Góc nhìn và thay đổi thái độ

| Đoạn | Sự kiện có nguồn | Nhân vật biết/tin điều gì | Khán giả biết điều gì | Thay đổi thái độ/hành động và nguyên nhân | Đoạn giải đáp |
|---|---|---|---|---|---|

Chỉ điền những thay đổi có vai trò trong câu chuyện. Ghi rõ điều chưa biết. Với nguồn là lời kể trên mạng, tách phần được tài liệu độc lập xác nhận khỏi diễn giải của người kể. Các lớp tiết lộ có thể giải thích cùng một phát hiện chính; không buộc thêm twist.

## Tài sản dựng — assets.csv

asset_id,description,source_id,url,local_path,download_status,rights,credit,planned_segment,replacement_if_unavailable

## Bộ bàn giao

- dossier.md: hồ sơ này, bao gồm khoảng trống và kết luận nghiên cứu.
- sources.csv: nguồn, trạng thái tải và quyền dùng.
- claims.csv: chi tiết gắn bằng chứng.
- assets.csv: hình/âm thanh đã có và phần còn thiếu.
- sources/: tài liệu nghiên cứu thực sự đã lưu.
- assets/: tài sản dựng thực sự đã lưu.
- scripts/01-beat-sheet.md: dàn nhịp có nguồn.
- scripts/02-script-vi.md: bản đầy đủ tiếng Việt để duyệt.
- scripts/03-script-final-sourced.md: bản cuối có mã chứng cứ.
- scripts/04-narration-clean.txt: lời đọc sạch theo ngôn ngữ đã chọn.
- visual-plan.md: hình theo đoạn, phân biệt tư liệu thật và minh họa/tái dựng.
- packaging.md: 3 tiêu đề, ý tưởng thumbnail, mô tả và nguồn liên kết.
- quality-review.md: kết quả kiểm tra sự thật, nhịp kể, quảng cáo, quyền tư liệu và định dạng thu âm; nêu hạn chế thực tế.

Chỉ liệt kê là đã bàn giao những file tồn tại. Bản kịch bản chưa hoàn tất không được gắn trạng thái scripted.
