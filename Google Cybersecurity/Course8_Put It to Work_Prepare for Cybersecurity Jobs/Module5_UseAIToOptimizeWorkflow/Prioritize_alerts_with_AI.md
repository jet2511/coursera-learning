# Tóm Tắt Bài Học: Phân Mức Ưu Tiên Cảnh Báo Bằng AI (Prioritize Alerts with AI)

#### 1. Vai Trò Trợ Lý Xử Lý Sự Cố Của AI (Troubleshooting Assistant)
* **Giám sát & Phát hiện:** Hỗ trợ Security Analyst phân tích nhật ký (logs), nhận diện lưu lượng mạng bất thường và đánh giá các cảnh báo gửi về từ Hệ thống phát hiện xâm nhập (**IDS**).

---

#### 2. Kịch Bản Thực Tế: Xếp Thứ Tự Ưu Tiên Cảnh Báo IDS
* **Cách thực hiện:** Dán chi tiết thông tin của 3 cảnh báo IDS vào Gemini kèm prompt yêu cầu xếp hạng ưu tiên theo mức độ nghiêm trọng và tác động đến hệ thống.
* **Kết quả từ AI:**
  * Xếp danh sách ưu tiên kèm giải thích lý do cụ thể cho từng cảnh báo.
  * **Cảnh báo chiến thuật lừa đảo:** AI nhắc nhở kiểm tra mối liên hệ giữa các cảnh báo, vì một đợt tấn công **SYN flood** có thể chỉ là đòn "dương đông kích tây" (diversionary tactic) để đánh lạc hướng Analyst khỏi một cuộc tấn công nguy hiểm hơn.

---

#### 3. Bổ Sung Cho Kế Hoạch Ứng Phó Sự Cố (Incident Response Plan - IRP)
* **Nguyên tắc:** **Luôn luôn tra cứu Kế hoạch ứng phó sự cố (IRP) chính thức của tổ chức trước tiên.**
* **Ứng dụng AI khi IRP thiếu kịch bản:**
  * Với sự cố chưa có trong IRP: Dùng AI gợi ý luồng xử lý và ưu tiên cảnh báo phù hợp.
  * Với các lỗ hổng/cảnh báo mới: Dùng AI hỗ trợ soạn thảo nội dung quy trình để cập nhật bổ sung vào tài liệu IRP chính thức của công ty.

---

#### 4. Thông Điệp & Thách Thức Thực Hành
* Hãy chủ động thử nghiệm các dạng prompt khác nhau để biến AI thành công cụ nâng cao năng suất thực sự.
* **Thách thức:** Chọn một công việc đang tiêu tốn nhiều thời gian nhất của bạn hàng ngày và thử áp dụng AI để tối ưu hóa nó ngay hôm nay.
