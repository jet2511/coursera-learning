# The Process Mapping Process (6-Step Framework)

## 1. Khái niệm & Thuật ngữ quan trọng
- **QA (Quality Assurance - Đảm bảo chất lượng):** Quy trình kiểm thử nhằm phát hiện lỗi và đảm bảo phần mềm đạt chuẩn trước khi release.
- **Defect / Bug (Lỗi):** Sai lệch giữa kết quả thực tế và yêu cầu mong muốn.
- **Defect Lifecycle (Vòng đời lỗi):** Chuỗi trạng thái từ khi phát hiện (`Identify`) $\rightarrow$ ghi nhận (`Log`) $\rightarrow$ sửa (`Fix`) $\rightarrow$ kiểm thử lại (`Retest/Verify`) $\rightarrow$ đóng (`Close`).
- **Swimlanes (Làn bơi):** Các dải phân cách theo chiều dọc/ngang trên sơ đồ thể hiện ranh giới trách nhiệm của từng vai trò/bộ phận (QA, Developer, Release Team).
- **In-scope vs. Out-of-scope:** 
  - *In-scope:* Những phần/tác vụ nằm trong phạm vi cần vẽ bản đồ.
  - *Out-of-scope:* Những phần ngoài phạm vi, tạm thời bỏ qua để tránh loãng mục tiêu.

---

## 2. Quy trình 6 bước xây dựng Process Map (6 Steps)

| Bước | Mục tiêu | Do (Nên làm) | Don't (Không nên làm) |
| :--- | :--- | :--- | :--- |
| **1. Define Objective** | Xác định mục tiêu sơ đồ giải quyết bài toán gì | Cụ thể, đo lường được, gắn với kết quả cải tiến rõ ràng | Bắt đầu vẽ mà không có mục tiêu rõ ràng |
| **2. Define Scope** | Giới hạn ranh giới quy trình (In vs. Out) | Thiết lập ranh giới chặt chẽ (vd: chỉ làm Defect Management, bỏ qua Test Planning) | Cố vẽ toàn bộ hệ thống cùng lúc gây quá tải và mất trọng tâm |
| **3. Brainstorm Activities** | Liệt kê mọi hành động (chưa cần thứ tự) | Thu hút đúng người trực tiếp thực thi tham gia | Tự suy diễn quy trình trên bàn giấy, dễ sót bước/ngoại lệ |
| **4. Sequence Steps** | Sắp xếp thứ tự logic & các điểm quyết định | Xác định các nhánh rẽ điều kiện (If/Then), vòng lặp (loop), nhánh song song | Ép quy trình thành đường thẳng tuyến tính trong khi thực tế có lặp lại |
| **5. Create Visual** | Vẽ sơ đồ bằng ký hiệu chuẩn hóa | Dùng ký hiệu chuẩn (`Rectangle`, `Diamond`), phân làn (`Swimlanes`), tên bước ngắn gọn | Nhồi nhét quá nhiều chi tiết vụn vặt gây rối mắt |
| **6. Validate Map** | Xác thực sơ đồ với các bên liên quan | Mở phiên review ngắn cùng Tester, Dev, Release Manager để đối chiếu thực tế | Bỏ qua bước kiểm chứng, biến giả định sai thành quy chuẩn chính thức |

---

## 3. Case Study: Defect Management Workflow
- **Roles:** QA / Tester $\leftrightarrow$ Developer $\leftrightarrow$ Release Manager (dùng *Swimlanes*).
- **Luồng xử lý:** 
  1. QA chạy test case $\rightarrow$ phát hiện lỗi $\rightarrow$ log defect & gán mức độ nghiêm trọng (severity).
  2. QA thông báo cho Developer.
  3. Developer sửa lỗi (Fix) $\rightarrow$ chuyển lại QA.
  4. QA kiểm thử lại (Retest / Verify):
     - *Lỗi chưa hết:* Loop ngược lại Developer để sửa tiếp.
     - *Lỗi đã khắc phục:* Cập nhật trạng thái `Closed`.

---

## 4. Bài học cốt lõi
> *"Process mapping isn’t just documentation; it’s a conversation."*  
> Vẽ sơ đồ quy trình không đơn thuần là viết tài liệu, mà là công cụ giao tiếp liên chức năng nhằm xóa bỏ hiểu lầm và thúc đẩy cải tiến thực tế.
