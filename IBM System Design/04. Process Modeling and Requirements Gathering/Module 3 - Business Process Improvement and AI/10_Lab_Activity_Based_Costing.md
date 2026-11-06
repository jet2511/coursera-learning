# Lab: Activity Based Costing & ROI Calculation

## 1. Mục tiêu bài thực hành (Learning Objectives)
- Áp dụng công thức ROI cơ bản để đánh giá tính hiệu quả chi phí của quy trình hoàn tất đơn hàng (*Order Fulfillment Process*).
- Định lượng tác động tài chính của chi phí hoàn trả hàng (*Customer Returns*) lên toàn bộ lợi nhuận doanh nghiệp theo phương pháp Activity Based Costing (ABC).
- Phân tích sự sụt giảm ROI để nhận diện các điểm yếu trong vận hành và đề xuất giải pháp cắt giảm lãng phí.

---

## 2. Kịch bản bài toán (Scenario: Precision Auto Supply)
- **Doanh nghiệp:** Nhà phân phối phụ tùng ô tô khu vực (*Precision Auto Supply*).
- **Tổng doanh thu tháng từ các đơn hàng hoàn tất:** **\$90,000**
- **Chi phí các hoạt động trong quy trình xử lý đơn hàng (As-Is Fulfillment):**

| Hoạt động quy trình (Process Activity) | Mô tả chi tiết | Chi phí hàng tháng (\$) |
| :--- | :--- | :---: |
| **Receive & Enter Orders** | Tiếp nhận đơn qua điện thoại/online, xác thực thông tin | \$15,000 |
| **Pick Parts** | Tìm kiếm và lấy linh kiện tại kho | \$20,000 |
| **Pack & Ship Orders** | Đóng gói kiện hàng, dán nhãn và gửi hàng | \$20,000 |
| **Admin & Systems Support** | Hạ tầng IT, giám sát, chi phí quản lý chung | \$5,000 |
| **Tổng chi phí quy trình gốc (Original Process Cost)** | | **\$60,000** |

- **Dữ liệu phát sinh về đổi trả hàng (Cost of Returns):**
  - Số lượng đơn trả về trong tháng: **300 đơn**
  - Chi phí bình quân xử lý một đơn trả hàng (nhân công, nhập lại kho, chứng từ, vận chuyển): **\$50 / đơn**

---

## 3. Các bước tính toán chi tiết (Step-by-Step Calculations)

### Bước 1: Tính ROI trước khi tính chi phí đổi trả (ROI Before Returns)
$$\text{ROI}_{\text{before}} = \frac{\text{Revenue} - \text{Total Cost}}{\text{Total Cost}} = \frac{90,000 - 60,000}{60,000} = \frac{30,000}{60,000} = 0.50 = \mathbf{50\%}$$

### Bước 2: Tính tổng chi phí phát sinh do đổi trả (Total Return Cost)
$$\text{Total Return Cost} = \text{Số lượng đơn trả} \times \text{Chi phí mỗi đơn} = 300 \times 50 = \mathbf{\$15,000}$$

### Bước 3: Tính tổng chi phí mới sau khi cộng chi phí trả hàng (New Total Cost)
$$\text{New Total Cost} = \text{Original Cost} + \text{Total Return Cost} = 60,000 + 15,000 = \mathbf{\$75,000}$$

### Bước 4: Tính ROI thực tế sau khi tính chi phí trả hàng (ROI After Returns)
$$\text{ROI}_{\text{after}} = \frac{\text{Revenue} - \text{New Total Cost}}{\text{New Total Cost}} = \frac{90,000 - 75,000}{75,000} = \frac{15,000}{75,000} = 0.20 = \mathbf{20\%}$$

---

## 4. Bảng đối chiếu & Phân tích tác động tài chính

| Chỉ số | Trước khi tính Trả hàng | Sau khi tính Trả hàng (ABC) | Mức độ suy giảm |
| :--- | :---: | :---: | :---: |
| **Tổng chi phí (Total Cost)** | \$60,000 | **\$75,000** | Tăng +25.0% (+\$15,000) |
| **Lợi nhuận ròng (Net Profit)** | \$30,000 | **\$15,000** | Giảm một nửa (-50.0%) |
| **Tỷ suất sinh lời (ROI)** | **50%** | **20%** | **Tụt dốc 30 điểm phần trăm** |

### Ý nghĩa kinh tế:
- Chi phí đổi trả hàng (\$15,000) đã "ăn mòn" chính xác **50% lợi nhuận dự kiến** ban đầu của công ty (\$15,000 / \$30,000).
- Nếu chỉ nhìn vào báo cáo thực hiện đơn hàng thông thường (bỏ qua chi phí đổi trả), ban quản lý sẽ đánh giá sai lệch rất lớn về mức độ hiệu quả của chuỗi cung ứng.

---

## 5. Đề xuất giải pháp cải tiến giảm chi phí (Reflection & Action Plan)

Để bảo vệ biên lợi nhuận và kéo ROI trở lại mức cao, doanh nghiệp cần tập trung vào các giải pháp giảm tỷ lệ đổi trả:
1. **Nâng cao độ chính xác khi nhặt hàng tại kho (Improve Picking Accuracy):**
   - Áp dụng máy quét mã vạch (Barcode Scanner) cầm tay hoặc công nghệ Pick-to-Light trong bước *Pick Parts* (\$20,000) để đảm bảo lấy đúng phụ tùng, đúng thông số đời xe, loại trừ lỗi nhặt nhầm phụ tùng.
2. **Chuẩn hóa thông tin sản phẩm trên kênh đặt hàng (Better Product Information):**
   - Bổ sung tài liệu tương thích chi tiết (Part compatibility guides) và hình ảnh rõ ràng trên cổng đặt hàng online để khách/nhân viên tổng đài không đặt sai linh kiện ngay từ bước *Receive & Enter Orders*.
3. **Chuẩn hóa & Rà soát chính sách đổi trả (Return Policy Refinement):**
   - Thiết lập quy định rõ ràng về phí lưu kho đối với các lỗi do khách tự đặt nhầm, đồng thời yêu cầu cung cấp số VIN xe trước khi chốt đơn.
