# NET-0006 — Khung sườn / beat sheet

**Vụ:** Sherri Rasmussen / Stephanie Lazarus. **Tác giả bước 4:** Claude. **Bản 3**, viết lại ngày 18/09/2026 theo skill `ky-an-viet` mới nhất. Bản 2 (đã chốt ở luồng `net-0006-khung-suon`) còn trong lịch sử git. Luồng review của bản này: `net-0006-khung-suon-v3`.

Đây là bộ xương mà bản tiếng Việt đầy đủ (bước 5) phải bám. Khung không chứa câu văn hoàn chỉnh — chỉ chức năng từng đoạn, ai biết gì, câu hỏi mở và đóng, nhánh giả thuyết, mã claim và ranh giới. Mã `C01`–`C48` trỏ tới `claims.csv`. **C27–C48 là phần bổ sung ngày 18/09/2026, chưa qua review bước 3** (mục 9).

---

## 0. Bản 3 đổi gì so với bản 2

| Thay đổi | Vì sao |
| --- | --- |
| Người nghe là khán giả Việt Nam: bảng thuật ngữ, ngày theo ngày/tháng/năm, dặm đổi sang ki-lô-mét, bối cảnh đặt ngay trước chỗ cần | Tú đổi hướng kênh ngày 14/09; `thi-truong-viet-nam.md`; mục "Bối cảnh cho người nghe Việt" ở `kien-truc-cau-chuyen.md` |
| Hai điểm mở nhánh giả thuyết (B04, B05), mỗi nhánh có chủ và có chỗ đóng | Mục "Mở nhánh giả thuyết", thêm ngày 16/09 |
| Đánh dấu chỗ được kể suy nghĩ hoặc lời của nhân vật vì nguồn có ghi: nhật ký 1985, lời cha Sherri thuật lại, lời Lazarus trong phỏng vấn và ở phiên xét tha | `giong-ke.md` và Ví dụ 5, thêm ngày 16/09 |
| Thêm chặng thứ tư: năm 2023 Lazarus nhận tội; năm 2025 ủy viên hội đồng xét tha cho rằng lời kể của cô không khớp chứng cứ ADN | Skill bắt kiểm diễn biến mới trước khi kể kết cục, và ưu tiên chỗ chứng cứ pháp y soi vào mâu thuẫn trong lời người bị kết án. Bản 2 dừng ở lịch parole, bỏ sót việc này |
| Đoạn kết đi theo thứ tự: trả lời câu hỏi → nối chi tiết còn treo → hệ quả với con người → (suy ngẫm nếu đủ điều kiện) → CTA một câu | Mục "Kết thúc" ở `giong-ke.md`, thêm ngày 16/09 |
| Sửa ba chỗ bản 2 nói quá nguồn: "hai gã trộm **nam**", "trang sức còn nguyên, phòng ngủ không bị lục", "Costco" | Đọc lại S01 ngày 18/09: điều tra viên hình dung "một hoặc hai kẻ trộm", không nói giới tính (C28); phán quyết không nhắc trang sức (C29); ledger không có Costco |
| Chồng dàn âm thanh ở hook mang dấu vân tay chưa xác định, và bào chữa dùng chính chi tiết đó. B11 giờ đặt hai cách đọc chồng đồ cạnh nhau | S01, phần chứng cứ bào chữa (C37). Bản 2 chỉ nói chung là "vân tay lạ" |
| Nghề cảnh sát của Lazarus — cú lật của B06 — giờ có claim riêng | C46, C31. Trước đây không claim nào đỡ, đúng như D03 của luồng `net-0006-ban-tieng-viet` đã nêu |
| B13 mới là lời nhận tội và điều nó không khớp; phần "hôm nay" và đoạn kết gộp vào B14 | Giữ đủ 14 beat để cột `script_segment` của ledger chỉ phải đổi C25 (B13 → B14) |

## 1. Câu hỏi trung tâm

Vì sao lời giải "một vụ trộm" không đưa tới người đã giết Sherri, và mẫu nước bọt giữ trong tủ đông từ năm 1986 đã nối vụ án với một người cụ thể như thế nào?

Bốn chặng trả lời, giữ tách bạch, không dồn:

1. **2005 — mẫu chính là của một phụ nữ;** đối chiếu cơ sở dữ liệu không ra ai. Biết giới tính, chưa biết danh tính. Không nói chặng này "đánh sập giả thuyết trộm": phán quyết không nói kẻ trộm mà điều tra viên hình dung là nam (C28). Nó thu hẹp câu hỏi, không loại hẳn một kẻ trộm nữ.
2. **2009 — một cái tên:** từ những phụ nữ có liên hệ với Sherri và John tới Stephanie Lazarus — người gia đình Sherri nêu với điều tra viên từ năm 1986, nay là thám tử của chính LAPD.
3. **2009–2012 — kiểm chứng tới mức đưa ra toà,** cùng các phản biện của bào chữa.
4. **2023–2025 — người bị kết án nhận tội,** và ủy viên hội đồng xét tha dùng chính chứng cứ ADN để cho rằng lời kể của cô về diễn biến không khớp. Chặng này không đổi bản án. Nó đóng câu hỏi "ai" bằng lời chính người đó, còn câu hỏi "chuyện xảy ra thế nào trong căn hộ" chỉ được trả lời một phần.

## 2. Góc kể, người kể, người nghe

- **Mở bằng một vật cần giải thích:** dàn âm thanh bị kéo khỏi tủ, xếp cạnh cửa ra gara, nhưng không bị mang đi (C03, C29). Cách đọc "dàn dựng" để tới B11, và ở đó phải đứng cạnh dấu vân tay chưa xác định trên chính chồng đồ ấy (C37).
- **Xưng hô:** người kể xưng "mình", gọi người nghe "các bạn" — mặc định biên tập theo `giong-ke.md`, vì `channel.narrator_voice` trong sổ còn trống. Chưa phải quyết định của kênh. Bước 5 ghi rõ mặc định này ở đầu `02-script-vi.md`, ngoài phần lời kể.
- **Người kể xuất hiện có việc:** ở những chỗ khung ghi **Người kể** — nêu điều trái lẽ thường, nhắc một chi tiết sắp được dùng lại, giữ một giới hạn chứng cứ, mở nhánh. Không rải đều, không cứ hết đoạn lại úp mở.
- **Điều tra là diễn biến:** mỗi beat có người đang theo dõi, điều họ muốn biết, việc họ làm, kết quả, trở ngại.
- **Ba lớp phải tách ở mọi beat:** sự việc; điều nhân vật biết hoặc tin lúc đó; điều người nghe biết tại beat đó.
- **Tên:** mọi tên trong vụ viết bằng chữ Latin, giữ nguyên (Sherri Rasmussen, John Ruetten, Stephanie Lazarus, Van Nuys, Glendale, Santa Monica). Quy tắc Hán Việt không áp dụng. Cách đọc cho TTS là việc bước 6.
- **Gọi Lazarus:** trước B06 là "bạn gái cũ của John"; từ B06 gọi tên. Kể cả sau khi bị kết án cũng không "hắn", "ả", "ác quỷ" — gọi trung tính, để sự việc tự nói.

### Thuật ngữ và đơn vị

Chỉ giải thích khi beat cần, đặt ngay trước chỗ dùng. Cột "Beat" cho biết chỗ giải thích lần đầu.

