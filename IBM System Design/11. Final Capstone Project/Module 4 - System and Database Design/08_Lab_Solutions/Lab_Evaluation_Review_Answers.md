# Đánh Giá Kết Quả Thực Hiện Lab (Quiz / Review Answers - Enterprise Database Design)

Dưới đây là đáp án và giải trình đối chiếu cho 7 câu hỏi tự đánh giá (Self-Assessment) của bài Lab Enterprise Database Design:

---

### Câu 1 (Question 1)
> **Have you identified the key enterprise data entities for the retail banking database, including adding at least two additional relevant entities?**

- **Đáp án:** **Yes**
- **Giải trình:** Trong `Task1_Identify_Key_Data_Entities.md`, đã xác định đầy đủ 5 thực thể cốt lõi (`Customer`, `Account`, `Loan`, `Transaction`, `Compliance Log`) và bổ sung 2 thực thể mở rộng thiết yếu cho ngân hàng số: `Card` (Thẻ liên kết tài khoản) và `Branch` (Mạng lưới chi nhánh giao dịch).

---

### Câu 2 (Question 2)
> **Did you create a conceptual ERD showing entities and their relationships without attributes, as required?**

- **Đáp án:** **Yes**
- **Giải trình:** Trong `Task2_Conceptual_ERD.md`, biểu đồ Conceptual ERD thể hiện rõ ràng các khối thực thể và các mối quan hệ (1:N) theo chuẩn Crow's Foot mà không chứa bất kỳ thuộc tính chi tiết nào bên trong, đúng yêu cầu bài Lab.

---

### Câu 3 (Question 3)
> **Have you created a logical ERD that includes attributes, primary keys, foreign keys, and cardinalities for all entities?**

- **Đáp án:** **Yes**
- **Giải trình:** Trong `Task3_Logical_ERD.md`, sơ đồ Logical ERD đã bổ sung chi tiết toàn bộ các trường thuộc tính, định nghĩa rõ ràng Khóa chính (`PK`), Khóa ngoại (`FK`), kiểu dữ liệu và bản số quan hệ (Cardinalities) cho cả 7 thực thể.

---

### Câu 4 (Question 4)
> **Did you apply normalization rules (1NF to 3NF) with examples and document the normalization process in the template?**

- **Đáp án:** **Yes**
- **Giải trình:** Trong `Task4_Normalization_Summary.md`, tài liệu đã phân tích tường minh từ dạng chưa chuẩn hóa (UNF), minh họa ví dụ cụ thể về việc khử mảng lặp (1NF), khử phụ thuộc một phần (2NF), và khử phụ thuộc bắc cầu sang bảng Branch/Card độc lập (3NF).

---

### Câu 5 (Question 5)
> **Have you written secure, normalized SQL DDL scripts for at least five tables, including keys, constraints, and indexes?**

- **Đáp án:** **Yes**
- **Giải trình:** Tệp `SQL_DDL_scripts.sql` đã xây dựng hoàn chỉnh mã DDL cho 7 bảng (vượt mức tối thiểu 5 bảng), tích hợp đầy đủ `PRIMARY KEY`, `FOREIGN KEY`, `NOT NULL`, `CHECK constraints` (tuổi >= 18, số dư >= 0, enum trạng thái), `INDEXES` hiệu năng cao và tuân thủ PCI-DSS (không lưu số thẻ PAN thô).

---

### Câu 6 (Question 6)
> **Is your data dictionary complete with descriptions, data types, and constraints for all tables and fields?**

- **Đáp án:** **Yes**
- **Giải trình:** Trong `Task6_Data_Dictionary.md`, từ điển dữ liệu đã mô tả cặn kẽ 100% các cột của các bảng nghiệp vụ, bao gồm kiểu dữ liệu, ràng buộc, ý nghĩa kinh doanh và mức độ liên quan tới tuân thủ AML / KYC.

---

### Câu 7 (Question 7)
> **Have you validated your database design against business rules, regulatory compliance, and integrity standards using the lab checklist?**

- **Đáp án:** **Yes**
- **Giải trình:** Trong `Task7_Validation_Checklist.md`, toàn bộ 6 tiêu chí kiểm thử chất lượng thiết kế dữ liệu ngân hàng đã được đối soát và xác nhận đạt chuẩn (100% PASSED).

---

## Tổng kết đánh giá: **7/7 (100% Đạt - 7 points)**
