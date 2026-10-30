# Lab: Analyze Business Needs and Gaps in a Business Solution

Tóm tắt đề bài lab và giải pháp mẫu chuẩn BA cho case study bán lẻ trực tuyến **Cright Cart**.

---

## 1. Bối cảnh tình huống (Scenario)
- **Doanh nghiệp:** Cright Cart — nhà bán lẻ thương mại điện tử chuyên đồ gia dụng và phong cách sống, cam kết giá rẻ và giao nhanh (3–5 ngày làm việc).
- **Vấn đề phát sinh (Pain Points):**
  1. Điểm hài lòng khách hàng (CSAT) sụt giảm mạnh.
  2. Khách hàng phàn nàn đơn hàng giao trễ hơn cam kết 3–5 ngày.
  3. Bộ phận CSKH (Customer Service) quá tải vì các cuộc gọi thắc mắc về mã vận đơn / tracking bị thiếu hoặc chậm cập nhật.
  4. Đội ngũ kho (Warehouse) phản ánh thông tin đơn hàng bị thiếu hoặc truyền đến chậm, đặc biệt vào giờ cao điểm.
  5. Bộ phận Tài chính (Finance) phát hiện sai lệch (discrepancies) giữa số lượng đơn hàng xác nhận và các khoản thanh toán thực tế đã xử lý.
- **Yêu cầu từ Ban lãnh đạo:** Trước khi quyết định đầu tư hệ thống mới tốn kém, Process Owner / BA cần mô tả chi tiết quy trình xử lý đơn hàng hiện tại (**Current Order Fulfilment Process - As-Is**) từ lúc khách đặt hàng đến khi kiện hàng được xuất kho, chỉ ra các điểm nghẽn và khoảng trống dữ liệu.

---

## 2. Lời giải mẫu chi tiết (Sample Solution)

### Phần 1: Mục đích phân tích (Define the Purpose)
- **Mục tiêu:** Mô tả và trực quan hóa quy trình xử lý đơn hàng hiện tại (End-to-End Fulfilment Process) từ lúc đặt hàng trên website đến khi hàng rời khỏi kho.
- **Kỳ vọng đạt được:**
  - Xác định chính xác các điểm nghẽn (bottlenecks), độ trễ (latency), và lỗ hổng truyền thông/dữ liệu giữa các hệ thống (Web $\to$ Payment Gateway $\to$ ERP/Warehouse $\to$ Logistics).
  - Làm rõ nguyên nhân gốc rễ gây ra chậm trễ giao hàng, sai lệch thanh toán và thiếu tracking.
  - Cung cấp cơ sở thực tế (evidence-based) để ban lãnh đạo đưa ra quyết định cải tiến có mục tiêu thay vì đầu tư hệ thống dàn trải.

---

### Phần 2: Trình tự các bước & Phân định vai trò (Sequence of Steps & Key Roles)

#### A. Các vai trò & Hệ thống tham gia (Key Roles & Systems):
1. **Customer (Khách hàng):** Duyệt web, chọn sản phẩm, thanh toán và chờ nhận hàng.
2. **E-Commerce Web Platform (Hệ thống Web/Frontend):** Tiếp nhận giỏ hàng, hiển thị form thanh toán.
3. **Payment Gateway (Cổng thanh toán) / Finance:** Xử lý trừ tiền, ghi nhận doanh thu và đối soát thanh toán.
4. **Order Management System (OMS) / Inventory Management:** Quản lý tồn kho, phân bổ đơn hàng.
5. **Warehouse Team (Đội ngũ Kho bãi):** Lấy hàng (picking), đóng gói (packing), dán nhãn vận đơn.
6. **Logistics / Carrier (Đơn vị vận chuyển):** Nhận kiện hàng, cập nhật mã vận đơn (tracking number) và vận chuyển tới khách hàng.
7. **Customer Service (CSKH):** Hỗ trợ khách hàng tra cứu trạng thái đơn.

