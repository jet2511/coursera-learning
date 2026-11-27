# 09 - Assignment Overview: Create a Security Architecture Diagram

- **Thời lượng ước tính:** 2 phút
- **Tác giả:** Parikshit Jain
- **Mục tiêu:** Thiết kế biểu đồ kiến trúc an ninh bảo mật đa tầng (**Multi-layered Security Architecture Diagram**) theo mô hình phòng thủ theo chiều sâu (**Defense-in-Depth**) và nguyên lý **Zero-Trust** cho quá trình chuyển đổi số của ngân hàng ABC Bank.

---

## 1. Mục đích bài tập (Purpose)

1. Hiểu và mô hình hóa cách các lớp kiểm soát bảo mật đa tầng phối hợp bảo vệ hệ sinh thái ngân hàng số.
2. Nhận diện và biểu diễn 4 tầng bảo mật cốt lõi (+ 1 tầng IAM mở rộng):
   - **Tầng An ninh Mạng (Network Security Layer)**
   - **Tầng An ninh Ứng dụng (Application Security Layer)**
   - **Tầng An ninh Dữ liệu (Data Security Layer)**
   - **Tầng Giám sát & Ứng phó sự cố (Monitoring & Incident Response Layer)**
   - **Tầng Quản lý Danh tính & Phân quyền (Identity & Access Management - IAM Layer)**
3. Định vị chính xác các công nghệ an ninh: Firewalls, VPN, SASE, WAF, DevSecOps (SAST/DAST/Secret Scan), API Gateway, Mã hóa (In-Transit & At-Rest), HSM Key Management, SIEM, SOC, DLP.
4. Xây dựng bản vẽ thiết kế an ninh trực quan phục vụ đánh giá rủi ro và thẩm định kiểm toán tuân thủ (PCI-DSS, SOC 2, ISO 27001).

---

## 2. Quy trình 3 bước thực hiện (3 Steps Workflow)

### Step 1: Identify Required Security Layers
Lập bảng danh mục các tầng an ninh bảo mật và các thành phần kỹ thuật tương ứng thuộc từng tầng.

### Step 2: Create a Multi-Layered Security Architecture Diagram
Sử dụng công cụ thiết kế trực quan (Lucidchart, Draw.io, PowerPoint) để vẽ sơ đồ kiến trúc an ninh đa tầng bao gồm:
- **Network Security:** Packet filter/Stateful firewall, VPN Gateway, SASE Edge, DMZ, Phân vùng mạng (VPC Peering, Subnet segmentation), WAF.
- **Application Security:** DevSecOps pipeline, SAST/DAST scanners, Secret scanning, API Gateway bảo mật, Microservices trong phân vùng cô lập an toàn.
- **Data Security:** Phân loại dữ liệu (Data classification), Mã hóa đường truyền (TLS 1.3) và lưu trữ (AES-256), Quản lý khóa (KMS / HSM), Phân vùng nhạy cảm (PCI-DSS, KYC, AML).
- **Monitoring & Response:** SIEM (Splunk/QRadar), DLP (Data Loss Prevention), Quy trình giám sát SOC 24/7 (Alerts → Investigation → Containment).

### Step 3: Validate Architecture Using a Checklist
Đối soát 5 tiêu chí:
- Thể hiện đầy đủ các domain an ninh.
- Bố trí thành phần vào đúng tầng kiến trúc.
- Luồng tương tác giữa các tầng rõ ràng.
- Thỏa mãn quy định bảo mật ngành ngân hàng.
- Trình bày định dạng chuyên nghiệp, dễ đọc.

---

## 3. Sản phẩm bàn giao (Deliverables)

1. **Security Layers & Components Table:** Bảng định nghĩa các tầng và thành phần bảo mật.
2. **Multi-layered Security Architecture Diagram (.png hoặc .pptx):** Sơ đồ kiến trúc an ninh đa tầng.
3. **Short Explanation of the Diagram:** Bản tóm tắt giải trình sơ đồ (5–7 gạch đầu dòng súc tích).
4. **Completed Validation Checklist:** Bảng kiểm tra nghiệm thu an ninh doanh nghiệp.
