# Tóm tắt bài học: Khám phá dịch vụ AWS Lambda (AWS Lambda Exploration)

**Khóa học:** Course 2 - Architecting Solutions on AWS  
**Chủ đề:** Khám phá cấu hình chi tiết, cách tạo, liên kết trigger và test hàm Lambda trên AWS Console  
**Vị trí:** Module 1 - Designing a serverless web backend on AWS

---

## 1. Quy trình tạo hàm Lambda mới trên Console
1. **Đặt tên hàm (Function name).**
2. **Chọn Runtime (Môi trường thực thi):**
   * Lambda hỗ trợ sẵn nhiều ngôn ngữ phổ biến: `.NET`, `Go`, `Java`, `Node.js`, `Python`, `Ruby`.
   * **Custom Runtime:** Nếu ngôn ngữ bạn muốn sử dụng không nằm trong danh sách hỗ trợ sẵn, bạn có thể tự thiết lập môi trường chạy tùy chỉnh.
   * *Ví dụ trong bài học:* Sử dụng `Python 3.9`.
3. **Execution Role (Vai trò thực thi):**
   * Cấp quyền hạn để Lambda truy cập các tài nguyên AWS khác (ví dụ: ghi file vào S3, gửi thông báo qua SNS).
   * Khi thực thi, Lambda sẽ giả lập (*assume*) IAM Role được gán để thực hiện các thao tác này.
4. **Cấu hình nâng cao (Advanced settings):**
   * **Enable VPC functionality:** Cho phép Lambda chạy trong VPC để truy cập bảo mật tới các tài nguyên nội bộ (như cơ sở dữ liệu Amazon RDS nằm trong private subnets).

---

## 2. Các thành phần chính trong Function Overview

### 2.1. Triggers (Bộ kích hoạt)
* Lambda có thể được kích hoạt bởi rất nhiều nguồn sự kiện khác nhau: `API Gateway`, `Application Load Balancer (ALB)`, `CloudFront`, `CloudWatch Logs`, `DynamoDB`, `EventBridge`, `Kinesis`...
* **Amazon EventBridge:** Giúp tích hợp và kích hoạt Lambda từ các sự kiện của ứng dụng bên thứ ba (SaaS) bên ngoài môi trường AWS.
* *Thiết lập cụ thể:* Tạo một cổng **API Gateway** loại **HTTP API** (đơn giản, hiệu năng cao, tích hợp trực tiếp, không cần biến đổi dữ liệu) và cấu hình chế độ bảo mật mở (*Open*) để kiểm thử.

### 2.2. Code Tab (Trình soạn thảo mã nguồn)
* Console cung cấp một trình biên tập trực quan phù hợp với các hàm ngắn, đơn giản. Đối với các gói mã nguồn lớn hoặc có nhiều thư viện phụ thuộc (*dependencies*), bạn cần đóng gói (zip/container image) và tải lên.
* **Lambda Handler:** Điểm khởi chạy của hàm, nhận vào hai tham số:
  * `event`: Chứa dữ liệu đầu vào (payload) của request.
  * `context`: Chứa thông tin về lượt thực thi hiện tại (thời gian chạy còn lại, ID lượt chạy...).

### 2.3. Configuration Tab (Cấu hình bổ sung)
* **Environment Variables (Biến môi trường):** Cấu hình các cặp key-value để mã nguồn sử dụng mà không cần sửa code.
* **Tags:** Phân loại tài nguyên, phục vụ cho bộ lọc hoặc theo dõi hóa đơn chi phí.
* **Monitoring & Operations:** Tích hợp mặc định với **Amazon CloudWatch Logs** để lưu trữ log hệ thống (Lambda runtime logs) và log nghiệp vụ (Application logs) tại một nơi tập trung.

### 2.4. Test Tab (Kiểm thử chức năng)
* Tạo các sự kiện giả lập (*test events*) bằng file JSON (ví dụ mẫu Hello World) để chạy thử và kiểm tra ngay kết quả phản hồi của hàm Lambda trực tiếp trên AWS Console.
