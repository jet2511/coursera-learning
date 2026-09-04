# AWS Automated Account Provisioning & Environment Standardization: Service Catalog vs. Control Tower

> **Course:** AWS Cloud Solutions Architect Professional Certificate  
> **Course 2:** Architecting Solutions on AWS  
> **Module 4:** Designing a solution following account governance and management best practices  
> **Topic:** Automating Account Provisioning and Maintenance (AWS Service Catalog & AWS Control Tower)  

---

## 1. Bài toán thực tế (The Business Problem)

* **Tình huống:** Một lập trình viên mới (Maria) gia nhập đội ngũ. Maria cần một môi trường phát triển (Dev environment) chuẩn hóa trên đám mây (gồm AWS Cloud9 IDE, EC2, SQS, API Gateway, mock Lambda...) tương thích với môi trường Production mà không muốn mất nhiều ngày tự cấu hình thủ công trên máy tính cá nhân.
* **Yêu cầu:** 
  1. Tự động hóa việc tạo và cấu hình tài nguyên cho lập trình viên.
  2. Đảm bảo tài nguyên tuân thủ quy chuẩn bảo mật (instance type hợp lệ, tagging bắt buộc, logging định tuyến về trung tâm).
  3. Khi một tài khoản AWS mới được tạo, toàn bộ nền tảng và danh mục dịch vụ phải sẵn sàng sử dụng ngay lập tức mà không bị **Account Drift** (sự phân kỳ/lệch chuẩn cấu hình giữa các tài khoản).

---

## 2. So sánh cốt lõi: Service Catalog vs. Control Tower

Một phép ẩn dụ trực quan và chuẩn xác để phân biệt phạm vi hoạt động của hai dịch vụ:

```text
+-------------------------------------------------------------------------------+
|                 RESOURCE LEVEL vs. ACCOUNT LEVEL AUTOMATION                   |
+-----------------------------------+-------------------------------------------+
| AWS Service Catalog               | AWS Control Tower                         |
| ("Resource Vending Machine")      | ("Account Vending Machine")               |
+-----------------------------------+-------------------------------------------+
| • Phạm vi: Bên trong 1 tài khoản  | • Phạm vi: Toàn bộ AWS Organization       |
| • Quản lý tài nguyên, sản phẩm    | • Quản lý vòng đời tài khoản              |
| • Người dùng: Developer, End-user | • Người dùng: Cloud Architect, DevOps lead|
+-----------------------------------+-------------------------------------------+
```

---

## 3. Chi tiết dịch vụ

### 3.1. AWS Service Catalog (Resource Vending Machine)
* **Bản chất:** Cung cấp cổng tự phục vụ (*self-service portal*) cho phép người dùng triển khai các tài nguyên đã được đội ngũ Cloud/Security phê duyệt trước mà không cần cấp quyền truy cập AWS CloudFormation hay admin trực tiếp.
* **Cơ chế hoạt động:**
  1. **Products:** Đội ngũ quản trị viết template CloudFormation đóng gói một tập hợp tài nguyên hoàn chỉnh (ví dụ: product *"Dev Stack A"* gồm 1 t2.micro + SQS Queue + API Gateway trỏ tới mock Lambda).
  2. **Portfolios:** Gom các Products thành từng danh mục (portfolio) theo nhu cầu (ví dụ portfolio *"Dev Environments"*).
  3. **Launch Constraints:** Thiết lập IAM role cấp quyền riêng cho Service Catalog thực thi CloudFormation, giúp người dùng launch được hạ tầng mà tài khoản cá nhân của họ không cần quyền tạo tài nguyên trực tiếp.
  4. **Standardization:** Tự động enforce kích thước máy chủ, quy chuẩn gắn thẻ (mandatory tags), cấu hình mạng an toàn.

### 3.2. AWS Control Tower (Account Vending Machine & Landing Zone)
* **Vấn đề đặt ra:** Tài khoản mới tạo qua AWS Organizations là một tài khoản trắng (*empty account*). Làm sao để Service Catalog và các baseline stacks xuất hiện tự động ngay khi tài khoản vừa sinh ra?
* **Giải pháp Control Tower:**
  * **Landing Zone:** Triển khai một môi trường đa tài khoản hoàn chỉnh, tự động kích hoạt CloudFormation StackSets mỗi khi tạo tài khoản mới.
  * **Account Factory:** Tự động tạo tài khoản mới theo mẫu chuẩn: tự gắn SCPs, cấu hình VPC, đẩy log về Shared Services, và **tự động deploy các Portfolio của AWS Service Catalog vào tài khoản con**.
  * **Chống Account Drift:** Đảm bảo mọi tài khoản dù mới hay cũ đều nhất quán về cấu hình bảo mật và công cụ làm việc.

---

## 4. Bức tranh kiến trúc tổng thể toàn diện (The Complete Multi-Account Stack)

Sự kết hợp hoàn chỉnh của bộ giải pháp quản trị AWS đã được tổng hợp trong sơ đồ kiến trúc:

```text
[AWS Organizations]
  └── Centralized Hierarchy, OUs, Account Boundaries
       │
[AWS Control Tower] (Quản trị tập trung tại Management/Shared Services)
  ├── Account Factory: Cấp phát tài khoản tự động & Chống Drift
  └── Guardrails / Landing Zone: Tự động chạy CloudFormation StackSets
       │
       ├──► [IAM Identity Center]: Single Sign-On (SSO) & phân quyền theo IdP Groups
       ├──► [SCPs]: Ranh giới quyền tối đa (Chặn tắt logging, chặn đổi vùng, chặn xóa tài nguyên Prod)
       ├──► [Centralized Logging]:
       │      ├── CloudTrail: Ghi nhận toàn bộ API calls gom về S3 trung tâm
       │      └── CloudWatch Logs: Gom app logs từ các tài khoản con về Shared Services Account
       │
       └──► [Member / Developer Accounts]:
              └── [AWS Service Catalog]:
                    └── Portfolios & Products (Dev Cloud9, mock APIs, standardized DBs)
                          └── Tích hợp sẵn Centralized CloudWatch Logging & Security Tags
```

---

## 5. Kết luận & Giá trị kiến trúc

1. **Self-Service with Guardrails:** Developer như Maria có thể tự tạo môi trường làm việc chỉ với vài cú click trên Service Catalog mà không sợ vi phạm chính sách bảo mật hay chi phí.
2. **Zero Manual Setup:** Không còn thao tác thủ công cấu hình máy ảo, phân quyền hay thiết lập đường truyền log mỗi khi tuyển thêm kỹ sư.
3. **Enterprise Compliance:** Mọi tài nguyên sinh ra đều tự động tích hợp sẵn centralised logging (CloudWatch/CloudTrail) và tuân thủ các quy tắc bảo mật của tổ chức.
