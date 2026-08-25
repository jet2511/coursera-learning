# Tóm tắt Video Demo: Project Management Tools (Ví dụ thực tế: "Develop a New Process")

Tài liệu này tổng hợp chi tiết demo thực hành cách áp dụng 3 công cụ quản lý dự án hàng đầu: **Gantt Chart**, **Milestone Chart**, và **Kanban Board** qua case study cụ thể: dự án *"Develop a New Process"*.

---

## 1. Gantt Chart – Lộ trình chi tiết & Tiến độ (Detailed Roadmap)

- **Cấu trúc biểu đồ:**
  - **Trục dọc (Vertical axis):** Danh sách các hoạt động / đầu việc của dự án (ví dụ: *Design new process*, *Measure new process*).
  - **Trục ngang (Horizontal axis):** Dòng thời gian dự án (trong ví dụ là 5 tháng: từ tháng 8 đến tháng 12).
  - **Thanh ngang (Horizontal bars):** Đại diện cho thời lượng thực hiện công việc (thanh càng dài, thời gian làm càng lâu).
- **Điểm nhấn trong Demo:**
  - *Design new process* chạy từ tháng 8 đến đầu tháng 9.
  - *Measure new process* chạy trong tháng 9.
  - Đoạn gối đầu (overlap) ở tuần đầu tháng 9 thể hiện 2 công việc chạy **song song (parallel)**.
- **Giá trị ứng dụng theo vai trò:**
  - **Project Managers:** Lập chuỗi thứ tự công việc, xác định các phụ thuộc (dependencies), theo dõi tiến độ và xử lý điểm nghẽn.
  - **Business Analysts (BA):** Đảm bảo yêu cầu (requirements), kiểm thử (testing), và phê duyệt (approvals) khớp với timeline bàn giao.
  - **Department/Functional Managers:** Xem lịch trình của team để phân bổ và điều phối nhân sự hiệu quả.
- **Khẩu quyết:** *"Gantt chart cho biết cái gì đang diễn ra, khi nào và theo thứ tự nào."*

---

## 2. Milestone Chart – Bảng điểm tiến độ (Progress Scoreboard)

- **Cấu trúc & Ký hiệu:**
  - Khung tương tự Gantt chart nhưng **sử dụng biểu tượng hình thoi (Diamonds)** để đánh dấu các mốc hoàn thành quan trọng thay vì các thanh ngang kéo dài.
  - **Quy ước màu sắc trong Demo:**
    - **Xanh đậm (Dark Blue):** Các hoạt động / mốc đã hoàn thành.
    - **Xám (Gray):** Các mốc chưa hoàn thành.
  - **Đường kẻ dọc (Vertical line):** Đại diện cho **thời điểm hiện tại**, giúp phân biệt rõ ràng mốc nào đã đạt được và mốc nào sắp tới.
- **Giá trị ứng dụng theo vai trò:**
  - **Executives & Sponsors:** Đánh giá nhanh trong vài giây dự án có đang đúng tiến độ (on track) hay không mà không bị ngợp bởi chi tiết vụn vặt.
  - **PMs & BAs:** Trình bày báo cáo cô đọng, tập trung vào kết quả then chốt.
- **Khẩu quyết:** *"Nếu Gantt chart là Bản đồ chi tiết (Roadmap), thì Milestone chart là Bảng điểm tiến độ (Scoreboard)."*

---

## 3. Kanban Board – Trực quan hóa luồng công việc thời gian thực (Real-time Workflow)

- **Cấu trúc & Quy tắc vận hành:**
  - **Cột trạng thái (Columns):** Thể hiện các giai đoạn công việc: `To Do` $\rightarrow$ `In Progress` $\rightarrow$ `Done` (kèm cột `Blocked` khi bị nghẽn).
  - **Thẻ việc (Task Cards):** Mỗi task là một thẻ di chuyển từ trái sang phải theo tiến trình thực tế.
  - **Mã màu thẻ (Color-coding) trong Demo:**
    - **Thẻ xanh dương (Blue):** Thuộc về Team A.
    - **Thẻ xanh lá (Green):** Thuộc về Team B.
    - Dùng để xác định rõ quyền sở hữu (ownership) hoặc mức độ ưu tiên.
- **Giá trị ứng dụng theo vai trò:**
  - **Tập trung vào luồng (Workflow) thay vì chỉ nhìn deadline:** Phát hiện tức thì các điểm nghẽn (ví dụ cột `In Progress` hoặc `Blocked` bị ứ đọng).
  - **BAs:** Theo dõi trạng thái triển khai của các yêu cầu chức năng.
  - **Functional Managers:** Cân bằng khối lượng công việc giữa các thành viên, phân bổ ưu tiên và đảm bảo tính trách nhiệm (accountability).

---

## 4. Tổng kết đối chiếu nhanh

| Công cụ | Đại diện trực quan | Trọng tâm cốt lõi | Câu hỏi chính giải quyết |
| :--- | :--- | :--- | :--- |
| **Gantt Chart** | Thanh ngang (Horizontal Bars) | Lịch trình & Phụ thuộc | *Cần làm gì, mất bao lâu, theo thứ tự nào?* |
| **Milestone Chart** | Hình thoi (Diamonds) + Đường mốc thời gian | Kết quả then chốt & Báo cáo | *Dự án có đang đúng hạn ở các mốc lớn không?* |
| **Kanban Board** | Bảng cột + Thẻ việc mã màu | Luồng việc & Trạng thái Real-time | *Hiện tại ai đang làm gì, có việc gì đang bị nghẽn không?* |
