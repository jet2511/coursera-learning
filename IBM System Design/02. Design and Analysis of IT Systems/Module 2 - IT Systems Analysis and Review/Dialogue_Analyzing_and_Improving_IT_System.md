# Dialogue: Analyzing and Improving an Existing IT System

> **Nguồn:** IBM System Design – Module 2: IT Systems Analysis and Review  
> **Chủ đề:** Tình huống thực tế – Hệ thống Y tế Trực tuyến (Online Healthcare Services Company)  
> **Ngày lưu:** 2026-08-14

---

## 🎯 Bối Cảnh Tình Huống (Scenario)

Công ty dịch vụ y tế trực tuyến đang gặp 5 vấn đề nghiêm trọng với hệ thống quản lý đặt lịch và bệnh án:
1. **Chậm trễ khi đặt lịch khám** trong khung giờ cao điểm (Peak hours).
2. **Truy xuất hồ sơ bệnh nhân bị trễ** (Slow patient record retrieval).
3. **Gia tăng lỗi tính tiền/hóa đơn viện phí** (Billing errors).
4. **Khó khăn khi tích hợp API với bên bảo hiểm thứ ba** (Third-party insurance integration).
5. **Lo ngại về năng lực mở rộng (Scalability)** khi lượng bệnh nhân tăng nhanh.

---

## 🧭 Quy Trình Phân Tích & Giải Pháp 5 Bước Của Systems Analyst

```
[1. Current State]    → Xác định Stakeholders, System Components, Workflows
[2. Metrics]          → Đo lường Response Time, Throughput, Error Rate, Resource, Scalability
[3. Documentation]    → Dùng ERD, DFD, API Specs, Gap Analysis để trực quan hóa
[4. Bottlenecks]      → Định vị điểm nghẽn tại DB, API bảo hiểm, Quy trình thủ công, Hạ tầng
[5. BPR & Solutions]  → Tái thiết kế triệt để: Automation, Simplification, DB Tuning, Cloud Scale
```

---

## 1. Xác Định Hiện Trạng (Current State Identification)

- **Stakeholders:** Bệnh nhân, bác sĩ, lễ tân, kế toán thu ngân, đội ngũ IT, nhà cung cấp bảo hiểm bên thứ ba.
- **System Components:** Cổng giao diện bệnh nhân (Web/Mobile portal), CSDL bệnh án điện tử (EHR/EMR database), Phân hệ đặt lịch khám, Phân hệ thanh toán viện phí, Cổng kết nối API bảo hiểm.
- **Key Workflows:** Đặt lịch khám trực tuyến, Truy xuất hồ sơ bệnh án, Lập hóa đơn viện phí, Xác thực & giải quyết bảo hiểm.

---

## 2. Các Chỉ Số Hiệu Năng Cốt Lõi (Key Performance Metrics)

| Metric | Mô tả chi tiết | Vấn đề giải quyết |
|---|---|---|
| **Response Time & Latency** | Đo thời gian giao dịch đặt lịch và độ trễ truy vấn CSDL hồ sơ bệnh nhân. | Đặt lịch chậm, tải hồ sơ lâu |
| **Throughput** | Số lượng lịch hẹn và giao dịch thanh toán xử lý được trên mỗi phút (TPM/TPS). | Đánh giá tải bình thường vs. tải đỉnh |
| **Error Rate** | Tỷ lệ % hóa đơn sai sót và tỷ lệ timeout khi kết nối API bảo hiểm. | Lỗi viện phí & nghẽn tích hợp bảo hiểm |
| **Resource Utilization** | Mức tiêu thụ CPU, RAM, Disk I/O, Network của server ứng dụng và database. | Nhận diện quá tải phần cứng |
| **Scalability & Uptime** | Mức độ suy giảm hiệu năng khi tải tăng cao và thời gian hoạt động ổn định. | Đảm bảo tính sẵn sàng khi mở rộng |

---

## 3. Vai Trò Của Tài Liệu Hóa (System Documentation)

