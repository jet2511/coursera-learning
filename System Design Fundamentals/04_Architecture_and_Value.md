# System Design Fundamentals - Architecture and Value

## 📌 Tổng quan (Overview)
- **Khóa học**: System Design Fundamentals (Pearson / Coursera)
- **Chương**: What Not to Do
- **Bài học**: Architecture and Value (Kiến trúc và Giá trị)
- **Thời lượng**: 17 phút 41 giây
- **Diễn giả**: Juval Löwy

---

## 🔬 1. Định luật 1 Nhiệt động lực học & Sự vô nghĩa của Functional Decomposition

Juval Löwy chứng minh Functional Decomposition sai lầm bằng quy luật vật lý nguyên thủy mà không cần đến lập luận phần mềm nào:

- **Định luật 1 Nhiệt động lực học**: *"You cannot add value without sweating"* (Không thể tạo ra giá trị nếu không đổ mồ hôi).
- **Giá trị của Kiến trúc**: Kiến trúc phần mềm là hoạt động có **giá trị gia tăng cực kỳ cao** (high added value). Những quyết định kiến trúc ban đầu định hình toàn bộ hệ thống mãi mãi về sau. Sai lầm nhỏ ở kiến trúc dẫn đến thảm họa lớn ở tương lai.
- **Gian lận quy luật tự nhiên**: Khi nhìn spec ghi làm A, B, C và lập tức tạo ra block A, block B, block C $\rightarrow$ Bạn đang nghĩ *"No sweat"* (không cần tốn sức). Bạn đang cố gắng gian lận Định luật 1 Nhiệt động lực học để tạo ra giá trị mà không đổ mồ hôi. Về mặt bản chất của vũ trụ, điều này **không bao giờ hoạt động**.

---

## 🧪 2. Bản chất con người, Bữa ăn miễn phí & Giả kim thuật (Alchemy)

- **Sức hút của "Bữa ăn miễn phí" (The Free Lunch)**: Con người luôn khao khát tìm kiếm bữa ăn miễn phí. Hàng nghìn năm trước, những nhà trí thức vĩ đại nhất (như Isaac Newton) đã dành phần lớn đời mình cho Giả kim thuật (biến chì thành vàng). Dù thu được kết quả bằng 0, con người vẫn không ngừng thử.
- **Thực nghiệm Anti-Design (iDesign)**:
  - Chia team làm 2 phòng riêng biệt: 
    - Phòng 1: Thiết kế kiến trúc tốt nhất cho hệ thống thế hệ mới.
    - Phòng 2: Thiết kế kiến trúc **TỆ NHẤT** có thể (khó bảo trì, khó mở rộng nhất).
  - *Kết quả*: Sau một buổi chiều, kiến trúc của 2 phòng đưa ra **giống hệt nhau** (đều là Functional Decomposition, chỉ khác tên nhãn/label)! Điều này chứng minh thói quen thiết kế theo chức năng đã ăn sâu vào bản năng con người.

---

## 🏠 3. Thảm họa Domain Decomposition thông qua ví dụ Ngôi nhà

### A. Functional House (Ngôi nhà phân rã chức năng thuần túy)
- Spec yêu cầu Nấu ăn (Cooking) $\rightarrow$ Tạo block Nấu ăn: Đặt lò vi sóng giữa bãi đất trống, dựng giàn giáo giữ trên không, lợp mái che $\rightarrow$ Tuyên bố *"Sprint 1.0 Done: Nấu ăn đã xong!"*. Đây là sự dối trá vì không hề giải quyết được các kịch bản nấu ăn thực tế.

### B. Domain Decomposition (Nhà bếp, Phòng ngủ, Garage - Sự ngụy trang)
- Chia nhà thành Kitchen (nấu ăn), Bedroom (ngủ), Garage (đậu xe)... thực chất vẫn là **Functional Decomposition ngụy trang** (*"A rose by any other name is still a rose"*).

