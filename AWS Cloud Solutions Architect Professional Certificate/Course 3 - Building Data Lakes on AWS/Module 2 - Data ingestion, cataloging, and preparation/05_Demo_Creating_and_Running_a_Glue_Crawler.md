# Demo: Creating and Running an AWS Glue Crawler

Nội dung bài thực hành minh họa quá trình sử dụng **AWS Glue Crawler** để quét dữ liệu CSV từ Amazon S3, tự động suy luận schema và lập bảng metadata trong **AWS Glue Data Catalog**, sau đó xem bảng qua **Amazon Athena**.

---

## 1. Chuẩn bị Dữ liệu nguồn trên Amazon S3
* **Dataset sử dụng**: New York City Taxi and Limousine Commission (NYC TLC Trip Data).
* **Cấu trúc thư mục phân vùng mẫu**:
  `s3://<bucket-name>/csv/type=yellow/year=2018/month=06/trip_data_2018-06.csv`
* **Kiểm tra cấu trúc file (bằng lệnh `head`)**:
  - Dòng header đầu tiên chứa các trường dữ liệu: `VendorID, tpep_pickup_datetime, tpep_dropoff_datetime, passenger_count, trip_distance, fare_amount,...`
* **Đích copy demo**: `s3://tlc-demo-raf/csv/`

---

## 2. Các bước cấu hình và chạy AWS Glue Crawler
1. **Tạo Glue Database**:
   - Truy cập AWS Glue $\rightarrow$ **Databases** $\rightarrow$ **Add database**.
   - Đặt tên database: `TLC`.
2. **Tạo Glue Crawler**:
   - Vào **Crawlers** $\rightarrow$ **Create crawler**.
   - Tên Crawler: `CSV-crawler`.
   - **Data Source**: Chọn S3 path `s3://tlc-demo-raf/csv/`.
   - **IAM Role**: Gán Role có quyền truy cập S3 (ví dụ `AWSGlueServiceRole-S3FullAccess` hoặc custom Glue Service Role).
   - **Target Database**: Chọn database `TLC`.
3. **Thực thi Crawler**:
   - Bấm **Run crawler** (chạy on-demand).
   - Kiểm tra log chạy qua AWS Console hoặc **CloudWatch Logs** (`/aws-glue/crawlers`).
   - Kết quả: Crawler hoàn thành (`Status: COMPLETED`), tự động thêm 1 bảng tên là `csv` vào database `TLC`.

---

## 3. Kiểm tra kết quả trên Amazon Athena
* Truy cập **Amazon Athena Query Editor** $\rightarrow$ Chọn Database `TLC` $\rightarrow$ Thấy bảng `csv`.
* **Phân tích DDL (Data Definition Language) do Crawler sinh ra**:
  - Crawler tự động map kiểu dữ liệu cho từng cột:
    - `VendorID`: `bigint`
    - `fare_amount`: `double`
    - `tpep_pickup_datetime`: `string`/`timestamp`
  - Bảng được tạo là **EXTERNAL TABLE**.

---

## 4. Điểm kiến trúc cốt lõi cần nhớ
* **Thuộc tính `LOCATION`**:
  - Bảng Glue Data Catalog chỉ chứa con trỏ (`LOCATION 's3://tlc-demo-raf/csv'`) trỏ đến S3.
  - **Không lưu dữ liệu thực tế** bên trong Glue.
* **Xóa Bảng (Drop Table)**:
  - Nếu xóa bảng trong Glue Data Catalog, **chỉ có metadata bị xóa**, toàn bộ dữ liệu gốc trên S3 **vẫn nguyên vẹn không bị mất**.
