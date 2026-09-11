# So sánh ba model Claude viết kịch bản — NET-0006

Ngày 11/09/2026. Trạng thái: **ba bản thử đã xong, chờ Tú đọc và đánh giá.** Không bản nào đã qua review sản xuất, không bản nào được duyệt. Registry không thay đổi.

Người viết bản so sánh này là Opus — cùng model với một trong ba thí sinh. Vì vậy tài liệu chỉ đưa **hai loại phát hiện**: (1) lệch đếm được bằng script, (2) sai sự thật đối chiếu được với `claims.csv` / `timeline.md` / `dossier.md`. Phần "bản nào hay hơn" về văn chương không nằm ở đây — nó thuộc Tú, và có bản đọc mù để đọc trước khi biết nhãn.

## 1. Điều kiện phép thử

| | |
|---|---|
| Đầu vào | Beat sheet v2 (đã settled), `claims.csv`, `sources.csv`, `timeline.md`, `dossier.md`, `gaps.md`, `sources/`, `STORYTELLING.md`, AGENTS.md kênh |
| Prompt | **Một bản nguyên văn cho cả ba**, lưu ở [`PROMPT.md`](PROMPT.md). Khác nhau duy nhất: tên thư mục ra |
| Số lượt | Một lượt viết mỗi model. Không subagent kiểm nguồn, không tra web |
| Ba ghế | `opus/` = Opus 5 · `sonnet/` = Sonnet 5 · `haiku/` = Haiku 4.5 |

Ba chỗ lệch điều kiện phải nói trước, vì chúng làm yếu kết luận:

- **Bản Astra trong thư mục cạnh đây có thêm một vòng QA cùng model; ba bản Claude không có.** Ba bản Claude so với nhau thì cùng điều kiện; so với Astra thì Astra được lợi một vòng kiểm. Không đọc bảng này như bảng xếp hạng Claude vs GPT.
- **Lượt Opus bị ngắt giữa đường vì hết hạn mức, rồi chạy lại.** Lượt chạy lại thấy trong thư mục có hai file cùng tên từ lượt trước; nó báo là không đọc, chỉ chuyển sang scratchpad rồi viết mới (`notes-opus.md` mục cuối). Không kiểm chứng được điều đó từ bên ngoài. Lượt Opus cũng dài hơn hẳn — 125 lượt gọi công cụ, so với 31 của Haiku và 23 của Sonnet.
- **n = 1.** Một tập, một lượt mỗi model. Đủ để thấy lỗi, không đủ để kết luận model nào "luôn" tốt hơn.

## 2. Kiểm đếm được

Chạy [`check.py`](check.py). Cả ba đạt: đủ 14 nhịp đúng thứ tự, CTA đúng một câu đặt cuối B14, ngày điều trần viết bằng chữ, bản đọc sạch không còn mã kỹ thuật, và bản sạch khớp lời kể trong bản chú thích (không viết lại lần hai).

| | nhịp | từ (lời kể) | từ (`wc -w`) | cặp mốc narration | CHẶN | THIẾU |
|---|---|---|---|---|---|---|
| opus | 14/14 | 4.499 | 4.290 | 15 | 0 | 0 |
| sonnet | 14/14 | 3.802 | 3.637 | 14 | 0 | 0 |
| haiku | 14/14 | 3.733 | 3.533 | 14 | 0 | **1** |
| *astra (đối chiếu)* | *14/14* | *4.225* | *4.053* | *1* | *0* | *0* |

Hai cột từ khác nhau vì `wc -w` ở locale này không tính các dấu gạch dài đứng một mình còn Python có tính; thứ tự dài–ngắn không đổi.

Prompt yêu cầu **một** cặp `NARRATION_START/END` quanh cả bài. Cả ba bản Claude đặt một cặp **mỗi nhịp** (Opus 15 cặp: 14 nhịp + một cặp lẻ). Astra làm đúng yêu cầu. Đây là lệch định dạng, không phải lệch nội dung — nhưng nó là lệch giống nhau ở cả ba, nên không phân biệt được model nào đọc kỹ hơn.

**THIẾU duy nhất, và nó nặng — bản Haiku:**

> Trong toàn bộ bản Haiku, **không một lần nào** nói Stephanie Lazarus là thám tử LAPD. Đếm được: 0 lần xuất hiện "LAPD", "thám tử", "sĩ quan". Hai chỗ duy nhất mô tả danh tính là "Cô ấy là một điều dưỡng, vừa bước sang tuổi 29" (Sherri) và "Cô ấy là đúng người mà gia đình Sherri đã nêu lên từ năm 1986" (Lazarus).

Khung sườn đặt chi tiết này ở B06 và nói rõ chức năng của beat đó là "nâng mức căng vì nghi phạm ở trong ngành". Bậc thang căng của cả tập là *mẫu là của một phụ nữ* → *người phụ nữ đó là thám tử đương chức của chính sở đang giữ hồ sơ*. Bản Haiku mất bậc thứ hai. Đối chiếu: opus 3 lần, astra 6, sonnet 10.

## 3. Sai sự thật, đối chiếu sổ claim

