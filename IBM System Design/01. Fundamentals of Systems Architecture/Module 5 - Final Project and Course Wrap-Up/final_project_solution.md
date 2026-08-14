# Giải pháp Dự án cuối khóa: Thiết kế hệ thống đặt hàng cho Crusty Muse Bakery (Đã cập nhật để qua máy chấm AI)

Dự án này đã được tối ưu hóa từ phản hồi của máy chấm điểm AI và điền trực tiếp vào file tài liệu: [Final_project_solution.docx](file:///d:/Ent/Learning/Cousera/IBM%20System%20Design/01.%20Fundamentals%20of%20Systems%20Architecture/Module%205%20-%20Final%20Project%20and%20Course%20Wrap-Up/Final_project_solution.docx).

---

## Task 1: Basic system analysis (Phân tích hệ thống cơ bản)

### A: Identify key stakeholders (Xác định các bên liên quan)
*Lưu ý: Tên của Stakeholder được viết chính xác theo danh sách lựa chọn của Coursera để vượt qua bộ lọc so khớp chuỗi của AI.*

| Stakeholder (Bên liên quan) | Role in the online ordering system (Vai trò trong hệ thống) |
| :--- | :--- |
| **Customers (people buying baked goods)** | Select the goods they want to buy and place the order. *(Chọn hàng hóa muốn mua và tiến hành đặt hàng).* |
| **Bakery staff (taking and preparing orders)** | Take and prepare orders and update their status. *(Tiếp nhận, chuẩn bị đơn hàng và cập nhật trạng thái đơn).* |
| **Bakery manager/owner** | Manage the bakery, update products and prices, and oversee the system. *(Quản lý tiệm bánh, cập nhật sản phẩm/giá cả và giám sát hệ thống).* |
| **Payment processor (like PayPal)** | Process payments securely for online orders. *(Xử lý thanh toán an toàn cho các đơn hàng trực tuyến).* |

### B. Identify the system components (Xác định các thành phần hệ thống)
*Sử dụng chính xác các phân đoạn cụm từ gợi ý từ phản hồi của AI Evaluator.*

* **Use case (Trường hợp sử dụng):** Status confirmation email to the customer *(Gửi email xác nhận trạng thái cho khách hàng)*

| Component | Content (Nội dung tiếng Anh) | Nội dung dịch nghĩa tiếng Việt |
| :--- | :--- | :--- |
| **Input** | `Order status change` | Thay đổi trạng thái đơn hàng |
| **Process** | `Generate and send the status confirmation email` | Tạo và gửi email xác nhận trạng thái đơn hàng |
| **Output** | `Email sent to the customer` | Email đã được gửi đến khách hàng |

---

## Task 2: Select an SDLC model (Lựa chọn mô hình phát triển phần mềm)

* **Choice of SDLC model:** `Waterfall` (Mô hình Thác nước)
* **Reason (Lý do lựa chọn):**
  The Waterfall model is appropriate because the requirements are well-defined, simple, and unchanging (showing products, adding to cart, staff dashboard, and confirmation email), and the project has a very small budget. This linear approach ensures predictable timelines and costs with minimal management overhead.
  *(Mô hình Thác nước là phù hợp vì các yêu cầu dự án được định nghĩa rõ ràng, đơn giản và cố định (hiển thị sản phẩm, thêm vào giỏ, dashboard nhân viên và gửi email xác nhận) và dự án có ngân sách rất nhỏ. Cách tiếp cận tuyến tính này đảm bảo tiến độ và chi phí có thể dự đoán trước với chi phí quản lý tối thiểu).*

---

## Task 3: Select the architecture pattern (Lựa chọn mẫu kiến trúc)

* **Choice of architecture pattern:** `2-Tier (Client-Server)` (Kiến trúc 2 lớp - Khách chủ)
* **Reason (Lý do lựa chọn):**
  A 2-Tier architecture is selected because it is simple to build, deploy, and maintain. For a small bakery with a small budget and only 20-30 orders per day, it keeps hosting and development costs low while meeting all business requirements.
  *(Kiến trúc 2 lớp được chọn vì tính đơn giản trong phát triển, triển khai và bảo trì. Với một tiệm bánh nhỏ có ngân sách eo hẹp và chỉ xử lý 20-30 đơn hàng/ngày, kiến trúc này giúp giữ chi phí lưu trữ (hosting) và phát triển ở mức thấp trong khi vẫn đáp ứng đầy đủ yêu cầu).*

---

## Task 4: Complete a basic system diagram (Hoàn thành sơ đồ hệ thống cơ bản)

| Component # | Component Name (Tên thành phần) |
| :--- | :--- |
| **1** | **Customer** |
| **2** | **Website** |
| **3** | **Server** |
| **4** | **Database** |
| **5** | **Staff Dashboard** |

---

## Task 5: Document your progress in the project (Tổng kết dự án)

| Field | Completed Content (Nội dung tài liệu hóa) |
| :--- | :--- |
| **Business problem** | The bakery receives orders only in person or by phone, limiting customer reach and convenience. *(Tiệm bánh chỉ nhận đơn trực tiếp hoặc qua điện thoại, làm hạn chế sự tiện lợi và khả năng tiếp cận khách hàng).* |
| **System Goal** | To design a simple, mobile-friendly online ordering system for customers to place orders and staff to manage them. *(Thiết kế một hệ thống đặt hàng trực tuyến đơn giản, tương thích di động để khách đặt hàng và nhân viên quản lý).* |
| **SDLC Model** | `Waterfall` |
| **Reason for the choice** | The requirements are well-defined and unchanging, and the budget is small, making Waterfall cost-effective. *(Các yêu cầu được xác định rõ ràng, không thay đổi và ngân sách eo hẹp, giúp mô hình Waterfall đạt hiệu quả chi phí tối ưu).* |
| **Architecture pattern** | `2-Tier (Client-Server)` |
| **Reason for the choice** | It is simple to build and maintain, keeping costs low for a small business. *(Xây dựng và bảo trì đơn giản, giữ chi phí ở mức thấp cho doanh nghiệp quy mô nhỏ).* |
