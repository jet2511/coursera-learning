# Project Management and Documentation Tools (Công cụ quản lý dự án và tài liệu)

Bản tóm tắt nội dung học tập về vai trò, các công cụ phổ biến và các thực hành tốt nhất (best practices) trong quản lý dự án và tài liệu hóa hệ thống.

---

### 1. Vai trò của quản lý dự án và tài liệu hóa
*   **Quản lý dự án:** Giúp kiểm soát phạm vi (scope), lịch trình (schedule), tài nguyên (resources), theo dõi tiến độ, quản lý rủi ro và đảm bảo sự đồng bộ giữa mục tiêu dự án và mục tiêu kinh doanh. Đặc biệt quan trọng khi làm việc trong các nhóm chức năng chéo (cross-functional teams).
*   **Tài liệu hóa (Documentation):** Là nền tảng của kiến trúc hệ thống, đảm bảo tất cả các bên liên quan (Kiến trúc sư, Lập trình viên, QA/Tester, Stakeholders, Quản lý) có chung một hiểu biết thống nhất về hệ thống được xây dựng.

---

### 2. Các công cụ quản lý dự án phổ biến

*   **Jira (Atlassian):** 
    *   Công cụ hàng đầu cho môi trường Agile (Scrum/Kanban).
    *   Giúp tạo và quản lý User Stories, Tasks, Bugs; liên kết công việc vào Sprint/Backlog; trực quan hóa tiến độ thông qua bảng Scrum/Kanban và cộng tác với các đội ngũ QA/Dev.
*   **Trello:**
    *   Giao diện dạng thẻ (card-based) đơn giản, trực quan.
    *   Phù hợp cho các dự án quy mô nhỏ đến trung bình, giúp tổ chức công việc bằng checklist, nhãn (labels) và thời hạn (due dates).
*   **Microsoft Project (MS Project):**
    *   Thiết kế chuyên biệt cho mô hình phát triển tuần tự (Waterfall).
    *   Mạnh về xây dựng sơ đồ Gantt (Gantt charts) biểu diễn dòng thời gian và mối quan hệ phụ thuộc công việc, phân bổ tài nguyên và quản lý ngân sách.
*   **Asana:**
    *   Sự kết hợp giữa lập kế hoạch công việc và cộng tác nhóm, hỗ trợ theo dõi trạng thái công việc liên phòng ban.

---

### 3. Các công cụ tài liệu hóa và mô hình hóa

*   **Tài liệu văn bản & Bảng tính (MS Word & MS Excel):**
    *   Sử dụng để viết tài liệu yêu cầu nghiệp vụ (Business Requirements Documents - BRD), tài liệu đặc tả kỹ thuật và xây dựng ma trận truy vết yêu cầu (traceability matrices).
*   **Thiết kế sơ đồ (Lucidchart & MS Visio):**
    *   Dùng để vẽ sơ đồ kiến trúc hệ thống, sơ đồ luồng dữ liệu (DFD), sơ đồ quan hệ thực thể (ERD), sơ đồ ca sử dụng (Use Cases) và lưu đồ quy trình.
*   **Nền tảng cộng tác và lưu trữ:**
    *   **Confluence:** Nền tảng Wiki chia sẻ tài liệu dự án, biên bản họp, liên kết trực tiếp với các issues/tickets trên Jira và các sơ đồ hệ thống.
    *   **Google Workspace (Docs, Sheets, Drive):** Hỗ trợ đồng biên tập (co-editing) và đánh giá tài liệu theo thời gian thực, tối ưu cho các nhóm làm việc từ xa hoặc hybrid.

---

### 4. Khả năng tích hợp và tự động hóa
Việc tích hợp chéo giữa các công cụ (ví dụ: Jira + Confluence + Slack; Trello + Google Drive; MS Project + Teams) giúp:
*   Giảm thiểu sự dư thừa và nhập liệu thủ công.
*   Đồng bộ hóa các cập nhật theo thời gian thực.
*   Thiết lập luồng tự động hóa (automation): Tự động tạo hoặc chuyển trạng thái task khi một tài liệu hoặc mã nguồn được phê duyệt.

---

### 5. Thực hành tốt nhất (Best Practices)
1.  **Giữ mọi thứ đơn giản (Keep it simple):** Lựa chọn công cụ phù hợp với quy mô và độ phức tạp của dự án, tránh lạm dụng quá nhiều công cụ cồng kềnh cho dự án nhỏ.
2.  **Nhất quán (Stay consistent):** Sử dụng các biểu mẫu (templates) sẵn có và tuân thủ quy tắc đặt tên (naming conventions) chuẩn hóa để dễ tìm kiếm.
3.  **Giao tiếp thường xuyên (Communicate often):** Sử dụng các công cụ quản lý dự án để chủ động cập nhật trạng thái thay vì chỉ dùng để giao việc thụ động.
4.  **Tài liệu hóa các quyết định (Document decisions):** Tập trung lưu lại lý do (câu hỏi **Tại sao - Why**) đằng sau các quyết định kiến trúc quan trọng, không chỉ mô tả hệ thống có những gì (**Cái gì - What**).
5.  **Đào tạo đội ngũ (Train your team):** Đảm bảo tất cả các thành viên tham gia dự án đều được hướng dẫn cách sử dụng công cụ thống nhất.
