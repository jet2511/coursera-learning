# Module 4: Data processing and analytics

## Bài học: Data Transformation

### 1. Vấn đề thực tế: Non-uniform Data (Dữ liệu không đồng nhất)
Khi thu thập dữ liệu từ nhiều nguồn khác nhau vào Data Lake, dữ liệu thô (raw data) thường gặp các vấn đề lớn về tính nhất quán:
- **Định dạng ngày tháng khác nhau**: Khách hàng châu Âu dùng định dạng `dd/mm/yyyy`, trong khi Mỹ dùng `mm/dd/yyyy`.
- **Định dạng số điện thoại**: Nơi có dấu gạch ngang, mã vùng; nơi chỉ là chuỗi số liền.
- **Mã bưu chính (Postal code)**: Một số quốc gia dùng ký tự chữ lẫn số, một số chỉ dùng số.

> **Thực tế vận hành:** Kỹ sư xây dựng và vận hành Data Lake dành gần **80% thời gian** cho việc thu thập, làm sạch (cleaning) và tổ chức (organizing) dữ liệu.

---

### 2. Giải pháp cốt lõi: AWS Glue
**AWS Glue** là dịch vụ ETL (Extract, Transform, Load) được quản lý hoàn toàn (fully managed / serverless):
- Tiếp nhận dữ liệu thô (raw, unorganized data) từ các nguồn.
- Thực hiện xử lý, chuẩn hóa dữ liệu.
- Ghi dữ liệu đã làm sạch vào S3 bucket đích (clean data bucket) để phục vụ cho các tác vụ phân tích và trực quan hóa dữ liệu (visualization) sau này.

---

### 3. Case Study: Tuân thủ quyền riêng tư & Bảo mật dữ liệu (Data Privacy & Compliance)
- **Yêu cầu bảo mật/pháp lý**: Tùy theo quy định từng quốc gia, một số thông tin nhạy cảm (PII) phải được làm mờ hoặc ẩn trước khi lưu trữ/phân tích.
- **Trước khi có AWS Glue**: Việc can thiệp mã hóa thủ công (ví dụ ẩn 3 số cuối của IP address) rất phức tạp và tốn công sức.
- **Với AWS Glue ETL Jobs**:
  - Dễ dàng tạo các job để tự động lọc, làm sạch dữ liệu.
  - Hỗ trợ masking/loại bỏ các trường nhạy cảm như họ tên (`last name`), một phần email (`email masking`), hoặc mã số thuế (`TaxID`).

---

### 4. Giới thiệu AWS Glue DataBrew
- **Bản chất**: Giải pháp xử lý/biến đổi dữ liệu dạng giao diện trực quan trực tiếp (visual, point-and-click tool) cho các ETL jobs mà không cần viết code.
- **Tính năng nổi bật**:
  - Tích hợp sẵn hơn **250 phép biến đổi dựng sẵn (prebuilt transformations)** giúp việc làm sạch dữ liệu diễn ra nhanh chóng.
  - Hoàn toàn **Serverless**: Tự động co giãn theo dung lượng dữ liệu, không cần quản lý hạ tầng hay máy chủ.
