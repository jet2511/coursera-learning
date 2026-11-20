# Final Project: Comprehensive AI-Enhanced Business Analysis Portfolio

## 1. Tổng quan Dự án (Project Context)
- **Thời gian ước tính:** 90 phút.
- **Hình thức đánh giá:** Peer-reviewed (chấm chéo giữa các học viên).
- **Format nộp bài:** 6 file riêng biệt (định dạng **DOCX** hoặc **PDF**).
- **Bối cảnh giả lập:** Bạn đóng vai trò Chuyên gia tư vấn phân tích kinh doanh / Kiến trúc sư hệ thống cho một **Ngân hàng trực tuyến (Online Bank)** đang chuẩn bị ra mắt hệ thống phê duyệt trước khoản vay và tiếp nhận khách hàng tự động (**Digital Loan Pre-Approval and Onboarding System**).
- **Phạm vi MVP:**
  - Thu thập dữ liệu KYC.
  - Tra cứu tín dụng sơ bộ (Soft credit pull).
  - Phê duyệt tự động trong vài phút.
  - Định tuyến các ca phức tạp đến giao dịch viên/chuyên viên (manual review queue).
  - Hoạt động đa nền tảng (Web & Mobile), ghi nhận sự đồng thuận của khách hàng (consent log), tuân thủ kiểm toán và bảo mật.
  - *Out-of-scope (MVP):* Đa ngôn ngữ, upload tài liệu phức tạp, tính năng trải nghiệm nâng cao (cross-sell).

---

## 2. Chi tiết 6 Nhiệm vụ & Deliverables cần nộp

### Task 1: Khám phá & Xác định Yêu cầu (`Task1_Discovery_and_Requirements`)
- **Part 1 - Interview Plan:** Tạo kế hoạch phỏng vấn với 10 câu hỏi chia theo 3 nhóm bên liên quan:
  - *Product Team:* Mục tiêu kinh doanh, tính năng.
  - *Compliance Team:* Pháp lý, quy định, kiểm toán.
  - *Operations Team:* Hiệu quả vận hành, quy trình xử lý thủ công.
