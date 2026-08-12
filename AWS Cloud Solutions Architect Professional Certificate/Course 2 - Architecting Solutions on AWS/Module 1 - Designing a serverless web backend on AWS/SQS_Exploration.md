# Tóm tắt bài học: Thực hành khám phá Amazon SQS (SQS Exploration)

**Khóa học:** Course 2 - Architecting Solutions on AWS  
**Chủ đề:** Khám phá cấu hình chi tiết hàng đợi SQS, so sánh SQS vs SNS, các tham số cốt lõi (size, retention, polling, visibility timeout) và giám sát lỗi  
**Vị trí:** Module 1 - Designing a serverless web backend on AWS

---

## 1. Phân biệt cốt lõi: Amazon SQS vs Amazon SNS
* **Amazon SNS (Push-based):** Đẩy tin nhắn trực tiếp đến các người nhận ngay khi có tin mới. Việc tin nhắn có được tiếp nhận thành công hay không phụ thuộc hoàn toàn vào tình trạng hoạt động của người nhận tại thời điểm đó.
* **Amazon SQS (Pull-based):** Lưu giữ tin nhắn an toàn trong hàng đợi cho đến khi có người nhận thực hiện thăm dò (**Polling**) kéo tin nhắn về, xử lý xong và gửi lệnh xóa tin nhắn khỏi hàng đợi.

---

## 2. Phân loại hàng đợi & Các tham số cấu hình cốt lõi

### 2.1. Phân loại hàng đợi (Standard vs FIFO)
* **Standard Queue:** Mặc định, thông lượng xử lý gần như không giới hạn, phân phối tin theo mô hình nỗ lực tối đa (best-effort ordering) và có thể phát sinh trùng lặp tin.
* **FIFO Queue:** Đảm bảo chính xác thứ tự gửi trước - nhận trước và tin nhắn chỉ được xử lý duy nhất một lần (exactly-once processing), nhưng bị giới hạn thông lượng.

### 2.2. Các tham số cấu hình quan trọng
1. **Maximum message size (Kích thước tối đa):** Giới hạn từ **1 KB đến 256 KB**. Không dùng để truyền tải tệp tin lớn. Với các payload lớn, giải pháp khuyên dùng là lưu file vào S3/Database và chỉ gửi đường dẫn tham chiếu (reference/pointer) qua tin nhắn SQS.
2. **Message retention period (Thời gian lưu giữ):** Cấu hình từ **1 phút đến tối đa 14 ngày**. Tin nhắn sẽ bị hệ thống tự động xóa nếu quá thời hạn lưu giữ mà chưa được xử lý thành công.
3. **Receive message wait time (Thời gian chờ nhận tin - Polling):**
   * Giới hạn từ **0 đến 20 giây**. Là thời gian tối đa mà kết nối polling sẽ chờ để nhận được tin nhắn nếu hàng đợi trống.
   * **Long Polling (Thăm dò lâu):** Đặt cấu hình > 0 giây (khuyên dùng 20 giây) cho các hàng đợi có lượng tin nhắn thấp để tránh các cuộc gọi API liên tục kiểm tra hàng đợi rỗng, giúp tiết kiệm chi phí.
   * **Short Polling (Thăm dò ngắn):** Đặt = 0 giây, trả phản hồi lập tức ngay cả khi không có tin nhắn.
4. **Visibility timeout (Thời gian ẩn tin nhắn):**
   * Là khoảng thời gian mà một tin nhắn sau khi được một consumer lấy ra sẽ tạm thời "ẩn đi" để các consumer khác không nhìn thấy và không xử lý trùng lặp.
   * Nếu consumer xử lý thành công, nó sẽ gửi lệnh xóa tin. Nếu consumer bị crash hoặc lỗi giữa chừng, sau khi hết thời gian ẩn, tin nhắn sẽ xuất hiện lại trong hàng đợi để consumer khác kéo về xử lý lại.

---

## 3. Phân quyền, Tích hợp & Giám sát lỗi

### 3.1. Phân quyền bằng Resource Policy
* Tương tự SNS, SQS có chính sách tài nguyên gán trực tiếp để định nghĩa ai có quyền gửi tin vào queue (Publishers) và ai có quyền kéo tin khỏi queue (Consumers).

### 3.2. Khả năng tích hợp
* SQS có thể đăng ký làm Subscriber để hứng tin nhắn trực tiếp từ một SNS Topic gửi tới.
* SQS được hỗ trợ tích hợp sẵn làm nguồn sự kiện (Event Source/Trigger) để tự động kích hoạt các hàm **AWS Lambda**.

### 3.3. Giám sát lỗi qua Amazon CloudWatch
* CloudWatch hiển thị các số liệu trực quan như lượng tin nhắn tồn đọng, số tin nhắn được thêm và số tin nhắn bị xóa.
* **Mẹo debug:** Nếu biểu đồ CloudWatch ghi nhận lượng tin nhắn đổ về hàng đợi tăng vọt nhưng lượng tin nhắn bị xóa (deleted messages) rất thấp, điều này chỉ ra bug trong mã nguồn ứng dụng: Consumer đang xử lý lỗi hoặc quên không gửi lệnh xóa tin nhắn sau khi hoàn thành, dẫn đến việc tin nhắn bị xử lý lặp đi lặp lại.
