# Design Cost-Optimized Network Architectures

## 1. Tối ưu Kết nối Hybrid (AWS to On-Premises)

| Phương thức kết nối | Chi phí & Tính chất | Khi nào nên chọn? |
| :--- | :--- | :--- |
| **AWS Site-to-Site VPN** | **Chi phí thấp**, triển khai nhanh qua Internet công cộng, có mã hóa IPsec. | - Kết nối lưu lượng vừa/nhỏ.<br>- **Làm đường kết nối dự phòng (Failover/Backup)** chi phí thấp cho kết nối Direct Connect chính. |
| **AWS Direct Connect (DX)** | **Chi phí cao** (cần đường truyền vật lý chuyên dụng), thời gian setup lâu. | Cần băng thông cực lớn, độ trễ cực thấp, ổn định cao và lưu lượng truyền tải liên tục khổng lồ. |

---

## 2. Kết nối giữa các VPC (VPC Peering vs Transit Gateway)

- **VPC Peering:**
  - **Không tốn phí cố định hàng giờ (No hourly fee).**
  - Chỉ tính phí truyền dữ liệu (Data transfer) giữa các AZ/Region.
  - **Tối ưu chi phí nhất** khi chỉ cần kết nối giữa ít VPC (Point-to-point 1-1).
- **AWS Transit Gateway (TGW):**
  - Có **phí cố định theo giờ cho mỗi Attachment** + phí xử lý dữ liệu (Data processing fee).
  - Phù hợp khi kiến trúc có hàng chục/hàng trăm VPC cần kết nối dạng Hub-and-Spoke phức tạp.

---

## 3. Quy tắc & Chiến lược Giảm chi phí Data Transfer trong AWS

```
[Miễn phí] Cùng AZ (Private IP) 
    ⬇
[Có phí vừa] Khác AZ (Cross-AZ trong cùng Region) 
    ⬇
[Có phí cao] Khác Region (Cross-Region) 
    ⬇
[Chi phí cao nhất] Ra ngoài Internet (Data Transfer Out - Egress)
```

1. **Giữ traffic trong cùng một Availability Zone (Local AZ):** Giao tiếp nội bộ giữa các dịch vụ trong cùng AZ bằng Private IP là miễn phí (tránh cross-AZ không cần thiết).
2. **Sử dụng VPC Gateway Endpoints (Miễn phí):**
   - Dành cho **Amazon S3** và **Amazon DynamoDB**.
   - Miễn phí data transfer qua endpoint và không tốn phí duy trì theo giờ (khác với Interface Endpoints / PrivateLink có tính phí theo giờ và GB xử lý).
3. **Tối ưu triển khai NAT Gateway:**
   - **Production:** Đặt NAT Gateway tại mỗi AZ để đảm bảo High Availability (HA).
   - **Development / Non-Prod:** Dùng **một Shared NAT Gateway** duy nhất trong VPC để tiết kiệm phí giờ hoạt động ($0.045/giờ mỗi NAT GW).

---

## 4. Tối ưu hóa Chi phí Data Transfer với Amazon CloudFront

- **Cơ chế tiết kiệm:**
  - **Miễn phí Data Transfer Out từ AWS Origins đến CloudFront:** Dữ liệu từ S3, EC2, ALB chuyển tới các CloudFront Edge Locations là **hoàn toàn $0 (Free)**.
  - **Giảm số lượng Request và Data Egress từ S3:** CloudFront Edge Cache và Regional Edge Caches (miễn phí) lưu trữ bản sao phản hồi, giảm trực tiếp số lượng request API GET và dung lượng download từ S3 bucket.
  - Giá cước Data Transfer Out từ CloudFront ra Internet thường rẻ hơn trực tiếp từ EC2/S3 ra Internet.

---

## 5. Kiểm soát lưu lượng & Giới hạn API (API Gateway Throttling)
- Sử dụng **API Gateway Usage Plans & API Keys** để:
  - Thiết lập định mức (Quotas) theo ngày/tuần/tháng và giới hạn tốc độ (Throttling - Rate/Burst limits) cho từng khách hàng.
  - Ngăn chặn backend compute bị quá tải dẫn đến chi phí tăng vọt ngoài tầm kiểm soát.

---

## 6. Công cụ Giám sát & Quản lý Cấu hình Network
- **AWS CloudWatch & VPC Flow Logs:** Phân tích lưu lượng IP và phát hiện các luồng traffic cross-AZ/cross-Region bất thường.
- **AWS Transit Gateway Network Manager & VPC Reachability Analyzer:** Kiểm tra và chẩn đoán cấu hình đường truyền mạng mà không cần gửi gói tin thực tế (tiết kiệm chi phí test).
- **Lựa chọn Region:** Chi phí vận hành mạng và compute khác nhau giữa các Region $\to$ Chọn Region có mức giá rẻ hơn nếu không bị ràng buộc về độ trễ hoặc tuân thủ dữ liệu.

---

## 7. Key Exam Takeaways
1. **Dự phòng (Backup/Failover) chi phí thấp cho Direct Connect $\to$ AWS Site-to-Site VPN.**
2. **Kết nối vài VPC trong cùng/khác Region với chi phí rẻ nhất $\to$ VPC Peering** (tránh dùng Transit Gateway nếu số lượng VPC ít).
3. **Truy cập S3 & DynamoDB từ private subnet không tốn phí $\to$ VPC Gateway Endpoints.**
4. **Giảm chi phí truyền dữ liệu từ S3 ra Internet $\to$ Amazon CloudFront** (miễn phí S3-to-CloudFront transfer).
5. **Tiết kiệm NAT Gateway trong môi trường Dev/Test $\to$ Dùng 1 Shared NAT Gateway.**
