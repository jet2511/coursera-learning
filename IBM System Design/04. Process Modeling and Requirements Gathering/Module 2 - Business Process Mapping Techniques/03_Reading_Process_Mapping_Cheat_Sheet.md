# Process Mapping Cheat Sheet

## 1. Khái niệm & Thuật ngữ quan trọng
- **Process Mapping (Lập bản đồ quy trình):** Phương pháp trực quan hóa dòng chảy công việc trong tổ chức, giúp BA, PM và Team Lead truyền đạt quy trình phức tạp một cách nhất quán.
- **Thuật ngữ & Khái niệm nâng cao:**
  - **On-Page Connector (Bộ kết nối cùng trang - Hình tròn):** Điểm nối các nhánh trong cùng 1 trang để tránh vẽ đường cắt nhau gây rối mắt.
  - **Off-Page Connector (Bộ kết nối khác trang - Ngũ giác/Hình nhà lộn ngược):** Điểm chuyển tiếp luồng công việc sang một trang tài liệu khác (gán nhãn "A", "B", "Page 2").
  - **Pre-Defined Process (Quy trình tiền định nghĩa / Quy trình con):** Đại diện cho một quy trình con chuẩn hóa đã được định nghĩa chi tiết ở tài liệu khác (thường mô tả qua *Process Narrative*).
  - **Process Narrative (Bản tường thuật quy trình):** Văn bản mô tả chi tiết bằng lời từng bước thực hiện của một quy trình hoặc quy trình con.
  - **Handoff (Bàn giao):** Điểm giao thoa công việc/thông tin từ vai trò/bộ phận này sang vai trò/bộ phận khác trong sơ đồ *Swimlanes*.

---

## 2. Bảng ký hiệu chuẩn hóa (Standard Symbols Cheat Sheet)

| Ký hiệu (Symbol) | Hình dạng | Ý nghĩa / Ứng dụng | Ví dụ thực tế |
| :--- | :--- | :--- | :--- |
| **Oval / Terminator** | Bầu dục | Điểm bắt đầu (Start) hoặc kết thúc (End) | "Start", "End" |
| **Rectangle** | Chữ nhật | Hành động, tác vụ hoặc bước xử lý | "Review Document", "Approve Request" |
| **Diamond** | Hình thoi | Điểm quyết định, phân nhánh có điều kiện | "Approved? (Yes / No)" |
| **Parallelogram** | Hình bình hành | Nhập dữ liệu (Input) hoặc xuất dữ liệu (Output) | "Receive Order Data", "Send Email" |
| **Document** | Chữ nhật lượn sóng đáy | Tạo ra hoặc sử dụng tài liệu giấy / file số | "Invoice", "Purchase Order (PO)" |
| **Cylinder** | Hình trụ (Database) | Nơi lưu trữ dữ liệu (Database, kho lưu trữ, file hệ thống) | "Customer DB", "ERP Storage" |
| **Circle** | Hình tròn nhỏ | Bộ kết nối nội bộ trong cùng một trang (On-Page Connector) | Nối tránh đường cắt nhau |
| **Pre-Defined Process** | Chữ nhật có 2 sọc dọc hai bên | Quy trình con đã chuẩn hóa ở tài liệu riêng | "Conduct Quality Check" |
| **Off-Page Connector** | Hình ngũ giác chỉ xuống | Tiếp tục quy trình ở trang khác | Gắn nhãn "Page 2", "Connector A" |
| **Arrow** | Mũi tên | Chỉ hướng luồng công việc & trình tự dữ liệu | Luồng thực hiện từ bước này sang bước kia |
| **Swim Lane Divider** | Đường kẻ phân làn | Phân chia công việc theo vai trò, cá nhân hoặc phòng ban | Phân quyền QA, Dev, Kế toán |

---

## 3. Best Practices & Sai lầm cần tránh (Dos & Don'ts)

### Best Practices (Nên làm)
- **Define Objective:** Xác định rõ mục tiêu bản đồ (cải tiến, đào tạo hay tài liệu hóa).
- **Start Simple:** Bắt đầu từ luồng chính (Happy Path) trước khi đi sâu vào chi tiết rẽ nhánh.
- **Use Standard Symbols:** Luôn dùng ký hiệu chuẩn để mọi người cùng hiểu chung một ngữ cảnh.
- **Validate with Stakeholders:** Kiểm chứng thực tế với người trực tiếp làm việc, không dựa trên suy đoán.
- **Highlight Decisions:** Làm nổi bật điểm kiểm duyệt/rẽ nhánh.
- **Label Clearly:** Dùng cụm từ ngắn gọn, hướng hành động (Động từ + Danh từ).
- **Include Roles:** Dùng *Swimlanes* để minh bạch trách nhiệm bàn giao (*handoffs*).

### Common Pitfalls (Cần tránh)
- **Don't Overcomplicate:** Quá nhiều chi tiết vụn vặt làm sơ đồ rối rắm, khó theo dõi.
- **Don't Skip Validation:** Bỏ qua xác thực sẽ biến quy trình sai lệch thành chuẩn mực chính thức.
- **Don't Mix Levels:** Tránh trộn lẫn các bước mức vĩ mô (High-level) với chi tiết mức vi mô trong cùng một sơ đồ.
- **Don't Assume Linear Flow:** Đừng mặc định quy trình luôn thẳng hàng; phải thể hiện các vòng lặp sửa lỗi (loops), làm lại (rework) và xử lý song song.
- **Don't Forget the Audience:** Điều chỉnh độ chi tiết phù hợp với người đọc (C-level, Quản lý hay Nhân viên thực thi).
- **Don't Neglect Updates:** Định kỳ rà soát và cập nhật vì quy trình luôn biến đổi theo thời gian.
