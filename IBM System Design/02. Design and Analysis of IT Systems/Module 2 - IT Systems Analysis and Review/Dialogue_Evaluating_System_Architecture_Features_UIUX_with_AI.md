# Dialogue: Evaluating System Architecture, Features, and User Experience with AI

> **Nguồn:** IBM System Design – Module 2: IT Systems Analysis and Review  
> **Chủ đề:** Đánh giá toàn diện hệ thống LMS trường học trực tuyến (EdTech Platform Case Study)  
> **Ngày lưu:** 2026-08-14

---

## 🎯 Bối Cảnh Tình Huống (Scenario)

Một công ty giáo dục trực tuyến đang tăng trưởng nhanh gặp 5 bài toán hóc búa với hệ thống **LMS (Learning Management System)**:
1. **Hiệu năng:** Tải trang chậm khi sinh viên nộp bài đồng thời trong giờ cao điểm.
2. **UI/UX:** Điều hướng môn học quá phức tạp, mất nhiều lượt click để tìm tài liệu.
3. **Tính năng:** Giảng viên thiếu dashboard phân tích và báo cáo tiến độ học tập.
4. **Tiếp cận (a11y):** Vi phạm nhiều chuẩn tiếp cận **WCAG 2.1** (bàn phím, Screen Reader).
5. **Kiến trúc:** Khó tích hợp công cụ học tập của bên thứ ba (LTI / Third-party APIs).

---

## 🧭 Khung Đánh Giá 7 Bước Của Systems Analyst

```
[1. Investigation]     → Phỏng vấn Stakeholders, Giám sát APM, Audit a11y, Rà soát kiến trúc
[2. Inefficiencies]    → Dự đoán & Xác thực nghẽn CSDL (JMeter/Datadog), Lỗi WCAG (WAVE/NVDA)
[3. Architecture]      → Bóc tách hạn chế Monolith, Ghép nối chặt, Xử lý đồng bộ, Thiếu API mở
[4. Feature Alignment] → Lập Feature Gap Matrix, Đo lường User KPIs, Benchmarking đối thủ
[5. UI/UX Evaluation]  → Heuristic Nielsen, Task Analysis, Wave Audit, Hotjar Heatmaps
[6. Recommendations]   → Phân cấp: Quick Wins (Ngay) $\rightarrow$ Medium (Tính năng) $\rightarrow$ Long-term (Microservices)
[7. AI & Sustainability]→ Dùng AI hỗ trợ Logs/NLP + Human Validation + CI/CD & Giám sát liên tục
```

---

## 1. Kế Hoạch Điều Tra Ban Đầu (Initial Investigation)

- **Stakeholder Interviews:** Khảo sát sinh viên và giảng viên để ghi nhận pain points và tính năng còn thiếu.
- **Performance Monitoring:** Dùng **Datadog / APM** đo Response time, độ trễ query DB và tải CPU/RAM giờ cao điểm.
- **Usability & a11y Audit:** Task analysis đếm số click điều hướng; dùng **WAVE** và **NVDA Screen Reader** rà soát chuẩn WCAG 2.1.
- **Architecture Review:** Xem xét sơ đồ UML Component, cấu trúc CSDL và tài liệu API để tìm rào cản tích hợp.

---

## 2. Nhận Diện Điểm Nghẽn & Khoảng Trống (Gaps & Verification)

| Phân loại | Vấn đề dự đoán | Phương pháp xác thực (Confirmation) |
|---|---|---|
| **Performance** | Khóa bảng CSDL và nghẽn I/O khi upload file nặng. | Chạy Stress test bằng **Apache JMeter** và soi slow-query log trên **Datadog**. |
| **Feature Gaps** | Giảng viên thiếu báo cáo tiến độ và phân tích học tập. | Lập ma trận đối chiếu tính năng (**Feature Gap Matrix**) với nhu cầu thực tế. |
| **UI/UX & a11y** | Menu phân cấp quá sâu, vi phạm tương phản màu và thiếu thẻ ARIA. | Task step analysis, quét tự động **WAVE** và test thủ công bằng phím Tab/NVDA. |
| **Architecture** | Kiến trúc Monolithic cũ, thiếu chuẩn LTI và REST APIs mở. | Rà soát mã nguồn và kiểm thử API endpoints bằng **Postman**. |

---

## 3. Ảnh Hưởng Của Kiến Trúc Đến Khả Năng Mở Rộng & Tích Hợp

```
[Monolithic & Tight Coupling]  → Toàn bộ module dùng chung 1 codebase & DB → Không thể scale riêng lẻ service nộp bài.
[Synchronous Processing]       → Xử lý upload file đồng bộ làm nghẽn luồng (threads) của Web server.
[Lack of Standardized APIs]    → Thiếu chuẩn LTI/REST APIs làm tăng ma sát và rủi ro bảo mật khi kết nối tool ngoài.
[Centralized DB Bottleneck]    → Request dồn thẳng vào DB mà không có Redis Cache hay Read-replicas.
```

