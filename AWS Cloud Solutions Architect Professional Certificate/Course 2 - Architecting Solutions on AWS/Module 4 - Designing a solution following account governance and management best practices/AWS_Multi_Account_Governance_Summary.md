# AWS Multi-Account Architecture & Governance: Architectural Decisions & Best Practices

> **Course:** AWS Cloud Solutions Architect Professional Certificate  
> **Course 2:** Architecting Solutions on AWS  
> **Module 4:** Designing a solution following account governance and management best practices  
> **Topic:** Reflecting on AWS Multi-Account Architecture Decisions  

---

## 1. Executive Summary & Core Objectives

Khi tổ chức phát triển quy mô trên AWS, việc chuyển đổi từ kiến trúc đơn tài khoản (**Single Account**) sang đa tài khoản (**Multi-Account Architecture**) là yêu cầu tất yếu để đảm bảo:
* **Thu hẹp Blast Radius** (vùng ảnh hưởng khi có sự cố bảo mật hoặc cấu hình sai).
* **Quản trị chi phí minh bạch** (Cost Allocation & Chargeback).
* **Tránh cạn kiệt AWS Service Quotas/Limits**.
* **Đáp ứng các tiêu chuẩn tuân thủ khắt khe** (PCI-DSS, HIPAA, SOC 2) mà không làm suy giảm tốc độ phát triển (Agility).

Tài liệu này tổng hợp toàn bộ bài học đối thoại kiến trúc qua 5 khía cạnh cốt lõi:
1. Lợi ích của kiến trúc Multi-Account.
2. Quản trị bằng AWS Organizations & Service Control Policies (SCPs).
3. Thiết kế phân tách tài khoản & IAM cho bài toán Fintech (PCI-DSS).
4. Khả năng mở rộng quy mô (Scale to 50+ Developers).
5. Giám sát tập trung (Centralized Observability) & Đối chiếu AWS Well-Architected Framework.

---

## 2. Chi tiết các trụ cột kiến trúc

### 2.1. Multi-Account vs Single-Account: Lợi ích chiến lược
* **Security & Blast Radius:** Mỗi AWS Account là một ranh giới bảo mật cứng (*hard security boundary*). Sự cố rò rỉ ở môi trường Dev không thể lan sang Production.
* **Cost Tracking:** Đơn giản hóa việc bóc tách chi phí bằng AWS Cost Explorer, Cost & Usage Report (CUR) theo từng BU/Project/Environment.
* **Service Quotas:** Phân bổ tải tránh bị chạm ngưỡng Rate Limit / Quota toàn cục của AWS APIs.
* **Governance:** Cho phép áp dụng các bộ chính sách (*guardrails*) khác nhau cho từng nhóm tài khoản mà không xung đột.

---

### 2.2. AWS Organizations & Service Control Policies (SCPs)
* **Tổ chức OUs (Organizational Units):** Phân tầng tài khoản theo chức năng (`Security`, `SharedServices/Core`, `Workloads/Prod`, `Workloads/Non-Prod`).
* **Bản chất của SCPs:**
  * SCPs là **hàng rào bảo vệ tối đa (Maximum Permission Boundary)**.
  * **SCPs không cấp quyền** mà chỉ lọc/chặn hành động (`Deny` luôn ưu tiên).
  * SCPs áp dụng lên mọi IAM entity trong member accounts, **kể cả Root user**.
* **Chiến lược áp dụng:**
  * *Baseline Guardrails (Root/Top OU):* Chặn sử dụng các AWS Region ngoài danh mục cho phép, cấm vô hiệu hoá CloudTrail/GuardDuty, chặn xoá AWS Config.
  * *Environment-Specific Guardrails (Workload OUs):* Cấm xoá Production RDS/S3 ở OU `Prod`, trong khi giữ OU `Non-Prod` linh hoạt để thử nghiệm.

---

### 2.3. Case Study: Fintech Startup & Tuân thủ chuẩn PCI-DSS

#### Chiến lược phân tách tài khoản:
1. **Dedicated CDE Account (Cardholder Data Environment):** Đặt trong OU riêng biệt chịu kiểm soát nghiêm ngặt nhằm thu hẹp tối đa phạm vi audit PCI-DSS (*minimize audit scope*).
2. **Dedicated Non-Prod / Dev Accounts:** Hoàn toàn không chứa dữ liệu thẻ thực tế (No Real Cardholder Data - CHD). Đội ngũ phát triển làm việc trên dữ liệu mock/tokenized để giữ tính linh hoạt (*Developer Agility*).
3. **Network Boundary:** Không thiết lập direct VPC Peering giữa Dev và Prod CDE; giao tiếp dịch vụ thông qua **AWS PrivateLink** hoặc **API Gateway** với xác thực mTLS và mã hóa KMS.

#### Cấu hình IAM Role & Least Privilege:
* **Staging Account (`StagingDeployerRole`):**
  * *Trust Policy:* Tin cậy định danh của Developer từ Identity account qua `sts:AssumeRole`.
  * *Permissions Policy:* Cho phép deploy tài nguyên ứng dụng (ECS, Lambda, S3) trên phạm vi staging.
* **Production PCI Account (`ProdDeployerRole`):**
  * *Trust Policy:* **Tuyệt đối không tin cậy Developer trực tiếp**. Chỉ tin cậy pipeline CI/CD tự động (thông qua OIDC hoặc Role chuyên dụng ở Central CI/CD Account).
  * Quy trình lên Prod bắt buộc có **Approval Gates** (phê duyệt trước khi release).
