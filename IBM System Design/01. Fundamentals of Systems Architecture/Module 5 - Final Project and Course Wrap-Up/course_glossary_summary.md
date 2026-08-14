# Tóm tắt Thuật ngữ Khóa học: Cơ sở Kiến trúc Hệ thống (Course Glossary)

Tài liệu này hệ thống hóa toàn bộ thuật ngữ cốt lõi của khóa học kiến trúc hệ thống, được phân loại theo các nhóm chủ đề logic để thuận tiện cho việc tra cứu nhanh.

---

## 1. Các Khái niệm Cơ bản về Hệ thống (System Fundamentals)
* **System (Hệ thống):** Tập hợp các thành phần có mối quan hệ tương hỗ hoạt động cùng nhau để thực hiện nhiệm vụ và đạt mục tiêu chung.
* **Systems thinking (Tư duy hệ thống):** Nhãn quan kiến trúc tập trung vào sự liên kết giữa các bộ phận trong hệ thống và tầm ảnh hưởng của chúng lẫn nhau theo thời gian.
* **Input (Đầu vào):** Dữ liệu, vật liệu hoặc tín hiệu thô mà hệ thống tiếp nhận để xử lý.
* **Process (Xử lý):** Tập hợp các thao tác, chuyển đổi mà hệ thống thực hiện trên dữ liệu đầu vào.
* **Output (Đầu ra):** Kết quả cuối cùng sau khi xử lý (báo cáo, dịch vụ, thông báo, quyết định).
* **Boundary (Ranh giới):** Giới hạn phân tách các thành phần bên trong hệ thống với môi trường bên ngoài.
* **Feedback (Phản hồi):** Dữ liệu về hiệu suất của hệ thống được dùng để điều chỉnh, sửa lỗi hoặc tối ưu hóa hoạt động.
* **Control (Kiểm soát):** Cơ chế, chính sách giám sát hiệu suất nhằm đảm bảo hệ thống hoạt động đúng mục tiêu.
* **Coupling (Độ liên kết/Độ phụ thuộc):** Mức độ phụ thuộc lẫn nhau giữa các mô-đun phần mềm. Thiết kế tốt cần hướng tới **Loose coupling** (liên kết lỏng lẻo) để tăng tính linh hoạt và giảm thiểu lỗi lan truyền.
* **Phân loại hệ thống:**
  * *Open system (Hệ thống mở):* Trao đổi thông tin/năng lượng với môi trường bên ngoài và tự thích nghi.
  * *Closed system (Hệ thống đóng):* Hoạt động độc lập, không trao đổi với bên ngoài.
  * *Adaptive system (Hệ thống thích ứng):* Có thể tự thay đổi cấu trúc/hành vi dựa trên phản hồi.
  * *Deterministic system (Hệ thống tất định):* Kết quả đầu ra luôn nhất quán và dự đoán được từ một tập đầu vào xác định.
  * *Probabilistic system (Hệ thống xác suất):* Có yếu tố ngẫu nhiên, đầu ra có thể khác nhau dù cùng đầu vào.

---

## 2. Vòng đời Phát triển Phần mềm (SDLC & Methodologies)
* **SDLC (System Development Life Cycle):** Quy trình tuần tự để lập kế hoạch, phân tích, thiết kế, kiểm thử và bảo trì hệ thống thông tin.
* **Các giai đoạn chính của SDLC:**
  1. *Planning (Lập kế hoạch):* Xác định vấn đề, mục tiêu, ước tính tài nguyên và đánh giá tính khả thi.
  2. *Analysis (Phân tích):* Nghiên cứu sâu nhu cầu nghiệp vụ, thu thập yêu cầu từ stakeholders qua các kỹ thuật khơi gợi (elicitation techniques).
  3. *Design (Thiết kế):* Tạo đặc tả kỹ thuật bao gồm kiến trúc hệ thống, cấu trúc dữ liệu và logic xử lý.
  4. *Development (Phát triển):* Viết mã nguồn, cấu hình hệ thống và tích hợp các thành phần.
  5. *Testing (Kiểm thử):* QA chạy thử để tìm lỗi và kiểm tra tính năng. Bao gồm cả **User Acceptance Testing (UAT)** (kiểm thử chấp nhận người dùng cuối).
  6. *Deployment (Triển khai):* Cài đặt và đưa hệ thống vào hoạt động (toàn bộ, theo pha hoặc chạy song song).
  7. *Maintenance (Bảo trì):* Sửa lỗi, nâng cấp tính năng và đảm bảo an ninh sau khi bàn giao.
