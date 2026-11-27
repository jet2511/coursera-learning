# LAB DELIVERABLE: Project Charter, Stakeholder Register & Engagement Plan
**Dự án:** Core Digital Transformation for Retail Banking  
**Vai trò:** Systems and Solutions Architect  
**Chuẩn áp dụng:** PMI Standards, TOGAF, KYC, AML, PCI-DSS, GDPR  

---

# PHẦN 1: PROJECT CHARTER (Hiến chương dự án)

### 1. Thông tin chung
- **Project Title:** Core Digital Transformation for Retail Banking
- **Date:** 18/11/2026
- **Project Sponsor:** Chief Executive Officer (CEO) / Board of Directors
- **Project Lead:** Systems and Solutions Architect Lead

### 2. Project Description (Mô tả dự án)
Dự án chuyển đổi toàn diện hệ thống công nghệ thông tin lõi (Core Banking & Operational IT) của ngân hàng bán lẻ quy mô vừa từ kiến trúc Legacy nguyên khối, dữ liệu phân mảnh (siloed databases) và xử lý theo lô (batch processing) sang nền tảng **Cloud-Native**, kiến trúc **Microservices**, **Containerization** và xử lý dữ liệu thời gian thực (**Real-time Event-Driven Architecture**).

### 3. Problem Statement & Opportunity (Bài toán & Cơ hội)
- **Hiện trạng (As-is):**
  - Hệ thống Legacy phân mảnh giữa các nghiệp vụ: Customer Onboarding, Transaction Processing và Loan Servicing.
  - Xử lý dữ liệu dạng batch, thiếu khả năng quan sát dữ liệu real-time.
  - Nguy cơ vi phạm quy chuẩn tuân thủ và bảo mật rất cao (KYC, AML, PCI-DSS, GDPR).
  - Vận hành chậm, sai lệch dữ liệu, thời gian phát hành tính năng mới kéo dài.
- **Tương lai (To-be):**
  - Kiến trúc Cloud-Native thống nhất kết nối qua RESTful/gRPC APIs chuẩn hóa.
  - Pipeline dữ liệu real-time kết hợp Centralized Data Warehouse / Lakehouse.
  - Cảnh báo thời gian thực phát hiện gian lận (Fraud Detection) và hành vi bất thường.
  - Cơ chế kiểm toán toàn diện (Auditability), mã hóa đa tầng (Encryption at rest/in transit), và kiểm soát truy cập dựa trên vai trò (RBAC).

### 4. Objectives (Mục tiêu dự án)
1. **Hiện đại hóa kiến trúc:** Thay thế/tái cấu trúc hệ thống Legacy sang kiến trúc Cloud-Native Microservices đạt SLA Availability ≥ 99.99%.
2. **Xử lý thời gian thực:** Giảm độ trễ giao dịch và đồng bộ dữ liệu từ hàng giờ (batch) xuống dưới 1 giây (sub-second real-time).
3. **Tuân thủ quy chế pháp lý:** Đạt 100% tuân thủ các tiêu chuẩn KYC, AML, PCI-DSS và GDPR ngay trong giai đoạn thiết kế kiến trúc.
4. **Tối ưu vận hành & Time-to-Market:** Rút ngắn chu kỳ phát hành tính năng/dịch vụ từ vài tháng xuống chu kỳ Agile 2 tuần thông qua CI/CD tự động hóa.

### 5. Success Criteria (Tiêu chí thành công)
- Triển khai thành công nền tảng Core mới không làm gián đoạn các dịch vụ ngân hàng hiện hữu.
- 0 lỗi vi phạm tuân thủ nghiêm trọng trong các đợt kiểm toán bảo mật và pháp lý độc lập.
- Thời gian phê duyệt onboarding và xử lý hồ sơ vay giảm tối thiểu 60%.
- Giảm chi phí bảo trì hạ tầng Legacy hàng năm ít nhất 30%.

