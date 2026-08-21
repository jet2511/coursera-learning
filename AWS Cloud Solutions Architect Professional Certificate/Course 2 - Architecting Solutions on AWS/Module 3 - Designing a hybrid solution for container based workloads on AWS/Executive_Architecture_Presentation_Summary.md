# Tóm Tắt Bài Thuyết Trình Kiến Trúc Tổng Thể Cho Ban Lãnh Đạo: Chuyển Đổi Lên Cloud (TechCorp)

> **Thư mục lưu trữ:** `Module 3 - Designing a hybrid solution for container based workloads on AWS`  
> **Kịch bản Role Play:** Trình bày đề xuất kiến trúc điện toán đám mây toàn diện cho Ban lãnh đạo cấp cao (Alexandra Chen - Nhà tài trợ điều hành).

---

## 1. Tổng Quan Kiến Trúc Hợp Nhất (Unified Architecture)

* **Hạ tầng Hybrid Core:** Trung tâm dữ liệu on-premises kết nối bảo mật với AWS thông qua **AWS Direct Connect (DX)** (mã hóa **MACsec**) kết hợp kênh dự phòng **IPsec Site-to-Site VPN tự động chuyển đổi dự phòng (failover)**, được định tuyến tập trung qua **AWS Transit Gateway (TGW)**.
* **Tầng Ứng Dụng Serverless (Serverless Application Layer):** Các dịch vụ hướng đến khách hàng hoạt động trên **Amazon API Gateway + AWS Lambda / Amazon ECS (Fargate)**, lưu trữ dữ liệu với **Amazon Aurora Serverless v2 / Amazon DynamoDB**.
* **Nền Tảng Phân Tích Dữ Liệu (Medallion Architecture):** S3 Data Lake thu thập dữ liệu streaming qua **Amazon Kinesis & AWS Glue**, truy vấn trực tiếp bằng **Amazon Athena** và **Amazon Redshift Serverless**, trực quan hóa báo cáo trên **Amazon QuickSight**.
* **Xương Sống Tích Hợp (Integration Backbone):** **Amazon EventBridge** đảm nhiệm vai trò định tuyến sự kiện bất đồng bộ giữa hệ thống hybrid, serverless và analytics, giúp phân tách lỏng (decoupling) các dịch vụ và xử lý theo thời gian thực.

---

## 2. Tối Ưu Hóa & Vận Hành Hệ Thống Serverless

* **Tối ưu chi phí & Quản trị tài chính (FinOps):**
  * Sử dụng **AWS Lambda** cho tác vụ chạy ngắt quãng/đột biến; dùng **ECS Fargate (Spot instances)** cho khối lượng công việc ổn định, liên tục để tránh chi phí Lambda tăng cao.
  * Thiết lập giới hạn ACU tối thiểu/tối đa cho **Aurora Serverless v2**; dùng DynamoDB On-Demand và chuyển sang Provisioned (có auto-scaling) khi lưu lượng ổn định.
  * Giám sát chi phí thời gian thực bằng **AWS Budgets** và **AWS Cost Anomaly Detection** để cảnh báo sớm bất thường.
* **Xử lý hiện tượng Khởi động nguội (Cold Start):**
  * Thiết lập **Provisioned Concurrency** cho các API quan trọng trong khung giờ cao điểm.
  * Tối ưu runtime (ARM64 / Graviton, Node.js / Go) giúp giảm thời gian cold start tự nhiên xuống dưới 100ms với chi phí thấp hơn.
* **Quản lý Trạng thái Phân tán (Distributed State):**
  * Thiết kế microservices hoàn toàn phi trạng thái (stateless); lưu trữ session/state tập trung tại **Amazon ElastiCache (Redis)** hoặc **Amazon DynamoDB**.
  * Điều phối quy trình phức tạp và xử lý lỗi tự động bằng **AWS Step Functions**.
  * Giám sát phân tán toàn diện từ đầu đến cuối với **AWS X-Ray** và **CloudWatch Embedded Metric Format (EMF)**.

---

## 3. Đường Ống Phân Tích & Quản Trị Dữ Liệu (Data Pipeline & Governance)

* **Kiến trúc dữ liệu Medallion (Amazon S3):**
  * **Bronze (Tầng Raw):** Khu vực lưu trữ dữ liệu thô bất biến; áp dụng **S3 Lifecycle Policies** tự động chuyển dữ liệu ít dùng sang S3 Glacier Deep Archive sau 90 ngày để tiết kiệm chi phí.
  * **Silver (Tầng Clean):** Dữ liệu đã được làm sạch, khử trùng lặp và chuyển đổi sang định dạng cột (Parquet).
  * **Gold (Tầng Business):** Dữ liệu tổng hợp chất lượng cao, sẵn sàng cho Athena, Redshift Serverless và QuickSight.
