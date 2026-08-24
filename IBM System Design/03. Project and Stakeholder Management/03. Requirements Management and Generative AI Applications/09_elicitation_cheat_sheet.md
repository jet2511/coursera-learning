# Elicitation Cheat Sheet (Ma trận Khơi gợi Yêu cầu chuẩn BABOK)

## 1. Mục đích & Giá trị của Cheat Sheet
- Cung cấp khung tra cứu nhanh (**Quick Reference**) cho quy trình khơi gợi yêu cầu 5 bước chuẩn **BABOK® Guide**.
- Phân định rõ ràng trách nhiệm giữa 3 nhóm vai trò: **Business Analyst (BA)**, **Project Manager (PM)** và **Non-PM / Non-BA (SMEs, End-users, Managers)**.
- Đảm bảo yêu cầu được xác thực, giảm hiểu lầm và chuyển hóa các cuộc trao đổi thành kết quả hành động cụ thể (*actionable outcomes*).

---

## 2. Ma trận Trách nhiệm 5 Bước Khơi gợi Yêu cầu

| Bước (Step) & Mục tiêu | 🧠 Business Analyst (BA) | 📋 Project Manager (PM) | 👥 Non-PM / Non-BA (SMEs/Users) |
| :--- | :--- | :--- | :--- |
| **1. Prepare for Elicitation**<br>*(Chuẩn bị)*<br>• Xác định mục đích, phạm vi, phương pháp & đối tượng. | - Lập kế hoạch khơi gợi & chọn kỹ thuật phù hợp.<br>- Xác định danh sách stakeholders.<br>- Thống nhất thời gian & nguồn lực với PM. | - Tích hợp hoạt động khơi gợi vào lịch trình dự án tổng thể.<br>- Đảm bảo phòng họp, hậu cần, nguồn lực và phê duyệt.<br>- Kết nối đầu ra khơi gợi với mục tiêu dự án. | - Cung cấp bối cảnh vận hành & nỗi đau nghiệp vụ (*pain points*).<br>- Gợi ý các chuyên gia nghiệp vụ (SMEs) cần tham gia.<br>- Chia sẻ lịch trống & các ràng buộc thời gian. |
| **2. Conduct Elicitation**<br>*(Tiến hành)*<br>• Thu thập dữ liệu qua tương tác, quan sát & phân tích. | - Điều phối workshop, phỏng vấn, focus group.<br>- Đặt câu hỏi mở & đào sâu (*probing questions*).<br>- Ghi chép insight khách quan. | - Hỗ trợ quản lý thời gian (timekeeping) & mức độ gắn kết.<br>- Quan sát đảm bảo nội dung bám sát mục tiêu dự án. | - Chia sẻ trải nghiệm thực tế, quy trình và thách thức.<br>- Làm rõ *"công việc thực tế được xử lý như thế nào"*.<br>- Đề xuất ý tưởng cải tiến & xác nhận tính khả thi. |
| **3. Confirm Results**<br>*(Xác nhận)*<br>• Kiểm chứng độ chính xác, đầy đủ & hiểu đúng. | - Tóm tắt phát hiện & đối chiếu với stakeholders.<br>- Giải quyết xung đột quan điểm.<br>- Tài liệu hóa giả định & ràng buộc. | - Đánh giá yêu cầu đã xác nhận với Scope baseline.<br>- Nhận diện các thay đổi ảnh hưởng tới Schedule & Cost. | - Đọc lại tài liệu tóm tắt để xác thực độ chính xác.<br>- Xác nhận yêu cầu phản ánh đúng nhu cầu thực.<br>- Chỉ ra các điểm bị thiếu hoặc hiểu sai. |
| **4. Communicate Info**<br>*(Truyền thông)*<br>• Trực quan hóa & chia sẻ kết quả rõ ràng. | - Xây dựng sơ đồ trực quan (models), tóm tắt, spec.<br>- Thuyết trình & giải đáp thắc mắc.<br>- May đo tài liệu theo từng đối tượng tiếp nhận. | - Cập nhật Scope baseline & tài liệu lập kế hoạch.<br>- Đảm bảo team dev & Project Sponsor hiểu tác động của yêu cầu. | - Đánh giá độ rõ ràng & tính đầy đủ của tài liệu.<br>- Góp ý về tính khả dụng (usability).<br>- Cảnh báo các thách thức triển khai thực tế. |
| **5. Manage Collaboration**<br>*(Quản trị Cộng tác)*<br>• Duy trì gắn kết & thúc đẩy đồng sở hữu. | - Điều phối trao đổi liên tục & thu thập feedback.<br>- Theo dõi mức độ gắn kết của stakeholder.<br>- Linh hoạt điều chỉnh cách tiếp cận. | - Củng cố qua governance, communication plans & reviews.<br>- Leo thang (escalate) các khúc mắc chưa giải quyết. | - Tiếp tục tham gia review, kiểm thử (UAT) & change requests.<br>- Đưa ra phản hồi và nêu nhu cầu mới khi phát sinh.<br>- Hỗ trợ thúc đẩy chuyển đổi (adoption) hệ thống mới. |

---

## 3. Quy trình Dòng chảy Tổng quát (Flow Diagram)

```mermaid
flowchart TD
    S1["<b>1. Prepare</b><br/>BA lập plan, PM sắp lịch & hậu cần, SME cấp bối cảnh"]
    S2["<b>2. Conduct</b><br/>BA dẫn dắt & hỏi sâu, PM giữ nhịp, SME chia sẻ 'how work really gets done'"]
    S3["<b>3. Confirm</b><br/>BA tóm tắt & giải quyết xung đột, PM soi Scope/Cost, SME duyệt độ chính xác"]
    S4["<b>4. Communicate</b><br/>BA mô hình hóa trực quan, PM chốt Baseline, SME phản hồi tính khả dụng"]
    S5["<b>5. Collaborate</b><br/>Duy trì tương tác liên tục qua Design, Testing (UAT) & Go-live"]

    S1 --> S2 --> S3 --> S4 --> S5
```

---

## 4. Tóm tắt 4 Điểm cốt lõi (Key Takeaways)
1. **Chuẩn bị kỹ lưỡng:** Định nghĩa rõ mục đích, phạm vi và công cụ trước khi bắt đầu giúp tiết kiệm thời gian cho tất cả các bên.
2. **Khám phá chiều sâu:** BA đóng vai trò "người khai mở" (discovery), PM giữ vững ranh giới dự án, còn Non-PM/SME mang lại hơi thở thực tiễn vận hành.
3. **Xác nhận sớm để giảm rủi ro:** Xác thực và mô hình hóa trực quan giúp triệt tiêu hiểu lầm trước khi bước vào khâu lập trình/thiết kế tốn kém.
4. **Cộng tác là một chu kỳ liên tục:** Không dừng lại sau buổi phỏng vấn mà kéo dài xuyên suốt qua khâu Review, Prototype, Testing và Adoption.
