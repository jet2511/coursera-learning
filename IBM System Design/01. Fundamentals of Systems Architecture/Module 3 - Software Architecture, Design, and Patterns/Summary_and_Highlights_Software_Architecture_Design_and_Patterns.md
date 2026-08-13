# Tóm tắt và Điểm nổi bật: Kiến trúc, Thiết kế và Mẫu Phần mềm (Summary and Highlights: Software Architecture, Design, and Patterns)

Chúc mừng bạn đã hoàn thành module này. Dưới đây là tóm tắt toàn bộ các kiến thức cốt lõi đã học:

---

## 1. Kiến trúc và Thiết kế Phần mềm
* **Kiến trúc phần mềm (Software Architecture):** Hoạt động như một bản thiết kế (blueprint) hệ thống, thể hiện tầm quan trọng của việc có một thiết kế kiến trúc tốt ngay từ đầu.
* **Thiết kế cấu trúc (Structured Design):** Phân rã một bài toán phần mềm thành các phần tử giải pháp nhỏ hơn và được tổ chức tốt.
* **Mô hình hành vi (Behavioral Models):** Mô tả những gì hệ thống làm (hành vi) mà không đi sâu vào giải thích cách thức hệ thống triển khai hành vi đó.

---

## 2. Mô hình hóa với UML (Unified Modeling Language)
* Việc xây dựng sơ đồ UML giúp tiết kiệm thời gian và chi phí nhờ:
  * Giúp các nhà phát triển nhanh chóng nắm bắt và tiếp cận dự án.
  * Lập kế hoạch trước các tính năng trước khi tiến hành code.
  * Dễ dàng điều hướng và đọc hiểu mã nguồn.
* **Các loại sơ đồ UML phổ biến:** Sơ đồ chuyển trạng thái (state transition), sơ đồ tương tác (interaction), và sơ đồ lớp (class).

---

## 3. Lập trình Hướng Đối tượng (OOP)
* **Đối tượng (Objects):** Chứa dữ liệu (data) và các hành vi (behaviors) quy định những hành động đối tượng có thể thực hiện.
* **Lớp (Classes):** Đóng vai trò là bản thiết kế hoặc khuôn mẫu để tạo ra các đối tượng cụ thể.

---

## 4. Kiến trúc Hướng Dịch vụ (SOA) và Hệ thống Phân tán
* **Kiến trúc hướng dịch vụ (SOA):** Gồm các dịch vụ liên kết lỏng lẻo (loosely coupled) giao tiếp với nhau thông qua một giao thức truyền thông trên mạng.
* **Hệ thống phân tán (Distributed Systems):** Vận hành nhiều dịch vụ nằm trên các máy tính khác nhau, nhưng hiển thị đối với người dùng cuối như một hệ thống nhất quán duy nhất.

---

## 5. Mẫu Kiến trúc (Architectural Patterns)
* Là giải pháp có thể tái sử dụng cho các vấn đề kiến trúc thường gặp.
* **Các mẫu kiến trúc phổ biến:** 2-tier (2 lớp), 3-tier (3 lớp), event-driven (hướng sự kiện), peer-to-peer (ngang hàng), và microservices.
* Có thể kết hợp hai hoặc nhiều mẫu thiết kế trong cùng một hệ thống, tuy nhiên một số mẫu loại trừ lẫn nhau (mutually exclusive).

---

## 6. Môi trường và Hạ tầng Triển khai
* **Các môi trường ứng dụng:** Development (phát triển), Testing/QA (kiểm thử), Staging (tiền sản xuất), và Production (sản xuất).
* **Đặc tính môi trường Production:** Phức tạp hơn nhiều so với các môi trường tiền sản xuất vì phải đáp ứng các yêu cầu phi chức năng quan trọng như: tải thực tế (load), bảo mật (security), độ tin cậy (reliability), và khả năng mở rộng (scalability).
* **Phương thức triển khai:** Triển khai tại chỗ (**On-premises**) trên phần cứng truyền thống hoặc sử dụng điện toán đám mây (**Public, Private, hoặc Hybrid Cloud**).
* **Thành phần hạ tầng Production phổ biến:** Tường lửa (firewall), bộ cân bằng tải (load balancer), máy chủ web (web server), máy chủ ứng dụng (application server), máy chủ ủy quyền (proxy server), và máy chủ cơ sở dữ liệu (database server).

---

## 7. Kiểm thử Mô phỏng và Sử dụng Công cụ
* **Mô phỏng (Simulations):** Tái tạo quy trình trong thế giới thực, giúp các chuyên gia hệ thống kiểm thử luồng công việc, đánh giá hiệu năng, dự báo rủi ro và xác định điểm nghẽn (bottlenecks) trước khi triển khai hệ thống thực tế.
* **Thực hành tốt nhất về công cụ:** Nhấn mạnh vào tính đơn giản, nhất quán, truyền thông rõ ràng, ghi chép tài liệu đầy đủ các quyết định (như ADR) và đào tạo đội ngũ để đảm bảo cộng tác hiệu quả.
