# r2 · Phản hồi khung sườn NET-0006 (tác giả: Claude)

Sản phẩm: `t-i/outputs/YouTube-Research-System/episodes/NET-0006-sherri-rasmussen/scripts/01-beat-sheet.md`. Đã đọc `THREAD.md`, `r1-00-proposal-claude.md`, `r1-01-review-codex.md`, `r1-02-review-gemini.md`, AGENTS.md mục 8, `.claude/skills/deliberation/SKILL.md`, `claims.csv` (C01–C26) và `sources/S07-schedule-excerpt.md`.

17 điểm đang mở. Tôi chấp nhận và đã sửa 13 điểm của người review (D07–D17) và 2 điểm tự nêu (D05, D06 phần ghi chú). 4 điểm tự nêu còn lại (D01, D03, D04) hội tụ với cả hai người review về hướng "giữ nguyên cấu trúc" — đóng bằng `chốt: giữ nguyên`. Không phản bác điểm nào: không có điểm nào rơi vào bốn lý do phản bác mà tôi thấy đứng vững hơn nhận xét.

`artifact_version` cũ 1 → mới **2**. Đường dẫn dòng dưới đây tính theo bản v2 vừa sửa.

---

## Các điểm tôi tự nêu (D01–D06)

### D01 — Hook C03 vs C05 · `chốt: giữ nguyên`

Cả Codex (r1-01 §D01/Q2) và Gemini (r1-02 Q2) đều xác nhận giữ hook thuần C03 là lựa chọn hợp lệ: bám đúng cột `script_segment` của ledger bước 3, là mâu thuẫn vật lý trực diện (STORYTELLING.md §2 lựa chọn 3), tạo tiền đề cho lời giải B11. Hai bản prose lệch nhau (Codex mở C03, Gemini mở C05) là vì viết **trước** khi có khung; bước 5 quy chúng về khung, không phải lý do đổi khung.

Điểm phụ còn lại — dòng 57 cũ nhắc "chìa và lái xe" mâu thuẫn ranh giới "hook gọn" — **đã xử lý ở D12** (viết lại câu hỏi mở, bỏ chi tiết xe/chìa). Ranh giới B01 dòng 59 nay ghi rõ: "Không nêu BMW / chìa khóa ở B01 — hook thuần C03; chi tiết chiếc xe để B04".

### D02 — B04 lộ "sĩ quan tuần tra LAPD" quá sớm · `đã sửa ở v2`

**Chấp nhận** (lỗi trình tự tiết lộ). Gemini (r1-02 Q3) nêu đúng: nếu B04 đã cho biết nghi phạm của gia đình là **một phụ nữ ngành LAPD**, cú lật B05 ("mẫu chính là của nữ") và cú lật B06 ("cô ta là cảnh sát") đều bị mòn — khán giả ghép ngay. Codex (r1-01 §D02) chấp nhận giữ "LAPD" ở B04 nhưng buộc B06 không được kể như "khán giả lần đầu biết". Tôi chọn phương án chặt hơn của Gemini vì nó thỏa mãn cả hai.

Sửa ở đâu:
- **Dòng 34** (thang tiết lộ, hàng B04): bỏ "người đó là sĩ quan tuần tra LAPD năm 1986" khỏi cột "khán giả mới được biết"; thêm vào cột cấm: "chưa nói người đó là cảnh sát / thuộc LAPD — để tới B06".
- **Dòng 79** (B04 · Ai biết gì): "một phụ nữ — bạn gái cũ của John — … chưa biết tên, **chưa biết nghề nghiệp**, chưa biết có phải hung thủ".
- **Dòng 83** (B04 · Ranh giới): "Chưa tiết lộ người đó là cảnh sát — cả nghề nghiệp lẫn tên và cấp bậc để tới B06, giữ nút 'nghi phạm trong ngành' cho B06 để không làm mòn cú lật B05".
- **Dòng 95** (B06 · Ai biết gì): B06 nay là nơi khán giả biết tên **và** biết cô ta ở trong ngành — "sĩ quan tuần tra LAPD năm 1986, nay là thám tử bậc ba" (khớp Codex: từ tuần tra → thám tử).

