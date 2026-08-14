# System Documentation and Mapping

> **Nguồn:** IBM System Design – Module 2: IT Systems Analysis and Review  
> **Ngày lưu:** 2026-08-14

---

## 🎯 Mục tiêu học tập

- Giải thích mục đích của System Documentation (Tài liệu hóa hệ thống) và Mapping (Sơ đồ hóa hệ thống).
- Thảo luận các phương pháp/quy trình thực hiện documentation và mapping.
- Phân tích các lợi ích của tài liệu hóa và sơ đồ hóa hệ thống.
- Nhận diện các thách thức và áp dụng best practices khi triển khai.

---

## 1. Khái Niệm Cơ Bản

| Khái niệm | Định nghĩa | Công cụ / Ví dụ |
|---|---|---|
| **System Documentation** | Bản ghi chi tiết về cấu trúc, thành phần và vận hành của hệ thống IT (phần cứng, phần mềm, database, UI). | Confluence, Swagger/OpenAPI, Javadoc, tài liệu kỹ thuật. |
| **System Mapping** | Sử dụng các công cụ trực quan để minh họa luồng dữ liệu, tiến trình và kiến trúc hệ thống. | DFD, ERD, UML, BPMN, Lucidchart, draw.io. |

> **Mối liên hệ:** Documentation cung cấp chi tiết kỹ thuật (schema database, API spec), còn Mapping trực quan hóa luồng hoạt động (Data Flow Diagram cho order processing), giúp xóa bỏ sự mơ hồ và hỗ trợ ra quyết định hiện đại hóa.

---

## 2. Quy Trình Thực Hiện (Methodologies)

```
1. Gather Existing Docs   → Thu thập manual, tech spec, code comments; phỏng vấn IT staff (legacy).
2. Engage Stakeholders    → Phỏng vấn users, dev, manager để hiểu tính năng & pain points.
3. Observe Operations     → Dùng Splunk, Nagios theo dõi hiệu năng, user interaction & logs thực tế.
4. Map Processes & Data   → Vẽ DFD/BPMN (workflow), ERD (database), UML (kiến trúc, API, modules).
5. Standardize Docs       → Dùng template chuẩn trên Confluence, Visio để lưu trữ tập trung.
6. Validate & Update      → Review cùng stakeholders để đảm bảo tính chính xác và duy trì cập nhật.
```

---

## 3. Lợi Ích Chính

| Lợi ích | Chi tiết |
|---|---|
| **Clarity & Transparency** | Tạo hiểu biết chung, giảm hiểu lầm giữa các bên liên quan |
| **Improved Maintenance** | Dễ dàng debug, tìm bottleneck và nâng cấp hệ thống |
| **Onboarding Efficiency** | Rút ngắn thời gian training nhân sự mới, tránh phụ thuộc tribal knowledge |
| **Optimization** | Phát hiện quy trình thừa, nhập dữ liệu trùng lặp hoặc API calls chậm |
| **Compliance** | Cung cấp bằng chứng tuân thủ chuẩn quy định (tài chính, y tế) |
| **Strategic Modernization** | Cơ sở dữ liệu chính xác cho việc migrate cloud hoặc thay thế legacy |

---

## 4. Thách Thức

- Tài liệu hiện tại bị thiếu hoặc lỗi thời (incomplete documentation).
- Sự phụ thuộc chéo phức tạp giữa các hệ thống (complex interdependencies).
- Tâm lý ngại/ngại kháng cự tài liệu hóa hệ thống cũ (resistance to documenting legacy systems).

---

## 5. Best Practices

| Best Practice | Hành động cụ thể |
|---|---|
| **Start Small** | Bắt đầu từ các component/quy trình trọng yếu trước để tạo đà |
| **Use Visual Tools** | Sử dụng Lucidchart, draw.io để chuẩn hóa sơ đồ |
| **Engage Stakeholders** | Thu hút sự tham gia sớm của IT và end-user |
| **Automate Documentation** | Tự động sinh tài liệu code/API qua Swagger, Javadoc |
| **Maintain Regularly** | Cập nhật tài liệu định kỳ theo từng chu kỳ thay đổi của hệ thống |

---

## 📝 Tóm Tắt Nhanh

- **Documentation & Mapping** là bước nền tảng phân tích hệ thống hiện hữu trước khi thiết kế/nâng cấp.
- **Phương pháp:** Thu thập tài liệu cũ → Tham vấn bên liên quan → Quan sát vận hành → Vẽ sơ đồ (DFD, ERD, UML, BPMN) → Chuẩn hóa → Review & Update.
- **Lợi ích:** Minh bạch hóa, bảo trì nhanh, onboarding dễ dàng, tối ưu hóa và hỗ trợ compliance/cloud migration.
- **Best practices:** Làm từng phần nhỏ, trực quan hóa, tự động hóa bằng tool và bảo trì tài liệu thường xuyên.
