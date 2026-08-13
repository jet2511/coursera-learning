# Glossary: Introducing the Systems Architect Role

- **Khóa học:** IBM System Design
- **Module:** 01. Fundamentals of Systems Architecture \ Module 1 - Introducing the Systems & Solutions Architect Roles
- **Nội dung:** Thuật ngữ chuyên ngành cốt lõi trong Module 1.

---

| Thuật ngữ (Term) | Định nghĩa (Definition) | Giải thích chi tiết / Ứng dụng |
| :--- | :--- | :--- |
| **Agentic AI** | Hệ thống AI tự chủ hành động để hoàn thành mục tiêu, sử dụng các công cụ/model chuyên biệt để tạo ra thiết kế linh hoạt, sẵn sàng cho tương lai. | Ứng dụng AI tự ra quyết định và thực thi task tự động thay vì chỉ trả lời văn bản. |
| **Application programming interface (API) design** | Thiết kế giao diện lập trình ứng dụng – cấu trúc giao tiếp giữa các hệ thống thông qua các dịch vụ RESTful, GraphQL hoặc API gateway. | Đảm bảo luồng trao đổi dữ liệu mượt mà, bảo mật và chuẩn hóa giữa các dịch vụ. |
| **Architecture review** | Đánh giá kiến trúc – quy trình đánh giá các thay đổi đề xuất để đảm bảo tính đồng bộ với nguyên tắc tổ chức, khả năng mở rộng và bảo mật. | Giúp kiểm soát rủi ro hệ thống trước khi triển khai các tính năng lớn. |
| **Business analyst** | Nhà phân tích nghiệp vụ – chuyên gia cung cấp chuyên môn về domain và phân tích quy trình kinh doanh, đảm bảo quyết định công nghệ phù hợp với ưu tiên của tổ chức. | Cầu nối dịch các yêu cầu nghiệp vụ thành ngôn ngữ kỹ thuật cơ bản. |
| **Caching** | Bộ nhớ đệm – kỹ thuật lưu trữ dữ liệu thường xuyên truy cập ở một tầng tạm thời tốc độ cao (như RAM) để giảm tải cho DB/ổ đĩa. | Sử dụng các công cụ như Redis, Memcached nhằm tối ưu hiệu năng và tốc độ phản hồi. |
| **Cloud computing** | Điện toán đám mây – cung cấp tài nguyên điện toán (lưu trữ, server, ứng dụng) qua Internet (AWS, Azure, GCP, IBM Cloud...). | Giúp hệ thống dễ dàng mở rộng linh hoạt mà không cần tự duy trì phần cứng vật lý. |
| **Cloud migration** | Di cư đám mây – quá trình chuyển dịch ứng dụng, khối lượng công việc và hạ tầng lên các nền tảng cloud. | Thường liên quan đến chiến lược đám mây lai (hybrid) hoặc đa đám mây (multi-cloud). |
| **Continuous integration/Continuous deployment (CI/CD)** | Tích hợp liên tục/Triển khai liên tục – thực hành DevOps sử dụng các công cụ tự động (Jenkins, GitLab CI, GitHub Actions) để tinh giản quy trình build, test, deploy. | Đảm bảo tốc độ phát hành tính năng nhanh và giảm thiểu lỗi thủ công khi phát hành. |
| **Data architecture** | Kiến trúc dữ liệu – thiết kế hệ sinh thái dữ liệu bao gồm data lake, data warehouse, quy trình ETL, và các công cụ như Kafka, Spark. | Tổ chức lưu trữ dữ liệu hiệu quả và phục vụ phân tích dữ liệu lớn. |
| **DevOps engineer** | Kỹ sư DevOps – cầu nối giữa phát triển (Dev) và vận hành (Ops), hỗ trợ triển khai, giám sát và bảo trì hệ thống. | Giúp xây dựng và vận hành hạ tầng tự động hóa cho kiến trúc sư thiết kế. |
| **Disinformation detection** | Phát hiện thông tin sai lệch – khả năng bảo mật được tích hợp vào kiến trúc hệ thống để xác định và giảm thiểu nội dung số sai lệch. | Ứng dụng quan trọng trong bảo mật thông tin và quản trị nội dung. |
| **Enterprise architecture** | Kiến trúc doanh nghiệp – chịu trách nhiệm đồng bộ hóa các thiết kế hệ thống riêng lẻ với các tiêu chuẩn chung và chiến lược công nghệ dài hạn của toàn doanh nghiệp. | Đảm bảo các hệ thống của các phòng ban khác nhau không bị rời rạc, chồng chéo. |
| **Hybrid cloud** | Đám mây lai – chiến lược tích hợp các dịch vụ đám mây công cộng (public cloud) và đám mây riêng tư (private cloud). | Giúp cân bằng giữa tính linh hoạt của cloud công cộng và độ bảo mật của hạ tầng vật lý riêng. |
| **Infrastructure architect** | Kiến trúc sư hạ tầng – chuyên gia tập trung vào các tầng công nghệ nền tảng (server, mạng, database) nhằm đảm bảo tính tin cậy và khả năng mở rộng. | Thiết kế cấu trúc mạng, cụm server vật lý hoặc ảo hóa để hỗ trợ ứng dụng. |
| **Load balancing** | Cân bằng tải – phương pháp phân phối khối lượng công việc trên nhiều tài nguyên máy tính để tối ưu hóa hiệu năng và tính sẵn sàng. | Tránh tình trạng quá tải ở một server đơn lẻ, tăng tính chịu lỗi của hệ thống. |
| **Mentoring** | Cố vấn – hoạt động cốt lõi nơi các kiến trúc sư cấp cao hướng dẫn các chuyên gia cấp dưới. | Chia sẻ tri thức kiến trúc và phát triển năng lực nội bộ của tổ chức. |
| **Multi-cloud expertise** | Chuyên môn đa đám mây – khả năng quản lý và tích hợp đồng thời nhiều nhà cung cấp cloud khác nhau (AWS, Azure, GCP...). | Giúp giảm rủi ro phụ thuộc vào một nhà cung cấp duy nhất (vendor lock-in). |
| **Pega Certified System Architect (CSA)** | Chứng chỉ sơ cấp về tự động hóa quy trình nghiệp vụ bằng nền tảng Pega. | Mở ra cơ hội phát triển trong lĩnh vực tự động hóa quy trình (BPA). |
| **Problem resolution** | Giải quyết vấn đề – hoạt động phân tích sự cố hệ thống, tìm nguyên nhân gốc rễ (Root Cause Analysis - RCA) và thiết kế giải pháp khắc phục. | Nhiệm vụ phản ứng nhanh khi hệ thống gặp sự cố production nghiêm trọng. |
| **Retrieval-augmented generation (RAG)** | Thế tạo tăng cường truy xuất – kỹ thuật AI kết hợp mô hình ngôn ngữ lớn (LLM) với việc truy xuất kiến thức bên ngoài. | Giúp câu trả lời của AI chính xác hơn, có ngữ cảnh thực tế của doanh nghiệp. |
| **Security architect** | Kiến trúc sư bảo mật – chuyên gia nhúng các nguyên tắc bảo mật, tuân thủ và chiến lược giảm thiểu rủi ro trực tiếp vào thiết kế hệ thống. | Thiết kế hệ thống phòng thủ trước các cuộc tấn công mạng. |
| **Security-first design** | Thiết kế ưu tiên bảo mật – phương pháp xem xét bảo mật và quản lý rủi ro ngay từ đầu khi lập kế hoạch hệ thống. | Ngăn ngừa tối đa các lỗ hổng trước khi đưa code lên môi trường chạy thực tế. |
| **Senior developer** | Lập trình viên cấp cao – hỗ trợ tính khả thi của kiến trúc, xác thực thiết kế và cố vấn lập trình viên cấp dưới. | Hiện thực hóa các thiết kế trừu tượng của kiến trúc sư thành code thực tế. |
| **Solution architect** | Kiến trúc sư giải pháp – chịu trách nhiệm thiết kế các ứng dụng hoặc giải pháp riêng lẻ và đảm bảo chúng tích hợp tốt vào hệ thống chung. | Tập trung vào giải quyết một bài toán cụ thể của khách hàng/dự án. |
| **Stakeholder management** | Quản lý bên liên quan – thực hành tương tác với các bên liên quan về mặt kinh doanh và kỹ thuật để thống nhất mục tiêu. | Giúp kiến trúc sư dung hòa lợi ích giữa mong muốn của kinh doanh và giới hạn của kỹ thuật. |
| **Systems analyst** | Nhà phân tích hệ thống – thu thập các yêu cầu kinh doanh và dịch chúng thành đặc tả chức năng (functional specs). | Đưa ra các luồng dữ liệu (data flow) cụ thể để phục vụ việc lập trình. |
| **Systems thinking** | Tư duy hệ thống – tư duy hiểu cách các thành phần riêng lẻ tương tác với nhau trong toàn hệ sinh thái. | Đảm bảo khi thay đổi một component không gây ra hiệu ứng sập dây chuyền ở nơi khác. |
| **Technical project manager** | Quản lý dự án kỹ thuật – điều phối các sáng kiến kiến trúc, sắp xếp tài nguyên và lịch trình để đảm bảo thành công của dự án. | Giữ dự án đi đúng hướng về mặt thời gian và nguồn lực. |
| **The Open Group Architecture Framework (TOGAF)** | Khung kiến trúc doanh nghiệp hàng đầu cung cấp phương pháp luận và cấu trúc để đồng bộ hóa IT với chiến lược kinh doanh. | Chuẩn công nghiệp được thừa nhận rộng rãi để thiết kế kiến trúc doanh nghiệp. |
| **Zero-trust architecture** | Kiến trúc không tin cậy – mô hình bảo mật giả định không có sự tin cậy ngầm định, yêu cầu xác thực liên tục mọi thực thể. | "Never trust, always verify" (Không bao giờ tin tưởng, luôn luôn xác thực) đối với mọi user, thiết bị. |
