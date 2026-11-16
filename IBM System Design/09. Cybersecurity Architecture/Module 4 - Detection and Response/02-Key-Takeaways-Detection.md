# Key Takeaways: Detection (Phát hiện)

## 1. Tổng quan về Bảo mật & Detection
- **CIA Triad**: Đại diện cho **"What"** (chúng ta đang cố gắng bảo vệ điều gì).
- **S = P + D + R (Security = Prevention + Detection + Response)**: Đại diện cho **"How"** (cách thức thực hiện bảo mật).
  - **Prevention (Phòng ngừa)**: Các domain như IAM, Endpoint Security, Application Security, Data Security cùng các kiểm soát (controls) đi kèm.
  - **Detection (Phát hiện)**: Thu thập thông tin từ tất cả các domain đưa vào monitoring engine, sau đó phân tích (analyzing), báo cáo (reporting) và săn tìm mối đe dọa (threat hunting).
- Hoạt động **Detection & Response** được thực hiện bởi đội ngũ **SOC (Security Operations Center)**.

---

## 2. Các công nghệ Detection chính

### A. SIEM (Security Information and Event Management)
**Tại sao cần SIEM?**
- Việc duy trì các console bảo mật riêng lẻ cho từng domain với chuyên gia phân tích riêng rất tốn kém và không có cái nhìn tổng thể nhất quán.
- Khi có sự cố, nhiều console cùng báo động dẫn đến nhiều người cùng xử lý một vấn đề (kém hiệu quả).

**Cách hoạt động của SIEM (thêm một lớp quản lý tập trung phía trên các console):**
1. **Collect (Thu thập)**: Gom logs, alarms, events, flow data từ các console của từng domain và lưu vào database.
2. **Correlate (Tương quan)**: Áp dụng phân tích để liên kết dữ liệu và thu gọn thành tập dữ liệu có thể quản lý được.
3. **Analyze (Phân tích)**:
   - Dùng rule có sẵn hoặc tùy chỉnh theo policy để phân mức độ ưu tiên thông báo/hành động: **High, Medium, Low**.
   - Tìm kiếm bất thường (anomalies) / Indicators of Compromise (IoCs) bằng **AI/ML** — công nghệ này gọi là **UBA (User Behavior Analytics)**.
4. **Report (Báo cáo)**: Xem báo cáo xu hướng để đánh giá hiệu quả của SOC (ví dụ: hiện tại có làm tốt hơn trước không, thời gian xử lý có nhanh hơn không).

### B. XDR (Extended Detection and Response)
- Phát triển từ **EDR** (cài agent trên từng hệ thống để phát hiện và phản ứng).
- XDR đọc và lưu giữ thông tin từ EDR hoặc SIEM, đồng thời hỗ trợ **Federated Search** để tìm kiếm IoC trên toàn bộ hệ thống.
- **Ưu điểm**: Không cần nạp sẵn (prefetch) toàn bộ dữ liệu vào database; lấy dữ liệu **just-in-time** (ngay tại thời điểm cần).

### C. Kết hợp SIEM và XDR
- **SIEM**: Tiếp cận theo hướng **bottom-up** (từ dưới lên), mạnh về kích hoạt cảnh báo (alarms).
- **XDR**: Tiếp cận theo hướng **top-down** (từ trên xuống).
- **Sức mạnh cộng hưởng**: Cảnh báo từ SIEM chuyển sang XDR là điểm khởi đầu lý tưởng cho quá trình điều tra. Kết hợp cả hai giúp giám sát, phân tích và báo cáo toàn diện hơn.

---

## 3. Threat Hunting (Săn tìm mối đe dọa)
- **Threat Hunting Timeline**:
  - **Reconnaissance**: Kẻ tấn công tìm kiếm điểm yếu/lỗ hổng.
  - **MTTI (Mean Time to Identify)**: Thời gian trung bình để tổ chức phát hiện ra cuộc tấn công (thường vào khoảng **200 ngày**).
  - **MTTC (Mean Time to Contain)**: Thời gian để khắc phục và phục hồi sau khi đã phát hiện tấn công.
- **Bản chất**: Là hoạt động **chủ động (proactive)** của tổ chức. Chuyên gia phân tích dựa trên kinh nghiệm và trực giác để đặt ra giả thuyết (hypothesis), từ đó xác định công cụ phù hợp nhằm phát hiện sớm mối đe dọa hoặc cuộc tấn công tiềm ẩn.