| Trong nguồn | Lời kể | Beat | Ghi chú |
| --- | --- | --- | --- |
| LAPD | Sở Cảnh sát Los Angeles; sau đó "LAPD" hoặc "sở cảnh sát" | B03 | |
| coroner's office | văn phòng pháp y — nơi khám nghiệm tử thi và lưu mẫu | B03 | C36 |
| cold case unit | đội chuyên xem lại các vụ án cũ chưa phá | B05 | |
| national data bases | cơ sở dữ liệu toàn quốc lưu hồ sơ ADN của người từng phạm tội | B05 | C35. Không gọi tên CODIS khi ledger chưa có |
| major / minor profile | mẫu lẫn ADN của hai người: phần nhiều hơn là của một phụ nữ khác, phần ít hơn khớp Sherri | B05 | C09 |
| loci | những vị trí trên ADN mà phòng xét nghiệm đem so | B07 | Chỉ nêu số vị trí khi cần phân biệt 11 / 13 / 15 |
| Miranda | quyền giữ im lặng và có luật sư mà cảnh sát Mỹ phải đọc cho người bị bắt | B09 | |
| SERI | một phòng xét nghiệm tư, độc lập với LAPD | B10 | |
| amylase | một enzym có nhiều trong nước bọt | B10 | C18 |
| jury | bồi thẩm đoàn — người dân được chọn để quyết định bị cáo có tội hay không | B12 | Không gọi là hội thẩm nhân dân |
| first degree murder | giữ tên tội gốc, giải thích bằng chức năng | B12 | Định nghĩa chưa có nguồn trong ledger (mục 11). Không nói "giết người cấp độ một" |
| 25 years to life + 2 | 25 năm tới chung thân cho tội giết người, cộng 2 năm vì dùng súng: tổng 27 năm tới chung thân | B12 | C39. Không nói "phải đủ 27 năm mới được xét tha" — mâu thuẫn với phiên 2023 (C40) |
| Court of Appeal | toà phúc thẩm của bang California | B12 | C21 |
| habeas corpus / Ninth Circuit | yêu cầu toà liên bang xem việc giam giữ có hợp hiến không; Toà phúc thẩm liên bang khu vực 9 giữ nguyên việc bác yêu cầu | B12 | C22. Tên gốc chỉ cần trong kịch bản làm việc |
| parole | tha có điều kiện trước khi hết án | B13 | Không gọi là đặc xá |
| Board of Parole Hearings | hội đồng xét tha có điều kiện của bang California | B13 | |
| youthful offender law | một đạo luật của California dành cho người phạm tội khi còn trẻ — lúc gây án Lazarus gần 26 tuổi | B13 | C40. Không nêu ngưỡng tuổi khi nguồn chưa nói |
| 2.5 miles | khoảng 4 ki-lô-mét | B04 | Kịch bản làm việc giữ "2,5 dặm" |

Ngày trong lời kể nói bằng chữ ("ngày 24 tháng 2 năm 1986"). Không viết ngày dạng số trong lời đọc — "09/10" dễ bị nghe thành tháng 9 (D16 bản 2).

## 3. Thang tiết lộ

Người nghe chỉ được biết một điều **sau khi** manh mối cho điều đó đã nằm trên bàn.

| Beat | Người nghe mới được biết | Chưa được lộ |
| --- | --- | --- |
| B01 | Chồng dàn âm thanh xếp cạnh cửa gara, không bị mang đi; các phòng khác có đồ giá trị không bị đụng; một người phụ nữ đã chết | "dàn dựng"; chiếc xe; vân tay trên chồng đồ; mọi nghi phạm |
| B02 | Sherri là ai; khung giờ ngày 24/02/1986 qua các cuộc gọi không ai nghe | giờ tử vong |
| B03 | Điều tra viên đọc là trộm; mẫu nước bọt ở vết cắn được thu và cất tủ đông | giới tính trong mẫu; "trộm nam" |
| B04 | Chiếc xe; gia đình và John nêu bạn gái cũ của John; cha Sherri nói chị từng bị người này đe doạ; **mở NB1** | tên, nghề (D02 bản 2 giữ nguyên); chuyện đồng phục (C31); câu "If I can't have John" (C32) |
| B05 | Mẫu chính là của nữ; cơ sở dữ liệu không ra ai; **mở NB2** | "mọi ADN ở hiện trường là của nữ"; 15 vị trí |
| B06 | Stephanie Lazarus, thám tử LAPD; năm 1986 đã là cảnh sát; lời cha Sherri về lần thấy cô mặc đồng phục trong phòng khách | chưa có kết quả so mẫu |
| B07 | Cốc và ống hút cô bỏ đi → khớp một phần, 11 vị trí đọc được | toàn bộ hồ sơ; chuẩn ra toà |
| B08 | Quan hệ từ đại học; lời khai của John về tháng 6/1985; câu "If I can't have John" (bị cho là, quy nguồn); động cơ là lập luận của công tố | nhật ký (thu sau khi bắt) |
| B09 | Phỏng vấn 05/06/2009 lấy cớ vụ trộm tác phẩm nghệ thuật; những câu cô nói; đòi luật sư; bị bắt; lệnh lấy mẫu niêm mạc miệng | kết quả 13 vị trí (D14 bản 2); gọi là thú tội |
| B10 | 13 vị trí; SERI 15 vị trí có đại diện bào chữa; nhật ký 1985; súng dự phòng báo mất; tranh cãi đạn; ADN dưới móng tay chưa xác định | "dàn dựng" (D11 bản 2); vân tay trên chồng đồ |
| B11 | Hai cách đọc chồng đồ tại toà: chuyên gia công tố nói hiện trường được dàn dựng; bào chữa chỉ ra vân tay không thuộc ba người đã biết trên chính chồng đồ đó | phán quyết; "dàn dựng" nói bằng giọng người kể |
| B12 | Có tội; 27 năm tới chung thân; phúc thẩm 2015 giữ; habeas 2023 bác; lập luận "truy tố chậm" của bào chữa | bao che có tổ chức (C22); lời nhận tội 2023 |
| B13 | Nhận tội 11/2023; đề xuất tha; thống đốc; rút lại 10/2024; phiên 2025 và lập luận ADN của ủy viên | "đã được thả"; coi lời kể 2023–2025 là diễn biến đã xác lập |
| B14 | Phiên ngày 9 tháng 10 năm 2026 theo lịch; điều còn để ngỏ; hệ quả với con người; CTA | kết quả phiên khi chưa có |

Không đoạn nào gọi sai bản chất để tạo bất ngờ. Hai cú lật — mẫu của một phụ nữ, rồi phụ nữ ấy là cảnh sát — đến đúng thứ tự vụ án thật sự phát hiện. Lời nhận tội đến đúng lúc nó xảy ra, sau mọi cấp xét lại.

## 4. Nhánh giả thuyết

Luật ở `kien-truc-cau-chuyen.md`: nhánh mọc từ dữ kiện đã kể; mỗi nhánh giải thích được mọi dữ kiện tới lúc đó, hoặc nói rõ vướng ở đâu; nói rõ nhánh của ai; có một nhánh bình thường; hai tới ba nhánh; nhánh nào mở phải đóng.

### NB1 — B04, năm 1986: một kẻ lạ, hay một người Sherri quen?

**Dữ kiện đã kể tới lúc mở:** chồng đồ gom mà không mang đi; ngăn kéo bị đổ; các phòng khác có đồ giá trị không bị đụng; không có dấu đột nhập bằng vũ lực; vết cắn trên cẳng tay, mẫu nước bọt cất tủ đông; chiếc BMW biến mất, tìm thấy ngày 7/3 cách nhà khoảng 4 ki-lô-mét, chìa khoá còn, không bị tháo gì; John nói với điều tra viên về bạn gái cũ, cha Sherri nói chị từng bị người này đe doạ, cha mẹ Sherri đề nghị điều tra người ấy.