- **Part 2 - Simulate Interviews:** Dùng AI mô phỏng phỏng vấn dạng Q&A (8–12 cặp hỏi/đáp), làm rõ giả định, rủi ro, ràng buộc hệ thống.
- **Part 3 - Requirements Pack:**
  - Danh sách Yêu cầu chức năng (FR) và phi chức năng (NFR: latency, throughput, RTO/RPO, data retention).
  - Phân loại ưu tiên theo **MoSCoW** (Must, Should, Could, Won't).
  - 8–12 **User Stories** (`As a [user], I want [feature], so that [value]`).
  - Tiêu chí chấp nhận (**Acceptance Criteria**) dạng `Given / When / Then` cho từng story.

---

### Task 2: Mô hình hóa Quy trình & Kiến trúc (`Task2_Process_and_Architecture`)
- **Part 1 - To-Be BPMN Process Model:**
  - Quy trình từ lúc nộp đơn đến khi duyệt tự động hoặc chuyển sang duyệt thủ công.
  - Gồm Gateway kiểm tra điểm tín dụng, nhánh KYC fail, lane review thủ công, thông báo khách hàng (vẽ bằng Mermaid, Lucidchart hoặc Miro).
- **Part 2 - Customer Journey Map:**
  - Trải qua 5 giai đoạn: **Discover → Apply → Pre-approve → Verify → Fund**.
  - Liệt kê hành động (actions), mục tiêu, cảm xúc/pain points và điểm tiếp xúc hệ thống (touchpoints).
- **Part 3 - Component & Data Flow Diagram:**
  - Các thành phần: Web/Mobile App, API Gateway, Credit Bureau API, KYC Service, Core Banking, Audit Logging.
  - Luồng dữ liệu (Data Flow) 2 chiều rõ ràng giữa các service.

---

### Task 3: Quy tắc Kinh doanh, Dữ liệu & Báo cáo (`Task3_Rules_Data_Insights`)
- **Part 1 - Business Rules Catalog:**
  - 6–10 quy tắc kinh doanh dạng `IF / THEN` rõ ràng (Kiểm tra đủ thông tin, logic KYC, ngưỡng điểm tín dụng, retry/backoff khi gọi 3rd-party API, routing quyết định).
- **Part 2 - Data Entities & Attributes:**
  - Bảng thực thể cốt lõi: `Customer`, `Application`, `CreditPull`, `KYCCheck`, `AuditLog`.
  - Mỗi thực thể có 6–8 thuộc tính (kiểu dữ liệu, mô tả, quan hệ giữa các thực thể).
- **Part 3 - Insights & Dashboard Layout:**
  - Định nghĩa 8 KPIs cốt lõi (Tỉ lệ hoàn tất hồ sơ, tỉ lệ duyệt, thời gian xử lý TB, tỉ lệ rớt KYC, khối lượng duyệt thủ công...).
  - Thiết kế bố cục Dashboard (Power BI / Tableau layout: Phễu chuyển đổi, biểu đồ tròn/cột kết quả duyệt, trendline theo tuần, KPI summary cards).

---

### Task 4: Chất lượng, Triển khai & Tuân thủ (`Task4_Quality_Deployment_Compliance`)
- **Part 1 - Test Cases:** 6–10 test cases chuẩn định dạng **Gherkin** (Gồm kịch bản Happy path, KYC lỗi, thiếu data, timeout API tín dụng, retry logic).
- **Part 2 - User Acceptance Testing (UAT) Plan:**
  - Phạm vi UAT, phân công vai trò (PO, QA Lead, Compliance, Ops).
  - Tiêu chí bắt đầu (Entry Criteria) và kết thúc (Exit Criteria - ví dụ: 95% pass, 0 critical bug).
  - Quản lý defect & SLA xử lý theo mức độ nghiêm trọng.
- **Part 3 - Deployment & Rollback Checklist:**
  - Pre-deployment checklist (Code review, feature flags, secrets/creds, monitoring).
  - Post-deployment smoke tests.
  - Chiến lược Rollback (điều kiện kích hoạt, người phê duyệt, tự động vs thủ công, khôi phục dữ liệu).
- **Part 4 - Brief về Compliance, Performance & Scalability:** Tóm tắt SLA/RPO/RTO và kiểm soát tuân thủ.

---

### Task 5: Truyền thông & Tạo khung Platform (`Task5_Communication_Platform_Stubs`)
- **Part 1 - Executive Brief:** Bản tóm tắt dự án 1 trang dành cho Ban lãnh đạo (Vấn đề, giá trị kinh doanh, phạm vi MVP & Out-of-scope).
- **Part 2 - Stakeholder Map & Engagement Plan:** Ma trận phân loại quyền lực/mức độ quan tâm và kế hoạch truyền thông (kênh, tần suất, ma trận RACI).
- **Part 3 - Multilingual Executive Brief:** Bản dịch chuyên nghiệp của Executive Brief sang ngôn ngữ thứ 2 (Tây Ban Nha, Pháp, Đức,...).
- **Part 4 - Platform Implementation Stubs:**
  - **Jira:** 1 Epic tổng quan + 3 User Stories hoàn chỉnh (KYC, soft credit pull, decision engine) kèm Acceptance Criteria.
  - **Confluence:** Khung outline trang tài liệu dự án (Overview, Architecture, Requirements, Risks, Decisions).
  - Liên kết/export các sơ đồ đã vẽ ở Task 2.

---

### Task 6: Báo cáo Đúc kết Sử dụng AI (`Task6_AI_Usage_Reflection`)
- **Part 1 - Tóm tắt Quy trình làm việc với AI:**
  - Liệt kê công cụ AI đã dùng (ChatGPT, Claude, Copilot...).
  - Mô tả cụ thể từng task đã ứng dụng prompt như thế nào, review và hiệu chỉnh kết quả ra sao, phần nào dùng năng lực phân tích cá nhân thay vì dựa hoàn toàn vào AI.
- **Part 2 - Trách nhiệm & Đạo đức khi dùng AI:**
  - Cách bảo vệ dữ liệu nhạy cảm / PII, đối chiếu tính chuẩn xác với nghiệp vụ ngân hàng/tuân thủ, kiểm soát ảo giác (hallucination) và định kiến.
- **Part 3 - Hạn chế của AI & Đánh giá của con người:**
  - Chỉ ra điểm yếu/thiếu sót của AI trong ngữ cảnh chuyên ngành ngân hàng và cách con người can thiệp, điều chỉnh.

---

## 3. Danh sách File nộp bài (Checklist 6 files)
1. `Task1_Discovery_and_Requirements.docx` (hoặc `.pdf`)
2. `Task2_Process_and_Architecture.docx` (hoặc `.pdf`)
3. `Task3_Rules_Data_Insights.docx` (hoặc `.pdf`)
4. `Task4_Quality_Deployment_Compliance.docx` (hoặc `.pdf`)
5. `Task5_Communication_Platform_Stubs.docx` (hoặc `.pdf`)
6. `Task6_AI_Usage_Reflection.docx` (hoặc `.pdf`)
