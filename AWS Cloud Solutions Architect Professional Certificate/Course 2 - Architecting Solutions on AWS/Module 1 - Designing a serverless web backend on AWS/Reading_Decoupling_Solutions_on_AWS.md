# Tóm tắt bài học: Giải phóng liên kết các giải pháp trên AWS (Decoupling Solutions on AWS)

**Khóa học:** Course 2 - Architecting Solutions on AWS  
**Chủ đề:** Lợi ích của kiến trúc bất đồng bộ, Storage-First, Các tham số SQS nâng cao, và So sánh Short Polling vs Long Polling  
**Vị trí:** Module 1 - Designing a serverless web backend on AWS

---

## 1. Lợi ích của Kiến trúc bất đồng bộ & Loose Coupling
* **Khắc phục nghẽn tải:** Kiến trúc liên kết lỏng lẻo (*loosely coupled*) giúp loại bỏ các nút thắt cổ chai do giao tiếp đồng bộ, độ trễ mạng và các hoạt động I/O gây ra.
* **Tích hợp SQS và Lambda:** Là giải pháp kinh điển để xây dựng giao tiếp bất đồng bộ giữa các microservices.
* **Khi nào nên áp dụng:**
  * Cần xây dựng hệ thống có tính độc lập cao giữa các thành phần.
  * Các bước nghiệp vụ không nhất thiết phải hoàn thành chung trong một giao dịch (transaction) đồng bộ duy nhất.
  * Hệ thống hạ nguồn (downstream) có năng lực xử lý (TPS - Transactions Per Second) thấp hơn tốc độ yêu cầu đổ về từ thượng nguồn. SQS sẽ đóng vai trò làm bể chứa hấp thụ tải và phân phối dần tùy theo tài nguyên sẵn có của hạ nguồn.
* **Nhược điểm:** Tính đồng bộ bị phá vỡ. Khi người dùng nhận được phản hồi thành công từ API đầu vào, thực chất một phần của giao dịch vẫn đang trong quá trình được xử lý tiếp ở hạ nguồn.

---

## 2. Tìm hiểu sâu các tham số cấu hình của Amazon SQS
Khi tạo hoặc chỉnh sửa hàng đợi SQS, bạn có thể thiết lập các thông số kỹ thuật sau:
* **Visibility timeout (Thời gian ẩn):** Thời gian tin nhắn tạm ẩn đối với các consumer khác khi đang được một consumer xử lý.
* **Message retention period (Thời gian lưu giữ):** Thời gian giữ tin nhắn chưa xử lý trong hàng đợi. Mặc định là **4 ngày**, cấu hình tối đa là **14 ngày**.
* **Delivery delay (Độ trễ phân phối):** Thời gian trì hoãn trước khi cho phép consumer nhìn thấy tin nhắn mới được thêm vào hàng đợi.
* **Maximum message size (Kích thước tối đa):** Dung lượng tối đa của một tin nhắn.
* **Receive message wait time (Thời gian chờ nhận):** Thời gian kết nối poll chờ tin nhắn mới đổ vào queue (kích hoạt Long Polling khi giá trị > 0).
* **Content-based deduplication (Chống trùng lặp dựa trên nội dung):** Tự động băm nội dung tin nhắn để tạo ID chống trùng lặp (chỉ áp dụng cho hàng đợi FIFO).
* **High throughput FIFO (FIFO thông lượng cao):** Bật chế độ tối ưu hóa hiệu năng cao cho hàng đợi FIFO.
* **Redrive allow policy:** Quy định các hàng đợi nguồn nào được phép sử dụng hàng đợi này làm Dead-Letter Queue (DLQ - Hàng đợi thư chết để chứa các tin nhắn lỗi).

---

## 3. So sánh Short Polling vs Long Polling

### 3.1. Short Polling (Thăm dò ngắn)
* **Cơ chế:** Khi có yêu cầu lấy tin (`ReceiveMessage`), SQS chỉ truy vấn ngẫu nhiên một nhóm nhỏ các máy chủ lưu trữ vật lý bên dưới của nó để quét tin nhắn.
* **Đặc điểm:** Lượt truy vấn đầu tiên có thể không trả về đầy đủ toàn bộ tin nhắn đang có trong hàng đợi (nếu số lượng tin nhắn trong queue ít hơn 1,000 tin). Cần phải thực hiện các đợt gọi liên tiếp để lấy hết dữ liệu.

### 3.2. Long Polling (Thăm dò lâu)
* **Cơ chế:** Kích hoạt khi tham số `ReceiveMessageWaitTime` được cấu hình lớn hơn 0 giây (tối đa là 20 giây).
* **Lợi ích vượt trội:**
  1. **Giảm thiểu tối đa phản hồi rỗng (empty responses):** SQS giữ kết nối mở và chờ cho đến khi có tin nhắn mới đổ vào hàng đợi trước khi trả về kết quả. Việc này làm giảm số lượng request trống không cần thiết, giúp **tiết kiệm đáng kể chi phí gọi API SQS**.
  2. **Tránh phản hồi rỗng giả (false empty responses):** Thay vì quét một nhóm nhỏ, Long Polling sẽ thực hiện truy vấn tất cả các máy chủ vật lý của SQS để đảm bảo lấy ra tin nhắn.
  3. **Tốc độ đáp ứng tức thì:** Ngay khi tin nhắn xuất hiện trong hàng đợi, nó sẽ được trả về lập tức cho consumer đang mở kết nối chờ.
