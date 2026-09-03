# Automatic Account Provisioning & Governance Engine Deep Dive

> **Course:** AWS Cloud Solutions Architect Professional Certificate  
> **Course 2:** Architecting Solutions on AWS  
> **Module 4:** Designing a solution following account governance and management best practices  
> **Topic:** Automatic Account Provisioning: AWS CloudFormation, AWS Control Tower, and AWS Service Catalog  

---

## 1. Mối quan hệ và vai trò tổng thể của bộ ba dịch vụ

Để hiện thực hóa triết lý **"Automate as much as possible"** trong kiến trúc Multi-Account, 3 dịch vụ này phối hợp chặt chẽ theo mô hình phân tầng:

```text
[ AWS Control Tower ] (Orchestration & Account Governance Layer)
         │
         │  (Uses StackSets to deploy landing zones, guardrails, and baseline configs)
         ▼
[ AWS CloudFormation ] (Infrastructure as Code - IaC Engine)
         ▲
         │  (Uses CloudFormation templates to package approved IT products)
         │
[ AWS Service Catalog ] (End-user Self-Service & Resource Standardization Layer)
```

---

## 2. Chi tiết từng dịch vụ cốt lõi

### 2.1. AWS CloudFormation (Động cơ Infrastructure as Code - IaC)
* **Bản chất:** Dịch vụ IaC nền tảng giúp mô hình hóa và tự động cấp phát tài nguyên AWS bằng code (JSON hoặc YAML).
* **Cơ chế vận hành:**
  * Người dùng khai báo các tài nguyên (EC2, RDS, VPC, S3...) trong template.
  * CloudFormation tự động tính toán thứ tự phụ thuộc giữa các tài nguyên (*dependency mapping*) và thực hiện tạo/cấu hình.
* **Lợi ích kiến trúc:** Loại bỏ hoàn toàn thao tác cấu hình thủ công qua Console, đảm bảo tính lặp lại (*repeatability*), có thể kiểm soát phiên bản qua Git và tái sử dụng cho nhiều môi trường.
* **CloudFormation StackSets:** Mở rộng khả năng của CloudFormation cho phép deploy các stack instances đồng loạt trên **nhiều tài khoản (multiple accounts)** và **nhiều khu vực (multiple Regions)** từ một tài khoản quản trị duy nhất.

---

### 2.2. AWS Control Tower (Tầng điều phối & Quản trị Multi-Account)
* **Bản chất:** Dịch vụ điều phối (*orchestrator*) cấp cao nhất, tự động kết hợp các dịch vụ nền tảng (AWS Organizations, AWS Service Catalog, IAM Identity Center, CloudTrail, Config) để dựng một **Landing Zone** chuẩn mực trong vòng chưa đầy 1 giờ.
* **Cơ chế hoạt động:**
  * Sử dụng **CloudFormation StackSets** làm engine bên dưới để tự động đẩy cấu hình chuẩn đến từng account và từng Region.
  * **Controls / Guardrails:**
    * *Preventive controls:* Dùng SCPs để chặn các hành vi vi phạm (ví dụ: cấm tắt logging, cấm đổi region).
    * *Detective controls:* Dùng AWS Config rules để liên tục phát hiện các vi phạm cấu hình và báo cáo về dashboard tập trung.
  * **Chống Drift:** Giám sát liên tục để đảm bảo các tài khoản không bị lệch chuẩn (drift) so với các baseline ban đầu của doanh nghiệp.

---

### 2.3. AWS Service Catalog (Cổng tự phục vụ & Chuẩn hóa tài nguyên IT)
* **Bản chất:** Cho phép tổ chức tạo danh mục các dịch vụ/sản phẩm CNTT đã được phê duyệt an toàn (từ máy ảo, phần mềm, cơ sở dữ liệu đến toàn bộ kiến trúc ứng dụng multi-tier).
* **4 Lợi ích chiến lược:**
  1. **Standardization (Chuẩn hóa):** Quản trị viên kiểm soát chặt chẽ nơi sản phẩm được deploy, loại instance được dùng, cấu hình mạng và gắn thẻ (tagging).
  2. **Self-service discovery and launch (Tự phục vụ an toàn):** Lập trình viên tự do tìm kiếm và khởi chạy sản phẩm họ cần trong vài phút mà không cần tạo ticket nhờ đội hạ tầng hỗ trợ.
  3. **Fine-grained access control (Kiểm soát truy cập chi tiết):**
     * Admin gom sản phẩm thành các **Portfolios**.
     * Gán quyền truy cập Portfolio cho các nhóm IAM hoặc IAM Identity Center users/groups.
     * Sử dụng **Launch Constraints** (gán IAM Role riêng cho Service Catalog thực thi) giúp end-user tạo được tài nguyên mà tài khoản của chính họ không cần cấp quyền quản trị rộng.
  4. **Extensibility and version control (Mở rộng & Quản lý phiên bản):** Khi cập nhật template sản phẩm lên phiên bản mới, bản cập nhật sẽ tự động lan truyền đến mọi portfolio đang tham chiếu sản phẩm đó.

---

## 3. Bảng so sánh tổng hợp vai trò kiến trúc

| Tiêu chí | AWS CloudFormation | AWS Service Catalog | AWS Control Tower |
| :--- | :--- | :--- | :--- |
| **Phạm vi (Scope)** | Resource & Stack level (hạ tầng kỹ thuật chi tiết). | Portfolio & Product level (dịch vụ IT cho end-user). | Organization & Account level (toàn bộ hệ sinh thái multi-account). |
| **Bản chất vai trò** | Engine IaC gốc để sinh tài nguyên. | Cổng tự phục vụ (Self-service store) cung cấp hạ tầng đã duyệt. | Nhạc trưởng điều phối (Orchestrator) thiết lập Landing Zone và Guardrails. |
| **Đối tượng sử dụng** | DevOps / Cloud Engineers viết code hạ tầng. | Developers / Data Analysts / Testers tự tạo môi trường làm việc. | Enterprise Cloud Architects / Security Administrators. |
| **Cơ chế bên dưới** | CloudFormation Stacks & StackSets. | Dựa trên CloudFormation templates. | Sử dụng CloudFormation StackSets, SCPs, AWS Config. |
