# Module 2 Summary & Highlights: Access Management and Endpoint Security

> **Source**: Course *Cybersecurity Architecture* - Reading: *Summary and Highlights: Access Management and Endpoint Security*

---

## 1. Bản chất của IAM & Mô hình 4 chữ A (The 4 A's of IAM)

* **IAM (Identity and Access Management)**: Trọng tâm là quản lý và bảo vệ an toàn cho danh tính người dùng/thực thể.
* **4 Chữ A cốt lõi**:
  1. **Administration (Quản trị)**: Quản lý danh tính, cấp phát quyền (**Provisioning**) và thu hồi quyền (**De-provisioning**). Thường được gọi là **Identity Management** hoặc **Identity Governance**.
  2. **Authentication (Xác thực)**: Thuộc phân hệ Access Management, trả lời câu hỏi **"Who are you?"** (Bạn là ai?). Các giải pháp tiêu biểu bao gồm **MFA (Multi-Factor Authentication)** và **SSO (Single Sign-On)**.
  3. **Authorization (Ủy quyền / Phân quyền)**: Thuộc phân hệ Access Management, trả lời câu hỏi **"What can you do?"** (Bạn được phép làm những gì?).
     * Triển khai qua **RBA (Risk-Based Authorization)** và **AA (Adaptive Access)** dựa trên các thông số ngữ cảnh: vị trí truy cập (Location), loại yêu cầu (Request Type), số tiền/giá trị (Request Amount), và tần suất thực hiện (Frequency).
     * **PAM (Privileged Access Management)**: Chuyên trách quản lý và bảo vệ các tài khoản có đặc quyền tối cao như Root, System Admin (sysadmin), Database Admin (DBA), và Network Admin.
  4. **Audit (Kiểm toán)**: Ghi và lưu trữ nhật ký (logs) về mọi hành vi và hoạt động xuyên suốt các hệ thống. Thường được thực hiện thông qua công nghệ phân tích hành vi người dùng/thực thể (**UBA / UEBA - User and Entity Behavior Analytics**).

---

## 2. Liên kết danh tính (Federation System)

* **Federation System**: Cho phép người dùng sử dụng danh tính tại tổ chức của mình để kết nối và truy cập vào các hệ thống thuộc các tổ chức/nhà cung cấp dịch vụ bên ngoài (như Cloud SaaS, đối tác kinh doanh) một cách chuẩn hóa và an toàn.

---

## 3. Quản lý An ninh Điểm cuối (Endpoint Security)

* **Endpoint (Điểm cuối)**: Bất kỳ thiết bị vật lý nào kết nối vào mạng doanh nghiệp (Servers, Laptops, Desktops, Smartphones, Tablets, IoT devices).
* **Endpoint Management System (Hệ thống quản lý điểm cuối tập trung)**:
  * Cho phép triển khai đồng bộ các chính sách (Policies), bản vá (Patches), thông tin và cảnh báo (Alerts) từ một giao diện quản trị duy nhất xuống toàn mạng lưới.
  * Thu thập dữ liệu trạng thái và nhật ký từ các hệ thống kết nối về trung tâm.

### 3.1. Các biện pháp kiểm soát trọng yếu (Key Controls)
1. **Inventory**: Nắm bắt và kiểm kê chi tiết mức độ phiên bản phần cứng và phần mềm.
2. **Security Policies**: Quy định các loại phần cứng và phần mềm nào được phép hoạt động trong tổ chức.
3. **Patching**: Cập nhật bản vá định kỳ và khẩn cấp.
4. **Encryption Policy**: Đảm bảo tính bảo mật (Confidentiality) và tính toàn vẹn (Integrity) của dữ liệu lưu trữ.
5. **Remote Wipe**: Xóa sạch toàn bộ dữ liệu thiết bị từ xa trong các trường hợp rủi ro (thất lạc, mất trộm, thôi việc).
6. **Location Tracking**: Định vị thiết bị khi cần tìm kiếm phần cứng doanh nghiệp.
7. **Anti-virus / EDR (Endpoint Detection and Response)**: Đảm bảo thiết bị không bị lây nhiễm mã độc.
8. **Disposal Policy**: Quy chuẩn tiêu hủy và làm sạch dữ liệu khi thanh lý thiết bị.

---

## 4. Chương trình an ninh BYOD chuẩn mực (Well-Defined BYOD Program)

Một chương trình BYOD (Bring Your Own Device) hoàn chỉnh bắt buộc phải có các chính sách rõ ràng về:
* **Consent (Sự đồng thuận)**: Thỏa thuận rõ ràng về việc giám sát và quyền hạn can thiệp trên thiết bị cá nhân.
* **Software**: Các ứng dụng bắt buộc phải cài đặt và danh sách các ứng dụng bị cấm.
* **Hardware**: Các tiêu chuẩn cấu hình phần cứng cá nhân được phép kết nối.
* **Services**: Danh sách các dịch vụ đám mây/chia sẻ dữ liệu được cấp phép sử dụng.
