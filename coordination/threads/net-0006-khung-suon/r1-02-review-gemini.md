# r1-02 — Review Gemini: khung sườn NET-0006 v1

Đã đọc `coordination/threads/net-0006-khung-suon/THREAD.md`, đề xuất `r1-00-proposal-claude.md`, bản review `r1-01-review-codex.md`, toàn bộ khung sườn `01-beat-sheet.md` (v1), cùng `claims.csv` (C01–C26) và `sources.csv`.

Khung sườn v1 của Claude đã thiết lập được cấu trúc 14 beat chặt chẽ, giữ vững ba chặng phát triển thực tế của vụ án (2005 phát hiện hồ sơ nữ → 2009 xác định nghi phạm LAPD → 2009–2012 kiểm chứng vật chứng trước tòa), đồng thời tuân thủ tốt các ranh giới tố tụng và quy nguồn. Tuy nhiên, qua đối chiếu kỹ thuật với claim ledger và logic tự sự, vẫn còn một số mâu thuẫn nội tại về thang tiết lộ, đứt gãy câu hỏi nối tiếp và lặp chức năng giữa các beat cần giải quyết.

Các đường dẫn file dưới đây tính từ thư mục gốc của repository (`t-i/outputs/YouTube-Research-System/episodes/NET-0006-sherri-rasmussen/`). Các điểm mới của lượt này đánh số từ D12.

---

## Các điểm review mới (D12–D17)

**D12 — SUA: Mâu thuẫn nội tại ở B01 giữa câu hỏi mở và ranh giới loại trừ xe BMW (C05)**

- **Chỗ nào:** `scripts/01-beat-sheet.md:57-59`, đối chiếu C03 và C05.
- **Vấn đề gì:** Dòng 59 ghi ranh giới nghiêm ngặt: *"Không nêu BMW ở đây nếu muốn giữ hook gọn (xem câu hỏi Q2 cho người review)"*, và dòng 58 chỉ gán duy nhất `C03`. Tuy nhiên, ngay dòng 57, câu hỏi mở của beat lại viết: *"Nếu kẻ trộm lấy được chìa và lái xe đi, sao lại bỏ lại chồng đồ đã gom sẵn ngay lối ra?"*. Chi tiết "lấy chìa lái xe đi" thuộc về tài sản ô tô bị mất (`C05`). Nếu khán giả ở B01 chưa được biết chiếc xe bị lấy mất, câu hỏi mở này trở nên vô căn cứ; ngược lại, nếu câu hỏi được đặt ra thì thông tin về chiếc xe đã bị rò rỉ trước mốc B04.
- **Cần gì để đóng:** Chọn một trong hai hướng xử lý nhất quán:
  1. *Nếu giữ hook thuần C03 (khuyên dùng):* Sửa câu hỏi mở ở dòng 57 thành: *"Nếu kẻ đột nhập đã gom sẵn chồng đồ giá trị ngay lối ra, sao lại bỏ lại tất cả sau một cuộc giằng co dữ dội?"*. Bỏ hoàn toàn chi tiết chìa khóa và lái xe ở B01.
  2. *Nếu muốn nhắc việc xe bị mất ngay B01:* Đưa sự kiện xe biến mất vào phần sự kiện B01, bổ sung `C05` vào mục Claims của B01 (chỉ ở khía cạnh xe bị mất cùng chìa), và giữ mốc tìm thấy xe ngày 07/03/1986 cho B04.

**D13 — SUA: Đứt mạch nối câu hỏi giữa B07, B08 và B09 (bước nhảy cóc qua B08)**

