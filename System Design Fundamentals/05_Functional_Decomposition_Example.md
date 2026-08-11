# System Design Fundamentals - Functional Decomposition Example

## 📌 Tổng quan (Overview)
- **Khóa học**: System Design Fundamentals (Pearson / Coursera)
- **Chương**: What Not to Do
- **Bài học**: Functional Decomposition Example (Ví dụ thực tế về thảm họa phân rã theo chức năng)
- **Thời lượng**: 11 phút 17 giây
- **Diễn giả**: Juval Löwy

---

## 📈 1. Bài toán: Hệ thống Giao dịch Cổ phiếu (Stock Trading System)

Juval Löwy đưa ra một bài toán kinh điển thường gặp trong các tài liệu và bài giảng kiến trúc:

### Yêu cầu bài toán (Requirement Spec):
1. **Trading**: Cho phép Trader thực hiện Mua (Buy) và Bán (Sell) cổ phiếu.
2. **Scheduling**: Cho phép lập lịch giao dịch (ví dụ: Mua cổ phiếu vào thứ Tư tuần sau).
3. **Reporting & Analysis**: Xuất báo cáo giao dịch và Phân tích hiệu quả giao dịch.
4. **Client**: Web Browser kết nối đồng bộ (connected session).
5. **Notification**: Gửi email xác nhận sau mỗi giao dịch/hoạt động.
6. **Persistence**: Lưu trữ toàn bộ dữ liệu vào Database local.

---

## 📐 2. Thiết kế ngây thơ (Naive Functional Decomposition)

Hầu hết các lập trình viên sẽ tạo ra một thiết kế "1-đối-1" trực tiếp từ spec:
- **Client (xanh lá)**: Web Browser.
- **Backend Services (vàng)**: Tạo từng khối tương ứng với từng dòng yêu cầu: `Buy`, `Sell`, `Schedule`, `Analyze`, `Report`.
- **Database**: Một cơ sở dữ liệu dùng chung phía dưới cho tất cả các khối.

> **Đánh giá của Juval Löwy**: Đây là một thiết kế **cực kỳ tồi tệ** nhưng 99% các kỹ sư phần mềm đều cho rằng nó hợp lý khi mới nhìn vào.

---

## 🕳️ 3. Phân tích 5 "Lỗ hổng" chí mạng của Thiết kế này

### 💣 Lỗ hổng 1: Logic nghiệp vụ bị đẩy hoàn toàn về phía Client
- **Kịch bản**: Trader muốn bán cổ phiếu A để lấy tiền mua cổ phiếu B.
- **Rủi ro**: Trong quá trình thực thi, giá A giảm và giá B tăng $\rightarrow$ Không đủ tiền mua B.
- **Xử lý ra sao?** Hủy lệnh? Mua một phần? Lấy tiền mặt dự phòng? Bán cổ phiếu C? Hỏi ý kiến người dùng?
- **Hậu quả**: Toàn bộ logic giải quyết tình huống này buộc phải nằm ở **Client**. 
- **Khi mở rộng Client**: Khi doanh nghiệp muốn thêm Mobile App, Desktop App, VR/HoloLens... mỗi Client mới buộc phải viết lại toàn bộ Business Logic đó. Chi phí nhân bản hệ thống và đội ngũ dev tăng gấp bội, cản trở sự phát triển của doanh nghiệp.

### 💣 Lỗ hổng 2: Sự thay đổi càn quét (Sweeping Expensive Changes)
- **Thay đổi Email $\rightarrow$ SMS**: Yêu cầu gửi email nằm rải rác ở tất cả các khối màu vàng. Khi muốn chuyển sang SMS, lập trình viên phải truy cập từng khối để sửa ("Not email, SMS").
- **Chuyển sang Cloud Database**:
  1. Phải sửa tất cả các khối từ Local DB sang Cloud DB.
  2. Cloud DB tính phí theo kết nối và lưu lượng $\rightarrow$ Phải chuyển kiểu gọi từ **Chatty** (nhiều cuộc gọi nhỏ) sang **Chubby** (gộp cuộc gọi lớn).
  3. Cloud DB dùng NoSQL/Document thay vì Relational DB $\rightarrow$ Phải viết lại hoàn toàn cấu trúc dữ liệu ở mọi khối.

### 💣 Lỗ hổng 3: Thảm họa Bất đồng bộ & Mất thứ tự thực thi (Async & Out-of-Order)
- **Vấn đề**: Giao dịch đồng bộ (Blocking UI) làm Trader bị chậm, giảm doanh thu $\rightarrow$ Trader đòi chuyển sang **Asynchronous (Async)**.
- **Thảm họa**: Khi chuyển sang Async, các cuộc gọi bị **mất thứ tự** (Lệnh Buy có thể đến trước lệnh Sell $\rightarrow$ Thất bại hoặc vi phạm pháp luật/Front-running).
- **Cách sửa chữa sai lầm**: Phải gắn tag thứ tự ($1/3, 2/3, 3/3$) và tạo bộ đệm (Buffer) ở Backend để sắp xếp lại cuộc gọi.
- **Hậu quả**: Các khối màu vàng bây giờ bị ép phải mang thêm logic quản lý thứ tự (sequencing), làm gia tăng sự phụ thuộc nội tại (coupling).

### 💣 Lỗ hổng 4: Nhân bản khối khi mở rộng Sản phẩm Tài chính (Financial Instruments)
- Danh mục đầu tư thực tế không chỉ có Cổ phiếu (Stocks), mà còn có Trái phiếu (Bonds), Ngoại tệ (Currencies), Hàng hóa (Commodities)...
- Quy trình mua/bán Trái phiếu hay Ngoại tệ hoàn toàn khác Cổ phiếu.
- Với thiết kế theo chức năng, mỗi khi thêm 1 loại tài sản mới $\rightarrow$ Hệ thống buộc phải nhân bản (duplicate) thêm hàng loạt khối `Buy Bond`, `Sell Bond`, `Buy Currency`... gây bùng nổ độ phức tạp.

### 💣 Lỗ hổng 5: Toàn cầu hóa & Tuân thủ Luật lệ Địa phương (Globalization & Compliance)
- Toàn cầu hóa không chỉ là dịch giao diện (Anh, Đức, Hàn).
- Luật giao dịch ở Wall Street (New York) khác City of London; California khác New York.
- Do logic bị bão hòa ở Client và luồng tương tác giữa các khối, mỗi thị trường mới đòi hỏi một **phiên bản hệ thống riêng biệt** (Version for NY, London, Singapore...). Doanh nghiệp hoàn toàn bị cản trở khi muốn mở rộng ra quốc tế.

---

## 💡 Điểm đúc kết chính (Key Takeaways)

1. **Thiết kế 1-đối-1 với Spec là bẫy chết người**: Tạo service theo từng gạch đầu dòng của tài liệu yêu cầu sẽ dẫn đến thảm họa bảo trì.
2. **Khả năng mở rộng Client bị phá hủy**: Nếu Client gánh Business Logic, bạn không thể thêm Mobile/Desktop App mà không nhân bản chi phí phát triển.
3. **Biến đổi hạ tầng (DB/Notification) trở thành thảm họa càn quét**: Khi không cô lập được biến động (Volatility), một thay đổi nhỏ ở DB/Email sẽ bắt toàn bộ hệ thống phải thay đổi theo.
4. **Không thể xử lý bất đồng bộ chuẩn mực**: Async trong hệ thống phân rã chức năng làm mất thứ tự thực thi, ép các dịch vụ phải tự gánh thêm logic sắp xếp phức tạp.
