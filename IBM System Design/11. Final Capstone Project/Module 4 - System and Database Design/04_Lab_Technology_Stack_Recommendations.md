# 04 - Lab Guide: Technology Stack Recommendations

- **Thời lượng ước tính:** 30 phút
- **Tác giả:** Parikshit Jain
- **Vai trò:** Systems and Solutions Architect
- **Bối cảnh (Scenario):** Đề xuất bộ công nghệ (Technology Stack) toàn diện cho quá trình chuyển đổi số Digital Core của Retail Bank. Hệ thống phải hỗ trợ hợp nhất: Onboarding, Loan Management, và Transaction Processing, đòi hỏi khả năng phân tích thời gian thực (real-time analytics), bảo mật API, độ sẵn sàng cao (High Availability), và tuân thủ các chuẩn ngân hàng quốc tế: **PCI-DSS, SOC 2**.

---

## 1. Công cụ & Tài liệu mẫu
- **Công cụ:** Google Docs, Google Sheets (hoặc Microsoft Word/Excel).
- **Template tham chiếu:** `Template-Technology stack recommendations.docx / .pdf`.

---

## 2. Chi tiết 4 nhiệm vụ (Tasks to be performed)

### Task 1: Identify the Key Architecture Layers
Xác định 8 tầng công nghệ nòng cốt, chức năng nghiệp vụ, các công nghệ ứng viên, lựa chọn khuyến nghị và lý do biện minh (Front-End, Back-End, Database, Integration/Middleware, Analytics/BI, DevOps & CI/CD, Security & IAM, Cloud/Hosting).

### Task 2: Evaluate Technology Options
So sánh đối đầu từ 2 đến 3 công nghệ ứng viên cho mỗi tầng dựa trên 5 tiêu chí:
1. **Scalability:** Khả năng mở rộng ngang/dọc, xử lý tải đột biến.
2. **Integration Compatibility:** Khả năng tương thích microservices, API REST/gRPC.
3. **Regulatory Compliance:** Khả năng đáp ứng chuẩn PCI-DSS, SOC 2, mã hóa dữ liệu.
4. **Ease of Maintenance:** Tính ổn định, hệ sinh thái, độ sẵn sàng nhân lực.
5. **Cost Efficiency:** Chi phí bản quyền, hạ tầng và tổng chi phí sở hữu (TCO).

### Task 3: Justify Final Stack Selection
Tổng hợp và đưa ra bảng tóm tắt cấu hình công nghệ cuối cùng kèm luận điểm thuyết phục ban lãnh đạo ngân hàng và kiểm toán kỹ thuật.

### Task 4: Validation Checklist
Kiểm tra nghiệm thu bộ công nghệ dựa trên 6 tiêu chí:
- An toàn & tuân thủ quy định ngành ngân hàng.
- Khả năng mở rộng ngang và dọc.
- Tích hợp linh hoạt qua API và Microservices.
- Hỗ trợ mạnh mẽ từ hãng (vendor support) và cộng đồng.
- Tương thích với hệ sinh thái công cụ hiện hữu.
- Tối ưu hóa giữa chi phí và hiệu năng.