#### B. Trình tự các bước thực hiện (Current Workflow):
1. **Bước 1 (Đặt hàng):** Khách hàng chọn mặt hàng vào giỏ và nhấn thanh toán trên website.
2. **Bước 2 (Xử lý thanh toán):** Cổng thanh toán xử lý giao dịch; website hiển thị thông báo "Đặt hàng thành công".
3. **Bước 3 (Đồng bộ thông tin):** Đơn hàng được đẩy từ hệ thống web sang phần mềm kho/OMS (hiện tại có dấu hiệu bị trễ theo batch vào giờ cao điểm).
4. **Bước 4 (Đối soát Tài chính):** Phòng Tài chính ghi nhận doanh thu (thực tế kiểm tra thủ công, dẫn đến sai lệch với đơn đã chốt).
5. **Bước 5 (Nhận đơn tại kho):** Đội ngũ kho in phiếu lấy hàng (pick list) dựa trên dữ liệu nhận được.
6. **Bước 6 (Nhặt & Đóng gói hàng):** Nhân viên kho nhặt hàng từ kệ, kiểm tra và đóng thùng.
7. **Bước 7 (Tạo vận đơn & Bàn giao):** Đơn vị vận chuyển tiếp nhận kiện hàng, tạo mã tracking (hiện tại mã tracking bị chậm cập nhật ngược lại về hệ thống CSKH/Web).
8. **Bước 8 (Xuất kho & Giao hàng):** Kiện hàng bắt đầu hành trình vận chuyển đến tay khách hàng.

---

### Phần 3: Nhận diện rủi ro/tắc nghẽn & Giải pháp cải tiến (Potential Issues & One Improvement)

#### Các điểm nghẽn & Rủi ro tiềm ẩn (Potential Issues):
- **Giao tiếp bất đồng bộ & Nghẽn dữ liệu (Peak Hour Bottlenecks):** Việc truyền dữ liệu từ Web sang Warehouse xử lý theo batch hoặc hệ thống quá tải vào giờ cao điểm làm đơn hàng tới kho muộn vài tiếng đến cả ngày.
- **Rủi ro đối soát tài chính (Payment Reconciliation Gaps):** Việc trừ tiền và xác nhận đơn không atomic/đồng bộ theo thời gian thực khiến khách tưởng đơn đã thành công nhưng thanh toán bị fail hoặc pending, tạo ra chênh lệch dữ liệu giữa Web và Kế toán.
- **Lỗ hổng cập nhật Tracking (Missing Tracking Updates):** Thiếu tích hợp API 2 chiều tự động (Webhook) giữa hệ thống đối tác vận chuyển và nền tảng của Cright Cart. Thông tin tracking phụ thuộc vào cập nhật thủ công/chậm trễ, khiến CSKH không có dữ liệu trả lời khách.

#### Đề xuất một giải pháp cải tiến cốt lõi (One Key Improvement):
- **Tích hợp API thời gian thực & Tự động hóa luồng thông tin (Real-time Event-Driven Integration):**
  - Thay thế cơ chế truyền file/batch trễ bằng kiến trúc Webhook/Event-driven: Ngay khi thanh toán được Gateway xác nhận thành công, đơn hàng lập tức bắn sang hệ thống kho theo thời gian thực (real-time).
  - Tích hợp trực tiếp API với hãng vận chuyển: Khi kho quét mã vạch đóng gói, hệ thống tự động sinh tracking code và gửi ngay email/SMS cho khách hàng, đồng thời đồng bộ thẳng vào màn hình tra cứu của CSKH.

---

### Phần 4: Đúc kết bài học & Suy ngẫm (Reflection)
- **Giá trị của việc viết quy trình ra từng bước:**
  - Giúp phát hiện ra những "khoảng trống vô hình" (invisible gaps) nằm ở các điểm bàn giao (handoffs) giữa các phòng ban và hệ thống mà nếu chỉ nói chuyện miệng sẽ không ai nhận ra.
  - Phân định rõ ranh giới trách nhiệm (ownership) của từng vai trò, tránh tình trạng đổ lỗi chéo khi có sự cố.
  - Là bước nền tảng sống còn trước khi vẽ biểu đồ (BPMN/Flowchart), giúp BA có tư duy cấu trúc, lập luận chặt chẽ và tập trung vào giải quyết vấn đề gốc rễ thay vì chữa cháy triệu chứng.
