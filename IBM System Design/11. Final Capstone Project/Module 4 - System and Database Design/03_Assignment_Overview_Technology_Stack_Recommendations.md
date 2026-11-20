# 03 - Assignment Overview: Technology Stack Recommendations

- **Thời lượng ước tính:** 2 phút
- **Tác giả:** Parikshit Jain
- **Mục tiêu:** Đánh giá và lựa chọn bộ công nghệ (Technology Stack) toàn diện cho quá trình chuyển đổi số Digital Core của Retail Bank. Cân bằng giữa hiệu năng (performance), khả năng mở rộng (scalability), bảo mật (security) và tuân thủ quy định tài chính ngân hàng (regulatory compliance).

---

## 1. Các nhiệm vụ chính (Tasks)

### Task 1: Define Architecture Layers (Xác định các tầng kiến trúc)
Xác định các tầng công nghệ cốt lõi cần thiết cho nền tảng ngân hàng bán lẻ:
- **Front-end:** Giao diện người dùng Web & Mobile.
- **Back-end:** Xử lý nghiệp vụ lõi, microservices.
- **Database:** Cơ sở dữ liệu giao dịch (OLTP), cache và tìm kiếm.
- **Integration / Messaging:** Tích hợp API, hàng đợi thông điệp, event-driven streaming.
- **Analytics / Reporting:** Phân tích dữ liệu lớn, báo cáo tài chính (OLAP/BI).
- **DevOps / CI/CD:** Tự động hóa build, test, deploy và quản trị container.
- **Security / Identity:** Xác thực, phân quyền (IAM), mã hóa, API Gateway bảo mật.
- **Cloud Infrastructure:** Hạ tầng điện toán đám mây (Cloud/Hybrid/Multi-cloud).

### Task 2: Compare Technology Options (So sánh các giải pháp công nghệ)
Đánh giá các ứng viên công nghệ tiềm năng cho từng tầng dựa trên các tiêu chí:
- Khả năng mở rộng (Scalability & High Availability).
- Khả năng tích hợp (Integration capabilities & Interoperability).
- Tuân thủ quy định ngành (Compliance: PCI-DSS, SOC 2, ISO 27001).
- Chi phí (TCO: License, vận hành, nhân sự).
- Hỗ trợ cộng đồng & hệ sinh thái doanh nghiệp (Ecosystem & Enterprise Support).

### Task 3: Recommend Final Stack (Đề xuất giải pháp cuối cùng)
- Chọn 1 công nghệ tối ưu nhất cho mỗi tầng kiến trúc.
- Cung cấp luận điểm biện minh rõ ràng về mặt kỹ thuật (Technical Justification) và nghiệp vụ (Business Justification) phù hợp với chiến lược chuyển đổi số của ngân hàng.

### Task 4: Validate Recommendations (Nghiệm thu khuyến nghị)
Sử dụng checklist để kiểm tra và xác nhận:
- Khả năng mở rộng chịu tải cao.
- Đáp ứng các chuẩn an toàn thông tin khắt khe của ngành ngân hàng: **PCI-DSS, SOC 2, GDPR/Quy định bảo vệ dữ liệu cá nhân**.
- Tương thích tốt với kiến trúc Microservices và Event-Driven.
- Khả năng hòa nhập với hệ thống công cụ sẵn có của doanh nghiệp.

---

## 2. Sản phẩm bàn giao (Deliverables)

1. **Technology Stack Recommendation Report (Word hoặc Excel):** Báo cáo khuyến nghị kiến trúc công nghệ kèm bảng định nghĩa các tầng (Layer Definition Table).
2. **Technology Comparison Table:** Bảng phân tích, so sánh các giải pháp công nghệ ứng viên cho từng tầng.
3. **Final Technology Stack Summary:** Bảng tóm tắt bộ công nghệ được chọn kèm lý do biện minh chi tiết.
4. **Completed Validation Checklist:** Bảng kiểm tra nghiệm thu xác nhận tính tuân thủ quy định, khả năng mở rộng và hiệu quả chi phí.