* **Các mô hình SDLC tiêu biểu:**
  * *Waterfall (Thác nước):* Tiếp cận tuyến tính, hoàn thành pha này mới qua pha tiếp theo. Phù hợp yêu cầu cố định, rõ ràng.
  * *Agile (Linh hoạt):* Phát triển lặp đi lặp lại qua các chu kỳ ngắn (sprints), nhấn mạnh phản hồi liên tục.
  * *V-model (Xác thực & Kiểm chứng):* Đối xứng hóa mỗi pha phát triển với một pha kiểm thử tương ứng.
  * *Spiral (Xoắn ốc):* Kết hợp giữa phát triển lặp (iterative) và phân tích rủi ro hệ thống ở mỗi chu kỳ.

---

## 3. Kiến trúc Phần mềm & Các Mẫu Thiết kế (Architecture Patterns & Concepts)
* **Architectural pattern (Mẫu kiến trúc):** Giải pháp tái sử dụng cho các vấn đề thiết kế hệ thống lặp đi lặp lại.
* **Các mẫu kiến trúc chính:**
  * *2-tier architecture (Client-Server / Khách-Chủ):* Trình duyệt hoặc ứng dụng khách gửi yêu cầu trực tiếp đến máy chủ (nơi xử lý cả logic nghiệp vụ lẫn lưu trữ dữ liệu).
  * *3-tier architecture (Kiến trúc 3 lớp):* Tách biệt rõ ràng 3 tầng: Tầng hiển thị (Presentation tier), Tầng xử lý logic nghiệp vụ (Application/Business logic tier), và Tầng dữ liệu (Data tier).
  * *Microservices (Vi dịch vụ):* Chia nhỏ ứng dụng thành các dịch vụ độc lập, giao tiếp với nhau qua API.
  * *Event-driven architecture (Kiến trúc hướng sự kiện):* Các hành động được kích hoạt và điều phối thông qua việc tạo ra và xử lý các sự kiện (events).
  * *Service-oriented architecture (SOA):* Kiểu kiến trúc liên kết các dịch vụ lỏng lẻo thông qua giao thức truyền thông như HTTP.
  * *Peer-to-peer (P2P):* Hệ thống phi tập trung nơi các nút vừa đóng vai trò là client vừa là server.
* **Các cơ chế kỹ thuật & Môi trường:**
  * *Caching (Bộ nhớ đệm):* Lưu trữ dữ liệu thường dùng trong bộ nhớ tốc độ cao để phản hồi nhanh, giảm tải cho cơ sở dữ liệu.
  * *Load balancing (Cân bằng tải):* Phân phối lưu lượng mạng đồng đều qua các máy chủ để tối ưu hóa hiệu suất và tránh quá tải.
  * *Pre-production environments (Môi trường tiền sản xuất):* Bao gồm môi trường Phát triển (Dev), Kiểm thử chất lượng (QA), và Staging (môi trường mô phỏng giống hệt Production để kiểm tra cuối cùng).
  * *Production environment (Môi trường sản xuất):* Môi trường vận hành thực tế nơi người dùng cuối truy cập hệ thống.

---

