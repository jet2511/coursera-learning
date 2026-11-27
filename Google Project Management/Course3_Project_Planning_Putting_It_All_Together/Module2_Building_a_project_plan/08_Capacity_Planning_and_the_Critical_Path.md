# Capacity Planning and the Critical Path (Lập kế hoạch Năng lực & Đường găng)

- **Khóa học:** Google Project Management Certificate | Course 3: Project Planning
- **Vị trí bài học:** Module 2: Building a project plan > Using estimation to set project timelines
- **Định dạng:** Video (~8 phút 07 giây)

---

## 1. Capacity & Capacity Planning (Năng lực & Lập kế hoạch Năng lực)

- **Capacity (Năng lực):** Lượng công việc mà một cá nhân hoặc tài nguyên được phân công có thể hoàn thành một cách hợp lý trong một khoảng thời gian nhất định.
- **Capacity Planning (Lập kế hoạch Năng lực):** Hành động phân bổ nhân sự và tài nguyên cho các đầu việc của dự án, nhằm xác định xem đội ngũ có đủ nguồn lực để hoàn thành công việc đúng hạn hay không.
  - *Ví dụ (Plant Pals):* Cần giao 100 chậu cây trong 5 ngày. Trung bình 1 tài xế giao được 4 đơn/ngày (8 giờ làm việc). Vậy trong 5 ngày, 1 tài xế giao được $4 \times 5 = 20$ đơn $\rightarrow$ Cần ít nhất **5 tài xế** để kịp tiến độ.
  - *Thực tế làm việc:* Dù một nhân sự dành 100% thời gian cho dự án, năng lực thực tế của họ vẫn bị giới hạn bởi các cuộc họp, việc khẩn cấp phát sinh và nhịp làm việc thông thường.

---

## 2. The Critical Path (Đường găng / Đường tới hạn)

- **Định nghĩa:** Là danh sách các **cột mốc bắt buộc (mandatory milestones)** và các **nhiệm vụ then chốt (critical tasks)** cần phải hoàn thành để dự án về đích đúng hạn.
- **Đặc trưng:**
  - Đại diện cho chuỗi công việc có **tổng thời lượng dài nhất từ đầu đến cuối** để đưa dự án tới thành công.
  - Bao gồm số lượng nhiệm vụ tối thiểu không thể thiếu (*bare minimum*).
  - Bất kỳ sự chậm trễ nào trên Critical Path đều trực tiếp làm **chậm trễ toàn bộ dự án**.
  - *Ví dụ (Plant Pals):* Tuyển chọn vendor cung ứng cây, phát triển website, giao hàng $\rightarrow$ Nằm trên Critical Path. Việc bổ sung bán thêm hoa là *"nice to have"* $\rightarrow$ Nằm ngoài Critical Path (*off the critical path*).

### Quy trình xác định Critical Path:
1. Liệt kê toàn bộ tasks và milestones (sử dụng WBS).
2. Xác định các mối phụ thuộc giữa các công việc (**Dependencies** - việc nào phải xong trước việc nào).
3. Ước tính thời gian cho từng task và vẽ sơ đồ từ điểm xuất phát đến kết thúc.
4. Con đường có chuỗi thời gian dài nhất chính là **Critical Path**.

---

## 3. Các yếu tố tác động đến Lập kế hoạch Năng lực & Lịch trình

### 3.1. Phân loại thứ tự thực thi
- **Parallel Tasks (Công việc song song):** Các công việc độc lập có thể triển khai cùng một lúc bởi các nhân sự khác nhau (ví dụ: vừa tuyển tài xế vừa lập trình website). Giúp tối ưu hóa và rút ngắn tiến độ (*create efficiencies*).
- **Sequential Tasks (Công việc tuần tự):** Các công việc phụ thuộc lẫn nhau, bắt buộc phải làm theo thứ tự nhất định (ví dụ: phải duyệt ngân sách xong mới được ký hợp đồng thuê vendor).

### 3.2. Ràng buộc về thời điểm bắt đầu
- **Fixed Start Date (Ngày bắt đầu cố định):** Ngày ấn định bắt buộc phải khởi động task để kịp mục tiêu (ví dụ: giao cây vào thứ Sáu thì bắt buộc phải lấy cây từ vườn ươm vào thứ Năm).
- **Earliest Start Date (Ngày bắt đầu sớm nhất):** Thời điểm sớm nhất có thể khởi động một task sau khi hoàn tất các thủ tục tiên quyết (ví dụ: vendor mới chỉ có thể bắt đầu làm việc sau 3 tuần kể từ họp kickoff vì cần chờ ký hợp đồng và duyệt Purchase Order).

---

## 4. Khái niệm Float / Slack (Độ trượt / Thời gian rảnh)

- **Float (hoặc Slack):** Khoảng thời gian một nhiệm vụ có thể trì hoãn mà **không làm ảnh hưởng** đến lịch trình tổng thể và kết quả cuối cùng của dự án.
- **Quy tắc vàng về Float và Critical Path:**
  - **Tasks trên Critical Path:** Có **Float = 0 (Zero float)**, nghĩa là không có khoảng dung sai nào cho sự chậm trễ (*no wiggle room*).
  - **Tasks có Float > 0:** Nằm **ngoài** Critical Path, có thể linh hoạt dời lịch mà không gây trễ hạn dự án.
