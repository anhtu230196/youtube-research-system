# r1 · Đề xuất khung sườn mới NET-0006 (tác giả: Claude)

Sản phẩm: `t-i/outputs/YouTube-Research-System/episodes/NET-0006-sherri-rasmussen/scripts/01-beat-sheet.md`, `artifact_version: 1`.

Ngày 18/09/2026 Tú yêu cầu bỏ hẳn khung cũ và viết một khung mới từ đầu theo skill `ky-an-viet` mới nhất. Khung này không kế thừa cấu trúc, đánh số hay các quyết định của những bản trước; nó chỉ dựa trên ledger bước 3 và skill. Luồng `net-0006-khung-suon-v3` bị thay thế (đã ghi ngoài lượt ở đó), và các điểm đã chốt ở luồng `net-0006-khung-suon` không ràng buộc khung này.

Đi kèm khung là phần sửa ledger: C27–C52 trong `claims.csv` (C49–C52 mới thêm; C31, C32, C46 được sửa), S11–S13 trong `sources.csv`, và `timeline.md`. Cột `script_segment` của cả 52 claim được đổi sang mã cảnh K01–K18.

## Tôi đã quyết gì và vì sao

1. **Hình dạng câu chuyện: hai sợi dây hội tụ.** Sợi dây người là lời báo của John và gia đình Sherri năm 1986 (C30). Sợi dây vật là que bông từ vết cắn, nằm trong tủ đông (C04, C36). Mỗi sợi một mình không đi tới đâu: lời báo chỉ là lời báo, còn năm 2005 que bông chỉ cho biết đó là một phụ nữ. Năm 2009 hai sợi gặp nhau ở chiếc cốc (C11, C52). Kết thúc là một lời kể bị tranh cãi: năm 2023 Lazarus nhận tội, và năm 2025 que bông được dùng để cân lời kể của cô (C41, C42). Hình dạng này có sẵn trong `kien-truc-cau-chuyen.md` ("hai cuộc điều tra hội tụ"). Nó cũng khớp câu hỏi trung tâm trong `dossier.md`.

2. **Mở đầu bằng que bông trong tủ đông, chọn trong ba phương án viết thử** (mục 2 của khung): que bông, ngày bình thường của John, và chồng dàn âm thanh. Câu hỏi của que bông được trả lời trọn và nhiều lần (2005, 2009, 2010, 2025), và câu chuyện khép lại ở đúng vật đã mở nó. Câu hỏi của hai phương án kia chỉ được trả lời một phần. Chất liệu của chúng không mất: thành K03 và K04.

3. **Kể theo thứ tự điều tra viên biết, không theo thứ tự sự việc xảy ra.** Chuyện giữa Lazarus, John và Sherri năm 1984–1985 được kể vào năm 2009 (K08–K09), lúc thám tử Nuttal nghe nó. Đọc lại S01 cho thấy Nuttal được giao hồ sơ năm 2009, và cha Sherri kể với ông hai lần Sherri đối mặt Lazarus (C31, C32). Đặt hai chuyện ấy vào năm 1986 là sai mốc. Tôi đã mắc đúng lỗi này ở timeline trong lượt trước, và đã sửa.

4. **Hai cú lật đến đúng lúc điều tra viên biết:** một phụ nữ (K07), rồi người đó là cảnh sát (K09). Nghề của cô được lộ qua lời cha Sherri về lần Sherri thấy cô mặc đồng phục đứng trong phòng khách — một lời báo cũ mang thêm nghĩa mới. Khung không nói điều tra viên năm 1986 biết cô là cảnh sát, vì nguồn không nói vậy (G3).

5. **Mỗi cảnh ghi điểm nhìn và điều người đó muốn biết** (`STORYTELLING.md` mục 3). Có hai chi tiết đời thường được đặt sớm để dùng lại, theo mục "một chi tiết làm hai việc": nơi Sherri làm việc (K02 → K09) và tháng đính hôn (K02 → K08).

