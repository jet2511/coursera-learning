# Design Cost-Optimized Compute Solutions

## 1. 5 Trụ Cột Tối Ưu Hóa Chi Phí Compute (Cost Optimization Pillars)

### Trụ cột 1: Right-Sizing (Chọn đúng loại & kích thước tài nguyên)
- **Nguyên tắc:** Lựa chọn loại instance rẻ nhất đáp ứng đủ yêu cầu kỹ thuật/hiệu năng, tránh over-provisioning.
- **Instance Families:**
  - *Compute Optimized (C-family):* Xử lý tính toán cao, batch processing.
  - *Memory Optimized (R/X-family):* Xử lý in-memory caching, cơ sở dữ liệu lớn.
  - *General Purpose (M/T-family):* Cân bằng giữa CPU, RAM, Network (T-family burstable cho workload tải không đều).
- **Managed & Serverless Services:** Thay vì tự vận hành và duy trì server ảo, chuyển sang AWS Lambda, ECS/Fargate, hoặc Aurora Serverless để cắt giảm chi phí hạ tầng và license bản quyền.

---

### Trụ cột 2: Tăng cường tính co giãn (Increase Elasticity)
- **Mô hình trả tiền theo nhu cầu thực tế (Pay-for-what-you-use):**
  - Sử dụng **nhiều instance nhỏ (horizontal scaling)** thay vì một vài instance lớn (vertical scaling) để linh hoạt co giãn theo lượng tải.
  - Tích hợp **Amazon EC2 Auto Scaling** để scale-in (giảm số lượng instance) ngoài giờ cao điểm hoặc khi nhàn rỗi.
  - Tích hợp **Elastic Load Balancing (ELB)** với Auto Scaling Group (ASG): dùng metric như `RequestCountPerTarget` trên Application Load Balancer (ALB) để tự động điều chỉnh số lượng instance chính xác theo lưu lượng truy cập.
  - Cấu hình ELB health checks trên ASG để phát hiện và thay thế sớm các instance lỗi mà không lãng phí chi phí chạy vô ích.

---

### Trụ cột 3: Chọn đúng mô hình định giá (Pricing Models)

| Mô hình định giá | Đặc điểm & Mức độ tối ưu | Trường hợp sử dụng điển hình |
| :--- | :--- | :--- |
| **On-Demand** | Không cam kết, tính phí theo giây/giờ, chi phí cao nhất trên đơn vị thời gian. | Workload ngắn hạn, đột xuất, chưa dự đoán được lưu lượng hoặc môi trường dev/test tạm thời. |
| **Spot Instances** | Giảm giá tới **90%** so với On-Demand, nhưng **có thể bị ngắt (interrupt)** với thông báo trước 2 phút. | Workload chịu lỗi tốt (fault-tolerant, stateless), batch jobs, HPC, xử lý big data. |
| **Savings Plans** | Cam kết mức chi tiêu (\$ / giờ) trong 1 hoặc 3 năm. Giảm tới 72%. Rất linh hoạt (chuyển đổi giữa EC2, Fargate, Lambda). | Workload chạy ổn định, dài hạn và cần sự linh hoạt giữa các dịch vụ compute. |
| **Reserved Instances (RI)** | Cam kết sử dụng instance cụ thể (Standard / Convertible) trong 1 hoặc 3 năm. Giảm tới 72%. | Workload chạy ổn định liên tục 24/7 (stateful database, ERP backend). |
| **Dedicated Hosts / Instances** | Thuê server vật lý riêng cho doanh nghiệp, chi phí cao. | Yêu cầu nghiêm ngặt về tuân thủ (compliance) hoặc sử dụng giấy phép phần mềm theo socket/core (BYOL). |

---

### Trụ cột 4: Khớp lưu trữ với mức sử dụng compute (Match Storage to Usage)
- Right-size dung lượng và loại volume EBS (gp3, io2, st1) phù hợp với instance để tránh lãng phí chi phí storage kèm theo compute.

---

### Trụ cột 5: Đo lường, giám sát và cải tiến liên tục (Continuous Improvement)
- **Amazon CloudWatch:** Theo dõi CPU, RAM, Network, Storage utilization để xác định các instance hoạt động dưới công suất cần downsize hoặc tắt.
- **AWS Cost Explorer & AWS Budgets:** Đặt hạn mức chi phí, phân tích xu hướng chi tiêu và kích hoạt tự động hóa khi vượt ngân sách.
- **Cost Allocation Tags:** Gắn thẻ phân bổ chi phí theo môi trường, phòng ban, ứng dụng để tối ưu hoá và theo dõi chính xác.
- **AWS Trusted Advisor:** Tự động quét và phát hiện các instance nhàn rỗi (idle), low-utilization EC2 instances.

---

## 2. Hybrid & Edge Compute Cost Optimization
- **AWS Outposts:** Khi chạy dịch vụ quản lý của AWS trên Outpost, chi phí chỉ tính trên mức sử dụng instance-hour (không tính trùng phí phần cứng bên dưới).
- **Edge Computing (CloudFront, AWS IoT, Wavelength):** Đưa năng lực xử lý/cache ra gần người dùng hơn, giúp giảm thiểu đáng kể chi phí truyền dữ liệu ra ngoài (Data Transfer Out - Egress) và loại bỏ việc duy trì on-premises data center.

---

## 3. Key Exam Takeaways
1. **Chấp nhận gián đoạn + Tiết kiệm tối đa chi phí $\to$ Spot Instances.**
2. **Workload ổn định dài hạn + Cần linh hoạt giữa EC2, Fargate, Lambda $\to$ Compute Savings Plans.**
3. **Giảm chi phí compute cho web server $\to$ Dùng ASG với nhiều instance nhỏ + ALB scaling metric (`RequestCountPerTarget`).**
4. **Cắt giảm chi phí license phần mềm $\to$ Dùng AWS native database/compute (Amazon Aurora / Graviton processor).**
