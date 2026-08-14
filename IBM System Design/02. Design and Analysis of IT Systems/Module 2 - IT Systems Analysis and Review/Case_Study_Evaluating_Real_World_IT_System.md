# Case Study: Evaluating a Real-World IT System (Hospital Patient Management System)

> **Nguồn:** IBM System Design – Module 2: IT Systems Analysis and Review  
> **Ngày lưu:** 2026-08-14

---

## 🎯 Mục tiêu học tập

- Xác định các thách thức về hiệu năng (performance) và trải nghiệm sử dụng (usability) qua phương pháp Case Study.
- Diễn giải và xây dựng các sơ đồ luồng dữ liệu cơ bản (DFD) và sơ đồ thực thể mối quan hệ (ERD).
- Áp dụng các metrics đánh giá hiệu năng (throughput, error rates, scalability).

---

## 1. Bối Cảnh Case Study (Hospital Patient Management System)

Một bệnh viện quy mô vừa vận hành hệ thống quản lý bệnh nhân (đăng ký, đặt lịch khám, bệnh án điện tử, thanh toán viện phí).

- **Kiến trúc:** Frontend cho nhân viên + CSDL dữ liệu bệnh nhân + Tích hợp bên ngoài với bảo hiểm.
- **Triệu chứng gặp phải:** Đặt lịch chậm, lỗi tính tiền viện phí, khó khăn khi truy xuất hồ sơ bệnh án cũ.
- **Mục tiêu:** Nâng cao hiệu quả, giảm lỗi và tăng mức độ hài lòng của bệnh nhân.

---

## 2. Phương Pháp Đánh Giá Hệ Thống (Evaluation Methodologies)

| Phương pháp | Mô tả chi tiết | Mục đích / Công cụ |
|---|---|---|
| **Stakeholder Interviews** | Phỏng vấn lễ tân, bác sĩ, kế toán và bệnh nhân | Thu thập pain points thực tế (chậm giờ cao điểm, khó đặt lịch online) |
| **Documentation Review** | Rà soát sổ tay, DB schema, API specs | Tìm ra các khoảng trống do tài liệu thiếu/lỗi thời |
| **Process Mapping** | Vẽ luồng Patient → Registration → Database qua DFD | Phát hiện thao tác nhập liệu dư thừa |
| **Data Structure Analysis** | Dùng ERD phân tích Patient, Appointment, Invoice | Phát hiện thiếu foreign key, sai mối quan hệ |
| **Performance Metrics** | Đo response time, throughput, error rates | Giám sát real-time bằng New Relic, Prometheus |
| **Workload Testing** | Stress test mô phỏng tải đỉnh đồng thời nhiều request | Dùng Apache JMeter đánh giá scalability |
| **Gap Analysis** | Đối chiếu hiện trạng với SLA/Requirement (< 1s query, 99.9% uptime) | Chỉ ra khoảng cách cần cải thiện |

---

## 3. Kết Quả Phân Tích (Key Findings)

```
[1. Bottlenecks]           → Chậm query DB do thiếu/chưa tối ưu index, làm trễ quá trình book lịch.
[2. Data Inconsistencies]  → Thiếu ràng buộc quan hệ/khóa ngoại trong ERD dẫn đến hóa đơn gán sai bệnh nhân.
[3. Usability Issues]      → Giao diện lỗi thời, tốn quá nhiều bước thao tác cho việc cập nhật thông tin đơn giản.
[4. Scalability Limits]    → Response time tăng gấp đôi trong giờ cao điểm khi lượng truy cập tăng.
[5. Lack of Integration]   → Thiếu API tích hợp tự động với bên bảo hiểm → phải nhập tay → tăng tỷ lệ sai sót.
```

---

## 4. Đề Xuất Cải Tiến (Recommendations & BPR Alignment)

| Hạng mục | Giải pháp đề xuất |
|---|---|
| **Tối ưu Database** | Tái cấu trúc DB Schema với ERD chuẩn, bổ sung indexing và quan hệ khóa ngoại. |
| **Hợp lý hóa quy trình (Streamline)** | Thiết kế lại workflow bằng DFD, tự động hóa khâu xác thực bảo hiểm (insurance verification). |
| **Nâng cấp UI/UX** | Triển khai giao diện hiện đại, tinh gọn quy trình đặt lịch. |
| **Mở rộng năng lực (Scalability)** | Nâng cấp hạ tầng server hoặc chuyển đổi sang Cloud, nghiệm thu qua stress test. |
| **Tăng cường tích hợp** | Xây dựng RESTful API kết nối trực tiếp các đơn vị bảo hiểm. |

---

## 5. Giá Trị Của Phương Pháp Case Study

- **Practical Insights:** Mang lại ngữ cảnh thực tế, giúp đề xuất mang tính khả thi cao.
- **Holistic Analysis:** Kết hợp hài hòa giữa DFD (quy trình), ERD (dữ liệu) và Performance Metrics (kỹ thuật).
- **Stakeholder Alignment:** Gắn kết người dùng cuối và đội ngũ IT kỹ thuật.
- **Risk Reduction & Growth:** Xử lý sớm các lỗi nghiêm trọng (hóa đơn, hồ sơ bệnh nhân) và chuẩn bị cho mở rộng dài hạn.

---

## 6. Thách Thức & Best Practices

```
[Challenges]
├── Tài liệu cũ không đầy đủ (Incomplete documentation)
├── Sự phụ thuộc phức tạp giữa các phân hệ (Complex dependencies)
└── Tâm lý ngại thay đổi từ người dùng (Resistance to change)

[Best Practices]
├── Engage Stakeholders Early  (Phỏng vấn đa chiều từ sớm)
├── Standardized Tools         (Chuẩn hóa sơ đồ qua UML, DFD, ERD)
├── Automated Monitoring       (Giám sát tải và lỗi qua Splunk, Prometheus)
└── Iterate and Validate       (Chạy pilot thử nghiệm trước khi áp dụng toàn diện)
```

---

## 📝 Tóm Tắt Nhanh

- **Đánh giá hệ thống thực tế** cần kết hợp cả định tính (interviews) và định lượng (metrics, stress test).
- **DFD & ERD** là 2 công cụ bắt buộc để bóc tách luồng xử lý và toàn vẹn dữ liệu.
- **Mọi tối ưu hóa kỹ thuật** (DB indexing, Cloud migration, API integration) đều phải bám sát **mục tiêu nghiệp vụ** (giảm lỗi viện phí, tăng sự hài lòng của bệnh nhân, đảm bảo uptime).
