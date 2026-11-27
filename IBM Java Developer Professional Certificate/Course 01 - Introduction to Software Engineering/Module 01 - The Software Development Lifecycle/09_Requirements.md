# Requirements in Software Engineering

> **Khóa học**: Introduction to Software Engineering (Course 01 trong chứng chỉ *IBM Java Developer Professional Certificate*)  
> **Phần**: Overview of Software Engineering  
> **Video**: Requirements  
> **Thời lượng**: 6:00  

---

## 1. Quy trình 6 bước thu thập yêu cầu (Requirement Gathering Process)
Thu thập yêu cầu là quá trình xác định bài toán cần giải quyết và tài liệu hóa phương pháp giải quyết bài toán đó qua 6 bước:

```
1. Identify Stakeholders
       ↓
2. Establish Goals & Objectives
       ↓
3. Elicit Requirements  ←───┐
       ↓                    │ (Lặp - Iterative)
4. Document Requirements    │
       ↓                    │
5. Confirm Requirements ────┘
       ↓
6. Prioritize Requirements
```

1. **Identifying Stakeholders (Xác định các bên liên quan):**
   - Đảm bảo có đại diện từ mọi nhóm bị sản phẩm tác động: Người ra quyết định (decision-makers), người dùng cuối (end-users), quản trị hệ thống (sysadmins), kỹ thuật (engineering), marketing, sales, customer support.
2. **Establishing Goals and Objectives (Thiết lập mục tiêu):**
   - **Goals:** Kết quả kỳ vọng dài hạn, mang tính bao quát (gồm kết quả cho khách hàng và mục tiêu kinh doanh).
   - **Objectives:** Hành động cụ thể, khả thi và có thể đo lường được (**actionable & measurable**) để đạt được Goals.
3. **Eliciting Requirements (Khơi gợi / Thu thập yêu cầu):**
   - Thực hiện qua khảo sát (surveys), bảng câu hỏi (questionnaires), phỏng vấn trực tiếp (interviews).
4. **Documenting the Requirements (Tài liệu hóa):**
   - Diễn đạt yêu cầu rõ ràng, dễ hiểu cho cả stakeholders lẫn technical team; đảm bảo bám sát Goals & Objectives.
5. **Analyzing and Confirming Requirements (Phân tích và xác nhận):**
   - Kiểm tra tính nhất quán (consistency), rõ ràng (clarity) và đầy đủ (completeness).
   - Trình bày và được phê duyệt chính thức (approved) bởi stakeholders.
   *(Lưu ý: 3 bước Thu thập – Tài liệu hóa – Xác nhận thường diễn ra theo chu trình lặp).*
6. **Prioritizing Requirements (Ưu tiên hóa yêu cầu):**
   - Phân loại theo mức độ: **Must-have** (bắt buộc phải có), **Highly desired** (rất mong muốn), **Nice to have** (có thì tốt). Sắp xếp thứ tự ưu tiên bên trong từng nhóm.

---

## 2. Ba bộ tài liệu đặc tả yêu cầu (SRS vs. URS vs. SysRS)

| Đặc tả | Viết tắt | Mục đích chính | Phạm vi & Nội dung |
| :--- | :--- | :--- | :--- |
| **Software Requirements Specification** | **SRS** | Đặc tả chức năng và tiêu chuẩn hiệu năng cho **phần mềm**. | Phổ biến nhất trong các dự án phần mềm. Bao gồm mục đích, phạm vi, ràng buộc, giả định, phụ thuộc và 4 nhóm yêu cầu kỹ thuật. |
| **User Requirements Specification** | **URS** | Đặc tả nhu cầu và kỳ vọng của **người dùng cuối**. | Viết dưới dạng **User Stories** hoặc **Use Cases** trả lời 3 câu hỏi: *Ai là người dùng? Họ muốn thực hiện chức năng gì? Tại sao họ cần chức năng đó?* Là căn cứ cho kiểm thử chấp nhận (UAT). Thường được tích hợp thẳng vào SRS. |
| **System Requirements Specification** | **SysRS** | Đặc tả toàn diện cho **toàn bộ hệ thống** (bao gồm cả phần cứng và phần mềm). | Rộng hơn SRS. Bao gồm năng lực hệ thống, giao diện phần cứng/phần mềm, tiêu chuẩn pháp lý/chính sách, yêu cầu nhân sự, an ninh, tiêu chí nghiệm thu toàn hệ thống. |

---

## 3. Cấu trúc chi tiết của một tài liệu SRS

Một tài liệu SRS tiêu chuẩn bao gồm các thành phần chính:

1. **Purpose Statement (Tuyên bố mục đích & Phạm vi):**
   - Đối tượng độc giả, quyền truy cập và cách thức sử dụng SRS.
   - Phạm vi sản phẩm (Scope): Lợi ích, Goals và Objectives mang lại.
2. **Constraints, Assumptions & Dependencies (Ràng buộc, Giả định & Phụ thuộc):**
   - **Constraints (Ràng buộc):** Điều kiện vận hành bắt buộc giới hạn phương án thiết kế (tuân thủ tiêu chuẩn kỹ thuật, hạn chế phần cứng).
   - **Assumptions (Giả định):** Hệ điều hành yêu cầu, thiết bị phần cứng mặc định cần để phần mềm chạy.
   - **Dependencies (Phụ thuộc):** Các sản phẩm phần mềm bên thứ ba hoặc dịch vụ phụ thuộc.
3. **Bốn nhóm phân loại yêu cầu phần mềm:**
   - **Functional Requirements:** Các chức năng cụ thể phần mềm phải thực hiện.
   - **System Features:** Tập con của Functional Requirements, là các tính năng thiết yếu bắt buộc để hệ thống vận hành.
   - **External Interface Requirements:** Hành vi tương tác của phần mềm với thực thể bên ngoài (người dùng, giao tiếp phần cứng, phần mềm/dịch vụ khác).
   - **Non-functional Requirements:** Tiêu chuẩn chất lượng phi chức năng như hiệu năng (performance), an toàn (safety), bảo mật (security), tiêu chuẩn chất lượng (quality standards).
