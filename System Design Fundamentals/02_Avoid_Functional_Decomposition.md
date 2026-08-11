# System Design Fundamentals - Avoid Functional Decomposition

## 📌 Tổng quan (Overview)
- **Khóa học**: System Design Fundamentals (Pearson / Coursera)
- **Chương**: What Not to Do
- **Bài học**: Avoid Functional Decomposition (Né tránh phân rã theo chức năng)
- **Thời lượng**: 7 phút 40 giây
- **Diễn giả**: Juval Löwy

---

## 🛑 1. Phân rã theo chức năng (Functional Decomposition) là gì?

- **Kiến trúc là hành vi phân rã (Act of Decomposition)**: Chia một ý tưởng lớn thành các khối xây dựng nhỏ hơn (components, modules, services, classes).
- **Functional Decomposition**: Thực hiện phân rã hệ thống dựa trực tiếp vào danh sách chức năng/yêu cầu (requirement spec). 
  - *Ví dụ*: Spec yêu cầu hệ thống làm A, B, C (như Billing, Shipping, Invoicing) $\rightarrow$ Tạo ra Block A, Block B, Block C.
- **Cảnh báo cốt lõi của Juval Löwy**:
  > *"If that is your architecture, the project has already failed in past tense. The project is already dead before anybody wrote the first line of code."*  
  > *(Nếu đó là kiến trúc của bạn, dự án đã thất bại ở thì quá khứ. Dự án đã chết trước khi có ai viết dòng code đầu tiên.)*

---

## 🔨 2. Các "cây đinh đóng vào quan tài" của Functional Decomposition

Dù rất đơn giản, dễ hiểu và được áp dụng phổ biến, Functional Decomposition mang lại những thảm họa kiến trúc nghiêm trọng:

### 📌 Đinh 1: Phân rã theo chức năng luôn là Phân rã theo Thời gian (Time Decomposition)
- Khi chia hệ thống thành A, B, C, bản chất là làm A $\rightarrow$ rồi đến B $\rightarrow$ rồi đến C.
- Khái niệm về B đã bị ràng buộc cứng (tightly coupled) là **diễn ra sau A và trước C**.
- **Không thể tái sử dụng (No Reuse)**: Khi muốn đem B sang một hệ thống khác, bạn không thể nhấc riêng B đi được vì B bị kéo theo A và C.
- **Hậu quả**: Dẫn đến sự lặp lại tính năng khủng khiếp giữa các hệ thống (enormous duplication), mọi người luôn phải "chế tạo lại bánh xe bò" (reinventing the wheel).

### 📌 Đinh 2: Thảm họa về Độ phức tạp (Integration Cost vs. Internal Complexity)
Một hệ thống thực tế có thể chứa hàng trăm chức năng (ví dụ 300 chức năng). Phân rã theo chức năng sẽ dẫn đến 1 trong 2 cực đoan:
1. **Explosion of Components (Bùng nổ linh kiện nhỏ)**: Tạo ra 300 khối nhỏ. Mỗi khối tuy đơn giản nhưng chi phí tích hợp (integration cost) giữa 300 khối này tăng theo tỷ lệ phi tuyến tính (non-linear cost).
2. **God Service / Monolith of Doom (Dịch vụ phình to)**: Gom nhóm các chức năng lại thành vài dịch vụ khổng lồ. Chi phí tích hợp giảm nhưng độ phức tạp nội tại (internal complexity) cực kỳ thảm hại.

### 📌 Đinh 3: Ô nhiễm Logic Nghiệp vụ vào Client (Client Pollution)
- Khi các khối A, B, C bị tách rời theo chức năng, **Client buộc phải đảm nhận vai trò điều phối** (sequencing): Gọi A $\rightarrow$ Gọi B $\rightarrow$ Nếu B lỗi thì rollback A ra sao...
- Nguyên tắc kinh điển: *"Không được đưa Business Logic vào Client"*. Nhưng Functional Decomposition **bắt buộc** lập trình viên phải vi phạm nguyên tắc này. Khi quy trình nghiệp vụ thay đổi, Client buộc phải thay đổi theo.

### 📌 Đinh 4: Tối đa hóa các Điểm truy cập (Maximizing Points of Entry)
- Client phải ra/vào hệ thống tại nhiều điểm khác nhau (vào A rồi ra, vào B rồi ra, vào C rồi ra).
- Thiết kế tốt cần tối thiểu hóa điểm truy cập (lý tưởng nhất là single point of entry). 
- Việc có quá nhiều điểm truy cập làm gia tăng độ phức tạp khi xử lý: **Security, Scalability, Availability, Responsiveness, Performance**.

---

## 📉 3. Ví dụ thực tế: Thẩm định hệ thống 8 chữ số (Eight-Zero Due Diligence)

- **Ngữ cảnh**: Juval Löwy thực hiện thẩm định kiến trúc (due diligence) cho một thương vụ M&A giá trị 8 chữ số (hàng chục triệu USD).
- **Phương pháp**: Phân tích độ phức tạp theo chu kỳ (Cyclomatic Complexity Analysis).
- **Phát hiện**:
  - **`MainForm`**: Vốn chỉ nên là một giao diện UI đơn giản (pretty face), nhưng lại bị biến thành toàn bộ hệ thống, chứa đựng lượng Business Logic khổng lồ và độ phức tạp cực cao.
  - **`FormSetup`**: Phải sinh ra chỉ để giúp khởi tạo cái "quái vật" `MainForm`.
  - **`Resources`**: Chỉ là danh sách string/image nhưng có độ phức tạp cao bất thường do sự phình to của `MainForm`.
  - **Xung quanh**: Bùng nổ hàng loạt khối nhỏ phân rã theo chức năng.
- **Kết luận**: Dự án phải chịu cả 2 thảm họa cùng lúc: Thành phần phình to quái vật + hàng loạt khối nhỏ chi phí tích hợp cao.

---

## 💡 Điểm đúc kết chính (Key Takeaways)

1. **Đừng thiết kế dựa trên Feature/Function Spec**: Đừng tạo ra service/component chỉ vì tài liệu spec ghi "Hệ thống cần làm tính năng X".
2. **Tránh Coupling theo Thời gian**: Tránh việc các component phụ thuộc lẫn nhau theo thứ tự thực thi A $\rightarrow$ B $\rightarrow$ C.
3. **Giữ Client đơn giản**: Không để Client gánh trách nhiệm điều phối chuỗi thực thi nghiệp vụ.
4. **Tối thiểu hóa điểm truy cập**: Giảm số lượng entry points để kiểm soát tốt Security, Performance và Scalability.
