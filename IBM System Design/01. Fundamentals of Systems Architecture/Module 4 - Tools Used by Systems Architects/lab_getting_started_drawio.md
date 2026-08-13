# Lab: Getting Started with draw.io for Systems Modeling (Thực hành: Làm quen với draw.io trong Mô hình hóa Hệ thống)

Bản tóm tắt hướng dẫn thực hành xây dựng các sơ đồ kiến trúc cho **Hệ thống Quản lý Thư viện (Library Management System - LMS)** bằng công cụ trực tuyến draw.io.

---

### 1. Mục tiêu bài thực hành
*   Sử dụng thành thạo các tính năng cơ bản của draw.io (diagrams.net).
*   Xây dựng Sơ đồ ngữ cảnh (Context Diagram) để biểu diễn mức cao của hệ thống.
*   Xây dựng Sơ đồ luồng dữ liệu cấp 0 (Level 0 DFD) mô tả luồng trao đổi dữ liệu.
*   Xây dựng Sơ đồ ca sử dụng (Use Case Diagram) mô tả các tương tác của người dùng.

---

### 2. Các bước triển khai thực hành

#### Bài 1: Khởi động draw.io
1.  Truy cập [diagrams.net](https://app.diagrams.net/).
2.  Chọn **Create New Diagram** -> Đặt tên file (ví dụ: `LMS.drawio`) -> Chọn định dạng file lưu trữ (chọn Editable Bitmap Image `.png` hoặc định dạng `.drawio` gốc).
3.  Chọn **Blank Diagram** -> **Create** và chọn thư mục lưu trữ cục bộ.

#### Bài 2: Thiết kế Sơ đồ ngữ cảnh (Context Diagram)
Sơ đồ ngữ cảnh cung cấp góc nhìn tổng quan nhất về hệ thống và các tác nhân tương tác xung quanh.
*   **Thành phần trung tâm:** Vẽ một hình chữ nhật lớn ở giữa canvas, dán nhãn là `Library Management System`.
*   **Tác nhân bên ngoài (External Entities):** Vẽ 3 hình oval/ellipse xung quanh hệ thống trung tâm gồm:
    1.  `Student` (Sinh viên)
    2.  `Librarian` (Thủ thư)
    3.  `Admin` (Quản trị viên)
*   **Kết nối:** Dùng các đường mũi tên chỉ hướng để kết nối các tác nhân này với hệ thống trung tâm nhằm minh họa hướng đi của dữ liệu.

#### Bài 3: Thiết kế Sơ đồ luồng dữ liệu cấp 0 (Level 0 DFD)
DFD cấp 0 đi sâu hơn một bước bằng cách phân rã hệ thống thành các quy trình nghiệp vụ và kho chứa dữ liệu tĩnh.
*   Tạo trang mới (**Page-2**). Vẽ 3 thực thể tương tự bài trước: `Student`, `Librarian`, `Admin`.
*   **Thiết lập luồng công việc cho Sinh viên (`Student`):**
    *   Sử dụng hình trụ (Cylinder) làm kho dữ liệu dán nhãn `Book database` (Cơ sở dữ liệu sách).
    *   Vẽ 2 mũi tên khuỷu (Horizontal Elbow arrow) từ `Student` tới `Book database`. Dán nhãn văn bản trên mũi tên mô tả hành động: `Borrow book` (Mượn sách) và `Return book` (Trả sách).
*   **Thiết lập luồng công việc cho Thủ thư (`Librarian`):**
    *   Vẽ mũi tên kết nối từ `Librarian` tới `Book database` với nhãn mô tả: `Manage inventory` (Quản lý kho sách).
*   **Thiết lập luồng công việc cho Quản trị viên (`Admin`):**
    *   Vẽ một hình trụ làm kho dữ liệu dán nhãn `User records` (Hồ sơ người dùng).
    *   Vẽ mũi tên kết nối từ `Admin` tới `User records` với nhãn mô tả: `Manage users` (Quản lý người dùng).

#### Bài 4: Thiết kế Sơ đồ ca sử dụng (Use Case Diagram)
Use Case Diagram tập trung vào việc mô tả các chức năng cụ thể mà hệ thống cung cấp cho từng nhóm người dùng.
*   Tạo trang mới (**Page-3**). Vẽ 2 tác nhân (Actors): `Student` và `Librarian`.
*   Thêm các ca sử dụng (Use Cases) dạng hình oval và các kho dữ liệu dạng hình trụ:
    *   *Ca sử dụng:* `Login`, `Search book` (Tìm sách), `Borrow book`, `Return book`, `Update inventory` (Cập nhật kho).
    *   *Kho dữ liệu:* `User records`, `Book database`.
*   **Thiết lập các liên kết tương tác:**
    *   `Student` $\rightarrow$ `Login` $\rightarrow$ `User records` (Sinh viên đăng nhập để xác thực thông tin tài khoản).
    *   `Student` $\rightarrow$ `Search book`, `Borrow book`, `Return book` $\rightarrow$ `Book database` (Sinh viên mượn/trả/tìm sách tương tác trực tiếp với cơ sở dữ liệu sách).
    *   `Librarian` $\rightarrow$ `Update inventory` $\rightarrow$ `Book database` (Thủ thư cập nhật thông tin sách vào cơ sở dữ liệu sách).
