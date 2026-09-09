# r1 · Đề xuất khung sườn NET-0006 (tác giả: Claude)

Sản phẩm đang đề xuất: `t-i/outputs/YouTube-Research-System/episodes/NET-0006-sherri-rasmussen/scripts/01-beat-sheet.md`, `artifact_version: 1`.

Đây là bước 4 chạy **sau khi** bước 5 đã có hai bản kịch bản tiếng Việt (`02-script-vi.md` của Codex, `02-script-vi-gemini.md` của Gemini). Cả hai bản đã dùng cấu trúc B01–B14, và `claims.csv` đã có cột `script_segment` map C01–C26 vào B01–B14. Khung này **hình thức hóa** bộ xương đó thành một tài liệu review được: chức năng từng beat, ai-biết-gì, câu hỏi đóng/mở, mã claim, ranh giới. Nó không viết câu văn — đó là bước 5.

## Tôi đã quyết gì và vì sao

1. **Giữ nguyên đánh số B01–B14 và bản đồ claim của `claims.csv`.** Đổi số beat lúc này sẽ phá map `script_segment` trong ledger bước 3 (ngoài phạm vi của tôi) và làm hai bản kịch bản đang tồn tại lệch khỏi khung. Khung bám đúng cột `script_segment`, kể cả ở chỗ tôi thấy hơi gò (xem D dưới).

2. **Ba chặng của câu hỏi trung tâm phải tách bạch, không dồn:** (a) 2005 biết mẫu chính là nữ, CODIS không khớp; (b) 2009 xác định người cụ thể; (c) 2009–2012 kiểm chứng đủ để ra tòa. Góc kể trong dossier nói rõ "hai lần thay đổi cần tách". B05 và B06 là hai beat riêng, cách nhau bốn năm và hai nguyên nhân khác nhau — khung ghi rõ điều này ở mục 1 và trong từng beat.

3. **Hook = một vật chứng cần giải thích (STORYTELLING.md §2 lựa chọn 3):** chồng thiết bị âm thanh gom cạnh cửa gara mà không mang đi (C03). Cho biết chi tiết tồn tại ở B01; giữ lời giải "dàn dựng" tới B11. Tôi chọn C03 làm hook thay vì BMW (C05) vì `claims.csv` map C03→B01 (C05→B04 B11), và vì "một vụ trộm mà đồ vẫn còn" là đúng cái nghịch lý mà câu hỏi trung tâm nói tới. Bản Codex mở bằng C03, bản Gemini mở bằng C05 — hai bản không thống nhất, nên tôi coi đây là điểm cần review (D01).

4. **Thang tiết lộ thành bảng bắt buộc (mục 3 của khung).** Mỗi dòng: khán giả được biết gì ở beat nào, và điều gì **không** được lộ trước đó. Twist duy nhất — mẫu là của nữ, rồi là của một nữ cảnh sát — đến theo đúng thứ tự vụ án thật phát hiện. Không beat nào được "gọi sai bản chất để tạo bất ngờ".

5. **Ba claim `alleged`/`inference` bị khoanh riêng và buộc quy nguồn:** C20 (hiện trường dàn dựng — diễn giải chuyên gia công tố, không phải camera tái dựng) chỉ được nói ở B11 với quy nguồn; C22 (habeas 2023 — tòa *giả định* cáo buộc, **không** xác nhận cover-up) khoanh ở B12; C26 (bài học đọc chứng cứ) gắn nhãn nhận xét biên tập ở B14, không phải phán quyết về cả LAPD.

6. **C13 (nhật ký + thư gửi mẹ John) chỉ đặt ở B10, không ở B08.** `claims.csv` map C13→B10. Conflict note của C13: "Không nói điều tra viên đã đọc trước phỏng vấn." Nhật ký thu **sau** khi bắt. Đặt nó ở beat động cơ B08 (trước phỏng vấn B09) sẽ ngầm nói nó có sớm hơn thực tế. Nên B08 chỉ dựa C12 (lời khai về quan hệ và lần gặp ở bệnh viện).

7. **Ghi chú "cho bước 5" tại B09 và B11, không sửa kịch bản.** Bản Gemini B09 có thoại nguyên văn và mô tả "nghẹt thở" không có trong hồ sơ; B11 viết "Điều đó chứng minh một sự thật lạnh người" — biến C20 `alleged` thành sự thật của người kể. Khung đặt rào ở đúng hai beat đó. Sửa câu chữ là việc bước 5; tôi không đụng vào artifact của bước khác (AGENTS.md mục 8).

## Chỗ tôi tự thấy yếu nhất

- **B01 hook C03 vs C05.** Tôi chọn theo ledger, nhưng cold open bằng BMW bỏ lại ngoài đường (bản Gemini) tạo chuyển động và tò mò về "chủ xe là ai" mạnh hơn một mô tả tĩnh chồng đồ. Nếu người review thấy BMW mạnh hơn thì cần một ghi chú thêm C05→B01 trong ledger. → D01
- **B04 lộ nghi phạm là sĩ quan LAPD.** Tôi để "sĩ quan tuần tra LAPD năm 1986" ở B04 (mức thông tin biết được từ 1986), giữ tên và cấp bậc hiện tại cho B06. Có thể lập luận điều này lộ nút thắt quá sớm. → D02
- **B08 — beat động cơ.** Rủi ro cố hữu: mọi beat động cơ dễ trôi sang tâm lý không nguồn. Khung đặt rào ("mọi khẳng định cảm xúc quy về tài liệu/lời khai hoặc cắt"), nhưng rào trong khung có đủ không, hay B08 nên gộp vào B06 để bớt một mặt phẳng dễ vi phạm? → D03
- **B10 nặng — 6 claim, cả công tố lẫn bào chữa.** Tôi lập luận mỗi mục trả lời một phản biện riêng (nhiễm bẩn / súng / vân tay lạ / 15 loci), nhưng nó có nguy cơ thành danh sách. → D04
- **B11 trả hook chỉ bằng C20 (`alleged`).** Toàn bộ lời giải cho hình ảnh mở đầu tựa vào một diễn giải chuyên gia còn tranh luận. Tôi cho rằng quy nguồn là đủ và trung thực, nhưng đây là điểm cấu trúc mềm nhất. → D05
- **Locator chưa tự truy ngược.** Tôi không đọc toàn văn S01 (PDF S08 bị chặn; chỉ có `S01-excerpt.md` một blockquote + `claims.csv`). Bản đồ claim→beat tin vào ledger bước 3. → D06

