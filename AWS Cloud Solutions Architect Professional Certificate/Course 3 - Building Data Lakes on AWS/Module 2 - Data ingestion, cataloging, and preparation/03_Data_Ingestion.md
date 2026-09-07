# Data Ingestion (Nạp dữ liệu vào Data Lake)

Dựa vào loại dữ liệu và trường hợp sử dụng, AWS chia các phương pháp/công cụ Ingestion thành **3 nhóm chính**:

---

## 1. Files & Objects Ingestion (Nạp tập tin & đối tượng có sẵn)
Áp dụng cho các dữ liệu đã tồn tại sẵn dưới dạng tệp tin như: hình ảnh, video, PDF, log files, text files,...

* **AWS Transfer Family**: 
  - Quản lý và chuyển file bảo mật qua các giao thức tiêu chuẩn: **SFTP, FTPS, FTP**.
  - Kết nối trực tiếp vào Amazon S3 chỉ với vài cú click trên Console.
* **Amazon AppFlow**: 
  - Tích hợp và truyền dữ liệu 2 chiều bảo mật giữa các ứng dụng **SaaS** (như Salesforce, ServiceNow, Zendesk, Marketo,...) và các dịch vụ AWS như **Amazon S3**.
* **AWS Snow Family** (*Snowcone, Snowball, Snowmobile*): 
  - Thiết bị phần cứng vật lý chuyên dụng dùng để di chuyển dữ liệu dung lượng lớn (hàng chục đến hàng trăm Terabytes/Petabytes) trong điều kiện **không có hoặc băng thông Internet bị giới hạn**.
* **Công cụ Open-source phổ biến**: Logstash, Apache Flume, Apache Log4j.

---

## 2. Transactional / Operational Data Ingestion (Dữ liệu giao dịch / Cơ sở dữ liệu)
Áp dụng cho việc đồng bộ và di chuyển dữ liệu từ Database quan hệ (RDBMS) hoặc NoSQL vào Data Lake với độ trễ tối thiểu (Change Data Capture - CDC), đảm bảo không mất mát dữ liệu và hạn chế downtime.

* **AWS Database Migration Service (AWS DMS)**:
  - Dịch vụ di chuyển và đồng bộ (replication) cơ sở dữ liệu có quản lý.
  - Hỗ trợ hơn **20 database engines** khác nhau (Oracle, SQL Server, MySQL, PostgreSQL,... sang Amazon S3/Aurora/Redshift).
  - Hoạt động liên tục với độ trễ thấp (near real-time CDC).
* **AWS Schema Conversion Tool (AWS SCT)**:
  - Công cụ phần mềm cài đặt cục bộ (Client-side app) dùng để **tự động chuyển đổi schema/code database** khác nguồn (ví dụ: Oracle $\rightarrow$ PostgreSQL / Amazon Aurora / Redshift).
  - Thường là "cặp bài trùng" đi trước DMS: Dùng **SCT** để convert cấu trúc schema $\rightarrow$ Dùng **DMS** để replicate và đồng bộ dữ liệu.

---

## 3. Streaming Data Ingestion (Dữ liệu dòng thời gian thực)
Áp dụng cho dữ liệu phát sinh liên tục theo thời gian thực (real-time) như: IoT sensors, Clickstreams từ website, telemetry trong game, log events,...

* **Amazon Kinesis**: Bộ dịch vụ fully managed để thu thập, xử lý và phân tích streaming data theo mọi quy mô.
  - **Kinesis Agent**: Cài đặt trên source (như EC2) để thu thập log và đẩy dữ liệu.
  - **Kinesis Data Firehose**: Tự động load streaming data trực tiếp vào **Amazon S3**, Redshift, OpenSearch,... Hỗ trợ biến đổi dữ liệu inline qua **AWS Lambda**.
  - **Kinesis Data Streams & Kinesis Data Analytics**: Xử lý, tính toán luồng thời gian thực qua SQL hoặc Apache Flink.
* **Công cụ Open-source phổ biến**: Apache Kafka, Fluentd, Apache Sqoop.

---

## 📌 Bảng tổng hợp công cụ Data Ingestion

| Loại Dữ Liệu | Nguồn / Định dạng tiêu biểu | Dịch vụ AWS khuyến nghị | Công cụ Open Source tương đương |
| :--- | :--- | :--- | :--- |
| **Files / Objects** | SFTP/FTP server, SaaS Apps (Salesforce), Offline Data | AWS Transfer Family, Amazon AppFlow, AWS Snow Family | Logstash, Apache Flume |
| **Transactional / DB** | Oracle, SQL Server, MySQL, Postgres (CDC, Snapshot) | AWS DMS, AWS SCT | Debezium, Apache Sqoop |
| **Streaming Data** | IoT sensors, Web Clickstreams, Logs thời gian thực | Amazon Kinesis (Firehose / Data Streams) | Apache Kafka, Fluentd |
