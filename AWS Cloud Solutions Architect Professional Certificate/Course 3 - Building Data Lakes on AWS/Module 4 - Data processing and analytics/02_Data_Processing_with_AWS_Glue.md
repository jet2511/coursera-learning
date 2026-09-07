# Module 4: Data processing and analytics

## Bài học: Data Processing with AWS Glue

### 1. Tổng quan & Lợi ích so với phương pháp truyền thống
- **Truyền thống**: Xây dựng pipeline ETL rất phức tạp và tốn thời gian. Phải tự provisioning/quản lý cụm server, cài đặt phần mềm, tự dựng cơ chế trigger và scale.
- **Với AWS Glue**:
  - Dịch vụ **Serverless**: Tự động gánh toàn bộ phần hạ tầng (heavy lifting).
  - Tự động scale theo tải dữ liệu.
  - Hỗ trợ trigger linh hoạt, ví dụ kết hợp cùng **AWS Lambda** để kích hoạt Glue Job tự động ngay khi có file mới ghi vào S3 bucket.

---

### 2. Quy trình 3 bước cốt lõi của một ETL Job
1. **Extract (Trích xuất)**:
   - Truy vấn nguồn dữ liệu để lấy thông tin cần thiết.
   - Có thể lấy dạng delta ("có dữ liệu mới từ lần chạy trước không?") hoặc lọc chi tiết theo khoảng thời gian, kiểu dữ liệu, trường cụ thể.
   - Nguồn phổ biến: S3 bucket, RDS, DynamoDB, JDBC sources,...
2. **Transform (Biến đổi)**:
   - Làm sạch, cắt tỉa, chuẩn hóa và định hình lại dữ liệu thô.
   - Môi trường thực thi hỗ trợ: **Apache Spark** (xử lý dữ liệu lớn phân tán) và **Python** (Python shell cho các tác vụ nhẹ).
3. **Load (Nạp dữ liệu)**:
   - Ghi dữ liệu đã qua xử lý tới đích đến phục vụ khai thác: Database, Data Warehouse (Redshift), hoặc S3 bucket (Clean/Curated zone).

---

### 3. Ba phương thức phát triển / viết code cho AWS Glue Jobs
Khi định nghĩa logic biến đổi dữ liệu, AWS Glue cung cấp 3 lựa chọn:
- **AWS Glue Script Editor**: Viết code trực tiếp hoặc upload mã nguồn sẵn có (`.py`, Spark script). Phù hợp cho developer muốn toàn quyền kiểm soát mã nguồn.
- **AWS Glue Interactive Sessions**: Cung cấp môi trường **Jupyter Notebook** tương tác tức thì, cho phép thử nghiệm, chỉnh sửa và chạy thử code Spark/Python theo từng cell.
- **AWS Glue Studio**: Trình dựng luồng ETL trực quan (Visual Editor). Hỗ trợ kéo-thả luồng từ Source $\rightarrow$ Transform $\rightarrow$ Target, có sẵn các template dựng sẵn và tự động sinh mã nguồn bên dưới.
