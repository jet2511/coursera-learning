# Task 1: PoC Scope and Objective Definition

Bảng định nghĩa mục tiêu, phạm vi và tiêu chí thành công cho thử nghiệm PoC kiến trúc lõi số Retail Bank.

---

## 1. Bảng tóm tắt định nghĩa PoC (PoC Overview Table)

| Mục (Section) | Nội dung đặc tả kỹ thuật (Technical Specification) |
| :--- | :--- |
| **PoC Objective (Mục tiêu)** | Kiểm chứng tính khả thi kỹ thuật của kiến trúc **Event-Driven Microservices** sử dụng **Apache Kafka** kết hợp **Java Spring Boot** và **PostgreSQL** để xử lý luồng phát hiện gian lận giao dịch thời gian thực (Real-time Fraud Detection) trước khi đầu tư triển khai quy mô lớn trên nền tảng ngân hàng lõi. |
| **In-Scope (Trong phạm vi)** | 1. Đóng gói container hóa dịch vụ Spring Boot Fraud Detection Service chạy trên Docker.<br/>2. Cấu hình cụm Apache Kafka phân tán với topic `fraud-events` (3 partitions, replication factor = 1 trong sandbox).<br/>3. Xây dựng Producer sinh mã giao dịch và Consumer phân tích quy tắc gian lận (Rule Engine).<br/>4. Lưu trữ trạng thái và lịch sử kiểm toán vào cơ sở dữ liệu quan hệ PostgreSQL (`fraud_event_log`).<br/>5. Đo lường các chỉ số hiệu năng (throughput, p99 latency) và khả năng chịu lỗi (fault-tolerance). |
| **Out-of-Scope (Ngoài phạm vi)** | 1. Xây dựng giao diện đồ họa Web Portal hoặc Mobile App.<br/>2. Đấu nối trực tiếp vào mạng lưới thanh toán thẻ Visa/Mastercard thật hoặc hệ thống Core Mainframe kế thừa.<br/>3. Tích hợp thiết bị bảo mật phần cứng chuyên dụng (Hardware Security Module - HSM).<br/>4. Kiểm thử tải cực hạn quy mô toàn cầu (> 100.000 TPS). |
| **Success Criteria (Tiêu chí đo lường)** | 1. **Độ trễ xử lý (End-to-End Latency):** Thời gian từ khi event đẩy vào Kafka đến khi phân tích và ghi DB hoàn tất < **150 ms** (p99).<br/>2. **Tính toàn vẹn dữ liệu (Message Delivery):** Đạt tỷ lệ **100% không mất mát thông điệp (Zero message loss)** kể cả khi Consumer bị khởi động lại đột ngột.<br/>3. **Tỷ lệ thành công API (API Success Rate):** Đạt **100%** đối với các request hợp lệ.<br/>4. **Thời gian phục hồi (Recovery Time):** Khởi động lại container dịch vụ và kết nối lại Kafka < **5 giây**. |
| **Selected Use Case (Use case được chọn)** | **Real-time Fraud Detection Event Flow:** Giám sát và gắn cờ các giao dịch chuyển tiền có dấu hiệu bất thường (ví dụ: giao dịch vượt hạn mức 100 triệu VNĐ trong đêm, hoặc nhiều giao dịch liên tiếp từ các địa chỉ IP khác nhau) trong thời gian thực. |
| **Assumptions (Giả định thực hiện)** | 1. Thực hiện trên môi trường Sandbox Docker Compose trên máy phát triển cục bộ.<br/>2. Sử dụng bộ dữ liệu giao dịch mẫu (mock dataset) 10.000 bản ghi chuẩn hóa theo định dạng ISO 20022.<br/>3. Các dịch vụ bên thứ ba (Credit Bureau / Sanction List) được mô phỏng qua Mock REST API Server. |