Thang tiết lộ B05 không bị "gia đình từng nêu một phụ nữ" làm mòn: biết gia đình nghi một phụ nữ năm 1986 không cho biết **mẫu pháp y** là nữ — đó vẫn là cú sập giả thuyết "hai gã trộm nam". Gemini cũng đồng ý để "gia đình nêu một phụ nữ" ở lại B04.

### D03 — B08 giữ riêng hay gộp vào B06 · `chốt: giữ nguyên`

Cả Codex (r1-01 §D03) và Gemini (r1-02 Q1) đều nói: **giữ B08 là beat riêng**, không gộp; rào chống nội tâm không nguồn trong khung là đủ. Gemini thêm: cần B08 để tạo khoảng lắng trước màn đối đầu B09. Điều kiện kèm theo — B06 không được "nói trước" nội dung B08 — **đã xử lý ở D15**.

Ghi rõ kết luận này vào **dòng 115** (B08 · Ranh giới): "B08 giữ là beat riêng, không gộp vào B06 (D03)".

### D04 — B10 nặng, có nên tách B10a/B10b · `chốt: giữ nguyên`

Cả Codex (r1-01 §D04/Q5) và Gemini (r1-02 Q5) đều nói: **không tách beat** (giữ B01–B14 khớp ledger); thay vào đó phân định chức năng/giới hạn từng nhóm chứng cứ **trong nội bộ** B10 — chính là D09. Ghi kết luận vào **dòng 131** (B10 · Ranh giới): "Không tách B10 thành hai beat — phân định chức năng trong nội bộ beat là đủ (D04)".

### D05 — B11 trả hook chỉ bằng C20 (`alleged`) · `đã sửa ở v2`

Cả Codex (r1-01 §D05, đã đối chiếu S01 note 10: lời khai Safarik có phần giải thích chồng thiết bị) và Gemini (r1-02 Q4) đều xác nhận: quy nguồn cho diễn giải chuyên gia tại tòa là **giới hạn trung thực tối đa** hồ sơ cho phép; không được "sáng tác" một lời giải `established` sớm hơn.

Tôi chấp nhận kết luận đó, và thêm một câu ở **dòng 135** (B11 · Ai biết gì) để ghi rõ phần trả lời hook **không tựa hết** vào C20: các sự kiện `established` — chồng đồ còn nguyên (C03), BMW bị bỏ lại còn chìa (C05), nhiều phòng không bị lục — đã tự làm suy yếu lời giải "trộm" từ B01/B04; C20 chỉ bổ sung cách đọc "dàn dựng sau khi giết", luôn quy nguồn cho chuyên gia công tố. Đây là chỗ cấu trúc mềm nhất tôi tự nêu; câu thêm này làm rõ payoff được phân bổ, không dồn hết vào một diễn giải tranh luận.

### D06 — Locator chưa tự truy ngược (PDF S08 bị chặn) · `chốt: giữ nguyên`

Cả hai người review coi việc không tải được PDF gốc S08 (lỗi TLS rồi challenge JavaScript) là **bất khả kháng**, đã ghi minh bạch từ bước nghiên cứu, **không phải lỗi nội dung riêng** (Codex r1-01 §D06; Gemini r1-02 D06). Codex đã truy ngược được một phần qua bản HTML S01: note 10 (đỡ C20) và note 13 (đỡ C11 — 11 vị trí).

Cập nhật mục §7 (**dòng 193**) để ghi lại tình trạng truy nguồn hiện tại: phần Codex đã truy được, phần còn chưa đủ để xác nhận toàn bộ C01–C26. Đây là housekeeping — bản chất điểm (có phải lỗi không) đã hội tụ là "không".

---

## Các điểm của Codex (D07–D11)

### D07 — Mẫu cốc ghi "11/13" · `đã sửa ở v2`

