# 05 - Assignment Overview: Proof of Concept (PoC) Reports

- **Thời lượng ước tính:** 2 phút
- **Tác giả:** Parikshit Jain
- **Mục tiêu:** Hướng dẫn phương pháp lập kế hoạch, triển khai thử nghiệm thực tế (prototype quy mô nhỏ) và soạn thảo **Báo cáo Proof of Concept (PoC Report)** để kiểm chứng quyết định kiến trúc then chốt trước khi đầu tư triển khai diện rộng cho dự án chuyển đổi số **ABC Bank Digital Core Transformation**.

---

## 1. Bối cảnh & Mục đích (Context & Purpose)

### Bối cảnh dự án ABC Bank
- Ngân hàng ABC đang chuyển đổi từ hệ thống Core cũ (Legacy) sang nền tảng Core số thế hệ mới.
- Các công nghệ & giải pháp mới (Microservices container hóa, Event Streaming với Kafka, Phát hiện gian lận thời gian thực, Tích hợp API đối tác) cần phải được chứng minh tính khả thi kỹ thuật bằng dữ liệu và bằng chứng thực nghiệm (không dựa trên giả định).

### Một số câu hỏi kiến trúc cần PoC kiểm chứng:
1. *Cụm Kafka có chịu tải được lưu lượng giao dịch hàng nghìn msg/giây của ngân hàng mà không bị trễ hay mất gói tin?*
2. *Framework microservice được chọn có khả năng auto-scale khi tải tăng vọt?*
3. *API cổng chấm điểm tín dụng bên ngoài (Credit Bureau) có phản hồi trong ngưỡng thời gian quy định (< 2 giây)?*
4. *Cơ chế đồng bộ dữ liệu có đáp ứng độ trễ (latency) và yêu cầu lưu vết kiểm toán của ngân hàng nhà nước?*
5. *Mô hình bảo mật đám mây có thỏa mãn các chuẩn khắt khe PCI-DSS và mã hóa FIPS?*

---

## 2. Các bước thực hiện PoC (6 Steps Workflow)

1. **Step 1: Define PoC Scope & Objective (Xác định phạm vi & Mục tiêu)**
   - Nêu rõ công nghệ/thành phần kiến trúc cần kiểm thử và lý do.
   - Phân định rõ những gì nằm trong phạm vi (In-scope) và ngoài phạm vi (Out-of-scope).
   - Thiết lập các tiêu chí thành công đo lường được (Measurable Success Criteria: TPS, latency p99 < 500ms, tỷ lệ lỗi 0%).

2. **Step 2: Build a Small-Scale Prototype (Xây dựng Prototype thu nhỏ)**
   - Chọn 1 use case thực tế: Phát hiện gian lận real-time / Tích hợp REST API bên thứ 3 / Triển khai Microservice trên Docker-K8s / Đồng bộ dữ liệu.
   - Triển khai các thành phần tối thiểu bằng Docker, Kafka, Database, hoặc Cloud services.

3. **Step 3: Test Core Functionality (Thực thi kiểm thử chức năng & hiệu năng)**
   - Chạy từ 3 đến 5 kịch bản kiểm thử trọng tâm (Test Scenarios).
   - Ghi lại kết quả mong đợi (Expected) vs kết quả thực tế (Actual).
   - Thu thập log hệ thống, ảnh chụp màn hình, hoặc kết quả lệnh benchmark.

4. **Step 4: Analyze Findings & Limitations (Phân tích kết quả & Giới hạn)**
   - Đánh giá hiệu năng, độ phức tạp tích hợp, độ ổn định, tuân thủ an toàn thông tin và tính khả chuyển.
   - Chỉ ra các lỗ hổng, rủi ro kỹ thuật hoặc điểm nghẽn phát hiện được.

5. **Step 5: Evaluate Against Success Criteria (Đối chiếu tiêu chí thành công)**
   - Xác định mức độ hoàn thành mục tiêu.
   - Đưa ra quyết định khuyến nghị rõ ràng: **Go**, **No-Go**, hoặc **Conditional Go** (đi kèm điều kiện bổ sung).

6. **Step 6: Compile the PoC Report (Biên soạn báo cáo PoC hoàn chỉnh)**
   - Định dạng tài liệu chuyên nghiệp, chuẩn mực phục vụ Hội đồng Kiến trúc Doanh nghiệp (Architecture Review Board).

---

## 3. Tiêu chí đánh giá bài làm (Evaluation Criteria)

| Tiêu chí | Mô tả yêu cầu |
| :--- | :--- |
| **Clarity & Completeness** | Mục tiêu PoC, phạm vi và use case được định nghĩa rõ ràng, mạch lạc |
| **Technical Accuracy** | Cấu hình, thiết lập môi trường và quy trình test chính xác về mặt kỹ thuật |
| **Depth of Testing** | Các kịch bản kiểm thử sát thực tế, đo lường được và bám sát mục tiêu PoC |
| **Analytical Quality** | Phân tích sâu sắc nguyên nhân/kết quả, không dừng lại ở mức liệt kê quan sát |
| **Actionable Recommendations**| Khuyến nghị Go / No-Go / Conditional Go dứt khoát, có phương án kế tiếp |
| **Professional Documentation**| Bố cục văn bản chuẩn mực, súc tích, phù hợp trình bày trước hội đồng kiến trúc |

---

## 4. Sản phẩm bàn giao (Deliverables)
1. **Báo cáo PoC hoàn chỉnh (Complete PoC Report):**
   - Mục tiêu & Phạm vi (Objective & Scope)
   - Cấu hình Prototype (Prototype Setup & Architecture)
   - Các kịch bản kiểm thử & Dữ liệu kết quả (Test Scenarios & Results)
   - Phân tích phát hiện, giới hạn và bài học rút ra (Findings, Limitations, Lessons Learned)
   - Khuyến nghị quyết định (Final Go / No-Go Recommendation)
2. **Completed Validation Checklist:** Bảng kiểm tra nghiệm thu chất lượng báo cáo PoC.
