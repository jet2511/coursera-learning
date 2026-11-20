# Assignment Overview: Infrastructure Inventory
**Module:** Module 3 - Enterprise Architecture and Cloud Setup  
**Dự án:** Retail Bank's Digital Core Transformation  
**Tác giả:** Parikshit Jain  

---

## 1. Giới thiệu tổng quan
Trong quá trình chuyển đổi số của Ngân hàng bán lẻ (**Retail Bank**), việc thiết lập và duy trì một **Bảng kiểm kê hạ tầng chi tiết (Infrastructure Inventory)** là yêu cầu bắt buộc nhằm:
- Nâng cao năng lực quản trị công nghệ thông tin (IT Governance).
- Kiểm soát và giảm thiểu rủi ro vận hành (Risk Management).
- Minh bạch hóa hiện trạng tài nguyên trên các môi trường Phát triển (**Development**), Kiểm thử (**Staging**), và Vận hành chính thức (**Production**).
- Sẵn sàng đáp ứng các đợt thanh tra, kiểm toán định kỳ của cơ quan quản lý nhà nước (Audit & Compliance Readiness).

---

## 2. Bốn nhiệm vụ cốt lõi (Core Tasks)

### Task 1: Lập danh mục phần cứng (Hardware Components)
- Xây dựng danh mục chi tiết các tài sản phần cứng (vật lý hoặc máy chủ ảo/bare-metal trên Cloud):
  - Máy chủ ứng dụng & cơ sở dữ liệu (Application & Database Servers).
  - Thiết bị cân bằng tải phần cứng/mạng (Hardware/Cloud Load Balancers).
  - Hệ thống lưu trữ dữ liệu (SAN/NAS/Cloud Storage Volumes).
- Ghi nhận đầy đủ các thuộc tính: Tên model, Nhà sản xuất (Manufacturer/Vendor), Môi trường triển khai (Dev/Staging/Prod), và Người/Đơn vị sở hữu chịu trách nhiệm (Asset Owner).

### Task 2: Lập danh mục phần mềm (Catalog Software Assets)
- Thống kê toàn diện các nền tảng và giải pháp phần mềm đang vận hành:
  - Hệ điều hành (Operating Systems: RHEL, Ubuntu LTS).
  - Hệ quản trị cơ sở dữ liệu (Databases: MySQL Cluster, Redis, PostgreSQL).
  - Tầng trung gian & Broker (Middleware: Apache Kafka, IBM MQ).
  - Bộ công cụ CI/CD & DevOps (DevOps Tools: Jenkins, Docker, Kubernetes/OpenShift, SonarQube).
- Ghi nhận chi tiết: Phiên bản đang chạy (Version/Patch level), Thông tin bản quyền/giấy phép (License status/type), Môi trường cài đặt, và Đội ngũ phụ trách bảo trì.

### Task 3: Lập bản đồ hạ tầng mạng (Map Network Infrastructure)
- Nhận diện các thiết bị mạng và cấu hình phân đoạn logic:
  - Tường lửa ứng dụng & mạng (Firewalls / WAF).
  - Cổng kết nối bảo mật (VPN Gateways / Direct Links).
  - Thiết bị định tuyến và chuyển mạch (Routers, Switches, Cloud VPC / Subnets).
  - Phân vùng mạng ảo (Virtual Network Segments: DMZ, Private App Subnet, Isolated DB Subnet).
- Làm rõ vai trò, phiên bản firmware/OS mạng và môi trường hoạt động của từng thành phần.

### Task 4: Phân loại theo môi trường và chuẩn tuân thủ (Environment & Compliance Segmentation)
- Tách bạch rõ ràng tài sản theo từng môi trường độc lập: **Development**, **Staging**, và **Production**.
- Bổ sung các thông tin quản trị nâng cao:
  - Phân định quyền sở hữu tài sản (Asset Ownership).
  - Tình trạng giấy phép sử dụng (License compliance).
  - Lịch sử cập nhật bản vá bảo mật (Patch History & Vulnerability status).
  - Mối quan hệ phụ thuộc giữa các tài sản (Dependencies & Shared Usage) phục vụ đánh giá tác động khi nâng cấp hoặc khắc phục sự cố.

---

## 3. Danh mục sản phẩm bàn giao (Deliverables Checklist)

- [ ] **1. Comprehensive Infrastructure Inventory:** Bảng tính hoặc tài liệu tổng hợp phân loại đầy đủ 3 nhóm tài sản: Phần cứng (Hardware), Phần mềm (Software), và Mạng (Network).
- [ ] **2. Environment-Segregated Asset Lists:** Danh sách tài sản được phân tách theo môi trường (Dev/Staging/Prod) kèm thông tin phân định sở hữu và tình trạng bản quyền.
- [ ] **3. Dependency & Shared Usage Documentation:** Tài liệu làm rõ sự phụ thuộc giữa các thành phần và các tài nguyên dùng chung phục vụ công tác quản trị và kiểm toán.
