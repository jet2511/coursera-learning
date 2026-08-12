# Tóm tắt bài học: Thực hành khám phá Amazon SNS (SNS Exploration)

**Khóa học:** Course 2 - Architecting Solutions on AWS  
**Chủ đề:** Khám phá chi tiết cách cấu hình Topic, phân loại Standard vs FIFO, thiết lập mã hóa, Access Policy và các giao thức Subscription trên Amazon SNS  
**Vị trí:** Module 1 - Designing a serverless web backend on AWS

---

## 1. Khái niệm cơ bản về Amazon SNS
* **Mô hình hoạt động:** Pub/Sub (Publish/Subscribe - Nhà xuất bản / Người đăng ký).
* **Cơ chế:** Cho phép gửi thông điệp vào một kênh truyền tin gọi là **Topic**. SNS tự động nhân bản và gửi thông điệp đó đồng loạt (*fan out*) tới toàn bộ các đích nhận đã đăng ký (*subscribed endpoints*).

---

## 2. Các cấu hình quan trọng khi tạo Topic

### 2.1. Phân loại Topic: Standard vs FIFO
* **FIFO (First-In, First-Out) Topic:**
  * Đảm bảo thứ tự truyền tin chính xác tuyệt đối như lúc nhận tin.
  * Phân phối tin đúng một lần duy nhất (*exactly-once message delivery*), loại bỏ hoàn toàn khả năng lặp tin.
  * Giới hạn thông lượng: Hỗ trợ tối đa 300 lượt publish mỗi giây.
* **Standard Topic:**
  * Phân phối tin theo cơ chế nỗ lực tối đa (*best-effort message ordering*), thứ tự tin nhắn đi ra có thể không hoàn toàn chính xác theo thứ tự vào.
  * Cung cấp thông lượng xử lý cực kỳ lớn (gần như không giới hạn).
  * *Lựa chọn trong bài học:* Do thanh toán đơn hàng đã được xử lý xong trước đó và thứ tự đơn hàng không cần độ chính xác tuyệt đối ở tầng này, **Standard Topic** được chọn để đáp ứng thông lượng lớn và hiệu năng cao nhất.

### 2.2. Bảo mật & Mã hóa dữ liệu
* **Mã hóa trên đường truyền (Encryption in transit):** Được AWS kích hoạt mặc định.
* **Mã hóa lưu trữ (Server-side encryption - SSE):** Người dùng có thể tùy chọn kích hoạt mã hóa dữ liệu tĩnh (at rest). Khi bật, dữ liệu tin nhắn sẽ được mã hóa ngay khi đến SNS và chỉ giải mã ngay trước khi chuyển tiếp tới người nhận, bảo vệ tuyệt đối dữ liệu nhạy cảm. Quản lý khóa thông qua **AWS KMS**.

### 2.3. Chính sách truy cập (Access Policy)
* Là một dạng chính sách tài nguyên (*Resource Policy*) được gán trực tiếp lên SNS Topic để phân quyền cụ thể:
  * **Quyền gửi tin (Publish):** Chỉ định ai có quyền gửi thông điệp vào topic (Chỉ chủ sở hữu, Mọi người, hay Một số tài khoản AWS cụ thể).
  * **Quyền nhận tin (Subscribe):** Chỉ định ai có thể đăng ký nhận tin từ topic.
* Console hỗ trợ tạo nhanh qua bộ lọc trực quan (Basic mode) hoặc chỉnh sửa trực tiếp file cấu hình dạng JSON (Advanced mode).

---

## 3. Các loại giao thức đăng ký nhận tin (Subscriptions)
Sau khi tạo Topic thành công, người dùng có thể thiết lập các Endpoint nhận tin thông qua các giao thức đa dạng:
* **Kinesis Data Firehose:** Đẩy tin trực tiếp vào luồng xử lý dữ liệu.
* **Amazon SQS Queue:** Chuyển tiếp tin nhắn vào hàng đợi để xử lý bất đồng bộ.
* **AWS Lambda:** Kích hoạt một hàm Lambda chạy xử lý logic.
* **HTTPS/HTTP:** Gửi request POST chứa payload tin nhắn đến một địa chỉ web server cụ thể.
* **Email:** Gửi thông báo trực tiếp đến hòm thư điện tử.
* **SMS:** Gửi tin nhắn văn bản đến số điện thoại di động của người dùng.
