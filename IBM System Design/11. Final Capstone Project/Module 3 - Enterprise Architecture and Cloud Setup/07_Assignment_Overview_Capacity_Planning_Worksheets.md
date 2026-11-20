# Assignment Overview: Capacity Planning Worksheets
**Module:** Module 3 - Enterprise Architecture and Cloud Setup  
**Dự án:** Retail Bank's Digital Core Transformation  
**Tác giả:** Parikshit Jain  

---

## 1. Giới thiệu tổng quan
Trong quá trình hiện đại hóa hệ thống ngân hàng số lõi (Digital Core), **Hoạch định năng lực hạ tầng (Capacity Planning)** là bước bắt buộc để đảm bảo hệ thống có khả năng co giãn linh hoạt (auto-scaling), đáp ứng khối lượng công việc vào giờ cao điểm (peak workloads) của các microservices, đồng thời tối ưu hóa chi phí và đảm bảo độ bền vững (resilience).

---

## 2. Bốn nhiệm vụ cốt lõi (Core Tasks)

### Task 1: Ước tính nhu cầu năng lực tính toán (Compute Requirements)
- Tính toán số lượng **vCPU** và dung lượng **RAM** cần thiết dựa trên số người dùng đồng thời (**concurrent users**) và cấu hình tài nguyên theo phiên (session resource profiles).
- Bổ sung hệ số an toàn/dự phòng (buffer/headroom) để đảm bảo tính chịu lỗi (resiliency/failover).
- Ánh xạ nhu cầu tính toán vào các loại máy chủ ảo thực tế trên Cloud (Cloud Instance Types: General Purpose, Compute Optimized, Memory Optimized).

### Task 2: Dự báo nhu cầu dung lượng lưu trữ (Storage Needs)
- Xác định dung lượng lưu trữ cho dữ liệu hoạt động (**Active Storage**) và dữ liệu lưu trữ dài hạn (**Archival Storage**).
- Tính toán dựa trên:
  - Kích thước trung bình mỗi giao dịch (Transaction size).
  - Chính sách lưu trữ dữ liệu theo quy định pháp lý (Data Retention Policies - ví dụ: 5-7 năm).
  - Chi phí phụ trội cho việc đánh chỉ mục và metadata (Indexing overhead ~20-30%).
- Đề xuất chiến lược lưu trữ phân tầng (**Tiered Storage Strategy**):
  - **Hot/Active Tier:** Ổ cứng tốc độ cao (NVMe/SSD) cho dữ liệu giao dịch trực tiếp.
  - **Cold/Archive Tier:** Lưu trữ đối tượng (Cloud Object Storage: S3/Cloud Object Storage) cho dữ liệu lịch sử/sao lưu.

### Task 3: Lập kế hoạch băng thông mạng (Network Bandwidth)
- Tính toán nhu cầu băng thông tại thời điểm cao điểm (**Peak Bandwidth Demands**) dựa trên thông lượng giao dịch (**Throughput / TPS**) và kích thước gói tin trung bình (**Payload size**).
- Dự trù chi phí phụ trội cho việc dự phòng mạng (Redundancy overheads / Cross-zone replication).
- Thiết lập các quy tắc tự động co giãn băng thông (Autoscaling rules/triggers) để đảm bảo dịch vụ không bao giờ bị nghẽn gián đoạn.

### Task 4: Thẩm định kế hoạch năng lực (Validate Capacity Plans)
- Sử dụng bảng kiểm tra (Checklist) để rà soát:
  - Khả năng chịu lỗi (Fault tolerance: N+1 hoặc Active-Active multi-zone).
  - Năng lực mở rộng (Scalability: Horizontal Pod Autoscaler).
  - Tối ưu hóa chi phí (Cost optimization: Reserved Instances / Savings Plans).
  - Đảm bảo phù hợp hoàn toàn với SLA vận hành của ngân hàng.

---

## 3. Danh mục sản phẩm bàn giao (Deliverables Checklist)

- [ ] **1. Compute Capacity Worksheet:** Bảng tính định cỡ vCPU/RAM cho các microservices theo tải cao điểm.
- [ ] **2. Storage Estimate Worksheet:** Bảng dự toán dung lượng lưu trữ Active (SSD) và Archive (Object Storage).
- [ ] **3. Network Bandwidth Worksheet:** Bảng tính băng thông mạng cao điểm kèm dự phòng và các ngưỡng kích hoạt co giãn (scaling triggers).
- [ ] **4. Capacity Planning Validation Checklist:** Bảng đối soát khẳng định tính vững chắc, khả năng chịu lỗi và tối ưu chi phí của hạ tầng.
