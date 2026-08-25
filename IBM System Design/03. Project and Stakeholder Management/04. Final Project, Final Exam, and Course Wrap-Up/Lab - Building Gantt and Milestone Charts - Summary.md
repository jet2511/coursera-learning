# Tóm tắt Lab: Xây dựng Gantt Chart & Milestone Chart (Dự án Cập nhật SOP Quản lý Kho hàng)

Tài liệu này ghi lại chi tiết đề bài, kịch bản, các bước thực hành và nguyên tắc xây dựng biểu đồ Gantt & Milestone cho dự án **"SOP Update for Inventory Management"**.

---

## 1. Kịch bản dự án (Scenario)
- **Mục tiêu:** Phòng Quản lý Kho hàng (Inventory Management Department) cập nhật quy trình thao tác chuẩn (SOPs) nhằm nâng cao tính chính xác, hiệu quả và tuân thủ.
- **Thời lượng:** Diễn ra trong 4 quý (**Q1 – Q4**).
- **Thời điểm hiện tại (Today's Date / Current Status):** **Cuối Quý 2 (End of Q2)**.

### Danh mục 5 hoạt động chính:

| # | Hoạt động (Activity) | Mô tả chi tiết | Thời gian thực hiện (Duration) |
| :-: | :--- | :--- | :---: |
| **1** | **Review Current SOPs** | Thu thập tất cả quy trình hiện có, xác định các bước lỗi thời / thừa thãi. | **Q1** |
| **2** | **Conduct Process Mapping Workshops** | Phối hợp với nhân sự kho (warehouse), mua hàng (purchasing), vận hành (operations) để vẽ lại luồng công việc hiện tại. | **Q1 – Q2** |
| **3** | **Draft Updated SOPs** | Viết và gửi tài liệu quy trình cập nhật để lấy ý kiến phản hồi (phụ thuộc vào Hoạt động 2). | **Q2 – Q3** |
| **4** | **Train Staff on New Procedures** | Xây dựng tài liệu đào tạo và tổ chức các buổi đào tạo cho nhân sự. | **Q3** |
| **5** | **Implement and Monitor Compliance** | Triển khai áp dụng SOPs mới và giám sát tuân thủ để đảm bảo tính nhất quán. | **Q4** |

---

## 2. Hướng dẫn thiết lập biểu đồ (Step-by-Step)

### A. Gantt Chart
1. **Lập danh sách đầu việc & Trục thời gian:** Đưa 5 hoạt động lên trục dọc; trục ngang chia theo 4 quý `Q1`, `Q2`, `Q3`, `Q4`.
2. **Xác định thời lượng & Mối phụ thuộc (Dependencies):**
   - Hoạt động 1 chạy trong Q1.
   - Hoạt động 2 chạy song song từ Q1 kéo dài hết Q2.
   - Hoạt động 3 bắt đầu từ Q2 (sau khi có kết quả workshop) kéo dài đến Q3.
   - Hoạt động 4 diễn ra trong Q3.
   - Hoạt động 5 triển khai trong Q4.
3. **Mã màu & Đường mốc thời gian (Color-coding & Today's Line):**
   - Kẻ một **đường thẳng đứng (Vertical Line)** tại mốc **Cuối Q2** biểu thị thời điểm hiện tại.
   - **Completed (Đã xong):** Hoạt động 1 (Q1), Hoạt động 2 (Q1-Q2).
   - **In-Progress (Đang thực hiện):** Hoạt động 3 (đoạn trong Q2).
   - **Planned / Pending (Kế hoạch sắp tới):** Phần còn lại của Hoạt động 3 (Q3), Hoạt động 4 (Q3), Hoạt động 5 (Q4).

---

### B. Milestone Chart
1. **Xác định các mốc then chốt (Key Milestones):** Rút ra từ kết quả đầu ra của từng hoạt động:
   - *Mốc 1 (Cuối Q1):* Current SOPs Review Completed.
   - *Mốc 2 (Cuối Q2):* Process Mapping Workshops Completed.
   - *Mốc 3 (Cuối Q3):* Updated SOPs Drafted & Approved.
   - *Mốc 4 (Cuối Q3):* Staff Training Completed.
   - *Mốc 5 (Cuối Q4):* SOP Implementation & Compliance Monitored.
2. **Ký hiệu & Trạng thái (tại thời điểm cuối Q2):**
   - Sử dụng biểu tượng **hình thoi (Diamonds)**.
   - **Mốc đã hoàn thành (Xanh đậm / Completed):** Mốc 1 (Cuối Q1) và Mốc 2 (Cuối Q2).
   - **Mốc tương lai / Chưa hoàn thành (Xám / Planned):** Mốc 3, 4 (Cuối Q3) và Mốc 5 (Cuối Q4).
   - Đường kẻ dọc mốc thời gian hiện tại nằm ở ranh giới giữa Q2 và Q3.

---

## 3. Tài nguyên tham khảo
- **File mẫu thực hành:** [Project Tools_Spreadsheet.xlsx](https://project-stakeholder-requirements-management-fundamentals-6c8e81.gitlab.io/labs/Project%20Tools_Spreadsheet.xlsx)
- **File bài giải mẫu (Instructor Solution):** [Project Tools_Solution.xlsx](https://project-stakeholder-requirements-management-fundamentals-6c8e81.gitlab.io/labs/Project%20Tools_Solution.xlsx)
