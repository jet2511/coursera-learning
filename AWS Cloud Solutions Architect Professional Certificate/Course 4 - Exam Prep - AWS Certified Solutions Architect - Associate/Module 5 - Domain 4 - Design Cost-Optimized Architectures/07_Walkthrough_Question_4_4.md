# Walkthrough Question 4.4: Cost-Effective and Secure Remote Access to EC2 in Private Subnet

## 1. Nội dung câu hỏi (Question Stem)
Một công ty đang phát triển một ứng dụng chạy trên các **Amazon EC2 instances trong private subnet**. 
Các EC2 instance này sử dụng một **NAT Gateway để truy cập ra Internet**. 
Một Solutions Architect cần cung cấp một giải pháp **bảo mật** để các lập trình viên có thể **đăng nhập vào các instance** này.

**Giải pháp nào đáp ứng yêu cầu một cách tối ưu chi phí nhất (most cost-effectively)?**

---

## 2. Phân tích từ khóa (Keywords & Clues)
- **EC2 instances in private subnet:** Các máy chủ không có Public IP và nằm trong mạng riêng biệt.
- **Instances use NAT Gateway for outbound:** Đã có kết nối Internet outbound (cho phép SSM Agent giao tiếp với Systems Manager endpoints).
- **Secure login:** Đăng nhập an toàn mà không cần mở các port nguy hiểm ra Internet (ví dụ port 22/3389).
- **Most cost-effectively:** Tiết kiệm chi phí nhất (ưu tiên giải pháp miễn phí hoặc không phải tốn thêm chi phí phần cứng/dịch vụ trung gian).

---

## 3. Lựa chọn đáp án & Phân tích chi tiết

### Các lựa chọn:
- **A. (Đúng) Cấu hình AWS Systems Manager Session Manager cho các EC2 instance để kích hoạt tính năng đăng nhập.**
- **B.** Cấu hình một Bastion Host trong public subnet để đăng nhập vào các EC2 instance trong private subnet.
- **C.** Sử dụng NAT Gateway hiện có để đăng nhập vào các EC2 instance trong private subnet.
- **D.** Cấu hình AWS Site-to-Site VPN để đăng nhập trực tiếp vào các EC2 instance.

---

### Giải thích chi tiết:

| Lựa chọn | Đánh giá | Lý do |
| :--- | :---: | :--- |
| **A. AWS Systems Manager Session Manager** | **ĐÚNG** | - **Bảo mật tối đa:** Cho phép truy cập terminal 1-click qua AWS Management Console / CLI mà **không cần mở bất kỳ Inbound Port nào** trên Security Group, không cần Public IP, không cần quản lý SSH keys.<br>- **Kiểm toán (Auditable):** Lưu log phiên làm việc đầy đủ vào S3 / CloudWatch Logs.<br>- **Chi phí tối ưu nhất:** Tính năng Session Manager để quản lý EC2 là **hoàn toàn miễn phí ($0 additional charge)**. |
| **B. Bastion Host (Jump Box)** | **SAI** | Hoạt động được nhưng phải tốn chi phí duy trì một EC2 instance chạy liên tục trong public subnet và phải mở port SSH (22) ra ngoài, gây rủi ro bảo mật và tốn chi phí. |
| **C. Đăng nhập qua NAT Gateway** | **SAI** | **Về mặt kỹ thuật NAT Gateway là one-way (Egress-only outbound)**. NAT Gateway chỉ cho phép traffic từ bên trong đi ra ngoài Internet và phản hồi về, không cho phép khởi tạo kết nối Inbound từ Internet vào trong private subnet. |
| **D. AWS Site-to-Site VPN** | **SAI** | VPN có thể hoạt động nhưng tốn phí duy trì kết nối VPN Connection (\$0.05/giờ mỗi kết nối) + phí Data Transfer, không phải là lựa chọn tiết kiệm chi phí nhất so với Session Manager. |

---

## 4. Key Exam Takeaways
1. **Truy cập EC2 Private Subnet an toàn + Miễn phí $\to$ AWS Systems Manager Session Manager:**
   - Không cần mở Inbound Ports (Port 22/3389 = 0 Inbound rules).
   - Không cần Bastion Host / Jump Server.
   - Không cần Public IP trên EC2.
   - Hoàn toàn miễn phí quản lý EC2 cơ bản.
2. **Nguyên lý NAT Gateway:**
   - Chỉ cho phép **Outbound Egress** (từ private subnet $\to$ Internet).
   - Tuyệt đối **không hỗ trợ Inbound traffic** khởi tạo từ bên ngoài.
3. **So sánh chi phí truy cập:**
   - **Session Manager:** $0
   - **Bastion Host:** Phí EC2 Instance + Storage + Egress.
   - **Site-to-Site VPN:** Phí theo giờ kết nối VPN + Data Transfer.
