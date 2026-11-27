# Query and Assembly Programming Languages

- **Khóa học:** IBM Java Developer Professional Certificate / Course 01 - Introduction to Software Engineering
- **Module:** Module 03 - Basics of Programming
- **Chủ đề con:** Programming Languages and Organization
- **Hình thức:** Video (Thời lượng: ~7:25)

---

## 1. Phân loại: Ngôn ngữ bậc cao vs Bậc thấp

| Cấp bậc | Đặc điểm chính | Ví dụ điển hình |
| :--- | :--- | :--- |
| **High-level (Bậc cao)** | Sử dụng từ vựng tiếng Anh tự nhiên; cú pháp trừu tượng, dễ đọc, viết và debug nhanh. Một câu lệnh dịch ra nhiều lệnh mã máy. | SQL (Query), Pascal (Structured), Python (OOP/Multi-paradigm). |
| **Low-level (Bậc thấp)** | Gần sát phần cứng; dùng tập ký hiệu biểu diễn trực tiếp các bit `0` và `1` của mã máy. Ánh xạ 1:1 với lệnh CPU. | Assembly (x86, ARM, MIPS). |

---

## 2. Ngôn ngữ truy vấn (Query Languages)

### Khái niệm & Cơ chế
- **Query (Truy vấn):** Là một yêu cầu trích xuất hoặc thao tác dữ liệu gửi tới hệ quản trị cơ sở dữ liệu (DBMS). Cả ứng dụng và database phải sử dụng chung cú pháp lệnh chuẩn.
- **SQL (Structured Query Language):** Ngôn ngữ phổ biến nhất dùng cho CSDL quan hệ (**Relational Database**), tổ chức dữ liệu theo bảng gồm các hàng và cột với schema định nghĩa trước.
- **NoSQL (Not Only SQL):** CSDL phi quan hệ (**Non-relational**), có schema động phù hợp cho dữ liệu phi cấu trúc.
- Một số ngôn ngữ truy vấn khác: AQL, CQL, Datalog, DMX.

### Phân loại câu lệnh (Statements)
- **Select queries:** Yêu cầu truy xuất và sắp xếp dữ liệu từ các dòng/cột về cho client.
- **Action queries:** Thực hiện các thao tác thay đổi dữ liệu hoặc cấu trúc, gắn liền với các phép **CRUD**:
  - **C**reate: Tạo mới (`CREATE`, `INSERT`).
  - **R**ead: Đọc dữ liệu (`SELECT`).
  - **U**pdate: Cập nhật dữ liệu (`UPDATE`).
  - **D**elete: Xóa dữ liệu (`DELETE`).
- **Administrative queries:** Quản trị hệ thống, cấp quyền và quản lý tài khoản người dùng.

---

## 3. Hợp ngữ (Assembly Languages)

### Đặc điểm & Quan hệ phần cứng
- Thuộc nhóm ngôn ngữ bậc thấp, gắn liền chặt chẽ với kiến trúc vi xử lý của nhà sản xuất phần cứng (**Hardware Architecture**).
- Mỗi kiến trúc CPU có hợp ngữ riêng (ví dụ: Intel/AMD x86, ARM trên thiết bị di động, MIPS).

### Cơ chế dịch & Cú pháp
- **Bộ chuyển đổi:** Sử dụng trình hợp dịch (**Assembler**), không dùng Compiler hay Interpreter.
- **Ánh xạ 1:1 (One-to-One):** 1 dòng lệnh Assembly chuyển đổi thành đúng **1 chỉ dẫn mã máy duy nhất**.
- **Cấu trúc lệnh (1 lệnh/dòng):**
  - **Instruction / Mnemonic (Opcode):** Ký hiệu gợi nhớ cho lệnh CPU cần thực hiện (ví dụ: `LOAD`/`LDA`, `STORE`/`STA`, `ADD`, `INPUT`/`INP`, `OUTPUT`/`OUT`).
  - **Operands / Parameters:** Tham số chỉ định vị trí dữ liệu (thanh ghi, địa chỉ bộ nhớ).
  - Comment/chú thích và nhãn (label) là tùy chọn.

---

## 4. So sánh cốt lõi: Query vs Assembly

| Tiêu chí | Query Languages (SQL) | Assembly Languages (Hợp ngữ) |
| :--- | :--- | :--- |
| **Phân cấp** | High-level (Bậc cao) | Low-level (Bậc thấp) |
| **Mục tiêu chính** | Truy vấn, xử lý và quản trị dữ liệu trong DBMS | Giao tiếp, điều khiển trực tiếp CPU và thanh ghi phần cứng |
| **Độ phụ thuộc phần cứng** | Độc lập phần cứng (Hardware-independent) | Phụ thuộc hoàn toàn vào kiến trúc CPU (x86, ARM, MIPS) |
| **Cơ chế chuyển đổi** | Trình phân tích / xử lý SQL của DBMS | Bộ hợp dịch (**Assembler**) với ánh xạ 1:1 sang Machine Code |
| **Đơn vị thao tác** | Bảng, hàng, cột, tập dữ liệu | Thanh ghi (Registers), ô nhớ (Memory), Opcode |
