# r2-02 — Review Gemini: khung sườn NET-0006 v2

Đã đọc `coordination/threads/net-0006-khung-suon/THREAD.md`, các file vòng trước (`r1-00` đến `r2-01`), toàn bộ khung sườn v2 (`01-beat-sheet.md`), ledger `claims.csv` (C01–C26) và bản trích `sources/S07-schedule-excerpt.md`. 

Bản sửa v2 của tác giả Claude đã tiếp thu đầy đủ, chính xác tất cả các khuyến nghị và sửa chữa toàn diện 6 điểm của Gemini (D12–D17) cũng như các điểm của Codex và các điểm tự nêu. Khung sườn hiện tại đã đạt độ hoàn thiện cao, giải quyết triệt để các xung đột về thang tiết lộ, làm liền mạch chuỗi câu hỏi đóng-mở và phân định ranh giới chức năng rõ ràng giữa các beat. Không phát hiện điểm CHAN hay SUA mới.

Các đường dẫn file dưới đây tính từ thư mục repository `t-i/outputs/YouTube-Research-System/episodes/NET-0006-sherri-rasmussen/`.

---

## Xác nhận đóng các điểm của Gemini (D12–D17)

### D12 — OK: Đã thống nhất câu hỏi mở B01 theo hook thuần C03
- **Chỗ nào:** `scripts/01-beat-sheet.md:57-59`, đối chiếu C03 và C05.
- **Vấn đề đã xử lý:** Dòng 57 đã viết lại hoàn toàn câu hỏi mở: *"Nếu kẻ đột nhập đã gom sẵn chồng đồ giá trị ngay lối ra, sao lại bỏ lại tất cả — và vì sao vụ việc kết thúc bằng cái chết của Sherri?"*. Ranh giới dòng 59 quy định dứt khoát không nhắc đến xe BMW và chìa khóa ở B01. Toàn bộ chi tiết về chiếc BMW được bảo lưu cho B04 (khi phát hiện xe ngày 07/03/1986). Mâu thuẫn rò rỉ thông tin trước mốc B04 đã được triệt tiêu hoàn toàn.
- **Cần gì để đóng:** Đã đáp ứng trọn vẹn yêu cầu. Chốt: đã sửa.

### D13 — OK: Đã nối liền mạch chuỗi câu hỏi B07 → B08 → B09
- **Chỗ nào:** `scripts/01-beat-sheet.md:105`, đối chiếu dòng 113.
- **Vấn đề đã xử lý:** 
  - Câu hỏi mở B07 dòng 105 nay hỏi về mối liên hệ nhân thân và động cơ: *"Vì sao một thám tử LAPD đương chức lại dính tới hiện trường năm 1986 — mối liên hệ thật giữa cô ta và Sherri là gì? (→ B08)"*, dẫn nhập tự nhiên vào B08.
  - Câu hỏi mở B08 dòng 113 tiếp nối: *"Làm sao đối chất và lấy mẫu trực tiếp chuẩn pháp lý của một thám tử đương chức mà không làm lộ chuyên án? (→ B09)"*, mở đường trực tiếp cho cuộc thẩm vấn và lệnh bắt tại B09.
  - Cấu trúc nhân-quả liền mạch, không còn tình trạng B07 nhảy cóc qua B08.
- **Cần gì để đóng:** Đã đáp ứng trọn vẹn yêu cầu. Chốt: đã sửa.

### D14 — OK: Đã tách hành động thu mẫu ở B09 khỏi kết quả 13 loci ở B10
- **Chỗ nào:** `scripts/01-beat-sheet.md:38`, dòng 122 và dòng 130; C17.
- **Vấn đề đã xử lý:** Thang tiết lộ (dòng 38) và nội dung B09 (dòng 122) chỉ ghi nhận việc bắt giữ và thực thi lệnh cưỡng chế thu mẫu niêm mạc miệng. Cột cấm dòng 38 và ranh giới dòng 122 quy định rõ: kết quả phân tích khớp 13 loci được chuyển sang B10 (dòng 130). Điều này bảo đảm tính chân thực của quy trình giám định và giữ trọn chức năng bất ngờ của B10.
- **Cần gì để đóng:** Đã đáp ứng trọn vẹn yêu cầu. Chốt: đã sửa.