---

## 4. Đánh Giá Tính Năng Đối Chiếu Với Mục Tiêu Chiến Lược

- **Feature Gap Matrix:** Ánh xạ tính năng hiện có với mục tiêu tăng trưởng và mức độ hài lòng của sinh viên.
- **User KPIs & Surveys:** Đo lường CSAT/NPS gắn với từng tính năng cụ thể.
- **Usage Telemetry:** Phân tích log xem module nào được dùng nhiều, module nào bị bỏ rơi do UX khó dùng.
- **Competitive Benchmarking:** So sánh tính năng với các LMS hiện đại (Canvas, Blackboard) về AI grading, Gamification.

---

## 5. Phương Pháp Đánh Giá UI/UX & Insights Thu Được

| Phương pháp | Cách thực hiện | Insights thu được |
|---|---|---|
| **Heuristic Evaluation** | Đánh giá theo 10 nguyên lý Nielsen | Phát hiện lỗi thiếu nhất quán, nhãn menu gây hiểu nhầm, thiếu trạng thái phản hồi. |
| **Task Flow Analysis** | Đo số bước click tìm bài giảng/nộp bài | Chỉ ra các bước click dư thừa và phân cấp menu quá sâu. |
| **Accessibility Testing** | Quét tự động bằng WAVE + Tab/NVDA | Phát hiện màu chữ tương phản thấp, thiếu `alt text`, nút bấm không có ARIA label. |
| **Usability & Heatmaps** | Ghi hình phiên dùng thử & Heatmap Hotjar | Thấy rõ điểm sinh viên bị khựng lại, nhấp nhầm hoặc bỏ cuộc (drop-off points). |

---

## 6. Đề Xuất Cải Tiến Thực Tế Phân Cấp Ưu Tiên (Recommendations)

### 🔴 Ưu tiên cao (Immediate Quick Wins)
- **UI/UX & a11y:** Tinh gọn menu với shortcut trực tiếp đến bài tập; sửa lỗi WCAG (tăng tương phản, thêm `alt text`, nhãn ARIA).
- **Database Tuning:** Đánh Index các bảng nộp bài; cài đặt **Redis Cache** để giảm tải truy vấn tức thời.

### 🟡 Ưu tiên trung bình (Medium Priority - Functional & Workflow)
- **Instructor Dashboard:** Xây dựng dashboard theo dõi tiến độ học tập và xuất báo cáo tự động cho giảng viên.
- **Asynchronous Uploads:** Chuyển luồng nộp bài sang hàng đợi xử lý nền (**Background Queues / Message Queue**) kèm thanh tiến độ.

### 🟢 Ưu tiên dài hạn (Long-term Strategic Growth)
- **Modular Cloud Migration:** Tách các phân hệ nặng (Submission Engine, Video Streaming) thành **Microservices** chạy Cloud có Auto-scaling.
- **API Standardization:** Chuẩn hóa toàn bộ RESTful APIs và hỗ trợ chuẩn **LTI** để tích hợp mượt mà các công cụ học tập bên ngoài.

---

## 7. Vai Trò Của AI & Đảm Bảo Chất Lượng Bền Vững (Sustainability)

### 🤖 Ứng Dụng Của AI & Vai Trò Phản Biện Của Con Người:
- **AI Hỗ Trợ:** Quét log phát hiện bất thường tự động, dùng NLP tóm tắt hàng ngàn phản hồi khảo sát của sinh viên, quét lỗi WCAG và gợi ý tối ưu code.
- **Con Người Thẩm Định (Human-in-the-loop):** AI thiếu ngữ cảnh kinh doanh, ngân sách và dễ đưa ra giải pháp quá phức tạp (*over-engineering*). Tech Lead và Stakeholders phải là người đánh giá ROI/TCO và ra quyết định cuối cùng.

### 🔄 4 Trụ Cột Duy Trì Chất Lượng Bền Vững:
1. **Continuous Monitoring:** Cài đặt APM (Datadog/Prometheus) với ngưỡng cảnh báo tự động khi Latency > 1s hoặc Error Rate > 1%.
2. **Periodic System Audits:** Kiểm toán định kỳ hàng quý về CSDL, bảo mật, API và chuẩn tiếp cận WCAG trước mỗi kỳ học mới.
3. **Ongoing Feedback Loops:** Nhúng widget lấy phản hồi trực tiếp trong app từ sinh viên và giảng viên.
4. **Iterative Agile & CI/CD:** Áp dụng CI/CD tự động kiểm thử hiệu năng và accessibility trong từng Sprint phát triển.
