# AWS Infrastructure Logging & Security Services Deep Dive

> **Course:** AWS Cloud Solutions Architect Professional Certificate  
> **Course 2:** Architecting Solutions on AWS  
> **Module 4:** Designing a solution following account governance and management best practices  
> **Topic:** Infrastructure Logging Services (CloudTrail, Config, VPC Flow Logs, GuardDuty)  

---

## 1. Tổng quan 4 dịch vụ Infrastructure Logging cốt lõi

Infrastructure logging cung cấp "dấu vết kiểm toán" (*paper trail*) về các hành vi thao tác, cấu hình tài nguyên, luồng mạng và các mối đe doạ an ninh. 4 dịch vụ chủ lực bao gồm:

```text
+-------------------------------------------------------------------------------+
|                        AWS INFRASTRUCTURE LOGGING                             |
+-----------------------------------+-------------------------------------------+
| AWS CloudTrail                    | "WHO did WHAT, WHERE, and WHEN?"          |
| (API Activity Audit)              | -> Nhật ký gọi API của người dùng & service|
+-----------------------------------+-------------------------------------------+
| AWS Config                        | "WHAT does it look like over time?"       |
| (Resource Configuration Tracking) | -> Bản kê tài nguyên, lịch sử đổi cấu hình|
+-----------------------------------+-------------------------------------------+
| VPC Flow Logs                     | "WHERE did network traffic go?"           |
| (Network IP Traffic)              | -> Nhật ký IP ra/vào các Network Interface|
+-----------------------------------+-------------------------------------------+
| Amazon GuardDuty                  | "IS THERE any malicious activity?"        |
| (Intelligent Threat Detection)    | -> Giám sát thông minh, phát hiện xâm nhập |
+-----------------------------------+-------------------------------------------+
```

---

## 2. Chi tiết từng dịch vụ

### 2.1. AWS CloudTrail (Theo dõi & Ghi vết API Call)
* **Chức năng:** Ghi lại các hoạt động và API calls phát sinh từ AWS Management Console, CLI, SDKs và internal AWS services.
* **Phạm vi KHÔNG ghi nhận:**
  * **Không** ghi lại các API call nội bộ của ứng dụng chạy trong EC2.
  * **Không** ghi lại các request người dùng gọi vào web app backend (ví dụ: HTTP requests người dùng gọi vào API server).
* **Đặc tính phân phối log:** Logs thường được chuyển giao về S3 trong khoảng thời gian trung bình ~15 phút (không cam kết cố định).
* **Organization Trail (Khuyến nghị kiến trúc):**
  * Tạo từ **Management Account** (hoặc Delegated Administrator).
  * Tự động áp dụng lên **tất cả member accounts** hiện có và tài khoản mới tạo.
  * Member accounts **chỉ thấy trail nhưng không thể sửa/xoá** và mặc định không có quyền truy cập file log trong S3 bucket đích.

---

### 2.2. AWS Config (Quản lý cấu hình & Đánh giá tuân thủ)
Khác biệt cốt lõi: **CloudTrail ghi nhận hành động gọi API**, còn **Config ghi nhận trạng thái của tài nguyên trước và sau hành động đó**.

* **Resource Inventory & Relationship Mapping:**
  * Lập danh mục (inventory) toàn bộ tài nguyên (EC2, EBS, Security Group, VPC, IAM role...).
  * Vẽ sơ đồ phụ thuộc/mối quan hệ giữa các tài nguyên (giúp đánh giá tác động trước khi sửa đổi).
* **Config Rules (Continuous Compliance):**
  * Định nghĩa các quy tắc chuẩn (ví dụ: cấm mở port 22 ra `0.0.0.0/0`, bắt buộc S3 bucket phải bật encryption).
  * Tự động đánh giá liên tục khi có tài nguyên tạo mới/thay đổi/xoá; đánh dấu `NON_COMPLIANT` và gửi thông báo nếu vi phạm.
* **Security & Forensic Analysis:**
  * Truy vết lịch sử chính xác: *"Vào ngày 01/01/2025, user John Doe có những quyền IAM nào?"* hoặc *"Tại thời điểm 10:00 hôm qua, Security Group có mở port TCP nhạy cảm nào không?"*.

---

### 2.3. VPC Flow Logs (Nhật ký lưu lượng mạng IP)
* **Chức năng:** Ghi lại metadata lưu lượng IP (Source IP, Destination IP, Port, Protocol, Action: `ACCEPT` hoặc `REJECT`) đi qua Elastic Network Interfaces (ENIs).
* **Điểm đến lưu trữ:** Amazon CloudWatch Logs hoặc Amazon S3.
* **Ứng dụng chính:**
  * Khắc phục sự cố Security Group / NACL bị cấu hình quá chặt (chặn nhầm traffic).
  * Giám sát các luồng traffic bất thường truy cập vào EC2 instances.
  * Phân tích hướng luồng mạng (inbound / outbound).
* **Đặc tính hiệu năng:** Dữ liệu được thu thập **nằm ngoài đường dẫn truyền tải mạng (out of network path)**, do đó **hoàn toàn không ảnh hưởng đến throughput hoặc độ trễ mạng (latency)**.

---

### 2.4. Amazon GuardDuty (Phát hiện mối đe dọa thông minh)
* **Chức năng:** Dịch vụ phát hiện đe dọa an ninh gần như liên tục (near-continuous threat detection) sử dụng **Machine Learning**, phân tích hành vi bất thường và các nguồn **Threat Intelligence feeds** (IP độc hại, tên miền tấn công).
* **Các nguồn dữ liệu đầu vào (Data Sources):**
  * CloudTrail Management Events & Data Events (S3).
  * VPC Flow Logs.
  * DNS Query Logs.
  * EKS Audit Logs & Runtime Activity.
  * Amazon EBS volume scan data.
* **Các mẫu đe doạ điển hình có thể phát hiện:**
  * EC2/Container bị chiếm quyền điều khiển để đào tiền ảo (Crypto mining) hoặc phát tán mã độc.
  * Leo thang đặc quyền (Privilege escalation), rò rỉ credential (Compromised AWS credentials).
  * Thao tác bất thường trên tài khoản: Triển khai instance ở Region chưa từng dùng, tự hạ thấp độ mạnh của Password Policy.

---

## 3. Bảng so sánh nhanh CloudTrail vs. AWS Config

| Tiêu chí | AWS CloudTrail | AWS Config |
| :--- | :--- | :--- |
| **Câu hỏi trả lời** | *Ai đã làm điều này? Khi nào? Từ IP nào?* | *Tài nguyên hiện đang cấu hình thế nào? Đã thay đổi ra sao so với trước? Có hợp chuẩn không?* |
| **Bản chất dữ liệu** | Lịch sử gọi API (API Call History / Event Stream). | Bản chụp trạng thái tài nguyên theo thời gian (Resource State & Change History). |
| **Focus chính** | Kiểm toán hành vi (Auditing & Accountability). | Quản trị tuân thủ (Compliance) & Quản lý cấu hình (Configuration Management). |
| **Hành động phản ứng** | Kích hoạt CloudWatch Alarms / EventBridge theo API. | Tự động cảnh báo `NON_COMPLIANT` hoặc Remediation tự sửa lại cấu hình. |
