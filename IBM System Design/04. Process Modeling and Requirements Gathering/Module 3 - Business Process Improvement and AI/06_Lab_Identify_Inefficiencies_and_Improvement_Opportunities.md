# Lab: Identify Inefficiencies and Improvement Opportunities in an Existing Process

## 1. Tổng quan bài thực hành (Lab Overview)
- **Mục tiêu thực hành:**
  - Phân tích quy trình hoàn trả hàng & hoàn tiền hiện tại (*As-Is Return & Refund workflow*) của một doanh nghiệp thương mại điện tử.
  - Nhận diện các điểm kém hiệu quả, lãng phí, độ trễ và khả năng xảy ra lỗi (*delays, waste, errors, rework, duplication*).
  - Đề xuất các giải pháp cải tiến quy trình (*improvement*), tối ưu hóa (*optimization*) và cơ hội tự động hóa (*automation*).
  - Đánh giá tác động của cải tiến lên sự hài lòng của khách hàng (*Customer*), chi phí vận hành (*Cost*), và chất lượng dịch vụ (*Quality*).

---

## 2. Phân tích hiện trạng quy trình (Process Narrative As-Is)

| Bước | Tác vụ | Bên phụ trách | Chi tiết thực hiện & Rủi ro tiềm ẩn |
| :---: | :--- | :--- | :--- |
| **1** | Nộp yêu cầu & biểu mẫu hoàn trả | Khách hàng | Khách phải tự tìm thông tin đơn hàng và **nhập thủ công** lý do trả hàng, thông tin liên hệ. *(Dễ sai sót, thiếu dữ liệu)* |
| **2** | Tạo nhãn vận chuyển | Hệ thống / Đơn vị vận chuyển | Hệ thống tạo nhãn; khách phải **tự tải, in ra giấy và dán thủ công** lên kiện hàng. *(Bất tiện nếu khách không có máy in)* |
| **3** | Gửi hàng về kho | Khách hàng / Đơn vị vận chuyển | Khách tự mang kiện hàng ra bưu cục hoặc đặt lịch hẹn lấy hàng. |
| **4** | Nhận kiện hàng tại kho | Nhân viên kho (Warehouse) | Nhân viên quét mã kiện hàng và **xếp vào khu vực lưu chờ (holding location)** để chờ kiểm định. *(Tạo độ trễ/chờ đợi)* |
| **5** | Kiểm định hàng & điều kiện hợp lệ | Nhân viên kho (Warehouse) | **Kiểm tra thủ công** tình trạng hàng, đối chiếu mã SKU với đơn hàng, so khớp chính sách hoàn trả. |
| **5A** | Không hợp lệ (*Not eligible*) | Nhân viên kho | Cập nhật trạng thái thủ công; bộ phận CSKH phải liên hệ báo khách $\rightarrow$ Kết thúc quy trình. |
| **5B** | Hợp lệ (*Eligible*) | Nhân viên kho | Cập nhật hồ sơ thủ công; chuyển hàng sang phân loại (nhập kho lại, tân trang hoặc tiêu hủy). |
| **6** | Cập nhật trạng thái hoàn trả | Nhân viên kho | **Nhập liệu thủ công lại (re-enters)** trạng thái vào hệ thống khác do **thiếu tích hợp giữa các nền tảng (lack of system integration)**. *(Lãng phí trùng lặp cực lớn, dễ sai số)* |
| **7** | Kế toán rà soát (*Finance review*) | Chuyên viên tài chính | **Rà soát thủ công** yêu cầu hoàn tiền và đối chiếu số tiền hoàn lại với lịch sử mua hàng ban đầu. |
| **8** | Phê duyệt (*Approval decision*) | Quản lý tài chính | Quản lý phê duyệt các khoản hoàn tiền $> \$100$, thường **thông qua trao đổi email thủ công**. *(Điểm nghẽn cổ chai - bottleneck)* |
| **9** | Thực hiện hoàn tiền | Bộ phận tài chính | Thao tác **hoàn tiền thủ công** trên cổng thanh toán (Payment Gateway) và xác nhận hoàn tất. |
| **10**| Thông báo cho khách hàng | Hệ thống / CSKH | Hệ thống kích hoạt thông báo cho khách; CSKH phải giải đáp các thắc mắc phát sinh. |

---

## 3. Bảng phân tích vấn đề & Cơ hội cải tiến (Findings & Improvement Opportunities)

