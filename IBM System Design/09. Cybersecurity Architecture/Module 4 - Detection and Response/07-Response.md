# Response (Phản ứng sự cố)

## 1. Tổng quan về Security Response
- Trong công thức **S = P + D + R**, **Response** là bước xử lý sau khi đã phát hiện sự cố.
- **MTTI (Mean-Time-to-Identify)**: Trung bình khoảng **200 ngày** (theo Ponemon Institute) từ khi kẻ tấn công xâm nhập đến khi tổ chức phát hiện.
- **MTTC (Mean-Time-to-Contain)**: Trung bình khoảng **70 ngày** để kiểm soát thiệt hại, đẩy kẻ tấn công ra ngoài và khôi phục hoạt động.
- Đội ngũ **SOC (Security Operations Center)** chịu trách nhiệm giám sát, phát hiện và phản ứng.
- **Incident Response (IR)** truyền thống thường mang tính thủ công, phụ thuộc vào kinh nghiệm cá nhân ("heroes and experts"), khó mở rộng và khó lặp lại:
  1. **Triage (Phân loại ưu tiên)**: Xác định cảnh báo là tấn công thật hay nhiễu, mức độ nghiêm trọng để xử lý theo thứ tự ưu tiên.
  2. **Remediation (Khắc phục)**: Chặn đứng, tắt hệ thống, vá lỗi, thiết lập kiểm soát để ngừng rò rỉ dữ liệu và khôi phục hệ thống.

---

## 2. SOAR (Security, Orchestration, Automation, and Response)
SOAR là cách tiếp cận hiện đại nhằm tự động hóa tối đa quy trình phản ứng để rút ngắn MTTC.

### Quy trình xử lý Case & Điều tra trong SOAR
1. **Tạo & Làm giàu Case (Case Creation & Enrichment)**:
   - Khi SIEM/XDR phát hiện vấn đề, hệ thống tự động mở một **Case** trong **Case Management** của SOAR.
   - Tự động đính kèm **artifacts, IoCs** và thông tin hữu ích để chuyên gia phân tích không phải bắt đầu từ con số 0.
   - Dashboard giúp theo dõi case đang mở, mức độ ưu tiên, người phụ trách và điều phối lại khi cần.
2. **Dynamic Playbooks (Kịch bản động)**:
   - Hướng dẫn chuyên gia điều tra một cách nhất quán và có thể lặp lại (đặc biệt hữu ích cho người ít kinh nghiệm).
   - Khác với SOP tĩnh (chạy cứng nhắc từ bước 1 đến 10), Dynamic Playbook rẽ nhánh linh hoạt dựa trên kết quả của từng bước/script trước đó để tìm ra nguyên nhân gốc rễ và bước khắc phục.

### Automation vs. Orchestration
- **Automation (Tự động hóa hoàn toàn)**: Chỉ áp dụng được cho những kịch bản đã từng thấy trước đó.
- **Thách thức**: Trong bảo mật thường có các sự kiện hiếm gặp (**Black Swan events**) hoặc chưa từng xảy ra (**First-of-a-kind events**), buộc phải xử lý thủ công.
- **Orchestration (Điều phối - Bán tự động)**: Nằm giữa thủ công và tự động hoàn toàn. Con người đóng vai trò như "nhạc trưởng" (conductor), bấm nút điều phối các quy trình/công cụ tự động chạy theo từng bước.

---

## 3. Breach Notification (Thông báo vi phạm dữ liệu)
Khi dữ liệu nhạy cảm bị rò rỉ, tổ chức có trách nhiệm pháp lý phải thông báo:
- **Cần xác định**:
  1. **Loại dữ liệu bị xâm phạm** (tên, SSN, số thẻ tín dụng, ID...).
  2. **Vị trí địa lý** của những người bị ảnh hưởng (quốc gia, bang/khu vực).
- **Quy định pháp lý**: Mỗi quốc gia/bang có luật riêng. Ví dụ: **GDPR (EU)** phạt rất nặng nếu không báo cáo kịp thời — lên tới **4% doanh thu toàn cầu** hoặc **20 triệu Euro** (tùy mức nào lớn hơn), áp dụng cho bất kỳ tổ chức nào nắm giữ dữ liệu công dân EU.
- **Giải pháp**: Sử dụng công cụ hỗ trợ (nhập loại dữ liệu, địa lý, quy định liên quan) để xác định chính xác **ai cần được thông báo**, tránh rủi ro bị phạt nặng.