**Chấp nhận.** `claims.csv` C11 chỉ ghi "hồ sơ một phần khớp 11 vị trí", locator "S01 pp7–8 note 13"; "11/13" trộn con số dòng đọc được với số loci bộ Identifiler và dễ nhầm với đối chiếu 13 loci ở C17. Sửa **dòng 37** (thang tiết lộ, hàng B07): "Mẫu lén (cốc) cho hồ sơ một phần, khớp tại **11 vị trí đọc được**" + ranh giới "không nhầm với 13 loci mẫu trực tiếp (C17) hay 15 loci SERI (C18)". Dòng 104 và 106 (B07) đã dùng "11 vị trí" từ v1, giữ nguyên. Gemini D07 đồng thuận.

### D08 — B03 biến mức bạo lực thành sự thật · `đã sửa ở v2`

**Chấp nhận** (CHAN). Không có claim nào trong ledger xác lập ngưỡng so sánh "vượt một vụ trộm hoảng loạn" — đó là suy luận hành vi, và nó đưa lập luận bác giả thuyết trộm vào giọng người kể trước diễn giải chuyên gia B11. Sửa **dòng 71** (B03 · Ai biết gì): bỏ mệnh đề so sánh, giữ các chi tiết có C03 đỡ (trang sức còn nguyên, phòng ngủ không bị lục, không dấu cạy phá, nhiều phòng nguyên) + ghi rõ "không đưa nhận định so sánh … vào giọng người kể — không có claim đỡ". Câu hỏi mở B01 (dòng 57) cũng đã bỏ đặc trưng "cái chết dữ dội" khi viết lại ở D12, chỉ giữ dữ kiện `established` (Sherri chết). Gemini D08 đồng thuận.

### D09 — B10 dùng C18 đóng chung nhiễm bẩn + vân tay lạ · `đã sửa ở v2`

**Chấp nhận** (CHAN). C18 xác lập lần xét nghiệm bổ sung của SERI; C19 vẫn ghi vân tay/DNA lạ **chưa xác định**. Khớp DNA không tự nhận diện vân tay lạ, không tự chứng minh toàn bộ quá trình bảo quản sạch. Tách hai câu hỏi:
- **Dòng 128** (B10 · Câu hỏi đóng): nói rõ "câu hỏi này **chỉ đóng** phần độ vững của kết quả DNA"; phong bì rách và vân tay/DNA lạ (C19) "**vẫn để mở**".
- **Dòng 131** (B10 · Ranh giới): "**C18 không đóng C19** … vân tay/DNA lạ giữ nguyên là giới hạn trung thực".
- **Dòng 179** (§5 bảng manh mối, hàng "Phong bì rách, vân tay lạ"): cột "Giải ở đâu" đổi thành "B10 nêu song song kết quả SERI …; phần vân tay/DNA lạ **không đóng** — giữ là giới hạn".

Gemini D09 đồng thuận.

### D10 — Tiêu đề B12 "sau 23 năm" · `đã sửa ở v2`

**Chấp nhận.** Vụ án 1986 → bắt 2009 (≈23 năm) → kết án 2012 (≈26 năm). Sửa **dòng 141**: "### B12 — **Bản án năm 2012**". Thêm ở **dòng 142** (Chức năng): "Nếu nêu khoảng cách thời gian: … bắt 2009 (≈23 năm) → kết án 2012 (≈26 năm); không gộp hai mốc". Gemini D10 đồng thuận.

### D11 — B10 nói "dàn dựng" trước mốc B11 · `đã sửa ở v2`

**Chấp nhận.** Câu chuyển cũ "hiện trường trông như dàn dựng" ở câu hỏi mở B10 trao trước cách diễn giải mà thang tiết lộ (dòng 32, 40) dành cho B11. Sửa **dòng 129** (B10 · Câu hỏi mở): "vì sao chồng thiết bị âm thanh vẫn nằm nguyên cạnh cửa gara và chiếc BMW bị bỏ lại nguyên vẹn — những chi tiết B01/B04 đặt ra mà chưa ai giải? (→ B11)" + ghi rõ "**không dùng từ 'dàn dựng' ở đây; từ đó thuộc B11**". Gemini D11 đồng thuận.

---

## Các điểm của Gemini (D12–D17)

### D12 — Câu hỏi mở B01 nhắc xe/chìa mâu thuẫn ranh giới BMW · `đã sửa ở v2`

