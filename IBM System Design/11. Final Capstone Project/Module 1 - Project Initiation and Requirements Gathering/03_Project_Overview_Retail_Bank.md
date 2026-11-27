# Project Overview: Retail Bank Digital Transformation

## 1. Bối cảnh bài toán doanh nghiệp (Business Context)
- **Đối tượng:** Một ngân hàng bán lẻ quy mô vừa (**Mid-sized Retail Bank**).
- **Vấn đề cốt lõi (Pain Points):**
  - Hệ thống bị phân mảnh (**Fragmented systems**) rời rạc giữa các phòng ban.
  - Trùng lặp dữ liệu (**Data duplication**) và dữ liệu thiếu đồng bộ.
  - Vận hành kém hiệu quả (**Operational inefficiencies**), chu kỳ phát hành tính năng/triển khai phần mềm chậm (**Slow deployment cycles**).
  - Khó khăn trong việc đáp ứng kỳ vọng khách hàng, tăng nguy cơ rủi ro tuân thủ quy chế (**Compliance risks**), và suy giảm năng lực cạnh tranh trước các đối thủ số.
- **Mục tiêu:** Thiết kế hạ tầng IT mạnh mẽ, chuyển đổi hệ thống Legacy, xây dựng ứng dụng mới phục vụ khách hàng (Customer-facing application), tối ưu luồng dữ liệu thời gian thực và nâng cao năng lực an ninh bảo mật.

---

## 2. Phân định vai trò: Systems Architect vs. Solutions Architect

| Vai trò | Trọng tâm công việc trong dự án |
| :--- | :--- |
| **Systems Architect** | - Đánh giá & thiết kế hạ tầng doanh nghiệp (Enterprise Infrastructure).<br>- Phân tích yêu cầu phi chức năng (NFRs: Performance, Scalability, High Availability).<br>- Thiết kế kiến trúc bảo mật (Security posture, mã hóa, phân đoạn mạng).<br>- Lập kế hoạch mạng, dịch vụ Cloud và Container orchestration. |
| **Solutions Architect** | - Diễn giải yêu cầu kinh doanh thành luồng ứng dụng cụ thể (Application flow).<br>- Định nghĩa chuẩn giao tiếp API và tích hợp liên hệ thống.<br>- Xây dựng mô hình dữ liệu (Data models) và thiết kế cơ sở dữ liệu.<br>- Đề xuất, ma trận hóa và bảo vệ lựa chọn ngăn xếp công nghệ (Technology stack). |

---

## 3. Bản đồ Deliverables thực chiến qua từng giai đoạn

### Giai đoạn 1: Project Initiation & Requirements Gathering
- **Project Charter:** Định nghĩa phạm vi, mục tiêu kinh doanh, ràng buộc và tiêu chuẩn thành công.
- **Stakeholder Register & Engagement Plan:** Nhận diện và chiến lược tương tác với các bên liên quan theo bối cảnh ngân hàng.
- **Elicitation & Documentation:** Thực hiện phỏng vấn/workshop để xây dựng **BRD** (Business Requirements Document), **SRS** (Software Requirements Specification) và **Use Case Diagrams**.
- **Traceability Matrix (RTM):** Liên kết yêu cầu kỹ thuật với mục tiêu nghiệp vụ.

### Giai đoạn 2: Project Planning & Process Modeling
- **WBS (Work Breakdown Structure):** Phân rã cấu trúc công việc theo từng giai đoạn.
- **SWOT Analysis & Risk Register:** Ma trận rủi ro với các trường bắt buộc: *Risk description, Probability (xác suất), Impact (mức độ ảnh hưởng), Risk rating/category*.
- **Quy trình nghiệp vụ:** Chuyển đổi yêu cầu thành Flowcharts và mô hình UML cho các nghiệp vụ ngân hàng trọng yếu.

### Giai đoạn 3: Enterprise Architecture & Cloud Setup
- **Cloud-Native & Container:** Đóng gói container microservices và bảo mật nền tảng cloud.
- **Data Flow & EDA Blueprint:** Vẽ Data Flow Diagram, xác định nguồn dữ liệu, thành phần ETL, chiến lược mã hóa/bảo mật quyền riêng tư; thiết kế kiến trúc hướng sự kiện (**Event-Driven Architecture**) phục vụ kịch bản ngân hàng real-time.
- **Capacity Planning & Inventory:** Bảng tính toán dung lượng lưu trữ cho dữ liệu giao dịch (**Storage requirements for transactional data**) và danh mục kiểm kê hạ tầng (Hardware, Software, Network).

### Giai đoạn 4: System and Database Design
- **PoC (Proof of Concept):** Xây dựng mẫu thử (API mockup, microservice deployment, cloud integration hoặc real-time data workflow).
- **System Models:** Use case và **Sequence Diagrams** mô tả tương tác từng bước giữa các component.
- **Technology Stack Matrix:** Ma trận lựa chọn giải pháp kèm phân tích lý do chọn lựa (Justification).
- **Database Modeling (3NF):** Thiết kế Conceptual & Logical ERD; chuẩn hóa dữ liệu về dạng chuẩn **3NF**; lập bảng **Data Dictionary** chi tiết (Description, DataType, Size, Constraints, Relationships).

### Giai đoạn 5: Testing & Deployment Strategies
- **Test Planning & Verification:** Rà soát và chú thích test plan đối chiếu qua RTM; viết test case theo chuẩn **TDD** và kịch bản **BDD** bằng cú pháp **Gherkin**.
- **CI/CD & Monitoring:** Đặc tả các giai đoạn trong CI/CD pipeline, phân định trách nhiệm RACI giữa các bên, định nghĩa KPIs, ngưỡng cảnh báo (alert triggers) và lịch trình giám sát định kỳ (daily/weekly/monthly).

### Giai đoạn 6: Final Submission & Evaluation
- **Comprehensive Solution Presentation:** Đóng gói toàn bộ câu chuyện giải pháp: tóm tắt bài toán kinh doanh, sơ đồ kiến trúc, minh họa PoC và bảo vệ các quyết định thiết kế cho Retail Bank thành bộ portfolio chuyên nghiệp.
