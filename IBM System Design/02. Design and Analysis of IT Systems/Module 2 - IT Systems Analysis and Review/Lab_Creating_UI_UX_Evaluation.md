# Lab: Creating a UI/UX Evaluation for User-Friendly Systems (Moodle LMS Case Study)

> **Nguồn:** IBM System Design – Module 2: IT Systems Analysis and Review  
> **Tác giả:** Parikshit Jain  
> **Hệ thống đánh giá:** Moodle LMS (Demo Mount Orange University)  
> **Ngày lưu:** 2026-08-14

---

## 🎯 Mục tiêu bài Lab

1. Áp dụng **10 nguyên lý Usability của Nielsen (Nielsen's 10 Usability Heuristics)** để đánh giá điểm mạnh & điểm yếu của giao diện.
2. Thực hiện **Usability Testing** bằng cách mô phỏng tác vụ thực tế của sinh viên và ghi lại các điểm nghẽn tương tác.
3. Phân tích lỗi tiếp cận (**Accessibility - a11y**) bằng công cụ tự động (**WAVE**) và kiểm thử thủ công (Keyboard Tab & Screen Reader).
4. Xây dựng **Báo cáo đánh giá (UI/UX Evaluation Report)** với các đề xuất cải tiến có gắn mức độ ưu tiên (Priority).

---

## 🛠️ Công Cụ & Môi Trường Kiểm Thử

- **Nền tảng:** Moodle LMS ([moodle.org/demo](https://moodle.org/demo) – Mount Orange Demo, Role: Student).
- **Công cụ:** Google Chrome DevTools, WAVE Accessibility Extension ([wave.webaim.org](https://wave.webaim.org/)), NVDA Screen Reader.

---

## 📋 BƯỚC 1: Xác Định Tác Vụ Người Dùng (Define User Tasks)

Ba tác vụ phổ biến nhất của sinh viên trên hệ thống:
1. **Task 1:** Đăng nhập với vai trò Student và điều hướng tới Dashboard cá nhân.
2. **Task 2:** Định vị khóa học và truy cập vào một bài tập được giao (Assignment).
3. **Task 3:** Nộp bài tập bằng cách tải tệp tin lên (File Upload) và xác nhận nộp.

---

## 🔍 BƯỚC 2: Đánh Giá 10 Nguyên Lý Heuristic (Nielsen’s Usability Heuristics)

| Nguyên lý Heuristic | Đánh giá | Quan sát & Ví dụ thực tế trên Moodle Dashboard |
|---|:---:|---|
| **1. Visibility of system status** | ✅ | Thanh tiến độ hiển thị rõ trạng thái bài tập: *"You have two assignments due"*. |
| **2. Match system & real world** | ❌ | Sử dụng thuật ngữ kỹ thuật khó hiểu như *"courseware"* $\rightarrow$ Nên đổi thành *"Course"*. |
| **3. User control and freedom** | ✅ | Nút Logout và thanh Breadcrumbs điều hướng quay lại rất rõ ràng. |
| **4. Consistency and standards** | ✅ | Icon và nhãn đồng nhất trên toàn bộ các trang (Icon Assignment chuẩn). |
| **5. Error prevention** | ❌ | Không có hộp thoại Pop-up xác nhận cảnh báo trước khi nộp bài tập chính thức. |
| **6. Recognition rather than recall**| ✅ | Menu hiển thị đầy đủ các liên kết điều hướng, dễ dàng tìm thấy mục "Grades". |
| **7. Flexibility and efficiency** | ❌ | Thiếu phím tắt thao tác nhanh (VD: Chưa hỗ trợ phím `Ctrl + S` để lưu nháp bài tập). |
| **8. Aesthetic and minimalist design** | ❌ | Thanh Sidebar bên phải bị nhồi nhét quá nhiều Widget không sử dụng, gây rối mắt. |
| **9. Help recover from errors** | ❌ | Thông báo lỗi upload file không rõ ràng $\rightarrow$ Cần ghi rõ: *"Only .doc/.pdf allowed"*. |
| **10. Help and documentation** | ✅ | Liên kết trợ giúp *"Need help?"* nằm rõ ràng ở Footer dẫn tới trang tài liệu hỗ trợ. |

---

## 🧪 BƯỚC 3: Usability Testing (Mô Phỏng Nộp Bài Tập)

**Kịch bản:** Mở khóa học $\rightarrow$ Mở bài tập $\rightarrow$ Bấm "Add submission" $\rightarrow$ Tải file $\rightarrow$ Bấm "Save changes".

| Giai đoạn tác vụ | Kỳ vọng của người dùng | Thực tế quan sát được | Vấn đề phát hiện (Issue) |
|---|---|---|---|
| **Tìm bài tập** | 1 click trực tiếp từ trang chính | Mất 2 clicks qua nhiều tầng menu | Gây bối rối nhẹ trong luồng điều hướng. |
| **Nộp file bài làm** | Nút bấm có nhãn rõ ràng: *"Submit Assignment"* | Nút bấm ghi: *"Save changes"* | Nhãn không rõ nghĩa, khiến sinh viên tưởng chỉ mới lưu nháp. |
| **Xác nhận nộp** | Nhận thông báo Toast/Pop-up thành công | Không có phản hồi rõ ràng | Thiếu feedback xác nhận trạng thái nộp bài. |

---

## 🗺️ BƯỚC 4: Sơ Đồ Luồng Điều Hướng (Navigation Flow to Grades)

- **Luồng hiện tại:** `Dashboard` $\rightarrow$ `Course Page` $\rightarrow$ `Grades` (Tổng cộng: **3 bước/clicks**).
- **Điểm nghẽn:** Trang Xem Điểm (*Grades*) bị ẩn quá sâu bên trong trang chi tiết môn học.
- **Đề xuất cải tiến:** Thêm trực tiếp nút bấm / shortcut **"Grades"** ngay trên thanh điều hướng chính của Dashboard.

---

## ♿ BƯỚC 5: Đánh Giá Khả Năng Tiếp Cận (Accessibility - a11y)

### 1. Kiểm tra tự động bằng WAVE Tool:
- ❌ **Missing Alt Text:** Các Icon môn học (Course Icon) bị thiếu thuộc tính `alt` mô tả ảnh.
- ❌ **Low Contrast:** Văn bản màu xám trên nền trắng ở các Sidebar widgets vi phạm tỷ lệ tương phản chuẩn WCAG 2.1.

### 2. Kiểm tra thủ công (Keyboard & Screen Reader):
- **Phím Tab điều hướng:**
  - ✅ Nút *"Submit"* có thể focus tới bằng phím Tab.
  - ❌ Một số menu Dropdown bị nhảy cóc (skip tab focus).
  - ✅ Các ô nhập form di chuyển theo thứ tự logic.
- **Screen Reader (NVDA):**
  - ✅ Các thẻ tiêu đề (H1, H2, H3) được đọc chuẩn xác.
  - ❌ Nút bấm *"Submit"* bị thiếu ARIA-label, chỉ đọc là *"button"* không rõ chức năng.
  - ❌ Ảnh thiếu thẻ `alt` bị bỏ qua hoặc đọc tên file rác.

---

## 📊 BƯỚC 6: Báo Cáo Đánh Giá & Đề Xuất Cải Tiến (Evaluation Report)

| Danh mục | Vấn đề phát hiện (Finding) | Đề xuất giải pháp (Recommendation) | Mức độ ưu tiên |
|---|---|---|:---:|
| **Usability** | Nhãn nút bấm *"Save changes"* gây mơ hồ | Đổi nhãn nút thành **"Submit Assignment"** rõ ràng | **High** |
| **Accessibility** | Icon khóa học thiếu thuộc tính mô tả hình ảnh | Bổ sung thuộc tính `alt="Course Icon"` chuẩn SEO & a11y | **High** |
| **Accessibility** | Độ tương phản kém ở thanh Sidebar (Grey on White) | Tăng độ tương phản màu chữ theo chuẩn **WCAG 2.1 AA** | **High** |
| **Navigation** | Mục "Grades" bị ẩn sâu trong trang Course | Thêm Shortcut liên kết trực tiếp tới "Grades" trên Dashboard | **Medium** |
| **Usability** | Thiếu phím tắt lưu bài nhanh | Tích hợp phím tắt `Ctrl + S` để lưu nháp bài làm tức thời | **Low** |

---

## 📝 Tổng Kết Bài Lab

- **UI/UX Evaluation** là sự phối hợp chặt chẽ giữa:
  1. **Heuristic Evaluation** (Nguyên lý kinh điển của Nielsen).
  2. **Usability Workflow Testing** (Kiểm thử hành vi thực tế của người dùng).
  3. **Accessibility Testing** (Tuân thủ tiêu chuẩn toàn cầu WCAG 2.1 qua WAVE & NVDA).
- Báo cáo đánh giá phải đi kèm **mức độ ưu tiên rõ ràng (Priority)** để đội ngũ kỹ thuật và thiết kế tập trung nguồn lực xử lý các vấn đề có tác động lớn nhất.
