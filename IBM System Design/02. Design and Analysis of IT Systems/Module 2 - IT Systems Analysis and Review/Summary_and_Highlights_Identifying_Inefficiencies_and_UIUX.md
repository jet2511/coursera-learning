# Summary and Highlights: Identifying Inefficiencies and Reviewing System Architecture, Features, and UI/UX

> **Nguồn:** IBM System Design – Module 2: IT Systems Analysis and Review  
> **Tổng kết bài học:** Nhận diện điểm kém hiệu quả, rà soát kiến trúc, tính năng và đánh giá UI/UX  
> **Ngày lưu:** 2026-08-14

---

## 🎯 Tổng Hợp Các Điểm Nhấn Cốt Lõi (Key Highlights)

### 1. Chiến Lược Nhận Diện Điểm Kém Hiệu Quả & Khoảng Trống (Inefficiencies & Gaps)
- Kết hợp hài hòa giữa **3 trụ cột:** Phân tích kỹ thuật (Technical analysis), Thấu hiểu người dùng (User insights) và Phân tích vận hành (Operational analysis).
- **Lợi ích mang lại:** Cải thiện tốc độ hệ thống, tăng năng suất, nâng cao sự hài lòng của người dùng, tối ưu hóa chi phí và đảm bảo bám sát mục tiêu chiến lược.
- **3 Trọng tâm đánh giá:**
  1. *Kiến trúc hệ thống:* Đảm bảo tính mở rộng (Scalability) và dễ bảo trì (Maintainability).
  2. *Tính năng & Chức năng:* Hỗ trợ toàn diện các nghiệp vụ cốt lõi của doanh nghiệp.
  3. *UI / UX:* Giao diện trực quan, tinh gọn thao tác và nâng cao trải nghiệm người dùng.
- **Phương pháp hiệu quả:** Phỏng vấn người dùng, sơ đồ hóa quy trình qua **BPMN**, giám sát metrics (Latency, Error rates), kiểm thử Usability và Benchmarking đối thủ.
- **Best Practices:** Lôi kéo đa dạng stakeholders, chuẩn hóa công cụ (BPMN, UML), ưu tiên các sự cố có tác động lớn (High-impact) và định kỳ rà soát hệ thống.

---

### 2. Đánh Giá Trải Nghiệm & Giao Diện Người Dùng (UI/UX Evaluation)
- **Mục đích:** Đảm bảo giao diện trực quan, thao tác nhanh chóng và đáp ứng đúng nhu cầu thực tế, thúc đẩy tỷ lệ chấp nhận (Adoption) và hiệu năng vận hành.
- **8 Phương pháp đánh giá phổ biến:**
  - Heuristic Reviews (10 nguyên lý Nielsen)
  - User Testing (Quan sát thao tác thực tế)
  - Surveys & Interviews (Thu thập pain points)
  - A/B Testing
  - Analytics Tracking (Hotjar Heatmaps, Google Analytics)
  - Accessibility Checks (Chuẩn tiếp cận WCAG 2.1)
  - Task Analysis (Đo số bước click & thời gian hoàn thành)
  - Prototype Testing (Thử nghiệm sớm trên Figma / Adobe XD)
- **6 Yếu tố then chốt:** Trực quan (*Intuitiveness*), Hiệu quả (*Efficiency*), Nhất quán (*Consistency*), Tiếp cận (*Accessibility*), Thẩm mỹ (*Aesthetics*), Phản hồi rõ ràng (*Clear Feedback*).
- **Lợi ích kinh doanh:** Tăng tỷ lệ sử dụng, tăng năng suất lao động, giảm thiểu sai sót thao tác, tiết kiệm chi phí sửa lỗi sau triển khai và tạo lợi thế cạnh tranh vượt trội.
- **Best Practices khắc phục thách thức:** Kiểm thử sớm từ bản Prototype, lôi kéo người dùng thật tham gia và chú trọng khả năng tiếp cận (Accessibility-first).

---

## 📝 Bảng Tra Cứu Nhanh

| Khía cạnh | Phương pháp chủ đạo | Tiêu chí đánh giá / Yếu tố cốt lõi | Giá trị kinh doanh |
|---|---|---|---|
| **Architecture & Performance** | Giám sát APM (Datadog), Test tải (JMeter), Component Diagrams | Scalability, Modularity, Maintainability, Uptime | Hệ thống chạy nhanh, không nghẽn giờ cao điểm, dễ scale |
| **Features & Functionality** | Feature Gap Matrix, BPMN, KPI Mapping | Đáp ứng trọn vẹn nghiệp vụ, Tự động hóa, Phân tích dữ liệu | Loại bỏ quy trình thừa, tiết kiệm chi phí vận hành |
| **UI / UX & Accessibility** | Heuristic Nielsen, Task Analysis, WAVE Tool, NVDA | Intuitiveness, Consistency, WCAG 2.1 Compliance | Giảm lỗi người dùng, tăng sự hài lòng và tỷ lệ gắn bó |
