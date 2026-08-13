# Giới thiệu về Kiến trúc Phần mềm (Introduction to Software Architecture)

Kiến trúc phần mềm (Software Architecture) được thiết kế và ghi nhận trong tài liệu ở giai đoạn thiết kế (Design Phase) của vòng đời phát triển phần mềm (SDLC).

---

## 1. Kiến trúc Phần mềm là gì?
* **Định nghĩa đơn giản:** Là cấu trúc tổ chức của một hệ thống.
* **Vai trò:** Hoạt động như một bản thiết kế (blueprint) để các lập trình viên sử dụng nhằm phát triển các thành phần tương tác của phần mềm.
* **Đặc điểm:**
  * Bao gồm các cấu trúc cơ bản của hệ thống và giải thích hành vi của hệ thống đó.
  * Định nghĩa cách các thành phần tương tác với nhau, với môi trường vận hành (operating environment) và các nguyên lý thiết kế hệ thống.
  * Ghi lại các quyết định thiết kế ban đầu (early design decisions) - những quyết định thường rất tốn kém để thay đổi một khi đã triển khai.
  * Giải quyết các khía cạnh phi chức năng (non-functional capabilities/requirements) như: hiệu năng (performance), khả năng mở rộng (scalability), khả năng bảo trì (maintainability), khả năng tương tác (interoperability), bảo mật (security) và khả năng quản lý (manageability).

---

## 2. Tầm quan trọng của một Kiến trúc Phần mềm tốt
* **Cơ sở giao tiếp:** Giúp cân bằng các nhu cầu khác nhau của các bên liên quan (stakeholders) và đóng vai trò làm cầu nối thông tin giữa các thành viên trong đội ngũ phát triển.
* **Định hình lập trình:** Đại diện cho các quyết định thiết kế sớm nhất và các quyết định này sẽ ảnh hưởng trực tiếp đến các quyết định lập trình chi tiết về sau.
* **Tăng tính linh hoạt (Agility):** Giúp hệ thống dễ dàng thích ứng trước sự thay đổi của yêu cầu nghiệp vụ.
* **Kéo dài tuổi thọ hệ thống:** Một kiến trúc có tổ chức tốt giúp tăng tuổi thọ của phần mềm ngay cả khi các chi tiết triển khai công nghệ bên dưới thay đổi.

---

## 3. Tác động đến Công nghệ (Tech Stack) & Môi trường Triển khai (Production Environment)
* **Định hướng lựa chọn Tech Stack:** 
  * Kiến trúc tập trung vào các yêu cầu phi chức năng, vì vậy việc lựa chọn một Tech Stack (danh sách các công nghệ bao gồm phần mềm, ngôn ngữ lập trình, thư viện, framework) phù hợp để đáp ứng các yêu cầu này là tối quan trọng.
  * Kiến trúc sư phải nắm rõ ưu và nhược điểm của từng stack để dự báo trước các nhu cầu phát triển.
* **Định hướng Môi trường Triển khai:**
  * Kiến trúc dẫn dắt các lựa chọn về cơ sở hạ tầng chạy và cung cấp ứng dụng đến người dùng cuối.
  * Môi trường production bao gồm các hạ tầng như: servers, load balancers (bộ cân bằng tải), và databases (cơ sở dữ liệu).

---

## 4. Các sản phẩm bàn giao (Artifacts) trong giai đoạn thiết kế kiến trúc
Để truyền tải thiết kế đến các stakeholders, nhiều tài liệu/sản phẩm bàn giao được tạo ra bao gồm:

* **Tài liệu Thiết kế Phần mềm (Software Design Document - SDD):**
  * Là tập hợp các đặc tả kỹ thuật hướng dẫn chi tiết cách thực thi thiết kế.
  * Cung cấp mô tả chức năng của phần mềm và các yếu tố cân nhắc thiết kế như: giả định (assumptions), phụ thuộc (dependencies), ràng buộc (constraints), yêu cầu (requirements), mục tiêu (objectives) và phương pháp luận (methodologies).
* **Sơ đồ Kiến trúc (Architectural Diagram):**
  * Hiển thị các thành phần (components), mối tương tác, ràng buộc và ranh giới của chúng.
  * Thể hiện các mẫu kiến trúc (architectural patterns - giải pháp tổng quát, có thể tái sử dụng cho các vấn đề thường gặp) được áp dụng.
* **Sơ đồ UML (Unified Modeling Language Diagrams):**
  * Sử dụng ký hiệu độc lập với ngôn ngữ lập trình để biểu diễn cấu trúc và hành vi của hệ thống.

---

## 5. Tóm tắt nhanh (Key Takeaways)
1. Kiến trúc phần mềm là bản thiết kế hệ thống và đại diện cho cấu trúc tổ chức của ứng dụng.
2. Thiết kế kiến trúc tốt là nền tảng giao tiếp, khó thay đổi khi đã bắt đầu code và hỗ trợ tốt cho việc thay đổi yêu cầu sau này.
3. Kiến trúc ảnh hưởng lớn đến việc lựa chọn công nghệ (Tech Stack) và hạ tầng triển khai thực tế (Production Environment).
4. Các tài liệu đầu ra chính gồm: SDD, sơ đồ kiến trúc và sơ đồ UML.
