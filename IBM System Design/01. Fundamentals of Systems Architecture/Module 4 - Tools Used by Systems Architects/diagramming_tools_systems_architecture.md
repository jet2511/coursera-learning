# Diagramming Tools for Systems Architecture (Công cụ vẽ sơ đồ cho kiến trúc hệ thống)

Bản tóm tắt nội dung học tập về định nghĩa, tầm quan trọng và các kỹ thuật vẽ sơ đồ (diagramming techniques) cốt lõi được sử dụng bởi các chuyên gia kiến trúc hệ thống.

---

### 1. Khái niệm và Vai trò của Vẽ sơ đồ
*   **Định nghĩa:** Vẽ sơ đồ là phương pháp cấu trúc để biểu diễn trực quan các thông tin, hệ thống, quy trình, dữ liệu hoặc các tương tác. 
*   **Tầm quan trọng:** Vẽ sơ đồ không chỉ dừng lại ở nhiệm vụ viết tài liệu (documentation). Đây là một **công cụ tư duy và giao tiếp** mạnh mẽ giúp:
    *   Làm rõ các ý tưởng và cấu trúc phức tạp.
    *   Phát hiện sớm các lỗi thiết kế (ví dụ: thiếu dữ liệu, đứt gãy quy trình, phân định trách nhiệm không rõ ràng).
    *   Thúc đẩy sự cộng tác hiệu quả giữa stakeholders, nhà phát triển và người dùng.
    *   Tạo ra bản thiết kế chi tiết (blueprint), giảm thiểu hiểu lầm và giảm thiểu việc phải làm lại (rework).

---

### 2. Các kỹ thuật vẽ sơ đồ cốt lõi

#### A. Sơ đồ luồng dữ liệu (Dataflow Diagrams - DFDs)
*   **Mục đích:** Theo dõi luồng di chuyển của dữ liệu, các điểm xử lý làm biến đổi dữ liệu và nơi lưu trữ.
*   **Ký hiệu chuẩn:**
    *   *Quy trình (Processes):* Hình tròn hoặc hình chữ nhật bo góc biểu diễn hoạt động xử lý dữ liệu.
    *   *Kho dữ liệu (Data Stores):* Hình chữ nhật hở biểu diễn nơi lưu trữ dữ liệu tĩnh.
    *   *Thực thể ngoài (External Entities):* Hình vuông biểu diễn các tác nhân bên ngoài gửi hoặc nhận dữ liệu.
    *   *Luồng dữ liệu (Dataflows):* Mũi tên chỉ hướng di chuyển của dữ liệu.
*   **Đặc điểm:** Hỗ trợ phân rã hệ thống từ tổng quát (Level 0 DFD - sơ đồ ngữ cảnh) sang các mức chi tiết hơn (Level 1, Level 2,...) để dễ quản lý.

#### B. Sơ đồ quan hệ thực thể (Entity Relationship Diagrams - ERDs)
*   **Mục đích:** Mô hình hóa dữ liệu (data modeling) làm cơ sở thiết kế cơ sở dữ liệu quan hệ, đảm bảo tính toàn vẹn dữ liệu và hỗ trợ quá trình chuẩn hóa (normalization).
*   **Thành phần chính:**
    *   *Thực thể (Entities):* Đối tượng cụ thể (ví dụ: Khách hàng, Đơn hàng).
    *   *Thuộc tính (Attributes):* Đặc điểm của thực thể (ví dụ: Tên khách hàng, Ngày đặt hàng).
    *   *Mối quan hệ (Relationships):* Cách các thực thể liên kết với nhau.

#### C. Sơ đồ ca sử dụng (Use Case Diagrams - UML)
*   **Mục đích:** Xác định các yêu cầu chức năng từ góc nhìn của người dùng (user's perspective).
*   **Thành phần chính:**
    *   *Actor (Tác nhân):* Người dùng hoặc hệ thống bên ngoài tương tác với hệ thống.
    *   *Use Case (Ca sử dụng):* Các hành động hoặc dịch vụ mà hệ thống thực hiện để hoàn thành mục tiêu của Actor.
    *   *Association (Mối liên kết):* Đường nối Actor với Use Case tham gia.

#### D. Sơ đồ hoạt động (Activity Diagrams - UML)
*   **Mục đích:** Biểu diễn tuần tự các bước trong một quy trình nghiệp vụ hoặc luồng điều khiển của hệ thống (tương tự lưu đồ - flowchart truyền thống nhưng theo chuẩn UML).
*   **Ứng dụng:** Giúp hiểu rõ logic vận hành, phát hiện các điểm nghẽn và tối ưu hóa quy trình.

#### E. Sơ đồ tuần tự (Sequence Diagrams - UML)
*   **Mục đích:** Tập trung vào các tương tác truyền nhận thông điệp giữa các đối tượng/thành phần hệ thống theo trình tự thời gian.
*   **Thành phần chính:**
    *   *Đường đời (Lifelines):* Biểu diễn sự tồn tại của đối tượng/tác nhân theo trục dọc thời gian.
    *   *Thông điệp (Messages):* Tín hiệu trao đổi giữa các lifelines.
    *   *Thanh kích hoạt (Activation Bars):* Biểu thị khoảng thời gian đối tượng đang thực hiện hành động.

#### F. Sơ đồ lớp (Class Diagrams - UML)
*   **Mục đích:** Mô hình hóa cấu trúc tĩnh của hệ thống theo lập trình hướng đối tượng (OOP).
*   **Thành phần chính:** Định nghĩa các Class (Lớp) bao gồm các thuộc tính (attributes) và phương thức (methods/operations), cùng các liên kết (associations) và quan hệ kế thừa (generalization).
