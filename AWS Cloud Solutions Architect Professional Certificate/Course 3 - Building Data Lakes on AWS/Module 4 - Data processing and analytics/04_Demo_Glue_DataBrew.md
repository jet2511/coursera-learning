# Module 4: Data processing and analytics

## Bài học: Demo - AWS Glue DataBrew

### 1. Mục tiêu Demo
Minh họa cách sử dụng **AWS Glue DataBrew** để khám phá, đánh giá chất lượng và cấu hình quy tắc dữ liệu mà không cần viết code:
- Sử dụng **Data Profiler** để phân tích tổng quan cấu trúc, tỷ lệ thiếu dữ liệu và quét PII.
- Định nghĩa các bộ quy tắc chất lượng dữ liệu (**Data Quality Rules - DQ Rules**) để tự động kiểm tra tính hợp lệ của tập dữ liệu.

---

### 2. Data Profiler & Quét thông tin nhạy cảm (PII)
- **Data Profiler**:
  - Chạy trên toàn bộ dataset và lưu kết quả profile vào một S3 Bucket chỉ định.
  - Cung cấp cái nhìn trực quan: tỷ lệ ô trống/null (ví dụ: 22% missing values do trường tùy chọn hoặc lỗi ingest), kiểm tra dòng trùng lặp (duplicate rows).
- **PII Detection (Personally Identifiable Information)**:
  - Cho phép kích hoạt thống kê PII trên nhiều danh mục: Thẻ tín dụng, tài khoản ngân hàng, bằng lái xe, tên, địa chỉ, ngày sinh, giới tính,...
  - Giúp phát hiện kịp thời dữ liệu nhạy cảm để áp dụng các biện pháp bảo mật và masking thích hợp.

---

### 3. Data Quality Rules (DQ Rulesets)
- **Mục đích**: Thiết lập bộ tiêu chuẩn để kiểm soát chất lượng dữ liệu trước khi đưa vào khai thác.
- **Quy trình tạo và áp dụng Ruleset**:
  1. **Tạo Ruleset**:
     - Có thể dựa trên các gợi ý tự động của DataBrew (Recommendations) hoặc tự định nghĩa.
     - Ví dụ quy tắc 1: Kiểm tra dòng trùng lặp (`duplicate rows == 0`).
     - Ví dụ quy tắc 2: Kiểm tra giá trị số hợp lệ trên các cột cụ thể (`Quantity > 0`, `Total_Sales > 0`).
  2. **Tạo Profile Job gắn kèm Ruleset**:
     - Chạy Job phân tích dữ liệu áp dụng ruleset vừa tạo.
  3. **Đánh giá kết quả kiểm tra**:
     - Báo cáo tỷ lệ đạt/không đạt (ví dụ: 99% đạt chuẩn, <1% không hợp lệ do phát sinh giá trị `<= 0`).
     - Chỉ ra chính xác các bản ghi/cột cần thêm các bước xử lý biến đổi (Data Transformation) tiếp theo trong pipeline.