### D15 — OK: Đã phân định ranh giới C12 giữa B06 (nhân thân) và B08 (động cơ)
- **Chỗ nào:** `scripts/01-beat-sheet.md:98-99`, đối chiếu dòng 114-115; C12.
- **Vấn đề đã xử lý:** 
  - B06 chỉ dùng C12 ở mức nhận diện nhân thân: Lazarus từng có quan hệ tình cảm thời đại học với John Ruetten nên lọt vào danh sách phụ nữ rà soát năm 2009; ranh giới cấm kể chi tiết chạm trán tại bệnh viện.
  - B08 triển khai toàn bộ tình tiết cuộc đối mặt ở bệnh viện nơi Sherri làm việc và thái độ thù địch theo lời khai để phục vụ tuyến động cơ do công tố xây dựng. B08 không còn bị rỗng chức năng hay lặp lại B06.
- **Cần gì để đóng:** Đã đáp ứng trọn vẹn yêu cầu. Chốt: đã sửa.

### D16 — OK: Đã viết rõ ngày điều trần parole bằng chữ tránh nhầm lẫn định dạng
- **Chỗ nào:** `scripts/01-beat-sheet.md:42`, dòng 154–155 và dòng 195; C25, S07.
- **Vấn đề đã xử lý:** Mốc thời gian được viết bằng chữ rõ ràng tại thang tiết lộ và B13: "dự kiến ngày 9 tháng 10 năm 2026", kèm giải thích nguồn S07 ghi theo chuẩn Mỹ `10/09/2026` trong "October 2026 Hearing Calendar". Ranh giới ghi rõ cấm viết số "09/10" để ngăn ngừa tuyệt đối nguy cơ người viết kịch bản ở bước 5 đọc nhầm thành tháng Chín.
- **Cần gì để đóng:** Đã đáp ứng trọn vẹn yêu cầu. Chốt: đã sửa.

### D17 — OK: Đã bổ sung manh mối chiếc cốc và ống hút C11 vào bảng §5
- **Chỗ nào:** `scripts/01-beat-sheet.md:176` (Bảng manh mối §5); C11.
- **Vấn đề đã xử lý:** Hàng vật chứng "Chiếc cốc và ống hút bỏ đi tại Costco" đã được thêm vào bảng manh mối sau CODIS, xuất hiện ở B07, xác định rõ tính chất `established` nhưng chỉ khớp một phần 11 vị trí (chưa phải chuẩn ra tòa), và được giải đáp đầy đủ bằng đối chiếu mẫu trực tiếp 13 loci và SERI 15 loci tại B10.
- **Cần gì để đóng:** Đã đáp ứng trọn vẹn yêu cầu. Chốt: đã sửa.

---

## Xác nhận các điểm D01–D11

- **D01, D03, D04, D06 (`chốt: giữ nguyên`):** Cả ba bên tác giả và reviewer đều đã đạt đồng thuận cao: giữ hook thuần C03, giữ B08 làm beat riêng tạo khoảng lắng trước B09, giữ nguyên B10 không chia nhỏ (phân định nội bộ là đủ), và ghi nhận việc không truy cập trực tiếp PDF S08 là bất khả kháng kỹ thuật đã được khoanh vùng minh bạch.
- **D02 (`chốt: đã sửa`):** Tác giả đã sửa B04 (dòng 79, 83) chỉ dừng ở việc gia đình nêu "bạn gái cũ của John", giữ kín chức nghiệp cảnh sát/LAPD cho cú lật tại B06 (dòng 95). Gemini xác nhận việc này bảo toàn trọn vẹn độ giật gân cho cú lật kép ở B05 và B06.
- **D05 (`chốt: đã sửa`):** Tác giả đã bổ sung diễn giải tại dòng 135 làm rõ phần trả lời hook mở đầu được gánh bởi chuỗi sự kiện `established` (C03, C05), còn C20 chỉ bổ sung cách đọc "dàn dựng sau khi giết" và luôn quy nguồn cho chuyên gia công tố. Cách phân bổ payoff này là hoàn toàn xác đáng.
- **D07–D11 (`chốt: đã sửa`):** Đã kiểm tra lại các điểm Codex nêu: D07 (mẫu cốc 11 vị trí đọc được), D08 (bỏ nhận định so sánh mức bạo lực tại B03), D09 (tách độ vững DNA khỏi giới hạn C19 chưa giải), D10 (phân biệt mốc 23 năm tới khi bắt và 26 năm tới khi kết án tại B12), D11 (bỏ từ "dàn dựng" tại B10). Toàn bộ các sửa đổi này đã hiện diện chính xác trong bản v2.

---

## Đánh giá tổng thể theo câu hỏi của luồng

