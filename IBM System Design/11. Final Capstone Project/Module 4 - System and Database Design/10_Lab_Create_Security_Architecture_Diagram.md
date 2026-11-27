# 10 - Lab Guide: Create a Security Architecture Diagram

- **Thời lượng ước tính:** 15 phút
- **Tác giả:** Parikshit Jain
- **Vai trò:** Chief Information Security Officer (CISO) & Enterprise Security Architect
- **Bối cảnh (Scenario):** Ngân hàng bán lẻ hoạt động trong môi trường tài chính chịu sự giám sát chặt chẽ của các cơ quan quản lý. Nhóm kiến trúc sư cần thiết kế biểu đồ kiến trúc bảo mật đa tầng trực quan (**Multi-layered Security Architecture Diagram**) thể hiện cách các lớp phòng thủ chiều sâu (Defense-in-Depth) bảo vệ hệ thống, giao dịch, API và dữ liệu nhạy cảm của khách hàng.

---

## 1. Công cụ & Biểu mẫu mẫu (Template)
- **Công cụ thiết kế:** Lucidchart, Draw.io, Microsoft PowerPoint, Visio.
- **Biểu mẫu tham chiếu:** `Template-Solution-Create a security architecture diagram.docx / .pdf`.
- **Tệp xuất ra:** `security_architecture_diagram.pdf` (hoặc `.png`).

---

## 2. Chi tiết 4 nhiệm vụ thực hiện (Tasks to be performed)

### Task 1: Identify Security Layers and Components
Lập bảng danh mục định nghĩa 5 tầng an ninh bảo mật, các thành phần kỹ thuật nòng cốt và mục đích phòng thủ:
1. Network Security Layer
2. Application Security Layer
3. Data Security Layer
4. Monitoring & Response Layer
5. Identity & Access Management (IAM) Layer (Lớp xuyên suốt)

### Task 2: Create a Multi-Layered Security Architecture Diagram
Vẽ biểu đồ an ninh đa tầng theo 4 tầng ngang liên kết chặt chẽ:
- **Tầng 1 (Network Security):** External Firewall, SASE Edge, VPN Gateway, WAF, DMZ, Internal Stateful Firewall, Network Segmentation (North-South & East-West).
- **Tầng 2 (Application Security):** DevSecOps CI/CD pipeline, SAST/DAST, Secret scanning, API Gateway, Microservices đặt trong vùng nội bộ an toàn.
- **Tầng 3 (Data Security):** Data Classification, TDE (Transparent Data Encryption), TLS 1.3, Tokenization (mã hóa thẻ PCI), Phân quyền RBAC/ABAC, Vùng dữ liệu nhạy cảm (PCI, KYC, AML).
- **Tầng 4 (Monitoring & Response):** SIEM tập trung, SOC Dashboard 24/7, DLP (Chống thất thoát dữ liệu), Quy trình ứng cứu sự cố (Alerts → Investigation → Containment).
- **Luồng kết nối mũi tên:** Request đi từ Perimeter Firewall → API Gateway/App → Truy vấn Data mã hóa → Toàn bộ các tầng đẩy Log về SIEM/SOC.

### Task 3: Justify the Diagram
Viết bản giải trình ngắn gọn (5-7 điểm súc tích) giải thích vì sao kiến trúc này bảo vệ ngân hàng toàn diện trước các mối đe dọa mạng và đáp ứng chuẩn PCI-DSS / SOC 2.

### Task 4: Validate the Diagram
Đối soát toàn bộ 8 tiêu chí kiểm tra nghiệm thu theo checklist chuẩn ngành ngân hàng.
