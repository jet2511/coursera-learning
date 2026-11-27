# Choosing Your Development Approach: Scenario Exploration

> **Khóa học**: Introduction to Software Engineering (Course 01 trong chứng chỉ *IBM Java Developer Professional Certificate*)  
> **Phần**: The Software Building Process and Associated Roles  
> **Hoạt động**: Dialogue (Coursera AI Coach)  
> **Chủ đề**: Ứng dụng Waterfall, V-Model và Agile qua các kịch bản thực tế & Đánh giá Trade-offs  

---

## 1. Phân tích 3 kịch bản thực tế (Scenario Analysis)

### Kịch bản 1: Startup ứng dụng mạng xã hội (Social Media App)
- **Đặc trưng:** Cần tốc độ thâm nhập thị trường (**speed-to-market**), thử nghiệm nhanh và thu thập phản hồi người dùng liên tục.
- **Phương pháp tối ưu:** **Agile**.
  - Triển khai theo Sprint ngắn (1–4 tuần) để sớm đưa ra sản phẩm khả thi tối thiểu (**MVP**).
  - Liên tục kiểm chứng giả định và đưa phản hồi vào các vòng lặp tiếp theo.
- **Đánh đổi & Rủi ro (Trade-off):** Nguy cơ tích tụ **nợ kỹ thuật (Technical Debt)** và kiến trúc lỏng lẻo. Nếu quá tập trung đẩy tính năng nhanh mà bỏ qua tài liệu và quy hoạch kiến trúc dài hạn, hệ thống sẽ khó mở rộng (scale) và chi phí bảo trì tăng vọt khi lượng người dùng tăng đột biến.
- **Xử lý khi đổi hướng (Pivot):** Trong Agile, team chỉ cần tái sắp xếp **Product Backlog**, hủy bỏ các user stories cũ và chuyển hướng ngay trong Sprint tiếp theo. Waterfall sẽ sụp đổ trước pivot này do mọi tài liệu thiết kế và kế hoạch đã bị "khóa cứng" từ đầu.

---

### Kịch bản 2: Hệ thống giao dịch ngân hàng cốt lõi (Core Banking System)
- **Đặc trưng:** Ưu tiên tuyệt đối tính chính xác không tì vết (**zero-defect**), tuân thủ quy định tài chính nghiêm ngặt (regulatory compliance), bảo mật và khả năng kiểm toán (auditability). Chi phí sai sót cực kỳ đắt đỏ.
- **Phương pháp tối ưu:** **Mô hình chữ V (V-Shaped Model)** (hoặc Waterfall có cấu trúc).
  - Từng cấp độ thiết kế (Planning, System Design, Architecture, Module) đều được liên kết chặt chẽ với một cấp độ kiểm thử tương ứng (Acceptance, System, Integration, Unit Testing).
  - Kiểm soát rủi ro toàn diện trước khi phát hành lên môi trường vận hành thực tế.
- **Đánh đổi & Rủi ro (Trade-off):** **Cực kỳ cứng nhắc (extreme rigidity)** và chi phí thay đổi rất cao. Khi có thay đổi chính sách/luật định mới giữa chừng, sự liên kết chặt giữa Verification và Validation buộc dự án phải sửa đổi dây chuyền trên toàn bộ tài liệu thiết kế lẫn kịch bản kiểm thử, gây trễ hạn và đội chi phí.

---

### Kịch bản 3: Thiết bị y tế theo dõi bệnh nhân (Patient Monitoring Software)
- **Đặc trưng:** Bài toán kết hợp hai nhu cầu xung đột: độ an toàn/chính xác sinh mạng tuyệt đối (tương tự ngân hàng) và tính tiện dụng, dễ thao tác cho bác sĩ ngoài thực địa (tương tự startup).
- **Phương pháp tối ưu:** **Mô hình lai (Hybrid Approach: Agile + V-Model)**:
  - **Lớp giao diện & trải nghiệm (UI/UX):** Áp dụng **Agile** – xây dựng prototype nhanh, thu thập và lặp phản hồi thực tế từ các y bác sĩ qua từng sprint.
  - **Lớp lõi an toàn (Core Engine, Telemetry, Hardware Integration):** Áp dụng **V-Model** – thẩm định và kiểm thử nghiêm ngặt, đảm bảo an toàn bệnh nhân, truy vết lỗi (traceability) và đạt chuẩn kiểm định y tế.

---

## 2. Thách thức lớn nhất của mô hình lai (Hybrid Rhythm Challenge)
- **Lệch nhịp vận hành (Rhythm Mismatch):** Đội UI/UX chạy theo nhịp nhanh (Agile Sprints 1–2 tuần), trong khi đội Core Engine chạy theo nhịp tuần tự nghiêm ngặt (V-Model kéo dài nhiều tháng).
- **Nguy cơ phá vỡ ràng buộc an toàn:** Một thay đổi nhỏ ở tầng giao diện của Agile (ví dụ: cách hiển thị cảnh báo nhịp tim) có thể làm thay đổi yêu cầu phi chức năng hoặc ngưỡng an toàn ở tầng Core.
- **Giải pháp điều phối:** Cần thiết lập **hợp đồng giao diện (Interface Contracts)** rõ ràng, cơ chế quản trị thay đổi (Change Governance) chặt chẽ và tài liệu hóa chuẩn mực làm "chất keo" liên kết hai nhóm.

---

## 3. Tổng kết bài học ra quyết định (Decision-Making Framework)

| Tiêu chí dự án | Waterfall | V-Model | Agile | Hybrid (Lai) |
| :--- | :---: | :---: | :---: | :---: |
| **Yêu cầu không đổi, tài chính/thời gian cố định** | ★★★ | ★★☆ | ★☆☆ | ★☆☆ |
| **Hệ thống sống còn (Mission-critical / Safety)** | ★★☆ | ★★★ | ★☆☆ | ★★☆ |
| **Khám phá thị trường, tốc độ ra MVP** | ★☆☆ | ★☆☆ | ★★★ | ★★☆ |
| **Đa tầng (Lõi an toàn khắt khe + Giao diện người dùng cao)** | ★☆☆ | ★★☆ | ★★☆ | ★★★ |
