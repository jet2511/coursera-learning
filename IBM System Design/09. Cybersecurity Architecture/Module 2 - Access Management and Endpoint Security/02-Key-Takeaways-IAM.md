# Reading: Key Takeaways - Identity and Access Management (IAM)

> **Source**: Course *Cybersecurity Architecture* - Reading: *Key Takeaways: IAM*  
> **Author**: Dee Dee Collette (IBM)

---

## 1. Định nghĩa IAM
* **IAM (Identity and Access Management)**: Là dịch vụ/hệ thống giúp kiểm soát truy cập an toàn, chặt chẽ tới các tài nguyên của tổ chức.
* **Identity (Danh tính)**: Bất kỳ thông tin nào liên quan đến người dùng (tên, tài khoản, phòng ban, chức vụ...) đều được coi là danh tính.

---

## 2. Mô hình 4 chữ A cốt lõi (4As of IAM)

1. **Administration (Quản trị)**:
   * Xác định các quyền truy cập hiện tại và khởi tạo quyền mới.
   * Quản lý toàn bộ vòng đời tài khoản: Tạo mới (Create), Cập nhật (Update), và Xóa/Thu hồi (Delete).
2. **Authentication (Xác thực)**:
   * Xác định danh tính của người/đối tượng đang yêu cầu truy cập (*Ai đang truy cập?*).
3. **Authorization (Ủy quyền / Phân quyền)**:
   * Xác định những việc đối tượng **được phép làm** và **không được phép làm** (*Được làm gì trên tài nguyên?*).
4. **Audit (Kiểm toán)**:
   * Phân tích, rà soát 3 chữ A ở trên nhằm đảm bảo mọi chính sách và quy trình luôn được tuân thủ nghiêm ngặt.

---

## 3. Directory & Đồng bộ hóa (Synchronization)

* **Directory (Thư mục danh tính)**: Nơi lưu trữ toàn bộ thông tin danh tính của người dùng. Một Directory chuẩn bao gồm 3 thành phần:
  * **Database**: Cơ sở dữ liệu lưu trữ các tài khoản.
  * **Schema**: Cấu trúc, quy tắc định dạng dữ liệu danh tính.
  * **Protocol**: Giao thức giao tiếp (phổ biến nhất là **LDAP** - *Lightweight Directory Access Protocol*).

* **Phương pháp tiếp cận đồng bộ hóa (Synchronization Approaches)**:
  * **Virtual Directory**: Hoạt động như bộ chỉ mục theo thời gian thực; nhận yêu cầu từ người dùng và truy xuất thông tin từ các kho tương ứng khi có truy vấn.
  * **Meta Directory**: Thu thập trước (pre-fetch) dữ liệu từ nhiều nguồn khác nhau và gom lưu trữ tập trung vào một Enterprise Directory duy nhất.

---

## 4. Quản lý truy cập nâng cao & Mở rộng

* **Privilege Access Management (PAM)**: Giám sát, kiểm soát và ngăn chặn việc truy cập đặc quyền trái phép vào các tài nguyên trọng yếu (Critical Resources) của hệ thống.
* **Identity Federation (Liên kết danh tính)**: Cho phép người dùng đăng nhập vào hệ thống đóng vai trò là **Identity Provider (IdP)** và sử dụng danh tính đó để truy cập các hệ thống bên ngoài với tư cách **Service Provider (SP)**.
* **Workforce Identity Management**: Tập hợp các quy trình, công cụ và chiến lược dùng để quản lý danh tính của lực lượng lao động nội bộ (nhân viên, nhà thầu nội bộ).
* **Consumer Identity and Access Management (CIAM)**: Giải pháp tích hợp cả xác thực (Authentication) và ủy quyền (Authorization) vào các ứng dụng hướng tới khách hàng bên ngoài (Customer-facing apps), tối ưu hóa trải nghiệm mượt mà và bảo vệ dữ liệu người dùng.
