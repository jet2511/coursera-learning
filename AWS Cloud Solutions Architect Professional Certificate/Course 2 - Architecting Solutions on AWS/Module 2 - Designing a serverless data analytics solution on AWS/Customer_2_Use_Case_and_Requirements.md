# Tóm tắt bài học: Customer #2 - Use Case & Requirements

**Khóa học:** Course 2 - Architecting Solutions on AWS  
**Chủ đề:** Khảo sát hiện trạng và xác định yêu cầu thiết kế kiến trúc phân tích dữ liệu (Clickstream Analytics)  
**Vị trí:** Module 2 - Designing a serverless data analytics solution on AWS

---

## 1. Hiện trạng hệ thống của khách hàng (Current Architecture State)
* **Lưu trữ & Phục vụ Web:** Sử dụng **Amazon S3 Static Website Hosting** để lưu trữ và phân phối trang HTML menu món ăn.
* **Cập nhật nội dung:** Quản trị viên nhà hàng đăng nhập vào hệ thống quản lý nội bộ để cập nhật trực tiếp file menu (object) trên S3 bucket.
* **Phân phối qua QR Code:** Hệ thống tự động tạo mã QR Code trỏ đến S3 bucket, được in và dán trên từng bàn ăn.
* **Hạn chế hiện tại:** Khách hàng quét mã xem menu nhưng vẫn phải chờ phục vụ đến bàn để ghi món $\rightarrow$ gây độ trễ và chưa tối ưu trải nghiệm.

---

## 2. Nâng cấp tính năng & Phạm vi dự án (Scope Definition)

### A. Ngoài phạm vi (Out of Scope)
* **Lập trình Client-side:** Đội ngũ khách hàng đã tự viết thư viện JavaScript trên web menu để theo dõi tương tác người dùng.
* **Tích hợp cổng thanh toán (Payment Gateway):** Khách hàng đã có API xử lý thanh toán qua bên thứ ba và tự tích hợp nút *"Order this item"*.

### B. Trong phạm vi thiết kế kiến trúc (In Scope)
* Xây dựng giải pháp thu nạp, lưu trữ và xử lý dữ liệu hành vi người dùng (**Clickstream Data Analytics**).
* Cung cấp một **RESTful HTTPS Endpoint** tiếp nhận dữ liệu (qua phương thức HTTP POST) từ thư viện JavaScript của khách hàng.

---

## 3. Mục tiêu phân tích dữ liệu (Clickstream Analytics Goals)
Hệ thống phân tích dữ liệu giúp các nhà hàng tối ưu hóa thực đơn và kinh doanh:
* **Hành vi xem món:** Món nào được xem nhiều nhất? Khách cuộn xem toàn bộ menu hay dừng lại sau món khai vị (*appetizers*) mà không xem món chính (*entrees*)?
* **Tỷ lệ chuyển đổi:** Món nào khách mở xem chi tiết nhưng không thêm vào hóa đơn?
* **Thời gian ra quyết định:** Khoảng thời gian từ khi xem chi tiết món ăn đến khi hoàn tất thanh toán.
* **Báo cáo & Gợi ý (BI & Recommendations):** Cung cấp dữ liệu phiên (*session data*) cho các chuyên viên BI để lập báo cáo và phát triển tính năng gợi ý món ăn tương tự giữa các nhà hàng.

---

## 4. Các yêu cầu phi chức năng & Ràng buộc kiến trúc (Architectural Requirements)

| Tiêu chí | Yêu cầu của khách hàng | Định hướng giải pháp AWS |
| :--- | :--- | :--- |
| **Giao thức tiếp nhận (Ingestion)** | Endpoint chuẩn RESTful qua HTTPS (hỗ trợ HTTP POST). | Sử dụng **Amazon API Gateway** hoặc dịch vụ Ingestion tương thích REST. |
| **Mô hình chi phí (Cost)** | Ưu tiên thanh toán theo lượng sử dụng thực tế (pay-per-use), không trả phí cố định theo thời gian chạy máy chủ. | Lựa chọn các dịch vụ **Serverless**. |
| **Mô hình vận hành (Operations)** | Đội ngũ nhân sự mỏng, không muốn bảo trì hạ tầng, không dùng máy chủ EC2 hay quản lý HĐH. | Dịch vụ **Fully Managed / Serverless** (Amazon S3, AWS Lambda, Amazon Kinesis, v.v.). |
| **Sao lưu & Dự phòng (Disaster Recovery)** | Dữ liệu thu nạp cần được sao lưu tự động sang một **AWS Region khác (Cross-Region Backup)**. | Sử dụng tính năng **S3 Cross-Region Replication (CRR)**. |
| **Bảo mật dữ liệu (Security)** | Mã hóa dữ liệu ở cả hai trạng thái: Lưu trữ (**Encryption at rest**) và Truyền tải (**Encryption in transit**). | HTTPS/TLS cho đường truyền và **AWS KMS / S3-SSE** cho lưu trữ. |

> [!NOTE]
> **Triết lý bảo mật từ Werner Vogels (CTO Amazon):**  
> *"Dance like nobody's watching, encrypt like everyone is."* (Hãy nhảy như không ai nhìn, nhưng hãy mã hóa như thể mọi người đều đang theo dõi).
