# Tổng hợp & Điểm nhấn: Mô hình hóa Luồng Dữ liệu và Thực thể Mối quan hệ

Tài liệu này tổng hợp lại các điểm cốt lõi của bài học về hai phương pháp mô hình hóa quan trọng: **Sơ đồ luồng dữ liệu (DFD)** và **Sơ đồ mối quan hệ thực thể (ERD)**.

---

## 1. Điểm nhấn về Sơ đồ Luồng Dữ liệu (DFD)
* **Khái niệm:** DFD là công cụ trực quan hóa cách dữ liệu di chuyển trong hệ thống, tập trung vào chức năng hệ thống và các tương tác dữ liệu.
* **Thành phần:** Biểu diễn các quy trình, kho dữ liệu, đầu vào, đầu ra và thực thể ngoài thông qua các ký hiệu tiêu chuẩn.
* **Cấu trúc phân cấp:**
  * **Sơ đồ ngữ cảnh (Context Diagram / Level 0):** Cung cấp góc nhìn ở cấp độ cao nhất về sự tương tác giữa hệ thống với các thực thể bên ngoài.
  * **Sơ đồ cấp 1 (Level 1 DFD):** Phân rã quy trình chính thành các quy trình con, kho dữ liệu và luồng dữ liệu chi tiết hơn.
* **Quy trình xây dựng:** 
  1. Xác định thực thể ngoài
  2. Xác định các quy trình
  3. Xác định các kho dữ liệu
  4. Xác định các luồng dữ liệu
  5. Xây dựng các cấp độ sơ đồ phân cấp.
* **Công cụ hỗ trợ:** Lucidchart, draw.io, Microsoft Visio.
* **Thực hành tốt nhất (Best Practices):** Sử dụng ký pháp chuẩn hóa, giữ sơ đồ sạch sẽ, kiểm chứng các luồng dữ liệu hợp lệ, liên tục đánh giá và tinh chỉnh.

---

## 2. Điểm nhấn về Sơ đồ Mối quan hệ Thực thể (ERD)
* **Khái niệm:** ERD chuyển dịch các yêu cầu nghiệp vụ thành thiết kế cấu trúc cơ sở dữ liệu quan hệ.
* **Quy trình phát triển:** Ánh xạ các quy tắc nghiệp vụ (Business Rules) vào mối quan hệ cơ sở dữ liệu và áp dụng chuẩn hóa (Normalization).
* **Quy tắc nghiệp vụ:** Là các chính sách, ràng buộc và chỉ dẫn vận hành cách tổ chức quản lý dữ liệu và quy trình.
* **Các thành phần cơ bản:**
  * **Thực thể (Entities):** Đại diện cho các thành phần cốt lõi của hệ thống (Hình chữ nhật).
  * **Thuộc tính (Attributes):** Đại diện cho dữ liệu lưu trữ trong thực thể (Hình oval).
  * **Mối quan hệ (Relationships):** Cách các thực thể tương tác dựa trên quy tắc nghiệp vụ (Hình kim cương).
  * **Bản số (Cardinality):** Phân loại quan hệ thành Một-Một (1:1), Một-Nhiều (1:N), Nhiều-Nhiều (M:N).
* **Chuẩn hóa (Normalization):** Tổ chức dữ liệu nhằm loại bỏ sự trùng lặp (dư thừa) và tránh các lỗi dị thường khi thực hiện Thêm/Sửa/Xóa.
