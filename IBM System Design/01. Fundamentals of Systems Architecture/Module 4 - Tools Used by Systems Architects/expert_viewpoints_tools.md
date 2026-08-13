# Expert Viewpoints: Tools used by Systems Architect (Góc nhìn chuyên gia: Các công cụ của Kiến trúc sư)

Bản tóm tắt thực tế từ các chuyên gia về cách áp dụng công cụ trong công việc kiến trúc hàng ngày, nhấn mạnh tính thực tiễn và cách quản lý tài liệu hiệu quả.

---

### 1. Thiết kế sơ đồ kiến trúc (Architecture Diagramming)
*   **Công cụ:** *Visio*, *draw.io* (web-based, miễn phí, tích hợp Google Drive).
*   **Mô hình áp dụng:** **C4 Model** (chia thành 4 cấp độ: Context, Container, Component, Code).
    *   *Sơ đồ Context (Bối cảnh):* Dành cho cấp quản lý/executive để hiểu hệ thống trong môi trường tổng quan.
    *   *Sơ đồ Component/Code (Thành phần/Mã nguồn):* Dành cho các lập trình viên để nắm cấu trúc chi tiết và triển khai.
*   **Mô hình hóa miền nghiệp vụ:** Sử dụng kỹ thuật **Event-Storming** mang tính cộng tác cao đối với các domain phức tạp thay vì chỉ dùng công cụ vẽ đơn thuần.
*   **Thiết kế dữ liệu:** Sử dụng *DBDiagram.io* hoặc các công cụ tương đương để mô hình hóa nhanh dữ liệu.

---

### 2. Quản lý tài liệu và các quyết định kiến trúc
*   **ADR (Architecture Decision Records):** Tài liệu gọn nhẹ để lưu vết các quyết định thiết kế. Mỗi ADR phải bao gồm:
    1.  *Context (Bối cảnh):* Vấn đề hoặc yêu cầu nghiệp vụ là gì.
    2.  *Decision (Quyết định):* Hệ thống chọn giải pháp nào.
    3.  *Consequences (Hệ quả):* Ưu/nhược điểm và độ phức tạp phát sinh sau quyết định.
    4.  *Alternatives (Phương án thay thế):* Các hướng đi khác đã bị loại bỏ và lý do vì sao loại bỏ.
*   **Thực hành tốt nhất về tài liệu hóa:**
    *   *Giữ tài liệu gần mã nguồn:* Lưu trữ ADR trực tiếp trong Git repository, quản lý phiên bản (versioned) và kiểm duyệt thông qua Pull Requests (PRs).
    *   *Không viết tài liệu tràn lan:* Chỉ tài liệu hóa các quyết định kiến trúc và các pattern không thể tự giải thích bằng mã nguồn.
    *   *Vận hành:* Xây dựng **Runbooks** hướng dẫn cách deploy, scale, khắc phục sự cố (troubleshoot) và khôi phục sau thảm họa (disaster recovery).
    *   *Phù hợp đối tượng:* Executives nhận tóm tắt 1 trang làm rõ giá trị kinh doanh; Developers nhận sơ đồ kỹ thuật chi tiết và runbooks.

---

### 3. Thiết kế và Đặc tả API
*   **Công cụ:** *Swagger*, *OpenAPI specification*.
*   **Thực hành tốt nhất:** Định nghĩa và thống nhất thiết kế API trước khi viết code (API-first design) giúp các đội phát triển độc lập không bị lệch pha về mặt giao tiếp dữ liệu (contract alignment).

---

### 4. Hạ tầng dưới dạng mã (Infrastructure as Code - IaC)
*   **Công cụ:** *Terraform*, *IBM Cloud Schematics*.
*   **Mục đích:** Tự động hóa triển khai hạ tầng đám mây (AWS, Azure, GCP, IBM Cloud), đảm bảo tính nhất quán trên các môi trường phát triển/kiểm thử/production và tuân thủ các quy tắc quản trị (governance/compliance).

---

### 5. Giám sát hệ thống & Thu thập chỉ số (Monitoring & Observability)
*   **Công cụ:** *Datadog*, *Grafana*, *Prometheus*.
*   **Mục đích:** Kiến trúc sư bắt buộc phải hiểu cách hệ thống vận hành thực tế trên môi trường production. Các chỉ số đo lường (metrics) thực tế sẽ là cơ sở đầu vào để đưa ra các quyết định điều chỉnh cấu trúc hệ thống tiếp theo.

---

### 6. Cộng tác và Tư duy Kiến trúc
*   **Công cụ cộng tác:** *Miro* (bảng trắng ảo), họp rà soát kiến trúc (architecture review meetings) định kỳ với stakeholders để đảm bảo tính minh bạch.
*   **Khung kiến trúc mẫu:** Sử dụng các thư viện mẫu thiết kế (design patterns), cẩm nang kiến trúc (playbooks) và framework tiêu chuẩn doanh nghiệp như *TOGAF*.

> [!IMPORTANT]
> **Thông điệp cốt lõi từ chuyên gia:**
> Công cụ chỉ là phương tiện hỗ trợ (enablers). Công cụ quan trọng nhất của một kiến trúc sư chính là **tư duy phản biện (critical thinking)** và **năng lực phân tích, đánh giá các sự đánh đổi (trade-offs)** trong hệ thống.
