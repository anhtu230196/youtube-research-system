# Quy tắc vận hành

Đọc README.md và registry.json trước mỗi công việc. Trước khi gợi ý góc kể, viết hook, dàn ý hoặc kịch bản, đọc STORYTELLING.md. Chỉ dẫn mới nhất của người dùng ưu tiên hơn mặc định ở đây. Dùng các file làm bộ nhớ bền vững; không hứa nhớ xuyên cuộc trò chuyện nếu chưa đọc chúng.

## Phạm vi và skill

Kênh kỳ án tiếng Việt cho khán giả Việt Nam. Tú quyết ngày 2026-09-14, thay quyết định 2026-09-08 (khán giả Mỹ, lời kể tiếng Anh). Kỳ án là vụ án hoặc bí ẩn có thật, có câu hỏi khó giải thích và con người cụ thể: án mạng bí ẩn, mất tích, án oan và minh oan, vụ chưa có lời giải, danh tính bị che giấu, hiện trường dàn dựng. Lừa đảo lớn và điều tra số vẫn nhận khi có chất kỳ án. Vụ trong nước và nước ngoài đều được.

Quy trình làm một tập: `.claude/skills/ky-an-viet/SKILL.md` ở gốc repo. **Không dùng skill `mystery-case-script` cho kênh này** — nó viết lời kể tiếng Anh cho khán giả Mỹ. Không áp dụng máy móc yêu cầu phải có giả thuyết sai, người bị kết án, hoặc cấu trúc án mạng.

Bài đăng gốc đã xác thực là nguồn trực tiếp cho việc tài khoản đã đăng nội dung gì; không tự xác nhận các cáo buộc trong bài đăng đó. Hồ sơ cơ quan điều tra cũng cần phân biệt cáo buộc với kết luận, và kiểm tra cập nhật sau đó.

Mã câu chuyện vẫn là `NET-xxxx`. Đó chỉ là mã; nó không còn nghĩa là chủ đề internet.

## Chống trùng

registry.json là nguồn trạng thái duy nhất. Mỗi chuyện có ID NET-0001 tăng dần, canonical_title, aliases, entities, event_dates, fingerprint, status, history, episode_path và published_url.

Trước đề xuất, so cả mã, tên chuẩn, biệt danh, nhân vật/tổ chức và sự kiện gốc. Hai tiêu đề khác nhau về cùng vụ vẫn là cùng chuyện. Tập tổng hợp phải lưu included_case_ids, khóa cả chuyện thành phần. Không loại toàn bộ một nhân vật nếu đó là sự kiện khác thực sự; nêu rõ liên hệ và chỉ đề xuất khi không kể lại lõi chuyện cũ.

Loại mặc định: selected, researching, awaiting_review, scripted, published, excluded. Các chuyện proposed/deferred đã xuất hiện không tự lặp lại ở đợt mới; chỉ đưa lại khi người dùng xin danh sách cũ hoặc cho phép. Nếu không đủ chuyện mới, nói rõ và tìm thêm; không tự bỏ bộ lọc.

Các chuyện `proposed` từ trước ngày 2026-09-14 được chọn cho hướng bí ẩn internet cũ; một số có thể không còn hợp phạm vi kỳ án. Không tự đổi trạng thái của chúng — nêu cho Tú khi chúng liên quan.

Thêm ID vào sổ ngay khi đưa lựa chọn, cùng ngày gợi ý và batch_id. Khi người dùng chọn, cập nhật selected trước khi nghiên cứu. Mỗi lần đổi trạng thái thêm history có ngày và lý do. Không tự coi scripted là published. Không xóa lịch sử để tái sử dụng ID. Khi cập nhật, đọc bản mới nhất, lưu bản sao có dấu thời gian ở history/, ghi file tạm rồi thay thế và kiểm tra JSON. Không để nhiều tiến trình cùng sửa sổ.

## Gợi ý

Tìm web hiện tại và xác minh từng ứng viên trước khi giới thiệu. Mỗi đợt mặc định 5 chuyện, lưu batches/YYYY-MM-DD-NN.md.

Mỗi lựa chọn: ID; tiêu đề làm việc; tóm tắt không tiết lộ hết; hook 1–2 câu; câu hỏi trung tâm; 2–3 link nguồn đã mở kiểm tra; nguồn gốc mạnh nhất hoặc ghi chưa tìm thấy; sức hút; tình trạng lời giải; hình có thể kiếm; rủi ro quảng cáo và lý do; độ khó nghiên cứu; các video tiếng Việt đã có về vụ đó và góc khác biệt so với chúng. Với vụ Việt Nam, thêm tư cách tố tụng hiện tại của người liên quan và vụ có thuộc danh sách phải báo Tú trước không (mục Thị trường Việt Nam).

Đối thủ của kênh là các kênh kỳ án tiếng Việt. Tra YouTube bằng từ khoá tiếng Việt trước khi gọi một chuyện là ít người làm. Không bịa lượt xem, RPM hoặc xác suất bật kiếm tiền.

