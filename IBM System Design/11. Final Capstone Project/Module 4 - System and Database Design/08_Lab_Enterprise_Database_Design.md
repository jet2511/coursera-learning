# 08 - Lab Guide: Enterprise Database Design

- **Thời lượng ước tính:** 30 phút
- **Tác giả:** Parikshit Jain
- **Vai trò:** Database Architect & Data Engineer
- **Bối cảnh (Scenario):** Ngân hàng bán lẻ chuyển đổi sang nền tảng Digital Core Banking hợp nhất, thay thế nhiều hệ thống phân mảnh kế thừa. Yêu cầu thiết kế lược đồ cơ sở dữ liệu quan hệ hoàn chỉnh: Khái niệm (Conceptual ERD), Logic (Logical ERD), Chuẩn hóa 3NF, mã SQL DDL và Từ điển dữ liệu (Data Dictionary).

---

## 1. Công cụ & Biểu mẫu mẫu (Template)
- **Công cụ thiết kế ERD:** Lucidchart, Draw.io.
- **Công cụ SQL / DB:** DBeaver, pgAdmin, MySQL Workbench, VS Code.
- **Biểu mẫu tham chiếu:** `Template-Enterprise Database Design.docx / .pdf`.

---

## 2. Chi tiết 7 nhiệm vụ thực hiện (Tasks to be performed)

### Task 1: Identify Key Banking Data Entities
Xác định 5 thực thể cốt lõi (`Customer`, `Account`, `Loan`, `Transaction`, `Compliance Log`) và bổ sung ít nhất 2 thực thể mở rộng thiết yếu cho ngân hàng số:
1. `Card` (Thẻ thanh toán gắn với tài khoản).
2. `Branch` (Chi nhánh / Điểm giao dịch phục vụ đối soát và quản lý nhân sự).

### Task 2: Create a Conceptual ERD
Vẽ sơ đồ thực thể mức khái niệm chỉ gồm các hộp thực thể và mối quan hệ (1:M, M:N) không thuộc tính. Xuất tệp `ConceptualERD.pdf`.

### Task 3: Build a Logical ERD with Attributes and Keys
Bổ sung đầy đủ các trường thuộc tính, xác định khóa chính (PK), khóa ngoại (FK), và bản số quan hệ (Cardinality). Xuất tệp `Logical_ERD.pdf`.

### Task 4: Apply Normalization (1NF → 2NF → 3NF)
Phân tích và minh chứng quá trình chuẩn hóa:
- **1NF:** Loại bỏ mảng/danh sách lặp lại (ví dụ tách nhiều số điện thoại, tách nhiều người đồng sở hữu).
- **2NF:** Loại bỏ phụ thuộc một phần (Partial dependency vào khóa chính tổng hợp).
- **3NF:** Loại bỏ phụ thuộc bắc cầu (Transitive dependency - ví dụ tách thông tin chi nhánh, mã bưu điện, lãi suất gói vay).

### Task 5: Write SQL DDL Scripts
Viết mã script DDL tạo bảng chuẩn Production (PostgreSQL syntax) cho 7 bảng với đầy đủ PK, FK, NOT NULL, UNIQUE, CHECK constraints, Indexes, và các trường kiểm toán (`created_at`, `updated_at`). Lưu tệp `SQL_DDL_scripts.sql`.

### Task 6: Create Data Dictionary
Lập bảng mô tả từ điển dữ liệu chi tiết: Tên bảng, Tên cột, Kiểu dữ liệu, Ràng buộc, Ý nghĩa nghiệp vụ, và đánh dấu mức độ liên quan tới tuân thủ AML / KYC.

### Task 7: Validate Database Checklist
Đối soát 6 tiêu chí nghiệm thu chất lượng thiết kế cơ sở dữ liệu ngân hàng.
