# Partitioning, Compressing, and Compacting Data in Data Lake

Sau khâu **Formatting** (chuyển sang Columnar như Parquet), 3 kỹ thuật bổ trợ cực kỳ quan trọng để tối ưu hóa chi phí, hiệu năng quét và tốc độ truy vấn trên Data Lake là **Partitioning**, **Compression**, và **Compaction**.

---

## 1. Data Partitioning (Phân vùng dữ liệu)
- **Định nghĩa**: Kỹ thuật chia nhỏ tập dữ liệu thành các phân vùng/khối nhỏ (chunks/folders) dựa trên các tiêu chí lọc thường xuyên xuất hiện trong câu lệnh truy vấn (ví dụ: `year`, `month`, `day`, `region`, `device_type`).
- **Cơ chế**: Ví dụ đường dẫn trên S3: `s3://bucket/data/year=2024/month=02/day=05/`. Khi thực thi truy vấn lọc theo ngày 05/02, công cụ query (Athena/Presto) chỉ đọc thư mục tương ứng (**Partition Pruning**), bỏ qua toàn bộ dữ liệu của các ngày/tháng khác.
- **Lợi ích**: Giảm mạnh dung lượng dữ liệu phải quét (Scanned Data Size) $\rightarrow$ Tăng tốc độ truy vấn và tiết kiệm chi phí.
- **Lưu ý quan trọng**: Phải hiểu rõ hành vi/nhu cầu truy vấn của nghiệp vụ (Business query patterns) để chọn cột phân vùng phù hợp, tránh phân vùng quá chi tiết gây ra vấn đề Small Files.

---

## 2. Data Compression (Nén dữ liệu)
- **Định nghĩa**: Kỹ thuật nén các khối dữ liệu để giảm kích thước lưu trữ vật lý trên đĩa.
- **Các thuật toán nén phổ biến**:
  - **Snappy**: Cân bằng tối ưu giữa tốc độ nén/giải nén cực nhanh và tỷ lệ nén tốt (thường đi kèm mặc định với Apache Parquet).
  - **GZIP**: Tỷ lệ nén cao hơn Snappy nhưng tốn nhiều CPU khi giải nén hơn.
  - **LZO, ZSTD**: Các chuẩn nén hỗ trợ splitable và hiệu năng cao.
- **Lợi ích**: 
  - Giảm chi phí lưu trữ hàng tháng trên S3 (Pay-as-you-go).
  - Giảm lưu lượng truyền qua mạng (Network I/O) và Disk I/O trong quá trình quét dữ liệu.

---

## 3. Data Compaction (Gom cụm / Hợp nhất file)
- **Vấn đề Small Files (Small File Problem)**: Nếu nạp dữ liệu streaming hoặc phân vùng quá mịn (ví dụ tạo 1 file nhỏ theo từng giây/phút hoặc mỗi chuyến xe 1 file), Data Lake sẽ chứa hàng triệu file có dung lượng chỉ vài KB. Việc này gây ra quá tải gọi API S3 (S3 GET/LIST metadata overhead), khiến hiệu năng truy vấn chậm nghiêm trọng.
- **Định nghĩa Compaction**: Tiến trình gom gộp (combine/merge) nhiều file nhỏ thành một số lượng ít hơn các file có kích thước tối ưu (thường từ **128MB - 512MB**).
- **Công cụ thực hiện**: Dùng **AWS Glue ETL Jobs** hoặc EMR định kỳ để gộp các file nhỏ thành các file Parquet kích thước chuẩn.
- **Quy tắc "Xay cà phê" (Coffee Grinding Analogy)**: Kích thước file và độ mịn phân vùng cần được thiết kế vừa vặn dựa trên thói quen query của doanh nghiệp.

---

## 4. Security: Mã hóa Dữ liệu (Encryption Best Practices)
"Security is Job Zero at AWS":
- **Encryption in Transit (Mã hóa khi truyền tải)**: AWS tự động áp dụng qua TLS/HTTPS khi giao tiếp với Amazon S3.
- **Encryption at Rest (Mã hóa khi lưu trữ)**:
  - **Server-Side Encryption (SSE)**: `SSE-S3` (khóa do S3 quản lý), `SSE-KMS` (quản lý khóa qua AWS KMS với audit trail), `SSE-C` (khách hàng tự cấp khóa).
  - **Client-Side Encryption (CSE)**: Mã hóa dữ liệu ngay từ client trước khi upload lên S3.
