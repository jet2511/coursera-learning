# Chi Tiết Hướng Dẫn & Đề Bài Final Project: Shop Ease Online AI Chatbot

Tài liệu này cung cấp toàn văn bối cảnh, dữ liệu đầu vào, bảng stakeholders, hướng dẫn từng bước (prompts gợi ý, cấu trúc bảng chuẩn, tiêu chí chấm) để hoàn thiện trọn vẹn 5 Task của Final Project.

---

## I. Bối cảnh tình huống (Business Case Scenario)

### 1. Bối cảnh (Background)
- **Doanh nghiệp:** **Shop Ease Online** – Nhà bán lẻ thương mại điện tử chuyên về điện tử tiêu dùng (consumer electronics) đang trên đà tăng trưởng nhanh.
- **Vấn đề cốt lõi:** Lượng yêu cầu hỗ trợ khách hàng tăng đột biến trong khi hệ thống CSKH vẫn phụ thuộc vào điện thoại viên trực tiếp (live agents) và phản hồi qua email.
- **Hậu quả:** Gây trễ hạn (delays), dịch vụ không đồng đều (inconsistent service) và chi phí vận hành tăng cao (high costs).

### 2. Giải pháp đề xuất (The Proposed Solution)
Triển khai hệ sinh thái **AI-powered Chatbot** có khả năng:
- Hỗ trợ tức thì 24/7.
- Tự động giải đáp các câu hỏi thường gặp (routine FAQs).
- Cung cấp tính năng tra cứu hành trình đơn hàng (order tracking).
- Chuyển giao mượt mà các ca phức tạp cho nhân viên hỗ trợ (seamless human handoff).
- Tích hợp sâu với hệ thống CRM và Order Management System (OMS).
- Hỗ trợ đa ngôn ngữ (multi-language).

### 3. Lợi ích kỳ vọng (Expected Benefits)
- Giảm **30% chi phí dịch vụ khách hàng**.
- Nâng chỉ số hài lòng khách hàng (**CSAT**) từ **78% lên 90%**.
- Tốc độ phản hồi dưới **10 giây**.
- Tăng tỷ lệ chuyển đổi đơn hàng (conversion) ngoài giờ làm việc hành chính.

### 4. Danh sách 7 nhóm Stakeholders chính

| Stakeholder (Role) | Power | Interest | Trách nhiệm chính (Responsibility) |
| :--- | :---: | :---: | :--- |
| **Executive Sponsor (CEO)** | High | High | Định hướng chiến lược và phê duyệt ngân sách/kế hoạch |
| **Program Manager** | High | High | Giám sát và điều phối toàn bộ quá trình triển khai |
| **IT/AI Lead** | Medium | High | Giám sát giải pháp kỹ thuật, tích hợp AI và hệ thống |
| **Customer Service Manager** | Medium | High | Quản lý việc áp dụng, quy trình tiếp nhận và đào tạo đội ngũ |
| **Marketing Manager** | Low | High | Quảng bá, truyền thông giải pháp tới khách hàng |
| **Data Protection Officer (DPO)** | High | Medium | Đảm bảo tuân thủ quyền riêng tư và an toàn dữ liệu (GDPR/privacy) |
| **End Customers** | Low | High | Người dùng cuối trực tiếp tương tác với Chatbot |

---

## II. Chi tiết 5 Task Thực hành, Prompts gợi ý & Yêu cầu sản phẩm

### 🎯 Task 1: Review the Business Case
- **Mục tiêu:** Xác định rõ những gì đã biết, các giả định còn tồn tại, khoảng trống dữ liệu và câu hỏi cần làm rõ trước khi bắt tay thực hiện.
- **Prompt gợi ý:**
  > *"Based on the Shop Ease AI Chatbot Business Case, identify the key goals, challenges, assumptions, data gaps, and clarification questions that a Program Manager should address before implementation."*
