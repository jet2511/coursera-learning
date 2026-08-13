# Danh sách Kiểm tra Kỹ năng và Sản phẩm Bàn giao (Skills and Deliverables Checklist)

Tài liệu này tóm tắt chi tiết các kỹ năng, công cụ chuyên môn và các sản phẩm bàn giao (deliverables) cốt lõi của Kiến trúc sư Giải pháp (Solutions Architect) và Kiến trúc sư Hệ thống (Systems Architect).

---

## 1. Bản đồ Kỹ năng và Công cụ (Skills & Tools)

| Danh mục | Solutions Architect (Kiến trúc sư Giải pháp) | Systems Architect (Kiến trúc sư Hệ thống) |
| :--- | :--- | :--- |
| **Kỹ năng Kỹ thuật** | • Kiến trúc ứng dụng (microservices, serverless)<br>• Thiết kế và tích hợp API (REST, GraphQL)<br>• Dịch vụ đám mây gốc (AWS Lambda, Azure Functions)<br>• Mô hình hóa dữ liệu (ETL, data pipelines)<br>• DevOps cơ bản (CI/CD, GitOps)<br>• Bảo mật ứng dụng (OAuth, JWT, RBAC) | • Kiến trúc hạ tầng (on-prem, hybrid, cloud)<br>• Mạng (TCP/IP, DNS, VPN, tường lửa)<br>• Ảo hóa & Điều phối container (Docker, Kubernetes, VMware)<br>• Kế hoạch dự phòng và khôi phục sau sự cố (HA, DR)<br>• Giám sát & Đo lường (Prometheus, Grafana, ELK)<br>• Kiến trúc bảo mật hạ tầng (IAM, ISO 27001, NIST) |
| **Kỹ năng Phân tích & Thiết kế** | • Thu thập và phân tích yêu cầu nghiệp vụ<br>• Phác thảo giải pháp và tài liệu hóa sơ bộ<br>• Phân tích các yếu tố đánh đổi (chi phí, hiệu năng)<br>• Phát triển bản thử nghiệm khả thi (Proof of Concept - PoC) | • Lập kế hoạch dung lượng & hiệu năng (Capacity/Performance)<br>• Tích hợp hệ thống và đảm bảo tính tương thích (interoperability)<br>• Hạ tầng dưới dạng mã nguồn (IaC - Infrastructure as Code)<br>• Quản lý vòng đời hệ thống (System Lifecycle Management) |
| **Kỹ năng Mềm** | • Giao tiếp với các bên liên quan và thuyết trình giải pháp<br>• Dịch chuyển nhu cầu kinh doanh thành giải pháp công nghệ<br>• Cộng tác trong môi trường Agile/Scrum | • Cộng tác liên chức năng (DevOps, IT, Security)<br>• Đánh giá và lập kế hoạch giảm thiểu rủi ro<br>• Quản trị hệ thống và chuẩn hóa tài liệu (System Governance) |
| **Công cụ sử dụng** | • Lucidchart, Draw.io, ArchiMate (mô hình hóa trực quan)<br>• Postman, Swagger (xác thực API)<br>• Terraform (triển khai tài nguyên ở cấp độ giải pháp) | • AWS CloudFormation, Azure ARM, Terraform (triển khai IaC)<br>• Visio, Balsamiq (vẽ sơ đồ)<br>• Ansible, Chef, Puppet (tự động hóa cấu hình) |

---

## 2. Các Sản phẩm Bàn giao Chính (Key Deliverables)

| Loại sản phẩm | Solutions Architect (Kiến trúc sư Giải pháp) | Systems Architect (Kiến trúc sư Hệ thống) |
| :--- | :--- | :--- |
| **Tài liệu Kiến trúc** | **Tài liệu Thiết kế Giải pháp (SDD - Solution Design Document)**:<br>Mô tả chi tiết giải pháp đề xuất bao gồm các thành phần, tích hợp và luồng dữ liệu. | **Sơ đồ Kiến trúc Hệ thống (System Architecture Diagrams)**:<br>Chi tiết về hạ tầng vật lý và logic bao gồm máy chủ, mạng, lưu trữ và kết nối. |
| **Theo dõi Yêu cầu** | **Ma trận Ánh xạ Yêu cầu (Requirements Mapping Matrix)**:<br>Liên kết các yêu cầu kinh doanh trực tiếp với các tính năng và thành phần kỹ thuật. | **Bảng Kê khai Hạ tầng & Thiết bị (BOM - Bill of Materials)**:<br>Danh sách toàn bộ phần cứng, thông số kỹ thuật, số lượng và giấy phép (licenses). |
| **Thiết kế Trực quan** | **Sơ đồ Kiến trúc Tích hợp (Integration Architecture Diagrams)**:<br>Luồng tương tác giữa các hệ thống, API, hàng đợi tin nhắn và dữ liệu. | **Sơ đồ Sắp xếp Mạng (Network Topology Diagrams)**:<br>Bản đồ kiến trúc mạng bao gồm các kết nối, VLAN, giao thức định tuyến và băng thông. |
| **Công nghệ & Công cụ** | **Khuyến nghị Công nghệ (Tech Stack Recommendations)**:<br>Đánh giá và lựa chọn các công nghệ phù hợp kèm lý do và các điểm đánh đổi. | **Mô hình Quy hoạch Dung lượng (Capacity Planning Models)**:<br>Tính toán tài nguyên phần cứng cần thiết, ngưỡng kích hoạt mở rộng tự động. |
| **Xác thực & Bảo mật** | **Báo cáo Thử nghiệm PoC (Proof of Concept Reports)**:<br>Tài liệu đánh giá tính khả thi kỹ thuật của mô hình trước khi phát triển hàng loạt. | **Bản thiết kế Bảo mật Hạ tầng (Security Architecture Blueprints)**:<br>Cấu hình tường lửa, sơ đồ mã hóa, phân quyền truy cập và tuân thủ tiêu chuẩn. |
| **Giao tiếp / Đo lường** | **Tài liệu API (API Documentation)**:<br>Đặc tả chi tiết các endpoint, định dạng dữ liệu, phương thức xác thực và ví dụ cụ thể. | **Khung Giám sát & Đo lường (Monitoring Framework)**:<br>Thiết kế hệ thống cảnh báo (alerting), bảng thông số (dashboard) và chẩn đoán lỗi. |
| **Kế hoạch Triển khai** | **Kế hoạch Di chuyển & Triển khai (Migration & Deployment Plans)**:<br>Lộ trình chuyển đổi từ hệ thống cũ sang mới, kế hoạch backup và rollback. | **Kế hoạch Khôi phục sau Sự cố (DR & BCP)**:<br>Chiến lược backup dữ liệu, mục tiêu khôi phục (RTO, RPO) và quy trình chuyển đổi dự phòng. |
| **Tối ưu hóa** | **Thông số Bảo mật Ứng dụng (App Security Specs)**:<br>Các yêu cầu xác thực người dùng, phân quyền truy cập và tuân thủ dữ liệu. | **Báo cáo Tối ưu hóa Hiệu năng (Performance Reports)**:<br>Phân tích điểm nghẽn hệ thống và đưa ra các khuyến nghị tinh chỉnh hiệu năng. |
