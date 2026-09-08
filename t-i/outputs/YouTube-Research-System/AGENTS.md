# Quy tắc vận hành

Đọc README.md và registry.json trước mỗi công việc. Trước khi gợi ý góc kể, viết hook, dàn ý hoặc kịch bản, đọc STORYTELLING.md. Chỉ dẫn mới nhất của người dùng ưu tiên hơn mặc định ở đây. Dùng các file làm bộ nhớ bền vững; không hứa nhớ xuyên cuộc trò chuyện nếu chưa đọc chúng.

## Phạm vi và skill

Kênh về bí ẩn internet, lừa đảo và điều tra số, không phải riêng án mạng. Có thể dùng mystery-case-script cho nghiên cứu và kể chuyện, nhưng không áp dụng máy móc yêu cầu phải có giả thuyết sai, người bị kết án, hoặc cấu trúc án mạng. Bài đăng gốc đã xác thực là nguồn trực tiếp cho việc tài khoản đã đăng nội dung gì; không tự xác nhận các cáo buộc trong bài đăng đó. Hồ sơ cơ quan điều tra cũng cần phân biệt cáo buộc với kết luận, và kiểm tra cập nhật sau đó.

## Chống trùng

registry.json là nguồn trạng thái duy nhất. Mỗi chuyện có ID NET-0001 tăng dần, canonical_title, aliases, entities, event_dates, fingerprint, status, history, episode_path và published_url.

Trước đề xuất, so cả mã, tên chuẩn, biệt danh, nhân vật/tổ chức và sự kiện gốc. Hai tiêu đề khác nhau về cùng vụ vẫn là cùng chuyện. Tập tổng hợp phải lưu included_case_ids, khóa cả chuyện thành phần. Không loại toàn bộ một nhân vật nếu đó là sự kiện khác thực sự; nêu rõ liên hệ và chỉ đề xuất khi không kể lại lõi chuyện cũ.

Loại mặc định: selected, researching, awaiting_review, scripted, published, excluded. Các chuyện proposed/deferred đã xuất hiện không tự lặp lại ở đợt mới; chỉ đưa lại khi người dùng xin danh sách cũ hoặc cho phép. Nếu không đủ chuyện mới, nói rõ và tìm thêm; không tự bỏ bộ lọc.

Thêm ID vào sổ ngay khi đưa lựa chọn, cùng ngày gợi ý và batch_id. Khi người dùng chọn, cập nhật selected trước khi nghiên cứu. Mỗi lần đổi trạng thái thêm history có ngày và lý do. Không tự coi scripted là published. Không xóa lịch sử để tái sử dụng ID. Khi cập nhật, đọc bản mới nhất, lưu bản sao có dấu thời gian ở history/, ghi file tạm rồi thay thế và kiểm tra JSON. Không để nhiều tiến trình cùng sửa sổ.

## Gợi ý

Tìm web hiện tại và xác minh từng ứng viên trước khi giới thiệu. Mỗi đợt mặc định 5 chuyện, lưu batches/YYYY-MM-DD-NN.md.

Mỗi lựa chọn: ID; tiêu đề làm việc; tóm tắt không tiết lộ hết; hook 1–2 câu; câu hỏi trung tâm; 2–3 link nguồn đã mở kiểm tra; nguồn gốc mạnh nhất hoặc ghi chưa tìm thấy; sức hút; tình trạng lời giải; hình có thể kiếm; rủi ro quảng cáo và lý do; độ khó nghiên cứu; góc khác biệt so với video đã có. Tra cứu mức độ khai thác trên YouTube trước khi gọi một chuyện là ít người làm. Không bịa lượt xem, RPM hoặc xác suất bật kiếm tiền.

Chấm 1–5: sức hút, độ vững của nguồn, khả năng dựng hình, độ mới của góc kể, phù hợp quảng cáo, mức đáp ứng câu hỏi cuối. Đây là đánh giá biên tập, không phải đo lường khách quan. Không đề xuất nguồn yếu như thể đã đủ để sản xuất.

## Nghiên cứu và tải

Tạo episodes/ID-slug/ với sources/, assets/, scripts/. Áp dụng templates/episode.md.

Tìm nguồn sơ cấp, tin thời điểm xảy ra, phỏng vấn, bài điều tra, tài liệu kỹ thuật khi cần và diễn biến mới nhất. Thu thập các chi tiết và lời nói thực sự phục vụ câu chuyện. Theo các trích dẫn ngược về nguồn gốc, không đếm bài sao chép như xác nhận độc lập.

Mỗi source_id ghi URL gốc, tiêu đề, tác giả/cơ quan, ngày xuất bản/cập nhật, ngày truy cập, loại nguồn, đường dẫn local, trạng thái tải, quyền dùng lại, trang/timestamp liên quan. Phân biệt downloaded_original, saved_excerpt, link_only, blocked, missing. Bản tóm tắt tự viết không phải bản gốc tải về. Với file đã tải kiểm tra mở được, đúng loại, kích thước và SHA-256 nếu công cụ cho phép. Không đánh dấu downloaded nếu chưa có file thực.

Tải PDF/tài liệu và tài sản được phép; với trang web lưu bản nghiên cứu/excerpt trong phạm vi cho phép, hoặc link và ghi chú. Không vượt giới hạn truy cập hay bản quyền. Chưa rõ quyền đưa lên video: đánh dấu unknown, không tự coi là được phép. Dùng link cho media không được phép tải, ghi giải pháp thay thế. Không tải malware, dữ liệu bị đánh cắp, mật khẩu hoặc dữ liệu cá nhân rò rỉ để kể vụ án; dùng báo cáo về chúng.

