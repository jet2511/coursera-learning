# Insiders' Viewpoint: Tools and Technologies

- **Khóa học:** IBM Java Developer Professional Certificate / Course 01 - Introduction to Software Engineering
- **Module:** Module 02 - Introduction to Software Development
- **Chủ đề con:** Tools in Software Development
- **Hình thức:** Video (Thời lượng: ~6,5 phút)

---

## 1. Công cụ quản lý mã nguồn cốt lõi (Source Control)
- **Git & GitHub:** Công cụ hàng ngày không thể thiếu trong mọi dự án (open-source lẫn thương mại đóng).
- **Giá trị cốt lõi:**
  - Theo dõi mã nguồn, quản lý tính năng qua **Feature Branches** và quy trình **Pull Requests (PR)**.
  - Phục vụ theo dõi bugs, tính năng và nhiệm vụ (task tracking).
  - Ngay cả khi lập trình viên làm việc độc lập (sole committer), Git & GitHub vẫn cực kỳ giá trị nhờ tính năng sao lưu và hệ sinh thái cộng đồng.

---

## 2. Công cụ & Tiện ích IDE (IDEs, Linters & Formatters)
- **Lựa chọn IDE:**
  - Chuyên dụng Front-end: *Brackets*.
  - Đa năng, phổ quát nhất: **VS Code**.
- **Code Hygiene Tools (Bắt buộc phải tích hợp vào IDE):**
  - **ESLint:** Linter phát hiện lỗi cú pháp, vi phạm logic và phong cách code từ sớm.
  - **Prettier:** Tự động định dạng mã (code formatter) đồng nhất cho cả nhóm.

---

## 3. Hệ sinh thái Front-End & Thực hành tốt với JavaScript
- **Thực hành viết JavaScript chuẩn mực:**
  - Quản lý phạm vi biến và hàm chặt chẽ (proper scoping) để tránh lỗi runtime không mong muốn.
  - Tận dụng chuẩn hiện đại **ES6+**: arrow functions `() => {}`, spread operator `...` giúp code sạch và dễ đọc hơn.
  - Luôn viết **Unit Test** và **Integration Test** cho các tính năng.
- **Thư viện & Frameworks Front-End:**
  - **React.js (Facebook):** Rất được ưa chuộng nhờ kiến trúc hướng thành phần (**Component-driven architecture**), luồng dữ liệu một chiều với **props & state**, cú pháp **JSX** (giúp viết UI trong JS với thông báo lỗi rõ ràng) và giải quyết tốt các vấn đề tương thích đa trình duyệt (cross-browser).
  - **Angular (Google):** Thích hợp xây dựng ứng dụng trang đơn (Single Page Applications - SPAs).
  - **jQuery (John Resig, 2006) & Backbone.js:** Thư viện kinh điển, vẫn xuất hiện kết hợp trong nhiều dự án.

---

## 4. Hệ sinh thái Back-End từ góc nhìn chuyên gia
- **Node.js:** Nền tảng phía server chạy trên Chrome V8 engine, kiến trúc đơn luồng bất đồng bộ (**Asynchronous Single-Threaded**) giúp xử lý đồng thời số lượng kết nối cực lớn (high concurrent connections).
- **Express.js:** Web framework gọn nhẹ trên Node.js, hỗ trợ cơ chế caching giúp tăng tốc độ tải trang, dễ dàng đồng bộ ngôn ngữ JavaScript giữa Front-end và Back-end.
- **Các thư viện/gói npm không thể thiếu khi làm Back-end:**
  - **Axios:** Thư viện gửi HTTP requests (Web API) xử lý headers, Promise/async-await tiện lợi.
  - **NPM Database Clients:** Các gói kết nối và truy vấn RDBMS (PostgreSQL, MySQL) hoặc NoSQL (MongoDB).
- **Các Frameworks Back-End chuyên nghiệp khác:**
  - **Spring Framework / Spring Boot (Java):** Nền tảng kinh điển, bền vững hàng chục năm qua và là tiêu chuẩn vàng cho các hệ thống doanh nghiệp (Enterprise).
  - **Flask (Python):** Gọn nhẹ, linh hoạt cho cộng đồng Python.
