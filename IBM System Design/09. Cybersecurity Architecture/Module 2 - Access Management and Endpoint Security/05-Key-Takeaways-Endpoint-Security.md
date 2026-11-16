# Reading: Key Takeaways - Endpoint Security

> **Source**: Course *Cybersecurity Architecture* - Reading: *Key Takeaways: Endpoint Security*  
> **Author**: Dee Dee Collette (IBM)

---

## 1. Bản chất & Nguồn gốc rủi ro của Endpoint

* **Nền tảng của MFA**: Xác thực đa yếu tố (MFA) chỉ thực sự có ý nghĩa và hiệu quả khi dựa trên **sự tin cậy vào nền tảng nguồn (source platform)** gửi yêu cầu.
* **Khái niệm Endpoint**: Là bất kỳ thiết bị vật lý nào kết nối vào mạng máy tính để trao đổi, xử lý thông tin (Servers, Desktops, Laptops, Mobile Devices, IoT...).
* **Lỗ hổng bảo mật**: Có thể bắt nguồn từ cả hai phương diện:
  * **Hardware (Phần cứng)**.
  * **Software (Phần mềm & Hệ điều hành)**.

---

## 2. Hai trụ cột an ninh: Visibility & Control

> **"Visibility and control are keys to security."**  
> *(Khả năng nhìn thấy toàn cảnh và Khả năng kiểm soát là hai chìa khóa quyết định an ninh mạng).*

* Khả năng nhìn thấy và kiểm soát giúp tổ chức quy định rõ ràng **loại phần cứng và phần mềm nào được phép hoạt động** trong môi trường IT của doanh nghiệp.

---

## 3. Các hình thức kiểm soát Endpoint (Forms of Controls)

1. **Inventory (Kiểm kê / Quản lý tài sản)**: Quét và lập danh mục toàn bộ thiết bị đang kết nối.
2. **Policies (Chính sách)**: Các quy tắc bảo mật áp đặt lên thiết bị (mật khẩu, phần mềm được phép...).
3. **Patching (Cập nhật bản vá)**: Vá kịp thời các lỗ hổng hệ điều hành và phần mềm.
4. **Encryption (Mã hóa)**: Đảm bảo dữ liệu lưu trữ trên thiết bị luôn được mã hóa an toàn.
5. **Remote Wipe (Xóa từ xa)**: Xóa sạch dữ liệu khi thiết bị thất lạc, mất cắp hoặc nhân viên nghỉ việc.
6. **Location Tracking (Theo dõi vị trí)**: Giám sát tọa độ địa lý của thiết bị.
7. **Anti-virus / EDR**: Ngăn chặn, phát hiện và phản ứng trước mã độc.
8. **Disposal (Tiêu hủy an toàn)**: Quy chuẩn làm sạch dữ liệu và thanh lý thiết bị cũ không để lộ thông tin.

---

## 4. Chính sách bảo mật (Security Policies)

* **Mục tiêu**: Được ban hành và thực thi nhằm đạt được mức độ an toàn cao nhất cho tổ chức.
* **Yêu cầu đối với Mật khẩu**: Quy định nghiêm ngặt về độ dài tối thiểu, độ phức tạp/độ mạnh (strength) và thời hạn hiệu lực (expiry date).
* **Mã hóa**: Đảm bảo quy chuẩn mã hóa dữ liệu lưu trữ được thiết lập đúng cách trên toàn bộ thiết bị.
* **Giám sát & Minh bạch**: Các chính sách cần quy định và đánh giá rõ ràng việc **thiết bị có bị giám sát hay không**, và **trong những điều kiện cụ thể nào** (rất quan trọng trong các chương trình BYOD).