- **Quy chuẩn bàn giao:**
  - Bảng gồm 5 cột: `Goal`, `Challenge`, `Assumption`, `Data Gap`, `Clarification Question`.
  - Mỗi cột phải có ít nhất một nội dung bám sát tình huống Shop Ease.
  - **Tên file:** `Task1_BusinessCaseReview.docx` hoặc `.xlsx`.

---

### 🎯 Task 2: Gather Requirements (Functional & Non-Functional)
- **Mục tiêu:** Sử dụng GenAI để brainstorm, phân loại và ưu tiên hóa yêu cầu nghiệp vụ và kỹ thuật.
- **Yêu cầu số lượng:** Tối thiểu **12 yêu cầu** (gồm ít nhất **8 Functional** và **4 Non-Functional**).
- **Phương pháp ưu tiên:** Chuẩn **MoSCoW** (*Must Have*, *Should Have*, *Nice to Have* / *Could Have*).
- **Prompt gợi ý:**
  > *"Based on the Shop Ease AI Chatbot Business Case, identify at least eight functional and four non-functional requirements. Classify them as Must Have, Should Have, or Nice to Have, and provide a short rationale for each."*
- **Quy chuẩn bàn giao:**
  - Bảng gồm các cột: `Requirement Name`, `Type`, `Functional / Non-Functional`, `Priority (MoSCoW)`, `Rationale`.
  - **Tên file:** `Task2_Requirements.docx` hoặc `.xlsx`.

---

### 🎯 Task 3: Develop a RACI Chart
- **Mục tiêu:** Xác lập ma trận phân định trách nhiệm rõ ràng cho **đủ 7 nhóm Stakeholders** theo chuẩn RACI (*Responsible, Accountable, Consulted, Informed*).
- **Prompt gợi ý:**
  > *"Based on the Shop Ease AI Chatbot Business Case, identify key roles and responsibilities for each stakeholder using the RACI format. Include a short role definition and at least one RACI designator for each person."*
- **Quy chuẩn bàn giao:**
  - Bảng gồm các cột: `Stakeholder`, `Role Description`, `RACI Designator(s)`.
  - Đầy đủ 7 nhóm: CEO, Program Manager, IT/AI Lead, CS Manager, Marketing Manager, DPO, End Customers.
  - **Tên file:** `Task3_RACI.docx` hoặc `.xlsx`.

---

### 🎯 Task 4: Map Stakeholder Engagement Strategies
- **Mục tiêu:** Thiết lập chiến lược tương tác tùy biến theo ma trận Quyền lực / Quan tâm (Power/Interest Matrix).
- **Yêu cầu:** Tối thiểu **6 nhóm Stakeholders**.
- **Prompt gợi ý:**
  > *"Based on the Shop Ease AI Chatbot Business Case, develop stakeholder engagement strategies for each stakeholder using the Power/Interest model. Include communication method, frequency, and strategy."*
- **Quy chuẩn bàn giao:**
  - Bảng gồm các cột: `Stakeholder`, `Power`, `Interest`, `Strategy`, `Communication Method`, `Frequency`.
  - **Tên file:** `Task4_StakeholderEngagement.docx` hoặc `.xlsx`.

---

### 🎯 Task 5: Reflection
- **Mục tiêu:** Viết bài phản tư (**200 – 300 từ**) đánh giá trải nghiệm ứng dụng GenAI trong Business Analysis và Program Management.
- **Nội dung bắt buộc phải trả lời:**
  1. GenAI đã giúp đẩy nhanh tiến độ hoặc mang lại góc nhìn sâu sắc ra sao?
  2. Những hạn chế / thiếu sót quan sát được từ phản hồi của AI?
  3. Cách thức BA hoặc Quản lý dự án kiểm chứng (validate) và tinh chỉnh kết quả của AI trước khi đưa vào thực tiễn?
- **Prompt gợi ý:**
  > *"Write a short reflection (200–300 words) describing how AI helped, what limitations you noticed, and how you would validate the AI's outputs."*
- **Quy chuẩn bàn giao:**
  - Đoạn văn/bài luận ngắn 200–300 từ.
  - **Tên file:** `Task5_Reflection.docx` hoặc `.xlsx`.
