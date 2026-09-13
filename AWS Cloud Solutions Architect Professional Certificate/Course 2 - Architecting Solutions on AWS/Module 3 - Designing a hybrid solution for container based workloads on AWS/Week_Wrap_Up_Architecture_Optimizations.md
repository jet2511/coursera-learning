# Week Wrap-Up: Taking this Architecture to the Next Level (Optimization & DR Strategies)

## 1. Overview & Objectives
Buổi thảo luận giữa Morgan và Raf (AWS Solutions Architects) nhằm phân tích các phương án **nâng cấp, tối ưu hóa chi phí và tăng cường tính sẵn sàng (Resilience / Disaster Recovery)** cho bản kiến trúc Hybrid Cloud của Customer #3 (Enterprise Insurance Company).

---

## 2. Core Architectural Optimizations & Enhancements

### 2.1. Hybrid Connectivity Redundancy: VPN Backup for Direct Connect
* **Vấn đề:** AWS Direct Connect cung cấp tính sẵn sàng cao ở phía AWS (2 endpoints trên 2 AZs), nhưng tại On-Premises Data Center vẫn có thể gặp rủi ro hỏng hóc thiết bị router, đứt cáp vật lý hoặc lỗi cấu hình.
* **Giải pháp:** Thiết lập **AWS Site-to-Site VPN qua Internet** làm đường kết nối dự phòng (failover redundancy).
* **Lợi ích:** Đảm bảo hệ thống luôn có kênh liên lạc dự phòng với chi phí tối ưu, duy trì kết nối liên tục khi Direct Connect gặp sự cố.

### 2.2. Relational Database Scaling: RDS Storage Auto Scaling
* **Vấn đề:** Amazon RDS instance không tự động scale in/out như Serverless. Nếu dung lượng lưu trữ đầy, ứng dụng sẽ bị gián đoạn và đòi hỏi DBA can thiệp thủ công.
* **Giải pháp:** Kích hoạt tính năng **RDS Storage Auto Scaling**.
* **Lợi ích:** Hệ thống tự động mở rộng dung lượng ổ đĩa cơ sở dữ liệu dựa trên dung lượng tiêu thụ thực tế mà không gây downtime hay cần can thiệp thủ công.

### 2.3. Disaster Recovery (DR) & Multi-Region Strategies
Doanh nghiệp bảo hiểm yêu cầu chuẩn DR doanh nghiệp khắt khe. Các chiến lược Multi-Region được đề xuất:
* **Các mô hình DR:**
  * **Multi-Site Active/Active:** Chạy đồng thời toàn bộ workload trên 2 Region (chi phí cao nhất, RTO/RPO gần bằng 0).
  * **Warm Standby:** Chạy một phiên bản thu nhỏ (scaled-down fleet) ở Region thứ 2.
  * **Pilot Light:** Chỉ duy trì dữ liệu đồng bộ và các dịch vụ lõi tối thiểu ở Region thứ 2; compute fleet chỉ bật lên khi xảy ra thảm họa.
* **Yêu cầu then chốt:** Cần áp dụng **Infrastructure as Code (IaC)** (AWS CloudFormation / Terraform / AWS CDK) để đảm bảo môi trường ở Region thứ hai được sao chép đồng nhất 100% với Region chính.

### 2.4. Storage Optimization & Replication: S3 CRR & Lifecycle Policies
* **S3 Cross-Region Replication (CRR):** Tự động sao chép các đối tượng (objects) sang Region phụ để phục vụ DR (vẫn hỗ trợ mã hóa dữ liệu).
* **S3 Lifecycle Policies & Intelligent-Tiering:** Tự động chuyển đổi các đối tượng cũ hoặc ít truy cập sang các lớp lưu trữ rẻ hơn (S3 Standard-IA, Glacier).
* **Ý nghĩa:** Khi dữ liệu bị nhân bản nhiều bản trên nhiều Region, Lifecycle Policies là bắt buộc để **kiểm soát và tối ưu hóa chi phí lưu trữ**.

### 2.5. Database Cross-Region Replication
* **RDS Cross-Region Read Replicas:**
  * PostgreSQL trên Amazon RDS hỗ trợ tạo Read Replicas tại một Region khác.
  * Khi Region chính gặp sự cố, Read Replica tại Region phụ có thể được thăng cấp (promoted) thành Primary Database ngay lập tức.
* **AWS Database Migration Service (AWS DMS):** Lựa chọn thay thế để thực hiện continuous data replication nếu không dùng cơ chế replica native của RDS/Aurora.

### 2.6. Container Compute Layer Scaling (ECS on EC2)
* **Two-Layer Scaling:**
  1. **Infrastructure Layer:** Co giãn số lượng EC2 instances bằng **Auto Scaling Groups (ASG)** hoặc **ECS Capacity Providers**.
  2. **Container/Task Layer:** Co giãn số lượng tasks/containers bằng **ECS Service Auto Scaling** (dựa trên CPU, Memory hoặc custom CloudWatch metrics).
* **Lưu ý:** Cần phối hợp đồng bộ cả 2 lớp scaling để tránh tình trạng container cần scale nhưng cụm EC2 không đủ dung lượng (resource starvation).

---

## 3. Summary Optimization Matrix

| Hạng mục | Giải pháp nâng cấp | Lợi ích chính |
| :--- | :--- | :--- |
| **Network** | Site-to-Site VPN backup cho Direct Connect | Tự động failover khi router on-premise hoặc cáp DX gặp sự cố |
| **Storage (Database)** | RDS Storage Auto Scaling | Mở rộng dung lượng lưu trữ tự động, tránh downtime |
| **Disaster Recovery** | Multi-Region Deployment (Pilot Light / Warm Standby) + IaC | Khôi phục hệ thống nhanh chóng khi toàn bộ một Region gặp sự cố |
| **Storage (Object)** | S3 Cross-Region Replication + Lifecycle Policies | Sao lưu dữ liệu đa vùng kết hợp tối ưu hóa chi phí lưu trữ |
| **Database DR** | RDS Cross-Region Read Replicas (PostgreSQL) | Đồng bộ dữ liệu liên tục, promote thành Primary DB khi cần |
| **Container Compute**| ECS Capacity Providers + Service Auto Scaling | Tự động cân bằng tải và co giãn hai chiều (task & host EC2) |
