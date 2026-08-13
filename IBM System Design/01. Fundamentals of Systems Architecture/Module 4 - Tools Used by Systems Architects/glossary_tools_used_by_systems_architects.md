# Glossary: Tools Used by Systems Architects (Thuật ngữ các công cụ dành cho Kiến trúc sư Hệ thống)

Bản tra cứu nhanh các thuật ngữ và định nghĩa về công cụ được phân loại theo từng mục đích sử dụng trong thiết kế kiến trúc hệ thống.

---

### 1. Thiết kế sơ đồ & Mô hình hóa hệ thống (UML & System Diagramming)

| Thuật ngữ | Định nghĩa |
| :--- | :--- |
| **UML diagrams** | Các mô hình trực quan hóa chuẩn hóa để mô tả cấu trúc tĩnh và hành vi động của hệ thống, bao gồm sơ đồ ca sử dụng, sơ đồ lớp, sơ đồ tuần tự và sơ đồ hoạt động. |
| **Activity diagram** | Sơ đồ UML mô tả luồng công việc hoặc quy trình trong hệ thống. Tương tự như flowchart nhưng tuân theo chuẩn UML; sử dụng các nút hoạt động, quyết định, nút bắt đầu/kết thúc và các luồng chuyển tiếp để trực quan hóa luồng điều khiển. |
| **Class diagram** | Sơ đồ UML dùng để mô hình hóa hệ thống hướng đối tượng bằng cách định nghĩa các Lớp (Classes), thuộc tính, phương thức và các mối liên kết/kế thừa giữa các lớp. |
| **Sequence diagram** | Sơ đồ UML tập trung vào sự tương tác giữa các thành phần hệ thống theo thời gian thông qua các thông điệp (messages) được truyền giữa các đối tượng hoặc tác nhân (actors). |
| **Use case diagrams** | Sơ đồ UML chỉ ra cách người dùng (actors) tương tác với hệ thống để đạt được các mục tiêu cụ thể (use cases). Rất hữu ích trong pha phân tích để xác định yêu cầu chức năng. |
| **Data flow diagrams (DFDs)** | Sơ đồ biểu diễn trực quan cách dữ liệu di chuyển qua hệ thống (đầu vào, xử lý, lưu trữ, đầu ra) thông qua các ký hiệu chuẩn cho quy trình, kho dữ liệu, thực thể ngoài và luồng dữ liệu. |
| **Entity relationship diagrams (ERDs)** | Sơ đồ dùng để mô hình hóa dữ liệu bằng cách định nghĩa các thực thể (entities), thuộc tính (attributes) và mối quan hệ (relationships). Hỗ trợ chuẩn hóa cơ sở dữ liệu. |
| **Process flowcharts** | Lưu đồ ánh xạ tuần tự từng bước của các hoạt động hoặc quyết định trong một quy trình giúp làm rõ quy trình làm việc và tìm kiếm cải tiến. |

---

### 2. Thiết kế giao diện & Bản mẫu (Wireframing & Prototyping)

| Thuật ngữ | Định nghĩa |
| :--- | :--- |
| **Wireframing tools** | Phần mềm thiết kế bố cục trực quan cơ bản (khung xương) của ứng dụng hoặc giao diện hệ thống trước khi bắt tay vào thiết kế chi tiết. |
| **Prototyping tools** | Công cụ hỗ trợ xây dựng các mô hình tương tác (clickable mock-ups) của hệ thống hoặc ứng dụng để thử nghiệm và lấy feedback trước khi phát triển chính thức. |
| **Balsamiq** | Công cụ vẽ wireframe tĩnh có độ trung thực thấp (low-fidelity) thích hợp cho giai đoạn đầu của dự án nhằm phác thảo nhanh ý tưởng giao diện. |
| **Figma** | Công cụ thiết kế giao diện cộng tác trực tuyến mạnh mẽ, dùng để vẽ wireframes, thiết kế UI/UX và tạo bản mẫu (prototypes) tương tác. |
| **Axure RP** | Công cụ tạo bản mẫu nâng cao hỗ trợ các logic tương tác phức tạp, luồng điều kiện (conditional flows) và giả lập chức năng chi tiết. |
| **InVision** | Nền tảng đám mây hỗ trợ tải các bản thiết kế tĩnh lên và liên kết chúng thành bản mẫu có thể click, hỗ trợ lấy phản hồi nhanh từ stakeholders. |

---

### 3. Phân tích dữ liệu & Trí tuệ doanh nghiệp (Data Analysis & BI)