6. **Hai điểm mở nhánh, mỗi điểm có chủ và có chỗ đóng** (mục 6 của khung). NH1 ở K05: kẻ lạ (điều tra viên, nhánh bình thường) hay người Sherri quen (gia đình). NH2 ở K07: phụ nữ lạ, phụ nữ Sherri quen, hay mẫu bị lẫn (nhánh bình thường). Không mở nhánh "sắp đặt cho giống vụ trộm" từ năm 1986, vì trong hồ sơ cách đọc đó chỉ đến từ chuyên gia công tố tại toà (C20 `alleged`).

7. **Lời và suy nghĩ của nhân vật chỉ được kể ở chỗ nguồn có ghi:** lời John (K08), lời cha Sherri (K05, K09), các câu Lazarus nói trong phỏng vấn mà phán quyết trích lại (K11), nhật ký năm 1985 (K13), và lời cô tự kể ở phiên xét tha (K16–K17, luôn đặt cạnh nhận định của ủy viên).

8. **Phản biện của bào chữa đứng ngay cạnh chứng cứ nó phản biện.** Vân tay lạ trên chính chồng đồ ở cảnh mở (K14, C37). ADN dưới móng tay (K12). Hai vụ trộm ô tô cùng ngày Lazarus báo mất súng (K13, C48). Tranh cãi về đạn (K13). Phong bì rách (K06, K12).

9. **Đoạn kết không có phần suy ngẫm về cơ chế.** Động cơ chỉ là lập luận của công tố cộng lời tự kể bị bác, nên không đạt điều kiện 1 của `giong-ke.md`. Kết ở hệ quả với con người.

10. **Câu hỏi "vì sao lời báo năm 1986 không được theo"** — người nghe chắc chắn sẽ hỏi ở K09. Khung trả lời ở K15, chỉ tới mức nguồn cho phép: đó là điểm tranh luận tại toà, và nhiều chứng cứ về nó do chính bên Lazarus đưa ra khi kháng cáo (C30, C47). Toà liên bang không xác nhận có bao che (C22).

## Chỗ tôi tự thấy yếu nhất

- **D01 — Ledger do tác giả bước 4 tự thêm, đọc qua công cụ trích web.** Justia trả 403, PDF vẫn bị chặn. Bản FindLaw hình như thiếu chú thích, và công cụ đọc trả lời qua một mô hình tóm lược. C32 hai lần đọc ra hai câu trả lời khác nhau. C41 (nhận tội năm 2023) mới có một nguồn báo.
- **D02 — Chọn que bông làm mở đầu.** Câu đầu tiên chưa có con người. Người nghe Việt quen với mở đầu bằng một ngày bình thường bị cắt ngang (phương án B). Tôi chọn A vì câu hỏi của nó được trả lời trọn, nhưng đó là phán đoán biên tập.
- **D03 — Lazarus xuất hiện muộn.** Tên cô chỉ lộ ở K08, gần giữa tập. Cái giá của việc kể theo thứ tự điều tra viên biết là nửa đầu tập không có nhân vật đối trọng rõ. Chỉ có "người bạn gái cũ" ở K05 giữ chỗ đó.
- **D04 — Không mở nhánh "sắp đặt" ở K05.** Có thể lập luận ngược lại: người nghe tự nghĩ tới ngay ở K04, và người kể nêu nó như một khả năng thì không vi phạm gì.
- **D05 — K17 đặt sức nặng lên nhận định của một ủy viên xét tha, qua báo thuật lại** (S11, hãng tin gốc chưa rõ). Đã buộc quy nguồn, nhưng chọn nó làm điểm khép vòng đã là một quyết định biên tập.
- **D06 — K02 mỏng.** Về con người Sherri, ledger chỉ có tuổi, nghề và các mốc hôn nhân (G1). Skill đòi nhân hoá nạn nhân bằng chi tiết có nguồn và có chức năng. Bước 5 viết từ khung này thì K02 sẽ yếu, trừ khi bước 3 bổ sung.
- **D07 — Mười tám cảnh.** Có thể dài. Những chỗ có thể gộp nếu cần: K06 với K07, K12 với K13.

