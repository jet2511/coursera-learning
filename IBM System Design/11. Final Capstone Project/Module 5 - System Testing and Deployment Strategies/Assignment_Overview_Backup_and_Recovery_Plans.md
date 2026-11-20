# Assignment Overview: Backup and Recovery Plans

- **Khóa học:** IBM System Design - Capstone Project
- **Module:** Module 5 - System Testing and Deployment Strategies
- **Chủ đề:** Backup and Recovery Plans for Retail Bank
- **Tác giả:** Parikshit Jain
- **Mục tiêu:** Thiết kế kế hoạch sao lưu (Backup) và phục hồi thảm họa (Disaster Recovery - DR) toàn diện, bảo vệ dữ liệu tài chính nhạy cảm, tối ưu hóa RTO/RPO và tuân thủ các quy định ngân hàng (PCI-DSS, FFIEC, GDPR, KYC/AML).

---

## 1. Tóm tắt các nhiệm vụ (Tasks)

| Task | Tên nhiệm vụ | Nội dung cốt lõi |
| :--- | :--- | :--- |
| **Task 1** | **Identify Critical Systems & Data Assets** | Lập danh mục và phân loại các hệ thống cốt lõi (Core Transaction DB, Loan Engine, Fraud Logs, Ledger, Configurations); đánh giá mức độ quan trọng (Tier 1/Tier 2) và tính nhạy cảm pháp lý. |
| **Task 2** | **Define Backup Frequency & Retention Policies** | Xác định tần suất sao lưu (Continuous WAL/Streaming, Hourly, Daily), thời gian lưu trữ (Retention) và chỉ số phục hồi mục tiêu (**RTO/RPO**) theo chuẩn PCI-DSS, FFIEC, GDPR. |
| **Task 3** | **Select Appropriate Backup Strategies** | Lựa chọn phương pháp sao lưu phù hợp (Full, Incremental, Differential, Continuous Point-in-Time Recovery - PITR) cho từng loại dữ liệu và workload cụ thể. |
| **Task 4** | **Draft Disaster Recovery (DR) Plan** | Soạn thảo kế hoạch ứng phó thảm họa: chiến lược chuyển đổi dự phòng (Active-Passive / Multi-Region Hot-Standby), các bước failover/failback và kiểm toán tuân thủ. |
| **Task 5** | **Define Backup Storage Architecture** | Thiết kế kiến trúc lưu trữ sao lưu đa tầng (Block, Object Storage S3/GCS, Glacier/WORM archival) tích hợp mã hóa (AES-256/KMS), versioning, immutability và IAM RBAC. |
| **Task 6** | **Create Recovery Workflow Diagram** | Xây dựng sơ đồ quy trình phục hồi trực quan: Phát hiện sự cố $\rightarrow$ Cảnh báo $\rightarrow$ Kích hoạt DR $\rightarrow$ Khôi phục dữ liệu $\rightarrow$ Xác thực toàn vẹn $\rightarrow$ Đánh giá sau sự cố. |
| **Task 7** | **Validate Backup & Recovery Plans** | Hoàn thành bảng checklist kiểm tra độ hoàn chỉnh: bảo đảm 100% tài sản dữ liệu được phân loại, RTO/RPO đạt chuẩn, mã hóa đầy đủ và sẵn sàng cho các cuộc diễn tập thảm họa (DR drills). |

---

## 2. Danh sách sản phẩm cần nộp (Deliverables)

1. **Critical Systems Inventory Table:** Bảng phân loại hệ thống & tài sản dữ liệu.
2. **Backup Frequency and Retention Policy Matrix:** Ma trận tần suất sao lưu, thời gian lưu trữ và mục tiêu RTO/RPO.
3. **Backup Strategy Mapping Table:** Bảng ánh xạ chiến lược backup (Full/Incremental/Differential/PITR).
4. **Draft Disaster Recovery Plan:** Tài liệu kế hoạch phục hồi thảm họa và quy trình failover.
5. **Backup Storage Architecture Summary:** Tài liệu kiến trúc lưu trữ và giải pháp bảo mật dữ liệu sao lưu.
6. **Recovery Workflow Diagram:** Sơ đồ quy trình failover và phục hồi hoạt động kinh doanh.
7. **Validation Checklist:** Bảng kiểm tra xác nhận tính đầy đủ, khả thi và tuân thủ pháp lý.
