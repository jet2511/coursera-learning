# Hands-on Lab: Migrate an OLTP Schema to a NoSQL Database

## 1. Tóm tắt nội dung Lab (Summary)

- **Mục tiêu:** Chuyển đổi mô hình cơ sở dữ liệu quan hệ (RDBMS/OLTP trên MySQL) sang cơ sở dữ liệu phi quan hệ (NoSQL Document-based trên MongoDB) cho hệ thống ngân hàng giả định **FinHub Bank**.
- **Công cụ sử dụng:**
  - **MySQL 8.0.22 & phpMyAdmin:** Dùng để dựng schema OLTP, nạp dữ liệu và xuất dữ liệu dạng JSON.
  - **MongoDB & mongo-express:** Dùng để tạo database, collection và nhập các document JSON.
- **Quy trình thực hiện:**
  1. **Thiết lập RDBMS (MySQL):** Tạo database `finhub`, chạy script SQL dựng bảng và nạp dữ liệu gốc.
  2. **Trích xuất JSON:** Sử dụng SQL query để chuyển đổi dữ liệu các bảng thành định dạng JSON.
  3. **Nạp vào NoSQL (MongoDB):** Tạo database `finhub` trên MongoDB, tạo các collection tương ứng và chèn (import) dữ liệu JSON vào từng collection.

---

## 2. Chi tiết các bước thực hiện & Lời giải (Step-by-Step Solution)

### Exercise 1: Thiết lập cơ sở dữ liệu OLTP (MySQL)

1. **Khởi chạy MySQL & phpMyAdmin:**
   - Mở tab **DATABASES** -> Chọn **MySQL** -> Nhấn **Create** và chờ chuyển sang trạng thái **Active**.
   - Mở **Summary** -> Nhấp vào **phpMyAdmin**.
2. **Tạo Database:**
   - Trong phpMyAdmin, tạo database mới với tên: `finhub`.
3. **Import Cấu trúc & Dữ liệu:**
   - Tải file script: [`create-tables-scripts.sql`](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/ZtieImzuBhOe0cwzLwnZxA/create-tables-scripts.sql)
   - Chọn database `finhub` -> tab **Import** -> Chọn file vừa tải -> Nhấn **Import**.
4. **Xuất dữ liệu bảng MySQL sang JSON:**
   - Tải script query xuất JSON: [`mysql-table-to-json.sql`](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/HyNRvn88uA6d4wubLp0tXg/mysql-table-to-json.sql)
   - Thực thi từng câu query trong file SQL, chọn hiển thị **Full texts**, sao chép kết quả và lưu thành các file JSON tương ứng (hoặc tải trực tiếp theo link):
     - `account_type.json` (Gồm 7 loại tài khoản)
     - `branches.json`
     - `countries.json`
     - `customer_data.json`
     - `transaction_data.json`
     - `us_cities.json`

---

### Exercise 2: Migrate dữ liệu sang NoSQL Database (MongoDB)

1. **Khởi chạy MongoDB & mongo-express:**
   - Mở tab **DATABASES** -> Chọn **MongoDB** -> Nhấn **Create** và đợi trạng thái **Active**.
   - Mở **Summary** -> Nhấp vào **mongo-express** để vào giao diện quản trị MongoDB.
2. **Tạo Database:**
   - Tạo Database mới với tên: `finhub`.
3. **Tạo Collections và Import Document:**
   - Truy cập vào database `finhub`, tiến hành tạo lần lượt 6 collection và paste dữ liệu JSON tương ứng vào document mới:

| Collection Name | Nguồn file JSON | Kiểm tra kết quả |
| :--- | :--- | :--- |
| `account_type` | `account_type.json` | Đảm bảo document chứa đầy đủ 7 account types |
| `branches` | `branches.json` | Chứa dữ liệu các chi nhánh |
| `countries` | `countries.json` | Chứa danh sách quốc gia |
| `customer_data` | `customer_data.json` | Chứa thông tin khách hàng |
| `transaction_data` | `transaction_data.json`| Chứa lịch sử giao dịch |
| `us_cities` | `us_cities.json` | Chứa danh mục thành phố |

---

## 3. Bài học & Kiến trúc rút ra (Key Takeaways)

- **Chuyển đổi Paradigm:** Dữ liệu có cấu trúc dạng bảng (tables/rows/relations) được chuyển đổi thành các document BSON/JSON có tính linh hoạt cao hơn (collections/documents).
- **Mở rộng (Scalability):** Chuyển dịch sang NoSQL giúp FinHub Bank dễ dàng scale theo chiều ngang (horizontal scaling) và linh hoạt trong việc thay đổi schema dữ liệu giao dịch sau này mà không cần `ALTER TABLE` phức tạp.