## Câu hỏi tôi muốn người review trả lời

- **Q1 (Codex — tác giả ledger):** C27–C52 có đỡ được nội dung khung gắn vào không? Nhờ kiểm nguyên văn C31 và C32 (ai kể với ai, năm nào), C37, C38, C47, C49, C52. Nếu Codex muốn tách phần sửa ledger thành luồng bước 3 riêng, tôi không phản đối.
- **Q2 (Gemini — kiểm chứng chéo):** C40–C44 có nguồn thứ hai độc lập không, nhất là lời nhận tội năm 2023 và lập luận ADN của ủy viên Chappell?
- **Q3:** Mở đầu A có mạnh hơn B thật không, xét theo `mo-dau.md` — người nghe có nói được mình đang tò mò điều gì không?
- **Q4:** NH1 và NH2 có đạt từng điều của mục "Mở nhánh giả thuyết" không?
- **Q5:** Mục 4 (người nghe biết gì, khi nào) có chỗ nào để người nghe biết trước điều lẽ ra phải khám phá sau không?

## Cái tôi cố ý chưa làm vì thuộc bước sau

- **Lời kể** — bước 5. Ngoại lệ là ba phương án mở đầu viết thử, vì `STORYTELLING.md` mục 2 yêu cầu có chúng ở bản dàn ý.
- **Các bản `02-script-vi*.md` hiện có** được viết theo khung cũ, dùng mã B. Bước 5 phải viết lại từ khung này, không vá. Luồng `net-0006-ban-tieng-viet` vẫn mở ở lượt Gemini; việc đóng nó thuộc luồng ấy.
- **Hình ảnh, tiêu đề, thumbnail, cách đọc tên cho TTS** — bước 6.
- **`dossier.md`** (dòng "Khán giả Mỹ" đã cũ) và **`registry.json`** (lý do `awaiting_review` đã cũ) — không đụng tới. Đổi sổ là commit riêng và cần Tú quyết hướng đi của tập.

## Tôi đã không kiểm cái gì

- Nguyên văn S01 và các chú thích của nó (xem D01).
- Lời nhận tội năm 2023 ngoài S05; hãng tin gốc của S11.
- Nguồn luật cho các thuật ngữ ở G7.
- Teresa Lane là chị hay em của Sherri.
- Video phỏng vấn năm 2009.
- Chưa thử khung bằng một bản viết bước 5.
- Không tải file nào.

```points
D01 | mở | scripts/01-beat-sheet.md:386 | C27–C52 do tác giả bước 4 thêm, đọc qua công cụ trích web; C32 chưa chốt chuỗi thuật lại; C41 một nguồn
D02 | mở | scripts/01-beat-sheet.md:47 | Chọn mở đầu A (que bông) thay vì B (ngày của John) — câu đầu chưa có con người
D03 | mở | scripts/01-beat-sheet.md:29 | Kể theo thứ tự điều tra viên biết khiến Lazarus chỉ có tên ở K08, gần giữa tập
D04 | mở | scripts/01-beat-sheet.md:307 | Không mở nhánh "sắp đặt cho giống vụ trộm" ở K05 — có dè dặt quá không
D05 | mở | scripts/01-beat-sheet.md:274 | K17 khép vòng bằng nhận định của một ủy viên xét tha qua báo thuật lại (S11)
D06 | mở | scripts/01-beat-sheet.md:130 | K02 mỏng vì ledger thiếu chi tiết đời thật có nguồn về Sherri (G1)
D07 | mở | scripts/01-beat-sheet.md:115 | Mười tám cảnh — có nên gộp K06+K07, K12+K13
```
