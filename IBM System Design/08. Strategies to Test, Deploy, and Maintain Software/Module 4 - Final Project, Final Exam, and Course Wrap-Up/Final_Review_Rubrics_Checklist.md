# Final Review & Submission Guidelines: Grading Rubric Check (40/40)

> **Môn học:** IBM System Design — Course 08: Strategies to Test, Deploy, and Maintain Software (Module 4)  
> **Tài liệu nộp bài:** [NexaCare_Testing_Release_Planning_Kit_Submission.md](file:///d:/Ent/Learning/Cousera/IBM%20System%20Design/08.%20Strategies%20to%20Test,%20Deploy,%20and%20Maintain%20Software/Module%204%20-%20Final%20Project,%20Final%20Exam,%20and%20Course%20Wrap-Up/NexaCare_Testing_Release_Planning_Kit_Submission.md)  
> **Cơ chế nộp:** 2 files Word template theo yêu cầu (NexaCare Testing & Release Planning Template + NFR Template hoặc tích hợp đủ 8 phần).  
> **Điểm chuẩn tối thiểu để qua:** 70% (28/40 points).  
> **Mục tiêu đạt được:** 40/40 points (Mức 5 điểm tuyệt đối cho cả 8 Rubrics).

---

## Đối soát tiêu chí chấm điểm 8 Rubrics (Self-Audit Checklist)

| Rubric | Tiêu chí đánh giá mức 5 Điểm (Max Score) | Trạng thái đối soát trong bài nộp | Đạt điểm |
| :--- | :--- | :--- | :---: |
| **Rubric 1.1<br>Test Strategy Outline** | Chiến lược kiểm thử toàn diện, dựa trên rủi ro (risk-based). Bao quát mọi tính năng v3.0, phân loại cấp độ test (Unit, Integration, System, Security/HIPAA, Load, UAT). Thích ứng với sự đa dạng của 300 phòng khám (từ web cơ bản đến tích hợp PMS API). | Đã bao gồm: Mục tiêu bảo toàn 1.2M hồ sơ, phân tầng test chi tiết, ma trận ưu tiên P0-P3, phân tách rõ phòng khám độc lập vs phòng khám dùng API PMS. | **5 / 5** |
| **Rubric 1.2<br>Traceability Matrix** | Ma trận truy vết hoàn chỉnh, liên kết 100% yêu cầu chức năng (REQ-01 đến REQ-07) và use case sang Test Case IDs cụ thể. Bao gồm ca kiểm thử cho pilot clinics và điều kiện biên. | Bảng ma trận đầy đủ 8 cột: Req ID, Use Case, Priority, Test Case ID, Description, Test Type, Coverage Status, Pass/Fail Criteria. Bao phủ cả tải đỉnh Monday và tích hợp API cũ. | **5 / 5** |
| **Rubric 1.3<br>Annotated Test Plans** | Kế hoạch test chi tiết cho các tính năng trọng yếu. Có chú thích (annotations) về rủi ro, ca biên (edge conditions), dữ liệu bệnh nhân (HIPAA PHI) và tính biến thiên của phòng khám. | 3 Test Plans chuyên sâu: (1) SMS 3rd-party (rate limit, số E.164, HIPAA PHI); (2) Real-time concurrency (race conditions, khóa DB, rớt WebSocket); (3) Calendar Sync (OAuth token hết hạn/bị thu hồi, múi giờ IANA). | **5 / 5** |
| **Rubric 1.4<br>Deployment Checklist** | Danh sách triển khai thực tế, phân vai chính xác (Incident Commander, DevOps, DBA, QA, Comms), mốc giờ tuân thủ cửa sổ **Thứ Bảy 12:00 AM – 6:00 AM EST** và cổng quyết định **Go/No-Go Gate**. | Lộ trình 7 giai đoạn tuần tự từ T-48h đến 06:00 AM EST. Chốt chặn Go/No-Go tại **04:30 AM EST** với tiêu chí rõ ràng trước khi cutover cho 20 pilot clinics. | **5 / 5** |
| **Rubric 1.5<br>Rollback Strategy** | Kế hoạch hoàn nguyên chi tiết: Trigger points (lỗi hỏng data, vượt quá deadline 04:30 AM), quy trình khôi phục từng bước bảo vệ 1.2M hồ sơ, phân quyền người quyết định và kế hoạch truyền thông nội/ngoại bộ. | Xác định Release Manager giữ quyền quyết định; deadline cứng 04:30 AM (để kịp 90 phút restore); sơ đồ hoàn nguyên; script khôi phục cold snapshot 12:15 AM và mẫu thông báo phòng khám. | **5 / 5** |
| **Rubric 1.6<br>Data Migration Plan** | Kế hoạch di chuyển dữ liệu thực tế: Ánh xạ mức trường (field-level mapping), quy tắc chuyển đổi, ước lượng khối lượng 1.2M hồ sơ, script thẩm định và các bước khôi phục. | Bảng Mapping 6 trường dữ liệu then chốt (UUIDv5, chuẩn E.164, mã hóa AES-256-GCM cho PHI, opt-in flag). Cơ chế chạy batch 10,000 rows, đối soát row count $\Delta = 0$, hash checksum và xử lý lỗi duplicate/malformed. | **5 / 5** |
| **Rubric 1.7<br>Post-Deployment Monitoring** | Định nghĩa ngưỡng thành công, KPI cho từng tính năng mới (tỷ lệ lỗi SMS, calendar sync error, latency), vai trò giám sát, ngưỡng cảnh báo (alert thresholds), chu kỳ báo cáo và kênh tiếp nhận phản hồi cho nhóm pilot. | Bộ chỉ số cụ thể (5xx < 0.1%, latency P95 < 500ms, SMS failure < 1%); công cụ Datadog, ELK, Prometheus; cơ chế War Room 24/7 Hypercare 48h ưu tiên hàng đầu cho 20 phòng khám pilot. | **5 / 5** |
| **Rubric 1.8<br>NFR & Performance Plan** | Định nghĩa NFR đo lường được (Performance, Scalability, Availability, Security), giám sát **4 Golden Signals**, chiến lược đón đầu tải đỉnh sáng thứ Hai (3–5x) với ngưỡng cảnh báo thích ứng và tối ưu hóa 3 tầng. | Bảng NFR định lượng; bảng Four Golden Signals; ngưỡng thích ứng tải đỉnh thứ Hai (8–10 AM); mô hình tối ưu 3 tầng Top-Down (Infra HPA/CDN $\rightarrow$ App Redis/Queue $\rightarrow$ DB Index/PgBouncer) kèm runbook Circuit Breaking. | **5 / 5** |

---

## Hướng dẫn nộp bài (Submission Instructions)

1. Mở file Word template của khóa học: `NexaCare-Testing-Release-Planning-Template.docx` và `NFR template.docx` (hoặc dán toàn bộ vào template chính nếu được nộp dạng tài liệu hợp nhất).
2. Sao chép trực tiếp nội dung tương ứng từng phần từ file [NexaCare_Testing_Release_Planning_Kit_Submission.md](file:///d:/Ent/Learning/Cousera/IBM%20System%20Design/08.%20Strategies%20to%20Test,%20Deploy,%20and%20Maintain%20Software/Module%204%20-%20Final%20Project,%20Final%20Exam,%20and%20Course%20Wrap-Up/NexaCare_Testing_Release_Planning_Kit_Submission.md).
3. Đảm bảo giữ nguyên các tiêu đề chuẩn hóa:
   - `1. Test strategy outline`
   - `2. Traceability matrix`
   - `3. Annotated test plans`
   - `4. Deployment checklist`
   - `5. Rollback strategy`
   - `6. Data migration plan`
   - `7. Post-deployment monitoring summary`
   - `8. Non-functional requirements and performance plan`
4. Lưu thành file `.docx` / `.pdf` và tải lên cổng nộp bài Coursera.
