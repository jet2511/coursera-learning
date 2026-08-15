# Tóm tắt bài học: Customer #3 - Use Case & Requirements

**Khóa học:** Course 2 - Architecting Solutions on AWS  
**Khách hàng:** AnyCompany Insurance (Đại diện: Raf)  
**Chủ đề:** Khảo sát bối cảnh, trường hợp sử dụng và xác định yêu cầu thiết kế giải pháp Hybrid cho ứng dụng Container  
**Vị trí:** Module 3 - Designing a hybrid solution for container based workloads on AWS

---

## 1. Bối cảnh & Hiện trạng của Khách hàng (Current State & Background)
* **Khách hàng:** **AnyCompany Insurance** – Đang trong lộ trình chuyển đổi dần hạ tầng lên AWS theo thời hạn hết hạn hợp đồng thuê trung tâm dữ liệu (data center contracts).
* **Tình huống hiện tại:** 
  * Đã chuyển một phần hệ thống lên AWS.
  * Hiện tại, **50% số lượng máy chủ on-premise đã hết hạn hợp đồng**, trong khi 50% còn lại vẫn còn hợp đồng trong vài năm tới.
* **Mục tiêu giai đoạn này:**
  * Di chuyển 50% khối lượng công việc (workloads) lên AWS.
  * Giữ 50% còn lại tại On-Premises trong vài năm trước khi hoàn tất chuyển toàn bộ lên AWS.
  * $\rightarrow$ **Mô hình triển khai lai (Hybrid Cloud Deployment)** giữa Data Center On-Premise và AWS Cloud.

---

## 2. Các yêu cầu kỹ thuật & Ràng buộc kiến trúc (Architecture Requirements)

### A. Kết nối mạng Hybrid & Hiệu năng (Hybrid Network Connectivity)
* **Kết nối chuyên dụng:** Cần duy trì kết nối mạng bảo mật, tin cậy và chuyên dụng (*Dedicated Connectivity*) giữa On-Premises và AWS.
* **Độ trễ và Băng thông:** Yêu cầu **độ trễ thấp nhất có thể (lowest latency)** và **thông lượng ổn định (consistent throughput)** để đảm bảo không bị suy giảm hiệu năng khi phân tách hệ thống làm đôi.
* **Lưu lượng mạng lớn:** Dự kiến có khối lượng lớn dữ liệu trao đổi giữa On-Premises và AWS.

### B. Lưu trữ & Truy cập tệp tin (File Storage & Data Access)
* Các ứng dụng chạy tại On-Premises Data Center sẽ liên tục tạo ra các file dữ liệu mà ứng dụng trên AWS Cloud cần truy cập.
* **Vị trí lưu trữ mong muốn:** Khách hàng muốn lưu trữ dữ liệu này trực tiếp trên AWS để chuẩn bị sẵn cho tương lai khi toàn bộ hệ thống chuyển lên đám mây.

### C. Khối lượng công việc Container (Container Workloads & Orchestration)
* **Công nghệ ứng dụng:** Tất cả các ứng dụng (ngoại trừ cơ sở dữ liệu) hiện đều đang đóng gói bằng **Containers** và muốn tiếp tục chạy bằng Containers trên AWS.
* **Bảo mật mạng (Network Isolation):** Toàn bộ ứng dụng là **ứng dụng nội bộ (Internal Applications)**. **Tuyệt đối không cho phép truy cập từ Internet** tới các container trên AWS (100% Private Workloads).
* **Công cụ quản lý & Điều phối đồng nhất (Consistent Tooling):** 
  * Khách hàng muốn sử dụng chung công cụ quản lý và điều phối container (**same container orchestrator & management tools**) trên cả 2 môi trường On-Premises và AWS.
  * Tránh việc vận hành 2 hệ thống điều phối container hoàn toàn khác biệt.

### D. Cơ sở dữ liệu (Database Migration)
* Database on-premise hiện đang sử dụng **PostgreSQL** (chạy trên máy chủ, không đóng gói container).
* Kế hoạch di chuyển một số PostgreSQL DB lên AWS đồng thời cùng với container workloads.
* **Chiến lược di chuyển (Migration Strategy):** Tiếp cận theo hướng **Lift-and-Shift / Replatform** tương thích tối đa, **không viết lại mã nguồn ứng dụng (No application code rewriting)**.

### E. Tính sẵn sàng cao & Chịu lỗi (High Uptime & Resilience)
* Yêu cầu thời gian hoạt động liên tục ở mức tối đa (**High Uptime**).
* Đây là **yếu tố quan trọng nhất** trong dự án di chuyển lần này; cần tối đa hóa khả năng phục hồi (*Resilience*) và chịu lỗi (*Fault Tolerance*) trên toàn bộ giải pháp.

---

## 3. Bảng tổng hợp tiêu chí & Định hướng giải pháp

| Hạng mục | Yêu cầu của khách hàng | Định hướng giải pháp AWS sơ bộ |
| :--- | :--- | :--- |
| **Mô hình triển khai** | Hybrid Cloud (50% On-Premise, 50% AWS) trong vài năm. | Kiến trúc kết nối Hybrid VPC + On-Premises. |
| **Kết nối mạng** | Băng thông cao, độ trễ thấp, thông lượng ổn định, bảo mật. | **AWS Direct Connect** (hoặc kết hợp VPN dự phòng). |
| **Ứng dụng & Điều phối** | Ứng dụng chạy Container nội bộ (Private), dùng chung bộ công cụ điều phối. | **Amazon ECS Anywhere** hoặc **Amazon EKS Anywhere** / ECS Private Tasks trong VPC. |
| **Lưu trữ tệp dùng chung** | Ứng dụng on-premise tạo file, cloud truy cập; lưu trữ trên AWS. | **Amazon EFS / AWS Storage Gateway (File Gateway)** hoặc **Amazon S3**. |
| **Cơ sở dữ liệu** | PostgreSQL, giữ nguyên mã nguồn, tính sẵn sàng cao. | **Amazon RDS for PostgreSQL (Multi-AZ)** hoặc **Amazon Aurora PostgreSQL**. |
| **Độ tin cậy (Resilience)** | Uptime tối đa, chịu lỗi cao (Fault Tolerance). | Triển khai Multi-AZ, tự động failover, hạ tầng dự phòng. |
