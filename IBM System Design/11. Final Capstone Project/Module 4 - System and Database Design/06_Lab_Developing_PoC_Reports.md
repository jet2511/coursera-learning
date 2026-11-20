# 06 - Lab Guide: Developing Proof of Concept (PoC) Reports

- **Thời lượng ước tính:** 30 phút
- **Tác giả:** Parikshit Jain
- **Vai trò:** Systems and Solutions Architect
- **Bối cảnh (Scenario):** Ngân hàng bán lẻ đang hiện đại hóa nền tảng số. Trước khi triển khai sản xuất diện rộng (full-scale rollout), nhóm kiến trúc sư phải thẩm định tính khả thi kỹ thuật của các thành phần kiến trúc trọng yếu thông qua việc xây dựng Prototype thu nhỏ và lập Báo cáo PoC.

---

## 1. Công cụ & Biểu mẫu mẫu (Template)
- **Biểu mẫu tham chiếu:** `Template-Developing PoC Report.docx / .pdf`.
- **Mục tiêu nộp bài:** Báo cáo PoC hoàn chỉnh phục vụ Hội đồng Đánh giá Kiến trúc (Architecture Review Board).

---

## 2. Chi tiết 6 nhiệm vụ thực hiện (Tasks to be performed)

### Task 1: Define PoC Scope and Objective
- **PoC Objective:** Kiểm chứng tính khả thi của kiến trúc xử lý sự kiện thời gian thực (Real-time Event Processing) bằng Kafka kết hợp Spring Boot Microservice và PostgreSQL.
- **Scope (In-scope & Out-of-scope):**
  - *In-scope:* Đóng gói microservice với Docker, luồng đẩy và tiêu thụ sự kiện qua Kafka topic `fraud-events`, ghi nhật ký giao dịch vào PostgreSQL, đo lường độ trễ (latency < 150ms), kiểm tra không mất dữ liệu.
  - *Out-of-scope:* Giao diện người dùng Web/Mobile, tích hợp HSM phần cứng thật, kiểm thử tải cực hạn (>100.000 TPS).
- **Success Criteria:** Độ trễ xử lý < 150ms, tỷ lệ mất message = 0%, dịch vụ tự phục hồi khi restart < 5 giây.
- **Use Case đã chọn:** *Real-time Fraud Detection Event Flow (Luồng sự kiện phát hiện gian lận giao dịch thời gian thực).*
- **Assumptions:** Chạy trên môi trường Sandbox Docker cục bộ, dữ liệu giao dịch mẫu giả lập (mock transaction dataset).

### Task 2: Build a Small-Scale Prototype
- Dựng cụm dịch vụ qua Docker Compose:
  1. `Spring Boot Microservice` (Cổng tiếp nhận và phân tích gian lận, port 8080).
  2. `Apache Kafka & Zookeeper/KRaft` (Hàng đợi sự kiện giao dịch, topic `fraud-events`, port 9092).
  3. `PostgreSQL Database` (Bảng lưu log `fraud_event_log`, port 5432).

### Task 3: Document Test Scenarios and Outcomes
- Thiết lập và thực thi 4 kịch bản kiểm thử đo lường:
  - **TC01:** Publish batch 100 sự kiện liên tục -> Đo lường độ trễ xử lý end-to-end.
  - **TC02:** Khởi động lại Kafka Consumer trong lúc bắn tải -> Xác thực cơ chế không mất tin nhắn (Zero message loss).
  - **TC03:** Gọi API giả lập thẩm định điểm tín dụng/gian lận bên ngoài -> Xác thực mã phản hồi HTTP 200 OK và timeout handling.
  - **TC04:** Giả lập mất kết nối Database tạm thời -> Kiểm tra cơ chế tự động thử lại (Retry logic & Dead Letter Queue).

### Task 4: Capture Findings, Limitations, and Recommendations
- Phân loại kết quả theo 4 nhóm: *Performance, Integration, Security, Deployment*.
- Ghi nhận các giới hạn kỹ thuật của Prototype (dataset nhỏ, chưa bật mã hóa SSL, chưa clustering multi-zone).
- Đưa ra đề xuất cải tiến cho giai đoạn Production.

### Task 5: Evaluate PoC Against Success Criteria
- Lập bảng ánh xạ giữa kết quả thực tế và các chỉ số thành công đo lường được.
- Đưa ra quyết định đánh giá: **Conditional-Go** (Cho phép triển khai giai đoạn kế tiếp nhưng phải hoàn thành cấu hình SSL/OAuth2 và K8s Auto-scaling trước khi Go-Live).

### Task 6: Validate Your PoC Report
- Kiểm tra toàn bộ 8 tiêu chí kiểm thử chất lượng văn bản trước khi ký duyệt nộp bài.
