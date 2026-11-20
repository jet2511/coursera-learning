# Lab Guide: Create System Models, Use Cases, and Sequence Diagrams

- **Thời lượng ước tính:** 45 phút
- **Tác giả:** Parikshit Jain
- **Vai trò:** Systems Architect
- **Bối cảnh (Scenario):** Hiện đại hóa hoạt động ngân hàng bán lẻ (Retail Bank Digital Transformation), hợp nhất 3 phân hệ trọng yếu:
  1. Customer onboarding (Đăng ký / tiếp nhận khách hàng mới).
  2. Transaction processing (Xử lý giao dịch / chuyển khoản).
  3. Loan management (Quản lý và xét duyệt khoản vay).

---

## 1. Công cụ khuyến nghị & Tiêu chuẩn UML
- **Công cụ:** Lucidchart, Draw.io, hoặc Microsoft PowerPoint.
- **Tiêu chuẩn:** UML notation chuẩn (Actor, Use Case, Association, System Boundary, Lifeline, Activation Box, Include / Extend relationships).

---

## 2. Chi tiết các bước thực hiện (Tasks)

### Task 1: Create a System Context Model
- **Mục tiêu:** Thể hiện ranh giới hệ thống, phụ thuộc bên ngoài và luồng dữ liệu trao đổi.
- **System Boundary Box:** `Retail Bank's Digital Core System`
- **Các Actors cần có:**
  - `Customer`: Khách hàng cá nhân (Retail user).
  - `Teller/Loan Officer`: Nhân viên giao dịch / cán bộ tín dụng ngân hàng (Bank staff).
  - `External Credit Bureau`: Trung tâm thông tin tín dụng (thẩm định vay).
  - `Payment Gateway`: Cổng thanh toán (xử lý chuyển tiền liên ngân hàng/thẻ).
  - `Authentication Service`: Dịch vụ xác thực tập trung (đăng nhập bảo mật/SSO/MFA).
- **Luồng dữ liệu mẫu:** `Customer` → `Digital Core System` → `Payment Gateway`.
- **Tệp xuất ra:** `System_Context_Model.png` (hoặc `.pdf`).

---

### Task 2: Create a Use Case Diagram
- **Mục tiêu:** Biểu diễn các chức năng nghiệp vụ và mối quan hệ với Actors theo chuẩn UML.
- **Actors:**
  - `Customer`
  - `Bank Staff`
  - `Credit Bureau`
  - `Payment Gateway`
- **Các Use Cases chính:**
  - `UC1`: Customer onboarding (Mở tài khoản).
  - `UC2`: Account login and authentication (Đăng nhập / xác thực tài khoản).
  - `UC3`: Loan application and approval (Nộp hồ sơ vay & phê duyệt khoản vay).
  - `UC4`: Transaction processing (Funds transfer - Chuyển khoản / giao dịch).
  - `UC5`: View transaction history (Xem lịch sử giao dịch).
- **Mối quan hệ:** Nối actor với use case, áp dụng quan hệ `<<include>>` (ví dụ: chuyển tiền thì bắt buộc include login/auth) và `<<extend>>` (ví dụ: áp dụng voucher, cảnh báo số dư thấp).
- **Tệp xuất ra:** `Use_Case_Diagram_Retail_Bank.png` (hoặc `.pdf`).

---

### Task 3: Create a Sequence Diagram
- **Mục tiêu:** Mô hình hóa luồng tương tác end-to-end theo trình tự thời gian cho 1 use case trọng tâm (chọn `Funds transfer` hoặc `Customer onboarding`).
- **Lifelines / Actors (Ví dụ cho luồng Chuyển tiền - Funds Transfer):**
  - `Customer` (Actor)
  - `Web Portal / Mobile App` (Client Interface)
  - `Authentication Service` (Security)
  - `Core Banking System` (Core Processing)
  - `Payment Gateway` (External Gateway)
- **Trình tự tương tác (Message Sequence):**
  1. `Customer` → `Portal`: Request Login
  2. `Portal` → `Auth Service`: Verify Credentials
  3. `Auth Service` → `Portal`: Token Granted / Auth Success
  4. `Customer` → `Portal`: Input Transfer Details & Submit
  5. `Portal` → `Core Banking`: Request Funds Transfer (với Auth Token)
  6. `Core Banking` → `Core Banking`: Validate Account Balance & Limits
  7. `Core Banking` → `Payment Gateway`: Process Interbank Transaction
  8. `Payment Gateway` → `Core Banking`: Transaction Success Response
  9. `Core Banking` → `Portal`: Transfer Confirmation & Updated Balance
  10. `Portal` → `Customer`: Hiển thị biên lai giao dịch thành công
- **Kỹ thuật:** Vẽ thanh kích hoạt (Activation boxes/bars) thể hiện thời gian xử lý của từng service.
- **Tệp xuất ra:** `Sequence_Diagram_Retail_Bank.png` (hoặc `.pdf`).

---

### Task 4: Validate the Diagrams (Checklist)
| Tiêu chí kiểm tra | Đạt (Yes/No) | Ghi chú kiểm tra |
| :--- | :---: | :--- |
| **All key actors included** | [ ] | Đủ Customer, Staff, Credit Bureau, Payment Gateway, Auth Service |
| **Critical banking processes covered** | [ ] | Đủ Onboarding, Auth, Loan, Transfer, History |
| **Correct relationships & data flows** | [ ] | Hướng mũi tên dữ liệu và liên kết use case chính xác |
| **Accurate sequence message order** | [ ] | Thứ tự thông điệp từ trên xuống dưới logic, có reply message |
| **UML-compliant notation** | [ ] | Đúng ký hiệu chuẩn (Actor stickman, oval usecase, dashed lifeline, activation bar) |
| **File naming convention** | [ ] | Đúng tên: `System_Context_Model`, `Use_Case_Diagram_Retail_Bank`, `Sequence_Diagram_Retail_Bank` |

---

## 4. Danh mục Deliverables cho Final Project
1. `System_Context_Model.png`
2. `Use_Case_Diagram_Retail_Bank.png`
3. `Sequence_Diagram_Retail_Bank.png`
4. Bảng Checklist kiểm thử hoàn chỉnh.
