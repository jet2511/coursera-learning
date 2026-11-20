# Đánh Giá Kết Quả Thực Hiện Lab (Quiz / Review Answers - Developing PoC Reports)

Dưới đây là đáp án và giải trình đối chiếu cho 7 câu hỏi tự đánh giá (Self-Assessment) của bài Lab Developing Proof of Concept (PoC) Reports:

---

### Câu 1 (Question 1)
> **Have you clearly defined the PoC scope and objectives, including in-scope and out-of-scope elements in the provided template?**

- **Đáp án:** **Yes**
- **Giải trình:** Trong `Task1_PoC_Scope_and_Objective.md`, mục tiêu kiểm chứng kiến trúc Event-Driven Microservices với Kafka, Spring Boot và PostgreSQL đã được định nghĩa rõ ràng, phân định minh bạch 5 điểm trong phạm vi (In-Scope) và 4 điểm ngoài phạm vi (Out-of-Scope).

---

### Câu 2 (Question 2)
> **Did you build a small-scale prototype based on a selected PoC use case, such as microservice deployment or event processing?**

- **Đáp án:** **Yes**
- **Giải trình:** Trong `Task2_Prototype_Setup_Configuration.md`, giải pháp đã xây dựng hoàn chỉnh mô hình prototype thu nhỏ cho use case **Real-time Fraud Detection Event Flow** với cụm container gồm Spring Boot Service, Kafka Broker (topic `fraud-events`) và cơ sở dữ liệu PostgreSQL.

---

### Câu 3 (Question 3)
> **Have you documented all relevant tools, environment, configuration, and connections used for the prototype?**

- **Đáp án:** **Yes**
- **Giải trình:** Tài liệu Task 2 đã lập bảng chi tiết các công cụ (Docker Compose, Java 17, Spring Boot 3.2, Kafka 3.6, PostgreSQL 15), môi trường, số hiệu cổng (ports 8080, 9092, 5432) và cấu hình kết nối.

---

### Câu 4 (Question 4)
> **Does your PoC report include defined test scenarios with outcomes, limitations, and improvement points?**

- **Đáp án:** **Yes**
- **Giải trình:** Trong `Task3_Test_Scenarios_and_Outcomes.md` và `Task4_Findings_Limitations_Recommendations.md`, đã thiết lập 4 kịch bản kiểm thử đo lường (TC01 đến TC04) với bảng kết quả mong đợi vs thực tế, log thực thi, đồng thời liệt kê đầy đủ các giới hạn kỹ thuật và 3 điểm cải tiến trọng tâm.

---

### Câu 5 (Question 5)
> **Have you evaluated the PoC results against success criteria, such as latency, message delivery, API response time, and security?**

- **Đáp án:** **Yes**
- **Giải trình:** Trong `Task5_Success_Criteria_Evaluation.md`, toàn bộ kết quả thực tế đã được ánh xạ với các tiêu chí thành công định lượng: độ trễ xử lý (p99 = 118 ms < 150 ms), tỷ lệ mất tin nhắn (0%), độ tin cậy API (100% status 200) và điều kiện an ninh để ra quyết định **Conditional-Go**.

---

### Câu 6 (Question 6)
> **Is your PoC report structured according to the checklist, with sections for scope, prototype steps, test results, findings, and recommendations?**

- **Đáp án:** **Yes**
- **Giải trình:** Báo cáo tuân thủ tuyệt đối cấu trúc chuẩn mực của biểu mẫu: Scope & Objectives -> Prototype Setup -> Test Results & Logs -> Findings & Limitations -> Success Criteria Evaluation & Decision (Conditional-Go) -> Validation Checklist.

---

### Câu 7 (Question 7)
> **Have you prepared and submitted the completed Proof of Concept report as required for this lab?**

- **Đáp án:** **Yes**
- **Giải trình:** Bộ hồ sơ tài liệu PoC Report gồm 6 tài liệu hoàn chỉnh đã được chuẩn bị đầy đủ trong thư mục `06_Lab_Solutions` và sẵn sàng nộp theo quy chuẩn danh dự (Coursera Honor Code).

---

## Tổng kết đánh giá: **7/7 (100% Đạt - 7 points)**
