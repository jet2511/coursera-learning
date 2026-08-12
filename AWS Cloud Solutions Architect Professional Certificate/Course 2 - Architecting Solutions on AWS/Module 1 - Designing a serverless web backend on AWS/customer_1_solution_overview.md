# Tóm tắt Bài học: Tổng quan Giải pháp cho Khách hàng số 1 (Customer #1: Solution Overview)

**Khóa học:** Course 2 - Architecting Solutions on AWS  
**Chủ đề:** Trực quan hóa và trình bày kiến trúc Serverless hoàn chỉnh cho Orders Service của AnyCompany Online  
**Vị trí:** Module 1 - Designing a serverless web backend on AWS  
**Nhân vật:** Morgan (AWS Solutions Architect) & Raf (Technical Architect đại diện AnyCompany Online)

---

## 1. Luồng dữ liệu chi tiết của hệ thống (End-to-End Flow)

1. **Giao diện Client (Frontend Clients):** Người dùng đặt hàng qua trình duyệt web, thiết bị di động, v.v. gửi các HTTPS requests chứa dữ liệu đơn hàng về backend.
2. **Amazon API Gateway (Front Door):** 
   * Tiếp nhận các request từ clients.
   * Xử lý xác thực (Authentication).
   * Kiểm tra định dạng dữ liệu (Schema Validation) để đảm bảo payload chứa đầy đủ các trường thông tin bắt buộc trước khi chuyển tiếp vào bên trong.
3. **Amazon SQS (Decoupling & Buffer):**
   * API Gateway ghi trực tiếp tin nhắn đơn hàng vào hàng đợi SQS.
   * Đóng vai trò tách rời hoàn toàn lớp API khỏi lớp tính toán (Compute Layer - Lambda).
   * **Bảo vệ hệ thống khi tải tăng đột biến:** Nếu lượng đặt hàng tăng vọt vượt quá giới hạn concurrency mặc định của Lambda, tin nhắn đơn hàng vẫn được lưu trữ an toàn trong queue để xử lý dần dần mà không bị mất mát dữ liệu.
4. **AWS Lambda 1 (Order Processor):**
   * Tích hợp cơ chế tự động thăm dò (polling) tin nhắn từ SQS.
   * Chứa mã nguồn logic nghiệp vụ xử lý đơn hàng và ghi vào cơ sở dữ liệu.
   * Để tăng tốc độ xử lý khi hàng đợi bị ùn ứ, có thể tăng giới hạn concurrency của Lambda lên.
5. **Amazon DynamoDB (Database):** Lưu trữ thông tin đơn hàng an toàn.
6. **DynamoDB Streams (Change Data Capture - CDC):** Tự động ghi lại nhật ký thay đổi dữ liệu (tạo mới/cập nhật đơn hàng) theo thời gian thực.
7. **AWS Lambda 2 (Stream Dispatcher):**
   * Lắng nghe các thay đổi từ DynamoDB Stream.
   * Đọc thông tin thay đổi đơn hàng và gửi (publish) dữ liệu sang cổng phát tin nhắn SNS.
8. **Amazon SNS (Pub/Sub Fan-out):**
   * Tiếp nhận tin nhắn và nhân bản đồng loạt (fan-out) tới các Subscribers.
   * Phân phối tin nhắn đồng thời tới 3 dịch vụ hạ nguồn độc lập: **Fulfillment (Kho/Giao nhận)**, **Accounting (Kế toán)**, và **Inventory (Hàng tồn kho)**.

---

## 2. Giải đáp thắc mắc về Giám sát và Co giãn (Monitoring & Scaling)

* **Giám sát và Ghi log (Monitoring & Logging):**
  * Tất cả các dịch vụ được chọn đều là Serverless nguyên bản.
  * Đã tích hợp sẵn và tự động đẩy các chỉ số (metrics) cùng nhật ký hoạt động (logs) về **Amazon CloudWatch** và **Amazon CloudWatch Logs** mà không cần cấu hình thủ công phức tạp.
* **Tự động co giãn (Managed Scaling):**
  * Toàn bộ hệ thống tự động co giãn dựa trên lượng tải thực tế.
  * Khách hàng vẫn có thể thiết lập các giới hạn (limits/rates) như cấu hình concurrency limit cho Lambda hay thiết lập throughput cho DynamoDB để kiểm soát chi phí và sự kiện mở rộng, giúp vận hành an nhàn hơn rất nhiều so với quản trị Amazon EC2.
* **Tối ưu chi phí:**
  * Hệ thống tự động co giãn về không (scale in to zero) khi không có yêu cầu nào, giúp tối ưu hóa chi phí vận hành cho các khoảng thời gian rảnh rỗi.

---

## 3. Bước tiếp theo (Next Steps)
Thiết kế kiến trúc ban đầu này có thể thay đổi trong quá trình triển khai thực tế khi xuất hiện thêm các yêu cầu mới. Bước tiếp theo của dự án là bắt tay vào xây dựng một **Proof of Concept (PoC - Bản thử nghiệm kiểm chứng khái niệm)** để kiểm tra tính khả thi và cách thức hoạt động chi tiết của hệ thống.
