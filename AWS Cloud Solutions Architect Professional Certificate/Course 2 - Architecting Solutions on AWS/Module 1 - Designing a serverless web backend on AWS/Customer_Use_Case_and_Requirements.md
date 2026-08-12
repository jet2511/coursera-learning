# Tóm tắt bài học: Yêu cầu và Tình huống của Khách hàng số 1 (Customer #1: Use Case and Requirements)

**Khóa học:** Course 2 - Architecting Solutions on AWS  
**Chủ đề:** Phân tích nhu cầu thực tế và thu thập yêu cầu từ khách hàng  
**Vị trí:** Module 1 - Designing a serverless web backend on AWS

---

## 1. Thông tin khách hàng & Bối cảnh dự án
* **Khách hàng:** Technical Architect đến từ công ty **Any Company Ecommerce** (Doanh nghiệp chuyên bán các sản phẩm tẩy rửa trực tuyến trên phạm vi toàn cầu).
* **Mục tiêu:** Di chuyển thành phần cốt lõi cuối cùng là **Dịch vụ Đơn hàng (Orders Service)** đang chạy on-premises lên AWS Cloud.
* **Chiến lược di chuyển:** Thay vì sử dụng mô hình di chuyển trực tiếp không đổi mã nguồn (*lift-and-shift*) như các dịch vụ trước đây, khách hàng quyết định **viết lại hoàn toàn** dịch vụ này theo mô hình **Cloud-native** và **Serverless** để tận dụng tối đa lợi ích của điện toán đám mây.

---

## 2. Hiện trạng kiến trúc mạng và ứng dụng hiện tại
* **Hạ tầng phân tán:** Các dịch vụ hạ nguồn (downstream) gồm Quản lý kho (Inventory/Fulfillment) và Kế toán (Accounting) đã được chuyển lên chạy ổn định trên AWS.
* **Orders Service hiện tại (On-premises):** 
  * Chạy trên máy chủ vật lý on-premises, tích hợp chung Web Server để định tuyến yêu cầu từ trình duyệt/ứng dụng client.
  * Cơ sở dữ liệu: Dùng **MySQL database** cài đặt on-premises. Cấu trúc dữ liệu đơn giản, chỉ sử dụng duy nhất một bảng để lưu trữ dữ liệu đơn hàng.
  * **Thanh toán (Payment Processing):** Nằm ngoài phạm vi dự án vì khách hàng sử dụng dịch vụ cổng thanh toán bên thứ ba (Payment Gateway). Khi request tới backend thì đơn hàng đã được thanh toán xong.

---

## 3. Các vấn đề và Điểm nghẽn (Pain Points) cần giải quyết
1. **Liên kết quá chặt chẽ (Tight Coupling):**
   * Khi Orders Service nhận đơn hàng, ứng dụng sẽ đồng thời gọi trực tiếp các API của dịch vụ hạ nguồn (inventory, accounting).
   * Nếu ứng dụng bị crash hoặc một trong các kết nối API hạ nguồn thất bại giữa chừng, các cuộc gọi API tiếp theo sẽ bị bỏ lỡ, gây mất mát dữ liệu và bất nhất dữ liệu đơn hàng (ví dụ: kho đã xác nhận nhưng kế toán chưa ghi nhận).
2. **Khó khăn trong việc co giãn (Scaling):**
   * Lưu lượng truy cập có tính chất đột biến rất cao (*spiky demand*): Rất cao khi mở đợt flash sale hoặc phát coupon code, nhưng gần như bằng không vào thời gian thường.
   * Để đối phó, khách hàng phải mua sắm dự phòng dư thừa nhiều phần cứng máy chủ (*overprovisioning*) gây lãng phí lớn nhưng hệ thống vẫn chậm hoặc crash khi tải đạt đỉnh.
3. **Gánh nặng vận hành cơ sở dữ liệu:**
   * Việc tự quản lý, bảo trì và cấu hình tính năng sẵn sàng cao cho cả một instance MySQL on-premises chỉ để lưu trữ một bảng dữ liệu đơn hàng duy nhất gây tốn rất nhiều thời gian và công sức của đội ngũ kỹ thuật.

---

## 4. Các yêu cầu kỹ thuật cho kiến trúc mới trên AWS
* **Tính độc lập (Decoupling):** Tách rời sự phụ thuộc giữa dịch vụ xử lý đơn hàng và các dịch vụ hạ nguồn. Việc gọi các API hạ nguồn phải độc lập và không được ảnh hưởng hoặc làm chậm tiến trình nhận đơn hàng chính của khách hàng.
* **Tự động co giãn (Managed Auto Scaling):** Hệ thống tự động mở rộng tài nguyên tính toán để xử lý các đợt lưu lượng tăng đột biến, và tự động thu hẹp về không khi không có yêu cầu để tối ưu hóa chi phí.
* **Cơ sở dữ liệu đơn giản & Quản lý dễ dàng:** Thay thế MySQL bằng một giải pháp cơ sở dữ liệu đám mây hoạt động ổn định, độ bền vững cao, tự động quản lý (hands-off) để giảm thiểu công sức vận hành.
* **Hệ thống giám sát và Ghi log tập trung (Logging & Monitoring):** Dễ dàng thiết lập cấu hình và ưu tiên gom toàn bộ log của các thành phần trong hệ thống về chung một nơi.
* **Tối ưu chi phí và Hiệu năng:** Thiết kế giải pháp dựa trên mô hình phi máy chủ (Serverless) để giảm thiểu tối đa chi phí chạy máy chủ rảnh rỗi và nâng cao hiệu năng đáp ứng.
