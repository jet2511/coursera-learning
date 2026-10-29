# Overview of Frameworks and Techniques

Tóm tắt nội dung video về tổng quan các khung làm việc (frameworks), kỹ thuật và công cụ mô hình hóa trong Phân tích Kinh doanh.

---

## 1. Tầm quan trọng của Mô hình hóa (Why Modeling Matters)
- **Hình tượng bức tranh ghép hình:** Giải quyết vấn đề nghiệp vụ mà không có mô hình giống như ghép bức tranh hàng nghìn mảnh mà không có hình mẫu hướng dẫn.
- **Lợi ích cốt lõi:**
  - **Đơn giản hóa độ phức tạp:** Chia nhỏ vấn đề lớn thành các thành phần trực quan, dễ quản lý.
  - **Ngôn ngữ chung (Universal Language):** Thu hẹp khoảng cách giao tiếp giữa nghiệp vụ (business) và kỹ thuật (IT/dev).
  - **Tối ưu hóa quy trình:** Giúp phát hiện tắc nghẽn, lỗ hổng và đề xuất phương án cải tiến chính xác.
  - **Tài liệu tham chiếu:** Phục vụ đào tạo, bảo trì, audit và phát triển hệ thống trong tương lai.

---

## 2. Các cấp độ & Phân loại mô hình (Model Levels & Types)

### Cấp độ mô hình hóa (Levels of Detail)
- **High-level Model:** Cung cấp bức tranh toàn cảnh, mối liên kết giữa các chức năng chính (phù hợp cho định hướng chiến lược).
- **Detailed Model:** Đi sâu vào từng bước tác vụ, dữ liệu chi tiết, rẽ nhánh điều kiện (phục vụ triển khai vận hành).

### 4 Loại mô hình chính
| Loại mô hình | Mục đích & Trọng tâm | Ví dụ điển hình |
| :--- | :--- | :--- |
| **Process Models (Mô hình quy trình)** | Minh họa trình tự các bước thực hiện trong luồng công việc để tối ưu hóa vận hành. | Flowchart quy trình hoàn tiền, BPMN xử lý đơn hàng e-commerce. |
| **Data Models (Mô hình dữ liệu)** | Mô tả cấu trúc dữ liệu, mối quan hệ thực thể và cách dữ liệu luân chuyển. | **ERD** (quan hệ Customer - Order - Product), **DFD** (luồng di chuyển của dữ liệu). |
| **Behavioral Models (Mô hình hành vi)** | Mô tả cách hệ thống phản ứng/chuyển trạng thái dưới các điều kiện hoặc sự kiện cụ thể. | **State Diagram** (tài khoản: Active $\to$ Suspended $\to$ Reactivated). |
| **Structural Models (Mô hình cấu trúc)** | Thể hiện tổ chức logic hoặc vật lý của các thành phần trong hệ thống phần mềm. | **Class Diagram** trong công nghệ phần mềm. |

---

## 3. Các kỹ thuật mô hình hóa tiêu chuẩn (Standard Modeling Techniques)
- **Flowcharts:** Sơ đồ trực quan đơn giản dùng hình khối cơ bản (chữ nhật cho bước xử lý, hình thoi cho rẽ nhánh điều kiện/decision, mũi tên chỉ hướng luồng).
- **UML (Unified Modeling Language):** Bộ chuẩn sơ đồ toàn diện dùng trong phần mềm (Use Case, Class, Sequence Diagrams...).
- **BPMN (Business Process Model and Notation):** Chuẩn đồ họa công nghiệp chuyên biệt cho quy trình nghiệp vụ (gồm Tasks, Events, Gateways, Swimlanes).

---

## 4. Quy trình 6 bước xây dựng mô hình (6-Step Modeling Process)
1. **Define Purpose:** Xác định rõ mục tiêu của mô hình (để phân tích, truyền thông, tài liệu hóa hay tối ưu hóa).
2. **Gather Information:** Thu thập dữ liệu từ phỏng vấn, quan sát thực tế và tài liệu sẵn có.
3. **Choose Technique:** Chọn kỹ thuật phù hợp nhất với bài toán (Flowchart, BPMN, hay UML).
4. **Draft Initial Model:** Phác thảo bản thảo đầu tiên tập trung vào các luồng chính và thực thể cốt lõi.
5. **Validate with Stakeholders & SMEs:** Rà soát cùng các chuyên gia nghiệp vụ để đảm bảo mô hình phản ánh đúng thực tế vận hành.
6. **Refine & Finalize:** Bổ sung chi tiết, chuẩn hóa ký hiệu, tinh chỉnh giao diện trực quan và hoàn thiện.

---

## 5. Công cụ mô hình hóa thông dụng (Common Tooling)
- **Microsoft Visio:** Công cụ truyền thống, giao diện thân thuộc để vẽ flowchart và sơ đồ trực quan.
- **Lucidchart:** Nền tảng vẽ trực tuyến mạnh về cộng tác theo thời gian thực (real-time), tích hợp Google Workspace, Slack.
- **Bizagi Modeler:** Phần mềm chuyên biệt, miễn phí và mạnh mẽ dành riêng cho mô hình hóa chuẩn BPMN.
- **Enterprise Architect:** Nền tảng cấp doanh nghiệp (Enterprise-grade) hỗ trợ toàn diện cả UML, BPMN và kiến trúc phức tạp.

---

## 6. Case Study thực tế: Tối ưu tồn kho bán lẻ (Retail Inventory Optimization)
- **Mục tiêu:** Giảm 20% chi phí lưu kho (holding costs), giảm 30% tình trạng đứt hàng (stockouts).
- **Cách BA triển khai:**
  1. Thu thập dữ liệu bán hàng lịch sử, phỏng vấn nhân sự kho và lập Data Model cho các thực thể: Products, Sales, Suppliers, Inventory Levels.
  2. Phân tích xu hướng, tính điểm tái đặt hàng (reorder points) dựa trên tốc độ bán trung bình và thời gian giao hàng (lead time).
  3. Lập mô hình dự báo nhu cầu (predictive model).
  4. Đề xuất tự động hóa điểm kích hoạt đặt hàng (reorder triggers) và xây dựng Dashboard quản lý tập trung.
  5. Chạy Pilot kiểm chứng trước khi nhân rộng ra toàn công ty và liên tục theo dõi, tinh chỉnh.