- **Chỗ nào:** `scripts/01-beat-sheet.md:105`, đối chiếu dòng 109–115 và dòng 120.
- **Vấn đề gì:** Tại B07 dòng 105, câu hỏi mở viết: *"Lấy mẫu xác nhận thế nào — và cô ta nói gì khi bị đối chất?"*. Câu hỏi mở này nhảy cóc qua toàn bộ B08 để trỏ thẳng vào cuộc thẩm vấn ở B09. Trong khi đó, B08 đóng câu hỏi về động cơ / mối quan hệ đại học (`C12`), rồi lại mở câu hỏi về phỏng vấn / chứng cứ. Việc B07 kích hoạt kỳ vọng về cuộc đối chất khiến B08 (động cơ) bị rơi vào vị trí chèn ngang bất ngờ, phá vỡ nguyên tắc "mỗi đoạn giải một câu hỏi và mở ra câu hỏi kế tiếp".
- **Cần gì để đóng:** Sửa câu hỏi mở của B07 để dẫn tự nhiên vào B08: Sau khi có kết quả khớp 11 vị trí từ chiếc cốc bỏ đi, câu hỏi mở ra cho điều tra viên là: *"Vì sao một thám tử kỳ cựu của LAPD lại có mặt tại hiện trường và cắn vào nạn nhân? Mối liên hệ thực sự giữa cô ta và Sherri trong quá khứ là gì?"*. Khi đó B08 đóng câu hỏi bằng động cơ từ lời khai quá khứ (`C12`), rồi mới mở câu hỏi sang B09: *"Động cơ trong quá khứ chỉ là lời khai; làm sao đối chất và lấy mẫu trực tiếp chuẩn pháp lý của một thám tử đương chức mà không làm lộ chuyên án?"*.

**D14 — SUA: Xung đột gán claim C17 giữa B09 và B10 trên Thang tiết lộ so với Beat sheet**

- **Chỗ nào:** `scripts/01-beat-sheet.md:38-39` đối chiếu dòng 122 và dòng 128–130, C17.
- **Vấn đề gì:**
  - Trên Thang tiết lộ (mục 3, dòng 38–39): Dòng 38 xác định B09 chỉ dừng ở *"Phỏng vấn lấy cớ vụ trộm tranh; bị bắt khi rời phòng"*, và để dành việc *"Mẫu trực tiếp khớp 13 loci"* cho B10 (dòng 39).
  - Nhưng tại Beat sheet chi tiết (mục 4, dòng 122): B09 lại ghi `C17` kèm kết quả: *"mẫu miệng trực tiếp khớp 13 loci"*. Về mặt thực tế điều tra, mẫu niêm mạc miệng thu sau khi bắt giữ cần thời gian chuyển phòng xét nghiệm phân tích; kết quả không thể có ngay khi Lazarus vừa bước ra khỏi phòng phỏng vấn ngày 05/06/2009. Ghi nhận kết quả này ở B09 làm triệt tiêu tính bất ngờ và chức năng chứng cứ của B10.
- **Cần gì để đóng:** Tách rõ hai vế của `C17`: Tại B09, chỉ ghi nhận hành động bắt giữ và lệnh cưỡng chế thu mẫu niêm mạc miệng. Rút toàn bộ kết quả phân tích "khớp 13 loci" sang B10 để đối chiếu song song với xét nghiệm 15 loci của SERI (`C18`) và các phản biện của bên bào chữa (`C19`).

**D15 — SUA: B06 lấn sân chi tiết đối đầu tại bệnh viện khiến B08 bị rỗng chức năng**

- **Chỗ nào:** `scripts/01-beat-sheet.md:98` đối chiếu dòng 114, C12.
- **Vấn đề gì:** Tại B06 dòng 98, phần claim ghi: *"C12 (Lazarus và John quen thời đại học; lời khai về quan hệ và lần gặp ở bệnh viện — động cơ do công tố quy)"*. Sang B08 dòng 114, claim duy nhất của cả beat lại là: *"C12 (quan hệ đại học; lời khai lần đối mặt ở bệnh viện)"*. Do `C13` (nhật ký) đã được chuyển đúng đắn sang B10, nếu B06 đã kể hết cả quan hệ lẫn cuộc gặp ở bệnh viện, thì B08 hoàn toàn không còn dữ kiện mới nào để phát triển, trở thành một đoạn lặp lại thuần túy.
- **Cần gì để đóng:** Phân định rõ phạm vi sử dụng `C12` giữa hai beat:
  - B06: Chỉ dừng ở mức nhận diện nhân thân — Lazarus lọt vào danh sách phụ nữ được rà soát năm 2009 vì từng có quan hệ tình cảm thời đại học với John Ruetten.
  - B08: Triển khai toàn bộ chi tiết chiều sâu về cuộc gặp chạm trán tại bệnh viện nơi Sherri làm việc và thái độ thù địch theo lời khai, phục vụ đúng chức năng phân tích động cơ mà công tố xây dựng trước khi bước vào cuộc phỏng vấn.

