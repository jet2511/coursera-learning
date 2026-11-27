# Task 3: Justify Final Stack Selection (Summary & Rationale)

Bảng tóm tắt bộ công nghệ đề xuất cuối cùng cho dự án **Retail Bank Digital Core Transformation** kèm luận điểm giải trình kỹ thuật và giá trị kinh doanh.

---

## 1. Bảng tóm tắt bộ công nghệ được chọn (Final Technology Stack Summary)

| Tầng kiến trúc (Layer) | Công nghệ được chọn (Selected Technology) | Luận điểm giải trình kỹ thuật & nghiệp vụ (Justification) |
| :--- | :--- | :--- |
| **Front-End** | **React.js + React Native** | Giao diện hiện đại, tốc độ phản hồi dưới 1 giây; kiến trúc Micro-frontends cho phép các team Onboarding, Loan, Transfer phát triển và release tính năng độc lập; dùng chung thư viện UI Design System giữa Web và Mobile App. |
| **Back-End** | **Java Spring Boot (Microservices)** | Đảm bảo tính nhất quán giao dịch (ACID transactions) qua Spring Data / JPA; hỗ trợ thiết kế Domain-Driven Design (DDD) và Clean Architecture; khả năng mở rộng ngang linh hoạt theo từng dịch vụ riêng biệt. |
| **Database** | **Oracle DB (Core) + PostgreSQL (Services)** | Đảm bảo an toàn tuyệt đối cho số dư tài khoản và sổ cái giao dịch với Oracle; tối ưu hóa chi phí bản quyền và gia tăng độ linh hoạt lưu trữ cho các dịch vụ khách hàng với PostgreSQL. |
| **Integration** | **Apache Kafka + Kong API Gateway** | Truyền phát sự kiện bất đồng bộ thời gian thực (Event-Driven Architecture) với độ trễ thấp (<10ms); lưu vết audit trail bất biến phục vụ thanh tra tài chính; API Gateway quản lý xác thực token, rate limiting và bảo vệ chống tấn công DDoS. |
| **Analytics & BI** | **Microsoft Power BI** | Cho phép ban lãnh đạo và cán bộ rủi ro theo dõi dashboard nợ xấu, khối lượng giao dịch và tỷ lệ phê duyệt hồ sơ vay trực tiếp theo thời gian thực với cơ chế phân quyền bảo mật cấp dòng dữ liệu (Row-Level Security). |
| **DevOps & CI/CD** | **GitHub Actions + Docker + Kubernetes** | Tự động hóa quy trình DevSecOps khép kín; Kubernetes tự động nhân bản (auto-scaling) pod khi có lượng truy cập đột biến vào các ngày trả lương/khuyến mại; triển khai không gián đoạn dịch vụ với chiến lược Blue-Green / Canary. |
| **Security & IAM** | **Azure AD (Entra ID) + OAuth 2.0 / OIDC** | Chuẩn hóa đăng nhập một lần (SSO) và bảo mật 2 lớp (MFA/Biometrics); phân quyền RBAC minh bạch theo chuẩn kiểm toán SOC 2 và PCI-DSS; loại bỏ nguy cơ rò rỉ mật khẩu tĩnh. |
| **Cloud Infrastructure**| **AWS (Amazon Web Services)** | Triển khai mô hình Multi-AZ (Active-Active) đảm bảo cam kết mức độ dịch vụ SLA 99.99%; tích hợp sẵn các dịch vụ bảo mật FIPS 140-2 Level 3 (AWS CloudHSM) và tường lửa WAF chống gian lận. |

---

## 2. Lợi ích kinh doanh và kỹ thuật cốt lõi (Strategic Business Value)

1. **Rút ngắn thời gian ra mắt sản phẩm (Time-to-Market):**
   - Sự kết hợp giữa React Micro-frontends, Spring Boot Microservices và GitHub Actions CI/CD cho phép các nhóm sản phẩm (Squads) triển khai tính năng độc lập mà không cần chờ đợi toàn bộ hệ thống lớn cùng release.

2. **Khả năng phục hồi và sẵn sàng cao (High Availability & Resilience):**
   - Kiến trúc phân tán dựa trên Kubernetes kết hợp Event Streaming qua Kafka giúp hệ thống không có "Single Point of Failure" (điểm lỗi đơn lẻ). Nếu dịch vụ thông báo hoặc tích hợp ngoài gặp sự cố, luồng giao dịch cốt lõi vẫn hoạt động bình thường nhờ cơ chế hàng đợi bất đồng bộ.

3. **Tuân thủ quy chuẩn bảo mật tài chính ngân hàng (Regulatory Compliance):**
   - Đạt chuẩn **PCI-DSS Level 1** cho các luồng xử lý thẻ và thanh toán.
   - Đáp ứng chuẩn **SOC 2 Type II** về tính bảo mật, tính toàn vẹn xử lý và quyền riêng tư dữ liệu.
   - Mã hóa toàn bộ dữ liệu ở trạng thái lưu trữ (Encryption at Rest - AES-256) và trên đường truyền (Encryption in Transit - TLS 1.3).

4. **Tối ưu hóa tổng chi phí sở hữu (TCO Optimization):**
   - Sử dụng giải pháp mã nguồn mở doanh nghiệp (PostgreSQL, Kafka, Kubernetes, Linux containers) cho các tầng dịch vụ xung quanh giúp ngân hàng tiết kiệm hơn 40% chi phí bản quyền phần mềm so với việc mua trọn gói các giải pháp đóng gói độc quyền (proprietary monolithic).
