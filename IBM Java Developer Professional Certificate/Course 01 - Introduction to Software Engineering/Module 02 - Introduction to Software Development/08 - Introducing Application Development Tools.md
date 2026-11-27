# Introducing Application Development Tools

- **Khóa học:** IBM Java Developer Professional Certificate / Course 01 - Introduction to Software Engineering
- **Module:** Module 02 - Introduction to Software Development
- **Chủ đề con:** Tools in Software Development
- **Hình thức:** Video (Thời lượng: ~5,5 phút)

---

## 1. Hệ thống quản lý phiên bản (Version Control Systems - VCS)
- **Mục đích:** Theo dõi lịch sử thay đổi (ai sửa, sửa lúc nào, sửa nội dung gì), giải quyết xung đột mã nguồn (merge conflicts) và cho phép rollback về phiên bản cũ an toàn khi xảy ra sự cố.
- **Tính cần thiết:** Quan trọng ngay cả khi chỉ có một lập trình viên duy nhất phát triển dự án.
- **Công cụ tiêu biểu:** **Git** (hệ thống phân tán quản lý commit, nhánh branch, merge) kết hợp **GitHub** (remote repository lưu trữ và cộng tác mã nguồn trên nền tảng đám mây).

---

## 2. Thư viện mã nguồn (Libraries)
- **Định nghĩa:** Tập hợp các hàm, chương trình con (subroutines), module dùng chung được đóng gói sẵn để tái sử dụng mà không cần phải viết lại từ đầu (ví dụ: tạo carousel ảnh, kiểm tra email).
- **Đặc trưng kiểm soát:** **Lập trình viên nắm quyền kiểm soát luồng (You are in control)**:
  - Code của bạn chủ động gọi tới hàm của Library khi cần.
  - Khi thư viện chạy xong, quyền điều khiển quay trở lại luồng chính của ứng dụng.
- **Tính linh hoạt:** Có thể tích hợp nhiều thư viện khác nhau vào bất kỳ giai đoạn nào của dự án.
- **Ví dụ:**
  - `jQuery`: Thư viện thao tác với DOM trong JavaScript.
  - `EmailValidator`: Thư viện kiểm tra định dạng email hợp lệ.
  - `Apache Commons`: Bộ sưu tập các thành phần Java tái sử dụng mạnh mẽ.

---

## 3. Khung ứng dụng (Frameworks)
- **Định nghĩa:** Bộ khung xương (skeleton / scaffold) tiêu chuẩn định hình toàn bộ kiến trúc ứng dụng. Lập trình viên xây dựng phần mềm bằng cách điền code của mình vào khung sườn đó.
- **Tính chất bắt buộc:** Phải được chọn và thiết lập ngay từ đầu dự án; rất khó để thay đổi hay chèn ép một framework mới vào dự án đang chạy.
- **Inversion of Control (Đảo ngược quyền điều khiển - IoC):**
  - Khác với Library, **Framework nắm quyền điều khiển luồng chương trình**.
  - Quy tắc: *"Framework gọi code của bạn, chứ không phải bạn gọi framework"* (The framework calls on your code).
- **Opinionated Frameworks:** Các framework áp đặt quy chuẩn cao (quy định cấu trúc thư mục, quy tắc đặt tên file, quy chuẩn viết code) để loại bỏ các quyết định cấu hình tẻ nhạt, giúp dự án đồng nhất, chuẩn hóa và tối ưu hiệu suất.
- **Ví dụ:**
  - `Angular`: Framework web app động toàn diện (Google).
  - `Vue.js`: Framework tập trung phát triển giao diện người dùng.
  - `Django`: Web framework hoàn chỉnh dựa trên Python.
  - *(Hệ sinh thái Java): Spring Boot / Spring Framework.*

---

## 4. Bảng so sánh cốt lõi: Library vs Framework

| Tiêu chí | Thư viện (Library) | Khung ứng dụng (Framework) |
| :--- | :--- | :--- |
| **Quyền kiểm soát (Control)** | Developer chủ động gọi thư viện (*You call it*). | Framework kiểm soát luồng và gọi code của bạn (*IoC*). |
| **Kiến trúc (Architecture)** | Không ràng buộc kiến trúc tổng thể của dự án. | Định đoạt kiến trúc và cấu trúc toàn bộ dự án. |
| **Tính linh hoạt** | Rất cao; dễ dàng thêm, bớt, thay thế lúc nào cũng được. | Kém linh hoạt hơn; phải cam kết chọn ngay từ đầu. |
| **Mục đích** | Giải quyết một bài toán/tính năng cụ thể. | Cung cấp chuẩn mực để xây dựng và triển khai toàn bộ ứng dụng. |
