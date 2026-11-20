# Task 4: Apply Normalization (1NF → 2NF → 3NF)

Tài liệu chứng minh quá trình chuẩn hóa cơ sở dữ liệu từ dạng chưa chuẩn hóa (Unnormalized Form - UNF) qua các dạng chuẩn 1NF, 2NF, và 3NF nhằm loại bỏ dư thừa dữ liệu (data redundancy) và ngăn ngừa các dị thường cập nhật (anomalies).

---

## 1. Dạng chưa chuẩn hóa ban đầu (Unnormalized Form - UNF)

Giả sử trong hệ thống cũ, toàn bộ thông tin ngân hàng lưu trong một bảng khổng lồ:
`BANK_RECORDS (Customer_ID, Full_Name, Phone_Numbers, Accounts_List, Branch_Code, Branch_Name, Branch_Address, Loan_ID, Loan_Amount, Loan_Interest_Rate, Txn_ID, Txn_Amount, Txn_Date)`

---

## 2. Quá trình chuẩn hóa chi tiết

### Bước 1: Dạng chuẩn 1 (1NF - First Normal Form)
- **Quy tắc:** Mỗi cột phải chứa giá trị nguyên tố (Atomic values), không chứa nhóm lặp (No repeating groups) hoặc mảng (Arrays).
- **Vấn đề phát hiện ở UNF:**
  - `Phone_Numbers` chứa nhiều số điện thoại trong 1 ô (ví dụ: `"0901234567, 0987654321"`).
  - `Accounts_List` chứa danh sách nhiều tài khoản trong cùng một dòng.
- **Hành động xử lý (Action Taken):**
  - Tách `Full_Name` thành `First_Name` và `Last_Name`.
  - Tách các nhóm lặp thành các thực thể độc lập: Tách riêng bảng `CUSTOMER` và bảng `ACCOUNT`, mỗi thuộc tính chỉ chứa 1 giá trị đơn lẻ. Đảm bảo mỗi bảng có khóa chính (PK) xác định duy nhất dòng.

---

### Bước 2: Dạng chuẩn 2 (2NF - Second Normal Form)
- **Quy tắc:** Bảng đã đạt 1NF và **không tồn tại phụ thuộc một phần (No partial dependencies)**. Mọi thuộc tính không khóa phải phụ thuộc hoàn toàn vào toàn bộ khóa chính (đặc biệt khi khóa chính là khóa tổng hợp composite PK).
- **Vấn đề phát hiện sau 1NF:**
  - Nếu lưu chung bảng quan hệ `CUSTOMER_ACCOUNT (Customer_ID, Account_Number, Customer_Name, Account_Balance)`:
    - Khóa chính là `(Customer_ID, Account_Number)`.
    - Thuộc tính `Customer_Name` chỉ phụ thuộc vào `Customer_ID` (phụ thuộc 1 phần).
    - Thuộc tính `Account_Balance` chỉ phụ thuộc vào `Account_Number` (phụ thuộc 1 phần).
- **Hành động xử lý (Action Taken):**
  - Tách thành 2 bảng riêng biệt với khóa chính đơn:
    - Bảng `CUSTOMER (customer_id [PK], first_name, last_name, ...)`
    - Bảng `ACCOUNT (account_id [PK], customer_id [FK], balance, ...)`
  - Mọi trường dữ liệu lúc này phụ thuộc trọn vẹn vào chính khóa của bảng đó.

---

### Bước 3: Dạng chuẩn 3 (3NF - Third Normal Form)
- **Quy tắc:** Bảng đã đạt 2NF và **không tồn tại phụ thuộc bắc cầu (No transitive dependencies)**. Nghĩa là: Thuộc tính không khóa không được phụ thuộc vào một thuộc tính không khóa khác (`X -> Y` và `Y -> Z`, với `X` là PK).
- **Vấn đề phát hiện sau 2NF:**
  - Trong bảng `CUSTOMER`: Có các cột `(customer_id [PK], ..., branch_code, branch_name, branch_city)`.
    - Ta có: `customer_id -> branch_code`, và `branch_code -> branch_name, branch_city`.
    - Khi đó, thông tin chi nhánh bị phụ thuộc bắc cầu vào `customer_id`. Nếu đổi tên chi nhánh, phải update hàng triệu dòng khách hàng (Dị thường sửa đổi - Update Anomaly).
  - Trong bảng `ACCOUNT`: Có các cột `(account_id [PK], card_number, card_expiry, card_status)`.
    - Tài khoản phụ thuộc bắc cầu tới thông tin thẻ (một tài khoản có thể đổi thẻ mới mà số tài khoản không đổi).
- **Hành động xử lý (Action Taken):**
  - Tách bảng `BRANCH` riêng: `BRANCH (branch_id [PK], branch_code [UK], branch_name, city)`. Trong bảng `CUSTOMER` và `ACCOUNT` chỉ lưu `branch_id` làm khóa ngoại (FK).
  - Tách bảng `CARD` riêng: `CARD (card_id [PK], account_id [FK], card_number_masked, expiry_date, card_status)`.
  - Tách bảng `COMPLIANCE_LOG` riêng khỏi `TRANSACTION` để tối ưu hóa hiệu năng bảng giao dịch tài chính (OLTP).

---

## 3. Bảng tóm tắt chuẩn hóa (Normalization Summary Table)

| Mức chuẩn hóa (Normal Form) | Tình trạng dị thường trước chuẩn hóa (Identified Anomalies) | Hành động cải tiến (Action Taken) | Kết quả đạt được (Clean Normalized Structure) |
| :---: | :--- | :--- | :--- |
| **1NF** | Cột chứa mảng giá trị (nhiều SĐT, chuỗi tài khoản gộp), họ tên ghép chung. | Phân rã dữ liệu thành đơn vị nguyên tử (Atomic); tách bảng cha-con cơ bản. | Các trường đều là atomic, xác định rõ PK cho từng bảng. |
| **2NF** | Thuộc tính không khóa phụ thuộc một phần vào khóa tổng hợp (Composite Keys). | Tách các thực thể con ra bảng độc lập, dùng surrogate key (ID tự tăng/UUID) làm PK đơn. | Loại bỏ hoàn toàn phụ thuộc một phần; mỗi bảng quản lý đúng một đối tượng nghiệp vụ. |
| **3NF** | Phụ thuộc bắc cầu: Thông tin chi nhánh nằm trong bảng khách hàng; thông tin thẻ nằm trong bảng tài khoản. | Tách riêng các bảng danh mục độc lập (`BRANCH`, `CARD`, `COMPLIANCE_LOG`), liên kết qua FK. | Cấu trúc dữ liệu 7 bảng sạch sẽ, loại bỏ 100% rủi ro dị thường thêm/xóa/sửa (Insert/Delete/Update Anomalies). |
