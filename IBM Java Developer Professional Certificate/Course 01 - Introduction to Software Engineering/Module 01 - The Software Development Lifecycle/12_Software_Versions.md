# Software Versions

> **Khóa học**: Introduction to Software Engineering (Course 01 trong chứng chỉ *IBM Java Developer Professional Certificate*)  
> **Phần**: The Software Building Process and Associated Roles  
> **Video**: Software Versions (4:00)  

---

## 1. Bản chất & Vai trò của Đánh số phiên bản (Software Versioning)
- **Định nghĩa:** Là phương pháp các nhà phát triển theo dõi lịch sử phát hành, cập nhật tính năng mới và các bản vá lỗi (patches) cho phần mềm.
- **Vai trò:**
  - Giúp người dùng biết chính xác phiên bản phần mềm đang sử dụng.
  - Cung cấp thông tin kỹ thuật rõ ràng cho lập trình viên để xác định thời điểm phát hành, các thay đổi lớn/nhỏ hoặc bản vá.

---

## 2. Các quy ước đặt số phiên bản phổ biến

### 2.1. Định dạng số cơ bản
- Thường gồm 2, 3 hoặc 4 nhóm số phân tách nhau bằng dấu chấm (`.`):
  - `0.x` (ví dụ: `0.9`): Phiên bản đang trong giai đoạn thử nghiệm (Beta hoặc Testing).
  - `1.0`: Bản phát hành chính thức đầu tiên (First release).
  - Nhiều bản vá và cải tiến sẽ làm chuỗi số dài hơn (ví dụ: 4 nhóm số).

### 2.2. Đặt phiên bản theo thời gian (Date-based Versioning)
- Sử dụng năm và tháng phát hành.
- **Ví dụ điển hình:** Ubuntu Linux `18.04.2` $\rightarrow$ Phát hành vào tháng 04 năm 2018; cụm `.2` biểu thị bản cập nhật/thay đổi phụ thứ hai.

### 2.3. Hệ thống đánh số ngữ nghĩa (Semantic Versioning)
Quy chuẩn thường thấy với 4 thành phần (`MAJOR.MINOR.PATCH.BUILD`):

| Thành phần | Tên gọi | Ý nghĩa kỹ thuật |
| :--- | :--- | :--- |
| **1st** | **Major** | Thay đổi lớn, phá vỡ tính tương thích cũ (Breaking changes/New major release). |
| **2nd** | **Minor** | Bổ sung tính năng mới nhưng vẫn tương thích ngược (New features/Backwards-compatible). |
| **3rd** | **Patch** | Vá các lỗi nhỏ (Bug fixes/patches). |
| **4th** | **Build** | Mã số bản build hoặc ngày build (Build number/Build date) với những thay đổi rất nhỏ. |

---

## 3. Khả năng tương thích ngược (Backwards Compatibility)
- **Vấn đề thường gặp:** Không tương thích giữa các phiên bản cũ và mới (compatibility issues) là bài toán phổ biến trong kỹ thuật phần mềm.
- **Troubleshooting:** Kiểm tra số phiên bản hiện hành (trong mục *About* hoặc *Help* của ứng dụng/trình duyệt) để xác định xem phiên bản đang dùng có bị lỗi thời (outdated) hay không. Cập nhật lên bản mới thường giúp khắc phục xung đột.
- **Tương thích ngược (Backwards Compatible):** Phần mềm phiên bản mới có khả năng đọc, xử lý và làm việc bình thường với các tệp tin, chương trình hoặc hệ thống được tạo ra từ các phiên bản cũ hơn.
