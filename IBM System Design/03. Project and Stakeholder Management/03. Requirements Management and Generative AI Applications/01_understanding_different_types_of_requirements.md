# Understanding Different Types of Requirements

## 1. Tầm quan trọng của Quản lý Yêu cầu (Requirements Management)
- **Định hướng rõ ràng:** Xác định mục tiêu dự án, dẫn dắt quá trình phát triển (development).
- **Căn chỉnh mục tiêu:** Đảm bảo sản phẩm đầu ra khớp với kỳ vọng người dùng và mục tiêu kinh doanh.
- **Giảm thiểu rủi ro:** Tạo lộ trình thành công rõ ràng, hạn chế nguy cơ thất bại của dự án.

---

## 2. Các loại Yêu cầu chính trong Dự án

| Loại Yêu cầu | Khái niệm & Mục đích | Ví dụ minh họa | Trách nhiệm của BA |
| :--- | :--- | :--- | :--- |
| **Business Requirements** *(Yêu cầu nghiệp vụ / kinh doanh)* | Mục tiêu và đích đến cấp cao (high-level goals & objectives) mà tổ chức muốn đạt được thông qua dự án. | Tăng 20% doanh số trong vòng 1 năm (thông qua cải thiện CSKH, nâng cấp trải nghiệm mua sắm online, chạy chiến dịch marketing). | Thu thập ngay giai đoạn đầu; phỏng vấn stakeholder, phân tích chiến lược kinh doanh và rà soát mục tiêu tổ chức. |
| **Stakeholder Requirements** *(Yêu cầu bên liên quan)* | Nhu cầu và kỳ vọng cụ thể của từng cá nhân/nhóm tham gia dự án tùy theo vai trò/lợi ích của họ. | - Marketing cần tính năng tạo banner khuyến mãi.<br>- Finance cần công cụ báo cáo theo dõi chi phí. | Thu thập qua workshop, khảo sát (survey), focus group; thúc đẩy cộng tác liên phòng ban. |
| **Functional Requirements** *(Yêu cầu chức năng)* | Định nghĩa **hệ thống/sản phẩm phải làm gì** (what the system should do); chi tiết hóa các tính năng đáp ứng nhu cầu business & stakeholder. | Đăng ký tài khoản, tìm kiếm sản phẩm, giỏ hàng, cổng thanh toán bảo mật trên sàn e-commerce. | Phối hợp với technical team để đánh giá tính khả thi; viết Use Cases / User Stories minh họa tương tác của user. |
| **Non-Functional Requirements (NFRs)** *(Yêu cầu phi chức năng)* | Định nghĩa **thuộc tính chất lượng** của hệ thống (Quality attributes: hiệu năng, bảo mật, khả năng sử dụng, độ tin cậy, v.v.) thay vì hành vi cụ thể. | Hệ thống chịu tải tối thiểu 10.000 user đồng thời không bị lag; response time < 2s; độ sẵn sàng 99.9%. | Ưu tiên định lượng bằng chỉ số/benchmark cụ thể (metrics); phối hợp với đội QA/QC để kiểm thử xác thực. |
| **Transition Requirements** *(Yêu cầu chuyển đổi)* | Các điều kiện tạm thời cần thiết để chuyển từ trạng thái hiện tại (as-is) sang trạng thái mong muốn (to-be). | Kế hoạch đào tạo nhân viên kho trước khi Go-live CRM mới; kế hoạch migration dữ liệu cũ sang hệ thống mới. | Đánh giá mức độ sẵn sàng của người dùng (user readiness); lập kế hoạch đào tạo và chiến lược truyền thông để giảm gián đoạn vận hành. |
| **Regulatory Requirements** *(Yêu cầu pháp lý / tuân thủ)* | Các tiêu chuẩn luật định hoặc chuẩn mực ngành bắt buộc phải tuân thủ (đặc biệt trong y tế, tài chính, viễn thông). | Ứng dụng y tế phải tuân thủ chuẩn HIPAA bảo vệ dữ liệu bệnh nhân; tiêu chuẩn ISO trong quản lý kho. | Phối hợp sớm với phòng pháp chế/compliance; tích hợp các ràng buộc pháp lý vào tài liệu đặc tả chức năng & phi chức năng. |

---

## 3. Case Study: Triển khai Hệ thống Quản lý Kho mới (Manufacturing)
Quy trình thực tế của Business Analyst:
1. **Business Requirements:** Họp stakeholder nắm mục tiêu cấp cao (giảm 15% chi phí lưu kho năm đầu).
2. **Stakeholder Requirements:** Phỏng vấn Giám đốc Vận hành (cần theo dõi tồn kho real-time để ra quyết định).
3. **Functional Requirements:** Làm việc với Tech team xác định tính năng (quét mã vạch tự động cập nhật tồn kho).
4. **Non-Functional Requirements:** Đặt benchmark (xử lý cập nhật trong vòng 2s, uptime 99.9%).
5. **Transition Requirements:** Lên kế hoạch training cho thủ kho & migrate dữ liệu tồn kho hiện tại.
6. **Regulatory Requirements:** Đảm bảo tuân thủ tiêu chuẩn ISO ngành quản trị kho bãi.
7. **Document & Validate:** Lập tài liệu, xác thực lại với stakeholders.
8. **Dev & Test Support:** Hỗ trợ developer và QA trong suốt chu kỳ phát triển/kiểm thử.
9. **Feedback:** Thu thập phản hồi sau Go-live để tiếp tục cải tiến.

---

## 4. Best Practices dành cho Business Analyst
- **Xây dựng quan hệ gắn kết với Stakeholders:** Thu thập yêu cầu toàn diện, chính xác.
- **Tài liệu hóa rõ ràng, cô đọng:** Giúp các bên dễ dàng tra cứu, thống nhất phạm vi.
- **Hợp tác chặt chẽ với Tech & QA:** Đảm bảo yêu cầu khả thi (feasible), kiểm thử được (testable) và đạt được (achievable).
- **Chuẩn bị chuyển đổi kỹ lưỡng:** Kế hoạch đào tạo và truyền thông rõ ràng.
- **Chủ động cập nhật quy định pháp lý:** Đưa vào kế hoạch sớm để tránh rủi ro pháp lý.
