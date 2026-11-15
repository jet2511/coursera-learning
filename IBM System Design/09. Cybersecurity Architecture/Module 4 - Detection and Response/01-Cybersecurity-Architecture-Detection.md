# Cybersecurity Architecture: Detection

> **Khóa học**: Cybersecurity Architecture (IBM)  
> **Module 4**: Detecting Cyberattacks and Creating a Response  
> **Bài học**: Cybersecurity Architecture: Detection (Thời lượng: ~17 phút)

---

## 📌 Tổng Quan (Overview)

Trong mô hình kiến trúc an ninh mạng tổng thể:
- **Tam giác CIA (CIA Triad)**: Confidentiality (Bảo mật), Integrity (Toàn vẹn), Availability (Khả dụng) chính là **MỤC TIÊU CỐT LÕI ("WHAT")** mà an ninh mạng hướng tới đạt được.
- **Công thức vận hành ("HOW")**:
  $$\text{Security} = \text{Prevention (P)} + \text{Detection (D)} + \text{Response (R)}$$
  *(An ninh mạng = Phòng ngừa + Phát hiện + Phản ứng/Ứng phó)*

Các domain đã học trước đây (IAM, Endpoint Security, Network Security, Application Security, Data Security) chủ yếu tập trung vào trụ cột **Prevention (Phòng ngừa)**. Bài học này tập trung chuyển sang trụ cột **Detection (Phát hiện)** và nền tảng công nghệ hỗ trợ.

---

## 1. Vai trò của SOC & 4 Quy trình Phát hiện (Detection Lifecycle)

Mọi luồng dữ liệu từ các domain bảo mật (Identity, Endpoint, Network, App, Data) được tập trung về **SOC (Security Operations Center - Trung tâm điều hành an ninh mạng)** để thực thi 4 bước then chốt:

```
[Identity & Access] ──┐
[Endpoint Security] ──┤
[Network Security]  ──┼──> [ SOC: Monitoring ──> Analyze ──> Report ──> Threat Hunting ]
[App Security]      ──┤
[Data Security]     ──┘
```

1. **Monitoring (Giám sát)**: Tiếp nhận liên tục logs, events, alerts và network flow từ toàn bộ hạ tầng.
2. **Analyze (Phân tích)**: Phân loại, tương quan sự kiện, nhận diện bất thường và tính toán mức độ nghiêm trọng.
3. **Report (Báo cáo)**: Báo cáo xu hướng, đánh giá hiệu năng SOC (số lượng cảnh báo, thời gian xử lý qua các tháng).
4. **Threat Hunting (Săn lùng mối đe dọa)**: Chủ động tìm kiếm dấu vết tấn công tiềm ẩn trước khi có cảnh báo chính thức phát sinh.

---

## 2. SIEM (Security Information and Event Management)

### 2.1. Vấn đề thực tế (Silo Console & Alert Fatigue)
- Thông thường, mỗi mảng bảo mật có một bảng điều khiển (console) riêng lẻ với đội ngũ vận hành riêng biệt.
- **Hệ quả**: Chi phí vận hành rất cao, thiếu góc nhìn toàn cảnh (single pane of glass), và khi bị tấn công thì nhiều hệ thống cùng hú chuông báo động độc lập khiến nhân sự chạy theo giải quyết chồng chéo.

### 2.2. Kiến trúc & Chức năng của SIEM
SIEM hoạt động như một tầng trung tâm gom dữ liệu từ dưới lên (**Bottom-up**):
- **Thu thập tập trung (Centralized Collection)**:
  - System logs (từ OS, Database, Applications).
  - Alarms & Events (từ firewall, IDS/IPS, antivirus).
  - Network Flow Data (NetFlow, IPFIX,...).
- **Tương quan sự kiện (Correlation)**: Gộp hàng loạt cảnh báo phân tán từ các hệ thống khác nhau thành **1 Incident duy nhất**, giảm thiểu cảnh báo rác (alert fatigue).
- **Phân tích theo quy tắc (Rule-based Analysis)**: Thiết lập điều kiện kết hợp (ví dụ: truy cập từ vị trí địa lý lạ + đăng nhập sai quá nhiều lần trong 1 phút $\rightarrow$ kích hoạt cảnh báo độ ưu tiên cao).
- **Xác định độ ưu tiên (Priority Assignment)**: Phân hạng High, Medium, Low tự động hoặc dựa trên mức độ tin cậy (confidence level).
- **Phát hiện bất thường với AI/ML (Anomaly Detection & UBA)**:
  - Tìm kiếm những hành vi "kỳ lạ" mà chưa có rule định nghĩa trước.
  - **UBA / UEBA (User Behavior Analytics)**: Nhận diện sai lệch hành vi của người dùng so với thói quen lịch sử hoặc so với nhóm đồng cấp (peer group).
- **Phân tích xu hướng (Trend Analysis & Reporting)**: Đánh giá hiệu suất SOC theo thời gian.

---

## 3. XDR (Extended Detection and Response)