| Nhánh | Của ai | Giải thích được | Vướng ở đâu | Đóng ở |
| --- | --- | --- | --- | --- |
| 1. Một hoặc hai kẻ trộm lạ vào qua cửa mở, bị bất ngờ, bắn chị khi giằng co khẩu súng, rồi bỏ chạy bằng xe — **nhánh bình thường** | Điều tra viên 1986 (C28, C06) | Ngăn kéo đổ, đồ đã gom, không phá cửa, xe mất | Gom rồi bỏ lại; lấy xe rồi bỏ xe còn chìa, không tháo gì. Hoảng loạn giải thích được phần nào — người kể nói thẳng vậy, không gọi là bác bỏ | B05 làm yếu (mẫu của nữ); B06–B12 thay bằng một người có tên; B13 lời nhận tội |
| 2. Một người Sherri quen — người phụ nữ gia đình nêu | Gia đình Sherri và John (C07, C30) | Có một người có lý do nhắm vào Sherri; lời cha Sherri kể chị từng bị đe doạ | Năm 1986 không dữ kiện hiện trường nào chỉ riêng về người này; lời đe doạ là lời thuật lại | B06 (đúng người đó), B07–B12, B13 |

**Người kể:** hỏi thay người nghe — thứ gì có thể phân xử hai hướng này? — rồi nhắc mẫu nước bọt đang nằm trong tủ đông. Không nói năm 1986 "chưa thể" xét nghiệm ADN (không có claim); chỉ nói mẫu nằm đó tới năm 2005 mới được xét nghiệm.

**Không mở nhánh "có người sắp đặt cho giống một vụ trộm" ở đây.** Trong hồ sơ, cách đọc ấy chỉ xuất hiện qua lời chuyên gia công tố tại toà (C20, `alleged`). Người kể nêu nó từ B04 là tự khởi xướng giả thuyết của công tố. Câu hỏi ở hook đủ để người nghe tự nghĩ tới; B11 trả lời bằng lời chuyên gia, có quy nguồn.

Nhánh 2 chỉ đích danh một người có thể nhận diện. Được mở vì hai lẽ: đó là điều gia đình thật sự đã nói với điều tra viên (C30), và người đó đã có bản án kết tội có hiệu lực (C21, C22). Ở B04 nhánh vẫn phải nghe là niềm tin của gia đình, không phải điều người kể khẳng định.

### NB2 — B05, năm 2005: người phụ nữ trong mẫu là ai?

**Dữ kiện đã kể tới lúc mở:** mẫu chính là của một phụ nữ; phần phụ khớp Sherri; đối chiếu cơ sở dữ liệu toàn quốc không ra; phong bì đựng mẫu rách khi được tìm lại, ống có vẻ còn nguyên (C19); lời báo của gia đình năm 1986 (B04).

| Nhánh | Của ai | Giải thích được | Vướng ở đâu | Đóng ở |
| --- | --- | --- | --- | --- |
| 1. Một phụ nữ lạ, chưa có hồ sơ | Hành động của đội án cũ: đối chiếu định kỳ với cơ sở dữ liệu người phạm tội (C35) | Mẫu của nữ; không khớp dữ liệu | Không vướng dữ kiện nào — chỉ là năm này qua năm khác không ra ai | B06–B07: khớp với một người có tên |
| 2. Một phụ nữ có liên hệ với Sherri | Điều tra viên năm 2009 (C10); trước đó là gia đình (C30) | Mẫu của nữ; lời báo năm 1986 | Chưa có mẫu của ai để so | B06, B07 |
| 3. Mẫu bị lẫn ADN của người khác trong 19 năm lưu giữ hoặc lúc xử lý — **nhánh bình thường** | Người kể nêu ở đây; tại toà bào chữa chất vấn việc lưu mẫu (C19) | Phong bì rách | Phần phụ khớp Sherri, mẫu lấy ngay tại vết cắn | B10: SERI xét ống mẫu thứ hai, có đại diện bào chữa, amylase và 15 vị trí (C18) — **làm yếu**, không bác bỏ; B12 bồi thẩm đoàn không chấp nhận; B13 lời nhận tội |

Nhánh 3 không gán việc làm lẫn mẫu cho người nào cụ thể.

### Câu hỏi treo và chỗ trả lời

| Câu hỏi | Mở | Trả lời |
| --- | --- | --- |
| Vì sao chồng đồ không bị mang đi? | B01 | B11: hai cách đọc tại toà. B14: phần vân tay vẫn để ngỏ |
| Chuyện gì xảy ra từ lúc John đi làm tới lúc anh về? | B02 | Một phần: B13 (lời Lazarus 2023–2025, và nhận định của ủy viên). B14 nói rõ không có giờ tử vong chắc chắn |
| Người phụ nữ gia đình nêu là ai? | B04 | B06 |
| Vì sao hướng ấy không được theo từ năm 1986? | B06 (người nghe sẽ tự hỏi khi biết cô là cảnh sát) | B12, và chỉ tới mức nguồn cho phép: đây là điểm tranh luận tại toà (C07, C30, C47); toà liên bang phân tích cả khi giả định cáo buộc là đúng và không xác nhận có bao che (C22) |
| Lấy mẫu của một thám tử đương chức thế nào để cô không biết? | B06 | B07 |
| 27 năm tới chung thân, sao năm 2023 đã xét tha? | B12 (ngầm) | B13 (C40) |
| Phiên ngày 9 tháng 10 năm 2026 ra sao? | B14 | Chưa có — nói rõ; kiểm lại trước khi xuất bản (mục 12) |

---

## 5. Beat sheet — B01→B14

Mỗi beat: **Chức năng · Ai biết gì · Câu hỏi đóng · Câu hỏi mở · Claims · Ranh giới.** Thêm **Bối cảnh**, **Người kể**, **Nhánh**, **Suy nghĩ/lời có nguồn** khi beat cần.

### B01 — Chồng đồ chưa bị mang đi
- **Chức năng:** hook. Một vật cụ thể đặt câu hỏi trung tâm mà chưa giới thiệu cả vụ.
- **Ai biết gì:** người nghe thấy một căn hộ ở Los Angeles: dàn âm thanh bị kéo khỏi tủ, xếp cạnh cửa ra gara, không bị mang đi; các phòng có đồ giá trị khác, kể cả một dàn âm thanh khác, không bị đụng tới; và một người phụ nữ đã chết. Chưa biết tên, giờ, nghi phạm.
- **Câu hỏi mở:** người vào nhà đã gom sẵn đồ ở lối ra, sao lại bỏ đi mà không mang theo?
- **Người kể:** được nói thẳng điều trái lẽ thường này trong một câu. Không đoán lời giải.
- **Claims:** C03, C29.
- **Ranh giới:** không "dàn dựng"; không chiếc xe (D01, D12 bản 2); không vân tay trên chồng đồ (để B11); không mô tả giác quan, không thương tích.

