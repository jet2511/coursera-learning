# Assignment Overview: Process Modeling and Visualization
**Module:** Module 2 - Project Planning and Process Modeling  
**Dự án:** Retail Bank's Digital Core Transformation  
**Tác giả:** Parikshit Jain  

---

## 1. Giới thiệu tổng quan
Giai đoạn này tập trung vào kỹ năng **Mô hình hóa quy trình (Process Modeling)** và **Trực quan hóa luồng dữ liệu/nghiệp vụ (Visualization)** để hỗ trợ quá trình chuyển đổi số của Ngân hàng bán lẻ (**Retail Bank**). 
Trọng tâm là thiết kế, tối ưu hóa quy trình mở tài khoản khách hàng (**Customer Onboarding**) kết hợp định danh điện tử (**eKYC**), phân tích điểm nghẽn (bottlenecks), và chuẩn hóa tài liệu kỹ thuật theo chuẩn **UML** phục vụ giao tiếp giữa các bên liên quan và định hướng triển khai hệ thống.

---

## 2. Năm nhiệm vụ cốt lõi (Core Tasks)

### Task 1: Mô hình hóa quy trình Customer Onboarding & KYC Verification
- Thiết kế lưu đồ (Flowchart) mô tả hành trình mở tài khoản đầu-cuối (End-to-End): từ yêu cầu ban đầu, xác minh giấy tờ, kiểm tra sinh trắc học/eKYC, đến khi kích hoạt tài khoản thành công.
- Ứng dụng các ký hiệu UML tiêu chuẩn (Start/End, Activity, Decision, Data Store).
- Nhận diện các điểm nghẽn vận hành (Operational Bottlenecks) hiện tại và xác định cơ hội tự động hóa.

### Task 2: Xác định và phân rã các giai đoạn nghiệp vụ (Process Components)
- Phân rã quy trình Onboarding thành các giai đoạn logic cụ thể (ví dụ: Khởi tạo hồ sơ, Xác thực danh tính tự động, Thẩm định tuân thủ thủ công/ngoại lệ, Cấp phát tài khoản & Cấu hình).
- Làm rõ từng điểm quyết định (Decision Points), các lời gọi API tự động, và các bước can thiệp thủ công của nhân viên tuân thủ.

### Task 3: Xây dựng lưu đồ UML Onboarding hoàn chỉnh
- Dựng lưu đồ trực quan bằng công cụ chuyên dụng (Draw.io / Lucidchart / Mermaid).
- Bổ sung các chú giải (annotations) chi tiết cho logic rẽ nhánh, luồng di chuyển dữ liệu và xử lý ngoại lệ (exception paths).

### Task 4: Phát triển sơ đồ Use Case tương tác hệ thống
- Mô hình hóa mối tương tác giữa các vai trò bên liên quan với Core Banking System:
  - **Retail Customers:** Đăng ký, chụp ảnh CCCD, xác thực khuôn mặt, tra cứu trạng thái.
  - **Branch Staff / Tellers:** Hỗ trợ tiếp nhận hồ sơ, đối soát giấy tờ gốc tại quầy.
  - **Compliance Officers:** Thẩm định danh sách đen (Watchlist/PEP), xử lý hồ sơ cảnh báo AML/KYC.
  - **IT Administrators / System:** Quản trị cấu hình, bảo trì API kết nối và giám sát vận hành.
- Ánh xạ trực tiếp từng Use Case với các yêu cầu chức năng (FRs) và phi chức năng (NFRs) đã xác lập ở Module 1.

### Task 5: Rà soát, tối ưu hóa và thẩm định mô hình (Review & Refinement)
- Kiểm tra tính đầy đủ (Completeness), hiệu quả vận hành (Efficiency), và độ trong sáng, dễ hiểu (Clarity).
- Loại bỏ các bước thừa thãi/lặp lại (redundant steps), chuẩn hóa các luồng rẽ nhánh và đảm bảo mô hình sẵn sàng trình duyệt các bên liên quan.

---

## 3. Danh mục sản phẩm bàn giao (Deliverables Checklist)

- [ ] **1. Customer Onboarding & KYC Process Flowchart:** Lưu đồ quy trình chuẩn UML kèm ghi chú luồng dữ liệu.
- [ ] **2. Process Stages & Decision Points Breakdown:** Bản đặc tả chi tiết từng bước, quyết định và tích hợp API.
- [ ] **3. Validated & Optimized Flowchart Documentation:** Bản tài liệu lưu đồ đã qua tối ưu hóa, loại bỏ điểm nghẽn.
- [ ] **4. Core Banking Use Case Diagram:** Sơ đồ Use Case tương tác hệ thống liên kết chặt chẽ với FRs & NFRs.
- [ ] **5. Validation Summary Report:** Báo cáo đánh giá chất lượng mô hình về tính hoàn thiện, hiệu năng và tính rõ ràng.
