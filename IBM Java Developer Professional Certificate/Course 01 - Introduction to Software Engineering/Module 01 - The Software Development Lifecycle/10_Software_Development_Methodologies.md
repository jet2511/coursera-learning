# Software Development Methodologies

> **Khóa học**: Introduction to Software Engineering (Course 01 trong chứng chỉ *IBM Java Developer Professional Certificate*)  
> **Phần**: The Software Building Process and Associated Roles  
> **Video**: Software Development Methodologies (7:13)  

---

## 1. Ba phương pháp phát triển phần mềm phổ biến

### 1.1. Mô hình Thác nước (Waterfall)
- **Bản chất:** Mô hình tuần tự tuyến tính (**sequential**). Giai đoạn sau chỉ bắt đầu khi giai đoạn trước hoàn thành 100%.
- **Đặc điểm:** Toàn bộ việc thu thập yêu cầu, lập kế hoạch và thiết kế kiến trúc đều được thực hiện trả trước (**upfront**). Khách hàng chỉ thấy sản phẩm khi đã vào giai đoạn kiểm thử; chu kỳ phát hành bản lớn thường kéo dài nhiều năm.

### 1.2. Mô hình chữ V (V-Shaped Model)
- **Bản chất:** Biến thể tuần tự của Waterfall, trong đó mỗi pha thiết kế đi xuống đều gắn liền với một pha kiểm thử tương ứng đi lên.
- **Cấu trúc 2 nhánh:**
  - **Nhánh trái (Verification - Thẩm định):** Lập kế hoạch theo từng cấp độ: *Planning* $\rightarrow$ *System Design* $\rightarrow$ *Architecture Design* $\rightarrow$ *Module Design*. Test plans được viết ngay trong các pha này.
  - **Đáy chữ V:** *Coding* (Viết mã nguồn).
  - **Nhánh phải (Validation - Xác nhận):** Thực thi test tương ứng: *Unit Testing* $\rightarrow$ *Integration Testing* $\rightarrow$ *System Testing* $\rightarrow$ *Acceptance Testing (UAT)*.

### 1.3. Mô hình Agile
- **Bản chất:** Phương pháp tiếp cận mang tính lặp và chu kỳ (**iterative & cyclical**), tập trung vào sự cộng tác liên tục.
- **Cơ chế vận hành:**
  - Nhóm làm việc theo các vòng lặp ngắn (**Sprints**, 1–4 tuần). Mỗi sprint đều có testing và kết thúc bằng buổi **Sprint Demo** để khách hàng/stakeholders nghiệm thu phần mềm chạy được (**working software**) và phản hồi.
  - Sau một số sprint, sản phẩm khả thi tối thiểu (**MVP - Minimum Viable Product**) được hình thành để kiểm chứng giả định thị trường.
- **4 giá trị cốt lõi (Agile Manifesto):**
  1. Cá nhân và tương tác hơn quy trình và công cụ.
  2. Phần mềm chạy tốt hơn tài liệu đầy đủ.
  3. Cộng tác với khách hàng hơn đàm phán hợp đồng.
  4. Thích ứng với thay đổi hơn bám sát kế hoạch.

---

## 2. Bảng so sánh Ưu - Nhược điểm (Pros & Cons)

| Mô hình | Ưu điểm (Pros) | Nhược điểm (Cons) | Phù hợp nhất khi |
| :--- | :--- | :--- | :--- |
| **Waterfall** | Đơn giản, vai trò rõ ràng, dễ ước lượng ngân sách và tiến độ cố định từ đầu. | Cực kỳ thiếu linh hoạt; chi phí sửa đổi rất cao nếu yêu cầu thay đổi hoặc bị sót. | Dự án có yêu cầu cố định, phạm vi rõ ràng, công nghệ ổn định. |
| **V-Shape** | Kỷ luật cao; thiết kế test plan từ sớm giúp tiết kiệm thời gian gỡ lỗi về sau. | Rất cứng nhắc; cực khó quay lại sửa chức năng khi đã bước vào pha kiểm thử. | Hệ thống yêu cầu độ tin cậy và an toàn nghiêm ngặt (y tế, hàng không, tài chính). |
| **Agile** | Thích ứng nhanh với thay đổi; phản hồi liên tục trên sản phẩm thực tế; sớm có MVP. | Khó cố định trước ngân sách, tài nguyên và deadline dài hạn do phạm vi liên tục tiến hóa. | Đa số dự án phần mềm hiện đại, sản phẩm số cần ra thị trường nhanh. |
