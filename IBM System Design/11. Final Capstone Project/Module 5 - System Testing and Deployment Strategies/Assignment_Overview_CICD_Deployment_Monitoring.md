# Assignment Overview: CI/CD Deployment and Monitoring Plan

- **Khóa học:** IBM System Design - Capstone Project
- **Module:** Module 5 - System Testing and Deployment Strategies
- **Chủ đề:** CI/CD Deployment and Monitoring Plan for Retail Bank
- **Tác giả:** Parikshit Jain
- **Mục tiêu:** Thiết kế pipeline CI/CD chuẩn ngân hàng bảo mật cao, chiến lược rủi ro/rollback tự động và kế hoạch giám sát hệ thống (Monitoring, Alerting, Escalation, Post-mortem) cho hệ thống Cloud-native Retail Bank.

---

## 1. Tóm tắt các nhiệm vụ (Tasks)

| Task | Tên nhiệm vụ | Nội dung cốt lõi |
| :--- | :--- | :--- |
| **Task 1** | **Design a CI/CD Pipeline** | Xây dựng sơ đồ quy trình CI/CD hoàn chỉnh từ code commit đến production: gồm các security gates (SAST/DAST/SCA), kiểm thử tự động, approval gates, chiến lược rollback (Blue-Green / Canary) và phân quyền vai trò (Dev, SecOps, Release Manager). |
| **Task 2** | **Define Deployment Risk Strategy** | Phân tích các rủi ro triển khai tài chính: lỗi hệ thống, sai lệch cấu hình/secrets, không tương thích API breaking changes; xác định rõ Trigger nhận diện, biện pháp giảm thiểu và kế hoạch rollback tự động. |
| **Task 3** | **Develop a System Monitoring Plan** | Xây dựng kế hoạch giám sát toàn diện: xác định KPIs kỹ thuật & nghiệp vụ (Golden Signals, TPS, tỷ lệ lỗi giao dịch), ngưỡng cảnh báo (Alert thresholds), kênh thông báo, quy trình leo thang sự cố (Escalation) và quy trình mổ xẻ sự cố (Post-mortem). |
| **Task 4** | **Validate Readiness Checklist** | Hoàn thiện bảng checklist kiểm tra độ sẵn sàng trước go-live: xác nhận đầy đủ các giai đoạn pipeline, chốt bảo mật, phân quyền phê duyệt, cơ chế rollback, giám sát KPI và tuân thủ quy định ngân hàng. |

---

## 2. Danh sách sản phẩm cần nộp (Deliverables)

1. **CI/CD Pipeline Diagram & Specification:** Sơ đồ quy trình CI/CD tích hợp đầy đủ security gates, approvals và rollback.
2. **Deployment Risk Strategy Table:** Bảng chi tiết rủi ro triển khai (Risks, Triggers, Mitigations, Rollback plans).
3. **System Monitoring Plan:** Kế hoạch giám sát hệ thống (KPIs, Alert Thresholds, Notification Channels).
4. **Escalation and Post-Mortem Workflow:** Quy trình điều phối xử lý sự cố và báo cáo sau sự cố (RCA).
5. **Final Validation Checklist:** Bảng kiểm tra xác nhận tính sẵn sàng toàn diện trước khi triển khai sản xuất.
