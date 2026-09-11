# Prompt dùng chung cho ba ghế viết — phép thử model Claude, NET-0006

Bản này là **nguyên văn** prompt gửi cho cả ba subagent. Chỗ duy nhất khác nhau giữa ba lượt là
giá trị `{SLUG}` (`opus` | `sonnet` | `haiku`) và model chạy lượt đó. Không thêm, không bớt câu nào.

---

Bạn viết **bản tiếng Việt đầy đủ** (bước 5) cho tập NET-0006 của một kênh YouTube điều tra/hình sự,
dựa trên khung sườn đã được duyệt. Đây là một phép thử so sánh model: bản của bạn sẽ đặt cạnh bản của
hai model khác trên cùng đầu vào, nên hãy viết bản tốt nhất bạn viết được trong một lượt.

## Đọc trước khi viết (đọc hết, theo thứ tự này)

1. `t-i/outputs/YouTube-Research-System/episodes/NET-0006-sherri-rasmussen/scripts/01-beat-sheet.md`
   — khung sườn v2, đã qua luồng review và settled. Đây là bộ xương bắt buộc.
2. `t-i/outputs/YouTube-Research-System/STORYTELLING.md` — bộ tiêu chí kể chuyện của kênh.
3. `t-i/outputs/YouTube-Research-System/AGENTS.md` — luật nghiệp vụ của kênh (CTA, độ dài, giọng kể).
4. Hồ sơ nghiên cứu cùng tập, thư mục
   `t-i/outputs/YouTube-Research-System/episodes/NET-0006-sherri-rasmussen/`:
   `claims.csv` (mã C01–C26 và trạng thái established/alleged/inference), `sources.csv`,
   `timeline.md`, `dossier.md`, `gaps.md`, và các file trong `sources/`.

## Không được đọc, không được làm

- **Không đọc bất kỳ bản kịch bản nào đã có.** Cụ thể: không mở `scripts/02-script-vi.md`,
  `scripts/02-script-vi-gemini.md`, `scripts/02b-*.txt`, `scripts/comparison-chatgpt-vs-gemini.md`,
  và không mở bất cứ gì trong `coordination/drafts/model-trials/NET-0006/astra/`, `.../sol/`,
  `.../opus/`, `.../sonnet/`, `.../haiku/`. Câu văn phải là của bạn, không lấy mẫu từ bản khác.
- **Không tra web.** Chỉ dùng hồ sơ trong repo. Nếu một chi tiết không có trong hồ sơ thì không viết nó.
- **Không chạy lệnh git** nào (không add, không commit, không checkout, không stash).
- **Không sửa** `registry.json`, không sửa gì trong `episodes/`, không sửa `coordination/claims/`,
  không sửa `coordination/threads/`. Chỉ ghi vào thư mục ra của bạn ở dưới.
- **Không gọi subagent.** Một lượt viết của chính bạn; được đọc lại và tự sửa trước khi ghi file.

## Việc phải làm

Viết đủ 14 nhịp **B01 → B14** đúng thứ tự khung sườn, giữ mọi ranh giới ở mục 3 (thang tiết lộ) và
ranh giới riêng của từng beat. Vài điểm dễ sai, nêu lại cho rõ:

- Không dùng chữ "dàn dựng" (hay từ đồng nghĩa nói như sự thật) trước B11; ở B11 phải quy nguồn cho
  chuyên gia công tố, giữ đúng nhãn `alleged`.
- Không nêu tên Stephanie Lazarus trước B06, và không nói người phụ nữ ở B04 là cảnh sát / thuộc LAPD.
- Không nêu BMW ở B01 — hook chỉ dùng C03.
- B07: hồ sơ một phần, khớp **11 vị trí đọc được**; không gọi là profile đầy đủ, không nhầm với 13 loci
  (mẫu trực tiếp) hay 15 loci (SERI).
- B09: không gọi cuộc phỏng vấn là "thú tội", không dựng thoại, không suy từ cử chỉ, và **chưa** nêu
  kết quả 13 loci — để ở B10.
- B10 phải nêu song song phần phản biện của bên bào chữa (phong bì rách, súng không thu hồi, vân tay/DNA
  lạ chưa xác định); phần vân tay/DNA lạ giữ là giới hạn trung thực, không đóng.
- B12: tòa **không** kết luận có âm mưu bao che có tổ chức.
- B13: viết ngày điều trần **bằng chữ** — "ngày 9 tháng 10 năm 2026" — không viết dạng số.
- B14: nhận xét biên tập (C26 là `inference`), rồi **đúng một câu** CTA, đặt sau phần trả lời câu chuyện.

Độ dài: nhắm khoảng **3.500–4.500 từ** cho phần lời kể, để so được với hai bản thử đã có. Không kéo dài
bằng lặp ý, không mở nút thắt rồi bỏ đó, không bịa chi tiết để đủ số.

## Ghi ra đúng ba file, trong `coordination/drafts/model-trials/NET-0006/{SLUG}/`

1. `02-script-vi-{SLUG}.md` — bản làm việc. Mỗi nhịp một heading `## B01 — <tên nhịp>` … `## B14 — …`.
   Cuối mỗi nhịp một dòng chú thích HTML `<!-- Cxx; nguồn Sxx tr.__; ghi chú ranh giới -->`. Lời kể
   nằm giữa hai mốc `<!-- NARRATION_START -->` và `<!-- NARRATION_END -->`.
2. `02b-ban-doc-{SLUG}.txt` — **chỉ lời kể**, tạo trực tiếp từ file trên bằng cách bỏ heading nhịp và
   mọi chú thích. Không viết lại lần hai, không thêm câu mới. Không còn mã `B**`, `C**`, `S**` trong file này.
3. `notes-{SLUG}.md` — ngắn, tối đa 400 từ: những lựa chọn kể chuyện bạn đã làm; chỗ nào hồ sơ không đủ
   nên bạn đã tránh; **và một mục "tôi đã không kiểm cái gì"** trung thực.

Không ghi file nào ngoài ba file trên. Không tự nhận bản của mình đã qua review hay đã được duyệt.

Báo lại cuối lượt: số từ phần lời kể, và một câu bạn thấy là điểm mạnh nhất của bản mình.
