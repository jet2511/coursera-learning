# Task 6: Data Dictionary (Enterprise Retail Banking Schema)

Bảng từ điển dữ liệu đặc tả chi tiết toàn bộ các trường, kiểu dữ liệu, ràng buộc bảo mật và mức độ liên quan tới tuân thủ AML / KYC cho cơ sở dữ liệu Retail Bank.

---

## 1. Bảng `customers` (Hồ sơ khách hàng)

| Tên trường (Field Name) | Kiểu dữ liệu (Data Type) | Ràng buộc (Constraints) | Ý nghĩa nghiệp vụ (Business Description) | Tuân thủ (Compliance / KYC / AML) |
| :--- | :--- | :--- | :--- | :---: |
| `customer_id` | SERIAL / INT | PK, NOT NULL | Mã định danh khách hàng duy nhất trong toàn hệ thống. | Định danh Core |
| `branch_id` | INT | FK -> `branches`, NOT NULL | Chi nhánh mở tài khoản gốc. | Quản trị địa bàn |
| `national_id` | VARCHAR(30) | UNIQUE, NOT NULL | Số Căn cước công dân / Hộ chiếu cá nhân. | **KYC Bắt buộc** |
| `first_name` | VARCHAR(50) | NOT NULL | Tên khách hàng. | KYC |
| `last_name` | VARCHAR(50) | NOT NULL | Họ và tên đệm khách hàng. | KYC |
| `dob` | DATE | NOT NULL, CHECK (>= 18 tuổi)| Ngày tháng năm sinh (đảm bảo đủ năng lực hành vi dân sự).| KYC |
| `email` | VARCHAR(100) | UNIQUE, NOT NULL | Hộp thư điện tử chính thức nhận thông báo & OTP. | Liên lạc & MFA |
| `phone` | VARCHAR(20) | NOT NULL | Số điện thoại di động đăng ký dịch vụ SMS Banking. | **2FA / OTP** |
| `kyc_status` | VARCHAR(20) | CHECK ('Pending', 'Verified', 'Rejected') | Trạng thái thẩm định danh tính điện tử eKYC. | **Quy chuẩn KYC** |
| `risk_level` | VARCHAR(10) | CHECK ('LOW', 'MEDIUM', 'HIGH') | Phân loại mức độ rủi ro phòng chống rửa tiền. | **Quy chuẩn AML** |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Thời điểm mở hồ sơ khách hàng. | Audit Trail |

---

## 2. Bảng `accounts` (Tài khoản ngân hàng)

