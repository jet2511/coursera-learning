# Prototyping and Simulation Tools (Các công cụ tạo bản mẫu và mô phỏng)

Bản tóm tắt nội dung học tập về định nghĩa, phân loại, công cụ và sự tích hợp giữa tạo bản mẫu (Prototyping) và mô phỏng (Simulation) trong phân tích hệ thống.

---

### 1. Tạo bản mẫu (Prototyping)
Là quá trình xây dựng một phiên bản đơn giản hóa của hệ thống (mẫu thử làm việc - working model) nhằm kiểm thử tính năng, thu thập phản hồi và tinh chỉnh ý tưởng thiết kế.
*   **Lợi ích:** Xác nhận yêu cầu của người dùng, giảm thiểu hiểu lầm giữa các bên liên quan và lập trình viên, cho phép lặp và tối ưu hóa thiết kế nhanh chóng.
*   **Phân loại theo độ chi tiết (Fidelity):**
    *   *Low-fidelity (Độ trung thực thấp):* Sơ đồ phác thảo trên giấy, khung xương giao diện tĩnh.
    *   *High-fidelity (Độ trung thực cao):* Bản mẫu kỹ thuật số tương tác được.
*   **Bốn loại bản mẫu chính:**
    1.  *Nhanh/Dùng một lần (Throwaway/Rapid):* Dựng nhanh để kiểm tra khái niệm rồi bỏ đi.
    2.  *Tiến hóa (Evolutionary):* Được nâng cấp và cải tiến liên tục cho đến khi trở thành hệ thống chính thức.
    3.  *Gia tăng (Incremental):* Xây dựng từng phần/mô-đun riêng lẻ của hệ thống.
    4.  *Cực đoan (Extreme):* Thường áp dụng cho ứng dụng web qua 3 pha: Trang HTML tĩnh -> Mô phỏng chức năng -> Tích hợp dịch vụ backend.
*   **Công cụ tiêu biểu:**
    *   *Balsamiq:* Dựng khung xương (wireframe) tĩnh nhanh chóng ở giai đoạn đầu.
    *   *Figma, Adobe XD, Sketch:* Thiết kế giao diện chất lượng cao, hỗ trợ làm việc nhóm.
    *   *Axure RP:* Tạo tương tác nâng cao với logic điều kiện và luồng xử lý phức tạp.
    *   *InVision:* Chia sẻ bản mẫu tương tác trực tuyến để lấy ý kiến phản hồi.
*   **Thời điểm áp dụng:** Giai đoạn thiết kế ban đầu; cần xác thực giao diện/tính năng với người dùng; yêu cầu nghiệp vụ chưa rõ ràng; ưu tiên tốc độ hơn sự chi tiết.

---

### 2. Mô phỏng (Simulation)
Là việc xây dựng mô hình giả lập hành vi của một quy trình hoặc hệ thống thực tế để kiểm tra các kịch bản, dự đoán kết quả và đánh giá hiệu năng mà không gây ảnh hưởng đến hệ thống đang vận hành.
*   **Lợi ích:** Kiểm thử hiệu năng hệ thống dưới tải trọng cao (load testing), mô hình hóa quy trình ra quyết định, nhận diện trước các điểm nghẽn (bottlenecks).
*   **Môi trường áp dụng:** 
    *   *Hệ thống kỹ thuật:* Cấu trúc mạng, cấu hình máy chủ.
    *   *Quy trình nghiệp vụ:* Luồng xử lý đơn hàng, chuỗi cung ứng, dịch vụ khách hàng.
*   **Công cụ tiêu biểu:**
    *   *Simul8, Arena, AnyLogic:* Phần mềm chuyên nghiệp giả lập quy trình và hệ thống.
    *   *Microsoft Visio:* Thiết lập bản đồ quy trình (không phải công cụ mô phỏng độc lập).
    *   *BPMN Tools (như Bizagi):* Mô phỏng quy trình nghiệp vụ theo chuẩn BPMN.
    *   *NetLogo, MATLAB, Simulink:* Mô phỏng dựa trên tác nhân (agent-based) hoặc mô phỏng mức độ hệ thống kỹ thuật sâu.
*   **Thời điểm áp dụng:** Cần kiểm thử hành vi của quy trình phức tạp; hiệu năng và khả năng mở rộng (scalability) là ưu tiên hàng đầu; cần đánh giá rủi ro vận hành; cần số liệu định lượng (quantitative data) để ra quyết định.

---

### 3. Sự tích hợp giữa Prototyping và Simulation trong SDLC
*   **Pha phân tích yêu cầu (Requirements Analysis):** Sử dụng các bản mẫu nhanh (Rapid Prototypes) để nắm bắt và làm mịn nhu cầu người dùng.
*   **Pha thiết kế (Design):** Sử dụng bản mẫu chi tiết hoặc các mô hình mô phỏng kỹ thuật để hỗ trợ ra quyết định lựa chọn kiến trúc hạ tầng.
*   **Pha kiểm thử (Testing):** Sử dụng mô phỏng (Simulation) để xác định giới hạn chịu tải và hiệu năng hệ thống trong các điều kiện khắc nghiệt, đồng thời tiếp tục dùng bản mẫu (Prototypes) để kiểm thử trải nghiệm sử dụng (usability testing).
