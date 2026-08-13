# Các Thành phần Triển khai Production (Production Deployment Components)

Tài liệu này chi tiết hóa các thành phần hạ tầng cơ bản thường được sử dụng để triển khai một ứng dụng trong môi trường Production thông qua mô hình kiến trúc đa tầng (n-tier).

---

## 1. Mô hình Kiến trúc Đa tầng (n-tier Architecture) trong Production
Một kiến trúc đa tầng tiêu chuẩn được phân chia từ ngoài vào trong như sau:

1. **Tầng Trình diễn (Presentation Tier):** Chứa các ứng dụng client frontend (web app, mobile app) tương tác trực tiếp với người dùng.
*👉 Ranh giới bảo mật: Tường lửa (Firewall) được đặt ngay sau tầng này để bảo vệ toàn bộ hệ thống nội bộ bên dưới.*
2. **Tầng Web (Web Tier):** Nhận yêu cầu từ client. Thường sử dụng **Web Load Balancer** để phân phối lưu lượng truy cập đến các **Web Server**.
3. **Tầng Máy chủ Ứng dụng (Application Server Tier):** Chứa **App Load Balancer** hoặc **Proxy Server** để định tuyến yêu cầu đến các **Application Server** xử lý logic nghiệp vụ.
4. **Tầng Dữ liệu (Data Tier):** Chứa **Database Server** và hệ quản trị cơ sở dữ liệu (DBMS). Tầng này thường cấu hình thêm các bản sao dự phòng sẵn sàng cao (High Availability Replica) để đảm bảo an toàn dữ liệu và tính liên tục của hệ thống.

*Lưu ý: Tùy thuộc vào quy mô dự án, không phải mọi triển khai đều cần phân tách đầy đủ tất cả các tầng trên (ví dụ: có thể gộp Web Server và App Server).*

---

## 2. Chi tiết các thành phần Hạ tầng chính

### A. Tường lửa (Firewall)
* **Khái niệm:** Là thiết bị bảo mật giám sát và kiểm soát lưu lượng mạng ra/vào giữa các vùng mạng khác nhau.
* **Chức năng:** Cho phép hoặc chặn dữ liệu dựa trên một tập hợp các quy tắc bảo mật được thiết lập trước, đóng vai trò như rào chắn ngăn chặn virus, mã độc và các cuộc tấn công của tin tặc vào mạng nội bộ.

### B. Bộ cân bằng tải (Load Balancer)
* **Khái niệm:** Thiết bị điều phối lưu lượng mạng một cách hiệu quả giữa nhiều máy chủ (server farm).
* **Vị trí:** Nằm giữa Client và các Máy chủ.
* **Chức năng:** Ngăn ngừa tình trạng quá tải lưu lượng tại một máy chủ đơn lẻ, tối đa hóa tính sẵn sàng (availability) và khả năng phản hồi (responsiveness) của toàn bộ hệ thống.

### C. Máy chủ Web (Web Server)
* **Khái niệm:** Máy chủ phần cứng hoặc phần mềm chuyên cung cấp các nội dung tĩnh như trang HTML, tệp tin, hình ảnh và video cho client.
* **Giao thức:** Chủ yếu tiếp nhận và phản hồi các yêu cầu thông qua giao thức HTTP/HTTPS từ trình duyệt web của người dùng.

### D. Máy chủ Ứng dụng (Application Server)
* **Khái niệm:** Máy chủ chạy mã nguồn chứa các logic nghiệp vụ (business logic) của hệ thống.
* **Chức năng:** Thiết lập tương tác giữa người dùng cuối và mã ứng dụng phía máy chủ. Logic nghiệp vụ tại đây quyết định cách dữ liệu được tạo ra, lưu trữ, thay đổi cũng như điều phối việc ghi/đọc dữ liệu từ Database.

### E. Máy chủ Ủy quyền (Proxy Server)
* **Khái niệm:** Là máy chủ trung gian đứng giữa hai tầng/thành phần để xử lý và chuyển tiếp các yêu cầu qua lại.
* **Vai trò đa năng:** Có thể thực hiện cân bằng tải, tối ưu hóa hệ thống, làm bộ nhớ đệm (caching), hoạt động như tường lửa, ẩn địa chỉ IP nguồn (anonymity), mã hóa dữ liệu hoặc quét mã độc, giúp tăng tính riêng tư, hiệu năng và bảo mật mạng.

### F. Máy chủ Cơ sở Dữ liệu (Database Server)
* **Khái niệm:** Lưu trữ dữ liệu có cấu trúc của hệ thống, được quản lý thông qua Hệ quản trị cơ sở dữ liệu (DBMS - Database Management System).
* **Chức năng:** DBMS kết nối cơ sở dữ liệu với ứng dụng, cho phép ứng dụng truy xuất, thêm mới hoặc chỉnh sửa dữ liệu được lưu trữ một cách an toàn và tối ưu.

---

## 3. Tóm tắt nhanh (Key Takeaways)
1. Hạ tầng Prod thường được tổ chức theo kiến trúc **n-tier** để phân tách trách nhiệm rõ ràng giữa các tầng Presentation, Web, App và Data.
2. **Firewall** và **Proxy Server** củng cố an ninh mạng; **Load Balancer** đảm bảo hệ thống không bị tắc nghẽn và tăng khả năng chịu tải.
3. **Web Server** chịu trách nhiệm phân phối nội dung tĩnh/HTTP; **Application Server** đảm nhận xử lý logic nghiệp vụ phức tạp; **Database Server** kiểm soát dữ liệu thông qua **DBMS**.
