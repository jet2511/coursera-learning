# Whitepapers and FAQs - AWS Certified Solutions Architect - Associate

Tài liệu kỹ thuật chính thức (Whitepapers) và danh sách câu hỏi thường gặp (FAQs) là nguồn tài liệu cốt lõi giúp củng cố kiến thức nền tảng và xử lý các câu hỏi tình huống chuyên sâu trong đề thi SAA-C03.

---

## 1. Top Whitepapers Trọng Tâm

### 1.1. [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)
*Whitepaper quan trọng nhất - Kim chỉ nam cho hầu hết các câu hỏi thiết kế kiến trúc trong đề thi.*

| Trụ cột (Pillar) | Trọng tâm thiết kế & Khái niệm then chốt |
| :--- | :--- |
| **1. Operational Excellence** *(Vận hành xuất sắc)* | • Tự động hóa thay đổi (IaC - CloudFormation)<br>• Phản hồi sự cố tự động (CloudWatch Alarms, SNS, Lambda)<br>• Học hỏi từ sự cố vận hành |
| **2. Security** *(Bảo mật)* | • Áp dụng nguyên tắc Least Privilege (IAM, SCPs)<br>• Bảo mật nhiều lớp (Defense in Depth: VPC, WAF, Shield, Security Groups)<br>• Mã hóa dữ liệu at-rest (KMS) & in-transit (TLS qua ACM)<br>• Truy vết & kiểm toán tự động (CloudTrail, GuardDuty, Macie) |
| **3. Reliability** *(Độ tin cậy)* | • Thiết kế kiến trúc chịu lỗi, tự phục hồi (Auto Scaling, Multi-AZ, Multi-Region)<br>• Phân tách thành phần (Decoupling bằng SQS, SNS, EventBridge)<br>• Kế hoạch khắc phục sự cố (Disaster Recovery: RPO & RTO) |
| **4. Performance Efficiency** *(Hiệu quả hiệu năng)* | • Sử dụng kiến trúc Serverless (Lambda, Fargate) và Microservices<br>• Caching đa tầng (CloudFront CDN, ElastiCache, DAX)<br>• Lựa chọn đúng loại storage/compute phù hợp khối lượng công việc (EBS gp3/io2, EFS, S3) |
| **5. Cost Optimization** *(Tối ưu chi phí)* | • Đo lường và giám sát chi phí liên tục (Cost Explorer, AWS Budgets, CUR)<br>• Right-sizing tài nguyên compute/database<br>• Tối ưu mô hình thanh toán (Savings Plans, Reserved Instances, Spot Instances)<br>• Tự động chuyển tier lưu trữ (S3 Lifecycle policies) |
| **6. Sustainability** *(Bền vững - Trụ cột mới)* | • Tối ưu hóa mức độ sử dụng tài nguyên (giảm tiêu thụ năng lượng/tài nguyên nhàn rỗi)<br>• Lựa chọn Managed Services thay vì tự quản lý EC2<br>• Chọn region có phát thải carbon thấp và kiến trúc serverless/ARM-based Graviton |

---

### 1.2. [AWS Security Best Practices](https://docs.aws.amazon.com/whitepapers/latest/introduction-aws-security/security-of-the-aws-infrastructure.html)
- **Mô hình Trách nhiệm Chung (Shared Responsibility Model):**
  - *AWS chịu trách nhiệm về:* Security **OF** the Cloud (phần cứng, hạ tầng mạng, data center vật lý, hypervisor).
  - *Khách hàng chịu trách nhiệm về:* Security **IN** the Cloud (dữ liệu, cấu hình IAM, OS patch, tường lửa/Security Groups, mã hóa).
- **Nguyên tắc bảo vệ dữ liệu:**
  - Tách biệt môi trường (Multi-Account qua AWS Organizations & SCPs).
  - Quản lý tập trung khóa mã hóa (KMS) và luân chuyển khóa (Key Rotation) định kỳ.

---

## 2. Top FAQs Cần Nắm Cho Từng Dịch Vụ Cốt Lõi

