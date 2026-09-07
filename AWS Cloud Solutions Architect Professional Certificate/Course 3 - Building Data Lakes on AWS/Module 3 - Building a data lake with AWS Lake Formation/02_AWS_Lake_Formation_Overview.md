# AWS Lake Formation Overview

## 1. Vấn đề đặt ra & Vai trò của Lake Formation
- **Thách thức:** Việc tự tay thiết lập và vận hành Data Lake truyền thống đòi hỏi rất nhiều công đoạn phức tạp: cấu hình data ingestion, chọn format (Parquet/ORC), nén (compression), phân vùng (partitioning), cấu hình vị trí lưu trữ S3, phân quyền IAM, viết/chạy Glue Crawlers, quản lý Glue Data Catalog, tối ưu query, v.v.
- **Giải pháp - AWS Lake Formation:** Là dịch vụ xây dựng trên nền tảng của **AWS Glue**, giúp tự động hóa toàn bộ quy trình thiết lập môi trường Data Lake (automate the entire build environment).

---

## 2. Kiến trúc & Các thành phần cốt lõi
- **Nền tảng AWS Glue dưới hạ tầng (Under the hood):**
  - Tận dụng các tính năng có sẵn của Glue: **Crawlers**, **Glue Data Catalog**, và **Glue ETL Jobs**.
  - **Glue Data Catalog** đóng vai trò là bộ não (brain) của Data Lake — hệ thống quản lý danh mục giúp định vị chính xác dữ liệu nằm ở đâu (như chỉ mục sách trong thư viện lớn).
- **Workflow Blueprints:**
  - Thay vì tự viết các trigger, crawlers và jobs rời rạc trong Glue workflows, Lake Formation cung cấp các **Blueprints** có sẵn cho các tác vụ phổ biến nhất (ingestion và xử lý các nguồn dữ liệu chuẩn).
- **Bảo mật & Phân quyền tập trung (Centralized Access Controls):**
  - Quản lý chính sách truy cập tập trung dựa trên AWS IAM.
  - Phân quyền chi tiết (granularity) đến cấp độ: **Database**, **Table**, và **Column-level**.
- **Mã hóa dữ liệu (Encryption):**
  - Tận dụng cơ chế mã hóa sẵn có của AWS:
    - **Encryption at rest (Lưu trữ):** Server-side encryption tự động với keys do **AWS KMS** quản lý.
    - **Encryption in transit (Truyền tải):** Sử dụng chứng chỉ SSL/TLS.

---

## 3. Quy trình 3 bước thiết lập Data Lake trên AWS Lake Formation (3-Step Guide)
Trên dashboard của Lake Formation, quy trình setup được chuẩn hóa qua 3 bước:

1. **Step 1: Register Storage Locations:** Đăng ký các vị trí bucket/path lưu trữ chỉ định trên Amazon S3 vào Lake Formation.
2. **Step 2: Create Databases:** Khởi tạo một hoặc nhiều database trong Lake Formation Data Catalog. Trong quá trình ingest dữ liệu (thông qua Blueprints), hệ thống sẽ tự động sinh các bảng (tables).
3. **Step 3: Grant Permissions:** Phân quyền truy cập tài nguyên Data Lake cho người dùng/roles với độ chi tiết cao (Database, Table, Column level).
