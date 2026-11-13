# Module 2: Identity and Access Management (IAM) & Access Architecture

> **Source**: Course *Cybersecurity Architecture* - Video: *Who Are You? Identity and Access Management Really Wants to Know* (Duration: ~31 mins)

---

## 1. Tổng quan & Triết lý cốt lõi

* **Identity is the new perimeter**: Trong bối cảnh hiện đại (Cloud, làm việc từ xa, phân tán), tường lửa và ranh giới mạng truyền thống không còn đủ. Căn tính người dùng (Identity) trở thành ranh giới phòng thủ tuyến đầu.
* **Mô hình 4 chữ A (The 4 As of IAM)**:
  1. **Administration (Quản trị)**: Xác định và khởi tạo quyền truy cập (Access Rights), vòng đời tài khoản (Provisioning / De-provisioning).
  2. **Authentication (Xác thực)**: Trả lời câu hỏi **"Who are you?"** (Bạn là ai?).
  3. **Authorization (Ủy quyền/Phân quyền)**: Trả lời câu hỏi **"What are you allowed to do?"** (Bạn được phép làm những gì?).
  4. **Audit (Kiểm toán)**: Đánh giá, giám sát và kiểm tra xem 3 chữ A trước đó có được thực thi chính xác và tuân thủ hay không.

---

## 2. Lớp nền tảng: Lưu trữ & Đồng bộ (Store & Sync)

### 2.1. Nhóm người dùng (User Groups) & Nhu cầu truy cập
* Phân loại điển hình:
  * **Employees (Nhân viên)**: Admin, Sales, Manufacturing...
  * **Suppliers / Partners (Đối tác & Nhà cung cấp)**.
  * **Customers (Khách hàng)**: Retail, Commercial.
* Mỗi nhóm cần danh tính trên nhiều hệ thống (HR, Email, CRM, Finance...).

### 2.2. Directory (Thư mục lưu trữ danh tính)
* **Khái niệm**: Bất kỳ nơi nào lưu trữ thông tin danh tính (tên, tài khoản, phòng ban, phòng ban chức năng...).
* **3 Thành phần cơ bản của Directory**:
  1. **Database**: Kho dữ liệu lưu trữ các tài khoản.
  2. **Schema**: Quy chuẩn tổ chức, cấu trúc dữ liệu người dùng.
  3. **Protocol**: Giao thức truy vấn/trao đổi dữ liệu (chuẩn công nghiệp phổ biến nhất là **LDAP** - *Lightweight Directory Access Protocol*; Microsoft triển khai dưới dạng **Active Directory**).

### 2.3. Vấn đề thực tế & Đồng bộ (Synchronization)
* Trong thực tế, doanh nghiệp luôn có **nhiều directories riêng biệt** (do các ứng dụng yêu cầu kho lưu trữ chuyên biệt).
* **Giải pháp đồng bộ**:
  * **Virtual Directory**: Đóng vai trò như một bộ chỉ mục (index/pointer). Khi có yêu cầu, nó tìm và truy xuất dữ liệu từ các directory tương ứng (có thể áp dụng cache).
  * **Meta Directory**: Thu thập trước (pre-fetch) và sao chép các thuộc tính dữ liệu cần thiết từ các directory cấp dưới gom vào một Enterprise Directory tập trung.

---

## 3. Administration: Quản lý Danh tính & Phân quyền (Provisioning & Roles)

### 3.1. RBAC (Role-Based Access Control)
* Ánh xạ giữa **Business Role** (Vị trí công việc: Giao dịch viên ngân hàng, Quản lý chi nhánh...) sang **IT Role** (Tập hợp các tài khoản & quyền truy cập hệ thống cần thiết).
* Tỷ lệ lý tưởng trong thực tế: Khoảng **80%** quyền được cấp tự động thông qua Role mapping, **20%** còn lại xử lý dưới dạng cấp phát ngoại lệ (one-off / ad-hoc requests).

### 3.2. Ba kịch bản vòng đời (Use Cases)
1. **New Hire (Tuyển mới - Provisioning tự động)**:
   * HR System $\rightarrow$ Identity Governance $\rightarrow$ Role Management $\rightarrow$ Approval Workflow (tự động hoặc duyệt cơ bản) $\rightarrow$ Connector ghi vào Directory $\rightarrow$ Cấp phát tài khoản hoàn tất.
2. **Additional Access Request (Yêu cầu thêm quyền)**:
   * Nhân viên gửi yêu cầu qua Self-service Portal/GUI $\rightarrow$ Đi qua quy trình phê duyệt (Approval Workflow đa cấp/song song) $\rightarrow$ Connector kích hoạt quyền trên hệ thống mục tiêu.
3. **Offboarding / Termination (Nghỉ việc - De-provisioning)**:
   * **Điểm rủi ro an ninh cao nhất!**
   * Nếu không có hệ thống tập trung (Single Source of Truth), quản trị viên phải đi xóa thủ công trên từng hệ thống.
   * Với IAM tập trung: HR đánh dấu nghỉ việc $\rightarrow$ Identity Governance tự động thu hồi/xóa tất cả tài khoản đã liên kết mà không cần chờ phê duyệt.

---

## 4. Authentication (Xác thực): "Who Are You?"

### 4.1. 3 Yếu tố xác thực truyền thống (Authentication Factors)
1. **Something you know (Điều bạn biết)**: Password, PIN. *Nhược điểm: Dễ bị rò rỉ, chia sẻ hoặc quên.*
2. **Something you have (Điều bạn sở hữu)**: Thiết bị di động (OTP SMS, Push notification qua App authenticator), Token phần cứng.
3. **Something you are (Đặc điểm sinh trắc học)**: Vân tay, khuôn mặt (FaceID). *Lưu ý: Voice print ngày nay dễ bị tấn công bởi AI Deepfake.*