- **ERDs & DB Schema:** Bóc tách cấu trúc dữ liệu, phát hiện thiếu khóa ngoại/thiếu index gây sai hóa đơn và chậm truy vấn.
- **Process Flow & DFDs:** Trực quan hóa toàn bộ luồng dữ liệu, xác định các khâu trung gian thừa thãi.
- **API Specs & Architecture Maps:** Làm rõ phụ thuộc và giao thức kết nối với bên bảo hiểm để khắc phục lỗi timeout.
- **Baseline for Gap Analysis:** Làm thước đo chuẩn so sánh giữa hiện trạng (*As-Is*) và yêu cầu mục tiêu (*To-Be*).
- **Stakeholder Alignment:** Xóa bỏ sự phụ thuộc vào kiến thức truyền miệng (*tribal knowledge*), tạo tiếng nói chung giữa IT và y bác sĩ.

---

## 4. Định Vị Điểm Nghẽn (Bottlenecks & Inefficiencies)

```
├── Database Layer:        Bảng chưa đánh index, thiếu bộ nhớ đệm (cache), query nặng giờ cao điểm.
├── External API Layer:    Gọi API bảo hiểm đồng bộ (synchronous) gây nghẽn luồng xử lý chính.
├── Data Validation Layer: Thiếu ràng buộc quan hệ dẫn đến hóa đơn gán sai thông tin bệnh nhân.
├── Workflow Layer:        Nhiều bước kiểm tra/xác thực bảo hiểm thủ công gây chậm tiến độ.
└── Infrastructure Layer:  Kiến trúc đơn khối (monolithic) thiếu cân bằng tải và tự động co giãn (auto-scaling).
```

---

## 5. Tái Cấu Trúc BPR & Đề Xuất Cải Tiến (Recommendations)

### 📌 3 Quy trình ưu tiên BPR:
1. **Xác thực bảo hiểm & Thanh toán:** Chuyển từ thủ công sang tự động hóa 100% qua API thời gian thực.
2. **Đặt lịch khám (Self-service Booking):** Rút gọn còn 2-3 bước trên Web/App với cơ chế khóa lịch tự động (slot locking).
3. **Truy xuất bệnh án:** Tập trung hóa dữ liệu EHR, tăng tốc truy vấn bằng Cache.

### 🛠️ 4 Nhóm giải pháp kỹ thuật cụ thể:

| Trụ cột | Giải pháp kỹ thuật | Lợi ích đạt được |
|---|---|---|
| **Automation** | Tích hợp API bảo hiểm real-time, gửi SMS/Email nhắc lịch tự động. | Không cần nhân viên nhập tay, giảm tỷ lệ vắng khám (no-shows). |
| **Workflow Simplification** | Cổng Self-Service 3 bước cho bệnh nhân tự đặt lịch và check-in trực tuyến. | Giảm áp lực cho quầy lễ tân, tăng trải nghiệm bệnh nhân. |
| **Database Optimization** | Thêm khóa ngoại/ràng buộc toàn vẹn dữ liệu, đánh Index trường tìm kiếm, thêm Redis Cache. | Triệt tiêu lỗi hóa đơn, truy xuất hồ sơ dưới 1 giây (<1s). |
| **Infrastructure Scalability** | Chuyển dịch lên Cloud (Load Balancer + Auto-Scaling), áp dụng Message Queue (Asynchronous) cho thanh toán/thông báo. | Xử lý mượt mà giờ cao điểm, sẵn sàng mở rộng quy mô. |

---

## 💡 Đánh Giá & Bài Học Rút Ra (Key Takeaways)

- Phân tích hệ thống IT là sự kết hợp chặt chẽ giữa **Hiểu hiện trạng $\rightarrow$ Đo lường metrics $\rightarrow$ Trực quan hóa $\rightarrow$ Bóc tách điểm nghẽn $\rightarrow$ Đề xuất giải pháp BPR**.
- **Kỹ năng cốt lõi của Tech Lead / Systems Analyst:** Luôn gắn liền giải pháp kỹ thuật (Redis, Cloud Auto-scaling, API Integration) với **mục tiêu nghiệp vụ** (giảm lỗi viện phí, tăng mức độ hài lòng của bệnh nhân, tối ưu chi phí vận hành).
