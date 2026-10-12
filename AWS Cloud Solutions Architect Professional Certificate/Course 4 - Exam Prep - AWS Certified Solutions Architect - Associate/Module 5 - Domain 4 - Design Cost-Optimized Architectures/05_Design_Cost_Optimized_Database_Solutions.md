# Design Cost-Optimized Database Solutions

## 1. Lựa chọn đúng loại Data Store (Right Data Store Selection)
- **Không dồn toàn bộ dữ liệu vào Relational Database (RDS):**
  - Việc lưu trữ tất cả dữ liệu (bao gồm cả file nhị phân, dữ liệu phi cấu trúc, log) vào RDBMS làm tăng TCO (Total Cost of Ownership) và gây nghẽn hiệu năng.
- **Chiến lược phân tách dữ liệu (Data Offloading Strategy):**
  - **Large Objects / Media / Blobs $\to$ Chuyển sang Amazon S3:** Giảm dung lượng storage đắt đỏ và chi phí backup của database.
  - **Dữ liệu phi cấu trúc / Key-Value / High Read-Write Throughput $\to$ Chuyển sang Amazon DynamoDB:** 
    - DynamoDB là fully-managed NoSQL, tự động phân vùng và scale mà không mất chi phí quản trị (hardware provisioning, setup, patching, cluster scaling).
  - **Dữ liệu có cấu trúc, quan hệ chặt chẽ, ràng buộc ACID $\to$ Giữ trên Amazon RDS / Aurora.**

---

## 2. Chiến lược Định cỡ & Co giãn Tối ưu Chi phí (Database Scaling Strategies)

### A. Tự động co giãn lưu trữ (RDS Storage Auto Scaling)
- Giúp bắt đầu với dung lượng lưu trữ nhỏ và chỉ tự động mở rộng khi gần đầy.
- Tránh over-provisioning storage ngay từ đầu.

### B. Vertical vs Horizontal Scaling cho Read Workloads
- **Vấn đề:** Database bị High CPU do lượng request **Read** tăng đột biến.
- **Giải pháp:**
  - *Scale Up (Vertical Scaling - tăng instance size):* Tốn kém chi phí, gây downtime khi đổi instance class.
  - *Tối ưu chi phí bằng Horizontal Offloading:*
    1. **Amazon RDS Read Replicas:** Thêm Read Replica để phân phối tải đọc, chi phí rẻ hơn nhiều so với việc nâng cấp instance chính lên size quá lớn.
    2. **Caching Layer (Amazon ElastiCache / Redis / Memcached / DAX):** Đưa cache lên trước DB để hấp thụ các query đọc lặp lại, giảm tải triệt để cho database.

### C. Chọn công cụ Serverless cho tải không liên tục
- **Amazon Aurora Serverless:** Tự động start/stop và scale compute capacity (ACUs) dựa trên lưu lượng thực tế $\to$ Cực kỳ tối ưu chi phí cho ứng dụng có tải ngắt quãng, tải đêm thấp hoặc không dự đoán trước được.

---

## 3. Tối ưu Chi phí Backup & Disaster Recovery (RPO / RTO)
- **Retention Policy (Chính sách lưu trữ bản sao lưu):**
  - Thiết lập thời gian lưu trữ Automated Backups và Manual Snapshots vừa đủ theo yêu cầu RPO/RTO.
  - Xóa hoặc archive các snapshot thủ công cũ không còn nhu cầu sử dụng để tránh chi phí lưu trữ tích lũy.
- **Point-in-Time Recovery (PITR):**
  - Tận dụng tính năng PITR của RDS và DynamoDB để khôi phục chính xác đến từng giây mà không cần tạo snapshot liên tục gây tốn kém.

---

## 4. Tận dụng Managed Services để giảm TCO
- Các dịch vụ cơ sở dữ liệu được quản lý hoàn toàn (Amazon RDS, Aurora, DynamoDB, ElastiCache) giúp:
  - Loại bỏ chi phí vận hành, bảo trì, vá lỗi OS/DB.
  - Hưởng lợi từ quy mô đám mây (Cloud scale) giúp giảm chi phí trên mỗi giao dịch (Cost per transaction).

---

## 5. Key Exam Takeaways
1. **Lưu trữ Blob/Large Files trong DB $\to$ Đưa sang Amazon S3** để giảm chi phí lưu trữ và IOPS của database.
2. **Database bị nghẽn tải Read (High CPU):**
   - Không vội Scale-up instance chính.
   - Giải pháp tối ưu chi phí nhất: Thêm **Read Replica** hoặc **ElastiCache/DAX**.
3. **Workload biến động thất thường, có thời gian idle $\to$ Amazon Aurora Serverless / DynamoDB On-Demand.**
4. **Tránh over-provisioning dung lượng $\to$ Kích hoạt RDS Storage Auto Scaling.**
