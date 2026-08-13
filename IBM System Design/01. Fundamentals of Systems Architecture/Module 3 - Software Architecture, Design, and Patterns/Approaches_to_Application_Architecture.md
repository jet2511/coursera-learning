# Các phương pháp tiếp cận Kiến trúc Ứng dụng (Approaches to Application Architecture)

Tài liệu này tổng hợp các kiến thức về Kiến trúc hướng thành phần (Component-Based), Kiến trúc hướng dịch vụ (SOA) và các đặc tính của Hệ thống phân tán (Distributed Systems).

---

## 1. Thành phần (Component) là gì?
* **Định nghĩa:** Là một đơn vị chức năng độc lập, được bao đóng (encapsulated functionality) và đóng vai trò là một phần của ứng dụng khi kết hợp với các thành phần khác.
* **6 Đặc tính cốt lõi của một Component:**
  1. **Có thể tái sử dụng (Reusable):** Thiết kế để sử dụng trong nhiều ứng dụng khác nhau.
  2. **Có thể thay thế (Replaceable):** Dễ dàng thay thế bằng một component khác có cùng giao diện.
  3. **Độc lập (Independent):** Không phụ thuộc trực tiếp vào các component khác.
  4. **Có thể mở rộng (Extensible):** Có thể bổ sung hành vi mới mà không cần chỉnh sửa các component khác.
  5. **Bao đóng (Encapsulated):** Gom nhóm dữ liệu và phương thức bên trong để ẩn trạng thái nội bộ, không để lộ chi tiết triển khai cụ thể.
  6. **Không phụ thuộc ngữ cảnh (Non-context-specific):** Thiết kế để hoạt động trong nhiều môi trường khác nhau. Dữ liệu thiết lập trạng thái nên được truyền vào (pass in) thay vì lưu trữ cứng hoặc do component tự truy cập.
* **Ví dụ về Component:** Một API dùng chung để kết nối database; Data Access Object (DAO) giúp chuyển đổi database mà ứng dụng không cần biết; bộ điều khiển (Controller) điều phối luồng dữ liệu.

---

## 2. Kiến trúc hướng Thành phần (Component-Based Architecture)
* Tập trung vào phân rã thiết kế hệ thống thành các component logic độc lập.
* Cung cấp mức độ trừu tượng (abstraction) cao hơn thiết kế hướng đối tượng (OO).
* Định nghĩa và triển khai các component độc lập liên kết lỏng lẻo (loosely coupled) để cùng nhau tạo nên ứng dụng.

---

## 3. Dịch vụ (Service) vs. Thành phần (Component)
* **Dịch vụ (Service):**
  * Cũng là một đơn vị chức năng nhưng được thiết kế để **triển khai độc lập (deployed independently)** và tái sử dụng bởi nhiều hệ thống khác nhau.
  * Tập trung vào việc giải quyết một nhu cầu/nghiệp vụ kinh doanh (business need) cụ thể (ví dụ: kiểm tra điểm tín dụng, tính toán khoản vay, xử lý hồ sơ thế chấp).
* **Khác biệt cốt lõi giữa Component và Service:** 
  * Một Service chỉ có **một thực thể duy nhất, luôn chạy (one unique, always running instance)** để nhiều client khác nhau cùng giao tiếp.
* **Mối quan hệ phân tầng:** 
  $$\text{Dịch vụ (Service)} \rightarrow \text{Thành phần (Component)} \rightarrow \text{Đối tượng (Object)}$$
  *(Dịch vụ được tạo nên từ các thành phần, và thành phần được cấu thành từ các đối tượng).*

---

## 4. Kiến trúc Hướng Dịch vụ (SOA - Service-Oriented Architecture)
* Trong SOA, các dịch vụ liên kết lỏng lẻo (loosely coupled) và giao tiếp với nhau thông qua một giao thức truyền thông (communication protocol) trên mạng.
* SOA là nền tảng để xây dựng các hệ thống phân tán nhằm cung cấp dịch vụ cho các ứng dụng khác.

---

## 5. Hệ thống Phân tán (Distributed Systems)
* **Định nghĩa:** Là hệ thống gồm nhiều dịch vụ nằm trên các máy tính khác nhau, điều phối tương tác bằng cách truyền thông điệp qua các giao thức mạng (ví dụ: HTTP).
* **Trải nghiệm người dùng:** Đối với người dùng cuối, toàn bộ hệ thống phân tán xuất hiện như một hệ thống nhất quán duy nhất (single coherent system).
* **Các đặc tính chính:**
  * **Chia sẻ tài nguyên (Shared resources):** Chia sẻ phần cứng, phần mềm và dữ liệu.
  * **Kháng lỗi (Fault-tolerant):** Nếu một nút (node) hoặc một dịch vụ bị lỗi, hệ thống vẫn tiếp tục chạy bình thường mà không gây gián đoạn dịch vụ.
  * **Xử lý đồng thời (Concurrency):** Nhiều hoạt động chạy đồng thời giúp giảm độ trễ (latency) và tăng băng thông (throughput).
  * **Khả năng mở rộng (Scalability):** Dễ dàng mở rộng quy mô khi lượng người dùng tăng lên.
  * **Hỗ trợ môi trường không đồng nhất (Heterogeneous):** Các máy tính trong hệ thống không cần cùng loại phần cứng hay hệ điều hành, và có thể viết bằng nhiều ngôn ngữ lập trình khác nhau.
* **Nút (Node):** Là bất kỳ thiết bị nào trên mạng có thể nhận diện, xử lý và truyền dữ liệu cho các node khác. Hệ thống phân tán gồm nhiều node kết nối với nhau, chạy một hoặc nhiều dịch vụ trong SOA.
* **Các kiểu kiến trúc hệ thống phân tán phổ biến:** Client-server, Three-tier (kiến trúc 3 lớp), Peer-to-peer (ngang hàng) hoặc Microservices.

---

## 6. Tóm tắt nhanh (Key Takeaways)
1. **Component** có 6 đặc tính: tái sử dụng, dễ thay thế, độc lập, có thể mở rộng, bao đóng, và không phụ thuộc ngữ cảnh.
2. **Service** là đơn vị nghiệp vụ được triển khai độc lập, có một thực thể chạy duy nhất phục vụ nhiều client.
3. Trong **SOA**, các dịch vụ giao tiếp qua mạng bằng các giao thức chuẩn.
4. **Hệ thống phân tán** phân tách các dịch vụ trên nhiều máy khác nhau nhưng hoạt động như một thực thể duy nhất, nổi bật với tính kháng lỗi, xử lý đồng thời và khả năng mở rộng tốt.
