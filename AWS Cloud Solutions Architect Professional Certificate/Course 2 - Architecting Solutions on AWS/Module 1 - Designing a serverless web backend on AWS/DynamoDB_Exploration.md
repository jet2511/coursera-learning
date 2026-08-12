# Tóm tắt bài học: Thực hành khám phá DynamoDB (DynamoDB Exploration)

**Khóa học:** Course 2 - Architecting Solutions on AWS  
**Chủ đề:** Cách tạo bảng, thiết lập khóa, chọn chế độ dung lượng, chỉ mục phụ, mã hóa và bật tính năng Streams trên DynamoDB Console  
**Vị trí:** Module 1 - Designing a serverless web backend on AWS

---

## 1. Khái niệm cơ bản về bảng trong DynamoDB
* **Bảng độc lập (Standalone Tables):** Trong DynamoDB, các bảng hoạt động độc lập và không nằm chung dưới một thực thể Database (như trong SQL). Không có liên kết khóa ngoại (Foreign Keys) hay truy vấn kết hợp bảng (SQL Joins) mặc định giữa các bảng.
* **Items (Mục dữ liệu):** Tương đương với các hàng (*rows*) trong cơ sở dữ liệu quan hệ.
* **Attributes (Thuộc tính):** Tương đương với các cột (*columns*).

---

## 2. Thiết lập Khóa chính & Chỉ mục

### 2.1. Khóa chính (Primary Key)
* **Partition Key (Khóa phân vùng):** Là bắt buộc, dùng để băm dữ liệu và phân phối đều trên các phân vùng vật lý bên dưới.
* **Sort Key (Khóa sắp xếp - Tùy chọn):** Dùng để sắp xếp các Item có cùng Partition Key. Khi kết hợp: **Partition Key + Sort Key = Unique Key** (Khóa phức hợp duy nhất).
* *Ví dụ trong bài học:* Tạo bảng tên `example-table`, đặt Partition Key là `userid`.

### 2.2. Lập chỉ mục phụ (Secondary Indexes)
* Gồm hai loại: **Local Secondary Index (LSI)** và **Global Secondary Index (GSI)**.
* **Mục đích:** Cho phép truy vấn nhanh dữ liệu dựa trên các thuộc tính không phải là khóa chính mà không cần thực hiện quét toàn bộ bảng (**Scan**).
* **Scan vs Query:** Hành động *Scan* phải quét qua toàn bộ Item của bảng để lọc dữ liệu, gây ra độ trễ (latency) lớn và tốn chi phí. Việc *Query* dựa trên khóa chính hoặc Index mang lại hiệu năng cao và độ trễ thấp hơn nhiều.

---

## 3. Các cấu hình quan trọng khác

### 3.1. Chế độ dung lượng (Capacity Modes)
* **Provisioned Mode (Dự phòng trước):** Tự cấu hình trước số lượng đơn vị dung lượng đọc/viết (RCU/WCU). Phù hợp với lưu lượng tải ổn định, dễ dự đoán.
* **On-demand Mode (Theo yêu cầu):** Tự động co giãn hiệu năng theo tải thực tế. Khách hàng chỉ trả tiền cho các yêu cầu đọc/ghi thực tế phát sinh. Phù hợp cho tải trồi sụt đột biến (*spiky demand*).
* **Table Classes:**
  * *DynamoDB Standard:* Lớp bảng thông thường cho mọi tác vụ truy cập thường xuyên.
  * *DynamoDB Standard-IA (Infrequent Access):* Phù hợp để lưu trữ dữ liệu ít truy cập với chi phí lưu kho thấp hơn.

### 3.2. Mã hóa dữ liệu lưu trữ (Encryption at rest)
Sử dụng **AWS Key Management Service (KMS)** để mã hóa. Ba tùy chọn khóa:
1. *Owned by Amazon DynamoDB:* Khóa mặc định do DynamoDB sở hữu và tự động quản lý.
2. *AWS managed key:* Khóa được tạo trong tài khoản AWS của bạn và do AWS KMS quản lý.
3. *Customer managed key:* Khóa do khách hàng tự tạo và quản lý quyền truy cập.

### 3.3. Giám sát (Monitoring)
Tích hợp trực tiếp với **Amazon CloudWatch** để hiển thị các biểu đồ:
* Lượng tài nguyên đọc/ghi thực tế đã tiêu thụ.
* Độ trễ của các truy vấn và quét bảng.

### 3.4. DynamoDB Streams (Luồng thay đổi dữ liệu)
* Ghi nhận và đẩy mọi thay đổi của dữ liệu (Create, Update, Delete) trên bảng vào một luồng dữ liệu thời gian thực.
* Cho phép các ứng dụng khác (như AWS Lambda) bắt lấy sự kiện để xử lý tiếp (ví dụ: đồng bộ dữ liệu hoặc gửi email thông báo).
* *Tùy chọn ghi nhận:* Key attributes only, Old image (dữ liệu cũ), New image (dữ liệu mới sau khi sửa - được chọn trong bài học), hoặc cả Old & New images.

### 3.5. Global Tables (Bảng toàn cầu)
* Hỗ trợ tự động nhân bản (replicate) dữ liệu sang các AWS Region khác nhau trên toàn cầu, giúp đồng bộ hóa dữ liệu thời gian thực và giảm thiểu độ trễ truy xuất đối với người dùng ở các khu vực địa lý khác nhau.
