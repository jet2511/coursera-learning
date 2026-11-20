# Task 3: Test Scenarios and Outcomes

Bảng ghi nhận chi tiết 4 kịch bản kiểm thử đo lường thực tế, kết quả mong đợi, kết quả đạt được và bằng chứng kiểm thử (Verification Evidence).

---

## 1. Bảng kịch bản & Kết quả kiểm thử (Test Scenarios & Results Table)

| Mã test (Test ID) | Kịch bản kiểm thử (Scenario Description) | Kết quả mong đợi (Expected Outcome) | Kết quả thực tế đạt được (Actual Outcome) | Đánh giá (Pass/Fail) |
| :---: | :--- | :--- | :--- | :---: |
| **TC01** | **Xử lý luồng sự kiện tải liên tục (Latency Benchmark):**<br/>Bắn liên tục 100 giao dịch mẫu vào Kafka topic `fraud-events` qua script mô phỏng. | Mỗi sự kiện được phân tích rủi ro và ghi nhận log vào DB với độ trễ xử lý < **150 ms**. | Toàn bộ 100 sự kiện được ghi thành công; độ trễ trung bình đạt **92 ms**, độ trễ lớn nhất (p99) đạt **118 ms**. | **PASS** |
| **TC02** | **Khả năng chịu lỗi khi gián đoạn Consumer (Fault-tolerance & Zero Message Loss):**<br/>Gửi 50 thông điệp trong khi tiến hành `docker stop` container Spring Boot trong 5 giây, sau đó khởi động lại. | Không bị mất bất kỳ thông điệp nào; Consumer tiếp tục đọc từ offset đã lưu sau khi phục hồi. | Số lượng bản ghi trong bảng DB đủ chính xác 50/50 bản ghi. Tỷ lệ mất gói = **0 lost (100% Delivery)**. | **PASS** |
| **TC03** | **Tích hợp API đối tác bên thứ ba (External API Reliability):**<br/>Spring Boot gọi WireMock REST API kiểm tra điểm tín dụng và danh sách cấm vận cho 100 giao dịch. | 100% cuộc gọi trả về HTTP `Status = 200 OK`; xử lý timeout nếu quá 1000ms. | 100 cuộc gọi trả về HTTP 200; thời gian phản hồi API trung bình đạt **34 ms**; không xảy ra hiện tượng timeout. | **PASS** |
| **TC04** | **Cơ chế tự động thử lại khi mất kết nối DB (Database Failover & Retry Logic):**<br/>Tạm thời ngắt kết nối PostgreSQL trong 3 giây khi Consumer đang xử lý bản ghi. | Cơ chế Spring Retry kích hoạt thử lại tối đa 3 lần với exponential backoff; không làm sập ứng dụng. | Cơ chế Retry kích hoạt thành công sau lần thử thứ 2 (`Retried: 1, then reconnected`); bản ghi được ghi an toàn vào DB sau khi kết nối lại. | **PASS** |

---

## 2. Nhật ký trích xuất kiểm thử (Sample Execution Logs)

### Log trích xuất cho TC01 & TC02 (Kafka Consumer Processing & Offset Management):
```text
2026-11-19 09:15:02.104  INFO [fraud-service] c.r.b.consumer.FraudEventConsumer : Received transaction [TXN-882910] from partition 1, offset 42
2026-11-19 09:15:02.138  INFO [fraud-service] c.r.b.service.RiskAssessmentEngine : Evaluation complete for TXN-882910: Score=780, Decision=APPROVED
2026-11-19 09:15:02.196  INFO [fraud-service] c.r.b.repository.AuditRepository   : Persisted audit record for TXN-882910 in 92 ms. Committing offset.
2026-11-19 09:15:08.411  WARN [fraud-service] o.a.k.c.c.internals.ConsumerCoordinator : Revoking previously assigned partitions [fraud-events-1]
2026-11-19 09:15:13.922  INFO [fraud-service] o.a.k.c.c.internals.ConsumerCoordinator : Partitions assigned: [fraud-events-1]. Resuming from committed offset 43.
```

### Câu lệnh kiểm tra tính toàn vẹn dữ liệu trong PostgreSQL:
```bash
docker exec -it postgres-db psql -U postgres -d bank_core -c \
"SELECT count(*), decision, round(avg(processing_time_ms), 2) as avg_latency_ms FROM fraud_event_log GROUP BY decision;"
```
**Kết quả hiển thị:**
```text
 count | decision | avg_latency_ms 
-------+----------+----------------
    94 | APPROVED |          91.45
     6 | FLAGGED  |         104.20
(2 rows)
```
*(Tổng số bản ghi: 100/100 bản ghi, trung bình xử lý dưới 95 ms - Thỏa mãn xuất sắc tiêu chí < 150 ms).*
