# Architects' Role in Security Incidents and Failures

> **Khóa học**: Cybersecurity Architecture (IBM)  
> **Module 3**: Network, Application, and Data Security  
> **Bài học**: Architects' Role in Security Incidents and Failures (Thời lượng: ~6 phút)

---

## 🎯 Mục tiêu học tập
- Xác định vai trò của kiến trúc sư hệ thống trong **ứng phó sự cố (Incident Response)** và **rà soát sau sự cố (Post-incident Review)**.
- Biến phát hiện từ sự cố thành **cải tiến kiến trúc, biện pháp kiểm soát và mẫu thiết kế có khả năng phục hồi**.

> Kiến trúc sư không được đứng ngoài cuộc khi sự cố xảy ra. Giống như kiến trúc sư đô thị thiết kế hệ thống thoát nước và công sự phòng thủ, kiến trúc sư hệ thống phải thiết kế phòng thủ cho hệ thống.

---

## 🧱 4 Tầng Vai Trò Của Kiến Trúc Sư

### Layer 1: Hành động ứng phó tức thời (Immediate Incident Response)
1. **Vẽ đường tấn công (Draw the attack path)** — trong 24 giờ đầu:
   - Lập bản đồ chính xác cách kẻ tấn công di chuyển trong hệ thống.
   - Dùng **Microsoft Threat Modeling Tool** để trực quan hóa kiến trúc rồi chồng đường xâm nhập thực tế lên.
   - Xác định nơi phân đoạn mạng thất bại, ranh giới tin cậy (trust boundaries) nào bị vượt qua.
2. **Xác định điểm nghẽn kiến trúc (Architectural choke points)**:
   - Tìm các điểm đang bị khai thác, đề xuất **cô lập ở mức kiến trúc**, không chỉ chặn IP.
3. **Rà soát kiến trúc khẩn cấp**:
   - Đánh dấu mọi thành phần kẻ tấn công đã chạm tới trên Data Flow Diagram; xác định các hệ thống lân cận đang gặp rủi ro.
   - Dùng **OWASP Threat Dragon** để tìm các đường di chuyển ngang (lateral movement) tiếp theo.

### Layer 2: Phân tích nguyên nhân gốc dưới góc nhìn kiến trúc (Root Cause Analysis)
- Đội bảo mật tập trung vào *điều gì đã xảy ra*; kiến trúc sư phải hiểu *vì sao điều đó có thể xảy ra*.
- **Phân tích STRIDE** cho từng thành phần bị xâm phạm: *Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege*.
- **Lập danh sách lỗi thiết kế (Design flaws)**:
  - Thiếu ranh giới xác thực.
  - Quan hệ tin cậy quá mức giữa các dịch vụ.
  - Thiếu mã hóa tại một số điểm truyền dữ liệu.
  - Phân đoạn mạng quá lỏng.
  - Thiếu giám sát tại các điểm giao trọng yếu.
- **Phân tích bằng AI**: Dùng **ThreatModeler**, **IriusRisk** (phiên âm trong video là "RSTUEN") để tìm các lỗ hổng tương tự ở nơi khác.
  - *Số liệu*: AI Threat Modeling Copilot của J.P. Morgan phát hiện trung bình **thêm 9 mối đe dọa/mô hình** mà con người bỏ sót.

### Layer 3: Thiết kế kiến trúc phòng ngừa (Preventative Architecture)
- **Ranh giới Zero Trust**: Mọi lệnh gọi service-to-service đều cần xác thực, mọi truy cập dữ liệu cần phân quyền, mọi giao dịch đều được ghi log.
- **Giới hạn bán kính thiệt hại (Blast radius containment)**:
  - Thiết kế theo các phân đoạn cô lập; web server bị chiếm cũng không thể chạm trực tiếp tới database.
  - Dùng **SD Elements** để tự động sinh yêu cầu bảo mật cho từng thành phần theo khung như **NIST CSF**.
- **Threat modeling liên tục**:
  - Công cụ tự động hóa threat modeling (IriusRisk) tăng khả năng nhìn thấy mối đe dọa **40%** và triển khai cloud an toàn nhanh hơn **80%**.
  - Tích hợp **Threagile** (mã nguồn mở) vào CI/CD để chạy threat model dưới dạng code mỗi khi kiến trúc thay đổi.

### Layer 4: Cơ chế dự phòng thực tiễn (Practical Failsafe Mechanisms)
| Cơ chế | Mô tả |
| :--- | :--- |
| **Default deny everything** | Network policy, API gateway, service mesh chặn mặc định; chỉ whitelist những gì cần thiết. |
| **Circuit breakers cho bảo mật** | Rate limiting, connection throttling, tự động khóa ở mức kiến trúc; dịch vụ nhận nhiều lần xác thực bất thường sẽ tự bị cô lập. |
| **Immutable infrastructure** | Thiết kế để *thay thế nhanh, không vá*; container bị xâm phạm thì hủy và dựng lại. |

> Tổ chức dùng bảo mật hỗ trợ AI phát hiện vi phạm nhanh hơn **108 ngày**, tiết kiệm **1,6 triệu USD/vụ**. Nhưng phát hiện chỉ có ích khi có khả năng phản ứng.

---

## ✅ Checklist Ứng Phó Sự Cố Cho Kiến Trúc Sư

| Giai đoạn | Hành động |
| :--- | :--- |
| **Giờ 1–24** | Vẽ đường tấn công trên sơ đồ kiến trúc; xác định các hệ thống lân cận bị phơi nhiễm. |
| **Ngày 2–7** | Chạy phân tích STRIDE; ghi lại mọi quyết định kiến trúc đã tạo điều kiện cho vi phạm. |
| **Tuần 2–4** | Thiết kế lại các thành phần dễ tổn thương theo Zero Trust; triển khai threat modeling tự động. |
| **Liên tục** | Tích hợp ThreatModeler / OWASP Threat Dragon vào các buổi design review; lấy **Assume Breach** làm tư duy mặc định. |

---

## 🧠 Tóm tắt Cốt lõi
1. Vai trò của kiến trúc sư vượt ra ngoài kiềm chế tức thời: đảm bảo **khả năng phục hồi và trách nhiệm giải trình dài hạn**.
2. Mỗi sự cố bộc lộ lỗ hổng thiết kế; cần cân bằng giữa độ tin cậy và quản trị rủi ro thực tế.
3. **Post-incident review** biến điểm yếu thành mẫu kiến trúc và kiểm soát phòng ngừa mạnh hơn.
4. Giao tiếp sự cố hiệu quả cần rõ ràng: dịch phát hiện kỹ thuật thành hành động cụ thể, thống nhất các nhóm chức năng.
5. Kiến trúc tốt là kiến trúc **chống chịu, phát hiện và phục hồi** sau tấn công.

> [!NOTE]
> Một số tên công cụ trong bản transcript bị nhận dạng giọng nói sai ("RSTUEN", "Thragile"); mình đã hiệu chỉnh theo công cụ có khả năng đúng nhất là IriusRisk và Threagile.