### 6. High-level Requirements (Yêu cầu cấp cao)
- **Functional:** Hỗ trợ quy trình mở tài khoản eKYC tự động, xử lý giao dịch thanh toán real-time, quản lý giải ngân và thu nợ vay tự động, hệ thống cảnh báo gian lận Event-driven.
- **Non-Functional:** Khả năng mở rộng ngang (Horizontal Scalability), chịu lỗi phân tán (Fault Tolerance), mã hóa chuẩn AES-256 (Data at Rest) và TLS 1.3 (Data in Transit), quản lý định danh RBAC/MFA.

### 7. Key Stakeholders and Roles
- **Executive Sponsor:** CEO & Board of Directors (Cấp ngân sách, chỉ đạo chiến lược).
- **Business Owners:** Head of Retail Banking, Head of Lending, Head of Operations.
- **Risk & Compliance:** Chief Risk Officer (CRO), Chief Compliance Officer (CCO), Data Protection Officer (DPO).
- **Technical Leaders:** Chief Information Officer (CIO), Chief Information Security Officer (CISO), Enterprise/Solutions Architect, DevOps Lead.
- **End Users:** Nhân viên giao dịch chi nhánh, Chuyên viên tín dụng, Khách hàng cá nhân.

### 8. Scope (Phạm vi dự án)
- **Trong phạm vi (In-Scope):**
  - Thiết kế kiến trúc tổng thể To-be (Microservices, Containerization, EDA).
  - Tái cấu trúc 3 phân hệ nghiệp vụ chính: Onboarding (eKYC), Transaction Processing, Loan Servicing.
  - Xây dựng Data Layer tập trung, Pipeline streaming real-time và hệ sinh thái API Gateway.
  - Thiết lập hạ tầng bảo mật, CI/CD pipeline, logging, monitoring và quy trình Backup/Disaster Recovery.
- **Ngoài phạm vi (Out-of-Scope):**
  - Mua sắm hoặc thay thế thiết bị phần cứng tại các điểm ATM/POS vật lý (chỉ hỗ trợ giao thức kết nối API).
  - Nghiệp vụ khối ngân hàng đầu tư (Investment Banking) và khối khách hàng doanh nghiệp lớn (Corporate Banking).

### 9. Deliverables (Sản phẩm bàn giao)
- Project Charter, Stakeholder Register & Engagement Plan.
- BRD, SRS, Use Case Diagrams, Requirements Traceability Matrix (RTM).
- Kiến trúc quy trình (Process Flowcharts, UML Sequence & Activity diagrams).
- Bản thiết kế kiến trúc EDA, Cloud Topology, Data Flow Diagram và Capacity Planning Sheet.
- ERD (Conceptual/Logical/3NF), Data Dictionary và tập lệnh SQL DDL scripts.
- Test Plans (TDD/BDD Gherkin), Pipeline CI/CD, Kế hoạch Backup & DR, và Final Portfolio Presentation.

### 10. Assumptions & Constraints (Giả định & Ràng buộc)
- **Assumptions:** Ban lãnh đạo cam kết nguồn lực và ngân sách xuyên suốt; cơ quan quản lý không thay đổi đột ngột chính sách pháp lý tiền tệ trong thời gian triển khai.
- **Constraints:** Ràng buộc bảo mật dữ liệu ngân hàng khắt khe (chỉ sử dụng Cloud đạt chuẩn hoặc Hybrid Cloud tại chỗ); thời gian gián đoạn chuyển đổi dữ liệu (downtime cut-over) không vượt quá 2 giờ ban đêm.

### 11. High-level Risks (Rủi ro chính)
- Rủi ro sai lệch dữ liệu lịch sử trong quá trình di chuyển (Data Migration risk).
- Sự phản kháng thay đổi từ nhân viên chi nhánh quen quy trình thủ công cũ (Change Resistance).
- Nguy cơ lỗ hổng bảo mật trong quá trình mở API kết nối hệ thống.
- Chậm tiến độ do các bước phê duyệt từ cơ quan tuân thủ / thanh tra ngân hàng.

