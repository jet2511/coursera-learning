# Tóm tắt bài học: Kiến trúc hướng sự kiện trên AWS (Event-Driven Architectures on AWS)

**Khóa học:** Course 2 - Architecting Solutions on AWS  
**Chủ đề:** Chi tiết về mô hình Event-Driven, So sánh EventBridge vs SNS, và cơ chế hoạt động của DynamoDB Streams  
**Vị trí:** Module 1 - Designing a serverless web backend on AWS

---

## 1. Bản chất của Kiến trúc hướng sự kiện
* **Định nghĩa:** Kiến trúc sử dụng các sự kiện (Events - sự thay đổi trạng thái của hệ thống, ví dụ: người dùng đặt mua hàng) để kích hoạt và giao tiếp giữa các dịch vụ được tách rời độc lập (Decoupled).
* **Mô hình 3 thành phần cốt lõi:**
  * **Event Producers (Nhà sản xuất):** Nơi phát sinh sự kiện.
  * **Event Routers (Bộ định tuyến):** Nơi tiếp nhận, áp dụng bộ lọc và định tuyến sự kiện.
  * **Event Consumers (Nhà tiêu thụ):** Nơi tiếp nhận sự kiện cuối cùng để xử lý nghiệp vụ.
* **Lợi ích:** Cho phép các dịch vụ thành phần tự co giãn, cập nhật và triển khai độc lập, giúp ứng dụng không bị crash khi lưu lượng truy cập tăng đột biến.

---

## 2. So sánh chi tiết: Amazon EventBridge vs Amazon SNS

| Tiêu chí so sánh | Amazon EventBridge (Event Bus) | Amazon Simple Notification Service - SNS (Pub/Sub) |
| :--- | :--- | :--- |
| **Use Case tối ưu** | Phản ứng lại sự kiện từ các ứng dụng SaaS bên thứ ba hoặc các dịch vụ AWS khác. | Xử lý thông điệp cần thông lượng cực lớn, độ trễ siêu thấp giữa các microservices. |
| **Độ trễ trung bình**| Khoảng **500 mili-giây (0.5 giây)**. | Siêu thấp, **dưới 30 mili-giây**. |
| **Thông lượng** | Có giới hạn mặc định ban đầu (có thể yêu cầu tăng). | Gần như **không giới hạn**. |
| **Độ bao phủ Fan-out**| Thấp hơn SNS. | Cực cao (hỗ trợ hàng ngàn đến hàng triệu endpoint nhận). |
| **Cấu trúc tin nhắn** | Dạng JSON có cấu trúc định nghĩa chặt chẽ. | Không cấu trúc, hỗ trợ mọi định dạng payload. |
| **Cơ chế lọc tin** | Hỗ trợ lọc rất sâu dựa trên nội dung (Body) của tin nhắn bằng các Rules. | Hỗ trợ lọc dựa trên thuộc tính (Attributes) và nội dung tin nhắn (Payload-based). |
| **Đích nhận tin** | Hỗ trợ hơn 15 dịch vụ AWS làm target. | Hỗ trợ 6 loại đích (Lambda, SQS, HTTPS, SMS, Push, Email). |
| **Tích hợp SaaS** | Có tích hợp trực tiếp độc quyền với các đối tác SaaS bên thứ ba. | Không hỗ trợ trực tiếp. |

=> **Lý do chọn SNS:** Đơn giản, độ trễ cực thấp, đáp ứng hoàn hảo nhu cầu truyền tin 1-nhiều (Fan-out) đến 3 dịch vụ hạ nguồn mà không cần đến các tính năng phức tạp của EventBridge.

---

## 3. Tìm hiểu sâu về các dịch vụ bổ trợ

### 3.1. Amazon EventBridge
* Hoạt động như một xe buýt sự kiện (Event Bus) phi máy chủ.
* Sử dụng các **Rules** (Quy tắc) để so khớp cấu trúc sự kiện (Event Pattern) hoặc theo lịch trình (Schedule) để định tuyến tới **Targets**.
* Mọi event đều đi qua một **Event Bus** (mặc định tài khoản có sẵn một default event bus để nhận tin từ các dịch vụ AWS, người dùng có thể tự tạo custom event bus để nhận tin từ các tài khoản/Vùng khác).

### 3.2. Amazon DynamoDB Streams
* **Định nghĩa:** Ghi nhận chuỗi thời gian thực các sự thay đổi dữ liệu ở cấp độ item (thêm, sửa, xóa) trong bảng DynamoDB.
* **Thời gian lưu trữ log:** Tối đa **24 giờ** (sau 24 giờ dữ liệu sẽ tự động bị xóa).
* **Cam kết chất lượng dịch vụ (SLA):**
  1. Mỗi bản ghi thay đổi chỉ xuất hiện **duy nhất một lần** trong luồng (exactly-once).
  2. Các bản ghi xuất hiện trong luồng tuân thủ **đúng trình tự thời gian thực tế** đã xảy ra trên bảng.
* **Hiệu năng:** Hoạt động theo cơ chế bất đồng bộ, hoàn toàn không gây ảnh hưởng hay suy giảm hiệu năng đọc/ghi của bảng DynamoDB gốc. Tự động mã hóa dữ liệu tĩnh (at rest) trong luồng.
