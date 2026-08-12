# Tóm tắt bài học: Giải phóng liên kết các giải pháp AWS (Decoupling AWS Solutions)

**Khóa học:** Course 2 - Architecting Solutions on AWS  
**Chủ đề:** Áp dụng mô hình Storage-First sử dụng Amazon SQS để giảm độ trễ API và hoàn thiện kiến trúc xử lý đơn hàng bất đồng bộ  
**Vị trí:** Module 1 - Designing a serverless web backend on AWS

---

## 1. Vấn đề Độ trễ hệ thống do Mô hình Đồng bộ (Synchronous Latency)
* **Thực trạng hệ thống cũ:** Luồng dữ liệu chạy đồng bộ hoàn toàn: 
  ```
  Người dùng đặt đơn ──> Tiếp nhận & Kiểm tra ──> Xử lý nghiệp vụ ──> Ghi DB ──> Gọi 3 dịch vụ hạ nguồn ──> Phản hồi
  ```
  Toàn bộ quá trình này mất nhiều thời gian, khiến trình duyệt của người dùng bị đơ (frozen) khi chờ phản hồi. Vào giờ cao điểm, hệ thống quá tải sẽ lập tức từ chối và làm mất mát đơn hàng.
* **Mục tiêu:** Chuyển đổi sang kiến trúc xử lý **bất đồng bộ (Asynchronous)**.

---

## 2. Mô hình Storage-First Pattern (Lưu trữ trước)
* **Ý tưởng cốt lõi:** Đưa lớp lưu trữ tạm thời (vùng đệm) lên đứng ngay sau API Gateway và trước Compute Layer (Lambda).
  * *Mô hình truyền thống:* API ──> Compute (Xử lý lâu) ──> Storage ──> Phản hồi Client.
  * *Mô hình Storage-First:* API ──> Storage (Vùng đệm) ──> Phản hồi ngay cho Client ──> Compute (Đọc từ vùng đệm và xử lý bất đồng bộ phía sau).
* **Khả năng tích hợp của API Gateway (Service Integration):** 
  * API Gateway hỗ trợ gọi trực tiếp API của các dịch vụ AWS khác (như ghi vào DynamoDB, gửi tin vào SQS, publish lên SNS) mà không cần lập trình một hàm Lambda trung gian.
  * API Gateway tự đảm nhận việc xác thực (Authentication) và kiểm tra dữ liệu đầu vào (Validation) trước khi đẩy vào vùng đệm.

---

## 3. So sánh 2 phương án làm vùng đệm (Buffer Storage)

### Phương án 1: API Gateway ghi trực tiếp vào DynamoDB
* **Cơ chế:** API Gateway xác thực và ghi thẳng đơn hàng vào bảng DynamoDB rồi phản hồi ngay cho client. 
* **Điều kiện áp dụng:** Chỉ khả thi nếu tiến trình tiếp nhận đơn hàng ban đầu **không chứa logic nghiệp vụ phức tạp** mà chỉ thuần túy kiểm tra dữ liệu và ghi vào bảng.

### Phương án 2: Sử dụng Amazon SQS (Simple Queue Service) làm hàng đợi
* **Cơ chế:** API Gateway gửi thông điệp đơn hàng vào hàng đợi SQS, lập tức trả về phản hồi thành công cho khách hàng. Hàm Lambda (được cấu hình làm event source của SQS) sẽ tự động kéo các thông điệp từ SQS về để xử lý bất đồng bộ theo năng lực của nó.
* **Lợi ích:** 
  * Hoàn toàn bảo vệ hệ thống khỏi bị quá tải (SQS đóng vai trò bộ đệm hấp thụ các đợt traffic tăng đột biến). Không lo mất mát đơn hàng do nghẽn tải.
  * Hoạt động theo cơ chế serverless, tự động co giãn và tối ưu chi phí.

---

## 4. Xác thực yêu cầu & Hoàn thiện kiến trúc cuối cùng (End-to-End)
Qua cuộc gọi làm rõ, khách hàng xác nhận ứng dụng **có xử lý logic nghiệp vụ phức tạp** khi tiếp nhận đơn hàng, do đó không thể bỏ hàm Lambda đầu tiên để ghi trực tiếp vào DB. 

=> **Quyết định:** Chọn **Amazon SQS** làm vùng đệm giữa API Gateway và AWS Lambda.

### Sơ đồ luồng dữ liệu hoàn chỉnh của hệ thống xử lý đơn hàng mới:
```
[Client]
   │ (1. Đặt hàng)
   ▼
[Amazon API Gateway]
   │ (2. Gửi message & Phản hồi thành công ngay lập tức)
   ▼
[Amazon SQS (Queue)]
   │
   │ (3. Lambda kéo message về xử lý bất đồng bộ)
   ▼
[AWS Lambda 1 (Order Processor)]
   │
   │ (4. Lưu thông tin đơn hàng)
   ▼
[Amazon DynamoDB (Table)]
   │
   │ (5. Ghi nhận thay đổi thời gian thực)
   ▼
[DynamoDB Streams]
   │
   │ (6. Kích hoạt hàm xử lý luồng)
   ▼
[AWS Lambda 2 (Stream Dispatcher)]
   │
   │ (7. Gọi API Publish tin nhắn)
   ▼
[Amazon SNS (Topic)]
   │
   ├─► [Inventory Service]  (8. Fan-out đồng loạt đến các dịch vụ hạ nguồn)
   ├─► [Accounting Service]
   └─► [Fulfillment Service]
```
Kiến trúc này giải quyết triệt để tất cả các bài toán của khách hàng: co giãn tự động (Managed Scaling), loại bỏ liên kết chặt chẽ (Decoupled), tăng tính bền vững (Resiliency), độ trễ thấp cho người dùng cuối và giảm thiểu tối đa chi phí vận hành.
