# Common Notations and Tools for Process Modeling

Tóm tắt tài liệu đọc về 3 ký hiệu chuẩn phổ biến nhất trong mô hình hóa quy trình nghiệp vụ: **Flowcharts**, **Swimlane Diagrams** và **BPMN**.

---

## 1. 3 Ký hiệu Mô hình hóa Chuẩn (3 Common Notations)

### 1. Flowcharts (Lưu đồ quy trình)
- **Định nghĩa:** Sơ đồ trực quan thể hiện trình tự các bước bằng các ký hiệu hình khối tiêu chuẩn: hình chữ nhật (bước thực hiện/step), hình thoi (ra quyết định/decision) và mũi tên (hướng luồng/flow).
- **Khi nào nên dùng:** Các luồng công việc đơn giản, thủ tục định kỳ, hoặc các nhánh quyết định thẳng thắn, dễ hiểu với mọi đối tượng.
- **Lợi ích:** Mang lại góc nhìn tổng quan (high-level), dễ phát hiện bước thừa/thiếu, phù hợp cho đào tạo người dùng phi kỹ thuật.
- **Ví dụ:** Quy trình hoàn tiền công tác phí (nộp yêu cầu $\to$ xác minh hóa đơn $\to$ phê duyệt $\to$ chi tiền).

---

### 2. Swimlane Diagrams (Sơ đồ làn bơi / Sơ đồ liên chức năng)
- **Định nghĩa:** Một dạng Flowchart nâng cao phân chia các hoạt động thành các "làn" (**lanes**), mỗi làn đại diện cho một cá nhân, vai trò hoặc phòng ban chịu trách nhiệm thực thi.
- **Khi nào nên dùng:** Quy trình phối hợp liên phòng ban (**cross-functional**), liên quan nhiều đội nhóm hoặc nhiều hệ thống.
- **Lợi ích:**
  - Làm rõ trách nhiệm (**accountability**) tại từng bước.
  - Làm nổi bật các điểm chuyển giao công việc (**handoffs**) và phụ thuộc (**dependencies**).
  - Chỉ ra lỗ hổng giao tiếp và sự kém hiệu quả giữa các bộ phận.
- **Ví dụ:** Quy trình xử lý đơn hàng gồm các làn: Bán hàng (**Sales**) $\to$ Kho (**Warehouse**) $\to$ Vận chuyển (**Shipping**) $\to$ Kế toán (**Finance**).

---

### 3. BPMN (Business Process Model and Notation)
- **Định nghĩa:** Bộ ký hiệu chuẩn hóa công nghiệp do tổ chức **OMG (Object Management Group - Tổ chức Quản lý Đối tượng)** phát triển, dùng các biểu tượng chuẩn cho Sự kiện (**Events**), Hoạt động (**Activities**), Cổng rẽ nhánh (**Gateways**) và Luồng tuần tự (**Flows**).
- **Khi nào nên dùng:** Phân tích chi tiết quy trình phức tạp, thiết kế hệ thống phần mềm, hoặc các dự án tự động hóa quy trình đòi hỏi tính nhất quán và độ chính xác cao.
- **Lợi ích:**
  - Ngôn ngữ chung cho cả nghiệp vụ (**business**) và kỹ thuật (**IT/dev**).
  - Hỗ trợ mô hình hóa xử lý ngoại lệ (**exceptions**), vòng lặp (**loops**) và luồng song song (**parallel activities**).
  - Nền tảng trực tiếp để lập trình cho các hệ thống tự động hóa và quản lý luồng công việc (**Workflow Management Systems**).
- **Ví dụ:** Quy trình phê duyệt khoản vay (nhận đơn $\to$ kiểm tra điểm tín dụng tự động $\to$ cổng rẽ nhánh duyệt/từ chối/yêu cầu thêm hồ sơ $\to$ gửi thông báo kết quả).

---

## 2. Bảng Hướng dẫn Lựa chọn Ký hiệu (Selection Matrix)

| Mục tiêu sử dụng | Ký hiệu khuyến nghị | Điểm mạnh cốt lõi |
| :--- | :--- | :--- |
| Trực quan hóa nhanh trình tự các bước đơn giản | **Flowchart** | Đơn giản, dễ hiểu cho mọi đối tượng |
| Thể hiện rõ trách nhiệm và các điểm bàn giao giữa các bên | **Swimlane Diagram** | Phân định rõ trách nhiệm (**Accountability**) |
| Mô hình hóa quy trình phức tạp, nhiều luật hoặc tự động hóa | **BPMN** | Toàn diện, chính xác, sẵn sàng tự động hóa |

---

## 3. Thuật ngữ viết tắt trong bài
- **BPMN (Business Process Model and Notation):** Ký hiệu và Mô hình Quy trình Nghiệp vụ (chuẩn mô hình hóa đồ họa cho quy trình kinh doanh).
- **OMG (Object Management Group):** Tổ chức Quản lý Đối tượng (tổ chức tiêu chuẩn quốc tế chuyên phát triển các chuẩn như UML, BPMN).
- **BA (Business Analyst):** Chuyên viên Phân tích Nghiệp vụ.
- **PM (Project Manager):** Quản lý Dự án.
