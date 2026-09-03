# Taking Multi-Account Architecture to the Next Level: Advanced Governance & Security Patterns

> **Course:** AWS Cloud Solutions Architect Professional Certificate  
> **Course 2:** Architecting Solutions on AWS  
> **Module 4:** Designing a solution following account governance and management best practices  
> **Topic:** Week Wrap-Up: Taking this Architecture to the Next Level (Advanced SCPs, Tag Policies, Billing Alarms & IAM Security)  

---

## 1. Nâng cao năng lực Service Control Policies (Advanced SCP Patterns)

SCPs áp dụng ở cấp độ tài khoản/OU và có thể kiểm soát hành vi trên toàn bộ phạm vi tổ chức. 4 mẫu SCP nâng cao được Raf và Morgan khuyến nghị:

### 1.1. Chặn người dùng Root trên các Member Accounts (Restricting Root User)
* **Thực trạng rủi ro:** Khi tạo member account mới qua AWS Organizations, tài khoản đó vẫn tồn tại một Root User tiềm ẩn. Bất kỳ ai có email quản trị đều có thể bấm *"Forgot Password"* để chiếm quyền Root và thực hiện mọi hành động mà IAM thông thường không chặn được.
* **Giải pháp SCP:** Tạo policy áp dụng lên OU/Root cấm cụ thể Principal là Root User thực thi các AWS actions nhạy cảm hoặc cấm toàn bộ (`"Principal": {"AWS": "arn:aws:iam::*:root"}`).

### 1.2. Chống giả mạo & Tắt dịch vụ giám sát (Anti-Tampering for CloudTrail & S3)
* **Thực trạng rủi ro:** Lập trình viên hoặc hacker có quyền admin trong account con có thể dừng ghi log CloudTrail hoặc xoá S3 bucket lưu log để xoá dấu vết.
* **Giải pháp SCP:** Gắn SCP tại Root OU có mệnh đề **Explicit Deny** đối với các hành động:
  * Chặn chỉnh sửa/dừng CloudTrail (`cloudtrail:DeleteTrail`, `cloudtrail:StopLogging`, `cloudtrail:UpdateTrail`).
  * Chặn xoá S3 bucket hoặc objects chứa audit log.

### 1.3. Giới hạn IP truy cập Console qua Văn phòng hoặc Corporate VPN (IP-Based Restrictions)
* **Mục tiêu:** Tương tự như mạng On-Premises, chỉ cho phép quản trị viên/thành viên CCoE (Cloud Center of Excellence) đăng nhập vào AWS Console từ dải IP an toàn.
* **Giải pháp SCP:** Dùng khối **`Condition`** với toán tử `NotIpAddress` kết hợp `aws:SourceIp`:
  * Nếu request không xuất phát từ IP tĩnh của văn phòng hoặc VPN Gateway $\rightarrow$ **Deny** quyền truy cập Console.

### 1.4. Chống lách luật di chuyển Account giữa các OUs (Preventing OU Hopping)
* **Thực trạng lách luật:** Prod OU có SCP chặn tạo instance cỡ lớn hoặc cấm mở port mạng; Dev OU thì lỏng hơn. Một user có thể nghĩ ra cách: *"Chuyển tạm Prod Account sang Dev OU, tạo tài nguyên vi phạm xong rồi chuyển ngược lại"*.
* **Giải pháp SCP:** Áp dụng SCP chặn hành vi di chuyển tài khoản (`organizations:MoveAccount`, `organizations:CreateOrganizationalUnit`) ngoại trừ một nhóm admin tối cao được uỷ quyền.

---

## 2. Chuẩn hoá gắn thẻ bằng Tag Policies (Enforcing Uniform Tagging)

* **Vấn đề:** Các tài nguyên trong tổ chức không được gắn thẻ đồng nhất, gây khó khăn cho việc bóc tách chi phí, phân bổ ngân sách và tự động hoá vận hành.
* **Đặc tính của Tags:** Tags trong AWS có phân biệt chữ hoa/chữ thường (**Case-Sensitive**).
  * Ví dụ: Tag `CostCenter` khác hoàn toàn với `costCenter` hay `Costcenter`. Nếu gán sai, hệ thống thanh toán và báo cáo sẽ bị phân mảnh dữ liệu.
* **AWS Organizations Tag Policies:**
  * Cho phép định nghĩa quy chuẩn thẻ thống nhất (tên tag, kiểu chữ, danh sách giá trị hợp lệ).
  * Ngăn chặn người dùng tạo mới hoặc sửa đổi tài nguyên nếu tag không tuân thủ quy chuẩn đã đặt ra.

---

## 3. Quản lý chi phí chi tiết bằng Billing Alarms đa tài khoản

* **Giám sát tập trung từ Shared Services Account:**
  * Kích hoạt tính năng **Billing Alerts** trong Organization.
  * Amazon CloudWatch tại tài khoản trung tâm sẽ nhận được **Billing Metrics tách biệt theo từng Member Account ID**.
* **Cảnh báo tức thì (Individual Billing Alarms):**
  * Thiết lập ngưỡng cảnh báo riêng cho từng account (ví dụ: Dev Account không được vượt quá $500/tháng).
  * Giúp phát hiện ngay lập tức trường hợp lập trình viên quên tắt máy ảo thử nghiệm hoặc vô tình khởi chạy loại instance đắt tiền.

---

## 4. Tăng cường an ninh định danh với IAM Identity Center & MFA

* **Bắt buộc Multi-Factor Authentication (MFA):**
  * Truy cập qua Single Sign-On (SSO) vào các môi trường AWS bắt buộc phải bật xác thực 2 yếu tố (MFA).
  * Sử dụng các yếu tố xác thực mạnh: FIDO2 / WebAuthn security keys, Authenticator App (TOTP) tạo mã OTP.
  * Giảm thiểu 99% rủi ro đánh cắp tài khoản do lộ mật khẩu.

---

## 5. Bảng tổng hợp các kỹ thuật kiến trúc nâng cao

| Cơ chế kiểm soát | Dịch vụ sử dụng | Tác động & Giá trị bảo vệ |
| :--- | :--- | :--- |
| **Restricting Root User** | AWS Organizations (SCP) | Vô hiệu hóa quyền năng tuyệt đối của Root user trong các member accounts. |
| **Tamper-Proof Audit** | AWS Organizations (SCP) | Khóa chặt CloudTrail và S3 log buckets ở cấp độ tổ chức. |
| **Network Boundary Access** | SCP + `aws:SourceIp` Condition | Buộc truy cập Console phải đi qua mạng nội bộ công ty hoặc VPN. |
| **Anti-Drift / Anti-Hopping** | SCP (`organizations:MoveAccount`) | Chặn hành vi tự ý di chuyển tài khoản qua OUs khác để lách luật. |
| **Tagging Enforcement** | AWS Organizations Tag Policies | Đảm bảo thẻ phân bổ chi phí chuẩn xác, chống lỗi Case-Sensitive. |
| **Per-Account Cost Alarms** | Amazon CloudWatch (Billing Metrics) | Cảnh báo vượt ngân sách chi tiết cho từng account riêng lẻ. |
| **Multi-Factor Authentication** | AWS IAM Identity Center | Ngăn chặn truy cập trái phép vào toàn bộ hệ sinh thái multi-account. |
