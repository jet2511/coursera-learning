# Module 2: Data ingestion, cataloging, and preparation

## 1. Tổng quan kiến trúc Data Lake (Core Layers)
Một kiến trúc Data Lake tiêu chuẩn thường gồm các tầng sau:
1. **Data Sources (Nguồn dữ liệu)**: Dữ liệu giao dịch, streaming, file logs, v.v.
2. **Data Ingestion (Nạp dữ liệu)**: Cơ chế đưa dữ liệu từ nguồn vào Data Lake (Batch / Streaming).
3. **Data Storage (Lưu trữ)**: Nơi chứa dữ liệu thô và dữ liệu đã xử lý (thường là Amazon S3).
4. **Catalog & Processing (Danh mục & Xử lý)**: Tự động trích xuất schema, lập danh mục dữ liệu (AWS Glue Data Catalog/Crawlers) và biến đổi dữ liệu (ETL).
5. **Search & Analytics (Tìm kiếm & Phân tích)**: Truy vấn dữ liệu trực tiếp không cần load vào DB (Amazon Athena, Amazon OpenSearch, Amazon Redshift Spectrum).
6. **Visualization (Trực quan hóa)**: Dashboard, báo cáo (Amazon QuickSight) *(tùy chọn theo use case)*.

---

## 2. Mục tiêu trọng tâm của Module 2 (Module Objectives)
Module này tập trung vào 4 khâu cốt lõi:
- **Data Ingestion & Storage**: Mối quan hệ giữa nạp dữ liệu và lựa chọn nơi lưu trữ phù hợp nhất trên AWS (S3).
- **Tối ưu hiệu năng & Chi phí**:
  - **Data Formatting**: Lựa chọn định dạng lưu trữ (Columnar format: Parquet, ORC so với Row-based: CSV, JSON).
  - **Partitioning & Compaction**: Phân vùng dữ liệu hợp lý và gom cụm các file nhỏ để tối ưu hóa quét dữ liệu.
  - **Compression**: Nén dữ liệu (Snappy, GZIP) giúp giảm dung lượng và I/O khi truy vấn.
- **Data Discovery & Cataloging (AWS Glue Crawlers)**:
  - Tự động infer/phát hiện schema từ dữ liệu trên S3.
  - Ghi metadata vào AWS Glue Data Catalog.
- **Data Lake Querying & Security**:
  - Truy vấn dữ liệu trên Data Lake bằng **Amazon Athena** mà không cần server (Serverless SQL).
  - Áp dụng các chính sách bảo mật cho Data Lake.
