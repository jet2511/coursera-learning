# Customer #3: Solution Overview — Complete Hybrid Architecture Review

## 1. Overview & Context
Buổi làm việc giữa Morgan (AWS Solutions Architect) và Raf (Đại diện khách hàng - Công ty bảo hiểm) nhằm rà soát bản thiết kế kiến trúc số hóa (digital architecture diagram) cho mô hình **Hybrid Cloud**, di chuyển một phần containerized workloads lên AWS trong khi vẫn giữ các thành phần on-premises.

---

## 2. Core Architectural Components Breakdown

### 2.1. Network Connectivity
* **AWS Direct Connect (DX):**
  * Được chọn làm kết nối chính thay vì AWS VPN.
  * **Lý do:** Khách hàng cần truyền tải khối lượng dữ liệu lớn (high volume) với băng thông và độ trễ ổn định, nhất quán (consistent throughput & low latency).

### 2.2. Container Orchestration & Registry
* **Amazon ECS (Elastic Container Service):** Quản lý containers trên AWS.
* **Amazon ECS Anywhere:** 
  * Quản lý thống nhất cả các containers còn lại tại On-Premises Data Center.
  * Chỉ cần viết **Task Definitions** chuẩn hóa, không cần thay đổi source code của container.
* **Container Registry:**
  * Khách hàng hiện đang dùng **Docker Hub** $\rightarrow$ Có thể tiếp tục giữ nguyên để tích hợp với ECS.
  * Đề xuất song song **Amazon ECR (Elastic Container Registry)** để tối ưu bảo mật và tốc độ trong hệ sinh thái AWS.

### 2.3. Compute & Load Balancing
* **EC2-based ECS Cluster (Bring Your Own AMI):**
  * Chọn EC2 instances thay vì Fargate để khách hàng có thể dùng Custom AMI và giữ quyền SSH access vào underlying instances, giúp duy trì tính đồng nhất trong quy trình vận hành giữa On-premises và Cloud.
  * **Amazon EC2 Auto Scaling:** Tự động co giãn cụm cluster EC2 theo nhu cầu tải.
* **Application Load Balancer (ALB):** Phân phối lưu lượng truy cập HTTP/HTTPS tới các container tasks.

### 2.4. Database Architecture
* **Amazon RDS for PostgreSQL (Multi-AZ Deployment):**
  * Phân bổ instance chính (Primary) và instance dự phòng (Standby) trên **2 Availability Zones (AZs)** khác nhau.
  * Đảm bảo tính chịu lỗi (fault-tolerant) và khả năng tự động failover nếu một AZ gặp sự cố.

### 2.5. Storage & Hybrid File Sharing
* **AWS Storage Gateway (File Gateway):**
  * Cho phép các containers chạy On-premises đọc/ghi file lên AWS qua giao thức chuẩn **NFS**.
  * **Local Cache:** Giữ bản cache dữ liệu ngay tại data center để giải quyết triệt để bài toán độ trễ (latency).
  * **Long-term Storage:** Bất đồng bộ đẩy dữ liệu lưu trữ lâu dài lên **Amazon S3** với độ bền cao và chi phí tối ưu.

### 2.6. VPC Security & Network Topology
* **Private Subnets:** Cả ECS Cluster và RDS instances đều nằm hoàn toàn trong Private Subnets (không có public IP).
* **Public Subnets & NAT Gateway:** Đặt 1 NAT Gateway tại mỗi AZ trong Public Subnet để hỗ trợ lưu lượng ra ngoài Internet (egress-only: tải bản vá, image, dependencies) mà không làm lộ hạ tầng ra ngoài Internet.

### 2.7. Hybrid Operations & Governance
* **AWS Systems Manager (SSM):** Công cụ quản lý tập trung cho cả EC2 trên AWS và máy chủ on-premises (chạy scripts, patch management, kiểm kê tài nguyên).
* **AWS Backup:** Quản lý chính sách sao lưu (backup policy) tập trung cho toàn bộ dữ liệu trên AWS lẫn on-premises từ một bảng điều khiển duy nhất.

---

## 3. Architecture Summary Mapping

| Hạng mục | Dịch vụ AWS | Vai trò kiến trúc |
| :--- | :--- | :--- |
| **Hybrid Connectivity** | AWS Direct Connect | Đường truyền vật lý chuyên dụng, thông lượng cao, ổn định |
| **Container Management**| Amazon ECS + ECS Anywhere | Điều phối container thống nhất trên cả Cloud và On-premises |
| **Container Compute** | Amazon EC2 (Multi-AZ + ASG) | Hỗ trợ custom AMI và SSH access theo yêu cầu vận hành |
| **Load Balancing** | Application Load Balancer (ALB) | Định tuyến thông minh tới các container targets |
| **Relational Database** | Amazon RDS PostgreSQL (Multi-AZ)| Tính sẵn sàng cao, sao chép đồng bộ, tự động failover |
| **Hybrid Storage** | Storage File Gateway + Amazon S3 | Giao thức NFS cho On-prem, cache cục bộ giảm latency, lưu trữ S3 |
| **Internet Egress** | NAT Gateway (Multi-AZ) | Cho phép private resources tải cập nhật internet an toàn |
| **Operations & Backup** | AWS Systems Manager & AWS Backup | Quản lý bản vá, script và chính sách sao lưu tập trung hybrid |
