# Module 5: AWS Lake Formation additional configurations and capabilities

## Bài học: Fine-grained Access Control

### 1. Khái niệm & Giá trị cốt lõi
- **Fine-grained Access Control (Kiểm soát truy cập chi tiết)**: Thay vì chỉ có 2 lựa chọn cực đoan là "không có quyền" (no access) hoặc "toàn quyền" (full access), Lake Formation cho phép phân quyền chi tiết tới mức:
  - **Column-level**: Chọn các cột được phép/không được phép xem (ví dụ: ẩn cột thẻ tín dụng, lương).
  - **Row-level (Data filtering)**: Chọn các dòng thỏa mãn điều kiện nhất định (ví dụ: chỉ xem dòng dữ liệu theo vùng miền hoặc phòng ban).
  - **Cell-level**: Kết hợp cả row-level và column-level để giới hạn chính xác từng ô dữ liệu.
- **Ví dụ thực tế**: Bảng dữ liệu bán hàng chứa cả thông tin sản phẩm lẫn số tài khoản ngân hàng của khách hàng. Bộ phận Marketing chỉ được cấp quyền xem các cột/dòng liên quan đến sản phẩm bán ra; trong khi bộ phận Tài chính mới được truy cập dữ liệu thanh toán.

---

### 2. Cơ chế cấp quyền hoạt động (Credential & Access Flow)
1. **User gửi yêu cầu**: User/ứng dụng yêu cầu truy vấn một tập dữ liệu qua Athena/Redshift Spectrum.
2. **Lake Formation xác thực**: Lake Formation kiểm tra chính sách quyền (permissions/policies) của User.
3. **Cấp Temporary Credentials**:
   - Lake Formation **không trực tiếp trả về dữ liệu**.
   - Nó sinh ra và cấp **Temporary Credentials (thông tin xác thực tạm thời)** cho dịch vụ truy vấn (như Athena).
4. **Truy xuất dữ liệu**: Dịch vụ dùng credentials tạm thời này để lấy đúng phần dữ liệu được phép từ S3 bucket và trả kết quả cho User. Quá trình này diễn ra hoàn toàn trong suốt (seamless) với người dùng cuối.

---

### 3. LF-Tags (Lake Formation Tags) - Quản lý quyền theo quy mô (Scale)
Khi số lượng bảng, cột và người dùng tăng nhanh, việc gán quyền tĩnh trực tiếp từng bảng/cột sẽ gây quá tải vận hành.
- **LF-Tags**: Sử dụng cặp khóa - giá trị (`key: value`), ví dụ: `Environment: Dev/QA/Prod`, `Classification: Confidential/Public`.
- **Gán Tag linh hoạt**: Tag có thể gán ở cấp độ **Database, Table, hoặc Column**.
- **LF-TBAC (Tag-Based Access Control)**:
  - Gán quyền cho IAM Role/Group dựa trên Tags (ví dụ: `Dev_Group` được truy cập tất cả tài nguyên có tag `Environment: Dev`).
  - Khi thêm tài nguyên mới hoặc nhân sự mới, chỉ cần gắn tag tương ứng mà không cần viết lại permission policy.
- **Cross-account Access**: Cho phép chia sẻ và quản lý truy cập dữ liệu giữa nhiều tài khoản AWS một cách tập trung và an toàn.

---

### 4. Các Persona/Roles tiêu biểu trong Data Lake
1. **IAM Administrator**: Quản trị viên quản lý danh tính và hạ tầng IAM toàn hệ thống.
2. **Data Lake Administrator**: "Người cứu hộ hồ dữ liệu" (Lifeguard) - có toàn quyền quản trị dữ liệu, catalog và thiết lập chính sách truy cập trong Lake Formation.
3. **Data Engineer**: Người vận hành luồng ETL, ingest dữ liệu; có quyền đọc/ghi mở rộng hơn để xử lý dữ liệu.
4. **Data Analyst**: Người khai thác dữ liệu, chủ yếu được cấp quyền chỉ đọc (Read-only) thông qua các công cụ truy vấn/BI.
5. **Workflow Role**: Role chuyên biệt dành cho các dịch vụ AWS ngầm (như Glue Crawlers, Glue Jobs) giả lập (assume role) để thay mặt hệ thống thực thi tác vụ trên Data Lake.
