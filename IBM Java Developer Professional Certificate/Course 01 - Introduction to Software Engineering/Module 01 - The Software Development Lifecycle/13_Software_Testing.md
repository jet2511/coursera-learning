# Software Testing

> **Khóa học**: Introduction to Software Engineering (Course 01 trong chứng chỉ *IBM Java Developer Professional Certificate*)  
> **Phần**: The Software Building Process and Associated Roles  
> **Video**: Software Testing (7:30)  

---

## 1. Khái niệm & Cấu trúc Test Case
- **Software Testing:** Là việc tích hợp các bước kiểm định chất lượng xuyên suốt chu trình SDLC nhằm đảm bảo phần mềm khớp với yêu cầu và không có lỗi (bug-free).
- **Test Case:** Được viết sau khi yêu cầu đã được chốt (finalized). Một test case tiêu chuẩn gồm 4 yếu tố:
  1. **Steps:** Các bước thực hiện.
  2. **Inputs:** Dữ liệu đầu vào.
  3. **Data:** Dữ liệu thử nghiệm.
  4. **Expected Outputs:** Kết quả đầu ra kỳ vọng tương ứng.

---

## 2. Ba loại kiểm thử chính (Testing Types)

### 2.1. Functional Testing (Kiểm thử chức năng)
- **Phương pháp:** Chủ yếu là kiểm thử hộp đen (**Black-box testing**) – kiểm tra mà không cần nhìn vào mã nguồn hay cấu trúc bên trong của hệ thống đang kiểm thử (**System Under Test - SUT**).
- **Mục tiêu:** Đảm bảo hệ thống đáp ứng đúng yêu cầu chức năng, tính tiện dụng và khả năng truy cập; kiểm tra phần mềm xử lý ngoại lệ (exceptions) mượt mà và hiển thị thông báo lỗi phù hợp khi người dùng nhập sai hoặc gặp edge cases.

### 2.2. Non-Functional Testing (Kiểm thử phi chức năng)
- **Mục tiêu:** Đo lường các thuộc tính chất lượng của hệ thống vận hành:
  - **Hiệu năng & Khả năng chịu tải:** Ứng dụng phản hồi thế nào khi có lượng lớn người dùng cùng lúc (load/stress test)?
  - **Khả năng tương thích:** Hệ thống hoạt động nhất quán trên các hệ điều hành khác nhau ra sao?
  - **Bảo mật & Phục hồi:** Mức độ an toàn thông tin và phương án phục hồi sau sự cố (disaster recovery).
  - **Tính nhất quán:** Hành vi thực tế có khớp với tài liệu hướng dẫn sử dụng không?

### 2.3. Regression Testing (Kiểm thử hồi quy / Maintenance Testing)
- **Mục tiêu:** Xác nhận các thay đổi gần đây (sửa bug hoặc bổ sung tính năng) không làm ảnh hưởng tiêu cực đến các chức năng hiện có đang hoạt động bình thường.
- **Tiêu chí ưu tiên chọn Test Cases cho hồi quy:**
  - Chức năng thường xuyên phát sinh lỗi trong quá khứ.
  - Các luồng tính năng được sử dụng nhiều nhất (core flows).
  - Các module vừa có sự thay đổi mã nguồn gần nhất.
  - Các ca kiểm thử phức tạp, ca biên (edge cases).

---

## 3. Bốn cấp độ kiểm thử (Testing Levels)

Bốn cấp độ diễn ra tuần tự tại các thời điểm khác nhau trong SDLC nhằm tránh chồng chéo công việc:

| Cấp độ Test | Đối tượng kiểm thử | Người thực hiện | Môi trường / Mục tiêu cốt lõi |
| :--- | :--- | :--- | :--- |
| **1. Unit Testing** | Hàm, phương thức hoặc khối mã độc lập nhỏ nhất. | Developer / Software Engineer | Thực hiện ngay trong pha Development; loại bỏ lỗi xây dựng mã (construction errors) trước khi ghép nối. |
| **2. Integration Testing** | Sự tương tác giữa 2 hoặc nhiều module độc lập khi kết hợp. | Developer / QA | Black-box testing; phát hiện lỗi lệch logic giữa các module, lỗi giao tiếp API, cơ sở dữ liệu hoặc phần cứng bên ngoài. |
| **3. System Testing** | Toàn bộ hệ thống phần mềm hoàn chỉnh đã tích hợp. | QA / Testing Team chuyên trách | Thực hiện trên môi trường **Staging** (mô phỏng sát Production); đánh giá cả Functional lẫn Non-functional. |
| **4. Acceptance Testing (UAT)** | Toàn bộ hệ thống đối chiếu với nhu cầu người dùng. | Khách hàng / Stakeholders / End-users | Thẩm định xem phần mềm có đáp ứng quy trình nghiệp vụ và sẵn sàng đưa vào vận hành chính thức hay không. |
