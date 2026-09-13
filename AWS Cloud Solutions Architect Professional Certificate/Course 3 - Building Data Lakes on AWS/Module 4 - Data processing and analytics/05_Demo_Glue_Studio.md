# Module 4: Data processing and analytics

## Bài học: Demo - AWS Glue Studio

### 1. Giới thiệu AWS Glue Studio
- Giao diện trực quan (Visual ETL) giúp xây dựng, chạy và giám sát các pipeline ETL hoàn chỉnh mà **không cần viết code thủ công**.
- Hỗ trợ xem trước mã nguồn tự động sinh ra (**Script tab**), cho phép chuyển đổi mượt mà từ visual kéo-thả sang tùy biến code chuyên sâu khi cần.

---

### 2. Các bước xây dựng Visual ETL Job bảo vệ PII (Sensitive Data)
Trong bài demo thực hành xử lý tập dữ liệu chứa thông tin nhạy cảm:

1. **Cấu hình chung (Job Details)**:
   - Gán IAM Role có đủ quyền hạn truy cập S3 và Glue.
   - Thiết lập số lượng worker phù hợp với khối lượng tải.

2. **Node 1: Source (Nguồn dữ liệu)**:
   - Chọn nguồn `S3` (định dạng CSV).
   - Data Preview cho phép xem nhanh các trường dữ liệu thô (tên, số định danh, ngày sinh,...).

3. **Node 2: Transform - Detect Sensitive Data (Phát hiện dữ liệu nhạy cảm)**:
   - Thêm node biến đổi chuyên biệt: **Detect sensitive data**.
   - Cấu hình các mẫu nhạy cảm cần tìm kiếm: Credit cards, Social Security Numbers (SSN), Email addresses.
   - Hành động xử lý: Chọn **Redact** (che giấu/thay thế giá trị nhạy cảm bằng chuỗi định sẵn, ví dụ: `"super duper secret"`).

4. **Node 3: Transform - Change Schema (Điều chỉnh lược đồ)**:
   - Nối tiếp sau bước detect để loại bỏ (drop) các cột hoặc trường phát hiện không cần thiết trong tập dữ liệu đích.

5. **Node 4: Target (Đích lưu trữ & Catalog)**:
   - Chọn target `S3` và định dạng lưu trữ (ví dụ: JSON, không nén).
   - Bật tùy chọn **Update AWS Glue Data Catalog**: Tự động tạo hoặc cập nhật bảng metadata trong Data Catalog ngay sau khi job hoàn thành.

---

### 3. Kết quả & Lợi ích
- **Tự động sinh mã nguồn (Auto-generated code)**: Toàn bộ cấu hình visual được dịch thành script hoàn chỉnh (Python/PySpark).
- **Masking PII thành công**: File kết quả trên S3 đã được che giấu dữ liệu nhạy cảm theo đúng quy chuẩn.
- **Tích hợp sẵn sàng phân tích**: Data Catalog được cập nhật metadata tức thì, cho phép các công cụ phân tích (như Athena, Redshift Spectrum) truy vấn bảng dữ liệu sạch ngay lập tức.
