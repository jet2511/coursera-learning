# Module 4: Data processing and analytics

## Bài học: AWS Glue Jobs and Workflows

### 1. Thuật ngữ AWS Glue Job
- Khi AWS Glue thực thi một khối công việc ETL (trích xuất, biến đổi, nạp dữ liệu), tác vụ đó được gọi là một **AWS Glue Job**.

---

### 2. Các cơ chế kích hoạt (Trigger Options) của AWS Glue Job
Có 3 phương thức chính để khởi chạy Glue Job:
1. **Schedule (Theo lịch trình)**:
   - Chạy định kỳ vào một mốc thời gian cố định (ví dụ: thứ Ba hàng tuần lúc 1:00 PM).
   - Phù hợp khi raw data được đổ về theo đợt định kỳ (batch) hoặc dữ liệu không yêu cầu xử lý tức thời theo thời gian thực (non-time-sensitive).
2. **On-demand (Theo yêu cầu thủ công)**:
   - Kích hoạt bằng tay khi cần thiết, không tự động chạy nếu không có lệnh.
   - Thích hợp cho các tập dữ liệu ít khi cập nhật hoặc các tác vụ chạy một lần (one-off jobs) để xử lý lượng dữ liệu đột biến lớn (large influx).
3. **Conditional / Event-based (Theo sự kiện / điều kiện)**:
   - Chạy dựa trên sự kiện phát sinh (ví dụ: khi có file dữ liệu mới được ghi vào S3 bucket).
   - Tự động hóa hoàn toàn quy trình xử lý dữ liệu ngay khi phát sinh.

---

### 3. AWS Glue Workflows (Điều phối chuỗi tác vụ)
- **Vấn đề**: Trong thực tế, một quy trình dữ liệu cần kết hợp nhiều Glue Jobs tuần tự hoặc song song (ví dụ: Job 1 làm sạch trùng lặp `deduplication`, Job 2 chuẩn hóa định dạng số điện thoại, sau đó chạy Crawler để cập nhật Data Catalog).
- **Giải pháp**: **AWS Glue Workflows** cho phép ghép nối (chain) nhiều bước/tác vụ lại thành một quy trình hoàn chỉnh.
- **Lợi ích**:
  - **Trực quan hóa (Visualized)**: Hiển thị đồ thị luồng xử lý trên AWS Management Console.
  - **Giám sát & Xử lý lỗi (Monitoring & Troubleshooting)**: Dễ dàng theo dõi tiến độ từng bước, xác định chính xác node bị lỗi (failure point) hoặc kiểm tra trạng thái thành công toàn bộ luồng.
