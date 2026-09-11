# Kiểm tra chất lượng — GPT-5.6 Terra

**Trạng thái:** đạt kiểm tra nội bộ cho bản thử độc lập, 11/09/2026

**Tác giả prose:** GPT-5.6 Terra
**Phạm vi:** `coordination/drafts/model-trials/NET-0006/terra/` — không phải artifact sản xuất của NET-0006.

## Đã kiểm

- Có đủ marker B01–B14 theo đúng thứ tự beat sheet; cú lật được giữ đúng trật tự: hiện trường → mẫu DNA nữ → Stephanie Lazarus → 11/13/15 loci → diễn giải chuyên gia tại tòa.
- `02b-ban-doc-terra.txt` trùng nguyên văn phần narration của bản Markdown sau khi bỏ front matter, tiêu đề và comment truy vết.
- Không gọi mẫu cốc/ống hút là profile hoàn chỉnh; tách đúng 11 loci sơ bộ, 13 loci mẫu trực tiếp, và 15 loci SERI.
- Không biến cuộc phỏng vấn 05/06/2009 thành lời thú tội hay lời từ chối mẫu dứt khoát; giữ trình tự được rời phòng → bị bắt → Miranda → không nói thêm.
- Giữ các giới hạn do bên bào chữa nêu: phong bì rách/ống có vẻ nguyên, dấu vân tay/DNA chưa xác định, Model 49 không thu hồi để đối chiếu, và tranh luận chuyên gia đạn đạo.
- Quy nguồn rõ cho động cơ và nhận định hiện trường bị sắp đặt; không khẳng định bao che có tổ chức hoặc diễn tiến sau khi Sherri qua đời như sự thật được camera xác nhận.
- Mốc parole: rút quyết định 02/10/2024, từ chối 12/02/2025; lịch hearing dự kiến 09/10/2026 lúc 08:30 chỉ là lịch thủ tục, không phải quyết định thả.

## Sửa trong lượt QA

- B03 đã bỏ cách gán vụ burglary 11/04 vào cách đọc ban đầu của điều tra viên. Tình tiết này chỉ còn ở B10, được quy đúng là chứng cứ third-party culpability do bào chữa nêu.
- B11 đã bỏ việc khẳng định thời điểm các vật bị sắp đặt; hiện chỉ kể đó là cách diễn giải của chuyên gia công tố Robert Safarik tại tòa.

## Cơ sở đối chiếu

Đối chiếu với beat sheet v2, `claims.csv` (C01–C26), `timeline.md`, `dossier.md`, `gaps.md`, cùng checklist factual độc lập. Nguồn trục là S01 (*People v. Lazarus*); các mốc hậu tố dùng S03–S07 theo source catalog của tập.

## Giới hạn

Đây là QA của phép thử model, không thay thế luồng review sản xuất với Claude, Gemini và Tú. Chưa kiểm thử TTS hoặc dựng hình/âm thanh; các quyết định biên tập và sử dụng bản này vẫn chờ Tú đánh giá.
