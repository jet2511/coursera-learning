# Demo: Querying CSV data with Amazon Athena

Nội dung bài thực hành minh họa việc sử dụng **Amazon Athena** để chạy các câu lệnh SQL trực tiếp trên bảng `csv` (được tạo bởi AWS Glue Crawler từ dữ liệu NYC Taxi Trip Data tháng 06/2018 lưu trên S3).

---

## 1. Các câu lệnh truy vấn mẫu trên Athena

### 1.1. Preview bảng (Xem trước dữ liệu)
```sql
SELECT * FROM "tlc"."csv" LIMIT 10;
```
* **Mục đích**: Kiểm tra kết nối và cấu trúc dữ liệu trả về từ S3.

### 1.2. Đếm tổng số bản ghi (Count records)
```sql
SELECT COUNT(*) FROM "tlc"."csv";
```
* **Kết quả**: Hơn **8.7 triệu chuyến xe** (`8,713,832` records) trong tháng 06/2018.
* **Thời gian thực thi**: ~113 ms.
* **Dữ liệu quét (Data Scanned)**: **733 MB** (toàn bộ kích thước file CSV).

### 1.3. Tính giá trị trung bình (Average)
```sql
SELECT AVG(tip_amount) FROM "tlc"."csv";
```
* **Kết quả**: Trung bình tiền tip là `$1.90`.
* **Dữ liệu quét**: Tiếp tục quét toàn bộ **733 MB**.

### 1.4. Tìm giá trị lớn nhất (Max)
```sql
SELECT MAX(tip_amount) FROM "tlc"."csv";
```
* **Kết quả**: Tiền tip lớn nhất là `$411.00`.
* **Dữ liệu quét**: Vẫn quét toàn bộ **733 MB**.

---

## 2. Quan sát và Đánh giá cốt lõi về định dạng CSV (Row-based)
- **Hạn chế lớn của Row-based (CSV)**: 
  - Mặc dù câu truy vấn chỉ yêu cầu dữ liệu từ **1 cột duy nhất** (ví dụ `AVG(tip_amount)` hoặc `COUNT(*)`), Athena **buộc phải quét toàn bộ 733 MB** của file CSV trên đĩa/S3 cho mỗi lần chạy query.
  - Do Athena tính phí theo **Data Scanned**, việc truy vấn trực tiếp trên file CSV lớn lặp đi lặp lại sẽ làm **tăng chi phí** và **tăng thời gian Disk I/O**.
- **Giải pháp chuyển tiếp**: Cần chuyển đổi tập dữ liệu CSV này sang định dạng **Columnar (Parquet)** để tối ưu lượng dữ liệu quét (sẽ được so sánh ở bài học tiếp theo).
