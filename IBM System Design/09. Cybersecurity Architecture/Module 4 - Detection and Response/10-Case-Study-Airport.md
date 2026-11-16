# Case Study: Stopping Cyberattacks at a Major International Airport

## 1. Bối cảnh & Sự cố (Compromise)
- Một sân bay quốc tế lớn sử dụng mạng **air-gapped** (cách ly hoàn toàn với bên ngoài) để quản lý vận hành nội bộ (từ logistics đến an ninh).
- Dù đã cách ly mạng, nhiều thiết bị vẫn bị nhiễm malware có chức năng thu thập và lưu trữ dữ liệu cục bộ.
- **Thách thức**:
  - Sân bay là hạ tầng trọng yếu (critical infrastructure), **không thể để xảy ra downtime**.
  - Mạng thiếu các biện pháp bảo vệ toàn diện; kết nối chung các thiết bị có mức độ bảo mật cao và thấp với nhau.
  - Thiếu khả năng quan sát (transparency) các hoạt động bên trong mạng.

---

## 2. Phát hiện (Discovery)
- Khi triển khai nền tảng **IBM QRadar EDR**, hệ thống phát hiện nhiều bất thường hành vi:
  - Một ứng dụng độc hại cài đặt **in-memory keylogger** và một luồng (thread) quét đĩa cứng tìm các file nhạy cảm.
  - Malware có cơ chế **vượt qua (bypass)** cả antivirus cục bộ lẫn phân tích sandbox.
- **Hai vector lây nhiễm** được phát hiện: một trên kiosk công cộng và một trên thiết bị thuộc cảm biến mạng quản lý check-in. Cả hai đều cố gắng liên lạc với cùng một **Command and Control (C2) server**.

---

## 3. Phản ứng & Khắc phục (Response)
- **Tái dựng cuộc tấn công (Post-breach)**: QRadar EDR cho thấy sự lây nhiễm xảy ra từ **5 tháng trước** thông qua **2 ổ USB riêng biệt**.
- Malware lây lan sang các endpoint khác chủ yếu do **mật khẩu yếu**. Tuy nhiên, nhờ mạng bị cách ly (air-gapped), malware không thể kết nối tới C2 server để trích xuất dữ liệu (exfiltration).
- **Khắc phục**:
  - Dùng module remediation của QRadar EDR để làm sạch các thiết bị và thư mục lưu trữ bị nhiễm.
  - Dùng giao diện **threat-hunting** để xác nhận đã loại bỏ hoàn toàn vector malware trên toàn hạ tầng.
  - Thiết lập quy tắc kiểm soát lưu lượng nội bộ chặt chẽ hơn, **tách biệt mạng công cộng khỏi mạng vận hành**, triển khai giám sát endpoint liên tục và các chiến dịch threat hunting định kỳ.

---

## 4. Kết luận
- Ngay cả các biện pháp mạnh như **air gap** vẫn có thể tồn tại lỗ hổng nếu không được triển khai nghiêm ngặt (như kiểm soát USB, mật khẩu yếu, phân tách mạng).
- Các biện pháp bảo mật liên tục và vững chắc là yếu tố sống còn để bảo vệ hạ tầng trọng yếu.
