# AWS Logging Strategy: Application Logs vs. Infrastructure Logs & Centralized CloudTrail

> **Course:** AWS Cloud Solutions Architect Professional Certificate  
> **Course 2:** Architecting Solutions on AWS  
> **Module 4:** Designing a solution following account governance and management best practices  
> **Topic:** Choosing Services for Logging & Centralized CloudTrail Implementation  

---

## 1. Phân loại Logging trong AWS (Two Core Categories)

Logging trong AWS được chia làm hai mảng chính với mục đích và dịch vụ xử lý khác nhau:

| Tiêu chí | Application Logs (Log ứng dụng) | Infrastructure Logs (Log hạ tầng) |
| :--- | :--- | :--- |
| **Định nghĩa** | Dữ liệu phát sinh từ hoạt động của ứng dụng mã nguồn hoặc tầng dịch vụ phân phối nội dung. | Dữ liệu ghi nhận các sự kiện thay đổi hạ tầng, API calls, thay đổi trạng thái và an ninh mạng. |
| **Ví dụ dữ liệu** | • Web server access/error logs (HTTP 4xx, 5xx)<br>• Database query/slow logs<br>• Code exceptions, application traces | • IAM API calls (ai gọi, gọi khi nào, thay đổi gì)<br>• Cấu hình tài nguyên trước/sau khi đổi<br>• Lưu lượng mạng (Network IP flows)<br>• Cảnh báo xâm nhập, an ninh |
| **Mục đích chính** | Hỗ trợ phát hiện lỗi phần mềm, troubleshoot sự cố ứng dụng, giám sát hiệu năng (Performance & Error Monitoring). | Phục vụ kiểm toán tuân thủ (Audit), truy vết điều tra (Forensics), quản trị hạ tầng (Paper trail). |
| **Dịch vụ AWS nguồn** | AWS Lambda, API Gateway, Application Load Balancer (ALB), S3 Static Website, CloudFront. | AWS CloudTrail, AWS Config, VPC Flow Logs, Amazon GuardDuty. |
| **Nơi lưu trữ/xử lý** | Amazon S3, Amazon CloudWatch Logs. | Dedicated S3 Buckets, CloudWatch Logs, Security Hub. |

---

## 2. Đi sâu vào Application Logging với CloudWatch Logs & S3

* **Tích hợp linh hoạt:** Các dịch vụ như Lambda, API Gateway, ALB, CloudFront hỗ trợ đẩy log trực tiếp sang S3 bucket hoặc CloudWatch Logs log stream (có thể thuộc cùng account hoặc cross-account).
* **Khả năng phân tích & hành động (Centralized Querying & Alerting):**
  * Sử dụng **CloudWatch Logs Insights** để truy vấn tập trung theo cú pháp lọc (e.g. lọc lỗi `HTTP 404` từ cụm Web Server).
  * Chuyển đổi kết quả log filter thành **CloudWatch Metrics**.
  * Thiết lập **CloudWatch Alarms** cảnh báo khi ngưỡng lỗi tăng vọt.
  * Tích hợp **Machine Learning / Anomaly Detection** để phát hiện bất thường tự động.

---

## 3. Thực hành: Centralized Infrastructure Logging với AWS CloudTrail

Video minh họa quy trình thu thập toàn bộ lịch sử API calls trong tổ chức về một S3 Bucket trung tâm tại **Shared Services Account**:

### 3.1. Các bước cấu hình Trail cấp Organization (Organization Trail)
1. Truy cập **AWS CloudTrail Console** tại tài khoản quản trị/Shared Services.
2. Tạo mới một Trail với tên: `centralized-logging`.
3. **Tuỳ chọn quan trọng:** Bật tích chọn **"Enable for all accounts in my organization"**.
   * Khi bật cờ này, CloudTrail tự động áp dụng và ghi log cho mọi tài khoản thành viên hiện có cũng như **bất kỳ tài khoản nào được tạo mới trong tương lai**.
4. Chọn tạo một S3 Bucket mới làm đích đến (`AWS CloudTrail Logs-<random-hash>`).
5. Chọn loại Event cần ghi: **Management Events** (ghi nhận các thao tác quản trị trên AWS resources: tạo EC2, đổi S3 bucket, tạo SQS...).

### 3.2. Cấu trúc lưu trữ log trên S3 Bucket (Directory Structure)
Logs được lưu trữ dưới dạng nén `.json.gz` theo cấu trúc phân tầng tự động:
```text
s3://<bucket-name>/AWSLogs/<Organization-ID>/<Account-ID>/CloudTrail/<Region>/<YYYY>/<MM>/<DD>/<LogFile>.json.gz
```
* **Phân tách theo Account ID:** Dù thao tác được thực hiện ở Dev Workload Account (`Account 4718`) qua IAM Identity Center (Single Sign-On), file log vẫn lập tức được gom về bucket tại Shared Services Account (`Account 3061`).

---

## 4. Best Practices về Bảo mật & Quản trị

1. **Bảo vệ toàn vẹn Log bằng SCPs (Preventive Guardrails):**
   * Áp dụng Service Control Policy (SCP) tại cấp **Root** của AWS Organizations.
   * Cấu hình **Explicit Deny** cho các API:
     * Chặn xoá hoặc tắt Trail (`cloudtrail:DeleteTrail`, `cloudtrail:StopLogging`, `cloudtrail:UpdateTrail`).
     * Chặn xoá S3 bucket hoặc các object log (`s3:DeleteBucket`, `s3:DeleteObject`).
   * Điều này đảm bảo kể cả root user hoặc admin tại các account con cũng không thể can thiệp hay xoá dấu vết (anti-tampering).
2. **Mã hoá (Encryption):** Trong môi trường Production, luôn bật **AWS KMS (SSE-KMS)** với Customer Managed Key (CMK) được quản lý tập trung và thiết lập Key Policy cho phép CloudTrail ghi log an toàn.
3. **Mở rộng hướng tới Account Factory:**
   * Tự động hóa việc gắn trail, CloudWatch log streams và baseline stacks khi tài khoản mới ra đời thông qua **Account Factory** (Control Tower / AFT).