### C. Quy trình xây dựng thảm họa của Domain Decomposition:
1. Xây Nhà bếp (Milestone 1.0).
2. Xây thêm Phòng ngủ 1 (Milestone 2.0): Bắt buộc phải đập vữa, tháo dỡ móng, dùng kích thủy lực nâng Nhà bếp ra, đập móng cũ, đào móng mới to hơn, hạ Nhà bếp xuống móng mới, đập tường chạy lại điện nước...
3. **Hậu quả**: Việc thêm tính năng mới buộc phải đập đi xây lại tính năng cũ với chi phí đắt hơn gấp nhiều lần.
4. **Sự lặp lại chức năng giữa các Domain**: Khách dồn vào Nhà bếp $\rightarrow$ Nhà bếp phải gánh tính năng tiếp khách của Phòng khách. Ngủ gật trên sofa $\rightarrow$ Phòng khách gánh tính năng của Phòng ngủ. Dần dần mọi domain đều lặp lại chức năng của nhau.

---

## 🔄 4. Nghịch lý Nâng cấp Hệ thống cũ (Rebuilding Legacy System Paradox)

- **Lý do xây hệ thống mới**: Hệ thống cũ quá phức tạp, đã hết vòng đời (end of life), không thể bảo trì hay mở rộng.
- **Nghịch lý 1**: Tại sao lại để cùng những người đã làm hỏng hệ thống cũ đứng ra thiết kế hệ thống mới?
- **Nghịch lý 2 (No Business Value)**: Khi tách tính năng A sang hệ thống mới, bản thân A **không có giá trị kinh doanh độc lập** nếu thiếu B và C (Billing vô nghĩa nếu thiếu Invoicing và Shipping).
- **Thảm họa Phẫu thuật/Hòa giải (Reconciliation)**: Để A mới chạy được với B, C cũ, kỹ sư phải tiến hành "phẫu thuật" ghép nối với một hệ thống cũ đã bị xơ cứng (calcified). Độ phức tạp của việc ghép nối này lớn hơn rất nhiều so với việc viết mới A.

---

## 💡 5. Ngộ nhận về Unit Testing & Ngụ ngôn "Tìm chìa khóa dưới đèn đường"

### A. Bài học từ Máy bay Jumbo Jet
- Một chiếc Boeing 747 có hàng trăm nghìn linh kiện. Nếu từng linh kiện pass 100% Unit Test nhưng chưa bao giờ test tổng thể, **không ai dám lên máy bay đó**.
- **Lỗi hệ thống xuất hiện ở sự tương tác giữa các thành phần (Interaction between components)**, không nằm ở bản thân từng thành phần riêng lẻ (Ví dụ: Máy bay rẽ gắt $\rightarrow$ lực G tác động nhiên liệu $\rightarrow$ sụt áp ống dẫn $\rightarrow$ bọt khí $\rightarrow$ bỏng kim phun động cơ).

### B. Hệ thống không thể test (Untestable Systems)
- Loại kiểm thử thực sự có giá trị là **Regression Testing** (xem xét hệ thống toàn diện qua nhiều tầng tương tác).
- Trong hệ thống Phân rã theo chức năng, mọi thứ bị đấu nối chằng chịt, khiến hệ thống **không thể thực hiện Regression Testing**.
- Hệ thống không thể test $\rightarrow$ Tràn ngập lỗi (rife with defects).

### C. Bias "Tìm chìa khóa dưới đèn đường" (Searching under the Streetlight)
- Tại sao lập trình viên vẫn tập trung vào Unit Testing? Không phải vì nó giải quyết được kiến trúc, mà vì đó là **thứ duy nhất họ có thể làm** trong một hệ thống rối rắm.
- Giống như câu chuyện ngụ ngôn: Mất chìa khóa ở chỗ tối góc đường, nhưng lại đứng dưới cột đèn đường để tìm chỉ vì... *ở đây có ánh sáng*.

---

## 💡 Điểm đúc kết chính (Key Takeaways)

1. **Không có bữa ăn miễn phí**: Không thể tạo ra kiến trúc tốt bằng cách chia nhỏ spec một cách lười biếng.
2. **Domain Decomposition = Functional Decomposition ngụy trang**: Chia hệ thống theo các miền nghiệp vụ bề nổi (Kitchen, Bedroom / Billing, Shipping) vẫn dẫn đến thảm họa đập đi xây lại khi phát triển.
3. **Giá trị nằm ở sự tương tác**: Tính đúng đắn của hệ thống phụ thuộc vào sự tương tác giữa các component, không phải việc từng component pass Unit Test độc lập.
4. **Tránh bẫy "Đèn đường"**: Đừng chỉ tập trung viết Unit Test cho từng khối nhỏ rồi tin rằng hệ thống đã an toàn.
