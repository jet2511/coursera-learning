# The Importance of Back-End Development

- **Khóa học:** IBM Java Developer Professional Certificate / Course 01 - Introduction to Software Engineering
- **Module:** Module 02 - Introduction to Software Development
- **Chủ đề con:** Introduction to Development
- **Hình thức:** Video (Thời lượng: ~6,5 phút)

---

## 1. Bản chất & Vai trò của Back-End Development
- Trong khi **Front-End** chịu trách nhiệm về giao diện hiển thị và tương tác trực tiếp với người dùng, **Back-End** quản lý toàn bộ tài nguyên, hạ tầng máy chủ (server infrastructure) để:
  - Tiếp nhận và xử lý các yêu cầu (requests) từ client.
  - Xử lý business logic, tính toán dữ liệu.
  - Tương tác với cơ sở dữ liệu để truy xuất hoặc lưu trữ thông tin.
  - Đảm bảo an toàn bảo mật dữ liệu nhạy cảm (thông tin đăng nhập, thông tin thẻ tín dụng, địa chỉ thanh toán).

---

## 2. API, Routing & Endpoints
Back-end xử lý các request từ front-end thông qua cơ chế định tuyến và giao tiếp chuẩn hóa:
- **API (Application Programming Interface):** Đoạn mã cho phép trao đổi dữ liệu có cấu trúc giữa các hệ thống (phổ biến qua định dạng JSON hoặc XML). Cung cấp cơ chế cho web app, mobile app, cloud app kết nối tới tài nguyên máy chủ.
- **Route:** Đường dẫn (path) logic trên server dẫn tới tài nguyên hoặc luồng xử lý cụ thể dựa trên input người dùng.
- **Endpoint:** Điểm cuối kết nối của API hoặc đường dẫn tài nguyên cụ thể.
- **Cơ chế Routing:**
  - Request từ client gửi đến -> Server định tuyến (routing) đến đúng service xử lý.
  - Nếu endpoint hợp lệ -> Server trả về kết quả tương ứng.
  - Nếu endpoint không tồn tại -> Server trả về mã lỗi **404 Not Found**.

---

## 3. Ngôn ngữ & Frameworks Back-End phổ biến
| Ngôn ngữ | Framework tiêu biểu | Đặc tính |
| :--- | :--- | :--- |
| **JavaScript / TypeScript** | Node.js, Express | Đưa JavaScript chạy trên server; xử lý bất đồng bộ tốt, tái sử dụng ngôn ngữ giữa FE & BE. |
| **Python** | Django, Flask | Dễ học, linh hoạt, hỗ trợ mạnh từ web app, kết nối database đến xử lý và phân tích dữ liệu. |
| **Java** *(Trọng tâm chuyên sâu của chứng chỉ)* | Spring Boot, Jakarta EE | Hiệu năng cao, bảo mật chặt chẽ, tiêu chuẩn cho các hệ thống doanh nghiệp (Enterprise Systems). |

---

## 4. Cơ sở dữ liệu & Công cụ ORM
- **SQL / Database Fundamentals:** Kỹ năng bắt buộc để truy vấn, tối ưu hóa và lưu trữ dữ liệu bền vững (RDBMS hoặc NoSQL).
- **ORM (Object-Relational Mapping):**
  - Công cụ ánh xạ bảng trong database thành các đối tượng (objects) trong mã nguồn back-end.
  - Giúp trừu tượng hóa, giảm độ phức tạp khi viết truy vấn thủ công.
  - *Lưu ý quan trọng:* Dù dùng ORM, developer vẫn phải nắm vững nguyên lý cơ sở dữ liệu để debug, tối ưu hiệu năng và xử lý lỗi khi cần.

---

## 5. Nhiệm vụ cốt lõi hàng ngày của Back-End Developer
- **Quản lý xác thực & phân quyền:** Authentication (xác minh danh tính) & Authorization (kiểm tra quyền truy cập).
- **Bảo mật dữ liệu:** Mã hóa và bảo vệ an toàn cho dữ liệu nhạy cảm khi truyền tải và lưu trữ.
- **Xây dựng & duy trì APIs:** Thiết kế các endpoints ổn định, chịu tải tốt cho Web, Mobile và Cloud.
- **Hợp tác chặt chẽ với Front-End:** Thống nhất contract/schema dữ liệu trước khi triển khai để hệ thống hoạt động ăn khớp.
