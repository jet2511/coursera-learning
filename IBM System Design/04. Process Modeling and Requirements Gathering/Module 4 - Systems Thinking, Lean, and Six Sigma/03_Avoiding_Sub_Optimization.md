# Avoiding Sub-Optimization

## 1. Khái niệm cốt lõi (Core Concept)
- **Định nghĩa Sub-Optimization (Tối ưu hóa cục bộ):** Tình trạng cải tiến hiệu năng của một phòng ban/bộ phận đơn lẻ nhưng lại làm suy giảm hiệu năng chung của toàn hệ thống.
- **Ẩn dụ Chạy tiếp sức (Relay Race):** Một vận động viên bứt tốc thật nhanh nhưng làm rơi gậy hoặc chuyền gậy ẩu, kết quả là cả đội thua cuộc.
- **Tối ưu hóa thực sự (Real Optimization):** Cân bằng dòng chảy toàn chuỗi. Toàn bộ tổ chức vận hành tốt hơn ngay cả khi một số mắt xích hoạt động dưới công suất tối đa của cá nhân chúng.

---

## 2. Bốn nguyên nhân gây Sub-Optimization

1. **Siloed Performance Measures:** Thưởng phạt theo KPI cục bộ của từng team thay vì kết quả đầu ra chung.
2. **Short-Term Focus:** Chạy theo chỉ số trước mắt có thể nhìn thấy ngay thay vì sự phát triển bền vững.
3. **Lack of Process Visibility:** Nhân sự không nhìn thấy công việc của mình tác động thế nào tới mắt xích kế tiếp.
4. **Misaligned Priorities:** Mục tiêu nội bộ phòng ban xung đột với mục tiêu khách hàng hoặc toàn doanh nghiệp.

---

## 3. So sánh 2 kịch bản thực tế (Warehouse Case Study)

| Khía cạnh | Kịch bản 1: Cải tiến cục bộ (Sub-Optimization) | Kịch bản 2: Tiếp cận toàn hệ thống (Optimization) |
| :--- | :--- | :--- |
| **Mục tiêu đặt ra** | Tăng số đơn nhặt/giờ trong kho (Picking speed) | Giảm tổng thời gian chu kỳ (Total cycle time) & tỷ lệ lỗi |
| **Hành động** | Thưởng tiền theo sản lượng nhặt hàng/giờ | Dùng Value Stream Map; chuẩn hóa bàn giao (handoffs); thêm kiểm soát chất lượng |
| **Kết quả cục bộ** | Năng suất nhặt hàng tăng 25% | Năng suất nhặt tăng khiêm tốn 10% |
| **Hậu quả hệ thống** | Bỏ qua bước kiểm tra kép, dán nhãn sai; khu đóng hàng quá tải, trả hàng tăng vọt; CSAT tụt dốc thảm hại | Tổng cycle time giảm 20%; tỷ lệ lỗi giảm 60%; CSAT tăng vọt |

---

## 4. Ba câu hỏi phản biện & Công cụ trực quan hóa

### 3 Câu hỏi lãnh đạo cần đặt ra trước mọi đề xuất cải tiến:
1. **Upstream & Downstream:** Thay đổi này tác động thế nào đến quy trình đầu nguồn (trước) và hạ nguồn (sau)?
2. **System-Level Measures:** Thước đo cấp hệ thống nào (CSAT, Lead Time, Defect Rate) sẽ chứng minh thành công chung?
3. **Cross-Team Alignment:** Các đội ngũ liên quan đã đồng thuận về thời gian, nguồn lực và kết quả kỳ vọng chưa?

### Công cụ trực quan hỗ trợ:
- **SIPOC** (Suppliers, Inputs, Process, Outputs, Customers): Nhìn rõ ranh giới đầu vào/đầu ra tổng thể.
- **Value Stream Mapping (VSM) & Process Maps:** Bộc lộ rõ các điểm bàn giao (handoffs) và hiệu ứng gợn sóng (ripple effects) trước khi bấm nút triển khai.
