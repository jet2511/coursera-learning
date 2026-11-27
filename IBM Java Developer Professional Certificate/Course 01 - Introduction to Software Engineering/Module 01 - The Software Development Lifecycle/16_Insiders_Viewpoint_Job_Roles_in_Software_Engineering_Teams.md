# Insiders' Viewpoint: Job Roles in Software Engineering Teams

> **Khóa học**: Introduction to Software Engineering (Course 01 trong chứng chỉ *IBM Java Developer Professional Certificate*)  
> **Phần**: The Software Building Process and Associated Roles  
> **Video**: Insiders' Viewpoint: Job Roles in Software Engineering Teams (7:17)  

---

## 1. Góc nhìn thực tế: Bản chất cộng tác của Kỹ sư phần mềm
- **Kỹ sư không bao giờ làm việc đơn độc:** Trong môi trường hiện đại, dự án ngày càng phức tạp và quy mô lớn. Kỹ năng quan trọng nhất của một kỹ sư là biết cách giao tiếp và cộng tác trực tiếp với các vai trò liên chức năng trong nhóm.
- **Văn hóa nhúng (Embedded Collaboration):** Thay vì bàn giao thụ động kiểu thác nước (waterfall hand-offs), mô hình hiệu quả nhất hiện nay là mọi vai trò cùng làm việc chặt chẽ trong một nhóm thông qua các buổi standup hàng ngày, thảo luận ticket Jira, brainstorm chung và kênh chat thời gian thực.

---

## 2. Các tương tác thường ngày giữa Kỹ sư phần mềm và các vai trò

### 2.1. Product Manager (PM) / Product Owner (PO)
- **Tần suất tương tác:** Nhiều nhất trong công việc hàng ngày.
- **Bản chất công việc:**
  - PM làm việc với sales, marketing, khách hàng để quyết định **cái gì cần xây dựng (what to build)**, nắm bắt nhu cầu và định hướng tính năng đổi mới.
  - Phối hợp cùng kỹ sư để bàn luận về phương án triển khai (**how to build**), đánh đổi kỹ thuật (**trade-offs**), thời hạn (**timelines**) và kỳ vọng kết quả.
  - Thường kiêm nhiệm vai trò điều phối như Scrum Master: chủ trì Daily Standup, theo dõi Jira tickets, giải quyết vướng mắc (**unblock**) để đảm bảo dự án đúng tiến độ.

### 2.2. Tech Lead / Senior Engineer
- Định hướng kiến trúc kỹ thuật vĩ mô (**big-picture architecture**).
- Chịu trách nhiệm trực tiếp trong khâu **Code Review** đối với code của các kỹ sư khác trước khi chuyển sang các bước kiểm thử tiếp theo.

### 2.3. UX Designer & UX Researcher
- **UX Designer:** Chuyển đổi ý tưởng từ phác thảo nháp/whiteboard thành bản vẽ chi tiết (**mockups/specs**) trên công cụ thiết kế (như **Figma**). Kỹ sư nhận specs (ví dụ: giao diện checkout page) và chuyển hóa trực quan thành mã nguồn.
- **UX Researcher:** Đi thực tế khảo sát thị trường, phỏng vấn đối tác và khách hàng để mang phản hồi thực tế về cho đội ngũ.

### 2.4. QA / Test Engineers
- **Quy trình phối hợp:** Sau khi code được Tech Lead phê duyệt, QA sẽ tiến hành test để đảm bảo tính năng mới không phá vỡ các chức năng cũ.
- **Tương tác khi có bug:** QA lập kế hoạch kiểm thử (**test plan**) hoặc tài liệu mô tả lỗi chi tiết $\rightarrow$ Kỹ sư fix lỗi và báo lại $\rightarrow$ QA kiểm thử lại (re-test) và kiểm tra lỗi hồi quy.
- Đội ngũ QA chuyên trách còn xây dựng pipeline tự động hóa kiểm thử (**automation test suites**), CI/CD pipelines cho kiểm thử E2E và Integration.

### 2.5. Site Reliability Engineers (SRE) / Sysadmins / DevOps
- Kết hợp quản trị hạ tầng IT với kỹ thuật phần mềm.
- Hỗ trợ triển khai phần mềm lên môi trường máy chủ/cloud (không chỉ chạy trên localhost), duy trì hệ thống giám sát cảnh báo (**monitoring & alerting**) và vận hành hạ tầng liên tục.

---

## 3. Điểm đúc kết (Key Takeaway)
Trong các tổ chức công nghệ, các danh xưng và vai trò có thể được phân tách rạch ròi hoặc một kỹ sư có thể mang nhiều "chiếc mũ" (DevOps, QA, kiến trúc, coding chi tiết). Thành công của dự án phụ thuộc hoàn toàn vào việc gắn kết các mảnh ghép này lại với nhau thành một thể thống nhất.
