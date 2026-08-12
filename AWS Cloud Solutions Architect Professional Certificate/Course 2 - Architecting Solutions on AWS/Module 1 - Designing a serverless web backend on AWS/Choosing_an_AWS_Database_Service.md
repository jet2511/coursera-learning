# Tóm tắt bài học: Lựa chọn dịch vụ Cơ sở dữ liệu AWS (Choosing an AWS Database Service)

**Khóa học:** Course 2 - Architecting Solutions on AWS  
**Chủ đề:** So sánh Relational (Aurora Serverless) vs Key-Value (DynamoDB) để chọn giải pháp lưu trữ cho Orders Service  
**Vị trí:** Module 1 - Designing a serverless web backend on AWS

---

## 1. Cơ sở dữ liệu chuyên dụng trên AWS (Purpose-built Databases)
AWS cung cấp nhiều loại cơ sở dữ liệu được tối ưu hóa cho từng mục đích cụ thể:
* **Relational (Cơ sở dữ liệu quan hệ):** Amazon RDS, Amazon Aurora. Dành cho các ứng dụng có cấu trúc schema cố định, quan hệ ràng buộc chặt chẽ giữa các bảng, truy vấn SQL phức tạp.
* **Key-Value (Khóa - Giá trị):** Amazon DynamoDB. Dành cho ứng dụng cần hiệu suất cực cao ở quy mô lớn, độ trễ phần nghìn giây nhất quán.
* **In-Memory (Trong bộ nhớ/Cache):** Amazon ElastiCache. Phục vụ tăng tốc truy vấn dữ liệu bằng bộ nhớ đệm.
* **Graph (Đồ thị):** Amazon Neptune. Dành cho các mối quan hệ đồ thị phức tạp (như mạng xã hội, hệ thống gợi ý).

---

## 2. Đánh giá hai ứng viên tiềm năng cho Dịch vụ Đơn hàng

### 2.1. Amazon Aurora Serverless (Relational)
* **Ưu điểm:**
  * Tương thích hoàn toàn (drop-in compatible) với cơ sở dữ liệu MySQL hiện tại của khách hàng.
  * Tự động co giãn tài nguyên dựa trên lượng tải thực tế, rất phù hợp với tải trồi sụt thất thường (*spiky workload*). Chỉ trả tiền cho dung lượng sử dụng thực tế.
* **Nhược điểm & Rào cản:**
  * **Quản lý kết nối từ Lambda:** Khi AWS Lambda co giãn mạnh lên hàng trăm thực thể thực thi đồng thời, mỗi thực thể sẽ mở một kết nối độc lập tới Aurora. Việc này dễ làm nghẽn và quá tải số lượng kết nối cơ sở dữ liệu quan hệ.
  * **Phát sinh dịch vụ:** Để giải quyết vấn đề nghẽn kết nối, bắt buộc phải triển khai và quản lý thêm **Amazon RDS Proxy** nằm ở giữa Lambda và Aurora. Điều này làm tăng gánh nặng cấu hình và quản lý vận hành.

### 2.2. Amazon DynamoDB (Key-Value/NoSQL)
* **Ưu điểm:**
  * Là dịch vụ **Fully Serverless** (phi máy chủ hoàn toàn) ngay từ thiết kế cốt lõi. Tự động co giãn bộ lưu trữ bên dưới mà không cần bất kỳ tác vụ quản trị nào (không lo về phân vùng hay thiếu bộ nhớ).
  * **Chế độ On-demand throughput:** Tự động điều chỉnh hiệu năng đọc/ghi theo thời gian thực, tối ưu cho spiky workload mà không cần dự phòng trước.
  * **Khả năng tích hợp Lambda hoàn hảo:** Không lo lắng về vấn đề nghẽn kết nối như cơ sở dữ liệu quan hệ, loại bỏ hoàn toàn nhu cầu sử dụng RDS Proxy.
* **Hạn chế:** Không hỗ trợ truy vấn kết hợp nhiều bảng (SQL Joins) hay truy vấn SQL phức tạp xuyên bảng. Cần định hình rõ các access pattern (mẫu truy vấn) trước để thiết kế index cho bảng.

---

## 3. Xác thực yêu cầu truy vấn & Quyết định thiết kế
Qua cuộc gọi làm rõ với khách hàng, các mẫu truy vấn dữ liệu đơn hàng của họ cực kỳ đơn giản:
* Thực hiện các thao tác CRUD cơ bản (tạo, đọc, cập nhật, xóa) đơn hàng dựa trên `order_id`.
* Lấy danh sách các đơn hàng thuộc về một khách hàng dựa trên `customer_id`.
* Không có các truy vấn SQL phức tạp hay liên kết bảng chéo.

=> **Quyết định:** Chọn **Amazon DynamoDB** làm cơ sở dữ liệu lưu trữ đơn hàng. Nó đáp ứng hoàn hảo mẫu truy vấn đơn giản của khách hàng, đem lại kiến trúc cực kỳ tối giản (không cần RDS Proxy) và giảm thiểu tối đa gánh nặng vận hành theo định hướng đám mây nguyên bản (cloud-native).

---

## 4. Cập nhật sơ đồ kiến trúc: Khối ghép thứ 3
Hệ thống hiện tại đã bổ sung thêm mảnh ghép cơ sở dữ liệu:
* **Giao diện API:** Amazon API Gateway
* **Xử lý tính toán (Compute):** AWS Lambda
* **Lưu trữ dữ liệu (Database):** Amazon DynamoDB (hoạt động ở chế độ *On-demand*)
