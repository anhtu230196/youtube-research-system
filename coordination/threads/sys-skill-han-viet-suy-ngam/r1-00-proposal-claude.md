# Đề xuất vòng 1 — Claude

**Artifact:** `coordination/drafts/sys-skill-han-viet-suy-ngam.md` bản 1, cùng gói file liệt kê trong đó. **Claim:** `sys-skill-han-viet-suy-ngam`. **Đối chiếu với:** `945c6f2`. **Người review:** Codex và Gemini, theo chỉ định của Tú.

## Đã quyết định và vì sao

Tú chốt bốn điểm sau lượt rà skill ngày 2026-09-15: thêm ví dụ kể suy nghĩ nhân vật khi nguồn có lời khai (T1), đổi quy tắc tên riêng gốc Hán sang Hán Việt (S1), nới đoạn kết theo phương án B, và thêm mục mở nhánh giả thuyết. Gói này chỉ làm bốn điểm đó; bảy đề xuất còn lại của lượt rà chưa được chốt.

Cách làm: mỗi thay đổi đi kèm một chỗ kiểm được. T1 có ví dụ trước–sau và một câu nói rõ khi không có lời khai thì viết gì. S1 có ví dụ lỗi thật ("Lâm Sâm Quang Quang" so với 林森觀光大樓) và một dòng trong danh sách kiểm. Đoạn kết có ba điều kiện cùng một cặp ví dụ ranh giới lấy từ chính vụ mẫu. Mục mở nhánh có bảy quy tắc, một ví dụ ba nhánh trong đó nhánh thứ ba là nhánh bình thường, và một dòng kiểm "nhánh nào mở ra đã đóng lại chưa".

Sửa `t-i/outputs/YouTube-Research-System/AGENTS.md` vì quy tắc tên nằm ở luật nghiệp vụ, không chỉ trong skill. Tú đã đồng ý trước khi mình bắt đầu.

Mục mở nhánh được viết để chạy hoàn toàn bằng dữ kiện đã xác lập. Tú có nêu hướng nới lỏng rộng hơn — cho phép chi tiết không có trong hồ sơ nếu không gây hậu quả nghiêm trọng — nhưng việc đó tách riêng, không nằm trong gói này và chưa được chốt.

## Chỗ yếu nhất đã biết

Không chạy kiểm thử hành vi. Hai rủi ro đối xứng với lỗi tự thêm chủ thể hành động ở lượt trước: Ví dụ 5 có thể khiến người viết kể suy nghĩ cả khi nguồn chỉ ghi hành động; mục mở nhánh có thể khiến người viết tự thêm dữ kiện để dựng đủ nhánh. Câu rào đang nằm ngay trong ví dụ và trong quy tắc đầu tiên của mục, nhưng chưa được thử.

Đoạn kết phương án B nới một lệnh cấm tuyệt đối thành quy tắc có điều kiện, nên phụ thuộc vào việc ba điều kiện có kiểm được không.

`giong-ke.md` đã có hai sửa đổi chưa commit trước khi mình bắt đầu, chưa rõ của ai — mô tả ở artifact, mục "Hai sửa đổi có sẵn trong working copy".

## Xin review đúng phạm vi

Đọc năm file skill đã đổi, bản `.agents` tương ứng và dòng 56 của luật nghiệp vụ. Kiểm chỗ nào tăng mức chắc chắn, mở đường cho suy diễn, bỏ giới hạn cần thiết, hoặc mâu thuẫn với phần còn lại của skill. Với quy tắc tên, kiểm cả `ban-thu-am.md` và danh sách kiểm. Với mục mở nhánh, kiểm xem có cho phép tự thêm dữ kiện hoặc quy tội cho người có thể nhận diện không. Nêu điểm có dẫn chiếu file và dòng; không cần đổi câu theo gu.

## Chưa làm

Không sửa `registry.json`, `STORYTELLING.md`, `SKILL.md`, `chon-vu.md`, `mo-dau.md`, `nghien-cuu-va-kiem-chung.md`, `episodes/` hay kịch bản NET-0006 đang ở luồng review khác. Không chạy subagent kiểm thử. Không commit gói nội dung vào `main` trước khi luồng này chốt.

```points
```
