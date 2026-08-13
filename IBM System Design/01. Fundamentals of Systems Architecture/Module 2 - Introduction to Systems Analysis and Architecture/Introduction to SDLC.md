# Tóm tắt: Giới thiệu về SDLC (Introduction to SDLC)

Tài liệu này định nghĩa Vòng đời Phát triển Hệ thống (SDLC), phân loại các mô hình SDLC phổ biến và chi tiết các giai đoạn cốt lõi của quy trình này.

---

## 1. Định nghĩa SDLC
**Vòng đời Phát triển Hệ thống (System Development Life Cycle - SDLC)** là một quy trình từng bước giúp chia nhỏ nhiệm vụ phức tạp của việc xây dựng mới hoặc nâng cấp một hệ thống thành các giai đoạn nhỏ dễ quản lý hơn. SDLC cung cấp một khung làm việc có hệ thống cho việc lập kế hoạch, thiết kế, phát triển, kiểm thử và triển khai hệ thống.

---

## 2. Các Mô hình SDLC Phổ biến (Common SDLC Models)
Tùy thuộc vào quy mô dự án, độ phức tạp, đội ngũ và thời gian bàn giao, các tổ chức lựa chọn các phương pháp luận khác nhau:

* **Mô hình Thác nước (Waterfall Model):** Tiếp cận theo dạng tuyến tính (từng bước một). Mỗi giai đoạn phải được hoàn thành 100% trước khi chuyển sang giai đoạn tiếp theo. Phù hợp nhất cho các dự án có yêu cầu rõ ràng, cố định và ít thay đổi ngay từ đầu.
* **Mô hình Linh hoạt (Agile Model):** Tiếp cận theo kiểu lặp và tăng dần (iterative and incremental). Hệ thống được xây dựng và bàn giao từng phần nhỏ thông qua các chu kỳ ngắn hạn gọi là **sprint**. Ưu tiên sự cộng tác của đội ngũ, sự hài lòng của khách hàng và việc tạo ra phần mềm hoạt động được hơn là tài liệu chi tiết.
* **Mô hình Xoắn ốc (Spiral Model):** Tập trung mạnh mẽ vào phân tích rủi ro và tinh chỉnh hệ thống lặp đi lặp lại qua các chu kỳ xoắn ốc. Gồm 4 giai đoạn chính trong mỗi vòng lặp: Lập kế hoạch, Phân tích rủi ro, Kỹ thuật (phát triển) và Đánh giá kết quả.
* **Mô hình chữ V (V-Model - Verification & Validation):** Là một nhánh mở rộng của Waterfall, nhấn mạnh mối quan hệ chặt chẽ giữa mỗi giai đoạn phát triển và giai đoạn kiểm thử tương ứng (kiểm thử song song). Thích hợp cho dự án có yêu cầu rõ ràng, đòi hỏi tính chính xác cao.

---

## 3. Các Giai đoạn trong SDLC (Key Phases of SDLC)

Hầu hết các mô hình phát triển đều tuân theo các giai đoạn cốt lõi sau:

```mermaid
flowchart LR
    1[Planning] --> 2[Analysis] --> 3[Design] --> 4[Development] --> 5[Testing] --> 6[Deployment] --> 7[Maintenance]
```

### 1. Lập kế hoạch (Planning)
* **Mục tiêu:** Thấu hiểu vấn đề/cơ hội kinh doanh và xác định xem có thực sự cần một hệ thống mới hoặc nâng cấp hệ thống cũ hay không.
* **Công việc chính:** Xác định phạm vi dự án (scope), dự toán thời gian và chi phí, xác định các bên liên quan (stakeholders) và thực hiện các báo cáo khả thi (feasibility studies) trên các khía cạnh: kỹ thuật, kinh tế, pháp lý, và vận hành.

### 2. Phân tích hệ thống (System Analysis)
* **Mục tiêu:** Thu thập các yêu cầu chi tiết từ người dùng cuối và các bên liên quan. Giai đoạn này trả lời câu hỏi: *Hệ thống cần làm gì (WHAT)?* chứ chưa giải quyết câu hỏi *Hệ thống làm thế nào (HOW)?*
* **Công việc chính:** Phỏng vấn, khảo sát, quan sát và phân tích hệ thống hiện tại; tài liệu hóa các yêu cầu chức năng (functional requirements) và yêu cầu phi chức năng (non-functional requirements).
* **Kết quả bàn giao:** Tài liệu Đặc tả Yêu cầu Hệ thống (**System Requirements Specification - SRS**) - kim chỉ nam cho giai đoạn thiết kế.

### 3. Thiết kế hệ thống (System Design)
* **Mục tiêu:** Phác thảo chi tiết cách thức xây dựng hệ thống mới dựa trên tài liệu phân tích yêu cầu SRS.
* **Công việc chính:** Định nghĩa kiến trúc hệ thống (architecture), giao diện người dùng (UI), thiết kế cơ sở dữ liệu (database schemas), cấu trúc tệp tin, sơ đồ luồng quy trình (process flowcharts), xác định nhu cầu phần cứng và phần mềm.
* **Kết quả bàn giao:** Tài liệu Đặc tả Thiết kế (Design Specification Document) phục vụ cho lập trình viên.

### 4. Phát triển (Development)
* **Mục tiêu:** Xây dựng hệ thống thực tế dựa trên các tài liệu thiết kế đã phê duyệt.
* **Công việc chính:** Lập trình phần mềm (coding), cấu hình hạ tầng mạng/phần cứng, tích hợp các hệ thống có sẵn.

### 5. Kiểm thử (Testing)
* **Mục tiêu:** Phát hiện và sửa lỗi (bugs) nhằm đảm bảo hệ thống vận hành chính xác và an toàn trước khi go-live.
* **Công việc chính:**
  * **Unit testing:** Kiểm thử đơn vị (từng đoạn code, chức năng riêng lẻ).
  * **System testing:** Kiểm thử toàn bộ hệ thống để xem các thành phần tích hợp có hoạt động mượt mà không.
  * **User Acceptance Testing (UAT):** Kiểm thử chấp nhận bởi người dùng cuối để xác nhận hệ thống đáp ứng đúng nhu cầu nghiệp vụ thực tế.

### 6. Triển khai (Deployment)
* **Mục tiêu:** Phát hành và chuyển giao hệ thống để đưa vào sử dụng thực tế.
* **Các phương thức phổ biến:**
  * **Triển khai toàn bộ (Full rollout):** Hệ thống mới đồng loạt go-live cho tất cả người dùng cùng lúc.
  * **Triển khai theo giai đoạn (Phased rollout):** Hệ thống được triển khai từng bước, theo từng phân hệ hoặc từng nhóm người dùng.
  * **Triển khai song song (Parallel rollout):** Hệ thống mới chạy song song với hệ thống cũ trong một khoảng thời gian để giảm thiểu rủi ro, nếu hệ mới lỗi vẫn có hệ cũ dự phòng.
* **Hỗ trợ:** Cung cấp đào tạo (training) và tài liệu hướng dẫn sử dụng.

### 7. Bảo trì (Maintenance)
* **Mục tiêu:** Đảm bảo hệ thống tiếp tục mang lại giá trị và thích ứng tốt với nhu cầu thay đổi của doanh nghiệp.
* **Công việc chính:** Sửa lỗi phát sinh sau vận hành, tối ưu hiệu suất, cập nhật tính năng mới hoặc hỗ trợ người dùng cuối.
