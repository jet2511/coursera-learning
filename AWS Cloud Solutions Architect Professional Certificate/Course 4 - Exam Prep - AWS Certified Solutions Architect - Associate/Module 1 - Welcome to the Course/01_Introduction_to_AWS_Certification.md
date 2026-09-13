# Introduction to AWS Certification (SAA-C03 Exam Prep)

## 1. Tổng quan về Chứng chỉ AWS SAA-C03
- **Đối tượng mục tiêu:** Solutions Architect hoặc kỹ sư có từ 1 năm kinh nghiệm thiết kế hệ thống phân tán có tính sẵn sàng cao (High Availability), tối ưu chi phí (Cost Efficient), chịu lỗi (Fault Tolerant) và mở rộng linh hoạt (Scalable) trên AWS.
- **Khung tiêu chuẩn:** Dựa trên **AWS Well-Architected Framework** với đầy đủ 6 trụ cột (đã bao gồm trụ cột mới nhất: **Sustainability**).
- **Phạm vi cập nhật:** Phiên bản SAA-C03 bổ sung hơn 30 dịch vụ/tính năng mới so với phiên bản SAA-C02 trước đó.

---

## 2. Chi tiết 4 Domains trong Kỳ thi

| Domain & Trọng số | Trọng tâm cốt lõi | Dịch vụ then chốt (Key Services) | Kỹ thuật & Khái niệm cần nắm |
| :--- | :--- | :--- | :--- |
| **Domain 1:<br>Design Secure Architectures**<br><br>*(30% - Trọng số cao nhất)* | • Quản lý danh tính & quyền truy cập<br>• Bảo vệ Workload & VPC<br>• Bảo mật và mã hóa dữ liệu | • **Identity & Governance:** AWS IAM, IAM Identity Center (AWS SSO), AWS STS, Control Tower, Service Control Policies (SCPs)<br>• **Workload Security:** Amazon Cognito, GuardDuty, Macie, AWS Shield, AWS WAF, Secrets Manager<br>• **Data Security:** AWS KMS, AWS Certificate Manager (ACM) | • Áp dụng Least Privilege & SCPs ở cấp Multi-Account<br>• VPC Security: Security Groups, NACLs, VPC Flow Logs<br>• Quản lý KMS key policies, tự động xoay key (key rotation)<br>• Cấp phát & tự động gia hạn chứng chỉ TLS/SSL qua ACM<br>• Mã hóa dữ liệu at-rest & in-transit, chính sách lưu trữ (retention) và khôi phục (recovery) |
| **Domain 2:<br>Design Resilient Architectures**<br><br>*(26%)* | • Kiến trúc Loosely Coupled & Scalable<br>• Tính sẵn sàng cao (High Availability)<br>• Khả năng chịu lỗi (Fault Tolerance) & DR | • **Decoupling & Containers:** Amazon API Gateway, Amazon SQS, Amazon SNS, AWS Transfer Family, AWS Lambda, AWS Fargate, Amazon ECS, Amazon EKS<br>• **HA & Tracing:** Amazon Route 53, Amazon RDS Proxy, AWS X-Ray | • Phân biệt rõ **Horizontal Scaling** vs **Vertical Scaling**<br>• Thiết kế Microservices, Event-Driven, Immutable Infrastructure<br>• Tận dụng AWS Global Infra (Multi-AZ, Multi-Region) & Load Balancer (ALB/NLB)<br>• Chiến lược Disaster Recovery theo RPO/RTO (Backup & Restore, Pilot Light, Warm Standby, Active-Active)<br>• RDS Proxy quản lý connection pooling giảm tải cho DB |
| **Domain 3:<br>Design High-Performing Architectures**<br><br>*(24%)* | • Data Ingestion & Storage hiệu năng cao<br>• Caching & Tăng tốc mạng<br>• Tối ưu Serverless & Cơ chế Scaling | • **Storage & Data:** Amazon S3, EBS (gp3, io2), EFS, AWS Lake Formation (mới), AWS Glue, Amazon EMR, Amazon Kinesis, Amazon Athena, QuickSight, DataSync, Storage Gateway<br>• **Network & Cache:** CloudFront, Direct Connect, VPN, PrivateLink, ElastiCache (Redis/Memcached), DAX | • S3 high throughput: Transfer Acceleration, Multipart Upload, tối ưu phân vùng prefix<br>• Lựa chọn storage phù hợp throughput/IOPS/File system<br>• Tối ưu hiệu năng Serverless (Lambda concurrency, Fargate)<br>• Ingestion tốc độ cao và xử lý dữ liệu streaming (Kinesis)<br>• Caching nhiều tầng (tầng Database & CDN Edge) |
| **Domain 4:<br>Design Cost-Optimized Architectures**<br><br>*(20%)* | • Quản trị & theo dõi chi phí<br>• Right-sizing tài nguyên<br>• Tối ưu chi phí Storage, Database & Network | • **Cost Management Tools:** AWS Cost Explorer, AWS Budgets, Cost & Usage Reports (CUR), Resource Tags<br>• **Network Cost:** AWS Transit Gateway, VPC Peering, Direct Connect | • Các mô hình mua: On-Demand, Savings Plans, Reserved Instances (RI), Spot Instances<br>• Right-sizing cấu hình Compute (EC2, Lambda) & Database (RDS, DynamoDB)<br>• Thiết lập S3 Lifecycle Rules chuyển tier tự động (Standard -> IA -> Glacier)<br>• Đánh giá chi phí Data Transfer: VPC Peering vs Transit Gateway vs PrivateLink |

---

## 3. Cấu trúc Đề thi & Kỹ năng làm bài

### Hình thức câu hỏi:
1. **Multiple Choice (Đơn lựa chọn):** 1 đáp án đúng + 3 đáp án gây nhiễu (distractors).
2. **Multiple Response (Đa lựa chọn):** Chọn từ 2 đáp án đúng trở lên trong 5+ lựa chọn.

### Đặc điểm đề thi SAA-C03:
- **Độ dài và độ phức tạp cao:** Đa số là câu hỏi tình huống (scenario-based) dài từ vài câu đến vài đoạn văn. Các lựa chọn trả lời cũng dài và chi tiết.
- **Bẫy từ khóa (Distractors):** Các đáp án thường có cấu trúc câu gần như giống hệt nhau, chỉ khác biệt ở 1–2 từ khóa công nghệ (ví dụ: SQS vs SNS, S3 Standard-IA vs Glacier Instant Retrieval, EBS gp3 vs io2).

### Chiến lược làm bài:
1. **Đọc kỹ từng từ khóa:** Chú ý các điều kiện ràng buộc trong kịch bản (ví dụ: *"most cost-effective"*, *"least operational overhead"*, *"highest availability"*, *"sub-millisecond latency"*).
2. **Kỹ thuật loại trừ:** Loại bỏ các phương án distractor sai về mặt kiến trúc hoặc không thỏa mãn ràng buộc chính trước khi chọn đáp án tối ưu nhất.
3. **Bám sát Well-Architected Framework:** Đảm bảo giải pháp cân bằng giữa Security, Reliability, Performance Efficiency, Cost Optimization, Operational Excellence và Sustainability.