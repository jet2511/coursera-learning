# Modern Data Architecture on AWS

**Khóa học:** Course 3 - Building Data Lakes on AWS  
**Module:** Module 6 - Modern data architecture on AWS  
**Chủ đề:** Modern Data Architecture (Kiến trúc dữ liệu hiện đại trên AWS)

---

## 1. Tổng quan về Kiến trúc dữ liệu hiện đại (Modern Data Architecture)

Một kiến trúc dữ liệu hiện đại (Modern Data Architecture / Lakehouse architecture) trên AWS được xây dựng và vận hành xoay quanh **5 trụ cột cốt lõi**:
1. **Scalable Data Lakes** (Data Lake mở rộng linh hoạt)
2. **Purpose-built Analytics Services** (Các dịch vụ phân tích chuyên biệt theo mục đích)
3. **Unified Data Access** (Truy cập dữ liệu hợp nhất & luân chuyển linh hoạt)
4. **Unified Governance** (Quản trị dữ liệu tập trung, bảo mật & kiểm toán)
5. **Performance and Cost Effectiveness** (Tối ưu hóa hiệu năng và chi phí)

---

## 2. Chi tiết 5 Trụ cột & Các Dịch vụ AWS tương ứng

### 1. Scalable Data Lakes (Data Lake có khả năng mở rộng)
* **Mục tiêu:** Lưu trữ an toàn, chi phí thấp, dung lượng không giới hạn và quản lý metadata cho các tập dữ liệu đa dạng (structured, semi-structured, unstructured).
* **Dịch vụ AWS chính:**
  * **Amazon S3:** Nền tảng lưu trữ đối tượng (Object Storage) cốt lõi cho Data Lake với độ bền 99.999999999% (11 số 9), khả năng mở rộng quy mô không giới hạn.
  * **AWS Lake Formation:** Đơn giản hóa và tự động hóa quy trình thiết lập, quản lý và bảo vệ Data Lake.
  * **Amazon Athena:** Dịch vụ truy vấn không máy chủ (Serverless interactive query) sử dụng chuẩn SQL trực tiếp trên dữ liệu thô/đã xử lý trong Amazon S3.

### 2. Purpose-built Analytics Services (Dịch vụ phân tích chuyên biệt)
* **Mục tiêu:** Chọn đúng công cụ/kho lưu trữ/công cụ tính toán phù hợp nhất cho từng bài toán nghiệp vụ cụ thể (*Right tool for the right job*).
* **Dịch vụ AWS chính:**
  * **Databases (OLTP / NoSQL):** 
    * **Amazon Aurora:** Cơ sở dữ liệu quan hệ hiệu năng cao tương thích MySQL/PostgreSQL.
    * **Amazon DynamoDB:** NoSQL database tốc độ mili-giây ở mọi quy mô.
  * **Search & Log Analytics:** **Amazon OpenSearch Service** (tìm kiếm toàn văn, phân tích log thời gian thực).
  * **Big Data Processing:** **Amazon EMR (Elastic MapReduce)** xử lý dữ liệu lớn phân tán (Apache Spark, Hadoop, Presto, Hive).
  * **Data Warehousing (OLAP):** **Amazon Redshift** phân tích dữ liệu kho tốc độ cao, hỗ trợ Redshift Spectrum để query trực tiếp trên S3.
  * **Machine Learning:** **Amazon SageMaker** xây dựng, huấn luyện và triển khai mô hình ML end-to-end.
  * **Streaming & Event Ingestion:** **Amazon MSK** (Managed Streaming for Apache Kafka).
  * **Real-time Analytics:** **Amazon Kinesis Data Analytics** (nay là Amazon Managed Service for Apache Flink) để xử lý luồng sự kiện thời gian thực bằng SQL/Java.

### 3. Unified Data Access (Truy cập dữ liệu hợp nhất)
* **Mục tiêu:** Truy cập trực tiếp dữ liệu tại nơi nó lưu trữ (*in-place query/zero-ETL*) và luân chuyển dữ liệu một cách chọn lọc (*selective movement*) khi cần thiết giữa các hệ thống (inside-out, outside-in, around-the-perimeter).
* **Dịch vụ AWS chính:**
  * **AWS Glue:** Dịch vụ Serverless ETL, phát hiện catalog (Crawlers, Data Catalog) và chuyển đổi dữ liệu.
  * **Amazon Data Firehose:** Thu thập, chuyển đổi và nạp dữ liệu streaming theo thời gian thực vào S3, Redshift, OpenSearch.
  * **AWS DMS (Database Migration Service):** Di chuyển và đồng bộ dữ liệu liên tục (CDC - Change Data Capture) giữa các CSDL và Data Lake.
  * **AWS Transfer Family:** Quản lý truyền tải file an toàn thông qua các giao thức SFTP, FTPS, FTP trực tiếp vào/ra S3.
  * **Amazon MSK:** Nền tảng bus dữ liệu sự kiện phân tán chuẩn Apache Kafka.
  * **Amazon AppFlow:** Tích hợp dữ liệu không cần code từ các ứng dụng SaaS (Salesforce, Zendesk, ServiceNow, Slack...) vào Data Lake AWS.

### 4. Unified Governance (Quản trị tập trung)
* **Mục tiêu:** Quản lý ủy quyền truy cập, bảo mật dữ liệu ở cấp độ chi tiết (Fine-grained access control) và kiểm toán (Audit logging) trên toàn bộ hệ thống phân tích.
* **Dịch vụ AWS chính:**
  * **AWS Lake Formation:**
    * Phân quyền tập trung ở cấp cơ sở dữ liệu, bảng (Table-level), cột (Column-level), hàng (Row-level) và lọc ô (Cell-level).
    * Áp dụng chính sách truy cập dựa trên thẻ tag (LF-TBAC - Tag-Based Access Control).
    * Tích hợp kiểm toán truy cập qua AWS CloudTrail.

### 5. Performance and Cost Effectiveness (Hiệu năng & Tối ưu chi phí)
* **Mục tiêu:** Đạt hiệu năng truy vấn tối đa với mức chi phí thấp nhất.
* **Kỹ thuật & Phương pháp tốt nhất (Best Practices):**
  * **Columnar Formats:** Sử dụng định dạng cột như Apache Parquet, Apache ORC để giảm dung lượng đọc quét (I/O) và tăng tốc truy vấn.
  * **Data Compression:** Áp dụng nén dữ liệu (Snappy, GZIP, ZSTD) để giảm chi phí lưu trữ S3 và băng thông mạng.
  * **Data Partitioning & Bucketing:** Phân vùng dữ liệu (ví dụ theo `year/month/day`) để Athena/EMR/Redshift chỉ quét các phân vùng cần thiết, giảm chi phí query.
  * **Cost Monitoring:** Thiết lập AWS Billing Alerts, AWS Cost Anomaly Detection và AWS Budgets để kiểm soát chi tiêu, tránh phát sinh chi phí ngoài dự kiến.
