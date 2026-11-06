# Final Project Overview: Testing & Release Planning Kit (NexaCare v3.0)

> **Khóa học:** IBM System Design — Course 08: Strategies to Test, Deploy, and Maintain Software (Module 4)  
> **Tổng điểm:** 40 points (8 phần x 5 points)

---

## 1. Bối cảnh & Ràng buộc cốt lõi (NexaCare v3.0)

- **Doanh nghiệp:** NexaCare Solutions — nền tảng đặt lịch khám cho hơn 300 phòng khám tại Bắc Mỹ.
- **Tính năng mới v3.0:**
  1. *SMS Reminders:* Tự động gửi SMS nhắc hẹn trước 24h & 1h qua dịch vụ bên thứ 3 hoàn toàn mới.
  2. *Real-time Availability:* Cập nhật trạng thái rảnh/bận tức thời, chống double-booking.
  3. *Calendar Sync:* Đồng bộ lịch 2 chiều với Google Calendar và Outlook.
  4. *Redesigned UI:* Giao diện mới chuẩn accessibility (WCAG) trên Web/Mobile.
- **Ràng buộc & Rủi ro chính:**
  - *Dữ liệu:* 1.2M hồ sơ bệnh nhân nhạy cảm (tuân thủ HIPAA); từng có tiền lệ mất dữ liệu ở sản phẩm khác nên yêu cầu kiểm soát rủi ro tối đa.
  - *Phòng khám:* Trình độ công nghệ không đều (từ dùng web cơ bản đến tích hợp qua API hệ thống PMS).
  - *Cửa sổ bảo trì:* Thứ Bảy, 12:00 AM – 6:00 AM EST (tối đa 6 tiếng downtime).
  - *Tải cao điểm:* Sáng thứ Hai (8-10 AM) lưu lượng tăng 3–5 lần bình thường.
  - *Lộ trình:* Chạy thử nghiệm Pilot trên 20 phòng khám trước khi mở toàn hệ thống.

---

## 2. Yêu cầu nộp bài: 8 Sections chuẩn hóa (5 pts/section)

Tài liệu nộp duy nhất gồm 8 phần bắt buộc đúng tiêu đề:

1. **Test strategy outline:** Phương pháp tiếp cận kiểm thử toàn diện (Functional, Regression cho 300 phòng khám, Integration với 3rd-party SMS/Calendar/PMS, Security/HIPAA, Load test tải đỉnh 3-5x, UAT với nhóm pilot).
2. **Traceability matrix:** Bảng ánh xạ 100% yêu cầu tính năng (Req ID, Use Cases) sang Test Case IDs, độ ưu tiên và tiêu chí Pass/Fail.
3. **Annotated test plans:** Kế hoạch test chi tiết kèm ghi chú rủi ro và ca biên (edge cases) cho 4 tính năng: SMS rate limit/opt-out, race-condition đặt trùng slot thời gian thực, token sync calendar bị revoke, màn hình responsive/screen reader UI mới.
4. **Deployment checklist:** Danh sách các bước triển khai theo mốc giờ trong 6 tiếng (Pre-check, Backup, Migrate DB, Deploy app, Smoke test) kèm phân vai rõ ràng và cổng quyết định **Go/No-Go** trước 05:00 AM.
5. **Rollback strategy:** Kế hoạch hoàn nguyên khẩn cấp (triggers kích hoạt, deadline quyết định lúc 04:30–05:00 AM để kịp 1h khôi phục, restore DB snapshot, revert code v2.x và thông báo sự cố).
6. **Data migration plan:** Chiến lược chuyển đổi an toàn 1.2M bản ghi bệnh nhân sang schema v3.0 (chạy script batching tránh lock bảng, đối soát số lượng row count 100%, checksum và kiểm tra tính toàn vẹn dữ liệu).
7. **Post-deployment monitoring summary:** Kế hoạch theo dõi sau cutover (lỗi 5xx, độ trễ API, tỷ lệ gửi SMS/sync calendar thất bại, thiết lập War Room và kênh hỗ trợ ưu tiên cho 20 pilot clinics).
8. **Non-functional requirements and performance plan:** Định nghĩa mục tiêu NFR (Latency p95 < 500ms, Uptime 99.9%, mã hóa TLS 1.3/AES-256), theo dõi **4 Golden Signals** (Latency, Traffic, Errors, Saturation) và giải pháp tối ưu 3 tầng: DB (indexing, connection pool), App (Redis cache, async queue cho SMS/Calendar), Infra (Pod autoscaling trước 7:30 AM thứ Hai).

---

## 3. Tiêu chí chấm điểm (Rubric)

- **Completeness:** Đủ 8 phần với đúng tên tiêu đề.
- **Relevance:** Bám sát tuyệt đối bài toán NexaCare (1.2M records, SMS bên thứ 3, 20 pilot clinics, tải đỉnh thứ Hai).
- **Professionalism & Application:** Trình bày cấu trúc rõ ràng, áp dụng chính xác các nguyên lý phát hành, kiểm thử và vận hành hệ thống.