### B02 — Sherri, và một ngày không ai nghe máy
- **Chức năng:** bối cảnh con người, vừa đủ.
- **Ai biết gì:** Sherri 29 tuổi, điều dưỡng ở một bệnh viện tại Glendale, cưới John tháng 11/1985 — ba tháng trước; hai người sống trong một căn hộ ở Van Nuys (C01, C27). Ngày 24/02/1986, John đi làm lúc 07:20; từ khoảng 10:00 gọi về không ai nghe; khoảng 18:00 anh về (C02).
- **Câu hỏi đóng:** nạn nhân là ai, mốc thời gian nào.
- **Câu hỏi mở:** chuyện gì xảy ra trong khoảng ấy?
- **Bối cảnh:** Van Nuys và Glendale đều thuộc vùng Los Angeles — một câu, đủ để người nghe biết đang ở đâu.
- **Claims:** C01, C02, C27.
- **Ranh giới:** không chốt giờ tử vong (C02, timeline). Không dựng chuỗi hành động trong khoảng trống. Không thêm lý do John gọi hay cảm giác của anh — nguồn không ghi. Không dùng lỗi "childhood" của S02. Không tên đường, số nhà.

### B03 — Điều tra viên đọc hiện trường
- **Chức năng:** đặt khung diễn giải của điều tra viên, và mẩu chứng cứ sẽ sống lâu hơn khung đó.
- **Ai biết gì:** điều tra viên cho rằng một hoặc hai kẻ trộm đã vào qua một cánh cửa mở, bất ngờ gặp Sherri, và bắn chị trong lúc giằng co khẩu súng (C28). Họ viện dẫn một vụ trộm khác trong khu vực, xảy ra sáu tuần sau (C06). Trên cẳng tay Sherri có vết cắn; chuyên viên hiện trường Lloyd Mahaney thấm mẫu ở đó (C04); ống mẫu nằm trong tủ đông của văn phòng pháp y từ đó (C36).
- **Câu hỏi đóng:** ban đầu cảnh sát giải thích thế nào?
- **Câu hỏi mở:** khung trộm giải thích được chồng đồ bị bỏ lại không? Mẫu ở vết cắn sẽ cho biết điều gì?
- **Bối cảnh:** LAPD; văn phòng pháp y — mỗi thứ một câu, đặt đúng chỗ nhắc tới.
- **Người kể:** có thể nhắc người nghe nhớ mẫu này, không gọi nó là "chìa khoá phá án".
- **Claims:** C03, C04, C06, C28, C29, C36.
- **Ranh giới:** giả thuyết trộm là niềm tin của điều tra viên, không phải sự thật của người kể, và không gọi là "sai" ở đây. Không "trộm nam" (C28). Không nói vụ trộm sáu tuần sau là cùng thủ phạm hay xảy ra trước (C06). Không so hình răng. Không nói năm 1986 không thể xét nghiệm ADN. Không nói vì sao mẫu được giữ — nguồn không ghi lý do (C36). Không trang sức, không phòng ngủ.

### B04 — Chiếc xe, lời báo của gia đình, và hai hướng
- **Chức năng:** đưa ra hướng thứ hai đã có từ những ngày đầu; mở NB1; hồ sơ nguội dần.
- **Ai biết gì:** ngày 07/03/1986, chiếc BMW được tìm thấy cách nhà khoảng 4 ki-lô-mét, chìa khoá còn, không bị tháo phụ tùng (C05). Trong vài ngày hoặc vài tuần sau vụ án, John cho điều tra viên biết về một người bạn gái cũ; cha Sherri nói Sherri từng bị bạn gái cũ của chồng đe doạ; cha mẹ Sherri đề nghị điều tra người này (C07, C30). Hướng trộm vẫn là hướng chính (C06). Người nghe biết có "bạn gái cũ của John" — chưa biết tên, nghề, chưa biết có liên quan hay không.
- **Câu hỏi đóng:** có ai chỉ ra một hướng khác không? — Có, gia đình.
- **Câu hỏi mở:** NB1. Thứ phân xử được đang nằm trong tủ đông.
- **Nhánh:** NB1 (mục 4).
- **Suy nghĩ/lời có nguồn:** lời cha Sherri là lời thuật lại của ông với điều tra viên — kể đúng như vậy ("cha chị nói với điều tra viên rằng…"), không dựng thành cảnh Sherri bị đe doạ.
- **Claims:** C05, C06, C07, C30.
- **Ranh giới:** chưa lộ tên, nghề (D02 bản 2). Chưa kể chuyện đồng phục (C31 → B06) và câu "If I can't have John" (C32 → B08). Không kết luận điều tra viên bỏ sót hay bao che. Lưu ý cho B12: C30 là chứng cứ **chính bên Lazarus** đưa ra khi kháng cáo, để lập luận rằng truy tố chậm làm cô bất lợi (C47).

### B05 — Năm 2005: mẫu là của một phụ nữ
- **Chức năng:** chặng ngoặt thứ nhất; mở NB2.
- **Ai biết gì:** tháng 9/2003, đội án cũ của LAPD yêu cầu xét nghiệm ADN; tháng 12/2004 họ mở lại hồ sơ và nhờ văn phòng pháp y tìm mẫu — mẫu nằm trong tủ đông từ năm 1986; phong bì rách, ống có vẻ còn nguyên (C19, C35, C36). Năm 2005, chuyên viên Jennifer Francis của LAPD xét nghiệm: phần chính là ADN của một phụ nữ, phần phụ khớp Sherri. Đối chiếu cơ sở dữ liệu toàn quốc: không ra ai; từ đó họ đối chiếu định kỳ (C08, C09, C35).
- **Câu hỏi đóng:** mẫu năm 1986 chứa gì?
- **Câu hỏi mở:** NB2 — người phụ nữ ấy là ai?
- **Bối cảnh:** đội án cũ; phần chính / phần phụ của một mẫu lẫn; cơ sở dữ liệu toàn quốc.
- **Nhánh:** NB2 (mục 4).
- **Claims:** C04, C08, C09, C19, C35, C36.
- **Ranh giới:** ba mốc 2003, 2004, 2005 là ba bước khác nhau (C08). Không nói mọi ADN ở hiện trường là của nữ (C09, C19, C37). Không 15 vị trí (đó là C18, năm 2010). Không nói kết quả này "đánh sập" giả thuyết trộm. Câu nguyên văn S01 để đối chiếu: "The DNA that comprised the major profile was from a female."

### B06 — Năm 2009: những người phụ nữ quanh Sherri và John, và một cái tên
- **Chức năng:** chặng ngoặt thứ hai — từ "một phụ nữ" thành "người phụ nữ này"; nghi phạm ở trong ngành.
- **Ai biết gì:** tháng 2/2009 hồ sơ được giao lại; điều tra viên xem xét những phụ nữ có liên hệ (C10). Trong đó có Stephanie Lazarus — quen John từ thời đại học (C12), đúng người gia đình Sherri đã nêu năm 1986 (C30). Năm 2009 cô là thám tử LAPD với 25 năm trong ngành; năm 1986 cô đã làm cảnh sát khoảng hai năm (C46). Chưa có mẫu để so.
- **Câu hỏi đóng:** người phụ nữ gia đình nêu là ai?
- **Câu hỏi mở:** lấy mẫu ADN của một thám tử đương chức thế nào để cô không biết? Và người nghe sẽ tự hỏi: sao năm 1986 hướng này không được theo? (→ B12)
- **Người kể:** nối lại một chi tiết cũ, giờ mang nghĩa khác — năm 1986 cha Sherri còn kể với thám tử rằng có lần Sherri thấy người phụ nữ này mặc nguyên đồng phục cảnh sát, đứng trong phòng khách căn hộ, và không biết cô vào bằng cách nào (C31). Rồi giữ giới hạn: tới lúc này đây vẫn là một cái tên trong danh sách, chưa phải một kết quả.
- **Claims:** C10, C12, C30, C31, C46.
- **Ranh giới:** C31 là lời thuật lại qua người thứ hai, quy cho cha Sherri. Chưa kể cuộc đối mặt ở nơi làm việc và câu "If I can't have John" (→ B08, D15 bản 2). Không nói điều tra viên đã đọc nhật ký (thu sau khi bắt, C13). Không nêu tên điều tra viên năm 2009 khi ledger chưa có. Không cấp bậc "Detective III" khi chưa có nguồn — chỉ nói "thám tử".