| Tên trường (Field Name) | Kiểu dữ liệu (Data Type) | Ràng buộc (Constraints) | Ý nghĩa nghiệp vụ (Business Description) | Tuân thủ (Compliance) |
| :--- | :--- | :--- | :--- | :---: |
| `account_id` | SERIAL / INT | PK, NOT NULL | Khóa chính nội bộ quản lý tài khoản. | Khóa hệ thống |
| `account_number` | VARCHAR(34) | UNIQUE, NOT NULL | Số tài khoản hiển thị phục vụ giao dịch (Chuẩn IBAN). | Core Ledger |
| `customer_id` | INT | FK -> `customers`, NOT NULL | Mã khách hàng chủ sở hữu tài khoản. | Liên kết chủ thể |
| `branch_id` | INT | FK -> `branches`, NOT NULL | Chi nhánh quản lý tài khoản. | Đối soát nội bộ |
| `account_type` | VARCHAR(20) | CHECK ('CHECKING', 'SAVINGS', 'PAYROLL') | Loại hình tài khoản (Thanh toán, Tiết kiệm, Trả lương).| Phân loại SP |
| `currency` | VARCHAR(3) | DEFAULT 'USD', NOT NULL | Loại tiền tệ giao dịch (USD, VND, EUR). | Quy chế ngoại hối |
| `balance` | NUMERIC(15,2)| NOT NULL, CHECK (>= 0.00) | Số dư khả dụng hiện tại (không cho phép số âm). | **Bảo toàn vốn** |
| `status` | VARCHAR(20) | CHECK ('ACTIVE', 'FROZEN', 'DORMANT', 'CLOSED') | Trạng thái tài khoản (Đang hoạt động, Phong tỏa, Đóng).| Kiểm soát rủi ro |
| `opened_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Ngày mở tài khoản. | Audit Trail |

---

## 3. Bảng `transactions` (Sổ cái giao dịch tài chính)

| Tên trường (Field Name) | Kiểu dữ liệu (Data Type) | Ràng buộc (Constraints) | Ý nghĩa nghiệp vụ (Business Description) | Tuân thủ (Compliance) |
| :--- | :--- | :--- | :--- | :---: |
| `transaction_id` | VARCHAR(64) | PK, NOT NULL | Mã tham chiếu giao dịch độc nhất toàn cầu (UUID/FTx). | **Audit Trail** |
| `account_id` | INT | FK -> `accounts`, NOT NULL | Tài khoản trích tiền (tài khoản nguồn). | Hạch toán |
| `destination_account`| VARCHAR(34)| NOT NULL | Tài khoản thụ hưởng (nội bộ hoặc ngân hàng khác). | Truy vết dòng tiền |
| `transaction_type` | VARCHAR(30) | CHECK ('DEPOSIT', 'WITHDRAWAL', 'TRANSFER', ...) | Bản chất giao dịch (Nạp, Rút, Chuyển khoản, Giải ngân).| Báo cáo kế toán |
| `amount` | NUMERIC(15,2)| NOT NULL, CHECK (> 0) | Giá trị tiền tệ của giao dịch (phải > 0). | **Bảo đảm hạch toán**|
| `currency` | VARCHAR(3) | NOT NULL, DEFAULT 'USD' | Loại tiền tệ giao dịch. | Quy chế tiền tệ |
| `status` | VARCHAR(20) | CHECK ('PENDING', 'COMPLETED', 'FAILED', ...) | Trạng thái xử lý giao dịch. | Đối soát giao dịch |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Thời điểm khởi tạo giao dịch. | Báo cáo giao dịch |
| `completed_at` | TIMESTAMP | NULLABLE | Thời điểm thanh toán thành công qua cổng liên ngân hàng.| Đối soát liên NH |

---

## 4. Bảng `loans` (Danh mục khoản vay tín dụng)

| Tên trường (Field Name) | Kiểu dữ liệu (Data Type) | Ràng buộc (Constraints) | Ý nghĩa nghiệp vụ (Business Description) | Tuân thủ (Compliance) |
| :--- | :--- | :--- | :--- | :---: |
| `loan_id` | SERIAL / INT | PK, NOT NULL | Mã định danh hợp đồng tín dụng. | Quản trị tín dụng |
| `customer_id` | INT | FK -> `customers`, NOT NULL | Khách hàng đứng tên vay vốn. | Trách nhiệm dân sự |
| `loan_type` | VARCHAR(30) | NOT NULL | Gói vay (Vay mua nhà MORTGAGE, Vay tiêu dùng PERSONAL). | Phân loại tài sản |
| `principal_amount` | NUMERIC(15,2)| NOT NULL, CHECK (> 0) | Số tiền gốc giải ngân. | Hạn mức tín dụng |
| `interest_rate` | NUMERIC(5,2) | NOT NULL, CHECK (>= 0) | Lãi suất vay (%/năm). | Hợp đồng tín dụng |
| `term_months` | INT | NOT NULL, CHECK (>= 1) | Thời hạn vay tính bằng tháng. | Lịch trả nợ |
| `loan_status` | VARCHAR(20) | CHECK ('PENDING', 'APPROVED', 'ACTIVE', ...) | Phân loại trạng thái nợ (Chuẩn nợ xấu CIC). | **Báo cáo trích lập DPRR**|

---

## 5. Bảng `compliance_logs` (Nhật ký giám sát & AML)

| Tên trường (Field Name) | Kiểu dữ liệu (Data Type) | Ràng buộc (Constraints) | Ý nghĩa nghiệp vụ (Business Description) | Tuân thủ (Compliance) |
| :--- | :--- | :--- | :--- | :---: |
| `log_id` | SERIAL / INT | PK, NOT NULL | Mã nhật ký kiểm toán duy nhất. | Bất biến (Immutable) |
| `transaction_id` | VARCHAR(64) | FK -> `transactions`, NULLABLE | Giao dịch phát sinh cảnh báo (nếu có). | Truy nguyên vết |
| `customer_id` | INT | FK -> `customers`, NULLABLE | Khách hàng bị gắn cờ giám sát. | Giám sát danh sách đen |
| `event_type` | VARCHAR(50) | NOT NULL, CHECK ('AML_SUSPICIOUS', ...) | Loại sự kiện (Giao dịch lớn, Gian lận thẻ, Đăng nhập lỗi).| **Báo cáo FIU/NHNN** |
| `risk_score` | INT | CHECK (BETWEEN 0 AND 100) | Điểm rủi ro do AI/Rule Engine tính toán. | Phân loại rủi ro |
| `action_taken` | VARCHAR(50) | NOT NULL | Biện pháp can thiệp (Chặn giao dịch, Cảnh báo, Báo cáo).| Quy trình tuân thủ |
| `logged_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Thời điểm ghi log hệ thống. | **Bằng chứng pháp lý** |