**Chấp nhận**, theo phương án 1 Gemini khuyên (giữ hook thuần C03). Sửa **dòng 57**: "Nếu kẻ đột nhập đã gom sẵn chồng đồ giá trị ngay lối ra, sao lại bỏ lại tất cả — và vì sao vụ việc kết thúc bằng cái chết của Sherri?" Bỏ hoàn toàn chìa khóa và lái xe khỏi B01. **Dòng 59** ranh giới nay ghi rõ: "Không nêu BMW / chìa khóa ở B01"; C05 vẫn xuất hiện lần đầu ở B04 (khớp thang tiết lộ và §5 dòng 172).

### D13 — Đứt mạch câu hỏi B07→B08→B09 · `đã sửa ở v2`

**Chấp nhận.** Câu hỏi mở B07 cũ ("cô ta nói gì khi bị đối chất?") nhảy cóc qua B08 (động cơ) thẳng tới B09. Sửa:
- **Dòng 105** (B07 · Câu hỏi mở): "Vì sao một thám tử LAPD đương chức lại dính tới hiện trường năm 1986 — mối liên hệ thật giữa cô ta và Sherri là gì? (→ B08)".
- **Dòng 113** (B08 · Câu hỏi mở): "Làm sao đối chất và lấy mẫu trực tiếp chuẩn pháp lý của một thám tử đương chức mà không làm lộ chuyên án? (→ B09)".

Chuỗi nay liền: B06 hỏi "lấy mẫu lén thế nào" → B07 đóng (cốc) + mở "vì sao/mối liên hệ" → B08 đóng (động cơ) + mở "đối chất + mẫu trực tiếp thế nào" → B09 đóng.

### D14 — B09 gán kết quả 13 loci của C17 · `đã sửa ở v2`

**Chấp nhận.** `claims.csv` cho C17 `script_segment` = "B09 B10", nên tách hành động (B09) khỏi kết quả (B10) vẫn khớp ledger. Sửa:
- **Dòng 122** (B09 · Claims): "C17 (rời phòng rồi bị bắt; **lệnh cưỡng chế thu mẫu niêm mạc miệng — kết quả khớp 13 loci để ở B10**)".
- **Dòng 38** (thang tiết lộ, hàng B09): thêm "có lệnh cưỡng chế thu mẫu niêm mạc miệng" vào cột "mới được biết" và "**chưa nêu kết quả khớp 13 loci** — để ở B10" vào cột cấm.

Dòng 39 (hàng B10) và dòng 130 (B10 · Claims) đã giữ kết quả 13 loci ở B10 từ v1.

### D15 — B06 lấn chi tiết bệnh viện làm B08 rỗng · `đã sửa ở v2`

**Chấp nhận.** `claims.csv` cho C12 `script_segment` = "B06 B08", nên chia phạm vi:
- **Dòng 98** (B06 · Claims): "C12 (Lazarus và John quen thời đại học — **cơ sở để cô lọt vào danh sách phụ nữ rà soát 2009**; chi tiết lần gặp ở bệnh viện và tuyến động cơ để ở B08)".
- **Dòng 99** (B06 · Ranh giới): "B06 chỉ dừng ở mức nhận diện nhân thân + lý do cô lọt vào danh sách — **chưa triển khai cuộc gặp ở bệnh viện**".
- **Dòng 114** (B08 · Claims): "C12 (lần đối mặt ở bệnh viện nơi Sherri làm việc; thái độ thù địch theo lời khai — triển khai ở đây để phục vụ lập luận động cơ của công tố)".

### D16 — B13 ghi ngày parole dạng số dễ nhầm · `đã sửa ở v2`

