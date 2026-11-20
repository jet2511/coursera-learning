# Đánh Giá Kết Quả Thực Hiện Lab (Quiz / Review Answers)

Dưới đây là đáp án và giải trình đối chiếu cho 7 câu hỏi tự đánh giá (Self-Assessment) của bài Lab:

---

### Câu 1 (Question 1)
> **Have you correctly identified and included all external and internal actors (Customer, Bank Staff, Credit Bureau, Payment Gateway, Authentication Service) in your System Context Model diagram?**

- **Đáp án:** **Yes**
- **Giải trình:** Trong `Task1_System_Context_Model.md`, mô hình đã bao gồm đầy đủ 5 actors:
  1. `Customer` (Retail user)
  2. `Bank Staff` (Teller / Loan Officer)
  3. `Credit Bureau` (External credit validation)
  4. `Payment Gateway` (Funds transfer)
  5. `Authentication Service` (Secure login / MFA)

---

### Câu 2 (Question 2)
> **Did you draw arrows in the System Context Model to represent precise data exchanges between the banking system and each actor?**

- **Đáp án:** **Yes**
- **Giải trình:** Trong Task 1, bảng đặc tả Data Flow và sơ đồ đã thể hiện chính xác hướng mũi tên và nội dung trao đổi dữ liệu hai chiều giữa Digital Core với từng Actor (như: hồ sơ onboarding, điểm tín dụng, JWT token, lệnh thanh toán, biên lai).

---

### Câu 3 (Question 3)
> **Does your Use Case Diagram include all major processes, such as Customer Onboarding, Transaction Processing, Account Login, Loan Application, and View Transaction History?**

- **Đáp án:** **Yes**
- **Giải trình:** Trong `Task2_Use_Case_Diagram.md`, hệ thống đã thể hiện trọn vẹn cả 5 ca sử dụng chính:
  - `UC1: Customer Onboarding`
  - `UC2: Account Login & Authentication`
  - `UC3: Loan Application & Approval`
  - `UC4: Transaction Processing (Funds Transfer)`
  - `UC5: View Transaction History`

---

### Câu 4 (Question 4)
> **Did you use appropriate association lines, “include,” or “extend” relationships between actors and use cases in your diagram, based on the interactions described in the scenario?**

- **Đáp án:** **Yes**
- **Giải trình:** Sơ đồ Use Case đã áp dụng chuẩn các mối quan hệ:
  - Association lines nối Actors với các Use Case liên quan.
  - Quan hệ `<<include>>`: Xác thực danh tính/OTP cho các thao tác giao dịch và kiểm tra điểm tín dụng CIC cho phê duyệt khoản vay.
  - Quan hệ `<<extend>>`: Gửi thông báo biến động số dư sau khi hoàn tất giao dịch.

---

### Câu 5 (Question 5)
> **For your sequence diagram, did you clearly show the step-by-step order of messages exchanged between actors and subsystems, including authentication and transaction/loan interactions?**

- **Đáp án:** **Yes**
- **Giải trình:** Trong `Task3_Sequence_Diagram.md`, quy trình chuyển tiền (Funds Transfer) được mô hình hóa thành 18 bước có số thứ tự tuần tự rõ ràng, đi qua tuần tự 4 giai đoạn: Xác thực phiên -> Khởi tạo giao dịch -> Xác minh 2FA OTP -> Hạch toán Core & Thanh toán liên ngân hàng qua Cổng thanh toán.

---

### Câu 6 (Question 6)
> **Have you used correct UML notation (such as actor symbols, system boundaries, lifelines, activation bars, message arrows) in all your diagrams?**

- **Đáp án:** **Yes**
- **Giải trình:** Tất cả biểu đồ đều tuân thủ đúng chuẩn OMG UML:
  - Context & Use Case: Ký hiệu Actor hình người, System Boundary hình chữ nhật, Use case hình oval.
  - Sequence Diagram: Đường Lifeline nét đứt, thanh kích hoạt (Activation Bars) biểu thị thời gian xử lý, mũi tên nét liền cho Request và nét đứt cho Response.

---

### Câu 7 (Question 7)
> **Have you submitted all the required deliverables: System_Context_Model.png, Use_Case_Diagram_ABC_Bank.png, Sequence_Diagram_ABC_Bank.png, and a completed validation checklist?**

- **Đáp án:** **Yes**
- **Giải trình:** Tất cả các deliverables theo yêu cầu (`System_Context_Model.png`, `Use_Case_Diagram_ABC_Bank.png`, `Sequence_Diagram_ABC_Bank.png`, và bản checklist kiểm thử hoàn chỉnh tại `Task4_Validation_Checklist.md`) đã được chuẩn bị đầy đủ và sẵn sàng để nộp.

---

## Tổng kết đánh giá: **7/7 (100% Đạt - 7 points)**
