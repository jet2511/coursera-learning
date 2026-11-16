# Hands-on Lab: Review Security Threat Reports using X-Force Threat Exchange

## 1. Giới thiệu
**IBM X-Force Threat Exchange** (`https://exchange.xforce.ibmcloud.com/`) là nền tảng cộng tác dựa trên đám mây của IBM, cho phép người dùng chia sẻ và truy cập các nguồn cấp dữ liệu tình báo mối đe dọa (threat intelligence) theo thời gian thực về các mối đe dọa, lỗ hổng và địa chỉ IP rủi ro.

---

## 2. Các thành phần chính trên Dashboard
1. **Đăng nhập**: Có thể đăng nhập bằng IBM ID (để mở khóa đầy đủ báo cáo) hoặc chọn **Enter as Guest** để xem tổng quan.
2. **IBM X-Force Threat Analysis Reports**:
   - Danh sách các báo cáo phân tích mối đe dọa mới nhất do đội ngũ IBM X-Force tổng hợp.
   - Nội dung gồm: tổng quan mối đe dọa, nguồn gốc, tác động tiềm ẩn, các lỗ hổng bị khai thác, danh sách IP mục tiêu/bị ảnh hưởng, và **chiến lược giảm thiểu (mitigation strategies)**.
3. **Early Warning Data**:
   - Cung cấp thông tin cảnh báo sớm về các mối đe dọa mới nổi và lỗ hổng tiềm ẩn (dữ liệu mới được thêm trong vài giờ gần đây).
   - Ví dụ: malware mới phát hiện, hoạt động IP đáng ngờ, mẫu lưu lượng mạng bất thường.
4. **Malicious Activity**:
   - Bản đồ thời gian thực hiển thị các sự kiện bảo mật bị gắn cờ độc hại trong vòng **1 giờ qua**.
   - Cung cấp chi tiết loại tấn công, nguồn, khu vực mục tiêu, IP bị ảnh hưởng (ví dụ: xem danh sách các IP mới bị phân loại là **Spam**).