Chấm 1–5: sức hút, độ vững của nguồn, khả năng dựng hình, độ mới của góc kể, phù hợp quảng cáo, mức đáp ứng câu hỏi cuối. Đây là đánh giá biên tập, không phải đo lường khách quan. Không đề xuất nguồn yếu như thể đã đủ để sản xuất.

## Nghiên cứu và tải

Tạo episodes/ID-slug/ với sources/, assets/, scripts/. Áp dụng templates/episode.md.

Tìm nguồn sơ cấp, tin thời điểm xảy ra, phỏng vấn, bài điều tra, hồ sơ toà án, tài liệu kỹ thuật khi cần và diễn biến mới nhất. Thu thập các chi tiết và lời nói thực sự phục vụ câu chuyện. Theo các trích dẫn ngược về nguồn gốc, không đếm bài sao chép như xác nhận độc lập.

Vụ nước ngoài: đọc nguồn ở ngôn ngữ gốc; bài tiếng Việt dịch lại không phải nguồn độc lập. Vụ Việt Nam: ưu tiên bản án đã có hiệu lực công bố trên congbobanan.toaan.gov.vn, thông tin chính thức của cơ quan tiến hành tố tụng, và báo chí chính thống lúc sự việc xảy ra; không tìm cách xác định lại danh tính đã bị ẩn trong bản án.

Mỗi source_id ghi URL gốc, tiêu đề, tác giả/cơ quan, ngày xuất bản/cập nhật, ngày truy cập, loại nguồn, đường dẫn local, trạng thái tải, quyền dùng lại, trang/timestamp liên quan. Phân biệt downloaded_original, saved_excerpt, link_only, blocked, missing. Bản tóm tắt tự viết không phải bản gốc tải về. Với file đã tải kiểm tra mở được, đúng loại, kích thước và SHA-256 nếu công cụ cho phép. Không đánh dấu downloaded nếu chưa có file thực.

Tải PDF/tài liệu và tài sản được phép; với trang web lưu bản nghiên cứu/excerpt trong phạm vi cho phép, hoặc link và ghi chú. Không vượt giới hạn truy cập hay bản quyền. Chưa rõ quyền đưa lên video: đánh dấu unknown, không tự coi là được phép. Dùng link cho media không được phép tải, ghi giải pháp thay thế. Không tải malware, dữ liệu bị đánh cắp, mật khẩu hoặc dữ liệu cá nhân rò rỉ để kể vụ án; dùng báo cáo về chúng.

Claim ledger phải có claim_id, chi tiết, source_id, vị trí chứng minh, mức chắc chắn, mâu thuẫn và trạng thái established/alleged/inference/unknown. Tránh suy diễn tâm lý hoặc viết thoại không có nguồn. Điểm nút thắt quan trọng cần nguồn trực tiếp hoặc đối chiếu độc lập đủ mạnh. Dừng đưa một chi tiết vào kịch bản khi bằng chứng chưa đủ, tiếp tục phần còn lại.

Hoàn tất nghiên cứu khi câu hỏi trung tâm, diễn biến và kết luận định kể có chứng cứ; đã kiểm tra cập nhật; đã truy nguồn các manh mối thiết yếu; có báo cáo khoảng trống và danh mục tải. Không tuyên bố đã tìm tất cả nguồn tồn tại. Nếu không đủ chất liệu, báo lý do và đề xuất chuyện khác trước khi viết dài.

## Thị trường Việt Nam

- **Lời kể cuối là tiếng Việt**, viết cho người Việt nghe, không dịch từng câu từ nguồn.
- **Bản địa hoá:** ngày/tháng/năm; hệ mét và độ C với độ chính xác tương đương nguồn; tiền giữ đơn vị gốc, chỉ quy đổi khi giúp hiểu và phải ghi tỷ giá cùng ngày áp tỷ giá; tên người giữ chữ viết gốc; thuật ngữ tư pháp nước ngoài giải thích bằng chức năng, không gán một chế định Việt Nam không tương đương.
- **Suy đoán vô tội:** chưa có bản án kết tội đã có hiệu lực thì gọi đúng tư cách tố tụng của người đó tại ngày kiểm tra, và ghi ngày kiểm tra. Không kết luận thay toà. Không gọi "hắn", "ả" hay dùng cách gọi phán xét với người chưa bị kết án.
- **Đời tư:** không nêu thông tin nhận diện nạn nhân, người thân, nhân chứng quá mức câu chuyện cần. Không nêu thông tin nhận diện người dưới 18 tuổi. Không nêu danh tính nạn nhân bị xâm hại tình dục.
- **Báo Tú trước khi đề xuất**, không tự đưa vào đợt gợi ý: vụ Việt Nam đang điều tra, truy tố hoặc xét xử; vụ có yếu tố chính trị, an ninh quốc gia, tôn giáo hoặc dân tộc; vụ liên quan người đang giữ chức vụ.
- Không miệt thị hay phân biệt vùng miền, tôn giáo, dân tộc, giới tính. Không gắn hành vi phạm tội với quê quán như một lời giải thích.
- **Đây là kiểm tra biên tập, không phải tư vấn pháp lý.** Rủi ro pháp lý không tự đánh giá được thì dừng chi tiết đó, báo Tú, làm tiếp phần còn lại.
- Xưng hô của người kể **chưa chốt** (`channel.narrator_voice` trong registry.json). Tú chốt thì ghi vào registry theo quy trình sửa sổ.

