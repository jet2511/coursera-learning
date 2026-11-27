# Roles in Software Engineering Projects

> **Khóa học**: Introduction to Software Engineering (Course 01 trong chứng chỉ *IBM Java Developer Professional Certificate*)  
> **Phần**: The Software Building Process and Associated Roles  
> **Video**: Roles in Software Engineering Projects (5:39)  

---

## 1. Tổng quan về các vai trò trong dự án phần mềm
Tùy thuộc vào phương pháp phát triển (Agile hay Waterfall) và quy mô từng công ty, tên gọi và cơ cấu vai trò có thể linh hoạt thay đổi. Một dự án phần mềm tiêu chuẩn thường bao gồm 9 vai trò chủ chốt.

---

## 2. Chi tiết 9 vai trò và trách nhiệm cốt lõi

### 2.1. Project Manager (PM) / Scrum Master
- **Project Manager (Mô hình truyền thống / Waterfall):**
  - Đảm bảo dự án vận hành trơn tru và điều phối luồng thông tin.
  - Quản lý các bài toán vĩ mô: Lập kế hoạch, tiến độ (scheduling), ngân sách (budgeting); phân bổ nhân sự và tài nguyên; thực thi kế hoạch phần mềm.
- **Scrum Master (Mô hình linh hoạt / Agile):**
  - Không tập trung vào kiểm soát kế hoạch cứng nhắc, mà tập trung thúc đẩy sự thành công của nhóm và từng cá nhân.
  - Tạo điều kiện thuận lợi và thúc đẩy giao tiếp nội bộ theo giá trị Agile (*con người và tương tác hơn quy trình*).

### 2.2. Stakeholders (Các bên liên quan)
- Là những người mà sản phẩm hướng tới phục vụ (khách hàng, người dùng cuối, người ra quyết định, quản trị viên hệ thống,...).
- **Trách nhiệm:** Định nghĩa yêu cầu dự án; làm rõ thắc mắc khi dev team cần phản hồi; tham gia thử nghiệm bản Beta và kiểm thử chấp nhận (Acceptance Testing/UAT) trước khi release.

### 2.3. System Architect / Software Architect / Solution Architect
- Thiết kế, mô tả cấu trúc kiến trúc của hệ thống và truyền đạt tới các thành viên trong nhóm.
- Chịu trách nhiệm về cấu trúc nội tại thiết yếu và các khía cạnh kỹ thuật nền tảng; hỗ trợ kỹ thuật xuyên suốt các giai đoạn của SDLC.

### 2.4. UX Designer (Nhà thiết kế trải nghiệm người dùng)
- Định nghĩa cách phần mềm phản hồi dưới góc nhìn của người dùng cuối.
- Cân bằng giữa việc tạo ra giao diện trực quan, dễ thao tác (intuitive) và độ vững chắc (robust) đáp ứng yêu cầu kỹ thuật.
- Xác định cách hệ thống truyền đạt chức năng và cách người dùng tương tác với sản phẩm.

### 2.5. Software Developer (Lập trình viên phát triển phần mềm)
- Trực tiếp viết mã nguồn vận hành ứng dụng.
- **Trách nhiệm:** Triển khai kiến trúc từ Design Document, hiện thực hóa các yêu cầu trong SRS và áp dụng đúng thiết kế giao diện từ UX Designer.

### 2.6. Tester / QA Engineer (Kỹ sư kiểm thử & Đảm bảo chất lượng)
- Đảm bảo chất lượng sản phẩm và xác minh giải pháp đáp ứng đúng yêu cầu khách hàng.
- Thiết kế, viết và thực thi các ca kiểm thử (**test cases**) để phát hiện bug hoặc các điểm thiếu sót, sau đó phản hồi lại cho dev team xử lý.

### 2.7. Site Reliability Engineer (SRE) / Ops Engineer (Kỹ sư vận hành hệ thống)
- Cầu nối giữa Development và Operations (DevOps), kết hợp chuyên môn công nghệ phần mềm với quản trị hệ thống IT.
- Theo dõi sự cố (incidents) và chủ trì họp phân tích nguyên nhân; tự động hóa hệ thống, quy trình; hỗ trợ khắc phục sự cố và bảo đảm tính sẵn sàng, ổn định (reliability) cho khách hàng.

### 2.8. Product Manager (PM) / Product Owner (PO)
- Nắm giữ tầm nhìn tổng thể (vision) của sản phẩm.
- Thấu hiểu sâu sắc yêu cầu của khách hàng và nhu cầu thực tế của người dùng cuối.
- Dẫn dắt nỗ lực phát triển và đảm bảo sản phẩm mang lại giá trị thực tế cao nhất cho các bên liên quan.

### 2.9. Technical Writer / Information Developer (Chuyên viên viết tài liệu kỹ thuật)
- Chuyển hóa các tài liệu/khái niệm kỹ thuật phức tạp thành văn bản dễ hiểu cho người dùng phổ thông (non-technical audience).
- Soạn thảo sách hướng dẫn sử dụng (user manuals), báo cáo kỹ thuật, white papers, và tài liệu hướng dẫn giúp khách hàng dễ tiếp cận và phản hồi kịp thời cho đội ngũ phát triển.

---

## 3. Bảng tóm tắt nhanh trách nhiệm các vai trò

| Vai trò | Trọng tâm chính |
| :--- | :--- |
| **PM / Scrum Master** | Quản lý tiến độ/ngân sách (PM) hoặc hỗ trợ nhóm tự chủ & giao tiếp (Scrum Master). |
| **Stakeholder** | Đưa ra yêu cầu, giải đáp thắc mắc và nghiệm thu UAT. |
| **Software Architect** | Thiết kế kiến trúc tổng thể, hạ tầng và quy chuẩn kỹ thuật. |
| **UX Designer** | Thiết kế luồng tương tác và trải nghiệm người dùng trực quan. |
| **Software Developer** | Viết code triển khai tính năng theo Design Document và SRS. |
| **QA / Tester** | Viết test case, tìm bug, kiểm soát chất lượng phần mềm. |
| **SRE / Ops Engineer** | Đảm bảo hạ tầng, tự động hóa quy trình, độ tin cậy và xử lý sự cố vận hành. |
| **Product Manager / PO** | Định hình tầm nhìn sản phẩm, quản lý backlog và tối ưu giá trị nghiệp vụ. |
| **Technical Writer** | Soạn thảo tài liệu hướng dẫn dễ hiểu cho người dùng cuối và khách hàng. |
