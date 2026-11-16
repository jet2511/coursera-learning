# Threat Intelligence (Tình báo mối đe dọa)

## 1. Khái niệm
**Threat Intelligence** là quá trình thu thập và phân tích thông tin về các cuộc tấn công tiềm ẩn có thể đe dọa tổ chức (bao gồm phương thức, chiến thuật, chiến lược của tội phạm mạng, các mẫu nhận dạng và IoCs). Mục tiêu là phòng thủ chủ động (preemptively) và củng cố tư thế bảo mật (security posture) của tổ chức.

---

## 2. Ba loại Threat Intelligence chính
1. **Behavioral Threat Intelligence (Tình báo hành vi)**:
   - Tập trung phân tích mẫu hành vi, phương pháp và chiến thuật của kẻ tấn công.
   - Giúp đội ngũ bảo mật dự đoán cuộc tấn công, phát hiện bất thường/sai lệch trong hành vi mạng một cách chủ động.
2. **Reputational Threat Intelligence (Tình báo danh tiếng)**:
   - Theo dõi độ uy tín của các địa chỉ IP, domain, URL dựa trên lịch sử hành vi.
   - Giúp đánh giá rủi ro và tránh tương tác với các domain/IP độc hại.
3. **Threat Data (Dữ liệu mối đe dọa)**:
   - Dữ liệu thô, chưa qua xử lý (từ logs, alerts, packet captures).
   - Chưa thể hành động ngay nhưng là nền tảng để phân tích sâu hơn và tạo ra các loại threat intelligence hữu ích.

---

## 3. Các nguồn Threat Intelligence
| Nguồn | Mô tả | Ví dụ |
| :--- | :--- | :--- |
| **Open-Source Threat Feeds** | Nguồn công khai (blog, diễn đàn, mạng xã hội). Cần lọc nhiễu kỹ lưỡng. | ThreatConnect, AlienVault OTX, `@malwrhunterteam`, Krebs on Security, Dark Reading |
| **Proprietary Threat Feeds** | Nguồn trả phí/độc quyền từ các công ty bảo mật, cung cấp thông tin chi tiết và có tính hành động cao. | Symantec DeepSight, IBM X-Force Exchange, CrowdStrike Falcon X |
| **Deep and Dark Web** | Khu vực không được công cụ tìm kiếm lập chỉ mục, nơi tội phạm mạng trao đổi, lên kế hoạch tấn công. Cần công cụ và chuyên môn đặc biệt. | Silk Road (đã đóng), AlphaBay, các diễn đàn ẩn trên mạng Tor |
| **Industry Reports & Threat Bulletins** | Báo cáo xu hướng, lỗ hổng mới và các cuộc tấn công gần đây từ tổ chức nghiên cứu. | IBM X-Force Threat Intelligence Index, Verizon DBIR, US-CERT |
| **Government & Regulatory Bodies** | Cảnh báo từ cơ quan an ninh mạng quốc gia/quốc tế, hữu ích cho các mối đe dọa cấp nhà nước hoặc quy mô lớn. | CISA, FBI, NCSC (UK), ENISA (EU) |
| **Incident Response (IR) Teams** | Thông tin thực tế từ đội ngũ ứng cứu sự cố nội bộ hoặc bên ngoài khi trực tiếp xử lý tấn công. | Phương thức tấn công ransomware, IP chiến dịch phishing, signature malware mới |
| **Honeypots & Deception Technology** | Hệ thống mồi nhử thu hút kẻ tấn công để giám sát và phân tích TTPs (Tactics, Techniques, Procedures). | Phát hiện biến thể malware mới, mẫu hành vi, vector tấn công chưa từng biết |