**D16 — SUA: B13 cần ghi rõ mốc thời gian điều trần parole bằng chữ tránh nhầm lẫn định dạng**

- **Chỗ nào:** `scripts/01-beat-sheet.md:42`, dòng 154 và dòng 194, đối chiếu `sources/S07-schedule-excerpt.md:9` và `claims.csv` (C25).
- **Vấn đề gì:** Beat sheet ghi ngày điều trần là `09/10/2026`. Trong nguồn trích `S07`, ngày gốc theo chuẩn Mỹ (MM/DD/YYYY) là `10/09/2026` thuộc lịch "October 2026 Hearing Calendar", tức ngày 09 tháng 10 năm 2026. Cách ghi số `09/10/2026` trong môi trường tiếng Việt rất dễ bị đọc nhầm thành ngày 10 tháng 09 năm 2026 (ngay sát mốc thời gian của vụ án trong hồ sơ).
- **Cần gì để đóng:** Ghi rõ mốc ngày bằng chữ tại B13: "dự kiến ngày 09 tháng 10 năm 2026" (thay vì chỉ viết dạng số `09/10/2026`) để bảo đảm người viết kịch bản ở bước 5 không diễn đạt sai thành tháng Chín.

**D17 — SUA: Bảng manh mối mục 5 thiếu manh mối trung tâm C11 (chiếc cốc vứt đi)**

- **Chỗ nào:** `scripts/01-beat-sheet.md:169-179` (Bảng manh mối §5).
- **Vấn đề gì:** Bảng manh mối liệt kê hầu hết các vật chứng chính (C03, C05, C04, C07, C09, C14, C13, C19), nhưng lại bỏ sót vật chứng tạo bước ngoặt đột phá quan trọng nhất của chuyên án năm 2009: chiếc cốc và ống hút bị vứt bỏ thu được mẫu DNA khớp sơ bộ 11 vị trí (`C11`).
- **Cần gì để đóng:** Bổ sung một hàng vào Bảng manh mối §5 cho `C11`:
  - *Manh mối:* Chiếc cốc và ống hút bỏ đi tại Costco.
  - *Xuất hiện:* B07.
  - *Khán giả hiểu gì lúc đó:* Mối nối sinh học trực tiếp đầu tiên giữa dấu cắn 1986 và nghi phạm có tên; khớp một phần 11 vị trí.
  - *Chứng cứ thật nói gì:* `C11` `established`; hồ sơ một phần, đủ căn cứ xin lệnh bắt/lấy mẫu trực tiếp, chưa phải chuẩn ra tòa.
  - *Giải ở đâu:* B07 (mẫu lén) và B10 (xác nhận lại bằng mẫu trực tiếp 13 loci và SERI 15 loci).
  - *Trả lời câu hỏi nào:* Mẫu dấu cắn 1986 nối với người cụ thể nào.

---

## Phản hồi các câu hỏi mở và thảo luận điểm D01–D11

### 1. Trả lời các câu hỏi tác giả nêu (Q1–Q5)

- **Về Q1 / D03 (Beat động cơ B08 và vị trí của C13):**
  - Đồng thuận với tác giả và Codex: Giữ nguyên `C13` ở B10 là hoàn toàn chính xác theo conflict note ("nhật ký thu sau khi bắt"). Việc này ngăn chặn triệt để nguy cơ người xem hiểu lầm điều tra viên đã đọc được nhật ký trước khi phỏng vấn.
  - Không gộp B08 vào B06: Cần giữ B08 để tạo khoảng lắng cần thiết nhằm xây dựng động cơ con người trước màn đối đầu căng thẳng ở B09. Tuy nhiên, tác giả phải áp dụng giải pháp ở D15 để B06 không "nói trước" nội dung của B08.

