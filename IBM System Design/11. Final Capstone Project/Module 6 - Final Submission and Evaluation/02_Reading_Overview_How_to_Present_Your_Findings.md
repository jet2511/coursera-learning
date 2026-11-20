# Reading: Overview - How to Present Your Findings

Tài liệu hướng dẫn phương pháp cấu trúc, trình bày và truyền đạt kết quả kiến trúc (Architectural Findings) trong đồ án hiện đại hóa hệ thống Ngân hàng Bán lẻ (Retail Bank Modernization Capstone).

---

## 1. Tầm quan trọng của kỹ năng thuyết trình kiến trúc (Presentation Matters)
Trong môi trường doanh nghiệp quy mô lớn và chịu nhiều quy chuẩn nghiêm ngặt (như Ngân hàng bán lẻ), một giải pháp kiến trúc không chỉ là tập hợp sơ đồ kỹ thuật mà là một **câu chuyện chiến lược (Strategic Narrative)** kết nối giữa:
- **Vấn đề nghiệp vụ (Business Problem)** và **Giải pháp kiến trúc đề xuất**.
- Các bằng chứng/lý giải đưa ra quyết định kỹ thuật (Architectural Reasoning).
- Giá trị mang lại, rủi ro đánh đổi (Trade-offs) và mức độ sẵn sàng triển khai.
- Giao tiếp hiệu quả với nhiều nhóm đối tượng: Ban điều hành (Executives), Kỹ thuật (Dev/DevOps), Bảo mật & Rủi ro (Security & Risk), Tuân thủ (Compliance), và Vận hành (Operations).

---

## 2. Nguyên tắc kể chuyện kiến trúc (Telling the Architecture Story)

1. **Khởi đầu bằng bối cảnh nghiệp vụ (Business Context):**
   - Nêu rõ các rào cản hiện tại: Hệ thống legacy xử lý chậm, quy trình thủ công gây nghẽn, rủi ro tuân thủ do dữ liệu phân mảnh.
   - Mục tiêu: Hiện đại hóa bằng nền tảng cloud-native, kiến trúc API-first, tự động hóa, tăng tính sẵn sàng và khả năng giám sát.

2. **Xác định mục tiêu & Phạm vi (Objectives & Scope):**
   - **Functional Objectives:** Luồng nghiệp vụ mới, cải tiến tích hợp hệ thống.
   - **Non-Functional Objectives (NFRs):** Khả năng mở rộng (Scalability), độ trễ (Latency thresholds), tính kiên cường (Resilience), kiểm soát an toàn bảo mật.
   - **Ràng buộc & Phụ thuộc:** Tuân thủ pháp lý tài chính, phụ thuộc bên thứ 3, hạ tầng cloud.

3. **Current-State $\rightarrow$ Target-State:**
   - Đối chiếu rõ các điểm nghẽn (Pain points) hiện tại với nâng cấp kiến trúc tương lai.

4. **Trình bày luồng hệ thống & Dữ liệu (System & Data Flows):**
   - Không đọc liệt kê các khối hình trên sơ đồ; hãy giải thích **cách dữ liệu di chuyển**, **hành trình khách hàng được tối ưu ra sao**, và **lý do lựa chọn pattern kiến trúc** tương ứng.

5. **Thiết kế CSDL & Quản trị dữ liệu (Database & Data Governance):**
   - Trình bày Conceptual / Logical ERD, giải thích tính toàn vẹn dữ liệu, chuẩn hóa (Normalization) để giảm thiểu dư thừa và hỗ trợ audit, báo cáo tuân thủ.

6. **Triển khai CI/CD, Cloud & Vận hành (Deployment & Operations):**
   - CI/CD workflow, cơ chế tự động rollback, hạ tầng cloud và khung giám sát (Observability framework).

7. **Bảo mật và Tuân thủ (Security by Design & Compliance):**
   - Mã hóa dữ liệu (in-transit / at-rest), MFA, API Security, IAM RBAC/ABAC, DLP, SIEM audit trail.
   - Đáp ứng chuẩn: PCI-DSS, FFIEC, ISO 27001, KYC/AML.

8. **Đưa ra các phát hiện chính & Đề xuất hành động (Findings & Actionable Recommendations):**
   - Số liệu hóa cải tiến (giảm X% thời gian xử lý, giảm tỷ lệ lỗi triển khai).
   - Đề xuất có tính khả thi, phân cấp ưu tiên rõ ràng (Prioritized, Feasible, Action-oriented).

---

## 3. Tiêu chuẩn trình bày Slide (Presentation Best Practices)
- **Quy tắc $6 \times 6$:** Tối đa 6 gạch đầu dòng mỗi slide, mỗi dòng không quá 6 từ.
- **Typography & Layout:** Font chữ to rõ ràng ($\ge 24\text{pt}$ cho body, $\ge 32\text{pt}$ cho heading); tránh các đoạn văn bản dài dòng.
- **Sơ đồ & Hình ảnh:** Nhúng trực tiếp sơ đồ độ phân giải cao vào slide kèm chú thích (caption); không dùng link trỏ ra ngoài.
- **Hiệu ứng:** Không lạm dụng animation; tập trung vào tính mạch lạc, rõ ràng và tác động nghiệp vụ.

---

## 4. Danh mục các mục bắt buộc trong bài thuyết trình (Sections of Presentation)

1. **Executive Summary**
2. **Introduction & Objectives**
3. **Project Management Artifacts:**
   - Project Charter
   - Stakeholder Register & Stakeholder Engagement Plan
   - Business Requirements Document (BRD)
   - Requirements Traceability Matrix (RTM)
   - Work Breakdown Structure (WBS) & Network Diagram
   - SWOT Analysis, Risk Register & Risk Matrix
4. **Process Model:**
   - Core Banking Process Flows: Customer Onboarding, Fund Transfer, Loan Application, Transaction Processing, Payment Authorization
5. **System Design:**
   - Data Flow Diagram (DFD Level 0 & Level 1)
   - Use Case Diagram & Sequence Diagram
   - Technology Stack Recommendations
   - System Architecture Diagram
   - Cloud Topology Diagram
   - Security Architecture Diagram
6. **Proof of Concept (PoC):**
   - PoC Objective and Scope
   - PoC Setup and Tools
   - Limitations and Recommendations
7. **Database Design:**
   - Conceptual ERD & Logical ERD
   - Data Dictionary
   - Normalization & Key Table Details
   - Data Migration Strategy
8. **Testing Strategy (TDD / BDD):**
   - Test Plan
   - TDD and BDD Test Cases
9. **CI/CD, Monitoring & Resilience:**
   - CI Workflow & CD Pipeline Diagram
   - Configuration Guides (Database, API Gateway, CI/CD)
   - Monitoring Framework & Cloud Components
   - Backup & Disaster Recovery Plan (BDR / RPO / RTO)
10. **Key Findings & Actionable Recommendations**
11. **Conclusion & Appendix**
