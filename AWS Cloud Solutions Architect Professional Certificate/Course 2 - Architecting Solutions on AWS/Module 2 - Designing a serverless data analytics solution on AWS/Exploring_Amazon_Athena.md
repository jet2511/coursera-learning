# Tóm tắt bài học: Thực hành & Khám phá Amazon Athena (Exploring Amazon Athena)

**Khóa học:** Course 2 - Architecting Solutions on AWS  
**Chủ đề:** Hướng dẫn sử dụng Athena Query Editor, câu lệnh DDL (`CREATE EXTERNAL TABLE`), cấu hình SerDe và thực thi truy vấn SQL  
**Vị trí:** Module 2 - Designing a serverless data analytics solution on AWS

---

## 1. Giao diện Athena Query Editor (Trình soạn thảo truy vấn)
* **Khám phá Query Editor:** Cho phép người dùng viết các câu lệnh SQL tiêu chuẩn để truy vấn trực tiếp dữ liệu đang nằm trên **Amazon S3** mà không cần khởi tạo cơ sở dữ liệu hay nạp dữ liệu (ETL) trước.

---

## 2. Bản chất câu lệnh DDL trong Athena (`CREATE EXTERNAL TABLE`)

Khi chọn tính năng **Generate table DDL** (*Data Definition Language*) cho một bảng có sẵn (ví dụ: bảng `year_2018`), Athena sẽ hiển thị cấu trúc lệnh tạo bảng tương tự như sau:

```sql
CREATE EXTERNAL TABLE IF NOT EXISTS `year_2018` (
  `vendorid` string,
  `passenger_count` int,
  `trip_distance` double,
  `total_amount` double
)
ROW FORMAT DELIMITED 
  FIELDS TERMINATED BY ',' 
STORED AS INPUTFORMAT 'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION 's3://nyc-tlc-raf/prefix_path/'
TBLPROPERTIES ('has_encrypted_data'='false');
```

### 🔍 Giải thích các thành phần kỹ thuật quan trọng:
* **`EXTERNAL`:** Khẳng định dữ liệu nằm bên ngoài Athena (trên Amazon S3). Nếu bạn thực hiện lệnh `DROP TABLE`, Athena chỉ xóa metadata (schema) trong bảng, **dữ liệu gốc trên S3 vẫn còn nguyên vẹn**.
* **`LOCATION 's3://...'`:** Chỉ định đường dẫn thư mục/tiền tố (prefix) trên S3 chứa các tệp dữ liệu cần phân tích.
* **`SerDe / ROW FORMAT`:** Định nghĩa cách thức Athena phân tích cú pháp tệp (ví dụ: phân cách bằng dấu phẩy `,` cho CSV, hoặc cấu trúc object cho JSON).

---

## 3. Thực thi truy vấn SQL & Tối ưu hóa

```sql
-- Ví dụ truy vấn giới hạn 10 bản ghi đầu tiên
SELECT * 
FROM year_2018 
LIMIT 10;
```

### Các định dạng dữ liệu hỗ trợ & Khả năng mở rộng:
1. **Định dạng tệp phong phú:** Hỗ trợ **JSON**, **CSV**, **ORC**, và đặc biệt là **Apache Parquet** (định dạng lưu trữ dạng cột - *Columnar Storage*, giúp giảm mạnh dung lượng quét và tiết kiệm chi phí truy vấn).
2. **Khả năng JOIN đa bảng:** Cho phép thực hiện các phép nối (`JOIN`) giữa nhiều bảng Athena khác nhau, kể cả khi dữ liệu của các bảng nằm ở **các S3 Bucket hoàn toàn khác nhau**.
