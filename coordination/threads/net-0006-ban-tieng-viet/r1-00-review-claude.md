# r1 · claude · review — net-0006-ban-tieng-viet

Sản phẩm: `t-i/outputs/YouTube-Research-System/episodes/NET-0006-sherri-rasmussen/scripts/02-script-vi.md` (v1, tác giả codex, bàn giao qua PR #1 / commit d329477).

Không có vòng trước. Bảng "Điểm tranh luận" trong THREAD.md trống, không có phản bác nào để xử.

## Trả lời câu hỏi của luồng

**"Các mã C01–C26 và S01–S07 có tra được vào một claim ledger thật không?"**
Có, ở mức sổ. Trái với dòng ghi ngoài lượt ngày 2026-09-09 trong THREAD.md, thư mục tập **đã có** `claims.csv` (C01–C26 đủ), `sources.csv` (S01–S10), `sources/S01-excerpt.md` và `sources/S07-schedule-excerpt.md`. Mỗi beat B01–B14 có dòng *Đối chiếu* trỏ tới mã C, mỗi mã C trỏ tới source_id kèm locator trang. S06 không xuất hiện trong kịch bản — đó là chủ ý, ghi rõ ở `gaps.md` dòng 13 và `dossier.md` dòng 20 (vụ dân sự Francis 2022, loại khỏi narration). Không phải lỗi.

**"Mỗi nút thắt của kịch bản có nguồn trực tiếp đó không?"**
Chỉ trả lời được một nửa, và nửa trả lời được thì có lỗ. (a) Không kiểm được *nội dung* nguồn: S01 gánh ~24/26 claim nhưng `sources/S01-excerpt.md` chỉ lưu **đúng một câu** nguyên văn ("The DNA that comprised the major profile was from a female."). Toàn văn phán quyết không nằm trong repo (PDF bị chặn tải — `dossier.md` dòng 22, S08). S02–S05 là `link_only`, không có trích đoạn lưu. Nên với C01–C08, C10–C22 tôi chỉ đối chiếu được tính nhất quán nội bộ (kịch bản ↔ claims.csv ↔ timeline.md ↔ dossier.md ↔ gaps.md), không xác nhận được nguồn có nói đúng như claim. Xem D01. (b) Có những chi tiết trong lời đọc **không gắn mã C nào** — vị trí bệnh viện, khu nhà, trang phục, tên điều tra viên và chuyên gia, và chính cú lật trung tâm "Lazarus là cảnh sát". Xem D02, D03, D04.

**"Có chỗ nào suy diễn được trình bày như sự thật không?"**
Kịch bản hedge rất dày, phần lớn đạt. Ba chỗ còn vấn đề: một trình tự tối-hôm-đó dựng lại như sự thật (D05), hai chỗ nói cụ thể hơn nguồn được viện (D06), và một chi tiết "đe dọa" vượt mã C được viện (D07).

---

## D01 — Không xác nhận được nguồn nói đúng như claim

**CHO NAO** `sources/S01-excerpt.md` toàn file; `claims.csv` cột `source_ids` (24/26 dòng là S01); `sources.csv` dòng S02–S05 (`download_status` = `link_only` / `saved_excerpt`).

**VAN DE GI** Câu hỏi trung tâm của luồng này là nguồn. Nhưng repo chỉ có một câu nguyên văn của S01. Các locator kiểu "pp10–12", "note13", "pp42–43" không kiểm được vì không có văn bản để mở tới trang đó. Reviewer đứng sau không thể phân biệt "claim đọc đúng phán quyết" với "claim nhớ nhầm/diễn giải rộng". Đây đúng là loại lỗi mà luật review chặn: khi lời kể dựa trên tường thuật của một văn bản mà không ai trong luồng kiểm được văn bản đó, thì phần lớn kịch bản đang ở trạng thái "trình bày như đã đối chiếu" mà chưa đối chiếu.

**CAN GI DE DONG** Một trong hai:
- Tác giả lưu trích đoạn nguyên văn (`saved_excerpt`) vào `sources/` cho các beat gánh nặng nhất — tối thiểu các claim C01–C05, C08–C09, C11–C18, C21–C22 — đủ để reviewer đọc thẳng câu nguồn cạnh câu kịch bản; hoặc
- Đẩy lên Tú quyết rằng với tập này, "locator trang + link_only" là mức đối chiếu chấp nhận được, và cả ba reviewer ký nhận là chỉ review được ở mức nhất quán nội bộ. Nếu chọn hướng này thì phải ghi vào THREAD.md, không để ngầm.

## D02 — B02: chi tiết hiện trường và nhân thân không gắn mã C

**CHO NAO** `scripts/02-script-vi.md:23` ("một bệnh viện ở Glendale, California"), `:25` ("căn nhà thuộc khu chung cư ở Van Nuys, phía bắc Los Angeles"), `:27` ("Sherri gọi báo nghỉ ốm"), `:33` ("Cánh cửa nối gara với căn nhà, vốn được John đóng và khóa lúc đi làm, giờ hé mở"), `:35` ("vẫn mặc đồ ngủ và áo choàng"). Dòng *Đối chiếu* ở `:43` chỉ viện C01–C02.

**VAN DE GI** C01 = "điều dưỡng 29 tuổi; cưới John 11/1985". C02 = ba mốc giờ ngày 24/02/1986. Không mã nào chứa: tên thành phố bệnh viện, tên khu dân cư, việc Sherri *gọi điện* báo ốm (khác với "ở nhà"), hành động John khóa cửa lúc đi làm, hay trang phục của Sherri khi được tìm thấy. Đây là các khẳng định sự thật cụ thể, đứng trong lời đọc, không có nguồn tra được. "John đóng và khóa lúc đi làm" đặc biệt đáng chú ý: nó là lời khai của John, cần được đánh dấu là lời khai.

**CAN GI DE DONG** Với từng chi tiết: hoặc thêm một dòng claim vào `claims.csv` (S01 hoặc S02) kèm locator, hoặc hạ mức cụ thể xuống đúng cái C01–C02 đỡ được — bỏ "Glendale", bỏ "Van Nuys, phía bắc Los Angeles", bỏ "đồ ngủ và áo choàng"; đổi "gọi báo nghỉ ốm" thành "ở nhà, không đi làm" nếu không có nguồn cho cuộc gọi; quy "khóa cửa" về lời khai John với một mã C.

## D03 — B06: cú lật trung tâm "Lazarus là cảnh sát năm 1986" không được mã C viện dẫn đỡ

**CHO NAO** `scripts/02-script-vi.md:131` ("Lazarus là người của LAPD."), `:133` ("Năm Sherri qua đời, cô đã là cảnh sát."). Dòng *Đối chiếu* ở `:137` viện C10, C12.

**VAN DE GI** Đây là điểm xoay của cả tập — lý do vụ án đáng kể. Nhưng C10 = "2009 xem xét phụ nữ liên quan", C12 = quan hệ Lazarus–John và lần gặp ở bệnh viện. Không mã nào nói Lazarus là cảnh sát tuyên thệ của LAPD vào tháng 2/1986. C14 ("súng dự phòng… báo mất 09/03/1986") *gợi* điều đó nhưng bản thân claim C14 cũng không viết ra, và B06 không viện C14. Nút thắt lớn nhất của kịch bản đang dựa trên một dữ kiện không câu nào trong ledger khẳng định.

**CAN GI DE DONG** Thêm một claim từ S01 nói rõ Lazarus là cảnh sát/điều tra viên LAPD tại thời điểm Sherri qua đời (locator), và đưa mã đó vào dòng *Đối chiếu* của B06; hoặc tối thiểu viện C14 và sửa C14 cho nói rõ "mua súng dự phòng khi đã là cảnh sát, trước 1986".

## D04 — Tên người cụ thể không có trong ledger

**CHO NAO** `scripts/02-script-vi.md:181` ("Gregory Stearns và Dan Jaramillo"), `:217` ("Thomas Fedor"), `:249` ("Mark Safarik").

**VAN DE GI** Ba dòng *Đối chiếu* liên quan (`:207` C16–C17, `:241` C13–C15/C17–C19, `:263` C03/C05/C20) không chứa tên nào trong số này. Tên một điều tra viên hay một nhân chứng chuyên gia là khẳng định sự thật — hoặc có nguồn, hoặc không nên đứng trong lời đọc dưới dạng đích danh.

**CAN GI DE DONG** Thêm mã C cho từng tên kèm locator S01, hoặc bỏ tên và giữ mô tả vai trò ("hai điều tra viên", "một phòng thí nghiệm độc lập", "chuyên gia phân tích hiện trường của phía công tố").

## D05 — B08: trình tự "tối hôm ấy" dựng lại như sự thật

**CHO NAO** `scripts/02-script-vi.md:167–169` ("Rồi Lazarus tới nơi Sherri làm việc. Hồ sơ tòa ghi nhận một cuộc đối mặt tại bệnh viện. Tối hôm ấy, Sherri trở về trong tâm trạng không vui. John thừa nhận với cô chuyện đã xảy ra…").

**VAN DE GI** Đoạn này buộc ba việc vào cùng một tối: Lazarus đối mặt Sherri ở bệnh viện → Sherri về nhà buồn → John thú nhận. Nếu S01 không xếp ba việc trong một buổi tối thì đây là tái dựng trình tự trình bày như sự thật — đúng loại "lời giải/trình tự tiết lộ" mà luật review chặn. C12 chỉ được mô tả trong ledger là "lời khai về quan hệ và lần gặp tại bệnh viện", không nói về mốc thời gian khớp trong ngày.

**CAN GI DE DONG** Trích locator S01 cho thấy phán quyết đặt ba việc trong cùng buổi tối; hoặc tách ra và bỏ "Tối hôm ấy" — "Về sau John thừa nhận với Sherri…", không ràng buộc thời điểm.

## D06 — Hai chỗ nói cụ thể hơn mã C được viện

**CHO NAO** `scripts/02-script-vi.md:105` ("hệ thống cơ sở dữ liệu quốc gia") — B05, viện C09. `scripts/02-script-vi.md:267` ("giết người cấp độ một") — B12, viện C21.

**VAN DE GI** C09 chỉ ghi "database không khớp", không nói quốc gia/CODIS. C21 ghi "Kết án 2012; tổng 27 năm đến chung thân", không ghi cấp độ tội. Cả hai bổ ngữ ("quốc gia", "cấp độ một") có thể đúng với hồ sơ thực, nhưng đang vượt claim được viện — người sau không biết bổ ngữ này lấy từ đâu.

**CAN GI DE DONG** Thêm "quốc gia/CODIS" vào C09 và "cấp độ một" vào C21 kèm locator; hoặc bỏ hai bổ ngữ, để "một hệ thống cơ sở dữ liệu" và "phạm tội giết người".

## D07 — B04: chi tiết "đe dọa" vượt mã C, và nghịch với chính guardrail của B08

**CHO NAO** `scripts/02-script-vi.md:79` ("Cha cô còn thuật lại việc Sherri từng bị người cũ của chồng đe dọa."). Dòng *Đối chiếu* `:87` viện C05–C07.

**VAN DE GI** C07 = "Gia đình/John nêu người cũ; hồ sơ tranh luận về bỏ sót hướng điều tra" — không nói tới một lời khai của cha Sherri về việc bị *đe dọa*. Guardrail của chính B08 (`:177`) ghi "Không dựng lời đe dọa trực tiếp… vượt quá nội dung đã có". B04 đang đưa một lời đe dọa vào — qua lời cha, có gán nguồn ("Cha cô còn thuật lại"), nhưng nguồn đó không kiểm được và không có mã C.

**CAN GI DE DONG** Trích locator S01 cho lời khai của cha Sherri về việc đe dọa (nếu có), thêm mã C; hoặc cắt chi tiết đe dọa, giữ "Cha mẹ Sherri đề nghị điều tra viên kiểm tra người đó".

---

## Tôi đã không kiểm cái gì

- **Nội dung phán quyết S01.** Repo chỉ lưu một câu nguyên văn (`sources/S01-excerpt.md`). Toàn văn không có trong repo, PDF bị chặn tải (S08, `dossier.md:22`). Tôi **không** đối chiếu được C01–C08, C10–C22 với văn bản nguồn — chỉ kiểm tính nhất quán giữa kịch bản, `claims.csv`, `timeline.md`, `dossier.md`, `gaps.md`. Đây là gốc của D01.
- **S02, S03, S04, S05 (link_only).** Không mở URL, không thực hiện web fetch (chế độ tự động chỉ đọc file; nguồn là `link_only`). Các mốc C21–C22 (S03), C23 (S04), C24 (S05) chỉ được đối chiếu với `claims.csv`/`timeline.md`, không với nguồn sống.
- **S07:** trích đoạn có lưu (`sources/S07-schedule-excerpt.md`), tôi có kiểm — dòng WE4479 ghi `10/09/2026` (MM/DD) = 9/10/2026, khớp câu "ngày chín tháng Mười năm 2026" ở B13. Không kiểm lịch sống, không kiểm múi giờ (bản thân excerpt cũng ghi chưa kiểm múi giờ).
- **Các claim kỹ thuật DNA/đạn đạo:** 11/13/15 loci, "Model 49", amylase/"chất chỉ dấu trong nước bọt" — chỉ đối chiếu với `claims.csv`, không với nguồn.
- **Thứ trong tuần:** "thứ Hai, 24/02/1986" — tự tính tay, ra thứ Hai, khớp. Không kiểm bằng công cụ.
- **Rủi ro quảng cáo/pháp lý:** S09/S10 là `link_only`, không kiểm lại chính sách YouTube. Kịch bản có vẻ chủ động tiết chế mô tả thương tích, nhưng tôi không thẩm định sâu.
- **Không đọc** `02-script-vi-gemini.md`, `02b-narration-vi-review.txt`, `comparison-chatgpt-vs-gemini.md` — ngoài phạm vi lượt này (review bản v1 của codex).
- Không công cụ nào bị chặn; tôi không dùng WebFetch/WebSearch do ràng buộc chỉ-đọc của chế độ tự động và do nguồn đều `link_only`.

```points
D01 | mở | sources/S01-excerpt.md + claims.csv:2-27 | Nguồn không kiểm được nội dung — S01 gánh 24/26 claim, chỉ 1 câu nguyên văn được lưu
D02 | mở | scripts/02-script-vi.md:23-35 | B02: Glendale, Van Nuys, đồ ngủ, gọi báo ốm, John khóa cửa — không mã C nào đỡ
D03 | mở | scripts/02-script-vi.md:131-133 | Cú lật trung tâm "Lazarus là cảnh sát 1986" không được C10/C12 viện dẫn đỡ
D04 | mở | scripts/02-script-vi.md:181,217,249 | Tên Stearns/Jaramillo/Fedor/Safarik không có trong ledger
D05 | mở | scripts/02-script-vi.md:167-169 | B08: trình tự "tối hôm ấy" (đối mặt → về buồn → John thú nhận) dựng như sự thật
D06 | mở | scripts/02-script-vi.md:105,267 | "cơ sở dữ liệu quốc gia" và "giết người cấp độ một" nói cụ thể hơn C09/C21
D07 | mở | scripts/02-script-vi.md:79 | B04: chi tiết Sherri "bị đe dọa" vượt C07 và nghịch guardrail của B08
```