**Chấp nhận.** Đối chiếu `sources/S07-schedule-excerpt.md:9`: nguồn giữ ngày theo MM/DD/YYYY, ô Date = `10/09/2026`, thuộc "October 2026 Hearing Calendar" → **9 tháng 10 năm 2026**. Bản v1 viết "09/10/2026" (đọc kiểu DD/MM thì đúng ngày, nhưng người viết bước 5 dễ đọc thành 10 tháng 9). Sửa:
- **Dòng 42** (thang tiết lộ, hàng B13): "phiên điều trần dự kiến **ngày 9 tháng 10 năm 2026**" + cấm "không viết ngày dạng số '09/10'".
- **Dòng 154** (B13 · Claims): "phiên điều trần dự kiến **ngày 9 tháng 10 năm 2026**, 08:30 — nguồn S07 ghi `10/09/2026` dạng MM/DD/YYYY … dòng WE4479".
- **Dòng 155** (B13 · Ranh giới): "Bước 5 viết ngày điều trần bằng chữ … không viết dạng số '09/10'".
- **Dòng 195** (§7): đổi "WE4479 = 09/10/2026 08:30" thành "phiên dự kiến ngày 9 tháng 10 năm 2026, 08:30 (nguồn S07 ghi `10/09/2026` dạng MM/DD/YYYY)".

Chỉ đổi C25 (ngày tôi xác minh được từ S07). C23/C24 giữ dạng số vì tôi không có trích đoạn S04/S05 để xác nhận thứ tự tháng/ngày — không đổi cái chưa kiểm.

### D17 — §5 bảng manh mối thiếu C11 (chiếc cốc) · `đã sửa ở v2`

**Chấp nhận.** Thêm một hàng vào bảng §5 sau hàng "CODIS không khớp" (**dòng 176**): "Chiếc cốc và ống hút bỏ đi tại Costco | B07 | Mối nối sinh học trực tiếp đầu tiên giữa dấu cắn 1986 và nghi phạm có tên; khớp một phần 11 vị trí | C11 `established`; hồ sơ một phần, đủ căn cứ xin lệnh bắt/lấy mẫu trực tiếp, chưa phải chuẩn ra tòa | B10 (xác nhận lại bằng mẫu trực tiếp 13 loci và SERI 15 loci) | Mẫu dấu cắn 1986 nối với người cụ thể nào". Dùng "11 vị trí" (nhất quán D07), không "11/13".

---

## Tôi đã không kiểm cái gì

- **Không đọc trực tiếp toàn văn phán quyết S01.** Vẫn chỉ có `sources/S01-excerpt.md` (một blockquote) và `claims.csv`. PDF gốc S08 bị chặn từ bước nghiên cứu; lượt này tôi **không thử vượt chặn và không dùng công cụ web**. Các sửa ở D07/D08/D09/D14 dựa trên `claims.csv` (cột `claim`, `locators`, `conflicts`) chứ không phải truy ngược toàn văn S01. Cụ thể chưa tự xác minh: S01 pp7–8 note 13 có đỡ đúng "11 vị trí" không (C11); S01 pp67–69 + note 10 có đỡ diễn giải dàn dựng của Safarik không (C20); S01 pp10–12 có phân định được mức chi tiết "nhận diện nhân thân" (B06) khác "cuộc gặp ở bệnh viện" (B08) trong C12 không. Codex báo đã truy ngược note 10 và 13 qua bản HTML S01 — tôi **tin phần đó của Codex, chưa tự lặp lại**.
- **Không xác minh lịch parole S07 hôm nay.** D16 dựa trên `sources/S07-schedule-excerpt.md` (truy cập 09/09/2026) và C25. Không mở lại URL CDCR. Nếu bước 5 chạy trễ, cần kiểm lại dòng WE4479.
- **Không xác minh ngày của C23 (02/10/2024) và C24 (12/02/2025).** Không có trích đoạn S04/S05; để nguyên dạng số, không "viết ra chữ" một ngày chưa kiểm được thứ tự tháng/ngày.
- **Không đối chiếu hai bản kịch bản tiếng Việt câu-theo-câu với khung v2.** Đó là việc bước 5. Các chỗ lệch đã biết (thoại bịa B09, khẳng định `alleged` thành sự thật B11 ở bản Gemini) vẫn ghi làm "ghi chú cho bước 5" ở dòng 123 và 139, không sửa trong lượt này.
- **Không chạy `python scripts/thread.py apply` hay bất kỳ script coordination nào.** Lượt tự động; orchestrator lấy stdout làm file vòng và cập nhật `THREAD.md`. Tôi không sửa `THREAD.md`, không tạo file vòng trên đĩa.
- **Chỉ sửa artifact `01-beat-sheet.md`.** Không đụng `claims.csv`, `02-script-*`, hay artifact của bước khác.

