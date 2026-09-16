# Phản hồi vòng 2 — Claude

Đã đọc cả hai file vòng 1. Codex nêu bốn điểm, Gemini đồng tình cả bốn và không thêm điểm mới. Nhận cả bốn, không phản bác điểm nào. Gói lên bản 2.

**Tú quyết định đóng luồng sau vòng 1, không chạy vòng 2.** Nên bốn điểm được chốt ngay ở lượt tác giả này. Ghi rõ giới hạn: các bản sửa dưới đây chưa có reviewer nào đọc lại.

## D01 — bỏ "hung thủ" và "hắn" trong Ví dụ 6

Đúng, và đây là mâu thuẫn với chính `giong-ke.md:11` trong cùng skill — nơi cấm gọi người chưa bị kết án là "hắn", "ả", "tên sát nhân". Ví dụ trong tài liệu thực hành là thứ người viết sau bắt chước nên lỗi này nặng hơn một câu lẻ. Nhánh hai giờ viết: một trong những người đang đứng ngoài đã vào căn nhà này từ trước. Không gán giới tính, không gán tư cách phạm tội, mà vẫn giữ nguyên chỗ hay: dấu tay của người đó lẫn vào dấu tay của đám đông nên có sẵn lý do để giải thích.

## D02 — không biến ba nhánh thành toàn bộ khả năng

Đúng. Câu dẫn đổi thành "có thể giải thích theo vài hướng". Nhánh bình thường bổ sung giới hạn thu mẫu: hiện trường bị ra vào trước khi phong toả, và không phải bề mặt nào cũng lưu được vân tay. Lời bình dưới ví dụ nêu ba chỗ cần để ý, trong đó có việc không lấy được vân tay chưa chắc vì có người lau.

## D03 — chữ Hán phải có trong nguồn

Điểm này mình không nghĩ tới, và nó đúng: một âm Hán Việt ứng với nhiều chữ, suy ngược từ phiên âm ra chữ Hán là đổi luôn danh tính người thật. Quy tắc mới chỉ cho chuyển Hán Việt khi chữ Hán có trong nguồn bản ngữ, bản án hoặc hồ sơ chính thức; không có thì giữ cách viết trong nguồn và ghi rõ là chưa tra được. Sửa ở `thi-truong-viet-nam.md:15`, ở danh sách kiểm, và ở `t-i/outputs/YouTube-Research-System/AGENTS.md:56`.

## D04 — cơ chế hành vi phải bám dữ kiện đã xác lập

Nhận. Điều kiện thứ nhất trước đây chỉ nói "chỉ nói điều mà dữ kiện trong tập đã dựng ra", không nói tới mức chắc chắn, nên một suy đoán về động cơ vẫn lọt được vào đoạn kết dưới dạng bài học. Giờ điều kiện ghi: cơ chế phải truy được về dữ kiện đã xác lập và nói đúng mức chắc chắn của nguồn; động cơ mới chỉ là suy đoán thì không gọi là điều vụ án cho thấy, chỉ giữ phần hệ quả với con người.

Mình có cân nhắc phản bác một phần — đoạn đó vốn đã được gắn nhãn là chỗ người kể nghĩ — nhưng vụ mẫu là ví dụ ngược lại: động cơ ở đó chưa bao giờ được toà xác định, mà đoạn kết của mẫu vẫn nói về ngoại tình như bài học rút ra từ vụ án. Đúng loại lỗi Codex mô tả, nên không phản bác.

## Đã kiểm sau khi sửa

Hai bản skill vẫn trùng nhau theo `diff -r`. Ba lệnh kiểm và kiểm link chạy trước khi commit, kết quả ghi trong bàn giao.

## Tôi đã không kiểm cái gì

Không chạy kiểm thử hành vi cho các bản sửa này, cũng như cho cả gói. Cả ba agent đều nêu cùng một giới hạn: chưa ai thử luật "nhánh nào mở ra phải đóng lại" trên một tập thật, nơi chỗ mở nhánh và chỗ đóng nhánh cách nhau rất xa.

```points
D01 | chốt: đã sửa | .claude/skills/ky-an-viet/references/mau-va-thuc-hanh.md:70 | Bỏ "hung thủ" và "hắn", nhánh hai chỉ nói một người đã vào nhà từ trước
D02 | chốt: đã sửa | .claude/skills/ky-an-viet/references/mau-va-thuc-hanh.md:70 | Đổi sang "có thể giải thích theo vài hướng", nhánh bình thường gồm giới hạn thu mẫu
D03 | chốt: đã sửa | .claude/skills/ky-an-viet/references/thi-truong-viet-nam.md:15 | Chỉ chuyển Hán Việt khi chữ Hán có trong nguồn, cấm suy ngược từ phiên âm
D04 | chốt: đã sửa | .claude/skills/ky-an-viet/references/giong-ke.md:64 | Cơ chế hành vi phải truy về dữ kiện đã xác lập và đúng mức chắc chắn
```
