# Key Takeaways: Application Security

> **Khóa học**: Cybersecurity Architecture (IBM)  
> **Module 3**: Network, Application, and Data Security  
> **Tài liệu**: Reading: Key Takeaways: Application Security (Thời lượng: ~5 phút)  
> **Tác giả**: Dee Dee Collette (IBM)

---

## 📌 Các Điểm Trọng Tâm Cần Ghi Nhớ (Core Highlights)

- **Mọi phần mềm đều có nguy cơ chứa lỗ hổng (Vulnerabilities)**:
  - Đa số các lỗ hổng an ninh được hình thành ngay trong giai đoạn **Coding (Lập trình)**.
  - Nguyên nhân chính xuất phát từ việc quy trình phát triển phần mềm truyền thống mang tính tuyến tính (Linear) và thiếu sự trao đổi/phối hợp giữa các bộ phận.
  - **DevOps** ra đời nhằm phá bỏ các rào cản ngăn cách này.

- **DevSecOps (Development + Security + Operations)**:
  - Tích hợp và tự động hóa an ninh mạng xuyên suốt mọi giai đoạn của vòng đời phát triển phần mềm (SDLC).
  - Là một quy trình tích hợp khép kín, được thiết kế chuyên biệt cho tính linh hoạt và tốc độ phản ứng nhanh (**Agility**).

- **Quy trình Viết mã An toàn (Secured Coding Processes)** bao gồm:
  1. **Danh mục kiểm tra thực hành lập trình (Coding Practices Checklist)**:
     - Định hướng và chuẩn hóa cách viết mã an toàn.
     - Xử lý triệt để lỗi tràn bộ đệm (**Buffer Overflow**).
     - Thiết lập các cơ chế xác thực (**Authentication**) chuẩn mực.
     - *Tài nguyên tham khảo*: Truy cập [OWASP.org](https://owasp.org) để xem danh mục checklist mẫu chuẩn công nghiệp.
  2. **Thư viện tin cậy (Trusted Libraries)**:
     - Giúp tái sử dụng mã nguồn an toàn mà không cần phải viết lại code từ đầu.
  3. **Kiến trúc tiêu chuẩn (Standard Architectures)**:
     - Tham chiếu các kiến trúc chuẩn để tránh lặp lại các sai lầm cũ và học hỏi từ các bài học thực tiễn.
  4. **Tránh các lỗ hổng phổ biến (Avoiding Vulnerabilities)**:
     - Tham khảo danh sách **OWASP Top 10** các lỗ hổng bảo mật ứng dụng web nguy hiểm nhất trên thế giới.
  5. **Bản kê khai nguyên vật liệu phần mềm (Software Bill of Materials - SBOM)**:
     - Quản lý chi tiết:
       - Các thành phần cấu thành (Components).
       - Các thư viện và nguồn gốc xuất xứ của chúng (Libraries & Sources).
       - Mối quan hệ phụ thuộc lẫn nhau giữa các thành phần (Dependencies).
       - Phiên bản cụ thể của từng gói thư viện (Versions).
       - Các lỗ hổng đã biết trong chuỗi cung ứng (ví dụ điển hình: sự cố **Log4j**).

- **Kiểm thử Lỗ hổng Bảo mật (Vulnerability Testing)**:
  - **SAST (Static Application Security Testing)**: Còn gọi là **White Box Testing (Kiểm thử hộp trắng)**, soi chiếu và phân tích trực tiếp mã nguồn.
  - **DAST (Dynamic Application Security Testing)**: Còn gọi là **Black Box Testing (Kiểm thử hộp đen)**, kiểm thử ứng dụng khi đang chạy ở dạng thực thi từ góc nhìn của kẻ tấn công bên ngoài.