| Thuật ngữ | Định nghĩa |
| :--- | :--- |
| **Data analysis tools** | Phần mềm xử lý và diễn giải dữ liệu, giúp phát hiện các mẫu (patterns), xu hướng và insight phục vụ ra quyết định. |
| **Data visualization** | Trực quan hóa dữ liệu bằng đồ họa (biểu đồ, đồ thị, dashboard) để truyền tải thông tin phân tích rõ ràng. |
| **Business intelligence (BI) tools** | Các nền tảng tích hợp phân tích và trực quan hóa dữ liệu thành các real-time dashboards, báo cáo tự động và quản lý phân quyền (ví dụ: Tableau, Power BI, Qlik Sense, Looker). |
| **Python** | Ngôn ngữ lập trình phổ biến bậc nhất trong tự động hóa, phân tích dữ liệu và học máy thông qua các thư viện mở rộng như Pandas, NumPy, Matplotlib. |
| **Python visualization libraries** | Các thư viện hỗ trợ tự do tùy biến biểu đồ như *Matplotlib, Seaborn, Plotly*, dễ tích hợp vào luồng dữ liệu tự động. |
| **R** | Ngôn ngữ lập trình chuyên sâu về tính toán thống kê, phân tích dữ liệu và vẽ đồ thị, được dùng rộng rãi trong nghiên cứu và học thuật. |
| **SPSS Statistics** | Phần mềm phân tích thống kê thương mại của IBM; cung cấp giao diện đồ họa (GUI) thân thiện và không yêu cầu người dùng phải viết mã. |
| **Scikit-learn** | Thư viện mã nguồn mở của Python cung cấp các công cụ mạnh mẽ và linh hoạt cho học máy (machine learning) và phân tích dự báo. |
| **Google's Looker** | Nền tảng BI cloud-native thuộc hệ sinh thái Google Cloud phục vụ các nhóm dữ liệu hiện đại. |
| **Microsoft Power BI** | Nền tảng BI tích hợp sâu với Excel và Azure của Microsoft. |
| **Tableau** | Công cụ trực quan hóa dữ liệu hàng đầu hỗ trợ kết nối đa nguồn dữ liệu và thiết lập báo cáo trực quan sinh động. |
| **Qlik Sense** | Công cụ BI hỗ trợ tìm kiếm insight thông qua phân tích liên kết (associative analysis) và khả năng tích hợp dữ liệu mạnh mẽ. |

---

### 4. Thiết kế & Quản lý cơ sở dữ liệu (Database Design & Management)

| Thuật ngữ | Định nghĩa |
| :--- | :--- |
| **ER Studio** | Công cụ mô hình hóa dữ liệu chuyên sâu để thiết kế và quản trị các cơ sở dữ liệu doanh nghiệp quy mô lớn và phức tạp. |
| **MySQL Workbench** | Công cụ tích hợp dành cho nhà quản trị và lập trình viên MySQL hỗ trợ thiết kế, mô hình hóa, thực thi truy vấn và quản trị máy chủ. |
| **Oracle SQL Developer** | Môi trường phát triển tích hợp (IDE) miễn phí giúp đơn giản hóa việc phát triển và quản trị cơ sở dữ liệu Oracle. |

---

### 5. Mô phỏng quy trình (Simulation)

| Thuật ngữ | Định nghĩa |
| :--- | :--- |
| **Simulation tools** | Phần mềm (*Arena, AnyLogic, MATLAB, Simulink*) bắt chước hành vi của hệ thống thực tế để kiểm thử hiệu năng, độ chịu tải và rủi ro trong nhiều kịch bản khác nhau. |
| **BPMN tools** | Công cụ mô phỏng quy trình nghiệp vụ theo chuẩn ký hiệu BPMN (ví dụ: *Bizagi*) để tài liệu hóa và tối ưu hóa hiệu quả vận hành. |

---

### 6. Quản lý dự án & Tác vụ (Project & Task Management)

| Thuật ngữ | Định nghĩa |
| :--- | :--- |
| **Systems management software** | Phần mềm giám sát, cấu hình và quản trị hệ thống công nghệ thông tin. Các công cụ như *Jira, Trello, Asana* thuộc nhóm này khi hỗ trợ quản lý công việc và cộng tác. |
| **Gantt charts** | Sơ đồ biểu diễn tiến độ dự án theo dòng thời gian thể hiện các đầu việc, thời hạn và mối quan hệ phụ thuộc. |
| **PERT charts** | Sơ đồ mạng lưới công việc thể hiện trình tự thực hiện, sự phụ thuộc chéo và ước lượng thời gian để tìm ra đường găng (critical path) của dự án. |
| **Jira** | Công cụ theo dõi lỗi và quản lý dự án Agile phổ biến của Atlassian, quản lý công việc qua Scrum/Kanban boards. |
| **Trello** | Công cụ quản lý trực quan giao diện Kanban đơn giản (card-based) phù hợp cho các dự án nhỏ và vừa. |
| **Asana** | Công cụ lập kế hoạch dự án hỗ trợ giao việc và cập nhật trạng thái giữa các phòng ban. |
| **Notion** | Không gian làm việc linh hoạt kết hợp viết tài liệu, quản lý tác vụ và xây dựng cơ sở dữ liệu nhỏ trong một nền tảng duy nhất. |

---

### 7. Cộng tác & Giao tiếp (Collaboration & Communication)

| Thuật ngữ | Định nghĩa |
| :--- | :--- |
| **Documentation tools** | Các ứng dụng biên soạn và lưu trữ tài liệu đặc tả hệ thống và kỹ thuật (ví dụ: Word, Confluence, Google Docs). |
| **Confluence** | Nền tảng tài liệu cộng tác của Atlassian, thường đi kèm Jira để quản lý Wiki dự án và tài liệu kiến trúc. |
| **Google Workspace** | Bộ công cụ năng suất đám mây (Gmail, Drive, Docs, Sheets, Slides) hỗ trợ cộng tác đồng biên tập theo thời gian thực. |
| **Microsoft Teams** | Nền tảng giao tiếp doanh nghiệp tích hợp hội thoại, chat và chia sẻ tài liệu đồng bộ trong Microsoft 365. |
| **Slack** | Nền tảng giao tiếp qua các kênh (channels) theo chủ đề, giúp giảm tải lượng email nội bộ. |
| **Zoom** | Nền tảng hội thảo video hỗ trợ họp trực tuyến, chia sẻ màn hình và demo hệ thống từ xa. |
