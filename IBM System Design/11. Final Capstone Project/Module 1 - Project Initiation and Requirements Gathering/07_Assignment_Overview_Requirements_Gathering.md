# Assignment Overview: Requirements Gathering
**Dự án:** Retail Bank's Digital Core Transformation  
**Giai đoạn:** Thu thập và Quản trị Yêu cầu (Requirements Gathering Lifecycle)  
**Tác giả:** Parikshit Jain  

---

## 1. Giới thiệu tổng quan
Giai đoạn này tập trung vào toàn bộ vòng đời thu thập, phân tích và tài liệu hóa yêu cầu cho dự án chuyển đổi số ngân hàng bán lẻ (**Retail Bank**). 
Mục tiêu là chuyển dịch các mong muốn kinh doanh và ràng buộc pháp lý thành các đặc tả kỹ thuật có khả năng truy vết (**Traceability**) rõ ràng, tuân thủ các khung kiến trúc doanh nghiệp chuẩn mực.

---

## 2. Bốn nhiệm vụ cốt lõi (Core Tasks)

### Task 1: Soạn thảo Business Requirements Document (BRD)
- **Mục tiêu:** Định hình bức tranh tổng thể về mặt nghiệp vụ cho dự án chuyển đổi Core Banking sang Cloud-Native.
- **Nội dung chính:**
  - Định nghĩa phạm vi dự án (Project Scope), mục tiêu chiến lược và các chỉ số đo lường thành công (Success Metrics / KPIs).
  - Ghi nhận các giả định (Assumptions) và ràng buộc (Constraints).
  - Thiết lập tiêu chí thành công có thể đo lường được để hỗ trợ việc lập kế hoạch kiến trúc và đảm bảo tuân thủ quy chế tài chính (KYC, AML, PCI-DSS, GDPR).

### Task 2: Khai thác yêu cầu qua phỏng vấn & workshop (Requirements Elicitation)
- **Đối tượng khai thác:** Product Owners, Compliance Teams (Đội ngũ tuân thủ), DevOps Engineers, và Khách hàng/Người dùng cuối.
- **Phân loại yêu cầu thu thập:**
  - **Yêu cầu chức năng (Functional Requirements - FRs):** Quy trình eKYC Onboarding tự động, xử lý giao dịch thanh toán, quy trình thẩm định cho vay, báo cáo kiểm toán tự động.
  - **Yêu cầu phi chức năng (Non-Functional Requirements - NFRs):** Độ khả dụng (Uptime ≥ 99.99%), hiệu năng xử lý (Latency < 1s), mức độ tự động hóa triển khai (CI/CD Automation), tiêu chuẩn mã hóa và bảo mật nhiều lớp.
- Ánh xạ trực tiếp các phản hồi này vào các mục tiêu kinh doanh chiến lược của ngân hàng.

### Task 3: Xây dựng sơ đồ Use Case và kịch bản luồng (Use Case Diagram & Flow Descriptions)
- **Mục tiêu:** Trực quan hóa ranh giới hệ thống (System Boundaries) và phân định trách nhiệm của các tác nhân (Actors).
- **Tác nhân tham gia (Actors):** Internal Teams (Giao dịch viên, Quản trị viên, Kiểm toán viên), End Customers (Khách hàng cá nhân), và Regulators (Cơ quan quản lý/Ngân hàng Trung ương).
- **Kịch bản chính cần mô hình hóa:**
  - Quy trình mở tài khoản và định danh khách hàng (Customer Onboarding & eKYC).
  - Quy trình giám sát và báo cáo tuân thủ phòng chống gian lận (Compliance & Fraud Monitoring).
  - Quy trình tự động hóa triển khai hệ thống (Automated Deployment & CI/CD).
  - Hệ thống báo cáo định kỳ và đột xuất cho cơ quan thanh tra (Regulatory Reporting).

### Task 4: Xây dựng ma trận truy vết yêu cầu (Requirements Traceability Matrix - RTM)
- **Công cụ:** Bảng tính Excel / Markdown Table.
- **Ý nghĩa kỹ thuật:** Đảm bảo mỗi yêu cầu nghiệp vụ đều được hiện thực hóa bởi các thành phần kiến trúc cụ thể và có phương án kiểm thử xác minh tương ứng (End-to-End Traceability).
- **Các trường thông tin bắt buộc trong RTM:**
  - Mã yêu cầu (Requirement ID) & Phân loại (Business, Functional, Non-Functional).
  - Mục tiêu kinh doanh liên kết (Business Objective).
  - Tiêu chí chấp nhận (Acceptance Criteria).
  - Phương pháp xác minh / kiểm thử (Verification Method: Unit, Integration, Security Pentest, UAT).
  - Ghi chú rủi ro liên quan (Risk Notes).

---

## 3. Danh mục sản phẩm bàn giao (Deliverables Checklist)

- [ ] **1. Business Requirements Document (BRD):** Văn bản tổng hợp đầy đủ phạm vi, mục tiêu, giả định và số liệu đo lường.
- [ ] **2. Use Case Diagram & Flow Descriptions:** Sơ đồ Use Case tương tác giữa Tác nhân - Hệ thống kèm mô tả chi tiết các luồng chính/phụ (Main/Alternate flows).
- [ ] **3. Requirements Traceability Matrix (RTM):** Ma trận truy vết kết nối Requirement $\rightarrow$ Architecture $\rightarrow$ Test Method & Acceptance Criteria.