### 3.1. Sự phát triển từ EDR sang XDR
- **EDR (Endpoint Detection and Response)**: Cài đặt Agent trực tiếp lên máy chủ, máy trạm, laptop để phát hiện và phản ứng tự động ngay tại thiết bị nguồn.
- **XDR (Extended Detection and Response)**: Mở rộng phạm vi của EDR, bao quát từ Endpoint lên Network, Cloud, Servers và tích hợp dữ liệu từ nhiều nguồn.

### 3.2. Tính năng đột phá: Federated Search (Tìm kiếm liên kết)
- **Cơ chế**: Thay vì phải đẩy toàn bộ dữ liệu thô về một cơ sở dữ liệu khổng lồ tập trung từ trước (gây tốn kém chi phí lưu trữ/băng thông như SIEM truyền thống), XDR cho phép **để dữ liệu tại chỗ (Leave data in place)**.
- **Nguyên lý "Go Fish"**: Khi cần truy vết một IoC (Indicator of Compromise) cụ thể, XDR gửi truy vấn tới tất cả các endpoint: *"Hệ thống nào đang xuất hiện file hash / IP / tiến trình này?"* $\rightarrow$ Các endpoint tự tìm kiếm cục bộ và chỉ gửi trả kết quả khớp về trung tâm.

---

## 4. So sánh & Mối quan hệ: SIEM vs XDR

| Tiêu chí | SIEM (Security Information & Event Mgmt) | XDR (Extended Detection & Response) |
| :--- | :--- | :--- |
| **Nguồn gốc** | Xuất phát từ Log Management & Network Behavior Analysis | Phát triển từ EDR (Endpoint Detection & Response) |
| **Hướng tiếp cận** | **Bottom-up**: Thu thập toàn bộ log/flow đẩy về kho dữ liệu tập trung | **Top-down**: Đẩy năng lực kiểm tra và phản ứng xuống gần nguồn sự cố |
| **Lưu trữ dữ liệu** | Gom và lưu trữ trước tập trung (dễ tốn kém khi dung lượng log quá lớn) | **Federated Search**: Dữ liệu lưu tại chỗ, chỉ truy vấn khi cần thiết (Just-in-time) |
| **Thế mạnh chính** | Lưu vết lịch sử, phân tích tương quan rộng, Compliance & Reporting | Phát hiện sâu, hành động phản ứng tự động/nhanh tại endpoint |

> 💡 **Khuyến nghị kiến trúc**: Không phải là phép đối đầu *"SIEM vs XDR"* mà là sự cộng hưởng **"SIEM + XDR"**. Cảnh báo chất lượng cao từ SIEM có thể là ngòi nổ (trigger) để điều tra viên dùng Federated Search của XDR truy lùng chi tiết trên các endpoint.

---

## 5. Threat Hunting (Săn lùng mối đe dọa chủ động)

### 5.1. Vấn đề thời gian tổn hại (Attack Timeline & MTTI/MTTC)
Theo báo cáo *Cost of a Data Breach* (Ponemon Institute/IBM):
- **MTTI (Mean-Time-To-Identify)**: Thời gian từ khi kẻ tấn công xâm nhập hệ thống đến khi tổ chức phát hiện ra mất trung bình khoảng **~200 ngày**.
- **MTTC (Mean-Time-To-Contain)**: Thời gian từ lúc phát hiện cho tới khi cô lập/khắc phục hoàn toàn sự cố mất thêm khoảng **~70 ngày**.
- **Tổng chu kỳ**: Gần **270 ngày (~9 tháng)** kẻ tấn công tồn tại hoặc gây ảnh hưởng trong mạng.

```
Reconnaissance ──> Attack ──────────────( MTTI: ~200 days )──────────────> Identified ──( MTTC: ~70 days )──> Contained
                                                                           ▲
                     [ THREAT HUNTING: Kéo mốc phát hiện sớm về đây! ] ────┘
```

### 5.2. Reactive Investigation vs Proactive Threat Hunting

- **Điều tra phản ứng (Reactive Investigation)**:
  - Chờ hệ thống kích hoạt cảnh báo/chuông báo động rồi mới bắt đầu khám nghiệm pháp y (Forensics).
  - Thường dùng SIEM/XDR để tra cứu sự cố đã xảy ra.
- **Săn lùng chủ động (Proactive Threat Hunting)**:
  - **Không chờ cảnh báo**: Giả định rằng hệ thống đã có thể bị xâm nhập mà công cụ chưa phát hiện ra.
  - **Dựa trên giả thuyết (Hypothesis-driven)**: Chuyên gia an ninh kết hợp kinh nghiệm, trực giác, xu hướng tấn công trong ngành và Threat Intelligence để đặt câu hỏi: *"Nếu kẻ xấu tấn công qua hướng X, chúng sẽ để lại dấu vết gì?"*.
  - **Công cụ thực thi**: Dùng SIEM và XDR để truy vấn tìm kiếm các IoC (Indicators of Compromise).
  - **Mục tiêu**: Kéo mốc thời gian phát hiện (MTTI) về càng gần thời điểm bị xâm nhập càng tốt, triệt tiêu thời gian ẩn nấp (dwell time) của kẻ tấn công.
