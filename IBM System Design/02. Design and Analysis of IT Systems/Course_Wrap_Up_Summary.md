# Course Wrap-Up: Design and Analysis of IT Systems (Tổng Kết Khóa Học)

---

## 1. Thiết Kế & Mô Hình Hóa Hệ Thống (System Design and Modeling)

### Data Flow Diagrams (DFDs) - Sơ đồ luồng dữ liệu
- **Mục đích:** Minh họa cách dữ liệu di chuyển, xử lý và lưu trữ trong hệ thống.
- **Cấu trúc phân tầng (Hierarchy of Levels):**
  - **Context Diagram (Mức ngữ cảnh):** Góc nhìn tổng thể mức cao nhất, xem toàn bộ hệ thống là 1 process duy nhất tương tác với các External Entities.
  - **Level 0 Diagram:** Phân rã tiến trình đơn lẻ từ Context Diagram thành các tiến trình chính (major processes), kho dữ liệu (data stores) và luồng dữ liệu (data flows).
  - **Level 1 Diagram:** Phân rã chi tiết từng tiến trình Level 0 thành các tiến trình con (sub-processes).
  - **Level 2, 3...:** Đào sâu độ chi tiết cho các tiến trình nghiệp vụ phức tạp.

### Entity Relationship Diagrams (ERDs) - Sơ đồ quan hệ thực thể
- **Mục đích:** Chuyển đổi yêu cầu nghiệp vụ thành thiết kế cơ sở dữ liệu có cấu trúc.
- **Quy trình xây dựng:** Xác định quy tắc nghiệp vụ (Business Rules) $\rightarrow$ Định danh các thực thể (Entities) & thuộc tính (Attributes) $\rightarrow$ Xác định mối quan hệ (Relationships: 1-1, 1-N, N-N).
- **Chuẩn hóa dữ liệu (Normalization):** Tổ chức dữ liệu nhằm loại bỏ dư thừa (redundancy) và ngăn ngừa các dị thường (anomalies) khi thêm/sửa/xóa.

### Unified Modeling Language (UML) - Ngôn ngữ mô hình hóa thống nhất
- **Class Diagram:** Mô hình hóa kiến trúc tĩnh (static architecture) — gồm các class, thuộc tính (attributes), phương thức (operations/methods) và mối quan hệ (association, inheritance, dependency).
- **Sequence Diagram:** Mô hình hóa hành vi động (dynamic behavior) — thể hiện sự tương tác, truyền thông điệp giữa các đối tượng theo trục thời gian để hoàn thành một ca sử dụng.
- **Activity Diagram:** Mô hình hóa luồng công việc/hoạt động (workflows, business processes, use cases).
- **State Diagram:** Mô hình hóa vòng đời của một đối tượng đơn lẻ qua các trạng thái (states) và sự kiện chuyển trạng thái (event transitions).

---

## 2. Phân Tích Hệ Thống & Tái Thiết Quy Trình (System Analysis & BPR)

### Đánh giá hiệu năng hệ thống (System Performance Assessment)
- Đo lường 5 chỉ số cốt lõi:
  - **Response Time:** Thời gian phản hồi.
  - **Throughput:** Thông lượng xử lý giao dịch.
  - **Resource Utilization:** Mức độ sử dụng tài nguyên (CPU, RAM, Disk, Network).
  - **Reliability:** Độ tin cậy và khả năng chịu lỗi.
  - **Scalability:** Khả năng mở rộng khi khối lượng tải tăng.

### Tái thiết quy trình nghiệp vụ (Business Process Re-engineering - BPR)
- Phân tích hiện trạng (**As-Is State**) và thiết kế quy trình tương lai (**To-Be State**) áp dụng công nghệ mới.
- BPR là phương pháp chiến lược để chuyển đổi toàn diện quy trình làm việc (transform workflows), không chỉ đơn thuần là chỉnh sửa nhỏ lẻ.
- **System Documentation & Mapping:** Lập tài liệu chi tiết cấu trúc hệ thống và dùng sơ đồ trực quan để ánh xạ luồng dữ liệu & quy trình.

---

## 3. Hệ Thống Thông Tin Doanh Nghiệp (Enterprise IT Systems)
- Các nền tảng phần mềm hợp nhất, tự động hóa quy trình và tối ưu hóa vận hành liên phòng ban:
  - **ERP (Enterprise Resource Planning):** Quản trị nguồn lực doanh nghiệp.
  - **CRM (Customer Relationship Management):** Quản trị quan hệ khách hàng.
  - **SCM (Supply Chain Management):** Quản trị chuỗi cung ứng.
  - **HRM (Human Resource Management):** Quản trị nhân sự.
- **Đánh giá mức độ phù hợp (System Fit):** Xem xét tính năng (Functionality), trải nghiệm người dùng (UX), tích hợp (Integration), khả năng mở rộng (Scalability), chi phí (Cost efficiency) và tuân thủ (Compliance).
- **Đánh giá UI/UX:** Sử dụng Heuristic review, User testing, A/B testing, Analytics, Accessibility checks, Task analysis và Prototype testing.

---

## 4. Đánh Giá Giải Pháp & Phân Tích Tính Khả Thi (Solution Evaluation & Feasibility)

### So sánh và lựa chọn giải pháp IT (Comparing Solutions)
- Các tiêu chí so sánh: Tính năng, Khả năng mở rộng, Tích hợp, Chi phí (TCO), Dễ sử dụng, Bảo mật, Độ uy tín nhà cung cấp (Vendor viability), Thời gian triển khai.
- **Phương pháp ma trận trọng số (Weighted Scoring Matrix):**
  1. Xác định danh sách các giải pháp tiềm năng.
  2. Định nghĩa bộ tiêu chí đánh giá.
  3. Gán trọng số (%) cho từng tiêu chí.
  4. Chấm điểm từng giải pháp theo tiêu chí.
  5. Tính tổng điểm có trọng số để đưa ra quyết định tối ưu.

### Phân tích tính khả thi (Feasibility Analysis)
- **Cost-Benefit Analysis (Khả thi kinh tế):** So sánh tổng chi phí đầu tư (TCO) với lợi ích kỳ vọng (ROI / NPV) để đảm bảo hiệu quả tài chính.
- **Operational Feasibility (Khả thi vận hành):** Đánh giá năng lực của tổ chức trong việc tiếp nhận, đào tạo nhân viên và duy trì giải pháp hiệu quả.

### Quản trị rủi ro (Risk Management)
- Nhận diện và lập kế hoạch giảm thiểu rủi ro ảnh hưởng đến: Kiểm soát chi phí, thành công của dự án, tính liên tục kinh doanh (Business Continuity), sự hài lòng của người dùng và tuân thủ bảo mật.

---

## 5. Tổng Kết Các Kỹ Năng Thực Hành Đã Đạt Được
- Xây dựng mô hình hệ thống hoàn chỉnh bằng DFD (Context, Level 0, Level 1), ERD và UML (Class, Sequence, Activity).
- Lập tài liệu As-Is, phân tích điểm nghẽn (Pain points) và đánh giá độ phù hợp của hệ thống.
- Đánh giá giải pháp theo ma trận trọng số và phân tích khả thi kỹ thuật/kinh tế/vận hành (TELOS).
- Xây dựng **Chiến lược chuyển đổi số hoàn chỉnh (Digital Transformation Strategy)** cho doanh nghiệp bán lẻ bao gồm phân tích FR/NFR, kiến trúc Cloud Unified Commerce và lộ trình triển khai 9 tháng.
