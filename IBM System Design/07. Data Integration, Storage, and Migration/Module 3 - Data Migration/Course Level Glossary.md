# Course Level Glossary: Data Integration, Storage, and Migration

Bản tổng hợp và chuẩn hóa thuật ngữ chuyên ngành (Architecture & Data Engineering) xuyên suốt khóa học.

---

## 1. Storage Technologies & Types (Lưu trữ dữ liệu)

| Thuật ngữ | Khái niệm & Đặc điểm kỹ thuật |
| :--- | :--- |
| **Storage** | Công nghệ và quy trình dùng để lưu giữ và duy trì dữ liệu số. |
| **Memory** | Bộ nhớ tạm (RAM) lưu trữ dữ liệu đang được CPU xử lý tích cực, tốc độ cực cao, mất dữ liệu khi mất nguồn (volatile). |
| **Direct-Attached Storage (DAS)** | Thiết bị lưu trữ kết nối trực tiếp với một máy chủ duy nhất (như internal disk hoặc external array cáp riêng), không chia sẻ qua network chung. |
| **Network-Attached Storage (NAS)** | Hệ thống lưu trữ cấp file (file-level) kết nối trực tiếp vào mạng IP nội bộ (LAN), cho phép nhiều máy trạm truy cập dữ liệu qua giao thức chia sẻ file. |
| **Storage Area Network (SAN)** | Mạng chuyên dụng tốc độ cao chuyên kết nối các thiết bị lưu trữ cấp block (block-level) tới nhiều server, tách biệt khỏi LAN thông thường. |
| **Block Storage** | Quản lý dữ liệu dưới dạng các khối có kích thước cố định độc lập (fixed-size blocks). Hệ điều hành coi nó như raw disk drives. Hiệu năng I/O và IOPS tối ưu cho Database. |
| **File Storage** | Quản lý dữ liệu dưới dạng tệp tin, tổ chức theo cấu trúc phân cấp cây thư mục (hierarchical directory/files). Thích hợp chia sẻ tài liệu và file văn phòng. |
| **Hard Disk Drives (HDD)** | Lưu trữ từ tính truyền thống dùng đĩa quay cơ học, dung lượng lớn, giá rẻ nhưng latency cao và IOPS thấp. |
| **Solid State Drives (SSD)** | Lưu trữ thể rắn dùng bộ nhớ flash NAND, không có bộ phận chuyển động, tốc độ đọc/ghi và IOPS vượt trội. |
| **Magnetic Tape** | Băng từ lưu trữ dữ liệu tuyến tính, chi phí cực thấp và độ bền cao, chuyên dùng cho backup lâu dài và cold archive. |
| **Optical Storage** | Lưu trữ quang học sử dụng tia laser để đọc/ghi dữ liệu (CD, DVD, Blu-ray). |

---

## 2. Storage Protocols (Giao thức truyền thông lưu trữ)

| Giao thức | Lớp lưu trữ | Chi tiết kỹ thuật & Trường hợp sử dụng |
| :--- | :--- | :--- |
| **Storage Protocol** | Chung | Bộ quy tắc và tiêu chuẩn định nghĩa cách hệ thống máy chủ và thiết bị lưu trữ giao tiếp với nhau. |
| **SCSI (Small Computer System Interface)** | Block | Chuẩn giao tiếp truyền thống kết nối máy tính với thiết bị ngoại vi và ổ cứng; là nền tảng cho nhiều giao thức hiện đại. |
| **SAS (Serial Attached SCSI)** | Block | Tiến hóa dạng point-to-point tuần tự từ parallel SCSI, chuyên dụng kết nối ổ cứng HDD/SSD doanh nghiệp với controller của server. |
| **iSCSI (Internet Small Computer System Interface)** | Block | Đóng gói tập lệnh SCSI qua mạng IP (TCP/IP), cho phép dựng hạ tầng SAN chi phí thấp trên switch/cable Ethernet thông thường. |
| **Fiber Channel (FC)** | Block | Giao thức quang chuyên dụng hiệu năng cực cao (lên tới 128 Gbps), độ trễ thấp và zero-packet-loss cho Enterprise SAN. |
| **Fiber Channel over Ethernet (FCoE)** | Block | Đóng gói frame Fibre Channel truyền trực tiếp qua hạ tầng mạng 10GbE/40GbE Lossless Ethernet, hợp nhất lưu trữ và mạng. |
| **NVMe (Non-Volatile Memory Express)** | Block | Giao thức tối ưu riêng cho SSD flash kết nối trực tiếp qua bus PCIe, tận dụng tối đa hàng ngàn hàng đợi (queues) với độ trễ tối thiểu. |
| **NFS (Network File System)** | File | Giao thức chia sẻ file qua mạng mạng IP (phát triển bởi Sun Microsystems), tiêu chuẩn trong môi trường Linux/UNIX. |
| **SMB/CIFS (Server Message Block / Common Internet File System)** | File | Giao thức chia sẻ tệp và máy in qua mạng, tiêu chuẩn phổ biến trong môi trường Windows. |
| **AFP (Apple Filing Protocol)** | File | Giao thức lưu trữ và chia sẻ file độc quyền qua mạng dành cho macOS/Apple. |

---

## 3. Data Integration, Pipeline & Movements (Tích hợp & Xử lý dữ liệu)

