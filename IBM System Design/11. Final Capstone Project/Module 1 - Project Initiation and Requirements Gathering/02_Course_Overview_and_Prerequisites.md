# Course Overview: Systems & Solutions Architect Capstone Project

## 1. Mục tiêu và Vai trò
- **Bối cảnh thực chiến:** Đóng vai trò là **Systems & Solutions Architect** cho một ngân hàng bán lẻ (**Retail Bank**), chuyển đổi hệ thống Legacy sang nền tảng đám mây (**Cloud-driven platform**) bảo mật, khả năng mở rộng cao và tuân thủ các quy định tài chính.
- **Phương pháp tiếp cận:** Enterprise Design Thinking, căn chỉnh chuẩn tuân thủ (compliance alignment), quản trị rủi ro và giao tiếp với các bên liên quan (stakeholders).
- **Thời lượng dự kiến:** Khoảng **18 giờ học** qua 6 modules chính + 1 module bonus sự nghiệp.

---

## 2. Bản đồ công cụ & phần mềm sử dụng (Tools & Tech Stack)
Khóa học yêu cầu sử dụng các công cụ (bản free/trial):
- **Văn phòng & Tài liệu:** Microsoft Word, Excel, PowerPoint.
- **Mô hình hóa kiến trúc & sơ đồ:** Draw.io, Lucidchart (UML, ERD, Process Flows, System Blueprints).
- **Cloud & Containerization:** Docker, Kubernetes, IBM Cloud Container Registry / AWS ECR.
- **Bảo mật & Mã hóa:** BitLocker, Network Security (VPNs, Network Segmentation).
- **Cơ sở dữ liệu:** MySQL (Thiết kế Schema 3NF, SQL DDL scripts, Data Migration).
- **CI/CD & DevOps:** Jenkins, CI/CD Pipeline Configuration.
- **Code & Triển khai:** Visual Studio Code (VS Code).

---

## 3. Lộ trình phân rã chi tiết từng Module & Deliverables

### Module 1: Project Initiation and Requirements Gathering
- **Mục tiêu:** Định hình kiến trúc từ giai đoạn khởi tạo, thiết lập sự đồng thuận giữa kinh doanh, kỹ thuật và tuân thủ pháp lý.
- **Deliverables:**
  - Project Charter (Hiến chương dự án), Stakeholder Mapping & Stakeholder Register.
  - Chiến lược tương tác bên liên quan (Stakeholder Engagement Plan).
  - Business Requirements Document (BRD), Software Requirements Specifications (SRS).
  - Thu thập và phân loại yêu cầu: Functional (FRs) vs Non-Functional (NFRs).
  - Requirements Traceability Matrix (RTM) ban đầu.

### Module 2: Project Planning and Process Modeling
- **Mục tiêu:** Chuyển đổi yêu cầu kinh doanh cấp cao thành các thành phần kiến trúc cụ thể và mô hình hóa luồng dữ liệu/quy trình.
- **Deliverables:**
  - Hoàn thiện RTM và Risk Register (định lượng rủi ro gian lận, gián đoạn, phạt quy định).
  - Phân tích SWOT (Strengths, Weaknesses, Opportunities, Threats).
  - Sơ đồ UML (Use Case, Activity, Sequence) và Flowcharts mô tả end-to-end data/logic flow.

### Module 3: Enterprise Architecture and Cloud Setup
- **Mục tiêu:** Thiết kế hạ tầng cloud-native có khả năng mở rộng, an toàn và đạt chuẩn audit.
- **Deliverables:**
  - Mô hình triển khai Microservices trên Docker / Kubernetes / IBM Cloud / AWS.
  - Cấu hình Container Registry an toàn.
  - Bản thiết kế EDA (Event-Driven Architecture) với cơ chế cảnh báo rủi ro thời gian thực (real-time risk mitigation).
  - Capacity Planning: Dự toán năng lực tính toán (Compute), lưu trữ (Storage), băng thông (Bandwidth), và bảng kiểm kê hạ tầng (Infrastructure Inventory).
  - Audit trails và regulatory reporting templates.

### Module 4: System and Database Design
- **Mục tiêu:** Thiết kế chi tiết thành phần hệ thống, cơ sở dữ liệu và bảo mật dữ liệu.
- **Deliverables:**
  - Component Architecture Diagrams & UML Component/Deployment models.
  - Ma trận lựa chọn giải pháp (Components Selection Matrix) cho từng tầng kiến trúc.
  - Báo cáo PoC (Proof of Concept) kiểm chứng tích hợp API bên thứ ba.
  - Thiết kế ERD (Conceptual & Logical) chuẩn hóa đến 3NF và sinh tập lệnh SQL DDL scripts.
  - Security Architecture Diagram (phân đoạn mạng, VPN, mã hóa lưu trữ/truyền dẫn).

### Module 5: System Testing and Deployment Strategies
- **Mục tiêu:** Xác thực giải pháp qua chiến lược kiểm thử, tự động hóa phát hành và duy trì tính liên tục của doanh nghiệp.
- **Deliverables:**
  - Test Plans & đối soát qua RTM, áp dụng phương pháp TDD / BDD.
  - Tài liệu cấu hình triển khai và đặc tả API (Configuration & API Documentation).
  - Chiến lược sao lưu và phục hồi thảm họa (Backup & Disaster Recovery Strategy - RPO/RTO).
  - Thiết kế CI/CD Pipelines (Jenkins), khung giám sát (Monitoring) và kế hoạch xử lý sự cố (Incident Response Plan).

### Module 6: Final Submission and Evaluation
- **Mục tiêu:** Đóng gói toàn bộ giải pháp kiến trúc tổng thể thành hồ sơ Portfolio sẵn sàng bàn giao/triển khai.
- **Deliverables:**
  - Bộ hồ sơ hoàn chỉnh gồm: System Blueprint, UML Diagrams, ERDs, Data Flowcharts, Cloud Topology, CI/CD, Monitoring Frameworks.
  - Đánh giá Capstone cuối khóa.

### Module 7 [Bonus]: Career Guidance and Next Steps
- **Mục tiêu:** Chuẩn bị hành trang sự nghiệp cho vị trí Systems & Solutions Architect.
- **Deliverables:**
  - Xây dựng Resume & Cover Letter chuyên biệt cho Kiến trúc sư hệ thống.
  - Luyện tập bộ câu hỏi phỏng vấn tình huống kiến trúc thực tế.