### 4.2. MFA & Xu hướng Passwordless
* **MFA (Multi-Factor Authentication)**: Kết hợp từ 2 yếu tố khác nhau trở lên (ví dụ: Điện thoại + FaceID).
* **Passwordless Authentication**: Xu hướng tương lai loại bỏ hoàn toàn mật khẩu kiến thức, giảm chi phí hỗ trợ helpdesk (quên mật khẩu) và ngăn ngừa đánh cắp mật khẩu từ xa.

### 4.3. Single Sign-On (SSO)
* **Vấn đề**: Người dùng phải nhớ hàng chục mật khẩu phức tạp riêng lẻ $\rightarrow$ họ có xu hướng đặt chung 1 mật khẩu đơn giản ở mọi nơi.
* **Cơ chế SSO**: Người dùng xác thực 1 lần duy nhất qua hệ thống SSO (được bảo vệ nghiêm ngặt bằng MFA) $\rightarrow$ SSO tự động chuyển tiếp/cung cấp thông tin xác thực đến các ứng dụng đích.
* **Lợi ích**: Tăng trải nghiệm người dùng đồng thời tăng cường an ninh tổng thể.

---

## 5. Authorization (Ủy quyền): "What Are You Allowed To Do?"

* Không chỉ là quyết định nhị phân tĩnh (cho phép / từ chối).
* **Risk-based Authorization / Adaptive Access (Ủy quyền thích ứng dựa trên rủi ro)**:
  * **Location (Vị trí)**: Cho phép truy cập từ mạng công ty; chặn hoặc yêu cầu bước xác thực nâng cao nếu đến từ vị trí địa lý bất thường.
  * **Request Type (Loại tác vụ)**: Xem số dư (rủi ro thấp); Chuyển tiền (rủi ro cao $\rightarrow$ yêu cầu xác nhận thêm).
  * **Amount (Giá trị giao dịch)**: Chuyển dưới \$1,000 thực hiện ngay; trên mức đó kích hoạt kiểm soát bổ sung.
  * **Frequency (Tần suất)**: Tần suất giao dịch đột biến so với hành vi chuẩn sẽ kích hoạt cảnh báo/chặn.

---

## 6. Privileged Access Management (PAM / PIM)

### 6.1. Rủi ro thực tế với tài khoản đặc quyền
* Các tài khoản tối cao (Root, System Admin, DBA, Network Admin) nắm giữ "chìa khóa vương quốc".
* **Thực trạng xấu**: Dùng chung tài khoản Root/Admin với cùng một mật khẩu trên hàng trăm/hàng nghìn máy chủ $\rightarrow$ Không thể biết ai thực hiện thao tác khi xảy ra sự cố, khó đổi mật khẩu khi có người nghỉ việc.

### 6.2. Cơ chế hoạt động chuẩn của PAM
* Người quản trị **không** kết nối trực tiếp đến server đích. Họ đăng nhập vào hệ thống PAM (bắt buộc qua MFA).
* **Check-out / Check-in Credential**:
  1. Admin xin cấp quyền vào Server A qua cổng PAM.
  2. PAM cấp quyền tạm thời hoặc dùng phần mềm trung gian tự điền mật khẩu.
  3. Sau khi hoàn thành phiên làm việc, Admin **Check-in** trả lại tài khoản.
  4. PAM **tự động xoay vòng (đổi mật khẩu mới)** trên server đó ngay lập tức.
* **Audit & Session Recording**: PAM ghi hình và lưu nhật ký toàn bộ keystroke (từng phím bấm) trong phiên để giám sát và phục vụ điều tra forensics.

---

## 7. Audit (Kiểm toán) & UEBA

* Kiểm toán xác nhận tính toàn vẹn của 3 chữ A trước đó thông qua phân tích Log tập trung.
* **UEBA (User and Entity Behavior Analytics)**:
  * Ứng dụng Machine Learning & Phân tích hành vi để phát hiện các bất thường (Anomalies).
  * *Ví dụ kịch bản tấn công*: Tạo một tài khoản mới $\rightarrow$ Lập tức dump toàn bộ database $\rightarrow$ Xóa ngay tài khoản đó trong vòng vài phút. Các hành động đơn lẻ có thể hợp lệ, nhưng chuỗi hành động diễn ra nhanh bất thường sẽ bị UEBA phát hiện và cảnh báo.

---

## 8. Mở rộng kiến trúc IAM

1. **Identity Federation (Liên kết danh tính)**:
   * Cho phép nhân viên dùng danh tính nội bộ (Identity Provider - IdP) để đăng nhập vào dịch vụ Cloud/SaaS hoặc hệ thống của đối tác (Service Provider - SP) dựa trên các chuẩn công nghiệp (SAML, OIDC/OAuth2).
2. **Workforce IAM vs CIAM (Consumer IAM)**:
   * **Workforce IAM**: Tập trung vào nhân viên nội bộ, yêu cầu kiểm soát chặt chẽ, quy trình phê duyệt nghiêm ngặt, tuân thủ chính sách doanh nghiệp.
   * **CIAM**: Tập trung vào khách hàng, tối ưu trải nghiệm người dùng (frictionless/mượt mà), giảm tối đa rào cản đăng ký, chú trọng bảo vệ quyền riêng tư (Privacy) và khả năng mở rộng hàng triệu tài khoản.
