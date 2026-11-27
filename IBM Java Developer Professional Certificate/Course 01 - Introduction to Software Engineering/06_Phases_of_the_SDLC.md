# Phases of the SDLC

> **Khóa học**: Introduction to Software Engineering (Course 01 trong chứng chỉ *IBM Java Developer Professional Certificate*)  
> **Phần**: Overview of Software Engineering  
> **Video**: Phases of the SDLC  
> **Thời lượng**: 6:41  

---

## 1. Tổng quan 6 giai đoạn chuẩn trong SDLC
Mô hình SDLC tiêu chuẩn thường gồm **6 giai đoạn riêng biệt (discrete phases)**:
1. **Planning** (Lập kế hoạch)
2. **Design** (Thiết kế)
3. **Development** (Phát triển / Lập trình)
4. **Testing** (Kiểm thử)
5. **Deployment** (Triển khai)
6. **Maintenance** (Bảo trì & Vận hành)

> *Lưu ý về thuật ngữ:* Tùy tổ chức, tên gọi có thể thay đổi (ví dụ: Planning có thể gọi là *Requirements*, *Strategy*, hoặc *Analysis*), hoặc số lượng bước có thể gộp/tách tùy theo quy mô dự án.

---

## 2. Chi tiết từng giai đoạn & Nhiệm vụ tương ứng

### Giai đoạn 1: Planning (Lập kế hoạch)
- **Nội dung:** Thu thập, phân tích, tài liệu hóa và ưu tiên hóa các yêu cầu (requirements).
- **Các yếu tố cần xem xét:**
  - Đối tượng người dùng mục tiêu và mục đích tổng thể của giải pháp.
  - Luồng dữ liệu vào/ra (Data inputs and outputs).
  - Tuân thủ pháp lý & quy định (Legal & regulatory compliance).
  - Nhận diện rủi ro (Risk identification) và yêu cầu đảm bảo chất lượng (QA requirements).
  - Phân bổ nguồn lực (nhân sự, tài chính), ước tính chi phí vật tư/lao động và lập tiến độ (scheduling).
- **Prototyping trong Planning:** Dựng mô hình mẫu quy mô nhỏ (small-scale replica) để xin phản hồi sớm từ stakeholders nếu yêu cầu chưa rõ ràng.
- **Sản phẩm bàn giao (Deliverable):** Tài liệu đặc tả yêu cầu phần mềm (**Software Requirements Specification - SRS**) – cần được phê duyệt bởi tất cả các bên liên quan và dev team phải nắm rõ.

---

### Giai đoạn 2: Design (Thiết kế)
- **Nội dung:** Dựa trên SRS để xây dựng kiến trúc phần mềm (**software architecture**).
- **Nhiệm vụ:**
  - Phối hợp giữa các thành viên để thiết kế kiến trúc hệ thống, mô hình dữ liệu và giao diện.
  - Xây dựng bản mẫu mô phỏng (**prototypes / mock-ups**) phục vụ demo và đánh giá tính khả thi.
  - Stakeholders và nhóm kỹ thuật tiến hành review, phê duyệt kiến trúc.
- **Sản phẩm bàn giao (Deliverable):** Tài liệu thiết kế kỹ thuật (**Design Document**) làm cơ sở trực tiếp cho giai đoạn coding tiếp theo.

---

### Giai đoạn 3: Development / Implementation (Phát triển / Lập trình)
- **Nội dung:** Lập trình viên bắt đầu viết code khi tài liệu thiết kế (Design Document) đã hoàn thiện.
- **Nhiệm vụ:**
  - Planners/Leads phân rã tài liệu thiết kế thành các task coding cụ thể cho lập trình viên.
  - Áp dụng các công cụ lập trình, bộ ngôn ngữ và tech stack tương ứng.
  - Tuân thủ các tiêu chuẩn kỹ thuật, coding conventions và guidelines của tổ chức.

---

### Giai đoạn 4: Testing (Kiểm thử)
- **Nội dung:** Xác minh mã nguồn hoạt động ổn định, bảo mật và đáp ứng đầy đủ yêu cầu trong SRS.
- **Hình thức:** Kiểm thử thủ công (manual), tự động (automated) hoặc kết hợp (hybrid).
- **Quy trình:** Phát hiện bug $\rightarrow$ Báo cáo & theo dõi (track) $\rightarrow$ Sửa lỗi (fix) $\rightarrow$ Kiểm thử lại (retest) cho tới khi phần mềm đạt trạng thái ổn định.
- **Các cấp độ kiểm thử phổ biến:**
  - **Unit testing:** Kiểm thử đơn vị (hàm, module nhỏ).
  - **Integration testing:** Kiểm thử tích hợp giữa các module/dịch vụ.
  - **System testing:** Kiểm thử toàn bộ hệ thống tích hợp.
  - **Acceptance testing (UAT):** Kiểm thử chấp nhận từ người dùng/khách hàng.

---

### Giai đoạn 5: Deployment (Triển khai)
- **Nội dung:** Phát hành ứng dụng lên môi trường production để cung cấp cho người dùng cuối.
- **Quy trình phát hành theo tầng (Staged Deployment):**
  - Đưa lên môi trường UAT (User Acceptance Testing) để khách hàng nghiệm thu chức năng.
  - Sau khi khách hàng ký xác nhận (sign-off) $\rightarrow$ Release chính thức lên Production (Web, App Store, hoặc Server nội bộ doanh nghiệp).

---

### Giai đoạn 6: Maintenance (Bảo trì & Tiến hóa)
- **Nội dung:** Diễn ra liên tục sau khi phần mềm chạy trên Production.
- **Nhiệm vụ:**
  - Giám sát, phát hiện các bug còn sót sau pha testing hoặc các lỗi giao diện (UI issues).
  - Khắc phục khẩn cấp các lỗi có độ ưu tiên cao (critical/high-priority fixes).
  - Thu thập phản hồi từ người dùng/stakeholders và đề xuất cải tiến mã nguồn (code enhancements), phát hiện yêu cầu mới chưa có trong SRS ban đầu.
- **Vòng lặp tiếp theo:** Các cải tiến và tính năng mới được nạp ngược lại vào chu trình SDLC mới (Planning cho bản release tiếp theo).
