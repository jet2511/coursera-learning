# Building Quality Software

> **Khóa học**: Introduction to Software Engineering (Course 01 trong chứng chỉ *IBM Java Developer Professional Certificate*)  
> **Phần**: Overview of Software Engineering  
> **Video**: Building Quality Software  
> **Thời lượng**: 6:58  

---

## 1. Tổng quan về 6 quy trình cốt lõi để xây dựng phần mềm chất lượng cao
Để đảm bảo phần mềm có chất lượng cao, các dự án kỹ thuật phần mềm chuẩn mực đều triển khai 6 quy trình cốt lõi:
1. **Requirements Gathering** (Thu thập yêu cầu)
2. **Software Design** (Thiết kế phần mềm)
3. **Coding for Quality** (Lập trình đảm bảo chất lượng)
4. **Software Testing** (Kiểm thử phần mềm)
5. **Releases** (Phát hành phần mềm)
6. **Documenting** (Tài liệu hóa)

---

## 2. Chi tiết từng quy trình

### 2.1. Requirements Gathering (Thu thập yêu cầu & SRS)
- **Software Requirements Specification (SRS):** Là tài liệu tập hợp, ghi nhận các yêu cầu nghiệp vụ và luồng người dùng (use cases & user flows) mà phần mềm phải đáp ứng.
- **4 phân loại yêu cầu chính:**
  1. *Functional* (Yêu cầu chức năng)
  2. *External & User Interface (UI)* (Giao diện người dùng & kết nối bên ngoài)
  3. *System features* (Tính năng hệ thống)
  4. *Non-functional* (Yêu cầu phi chức năng: hiệu năng, bảo mật, độ tin cậy,...)

---

### 2.2. Software Design (Thiết kế kiến trúc)
- **Mục tiêu:** Chuyển đổi các yêu cầu thành cấu trúc khả thi để lập trình viên có thể viết mã (dịch ngôn ngữ yêu cầu sang ngôn ngữ kỹ thuật).
- **Vai trò Technical Lead/Architect:**
  - Phân rã yêu cầu thành các thành phần (components) có ranh giới (boundaries), hành vi và tương tác xác định $\rightarrow$ Định hình kiến trúc hệ thống (**System Architecture**).
  - Định hướng về hiệu năng, bảo mật và nền tảng (platforms).
  - Thiết kế quy tắc nghiệp vụ (business rules), logic ứng dụng, thiết kế API (giao tiếp giữa các app hoặc app với DB), giao diện người dùng (UI) và thiết kế cơ sở dữ liệu (Database Design).

---

### 2.3. Coding for Quality (Lập trình chuẩn chất lượng)
- **Đặc tính của Quality Code:**
  - **Maintainability** (Dễ bảo trì)
  - **Readability** (Dễ đọc, code sạch, nhất quán)
  - **Testability** (Dễ viết test)
  - **Security** (Bảo mật, không có lỗ hổng)
  - **Efficiency** (Hiệu quả, tối ưu tài nguyên)
  - Thỏa mãn chính xác yêu cầu mà không phát sinh lỗi (defects).
- **Thực hành kỹ thuật (Best Practices):**
  - Tuân thủ coding standards, conventions, design patterns và style guides của dự án.
  - Sử dụng công cụ tự động (**Linters**) để phát hiện sớm các lỗi cú pháp, logic và phong cách code.
  - Viết chú thích code (**inline comments**) hợp lý giúp người khác dễ hiểu và phát triển tiếp.

---

### 2.4. Software Testing (Kiểm thử)
- **Mục tiêu:** Xác minh phần mềm khớp với yêu cầu trong SRS và không có lỗi (bugs). Đảm bảo tính tin cậy (reliability), bảo mật, hiệu năng.
- **Phương thức:** Thủ công (Manual), Tự động (Automated) hoặc Kết hợp (Hybrid).
- **4 cấp độ kiểm thử (Testing Levels):**
  1. **Unit Testing:** Do developer viết, test từng thành phần/hàm cô lập nhỏ nhất.
  2. **Integration Testing:** Kiểm thử khi các thành phần được ghép nối với nhau.
  3. **System Testing:** Kiểm thử toàn bộ hệ thống hoàn chỉnh.
  4. **User Acceptance Testing (UAT / Beta Testing):** Kiểm thử chấp nhận bởi người dùng cuối thực tế.
- **3 nhóm phân loại kiểm thử chính:** Functional, Non-functional, và Regression.

---

### 2.5. Releases (Các giai đoạn phát hành)
Phân phối phiên bản mới tới từng đối tượng mục tiêu:
- **Alpha Release:** Phiên bản hoạt động đầu tiên phát hành nội bộ cho nhóm chọn lọc stakeholders. Vẫn có thể còn lỗi và chưa đủ toàn bộ tính năng, vẫn có thể có thay đổi về thiết kế.
- **Beta Release (Limited Release):** Cung cấp cho người dùng/stakeholders bên ngoài tổ chức để kiểm thử trong điều kiện thực tế (real-world conditions), tìm lỗi phát sinh. Bản Beta phải đáp ứng đầy đủ các yêu cầu chức năng.
- **GA Release (General Availability):** Phiên bản ổn định chính thức, phát hành rộng rãi cho toàn bộ người dùng (Production).

---

### 2.6. Software Documentation (Tài liệu hóa)
Được phân thành 2 nhóm độc lập theo đối tượng thụ hưởng:
1. **System Documentation (Dành cho Technical Users - Engineers, Developers, Architects):**
   - Giải thích cách hệ thống hoạt động, kiến trúc và cách sử dụng dưới góc độ kỹ thuật.
   - Bao gồm: File `README`, inline comments, tài liệu kiến trúc & thiết kế, thông tin xác minh (verification), tài liệu hướng dẫn bảo trì (maintenance guides).
2. **User Documentation (Dành cho Non-technical End-users):**
   - Hướng dẫn người dùng thao tác và sử dụng tính năng sản phẩm.
   - Bao gồm: Sách hướng dẫn (user guides/manuals), video hướng dẫn, trung tâm trợ giúp trực tuyến (online help) và trợ giúp tương tác trực tiếp (inline help/tooltips).
