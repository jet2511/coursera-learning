# Pair Programming

- **Khóa học:** IBM Java Developer Professional Certificate / Course 01 - Introduction to Software Engineering
- **Module:** Module 02 - Introduction to Software Development
- **Chủ đề con:** Introduction to Development
- **Hình thức:** Video (Thời lượng: ~4,5 phút)

---

## 1. Khái niệm cốt lõi về Pair Programming
- Là kỹ thuật phát triển phần mềm trong **Agile**, nơi **hai lập trình viên cùng làm việc cạnh nhau trên một máy tính** (trực tiếp hoặc trực tuyến qua screen sharing/video call).
- Hai người liên tục thảo luận, phản biện và lên kế hoạch trong quá trình hiện thực hóa giải pháp.

---

## 2. Ba phong cách Pair Programming (Styles)
| Phong cách | Cơ chế hoạt động | Mục tiêu / Tình huống phù hợp |
| :--- | :--- | :--- |
| **Driver / Navigator** *(Phổ biến nhất)* | - **Driver:** Trực tiếp gõ mã nguồn.<br>- **Navigator:** Quan sát, rà soát lỗi tức thì, định hướng bước tiếp theo và bao quát bức tranh tổng thể.<br>- *Quy tắc:* Phải luân chuyển vai trò (swap roles) thường xuyên. | Cân bằng sự tham gia của cả 2 kỹ sư xuyên suốt tác vụ. |
| **Ping-Pong** *(Kết hợp TDD)* | - Gắn liền với **Test-Driven Development (TDD)**.<br>- Người A viết test case bị fail -> Người B viết mã để pass test đó.<br>- Đổi vai cho task kế tiếp. Cùng nhau refactor mã nguồn sau khi pass. | Đảm bảo độ bao phủ test (coverage), tư duy test-first và refactoring liên tục. |
| **Strong-Style** *(Mentor - Mentee)* | - Quy tắc vàng: *"Để một ý tưởng đi từ đầu vào máy tính, nó phải đi qua đôi tay của người khác" (from your head through someone else's hands)*.<br>- Kỹ sư có kinh nghiệm đóng vai **Navigator** (hướng dẫn tư duy). Kỹ sư ít kinh nghiệm hơn là **Driver** (gõ code theo hướng dẫn, không phản biện cho đến khi hoàn thành xong dòng suy nghĩ). | Đào tạo, onboarding thành viên mới, chuyển giao kiến thức (knowledge transfer) từ senior sang junior. |

---

## 3. Lợi ích (Benefits)
- **Chất lượng code vượt trội:** Hai cặp mắt cùng soi code giúp hạn chế tối đa lỗi chính tả (typos), lỗi logic và bugs.
- **Code review tức thì (On-the-fly review):** Giảm thiểu gánh nặng cho quy trình code review chính thức sau này.
- **Tối ưu giải pháp từ sớm:** Thảo luận 2 chiều giúp chọn ra kiến trúc/hướng đi tốt nhất ngay từ ban đầu.
- **Phát triển toàn diện kỹ năng:** Nâng cao cả kỹ năng kỹ thuật (hard skills) và kỹ năng mềm (soft skills: giao tiếp, giải quyết vấn đề).
- **Tiết kiệm tổng chi phí vòng đời:** Dù ban đầu tốn thời gian hơn 1 người tự viết, nhưng tiết kiệm rất nhiều thời gian về sau cho khâu testing, review và fix bug production.

---

## 4. Thách thức & Cách khắc phục (Challenges)
- **Tiêu hao năng lượng (Exhausting):** Đòi hỏi sự tập trung cao độ liên tục; cần có thời gian nghỉ hợp lý.
- **Lệch pha vai trò (Typist vs Programmer):** Tránh trường hợp một người lấn át kiểm soát toàn bộ, biến người kia thành "máy đánh máy thuần túy".
- **Xung đột tính cách (Personality clash):** Cần sự cởi mở, tôn trọng lẫn nhau.
- **Ô nhiễm tiếng ồn (Noisy environment):** Thảo luận liên tục có thể ảnh hưởng đến các đồng nghiệp xung quanh trong văn phòng mở.