### 12. Milestones & Budget & Approval
- **Milestones:**
  - *M1 (Tháng 1-2):* Hoàn thành Khảo sát, Charter, BRD/SRS & RTM.
  - *M2 (Tháng 3-4):* Hoàn thành Thiết kế kiến trúc (EDA, Cloud Setup, ERD 3NF, Security Blueprint).
  - *M3 (Tháng 5-8):* Xây dựng Core Microservices, Data Pipeline & PoC Verification.
  - *M4 (Tháng 9-10):* Tích hợp CI/CD, Kiểm thử toàn diện (Testing) & Kế hoạch DR.
  - *M5 (Tháng 11-12):* Pilot thử nghiệm, Di chuyển dữ liệu và Go-Live chính thức.
- **Budget:** Ước tính sơ bộ thuộc nhóm dự án chiến lược trung hạn của ngân hàng.
- **Approval:** Được phê duyệt bởi CEO, CIO, CISO và Head of Retail Banking.

---

# PHẦN 2: STAKEHOLDER REGISTER (Sổ đăng ký các bên liên quan)

| Stakeholder / Group | Role | Attitude | Interests | Impact | Influence | Communication Preferences | Location / Availability | Success Criteria | Work Hours |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Chief Executive Officer (CEO)** | Executive Sponsor | Rất tích cực | ROI, năng lực cạnh tranh số, nâng cao định giá ngân hàng | High | High | Báo cáo tóm tắt hàng tháng (Executive Summary), Dashboard trực quan | Hội sở chính (HQ) / Theo lịch hẹn trước | Đúng tiến độ, trong ngân sách, tăng trưởng khách hàng số | 08:00 - 17:00 |
| **Head of Retail Banking** | Business Owner (Nghiệp vụ Bán lẻ) | Tích cực | Trải nghiệm khách hàng mượt mà, thời gian mở tài khoản và cấp vay nhanh | High | High | Họp giao ban định kỳ 2 tuần, demo tính năng | Hội sở chính / Sẵn sàng cao | Giảm 60% thời gian phục vụ, tăng NPS (Net Promoter Score) | 08:30 - 17:30 |
| **Chief Compliance Officer (CCO)** | Regulatory & Compliance Lead | Thận trọng | Tuân thủ tuyệt đối chuẩn KYC, AML, báo cáo định kỳ cho Ngân hàng Trung ương | High | High | Văn bản chính thức, tài liệu đặc tả tuân thủ, họp thẩm định kỹ thuật | HQ / Tham gia các trạm kiểm soát cố định | 0 lỗi vi phạm quy định, audit trail đầy đủ | 08:30 - 17:00 |
| **Chief Information Security Officer (CISO)** | Security Lead | Thận trọng / Nghiêm ngặt | Bảo mật dữ liệu khách hàng, mã hóa, PCI-DSS, ngăn ngừa tấn công mạng | High | High | Báo cáo kiến trúc bảo mật (Threat Modeling), kết quả Pentest | HQ / Sẵn sàng cao cho review kiến trúc | Zero data breach, vượt qua bài kiểm toán PCI-DSS | 09:00 - 18:00 |
| **Legacy Systems Operations Team** | Kỹ sư vận hành hệ thống cũ | Lo ngại / Thận trọng | Ổn định vận hành hàng ngày, tương thích hạ tầng, tránh mất việc làm | Medium | Medium | Workshop kỹ thuật, tài liệu đào tạo chuyển giao, họp kỹ thuật hàng tuần | Data Center / Onsite | Không bị gián đoạn ca trực, được đào tạo công nghệ Cloud mới | 24/7 (Theo ca) |
| **Branch Managers & Tellers** | Người dùng nội bộ (End Users) | Hơi e ngại thay đổi | Phần mềm dễ thao tác, không bị giật lag, giảm nhập liệu thủ công | High | Low | Khảo sát nhu cầu, video hướng dẫn, các buổi đào tạo thực hành | Hệ thống mạng lưới chi nhánh | Giao diện thân thiện, xử lý hồ sơ nhanh, giảm áp lực quầy | 08:00 - 17:00 |
| **Customer Experience / End Customers** | Khách hàng cuối | Mong đợi cao | Dịch vụ 24/7 không gián đoạn, an toàn tiền gửi, giao dịch tức thì | High | Low | Thông báo qua Mobile App / Email / SMS | Phân tán trên toàn quốc | Ứng dụng ngân hàng số mượt mà, xác thực sinh trắc học nhanh | 24/7 |