| Thuật ngữ | Phân loại | Định nghĩa & Nguyên lý |
| :--- | :--- | :--- |
| **Data Integration** | Tổng quan | Quá trình gom và hợp nhất dữ liệu từ nhiều nguồn phân tán để tạo nên một góc nhìn thống nhất, mạch lạc (single coherent view). |
| **Data Extraction** | Bước xử lý | Trích xuất và lấy dữ liệu thô từ hệ thống nguồn gốc (source database, logs, APIs, flat files). |
| **Data Mapping** | Bước xử lý | Ánh xạ các trường dữ liệu tương ứng giữa hệ thống nguồn và đích nhằm bảo đảm tính chính xác khi chuyển đổi. |
| **Data Transformation** | Bước xử lý | Chuyển đổi định dạng, làm sạch, chuẩn hóa và tổng hợp dữ liệu phù hợp với schema và logic của hệ thống đích. |
| **Data Loading** | Bước xử lý | Nạp dữ liệu đã xử lý vào hệ thống đích (data warehouse, data mart, operational database). |
| **ETL (Extract-Transform-Load)** | Pipeline | Quy trình trích xuất -> chuyển đổi dữ liệu trên intermediate server/engine -> nạp vào hệ thống đích. Phù hợp xử lý dữ liệu truyền thống với relational DWH. |
| **ELT (Extract-Load-Transform)** | Pipeline | Trích xuất -> nạp trực tiếp toàn bộ dữ liệu thô vào hệ thống đích (như BigQuery/Snowflake) -> dùng sức mạnh xử lý song song của đích để transform. |
| **Data Virtualization** | Kiến trúc | Tạo một tầng dữ liệu ảo (logical/abstraction layer) truy vấn trực tiếp vào dữ liệu nguồn mà không cần sao chép, di dời dữ liệu vật lý. |
| **Data Replication** | Đồng bộ | Sao chép dữ liệu từ một hệ thống sang hệ thống khác nhằm bảo đảm tính sẵn sàng cao (HA), phân tán tải và dự phòng thảm họa (DR). |
| **Data Synchronization** | Đồng bộ | Duy trì trạng thái dữ liệu luôn đồng nhất và mới nhất giữa các hệ thống (real-time streaming hoặc batch schedules). |
| **Change Data Capture (CDC)** | Đồng bộ | Kỹ thuật theo dõi, chụp lại các thao tác thay đổi dữ liệu (Insert, Update, Delete) ở mức database log và truyền ngay lập tức sang đích theo thời gian thực. |
| **Primary-replica Backup Configuration** | Backup/HA | Cấu hình trong đó toàn bộ thao tác ghi và xử lý chính diễn ra tại Primary system, sau đó dữ liệu được replicate sang Replica (Secondary) theo thời gian thực hoặc định kỳ. |

---

## 4. Integration Patterns & Connectors (Mô hình kết nối)

| Thuật ngữ | Định nghĩa & Ứng dụng |
| :--- | :--- |
| **Integration Patterns** | Các mô hình và kiến trúc mẫu được chuẩn hóa để bảo đảm việc tích hợp dữ liệu hiệu quả, mở rộng và dễ bảo trì. |
| **Point-to-point** | Kết nối trực tiếp giữa từng cặp nguồn và đích. Dễ triển khai ban đầu nhưng nhanh chóng biến thành mớ bòng bong (spaghetti architecture, $O(N^2)$) khi số lượng hệ thống tăng. |
| **Hub-and-spoke** | Mô hình kết nối tập trung qua một Broker/Hub ở giữa; tất cả hệ thống kết nối vào hub, giảm số lượng kết nối trực tiếp xuống $O(N)$. |
| **Data Connectors** | Các module/công cụ phần mềm hỗ trợ kết nối và trung chuyển dữ liệu giữa các hệ thống. |
| **API Connectors** | Đầu nối tận dụng REST/SOAP/GraphQL APIs để tích hợp ứng dụng và dịch vụ. |
| **Application Connectors** | Đầu nối chuyên biệt được đóng gói sẵn để kéo/đẩy dữ liệu từ hệ thống ERP, CRM doanh nghiệp (SAP, Salesforce,...). |
| **Database Connectors** | Đầu nối giao tiếp trực tiếp với database engine qua driver bản địa (JDBC/ODBC, MongoDB driver, MySQL/Postgres wire protocol). |
| **File-based Connectors** | Đầu nối xử lý tích hợp dữ liệu qua việc đọc/ghi các file có cấu trúc (CSV, JSON, XML, Parquet). |
| **Cloud Connectors** | Đầu nối trung chuyển dữ liệu giữa các dịch vụ và ứng dụng chạy trên nền tảng cloud. |
| **Custom Connectors** | Đầu nối tự lập trình để giải quyết các giao thức hoặc hệ thống chuyên biệt (legacy/proprietary) mà connector tiêu chuẩn không đáp ứng được. |

---

## 5. Cloud Computing & Deployment Models (Mô hình đám mây)

| Thuật ngữ | Đặc điểm |
| :--- | :--- |
| **Cloud Storage** | Dịch vụ lưu trữ dữ liệu trên máy chủ từ xa, quản trị bởi nhà cung cấp đám mây và truy cập qua Internet (ví dụ: S3, GCS, Azure Blob). |
| **Public Cloud** | Hạ tầng và dịch vụ được nhà cung cấp (AWS, GCP, Azure, IBM Cloud) cung cấp đại chúng cho nhiều khách hàng (multi-tenant) qua Internet. |
| **Private Cloud** | Hạ tầng đám mây dành riêng hoàn toàn cho một tổ chức duy nhất, triển khai on-premises hoặc hosted riêng biệt, kiểm soát tối đa về bảo mật. |
| **Hybrid Cloud** | Mô hình lai kết hợp giữa Private Cloud (hoặc on-premises data center) và Public Cloud, cho phép chia sẻ dữ liệu và workload linh hoạt giữa 2 môi trường. |
