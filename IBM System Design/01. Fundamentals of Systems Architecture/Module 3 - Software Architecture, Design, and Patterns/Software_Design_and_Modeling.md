# Thiết kế và Mô hình hóa Phần mềm (Software Design and Modeling)

Thiết kế phần mềm là quá trình tài liệu hóa các thành phần cấu trúc (structural components) và các thuộc tính hành vi (behavioral attributes) của phần mềm trước khi tiến hành phát triển thực tế.

---

## 1. Thiết kế Cấu trúc (Structured Design)
* **Khái niệm:** Chia nhỏ một bài toán phần mềm thành các phần tử giải pháp nhỏ hơn được tổ chức tốt gọi là **module** và **sub-module**. Thiết kế cấu trúc nhấn mạnh vào tính tổ chức của hệ thống để đạt được giải pháp.
* **Nguyên lý cốt lõi của một thiết kế tốt:**
  * **Tính kết dính cao (High Cohesion):** Tất cả các phần tử có liên quan chặt chẽ về mặt chức năng được gom cụm lại với nhau.
  * **Liên kết lỏng lẻo (Loose Coupling):** Giảm thiểu sự phụ thuộc và giao tiếp trực tiếp giữa các module khác nhau. Khi các module liên kết yếu với nhau, sự thay đổi ở một thành phần sẽ ít gây ảnh hưởng nhất đến các thành phần khác.
  * *Lưu ý:* Liên kết lỏng lẻo là nguyên lý kiến trúc cốt lõi được sử dụng rộng rãi trong các mẫu kiến trúc hướng dịch vụ (SOA) và microservices.

---

## 2. Mô hình Hành vi (Behavioral Models)
* **Khái niệm:** Mô tả những gì một hệ thống thực hiện (*what the system does*) mà không giải thích cách thức hệ thống triển khai hành vi đó như thế nào (*without explaining how it does it*).
* Giúp truyền tải hành vi tổng thể của hệ thống đến các bên liên quan.

---

## 3. Ngôn ngữ Mô hình hóa Thống nhất (UML - Unified Modeling Language)
* **Khái niệm:** Là một ngôn ngữ mô hình hóa tiêu chuẩn nhằm trực quan hóa kiến trúc, thiết kế và cách thức triển khai của các hệ thống phần mềm phức tạp.
* **Đặc tính:** Độc lập với ngôn ngữ lập trình (programming language agnostic), giúp nhà phát triển dễ dàng đọc hiểu bất kể họ đang lập trình bằng ngôn ngữ nào.
* **Phân loại chính:** Sơ đồ UML được chia thành hai nhóm chính là **Sơ đồ cấu trúc (Structural)** và **Sơ đồ hành vi (Behavioral)**.
* **Lợi ích của việc sử dụng UML:**
  * Cho phép lập kế hoạch các tính năng trước khi lập trình, giúp tiết kiệm thời gian và chi phí.
  * Giúp các thành viên mới hoặc lập trình viên mới chuyển đội nắm bắt dự án một cách nhanh chóng.
  * Hỗ trợ giao tiếp và đồng thuận dễ dàng hơn giữa nhóm kỹ thuật và phi kỹ thuật.
  * Giúp các lập trình viên điều hướng mã nguồn (source code) dễ dàng hơn nhờ hiểu rõ mối quan hệ giữa các module.

---

## 4. Các Sơ đồ Hành vi Tiêu biểu
* **Sơ đồ Chuyển trạng thái (State Transition Diagram):**
  * Là một tập hợp các trạng thái (states) và sự kiện (events) mô tả các trạng thái khác nhau của hệ thống và các sự kiện kích hoạt sự thay đổi từ trạng thái này sang trạng thái khác.
  * *Ví dụ:* Mô hình hóa quy trình bệnh nhân đi khám bệnh tại phòng khám (Trạng thái: Chờ đợi -> Làm xét nghiệm -> Gặp bác sĩ).
* **Sơ đồ Tương tác (Interaction Diagram):**
  * Dùng để mô hình hóa tính chất động (dynamic nature) của hệ thống phần mềm bằng cách trực quan hóa các đối tượng và mối quan hệ giữa chúng.
  * **Sơ đồ Tuần tự (Sequence Diagram):** Là một dạng sơ đồ tương tác hiển thị sự giao tiếp giữa các đối tượng theo thứ tự thời gian.
  * *Ví dụ:* Mô tả các bước tương tác giữa bệnh nhân, hệ thống và cơ sở dữ liệu khi đặt lịch hẹn khám trực tuyến.

---

## 5. Tóm tắt nhanh (Key Takeaways)
1. Thiết kế cấu trúc chia nhỏ hệ thống thành các module và sub-module có tính **kết dính cao (cohesive)** và **liên kết lỏng lẻo (loosely coupled)**.
2. Mô hình hành vi tập trung vào những gì hệ thống làm thay vì cách hệ thống thực hiện.
3. UML là ngôn ngữ chuẩn hóa độc lập với code, giúp tối ưu thời gian, chi phí thiết kế và hỗ trợ giao tiếp hiệu quả.
4. Sơ đồ chuyển trạng thái hiển thị các trạng thái và sự kiện kích hoạt; sơ đồ tương tác (như sơ đồ tuần tự) hiển thị sự giao tiếp giữa các đối tượng theo thời gian.
