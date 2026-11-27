# Module 1 Summary & Highlights: The Software Development Lifecycle

> **Khóa học**: Introduction to Software Engineering (Course 01 trong chứng chỉ *IBM Java Developer Professional Certificate*)  
> **Phần**: Module Summary and Graded Quiz  
> **Bài đọc**: Summary & Highlights (2:16)  

---

## 1. Nền tảng Kỹ nghệ Phần mềm (Software Engineering Fundamentals)
- **Định nghĩa:** Áp dụng các nguyên lý khoa học và kỹ thuật vào quá trình thiết kế và tạo ra phần mềm.
- **Trách nhiệm của Kỹ sư phần mềm:** Chịu trách nhiệm thiết kế, xây dựng và bảo trì các hệ thống phần mềm xuyên suốt toàn bộ vòng đời (full lifecycle).

---

## 2. Tầm quan trọng của SDLC (Why the SDLC Matters)
Việc tuân thủ vòng đời phát triển phần mềm (**SDLC**) giúp nâng cao hiệu suất làm việc và giảm thiểu rủi ro thông qua 4 cơ chế:
1. **Minh bạch hóa nhiệm vụ:** Xác định rõ ai làm cái gì và vào thời điểm nào (*who works on what, and when*).
2. **Cải thiện giao tiếp:** Tăng cường tương tác giữa khách hàng, stakeholders và đội ngũ kỹ thuật.
3. **Định vị vai trò:** Giúp các bên liên quan hiểu rõ vị trí của mình trong từng giai đoạn của quy trình.
4. **Hỗ trợ bàn giao (Handoffs):** Giúp các nhóm liên chức năng (cross-domain teams) chuyển giao đầu việc sang giai đoạn kế tiếp nhịp nhàng, đúng chuẩn.

---

## 3. Sáu quy trình cốt lõi xây dựng phần mềm chất lượng cao
1. **Requirements gathering** (Thu thập yêu cầu)
2. **Design** (Thiết kế kiến trúc)
3. **Coding** (Lập trình chuẩn chất lượng)
4. **Testing** (Kiểm thử đa tầng)
5. **Releasing** (Phát hành: Alpha $\rightarrow$ Beta $\rightarrow$ GA)
6. **Documenting** (Tài liệu hóa kỹ thuật & người dùng)

---

## 4. Quản lý yêu cầu & Bộ 3 tài liệu đặc tả (Requirements & Documents)
- **Quy trình thu thập yêu cầu:**
  1. Xác định các bên liên quan (Identifying stakeholders).
  2. Thiết lập mục tiêu tổng thể và chỉ số đo lường (Goals & Objectives).
  3. Khơi gợi yêu cầu (Eliciting requirements qua khảo sát, phỏng vấn).
  4. Tài liệu hóa, phân tích, xác nhận và ưu tiên hóa yêu cầu (Documenting, Analyzing, Confirming, Prioritizing).
- **Bộ 3 tài liệu đặc tả chuẩn:**
  - **SRS (Software Requirements Specification):** Ghi nhận chi tiết các chức năng phần mềm và thiết lập chuẩn mực (benchmarks) / cấp độ dịch vụ (service levels) cho hiệu năng.
  - **URS (User Requirements Specification):** Tập con của SRS mô tả chi tiết kỳ vọng của người dùng dưới dạng User Stories / Use Cases.
  - **SysRS (System Requirements Specification):** Rộng hơn SRS; ngoài thông tin phần mềm còn chứa năng lực hệ thống, giao tiếp phần cứng, đặc điểm người dùng, quy định chính sách/pháp lý/nhân sự, yêu cầu an ninh/hiệu năng và tiêu chí nghiệm thu toàn hệ thống.

---

## 5. Các phương pháp luận SDLC phổ biến (Methodologies)
- **Waterfall:** Mô hình tuần tự tuyến tính (Sequential); yêu cầu và thiết kế chốt từ đầu (upfront); chặt chẽ nhưng thiếu linh hoạt.
- **V-Shaped Model:** Mô hình tuần tự đối xứng; nhánh Verification (thiết kế & lập test plan từ sớm) gắn liền với nhánh Validation (thực thi kiểm thử); kỷ luật cao nhưng cứng nhắc.
- **Agile:** Mô hình lặp và chu kỳ (Iterative & Cyclical); làm việc theo Sprint (1–4 tuần); liên tục bàn giao working software tại Sprint Demo để lấy phản hồi; nhanh ra MVP; linh hoạt thích ứng với thay đổi.

---

## 6. Tổng quan về Kiểm thử phần mềm (Testing Overview)
- **Phân loại kiểm thử (Testing Types):**
  - **Functional testing:** Kiểm thử hộp đen kiểm tra tính tương ứng giữa inputs và expected outputs của SUT.
  - **Non-functional testing:** Kiểm tra các thuộc tính vận hành như hiệu năng (performance), bảo mật (security), khả năng mở rộng (scalability), tính sẵn sàng (availability).
  - **Regression testing:** Xác nhận việc sửa lỗi hoặc cập nhật mới không làm hỏng các tính năng cũ đang chạy ổn định.
- **Bốn cấp độ kiểm thử (Testing Levels):**
  - **Unit Testing:** Do Dev viết, test các hàm/khối mã độc lập nhỏ nhất.
  - **Integration Testing:** Kiểm tra tương tác giữa các module độc lập khi kết hợp.
  - **System Testing:** Đánh giá toàn bộ hệ thống hoàn chỉnh trên môi trường Staging.
  - **Acceptance Testing (UAT):** Do khách hàng/người dùng cuối nghiệm thu theo nhu cầu thực tế.

---

## 7. Năm loại tài liệu phần mềm (Documentation Types)
1. **Requirements documentation:** SRS, SysRS, URS.
2. **Design documentation:** Thiết kế khái niệm (conceptual) và kỹ thuật (technical design).
3. **Technical documentation:** Comments trong mã nguồn, working papers.
4. **Quality assurance documentation:** Test plans, test cases, test data, traceability matrices.
5. **User documentation:** User manuals, FAQs, tutorials, installation guides.

---

## 8. Chín vai trò chủ chốt trong dự án phần mềm (Key Job Roles)
1. **Project Manager / Scrum Master:** Quản lý kế hoạch/ngân sách (PM) hoặc hỗ trợ tương tác và loại bỏ rào cản (Scrum Master).
2. **Stakeholder:** Đưa ra yêu cầu nghiệp vụ và nghiệm thu UAT.
3. **System / Software Architect:** Thiết kế kiến trúc kỹ thuật nền tảng.
4. **UX Designer:** Thiết kế luồng trải nghiệm trực quan và hành vi giao diện người dùng.
5. **Software Developer:** Viết mã nguồn hiện thực hóa thiết kế và yêu cầu.
6. **Tester / QA Engineer:** Viết và chạy test case, phát hiện bug, đảm bảo chất lượng.
7. **Site Reliability / Ops Engineer (SRE):** Đảm bảo tính ổn định, độ tin cậy, tự động hóa và hạ tầng cloud/production.
8. **Product Manager / Product Owner:** Định hình tầm nhìn sản phẩm, quản lý backlog và tối ưu giá trị cho khách hàng.
9. **Technical Writer / Information Developer:** Soạn thảo tài liệu kỹ thuật dễ hiểu cho người dùng cuối.
