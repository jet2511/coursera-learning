# Tổng hợp & Điểm nhấn: Ngôn ngữ Mô hình hóa Thống nhất (UML) trong Kiến trúc Hệ thống

Tài liệu này tổng hợp toàn bộ các nội dung và điểm nhấn cốt lõi về **Ngôn ngữ Mô hình hóa Thống nhất (Unified Modeling Language - UML)** trong thiết kế và xây dựng kiến trúc hệ thống.

---

## 1. Bản chất & Vai trò của UML
* **Định nghĩa:** UML là ngôn ngữ mô hình hóa tiêu chuẩn hóa được sử dụng để trực quan hóa, đặc tả, xây dựng và lập tài liệu về cấu trúc cũng như hành vi của hệ thống phần mềm.
* **Phân loại chính:**
  * **Sơ đồ cấu trúc (Structural Diagrams):** Biểu diễn kiến trúc tĩnh (ví dụ: *Class Diagram*, *Component Diagram*, *Object Diagram*).
  * **Sơ đồ hành vi (Behavioral Diagrams):** Biểu diễn hành vi động theo thời gian (ví dụ: *Use Case Diagram*, *Sequence Diagram*, *Activity Diagram*, *State Machine Diagram*).
* **Lợi ích:** Nâng cao hiệu quả giao tiếp giữa các bên liên quan, hỗ trợ phân tích yêu cầu, phát hiện lỗi sớm, cung cấp bản thiết kế kỹ thuật (blueprint) có tính module hóa, dễ mở rộng, bảo trì và đóng vai trò như tài liệu hệ thống.
* **Khả năng tương thích:** Áp dụng linh hoạt cho cả mô hình phát triển **Agile** lẫn **Waterfall**, đồng thời bổ trợ hoàn hảo cho **DFD** và **ERD**.
* **Thực hành tốt nhất (Best Practices):** Bắt đầu từ mức độ đơn giản (Start simple), sử dụng các công cụ vẽ chuẩn hóa, giữ sơ đồ rõ ràng tránh rác thông tin, và liên tục đánh giá - tinh chỉnh cùng các bên liên quan.

---

## 2. Điểm nhấn về Sơ đồ Lớp & Sơ đồ Tuần tự

### **a. Sơ đồ Lớp (Class Diagram - Góc nhìn Tĩnh)**
* Mô tả các lớp (Classes), thuộc tính (Attributes), phương thức (Operations) và mối quan hệ tĩnh giữa chúng.
* **Cấu trúc 1 lớp:** Hình chữ nhật chia làm 3 phần (*Tên lớp*, *Thuộc tính*, *Phương thức*).
* **Các mối quan hệ:**
  * *Association (Liên kết)*
  * *Aggregation (Thu nạp - "has-a")*
  * *Composition (Hợp thành - "owns-a")*
  * *Inheritance (Kế thừa - "is-a")*
  * *Dependency (Phụ thuộc)*
  * *Multiplicity (Bản số: 1:1, 1:N, N:1, N:N)*.

### **b. Sơ đồ Tuần tự (Sequence Diagram - Góc nhìn Động)**
* Mô tả cách các đối tượng tương tác với nhau theo trình tự thời gian (từ trên xuống dưới) để hoàn thành một Use Case hoặc chức năng.
* **Các thành phần chính:**
  * *Đường sinh mệnh (Lifelines)*
  * *Thông điệp (Messages):* Đồng bộ (Synchronous), Bất đồng bộ (Asynchronous), Phản hồi (Return)
  * *Thanh kích hoạt (Activation bars)*
  * *Khung tương tác (Fragments):* Khối điều kiện (`alt`, `opt`) hoặc vòng lặp (`loop`).

---

## 3. Điểm nhấn về Sơ đồ Hoạt động & Sơ đồ Trạng thái

### **a. Sơ đồ Hoạt động (Activity Diagram - Luồng Quy trình & Tiến trình)**
* Biểu diễn luồng công việc (workflows), quy trình nghiệp vụ hoặc kịch bản Use Case theo dạng lưu đồ tiến trình.
* **Các thành phần chính:**
  * *Nút Bắt đầu & Kết thúc (Start & End nodes)*
  * *Hoạt động/Tác vụ (Activities)*
  * *Chuyển tiếp (Transitions)*
  * *Rẽ nhánh quyết định (Decision nodes)*
  * *Luồng song song (Parallel flows: Fork / Join)*
  * *Phân làn trách nhiệm (Swimlanes).*

### **b. Sơ đồ Trạng thái (State Machine Diagram - Vòng đời Đối tượng)**
* Mô tả vòng đời của **một đối tượng duy nhất**, ghi nhận cách đối tượng chuyển dịch giữa các trạng thái khi có sự kiện tác động.
* **Các thành phần chính:**
  * *Trạng thái (States)*
  * *Chuyển đổi trạng thái (Transitions)*
  * *Sự kiện kích hoạt (Events)*
  * *Điều kiện bảo vệ (Guard conditions `[Condition]`)*
  * *Hành động (Actions).*

---

## 4. Bảng Tổng kết Các Loại Sơ đồ UML Cốt lõi

| Loại sơ đồ UML | Phân nhóm | Mục đích cốt lõi | Thành phần chính |
| :--- | :--- | :--- | :--- |
| **Use Case Diagram** | Hành vi | Định nghĩa phạm vi và chức năng từ góc nhìn người dùng/hệ thống ngoài. | Actor, Use Case, Association, `<<include>>`, `<<extend>>`. |
| **Class Diagram** | Cấu trúc | Bản thiết kế cấu trúc dữ liệu, OOP và quan hệ tĩnh. | Class (Name, Attributes, Methods), Association, Inheritance, Multiplicity. |
| **Sequence Diagram** | Hành vi | Thể hiện thứ tự trao đổi message/API giữa các đối tượng theo thời gian. | Lifeline, Activation Bar, Sync/Async Messages, Return, Fragments. |
| **Activity Diagram** | Hành vi | Thể hiện luồng tiến trình, rẽ nhánh điều kiện và các tác vụ chạy song song. | Start/End, Action, Decision (Diamond), Fork/Join, Swimlanes. |
| **State Diagram** | Hành vi | Theo dõi vòng đời và sự chuyển đổi trạng thái của một đối tượng cụ thể. | Initial/Final States, State, Transition, Event, Guard Condition. |
