---
name: ky-an-viet
description: Làm kỳ án tiếng Việt cho khán giả Việt Nam — chọn vụ, nghiên cứu, khung sườn, lời kể tự nhiên, bản thu âm và đóng gói. Dùng khi làm một tập, review kịch bản hoặc sửa lời kể bị cứng, văn dịch, giống báo cáo; giữ dữ kiện, mức chắc chắn và quy trình chống trùng của kênh. Kỳ án, mất tích, true crime, TTS tiếng Việt.
---

# Kỳ án tiếng Việt

Kênh kể các vụ án và bí ẩn có thật cho khán giả Việt Nam, lời kể tiếng Việt. Tú chốt hướng này ngày 2026-09-14, thay cho quyết định 2026-09-08 (khán giả Mỹ, lời kể tiếng Anh).

Skill này dùng chung cho Codex, Claude Code và Gemini. Nó kế thừa phần nghiên cứu, kiến trúc câu chuyện và các bất biến biên tập của `mystery-case-script` (bản đã chỉnh ngày 2026-09-08), nhưng đổi đích đến: bản tiếng Việt là sản phẩm cuối, không còn bước viết lời kể tiếng Anh.

**Không dùng `mystery-case-script` cho kênh này nữa.** Skill đó — dù nằm ở `~/.codex/skills/` hay là plugin của Claude — được viết để ra lời kể tiếng Anh cho khán giả Mỹ, và sẽ kéo bài viết về sai đích.

## Thứ tự ưu tiên

Chỉ dẫn mới nhất của Tú → `t-i/outputs/YouTube-Research-System/AGENTS.md` (luật nghiệp vụ, quyết định nội dung) → `AGENTS.md` ở gốc repo (quy trình nhiều agent) → skill này. Skill nói *làm thế nào*; nó không nới luật nào ở hai file kia.

Trước mọi việc của kênh, đọc `README.md`, `registry.json` và — với việc chạm tới cách kể — `STORYTELLING.md` trong `t-i/outputs/YouTube-Research-System/`.

## Đích giọng kể

Theo yêu cầu ngày 2026-09-15 và mẫu Cẩm Tân Đại Lâu / mất tích đêm Trung thu: lời kể gần gũi, có người dẫn chuyện, để người nghe lần theo từng việc và hiểu lại chi tiết cũ khi có chứng cứ mới. Viết thẳng bằng tiếng Việt từ dữ kiện; không dùng bản tiếng Việt như bản dịch trung gian hoặc đọc bảng kiểm chứng thành lời kể.

Khi viết hoặc sửa câu văn, đọc [giọng kể](references/giong-ke.md) và [mẫu và thực hành](references/mau-va-thuc-hanh.md). Khi dựng khung, đọc thêm [kiến trúc câu chuyện](references/kien-truc-cau-chuyen.md). Học cách dẫn dắt trong mẫu, không chép câu cửa miệng hay nhập lời đồn vào hồ sơ sự thật.

Yêu cầu sửa chính tả, làm mượt hoặc thử một trích đoạn không tự trở thành việc sản xuất cả tập. Trả đúng phần được giao; nếu Tú yêu cầu không lược chi tiết, đối chiếu để giữ đủ thông tin. Với artifact đang đóng băng trong vòng review, tuân thủ luật lượt ở `AGENTS.md`, không sửa ngoài lượt.

## Luồng làm việc

Số bước khớp bảng ở `AGENTS.md` gốc mục 8. Mỗi bước vẫn đi qua luồng review nhiều vòng trước khi bước sau bắt đầu.

| Bước | Việc | Đọc | Sản phẩm |
| --- | --- | --- | --- |
| 1 | Gợi ý vụ mới | [chọn vụ](references/chon-vu.md), [thị trường Việt Nam](references/thi-truong-viet-nam.md) | `batches/YYYY-MM-DD-NN.md`; case `proposed` trong sổ, qua skill `registry-safe-update` |
| 2 | Câu hỏi trung tâm và góc kể | [chọn vụ](references/chon-vu.md), [mở đầu](references/mo-dau.md) | ghi trong `dossier.md` |
| 3 | Nghiên cứu, timeline, claim ledger | [nghiên cứu và kiểm chứng](references/nghien-cuu-va-kiem-chung.md) | `sources.csv`, `claims.csv`, `timeline.md`, `gaps.md`, `assets.csv`, `sources/` |
| 4 | Khung sườn | [kiến trúc câu chuyện](references/kien-truc-cau-chuyen.md), [mở đầu](references/mo-dau.md), `STORYTELLING.md` | `scripts/01-beat-sheet.md` |
| 5 | Bản tiếng Việt đầy đủ | [giọng kể](references/giong-ke.md), [mẫu và thực hành](references/mau-va-thuc-hanh.md), [thị trường Việt Nam](references/thi-truong-viet-nam.md) | `scripts/02-script-vi.md` → `awaiting_review`, **Tú duyệt nội dung** |
| 6 | Bản thu âm và đóng gói, sau khi Tú duyệt | [bản thu âm](references/ban-thu-am.md) | `scripts/03-script-final-sourced.md`, `scripts/04-narration-clean.txt`, `pronunciation.md`, `visual-plan.md`, `packaging.md`, `quality-review.md` → `scripted` |