### B07 — Chiếc cốc bỏ đi
- **Chức năng:** mối nối khoa học đầu tiên tới một người có tên.
- **Ai biết gì:** điều tra viên thu chiếc cốc và ống hút Lazarus bỏ đi; phòng xét nghiệm có được hồ sơ một phần, khớp mẫu vết cắn ở 11 vị trí đọc được (C11). Cô chưa biết mình bị nhắm tới.
- **Câu hỏi đóng:** ADN của cô có khớp mẫu năm 1986 không? — Khớp, một phần.
- **Câu hỏi mở:** vì sao một nữ cảnh sát lại dính tới căn hộ ấy năm 1986 — giữa cô và Sherri đã có chuyện gì?
- **Người kể:** nói rõ "một phần" nghĩa là gì — chưa phải trọn hồ sơ, chưa phải chuẩn đưa ra toà.
- **Claims:** C11.
- **Ranh giới:** không "toàn bộ hồ sơ 15 vị trí". Không "Costco", không "probable cause" — ledger không có; kể hành động kế tiếp (B09) thay cho nhãn pháp lý. Không xác suất trùng ngẫu nhiên trừ khi S01 có số.

### B08 — Hai người phụ nữ và John: điều công tố dựng thành động cơ
- **Chức năng:** lớp con người và động cơ, gắn nhãn là lập luận của công tố.
- **Ai biết gì:** Lazarus và John quen từ thời đại học (C12). John khai rằng tháng 6/1985, khi anh báo tin đính hôn, cô vừa khóc vừa nói vẫn yêu anh (C33). Tại nơi Sherri làm việc, Lazarus bị cho là đã kể với Sherri chuyện gặp lại John sau khi anh bắt đầu hẹn hò Sherri, và nói câu "If I can't have John, you can't either" (C32, `alleged`).
- **Câu hỏi đóng:** công tố lập luận động cơ gì?
- **Câu hỏi mở:** động cơ chưa phải bằng chứng về hành vi. Khi đối mặt điều tra viên, cô sẽ nói gì?
- **Suy nghĩ/lời có nguồn:** kể được điều John khai về lời Lazarus nói với anh, kèm "John khai". Câu "If I can't have John" dịch sát nghĩa và giữ chữ "bị cho là" — phán quyết dùng "allegedly", và chuỗi người thuật lại chưa chốt (mục 11). Không kể Lazarus nghĩ gì ở beat này: nhật ký để B10.
- **Claims:** C12, C32, C33.
- **Ranh giới:** động cơ là lập luận công tố, không phải sự thật của người kể. Không đổ lỗi cho John hay Sherri. Chi tiết quan hệ thể xác giữa John và Lazarus tháng 6/1985 có trong S01; bước 5 chỉ dùng nếu thiếu nó lập luận động cơ không hiểu được, và không dùng để phán xét John. Không "si mê", "ám ảnh" bằng giọng người kể. B08 là beat riêng (D03 bản 2).

### B09 — Ngày 05/06/2009: cuộc phỏng vấn
- **Chức năng:** đối mặt; cô biết mình là nghi phạm; bị bắt.
- **Ai biết gì:** điều tra viên mời cô tới, nói cần chuyên môn của cô cho một vụ trộm tác phẩm nghệ thuật, rồi hỏi về John và Sherri (C16, C38). Cô nói hai người quen thời đại học; về Sherri, cô nói có thể đã tới hỏi chị chuyện John. Có lúc cô nói, đại ý: chúng tôi cãi nhau, rồi tôi đi giết chị ấy à, thôi nào (C38). Hỏi có cho mẫu ADN không, cô nói "có thể" và cần nói chuyện với luật sư. Cô được ra khỏi phòng rồi bị bắt, được đọc quyền Miranda và từ chối nói thêm (C17, C38). Sau đó có lệnh lấy mẫu niêm mạc miệng (C17).
- **Câu hỏi đóng:** khi bị đối mặt, cô nói gì?
- **Câu hỏi mở:** mẫu lấy trực tiếp có khớp, và có đứng vững trước bào chữa không?
- **Bối cảnh:** quyền Miranda — một câu.
- **Suy nghĩ/lời có nguồn:** chỉ những câu cô nói mà phán quyết trích lại. Không đoán cô nghĩ gì, không cử chỉ, không giọng điệu — chưa ai trong nhóm xem video phỏng vấn (A03 `missing`).
- **Claims:** C16, C17, C38.
- **Ranh giới:** không gọi là thú tội (C17). Kết quả 13 vị trí để B10 (D14 bản 2). **Không nối** câu "we had a fight" ở đây với chữ "fight" cô dùng ở phiên 2025 (B13): hai chữ nói về hai chuyện khác nhau, nối lại là tạo ra một mối liên hệ nguồn không có. Không dựng thoại ngoài các câu có trong S01.

### B10 — Tại toà: ADN và những chứng cứ khác
- **Chức năng:** kiểm chứng tới chuẩn đưa ra toà; trình bày cả công tố lẫn bào chữa.
- **Ai biết gì:** mẫu lấy trực tiếp khớp 13 vị trí (C17). Năm 2010, phòng xét nghiệm độc lập SERI xét ống mẫu thứ hai, có đại diện bào chữa có mặt: có amylase — dấu hiệu của nước bọt — và khớp 15 vị trí (C18). Nhật ký năm 1985 của Lazarus, thu sau khi bắt (C13, C34). Khẩu súng dự phòng cô báo mất trong xe ở Santa Monica ngày 09/03/1986, 13 ngày sau vụ án, không bao giờ thu hồi để đối chiếu (C14); bào chữa đưa hồ sơ cho thấy cùng ngày, cùng khu còn hai vụ trộm đồ trong ô tô (C48). Chuyên gia công tố liên hệ loại đạn với loại súng, chuyên gia bào chữa phản bác (C15). Dưới sáu móng tay khác của Sherri có lượng ADN rất nhỏ của cả nam lẫn nữ, một phần không khớp Sherri (C37).
- **Câu hỏi đóng:** kết quả ADN vững tới đâu khi bị phản biện? Chỉ đóng phần độ vững của ADN. Phong bì rách (C19) và ADN chưa xác định dưới móng tay (C37) **vẫn mở** (D09 bản 2).
- **Câu hỏi mở:** ADN đứng vững rồi, còn chồng đồ ở cửa gara — thứ mở đầu câu chuyện — thì tại toà được giải thích thế nào? (→ B11)
- **Nhánh:** NB2 nhánh 3 (lẫn mẫu) — kết quả SERI làm yếu nhánh này; người kể nói đúng chữ "làm yếu", không "bác bỏ".
- **Suy nghĩ/lời có nguồn:** nhật ký là chỗ duy nhất trước năm 2023 ghi điều Lazarus tự nói về cảm xúc của mình. Kể là điều cô viết năm 1985 ("cô viết trong nhật ký rằng…"), đặt đúng chỗ công tố đưa ra tại toà. Không suy từ nhật ký sang kế hoạch hay trạng thái năm 1986.
- **Claims:** C13, C14, C15, C17, C18, C19, C34, C37, C48.
- **Ranh giới:** không gọi súng là hung khí đã khớp (C14); đạn là chứng cứ tranh luận (C15). Nêu rõ đại diện bào chữa có mặt ở SERI. C18 không đóng C19, C37. Không "dàn dựng" (D11 bản 2). Vân tay trên chồng đồ để B11. Không tách B10 thành hai beat (D04 bản 2) — bản này đã chuyển phần vân tay sang B11 nên B10 nhẹ hơn bản 2.

