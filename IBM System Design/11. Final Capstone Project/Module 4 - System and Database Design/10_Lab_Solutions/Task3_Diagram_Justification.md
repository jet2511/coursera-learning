# Task 3: Justify the Security Architecture Diagram

Bản giải trình kiến trúc an ninh bảo mật đa tầng cho nền tảng ngân hàng số Retail Bank.

---

## Các luận điểm giải trình then chốt (Key Architectural Justifications):

1. **Thực thi nguyên lý Phòng thủ theo chiều sâu (Defense-in-Depth):**
   - Kiến trúc không chỉ dựa vào tường lửa biên giới (Perimeter Firewall) mà thiết lập 4 lớp kiểm soát độc lập. Kẻ tấn công nếu có thể vượt qua lớp mạng (Network) vẫn sẽ bị chặn lại ở tầng Ứng dụng (WAF, API Gateway, OAuth2) hoặc tầng Dữ liệu (mã hóa TDE, Tokenization, và kiểm soát quyền RBAC/ABAC).

2. **Triệt để áp dụng mô hình Zero-Trust ("Never Trust, Always Verify"):**
   - Mọi kết nối giữa các Microservices trong vùng nội bộ (East-West Traffic) đều bắt buộc phải xác thực thông qua Mutual TLS (mTLS) và kiểm tra tính hợp lệ của JWT token. Nhân viên ngân hàng truy cập từ xa bắt buộc phải qua cổng SASE / VPN kết hợp xác thực đa yếu tố (MFA).

3. **Bảo vệ ứng dụng theo chu trình DevSecOps từ sớm (Shift-Left Security):**
   - Tích hợp công cụ rà quét tĩnh (SAST SonarQube), quét động (DAST OWASP ZAP) và quét lộ lọt mã bí mật (Secret Scanning) trực tiếp vào CI/CD Pipeline. Đảm bảo 100% các lỗ hổng OWASP Top 10 được phát hiện và khắc phục ngay trong giai đoạn phát triển trước khi release lên môi trường Production.

4. **Bảo vệ dữ liệu nhạy cảm theo chuẩn khắt khe PCI-DSS & GDPR:**
   - Dữ liệu số thẻ thanh toán được **Token hóa (Tokenization)** và lưu trữ cô lập trong phân vùng PCI Card Vault riêng biệt; các trường dữ liệu định danh eKYC và số dư tài khoản được mã hóa toàn diện (AES-256) với cơ chế bảo vệ khóa qua thiết bị phần cứng chuyên dụng **KMS / CloudHSM**.

5. **Năng lực giám sát tập trung và phản ứng sự cố tự động (SIEM & SOC 24/7):**
   - Toàn bộ log an ninh từ Firewall, WAF, API Gateway, Container, và Database đều được đẩy về hệ thống SIEM tập trung theo thời gian thực. Cơ chế tương quan sự kiện (Event Correlation) và DLP giúp Trung tâm Điều hành An ninh (SOC) phát hiện ngay các dấu hiệu rò rỉ dữ liệu hoặc xâm nhập trái phép, tự động kích hoạt cô lập (Containment) trong vòng vài giây.