Dùng `templates/episode.md` của dự án cho hồ sơ tập. Chỉ ghi là đã bàn giao những file thật sự tồn tại.

Yêu cầu viết kịch bản bao gồm luôn quyền nghiên cứu, dựng khung và viết bản tiếng Việt; không xin duyệt dàn ý riêng trừ khi Tú yêu cầu. Lớp Tú duyệt ở bước 5 thì bắt buộc, trừ khi Tú nói rõ bỏ.

## Bất biến biên tập

- Không ép lên vụ án một giả thuyết sai, số manh mối cố định, một cú lật, một lỗi hệ thống hay thời lượng cố định. Vụ chưa giải được vẫn làm được nếu kết thúc nói rõ giới hạn chứng cứ.
- Hướng điều tra sai chỉ kể khi nó có thật, có người tin, và được kể là niềm tin của người đó — không phải sự thật khách quan rồi rút lại.
- Không nói sai sự việc hay giấu chứng cứ gỡ tội đã biết để quy chụp một người.
- Mỗi bước điều tra phải có mục đích và hệ quả dễ hiểu. Tác giả kiểm đủ điều kết quả chứng minh được và không chứng minh được trong hồ sơ; trong lời kể, giữ giới hạn khi nó làm đổi hướng điều tra hoặc khi bỏ nó sẽ làm người nghe hiểu sai mức chứng cứ của một kết luận (ví dụ: dấu vết nghi là máu thành máu đã xác nhận, camera không ghi được thành chắc chắn không đi qua). Cách áp dụng: [giọng kể](references/giong-ke.md). Không thêm câu tự đính chính sau mọi phát hiện. Giữ phản biện và chứng cứ gỡ tội; không đổi chúng lấy giọng kể trôi chảy.
- Lời giải có chỗ để nối lại các manh mối trước đó; không kể lại cả câu chuyện sau khi lộ.
- Nhân hoá nạn nhân bằng chi tiết đời thật có nguồn và có chức năng. Không bịa thoại, điều kiện cảnh, cảm xúc hay dựng lại từng phút.
- Ngôn ngữ trung tính, chính xác. Chỉ đưa chi tiết pháp y không ghê rợn khi nó thay đổi một kết luận điều tra. Đổi từ không bảo đảm được đủ điều kiện quảng cáo.
- CTA mặc định tối đa một câu, sau phần kết. Không chép phần tài trợ từ mẫu.
- Không tự gửi tin, liên hệ nguồn, thanh toán, đăng video hay nhập trạng thái vụ án từ bên ngoài vào sổ.

## Trạng thái trong sổ

- `awaiting_review`: bản tiếng Việt đầy đủ đã nộp, chờ Tú duyệt. Vẫn bị khoá khỏi gợi ý.
- `scripted`: chỉ khi bộ bàn giao bước 6 đã xong.
- `published`: chỉ khi Tú xác nhận và có đường dẫn đã kiểm.

## Skill này không làm được

- **Không phải tư vấn pháp lý.** Phần thận trọng với vụ án Việt Nam là kiểm tra biên tập để giảm rủi ro, không phải đánh giá pháp luật. Thấy rủi ro mà không tự đánh giá được thì dừng chi tiết đó và báo Tú.
- Không đo được sức giữ chân, lượt xem hay RPM. Điểm 1–5 là đánh giá biên tập.
- Không thay được lớp Tú duyệt nội dung ở bước 5.
- Không kiểm được âm thanh khi chưa nghe thật.
- Không bảo đảm đã tìm hết nguồn tồn tại.

## Phần chưa kiểm chứng

Tạo ngày 2026-09-14; cập nhật giọng kể ngày 2026-09-15. Phần kế thừa — nghiên cứu, claim ledger, kiến trúc câu chuyện, các bất biến — đã chạy thật trên NET-0006. Phần bản địa hoá, thận trọng với vụ án trong nước, tra cạnh tranh trên YouTube tiếng Việt và chuẩn bị TTS tiếng Việt **chưa chạy trọn trên tập thật nào**. Kiểm thử trích đoạn và review của lần cập nhật giọng kể được ghi riêng ở `coordination/drafts/sys-skill-ky-an-viet-voice.md`; không suy từ bài thử sang chất lượng cả tập hoặc số liệu giữ chân. Dùng trên tập thật thì ghi lại chỗ không khớp thực tế để sửa skill.

Ở một lượt thử hướng dẫn mới, người viết tự thêm người thực hiện khi nối câu, trong khi baseline không thêm. Đã bổ sung quy tắc giữ đúng đường đi của thông tin trong hướng dẫn giọng kể; lượt kiểm lại chỉ dùng cùng bộ dữ kiện đã phát hiện lỗi, chưa thử quy tắc này trên bộ khác. Đây là lỗi cần rà khi dùng skill, chưa đủ dữ liệu để quy kết nguyên nhân cho một câu hướng dẫn cụ thể.
