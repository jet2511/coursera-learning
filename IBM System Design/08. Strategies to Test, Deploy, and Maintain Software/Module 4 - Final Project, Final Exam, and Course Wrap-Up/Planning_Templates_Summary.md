# Planning Templates: Testing, Migration, Deployment

> **Khóa học:** IBM System Design — Course 08: Strategies to Test, Deploy, and Maintain Software (Module 4)  
> **Mục tiêu:** Cung cấp 3 template chuẩn mẫu để áp dụng trực tiếp vào tài liệu Final Project (NexaCare Solutions).

---

## Template 1: Test Strategy Outline

Tài liệu định hướng phạm vi, cấp độ và kỳ vọng kiểm thử giữa QA Lead, Solutions Architect và Product Owner.

| Trường thông tin | Ví dụ mẫu (CoursePilot v1.2.0) | Ứng dụng vào NexaCare v3.0 |
| :--- | :--- | :--- |
| **System & Version** | CoursePilot – v1.2.0 | NexaCare Appointment Platform – v3.0 |
| **Test Levels** | Unit, Integration, System, UAT | Unit, Integration (SMS/Calendar/PMS), System/Regression, Security/HIPAA, Load, UAT |
| **Primary Objectives** | Đảm bảo đăng ký, tạo khóa học, engine xếp lịch chạy đúng | Đảm bảo tính năng SMS nhắc hẹn, real-time availability, calendar sync, redesigned UI hoạt động tin cậy |
| **In-scope** | Xuất bản khóa học, logic ghi danh, engine xếp lịch | 4 tính năng mới + luồng nghiệp vụ đặt/hủy/đổi lịch hiện hữu của 300 phòng khám |
| **Out-of-scope** | Mẫu email thông báo, giao diện admin billing | Các module billing nội bộ không bị ảnh hưởng đợt này |
| **Test Environment** | Pre-production cloud instance (dữ liệu ẩn danh) | Staging/Pre-prod mô phỏng cấu hình prod, dùng 1.2M records giả lập/anonymized PHI |
| **Acceptance Criteria** | Dựa trên PRD và phản hồi UAT | 100% test case trọng yếu pass; không có lỗi Severity 1 & 2; hiệu năng p95 < 500ms |
| **Risks / Constraints** | Hạn chế tester UAT, refresh DB hàng tuần | Nguy cơ mất dữ liệu (tiền lệ xấu); SMS 3rd-party rate limit; tải đỉnh thứ Hai (3-5x) |
| **Key Stakeholders** | QA Lead, Systems Analyst, Architect, PO | QA Lead, DevOps, DBA, Product Owner, Support Lead, Đại diện 20 phòng khám Pilot |

---

## Template 2: Data Migration Mapping Table

Bảng quy chuẩn chuyển đổi dữ liệu từ hệ thống cũ (Legacy) sang hệ thống mới (Target), kèm quy tắc biến đổi và phê duyệt nghiệp vụ.

| Legacy Field | Target Field | Transformation Rule | Notes / Stakeholder Comments |
| :--- | :--- | :--- | :--- |
| `user_id` | `student_id` | None (Direct 1:1) | Xác nhận bởi Registrar's Office |
| `full_name` | `first_name`, `last_name` | Split theo khoảng trắng | Xử lý ca biên: tên đệm, tên có gạch nối (`-`) |
| `course_code` | `course_id` | Direct match | Chuẩn hóa theo schema khóa học mới |
| `enroll_date` | `registration_date` | `MM/DD/YYYY` → `YYYY-MM-DD` | Đã kiểm chứng qua đợt chạy thử (dry run) |
| `payment_status`| `tuition_flag` | `Y/N` → `Paid/Unpaid` | Xác nhận với bộ phận Tài chính |

> **Áp dụng vào NexaCare v3.0:** Bảng này dùng trực tiếp cho **Section 6 (Data Migration Plan)** để ánh xạ 1.2M hồ sơ bệnh nhân (ví dụ: `patient_phone` sang chuẩn quốc tế E.164 cho SMS, thêm cờ `sms_opt_out`, mã hóa trường `ssn`/`health_id`, token đồng bộ lịch).

---

## Template 3: Deployment Readiness Checklist

Bảng theo dõi trạng thái công việc, phân vai (Owner) và chốt chặn phê duyệt trước giờ G.

| Task | Owner | Status | Notes |
| :--- | :--- | :---: | :--- |
| **QA Sign-off completed** | QA Lead | Done | Vượt qua 100% test case trên Staging |
| **Final UAT session conducted** | Systems Analyst | Done | Đã vá và retest xong 2 defect phát hiện |
| **Architecture alignment verified** | Solutions Architect | Done | Đảm bảo đáp ứng chuẩn mở rộng và tuân thủ (compliance) |
| **Deployment window confirmed** | DevOps Lead | Confirmed | Cửa sổ bảo trì: Thứ Bảy, 12:00 AM – 6:00 AM EST |
| **Rollback plan reviewed & approved**| Release Manager | Approved | Đã tạo snapshot DB và backup artifact trước giờ G |
| **Stakeholder Go/No-Go collected** | Product Owner | Pending | Chờ xác nhận cuối cùng tại cổng quyết định |
| **Migration dry run rehearsed** | Data Analyst / DBA | Done | Khớp 100% số lượng bản ghi (record count reconciliation) |
| **System monitoring configured** | IT Support / SRE | Done | Đã kích hoạt cảnh báo latency, lỗi 5xx, saturation |

---

## Tóm tắt cốt lõi
1. **Test Strategy:** Xác định rõ *sẽ test cái gì*, *ở đâu*, *mức độ nào* và *ai chịu trách nhiệm*.
2. **Data Migration Mapping:** Chi tiết hóa quy tắc biến đổi từng trường, chặn đứng rủi ro mất mát hoặc sai lệch dữ liệu.
3. **Deployment Checklist:** Chốt chặn an toàn với người chịu trách nhiệm (Owner) rõ ràng, bảo đảm sẵn sàng cho quyết định Go/No-Go và Rollback.
