# Thuật ngữ Khóa học: Software Testing, Deployment, and Maintenance Strategies

> **Khóa học:** IBM System Design — Course 08 (Module 4 Glossary)  
> **Mục tiêu:** Hệ thống hóa toàn bộ các thuật ngữ cốt lõi theo từng nhóm chủ đề kiến trúc, kiểm thử, phát hành và bảo trì.

---

## 1. Kiểm thử phần mềm & Đảm bảo chất lượng (Software Testing & QA)

- **Anatomy of a test case:** Cấu trúc chi tiết của một test case gồm: ID, mục tiêu (objective), dữ liệu đầu vào (input data), các bước thực hiện (steps) và kết quả kỳ vọng (expected results).
- **Unit testing:** Kiểm thử đơn vị cô lập trên từng hàm/phương thức mã nguồn cụ thể.
- **Integration testing:** Kiểm thử tích hợp khi kết hợp các module/dịch vụ lại với nhau để đánh giá giao tiếp và ràng buộc hợp đồng (contract).
- **System testing:** Kiểm thử toàn diện toàn bộ hệ thống tích hợp hoàn chỉnh đối chiếu với tài liệu yêu cầu.
- **UAT (User Acceptance Testing):** Kiểm thử chấp nhận người dùng, do người dùng thật thực hiện để xác nhận phần mềm đáp ứng nhu cầu thực tế trước khi Go-Live.
- **TDD (Test-Driven Development):** Phương pháp viết test trước khi viết mã nguồn, dùng test để dẫn dắt thiết kế hệ thống.
- **BDD (Behavior-Driven Development):** Phát triển hướng hành vi, viết kịch bản test bằng ngôn ngữ tự nhiên từ góc nhìn người dùng.
- **Gherkin syntax:** Cú pháp văn bản thuần có cấu trúc dùng trong BDD với các từ khóa: `Given`, `When`, `Then`.
- **Traceability matrix:** Ma trận truy vết ánh xạ từ yêu cầu nghiệp vụ (Requirements/Use cases) sang Test Case IDs, đảm bảo bao phủ 100% phạm vi kiểm thử.
- **Test coverage:** Chỉ số đo lường mức độ bao phủ của bộ test đối với mã nguồn hoặc yêu cầu tính năng.
- **Edge cases:** Các điều kiện biên/cực trị bất thường dùng để thử thách giới hạn chịu đựng của hệ thống.

---

## 2. Di chuyển dữ liệu & Toàn vẹn hệ thống (Data Migration & Integrity)

- **Data migration:** Quá trình chuyển dịch dữ liệu từ hệ thống cũ sang nền tảng mới trong đợt nâng cấp.
- **Data mapping / Mapping template:** Kỹ thuật và biểu mẫu định nghĩa cách ánh xạ từng trường dữ liệu nguồn (Source field) sang trường đích (Target field) kèm quy tắc biến đổi.
- **Data cleansing:** Làm sạch, chuẩn hóa và khắc phục dữ liệu sai lệch trước khi di chuyển.
- **Data validation:** Quy trình kiểm tra dữ liệu sau di chuyển đảm bảo tính đầy đủ, chính xác và nhất quán.
- **Field-level validation:** Kiểm tra chi tiết định dạng, kiểu dữ liệu và nội dung của từng trường riêng lẻ.
- **Data sampling:** Chọn ngẫu nhiên một tập mẫu bản ghi để đối soát thủ công sau di chuyển.
- **Checksum:** Giá trị băm số học (MD5, SHA-256) dùng để phát hiện lỗi hoặc sai lệch dữ liệu trong quá trình truyền tải.
- **Cutover:** Thời khắc chuyển đổi hoạt động vận hành chính thức từ hệ thống cũ sang hệ thống mới.

---

## 3. Triển khai, Vận hành & Dự phòng (Deployment, Release & DR)