| Dịch vụ AWS | Các chủ đề & Khái niệm thường xuất hiện trong câu hỏi thi |
| :--- | :--- |
| **[Amazon EC2](https://aws.amazon.com/ec2/faqs/?saa=sec&sec=prep)** | • **Pricing models:** On-Demand, Spot (chấp nhận gián đoạn, tiết kiệm 90%), Reserved Instances (1-3 năm), Savings Plans.<br>• **Placement Groups:** Cluster (độ trễ thấp, throughput cao), Spread (giảm thiểu rủi ro lỗi phần cứng cùng rack), Partition (phân tán node cho Hadoop/Cassandra/Kafka).<br>• **Storage attachment:** EBS root volume lifecycles, Instance Store (ephemeral - mất dữ liệu khi stop/terminate). |
| **[Amazon S3](https://aws.amazon.com/s3/faqs/?saa=sec&sec=prep)** | • **Storage Classes:** Standard, Intelligent-Tiering, Standard-IA, One Zone-IA, Glacier Instant/Flexible/Deep Archive.<br>• **Security & Sharing:** Bucket Policies, S3 Pre-signed URLs, Cross-Origin Resource Sharing (CORS), Cross-Region Replication (CRR).<br>• **Performance:** Multipart Upload (bắt buộc cho file > 5GB, khuyến nghị > 100MB), S3 Transfer Acceleration, S3 Select. |
| **[Amazon VPC](https://aws.amazon.com/vpc/faqs/?saa=sec&sec=prep)** | • **Subnets & Routing:** Public Subnet (có route ra Internet Gateway - IGW), Private Subnet (truy cập Internet 1 chiều qua NAT Gateway / NAT Instance).<br>• **Security Layers:** Security Groups (Stateful, áp dụng ở cấp ENI) vs Network ACLs (Stateless, áp dụng ở cấp Subnet).<br>• **Connectivity:** VPC Peering (không hỗ trợ transitive routing), AWS Transit Gateway (kết nối Hub-and-Spoke nhiều VPC & On-Premises), VPC Endpoints (Gateway Endpoint cho S3/DynamoDB, Interface Endpoint qua PrivateLink). |
| **[Amazon Route 53](https://aws.amazon.com/route53/faqs/?saa=sec&sec=prep)** | • **Routing Policies:** Simple, Weighted (A/B testing, blue-green), Latency-based, Failover (Active-Passive với Health Checks), Geolocation (theo vị trí người dùng), Geoproximity, Multi-Value Answer.<br>• **Record Types:** Phân biệt **Alias Record** (trỏ trực tiếp vào AWS resources như ALB, CloudFront, S3 bucket endpoint, hoàn toàn miễn phí truy vấn DNS) vs **CNAME Record**. |
| **[Amazon RDS](https://aws.amazon.com/rds/faqs/?saa=sec&sec=prep)** | • **Multi-AZ Deployment:** Đồng bộ (Synchronous replication) cho High Availability & Disaster Recovery; tự động failover.<br>• **Read Replicas:** Không đồng bộ (Asynchronous replication) phục vụ mở rộng đọc (Read Scalability), có thể promote thành Standalone DB hoặc đặt ở Multi-Region.<br>• **Amazon Aurora:** Tự động mở rộng storage lên đến 128TB, replicate 6 bản copy qua 3 AZs; hỗ trợ Aurora Serverless & Global Database. |
| **[Amazon SQS](https://aws.amazon.com/sqs/faqs/?saa=sec&sec=prep)** | • **Standard Queue:** Throughput gần như vô hạn, Best-effort ordering (có thể không đúng thứ tự), At-least-once delivery (có thể bị duplicate).<br>• **FIFO Queue:** Đảm bảo đúng thứ tự chính xác (First-In-First-Out), Exactly-once processing, throughput giới hạn (3.000 msg/s khi batching).<br>• **Tính năng quan trọng:** Visibility Timeout (thời gian ẩn tin nhắn khi worker đang xử lý), Long Polling (WaitTimeSeconds > 0 giúp giảm chi phí và độ trễ), Dead Letter Queue (DLQ). |