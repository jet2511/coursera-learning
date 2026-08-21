# Tóm Tắt Video: Customer #3 - Solution Overview (Kiến Trúc Hybrid Container trên AWS)

> **Khóa học:** Course 2 - Architecting Solutions on AWS  
> **Module:** Module 3 - Designing a hybrid solution for container based workloads on AWS  
> **Chủ đề:** Đánh giá giải pháp kiến trúc đám mây kết hợp (Hybrid Cloud) cho khối lượng công việc Container hóa giữa On-Premises và AWS.

---

## 1. Kết Nối Mạng (Network Connectivity)
* **AWS Direct Connect:**
  * Lựa chọn tối ưu hơn VPN để kết nối Trung tâm Dữ liệu (On-Premises Data Center) với AWS.
  * **Lý do:** Đáp ứng nhu cầu truyền tải khối lượng dữ liệu lớn (high volume) với băng thông và thông lượng ổn định, nhất quán (consistent throughput).

---

## 2. Điều Phối Container & Lưu Trữ Image (Container Orchestration & Registry)
* **Amazon ECS & ECS Anywhere:**
  * **Trên AWS:** Các container chuyển dịch lên đám mây được quản lý bởi **Amazon ECS**.
  * **Tại On-Premises:** Các container giữ lại tại trung tâm dữ liệu được điều phối bởi tính năng **ECS Anywhere**.
  * **Yêu cầu:** Tạo **Task Definition** cho toàn bộ container; không cần thay đổi mã nguồn hoặc cấu trúc container hiện tại.
* **Container Registry:**
  * Có thể tiếp tục tích hợp với **Docker Hub** hiện tại hoặc chuyển đổi sang **Amazon ECR (Elastic Container Registry)** để quản lý tập trung và tối ưu bảo mật.

---

## 3. Hạ Tầng Tính Toán & Cân Bằng Tải (Compute & Load Balancing)
* **Amazon EC2 Launch Type cho ECS Cluster:**
  * Chọn cluster chạy trên nền tảng **EC2** (thay vì Fargate) để khách hàng có thể sử dụng AMI tùy chỉnh (Bring Your Own AMI) và duy trì quyền **SSH** trực tiếp vào máy chủ, đảm bảo quy trình vận hành tương đồng giữa on-premises và cloud.
  * Sử dụng **Amazon EC2 Auto Scaling** để mở rộng/thu hẹp dung lượng cụm máy chủ tự động.
* **Application Load Balancer (ALB):** Phân phối lưu lượng truy cập vào các container microservices.

---

## 4. Cơ Sở Dữ Liệu & Độ Sẵn Sàng Cao (Database & High Availability)
* **Amazon RDS PostgreSQL (Multi-AZ):**
  * Triển khai cấu hình **Multi-AZ** với các instance đặt trải dài qua ít nhất **2 Availability Zones (AZs)** độc lập.
  * Phân tán cả ECS EC2 instances và RDS Database đa vùng giúp hệ thống có khả năng chịu lỗi (fault-tolerant) và đảm bảo tính liên tục của dịch vụ nếu một AZ gặp sự cố.

---

## 5. Lưu Trữ File Lai (Hybrid File Storage)
* **AWS Storage File Gateway (NFS):**
  * Giải quyết yêu cầu các container chạy ở On-Premises cần lưu trữ file lên AWS qua giao thức **NFS**.
  * **Cơ chế hoạt động:** Duy trì **bộ nhớ đệm cục bộ (local cache)** tại Data Center để giảm độ trễ truy cập (low latency), sau đó tự động đẩy dữ liệu bất đồng bộ lên **Amazon S3** để lưu trữ dài hạn.

---

## 6. Bảo Mật Mạng VPC & Quản Lý Tập Trung (VPC Security & Governance)
* **Mô hình Mạng VPC:**
  * Cụm ECS Cluster và RDS instances được đặt hoàn toàn trong **Private Subnet** để cách ly với Internet.
  * Bố trí **NAT Gateway** tại **Public Subnet** của từng AZ để cho phép các instance tải bản cập nhật ra ngoài Internet mà không bị lộ địa chỉ IP ra công cộng.
* **Quản trị & Sao lưu tập trung:**
  * **AWS Systems Manager (SSM):** Dùng để chạy script tự động, vá lỗi bảo mật (patching) và quản lý vận hành đồng bộ trên cả máy chủ AWS lẫn On-Premises.
  * **AWS Backup:** Quản lý, lập lịch và giám sát toàn bộ chính sách sao lưu (backup) cho tài nguyên đám mây và tại chỗ từ một giao diện duy nhất.
