# Module 4: Final Project Overview & Walkthrough (NexaCare Solutions Upgrade)

> **Khóa học:** IBM System Design — Course 08: Strategies to Test, Deploy, and Maintain Software  
> **Nguồn:** Video *Final Project Overview and Walkthrough* & Lộ trình Module 4

---

## 1. Bản chất & Vai trò trong Final Project

- **Vai trò:** Bạn đóng vai trò **Systems Professional** dẫn dắt toàn diện đợt phát hành phần mềm lớn cho **NexaCare Solutions** (nâng cấp nền tảng web đặt lịch khám bệnh).
- **Yêu cầu cốt lõi:**
  - **Không yêu cầu viết code:** Tập trung hoàn toàn vào lập kế hoạch, tài liệu hóa, phân tích rủi ro và điều phối kỹ thuật (systems planning, documentation, release coordination).
  - **Không dùng kế hoạch chung chung:** Tất cả tài liệu phải bám chặt (anchored) vào case study thực tế của NexaCare (300 phòng khám, 1.2M hồ sơ bệnh nhân, downtime 6h, tải đỉnh 3-5x sáng thứ Hai).
  - **Mục tiêu tối thượng:** Đảm bảo hệ thống phát hành an toàn, không mất dữ liệu, hạn chế gián đoạn dịch vụ và xây dựng niềm tin cho các bên liên quan.

---

## 2. 4 Tính năng mới & Thách thức nghiệp vụ cần giải quyết

1. **Patient SMS Reminders:** Tự động gửi tin nhắn trước 24h & 1h (tích hợp qua nhà cung cấp bên thứ 3 mới).
2. **Real-time Doctor Availability:** Bác sĩ cập nhật trạng thái trống lịch tức thời; giải quyết triệt để vấn đề double-booking.
3. **Calendar Integration:** Đồng bộ 2 chiều với Google Calendar và Microsoft Outlook.
4. **Redesigned UI:** Giao diện mới chuẩn WCAG (accessibility), tối ưu cho cả desktop và mobile của phòng khám.

---

## 3. Bộ sản phẩm bàn giao: Testing and Release Planning Kit (8 Sections)

Bộ tài liệu nộp duy nhất bao gồm 8 phần chuẩn hóa:
1. **Test Strategy Outline:** Chiến lược kiểm thử toàn diện (Functional, Regression, Integration, Security/HIPAA, Load, UAT).
2. **Traceability Matrix:** Ánh xạ 100% yêu cầu & ca sử dụng sang Test Cases với tiêu chí Pass/Fail.
3. **Annotated Test Plans:** Kế hoạch kiểm thử tính năng kèm phân tích rủi ro & edge cases (rate limit SMS, race condition đặt lịch, lỗi token sync).
4. **Deployment Checklist:** Lộ trình chi tiết từng bước trong 6 tiếng bảo trì kèm phân vai (DevOps, QA, DBA, Support) và cổng quyết định **Go/No-Go**.
5. **Rollback Strategy:** Kịch bản hoàn nguyên khẩn cấp (triggers, deadline quyết định trước 05:00 AM, restore DB snapshot và revert code v2.x).
6. **Data Migration Plan:** Kế hoạch chuyển đổi 1.2M bản ghi (batch migration, đối soát row count 100%, checksum và ràng buộc toàn vẹn).
7. **Post-Deployment Monitoring Summary:** Giám sát sau cutover (lỗi 5xx, latency, tỷ lệ lỗi SMS/Sync, kênh trực War Room ưu tiên 20 pilot clinics).
8. **Non-Functional Requirements & Performance Plan:** NFR targets, giám sát **4 Golden Signals** (Latency, Traffic, Errors, Saturation), tối ưu 3 tầng: DB (index, pool), App (Redis cache, async queue), Infra (Autoscaling đón đầu tải thứ Hai).

---

## 4. Câu hỏi định hướng tư duy khi thực hiện

- **Chức năng then chốt:** Những tính năng nào sống còn với phòng khám và bệnh nhân?
- **Rủi ro thất bại:** Nếu nâng cấp gặp sự cố, quy trình xử lý và bảo vệ dữ liệu ra sao?
- **Toàn vẹn dữ liệu:** Dữ liệu nào cần bảo toàn nguyên vẹn, dữ liệu nào cần chuyển đổi (transform)?
- **Đo lường ổn định:** Dựa vào những chỉ số và ngưỡng cảnh báo nào để khẳng định hệ thống đã ổn định sau khi Go-Live?