## Câu hỏi tôi muốn người review trả lời

- **Q1 (Codex — tác giả ledger):** Giữ C13 hoàn toàn ở B10 và để B08 chỉ dựa C12 — có đúng tinh thần conflict note của C13 không, hay C13 cũng chính đáng thuộc B06/B08?
- **Q2:** Hook C03 (chồng đồ) hay C05 (BMW)? Nếu chọn BMW, có nên thêm ghi chú C05→B01 vào `claims.csv` không?
- **Q3:** "Người gia đình nêu tên là một sĩ quan tuần tra LAPD" — chấp nhận ở B04, hay mọi tiết lộ liên quan LAPD phải đợi tới B06?
- **Q4 (Gemini — kiểm chứng chéo):** B11 trả hook chỉ bằng C20 (`alleged`). Quy nguồn "chuyên gia công tố khai" đã đủ, hay hook cần một phần trả lời có chứng cứ `established` sớm hơn để không tựa hết vào diễn giải tranh luận?
- **Q5:** B10 nên tách B10a (xác minh DNA: C17/C18/C19) và B10b (chứng cứ khác: C13/C14/C15) không, hay một beat với các câu hỏi con là đủ?

## Cái tôi cố ý chưa làm vì thuộc bước sau

- **Câu chữ, nhịp câu, mọi wording** — bước 5. Khung chỉ cho chức năng + claim + ranh giới.
- **Ước lượng thời lượng** — sau bản prose (luật kênh: không số phút cố định).
- **Chọn tiêu đề** — có hai phương án đang tồn tại; không phải quyết định của khung sườn.
- **Kế hoạch hình ảnh theo cảnh** — việc của Gemini, tách riêng.
- **Bản tiếng Anh thu âm** — bước 6, chỉ sau khi Tú duyệt bản tiếng Việt.
- **Hòa giải hai bản kịch bản tiếng Việt đang tồn tại** — việc của bước 5. Khung là bộ xương chung cả hai phải quy về; chỗ chúng lệch (thoại bịa B09, khẳng định `alleged` thành sự thật B11 ở bản Gemini) tôi ghi làm "ghi chú cho bước 5", không sửa.

## Tôi đã không kiểm cái gì

- **Không đọc trực tiếp toàn văn phán quyết S01.** Chỉ có `sources/S01-excerpt.md` (một blockquote nguyên văn về hồ sơ chính là nữ) và `claims.csv`. PDF gốc S08 bị chặn (lỗi TLS, rồi trang thử thách JavaScript khi thử ngoài sandbox) — dossier ghi rõ, tôi không vượt chặn. Do đó **không tự truy ngược từng locator**: chưa xác minh S01 pp7–8 note 13 có đỡ "11 vị trí đọc được" (C11), S01 pp67–69 có đỡ diễn giải hiện trường dàn dựng của Safarik (C20), S01 pp10–12 có đỡ mức độ mô tả lần gặp ở bệnh viện (C12). Bản đồ claim→beat tin vào ledger bước 3.
- **Không kiểm chéo tên điều tra viên** (Stearns, Jaramillo, Francis, Mahaney, Safarik) ngoài những gì dossier và bản Gemini đã dùng; `claims.csv` không ghi hết tên riêng ở cột claim.
- **Không kiểm lại lịch parole S07 hôm nay.** Dossier ghi kiểm 2026-09-08/09, dòng WE4479 = 09/10/2026 08:30. Nếu bước 5 chạy trễ cần kiểm lại — công cụ web trong lượt này tôi không dùng để xác minh.
- **Không chạy `python scripts/thread.py check`** hay bất kỳ script coordination nào — lượt này là lượt tác giả viết nội dung, không phải lượt cập nhật sổ; orchestrator lo phần đó.

```points
D01 | mở | scripts/01-beat-sheet.md:58 | B01 hook: chọn C03 (chồng đồ) theo ledger; bản Gemini mở bằng C05 (BMW) — hai bản kịch bản không thống nhất
D02 | mở | scripts/01-beat-sheet.md:85 | B04 lộ nghi phạm gia đình nêu tên là sĩ quan tuần tra LAPD 1986 — có sớm quá trên thang tiết lộ không
D03 | mở | scripts/01-beat-sheet.md:121 | B08 beat động cơ: giữ riêng hay gộp vào B06; rào chống tâm lý không nguồn trong khung có đủ không
D04 | mở | scripts/01-beat-sheet.md:139 | B10 chứa 6 claim cả công tố lẫn bào chữa — có nên tách B10a (DNA) / B10b (chứng cứ khác) không
D05 | mở | scripts/01-beat-sheet.md:150 | B11 trả hook mở đầu chỉ bằng C20 (status alleged) — quy nguồn có đủ, hay cần phần trả lời established sớm hơn
D06 | mở | scripts/01-beat-sheet.md:208 | Locator C01–C26 chưa tự truy ngược S01 toàn văn (PDF bị chặn); bản đồ claim→beat tin vào ledger bước 3
```
