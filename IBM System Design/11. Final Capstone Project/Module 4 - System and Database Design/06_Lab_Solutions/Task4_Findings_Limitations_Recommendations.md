# Task 4: Findings, Limitations, and Recommendations

Bản phân tích chuyên sâu các kết quả thu được từ quá trình chạy thử nghiệm Prototype, các ranh giới hạn chế hiện tại và phương án đề xuất mở rộng lên môi trường Production.

---

## 1. Bảng phân loại kết quả (Categorized Findings Table)

| Nhóm danh mục (Category) | Kết quả ghi nhận (Key Findings) | Tác động hệ thống (System Impact) | Khuyến nghị hành động (Actionable Recommendations) |
| :--- | :--- | :--- | :--- |
| **Performance (Hiệu năng)** | - Độ trễ xử lý sự kiện trung bình đạt 92 ms (p99 < 120 ms).<br/>- Throughput trên 1 node đạt 450 events/giây mà không bị nghẽn CPU/RAM. | **Tích cực:** Vượt trội so với ngưỡng mục tiêu (< 150 ms), đảm bảo khách hàng không nhận thấy độ trễ khi quẹt thẻ hoặc chuyển tiền. | Mở rộng số lượng partition trên Kafka (tăng từ 3 lên 12 partitions) kết hợp scale ngang nhiều instance consumer để nâng throughput lên > 5.000 TPS khi lên Production. |
| **Integration (Tích hợp)** | - Spring Kafka tích hợp mượt mà với Consumer Group.<br/>- Mock REST API phản hồi ổn định trong 34 ms. | **Tích cực:** Cơ chế manual offset commit ngăn chặn tình trạng duplicate message hiệu quả. | Cần bổ sung thêm thư viện Resilience4j (Circuit Breaker & Retry) để ngắt mạch an toàn khi API đối tác bên thứ ba bị sập kéo dài. |
| **Security (Bảo mật)** | - Môi trường Sandbox hiện chỉ dùng xác thực cơ bản (Plaintext Kafka, DB mật khẩu cứng trong docker-compose). | **Rủi ro:** Không đạt chuẩn PCI-DSS và SOC 2 nếu đưa trực tiếp lên môi trường sản xuất. | Bắt buộc triển khai mã hóa kênh truyền TLS/mTLS (Kafka SASL/SCRAM hoặc mTLS), tích hợp HashiCorp Vault / AWS Secrets Manager để nạp mật khẩu động. |
| **Deployment (Triển khai)** | - Khởi động bằng Docker Compose đơn giản, thời gian container boot đạt 3.8 giây. | **Tích cực:** Môi trường kiểm thử dễ tái lập (reproducible). | Chuyển đổi manifest sang Helm Charts để triển khai trên cụm Kubernetes (EKS / OpenShift) nhằm tận dụng cơ chế Auto-scaling (HPA) và Rolling Update. |

---

## 2. Các giới hạn của bản thử nghiệm (Prototype Limitations)

1. **Giới hạn về dữ liệu (Data Limitation):** Sử dụng bộ dữ liệu giả lập chuẩn hóa (clean synthetic data), chưa phản ánh hết các trường hợp dữ liệu xấu, cấu trúc JSON bị lỗi hoặc kích thước payload bất thường.
2. **Giới hạn về tải (Scale Limitation):** Kiểm thử trên quy mô 100 - 500 events/giây trên 1 máy đơn; chưa đo lường tác động của nghẽn mạng WAN giữa các Data Center phân tán.
3. **Môi trường đơn cụm (Single-Cluster Setup):** Cụm Kafka và PostgreSQL chỉ chạy 1 node độc lập, chưa kiểm chứng được kịch bản failover tự động giữa các Availability Zones (Multi-AZ).
4. **Bảo mật sản xuất chưa kích hoạt:** Chưa bật tường lửa WAF, cơ chế mã hóa ổ đĩa tại chỗ (Encryption at Rest) và hệ thống SIEM/SOC giám sát an ninh.

---

## 3. Các điểm cải tiến trọng tâm cho giai đoạn tiếp theo (Action Items)

- [ ] **Kích hoạt Dead Letter Queue (DLQ):** Khi gặp thông điệp dị tật (malformed message), hệ thống phải tự động đẩy vào topic `fraud-events-dlq` để đội ngũ vận hành phân tích thay vì làm tắc nghẽn hàng đợi chính.
- [ ] **Tích hợp Kafka Schema Registry (Avro / Protobuf):** Đảm bảo tính tương thích ngược của cấu trúc dữ liệu giao dịch khi hệ thống nâng cấp phiên bản.
- [ ] **Xây dựng Dashboard quan sát (Observability):** Tích hợp Prometheus và Grafana để hiển thị biểu đồ Kafka lag, JVM memory và latency thời gian thực.
