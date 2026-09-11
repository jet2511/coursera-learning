# Walkthrough Question 2.2: Multi-AZ High Availability & Extreme Performance Scaling (SAA-C03)

## 1. Đề Bài (Scenario)
> **Đề bài:** Một công ty trò chơi điện tử (*gaming company*) đang có sự tăng trưởng vượt bậc (*exponential growth*). Đã có nhiều lần khách hàng không thể truy cập tài nguyên do quá tải. Để đáp ứng nhu cầu ngày càng tăng, ban quản lý đang cân nhắc triển khai một giải pháp trên nền tảng đám mây. 
> Công ty đang tìm kiếm một giải pháp có thể **tương đương với mức độ phục hồi (resilience) của nhiều trung tâm dữ liệu on-premises (multiple data centers)** và đủ mạnh mẽ để chịu được **tải tăng trưởng đột biến/cực lớn (increased growth activity)**.
> 
> Cấu hình nào mà một Solutions Architect nên triển khai để đạt được kết quả mong muốn?

---

## 2. Phân Tích Yêu Cầu & Từ Khóa (Keyword Breakdown)
- **Gaming company / Exponential growth:** Yêu cầu xử lý tải cực lớn với độ trễ siêu thấp (*ultra-low latency*), lưu lượng biến động nhanh (*volatile traffic*).
- **Customers unable to access resources / Keep up with demand:** Cần cơ chế tự động co giãn (**Auto Scaling**) và cân bằng tải (**Load Balancing**).
- **Match resilience of multiple data centers:** Tương đương mô hình nhiều DC vật lý $\rightarrow$ Triển khai trải rộng trên **nhiều Availability Zones (Multi-AZ)** trong 1 Region.
- **Robust & Resilient:** Kết hợp Load Balancer + Auto Scaling Group phân bổ trên nhiều AZs.

---

## 3. Các Phương Án Lựa Chọn (Options)
- **A.** A VPC configured with an Application Load Balancer targeting an EC2 Auto Scaling group consisting of Amazon EC2 instances in **one Availability Zone**.
- **B.** Multiple Amazon EC2 instances configured within **peered VPCs** across two Availability Zones.
- **C.** **A VPC configured with a Network Load Balancer targeting an EC2 Auto Scaling group consisting of Amazon EC2 instances spanning two Availability Zones.** *(Đáp án chính xác)*
- **D.** A VPC configured with an Application Load Balancer targeting an EC2 Auto Scaling group consisting of Amazon EC2 instances **spanning two AWS Regions**.

---

## 4. Giải Thích Chi Tiết & Phân Tích Đáp Án

### Đáp án đúng: C (NLB + Multi-AZ Auto Scaling Group)
- **Network Load Balancer (NLB):** Hoạt động ở Layer 4 (TCP/UDP/TLS), có khả năng xử lý hàng triệu requests mỗi giây (*millions of requests per second*) với độ trễ ở mức microsecond (*ultra-low latency*), xử lý tức thì các xung lượng truy cập đột biến (*sudden and volatile traffic spikes*) — cực kỳ tối ưu cho ứng dụng gaming.
- **Auto Scaling Group spanning 2 AZs:** Đảm bảo khả năng co giãn tự động theo nhu cầu và cung cấp tính sẵn sàng cao (**High Availability & Fault Tolerance**), tương đương với việc chạy song song trên nhiều data centers vật lý.

### Tại sao các đáp án khác sai?
- **A — SAI:** Chỉ triển khai trên **một Availability Zone (Single AZ)**. Nếu AZ đó gặp sự cố phần cứng hoặc mất điện/mạng, toàn bộ ứng dụng sẽ bị sập (Single Point of Failure - SPOF), không đáp ứng yêu cầu High Availability / Multi-DC resilience.
- **B — SAI:** **VPC Peering** chỉ là cơ chế định tuyến kết nối mạng riêng giữa 2 VPCs; nó không cung cấp tính năng cân bằng tải (Load Balancing) hay tự động co giãn/thay thế instance lỗi (Auto Scaling).
- **D — SAI:** Một **VPC và Load Balancer (ALB/NLB) là Regional resources** (chỉ thuộc về 1 AWS Region cụ thể). Một VPC/ALB/ASG **không thể trải dài qua 2 AWS Regions khác nhau** (ASG và VPC chỉ có thể mở rộng qua nhiều Availability Zones trong cùng 1 Region).

---

## 5. Bảng So Sánh Kiến Trúc Cân Bằng Tải & Phạm Vi AWS (Exam Quick Reference)

| Tiêu chí | Application Load Balancer (ALB) | Network Load Balancer (NLB) |
| :--- | :--- | :--- |
| **Tầng mạng (OSI Layer)** | Layer 7 (HTTP / HTTPS / gRPC / WebSockets) | Layer 4 (TCP / UDP / TLS) |
| **Hiệu năng & Độ trễ** | Rất cao, xử lý định tuyến URL/Path phức tạp (Latency: ms) | **Cực đại (Extreme throughput)**, hàng triệu req/s (Latency: microseconds) |
| **Xử lý Spike Traffic** | Cần thời gian khởi tạo/scale dần theo tải | **Đáp ứng tức thời (Instant burst scaling)** không cần warm-up |
| **Static IP** | Sử dụng DNS Name động (nhiều IP thay đổi) | Cung cấp **1 Static IP / Elastic IP cố định cho mỗi AZ** |
| **Phạm vi hoạt động** | **Regional** (Trải rộng qua nhiều AZs trong 1 Region, KHÔNG xuyên Region) | **Regional** (Trải rộng qua nhiều AZs trong 1 Region, KHÔNG xuyên Region) |

---

## 6. Mẹo Thi SAA-C03 (Exam Tip)
> 1. **Phạm vi hạ tầng cốt lõi:** VPC, Subnets, ALB, NLB, và Auto Scaling Group **luôn giới hạn trong 1 Region** (chỉ có thể span nhiều AZs trong Region đó, không thể span qua 2 Regions).
> 2. **Dấu hiệu chọn NLB:** Khi đề bài nhắc tới **Gaming**, **Extreme Performance**, **Millions of requests/sec**, **TCP/UDP**, **Ultra-low latency**, hoặc yêu cầu **Static IP**.