## 4. Mô hình hóa Hệ thống & Sơ đồ UML (UML & System Diagramming)
* **UML (Unified Modeling Language):** Ngôn ngữ mô hình hóa trực quan tiêu chuẩn để mô tả cấu trúc và hành vi hệ thống phần mềm.
* **Các sơ đồ UML hành vi & cấu trúc:**
  * *Use case diagram:* Chỉ ra cách người dùng (actors) tương tác với hệ thống để đạt mục tiêu cụ thể.
  * *Class diagram (Sơ đồ lớp):* Mô tả cấu trúc hệ thống tĩnh bằng cách hiển thị các lớp, thuộc tính, phương thức và các mối quan hệ (inheritance, association).
  * *Sequence diagram (Sơ đồ trình tự):* Biểu diễn sự tương tác của các đối tượng trong hệ thống theo trình tự thời gian.
  * *Activity diagram (Sơ đồ hoạt động):* Mô tả luồng công việc (workflows) hoặc quy trình nghiệp vụ tương tự như lưu đồ.
  * *State transition diagram (Sơ đồ chuyển trạng thái):* Biểu diễn các trạng thái khác nhau của đối tượng và cách các sự kiện kích hoạt chuyển trạng thái.
* **Sơ đồ luồng dữ liệu & cấu trúc dữ liệu:**
  * *Data Flow Diagram (DFD):* Sơ đồ luồng dữ liệu hiển thị cách dữ liệu di chuyển qua các thực thể, tiến trình và điểm lưu trữ.
  * *Entity Relationship Diagram (ERD):* Sơ đồ thực thể liên kết dùng cho thiết kế cơ sở dữ liệu, xác định thực thể, thuộc tính và mối quan hệ giữa chúng.

---

## 5. Công cụ của Kiến trúc sư Hệ thống (Architect's Toolset)
* **Quản lý dự án & Cộng tác:** MS Project, Jira (theo dõi User Story/Sprint), Confluence (tài liệu hóa), Trello, Asana, Notion, Slack, Teams.
* **Thiết kế & Prototype UI/UX:** Figma, Balsamiq (vẽ wireframe sơ bộ nhanh), Axure RP (prototype tương tác cao), InVision.
* **Vẽ sơ đồ hệ thống:** Microsoft Visio, Lucidchart.
* **Quản trị & Thiết kế CSDL:** MySQL Workbench, Oracle SQL Developer, ER Studio (quản lý cơ sở dữ liệu phức tạp).
* **Báo cáo & Trực quan hóa dữ liệu (BI):** Tableau, Power BI, Looker (Google Cloud native), Qlik Sense.
* **Mô phỏng & Tính toán:** Arena, AnyLogic, MATLAB, Python (Matplotlib, Seaborn), SPSS, R.

---

## 6. An ninh mạng & Bảo mật (Security & Zero Trust)
* **Security-first design (Thiết kế ưu tiên bảo mật):** Xem xét an ninh và quản trị rủi ro ngay từ đầu quy trình lập kế hoạch dự án.
* **Zero-trust architecture (Kiến trúc không tin cậy):** Mô hình bảo mật giả định không có sự tin cậy ngầm định, mọi thiết bị, người dùng đều phải liên tục xác thực và kiểm tra quyền truy cập.
* **Firewall (Tường lửa):** Thiết bị giám sát và kiểm soát lưu lượng mạng để ngăn chặn truy cập trái phép.

---

## 7. Các Vai trò trong Dự án Công nghệ (IT Roles)
* **Enterprise Architect (Kiến trúc sư doanh nghiệp):** Định hướng và đồng bộ hóa các thiết kế hệ thống nhỏ với tiêu chuẩn và chiến lược công nghệ dài hạn của toàn doanh nghiệp.
* **Systems Architect (Kiến trúc sư hệ thống):** Thiết kế cấu trúc kỹ thuật tổng quan của phần mềm, định cấu hình tương tác thành phần và môi trường vận hành.
* **Solution Architect (Kiến trúc sư giải pháp):** Chịu trách nhiệm thiết kế các giải pháp ứng dụng cụ thể và tích hợp chúng vào hệ thống chung.
* **Infrastructure Architect (Kiến trúc sư hạ tầng):** Tập trung vào lớp phần cứng, mạng, máy chủ và cơ sở dữ liệu nền tảng.
* **Security Architect (Kiến trúc sư bảo mật):** Thiết kế và lồng ghép cơ chế an ninh bảo mật vào toàn bộ kiến trúc hệ thống.
