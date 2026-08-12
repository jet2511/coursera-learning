# Tóm tắt bài học: Chào mừng đến với khóa học (Welcome to the Course)

**Khóa học:** Course 2 - Architecting Solutions on AWS  
**Chủ đề:** Giới thiệu tổng quan lộ trình học tập  
**Vị trí:** Module 1 - Designing a serverless web backend on AWS

---

## 1. Tổng quan khóa học
* **Vị trí:** Đây là khóa học thứ 2 trong số 4 khóa học của chương trình chứng chỉ chuyên nghiệp **AWS Cloud Solutions Architect Professional Certificate**.
* **Mục tiêu:** Trang bị kiến thức và tư duy thiết kế giải pháp hạ tầng CNTT an toàn, có khả năng phục hồi cao (resilient), bảo mật (secure) và có tính sẵn sàng cao (highly available) trên AWS Cloud.
* **Phương pháp tiếp cận:** Học tập qua các tình huống thực tế (scenarios). Mỗi tuần, một khách hàng giả định sẽ đưa ra yêu cầu cụ thể, các giảng viên (Morgan & Raf) sẽ phân tích lựa chọn, vẽ sơ đồ thiết kế kiến trúc trên bảng trắng và giải thích chi tiết.

---

## 2. Chi tiết lộ trình học tập 4 tuần

### Tuần 1: Thiết kế hệ thống Backend Web Serverless trên AWS
* **Kịch bản:** Một doanh nghiệp thương mại điện tử cần di chuyển (migrate) dịch vụ web backend của họ lên AWS để khắc phục các sự cố hiện tại.
* **Các dịch vụ nghiên cứu:**
  * **Amazon API Gateway:** Cổng API quản lý các request.
  * **AWS Lambda:** Công cụ tính toán serverless thực thi logic code theo sự kiện.
  * **Amazon SQS:** Hàng đợi tin nhắn hỗ trợ truyền tin bất đồng bộ và giảm liên kết trực tiếp giữa các dịch vụ.
  * **Amazon SNS:** Hệ thống pub/sub gửi thông báo sự kiện.
  * **Amazon DynamoDB:** Cơ sở dữ liệu NoSQL lưu trữ thông tin có tốc độ truy xuất nhanh.

### Tuần 2: Thiết kế giải pháp Phân tích Dữ liệu Serverless trên AWS
* **Kịch bản:** Một công ty phần mềm cần xây dựng hệ thống phân tích dữ liệu clickstream (luồng nhấp chuột) để thu thập các phân tích hành vi người dùng.
* **Các dịch vụ nghiên cứu:**
  * **Amazon S3:** Hồ dữ liệu lưu trữ đối tượng (Data Lake).
  * **Amazon Kinesis Data Firehose:** Truyền tải luồng dữ liệu thời gian thực vào các kho lưu trữ.
  * **Amazon Athena:** Truy vấn dữ liệu dạng ad-hoc trực tiếp trên S3 bằng SQL.
  * **Amazon QuickSight:** Công cụ BI trực quan hóa dữ liệu và xây dựng báo cáo Dashboard.

### Tuần 3: Thiết kế giải pháp Hybrid cho ứng dụng Container trên AWS
* **Kịch bản:** Một doanh nghiệp bảo hiểm lớn cần di chuyển một phần khối lượng công việc đang chạy dạng Container ở máy chủ vật lý cục bộ lên AWS theo mô hình đám mây lai (Hybrid Cloud).
* **Các dịch vụ nghiên cứu:**
  * **AWS Direct Connect:** Kết nối mạng riêng tốc độ cao và ổn định từ on-premises tới AWS.
  * **Amazon ECS (Elastic Container Service):** Quản lý và điều phối các ứng dụng container.
  * **Amazon ECS Anywhere:** Chạy và quản lý container trên hạ tầng on-premises thông qua bảng điều khiển ECS của AWS.
  * **Amazon RDS:** Cơ sở dữ liệu quan hệ được quản lý hoàn toàn bởi AWS.
  * **AWS Systems Manager:** Quản lý cấu hình và vận hành tập trung cho các máy chủ lai.

### Tuần 4: Thiết kế giải pháp tuân thủ Quản trị tài khoản và Quản lý tốt nhất
* **Kịch bản:** Một công ty khởi nghiệp (startup) cần hướng dẫn cách thiết kế chiến lược quản lý đa tài khoản tuân thủ các quy tắc quản trị hạ tầng (governance) và bảo mật nghiêm ngặt.
* **Các dịch vụ nghiên cứu:**
  * **AWS Organizations:** Nhóm và quản trị tập trung nhiều tài khoản AWS.
  * **AWS IAM Identity Center:** Quản lý truy cập Single Sign-On (SSO) và phân quyền tập trung cho nhân sự.
  * **AWS CloudTrail:** Theo dõi và kiểm toán lịch sử các hành động gọi API trên tài khoản.
