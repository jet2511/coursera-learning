# Đánh Giá Kết Quả Thực Hiện Lab (Quiz / Review Answers - Create a Security Architecture Diagram)

Dưới đây là đáp án và giải trình đối chiếu cho 7 câu hỏi tự đánh giá (Self-Assessment) của bài Lab Create a Security Architecture Diagram:

---

### Câu 1 (Question 1)
> **Have you identified and listed all required security layers and components, including network, application, data security, monitoring, and IAM?**

- **Đáp án:** **Yes**
- **Giải trình:** Trong `Task1_Security_Layers_and_Components.md`, đã lập danh mục định nghĩa đầy đủ 5 tầng an ninh bảo mật: Network Security, Application Security, Data Security, Monitoring & Incident Response, và Identity & Access Management (IAM) xuyên suốt.

---

### Câu 2 (Question 2)
> **Did you create a multi-layered security architecture diagram illustrating the bank’s security posture across all layers using an appropriate diagramming tool?**

- **Đáp án:** **Yes**
- **Giải trình:** Trong `Task2_Security_Architecture_Diagram.md`, sơ đồ kiến trúc bảo mật đa tầng đã được xây dựng hoàn chỉnh theo mô hình Defense-in-Depth, thể hiện rõ 4 tầng ngang, phân vùng an ninh, ranh giới DMZ và sẵn sàng xuất file `security_architecture_diagram.pdf`.

---

### Câu 3 (Question 3)
> **Are network security components such as firewalls, VPNs, SASE, segmentation, and proxy controls properly represented and labeled in your diagram?**

- **Đáp án:** **Yes**
- **Giải trình:** Tại Tầng 1 (Network Security Layer), toàn bộ các thành phần nòng cốt như External Firewall (Anti-DDoS), WAF, SASE Cloud Edge / VPN Gateway, DMZ Ingress Proxy, Internal Stateful Firewall, và phân đoạn mạng North-South / East-West đều được mô hình hóa và gắn nhãn rõ ràng.

---

### Câu 4 (Question 4)
> **Have you incorporated application security practices, such as DevSecOps pipelines, SAST, DAST, and secure SDLC, into your diagram?**

- **Đáp án:** **Yes**
- **Giải trình:** Tại Tầng 2 (Application Security Layer), quy trình DevSecOps CI/CD đã tích hợp đầy đủ các công cụ kiểm thử bảo mật tự động: SAST (SonarQube), DAST (OWASP ZAP), Secret Scanning (Trivy), kết hợp cùng API Gateway và runtime protection cho Microservices nội bộ.

---

### Câu 5 (Question 5)
> **Does your diagram include data security controls such as encryption, data classification, governance, and regulatory compliance elements?**

- **Đáp án:** **Yes**
- **Giải trình:** Tại Tầng 3 (Data Security Layer), hệ thống thể hiện cơ chế phân loại dữ liệu (Data Classification & Governance), mã hóa toàn diện (TDE AES-256 at rest, TLS 1.3 in transit), quản lý khóa phần cứng (KMS/CloudHSM), Tokenization thẻ thanh toán và các phân vùng nhạy cảm tuân thủ PCI-DSS, eKYC và AML.

---

### Câu 6 (Question 6)
> **Is the monitoring and response layer represented by components such as SIEM, DLP, incident response workflows, and alerts?**

- **Đáp án:** **Yes**
- **Giải trình:** Tại Tầng 4 (Monitoring & Response Layer), kiến trúc tích hợp hệ thống SIEM tập trung, động cơ chống thất thoát dữ liệu DLP, cùng quy trình ứng cứu sự cố SOC 24/7 khép kín theo chu trình: *Alerts → Analyst Triage → Auto Containment*.

---

### Câu 7 (Question 7)
> **Have you provided a clear justification for the architecture choices and validated the diagram against the lab checklist, including compliance alignment?**

- **Đáp án:** **Yes**
- **Giải trình:** Trong `Task3_Diagram_Justification.md` và `Task4_Validation_Checklist.md`, đã cung cấp 5 luận điểm giải trình kiến trúc vững chắc (Zero-Trust, Shift-Left, PCI-DSS Level 1, SOC 2, HA) và hoàn thành bản đối soát 8 tiêu chí kiểm tra nghiệm thu đạt 100% PASSED.

---

## Tổng kết đánh giá: **7/7 (100% Đạt - 7 points)**