### B11 — Hai cách đọc chồng đồ
- **Chức năng:** trả hook B01.
- **Ai biết gì:** chuyên gia của công tố khai rằng hiện trường đã được sắp đặt sau khi Sherri chết để trông như một vụ trộm, trong đó có chồng đồ gom mà không mang đi (C20, `alleged`). Bào chữa chỉ ra rằng trên chính chồng đồ ấy có dấu vân tay nhận dạng được mà không thuộc Lazarus, John hay Sherri (C37) — những dấu chưa bao giờ được xác định là của ai. Người kể gọi lại các dữ kiện `established` đã đặt từ trước: chồng đồ còn nguyên, các phòng khác không bị đụng (C03, C29), xe bị bỏ lại còn chìa (C05).
- **Câu hỏi đóng:** vì sao chồng đồ không bị mang đi? — Hai cách đọc tại toà, cả hai quy nguồn. Người kể không phân xử.
- **Câu hỏi mở:** bồi thẩm đoàn tin bên nào? (→ B12)
- **Người kể:** chỗ đáng để người kể có mặt — gợi lại hình ảnh đầu tập, và nói rõ đây là hai cách đọc chứ chưa phải lời giải cuối cùng.
- **Claims:** C03, C05, C20, C29, C37.
- **Ranh giới:** "dàn dựng" luôn quy cho chuyên gia công tố, không nói bằng giọng người kể. Không nói vân tay là của "kẻ trộm thật" — chưa xác định. Không nêu tên Safarik khi ledger chưa có (C20 ghi "chuyên gia công tố").

### B12 — Bản án
- **Chức năng:** kết quả pháp lý và các cấp xét lại.
- **Ai biết gì:** năm 2012, bồi thẩm đoàn kết luận Lazarus phạm tội first degree murder và xác nhận cô trực tiếp dùng súng; toà tuyên 25 năm tới chung thân, cộng 2 năm vì dùng súng — tổng 27 năm tới chung thân (C21, C39). Ngày 13/07/2015, toà phúc thẩm bang giữ nguyên bản án (C21), dù bào chữa lập luận rằng việc không điều tra cô năm 1986 và truy tố chậm đã làm cô bất lợi — người thư ký từng chứng kiến cuộc đối mặt giữa Sherri và Lazarus đã qua đời (C47). Ngày 05/09/2023, toà phúc thẩm liên bang giữ nguyên việc bác yêu cầu habeas (C22). Suốt thời gian đó cô vẫn nói mình vô tội (C41).
- **Câu hỏi đóng:** kết quả là gì? Và — ở mức nguồn cho phép — vì sao hướng gia đình nêu không được theo từ năm 1986.
- **Câu hỏi mở:** bản án có phải điểm cuối không?
- **Bối cảnh:** bồi thẩm đoàn; first degree murder; án "tới chung thân" không định sẵn ngày ra tù; habeas; toà liên bang khu vực 9.
- **Người kể:** đóng NB1 — hướng gia đình nêu đã đúng về người. Về câu hỏi "vì sao không được theo": hồ sơ chỉ cho biết đây là điểm tranh luận tại toà, và nhiều phần chứng cứ về nó do chính bên Lazarus đưa ra khi kháng cáo (C30, C47); toà liên bang phân tích cả trong giả định cáo buộc là đúng và không xác nhận có bao che (C22). Nói đúng tới đó.
- **Claims:** C07, C21, C22, C30, C39, C41, C47.
- **Ranh giới:** mốc thời gian: vụ án 1986 → bắt năm 2009 khoảng 23 năm → kết án năm 2012 khoảng 26 năm; không gộp hai mốc (D10). Không bao che có tổ chức (C22). Không "giết người cấp độ một". Chưa kể lời nhận tội năm 2023.

### B13 — Lời nhận tội, và điều nó không khớp
- **Chức năng:** chặng thứ tư. Đóng câu hỏi "ai" bằng lời chính người bị kết án; để chứng cứ ADN soi vào lời kể của cô.
- **Ai biết gì:** tháng 11/2023, tại phiên xét tha, Lazarus thừa nhận đã giết Sherri (C41). Một ủy viên đề xuất cho cô tha có điều kiện, viện dẫn một đạo luật về người phạm tội khi còn trẻ — lúc gây án cô gần 26 tuổi (C40). Tháng 4/2024 Thống đốc Newsom yêu cầu toàn hội đồng xem lại; ngày 02/10/2024 đề xuất bị rút lại (C23, C40). Ngày 12/02/2025, ở phiên tiếp theo, cô lại thừa nhận, nói đã mang theo một sợi dây, nói khi ấy mình giận dữ tột độ, và xin lỗi. Ủy viên Kevin Chappell kết luận cô chưa đủ điều kiện: lời kể của cô không khớp chứng cứ đã dùng để kết án — nếu đó là một cuộc "đánh nhau" như cô tả, hiện trường phải có nhiều ADN của cô hơn là chỉ ở vết cắn (C24, C42).
- **Câu hỏi đóng:** bản án có phải điểm cuối không; vì sao đã có phiên xét tha trước mốc 27 năm; và, theo lời chính cô, ai đã giết Sherri.
- **Câu hỏi mở:** lời nhận tội có trả lời hết chuyện đã xảy ra trong căn hộ không? (→ B14)
- **Bối cảnh:** tha có điều kiện; hội đồng xét tha; vai trò thống đốc — chỉ ở mức nguồn nói.
- **Người kể:** nối lại mẫu vết cắn — thứ đã nối cô với vụ án năm 2009 — giờ lại là thứ ủy viên dùng để cân lời kể của cô năm 2025. Skill ưu tiên nhấn đúng loại chỗ này: chứng cứ pháp y soi vào mâu thuẫn trong lời người bị kết án. Nhưng quy nguồn rõ: đây là lập luận của một ủy viên hội đồng xét tha, không phải kết quả giám định mới hay phán quyết của toà.
- **Suy nghĩ/lời có nguồn:** kể được điều cô nói về mình tại phiên xét tha ("cô nói khi ấy mình…"), vì đó là lời cô tự kể và báo chí có ghi lại. Luôn đặt ngay cạnh nhận định của ủy viên. Không kể lời ấy như diễn biến đã xác lập.
- **Claims:** C23, C24, C40, C41, C42.
- **Ranh giới:** không nói cô đã hoặc sắp được thả. Không suy ra vì sao cô đổi lời sau 14 năm; nhận xét của thống đốc là ý kiến của ông, dùng thì quy nguồn. Không nối chữ "fight" năm 2025 với câu trong phỏng vấn năm 2009 (C38). Không số phát súng, không vết thương. Chi tiết sợi dây chỉ giữ khi cần để hiểu vì sao lời kể "đánh nhau" không đứng được, và là lời cô khai. Không dùng lỗi "leg" và năm ADN của S05. Không dùng các chi tiết về lời khai 2023 chỉ thấy ở bài tổng hợp (Lazarus nghe Sherri nhấc máy, định trói Sherri) cho tới khi có nguồn gốc.

