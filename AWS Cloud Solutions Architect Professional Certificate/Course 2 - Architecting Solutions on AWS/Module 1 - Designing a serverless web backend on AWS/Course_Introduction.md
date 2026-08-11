# Giới thiệu khóa học: Architecting Solutions on AWS

**Khóa học:** Course 2 - Architecting Solutions on AWS  
**Chủ đề:** Giới thiệu tổng quan nội dung và mục tiêu khóa học  
**Vị trí:** Module 1 - Designing a serverless web backend on AWS

---

## 1. Mục tiêu của khóa học (Course Goal)
Khóa học **Architecting Solutions on AWS** được thiết kế bởi các chuyên gia công nghệ đám mây của AWS nhằm hướng dẫn cách:
* Phân tích các yêu cầu thực tế của khách hàng.
* So sánh các dịch vụ AWS khác nhau để lựa chọn giải pháp phù hợp nhất.
* Lắp ghép các mảnh ghép dịch vụ đơn lẻ thành một giải pháp hoàn chỉnh đáp ứng được mục tiêu kinh doanh và kỹ thuật.
* Khóa học sẽ tiếp cận theo phương pháp thực tế: Bắt đầu mỗi tuần bằng một cuộc gọi giả định giữa **Solutions Architect (SA)** và **Khách hàng** để xác định vấn đề và yêu cầu kỹ thuật.

---

## 2. Lộ trình nội dung chi tiết theo từng tuần (Weekly Roadmap)

### Tuần 1 (Module 1): Thiết kế hệ thống Backend Web Serverless trên AWS
* **Kịch bản khách hàng:** Một công ty bán sản phẩm tẩy rửa trực tuyến đang gặp lỗi gián đoạn hệ thống xử lý đơn hàng online. Họ muốn di chuyển ứng dụng lên AWS để tối ưu tính bền vững và khả năng chịu lỗi (Resiliency).
* **Các dịch vụ trọng tâm học tập:** 
  * **AWS Lambda:** Thực thi code backend dạng serverless.
  * **Amazon SQS (Simple Queue Service):** Hàng đợi tin nhắn để giải phóng liên kết trực tiếp (decoupling) giữa các thành phần.
  * **Amazon SNS (Simple Notification Service):** Gửi thông báo tin nhắn dạng pub/sub.
  * **Amazon API Gateway:** Tạo cổng API nhận request.

### Tuần 2 (Module 2): Thiết kế giải pháp Phân tích Dữ liệu Serverless trên AWS
* **Kịch bản khách hàng:** Một công ty cung cấp giải pháp quét mã QR để tải thực đơn nhà hàng muốn tích hợp thêm tính năng phân tích dữ liệu nhằm phục vụ giải pháp trí tuệ doanh nghiệp (Business Intelligence - BI).
* **Các dịch vụ trọng tâm học tập (Data Analytics):**
  * Thu thập dữ liệu (Data Ingestion), xử lý (Processing) và trực quan hóa (Visualization).
  * **Amazon Athena:** Truy vấn dữ liệu trực tiếp trên S3 bằng SQL thông thường.
  * **Amazon Kinesis:** Thu thập dữ liệu streaming thời gian thực.
  * **Amazon QuickSight:** Thiết lập các Dashboard báo cáo BI trực quan.

### Tuần 3 (Module 3): Thiết kế giải pháp Hybrid cho ứng dụng Container trên AWS
* **Kịch bản khách hàng:** Một công ty bảo hiểm đang vận hành hệ thống tại trung tâm dữ liệu cục bộ (On-premises) cần di chuyển một phần ứng dụng lên AWS tạo thành mô hình Hybrid Cloud (Đám mây lai).
* **Các dịch vụ trọng tâm học tập:**
  * **AWS Direct Connect:** Đường truyền kết nối mạng riêng chuyên dụng từ On-premises tới AWS.
  * **AWS Database Migration Service (DMS):** Di chuyển cơ sở dữ liệu an toàn lên cloud.
  * **NAT Gateway:** Hỗ trợ kết nối Internet chiều đi từ các tài nguyên chạy trong mạng nội bộ bảo mật.

### Tuần 4 (Module 4): Thiết kế giải pháp tuân thủ Quản trị tài khoản và Bảo mật
* **Kịch bản khách hàng:** Một công ty truyền thông đang chạy toàn bộ ứng dụng của nhiều đối tác/khách hàng khác nhau trên chung một tài khoản AWS duy nhất. Họ cần chuyển đổi sang mô hình nhiều tài khoản tách biệt (Multi-account).
* **Các dịch vụ trọng tâm học tập (Governance & Security):**
  * Quản lý ghi nhật ký tập trung (Centralized Logging), chiến lược đa tài khoản (Multi-account strategies) và cơ chế tự động cấp phát tài khoản (Account Vending Machine).
  * **AWS Organizations:** Quản trị tập trung nhiều tài khoản AWS.
  * **AWS IAM Identity Center (Single Sign-On):** Quản lý đăng nhập một lần tập trung.
  * **AWS Service Catalog:** Tạo danh mục dịch vụ được phê duyệt sẵn.
  * **AWS CloudTrail:** Ghi và giám sát lịch sử các hoạt động gọi API trên AWS.
