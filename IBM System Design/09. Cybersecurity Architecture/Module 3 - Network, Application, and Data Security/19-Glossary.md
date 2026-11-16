# Glossary: Network, Application, and Data Security

> **Khóa học**: Cybersecurity Architecture (IBM)  
> **Module 3**: Network, Application, and Data Security  
> **Tài liệu**: Glossary (Thuật ngữ chuyên ngành)

---

## 📖 Bảng Thuật Ngữ Chuyên Ngành (Glossary of Terms)

| Thuật ngữ (Term) | Định nghĩa chuẩn mực (Official Definition) | Giải thích & Ứng dụng kiến trúc |
| :--- | :--- | :--- |
| **Application Firewall (WAF)** | Giúp bảo vệ các ứng dụng web bằng cách lọc và giám sát lưu lượng HTTP/HTTPS giữa ứng dụng web và Internet. | Ngăn chặn các cuộc tấn công tầng ứng dụng phổ biến như SQL Injection, Cross-Site Scripting (XSS). |
| **Cryptography (Mật mã học)** | Quá trình chuyển đổi qua lại giữa văn bản đọc được (**plaintext**) và dạng không thể đọc được (**ciphertext**). Quá trình người gửi chuyển plaintext thành ciphertext được gọi là **Mã hóa (Encryption)**. | Đảm bảo tính bảo mật (Confidentiality) và toàn vẹn (Integrity) cho dữ liệu cả ở trạng thái lưu trữ (*at rest*) lẫn truyền tải (*in motion*). |
| **Demilitarized Zone (DMZ)** | Cấu hình sử dụng nhiều tường lửa để tạo thêm các lớp bảo vệ đệm giữa mạng nội bộ doanh nghiệp (Intranet) và mạng công cộng bên ngoài (Internet). | Cách ly các máy chủ hướng ngoại (Web, DNS, Email) khỏi mạng dữ liệu nội bộ nhằm ngăn ngừa tấn công lây lan ngang (*lateral movement*). |
| **DevOps Lifecycle** | Một chuỗi các quy trình phát triển lặp đi lặp lại và tự động hóa, được thực thi trong một vòng đời phát triển khép kín nhằm tối ưu hóa việc phân phối phần mềm chất lượng cao với tốc độ nhanh nhất. | Phá bỏ rào cản ngăn cách giữa bộ phận Lập trình (Development) và Vận hành (Operations). |
| **DevSecOps** | Viết tắt của **Development, Security, and Operations**. Tự động hóa việc tích hợp an ninh mạng vào mọi giai đoạn của vòng đời phần mềm, từ thiết kế ban đầu, tích hợp, kiểm thử đến triển khai. | Chuyển dịch tư duy an ninh sang bên trái (**Shift-Left**), thay vì coi bảo mật là phần chắp vá bổ sung vào cuối quy trình (*bolt-on*). |
| **Dynamic Application Security Testing (DAST)** | Phương pháp kiểm thử an ninh **Hộp đen (Black-box)** tiếp cận từ góc nhìn của một kẻ tấn công thực sự từ bên ngoài. Thường chạy tự động trên các ứng dụng/web service đang thực thi ở môi trường test. | Phát hiện các lỗi phát sinh ở trạng thái runtime (lỗi cấu hình máy chủ, xác thực phiên, lỗ hổng inject thực tế). |
| **Firewall (Tường lửa)** | Rào chắn kiểm soát giữa một mạng nội bộ an toàn và một mạng không tin cậy như Internet. Dùng để kết nối an toàn ra ngoài hoặc cách ly giữa các mạng nội bộ với nhau. | Chốt kiểm soát luồng giao tiếp, thực thi các chính sách cho phép (permit) hoặc từ chối (deny) lưu lượng truy cập. |
| **Network Address Translation (NAT)** | Chuyển đổi các địa chỉ mạng nội bộ/private thành các địa chỉ IP công cộng (Public IP) có thể định tuyến toàn cầu trên Internet. NAT cũng có khả năng dịch cổng (Port translation). | Bảo tồn không gian địa chỉ IPv4 và ẩn giấu cấu trúc mạng nội bộ, ngăn chặn kết nối trực tiếp trái phép từ bên ngoài. |
| **Packet Filter (Bộ lọc gói tin)** | Giới hạn và kiểm soát các dịch vụ đối với từng người dùng khi họ kết nối mạng. Cho phép hoặc từ chối dựa trên địa chỉ IP đích, cổng (port), hoặc cả hai. | Cơ chế lọc cơ bản ở phần Header của gói tin (không kiểm tra trạng thái phiên và không đọc nội dung payload). |
| **Proxy (Máy chủ ủy quyền)** | Hoạt động như một cầu nối trung gian: giảm tải lưu lượng mạng bằng cách từ chối yêu cầu không mong muốn, cân bằng tải, và phục vụ dữ liệu từ bộ nhớ đệm (Cache) thay vì phải liên hệ trực tiếp đến máy chủ đích. | Ẩn IP của máy trạm, bẻ gãy kết nối đầu cuối trực tiếp để kiểm tra mã độc và thực thi chính sách an ninh mạng. |
| **SASE (Secure Access Service Edge)** | Khung kiến trúc hội tụ giữa các dịch vụ mạng (như **SD-WAN**) và các công nghệ an ninh đám mây (như **CASB, FWaaS, ZTNA**) thành một mô hình dịch vụ duy nhất phân phối từ Đám mây (Cloud). | Nền tảng cốt lõi cho mô hình bảo mật Zero Trust, bảo vệ người dùng và thiết bị truy cập tài nguyên mọi lúc, mọi nơi. |
| **Software Bill of Materials (SBOM)** | Danh mục kiểm kê phân cấp chi tiết — một danh sách "thành phần nguyên liệu" cấu thành nên các thành phần phần mềm. | Giúp kiểm soát chuỗi cung ứng phần mềm, nhanh chóng định vị các thư viện nguồn mở phụ thuộc chứa lỗ hổng (ví dụ: Log4j). |
| **Stateful Packet Inspection (SPI)** | Kiểm tra địa chỉ nguồn/đích, số cổng và thông tin trạng thái kết nối. Áp dụng các luật lọc theo cờ header để ra quyết định lọc trong **ngữ cảnh của toàn bộ phiên giao tiếp**. | An toàn và thông minh hơn Packet Filter truyền thống do theo dõi được tính hợp lệ của luồng kết nối liên tục. |
| **Static Application Security Testing (SAST)** | Phương pháp kiểm thử an ninh **Hộp trắng (White-box)** được thực hiện bằng cách phân tích trực tiếp mã nguồn mà **không cần thực thi ứng dụng**. | Phát hiện sớm các lỗi logic, vi phạm chuẩn an toàn, lỗ hổng lập trình ngay trong giai đoạn viết mã (Coding). |
| **Virtual Private Network (VPN)** | Cho phép doanh nghiệp mở rộng mạng Intranet riêng tư một cách an toàn trên nền tảng mạng công cộng (như Internet). | Cung cấp kênh truyền mã hóa (Encrypted tunnel), đảm bảo tính bí mật và xác thực người dùng từ xa. |