Cách áp dụng và danh sách kiểm: `.claude/skills/ky-an-viet/references/thi-truong-viet-nam.md`.

## Kịch bản

STORYTELLING.md lưu phân tích bảy mẫu duy nhất người dùng cung cấp qua hai đợt và các quy tắc đã thích nghi cho kênh. Các file references/ chỉ là mẫu kể chuyện, không phải nguồn chứng minh vụ việc và không phải tập của người dùng đã kể. Không đưa chúng vào registry.cases khi chưa có yêu cầu chọn hoặc loại trừ câu chuyện cụ thể.

Theo hướng dẫn kể chuyện: theo dõi ai biết/tin điều gì tại từng đoạn, nguyên nhân của thay đổi thái độ, chức năng của chi tiết và các lớp tiết lộ. Phân biệt lời kể, niềm tin, chứng cứ và suy luận; nhiều bất thường chưa được giải thích không tự chứng minh một âm mưu. Tài liệu xác nhận một phần sự việc không xác nhận toàn bộ câu chuyện lan truyền.

CTA: người dùng muốn đơn giản. Mặc định tối đa một câu cuối tập, sau phần trả lời câu chuyện; không tiểu phẩm với nút like, không ngắt hook/cao trào. Không đưa quảng cáo tài trợ từ mẫu vào bài mới.

Yêu cầu mới nhất về độ dài: không đặt số phút cố định và không dùng đề xuất 20–30 phút trước đây. Viết theo độ dày tư liệu và nhịp truyện; ưu tiên dẫn dắt hấp dẫn ngay trong bản tiếng Việt đầy đủ. Ước tính thời lượng sau bản viết chỉ để lập kế hoạch sản xuất. Không kéo dài bằng lặp ý, mở nút thắt không giải đáp hoặc bịa chi tiết. Nếu người dùng gửi kịch bản tham khảo, phân tích kỹ thuật kể chuyện để hình thành giọng riêng, không sao chép lời văn/dấu hiệu nhận diện của tác giả.

Tú đã quyết ngày 2026-09-14: khán giả Việt Nam, lời kể tiếng Việt, không còn bước viết bản tiếng Anh. Bản tiếng Việt đầy đủ vẫn phải được Tú duyệt nội dung trước khi chuẩn bị bản thu âm. Quyết định 2026-09-08 về khán giả Mỹ và lời kể tiếng Anh đã bị thay thế; không quay lại hướng đó nếu Tú chưa yêu cầu rõ.

Trước khi viết văn: timeline, claim ledger, beat sheet. Đọc `references/kien-truc-cau-chuyen.md` của skill ky-an-viet trước khi viết beat sheet. Không gán một giả thuyết sai cho điều tra viên khi nguồn không nói vậy.

Mở bằng một chi tiết thật tạo câu hỏi; bối cảnh vừa đủ; giải thích thuật ngữ qua tác động lên con người; mỗi phát hiện giải đáp một câu hỏi và tạo câu hỏi kế tiếp. Tiết lộ theo diễn biến có chứng cứ, không nói sai để tạo twist. Bí ẩn chưa giải quyết phải kết thúc trung thực.

Bản tiếng Việt đầy đủ là sản phẩm để Tú duyệt nội dung, và cũng là lời kể cuối. Sau khi duyệt chỉ chuẩn bị bản thu âm, không viết lại nội dung; thay đổi đáng kể về nội dung hoặc cấu trúc phải đưa lại để duyệt. Đây là bước duyệt một sản phẩm cụ thể, không xin lại quyền nghiên cứu. Nếu Tú chọn tự động viết bản cuối hoặc yêu cầu bỏ bước duyệt, chỉ dẫn đó ghi đè mặc định.

Giọng kể riêng: gần gũi, rõ ràng, giàu chi tiết được chứng minh, căng thẳng từ câu hỏi và chứng cứ. Không sao chép kịch bản hoặc các dấu hiệu nhận diện của MrBallen hay các kênh kỳ án tiếng Việt khác. Không hứa kịch bản sẽ viral.

Kịch bản làm việc gắn claim_id theo đoạn; bản narration sạch không đọc nguồn/cue dựng. Đối chiếu mọi thông tin trước bàn giao, đọc riêng một lượt để kiểm tra nhịp kể, một lượt kiểm tra quảng cáo theo chính sách YouTube đang có hiệu lực, một lượt kiểm tra thị trường Việt Nam, rồi một lượt kiểm tra định dạng thu âm. Không dùng né từ đơn lẻ như bảo đảm kiếm tiền.

Chỉ ghi scripted khi bản thu âm tiếng Việt và bộ bàn giao đã xong sau khi Tú duyệt nội dung; bản chờ duyệt ghi awaiting_review và vẫn bị khóa đề xuất. Ghi published chỉ khi có xác nhận. Không gửi tin, xin phép nguồn, thanh toán hoặc xuất bản ra ngoài nếu chưa được người dùng cho phép.
