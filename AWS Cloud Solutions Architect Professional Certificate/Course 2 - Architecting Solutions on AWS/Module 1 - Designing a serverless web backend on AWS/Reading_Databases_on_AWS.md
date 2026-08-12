# Tóm tắt bài học: Cơ sở dữ liệu trên AWS (Databases on AWS)

**Khóa học:** Course 2 - Architecting Solutions on AWS  
**Chủ đề:** Phân tích chi tiết về Amazon Aurora, RDS Proxy, và Amazon DynamoDB  
**Vị trí:** Module 1 - Designing a serverless web backend on AWS

---

## 1. Triết lý Cơ sở dữ liệu chuyên dụng (Purpose-built Databases)
* **Triết lý của AWS:** Mỗi dịch vụ cơ sở dữ liệu của AWS được thiết kế tối ưu cho một hoặc một tập hợp các tình huống sử dụng cụ thể. Việc lựa chọn cơ sở dữ liệu phù hợp nhất giúp tiết kiệm đáng kể thời gian lập trình.
* **Thay đổi tư duy:** Tránh việc lạm dụng cơ sở dữ liệu quan hệ cho mọi bài toán như trước đây. AWS giúp dễ dàng triển khai và vận hành nhiều loại database (SQL, NoSQL, Cache...) mà không cần quản lý hạ tầng hay bị giới hạn bởi kỹ năng quản trị DB trong nhà.

---

## 2. Chi tiết các dịch vụ cơ sở dữ liệu

### 2.1. Amazon Aurora
* **Định nghĩa:** Động cơ cơ sở dữ liệu quan hệ được quản lý hoàn toàn, tương thích cao với MySQL và PostgreSQL.
* **Hiệu năng vượt trội:** Cung cấp thông lượng (throughput) gấp 5 lần MySQL tiêu chuẩn và gấp 3 lần PostgreSQL tiêu chuẩn mà không cần chỉnh sửa mã nguồn ứng dụng.
* **Cơ chế lưu trữ:** Sử dụng phân vùng lưu trữ phân tán, hiệu năng cao, tự động mở rộng dung lượng lên đến **128 TiB**. Aurora tự động xử lý các tác vụ phức tạp nhất như phân cụm (clustering) và sao chép (replication).
* **Aurora Serverless v2:** Tự động giám sát và điều chỉnh dung lượng tính toán (capacity) theo thời gian thực dựa trên nhu cầu ứng dụng, giúp tiết kiệm chi phí cho các tải biến động mạnh (multitenant DB, môi trường dev/test).
* *Lý do không chọn:* Khách hàng chỉ có nhu cầu lưu trữ đơn giản, không cần đến các tính năng quan hệ doanh nghiệp phức tạp và đắt đỏ của Aurora.

### 2.2. Amazon RDS Proxy
* **Định nghĩa:** Trình trung gian (Proxy) quản lý kết nối cơ sở dữ liệu, cho phép ứng dụng chia sẻ và gom cụm kết nối (*connection pooling*).
* **Tính năng:**
  * **Tối ưu co giãn:** Thiết lập pool kết nối để tái sử dụng, tránh hao phí CPU/RAM khi liên tục mở/tắt kết nối từ ứng dụng (đặc biệt hữu ích khi làm việc với AWS Lambda).
  * **Tăng tính bền vững:** Tự động định tuyến kết nối sang DB dự phòng (standby instance) khi DB chính gặp lỗi mà không làm ngắt kết nối từ phía ứng dụng.
  * **Chống quá tải (Throttling):** Xếp hàng hoặc điều tiết các yêu cầu kết nối vượt ngưỡng để bảo vệ cơ sở dữ liệu không bị sập khi traffic tăng đột biến.
  * **Bảo mật:** Cho phép xác thực bằng IAM và lưu trữ credential an toàn trong AWS Secrets Manager.

### 2.3. Amazon DynamoDB
* **Định nghĩa:** Dịch vụ cơ sở dữ liệu NoSQL (Key-Value và Document) được quản lý hoàn toàn bởi AWS, cung cấp hiệu suất phản hồi nhanh với độ trễ mili-giây ổn định ở mọi quy mô.
* **Giải phóng gánh nặng vận hành:** AWS tự quản trị từ phần cứng, thiết lập, nhân bản dữ liệu, vá lỗi bảo mật, co giãn cụm, đến mã hóa dữ liệu lưu trữ (encryption at rest).
* **Thành phần cốt lõi:**
  * **Tables:** Các bảng dữ liệu độc lập.
  * **Items:** Tập hợp các thuộc tính, tương đương một hàng (row) trong SQL.
  * **Attributes:** Tương đương một cột (column) trong SQL.
  * **Primary Keys / Secondary Indexes:** Dùng để định danh duy nhất và tối ưu hóa khả năng truy vấn dữ liệu linh hoạt.
  * **DynamoDB Streams:** Ghi nhận các sự kiện chỉnh sửa dữ liệu thời gian thực để kích hoạt các tiến trình xử lý hạ nguồn.
* *Lý do chọn lựa:* Hoàn hảo cho yêu cầu làm bảng tra cứu đơn giản, chế độ Serverless hoàn toàn giúp giảm thiểu tối đa gánh nặng vận hành.
