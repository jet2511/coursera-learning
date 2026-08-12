# Tóm tắt Bài đọc: Tối ưu hóa Kiến trúc Tuần 1 (Architecture Optimizations for Week 1)

**Khóa học:** Course 2 - Architecting Solutions on AWS  
**Chủ đề:** Chi tiết kỹ thuật về các phương án tối ưu kiến trúc Serverless cho Orders Service  
**Vị trí:** Module 1 - Designing a serverless web backend on AWS

---

## 1. Caching cho DynamoDB: Amazon DAX (DynamoDB Accelerator)

### Đặc điểm kỹ thuật
* **Bản chất:** Dịch vụ caching trong bộ nhớ (in-memory cache) được quản lý hoàn toàn bởi AWS, có tính sẵn sàng cao (Highly Available).
* **Hiệu năng:** Cải thiện hiệu năng lên đến **100 lần** - từ **milliseconds → microseconds** ngay cả khi xử lý hàng triệu requests mỗi giây.

### Lợi ích nổi bật
* **Không cần sửa code ứng dụng:** DAX tương thích hoàn toàn với các DynamoDB API calls hiện có. Ứng dụng chỉ cần trỏ endpoint sang DAX thay vì DynamoDB trực tiếp.
* **Quản lý tự động:** AWS tự động xử lý cache invalidation, data population và cluster management — lập trình viên không cần can thiệp.

### Triển khai
* DAX chạy bên trong **Amazon VPC** (Virtual Private Cloud).
* Kiểm soát truy cập thông qua **VPC Security Groups**.
* Khởi chạy DAX cluster trong virtual network của bạn giống như môi trường data center truyền thống.

---

## 2. Tối ưu hóa AWS Lambda

### 2.1. AWS Lambda Power Tuning

#### Cơ chế hoạt động
* **Bản chất:** Công cụ mã nguồn mở (open-source) chạy ngay trong tài khoản AWS của bạn.
* **Kiến trúc bên dưới:** Là một **State Machine được cung cấp bởi AWS Step Functions**.
* **Đầu vào:** Cung cấp **Amazon Resource Name (ARN)** của hàm Lambda cần tối ưu.
* **Đầu ra:** Công cụ tự động gọi hàm với nhiều cấu hình bộ nhớ khác nhau (từ **128 MB đến 10 GB**), phân tích execution logs và gợi ý cấu hình tối ưu nhất.

#### Ba chiến lược tối ưu
1. **Cost** - Tối thiểu hóa chi phí.
2. **Speed** - Tối đa hóa tốc độ thực thi.
3. **Balanced** - Cân bằng giữa chi phí và tốc độ.

#### Tính năng khác
* **Language agnostic:** Hoạt động với mọi ngôn ngữ lập trình Lambda hỗ trợ.
* **Cross-Region invocations:** Hỗ trợ gọi Lambda ở các Region khác nhau.
* **Parallel execution:** Chạy song song để tạo kết quả trong vài giây.
* **Visualization:** Sinh ra biểu đồ trực quan về chi phí trung bình và tốc độ cho từng cấu hình bộ nhớ.

> **Lưu ý quan trọng:** Công cụ sẽ thực sự gọi hàm Lambda của bạn (thực hiện HTTP requests, SDK calls, cold starts thực tế) trong quá trình đo lường.

---

### 2.2. AWS Lambda Powertools

* **Bản chất:** Bộ thư viện tiện ích toàn diện cho AWS Lambda giúp áp dụng các best practices một cách dễ dàng.
* **Tính năng chính:**

| Tính năng | Mô tả |
|---|---|
| **Tracing** | Tích hợp với AWS X-Ray để theo dõi luồng xử lý phân tán |
| **Structured Logging** | Ghi log có cấu trúc JSON nhất quán, dễ phân tích trong CloudWatch |
| **Custom Metrics** | Tạo và đẩy các chỉ số tùy chỉnh lên Amazon CloudWatch |
| **Idempotency** | Xử lý an toàn các tin nhắn bị gửi trùng lặp |
| **Batching** | Xử lý hiệu quả các lô tin nhắn từ SQS/Kinesis |

---

### 2.3. Tái sử dụng Execution Environment (Initialization Optimization)

#### Kỹ thuật
* Khai báo các tài nguyên tốn chi phí khởi tạo **bên ngoài hàm handler** thay vì bên trong.
* Các tài nguyên này sẽ được **tái sử dụng qua nhiều lần gọi** (invocations) trong cùng một execution environment instance.

#### Các tài nguyên nên khai báo ngoài handler
* SDK clients (AWS SDK, HTTP clients)
* Database connections
* Static assets → cache trong thư mục `/tmp`

#### Lợi ích
* Giảm thời gian thực thi (function run time) cho mỗi lần gọi → **giảm chi phí**.
* Giảm độ trễ khởi tạo (initialization latency).

#### Lưu ý bảo mật quan trọng
> ⚠️ **Không lưu dữ liệu người dùng, events, hoặc thông tin nhạy cảm trong execution environment** để tránh data leaks giữa các lần gọi khác nhau. Nếu cần lưu trạng thái thay đổi theo từng user, hãy tạo các Lambda function version riêng biệt.

---

## 3. Tổng hợp Quyết định Thiết kế

| Nhu cầu | Giải pháp | Khi nào áp dụng |
|---|---|---|
| Độ trễ đọc DynamoDB quá cao | Amazon DAX | Sau khi benchmark thực tế xác định DynamoDB chưa đủ nhanh |
| Tìm cấu hình Lambda tối ưu | Lambda Power Tuning | Khi cần cân bằng chi phí/hiệu năng cho production |
| Chuẩn hóa logging & observability | Lambda Powertools | Ngay từ đầu hoặc khi scale lên nhiều Lambda functions |
| Giảm cold start overhead | Init ngoài handler + `/tmp` cache | Khi hàm Lambda có thời gian khởi tạo đáng kể |