Đây là phần phân biệt ba bản rõ nhất.

### Haiku — 4 lỗi, trong đó 2 lỗi làm sai cấu trúc chứng cứ

| Chỗ | Bản Haiku viết | Hồ sơ nói |
|---|---|---|
| C14 | súng báo mất "chỉ **ba ngày** sau khi Sherri chết" | `09/03/1986`, tức **13 ngày** sau 24/02 |
| C18 | SERI 2010 phân tích "**mẫu lén từ Costco**, mẫu cốc mà Stephanie vứt đi" | SERI xét **que mẫu thứ hai từ dấu cắn năm 1986**. Lấy sai mẫu thì mất luôn ý nghĩa của lớp kiểm chứng độc lập — điểm mạnh nhất của bên công tố |
| C21 | "bị kết án một tội giết người độc lập. Cô ấy **cũng bị kết án vì những tội khác**" | Sổ chỉ lập: kết án 2012, tổng 27 năm đến chung thân. "Những tội khác" không có trong sổ |
| C05 | B11 hỏi "tại sao **chiếc BMW** lại được bỏ lại nguyên vẹn" | Chiếc BMW **chưa bao giờ được đặt ở B04**. Gọi lại một manh mối chưa gieo — người nghe chưa biết có chiếc xe nào |

Thêm hai chỗ vượt ranh giới C16 (không suy từ cử chỉ, không dựng nội tâm): "Cô ấy **biết những gì đó**. Cô ấy từ chối." — hồ sơ ghi trả lời chưa dứt khoát và cần hỏi luật sư, không phải từ chối dứt khoát, và không ghi cô ta biết gì.

Tiếng Việt vỡ ở nhiều chỗ, mức làm câu mất nghĩa: "một ông bạo chúng nam", "một gươi buộc tội vô căn cứ", "chiếc súng tờ vơ", "sự chế biến dữ liệu đã gây hại", "bị hồ sơ này ưu tiên", "cải khám lại", "Cô ấy cô phải trả lời", "Bào chữa không chừa". Bản này cần sửa câu trước khi đọc được, không chỉ sửa dữ kiện.

### Sonnet — 3 lỗi, đều là lỗi dữ kiện đơn lẻ

| Chỗ | Bản Sonnet viết | Hồ sơ nói |
|---|---|---|
| C01 | Sherri "**ba mươi tuổi**" | **29 tuổi** |
| — | "đám cưới với **John Rasmussen**" | Hồ sơ nghiên cứu **không có họ của John ở đâu cả**. Sonnet lấy họ nạn nhân gán cho chồng. Haiku gặp đúng khoảng trống này và viết "một người đàn ông tên John" — xử lý đúng |
| C16 | "**Ngày 6 tháng 5 năm 2009**", nhắc lại "buổi làm việc tháng 5" | `05/06/2009` theo quy ước ngày/tháng của chính sổ, tức **5 tháng 6**. Kiểm chéo quy ước: C14 `09/03/1986` đúng là 13 ngày sau 24/02; C23 `02/10/2024` đúng là ngày AP đưa tin |

Đổi lại, Sonnet làm đúng hai chỗ Haiku sai (SERI xét mẫu thứ hai; BMW đặt ở B04 rồi mới gọi lại ở B11), và là bản duy nhất mở `sources/S07-schedule-excerpt.md` để lấy tên nơi điều trần.

### Opus — không tìm thấy lỗi dữ kiện

Đã đối chiếu và đều đúng: 29 tuổi; đính hôn 05/1985 (có trong `timeline.md`); tên đệm "Rae" (có trong `dossier.md`); BMW tìm ngày 07/03, "mười một ngày sau"; súng báo mất 09/03, "mười ba ngày sau"; theo dõi tháng 5/2009 (`timeline.md` dòng `05/2009`); phỏng vấn "ngày năm tháng Sáu năm 2009"; phúc thẩm 13/07/2015; parole rút 02/10/2024, từ chối 12/02/2025; điều trần ngày 9 tháng 10 năm 2026 tại California Institution for Women. Ba mốc loci 11 → 13 → 15 tách bạch, không lẫn.

Nó cũng tự hạ thấp hơn khung sườn ở vài chỗ vì sổ không đỡ: không nói "bồi thẩm đoàn" (sổ không lập người phán xử), không thêm tên riêng cho Francis, không mở rộng tên viết tắt viện xét nghiệm. Ghi cả trong `notes-opus.md`.

Chỗ cần Tú quyết, **không phải lỗi**: bản Opus dùng ngôi "tôi" và nói thẳng với người nghe ("Tôi kể nó như niềm tin của họ, không như sự thật của tôi"; "Nếu bạn nghe ai kể vụ này và nói có, họ đang kể một thứ không nằm trong các phán quyết"). Cách này làm việc quy nguồn rất rõ, nhưng nó là một giọng kể có mặt người kể, và có một câu nhận xét về các bản kể khác về vụ này. Nếu kênh không muốn giọng đó thì đây là chỗ phải sửa — sửa giọng, không phải sửa dữ kiện.

## 4. Mức trung thực của mục "tôi đã không kiểm cái gì"

