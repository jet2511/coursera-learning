# Introduction to Software Stacks

- **Khóa học:** IBM Java Developer Professional Certificate / Course 01 - Introduction to Software Engineering
- **Module:** Module 02 - Introduction to Software Development
- **Chủ đề con:** Tools in Software Development
- **Hình thức:** Video (Thời lượng: ~7,5 phút)

---

## 1. Khái niệm cốt lõi về Software Stack
- **Định nghĩa:** Software Stack là tập hợp các công nghệ (phần mềm, ngôn ngữ lập trình, frameworks, cơ sở dữ liệu) được xếp chồng theo thứ bậc (hierarchy) và phối hợp với nhau để vận hành ứng dụng:
  - **Tầng trên (Higher levels):** Cung cấp dịch vụ và giao diện trực tiếp cho người dùng.
  - **Tầng dưới (Lower levels):** Tương tác với hệ điều hành và phần cứng máy tính.
- **Phân biệt Software Stack vs Technology Stack:**
  - **Software Stack:** Tập trung vào các lớp phần mềm (Front-end, Back-end, Database, OS).
  - **Technology Stack:** Khái niệm rộng hơn, bao hàm cả hạ tầng phần cứng, ảo hóa và network (Virtual Machines, Containers, Storage, Load Balancers, Cloud Infrastructure).
- **Mô hình kiến trúc cơ bản nhất (3 lớp):**
  1. **Presentation Layer:** Tầng giao diện người dùng (Front-end).
  2. **Business Logic Layer:** Tầng xử lý nghiệp vụ (Back-end / Application Server).
  3. **Data Layer:** Tầng lưu trữ và quản lý dữ liệu (Database).

---

## 2. Các Software Stacks phổ biến trong ngành
| Stack | Thành phần cấu tạo | Đặc điểm nổi bật |
| :--- | :--- | :--- |
| **Python Django** | Python + Django Web Framework | Mã nguồn mở, phát triển nhanh, phù hợp ứng dụng lớn có sự thay đổi liên tục. |
| **Ruby on Rails** | Ruby + Rails Server Framework | Xuất sắc trong xử lý dữ liệu qua JSON/XML; kết hợp mượt mà với HTML/CSS/JS. |
| **ASP.NET (Microsoft)** | ASP.NET MVC, IIS Web Server, MS SQL Server, Azure | Hệ sinh thái hoàn chỉnh của Microsoft cho môi trường doanh nghiệp. |
| **LAMP** | **L**inux + **A**pache + **M**ySQL + **P**HP (hoặc Perl/Python) | Stack truyền thống kinh điển, mã nguồn mở, kiến trúc ghép lỏng (loosely coupled) dễ hoán đổi linh kiện (ví dụ: đổi sang PostgreSQL thành **LAPP**). |
| **MEAN** | **M**ongoDB + **E**xpress.js + **A**ngular + **N**ode.js | Toàn bộ các tầng dùng chung **JavaScript**, đa nền tảng (platform-agnostic). |
| **MERN** | **M**ongoDB + **E**xpress.js + **R**eact + **N**ode.js | Thay Angular bằng React; linh hoạt và hiệu năng rendering UI rất cao. |
| **MEVN** | **M**ongoDB + **E**xpress.js + **V**ue.js + **N**ode.js | Thay Angular bằng Vue.js; nhẹ hơn, dễ tiếp cận hơn Angular. |

---

## 3. So sánh chuyên sâu: MEAN vs MEVN vs LAMP

| Tiêu chí | MEAN / MEVN | LAMP |
| :--- | :--- | :--- |
| **Ngôn ngữ lập trình** | **Đồng nhất 1 ngôn ngữ JavaScript** từ client đến server -> Developer không cần chuyển ngữ cảnh. | Bị phân tách: Client dùng HTML/CSS/JS, Server dùng PHP/Perl/Python. |
| **Mô hình Dữ liệu** | **MongoDB:** NoSQL (document-oriented), cực tốt cho dữ liệu phi cấu trúc (unstructured data). | **MySQL:** RDBMS (quan hệ, ACID), chuẩn hóa chặt chẽ cho dữ liệu có cấu trúc cao. |
| **Hệ điều hành / Nền tảng** | Đa nền tảng (**Platform-agnostic**), chạy mượt trên Windows, Linux, macOS, Cloud Containers. | Bị ràng buộc chặt chẽ với hệ điều hành **Linux** ở tầng dưới cùng. |
| **Hệ sinh thái & Thư viện** | Hệ sinh thái Node.js/npm đồ sộ. MEAN có nhiều thư viện hơn MEVN do Vue.js mới hơn. | Rất lâu đời, tài liệu và giải pháp cộng đồng phong phú, cực kỳ ổn định. |
| **Hạn chế chính** | - MongoDB không hỗ trợ quan hệ phức tạp tốt như RDBMS.<br>- Express.js tập trung logic trên server gây khó khăn cho một số tác vụ xử lý hàng loạt (batching) quy mô lớn. | Thiếu linh hoạt với dữ liệu phi cấu trúc, đòi hỏi kỹ sư nắm song song nhiều ngôn ngữ khác nhau. |
