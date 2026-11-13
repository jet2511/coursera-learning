# Role Play: Cost Analysis in Order Fulfillment & AR Collections

## 1. Mục tiêu & Bối cảnh thảo luận
- **Vai trò tham gia:** Chuyên viên phân tích chi phí / BA thảo luận cùng **Casey Rivera** (Senior Finance Manager).
- **Trọng tâm nghiệp vụ:** Áp dụng phương pháp **Activity-Based Costing (ABC)** vào quy trình thu hồi công nợ phải thu (**AR - Accounts Receivable Collections**) trong chuỗi hoàn tất đơn hàng.
- **Bài toán cốt lõi:** Kế toán truyền thống phân bổ chi phí chung (overhead) cào bằng, làm che khuất **chi phí phục vụ thực tế (true cost-to-serve)**; dẫn đến việc không nhìn thấy một số nhóm khách hàng nợ hoặc các hành vi đòi nợ tiêu tốn quá nhiều nguồn lực, trực tiếp bào mòn biên lợi nhuận.

---

## 2. Khung phân tích 5 bước ABC cho AR Collections

### Bước 1: Xác định vấn đề cốt lõi (Problem Statement)
- Thiếu tính minh bạch về *true cost-to-serve*.
- Việc cào bằng chi phí gián tiếp khiến ban lãnh đạo ngộ nhận rằng mọi nỗ lực đòi nợ đều mang lại lợi nhuận, trong khi thực tế có những phân khúc nợ mà chi phí bỏ ra để đòi cao hơn số tiền thu hồi được.

### Bước 2: Nhận diện 4 Hoạt động tiêu tốn tài nguyên nhất (Primary Activities)
1. **Manual follow-ups:** Gọi điện nhắc nợ thủ công liên tục, soạn email cá nhân hóa, xử lý leo thang nhắc nợ.
2. **Invoice dispute resolution:** Điều tra các tranh chấp về hóa đơn, sai lệch số liệu công nợ, chứng từ giao hàng.
3. **Complex payment matching & bank reconciliation:** Đối soát ngân hàng thủ công, khớp các khoản thanh toán gộp hoặc thiếu mã tham chiếu.
4. **Legal & external collections coordination:** Phối hợp với văn phòng luật hoặc thuê agency thu nợ bên ngoài cho các hồ sơ nợ xấu, rủi ro cao.

### Bước 3: Xác định Yếu tố thúc đẩy chi phí (Cost Drivers)
Để phân bổ chi phí chuẩn xác vào từng hoạt động:

| Hoạt động (Activity) | Yếu tố thúc đẩy chi phí (Cost Driver) |
| :--- | :--- |
| **Manual follow-ups** | Số lượng cuộc gọi/email nhắc nợ + Giờ công thực tế của nhân viên. |
| **Dispute resolution** | Số lượng tranh chấp phát sinh + Thời gian xử lý điều tra mỗi vụ việc. |
| **Payment reconciliation** | Số lượng giao dịch đối soát thủ công + Số dòng lệnh (line items) không khớp. |
| **Legal & agency collections** | Số lượng tài khoản nợ chuyển sang luật sư/agency + Tỷ lệ % phí dịch vụ agency thu. |

### Bước 4: Khung phân tích Chi phí vs. Giá trị (Cost-versus-Value Framework)
Xây dựng quy trình 3 giai đoạn đánh giá tính hợp lý của nguồn lực:
1. **Measure Value Realized (Đo lường giá trị thực thu):**
   - Lượng tiền mặt thu hồi được ($\text{Cash Collected}$).
   - Nợ khó đòi tránh được việc phải trích lập xóa sổ ($\text{Avoided Bad Debt Write-offs}$).
   - Chi phí vốn lưu động tiết kiệm được nhờ hạ chỉ số ngày thu tiền bình quân ($\text{Reduced DSO - Days Sales Outstanding}$).
2. **Segment-Level Net ROI (Đo ROI ròng theo phân khúc):**
   - Đối chiếu tổng chi phí ABC với số tiền thu hồi theo từng nhóm tuổi nợ (Aging buckets: 30-60-90+ ngày) và quy mô tài khoản:
   $$\text{Net Value} = \text{Cash Collected} - \text{Total Collection Cost}$$
3. **Strategic Thresholds (Thiết lập ngưỡng can thiệp chiến lược):**
   - Xác định rõ các **phân khúc có ROI âm (Negative-ROI segments)**: Nơi chi phí đòi nợ vượt quá giá trị nợ có thể thu hồi.
   - Kích hoạt quy tắc tự động hóa (Automated workflows), điều chỉnh chính sách tín dụng, hoặc xóa nợ sớm (early write-off) thay vì tiếp tục cử nhân sự theo đuổi tốn kém.

### Bước 5: Báo cáo & Đề xuất hành động cho CFO (Executive Narrative)
Truyền thông 4 thông điệp then chốt phục vụ ra quyết định:
- **1. Aggregate Net ROI:** Tỷ lệ hoàn vốn tổng thể trên mỗi đồng chi phí bỏ ra (*Ví dụ: Thu hồi được \$X tiền mặt trên mỗi \$1 chi phí đòi nợ*).
- **2. Negative-ROI Leakages:** Chỉ rõ các điểm "rò rỉ" ngân sách (ví dụ: các khoản nợ lẻ, nợ quá hạn $>90$ ngày chi phí đòi nợ lớn hơn gốc nợ).
- **3. Working Capital Impact:** Định lượng chính xác dòng tiền vốn lưu động được giải phóng nhờ rút ngắn DSO và giảm nợ xấu.
- **4. Actionable Next Steps:** Chuyển các tài khoản nợ nhỏ/ít rủi ro sang luồng tự động hóa nhắc nợ (dunning automation); dồn nhân sự chuyên môn giỏi xử lý các khoản nợ lớn có tranh chấp phức tạp.

---

## 3. Bài học rút ra (Key Takeaways)
1. **Dữ liệu ABC biến đổi chiến lược vận hành:** Chuyển đổi từ cách đòi nợ cảm tính/cào bằng sang chiến lược phân tầng thông minh dựa trên ROI ròng (*Net ROI*).
2. **Không phải mọi khoản nợ đều đáng để đòi thủ công:** Tự động hóa phân khúc giá trị thấp và tập trung nguồn lực cao cấp vào các tài khoản tạo giá trị cao giúp bảo vệ biên lợi nhuận của doanh nghiệp.
