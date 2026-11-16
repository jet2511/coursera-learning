# Key Takeaways: Network Security

> **Khóa học**: Cybersecurity Architecture (IBM)  
> **Module 3**: Network, Application, and Data Security  
> **Tài liệu**: Reading: Key Takeaways: Network Security (5 phút)  
> **Tác giả**: Dee Dee Collette (License: Apache 2.0)

---

## 📌 Khái niệm Trọng tâm (Key Concepts)

- **Mục tiêu của Network Security**: Bảo vệ khả năng sử dụng (usability) và tính toàn vẹn (integrity) của dữ liệu, sử dụng tường lửa để phân tách giữa mạng tin cậy (trusted) và mạng không tin cậy (untrusted).
- **Packet Filtering (Lọc gói tin)**: Quyết định cho qua hoặc chặn các gói tin mạng dựa trên thông tin trong header:
  - Địa chỉ nguồn (Source address).
  - Địa chỉ đích (Destination address).
  - Cổng dịch vụ sử dụng (Port).
- **Stateful Packet Inspection (SPI)**: Đánh giá xem gói tin có được phép đi qua tường lửa hay không dựa trên trạng thái phiên và kiểm tra cả nội dung bên trong gói tin (Packet contents / payload).
- **Application Firewall (Tường lửa ứng dụng)**: Giám sát và kiểm soát lưu lượng mạng vào/ra theo tập luật bảo mật định sẵn ở tầng ứng dụng.
- **Proxy Server**: Đóng vai trò đại diện/thay mặt cho một bên khác; giúp kiểm tra sâu và thực thi chính sách an ninh đối với dữ liệu trước khi vào mạng nội bộ.
- **Network Address Translation (NAT)**:
  - Ánh xạ nhiều địa chỉ IP với nhau.
  - Tăng cường bảo mật bằng cách chuyển đổi các địa chỉ nội bộ (Private IP - không định tuyến được trên Internet) thành địa chỉ IP công cộng (Routable IP).
- **Virtual Private Networking (VPN)**: Cung cấp một kênh truyền bảo mật đi qua mạng không tin cậy. *Secure Shell (SSH)* là một ví dụ về VPN cấp ứng dụng.
- **IPSec**: Hoạt động tại tầng Network (Network Layer - OSI Layer 3) nhằm mã hóa toàn bộ dữ liệu trao đổi giữa hai địa chỉ mạng.
- **Secure Access Service Edge (SASE)**: Kết hợp các năng lực mạng diện rộng (SD-WAN) và an ninh mạng (bao gồm VPN, FWaaS, SWG) rồi phân phối dưới dạng một dịch vụ đám mây (Cloud service) hợp nhất.
- **Data Loss Prevention (DLP)**: Hoạt động/công nghệ chuyên phát hiện, giám sát và ngăn chặn các hành vi rò rỉ, mất mát hoặc đánh cắp dữ liệu trái phép.
