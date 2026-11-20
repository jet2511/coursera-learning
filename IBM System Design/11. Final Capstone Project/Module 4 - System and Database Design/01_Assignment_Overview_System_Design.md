# Assignment Overview: System Design with Use Case and Sequence Diagrams

- **Estimated Time:** 2 minutes
- **Author:** Parikshit Jain
- **Target System:** Retail Bank Digital Transformation (Digital Core System)

---

## 1. Mục tiêu (Introduction)
Thiết kế các luồng tương tác hệ thống cho quá trình chuyển đổi số của Retail Bank bằng mô hình UML (Use Case & Sequence Diagrams):
- Xác định actors, workflow chính và dynamic processes.
- Làm rõ hành vi hệ thống và chuẩn bị sẵn sàng cho giai đoạn triển khai (implementation readiness).

---

## 2. Các nhiệm vụ chính (Tasks)

### Task 1: Develop a System Context Model
- Xác định và vẽ diagram thể hiện tất cả actors chính cùng tương tác trong phạm vi ranh giới hệ thống (system boundary) của Digital Core.
- Thể hiện các luồng dữ liệu giữa người dùng, các subsystem và external entities (hệ thống bên thứ 3/đối tác).

### Task 2: Create Use Case Diagrams
- Thiết kế UML Use Case Diagrams cho các nghiệp vụ ngân hàng cốt lõi:
  - Customer onboarding (mở tài khoản/đăng ký khách hàng).
  - Transaction management (quản lý giao dịch/chuyển tiền/thanh toán).
  - Loan servicing (quản lý và xử lý khoản vay).
- Thể hiện mối quan hệ giữa các use case với stakeholders/actors liên quan.

### Task 3: Build Sequence Diagrams
- Mô hình hóa luồng tương tác chi tiết theo thời gian cho một use case trọng tâm.
- Thể hiện rõ message exchange (gửi/nhận thông điệp), component activations (vòng đời kích hoạt), và responses qua các thành phần:
  - Authentication service
  - Core Banking system
  - Payment Gateways

### Task 4: Validate UML Diagrams
- Sử dụng checklist để nghiệm thu và kiểm tra:
  - Tính đầy đủ (completeness) và chính xác (accuracy).
  - Tuân thủ chuẩn UML (UML compliance).
  - Độ rõ ràng (clarity).
  - Khớp với yêu cầu kinh doanh và quy ước đặt tên (naming conventions) của Retail Bank.

---

## 3. Sản phẩm bàn giao (Deliverables)

1. `System_Context_Model.png`: Mô hình ngữ cảnh hệ thống (actors & boundary).
2. `Use_Case_Diagram_Retail_Bank.png`: Biểu đồ use case thể hiện chức năng nghiệp vụ và actors.
3. `Sequence_Diagram_Retail_Bank.png`: Biểu đồ tuần tự chi tiết cho use case trọng tâm.
4. **Completed validation checklist**: Bảng checklist kiểm tra chất lượng và độ tuân thủ chuẩn của các biểu đồ.
