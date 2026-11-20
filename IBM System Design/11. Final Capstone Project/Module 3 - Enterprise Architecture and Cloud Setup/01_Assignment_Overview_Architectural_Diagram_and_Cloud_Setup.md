# Assignment Overview: Architectural Diagram and Cloud Setup
**Module:** Module 3 - Enterprise Architecture and Cloud Setup  
**Dự án:** Retail Bank's Digital Core Transformation  
**Tác giả:** Parikshit Jain  

---

## 1. Giới thiệu tổng quan
Giai đoạn này tập trung vào việc thiết kế kiến trúc hạ tầng và ứng dụng dựa trên công nghệ Container (**Container-based Architecture**) nhằm phục vụ quá trình hiện đại hóa của Ngân hàng bán lẻ (**Retail Bank**). 
Mục tiêu là xây dựng sơ đồ topo triển khai (Deployment Topology Diagram), đóng gói các dịch vụ ngân hàng cốt lõi thành các container Docker độc lập, quản lý vòng đời container image trên Cloud Registry bảo mật (IBM Cloud Container Registry / AWS ECR), và thực thi các biện pháp an ninh bảo mật cấp ngân hàng.

---

## 2. Năm nhiệm vụ cốt lõi (Core Tasks)

### Task 1: Thiết kế kiến trúc triển khai dựa trên Container (Deployment Topology)
- Dựng sơ đồ kiến trúc trực quan thể hiện tính module hóa và phân tán của các microservices ngân hàng:
  - **Authentication Service:** Quản lý định danh, xác thực 2FA, OAuth2/JWT tokens.
  - **Customer Onboarding Service:** Xử lý hồ sơ đăng ký và luồng eKYC.
  - **Loan Servicing Service:** Tính toán điểm tín dụng, thẩm định và quản lý giải ngân.
- Làm rõ sự tương tác giữa các service qua API Gateway, cơ chế cân bằng tải (Ingress/Load Balancers), và topology triển khai trên cụm Kubernetes / Cloud Cluster.

### Task 2: Xây dựng Docker Containers cho Microservices
- Viết các file `Dockerfile` chuẩn sản xuất (production-ready) cho tối thiểu 3 microservices lõi (Authentication, Onboarding, Loan Servicing).
- Áp dụng kỹ thuật tối ưu kích thước image (Multi-stage builds, Distroless / Alpine base images), chạy dưới quyền người dùng không đặc quyền (non-root user).

### Task 3: Đẩy và quản lý Container Images trên Cloud Registry
- Thực hiện xác thực và đẩy (push) các container images đã gắn thẻ phiên bản (version tags) lên kho lưu trữ đám mây bảo mật (**IBM Cloud Container Registry** hoặc **AWS ECR**).
- Ghi nhận lại nhật ký dòng lệnh (CLI execution logs) làm bằng chứng kiểm chứng quy trình triển khai Cloud-Native.

### Task 4: Triển khai các biện pháp kiểm soát bảo mật Container (Security Controls)
- **Vulnerability Image Scanning:** Quét lỗ hổng bảo mật tự động trong container image trước khi triển khai (Trivy, Clair, IBM Vulnerability Advisor).
- **Role-Based Access Control (RBAC):** Giới hạn quyền truy cập kho ảnh registry và namespace cụm theo nguyên tắc đặc quyền tối thiểu (Least Privilege).
- **Image Signing & Verification:** Ký số ảnh container (Cosign / Notary) để đảm bảo tính toàn vẹn, chống can thiệp mã độc.

### Task 5: Thẩm định cấu hình Container (Configuration Validation)
- Xác minh tính độc lập và module hóa: Mỗi container chạy độc lập, tự phục hồi, chỉ mở (expose) các cổng mạng tối thiểu cần thiết.
- Rà soát các tiêu chuẩn tuân thủ (CIS Docker Benchmark, PCI-DSS compliance).
- Hoàn thành checklist thẩm định mức độ sẵn sàng triển khai thực tế.

---

## 3. Danh mục sản phẩm bàn giao (Deliverables Checklist)

- [ ] **1. Deployment Topology Diagram:** Sơ đồ topo triển khai kiến trúc microservices container (.png / .pptx).
- [ ] **2. Dockerfiles:** Bộ mã nguồn Dockerfile hoàn chỉnh cho ít nhất 3 dịch vụ cốt lõi (`auth-service`, `onboarding-service`, `loan-service`).
- [ ] **3. Cloud Registry Logs:** Bằng chứng dòng lệnh (CLI logs) chứng minh việc build, tag và push images thành công lên IBM Cloud Registry / AWS ECR.
- [ ] **4. Security Controls Report:** Báo cáo đặc tả các cơ chế bảo mật đã áp dụng (Image scanning, RBAC, Image signing, Non-root execution).
- [ ] **5. Container Readiness Validation Checklist:** Bảng đối soát xác nhận tính module hóa, an ninh và mức độ sẵn sàng tuân thủ quy chuẩn ngân hàng.
