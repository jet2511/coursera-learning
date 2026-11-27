# Quality Isn't Magic: It's Process

> **Khóa học**: Introduction to Software Engineering (Course 01 trong chứng chỉ *IBM Java Developer Professional Certificate*)  
> **Phần**: Overview of Software Engineering  
> **Hoạt động**: Dialogue (Coursera AI Coach)  
> **Chủ đề**: 6 trụ cột quy trình chất lượng & Phân tích kịch bản sự cố (Scenario Investigation)  

---

## 1. Sáu trụ cột xây dựng phần mềm chất lượng cao (The Six Pillars)

1. **Requirements Gathering (Thu thập yêu cầu):**
   - Xác định, thu thập và tài liệu hóa chính xác những gì phần mềm cần giải quyết cho bài toán nghiệp vụ của khách hàng.
   - Tạo sự đồng thuận giữa các bên liên quan (stakeholders) và đội ngũ phát triển thông qua tài liệu đặc tả **Software Requirements Specification (SRS)** trước khi bắt đầu thiết kế và lập trình.
2. **Design (Thiết kế kiến trúc & giải pháp):**
   - Cầu nối chuyển đổi yêu cầu từ SRS thành kiến trúc kỹ thuật khả thi (*chuyển dịch từ "làm cái gì" sang "làm như thế nào"*).
   - Định hình ranh giới các thành phần (components), giao diện lập trình ứng dụng (APIs), lược đồ cơ sở dữ liệu (database schemas) và trải nghiệm giao diện người dùng (UI).
3. **Coding for Quality (Lập trình chuẩn chất lượng):**
   - Viết mã nguồn tuân thủ coding standards, conventions, design patterns và sử dụng linters để đảm bảo tính dễ đọc (readability), dễ bảo trì (maintainability), bảo mật và hiệu năng.
4. **Testing (Kiểm thử):**
   - Xác minh phần mềm đáp ứng đúng đặc tả SRS và loại bỏ các lỗi tiềm ẩn.
   - Bắt các lỗi về chức năng (functional), bảo mật (security) và hiệu năng (performance) trước khi phát hành, giảm thiểu chi phí sửa lỗi và bảo vệ uy tín sản phẩm.
5. **Releases (Phát hành theo lộ trình):**
   - Phân phối phần mềm qua các tầng có kiểm soát: **Alpha** (nội bộ/stakeholders) $\rightarrow$ **Beta** (thử nghiệm người dùng thực tế) $\rightarrow$ **GA - General Availability** (phát hành rộng rãi).
6. **Documentation (Tài liệu hóa):**
   - Cung cấp **System Documentation** cho nhóm kỹ thuật (hướng dẫn vận hành, bảo trì, API docs, architecture specs) và **User Documentation** cho người dùng cuối (manuals, hướng dẫn sử dụng).

---

## 2. Phân tích kịch bản sự cố phần mềm (Scenario Investigation)

### Kịch bản 1: App ngân hàng đăng nhập tốt nhưng lỗi chuyển tiền vào ngày ra mắt
- **Vấn đề thực tế:** Ứng dụng cho phép đăng nhập trơn tru nhưng người dùng không thể chuyển tiền giữa các tài khoản khi ra mắt.
- **Quy trình bị rách/bỏ qua:** **Testing** (đặc biệt là *Integration Testing* và *Acceptance/UAT Testing*).
- **Phân tích nguyên nhân:** Đăng nhập chỉ là một module độc lập; chuyển tiền là luồng nghiệp vụ cốt lõi xuyên suốt đầu-cuối (end-to-end critical flow). Việc bỏ qua kiểm thử tích hợp giữa các dịch vụ tài khoản/giao dịch và không qua giai đoạn thử nghiệm Beta ngoài thực tế dẫn tới việc lỗi nghiêm trọng lọt ra môi trường Production.

### Kịch bản 2: Developer có test nhưng hiểu sai logic chuyển tiền giữa các loại tài khoản
- **Vấn đề thực tế:** Test case vẫn pass nhưng hành vi chuyển khoản giữa các loại tài khoản (checking, savings, v.v.) sai lệch so với mong đợi nghiệp vụ.
- **Quy trình bị lỗi:** **Requirements Gathering** và/hoặc **Design**.
- **Phân tích nguyên nhân:** SRS mô tả yêu cầu mơ hồ, thiếu chi tiết về các điều kiện kinh doanh (business rules) giữa các loại tài khoản. Giai đoạn Design không làm rõ use cases và data flow với stakeholders trước khi giao việc cho lập trình viên. Khi "nền móng" yêu cầu bị sai, thì dù kiểm thử kỹ lưỡng vẫn cho ra sản phẩm không đáp ứng đúng bài toán người dùng.

---

## 3. Bản chất: Tại sao chất lượng là quy trình (Quality is a Process)?
- **Chi phí khắc phục lỗi tăng theo cấp số nhân (Exponential Cost):** Phát hiện lỗi càng muộn trong vòng đời SDLC (đặc biệt là sau khi đã release lên Production), chi phí và nỗ lực sửa chữa càng lớn gấp nhiều lần so với việc xử lý ngay từ pha Requirements hay Design.
- **Kiểm thử chỉ kiểm tra cái đã có, không sửa được thiết kế hỏng:** Testing chỉ là chốt chặn thụ động giúp phát hiện lỗi trên mã đã viết, không thể bù đắp cho một kiến trúc sai lầm hay yêu cầu bị định nghĩa lệch.
- **Tiếp cận chủ động (Proactive Quality):** Chất lượng phần mềm không phải là phép thuật xuất hiện ở bước cuối, mà phải được "xây dựng" (built-in) xuyên suốt từng mắt xích: yêu cầu chuẩn $\rightarrow$ kiến trúc vững chắc $\rightarrow$ code sạch $\rightarrow$ kiểm thử đa tầng $\rightarrow$ phát hành có kiểm soát $\rightarrow$ tài liệu rõ ràng.
