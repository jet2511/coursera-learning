# Creating Process Maps and Flowcharts

## 1. Khái niệm cốt lõi & Thuật ngữ
- **Process Map (Bản đồ quy trình):** Biểu diễn trực quan chuỗi các bước và luồng thông tin/tác vụ giữa các bên liên quan từ đầu đến cuối.
- **Flowchart (Lưu đồ quy trình):** Một dạng *Process Map* cụ thể dùng hệ thống ký hiệu chuẩn hóa để biểu diễn hành động và điểm quyết định.
- **Thuật ngữ & Từ viết tắt cần nhớ:**
  - **BA (Business Analyst - Chuyên viên phân tích nghiệp vụ):** Người làm rõ yêu cầu, phân tích quy trình để đề xuất giải pháp cải tiến.
  - **PM (Project Manager - Quản lý dự án):** Sử dụng sơ đồ để phân chia công việc, trách nhiệm và kiểm soát tiến độ.
  - **CSR (Customer Service Representative - Đại diện dịch vụ khách hàng):** Nhân viên tuyến đầu tiếp nhận và xử lý khiếu nại.
  - **As-Is Process:** Quy trình hiện trạng đang vận hành (dùng để tìm lỗi/bottleneck).
  - **To-Be Process:** Quy trình mục tiêu/tương lai sau khi đã tối ưu hóa.
  - **Bottleneck (Điểm nghẽn):** Điểm tắc nghẽn làm chậm toàn bộ tiến độ luồng công việc.
  - **Redundancy (Sự dư thừa):** Các bước/tác vụ lặp thừa, không tạo ra giá trị gia tăng.
  - **QA (Quality Assurance - Đảm bảo chất lượng):** Giám sát quy trình đảm bảo đạt chuẩn chất lượng.

---

## 2. Ký hiệu chuẩn hóa (Flowchart Symbols)

| Ký hiệu | Hình dạng | Ý nghĩa / Ứng dụng |
| :--- | :--- | :--- |
| **Start / End** | Bầu dục (Oval) / Bo góc | Điểm bắt đầu hoặc kết thúc quy trình |
| **Process / Action** | Chữ nhật (Rectangle) | Bước xử lý hoặc hành động cụ thể |
| **Decision** | Hình thoi (Diamond) | Điểm rẽ nhánh điều kiện (Yes/No, Đạt/Không đạt) |
| **Input / Output** | Hình bình hành (Parallelogram) | Thao tác nhập dữ liệu hoặc xuất kết quả |
| **Flow Line** | Mũi tên (Arrows) | Hướng luồng di chuyển của tác vụ/thông tin |

---

## 3. Case Studies tóm lược
- **Xử lý khiếu nại khách hàng:** Khách gửi khiếu nại (`Start`) $\rightarrow$ CSR tiếp nhận (`Process`) $\rightarrow$ Hợp lệ? (`Decision`):
  - *Không:* Báo khách $\rightarrow$ `End`.
  - *Có:* Điều tra $\rightarrow$ Xử lý giải pháp $\rightarrow$ Báo kết quả $\rightarrow$ `End`.
- **Duyệt báo cáo chi phí:** Nộp báo cáo (`Start`) $\rightarrow$ Đủ chứng từ? (`Decision`):
  - *Chưa:* Trả lại bổ sung $\rightarrow$ nộp lại.
  - *Đủ:* Quản lý duyệt? (`Decision`): Duyệt $\rightarrow$ Kế toán chi trả $\rightarrow$ `End`; Từ chối $\rightarrow$ Thông báo $\rightarrow$ `End`.

---

## 4. Giá trị với BA & 5 Nguyên tắc thiết kế
- **Giá trị:** Tài liệu hóa *As-Is* để tìm bottleneck/lãng phí; thiết kế *To-Be*; làm tài liệu đào tạo (onboarding); công cụ trực quan để thống nhất yêu cầu với Stakeholder.
- **5 Nguyên tắc vàng:**
  1. **Keep it simple:** Trực quan, dễ đọc, tránh chi tiết thừa.
  2. **Use standard symbols:** Luôn dùng đúng chuẩn ký hiệu.
  3. **Consistent:** Thống nhất format và cách đặt tên bước (Động từ + Danh từ).
  4. **Engage stakeholders:** Lôi kéo đúng người thực thi tham gia đóng góp.
  5. **Update regularly:** Cập nhật liên tục theo thay đổi thực tế.
