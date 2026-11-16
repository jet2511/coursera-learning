# Summary and Highlights: Detection and Response

- **Detection (Phát hiện)**: Thu thập thông tin từ tất cả các domain đưa vào monitoring engine, do đội ngũ **SOC (Security Operations Center)** quản lý.
- **Công nghệ Detection**:
  - **SIEM**: Tiếp cận **bottom-up** để thu thập, phân tích và báo cáo mối đe dọa; rất mạnh trong việc tạo cảnh báo (alarms).
  - **XDR**: Tiếp cận **top-down** (mở rộng từ EDR với agent cài trên từng hệ thống).
  - **SIEM + XDR**: Kết hợp tạo thành hệ thống phát hiện vững chắc.
- **Dòng thời gian tấn công**:
  - **Reconnaissance**: Thời gian kẻ tấn công chuẩn bị, thăm dò.
  - **MTTI (Mean Time to Identify)**: Thời gian trung bình để phát hiện cuộc tấn công.
  - **MTTC (Mean Time to Contain)**: Thời gian trung bình để khắc phục và phục hồi.
- **Threat Hunting**: Phương pháp chủ động tìm kiếm tấn công, giúp tăng tỷ lệ phát hiện và rút ngắn thời gian điều tra.
- **Incident Response (IR) & SOAR**:
  - IR truyền thống làm thủ công (triage & remediate), khó mở rộng.
  - **SOAR** tự động hóa quy trình IR để giảm MTTC.
- **Quy trình điều tra & khắc phục trong SOAR**:
  1. Tạo Case trong Case Management của SOAR (kèm artifacts nếu có).
  2. Gán Case cho cybersecurity analyst.
  3. Theo dõi và điều phối lại khi cần.
  4. Điều tra và sử dụng **dynamic playbook** để chạy các quy trình phù hợp.
  5. Đưa ra các bước khắc phục (remediation).
  6. Thông báo cho cơ quan quản lý nếu xảy ra vi phạm dữ liệu (breach).