```points
D01 | chốt: giữ nguyên | scripts/01-beat-sheet.md:59 | Hook C03 giữ nguyên — cả hai người review xác nhận; điểm phụ dòng 57 đã xử lý ở D12
D02 | đã sửa ở v2 | scripts/01-beat-sheet.md:79 | Giữ "cảnh sát/LAPD" cho B06; B04 chỉ nêu "một phụ nữ, bạn gái cũ của John" — thang tiết lộ dòng 34, B06 dòng 95
D03 | chốt: giữ nguyên | scripts/01-beat-sheet.md:115 | B08 giữ là beat riêng, không gộp B06 — cả hai người review đồng ý; overlap xử lý ở D15
D04 | chốt: giữ nguyên | scripts/01-beat-sheet.md:131 | Không tách B10a/B10b — cả hai người review đồng ý; phân định nội bộ beat xử lý ở D09
D05 | đã sửa ở v2 | scripts/01-beat-sheet.md:135 | Quy nguồn C20 là đủ; thêm câu ghi rõ C03/C05 established đã gánh phần trả lời hook từ B01/B04
D06 | chốt: giữ nguyên | scripts/01-beat-sheet.md:193 | PDF S08 bị chặn là bất khả kháng, không phải lỗi nội dung; §7 cập nhật phần Codex đã truy ngược (note 10, 13)
D07 | đã sửa ở v2 | scripts/01-beat-sheet.md:37 | "11/13" → "khớp tại 11 vị trí đọc được"; thêm ranh giới không nhầm với 13 loci (C17) / 15 loci (C18)
D08 | đã sửa ở v2 | scripts/01-beat-sheet.md:71 | Bỏ "mức bạo lực vượt một vụ trộm hoảng loạn" khỏi B03; ghi rõ không có claim đỡ ngưỡng so sánh
D09 | đã sửa ở v2 | scripts/01-beat-sheet.md:128 | Tách độ vững DNA (C17/C18) khỏi giới hạn C19; câu hỏi đóng B10, ranh giới dòng 131, bảng §5 dòng 179
D10 | đã sửa ở v2 | scripts/01-beat-sheet.md:141 | Tiêu đề B12 → "Bản án năm 2012"; thêm phân biệt bắt 2009 (≈23 năm) / kết án 2012 (≈26 năm)
D11 | đã sửa ở v2 | scripts/01-beat-sheet.md:129 | Câu hỏi mở B10 bỏ "dàn dựng", thay bằng gọi lại chi tiết chưa giải của B01/B04; từ "dàn dựng" giữ cho B11
D12 | đã sửa ở v2 | scripts/01-beat-sheet.md:57 | Viết lại câu hỏi mở B01 bỏ chìa khóa và lái xe; ranh giới dòng 59 cấm nêu BMW/chìa ở B01
D13 | đã sửa ở v2 | scripts/01-beat-sheet.md:105 | Câu hỏi mở B07 dẫn vào B08 (mối liên hệ/động cơ); câu hỏi mở B08 dòng 113 dẫn vào B09 (đối chất + mẫu trực tiếp)
D14 | đã sửa ở v2 | scripts/01-beat-sheet.md:122 | B09 chỉ giữ bắt + lệnh cưỡng chế thu mẫu miệng; kết quả 13 loci chuyển sang B10; thang tiết lộ dòng 38
D15 | đã sửa ở v2 | scripts/01-beat-sheet.md:98 | B06 chỉ nhận diện nhân thân + lý do lọt danh sách; chi tiết cuộc gặp bệnh viện chuyển sang B08 dòng 114
D16 | đã sửa ở v2 | scripts/01-beat-sheet.md:42 | Ngày điều trần ghi bằng chữ "ngày 9 tháng 10 năm 2026" (S07 ghi 10/09/2026 MM/DD); B13 dòng 154–155, §7 dòng 195
D17 | đã sửa ở v2 | scripts/01-beat-sheet.md:176 | Thêm hàng C11 (chiếc cốc và ống hút bỏ đi) vào bảng manh mối §5, xuất hiện B07, giải ở B10
```
