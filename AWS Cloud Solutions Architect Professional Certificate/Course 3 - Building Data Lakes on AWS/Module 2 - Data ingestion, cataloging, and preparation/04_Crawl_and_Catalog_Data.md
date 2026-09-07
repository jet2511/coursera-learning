# Crawl and Catalog Data (Thu thập & Lập danh mục Dữ liệu)

## 1. Tầm quan trọng của Cataloging trong Data Lake
- **Biến đổi kho dữ liệu hỗn loạn (Data Swamp)** thành một tài nguyên được tổ chức bài bản, dễ khám phá (**Discoverability**), quản trị (**Data Governance**), và tăng hiệu quả phân tích (**Analytics**).
- Tránh tình trạng lưu trữ tràn lan trên S3 gây lãng phí chi phí và khó kiểm soát dữ liệu.

---

## 2. AWS Glue & AWS Glue Data Catalog
- **AWS Glue Data Catalog**: Là kho lưu trữ metadata trung tâm (Central Metadata Repository) tương thích với Apache Hive Metastore.
- **Bản chất của Glue Catalog Tables**:
  - **Không lưu dữ liệu thực tế** bên trong Glue, mà chỉ lưu thông tin metadata và **con trỏ (pointer/location)** trỏ đến vị trí dữ liệu thực tế (thường nằm trên Amazon S3 buckets).
  - Cho phép phân quyền truy cập thông qua AWS IAM / Lake Formation và hỗ trợ join chéo dữ liệu giữa các nguồn khác nhau.

---

## 3. AWS Glue Crawler & Classifiers
* **AWS Glue Crawler**: Là tiến trình tự động quét (scan) qua các data store để:
  1. Phát hiện định dạng và cấu trúc dữ liệu.
  2. Suy luận schema (**Schema Inferencing**).
  3. Tự động tạo mới hoặc cập nhật các bảng metadata trong **AWS Glue Data Catalog**.

* **Classifiers (Bộ phân loại)**: Chịu trách nhiệm nhận dạng định dạng dữ liệu và parse schema khi Crawler kết nối tới data source:
  - **Built-in Classifiers**: Hỗ trợ sẵn các định dạng phổ biến như **JSON, CSV, Apache Parquet, Apache ORC, Apache Avro, XML**, v.v.
  - **Custom Classifiers**: Tự định nghĩa (bằng Grok patterns, XML path, JSON path) để xử lý các file log tùy biến hoặc định dạng đặc thù của doanh nghiệp.

---

## 4. Các nguồn kết nối được AWS Glue Crawler hỗ trợ
Crawler có thể kết nối đến nhiều hệ thống dữ liệu qua các cơ chế:
- **Native Clients**: Kết nối trực tiếp đến **Amazon S3**, **Amazon DynamoDB**.
- **JDBC Drivers**: Kết nối đến các relational databases như: **Amazon RDS, Amazon Aurora, PostgreSQL, MySQL, Oracle, Microsoft SQL Server, MariaDB**.
- **MongoDB Compatibility Mode**: Kết nối tới **MongoDB** hoặc **Amazon DocumentDB**.