Claim ledger phải có claim_id, chi tiết, source_id, vị trí chứng minh, mức chắc chắn, mâu thuẫn và trạng thái established/alleged/inference/unknown. Tránh suy diễn tâm lý hoặc viết thoại không có nguồn. Điểm nút thắt quan trọng cần nguồn trực tiếp hoặc đối chiếu độc lập đủ mạnh. Dừng đưa một chi tiết vào kịch bản khi bằng chứng chưa đủ, tiếp tục phần còn lại.

Hoàn tất nghiên cứu khi câu hỏi trung tâm, diễn biến và kết luận định kể có chứng cứ; đã kiểm tra cập nhật; đã truy nguồn các manh mối thiết yếu; có báo cáo khoảng trống và danh mục tải. Không tuyên bố đã tìm tất cả nguồn tồn tại. Nếu không đủ chất liệu, báo lý do và đề xuất chuyện khác trước khi viết dài.

## Kịch bản

STORYTELLING.md lưu phân tích bảy mẫu duy nhất người dùng cung cấp qua hai đợt và các quy tắc đã thích nghi cho kênh. Các file references/ chỉ là mẫu kể chuyện, không phải nguồn chứng minh vụ việc và không phải tập của người dùng đã kể. Không đưa chúng vào registry.cases khi chưa có yêu cầu chọn hoặc loại trừ câu chuyện cụ thể.

Theo phiên bản 2 của hướng dẫn: theo dõi ai biết/tin điều gì tại từng đoạn, nguyên nhân của thay đổi thái độ, chức năng của chi tiết và các lớp tiết lộ. Phân biệt lời kể, niềm tin, chứng cứ và suy luận; nhiều bất thường chưa được giải thích không tự chứng minh một âm mưu. Tài liệu xác nhận một phần sự việc không xác nhận toàn bộ câu chuyện lan truyền.

CTA: người dùng muốn đơn giản. Mặc định tối đa một câu cuối tập, sau phần trả lời câu chuyện; không tiểu phẩm với nút like, không ngắt hook/cao trào. Không đưa quảng cáo tài trợ từ mẫu vào bài mới.

Yêu cầu mới nhất về độ dài: không đặt số phút cố định và không dùng đề xuất 20–30 phút trước đây. Viết theo độ dày tư liệu và nhịp truyện; ưu tiên dẫn dắt hấp dẫn ngay trong bản tiếng Việt đầy đủ. Ước tính thời lượng sau bản viết chỉ để lập kế hoạch sản xuất. Không kéo dài bằng lặp ý, mở nút thắt không giải đáp hoặc bịa chi tiết. Nếu người dùng gửi kịch bản tham khảo, phân tích kỹ thuật kể chuyện để hình thành giọng riêng, không sao chép lời văn/dấu hiệu nhận diện của tác giả.

Người dùng đã xác nhận ngày 2026-09-08: hướng tới khán giả Mỹ, lời kể tiếng Anh, bắt buộc xét duyệt bản đầy đủ tiếng Việt trước. Đây là yêu cầu của người dùng, không chỉ là mặc định skill. Không chuyển sang viết tiếng Anh khi chưa được duyệt. Chỉ bỏ bước này nếu người dùng sau đó yêu cầu rõ ràng. Bản Anh phải giữ nội dung đã duyệt và dùng cách diễn đạt tự nhiên với người Mỹ; thay đổi nội dung/cấu trúc đáng kể cần duyệt lại.

Trước prose: timeline, claim ledger, beat sheet. Nếu dùng kiến trúc của skill mystery-case-script, đọc story-architecture.md trước khi viết beat sheet. Không gán một giả thuyết sai cho điều tra viên khi nguồn không nói vậy.

Mở bằng một chi tiết thật tạo câu hỏi; bối cảnh vừa đủ; giải thích thuật ngữ qua tác động lên con người; mỗi phát hiện giải đáp một câu hỏi và tạo câu hỏi kế tiếp. Tiết lộ theo diễn biến có chứng cứ, không nói sai để tạo twist. Bí ẩn chưa giải quyết phải kết thúc trung thực.

Bản tiếng Việt đầy đủ là mặc định để người dùng duyệt nội dung trước bản tiếng Anh. Đây là bước duyệt một sản phẩm cụ thể, không xin lại quyền nghiên cứu. Nếu người dùng chọn tự động viết bản cuối hoặc yêu cầu bỏ bước duyệt, chỉ dẫn đó ghi đè mặc định. Khi phải chờ duyệt do skill, nêu đúng đường dẫn skill và điều khoản liên quan.

Giọng kể riêng: gần gũi, rõ ràng, giàu chi tiết được chứng minh, căng thẳng từ câu hỏi và chứng cứ. Không sao chép kịch bản hoặc các dấu hiệu nhận diện của MrBallen. Không hứa kịch bản sẽ viral.

Kịch bản làm việc gắn claim_id theo đoạn; bản narration sạch không đọc nguồn/cue dựng. Đối chiếu mọi thông tin trước bàn giao, đọc riêng một lượt để kiểm tra nhịp kể, một lượt kiểm tra quảng cáo theo chính sách YouTube đang có hiệu lực, rồi một lượt kiểm tra định dạng thu âm. Không dùng né từ đơn lẻ như bảo đảm kiếm tiền.

Chỉ ghi scripted khi bản cuối theo ngôn ngữ đã chọn được bàn giao; bản chờ duyệt ghi awaiting_review và vẫn bị khóa đề xuất. Ghi published chỉ khi có xác nhận. Không gửi tin, xin phép nguồn, thanh toán hoặc xuất bản ra ngoài nếu chưa được người dùng cho phép.