- **Về Q2 / D01 (Hook C03 vs C05):**
  - Chọn `C03` (chồng thiết bị âm thanh) làm hook chính là hoàn toàn xác đáng: Nó bám đúng cột `script_segment` của ledger bước 3, thể hiện trực diện mâu thuẫn vật lý tại hiện trường (lựa chọn 3 của STORYTELLING.md), và tạo tiền đề vững chắc cho lời giải "dàn dựng" ở B11.
  - Bản kịch bản trước đây của Gemini mở bằng BMW là do viết trước khi có khung sườn chuẩn hóa; ở bước 5 bản kịch bản sẽ được điều chỉnh quy về khung này. Tác giả chỉ cần giải quyết mâu thuẫn câu chữ nêu tại D12.

- **Về Q3 / D02 (Tiết lộ sĩ quan tuần tra LAPD ở B04 hay B06):**
  - **Khuyến nghị điều chỉnh:** Nên giữ thông tin người bị nghi ngờ thuộc LAPD tới B06. Ở B04, chỉ nên nêu: gia đình Sherri nghi ngờ một phụ nữ là bạn gái cũ của John từng đe dọa Sherri, nhưng cảnh sát thời điểm đó đang tin vào giả thuyết trộm nên không tập trung vào hướng này.
  - *Lý do:* Nếu khán giả biết ngay từ B04 rằng nghi phạm của gia đình là một nữ cảnh sát tuần tra LAPD, thì bước ngoặt B05 ("kết quả DNA cho thấy mẫu chính là của NỮ") sẽ bị giảm mạnh tính bất ngờ (khán giả sẽ lập tức liên hệ ngay với người phụ nữ LAPD ở B04). Để dành yếu tố thân phận LAPD và chức danh thám tử cho B06 sẽ tạo ra cú hích kép hoàn hảo: vừa hé lộ danh tính Stephanie Lazarus, vừa phơi bày vị trí công tác gây sốc của nghi phạm.
  - Trường hợp tác giả vẫn muốn giữ "sĩ quan tuần tra LAPD" ở B04 theo lời khai gia đình (`C07`), thì ở B06 không được viết theo hướng "khán giả lần đầu biết cô ta là cảnh sát", mà phải chuyển trọng tâm B06 thành: "từ một cảnh sát tuần tra năm 1986, đến 2009 cô ta đã thăng tiến thành thám tử kỳ cựu bậc ba của chính LAPD".

- **Về Q4 / D05 (B11 trả hook chỉ bằng C20 `alleged`):**
  - Hoàn toàn đủ và đúng chuẩn: Trong hồ sơ thực tế của vụ án, việc hiện trường bị dàn dựng để ngụy tạo trộm cắp là suy luận chuyên môn của chuyên gia hiện trường Mark Safarik được công tố trình bày tại tòa (`C20`), không có camera hay lời thú tội trực tiếp. Việc quy nguồn rõ ràng cho lời khai chuyên gia tại tòa là giới hạn trung thực tối đa mà hồ sơ pháp lý cho phép.
  - Không thể và không được "sáng tác" thêm một lời giải `established` nào sớm hơn, vì điều đó sẽ vi phạm tính xác thực của tư liệu tòa án.

- **Về Q5 / D04 (Tách B10 thành B10a / B10b):**
  - Đồng thuận với Codex: Không cần tách thành hai beat riêng để tránh làm xáo trộn cấu trúc B01–B14 đã khớp với ledger. Thay vào đó, trong nội bộ B10, cấu trúc bài viết cần phân định rõ hai mảng đối lập: một bên là chuỗi chứng cứ khoa học củng cố (`C17`, `C18`) và một bên là các phản biện/giới hạn vật chứng từ phía luật sư bào chữa (`C13`, `C14`, `C15`, `C19`).

- **Về D06 (Truy ngược locator và ranh giới nguồn):**
  - Ghi nhận việc không thể tải PDF gốc S08 do lỗi kỹ thuật TLS/challenge là bất khả kháng và đã được ghi chú minh bạch từ bước nghiên cứu. Bản trích HTML và các locator trong `claims.csv` đã đủ để bảo đảm tính chính xác của các beat.

