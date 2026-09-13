# Data Lake Storage (Lưu trữ trong Data Lake)

## 1. Vai trò trọng tâm của Amazon S3
Amazon S3 được xem là "trung tâm (core reservoir)" của mọi kiến trúc Data Lake trên AWS nhờ vào:
- **Massive Scalability**: Khả năng mở rộng quy mô lưu trữ đến mức Exabyte mà không cần lo hạ tầng.
- **Data Durability**: Độ bền dữ liệu 11 số 9 (99.999999999%) thông qua việc nhân bản dữ liệu tự động giữa nhiều Availability Zones trong 1 Region (hoặc liên Region).
- **Cost Optimization**: Đa dạng các tầng lưu trữ (Storage Tiers / Classes) giúp tối ưu chi phí theo tần suất truy cập.
- **Strong Read-after-Write Consistency**: Tính nhất quán dữ liệu ngay sau khi ghi.
- **Data Agnostic**: Lưu trữ mọi loại dữ liệu (video, text logs, IoT sensor, JSON/CSV, binary, hình ảnh y tế,...).

---

## 2. Nguyên lý cốt lõi: Tách biệt Storage và Compute (Decoupling Storage & Compute)
- **Truyền thống**: Storage và Compute đi liền (ví dụ server vật lý, cụm Hadoop cục bộ) $\rightarrow$ muốn tăng dung lượng đĩa phải mua thêm server có CPU/RAM, gây lãng phí.
- **Data Lake hiện đại**:
  - **Storage (Amazon S3)**: Chỉ tập trung lưu trữ an toàn, mở rộng độc lập.
  - **Compute (Athena, EMR, Glue, Redshift Spectrum)**: Khởi tạo theo nhu cầu (on-demand), mở rộng độc lập theo tải xử lý rồi tắt khi xong.

---

## 3. Các tầng dữ liệu trong Data Lake (Data Evolution Tiers)
Dữ liệu di chuyển qua các tầng để tăng dần giá trị (từ "kim cương thô" đến "kim cương đã cắt gọt"):

| Tầng Dữ Liệu (Data Tier) | Đặc điểm | Đối tượng sử dụng chính |
| :--- | :--- | :--- |
| **Raw Data** | Dữ liệu gốc, nguyên bản, chưa qua biến đổi (logs, raw sensor, json stream). | Infra Engineers, Data Admins |
| **Formatted Data** | Dữ liệu đã được tối ưu hóa cấu trúc (được xếp theo cột/index) phục vụ khám phá, nghiên cứu. | Data Engineers, Data Scientists |
| **Transformed Data** | Dữ liệu đã làm sạch, xử lý và áp dụng các quy tắc nghiệp vụ (business rules). | Data Analysts, BI Engineers |
| **Published Data** | Tập dữ liệu được kiểm soát chặt chẽ (governed), chuẩn hóa hoàn toàn, sẵn sàng kết nối BI/Dashboard. | Business Users, Executives |

---

## 4. Tối ưu chi phí lưu trữ với S3 Lifecycle & Glacier
- **S3 Storage Class Analysis**: Phân tích pattern truy cập dữ liệu theo thời gian thực tế.
- **S3 Lifecycle Rules**: Tự động chuyển dịch các dữ liệu ít truy cập dần xuống các tầng giá rẻ hơn:
  - `S3 Standard` $\rightarrow$ `S3 Standard-IA / One Zone-IA` $\rightarrow$ `S3 Glacier Flexible / Glacier Deep Archive` (chi phí cực thấp cho mục đích lưu trữ lâu dài).
