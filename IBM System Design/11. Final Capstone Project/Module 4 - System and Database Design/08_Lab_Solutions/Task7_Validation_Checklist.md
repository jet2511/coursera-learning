# Task 7: Database Design Validation Checklist

Bảng kiểm tra nghiệm thu chất lượng thiết kế cơ sở dữ liệu Retail Bank trước khi bàn giao đưa vào triển khai hệ sinh thái Core Banking.

---

## 1. Bảng đối soát nghiệm thu (Validation Checklist)

| STT | Tiêu chí kiểm tra (Validation Criteria) | Tiêu chuẩn chất lượng (Quality Standards) | Kết quả (Status) | Minh chứng tệp tương ứng (File Evidence) |
| :---: | :--- | :--- | :---: | :--- |
| **1** | **Entities cover required banking domains** | Bao phủ trọn vẹn 5 domain cốt lõi và 2 domain mở rộng (Customer, Account, Loan, Transaction, Compliance, Card, Branch). | **PASSED** | Đã liệt kê và phân tích tại `Task1_Identify_Key_Data_Entities.md` |
| **2** | **ERDs follow correct cardinalities** | Bản số quan hệ (1:1, 1:N) và ký hiệu Crow's Foot thể hiện chính xác logic ngân hàng. | **PASSED** | Thể hiện chuẩn xác tại `Task2_Conceptual_ERD.md` và `Task3_Logical_ERD.md` |
| **3** | **Normalization properly applied** | Cấu trúc dữ liệu đã chuẩn hóa 1NF, 2NF, 3NF; loại bỏ hoàn toàn các dị thường thêm/xóa/sửa. | **PASSED** | Minh chứng và giải trình tại `Task4_Normalization_Summary.md` |
| **4** | **SQL scripts follow naming and security standards** | Script DDL hoàn chỉnh, có ràng buộc PK, FK, NOT NULL, UNIQUE, CHECK, Indexes, bảo mật PCI-DSS (không lưu PAN thô). | **PASSED** | Tệp script `SQL_DDL_scripts.sql` đã sẵn sàng thực thi trên PostgreSQL/Oracle |
| **5** | **Data dictionary complete and clear** | Định nghĩa chi tiết từng cột, kiểu dữ liệu, kích thước, ràng buộc và ý nghĩa nghiệp vụ. | **PASSED** | Lập bảng chi tiết tại `Task6_Data_Dictionary.md` |
| **6** | **Design aligns with compliance (KYC/AML)** | Có trường phục vụ định danh khách hàng eKYC, phân loại rủi ro và lưu vết kiểm toán bất biến. | **PASSED** | Các cột `kyc_status`, `risk_level`, `compliance_logs` đáp ứng đầy đủ yêu cầu kiểm toán |

---

## 2. Tổng kết danh mục deliverables đã sẵn sàng bàn giao:
- `Task1_Identify_Key_Data_Entities.md`: Bảng nhận diện 7 thực thể dữ liệu.
- `Task2_Conceptual_ERD.md`: Conceptual ERD (.png/Mermaid).
- `Task3_Logical_ERD.md`: Logical ERD (.png/Mermaid).
- `Task4_Normalization_Summary.md`: Bảng tóm tắt chuẩn hóa 3NF.
- `SQL_DDL_scripts.sql`: Script DDL tạo bảng chuẩn Production.
- `Task6_Data_Dictionary.md`: Từ điển dữ liệu chi tiết cho toàn bộ bảng.
- `Task7_Validation_Checklist.md`: Bảng nghiệm thu đạt 100% (6/6 tiêu chí).
