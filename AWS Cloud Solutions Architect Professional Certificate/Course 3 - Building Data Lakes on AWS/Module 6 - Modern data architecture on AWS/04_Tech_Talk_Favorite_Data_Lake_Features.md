# Tech Talk: What's Your Favorite Data Lake Feature?

**Khóa học:** Course 3 - Building Data Lakes on AWS  
**Module:** Module 6 - Modern data architecture on AWS  
**Chủ đề:** Tech Talk - Thảo luận kỹ thuật giữa Raph Lopez & Alex về các tính năng / dịch vụ dữ liệu yêu thích nhất

---

## 1. Lựa chọn của Alex: Amazon QuickSight & Tự phục vụ Dữ liệu (Self-Service Data Presentation)

* **Vấn đề thực tế (Pain Point):**
  * Trong vai trò System Administrator trước đây, Alex thường xuyên bị quá tải khi đồng nghiệp gửi các file CSV khổng lồ vào phút chót ("chiều thứ 6 lúc 7 giờ tối") và nhờ dựng biểu đồ, làm pivot tables để thuyết trình.
  * Nhóm kỹ thuật trở thành "điểm nghẽn" (bottleneck) vì phải làm thủ công các báo cáo cho các phòng ban khác.
* **Giải pháp với Amazon QuickSight:**
  * **Tăng tốc năng suất (Productivity Boost):** Tạo biểu đồ, dashboard trực quan đẹp mắt và chuyên nghiệp một cách nhanh chóng để phục vụ các cuộc họp nhóm và thuyết trình cấp công ty.
  * **Trao quyền cho người dùng cuối (Self-Service Empowerment):** Cho phép các phòng ban nghiệp vụ tự do khám phá và tạo biểu đồ của riêng họ mà không cần phụ thuộc vào IT/Data Team.
  * **Hình thành "Data Product":** Dữ liệu được đóng gói thành sản phẩm trực quan, người dùng có thể tự tiêu thụ và ra quyết định.

---

## 2. Lựa chọn của Raph: Định dạng Dữ liệu dạng Cột (Columnar Data Formats & Apache Parquet)

* **Bản chất kỹ thuật (Cơ chế I/O ở tầng lưu trữ):**
  * **Định dạng theo hàng (Row-based: CSV, JSON):** Dữ liệu của từng bản ghi được lưu tuần tự trên đĩa. Khi thực hiện truy vấn lọc hoặc tính toán trên một vài cột, hệ thống vẫn phải đọc toàn bộ các hàng qua đầu đọc ổ đĩa $\rightarrow$ phát sinh lượng I/O khổng lồ và xử lý ghép bảng tốn kém.
  * **Định dạng theo cột (Columnar: Apache Parquet, ORC):** Dữ liệu được nhóm và lưu trữ theo từng cột riêng biệt. Hệ thống chỉ cần đọc đúng các cột được yêu cầu trong câu lệnh `SELECT`.

* **Cơ chế tối ưu hóa vượt trội của Apache Parquet:**
  1. **Block Metadata (First & Last record per block):**
     * Trong mỗi data block, Parquet lưu trữ giá trị đầu tiên và giá trị cuối cùng (Min/Max statistics).
  2. **Predicate Pushdown & Sort Optimization:**
     * Nếu dữ liệu được sắp xếp (*sorted*) theo một cột (ví dụ cột `name`), khi truy vấn `WHERE name = 'Alex'`, công cụ truy vấn (Athena, EMR, Redshift) chỉ cần kiểm tra metadata của từng block để biết block nào chứa dải giá trị từ 'A' đến 'F'.
     * Bỏ qua hoàn toàn các block không liên quan mà không cần quét đĩa (*intelligent skipping / predicate pushdown*).
  3. **Tiết kiệm chi phí & Tăng tốc độ truy vấn:**
     * Truy vấn chạy nhanh hơn gấp nhiều lần và giảm chi phí truy vấn trực tiếp (đặc biệt với các dịch vụ tính tiền theo dung lượng quét như **Amazon Athena** hoặc **Athena Federated Queries** qua môi trường mạng).
* **Ví dụ thực tế:**
  * Bộ dữ liệu nổi tiếng **NYC Taxi & Limousine Commission**: Ban đầu được công bố dưới dạng CSV, nhưng hiện nay đã được hiện đại hóa hoàn toàn sang định dạng **Parquet** để tối ưu hóa việc phân tích dữ liệu lớn trên toàn cầu.

---

## 3. Tổng kết & Mối liên hệ với Data Lake hiện đại

| Khía cạnh | Amazon QuickSight (Alex) | Columnar Data Formats / Parquet (Raph) |
| :--- | :--- | :--- |
| **Vị trí trong kiến trúc** | Tầng hiển thị, phân tích BI & người dùng cuối (Consumption Layer) | Tầng lưu trữ, cấu trúc file & I/O tối ưu (Storage & Format Layer) |
| **Giá trị mang lại** | Xóa bỏ "điểm nghẽn" IT, tự phục vụ (Self-service), tạo Data Product | Giảm dung lượng quét I/O, tăng tốc truy vấn, tiết kiệm chi phí |
| **Vai trò cốt lõi** | Biến dữ liệu thô thành thông tin hành động (*Actionable Insights*) | Nền tảng hiệu năng cho các engine truy vấn (Athena, EMR, Redshift) |
