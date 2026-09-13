# Module 4: Data processing and analytics

## Bài học: Tech Talk - Glue / Athena Federated Queries

### 1. Bối cảnh & Vấn đề thực tế
- **Tình huống**: Doanh nghiệp đang trong quá trình chuyển dịch (migration) từ On-premises Data Lake lên AWS Cloud.
- **Thách thức**: Dữ liệu bị phân mảnh ở cả 2 nơi (một nửa ở On-prem, một nửa đã đưa lên AWS S3). Nhu cầu đặt ra là phân tích, truy vấn và trực quan hóa (dashboard/BI) kết hợp cả 2 nguồn này trong thời gian chuyển tiếp mà không cần chờ đợi hoàn tất toàn bộ migration.

---

### 2. Giải pháp: Amazon Athena Federated Queries
- **Cơ chế hoạt động**:
  - Thông thường, Athena truy vấn trực tiếp trên S3 qua metadata của AWS Glue Data Catalog.
  - **Federated Queries** mở rộng khả năng truy vấn đến bất kỳ nguồn dữ liệu nào (On-premises databases, custom data sources, Cloud data sources khác).
  - Cho phép thực hiện các câu lệnh `JOIN` giữa bảng đã lưu trên S3 và bảng vẫn đang nằm tại On-prem trong cùng một câu query SQL duy nhất.
- **Kiến trúc bên dưới**:
  - Được vận hành bởi **AWS Lambda function** (Data Source Connectors).
  - Có thể đặt Lambda chạy trong **VPC** tùy chọn để kết nối mạng an toàn về On-prem.
  - Hỗ trợ chèn code tùy biến để biến đổi dữ liệu tức thời (on-the-fly transformations) trong lúc truy vấn.

---

### 3. Trade-offs (Đánh đổi về Hiệu năng & Khái niệm Data Gravity)
Mặc dù Federated Query mang lại sự linh hoạt tối đa, nhưng không nên xem đây là đích đến thay thế hoàn toàn việc di chuyển dữ liệu lên cloud:
- **Performance Hit**: Truy vấn qua mạng Internet/VPN từ Cloud về On-prem sẽ làm tăng độ trễ và thời gian phản hồi (đặc biệt với dataset lên tới hàng trăm GB hoặc TB).
- **Khái niệm "Data Gravity" (Trọng lực dữ liệu)**:
  - Dữ liệu rất "nặng" và khó di chuyển liên tục, trong khi ứng dụng/query/container rất "nhẹ" và dễ di chuyển.
  - Nguyên tắc kiến trúc: **Nên đưa ứng dụng lại gần nơi dữ liệu lưu trữ (Keep applications close to data)**. Khi dữ liệu được tập trung hóa trên S3 cùng Region, truy vấn và phân tích giữa các dịch vụ (DynamoDB, Redshift, Athena) đạt độ trễ cực thấp (single-digit millisecond latency).
  - Vì vậy, Federated Queries chỉ nên dùng như giải pháp chuyển tiếp hoặc truy vấn ad-hoc; mục tiêu chính vẫn là hoàn thành migration lên S3 để quản trị tập trung qua AWS Lake Formation.

---

### 4. Bảo mật trong Athena Federated Queries
- **Mã hóa khi truyền tải (Encryption in Transit)**:
  - Lambda connector đặt trong private VPC kết nối về On-premises qua **VPN Tunnel** / **Direct Connect** (mã hóa ở network layer).
  - Ứng dụng/Query sử dụng chứng chỉ TLS/SSL để mã hóa ở application layer.
- **Mã hóa khi lưu trữ (Encryption at Rest)**:
  - Phía On-premises: Tự quản lý encryption key trong Data Center.
  - Phía AWS Cloud: Quản lý khóa tập trung bằng **AWS KMS (Key Management Service)**, tích hợp sẵn và tự động mã hóa trên S3.
