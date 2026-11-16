# Module 2 Glossary: Access Management and Endpoint Security

> **Source**: Course *Cybersecurity Architecture* - Reading: *Glossary: Access Management and Endpoint Security*

---

## Bảng thuật ngữ chuyên ngành (Glossary)

| Thuật ngữ (Term) | Định nghĩa chi tiết (Definition) |
| :--- | :--- |
| **Access Control (Kiểm soát truy cập)** | Cơ chế xác định người dùng có thể hay không thể thực hiện các thao tác cụ thể bằng cách đối chiếu danh tính người dùng với Danh sách kiểm soát truy cập (**ACL - Access Control List**). Bao gồm quyền trên tập tin (file permissions), quyền ứng dụng (program permissions) và quyền dữ liệu (data permissions). |
| **Audit (Kiểm toán)** | Quá trình sử dụng các câu lệnh hệ thống và truy cập nhật ký (log, journal) để đánh giá hệ thống. Có thể tạo một hồ sơ (profile) đặc biệt cho kiểm toán viên an ninh sử dụng khi kiểm tra hệ thống. |
| **Authentication (Xác thực)** | Bất kỳ quy trình nào mà hệ thống sử dụng để **xác minh danh tính** của người dùng/thực thể đang muốn truy cập vào hệ thống (*"Bạn là ai?"*). |
| **Authorization (Ủy quyền / Phân quyền)** | Quy trình xác định xem một người dùng đã được xác thực có quyền thao tác trên một tài nguyên cụ thể trong miền bảo mật hay không (*"Bạn được phép làm gì?"*). |
| **Customer Identity and Access Management (CIAM)** | Giải pháp quản lý danh tính khách hàng, giúp tạo ra trải nghiệm mượt mà, liền mạch (seamless) và xây dựng niềm tin cho các ứng dụng hướng tới khách hàng bên ngoài. |
| **Endpoint (Điểm cuối)** | Thiết bị kết nối vào mạng máy tính (máy tính để bàn, laptop, smartphone, tablet, IoT...). Đây là các điểm vào (entry points) tiềm năng cho các cuộc tấn công mạng. **Lưu ý quan trọng**: Các thiết bị hạ tầng trung gian như **Routers, Switches, và Firewalls KHÔNG phải là endpoint** vì chúng không phải là điểm cuối của việc trao đổi dữ liệu. |
| **Federation (Liên kết danh tính)** | Mối quan hệ trong đó các thực thể tham gia đồng ý sử dụng cùng một tiêu chuẩn kỹ thuật chung để chia sẻ quyền truy cập tài nguyên. Gồm có: <br>• **IdP (Identity Provider)**: Đơn vị chịu trách nhiệm xác thực danh tính người dùng. <br>• **SP (Service Provider)**: Đơn vị hoặc chương trình cung cấp chức năng/dịch vụ nghiệp vụ. |
| **Identity and Access Management (IAM)** | Lĩnh vực an ninh mạng chuyên quản lý danh tính người dùng và phân quyền truy cập trên mạng máy tính. Mục tiêu tối thượng của IAM: Đảm bảo **đúng người dùng & đúng thiết bị** có thể truy cập **đúng tài nguyên**, vì **đúng lý do**, tại **đúng thời điểm**. |
| **Privileged Access Management (PAM)** | Giải pháp bảo vệ doanh nghiệp bằng cách giám sát, kiểm soát và bảo vệ các tài khoản có mức độ đặc quyền cao nhất (Root, Admin, DBA) khỏi các hoạt động độc hại và đảm bảo tuân thủ IT. |
| **Role-Based Access (RBAC - Truy cập dựa trên vai trò)** | Phương pháp giới hạn quyền truy cập hệ thống chỉ cho những người dùng được ủy quyền dựa trên vai trò công việc cụ thể của họ trong tổ chức. |
| **Single Sign-On (SSO - Đăng nhập một lần)** | Cơ chế xác thực cho phép người dùng chỉ cần đăng nhập một lần bằng một bộ thông tin xác thực duy nhất để truy cập an toàn vào nhiều ứng dụng và dịch vụ liên quan trong suốt phiên làm việc đó mà không phải đăng nhập lại. |
| **User and Entity Behavior Analytics (UEBA)** | Phần mềm an ninh sử dụng phân tích hành vi, thuật toán học máy (Machine Learning) và tự động hóa để phát hiện hành vi bất thường và nguy hiểm của người dùng lẫn thiết bị. Rất hiệu quả trong việc phát hiện **mối đe dọa nội bộ (Insider Threats)** mà các công cụ thông thường bỏ sót do chúng bắt chước lưu lượng truy cập hợp lệ. |
| **User Behavior Analytics (UBA)** | Hệ thống giám sát hoạt động của người dùng (lần đăng nhập, truy cập tệp tin, hành vi mạng...) và sử dụng thuật toán thống kê để phát hiện các mẫu hành vi đáng ngờ. |
