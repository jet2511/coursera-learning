# Assessing System Performance

> **Nguồn:** IBM System Design – Module 2: IT Systems Analysis and Review  
> **Ngày lưu:** 2026-08-14

---

## 🎯 Mục tiêu học tập

- Định nghĩa các thành phần và metrics đánh giá hiệu năng hệ thống (response time, throughput, resource utilization).
- Giải thích các phương pháp đánh giá hệ thống IT (workload analysis, benchmarking, system observation).
- Mô tả cách sử dụng dữ liệu hiệu năng để xác định kém hiệu quả và đề xuất cải tiến.
- Nhận diện các thách thức và best practices trong phân tích hiệu năng.

---

## 1. Các Thành Phần Cốt Lõi của Phân Tích Hiệu Năng

| Thành phần | Mô tả | Ví dụ |
|---|---|---|
| **Response Time** | Thời gian hệ thống xử lý request | Thời gian load trang, truy vấn DB |
| **Throughput** | Khối lượng giao dịch xử lý trong một khoảng thời gian | Số đơn hàng/phút |
| **Resource Utilization** | Mức độ sử dụng CPU, RAM, storage, network | Phát hiện overload hoặc lãng phí tài nguyên |
| **Reliability & Availability** | Uptime và tỷ lệ lỗi | Downtime trong hệ thống ngân hàng làm mất niềm tin |
| **Scalability** | Khả năng xử lý tải tăng mà không bị degradation | Xử lý thêm users hoặc data |

---

## 2. Phương Pháp Đánh Giá Hiệu Năng

### 2.1 Requirement Analysis
- Review yêu cầu business và user để thiết lập performance benchmarks.
- _Ví dụ:_ E-commerce yêu cầu response time < 1 giây cho tìm kiếm.

### 2.2 System Observation
- Monitor real-time hành vi hệ thống.
- **Tools:** New Relic, Nagios, Prometheus.
- Tracking: response time, CPU usage, error rates.

### 2.3 Workload Analysis
- Đánh giá hiệu năng dưới tải thông thường và tải đỉnh (stress/load testing).
- **Tools:** JMeter, LoadRunner.

### 2.4 Process Mapping
- Dùng DFD hoặc Activity Diagram để map workflow, phát hiện quy trình dư thừa.

### 2.5 Bottleneck Identification
- Phân tích resource usage và transaction logs tìm điểm nghẽn cổ chai.
- _Ví dụ:_ Slow database queries, network latency.

### 2.6 Stakeholder Feedback
- Thu thập ý kiến từ users và IT staff về các pain points (chậm report, crash thường xuyên).

### 2.7 Benchmarking
- So sánh hiệu năng với tiêu chuẩn ngành hoặc hệ thống tương đương.

---

## 3. Lợi Ích của Phân Tích Hiệu Năng

| Lợi ích | Chi tiết |
|---|---|
| **Improved Efficiency** | Giải quyết bottleneck, tối ưu query DB, tăng tốc độ và throughput |
| **Enhanced UX** | Response time nhanh hơn → hài lòng người dùng (online banking) |
| **Cost Optimization** | Giảm chi phí hạ tầng, tránh overprovisioning server |
| **Scalability Planning** | Chủ động nâng cấp trước khi hệ thống quá tải |
| **Risk Mitigation** | Phát hiện sớm vấn đề tin cậy, tránh downtime tốn kém (healthcare IT) |
| **Informed Decision-Making** | Dữ liệu hỗ trợ hiện đại hóa: thay legacy system, chuyển cloud |

---

## 4. Ứng Dụng Thực Tế

- **Online Retail:** Đánh giá checkout response time, throughput cập nhật kho hàng, server utilization trong peak sale.
- **Healthcare:** Đảm bảo hệ thống quản lý bệnh nhân xử lý đáng tin cậy khi lượng visit cao.
- Hỗ trợ legacy system modernization và new system design.
- Bổ sung cho UML Diagrams, Sequence Diagrams, ER Diagrams.

---

## 5. Thách Thức

- Sự phụ thuộc phức tạp giữa các hệ thống con (complex interdependencies).
- Hạn chế truy cập dữ liệu real-time.
- Sự kháng cự thay đổi từ phía stakeholders.

---

## 6. Best Practices

| Practice | Chi tiết |
|---|---|
| **Automate Monitoring** | Dùng Grafana, Splunk để phát hiện sớm sự cố |
| **Prioritize Key Metrics** | Tập trung response time, error rates phù hợp mục tiêu business |
| **Engage Stakeholders** | Bao gồm users và IT team trong quá trình phân tích |
| **Regular Iterations** | Thích nghi với yêu cầu và công nghệ thay đổi |
| **Document Findings** | Báo cáo chi tiết để hướng dẫn cải tiến tương lai và tuân thủ compliance |

---

## 📝 Tóm Tắt Nhanh

- **Đo lường hiệu năng** qua: Response Time, Throughput, Resource Utilization, Reliability, Scalability.
- **Phương pháp:** Benchmarking, Workload Testing, System Observation, Process Mapping.
- **Hành động:** Dùng dữ liệu để giải quyết bottleneck, tối ưu tài nguyên, lên kế hoạch nâng cấp hạ tầng.
- **Quản lý thách thức** bằng monitoring tự động, ưu tiên metrics đúng, ghi chép đầy đủ.
