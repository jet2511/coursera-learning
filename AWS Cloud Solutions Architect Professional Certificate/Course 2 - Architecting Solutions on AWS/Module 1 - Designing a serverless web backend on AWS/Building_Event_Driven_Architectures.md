# Tóm tắt bài học: Xây dựng Kiến trúc hướng sự kiện (Building Event-Driven Architectures)

**Khóa học:** Course 2 - Architecting Solutions on AWS  
**Chủ đề:** Tách rời liên kết hệ thống (Decoupling) bằng Amazon SNS, DynamoDB Streams và AWS Lambda  
**Vị trí:** Module 1 - Designing a serverless web backend on AWS

---

## 1. Ý tưởng thiết kế Kiến trúc hướng sự kiện (Event-Driven Architecture)
* **Vấn đề cần giải quyết:** Loại bỏ gánh nặng code xử lý chính (Lambda xử lý đơn hàng) phải tự thực hiện đồng thời các cuộc gọi API tới các dịch vụ hạ nguồn (inventory, accounting, fulfillment). Nếu gộp chung, đây vẫn là một hệ thống monolith thu nhỏ và dễ phát sinh lỗi bất nhất dữ liệu khi một API lỗi.
* **Mô hình 3 thành phần của kiến trúc hướng sự kiện:**
  ```
  Event Producer (Lambda 1) ──> Event Router (SNS Topic) ──> Event Consumers (Downstream APIs)
  ```
  * *Producer (Nhà sản xuất sự kiện):* Phát sinh sự kiện (ví dụ: có đơn hàng mới).
  * *Router (Bộ định tuyến sự kiện):* Tiếp nhận sự kiện, lọc và đẩy sự kiện đến đúng nơi nhận.
  * *Consumer (Nhà tiêu thụ sự kiện):* Tiếp nhận và thực hiện logic nghiệp vụ riêng độc lập.

---

## 2. So sánh lựa chọn dịch vụ Định tuyến sự kiện (Event Router)

### 2.1. Amazon Simple Notification Service (SNS)
* **Mô hình hoạt động:** Publish/Subscribe (Pub/Sub).
* **Đặc điểm:**
  * Hỗ trợ gửi thông điệp dạng **Fan-out** (1-nhiều): Một thông điệp gửi vào SNS Topic sẽ được sao chép và chuyển tiếp đồng loạt đến tất cả các Subscribers đã đăng ký (như HTTPS endpoints, Lambda, SQS...).
  * Hỗ trợ lọc tin nhắn (*Message Filtering*) dựa trên các thuộc tính của tin nhắn (attributes).
* **Ưu thế:** Cực kỳ đơn giản, chi phí rẻ, đáp ứng hoàn hảo cho nhu cầu gửi cùng một thông điệp đơn hàng đến cả 3 dịch vụ hạ nguồn.

### 2.2. Amazon EventBridge (Serverless Event Bus)
* **Đặc điểm:**
  * Rất mạnh mẽ, hỗ trợ kết nối nhiều nguồn sự kiện và đích đến hơn (bao gồm các ứng dụng SaaS bên thứ ba).
  * Hỗ trợ lọc tin nhắn sâu hơn nhiều bằng các quy tắc (*Rules*) dựa trên nội dung của tin nhắn (chứ không chỉ attribute như SNS).
  * Tích hợp *Schema Registry* để quản lý và chuẩn hóa cấu trúc dữ liệu tin nhắn.
* **Nhược điểm:** Phức tạp và có chi phí cao hơn SNS đối với các trường hợp sử dụng đơn giản.

=> **Quyết định:** Chọn **Amazon SNS** vì hệ thống khách hàng chỉ có duy nhất 1 loại tin nhắn đơn hàng tự quản lý cấu trúc, SNS đơn giản và tiết kiệm chi phí hơn.

---

## 3. Giải pháp kết nối: DynamoDB Streams & Lambda
Để kích hoạt gửi sự kiện từ Database sang SNS Topic mà không làm ảnh hưởng đến code xử lý đơn hàng chính:
1. **Kích hoạt DynamoDB Streams:** Trên bảng dữ liệu đơn hàng DynamoDB để ghi nhận luồng thay đổi dữ liệu thời gian thực.
2. **Khởi tạo AWS Lambda 2 (Stream Processor):** Thiết lập trigger lắng nghe sự kiện từ DynamoDB Stream.
3. **Quy trình hoạt động:** Khi có đơn hàng mới được lưu vào bảng DynamoDB -> DynamoDB Stream ghi nhận sự kiện -> Kích hoạt Lambda 2 -> Lambda 2 đọc payload dữ liệu và gọi API của SNS để gửi thông điệp vào SNS Topic -> SNS Topic đẩy tin tới 3 dịch vụ hạ nguồn.

---

## 4. Lợi ích lớn của kiến trúc hướng sự kiện mới
* **Decouple (Tách rời hoàn toàn):** Code xử lý nghiệp vụ đơn hàng (Lambda 1) được cô lập hoàn toàn với hạ nguồn. Nếu hệ thống kế toán hạ nguồn bị sập, việc nhận đơn hàng mới vẫn diễn ra bình thường.
* **Dễ dàng mở rộng (Scalability):** Khi có thêm dịch vụ hạ nguồn mới (ví dụ dịch vụ phân tích dữ liệu - *Analytics service*), chỉ cần đăng ký HTTP endpoint của dịch vụ đó vào SNS Topic hiện có mà **không cần sửa hay deploy lại bất kỳ dòng code nào** của hệ thống xử lý chính.
