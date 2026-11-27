# Interpreted and Compiled Programming Languages

- **Khóa học:** IBM Java Developer Professional Certificate / Course 01 - Introduction to Software Engineering
- **Module:** Module 03 - Basics of Programming
- **Hình thức:** Video (Thời lượng: ~5:36)

---

## 1. Bản chất của Ngôn ngữ lập trình
- Máy tính chỉ hiểu **mã máy (machine code)** dưới dạng nhị phân (**binary - 0 và 1**).
- Ngôn ngữ lập trình cung cấp cú pháp con người đọc hiểu được (**human-readable code**), làm cầu nối giao tiếp với phần cứng máy tính.
- Hai nhóm chính: **Ngôn ngữ thông dịch (Interpreted)** và **Ngôn ngữ biên dịch (Compiled)**. Lựa chọn loại nào phụ thuộc vào mục tiêu cụ thể của dự án.

---

## 2. Ngôn ngữ thông dịch (Interpreted / Scripting Languages)
- **Cơ chế:** Dùng trình thông dịch (**Interpreter**) dịch trực tiếp mã nguồn sang mã máy ngay trong lúc chạy (**runtime**). Trình thông dịch có sẵn trên trình duyệt web hoặc cài đặt trong hệ điều hành.
- **Đặc điểm:** Linh hoạt, đa nền tảng (chỉ cần có interpreter tương ứng), dễ học, phát triển nhanh; phù hợp cho các tác vụ mang tính kịch bản (script) và lặp đi lặp lại.
- **Ví dụ tiêu biểu:** 
  - **JavaScript:** Chạy qua trình thông dịch trên browser.
  - **Python:** Dễ học, cú pháp trực quan, đa dụng.
  - **Lua:** Nhẹ, phổ biến trong lập trình game.

---

## 3. Ngôn ngữ biên dịch (Compiled Programming Languages)
- **Cơ chế:** Dùng trình biên dịch (**Compiler**) chuyển đổi toàn bộ mã nguồn sang mã máy trước khi chạy, đóng gói thành một tệp thực thi duy nhất (**single executable file**). Ứng dụng chạy trực tiếp khi bấm đúp vào file/icon.
- **Đặc điểm:** Tốc độ thực thi vượt trội và tối ưu tài nguyên; phù hợp xây dựng các hệ thống lớn, phức tạp như hệ điều hành (OS), trình biên dịch, ứng dụng desktop.
- **Ví dụ tiêu biểu:** 
  - **C / C++ / C#:** Dùng trong lõi các hệ điều hành lớn (Windows, macOS, Linux).
  - **Java:** Đa nền tảng, nền tảng của Android OS (không nhầm lẫn với JavaScript).

---

## 4. Bảng so sánh tổng hợp

| Tiêu chí | Ngôn ngữ thông dịch (Interpreted) | Ngôn ngữ biên dịch (Compiled) |
| :--- | :--- | :--- |
| **Thời điểm dịch** | Lúc chạy (Runtime) theo từng dòng | Trước khi chạy (Compile-time) toàn bộ |
| **Công cụ dịch** | Trình thông dịch (**Interpreter**) | Trình biên dịch (**Compiler**) |
| **Đầu ra thực thi** | Chạy trực tiếp từ file script qua Interpreter | Đóng gói thành file thực thi độc lập (Executable / Binary) |
| **Tốc độ thực thi** | Chậm hơn (vừa dịch vừa chạy) | Rất nhanh và tối ưu (đã là mã máy sẵn) |
| **Phạm vi áp dụng** | Scripts, tự động hóa, tác vụ web, game logic | Hệ điều hành, phần mềm lớn, bài toán phức tạp |
| **Ví dụ** | JavaScript, Python, Lua | C, C++, C#, Java |
