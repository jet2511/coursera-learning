# Expert Viewpoints: Getting Started with Prototyping an Application Idea (Góc nhìn chuyên gia: Tạo bản mẫu ý tưởng ứng dụng)

Bản tóm tắt những chia sẻ thực tế từ chuyên gia về triết lý, phương pháp triển khai và những thành phần cốt lõi cần có trong một bản mẫu ứng dụng ban đầu (early prototype).

---

### 1. Triết lý tạo bản mẫu cốt lõi
> [!IMPORTANT]
> **"Build to learn, not to last" (Xây dựng để học hỏi, không phải để tồn tại lâu dài)**
> Bản mẫu chỉ là phương tiện để xác thực giả định và học hỏi, không phải mã nguồn sản xuất (production code). Việc cố gắng tái sử dụng hoặc refactor trực tiếp từ mã nguồn bản mẫu lên hệ thống thật sẽ tích tụ nợ kỹ thuật (technical debt) lớn. Hãy sẵn sàng vứt bỏ bản mẫu sau khi đạt được mục tiêu học tập.

---

### 2. Phương pháp tiếp cận quy trình tạo bản mẫu

*   **Xác định mục tiêu học tập trước tiên:** Làm rõ thứ cần kiểm chứng qua bản mẫu (tính khả thi kỹ thuật, trải nghiệm người dùng UX, đặc tính hiệu năng hay rào cản tích hợp hệ thống).
*   **Tập trung vào phần rủi ro và ẩn số (Spike the risky parts):** Chỉ tạo bản mẫu cho các phần chưa rõ ràng hoặc chứa nhiều rủi ro kỹ thuật. Tránh mất thời gian làm bản mẫu cho các tính năng đã biết chắc chắn là hoạt động tốt.
*   **Sử dụng công cụ và framework quen thuộc:** Quá trình tạo bản mẫu yêu cầu tốc độ. Đây không phải lúc để thử nghiệm và học các công nghệ mới; hãy dùng các công cụ đã thành thạo nhất.
*   **Giới hạn thời gian nghiêm ngặt (Time-box ruthlessly):** Giới hạn từ **1 đến 3 ngày** cho một bản mẫu. Nếu không thể chứng minh giả thuyết trong thời gian này, cần thu hẹp phạm vi hoặc thay đổi hướng tiếp cận.
*   **Tài liệu hóa các phát hiện (Document findings):** Ghi chép lại những gì chạy tốt, những gì thất bại, các quan sát về hiệu năng và tích hợp để làm cơ sở thiết kế kiến trúc thực tế sau này.

---

### 3. Những yếu tố cần có trong bản mẫu ban đầu (Early Prototype)
Quá trình chọn lọc tính năng đưa vào bản mẫu ban đầu cần tuân thủ 3 tiêu chí: **Sự rõ ràng (Clarity), Tác động (Impact), và Tính khả thi (Feasibility)**.

*   **Tập trung vào bài toán kinh doanh cốt lõi:** Chỉ kiểm chứng và xây dựng các chức năng mang lại giá trị lớn nhất thay vì cố gắng hoàn thiện toàn bộ giải pháp.
*   **Ưu tiên các tính năng định hình trải nghiệm người dùng:** Tập trung vào các tác vụ cốt lõi tạo nên sự khác biệt của sản phẩm (ví dụ: đối với ứng dụng tài chính, cần tập trung vào quy trình onboarding bảo mật, luồng giao dịch cơ bản và cập nhật tài khoản thời gian thực để tạo lòng tin với stakeholders).
*   **Nhận phản hồi sớm từ người dùng:** Tích hợp phản hồi từ khảo sát, phỏng vấn thực tế ngay từ đầu để xây dựng cái người dùng thực sự cần thay vì cái đội ngũ phát triển nghĩ là họ cần.
*   **Giữ thiết kế đơn giản:** Tránh nhồi nhét quá nhiều tính năng phụ. Tập trung vào cấu trúc điều hướng sạch, giao diện trực quan và thu thập các chỉ số hiệu năng cơ bản.
*   **Áp dụng nguyên lý mô-đun (Modular Design):** Dù bản mẫu có dung lượng nhẹ, vẫn nên thiết kế theo dạng mô-đun để các thành phần cấu trúc có thể phát triển độc lập khi giải pháp chín muồi.
