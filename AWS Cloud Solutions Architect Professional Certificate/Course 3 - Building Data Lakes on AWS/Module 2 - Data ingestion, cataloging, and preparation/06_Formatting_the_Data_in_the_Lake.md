# Formatting the Data in the Lake (Định dạng dữ liệu trong Data Lake)

## 1. Nguyên tắc xử lý dữ liệu thô (Raw Data)
- **Source of Truth**: Dữ liệu thô (Raw data) được nạp vào ở dạng nguyên bản để làm nguồn dữ liệu gốc đáng tin cậy. Sau đó có thể chuyển vào **Amazon Glacier** để lưu trữ lâu dài (archival) với chi phí rẻ.
- **Không truy vấn trực tiếp trên Raw Data**: Việc chạy các câu truy vấn phân tích trực tiếp trên dữ liệu thô (CSV/JSON dung lượng lớn) gây tốn tài nguyên tính toán (CPU/RAM), tốn thời gian và tăng chi phí quét dữ liệu trên Cloud.

---

## 2. Row-based Formats vs Columnar Data Formats

| Tiêu chí | Row-based Format (CSV, JSON, Avro) | Columnar Format (Apache Parquet, Apache ORC) |
| :--- | :--- | :--- |
| **Cách lưu trữ** | Dữ liệu được ghi tuần tự theo từng hàng (Row 1 $\rightarrow$ Row 2 $\rightarrow$ Row 3). | Dữ liệu được tổ chức và lưu trữ theo từng cột riêng biệt (Column A $\rightarrow$ Column B). |
| **Cơ chế quét (Scan)** | Phải quét toàn bộ dòng từ đầu đến cuối file để lấy dữ liệu của 1 cột cụ thể. | Chỉ đọc đúng phần block đĩa chứa cột được yêu cầu trong câu lệnh query (Column Projection / Pruning). |
| **Hiệu năng Disk I/O** | Disk I/O rất lớn khi bảng có nhiều dòng/cột. | Giảm thiểu tối đa Disk I/O operations. |
| **Use case tối ưu** | Transaction ghi/đọc cả bản ghi (OLTP), truyền nhận thông điệp API. | Phân tích dữ liệu lớn, tổng hợp, BI, Analytics (OLAP). |

---

## 3. Lợi ích khi chuyển đổi sang Columnar Data Formats
- **Giảm khối lượng Disk I/O**: Ví dụ câu lệnh `SELECT user_id FROM table;` chỉ cần đọc cột `user_id`, bỏ qua hoàn toàn các cột `age`, `state`, v.v.
- **Tăng tốc độ truy vấn (Performance)**: Query chạy nhanh hơn gấp nhiều lần so với quét trên file CSV/JSON.
- **Tối ưu chi phí (Cost Efficiency)**: Trên AWS (đặc biệt là dịch vụ tính phí theo lượng dữ liệu quét như **Amazon Athena**), dung lượng scan ít hơn $\rightarrow$ thời gian thực thi ngắn hơn $\rightarrow$ giảm chi phí trực tiếp.

---

## 4. Công cụ chuyển đổi định dạng trên AWS
- Sử dụng **AWS Glue ETL Jobs** (hoặc AWS EMR / Glue DataBrew) để tự động hóa việc đọc dữ liệu CSV/JSON từ S3 và chuyển đổi sang các định dạng columnar tối ưu như:
  - **Apache Parquet** (phổ biến nhất, tối ưu tốt với Spark/Athena/Redshift Spectrum).
  - **Apache ORC** (tối ưu mạnh với Hive/Presto).
