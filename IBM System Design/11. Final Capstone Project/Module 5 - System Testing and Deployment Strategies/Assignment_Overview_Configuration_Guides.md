# Assignment Overview: Configuration Guides

- **Khóa học:** IBM System Design - Capstone Project
- **Module:** Module 5 - System Testing and Deployment Strategies
- **Chủ đề:** Configuration Guides for Retail Bank's Digital Core
- **Tác giả:** Parikshit Jain
- **Mục tiêu:** Xây dựng tài liệu hướng dẫn cấu hình chuẩn hóa, an toàn và có khả năng tái lập (reproducible) cho các thành phần cốt lõi của ABC Bank qua các môi trường Dev, Test và Production, đảm bảo tuân thủ các tiêu chuẩn PCI-DSS, FFIEC, GDPR, KYC/AML.

---

## 1. Tóm tắt các bước thực hiện (What You Will Do)

| Bước | Tên bước | Nội dung cốt lõi |
| :--- | :--- | :--- |
| **Step 1** | **Identify Solution Components** | Xác định và lập danh mục các thành phần giải pháp cần cấu hình: Databases (PostgreSQL/MySQL), API Gateway (Kong/Apigee), Load Balancer (Nginx/ALB), Auth Module (Keycloak/IAM), CI/CD (GitHub Actions), Logging/Monitoring (Prometheus/ELK). |
| **Step 2** | **Document Step-by-Step Instructions** | Viết hướng dẫn cấu hình chi tiết, tuần tự: câu lệnh cài đặt, biến môi trường (environment variables), tham số runtime, giá trị mặc định vs giá trị ghi đè, định dạng file và đường dẫn cấu hình. |
| **Step 3** | **Include Script Snippets & Screenshots** | Đưa ra bằng chứng cấu hình cụ thể: YAML (Kubernetes manifests), JSON (Gateway routes, policies), CLI commands (DB init, migration), và screenshots/minh họa. |
| **Step 4** | **Provide Environment-Specific Notes** | Phân định rõ ràng sự khác biệt giữa các môi trường: **Dev** (Debug mode, mock data, reduced security), **Test** (Integration endpoints, synthetic tests), **Prod** (Full encryption TLS 1.3/AES-256, HSM/KMS keys, rate limiting, audit logging). |
| **Step 5** | **Document Dependencies & Compatibility** | Lập bảng ma trận tương thích phiên bản (Version Compatibility Table), yêu cầu tài nguyên (CPU/RAM/Storage), plugins bắt buộc và cảnh báo xung đột (incompatibilities). |
| **Step 6** | **Validate Using Configuration Checklist** | Sử dụng bảng kiểm định để xác nhận tính tuần tự, khả thi trên môi trường sạch (clean environment), tuân thủ bảo mật và tính đầy đủ của tài liệu. |

---

## 2. Danh sách sản phẩm cần nộp (Expected Deliverables)

1. **Component Inventory Table:** Bảng danh mục thành phần hệ thống cần cấu hình.
2. **Configuration Instructions for 3 Components:** Hướng dẫn cấu hình chi tiết cho 3 thành phần tiêu biểu (ví dụ: PostgreSQL Core DB, Kong/Apigee API Gateway, Keycloak Identity Provider).
3. **Configuration Snippets (YAML / JSON / CLI):** Các đoạn mã cấu hình thực tế, có thể copy-paste và chạy được ngay.
4. **Environment-Specific Guidelines:** Bảng so sánh cấu hình qua 3 môi trường Dev, Test, Prod.
5. **Version Compatibility Table:** Bảng ma trận tương thích phiên bản và phụ thuộc hệ thống.
6. **Completed Validation Checklist:** Bảng kiểm tra xác nhận tài liệu cấu hình đạt chuẩn doanh nghiệp ngân hàng.
