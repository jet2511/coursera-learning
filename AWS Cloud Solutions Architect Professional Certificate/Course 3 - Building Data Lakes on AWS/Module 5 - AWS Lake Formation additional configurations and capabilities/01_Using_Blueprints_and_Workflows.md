# Module 5: AWS Lake Formation additional configurations and capabilities

## Bài học: Using Blueprints and Workflows

### 1. Thách thức khi xây dựng Data Lake
- Việc xây dựng một Data Lake trên thực tế phức tạp hơn nhiều so với lý thuyết (cần nhiều bước cấu hình lưu trữ, catalog, bảo mật, ETL pipeline).
- **AWS Lake Formation** cung cấp bộ chuẩn hóa (set of standards) và công cụ tự động hóa giúp thiết lập Data Lake nhanh chóng, tránh việc phải tự mày mò cấu hình rời rạc từ đầu.

---

### 2. AWS Lake Formation Blueprints
- **Bản chất**: Hoạt động giống như bản thiết kế kiến trúc xây dựng (blueprint), chứa toàn bộ định nghĩa cấu trúc và hướng dẫn cần thiết từ đầu.
- **Tích hợp sâu với hệ sinh thái AWS**:
  - **Lưu trữ**: Amazon S3 hoặc Amazon Redshift (tùy thuộc vào dạng dữ liệu nguồn).
  - **ETL / Xử lý**: Thiết lập AWS Glue để chạy các tác vụ trích xuất và biến đổi dữ liệu.
  - **Truy vấn**: Tích hợp sẵn Amazon Athena để truy vấn dữ liệu trực tiếp trên S3.
  - **Khám phá dữ liệu**: Tự động kích hoạt Crawler và Catalog dữ liệu vào Glue Data Catalog.
  - **Bảo mật**: Thiết lập phân quyền chi tiết (Fine-grained access control), kiểm soát chính xác ai được phép truy cập dữ liệu nào.

---

### 3. Lake Formation Workflows
- **Bản chất**: Là chuỗi tác vụ / luồng công việc (workflows) chạy bên dưới Blueprint, định nghĩa chính xác cách dữ liệu được **Extract, Transform, and Load (ETL)** vào Data Lake.
- **Cơ chế thực thi**: Tận dụng trực tiếp **AWS Glue** bên dưới nền để thực hiện các tác vụ ETL tự động.

---

### 4. Quy trình 3 bước thiết lập với Blueprint
1. **Select Blueprint**: Chọn mẫu Blueprint dựng sẵn từ AWS (ví dụ: database ingest, log ingest...).
2. **Configure Source & Target**: Cấu hình nguồn dữ liệu (Source) và nơi lưu trữ dữ liệu đích (Target - thường là S3).
3. **Configure Workflow**: Cấu hình lịch trình chạy và thông số luồng workflow.

Sau khi hoàn tất 3 bước trên, Lake Formation sẽ tự động vận hành quy trình thu thập, xử lý, catalog và tổ chức dữ liệu vào Data Lake.
