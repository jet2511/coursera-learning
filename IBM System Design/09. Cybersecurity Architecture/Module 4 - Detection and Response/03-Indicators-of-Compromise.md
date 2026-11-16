# Indicators of Compromise (IoC - Chỉ số xâm phạm)

## 1. Khái niệm
**Indicator of Compromise (IoC)** là các bằng chứng cho thấy một hệ thống hoặc mạng có thể đã bị xâm phạm.

## 2. Các loại IoC phổ biến
- **Lưu lượng mạng đáng ngờ (Suspicious network traffic)**:
  - Lưu lượng mạng tăng đột biến bất thường (traffic spikes).
  - Các gói dữ liệu bất thường (unusual data packets).
  - Giao tiếp với các địa chỉ IP đáng ngờ, thường vào những khung giờ bất thường.
- **Hành vi hệ thống bất thường (Unusual system behavior)**:
  - Hệ thống chạy chậm hơn bình thường.
  - Hệ thống thường xuyên bị sập (crashes).
  - Xuất hiện các thông báo lỗi (error messages).
- **Bản ghi log bất thường (Abnormal log entries)**:
  - Các lần thử đăng nhập lặp đi lặp lại (repeated login attempts).
  - Đăng nhập từ các vị trí địa lý bất ngờ (unexpected locations).
- **Phishing & Social Engineering**:
  - Các email không xác định/lạ (unrecognized email messages).
  - Các đường dẫn URL đáng ngờ (suspicious URLs).
- **Tài khoản người dùng lạ (Unrecognized user accounts)**:
  - Tài khoản do kẻ tấn công tạo ra (attacker-created accounts).
  - Tài khoản cũ không còn sử dụng nhưng vẫn tồn tại (outdated accounts).
