# Software Documentation

> **Khóa học**: Introduction to Software Engineering (Course 01 trong chứng chỉ *IBM Java Developer Professional Certificate*)  
> **Phần**: The Software Building Process and Associated Roles  
> **Video**: Software Documentation (5:31)  

---

## 1. Bản chất & Định dạng Tài liệu Phần mềm
- **Khái niệm:** Tài liệu phần mềm là toàn bộ thông tin mô tả sản phẩm là gì và cách sử dụng nó. Áp dụng xuyên suốt tất cả các giai đoạn của SDLC.
- **3 định dạng chính:** Văn bản (Written), Video, hoặc Đồ họa/Hình ảnh (Graphical).
- **Đối tượng độc giả:** Người dùng cuối (end-users), lập trình viên (developers), kỹ sư QA, quản trị viên hệ thống (sysadmins) và các bên liên quan (stakeholders).

---

## 2. Phân loại cốt lõi: Product Documentation vs. Process Documentation

| Phân loại | Định nghĩa | Nội dung & Mục đích |
| :--- | :--- | :--- |
| **Product Documentation** | Mô tả **chức năng của sản phẩm** (*Product's functionality*). | Giải thích phần mềm làm được gì, cấu trúc ra sao và cách vận hành/sử dụng. |
| **Process Documentation** | Mô tả **cách thức hoàn thành một công việc** (*How to complete a task*). | Cung cấp các tiêu chuẩn và yêu cầu để thực thi một quy trình nghiệp vụ đạt chuẩn chất lượng. |

---

## 3. Năm nhóm tài liệu sản phẩm (Product Documentation Types)

1. **Requirements Documentation (Tài liệu yêu cầu):**
   - Soạn thảo trong pha *Planning* dành cho dev, architect, QA.
   - Bao gồm: Software Requirements Specification (SRS), System Requirements Specification (SysRS), User Acceptance Specification.
2. **Design Documentation (Tài liệu thiết kế):**
   - Do architects và dev team viết; giải thích cách xây dựng phần mềm để đáp ứng yêu cầu.
   - Bao gồm: Tài liệu thiết kế khái niệm (conceptual design) và thiết kế kỹ thuật chi tiết (technical design).
3. **Technical Documentation (Tài liệu kỹ thuật):**
   - Phục vụ trực tiếp cho developer.
   - Gồm inline comments trong code, working papers giải thích cơ chế hoạt động của thuật toán/code, và ghi chú thiết kế của kỹ sư trong quá trình triển khai.
4. **Quality Assurance Documentation (Tài liệu đảm bảo chất lượng/QA):**
   - Toàn bộ tài liệu liên quan đến chiến lược, tiến độ và số liệu kiểm thử: Test plans, test data, test scenarios, test cases, test strategies.
   - **Traceability Matrices (Ma trận truy vết):** Ánh xạ trực tiếp từng test case với yêu cầu tương ứng trong SRS để đảm bảo không bỏ sót tính năng.
5. **User Documentation (Tài liệu người dùng):**
   - Hướng dẫn người dùng cuối cài đặt, vận hành và xử lý sự cố.
   - Gồm FAQs, sách hướng dẫn sử dụng (user manuals), hướng dẫn cài đặt (installation guides), tài liệu hướng dẫn tương tác (tutorials).

---

## 4. Quy trình vận hành chuẩn (Standard Operating Procedures - SOPs)
- **Bản chất:** Là một nhánh chi tiết chuyên sâu của *Process Documentation*, giải thích từng bước (step-by-step) cách hoàn thành một tác vụ phức tạp mang tính đặc thù riêng của tổ chức.
- **Ví dụ thực tế:** Thao tác commit/push code lên repo là kiến thức chung của kỹ sư; nhưng quy trình phê duyệt, review, chạy CI kiểm tra để **merge code vào nhánh chính (main branch)** của một công ty cụ thể sẽ được quy định chi tiết trong SOP.
- **Hình thức biểu diễn:** Lưu đồ (flowchart), dàn ý phân cấp (hierarchical outline), hoặc danh sách chỉ dẫn từng bước.

---

## 5. Cập nhật và Bảo trì tài liệu (Documentation Maintenance)
- Mọi tài liệu phải được cập nhật đồng bộ khi phần mềm thay đổi (ví dụ: thay đổi giao diện web thì tài liệu online help phải sửa theo).
- Trong chu trình SDLC, việc cập nhật tài liệu chính thức diễn ra trong giai đoạn **Maintenance**. Cần được review định kỳ để đảm bảo tính chính xác tuyệt đối.