1. **Về việc bám sát claim ledger C01–C26:** Khung sườn v2 phản ánh trung thực toàn bộ 26 claim, khớp chính xác từng mã với cột `script_segment`. Giới hạn của các claim tranh luận (`alleged` như C15, C20), claim suy luận (`inference` như C26) và các vùng chưa có lời giải (`established` nhưng để mở như C19) được đóng khung kỷ luật, không bị đánh tráo thành sự thật hiển nhiên.
2. **Về trình tự tiết lộ:** Không có lời giải nào xuất hiện trước khi manh mối tương ứng được đưa ra bàn cờ. Các mắt xích bảo mật thông tin (không lộ thân phận LAPD ở B04; không lộ kết quả 13 loci ở B09; không lộ từ "dàn dựng" trước B11) được cài đặt thành các lệnh ranh giới cứng, bảo đảm sự bất ngờ tự nhiên theo tiến trình phá án thực tế.
3. **Về nhịp điệu và chức năng các beat:** Cấu trúc 14 beat vận hành trơn tru theo mô hình nhân - quả. Mỗi beat đều hoàn thành nhiệm vụ đóng một ẩn số trước đó và kích hoạt một câu hỏi cấp bách mới, triệt tiêu hoàn toàn nguy cơ lặp lại chức năng giữa B06 và B08. Khung sườn v2 đã sẵn sàng làm bộ xương chuẩn mực cho bước viết kịch bản tiếng Việt chi tiết (bước 5).

---

## Tôi đã không kiểm cái gì

- Công cụ chạy lệnh (`run_command`) bị từ chối bởi quy tắc phân quyền người dùng trong môi trường thực thi; toàn bộ việc kiểm tra được thực hiện độc lập qua các công cụ đọc tệp chuyên dụng (`view_file`, `list_dir`, `find_by_name`, `grep_search`).
- Không truy cập được toàn văn tệp PDF gốc S08 qua mạng do rào cản kỹ thuật TLS/challenge đã ghi nhận từ đầu dự án; việc thẩm định tính chuẩn xác của các mốc loci và trích dẫn dựa trên `claims.csv`, `sources/S01-excerpt.md` và các đối chiếu HTML của Codex.
- Không truy cập trực tiếp trang web CDCR để kiểm tra trạng thái cập nhật theo thời gian thực của lịch điều trần parole S07; chỉ xác nhận việc chuyển đổi ngày của D16 là hoàn toàn khớp với bản trích `sources/S07-schedule-excerpt.md`.
- Không kiểm tra thứ tự tháng/ngày của C23 (02/10/2024) và C24 (12/02/2025) do không có bản trích toàn văn S04/S05; đồng thuận giữ nguyên dạng số cho hai mốc này như tác giả đã đề xuất.
- Không rà soát từng dòng đối chiếu giữa hai bản kịch bản nháp tiếng Việt (`02-script-vi.md` và `02-script-vi-gemini.md`) với khung sườn này; các lưu ý về việc loại bỏ thoại hư cấu B09 và chuẩn hóa quy nguồn B11 thuộc phạm vi xử lý của bước 5.
- Không tạo mới, chỉnh sửa hay lưu bất kỳ tệp tin nào trên đĩa; không chạy script áp dụng tự động `thread.py apply`.

```points
D12 | chốt: đã sửa | scripts/01-beat-sheet.md:57 | OK: Đã viết lại câu hỏi mở B01 thuần C03; bỏ hoàn toàn xe BMW và chìa khóa
D13 | chốt: đã sửa | scripts/01-beat-sheet.md:105 | OK: B07 đã nối câu hỏi sang động cơ B08; B08 mở câu hỏi đối chất/mẫu trực tiếp sang B09
D14 | chốt: đã sửa | scripts/01-beat-sheet.md:122 | OK: B09 chỉ giữ hành động thu mẫu; kết quả 13 loci chuyển sang B10
D15 | chốt: đã sửa | scripts/01-beat-sheet.md:98 | OK: B06 chỉ nhận diện nhân thân; chi tiết cuộc gặp bệnh viện chuyển sang B08
D16 | chốt: đã sửa | scripts/01-beat-sheet.md:42 | OK: Ngày điều trần parole ghi bằng chữ "ngày 9 tháng 10 năm 2026" tránh nhầm định dạng
D17 | chốt: đã sửa | scripts/01-beat-sheet.md:176 | OK: Bảng manh mối §5 đã bổ sung manh mối chiếc cốc và ống hút C11
```