* **Kỹ thuật thực thi Least Privilege:**
  * Giới hạn `Resource: arn:aws:...` cụ thể, không dùng wildcard `*`.
  * Gán **Permission Boundaries** ngăn chặn dev tự leo thang đặc quyền (*privilege escalation*).
  * Điều kiện kiểm tra (`Condition`): `aws:MultiFactorAuthPresent: "true"`, giới hạn thời gian phiên (`DurationSeconds: 3600`), hạn chế dải IP.
  * Tách biệt quyền deploy app khỏi các quyền nhạy cảm (`iam:*`, `kms:*`).

---

### 2.4. Mở rộng quy mô (Scaling to 50+ Developers)
Để tránh gánh nặng quản trị (*administrative burden*) khi đội ngũ tăng nhanh:
1. **Centralized Identity Federation:**
   * Tích hợp **AWS IAM Identity Center** (trước đây là AWS SSO) với IdP doanh nghiệp (Okta, Google Workspace, Entra ID) qua chuẩn SAML 2.0 và SCIM.
   * Quản lý phân quyền dựa trên Nhóm (**Group-Based Access Control** - RBAC), cho phép Onboarding/Offboarding chỉ bằng 1 thao tác trên IdP.
2. **Standardized Permission Sets:** Chuẩn hóa các bộ quyền (ví dụ: `StagingDeployer`, `ProdReadOnly`, `SecurityAuditor`) và map với Account/OU tương ứng.
3. **Automated Account Provisioning:**
   * Sử dụng **AWS Control Tower** hoặc **Account Factory for Terraform (AFT)** để tự động hoá việc tạo tài khoản mới bằng IaC.
   * Tài khoản mới tự động được gắn sẵn SCPs, baseline security, VPC tiêu chuẩn và IAM roles.
4. **Just-In-Time (JIT) & Break-Glass Access:** Cấm cấp quyền Admin vĩnh viễn ở Prod. Chỉ cấp quyền nâng cao tạm thời có giới hạn thời gian khi xử lý sự cố qua quy trình phê duyệt tự động (Slack/Jira workflow).

---

### 2.5. Centralized Observability & Cross-Account Monitoring
Thiết lập giám sát đa tài khoản cho đội ngũ Monitoring mà **không cấp thừa quyền**:
* **Central Monitoring Account:** Thiết lập tài khoản giám sát trung tâm đóng vai trò là điểm nhìn duy nhất (*single pane of glass*).
* **CloudWatch Cross-Account Observability:**
  * Source Accounts (Dev, Staging, Prod PCI) chia sẻ metrics, logs, traces sang Monitoring Account.
  * Monitoring Team chỉ cần đăng nhập vào Monitoring Account là xem được toàn bộ dashboard, alarms, và X-Ray traces mà không cần assume role trực tiếp vào Prod PCI.
* **Central Log Aggregation & Data Protection:**
  * Đẩy CloudTrail, VPC Flow Logs, Application logs về S3 bucket tập trung tại `Log Archive Account` (bật S3 Object Lock và KMS).
  * Kích hoạt **CloudWatch Logs Data Protection** để tự động che/mã hoá (*data masking*) PII và dữ liệu thẻ trước khi log hiển thị cho đội monitoring.
* **Least Privilege:** Cấp quyền đọc thuần tuý (`CloudWatchReadOnlyAccess`, S3 Read-Only) tại Monitoring Account; **0 quyền truy cập console hoặc chỉnh sửa** ở các workload accounts.

---

## 3. Đối chiếu với AWS Well-Architected Framework

| Trụ cột (Pillar) | Ứng dụng trong thiết kế |
| :--- | :--- |
| **Security** | • **Strong Identity Foundation:** Tập trung hóa qua IAM Identity Center, dùng short-lived credentials (`sts:AssumeRole`), cấm static access keys.<br>• **Blast Radius Reduction:** Cách ly CDE (PCI DSS) khỏi Dev/Staging ở cấp độ tài khoản.<br>• **Preventive & Detective Guardrails:** Kết hợp SCPs (chặn từ gốc) với CloudTrail/GuardDuty tập trung (phát hiện vi phạm).<br>• **Data Protection:** Che dữ liệu nhạy cảm trên logs và kiểm soát truy cập qua private endpoints. |
| **Operational Excellence** | • **Operations as Code:** Tự động hoá quản lý tài khoản qua Control Tower/AFT và quản lý cấu hình bằng IaC.<br>• **Unified Observability:** CloudWatch Cross-Account Sharing giúp giảm MTTR (Mean Time to Resolution) mà không cần switch account.<br>• **Agility with Governance:** Môi trường Dev/Staging linh hoạt, an toàn để thử nghiệm/thất bại nhanh mà không gây rủi ro cho Production. |

---

## 4. Key Takeaways & Cheatsheet

```text
[AWS Organizations]
  └── Root (Global Baseline SCPs: Deny unused regions, protect security services)
       ├── Core / Infrastructure OU
       │    ├── Central Identity Account (IAM Identity Center / IdP Integration)
       │    ├── Log Archive Account (Tamper-proof S3, Object Lock)
       │    ├── Central Monitoring Account (CloudWatch Cross-Account aggregator)
       │    └── Shared Services / CI/CD Account (Automated deployment pipelines)
       ├── Workloads OU
       │    ├── Dev / Staging Accounts (Direct developer assume-role allowed)
       │    └── Production Account (CI/CD automated deployment only)
       └── Compliance / PCI OU
            └── PCI CDE Account (Strict SCPs, no direct human access, automated OIDC deployments)
```
