# Assignment Overview: EDA Blueprint (Event-Driven Architecture)
**Module:** Module 3 - Enterprise Architecture and Cloud Setup  
**Dự án:** Retail Bank's Digital Core Transformation  
**Tác giả:** Parikshit Jain  

---

## 1. Giới thiệu tổng quan
Giai đoạn này tập trung vào việc thiết kế **Bản thiết kế kiến trúc hướng sự kiện (EDA Blueprint - Event-Driven Architecture)** cho Ngân hàng bán lẻ (**Retail Bank**). 
Mục tiêu là hỗ trợ năng lực xử lý giao dịch thời gian thực (**Real-time transaction monitoring**), phát hiện gian lận tức thì (**Immediate fraud detection**), và gửi cảnh báo tự động đến khách hàng (**Instant customer notifications**). Bản thiết kế mô tả rõ ràng luồng sự kiện (Event flow), cơ chế đảm bảo độ tin cậy (Reliability & Fault tolerance) và các biện pháp bảo mật dữ liệu cấp ngân hàng.

---

## 2. Bốn nhiệm vụ cốt lõi (Core Tasks)

### Task 1: Nhận diện các thành phần EDA (EDA Components)
Phân loại và mô tả chi tiết 3 nhóm thành phần chính trong hệ sinh thái EDA của ngân hàng:
- **Event Producers (Nguồn phát sự kiện):** Các hệ thống giao dịch phát sinh sự kiện như Core Banking (chuyển tiền), POS/ATM Terminal (quẹt thẻ/rút tiền), Mobile Banking App, và Payment Gateway.
- **Event Brokers (Bộ điều phối & hàng đợi sự kiện):** Nền tảng phân tán đóng vai trò trung gian tiếp nhận, phân loại và định tuyến thông điệp như Apache Kafka, IBM Event Streams, hoặc AWS Kinesis / Amazon SQS.
- **Event Consumers (Bên tiêu thụ sự kiện):** Các microservices độc lập đăng ký lắng nghe sự kiện để kích hoạt xử lý nghiệp vụ như Fraud Detection Engine (Phát hiện gian lận), Notification Service (Gửi SMS/Push), Audit Logging Service, và Real-time Analytics Dashboard.

### Task 2: Thiết kế sơ đồ kiến trúc EDA (EDA Architecture Diagram)
- Xây dựng sơ đồ trực quan thể hiện luồng di chuyển của sự kiện từ Producers $\rightarrow$ Broker $\rightarrow$ Consumers.
- Tích hợp các cơ chế đảm bảo độ tin cậy và tự phục hồi (Reliability features):
  - **Retry Mechanism (Cơ chế thử lại):** Tự động thử lại khi consumer gặp sự cố tạm thời (transient failure).
  - **Dead-Letter Queue - DLQ (Hàng đợi thông điệp chết):** Cô lập các thông điệp bị lỗi định dạng hoặc lỗi logic nghiệp vụ sau số lần thử lại tối đa mà không làm nghẽn toàn bộ hàng đợi.
- Đính kèm các nhãn bảo mật an toàn truyền tải: Mã hóa **TLS 1.3** và xác thực hai chiều mTLS.

### Task 3: Xây dựng bảng ánh xạ sự kiện (Event Mapping Table)
- Lập bảng tổng hợp chuẩn mực liên kết các trường thông tin:
  - **Event Type (Tên loại sự kiện):** ví dụ: `TransactionInitiated`, `FraudSuspected`, `PaymentSuccessful`.
  - **Producer (Nguồn sinh sự kiện):** ví dụ: Mobile App, POS Terminal, Core Banking.
  - **Topic Name (Tên kênh/chủ đề trong Broker):** ví dụ: `banking.transactions.v1`, `banking.fraud.alerts`.
  - **Consumers (Các hệ thống tiêu thụ):** ví dụ: Fraud Detection Engine, Push Notification Service, Accounting Ledger.

### Task 4: Kiểm chứng các thành phần kiến trúc EDA (Mini-checklist)
- Rà soát tính đầy đủ của bản thiết kế:
  - Sự hiện diện của Message Broker chịu lỗi cao.
  - Cơ chế Retry và Dead-Letter Queue (DLQ).
  - Sự tham gia của nhiều Producers và Consumers độc lập (Loose coupling).
  - Gắn nhãn mã hóa an toàn dữ liệu đang truyền tải (TLS encryption).

---

## 3. Danh mục sản phẩm bàn giao (Deliverables Checklist)

- [ ] **1. EDA Architecture Diagram:** Sơ đồ kiến trúc EDA trực quan hóa luồng sự kiện, Retry, DLQ và nhãn bảo mật (.png hoặc .pptx).
- [ ] **2. Event Mapping Table:** Bảng định nghĩa ánh xạ sự kiện (Event Type $\leftrightarrow$ Producer $\leftrightarrow$ Topic $\leftrightarrow$ Consumer).
- [ ] **3. EDA Architecture Mini-Checklist:** Bảng kiểm tra đối soát xác nhận các tính năng độ tin cậy và an ninh mạng.
