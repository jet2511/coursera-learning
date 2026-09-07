# Module 5: AWS Lake Formation additional configurations and capabilities

## Bài học: Visualizing Data with QuickSight - Demo

### 1. Tổng quan về Amazon QuickSight
- **Định nghĩa**: Dịch vụ Business Intelligence (BI) trên nền tảng đám mây được quản lý hoàn toàn (fully managed), **serverless**, có khả năng mở rộng quy mô tự động.
- **Vai trò trong Data Lake**: Là tầng hiển thị và trực quan hóa dữ liệu (Presentation / Visualization Layer) ở chặng cuối của Data Lake, biến các tệp dữ liệu thô/đã làm sạch thành biểu đồ (charts), đồ thị (graphs) và bảng điều khiển (dashboards) phục vụ ra quyết định kinh doanh.

---

### 2. Quản lý nguồn dữ liệu (Datasets)
- QuickSight hỗ trợ linh hoạt nhiều nguồn dữ liệu:
  - **Nhập thủ công (Direct upload)**: Hỗ trợ các file dạng CSV, JSON, Excel trực tiếp từ máy tính.
  - **Kết nối Data Lake**: Kết nối trực tiếp với các tập dữ liệu lưu trữ trên **Amazon S3** hoặc thông qua bảng catalog trong **AWS Glue Data Catalog / Athena**.

---

### 3. Quy trình tạo và xuất bản Dashboard (Workflow)
1. **Chọn hoặc kết nối Dataset**: Vào mục `Datasets` -> Chọn tập dữ liệu mong muốn (ví dụ: `people overview` từ phòng HR).
2. **Xây dựng Visualizations (Visuals)**:
   - QuickSight cung cấp phong phú các loại biểu đồ: Bar chart, Line chart, Pie chart, Funnel chart...
   - Kéo thả các trường dữ liệu (fields/dimensions) vào biểu đồ (ví dụ: sắp xếp thâm niên làm việc `tenure` theo tên nhân viên `name` bằng Funnel chart).
   - Tùy chỉnh, chỉnh sửa các visual có sẵn hoặc bấm `Add Visual` để tạo thêm các góc nhìn phân tích mới.
3. **Publish & Share Dashboard**:
   - Nhấp `Publish dashboard` và đặt tên cho dashboard.
   - Chia sẻ an toàn tới các bên liên quan (stakeholders) trong tổ chức thay vì gửi các file dữ liệu thô (CSV/JSON). Người dùng không chuyên về kỹ thuật có thể dễ dàng tương tác và đọc hiểu dữ liệu trực quan.