| # | Cơ hội cải tiến (Opportunity for Improvement) | Phân loại lãng phí (Category) | Tác động tiềm năng (Potential Impact) | Giải pháp cụ thể (Solution / Type) |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **Bổ sung kiểm tra hợp lệ tự động ngay trên Form nộp đơn online** (Auto-fill thông tin từ mã đơn, kiểm tra thời hạn trả hàng theo chính sách trước khi cho nộp). | **Error / Rework** (Lỗi & Làm lại) | **Chất lượng & Chi phí:** Giảm chậm trễ do sửa lỗi thủ công; giảm đơn rác gửi về kho; tăng độ chính xác dữ liệu. | *Process Improvement / Validation Rules:* Khách không phải gõ lại thông tin; từ chối đơn không đủ điều kiện ngay từ đầu. |
| **2** | **Tích hợp hệ thống giữa Kho vận (WMS) và Phần mềm quản trị/Kế toán (ERP/Finance)**. | **Delay / Duplication / Error** (Trễ hạn, Trùng lặp, Sai số) | **Chi phí & Chất lượng:** Triệt tiêu hoàn toàn việc nhân viên kho phải nhập liệu lại 2 lần; giảm chi phí giờ công; giảm thiểu sai sót đối soát. | *System Integration & Automation:* Quét mã barcode tại kho tự động đồng bộ trạng thái sang hệ thống kế toán tức thì. |
| **3** | **Tự động hóa luồng phê duyệt hoàn tiền dưới ngưỡng (ví dụ: $< \$100$)**. | **Delay / Waste** (Chậm trễ, Lãng phí) | **Khách hàng & Chi phí:** Rút ngắn đáng kể thời gian chu kỳ hoàn tiền (Cycle Time); tăng mức độ hài lòng của khách; giải phóng thời gian cho Quản lý tài chính. | *Workflow Automation:* Các đơn hàng thỏa mãn điều kiện kho và $< \$100$ được hệ thống auto-trigger lệnh hoàn tiền qua cổng thanh toán. |
| **4** | **Cung cấp tính năng theo dõi trạng thái đổi trả theo thời gian thực (Real-time Status Tracking)**. | **Delay / Customer Confusion** (Mơ hồ, Chậm trễ) | **Khách hàng & Chi phí:** Giảm tải số lượng ticket/cuộc gọi hỏi CSKH *"Hàng của tôi đã đến đâu / Bao giờ tôi nhận được tiền?"*; tăng mức độ tin cậy và minh bạch. | *Customer Experience / Optimization:* Gửi link tra cứu trực quan và thông báo tự động (SMS/Push Notification) ở từng mốc (Đã nhận hàng $\rightarrow$ Đã kiểm định $\rightarrow$ Đã hoàn tiền). |
| **5** | **Điều phối nhân sự linh hoạt tại kho trong các đợt cao điểm (Peak Periods)**. | **Delay / Bottleneck** (Điểm nghẽn cổ chai) | **Khách hàng & Vận hành:** Rút ngắn thời gian chờ kiểm định hàng tại kho (*holding location*); đảm bảo cam kết SLA hoàn tiền cho khách. | *Process Optimization (Non-tech):* Dựa trên phân tích dữ liệu lịch sử để tăng ca hoặc bổ sung nhân viên thời vụ vào mùa mua sắm/hậu lễ Tết. |

---

## 4. Tổng kết & Bài học rút ra (Key Takeaways)

1. **Hiệu quả của việc kết hợp Sơ đồ (Process Map) & Bản tường giải (Process Narrative):**
   - Giúp soi rõ các "vùng mù" trong quy trình: nơi dữ liệu bị nhập lại thủ công, nơi tài liệu/kiện hàng bị nằm chờ, các điểm bàn giao (*handoffs*) giữa các phòng ban, và các nút thắt phê duyệt rườm rà (duyệt qua email).
2. **Cân đối giữa giải pháp Công nghệ & Phi công nghệ:**
   - Không phải cải tiến nào cũng đòi hỏi phần mềm đắt tiền. Ví dụ: **Cải tiến quy tắc biểu mẫu (Validation)** hay **Điều phối nhân sự theo mùa cao điểm** là các bước tối ưu hóa vận hành mang lại hiệu quả tức thì với chi phí thấp.
   - Các giải pháp **Tự động hóa (Automation)** và **Tích hợp hệ thống (Integration)** cần được triển khai khi quy trình nghiệp vụ đã được chuẩn hóa để loại bỏ triệt để lãng phí trùng lặp.
