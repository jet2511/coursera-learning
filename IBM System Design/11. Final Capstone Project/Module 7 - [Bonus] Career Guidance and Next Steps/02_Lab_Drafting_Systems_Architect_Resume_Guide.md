# Lab: Drafting Systems Architect Resume - Overview & Deliverables Guide

> **Course**: Systems and Solutions Architect Capstone Project  
> **Module**: Module 7 - [Bonus] Career Guidance and Next Steps  
> **Lab**: Drafting Systems Architect Resume (Duration: 15 minutes)  
> **Author**: Parikshit Jain

---

## 1. Mục tiêu thực hành (Learning Objectives)
1. Xây dựng cấu trúc bản CV chuyên biệt cho vị trí **Systems Architect** và **Solutions Architect**.
2. Làm nổi bật các kỹ năng kiến trúc kỹ thuật, bộ deliverables thiết kế (artifacts), công cụ và kinh nghiệm thực chiến từ đồ án capstone.
3. Ánh xạ các kết quả đã làm theo chuẩn trách nhiệm nghề nghiệp của ngành kiến trúc phần mềm/hệ thống.
4. Hoàn thiện CV 1–2 trang chuẩn format **ATS-friendly**.

---

## 2. Phân loại kỹ năng: Systems vs. Solutions Architecture

| Chiều không gian | Systems Architecture (Hạ tầng, Nền tảng, Vận hành) | Solutions Architecture (Ứng dụng, Tích hợp, Nghiệp vụ) |
| :--- | :--- | :--- |
| **Trọng tâm cốt lõi** | Nền tảng hạ tầng, Cloud Networking, Bảo mật mạng & OS, Resiliency | Ứng dụng nghiệp vụ, Kiến trúc phần mềm, Tích hợp hệ thống, Data Models |
| **Phạm vi kỹ thuật** | - Cloud VPC, Subnets, Gateways, Route Tables<br>- IAM RBAC, OAuth2/OIDC, Zero Trust, mTLS<br>- OS, Linux/Unix, Containerization (Docker, K8s)<br>- Monitoring/Logging (Prometheus, Grafana, CloudWatch)<br>- BDR (RPO < 15m, RTO < 1h), Multi-AZ Failover | - API Design (REST, OpenAPI, gRPC, Event-Driven/Kafka)<br>- Microservices Patterns (CQRS, Saga, Circuit Breaker)<br>- Data Modeling (ERD, Relational vs NoSQL, Sharding)<br>- Data Flow (DFD Level 0-2), Sequence Diagrams<br>- NFR Alignment (Throughput, Latency, SLA 99.99%) |
| **Deliverables chính** | Cloud Network Topologies, Infrastructure as Code (Terraform), BDR Runbooks, IAM Policies | HLD/LLD, OpenAPI 3.0 Specs, Data Flow Diagrams, ERD Schemas, Architecture Decision Records (ADRs) |

---

## 3. Danh mục Architecture Deliverables từ Capstone Project
*(Dự án: Modernizing Digital Banking Operations at a Retail Bank)*

1. **High-Level Design (HLD) & Low-Level Design (LLD)**: Mô hình kiến trúc phân tầng Microservices trên Multi-AZ Cloud.
2. **Entity-Relationship Diagrams (ERD)**: Mô hình dữ liệu quan hệ và NoSQL chuẩn hóa (3NF) cho Customer, Account, Transaction, Audit Logs.
3. **Data Flow Diagrams (DFD)**: Luồng dữ liệu Context Level 0 và Functional Level 1/2 cho quy trình mở tài khoản và xử lý giao dịch thời gian thực.
4. **Sequence & Use Case Diagrams**: Đặc tả luồng tương tác bảo mật end-to-end, xác thực biometric và authorization qua API Gateway.
5. **API Specifications**: Đặc tả OpenAPI 3.0 (Swagger) cho Core Banking APIs, mTLS và Rate Limiting.
6. **Non-Functional Requirements (NFRs)**: Định lượng chuẩn SLA (99.99% Availability, P99 Latency < 200ms, RPO ≤ 15 phút, RTO ≤ 1 giờ).
7. **Security & Zero Trust Architecture**: RBAC/ABAC matrix, Data-at-Rest (AES-256) & Data-in-Transit (TLS 1.3), HSM key management.
8. **CI/CD & BDR Automation**: GitOps pipeline, Blue-Green zero-downtime deployment, automated cross-region snapshot replication.

---

## 4. Công thức viết Bullet Points kiến trúc (Architecture Action Formula)

$$\text{Action Verb} + \text{Task / Component} + \text{Tools / Tech Stack} + \text{Architectural Outcome / NFR}$$

### Ví dụ áp dụng:
- **Scalability**: *"**Architected** an event-driven transaction processing pipeline **using** Apache Kafka and AWS ECS, **achieving** 10,000+ TPS and reducing P99 latency by 35%."*
- **Security & Compliance**: *"**Designed** an end-to-end Zero Trust security model **using** AWS API Gateway, OAuth2/OIDC, and KMS AES-256 encryption, **ensuring** full PCI-DSS and SOC 2 regulatory compliance."*
- **Resilience & BDR**: *"**Engineered** automated backup and disaster recovery plans across Multi-AZ cloud environments, **guaranteeing** RPO < 15 minutes and RTO < 1 hour during simulated regional failovers."*
- **API & Integration**: *"**Authored** comprehensive OpenAPI 3.0 specifications and integration patterns for retail banking APIs, **accelerating** partner onboarding velocity by 50%."*

---

## 5. Danh mục kiểm tra (Architect Resume Checklist)
- [x] Cân đối cả kỹ năng **Systems Architecture** lẫn **Solutions Architecture**.
- [x] Làm nổi bật danh mục các artifacts kiến trúc thực tế (ERD, DFD, HLD, OpenAPI, NFR).
- [x] Sử dụng động từ hành động mạnh: *Architected, Designed, Engineered, Formulated, Streamlined, Integrated*.
- [x] Lượng hóa kết quả (Quantitative Metrics): TPS, Latency, RPO/RTO, Uptime %, TCO reduction.
- [x] Bố cục 1–2 trang, sạch sẽ, chuẩn ATS (không lồng bảng lồng nhau, đồ họa phức tạp).
