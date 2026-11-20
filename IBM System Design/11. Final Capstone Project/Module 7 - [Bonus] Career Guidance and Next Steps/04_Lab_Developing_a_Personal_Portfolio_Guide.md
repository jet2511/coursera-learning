# Lab: Developing a Personal Portfolio - Guide & Implementation

> **Course**: Systems and Solutions Architect Capstone Project  
> **Module**: Module 7 - [Bonus] Career Guidance and Next Steps  
> **Lab**: Developing a Personal Portfolio (Estimated Duration: 15 minutes)  
> **Author**: Parikshit Jain

---

## 1. Mục tiêu thực hành (Learning Objectives)
1. Xây dựng một **Personal Architecture Portfolio** hoàn chỉnh để trưng bày năng lực Systems & Solutions Architect.
2. Tổ chức khoa học bộ **Architecture Artifacts** (ERD, DFD, Sequence Diagrams, OpenAPI, NFRs, Configuration Guides, PoCs).
3. Thiết lập bố cục trình bày theo chuẩn ngành trên các nền tảng trực tuyến (GitHub Pages, Notion, Google Sites, Webflow).
4. Xây dựng **3 đến 5 Case Studies** chuyên sâu tập trung vào kiến trúc hệ thống và kết quả kinh doanh.

---

## 2. Lựa chọn nền tảng & Bố cục khung (Structure Skeleton)

### 2.1. Nền tảng khuyến nghị
- **GitHub Pages / MkDocs / Astro / Docusaurus**: Tối ưu nhất cho Software/Systems Architect (hỗ trợ Markdown, Mermaid diagrams, nhúng code và liên kết trực tiếp repo).
- **Notion**: Triển khai cực nhanh, dễ chia sẻ, giao diện trực quan và quản lý database artifacts khoa học.
- **Google Sites / Webflow**: Dành cho giao diện phong cách website doanh nghiệp.

### 2.2. Khung điều hướng (Portfolio Skeleton)
1. **Home / Introduction**: Định vị vai trò, tóm tắt năng lực cốt lõi.
2. **Skills & Expertise**: Phân tầng rành mạch giữa *Systems* và *Solutions* Architecture.
3. **Architecture Artifacts Gallery**: Trưng bày 8–12 tài liệu/sơ đồ kiến trúc kèm giải thích.
4. **Project Case Studies**: 3–5 bài toán thực tế (*Problem $\to$ Architecture $\to$ Deliverables $\to$ Impact*).
5. **Prototypes & Repositories**: Liên kết mã nguồn, Terraform IaC, API demos.
6. **Certifications & Recognitions**: Chứng chỉ quốc tế (AWS, TOGAF, CKA,...).
7. **Contact Information**: Kênh kết nối chuyên nghiệp.

---

## 3. Ma trận kỹ năng: Systems vs. Solutions Architecture

| Nhóm kỹ năng | Systems Architecture (Hạ tầng, Mạng & Vận hành) | Solutions Architecture (Ứng dụng, Tích hợp & Dữ liệu) |
| :--- | :--- | :--- |
| **Hạ tầng & Cloud** | Multi-AZ Cloud VPC, Subnetting, Direct Connect, Hybrid Cloud | Cloud-Native microservices, Serverless, Container orchestration |
| **Bảo mật & Identity**| Zero Trust, IAM RBAC/ABAC, mTLS, AWS KMS Envelope Encryption | API Security, OAuth2/OIDC, JWT Validation, Data Masking |
| **Hệ thống & Vận hành**| Linux kernel, Virtualization, Docker, K8s cluster administration | Domain-Driven Design (DDD), Event-Driven Architecture (EDA) |
| **Giám sát & SRE** | Prometheus, Grafana, OpenTelemetry, Log aggregation, SLO/SLI | Distributed tracing, APM, Circuit Breaker, Fault tolerance |
| **BDR & Resiliency** | BCDR Runbooks, Automated cross-region backups, RPO/RTO | CQRS, Saga Pattern, Cache Aside (Redis), Message queues (Kafka) |
| **Mô hình hóa & API** | Network topology diagrams, Infrastructure-as-Code (Terraform) | High-Level Design (HLD), Low-Level Design (LLD), ERD, DFD, OpenAPI |

---

## 4. Danh mục Architecture Artifacts Gallery (Capstone Projects)