### 2. Ý kiến về các điểm D07–D11 của Codex

- **D07 (SUA - Mẫu cốc 11 vị trí):** ĐỒNG THUẬN. Dòng 37 cần sửa thành "khớp một phần tại 11 vị trí đọc được", tránh nhầm lẫn với bộ 13 loci của mẫu trực tiếp hoặc bộ 15 loci của SERI.
- **D08 (CHAN - Nhận định mức bạo lực tại B03):** ĐỒNG THUẬN. Nhận định "mức bạo lực vượt một vụ trộm hoảng loạn" ở dòng 71 mang tính suy diễn kết luận sớm của người kể, cần lược bỏ hoặc chỉ dẫn theo góc nhìn đánh giá ban đầu của điều tra viên.
- **D09 (CHAN - B10 không dùng C18 đóng chung dấu tay lạ C19):** ĐỒNG THUẬN. Phải giữ nguyên sự tồn tại của các dấu vết chưa xác định (`C19`) như một giới hạn trung thực của vụ án, không để kết quả DNA của SERI tạo cảm giác giả tạo rằng mọi nghi vấn hiện trường đều đã được giải quyết triệt để.
- **D10 (SUA - Tiêu đề B12 sửa 23 năm thành 26 năm):** ĐỒNG THUẬN. Khoảng cách từ vụ án 1986 đến bản án 2012 là 26 năm. 23 năm là mốc tính đến ngày bắt giữ 2009.
- **D11 (SUA - B10 nói "dàn dựng" trước mốc B11):** ĐỒNG THUẬN. Từ "dàn dựng" phải được bảo lưu tuyệt đối cho B11 theo đúng cam kết của Thang tiết lộ.

---

## Tôi đã không kiểm cái gì

- Chưa thể truy cập trực tiếp toàn văn tệp PDF gốc S08 qua mạng do hạn chế kỹ thuật của môi trường thực thi; việc đối chiếu dựa trên trích đoạn nguồn đã lưu, bản HTML phán quyết S01 và claim ledger C01–C26.
- Không sử dụng các công cụ duyệt web trực tiếp trong phiên này để tra cứu lại lịch parole S07 tại thời điểm hôm nay; thông tin kiểm tra dựa trên bản trích xuất S07 ngày 08/09–09/09/2026.
- Chưa tiến hành rà soát từng dòng đối chiếu giữa kịch bản tiếng Việt chi tiết với khung sườn này (đây là nhiệm vụ của bước 5 sau khi khung sườn được chốt).
- Không thực hiện tạo, sửa hay ghi đè bất kỳ tệp tin nào trong kho lưu trữ, tuân thủ nghiêm ngặt quy chế chạy tự động của reviewer.

```points
D12 | mở | scripts/01-beat-sheet.md:57 | SUA: Câu hỏi mở B01 nhắc xe và chìa khóa mâu thuẫn với ranh giới loại trừ BMW ở dòng 59
D13 | mở | scripts/01-beat-sheet.md:105 | SUA: Câu hỏi mở B07 nhảy cóc qua B08 để hỏi việc đối chất ở B09; làm đứt mạch nối câu hỏi
D14 | mở | scripts/01-beat-sheet.md:122 | SUA: B09 gán kết quả 13 loci của C17 xung đột với Thang tiết lộ dành mốc này cho B10
D15 | mở | scripts/01-beat-sheet.md:98 | SUA: B06 ôm trọn chi tiết lần gặp ở bệnh viện khiến B08 bị lặp và rỗng chức năng
D16 | mở | scripts/01-beat-sheet.md:42 | SUA: B13 cần ghi rõ ngày điều trần parole theo chữ tránh nhầm lẫn định dạng ngày MM/DD và DD/MM
D17 | mở | scripts/01-beat-sheet.md:169 | SUA: Bảng manh mối §5 bỏ quên manh mối bước ngoặt chiếc cốc và ống hút C11
```
