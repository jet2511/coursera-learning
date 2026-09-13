# Demo: Columnar Data Formats with Athena - Performance & Cost Comparison

Nội dung bài thực hành so sánh trực quan hiệu năng (thời gian chạy) và chi phí (lượng dữ liệu quét) khi chạy cùng một câu lệnh SQL trên **CSV (Row-based)** so với **Apache Parquet (Columnar + Compression)** trên Amazon Athena.

---

## 1. So sánh Dữ liệu lưu trữ trên Amazon S3
* **Dữ liệu CSV ban đầu**:
  - Gồm 1 file dung lượng **733 MB** (NYC TLC Trip Data tháng 06/2018).
* **Dữ liệu sau khi chuyển đổi sang Parquet (đã nén & phân chia)**:
  - Tập dữ liệu 733 MB CSV ban đầu được nén và chuyển đổi thành **8 file Parquet nhỏ (mỗi file ~19 MB)** $\rightarrow$ Tổng dung lượng chỉ còn ~**150 MB** (giảm gần **5 lần** dung lượng lưu trữ trên S3 nhờ thuật toán nén).

---

## 2. Quy trình thực hiện trong Demo
1. **Sync dữ liệu Parquet sang S3**:
   `aws s3 sync s3://nyc-tlc-raf/parquet/type=yellow s3://tlc-demo-raf/parquet`
2. **Tạo và chạy AWS Glue Crawler**:
   - Tên Crawler: `Parquet-Crawler`.
   - Data Source: `s3://tlc-demo-raf/parquet/`.
   - Target Database: `TLC`.
   - Chạy crawler hoàn tất $\rightarrow$ Tự động tạo bảng `parquet` trong Glue Data Catalog.
3. **Chạy cùng câu truy vấn SQL trên Amazon Athena**:
   ```sql
   SELECT AVG(fare_amount), AVG(tip_amount) FROM "tlc"."parquet";
   -- so sánh với:
   SELECT AVG(fare_amount), AVG(tip_amount) FROM "tlc"."csv";
   ```

---

## 3. Bảng so sánh kết quả thực tế (Benchmark)

| Tiêu chí | CSV Table (Row-based) | Parquet Table (Columnar + Snappy) | Mức độ cải thiện |
| :--- | :--- | :--- | :--- |
| **Dung lượng lưu trữ trên S3** | 733 MB | ~150 MB (gồm 8 files x 19 MB) | Giảm ~**80%** (tiết kiệm storage S3) |
| **Lượng dữ liệu bị quét (Data Scanned)** | **733 MB** (100% dung lượng file) | **Chỉ quét đúng 2 cột** `fare_amount` & `tip_amount` | Giảm mạnh dung lượng quét $\rightarrow$ **Tiết kiệm tới ~90% chi phí Athena** |
| **Thời gian thực thi (Execution Time)** | **2.18 giây** | **811 mili-giây (0.81s)** | **Nhanh hơn gần 3 lần** |

---

## 4. Kết luận & Best Practices cho Data Lake
- **Columnar Reading**: Khi query trên Parquet, Athena thực hiện đọc tuần tự theo chiều dọc (Vertical Sequential Read) chỉ cho các cột có trong mệnh đề `SELECT`/`WHERE` thay vì duyệt qua toàn bộ dòng như CSV.
- **Tiết kiệm chi phí kép (Double Cost Savings)**:
  1. Giảm chi phí lưu trữ trên S3 nhờ nén (Compression).
  2. Giảm chi phí truy vấn trên Athena nhờ chỉ quét phần dữ liệu cần thiết (Column Projection / Data Scanned).
- **Khuyến nghị kiến trúc**: Luôn sử dụng **AWS Glue ETL Jobs** để chuẩn hóa và chuyển đổi dữ liệu thô (CSV, JSON) sang **Apache Parquet / ORC** trước khi đưa vào tầng Analytics/BI.
