# Customer #4: Solution Overview & Multi-Account Migration Roadmap

> **Course:** AWS Cloud Solutions Architect Professional Certificate  
> **Course 2:** Architecting Solutions on AWS  
> **Module 4:** Designing a solution following account governance and management best practices  
> **Topic:** Customer #4 Solution Overview: Architecture Blueprint & Phased Implementation Plan  

---

## 1. Bối cảnh & Hiện trạng của Khách hàng (Morgan)

* **Hiện trạng rủi ro cao:**
  * Toàn bộ hệ thống chạy dồn trên **một tài khoản AWS duy nhất (single massive AWS account)**.
  * Mọi người (kể cả quản trị viên và lập trình viên) thường xuyên đăng nhập bằng **Root user** của tài khoản.
  * Không có ranh giới bảo mật, không có cơ chế tự động cấp phát tài nguyên hay quản trị tài khoản chuẩn hóa, gây tâm lý bất an và rủi ro sập hệ thống bất kỳ lúc nào.
* **Mục tiêu của giải pháp:**
  * Chuyển đổi từ mô hình Single Account sang **Multi-Account Architecture**.
  * Chấm dứt hoàn toàn thói quen dùng Root account để đăng nhập.
  * Thiết lập giàn giáo kiến trúc (**Scaffolding**) vững chắc với các dịch vụ quản trị chuẩn mực của AWS.

---

## 2. Bản thiết kế giải pháp tổng thể (Architecture Blueprint)

Raf đề xuất xây dựng một tài khoản chuyên trách đóng vai trò lõi là **Shared Services Account** (hoặc Core Infrastructure Account) tích hợp toàn bộ các dịch vụ quản trị:

```text
+-----------------------------------------------------------------------------------+
|                           SHARED SERVICES / CORE ACCOUNT                          |
+-----------------------------------------------------------------------------------+
|  1. AWS Organizations       -> Tạo, tổ chức OUs và áp ranh giới bảo mật bằng SCPs  |
|  2. IAM Identity Center     -> Cung cấp Single Sign-On (SSO), xóa bỏ Root login   |
|  3. Centralized CloudTrail  -> Thu thập toàn bộ nhật ký API calls của mọi account |
|  4. AWS Control Tower       -> Điều phối tạo account & dựng Landing Zone tự động |
|  5. Central CloudWatch Logs -> Điểm tập trung log ứng dụng từ các account con      |
+-----------------------------------------------------------------------------------+
                                         │
                 ┌───────────────────────┴───────────────────────┐
                 ▼                                               ▼
    [ Workload Accounts (Dev/Test) ]               [ Production Account ]
    • Cài đặt AWS Service Catalog                  • Tách biệt blast radius
    • Cung cấp các Products/Portfolios chuẩn       • Chỉ cho phép CI/CD deploy
    • Tự động stream App Logs về CloudWatch        • Nghiêm cấm login trực tiếp
      của Shared Services Account
```

---

## 3. Kế hoạch triển khai thực tế (The 3-Phase Implementation Plan)

Kiến trúc trên đóng vai trò là "bộ khung giàn giáo" (**Scaffolding**). Để di chuyển khối lượng công việc khổng lồ từ single account sang multi-account một cách an toàn (không thể làm xong chỉ trong một buổi chiều), Raf vạch ra lộ trình 3 bước lớn:

```text
[ Bước 1: Foundation & IaC ] ──► [ Bước 2: Workload Migration ] ──► [ Bước 3: Database Migration ]
  (Dựng khung giàn giáo,           (Di chuyển App/Service,           (Di chuyển dữ liệu bằng DMS,
   viết CloudFormation Stacks)       thực hành triển khai qua IaC)     zero-downtime cutover)
```

### Bước 1: Dựng khung giàn giáo & Hạ tầng dạng mã (Foundation & IaC Scaffolding)
* Triển khai Control Tower, Organizations, SCPs, IAM Identity Center và cấu hình Centralized Logging trong Shared Services Account.
* Xây dựng các mẫu template **Infrastructure as Code (IaC)** chuẩn hóa (CloudFormation / Terraform) cho các ứng dụng và môi trường.

### Bước 2: Di chuyển ứng dụng & Nâng cao năng lực vận hành (Workload Migration)
* Triển khai các workload phi trạng thái (stateless workloads: API, Web Servers, container, worker) sang các tài khoản mới bằng IaC.
* Đây là giai đoạn để đội ngũ kỹ thuật thực hành (*experiment*), làm quen với quy trình quản trị đa tài khoản và CI/CD deployment, tích lũy độ trưởng thành (*maturity*) về vận hành cloud.

### Bước 3: Di chuyển cơ sở dữ liệu với Zero-Downtime (Database Migration)
* Sau khi đội ngũ đã làm chủ được kiến trúc mới, tiến hành di chuyển tầng dữ liệu (Stateful / Database).
* Sử dụng dịch vụ **AWS Database Migration Service (AWS DMS)**:
  * Cho phép đồng bộ dữ liệu liên tục (Continuous Data Replication - CDC) từ database ở single account cũ sang database ở account mới.
  * Giữ cho cơ sở dữ liệu luôn online trong suốt quá trình đồng bộ và chỉ cần một khoảng dừng bảo trì rất ngắn (minimal downtime window) để chuyển hướng traffic (cutover).

---

## 4. Giá trị then chốt mang lại cho khách hàng

1. **Xóa bỏ thói quen nguy hiểm (No More Root Login):** Thay thế việc dùng Root Account bằng IAM Identity Center (SSO), phân quyền hạt mịn theo nhóm và sử dụng temporary credentials.
2. **Loại bỏ tâm lý bất an (Peace of Mind):** Có một bản thiết kế rõ ràng và lộ trình từng bước khả thi giúp ban lãnh đạo tự tin kiểm soát lộ trình di chuyển.
3. **Nền tảng sẵn sàng cho tương lai:** Doanh nghiệp có thể tự tin scale thêm hàng chục tài khoản, dự án mới mà không sợ vỡ trận kiến trúc.
