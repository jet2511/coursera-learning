# Implementation Planning

## 1. Khung Stacey (Stacey Agreement & Complexity Matrix)
- **Ẩn dụ Nấu ăn (Cooking):** Có công thức rõ ràng và nguyên liệu quen thuộc ➔ Nấu chuẩn theo từng bước (Predictive). Thử nghiệm món mới hoặc phục vụ thực khách khó tính ➔ Vừa nấu vừa nếm và tùy biến (Adaptive).
- **Khung Stacey (Ralph Stacey Model):** Định hướng lựa chọn phương pháp triển khai dự án dựa trên 2 trục:
  1. **Mức độ đồng thuận (Agreement on Goals & Requirements):** Các bên liên quan có thống nhất về mục tiêu và yêu cầu không?
  2. **Mức độ phức tạp / không chắc chắn (Uncertainty & Complexity of Work):** Công nghệ và giải pháp đã biết rõ hay chưa xác định?

---

## 2. Ba phương pháp tiếp cận triển khai (3 Planning Approaches)

| Phương pháp | Bối cảnh áp dụng lý tưởng | Đặc điểm & Thực hành tốt nhất (Best Practices) | Điều cần tránh (Don't) |
| :--- | :--- | :--- | :--- |
| **Predictive Planning**<br>*(Kế hoạch định trước / Waterfall)* | Yêu cầu rõ ràng, ít biến động; mối quan hệ nhân - quả đã được hiểu thấu đáo (vd: nâng cấp hạ tầng, chuẩn hóa vận hành, tuân thủ pháp lý). | - Xác định chi tiết Phạm vi (Scope), Tiến độ (Schedule), Chi phí (Cost).<br>- Kiểm soát chặt bằng Stage gates, Milestones, Baselines. | - Đừng lập kế hoạch quá mức (over-engineering) cho phần việc chắc chắn sẽ đổi.<br>- Đừng bám cứng kế hoạch cũ khi bài học thực tế mở ra hướng đi tốt hơn. |
| **Adaptive / Agile**<br>*(Thích ứng linh hoạt)* | Độ bất định công nghệ cao, nhu cầu stakeholder thay đổi nhanh (vd: Đổi mới sáng tạo, Digital Transformation, tái thiết kế quy trình phức tạp). | - Chia nhỏ chu kỳ (sprints/iterations) giao nộp kết quả đo kiểm được.<br>- Thu nhận phản hồi (feedback loops) liên tục từ nhóm liên chức năng. | - Đừng cố định nghĩa mọi chi tiết trước khi bắt đầu.<br>- Đừng để các vòng lặp trôi dạt (drift) thiếu định hướng và tách rời mục tiêu lớn. |
| **Hybrid Planning**<br>*(Phương pháp lai ghép)* | Phần lớn dự án quy mô lớn: có cấu phần ổn định kết hợp cấu phần mơ hồ (vd: phần cứng/hạ tầng dùng Predictive, UI/UX hoặc tích hợp quy trình dùng Agile). | - Dùng yếu tố Predictive để giữ khung điều phối liên phòng ban.<br>- Dùng yếu tố Adaptive để giải quyết rủi ro mới nổi và phản hồi người dùng.<br>- Thiết lập cơ chế quản trị (governance) tích hợp nhịp nhàng cả 2 chu kỳ. | - Đừng biến hybrid thành mớ hỗn độn chắp vá các phương pháp xung đột nhau.<br>- Cần truyền thông và giữ các nhóm cùng hướng về mục tiêu hệ thống chung. |

---

## 3. Căn chỉnh toàn hệ thống khi triển khai (System-Wide Alignment)
Bất kể chọn phương pháp nào (Predictive, Adaptive hay Hybrid), thành công đều phụ thuộc vào tư duy hệ thống:
1. **Truyền thông minh bạch:** Làm rõ mục tiêu tối thượng và các mối phụ thuộc chéo (dependencies) giữa các bên.
2. **Chỉ số đo lường chung (Shared KPIs):** Gắn kết quả dự án với hiệu năng toàn chuỗi, không đo theo tiến độ cục bộ của từng nhóm.
3. **Minh bạch dữ liệu & Feedback Loops:** Dữ liệu thông suốt giúp phát hiện sự cố sớm và điều chỉnh kịp thời trước khi hệ thống trôi dạt.