### B14 — Hôm nay, và những gì còn lại
- **Chức năng:** trạng thái hiện tại; trả lời câu hỏi mở đầu tới mức chứng cứ cho phép; nối các chi tiết còn treo; hệ quả với con người; CTA.
- **Ai biết gì:** lịch của hội đồng xét tha (dữ liệu ngày 16/09/2026) có phiên xét lại Lazarus **ngày 9 tháng 10 năm 2026** (C25, C44). Nguồn không nói vì sao phiên được xếp trước mốc ba năm, và kết quả chưa có.
- **Trả lời câu hỏi trung tâm — không kể lại cả tập:** lời giải trộm không dẫn tới người đã giết Sherri, vì theo bản án và theo chính lời cô từ năm 2023, đó là người Sherri biết — người gia đình chị nêu với điều tra viên từ những ngày đầu. Thứ nối được là mẫu nước bọt giữ từ năm 1986, qua bốn chặng. Mẫu ấy tự nó không nêu tên ai: phải có xét nghiệm năm 2005, danh sách năm 2009 và kiểm chứng tại toà (C26 — nhận xét biên tập, không phải phán quyết về cả LAPD).
- **Đóng nhánh và câu hỏi còn treo, nói thẳng phần để ngỏ:** vân tay trên chồng đồ và ADN dưới móng tay chưa xác định là của ai (C37); không có giờ tử vong chắc chắn (C02, timeline); lời kể của chính Lazarus về diễn biến bị ủy viên cho là không khớp chứng cứ (C42) — nên chuyện gì đã xảy ra trong căn hộ chỉ được trả lời một phần.
- **Hệ quả với con người:** Sherri mất năm 29 tuổi, ba tháng sau đám cưới (C01). Gia đình chị nêu đúng một cái tên với điều tra viên chỉ ít lâu sau vụ án (C30); khoảng 23 năm sau người ấy mới bị bắt. Teresa Lane, chị em gái của Sherri, nói tại phiên năm 2025 rằng bà chưa bao giờ được nói lời từ biệt (C43).
- **Suy ngẫm:** không có đoạn nêu cơ chế hành vi — xem mục 7. Kết ở hệ quả với con người.
- **CTA:** tối đa một câu, sau tất cả những phần trên; có thể bỏ.
- **Claims:** C01, C02, C25, C26, C30, C37, C42, C43, C44.
- **Ranh giới:** ngày điều trần viết bằng chữ (D16). Tập xuất bản sau ngày 9/10/2026 thì kiểm kết quả phiên và sửa beat này trước khi thu âm. Không kể lại cả tập. Không lên lớp.

---

## 6. Bảng manh mối

| Manh mối | Xuất hiện | Người nghe hiểu lúc đó | Chứng cứ thật nói gì | Giải ở đâu | Trả lời câu hỏi nào |
| --- | --- | --- | --- | --- | --- |
| Chồng dàn âm thanh cạnh cửa gara, không bị mang đi | B01 | Kẻ trộm bỏ dở? | C03, C29 `established`. "Dàn dựng" là lời chuyên gia công tố (C20 `alleged`); trên chồng đồ có vân tay chưa xác định (C37) | B11 hai cách đọc; B14 phần để ngỏ | Vì sao lời giải trộm không khớp |
| BMW bỏ lại còn chìa, không bị tháo gì | B04 | Kẻ trộm lấy xe để chạy? | C05 `established` | B11 gọi lại | như trên |
| Vết cắn, mẫu nước bọt trong tủ đông | B03 | Một mẫu chưa dùng tới | C04, C36 `established` | B05, B07, B10, B13 | Mẫu 1986 nối với ai; lời kể 2025 có khớp không |
| Gia đình nêu bạn gái cũ của John; lời đe doạ | B04 | Một hướng khác bị gạt | C07, C30 — lời đã nói với điều tra viên; đe doạ là lời thuật lại | B06 đúng người; B12 gọi lại | Vì sao hướng ấy không được theo |
| Người phụ nữ mặc đồng phục trong phòng khách | B06 | Chi tiết cũ giờ đổi nghĩa: người được nêu là cảnh sát | C31 `alleged` — lời cha Sherri thuật lại | Ngay B06 | Người được nêu là ai |
| Cơ sở dữ liệu không ra ai | B05 | Biết giới tính, chưa có tên | C09, C35 | B06: danh sách những người có liên hệ | Từ "một phụ nữ" tới "người này" |
| Cốc và ống hút bỏ đi | B07 | Mối nối sinh học đầu tiên; khớp một phần 11 vị trí | C11 `established`; chưa phải chuẩn ra toà | B10: 13 và 15 vị trí | Mẫu nối với người nào |
| Nhật ký năm 1985 | B10 | Cô viết mình căng thẳng vì John | C13, C34 — thu sau khi bắt | Ngay B10 | Công tố dựng động cơ thế nào |
| Súng dự phòng báo mất 13 ngày sau vụ án | B10 | Trùng hợp đáng ngờ | C14; bào chữa: cùng ngày có hai vụ trộm xe khác (C48); không phải hung khí đã khớp | Ngay B10, kèm phản biện | Chứng cứ vật chất mạnh tới đâu |
| Phong bì rách; ADN và vân tay chưa xác định | B05 nêu, B10–B11 dùng | Mẫu có thể bị lẫn? Có người khác? | C19, C37 `established`; chưa xác định | SERI làm yếu nhánh lẫn mẫu (B10); phần vân tay và ADN lạ **không đóng** — nói ở B14 | Mẫu có đứng vững không |
| Chữ "fight" năm 2009 và năm 2025 | — | **Không phải manh mối.** Không nối | C38, C42 nói về hai chuyện khác nhau | — | — |

## 7. Đoạn kết và suy ngẫm — ranh giới riêng của vụ này

`giong-ke.md` cho thêm một đoạn suy ngẫm ngắn với ba điều kiện. Kiểm từng điều:

1. **Cơ chế phải truy được về dữ kiện đã xác lập, đúng mức chắc chắn.** Động cơ là lập luận của công tố (C12, C32 `alleged`), cộng lời tự kể của Lazarus mà ủy viên cho là không khớp chứng cứ (C42). Không đủ để nói vụ án "cho thấy" một cơ chế như ghen tuông hay tự hợp lý hoá. Việc hướng gia đình nêu không được theo năm 1986 là điểm tranh luận, không phải kết luận của toà (C22, C30, C47) — cũng không dùng làm cơ chế được.
2. Không ngụ ý nạn nhân đáng bị như vậy.
3. Không lên lớp người nghe.

**Kết luận:** điều kiện 1 không đạt. Theo skill, bỏ đoạn nêu cơ chế, kết ở hệ quả với con người (B14).

| | Ví dụ ranh giới |
| --- | --- |
| **Được** | "Sherri mất khi 29 tuổi, ba tháng sau đám cưới. Gia đình chị nêu đúng một cái tên với cảnh sát chỉ ít lâu sau đó, và phải hơn hai mươi năm sau người ấy mới bị bắt." — hệ quả, không bài học |
| **Không được** | "Ghen tuông mù quáng thì phải trả giá." — lên lớp, và biến lập luận của công tố thành điều vụ án chứng minh |
| **Không được** | "Giá như John dứt khoát hơn…" — đổ lỗi cho người trong cuộc |
| **Không được** | "Cả một sở cảnh sát đã che chắn cho người của mình." — C22 không xác lập |

## 8. Chi tiết cố ý không dùng