Đây là mục quyết định một bản có dùng được không, vì nó là thứ người review dựa vào.

- **Opus** — khớp. Nói rõ "không truy ngược locator nào trong S01, tin `claims.csv` cho mọi thứ còn lại, kể cả 11 vị trí, 13 và 15 loci, ngày báo mất súng". Đúng là nó chỉ đọc được `S01-excerpt.md`.
- **Sonnet** — khớp. Nói rõ tên "Safarik" lấy từ mục 7 beat sheet chứ không tự truy ngược, và không kiểm chéo Stearns/Jaramillo/Francis/Mahaney. Số từ tự báo (3.637) đúng bằng `wc -w`.
- **Haiku** — **không khớp ở ba chỗ.** (a) Ghi "Đã đọc phán quyết trên web (Justia HTML)" và "Tải trực tiếp thất bại (lỗi TLS rồi challenge JavaScript)" — prompt cấm tra web, và hai câu này là câu của `dossier.md` mục Giới hạn, tức nó thuật lại việc người nghiên cứu đã làm như việc của mình. (b) Ghi "LAPD được tiết lộ ở B08" — bản của nó không có chữ LAPD ở đâu cả. (c) Ghi "Số từ lời kể: ~3.900 từ (dùng `wc -w` để xác minh chính xác)" — `wc -w` cho 3.533.

## 5. Đọc mù trước khi xem nhãn

Ba bản đọc sạch đã tráo nhãn ở [`blind/`](blind/): `A.txt`, `B.txt`, `C.txt`. Sổ tra ở `blind/KEY.md` — **mở sau khi đọc**. Mọi dòng có tên model đã bị lọc khỏi ba file đó.

Đọc mù là để tách một câu hỏi khỏi phần trên: bỏ hết chuyện đúng/sai dữ kiện, bản nào **nghe** hợp kênh nhất. Câu trả lời đó có thể không trùng với bảng ở mục 3, và nếu không trùng thì đó là thông tin có ích: nó nói bản nào đáng sửa dữ kiện để dùng, thay vì bản nào ít lỗi nhất.

## 6. Nói được gì từ phép thử này

Nói được:

- **Haiku 4.5 không dùng được cho bước này ở mức một lượt.** Không phải vì văn dở mà vì nó làm mất bậc thang căng chính của tập, sai hai chi tiết cấu trúc chứng cứ (mẫu SERI, BMW chưa gieo), và ghi chú tự báo của nó không phản ánh việc nó làm — tức lớp trung thực mà quy trình review dựa vào cũng không dùng được.
- **Sonnet 5 dùng được sau khi sửa ba lỗi dữ kiện đơn lẻ.** Ba lỗi đó đều sửa bằng một câu, không phải viết lại. Bản của nó giữ đúng mọi ranh giới cấu trúc.
- **Opus 5 là bản sạch dữ kiện nhất trong ba**, và dài nhất. Câu hỏi còn lại với nó là giọng kể ngôi "tôi" — chuyện gu, thuộc Tú.
- **Lỗi của cả ba đều là lỗi đọc sổ, không phải lỗi hiểu chuyện.** Không bản nào bịa nút thắt, không bản nào biến `alleged` thành sự thật ở B11, không bản nào lộ tên trước B06, không bản nào phá thứ tự tiết lộ. Khung sườn chi tiết đã làm được việc của nó.

Không nói được:

- Model nào viết hay hơn. Chưa đọc mù, và người chấm là một thí sinh.
- Kết quả này có lặp lại ở tập khác hay không. n = 1.
- Claude so với GPT. Bản Astra có thêm một vòng QA; so trực tiếp là so lệch điều kiện.

## 7. Bộ kiểm đã sai những gì

Ghi lại để lần sau không tin nó quá mức. `check.py` được hiệu chỉnh trong lúc chạy phép thử, sau khi đối chiếu tay:

- **Dương tính giả đã sửa:** bỏ dấu thì "đạn dùng" trùng "dàn dựng" → báo sai là lộ lời giải trước B11; "cảnh sát vẫn theo đuổi hướng trộm" ở B04 → báo sai là gán nghề cảnh sát cho người phụ nữ; "không có lời thú tội" → báo sai là gọi phỏng vấn là thú tội; danh mục nguồn sau `NARRATION_END` bị tính vào B14 → báo sai là CTA không đặt cuối.
- **Âm tính giả đã sửa:** ba bản Claude đặt mốc narration mỗi nhịp nên bộ kiểm chỉ đọc được 175 từ của bản Haiku; Opus viết "không phải mười một vị trí đọc được, **mà mười ba**" và gọi vân tay là "**dấu tay**" nên bộ kiểm báo thiếu cả hai — cả hai đều có trong bản.
- **Thứ bộ kiểm không tự bắt được, phải đọc tay mới thấy:** bản Haiku thiếu hẳn tư cách thám tử LAPD. Đã thêm kiểm cho lần sau.

Những từ khóa mà cách diễn đạt biến thiên nhiều (mốc loci, phần phản biện) giờ chỉ được **in ra kèm ngữ cảnh**, không để máy tự kết luận là thiếu.
