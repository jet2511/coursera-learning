# Key Takeaways: Response (Phản ứng sự cố)

## 1. Attack to Recovery Timeline (Dòng thời gian từ tấn công đến phục hồi)
- **Reconnaissance (Thăm dò)**: Kẻ tấn công dành thời gian tìm kiếm điểm yếu hoặc lỗ hổng bảo mật.
- **MTTI (Mean Time to Identify)**: Thời gian để tổ chức phát hiện ra cuộc tấn công (khoảng **200 ngày**).
  - Cần dịch chuyển thời điểm nhận biết cuộc tấn công sớm hơn thông qua **Threat Hunting**.
- **MTTC (Mean Time to Contain)**: Thời gian để xử lý, ngăn chặn và phục hồi sau khi phát hiện tấn công (khoảng **70 ngày**).

---

## 2. Phản ứng với cuộc tấn công (Responding to an Attack)
- Một quy trình **Incident Response (IR)** tốt giúp giảm thiểu đáng kể chi phí do vi phạm dữ liệu (data breach).
- **Truyền thống**: Cuộc tấn công được gọi là "incident" và phản ứng là "IR". Thường do các chuyên gia xử lý thủ công qua hai bước:
  - **Triage (Phân loại ưu tiên)**
  - **Remediate (Khắc phục sự cố)**
- **Hiện đại**: Rút ngắn MTTC bằng công nghệ **SOAR (Security Orchestration, Automation, and Response)** nhằm tự động hóa tối đa quy trình IR.

---

## 3. Quy trình xử lý Case
1. **Khởi tạo**: Khi cuộc tấn công kích hoạt cảnh báo, **SIEM** hoặc **XDR** sẽ tạo một Case trong thành phần Case Management của **SOAR**.
2. **Gán việc**: Phân công Case cho chuyên gia phân tích bảo mật (cybersecurity analyst) phù hợp.
3. **Điều tra với Dynamic Playbook**:
   - Sử dụng **Dynamic Playbook** để đảm bảo quy trình điều tra nhất quán và có thể lặp lại.
   - Dynamic Playbook cung cấp các bước dựa trên thuật toán/kết quả thực tế để dẫn dắt chuyên gia thực hiện điều tra.
4. **Khắc phục**: Khi xác định được nguyên nhân và các bước khắc phục, tiến hành áp dụng hành động sửa chữa/bảo vệ hệ thống.

---

## 4. Automation vs. Orchestration
- Tự động hóa rất tốt nhưng không thể tự động hóa tất cả vì có nhiều sự kiện xuất hiện lần đầu (**FOAK - First-of-a-Kind events**).
- **Nguyên tắc**: 
  - **Automate what you can** (Tự động hóa những gì có thể).
  - **Orchestrate wherever automation is not possible** (Điều phối/bán tự động ở những nơi không thể tự động hóa hoàn toàn).

---

## 5. Breach Notification (Thông báo vi phạm dữ liệu)
Khi xảy ra sự cố rò rỉ/vi phạm dữ liệu, bắt buộc phải:
1. Xác định tập dữ liệu bị ảnh hưởng (**Impacted data sets**).
2. Xác định vị trí địa lý nơi dữ liệu bị xâm phạm (**Geographic location**).
3. Thông báo cho cơ quan quản lý tại địa phương/khu vực đó (**Inform the regulatory body**).
> [!IMPORTANT]
> Tổ chức sẽ phải chịu các khoản phạt tài chính rất nặng (ví dụ GDPR) nếu không thông báo kịp thời cho cơ quan quản lý có thẩm quyền.
