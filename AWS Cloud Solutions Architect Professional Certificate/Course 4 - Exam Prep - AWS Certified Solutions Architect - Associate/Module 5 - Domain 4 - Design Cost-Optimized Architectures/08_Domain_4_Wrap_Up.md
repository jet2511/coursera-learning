# Domain 4 Wrap-Up: Design Cost-Optimized Architectures

## 1. Bản chất & Triết lý Tối ưu Chi phí trên AWS (Iterative Cost Optimization)
- **Mô hình chi phí linh hoạt (Variable Cost Model):** Đám mây cho phép tiếp cận tối ưu hóa chi phí theo phương pháp lặp lại (iterative). Bạn có toàn quyền tác động và hạ thấp hóa đơn AWS hàng tháng bằng các quyết định điều chỉnh kiến trúc.
- **Quy trình tối ưu hóa liên tục:**
  1. Giám sát & Đo lường (Monitoring metrics qua CloudWatch, Cost Explorer).
  2. Phát hiện lãng phí / Underutilization.
  3. Áp dụng Right-sizing / Thay đổi cấu hình / Chuyển đổi Pricing Model.
  4. Lặp lại chu kỳ đánh giá cho các thành phần khác.

---

## 2. Tổng hợp Chiến lược Tối ưu Chi phí 4 Thành phần Cốt lõi

```
                             Chiến lược Tối ưu Chi phí Domain 4
                                              │
    ┌───────────────────┬─────────────────────┼─────────────────────┬───────────────────┐
    ▼                   ▼                     ▼                     ▼                   ▼
 [Storage]          [Compute]            [Databases]            [Network]          [Governance]
• S3 Lifecycle/     • Right-sizing       • Offload Blob to S3   • Local AZ routing  • Cost Explorer
  Intelligent Tier  • Spot / Savings     • Read Replicas / Cache• Free VPC Endpoints• Budgets Alerts
• EBS gp3 vs io2      Plans / RI         • Aurora Serverless    • 1 NAT GW for Dev  • Cost Allocation
• Delete unattached • Serverless Lambda  • Snapshots Lifecycle  • CloudFront cache    Tags
  EBS & Snapshots   • ECS Fargate vs EC2                        • VPN for Backup
```

---

### A. Storage (Lưu trữ)
- **S3 Tiers & Automation:**
  - **S3 Lifecycle Configurations:** Dùng khi biết trước mốc thời gian truy cập (ví dụ: Log lưu 30 ngày ở Standard $\to$ chuyển sang Standard-IA $\to$ 90 ngày chuyển sang Glacier $\to$ 365 ngày Xóa).
  - **S3 Intelligent-Tiering:** Dùng khi access patterns không thể dự đoán hoặc thay đổi liên tục.
- **EBS Volumes & Snapshots:**
  - Chọn đúng volume type: Ưu tiên **gp3** (tách biệt dung lượng và IOPS) thay vì io1/io2 đắt đỏ nếu không cần IOPS siêu lớn liên tục.
  - Sử dụng **AWS Trusted Advisor** để tìm và xóa unattached EBS volumes.
  - Dùng **Amazon Data Lifecycle Manager (DLM)** để tự động hóa xóa snapshots cũ hết hạn.

---

### B. Compute (Điện toán)
- **Right-sizing:** Chọn instance size nhỏ nhất đáp ứng performance baseline.
- **Pricing Models Matrix:**
  - **Spot Instances:** Giảm đến 90% (dành cho batch job, stateless web, tolerant to interruption).
  - **Savings Plans / Reserved Instances (RI):** Giảm đến 72% cho workload chạy ổn định dài hạn (1-3 năm).
  - **On-Demand:** Workload ngắn hạn, bất thường, dev/test không thường xuyên.
- **Serverless & Containers:**
  - **AWS Lambda:** Tối ưu hóa thời gian thực thi (runtime) và memory cấp phát để giảm chi phí per-invocation.
  - **ECS / EKS:** Đánh giá trade-off giữa Fargate (zero server management, pay-per-task) vs EC2 (quản lý cluster nhưng tối ưu chi phí khi có workload ổn định với RI/Spot).
- **Auto Scaling & Hibernation:** Co giãn theo nhu cầu thực tế và ngủ đông (hibernation) instance khi không sử dụng.

---

### C. Database (Cơ sở dữ liệu)
- **Data Offloading:** Tách file đính kèm/blobs ra **Amazon S3**, chuyển dữ liệu key-value/phi cấu trúc sang **DynamoDB**.
- **Scale Out Read Workload thông minh:** Sử dụng **Read Replicas** hoặc bộ nhớ đệm (**ElastiCache / DAX**) thay vì vội vàng nâng cấp (scale up) instance chính lên kích thước lớn đắt đỏ.
- **Aurora Serverless:** Tự động start/stop/scale cho các workload biến động, không liên tục.
- **Backup Retention:** Thiết lập chu kỳ giữ bản sao lưu/snapshots đúng chuẩn RTO/RPO, không lưu vô thời hạn.

---

### D. Networking (Mạng)
- **Giảm Data Transfer Egress:**
  - Giữ traffic trong cùng **Availability Zone** (miễn phí qua private IP).
  - Sử dụng **VPC Gateway Endpoints** cho **S3** và **DynamoDB** (miễn phí).
  - Dùng **Amazon CloudFront** để cache dữ liệu: truyền dữ liệu từ AWS Origin sang CloudFront Edge là **miễn phí ($0)** và giá data transfer out ra Internet rẻ hơn.
- **Tối ưu hóa chi phí NAT Gateway:**
  - Production: 1 NAT Gateway / AZ (High Availability).
  - Dev/Test: **1 Shared NAT Gateway** cho toàn bộ VPC.
- **Hybrid Connection Failover:** Dùng **Site-to-Site VPN** làm đường backup chi phí thấp cho **Direct Connect**.
- **Bảo mật truy cập EC2 Private:** Dùng **AWS Systems Manager Session Manager** (miễn phí, không cần Bastion host/NAT/VPN).

---

## 3. Quản trị & Báo cáo Chi phí (Cost Management & Governance)
- **Cost Allocation Tags:** Gắn thẻ tài nguyên để phân bổ chi tiêu chính xác theo dự án, môi trường (Prod/Dev), team sở hữu.
- **AWS Cost Explorer:** Xem báo cáo tổng quan trực quan, phân tích xu hướng chi tiêu.
- **AWS Cost and Usage Reports (CUR):** Báo cáo chi tiết nhất theo từng giờ, tài nguyên.
- **AWS Budgets:** Đặt cảnh báo và tự động hóa hành động (ngắt tài nguyên/gửi thông báo) khi chi phí vượt ngưỡng dự kiến.

---

## 4. Kim chỉ nam khi làm bài thi (Exam Strategy for Domain 4)
1. **Tìm giải pháp thỏa mãn yêu cầu kỹ thuật trước (Requirement First):** Nếu có nhiều phương án đáp ứng đủ kỹ thuật, mới so sánh chi phí để chọn **Most Cost-Effective**.
2. **Loại trừ các phương án Over-provisioning:** Phương án nào dùng instance quá lớn, lưu trữ dung lượng cố định cao, hoặc triển khai dư thừa không cần thiết $\to$ Loại bỏ.
3. **Ưu tiên Serverless / Managed Services** khi yêu cầu loại bỏ gánh nặng quản trị (No operational overhead) và không muốn trả phí tài nguyên nhàn rỗi (Zero idle cost).