| Chi tiết | Nguồn | Vì sao không dùng |
| --- | --- | --- |
| Hai tuần trước khi chết, Sherri hẹn gặp một người để giải quyết "a serious problem" | C45 (S01, lời cha Sherri) | Mở một câu hỏi — gặp ai? — mà hồ sơ tập này không trả lời được, và dễ bị nghe thành ám chỉ. Luật: câu hỏi treo phải trả lời được |
| John và Lazarus gặp lại năm 1989 | S01 | Sau vụ án, không phục vụ câu hỏi trung tâm, dễ thành phán xét John |
| Vụ kiện dân sự của gia đình (2010) và của Jennifer Francis (S06) | Wikipedia; S06 | Cáo buộc dân sự chưa phân tích (dossier) |
| Tên đường, số nhà | S01 | Không cần cho câu chuyện |
| Cửa kính trượt vỡ, mảnh kính trên lối xe | S01 | C03 yêu cầu tách khỏi dấu vào nhà; kể mà không giải thích được đúng mức nguồn thì gây nhiễu. Bước 5 chỉ dùng nếu giải thích được |
| Người giúp việc nghe tiếng như hai người đánh nhau khoảng 12:30 | S01, chứng cứ bào chữa; chưa có claim | Tuỳ chọn. Nếu dùng thì thêm claim trước, quy nguồn, không biến thành giờ tử vong, và đặt ở B14 cạnh "không có giờ tử vong chắc chắn" |
| Chi tiết lời khai năm 2023 (nghe Sherri nhấc máy, định trói) | Wikipedia | Chưa có nguồn gốc trong ledger |
| Số phát súng, vết thương | S11 | Không cần để hiểu kết luận nào |
| Tên Safarik, Stearns, Jaramillo | các bản kịch bản cũ | Chưa có claim; nói bằng vai trò |

## 9. Claim bổ sung ngày 18/09/2026

Bản 3 cần những dữ kiện mà ledger bước 3 chưa có. Tôi thêm C27–C48 vào `claims.csv`, S11–S13 vào `sources.csv`, và các mốc tương ứng vào `timeline.md`. Mọi dòng mới đều ghi `confidence: medium` và "chưa đối chiếu nguyên văn".

| Nhóm | Claim | Nguồn |
| --- | --- | --- |
| Hiện trường và giả thuyết ban đầu | C27, C28, C29, C36 | S01 qua bản FindLaw (S13) |
| Lời báo của gia đình năm 1986 | C30, C31, C45 | S01 / S13 |
| Quan hệ, nhật ký, động cơ | C32, C33, C34 | S01 / S13 |
| Xét nghiệm 2003–2005 | C35 | S01 / S13 |
| Chứng cứ bào chữa | C37, C47, C48 | S01 / S13 |
| Phỏng vấn 2009 | C38 | S01 / S13 |
| Bản án | C39 | S01 / S13 |
| Nghề của Lazarus | C46 | S01 đoạn mở; S12 |
| Xét tha 2023–2026 | C40, C41, C42, C43, C44 | S05, S11, S12, S07 |

Đổi `script_segment` ở ba dòng cũ: C25 B13 → B14; C19 thêm B14; C03 thêm B11.

Các điểm này làm thay đổi bốn điểm đang mở ở luồng `net-0006-ban-tieng-viet` (luồng đó vẫn của Codex và Gemini, tôi không đóng hộ): D02 (Van Nuys, Glendale — nay có C27), D03 (Lazarus là cảnh sát năm 1986 — C31, C46), D06 ("cơ sở dữ liệu toàn quốc" — C35), D07 (Sherri "bị đe doạ" — C30, quy cho lời cha Sherri).

## 10. Kiểm tra khung này

Theo `STORYTELLING.md` mục 7, `kien-truc-cau-chuyen.md` và danh sách kiểm ở `thi-truong-viet-nam.md`, trong phạm vi bước 4:

- Hook có một câu hỏi cụ thể, có nguồn? — Có (C03, C29).
- Cảnh mở có được trả lời? — B11 bằng hai cách đọc có quy nguồn; phần vân tay nói rõ còn để ngỏ ở B14.
- Người nghe biết đang theo ai và người đó muốn gì? — Mỗi beat ghi người theo dõi trong "Ai biết gì".
- Manh mối đặt trước khi dùng để kết luận? — Mục 3 và mục 6.
- Có chỗ nào gọi sai bản chất để tạo bất ngờ? — Không. Đã bỏ "trộm nam", điều từng làm cú lật năm 2005 có vẻ mạnh hơn nguồn cho phép.
- Nhánh giả thuyết nào mở cũng được đóng hoặc nói rõ để ngỏ? — Mục 4, cột "Đóng ở".
- Thuật ngữ tư pháp nước ngoài giải thích bằng chức năng? — Bảng ở mục 2. Hai định nghĩa chưa có nguồn: mục 11.
- Ngày theo ngày/tháng/năm; đơn vị đổi mà không làm tròn sai? — 2,5 dặm → khoảng 4 ki-lô-mét.
- Xưng hô ghi rõ là mặc định tạm? — Mục 2.
- Không gọi người chưa bị kết án là "hắn", "ả"? — Lazarus đã bị kết án; khung vẫn buộc gọi trung tính.
- CTA một câu, sau phần kết? — B14.

## 11. Tôi đã không kiểm cái gì

- **Không đọc được nguyên văn S01.** Justia trả 403 ngày 18/09/2026; PDF S08 vẫn bị chặn. Tôi đọc bản FindLaw (S13) qua công cụ đọc web, mà công cụ này trả lời qua một mô hình tóm lược. Kể cả những câu nó trả về là "nguyên văn" cũng cần người đối chiếu với văn bản thật trước bước 5. Mọi claim C27–C39, C45–C48 mang giới hạn này.
- **Bản FindLaw hình như không có chú thích.** Tra "envelope", "staged", "six weeks" không ra, trong khi C06, C19, C20 dẫn đúng những chú thích hay đoạn đó. Tôi không suy ra ba claim này sai — chỉ là lượt này chưa kiểm lại được.
- **Chuỗi thuật lại câu "If I can't have John" (C32):** hai lần đọc cho hai câu trả lời khác nhau — cha Sherri kể với thám tử, hoặc Sherri kể với John ngay tối hôm đó. Phải chốt trước bước 5.
- **Lời nhận tội năm 2023 (C41) mới có một nguồn báo (S05)** cho mốc 2023; S11 là nguồn cho phiên 2025. S11 ghi byline "Contributing Editor", chưa xác định hãng tin gốc.
- **C46 ("a 25-year veteran")** tôi thấy ở đoạn mở S01 qua kết quả tìm kiếm, chưa đọc tận nơi.
- **Chưa có nguồn cho hai định nghĩa:** first degree murder theo luật California, và cơ chế án "25 năm tới chung thân" với hội đồng xét tha. Bảng thuật ngữ chỉ ghi cách gọi, bước 3 cần thêm nguồn luật hoặc bước 5 nói ở mức chung nhất.
- **Chưa biết Teresa Lane là chị hay em của Sherri** — tiếng Việt buộc phải chọn.
- **Không xem video phỏng vấn năm 2009** (A03 `missing`).
- **Chưa thử khung này bằng một bản viết bước 5.** Chưa biết hai điểm mở nhánh có làm đoạn B04, B05 quá dài không, hay câu hỏi treo "vì sao không theo hướng gia đình" có giữ được qua sáu beat không.
- **Không tải file nào.**

## 12. Cần Tú quyết

1. **Phiên xét tha ngày 9/10/2026 cách hôm nay ba tuần.** Đăng tập trước ngày đó — B14 nói "sắp có phiên" và kết quả chưa biết — hay đợi kết quả rồi chốt B14?
2. **Xưng hô "mình — các bạn"** vẫn là mặc định tạm. Tú chốt thì ghi vào `channel.narrator_voice` theo quy trình sửa sổ.
