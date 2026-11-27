# 07 - Assignment Overview: Database Design, Storage, and Migration

- **Thời lượng ước tính:** 2 phút
- **Tác giả:** Parikshit Jain
- **Mục tiêu:** Thiết kế nền tảng dữ liệu cốt lõi (Database Foundation Layer) cho nền tảng ngân hàng số **ABC Bank Digital Core**. Quy trình đi từ xác định thực thể dữ liệu, xây dựng biểu đồ ERD (Conceptual & Logical), chuẩn hóa dữ liệu (1NF → 2NF → 3NF), viết script SQL DDL chuẩn production, xây dựng từ điển dữ liệu (Data Dictionary), và hoạch định chiến lược lưu trữ / di chuyển dữ liệu (Storage & Migration).

---

## 1. Mục đích bài tập (Purpose)

1. Xác định các thực thể dữ liệu cốt lõi trong toàn ngân hàng: `Customer`, `Account`, `Loan`, `Transaction`, `Compliance / Audit Log`.
2. Vẽ biểu đồ quan hệ thực thể mức khái niệm (**Conceptual ERD**) và mức logic (**Logical ERD**) thể hiện rõ khóa chính, khóa ngoại và quan hệ bản số (cardinality).
3. Áp dụng chuẩn hóa cơ sở dữ liệu (**1NF, 2NF, 3NF**) để loại bỏ trùng lặp dữ liệu và bảo đảm tính toàn vẹn tham chiếu.
4. Viết script **SQL DDL** hoàn chỉnh cấp production với đầy đủ ràng buộc: PK, FK, NOT NULL, UNIQUE, CHECK constraints, Indexes và trường kiểm toán (Audit fields).
5. Xây dựng **Từ điển dữ liệu (Data Dictionary)** chi tiết phục vụ quản trị dữ liệu (Data Governance) và tuân thủ quy chuẩn phòng chống rửa tiền / định danh (AML / KYC).
6. Định hướng chiến lược phân tầng lưu trữ (Storage Tiering: Active, Warm, Cold/Archive) và lộ trình di chuyển dữ liệu (Migration Strategy) từ Core cũ sang Core mới.

---

## 2. Quy trình 7 bước thực hiện (7 Steps Workflow)

- **Step 1: Identify Key Data Entities:** Lập danh sách thực thể nghiệp vụ ngân hàng cốt lõi và thực thể bổ trợ.
- **Step 2: Draft a Conceptual ERD:** Vẽ biểu đồ thực thể mức khái niệm (chỉ gồm Entities và mối quan hệ 1:1, 1:N, M:N; không chứa thuộc tính).
- **Step 3: Build a Logical ERD:** Bổ sung đầy đủ thuộc tính, xác định Primary Keys (PK), Foreign Keys (FK), Cardinality rules.
- **Step 4: Apply Normalization (1NF → 2NF → 3NF):** Phân tích và xử lý Repeating groups (1NF), Partial dependencies (2NF), Transitive dependencies (3NF).
- **Step 5: Generate SQL DDL Scripts:** Viết mã lệnh SQL DDL hoàn chỉnh với các ràng buộc nghiệp vụ tài chính và index tối ưu truy vấn.
- **Step 6: Develop a Data Dictionary:** Lập bảng định nghĩa chi tiết cho từng cột (Data type, Size, Constraints, Business Meaning, KYC/AML relevance).
- **Step 7: Validate Using a Checklist:** Kiểm tra đối soát 6 tiêu chí chất lượng trước khi nộp bài.

---

## 3. Sản phẩm bàn giao (Deliverables)

1. **Entity Identification Table:** Bảng xác định và mô tả các thực thể dữ liệu.
2. **Conceptual ERD Diagram (.png):** Sơ đồ quan hệ thực thể mức khái niệm.
3. **Logical ERD Diagram (.png):** Sơ đồ quan hệ thực thể mức logic.
4. **Normalization Summary Table:** Bảng tổng hợp các bước chuẩn hóa 1NF, 2NF, 3NF.
5. **SQL DDL Script File (.sql hoặc .txt):** Tệp kịch bản khởi tạo cơ sở dữ liệu hoàn chỉnh.
6. **Data Dictionary (.docx hoặc .xlsx):** Từ điển dữ liệu chi tiết cho toàn bộ các trường.
7. **Validation Checklist:** Bảng kiểm tra nghiệm thu tuân thủ chuẩn dữ liệu ngân hàng.