* **Đảm bảo Chất lượng Dữ liệu & Quản lý Schema:**
  * Sử dụng **AWS Glue Data Quality** kiểm tra tự động ngay trên luồng ingestion; bản ghi lỗi được chuyển vào Dead-Letter Queue (DLQ) để xử lý riêng.
  * **AWS Glue Schema Registry** kết hợp **Glue Crawlers / Data Catalog** tự động phát hiện và quản lý tiến hóa schema mà không làm gián đoạn truy vấn phía dưới.
* **Bảo mật & Quản trị Dữ liệu:**
  * **AWS Lake Formation** thiết lập phân quyền truy cập chi tiết đến từng cấp độ bảng, cột và dòng (fine-grained, column/row-level access control).
  * Truy vết nguồn gốc dữ liệu (Data Lineage) và kiểm toán tuân thủ thông qua **AWS CloudTrail**.
  * Áp dụng **Row-Level Security (RLS)** trên QuickSight theo vai trò/phòng ban để ngăn rò rỉ dữ liệu chéo.

---

## 4. Tích Hợp Hybrid & Điều Phối Container

* **Quản lý Container Hợp nhất:** Sử dụng **Amazon ECS Anywhere** / **EKS Anywhere** để điều phối và quản lý toàn bộ container tại on-premises lẫn trên AWS Cloud thông qua một bảng điều khiển (control plane) và CI/CD pipeline duy nhất.
* **Chiến lược Di chuyển Hệ thống Cũ (Legacy Migration):**
  * **Mô hình Strangler Fig (Cây bóp cổ):** Tách dần từng API/chức năng từ hệ thống monolithic on-premises chuyển lên microservices trên AWS qua API Gateway mà không gây gián đoạn người dùng.
  * **Change Data Capture (CDC):** Sử dụng **AWS DMS (Database Migration Service)** đồng bộ dữ liệu liên tục từ CSDL on-prem (Oracle/SQL Server) lên CSDL đám mây với độ trễ gần bằng 0 và không cần dừng hệ thống.
* **Giám sát Hybrid Tập trung:** Triển khai **AWS Systems Manager (SSM)** và **CloudWatch Agent** trên tất cả máy chủ on-prem và cloud để gom log, vá lỗ hổng hệ điều hành và thiết lập cảnh báo tập trung.

---

## 5. Lộ Trình Triển Khai & Quản Lý Rủi Ro (Kế Hoạch 12 Tháng)

```
[Tháng 1-2] Thiết lập Nền tảng & Landing Zone 
   └── AWS Control Tower, IAM Identity Center, Transit Gateway, Direct Connect + VPN

[Tháng 3-5] Data Lake & Thành tựu Sớm (Quick Wins) 
   └── S3 Data Lake, Glue, Lake Formation, DMS CDC, Báo cáo QuickSight BI

[Tháng 6-9] Hiện đại hóa Khối Ứng dụng Cốt lõi 
   └── Container hóa với ECS/Fargate, di chuyển API theo mô hình Strangler Fig

[Tháng 10-12] Chuyển đổi Toàn diện & Tối ưu Chi phí 
   └── Tắt hệ thống cũ, kích hoạt Savings Plans/Spot, diễn tập phục hồi thảm họa (DR)
```

* **Chiến Lược Rollback Không Gián Đoạn (Zero-Downtime Rollback):**
  * **Chuyển dịch lưu lượng theo tỷ lệ (Canary / Weighted Routing):** Điều phối lưu lượng tăng dần qua Route 53 / API Gateway ($5\% \to 25\% \to 100\%$). Khi có lỗi vượt ngưỡng, hoàn nguyên (revert) về on-premises ngay lập tức chỉ bằng một thao tác chuyển đổi định tuyến.
  * **Đồng bộ Dữ liệu 2 Chiều (Bi-Directional DMS):** Duy trì cơ chế sao chép hai chiều liên tục trong quá trình chuyển đổi, đảm bảo rollback mà không mất mát dữ liệu mới phát sinh.
  * **Tự Động Hóa Rollback bằng CI/CD & IaC:** Toàn bộ hạ tầng được định nghĩa bằng mã (Terraform / AWS CDK), tích hợp kiểm tra sức khỏe tự động (synthetic checks) để tự động rollback bản build lỗi trong vòng dưới 60 giây.
