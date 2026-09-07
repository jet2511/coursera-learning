# Query Data with Amazon Athena (Truy vấn Dữ liệu với Amazon Athena)

## 1. Amazon Athena là gì?
- **Amazon Athena** là dịch vụ phân tích tương tác **Serverless** cho phép truy vấn trực tiếp dữ liệu lưu trữ trên Amazon S3 bằng ngôn ngữ **Standard SQL** chuẩn (dựa trên Presto / Trino).
- **Đặc điểm chính**:
  - **Serverless**: Không cần quản lý cụm máy chủ, cấu hình hệ điều hành, cài đặt gói mạng hay lo sizing hạ tầng.
  - **Dễ sử dụng**: Chỉ cần kiến thức SQL thông thường, không yêu cầu SDK hay code phức tạp.
  - **Hỗ trợ đa định dạng**: CSV, JSON, Apache Parquet, Apache ORC, Apache Avro.
  - **Tích hợp chặt chẽ với AWS Glue Data Catalog**: Bảng tạo trong Athena sẽ đồng bộ ngay với Glue Data Catalog và ngược lại.

---

## 2. Mô hình Chi phí & Tối ưu hóa (Pricing & Optimization)
- **Cơ chế tính phí**: Tính tiền dựa trên **khối lượng dữ liệu được quét (Data Scanned)** khi thực thi câu lệnh SQL (tính theo Terabyte quét).
- **Tiết kiệm tới 90% chi phí và tăng tốc độ truy vấn** bằng cách kết hợp 3 kỹ thuật:
  1. **Columnar Formats** (Parquet / ORC): Chỉ quét đúng cột cần SELECT, bỏ qua các cột khác.
  2. **Partitioning**: Chỉ quét đúng thư mục phân vùng chứa điều kiện WHERE.
  3. **Compression** (Snappy, GZIP): Giảm kích thước dung lượng file quét thực tế từ đĩa.

---

## 3. Kiến trúc Tích hợp (Athena Integrations)
* **Athena + Amazon QuickSight**: Kết nối trực tiếp để xây dựng Dashboard BI thời gian thực, câu query được kích hoạt on-demand mỗi khi user tải báo cáo.
* **Athena + AWS Lambda & API Gateway**: Xây dựng REST API không máy chủ để ứng dụng bên ngoài hoặc microservices có thể trigger query và nhận kết quả JSON.
* **Amazon Athena Federated Query**:
  - Cho phép chạy 1 câu lệnh SQL duy nhất để **JOIN dữ liệu chéo** giữa Amazon S3 với các nguồn dữ liệu bên ngoài (như DynamoDB, RDS MySQL, PostgreSQL, DocumentDB, Redshift, Snowflake,...).
  - Sử dụng các đầu nối dữ liệu (**Athena Data Source Connectors** chạy trên AWS Lambda) để truy vấn tại nguồn mà **không cần phải copy dữ liệu về S3 trước** (tránh tình trạng dữ liệu bị cũ - Stale Data).

---

## 4. Mối quan hệ giữa Athena, Glue Catalog và Data Source
```
[ Amazon Athena (Compute / Serverless SQL Engine) ]
                   │
                   ▼ (Đọc Schema & Metadata)
     [ AWS Glue Data Catalog (Database / Table Definitions) ]
                   │
                   ▼ (Trỏ tới vị trí vật lý: LOCATION 's3://...')
         [ Amazon S3 / External Sources (Actual Data) ]
```
- **Bảng (Table)** trong Glue/Athena chỉ là thực thể Metadata. 
- Xóa bảng trong Athena $\rightarrow$ dữ liệu thô trên S3 vẫn được giữ nguyên an toàn.