| # | Tên Artifact | Mô tả ngắn | Công nghệ / Tiêu chuẩn |
| :-: | :--- | :--- | :--- |
| 1 | **Context Diagram (Level 0)** | Tổng quan ranh giới hệ thống ngân hàng số và các thực thể ngoài (Khách hàng, Core Banking cũ, Cổng thanh toán quốc tế, Cơ quan quản lý). | C4 Model / Draw.io |
| 2 | **Data Flow Diagrams (DFD L1 & L2)** | Luồng xử lý giao dịch thanh toán và mở tài khoản trực tuyến (eKYC). | Gane-Sarson / DFD standards |
| 3 | **Entity-Relationship Diagram (ERD)** | Lược đồ cơ sở dữ liệu quan hệ chuẩn 3NF (Customer, Account, Transaction, Audit, Cards). | PostgreSQL / MySQL / dbdiagram.io |
| 4 | **Sequence Diagrams** | Luồng xác thực bảo mật đa yếu tố và điều phối giao dịch thanh toán tức thời. | UML 2.5 / PlantUML |
| 5 | **High-Level Architecture (HLA)** | Kiến trúc phân tầng (Presentation, API Gateway, Microservices, Event Bus, Data Layer, Core Banking). | AWS Multi-AZ Reference Architecture |
| 6 | **Low-Level Design (LLD)** | Thiết kế chi tiết module Payment Processing Service (Internal classes, connection pools, retry policies). | Java / Spring Boot / UML Class Diagram |
| 7 | **OpenAPI 3.0 Specifications** | Bộ đặc tả REST API cho Banking Gateway (Authentication, Accounts, Transfers, Balances). | OpenAPI 3.0 / Swagger UI |
| 8 | **Configuration Guides** | Hướng dẫn cấu hình môi trường Kubernetes, Service Mesh (Istio) và Helm charts. | Kubernetes / YAML / Linux |
| 9 | **NFR Specifications & SLA Matrix** | Định lượng chỉ số phi chức năng: Uptime 99.99%, P99 Latency < 200ms, RPO ≤ 15m, RTO ≤ 1h. | IEEE / TOGAF NFR Framework |
| 10 | **PoC Documentation & Test Plans** | Báo cáo kiểm thử hiệu năng k6, kiểm thử bảo mật OWASP, và kết quả diễn tập BDR Failover. | JMeter / k6 / OWASP ZAP |

---

## 5. Danh mục 3 Project Case Studies chuẩn

### Case Study 1: Modernizing Digital Banking Operations at a Retail Bank
- **Domain**: Fintech & Retail Banking.
- **Thách thức**: Hệ thống Core Banking cũ kỹ, nghẽn cổ chai khi số lượng người dùng tăng cao, thời gian xử lý giao dịch chậm chạp, không đáp ứng chuẩn mở rộng thanh toán tức thời.
- **Giải pháp**: Xây dựng kiến trúc Microservices phân tán trên AWS Multi-AZ kết hợp Event-Driven (Apache Kafka), tích hợp cơ chế Zero Trust và bảo vệ dữ liệu bằng KMS.
- **Kết quả**: Xử lý mượt mà **10,000+ TPS**, giảm độ trễ P99 từ **850ms xuống 180ms**, cam kết **RPO < 15 phút, RTO < 1 giờ**.

### Case Study 2: Enterprise API Gateway & Integration Platform
- **Domain**: Enterprise Integration & E-Commerce.
- **Thách thức**: Các hệ thống nội bộ phân mảnh, thiếu chuẩn bảo mật tập trung và không kiểm soát được tải truy cập từ các đối tác thứ ba.
- **Giải pháp**: Thiết kế cụm API Gateway tập trung (Kong/AWS API Gateway) với xác thực OAuth2/OIDC, áp dụng Rate Limiting động, Circuit Breaker và mTLS.
- **Kết quả**: Hỗ trợ hơn **50 triệu lượt gọi API/ngày**, bảo vệ hệ thống backend khỏi 100% các đợt bùng nổ lưu lượng bất thường.

### Case Study 3: Cloud Migration & Automated Disaster Recovery Platform
- **Domain**: Cloud Infrastructure & SRE.
- **Thách thức**: Toàn bộ dữ liệu nằm trên hạ tầng On-Premises có nguy cơ ngừng hoạt động cao khi gặp sự cố phần cứng, thiếu khả năng tự động phục hồi.
- **Giải pháp**: Thiết kế kiến trúc Hybrid Cloud sang AWS sử dụng Terraform IaC, thiết lập sao lưu dữ liệu tự động liên vùng và cơ chế chuyển đổi dự phòng nóng (Warm Standby).
- **Kết quả**: Đạt **99.99% Availability**, giảm chi phí vận hành TCO xuống **25%** và thời gian khôi phục hệ thống (RTO) từ 8 giờ xuống dưới 45 phút.

---

## 6. Bảng kiểm định chất lượng Portfolio (Validation Checklist)
- [x] Đầy đủ thông tin giới thiệu cá nhân, chức danh và định vị chuyên môn.
- [x] Phân chia rành mạch 2 cột kỹ năng: *Systems Architecture* vs *Solutions Architecture*.
- [x] Có thư viện 8–12 Architecture Artifacts trực quan kèm mô tả lý do thiết kế.
- [x] Tối thiểu 3 Case Studies chi tiết theo đúng cấu trúc chuẩn ngành.
- [x] Mục Prototypes & Code Repositories rõ ràng (Terraform, Microservices, OpenAPI).
- [x] Giao diện tối giản, chuyên nghiệp, responsive hoàn hảo trên máy tính và điện thoại.
