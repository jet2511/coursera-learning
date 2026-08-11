# Tóm tắt bài học: Giới thiệu Tuần 1 (Week 1 Introduction)

**Khóa học:** Course 2 - Architecting Solutions on AWS  
**Chủ đề:** Phương pháp thiết kế kiến trúc và cách tiếp cận tình huống trong Tuần 1  
**Vị trí:** Module 1 - Designing a serverless web backend on AWS

---

## 1. Phương pháp học tập nhập vai (Role-playing Method)
* **Phân vai trong Tuần 1:** Giảng viên **Morgan** đóng vai trò là *Solutions Architect (SA)*, còn giảng viên **Raf** đóng vai trò là *Khách hàng (Customer)*.
* **Quy trình giả định:** 
  1. SA gọi điện thoại cho khách hàng để thu thập yêu cầu nghiệp vụ ban đầu.
  2. Thực hiện các cuộc gọi làm rõ (clarification calls) trong suốt tuần để giải quyết các vướng mắc phát sinh.
  3. SA thiết kế giải pháp kiến trúc dựa trên dữ liệu thu thập được.

---

## 2. Tư duy thiết kế giải pháp AWS (Architectural Design Mindset)
* **Không có giải pháp đúng duy nhất:** Trên AWS, một bài toán có thể được giải quyết bằng nhiều cách khác nhau. Việc lựa chọn kiến trúc nào phụ thuộc hoàn toàn vào:
  * Tình huống thực tế (Use case).
  * Các yêu cầu nghiệp vụ cụ thể (Requirements).
  * Tiêu chí tối ưu hóa của khách hàng (hiệu năng, chi phí, hay sự đơn giản trong vận hành).
* **Mô hình hóa bằng khối (Building Blocks):** Các dịch vụ AWS được ví như các khối xếp hình. Giảng viên sẽ xây dựng kiến trúc trực quan bằng cách xếp các khối mô hình vật lý trên bàn học dưới góc quay từ trên xuống (top-down view) để người học dễ dàng hình dung dòng chảy dữ liệu.
* **Tối ưu hóa và cải tiến:** Sau khi hoàn thành sơ đồ khối, các giảng viên sẽ cùng thảo luận về các cách tiếp cận thay thế, phân tích ưu/nhược điểm và cách nâng cấp kiến trúc lên mức tối ưu hơn.

---

## 3. Lưu ý quan trọng cho người học
* **Tập trung vào lý do tại sao (The "Why"):** Khóa học tập trung giải thích *tại sao* nên chọn dịch vụ này thay vì dịch vụ khác cho một tình huống, hơn là hướng dẫn chi tiết từng bước nhấp chuột (*The "How"*).
* **Khái niệm đơn giản hóa:** Một số khái niệm hoặc chi tiết kiến trúc sẽ được đơn giản hóa mục đích để tối ưu cho việc học tập.
* **Tầm quan trọng của PoC:** Trong môi trường thực tế, sau khi thiết kế xong bản vẽ kiến trúc, Solutions Architect cần xây dựng một phiên bản thử nghiệm thực tế (**Proof of Concept - PoC**) để chứng minh giải pháp hoạt động đúng như mong đợi của khách hàng.
* **Học liệu bổ trợ:** Đọc kỹ các tài liệu văn bản xen kẽ các bài học video để lấy các đường dẫn tới các bài blog chuyên sâu, lab hướng dẫn chi tiết của AWS.