- **Deployment window:** Khoảng thời gian bảo trì định trước để triển khai hệ thống nhằm giảm thiểu gián đoạn kinh doanh (ví dụ: đêm Thứ Bảy).
- **Go/no-go decision:** Cổng chốt quyết định tại thời điểm then chốt, dựa trên tiêu chí sẵn sàng để quyết định tiến hành triển khai hay dừng lại.
- **Rollback / Rollback strategy:** Quy trình và kế hoạch hoàn nguyên hệ thống về phiên bản ổn định trước đó khi gặp lỗi nghiêm trọng sau phát hành.
- **Fallback plan:** Tập hợp các bước định sẵn để khôi phục trạng thái ban đầu nếu triển khai thất bại.
- **Post-deployment review / Post-mortem:** Buổi họp hồi tưởng phân tích nguyên nhân gốc rễ (Root Cause Analysis - RCA) sau sự cố để phòng ngừa tái diễn.
- **Active/Active model:** Mô hình DR chạy đồng thời nhiều môi trường sản xuất trên nhiều vùng (Multi-region), đảm bảo zero-downtime với chi phí vận hành cao hơn.
- **Pilot light:** Mô hình DR duy trì các thành phần dữ liệu cốt lõi luôn chạy, các tài nguyên khác chỉ bật lên khi có thảm họa nhằm tiết kiệm chi phí.
- **RPO (Recovery Point Objective):** Khoảng thời gian mất mát dữ liệu tối đa chấp nhận được (tính bằng thời gian).
- **RTO (Recovery Time Objective):** Thời gian tối đa cho phép hệ thống ngừng hoạt động trước khi được khôi phục.
- **Immutable backup:** Bản sao lưu bất biến không thể bị sửa đổi hoặc xóa, chống lại mã độc tống tiền (ransomware).

---

## 4. Yêu cầu phi chức năng & Giám sát hiệu năng (NFRs & Observability)

- **Non-functional requirements (NFRs):** Đặc tả các tiêu chuẩn chất lượng hệ thống như hiệu năng, độ co giãn, độ sẵn sàng và bảo mật (định nghĩa hệ thống hoạt động tốt như thế nào).
- **Observability:** Khả năng thấu hiểu trạng thái bên trong hệ thống thông qua việc thu thập và phân tích 3 trụ cột: **Metrics, Logs, Traces**.
- **Golden signals (4 Tín hiệu vàng SRE):**
  1. *Latency:* Thời gian trễ xử lý request (ms).
  2. *Traffic:* Mức độ tải / nhu cầu lên hệ thống (RPS, concurrent users).
  3. *Errors:* Tỷ lệ lỗi trên tổng số yêu cầu (ví dụ: HTTP 5xx rate).
  4. *Saturation:* Mức độ bão hòa tài nguyên (CPU, RAM, DB connection pool).
- **Capacity planning:** Cân bằng giữa tài nguyên cung cấp hiện tại với nhu cầu dự kiến trong tương lai:
  - *Lead strategy:* Bổ sung tài nguyên đón đầu trước khi nhu cầu tăng (an toàn nhưng tốn kém).
  - *Match strategy:* Điều chỉnh tài nguyên linh hoạt theo từng bước nhỏ bám sát nhu cầu đo lường được.
- **Auto-scaling / Horizontal scaling:** Tự động mở rộng tài nguyên tính toán (thêm pods/instances) theo chiều ngang để chia sẻ tải.
- **Asynchronous processing:** Đẩy các tác vụ tốn thời gian ra hàng đợi ngầm (Queue) để tránh chặn luồng giao diện người dùng.
- **Caching:** Lưu tạm dữ liệu truy cập thường xuyên (ví dụ: Redis) vào bộ nhớ để giảm tải truy vấn cơ sở dữ liệu.
- **Chatty APIs:** Giao diện gọi mạng quá nhiều lần liên tiếp gây tăng độ trễ và giảm khả năng mở rộng.
- **Resource utilization rate:** Tỷ lệ sử dụng tài nguyên so với công suất tối đa, lý tưởng duy trì ở mức **70% – 80%** để có vùng đệm an toàn.
