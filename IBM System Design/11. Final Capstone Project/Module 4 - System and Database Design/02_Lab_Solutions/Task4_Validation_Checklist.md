# Task 4: UML Diagrams Validation Checklist & Compliance Report

Bảng checklist đối soát chất lượng toàn diện của bộ biểu đồ hệ thống Retail Bank trước khi nộp đồ án Capstone.

---

## 1. Bảng Checklist kiểm thử chi tiết

| STT | Hạng mục kiểm tra | Tiêu chuẩn đánh giá | Kết quả (Status) | Ghi chú minh chứng (Evidence & Alignment) |
| :---: | :--- | :--- | :---: | :--- |
| **1** | **All key actors included** | Đầy đủ người dùng nội bộ, bên ngoài và hệ thống thứ 3 | **PASSED** | Đã bao gồm đủ 5 actors: `Customer`, `Teller/Loan Officer`, `Authentication Service`, `Credit Bureau`, `Payment Gateway`. |
| **2** | **Critical banking processes covered** | Bao phủ 3 quy trình cốt lõi và các chức năng bổ trợ | **PASSED** | Gồm đủ: Onboarding (eKYC), Login & Auth, Loan Management (thẩm định tín dụng), Funds Transfer, View Transaction History. |
| **3** | **Relationships & data flows correct** | Luồng dữ liệu và quan hệ UML thể hiện chính xác | **PASSED** | Thể hiện đúng hướng trao đổi thông tin ở Context Model; sử dụng đúng chuẩn quan hệ `<<include>>` (Auth, Credit Check) và `<<extend>>` (Notifications) ở Use Case Diagram. |
| **4** | **Sequence message order accuracy** | Trình tự thời gian thông điệp hợp lý, đầy đủ call & response | **PASSED** | Luồng 18 bước có đánh số rõ ràng, trải qua 4 giai đoạn: Xác thực -> Khởi tạo -> Kiểm tra OTP/2FA -> Hạch toán Core & Thanh toán Gateway. |
| **5** | **UML-compliant notation** | Ký hiệu đồ họa tuân thủ đúng chuẩn quốc tế OMG UML | **PASSED** | Sử dụng đúng Actor (hình người), System Boundary (hộp chữ nhật viền), Use Case (hình oval), Lifeline (đường nét đứt), Activation Bar (thanh kích hoạt chữ nhật đứng). |
| **6** | **File naming convention** | Tên tệp xuất ra đúng quy định của đề bài | **PASSED** | Chuẩn bị sẵn danh mục file: `System_Context_Model.png`, `Use_Case_Diagram_Retail_Bank.png`, `Sequence_Diagram_Retail_Bank.png`. |

---

## 2. Báo cáo đánh giá chất lượng (Quality Assessment Summary)

- **Tính toàn vẹn (Completeness):** 100% các yêu cầu từ bài toán chuyển đổi số của ngân hàng bán lẻ (Retail Bank Digital Transformation) được phản ánh vào các biểu đồ thiết kế.
- **Tính khả thi kỹ thuật (Technical Feasibility):** Các luồng tương tác giữa Core Banking và Payment Gateway / Credit Bureau phản ánh chính xác kiến trúc ngân hàng số thực tế (Microservices / Service-Oriented Architecture).
- **Tính chuẩn hóa (Standardization):** Tuân thủ tuyệt đối quy ước ký hiệu UML, giúp đội ngũ kỹ sư phát triển (Developers) và kiểm thử (QA) hiểu rõ trách nhiệm của từng subsystem mà không gây hiểu nhầm.

---

## 3. Tổng hợp danh mục tệp nộp bài (Final Submission Deliverables)

1. `System_Context_Model.png` (Task 1)
2. `Use_Case_Diagram_Retail_Bank.png` (Task 2)
3. `Sequence_Diagram_Retail_Bank.png` (Task 3)
4. `Task4_Validation_Checklist.md` (Task 4 - Bảng kiểm tra nghiệm thu)
