# Introduction to Use Cases

Tóm tắt nội dung video giới thiệu về Trường hợp sử dụng (**Use Case**) trong phân tích kinh doanh và mô hình hóa quy trình.

---

## 1. Bản chất & Vai trò của Use Case
- **Khái niệm:** Use Case (Trường hợp sử dụng) mô tả cách thức người dùng/thực thể tương tác (**Actors**) với hệ thống nhằm đạt được một mục tiêu cụ thể. Nó thể hiện chuỗi hành động của tác nhân và phản hồi tương ứng từ hệ thống.
- **2 Mục đích cốt lõi:**
  1. Ghi nhận và làm rõ nhu cầu của người dùng đối với hệ thống.
  2. Đóng vai trò là bản thiết kế tổng thể (**blueprint**) định hướng thiết kế phần mềm bám sát nhu cầu thực tế.
- **Đối tượng sử dụng rộng rãi:** BA (**Business Analyst** - Chuyên viên Phân tích Nghiệp vụ), PM (**Project Manager** - Quản lý Dự án), nhà phát triển phần mềm và các cấp quản lý nghiệp vụ.

---

## 2. 6 Thành phần cấu trúc cốt lõi của Use Case

| Thành phần | Ý nghĩa | Ví dụ trong "Purchase Product" |
| :--- | :--- | :--- |
| **Title** (Tiêu đề) | Tên ngắn gọn tóm tắt mục tiêu của Use Case. | *Purchase Product* (Mua hàng). |
| **Actors** (Tác nhân) | Thực thể tương tác với hệ thống (người dùng, hệ thống ngoài, thiết bị). | *Customer* (Khách hàng) & *Payment Gateway* (Cổng thanh toán bên thứ ba). |
| **Preconditions** (Tiền điều kiện) | Điều kiện bắt buộc phải thỏa mãn trước khi Use Case bắt đầu. | Khách hàng đã đăng nhập tài khoản; sản phẩm còn hàng trong kho. |
| **Main Flow** (Luồng chính / Happy Path) | Trình tự các bước chuẩn mực để tác nhân hoàn thành mục tiêu. | Duyệt hàng $\to$ Thêm vào giỏ $\to$ Checkout $\to$ Nhập thông tin & chọn phương thức $\to$ Thanh toán & hiển thị xác nhận. |
| **Alternate Flows** (Luồng thay thế / Ngoại lệ) | Các nhánh rẽ do lỗi hoặc sự lựa chọn khác của người dùng. | Hết hàng (hiển thị thông báo); thanh toán thất bại (cho phép nhập lại thông tin thẻ). |
| **Post-conditions** (Hậu điều kiện) | Trạng thái của hệ thống sau khi Use Case thực thi thành công. | Đơn hàng được ghi nhận trong CSDL (**Database**); gửi email xác nhận cho khách hàng. |

---

## 3. Lợi ích đối với Phân tích Kinh doanh
- **Cầu nối giao tiếp (Communication):** Cung cấp ngôn ngữ chung, rõ ràng giữa BA, Developer và End-User (Người dùng cuối).
- **Nâng cao trải nghiệm người dùng (UX - User Experience):** Tập trung vào tương tác thực tế, đảm bảo hệ thống đáp ứng đúng nhu cầu.
- **Cơ sở xây dựng Test Case:** Hỗ trợ đội ngũ QA (**Quality Assurance** - Đảm bảo chất lượng) tạo kịch bản kiểm thử, xác thực chức năng hệ thống trước khi triển khai.

---

## 4. Best Practices (Thực hành tốt) & Pitfalls (Cạm bẫy cần tránh)

### Nguyên tắc thực hành tốt (Best Practices):
- **Keep it simple (Giữ đơn giản):** Sử dụng ngôn ngữ rõ ràng, tránh từ ngữ chuyên ngành (jargon) gây khó hiểu cho stakeholder.
- **Be specific (Cụ thể, rõ ràng):** Định nghĩa chi tiết từng thành phần, tránh mô tả mơ hồ gây sai lệch khi lập trình.
- **Involve stakeholders (Gắn kết các bên):** Phối hợp chặt chẽ với người dùng thực tế và SME (**Subject Matter Expert** - Chuyên gia Nghiệp vụ).
- **Use visuals (Sử dụng trực quan):** Kết hợp sơ đồ Use Case (**Use Case Diagram**) hoặc lưu đồ (**Flowchart**) để làm rõ ngữ cảnh.

### Sai lầm phổ biến cần tránh (Common Pitfalls):
- **Overcomplicating (Phức tạp hóa kịch bản):** Đưa quá nhiều chi tiết vụn vặt làm mất đi bức tranh tổng quan.
- **Ignoring alternate flows (Bỏ qua luồng rẽ nhánh/lỗi):** Chỉ vẽ "Happy Path" dẫn đến thiếu sót yêu cầu xử lý ngoại lệ khi code.
- **Neglecting reviews (Bỏ qua bước duyệt):** Không rà soát lại với stakeholder trước khi bắt tay vào triển khai.

---

## 5. Ví dụ ứng dụng thực tế theo ngành
- **E-commerce (Thương mại điện tử - ví dụ: Amazon):** *Register Account, Add to Cart, Process Payment* $\to$ tối ưu hành trình mua hàng và thiết kế UI (**User Interface** - Giao diện người dùng).
- **Banking (Ngân hàng - ví dụ: Chase):** *Withdraw Cash, Transfer Funds, Apply for Loan* $\to$ đảm bảo yêu cầu chức năng lẫn phi chức năng như bảo mật và hiệu năng.
- **Healthcare (Y tế):** *Schedule Appointment, Access Patient Records* $\to$ số hóa hồ sơ bệnh án và tuân thủ quy định ngành y tế.
- **Transportation (Vận tải - ví dụ: Uber):** *Request Ride, Rate Driver* $\to$ luồng trải nghiệm liền mạch từ đặt xe đến đánh giá tài xế.
- **CRM (Customer Relationship Management - ví dụ: Salesforce):** *Create Lead, Close Deal* $\to$ quy trình hóa luồng bán hàng cho doanh nghiệp.
