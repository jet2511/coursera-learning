# Tools of a Systems Architect (Các công cụ của Kiến trúc sư Hệ thống)

Bản tóm tắt nội dung học tập về các công cụ cốt lõi được sử dụng bởi Kiến trúc sư Hệ thống trong suốt vòng đời phát triển dự án.

---

### 1. Thu thập yêu cầu (Requirements Gathering)
Hỗ trợ xác định chính xác nhu cầu của người dùng và các bên liên quan trước khi thiết kế hệ thống.
*   **Phỏng vấn (Interviews - Cá nhân/Nhóm):** Thu thập thông tin định tính trực tiếp từ người dùng cuối và stakeholders.
*   **Khảo sát & Bảng câu hỏi (Surveys & Questionnaires):** Thu thập dữ liệu định lượng từ quy mô mẫu lớn một cách nhanh chóng khi bị giới hạn thời gian.
*   **Quan sát thực tế (Observation Sessions):** Xem cách người dùng tương tác trực tiếp với hệ thống hiện tại để nhận diện các bất cập hoặc hành vi thực tế không được báo cáo trong phỏng vấn.
*   **Đánh giá tài liệu hiện có (Documentation Review):** Nghiên cứu tài liệu hướng dẫn hệ thống cũ, sơ đồ tổ chức và báo cáo quy trình để tìm ra các điểm nghẽn (pain points).

### 2. Mô hình hóa hệ thống (System Modeling)
Giúp trực quan hóa cấu trúc, quy trình và luồng dữ liệu của hệ thống, tạo ngôn ngữ chung giữa stakeholders và đội ngũ phát triển.
*   **Sơ đồ luồng dữ liệu (Data Flow Diagrams - DFDs):** Thể hiện sự di chuyển của dữ liệu từ đầu vào (Input) -> xử lý (Processing) -> đầu ra (Output), đồng thời định vị nguồn dữ liệu và các kho chứa (storage).
*   **Sơ đồ quan hệ thực thể (Entity Relationship Diagrams - ERDs):** Thiết kế cấu trúc cơ sở dữ liệu, định nghĩa thực thể (entities) và mối liên kết (relationships) giữa chúng.
*   **Sơ đồ ca sử dụng (Use Case Diagrams - UML):** Mô tả cách người dùng (actors) tương tác với hệ thống để hoàn thành một nhiệm vụ cụ thể.
*   **Lưu đồ quy trình (Process Flowcharts):** Trực quan hóa tuần tự các bước xử lý trong một quy trình kinh doanh hoặc nghiệp vụ, giúp phát hiện sự trùng lặp hoặc kém hiệu quả.

### 3. Quản lý dự án (Project Management)
Cung cấp công cụ lập kế hoạch, phân bổ nguồn lực và kiểm soát tiến độ.
*   **Sơ đồ Gantt (Gantt charts):** Trực quan hóa dòng thời gian, các phân đoạn dự án, thời hạn (deadlines) và các mối quan hệ phụ thuộc lẫn nhau.
*   **Sơ đồ PERT (Program Evaluation Review Technique):** Biểu diễn chuỗi liên kết các công việc, hỗ trợ ước lượng thời gian hoàn thành tối ưu và xác định đường găng (critical path).
*   **Phần mềm quản lý tác vụ:** *Microsoft Project, Trello, Asana, Jira* giúp giao việc, giám sát trạng thái và tối ưu hóa vận hành nhóm.

### 4. Thiết kế cơ sở dữ liệu (Database Design)
Giúp xây dựng cấu trúc lưu trữ tối ưu, giảm thiểu lỗi thiết kế và đảm bảo hiệu năng, khả năng mở rộng.
*   **Công cụ phổ biến:** *MySQL Workbench, Oracle SQL Developer, ER Studio*.
*   **Tính năng chính:** Mô hình hóa schema, thiết kế cấu trúc quan hệ, tự động sinh mã cấu trúc (SQL scripts) và trực quan hóa liên kết dữ liệu.

### 5. Thiết kế giao diện & Bản mẫu (Wireframing & Prototyping)
Hỗ trợ kiểm thử sớm các tính năng và trải nghiệm trước khi bước vào giai đoạn code thực tế.
*   **Khung xương giao diện (Wireframing - Low-fidelity):** Phác thảo nhanh giao diện tĩnh. Công cụ tiêu biểu: *Balsamiq, Figma, Adobe XD*.
*   **Bản mẫu tương tác (Interactive Prototyping - High/Medium-fidelity):** Tạo mẫu thử có thể click và điều hướng để mô phỏng trải nghiệm người dùng thực tế. Công cụ tiêu biểu: *Axure RP, Sketch*.

### 6. Hợp tác & Giao tiếp (Collaboration & Communication)
Đảm bảo thông tin của dự án đồng bộ xuyên suốt từ giai đoạn phân tích đến vận hành.
*   **Quản lý tài liệu:** *Microsoft Word, Confluence, Google Docs* dùng để lưu trữ đặc tả yêu cầu hệ thống, biên bản họp và tài liệu kiến trúc.
*   **Kênh truyền thông:** *Slack, Microsoft Teams, Zoom* phục vụ thảo luận trực tuyến, đặc biệt hiệu quả với các nhóm làm việc từ xa.
*   **Hệ thống kiểm soát phiên bản (Version Control Systems):** *Git, GitHub, Bitbucket* quản lý lịch sử thay đổi mã nguồn, sơ đồ thiết kế và tài liệu dự án một cách an toàn.