---

# PHẦN 3: STAKEHOLDER ENGAGEMENT PLAN (Theo thang đo PMI)

### Quy ước thang đo cam kết PMI:
- **U (Unaware):** Chưa biết/chưa rõ về dự án.
- **R (Resistant):** E ngại, phản kháng hoặc chống đối thay đổi.
- **N (Neutral):** Đã biết nhưng trung lập, không ủng hộ cũng không phản đối.
- **S (Supportive):** Ủng hộ và tạo điều kiện cho dự án.
- **L (Leading):** Tích cực lãnh đạo, dẫn dắt và thúc đẩy dự án thành công.
- **Ký hiệu ma trận:** `C` = Mức độ cam kết hiện tại (Current), `D` = Mức độ cam kết mong muốn (Desired).

### Ma trận đánh giá và Kế hoạch gắn kết (Engagement Matrix & Action Plan)

| Stakeholder Name / Group | Current (C) | Desired (D) | Ma trận PMI (U / R / N / S / L) | Chiến lược gắn kết & Kế hoạch hành động cụ thể (Engagement Strategies) |
| :--- | :---: | :---: | :---: | :--- |
| **CEO / Board of Directors** | S | L | `[U] [R] [N] [C] [D]` | - Duy trì báo cáo tiến độ KPI định kỳ hàng tháng.<br>- Cung cấp Executive Dashboard đo lường lợi ích kinh doanh và ROI.<br>- Mời tham gia chủ trì các lễ phát động và các cột mốc Go-Live quan trọng. |
| **Head of Retail Banking** | S | L | `[U] [R] [N] [C] [D]` | - Tham gia trực tiếp Product Steering Committee.<br>- Đồng phê duyệt BRD/SRS và nghiệm thu các phiên bản demo Sprint để đảm bảo đúng nhu cầu kinh doanh. |
| **Chief Compliance Officer (CCO)** | N | S | `[U] [R] [C] [D] [ ]` | - Thiết lập trạm kiểm soát tuân thủ (Compliance Checkpoint) trước mỗi giai đoạn kiến trúc.<br>- Mời chuyên gia pháp chế tham gia thẩm định luồng eKYC/AML và báo cáo kiểm toán bảo mật tự động. |
| **Chief Information Security Officer (CISO)** | N | S | `[U] [R] [C] [D] [ ]` | - Thực hiện Threat Modeling và rà soát kiến trúc an ninh mạng ngay từ giai đoạn thiết kế (Security by Design).<br>- Trình bày phương án phân đoạn mạng, mã hóa AES-256/TLS 1.3 và kiểm soát RBAC để đạt chuẩn PCI-DSS/GDPR. |
| **Legacy Systems Operations Team** | R | S | `[U] [C] [N] [D] [ ]` | - Tổ chức các buổi hội thảo chuyển đổi tâm lý: Nhấn mạnh cơ hội nâng cao trình độ công nghệ Cloud/DevOps thay vì cắt giảm nhân sự.<br>- Mời kỹ sư Core cũ tham gia thiết kế ánh xạ dữ liệu (Data Mapping) và đào tạo trực tiếp trên hạ tầng mới. |
| **Branch Managers & Tellers** | R | S | `[U] [C] [N] [D] [ ]` | - Thu thập phản hồi về các điểm nghẽn (Pain points) hiện tại ở quầy giao dịch.<br>- Xây dựng chương trình đào tạo "Train-the-Trainer", cung cấp tài liệu mẫu và video hướng dẫn trực quan trước khi Go-Live 1 tháng. |
| **End Customers (Khách hàng)** | U | S | `[C] [N] [ ] [D] [ ]` | - Xây dựng chiến dịch truyền thông ra mắt ứng dụng số mới với các ưu đãi giao dịch real-time.<br>- Đảm bảo kênh hỗ trợ 24/7 và giao diện thân thiện, hạn chế tối đa gián đoạn dịch vụ trong giai đoạn chuyển đổi. |
