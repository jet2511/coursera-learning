# Tóm tắt Bài học: Nâng cấp Kiến trúc Serverless lên Mức độ Tiếp theo (Week Wrap-up: Taking this Architecture to the Next Level)

**Khóa học:** Course 2 - Architecting Solutions on AWS  
**Chủ đề:** Các phương án tối ưu hóa kiến trúc Serverless sau khi đã có thiết kế nền tảng  
**Vị trí:** Module 1 - Designing a serverless web backend on AWS  
**Nhân vật:** Morgan & Raf (cả hai đều đóng vai trò Solutions Architect)

---

## 1. Tối ưu hóa DynamoDB

### 1.1. Amazon DAX (DynamoDB Accelerator)
* **Bản chất:** Thêm một lớp bộ nhớ đệm (caching layer) nằm giữa AWS Lambda và Amazon DynamoDB.
* **Lợi ích:** Giảm độ trễ truy vấn xuống mức **microsecond**, tránh các lần truy cập trực tiếp vào DynamoDB table liên tục.
* **Trade-off:** Mang lại hiệu năng cực cao nhưng **phát sinh thêm chi phí**. Chỉ nên triển khai DAX sau khi đã xác định hiệu năng của DynamoDB thuần chưa đáp ứng đủ yêu cầu thực tế.
* **Phương pháp đánh giá:** Nếu đã có Infrastructure as Code (IaC), có thể sao chép môi trường và thực hiện **A/B Testing** (stress test có DAX vs. không có DAX) để so sánh trước khi quyết định.

### 1.2. Tái thiết kế Index (Table Remodeling)
* Ngoài DAX, có thể tối ưu hóa hiệu năng DynamoDB bằng cách **thiết kế lại cấu trúc bảng và các chỉ mục (indexes)** cho phù hợp với các access pattern thực tế của ứng dụng.

---

## 2. Tối ưu hóa AWS Lambda

### 2.1. AWS Lambda Power Tuning (Tối ưu Bộ nhớ & CPU)
* **Cơ chế:** Công cụ hỗ trợ tìm ra cấu hình bộ nhớ và CPU tối ưu nhất cho Lambda.
* **Điều phản trực giác (Counterintuitive):** Tăng bộ nhớ cấp phát cho Lambda tuy làm tăng đơn giá (cost/GB-second), nhưng code thường chạy nhanh hơn đáng kể → thời gian thực thi ngắn hơn → **tổng chi phí thực tế có thể thấp hơn**. Vì Lambda được tính tiền theo thời gian thực thi (duration).

### 2.2. Lambda Layers (Chia sẻ thư viện chung)
* **Mục đích:** Tách các thư viện hoặc đoạn mã dùng chung (common libraries) ra khỏi từng hàm Lambda riêng lẻ và đóng gói thành một Layer dùng chung.
* **Lợi ích:**
  * **Dễ bảo trì:** Khi cần cập nhật thư viện, chỉ sửa ở Layer một lần duy nhất, không cần cập nhật từng hàm Lambda.
  * **Deploy nhanh hơn:** Package code triển khai (deployment package) nhỏ hơn vì không cần đóng gói kèm thư viện nặng trong mỗi hàm.
* **Phù hợp:** Khi kiến trúc mở rộng ra nhiều Lambda functions sử dụng chung các dependencies.

### 2.3. Tối ưu Code Lambda (Initialization Optimization)
* **Kỹ thuật:** Khai báo các biến, đối tượng (objects) hoặc kết nối cần khởi tạo tốn thời gian ở **ngoài hàm handler** thay vì bên trong handler.
* **Cơ chế:** Lambda có thể tái sử dụng môi trường thực thi (execution environment) cho nhiều lần gọi (invocations) liên tiếp. Các biến khai báo ngoài handler sẽ tồn tại và tái sử dụng qua các lần gọi đó, giúp giảm thời gian khởi tạo cho mỗi lần thực thi.

### 2.4. AWS Lambda Powertools (Observability)
* **Bản chất:** Bộ thư viện tiện ích (suite of utilities) giúp áp dụng các best practices của Lambda một cách dễ dàng.
* **Tính năng nổi bật:**
  * **Tracing** tích hợp với **AWS X-Ray** để theo dõi luồng xử lý phân tán.
  * **Structured Logging:** Ghi log có cấu trúc (JSON) nhất quán, dễ phân tích hơn trong CloudWatch Logs.
  * **Custom Metrics:** Tạo và đẩy các chỉ số tùy chỉnh lên Amazon CloudWatch.

---

## 3. Nâng cấp Lớp Định tuyến Sự kiện: SNS → Amazon EventBridge

* **Khi nào cần nâng cấp:** Khi yêu cầu lọc tin nhắn trở nên phức tạp hơn các khả năng lọc theo Message Attributes của SNS, hoặc khi cần tích hợp với nhiều nguồn sự kiện hơn (kể cả SaaS tools từ AWS Partners).
* **Ưu điểm của EventBridge so với SNS:**

| Tiêu chí | Amazon SNS | Amazon EventBridge |
|---|---|---|
| **Lọc tin nhắn** | Chỉ theo Message Attributes | Theo nội dung tin nhắn (content-based filtering) |
| **Số lượng Consumers** | Nhiều Subscribers | Nhiều Rules, mỗi rule có nhiều targets |
| **Tích hợp SaaS** | Hạn chế | Hỗ trợ phong phú (AWS Partners, 3rd-party SaaS) |
| **Chi phí** | Thấp hơn | Cao hơn |

* **Kiến trúc nâng cấp:** EventBridge có thể đặt ở giữa Lambda Dispatcher và các điểm đến hạ nguồn, đồng thời có thể fanout đến cả SNS Topic lẫn SQS Queue song song.

---

## 4. Tóm tắt Các Phương án Tối ưu

| Thành phần | Phương án Tối ưu | Mục đích Chính |
|---|---|---|
| **DynamoDB** | Amazon DAX | Giảm độ trễ đọc xuống microsecond |
| **DynamoDB** | Remodel Table Indexes | Tối ưu cho access patterns thực tế |
| **Lambda** | Lambda Power Tuning | Tìm cấu hình memory/CPU tối ưu nhất |
| **Lambda** | Lambda Layers | Tái sử dụng thư viện chung, giảm kích thước deploy |
| **Lambda** | Init ngoài handler | Giảm thời gian khởi tạo giữa các lần gọi |
| **Lambda** | Lambda Powertools | Tracing (X-Ray), structured logging, custom metrics |
| **SNS** | Thay bằng EventBridge | Lọc nâng cao, tích hợp SaaS, nhiều targets hơn |
